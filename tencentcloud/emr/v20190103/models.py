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


class AddUsersForUserManagerRequest(AbstractModel):
    """AddUsersForUserManager request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Cluster string ID
        :type InstanceId: str
        :param UserManagerUserList: User information list
        :type UserManagerUserList: list of UserInfoForUserManager
        """
        self.InstanceId = None
        self.UserManagerUserList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("UserManagerUserList") is not None:
            self.UserManagerUserList = []
            for item in params.get("UserManagerUserList"):
                obj = UserInfoForUserManager()
                obj._deserialize(item)
                self.UserManagerUserList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUsersForUserManagerResponse(AbstractModel):
    """AddUsersForUserManager response structure.

    """

    def __init__(self):
        r"""
        :param SuccessUserList: The user list that is successfully added
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SuccessUserList: list of str
        :param FailedUserList: The user list that is not successfully added
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FailedUserList: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SuccessUserList = None
        self.FailedUserList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessUserList = params.get("SuccessUserList")
        self.FailedUserList = params.get("FailedUserList")
        self.RequestId = params.get("RequestId")


class COSSettings(AbstractModel):
    """COS-related configuration

    """

    def __init__(self):
        r"""
        :param CosSecretId: COS `SecretId`
        :type CosSecretId: str
        :param CosSecretKey: COS `SecrectKey`
        :type CosSecretKey: str
        :param LogOnCosPath: COS path to log
        :type LogOnCosPath: str
        """
        self.CosSecretId = None
        self.CosSecretKey = None
        self.LogOnCosPath = None


    def _deserialize(self, params):
        self.CosSecretId = params.get("CosSecretId")
        self.CosSecretKey = params.get("CosSecretKey")
        self.LogOnCosPath = params.get("LogOnCosPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdbInfo(AbstractModel):
    """Output parameters

    """

    def __init__(self):
        r"""
        :param InstanceName: Database instance
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param Ip: Database IP
Note: this field may return null, indicating that no valid values can be obtained.
        :type Ip: str
        :param Port: Database port
Note: this field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param MemSize: Database memory specification
Note: this field may return null, indicating that no valid values can be obtained.
        :type MemSize: int
        :param Volume: Database disk specification
Note: this field may return null, indicating that no valid values can be obtained.
        :type Volume: int
        :param Service: Service flag
Note: this field may return null, indicating that no valid values can be obtained.
        :type Service: str
        :param ExpireTime: Expiration time
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param ApplyTime: Application time
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplyTime: str
        :param PayType: Payment type
Note: this field may return null, indicating that no valid values can be obtained.
        :type PayType: int
        :param ExpireFlag: Expiration flag
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExpireFlag: bool
        :param Status: Database status
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param IsAutoRenew: Renewal flag
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsAutoRenew: int
        :param SerialNo: Database string
Note: this field may return null, indicating that no valid values can be obtained.
        :type SerialNo: str
        :param ZoneId: ZoneId
Note: this field may return null, indicating that no valid values can be obtained.
        :type ZoneId: int
        :param RegionId: RegionId
Note: this field may return null, indicating that no valid values can be obtained.
        :type RegionId: int
        """
        self.InstanceName = None
        self.Ip = None
        self.Port = None
        self.MemSize = None
        self.Volume = None
        self.Service = None
        self.ExpireTime = None
        self.ApplyTime = None
        self.PayType = None
        self.ExpireFlag = None
        self.Status = None
        self.IsAutoRenew = None
        self.SerialNo = None
        self.ZoneId = None
        self.RegionId = None


    def _deserialize(self, params):
        self.InstanceName = params.get("InstanceName")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.MemSize = params.get("MemSize")
        self.Volume = params.get("Volume")
        self.Service = params.get("Service")
        self.ExpireTime = params.get("ExpireTime")
        self.ApplyTime = params.get("ApplyTime")
        self.PayType = params.get("PayType")
        self.ExpireFlag = params.get("ExpireFlag")
        self.Status = params.get("Status")
        self.IsAutoRenew = params.get("IsAutoRenew")
        self.SerialNo = params.get("SerialNo")
        self.ZoneId = params.get("ZoneId")
        self.RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterExternalServiceInfo(AbstractModel):
    """Relationship between shared components and the current cluster

    """

    def __init__(self):
        r"""
        :param DependType: Dependency. `0`: Other clusters depend on the current cluster. `1`: The current cluster depends on other clusters.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DependType: int
        :param Service: Shared component
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Service: str
        :param ClusterId: Sharing cluster
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClusterId: str
        :param ClusterStatus: Sharing cluster status
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClusterStatus: int
        """
        self.DependType = None
        self.Service = None
        self.ClusterId = None
        self.ClusterStatus = None


    def _deserialize(self, params):
        self.DependType = params.get("DependType")
        self.Service = params.get("Service")
        self.ClusterId = params.get("ClusterId")
        self.ClusterStatus = params.get("ClusterStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterInstancesInfo(AbstractModel):
    """Cluster instance information

    """

    def __init__(self):
        r"""
        :param Id: ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type Id: int
        :param ClusterId: Cluster ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClusterId: str
        :param Ftitle: Title
Note: this field may return null, indicating that no valid values can be obtained.
        :type Ftitle: str
        :param ClusterName: Cluster name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClusterName: str
        :param RegionId: Region ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type RegionId: int
        :param ZoneId: Region ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ZoneId: int
        :param AppId: User APPID
Note: this field may return null, indicating that no valid values can be obtained.
        :type AppId: int
        :param Uin: User UIN
Note: this field may return null, indicating that no valid values can be obtained.
        :type Uin: str
        :param ProjectId: Project ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectId: int
        :param VpcId: Cluster `VPCID`
Note: this field may return null, indicating that no valid values can be obtained.
        :type VpcId: int
        :param SubnetId: Subnet ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubnetId: int
        :param Status: Instance status code. Value range:
<li>2: cluster running</li>
<li>3: creating cluster.</li>
<li>4: scaling out cluster.</li>
<li>5: adding router node in cluster.</li>
<li>6: installing component in cluster.</li>
<li>7: cluster executing command.</li>
<li>8: restarting service.</li>
<li>9: entering maintenance.</li>
<li>10: suspending service.</li>
<li>11: exiting maintenance.</li>
<li>12: exiting suspension.</li>
<li>13: delivering configuration.</li>
<li>14: terminating cluster.</li>
<li>15: terminating core node.</li>
<li>16: terminating task node.</li>
<li>17: terminating router node.</li>
<li>18: changing webproxy password.</li>
<li>19: isolating cluster.</li>
<li>20: resuming cluster.</li>
<li>21: repossessing cluster.</li>
<li>22: waiting for configuration adjustment.</li>
<li>23: cluster isolated.</li>
<li>24: removing node.</li>
<li>33: waiting for refund.</li>
<li>34: refunded.</li>
<li>301: creation failed.</li>
<li>302: scale-out failed.</li>
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param AddTime: Creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :type AddTime: str
        :param RunTime: Execution duration
Note: this field may return null, indicating that no valid values can be obtained.
        :type RunTime: str
        :param Config: Cluster product configuration information
Note: this field may return null, indicating that no valid values can be obtained.
        :type Config: :class:`tencentcloud.emr.v20190103.models.EmrProductConfigOutter`
        :param MasterIp: Public IP of master node
Note: this field may return null, indicating that no valid values can be obtained.
        :type MasterIp: str
        :param EmrVersion: EMR version
Note: this field may return null, indicating that no valid values can be obtained.
        :type EmrVersion: str
        :param ChargeType: Billing mode
Note: this field may return null, indicating that no valid values can be obtained.
        :type ChargeType: int
        :param TradeVersion: Transaction version
Note: this field may return null, indicating that no valid values can be obtained.
        :type TradeVersion: int
        :param ResourceOrderId: Resource order ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResourceOrderId: int
        :param IsTradeCluster: Whether this is a paid cluster
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsTradeCluster: int
        :param AlarmInfo: Alarm information for cluster error
Note: this field may return null, indicating that no valid values can be obtained.
        :type AlarmInfo: str
        :param IsWoodpeckerCluster: Whether the new architecture is used
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsWoodpeckerCluster: int
        :param MetaDb: Metadatabase information
Note: this field may return null, indicating that no valid values can be obtained.
        :type MetaDb: str
        :param Tags: Tag information
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param HiveMetaDb: Hive metadata
Note: this field may return null, indicating that no valid values can be obtained.
        :type HiveMetaDb: str
        :param ServiceClass: Cluster type: EMR, CLICKHOUSE, DRUID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceClass: str
        :param AliasInfo: Alias serialization of all nodes in cluster
Note: this field may return null, indicating that no valid values can be obtained.
        :type AliasInfo: str
        :param ProductId: Cluster version ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProductId: int
        :param Zone: Availability zone
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Zone: str
        :param SceneName: Scenario name
Note: This field may return `null`, indicating that no valid value was found.
        :type SceneName: str
        :param SceneServiceClass: Scenario-based cluster type
Note: This field may return `null`, indicating that no valid value was found.
        :type SceneServiceClass: str
        :param SceneEmrVersion: Scenario-based EMR version
Note: This field may return `null`, indicating that no valid value was found.
        :type SceneEmrVersion: str
        :param DisplayName: Scenario-based cluster type
Note: This field may return `null`, indicating that no valid value was found.
        :type DisplayName: str
        :param VpcName: VPC name
Note: This field may return `null`, indicating that no valid value was found.
        :type VpcName: str
        :param SubnetName: Subnet name
Note: This field may return `null`, indicating that no valid value was found.
        :type SubnetName: str
        :param ClusterExternalServiceInfo: Cluster dependency
Note: This field may return `null`, indicating that no valid value was found.
        :type ClusterExternalServiceInfo: list of ClusterExternalServiceInfo
        :param UniqVpcId: The VPC ID string type of the cluster
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type UniqVpcId: str
        :param UniqSubnetId: The subnet ID string type of the cluster
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type UniqSubnetId: str
        :param TopologyInfoList: Node information
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TopologyInfoList: list of TopologyInfo
        :param IsMultiZoneCluster: Multi-AZ cluster
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type IsMultiZoneCluster: bool
        """
        self.Id = None
        self.ClusterId = None
        self.Ftitle = None
        self.ClusterName = None
        self.RegionId = None
        self.ZoneId = None
        self.AppId = None
        self.Uin = None
        self.ProjectId = None
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.AddTime = None
        self.RunTime = None
        self.Config = None
        self.MasterIp = None
        self.EmrVersion = None
        self.ChargeType = None
        self.TradeVersion = None
        self.ResourceOrderId = None
        self.IsTradeCluster = None
        self.AlarmInfo = None
        self.IsWoodpeckerCluster = None
        self.MetaDb = None
        self.Tags = None
        self.HiveMetaDb = None
        self.ServiceClass = None
        self.AliasInfo = None
        self.ProductId = None
        self.Zone = None
        self.SceneName = None
        self.SceneServiceClass = None
        self.SceneEmrVersion = None
        self.DisplayName = None
        self.VpcName = None
        self.SubnetName = None
        self.ClusterExternalServiceInfo = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.TopologyInfoList = None
        self.IsMultiZoneCluster = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.ClusterId = params.get("ClusterId")
        self.Ftitle = params.get("Ftitle")
        self.ClusterName = params.get("ClusterName")
        self.RegionId = params.get("RegionId")
        self.ZoneId = params.get("ZoneId")
        self.AppId = params.get("AppId")
        self.Uin = params.get("Uin")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.AddTime = params.get("AddTime")
        self.RunTime = params.get("RunTime")
        if params.get("Config") is not None:
            self.Config = EmrProductConfigOutter()
            self.Config._deserialize(params.get("Config"))
        self.MasterIp = params.get("MasterIp")
        self.EmrVersion = params.get("EmrVersion")
        self.ChargeType = params.get("ChargeType")
        self.TradeVersion = params.get("TradeVersion")
        self.ResourceOrderId = params.get("ResourceOrderId")
        self.IsTradeCluster = params.get("IsTradeCluster")
        self.AlarmInfo = params.get("AlarmInfo")
        self.IsWoodpeckerCluster = params.get("IsWoodpeckerCluster")
        self.MetaDb = params.get("MetaDb")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.HiveMetaDb = params.get("HiveMetaDb")
        self.ServiceClass = params.get("ServiceClass")
        self.AliasInfo = params.get("AliasInfo")
        self.ProductId = params.get("ProductId")
        self.Zone = params.get("Zone")
        self.SceneName = params.get("SceneName")
        self.SceneServiceClass = params.get("SceneServiceClass")
        self.SceneEmrVersion = params.get("SceneEmrVersion")
        self.DisplayName = params.get("DisplayName")
        self.VpcName = params.get("VpcName")
        self.SubnetName = params.get("SubnetName")
        if params.get("ClusterExternalServiceInfo") is not None:
            self.ClusterExternalServiceInfo = []
            for item in params.get("ClusterExternalServiceInfo"):
                obj = ClusterExternalServiceInfo()
                obj._deserialize(item)
                self.ClusterExternalServiceInfo.append(obj)
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        if params.get("TopologyInfoList") is not None:
            self.TopologyInfoList = []
            for item in params.get("TopologyInfoList"):
                obj = TopologyInfo()
                obj._deserialize(item)
                self.TopologyInfoList.append(obj)
        self.IsMultiZoneCluster = params.get("IsMultiZoneCluster")
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
        r"""
        :param ProductId: Product ID. Different product IDs represent different EMR product versions. Valid values:
<li>1: EMR v1.3.1</li>
<li>2: EMR v2.0.1</li>
<li>4: EMR v2.1.0</li>
<li>7: EMR v3.0.0</li>
<li>9: EMR v2.2.0</li>
<li>11: ClickHouse v1.0.0</li>
<li>13: Druid v1.0.0</li>
<li>15: EMR v2.2.1</li>
<li>16: EMR v2.3.0</li>
<li>17: ClickHouse v1.1.0</li>
<li>19: EMR v2.4.0</li>
<li>20: EMR v2.5.0</li>
<li>22: ClickHouse v1.2.0</li>
<li>24: EMR TianQiong v1.0.0</li>
<li>25: EMR v3.1.0</li>
<li>26: Doris v1.0.0</li>
<li>27: Kafka v1.0.0</li>
<li>28: EMR v3.2.0</li>
<li>29: EMR v2.5.1</li>
<li>30: EMR v2.6.0</li>
        :type ProductId: int
        :param Software: List of deployed components. The list of component options varies by EMR product ID (i.e., `ProductId`; for specific meanings, please see the `ProductId` input parameter). For more information, please see [Component Version](https://intl.cloud.tencent.com/document/product/589/20279?from_cn_redirect=1).
Enter an instance value: `hive` or `flink`.
        :type Software: list of str
        :param SupportHA: Whether to enable high node availability. Valid values:
<li>0: does not enable high availability of node.</li>
<li>1: enables high availability of node.</li>
        :type SupportHA: int
        :param InstanceName: Instance name.
<li>Length limit: 6-36 characters.</li>
<li>Only letters, numbers, dashes (-), and underscores (_) are supported.</li>
        :type InstanceName: str
        :param PayMode: Instance billing mode. Valid values:
<li>0: pay-as-you-go.</li>
        :type PayMode: int
        :param TimeSpan: Purchase duration of instance, which needs to be used together with `TimeUnit`.
<li>When `TimeUnit` is `s`, this parameter can only be filled with 3600, indicating a pay-as-you-go instance.</li>
<li>When `TimeUnit` is `m`, the number entered in this parameter indicates the purchase duration of the monthly-subscription instance; for example, 1 means one month</li>
        :type TimeSpan: int
        :param TimeUnit: Time unit of instance purchase duration. Valid values:
<li>s: seconds. When `PayMode` is 0, `TimeUnit` can only be `s`.</li>
<li>m: month. When `PayMode` is 1, `TimeUnit` can only be `m`.</li>
        :type TimeUnit: str
        :param LoginSettings: Instance login settings. This parameter allows you to set the login password or key for your purchased node.
<li>If the key is set, the password will be only used for login to the native component WebUI.</li>
<li>If the key is not set, the password will be used for login to all purchased nodes and the native component WebUI.</li>
        :type LoginSettings: :class:`tencentcloud.emr.v20190103.models.LoginSettings`
        :param VPCSettings: Configuration information of VPC. This parameter is used to specify the VPC ID, subnet ID, etc.
        :type VPCSettings: :class:`tencentcloud.emr.v20190103.models.VPCSettings`
        :param ResourceSpec: Node resource specification.
        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.NewResourceSpec`
        :param COSSettings: Parameter required for enabling COS access.
        :type COSSettings: :class:`tencentcloud.emr.v20190103.models.COSSettings`
        :param Placement: Instance location. This parameter is used to specify the AZ, project, and other attributes of the instance.
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param SgId: Security group to which an instance belongs in the format of `sg-xxxxxxxx`. This parameter can be obtained from the `SecurityGroupId` field in the return value of the [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808) API.
        :type SgId: str
        :param PreExecutedFileSettings: [Bootstrap action](https://intl.cloud.tencent.com/document/product/589/35656?from_cn_redirect=1) script settings
        :type PreExecutedFileSettings: list of PreExecuteFileSettings
        :param AutoRenew: Whether auto-renewal is enabled. Valid values:
<li>0: auto-renewal not enabled.</li>
<li>1: auto-renewal enabled.</li>
        :type AutoRenew: int
        :param ClientToken: Client token.
        :type ClientToken: str
        :param NeedMasterWan: Whether to enable public IP access for master node. Valid values:
<li>NEED_MASTER_WAN: enables public IP for master node.</li>
<li>NOT_NEED_MASTER_WAN: does not enable.</li>Public IP is enabled for master node by default.
        :type NeedMasterWan: str
        :param RemoteLoginAtCreate: Whether to enable remote public network login, i.e., port 22. When `SgId` is not empty, this parameter does not take effect.
        :type RemoteLoginAtCreate: int
        :param CheckSecurity: Whether to enable secure cluster. 0: no; other values: yes.
        :type CheckSecurity: int
        :param ExtendFsField: Accesses to external file system.
        :type ExtendFsField: str
        :param Tags: Tag description list. This parameter is used to bind a tag to a resource instance.
        :type Tags: list of Tag
        :param DisasterRecoverGroupIds: List of spread placement group IDs. Only one can be specified currently.
This parameter can be obtained in the `SecurityGroupId` field in the return value of the [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/product/213/15486?from_cn_redirect=1) API.
        :type DisasterRecoverGroupIds: list of str
        :param CbsEncrypt: CBS disk encryption at the cluster level. 0: not encrypted, 1: encrypted
        :type CbsEncrypt: int
        :param MetaType: Hive-shared metadatabase type. Valid values:
<li>EMR_DEFAULT_META: the cluster creates one by default.</li>
<li>EMR_EXIST_META: the cluster uses the specified EMR-MetaDB instance.</li>
<li>USER_CUSTOM_META: the cluster uses a custom MetaDB instance.</li>
        :type MetaType: str
        :param UnifyMetaInstanceId: EMR-MetaDB instance
        :type UnifyMetaInstanceId: str
        :param MetaDBInfo: Custom MetaDB instance information
        :type MetaDBInfo: :class:`tencentcloud.emr.v20190103.models.CustomMetaInfo`
        :param ApplicationRole: Custom application role.
        :type ApplicationRole: str
        :param SceneName: Scenario-based values:
Hadoop-Kudu
Hadoop-Zookeeper
Hadoop-Presto
Hadoop-Hbase
        :type SceneName: str
        :param ExternalService: Shared component information
        :type ExternalService: list of ExternalService
        :param VersionID: 
        :type VersionID: int
        :param MultiZone: `true` indicates that the multi-AZ deployment mode is enabled. This parameter is available only in cluster creation and cannot be changed after setting.
        :type MultiZone: bool
        :param MultiZoneSettings: Node resource specs. The actual number of AZs is set, with the first AZ as the primary AZ, the second as the backup AZ, and the third as the arbitrator AZ. If the multi-AZ mode is not enabled, set the value to `1`.
        :type MultiZoneSettings: list of MultiZoneSetting
        """
        self.ProductId = None
        self.Software = None
        self.SupportHA = None
        self.InstanceName = None
        self.PayMode = None
        self.TimeSpan = None
        self.TimeUnit = None
        self.LoginSettings = None
        self.VPCSettings = None
        self.ResourceSpec = None
        self.COSSettings = None
        self.Placement = None
        self.SgId = None
        self.PreExecutedFileSettings = None
        self.AutoRenew = None
        self.ClientToken = None
        self.NeedMasterWan = None
        self.RemoteLoginAtCreate = None
        self.CheckSecurity = None
        self.ExtendFsField = None
        self.Tags = None
        self.DisasterRecoverGroupIds = None
        self.CbsEncrypt = None
        self.MetaType = None
        self.UnifyMetaInstanceId = None
        self.MetaDBInfo = None
        self.ApplicationRole = None
        self.SceneName = None
        self.ExternalService = None
        self.VersionID = None
        self.MultiZone = None
        self.MultiZoneSettings = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Software = params.get("Software")
        self.SupportHA = params.get("SupportHA")
        self.InstanceName = params.get("InstanceName")
        self.PayMode = params.get("PayMode")
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnit = params.get("TimeUnit")
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        if params.get("VPCSettings") is not None:
            self.VPCSettings = VPCSettings()
            self.VPCSettings._deserialize(params.get("VPCSettings"))
        if params.get("ResourceSpec") is not None:
            self.ResourceSpec = NewResourceSpec()
            self.ResourceSpec._deserialize(params.get("ResourceSpec"))
        if params.get("COSSettings") is not None:
            self.COSSettings = COSSettings()
            self.COSSettings._deserialize(params.get("COSSettings"))
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.SgId = params.get("SgId")
        if params.get("PreExecutedFileSettings") is not None:
            self.PreExecutedFileSettings = []
            for item in params.get("PreExecutedFileSettings"):
                obj = PreExecuteFileSettings()
                obj._deserialize(item)
                self.PreExecutedFileSettings.append(obj)
        self.AutoRenew = params.get("AutoRenew")
        self.ClientToken = params.get("ClientToken")
        self.NeedMasterWan = params.get("NeedMasterWan")
        self.RemoteLoginAtCreate = params.get("RemoteLoginAtCreate")
        self.CheckSecurity = params.get("CheckSecurity")
        self.ExtendFsField = params.get("ExtendFsField")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        self.CbsEncrypt = params.get("CbsEncrypt")
        self.MetaType = params.get("MetaType")
        self.UnifyMetaInstanceId = params.get("UnifyMetaInstanceId")
        if params.get("MetaDBInfo") is not None:
            self.MetaDBInfo = CustomMetaInfo()
            self.MetaDBInfo._deserialize(params.get("MetaDBInfo"))
        self.ApplicationRole = params.get("ApplicationRole")
        self.SceneName = params.get("SceneName")
        if params.get("ExternalService") is not None:
            self.ExternalService = []
            for item in params.get("ExternalService"):
                obj = ExternalService()
                obj._deserialize(item)
                self.ExternalService.append(obj)
        self.VersionID = params.get("VersionID")
        self.MultiZone = params.get("MultiZone")
        if params.get("MultiZoneSettings") is not None:
            self.MultiZoneSettings = []
            for item in params.get("MultiZoneSettings"):
                obj = MultiZoneSetting()
                obj._deserialize(item)
                self.MultiZoneSettings.append(obj)
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
        r"""
        :param InstanceId: Instance ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class CustomMetaInfo(AbstractModel):
    """User-created Hive-MetaDB instance information

    """

    def __init__(self):
        r"""
        :param MetaDataJdbcUrl: JDBC connection to custom MetaDB instance beginning with `jdbc:mysql://`
        :type MetaDataJdbcUrl: str
        :param MetaDataUser: Custom MetaDB instance username
        :type MetaDataUser: str
        :param MetaDataPass: Custom MetaDB instance password
        :type MetaDataPass: str
        """
        self.MetaDataJdbcUrl = None
        self.MetaDataUser = None
        self.MetaDataPass = None


    def _deserialize(self, params):
        self.MetaDataJdbcUrl = params.get("MetaDataJdbcUrl")
        self.MetaDataUser = params.get("MetaDataUser")
        self.MetaDataPass = params.get("MetaDataPass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomServiceDefine(AbstractModel):
    """Shared self-built component parameters

    """

    def __init__(self):
        r"""
        :param Name: Custom parameter key
        :type Name: str
        :param Value: Custom parameter value
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterNodesRequest(AbstractModel):
    """DescribeClusterNodes request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Cluster instance ID in the format of emr-xxxxxxxx
        :type InstanceId: str
        :param NodeFlag: Node flag. Valid values:
<li>all: gets the information of nodes in all types except TencentDB information.</li>
<li>master: gets master node information.</li>
<li>core: gets core node information.</li>
<li>task: gets task node information.</li>
<li>common: gets common node information.</li>
<li>router: gets router node information.</li>
<li>db: gets TencentDB information in normal status.</li>
Note: only the above values are supported for the time being. Entering other values will cause errors.
        :type NodeFlag: str
        :param Offset: Page number. Default value: 0, indicating the first page.
        :type Offset: int
        :param Limit: Number of returned results per page. Default value: 100. Maximum value: 100
        :type Limit: int
        :param HardwareResourceType: Resource type. Valid values: all, host, pod. Default value: all
        :type HardwareResourceType: str
        :param SearchFields: Searchable field
        :type SearchFields: list of SearchItem
        """
        self.InstanceId = None
        self.NodeFlag = None
        self.Offset = None
        self.Limit = None
        self.HardwareResourceType = None
        self.SearchFields = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.NodeFlag = params.get("NodeFlag")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.HardwareResourceType = params.get("HardwareResourceType")
        if params.get("SearchFields") is not None:
            self.SearchFields = []
            for item in params.get("SearchFields"):
                obj = SearchItem()
                obj._deserialize(item)
                self.SearchFields.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterNodesResponse(AbstractModel):
    """DescribeClusterNodes response structure.

    """

    def __init__(self):
        r"""
        :param TotalCnt: Total number of queried nodes
        :type TotalCnt: int
        :param NodeList: List of node details
Note: this field may return null, indicating that no valid values can be obtained.
        :type NodeList: list of NodeHardwareInfo
        :param TagKeys: List of tag keys owned by user
Note: this field may return null, indicating that no valid values can be obtained.
        :type TagKeys: list of str
        :param HardwareResourceTypeList: Resource type list
Note: this field may return null, indicating that no valid values can be obtained.
        :type HardwareResourceTypeList: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCnt = None
        self.NodeList = None
        self.TagKeys = None
        self.HardwareResourceTypeList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCnt = params.get("TotalCnt")
        if params.get("NodeList") is not None:
            self.NodeList = []
            for item in params.get("NodeList"):
                obj = NodeHardwareInfo()
                obj._deserialize(item)
                self.NodeList.append(obj)
        self.TagKeys = params.get("TagKeys")
        self.HardwareResourceTypeList = params.get("HardwareResourceTypeList")
        self.RequestId = params.get("RequestId")


class DescribeInstancesListRequest(AbstractModel):
    """DescribeInstancesList request structure.

    """

    def __init__(self):
        r"""
        :param DisplayStrategy: Cluster filtering policy. Valid values: <li>clusterList: Queries the list of clusters excluding terminated ones.</li><li>monitorManage: Queries the list of clusters excluding those terminated, under creation and not successfully created.</li><li>cloudHardwareManage/componentManage: Two reserved values, which have the same implications as those of `monitorManage`.</li>
        :type DisplayStrategy: str
        :param Offset: Page number. Default value: `0`, indicating the first page.
        :type Offset: int
        :param Limit: Number of returned results per page. Default value: `10`; maximum value: `100`.
        :type Limit: int
        :param OrderField: Sorting field. Valid values: <li>clusterId: Sorting by instance ID. </li><li>addTime: Sorting by instance creation time.</li><li>status: Sorting by instance status code.</li>
        :type OrderField: str
        :param Asc: Sort ascending or descending based on `OrderField`. Valid values:<li>0: Descending.</li><li>1: Ascending.</li>Default value: `0`.
        :type Asc: int
        :param Filters: Custom query
        :type Filters: list of Filters
        """
        self.DisplayStrategy = None
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.Asc = None
        self.Filters = None


    def _deserialize(self, params):
        self.DisplayStrategy = params.get("DisplayStrategy")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderField = params.get("OrderField")
        self.Asc = params.get("Asc")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesListResponse(AbstractModel):
    """DescribeInstancesList response structure.

    """

    def __init__(self):
        r"""
        :param TotalCnt: Number of eligible instances.
        :type TotalCnt: int
        :param InstancesList: Cluster instance list.
        :type InstancesList: list of EmrListInstance
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCnt = None
        self.InstancesList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCnt = params.get("TotalCnt")
        if params.get("InstancesList") is not None:
            self.InstancesList = []
            for item in params.get("InstancesList"):
                obj = EmrListInstance()
                obj._deserialize(item)
                self.InstancesList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances request structure.

    """

    def __init__(self):
        r"""
        :param DisplayStrategy: Cluster filtering policy. Valid values:
<li>clusterList: queries the list of clusters except terminated ones.</li>
<li>monitorManage: queries the list of clusters except those that have been terminated, are being created, or failed to be created.</li>
<li>cloudHardwareManage/componentManage: reserved fields with the same meaning as `monitorManage`.</li>
        :type DisplayStrategy: str
        :param InstanceIds: Queries by one or more instance IDs in the format of `emr-xxxxxxxx`. For the format of this parameter, please see the `id.N` section in [API Overview](https://intl.cloud.tencent.com/document/api/213/15688). If no instance ID is entered, the list of all instances under this `APPID` will be returned.
        :type InstanceIds: list of str
        :param Offset: Page number. Default value: 0, indicating the first page.
        :type Offset: int
        :param Limit: Number of returned results per page. Default value: 10. Maximum value: 100
        :type Limit: int
        :param ProjectId: ID of the project to which the instance belongs. This parameter can be obtained from the `projectId` field in the return value of the `DescribeProject` API. If this value is -1, the list of all instances will be returned.
        :type ProjectId: int
        :param OrderField: Sorting field. Valid values:
<li>clusterId: sorts by cluster ID.</li>
<li>addTime: sorts by instance creation time.</li>
<li>status: sorts by instance status code.</li>
        :type OrderField: str
        :param Asc: Sorts according to `OrderField` in ascending or descending order. Valid values:
<li>0: descending order.</li>
<li>1: ascending order.</li>Default value: 0.
        :type Asc: int
        """
        self.DisplayStrategy = None
        self.InstanceIds = None
        self.Offset = None
        self.Limit = None
        self.ProjectId = None
        self.OrderField = None
        self.Asc = None


    def _deserialize(self, params):
        self.DisplayStrategy = params.get("DisplayStrategy")
        self.InstanceIds = params.get("InstanceIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ProjectId = params.get("ProjectId")
        self.OrderField = params.get("OrderField")
        self.Asc = params.get("Asc")
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
        r"""
        :param TotalCnt: Number of eligible instances.
        :type TotalCnt: int
        :param ClusterList: List of EMR instance details.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClusterList: list of ClusterInstancesInfo
        :param TagKeys: List of tag keys associated to an instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TagKeys: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCnt = None
        self.ClusterList = None
        self.TagKeys = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCnt = params.get("TotalCnt")
        if params.get("ClusterList") is not None:
            self.ClusterList = []
            for item in params.get("ClusterList"):
                obj = ClusterInstancesInfo()
                obj._deserialize(item)
                self.ClusterList.append(obj)
        self.TagKeys = params.get("TagKeys")
        self.RequestId = params.get("RequestId")


class DescribeResourceScheduleRequest(AbstractModel):
    """DescribeResourceSchedule request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: EMR cluster ID
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
        


class DescribeResourceScheduleResponse(AbstractModel):
    """DescribeResourceSchedule response structure.

    """

    def __init__(self):
        r"""
        :param OpenSwitch: Whether to enable the resource scheduling feature
        :type OpenSwitch: bool
        :param Scheduler: The resource scheduler in service
        :type Scheduler: str
        :param FSInfo: Fair Scheduler information
        :type FSInfo: str
        :param CSInfo: Capacity Scheduler information
        :type CSInfo: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.OpenSwitch = None
        self.Scheduler = None
        self.FSInfo = None
        self.CSInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OpenSwitch = params.get("OpenSwitch")
        self.Scheduler = params.get("Scheduler")
        self.FSInfo = params.get("FSInfo")
        self.CSInfo = params.get("CSInfo")
        self.RequestId = params.get("RequestId")


class DescribeUsersForUserManagerRequest(AbstractModel):
    """DescribeUsersForUserManager request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Cluster instance ID
        :type InstanceId: str
        :param PageNo: Page number
        :type PageNo: int
        :param PageSize: Page size
        :type PageSize: int
        :param UserManagerFilter: User list query filter
        :type UserManagerFilter: :class:`tencentcloud.emr.v20190103.models.UserManagerFilter`
        :param NeedKeytabInfo: Whether the Keytab file information is required. This field is only valid for clusters with Kerberos enabled and defaults to `false`.
        :type NeedKeytabInfo: bool
        """
        self.InstanceId = None
        self.PageNo = None
        self.PageSize = None
        self.UserManagerFilter = None
        self.NeedKeytabInfo = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.PageNo = params.get("PageNo")
        self.PageSize = params.get("PageSize")
        if params.get("UserManagerFilter") is not None:
            self.UserManagerFilter = UserManagerFilter()
            self.UserManagerFilter._deserialize(params.get("UserManagerFilter"))
        self.NeedKeytabInfo = params.get("NeedKeytabInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsersForUserManagerResponse(AbstractModel):
    """DescribeUsersForUserManager response structure.

    """

    def __init__(self):
        r"""
        :param TotalCnt: Total number
        :type TotalCnt: int
        :param UserManagerUserList: User information list
Note: This field may return null, indicating that no valid value can be obtained.
        :type UserManagerUserList: list of UserManagerUserBriefInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCnt = None
        self.UserManagerUserList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCnt = params.get("TotalCnt")
        if params.get("UserManagerUserList") is not None:
            self.UserManagerUserList = []
            for item in params.get("UserManagerUserList"):
                obj = UserManagerUserBriefInfo()
                obj._deserialize(item)
                self.UserManagerUserList.append(obj)
        self.RequestId = params.get("RequestId")


class EmrListInstance(AbstractModel):
    """Returned cluster list sample

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param StatusDesc: Status description
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type StatusDesc: str
        :param ClusterName: Cluster name
        :type ClusterName: str
        :param ZoneId: Cluster region
        :type ZoneId: int
        :param AppId: User APPID
        :type AppId: int
        :param AddTime: Creation time
        :type AddTime: str
        :param RunTime: Running time
        :type RunTime: str
        :param MasterIp: Cluster IP
        :type MasterIp: str
        :param EmrVersion: Cluster version
        :type EmrVersion: str
        :param ChargeType: Cluster billing mode
        :type ChargeType: int
        :param Id: EMR ID
        :type Id: int
        :param ProductId: Product ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ProductId: int
        :param ProjectId: Project ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ProjectId: int
        :param RegionId: Region
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RegionId: int
        :param SubnetId: Subnet ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SubnetId: int
        :param VpcId: VPC ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type VpcId: int
        :param Zone: Region
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Zone: str
        :param Status: Status code
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Status: int
        :param Tags: Instance tag
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Tags: list of Tag
        :param AlarmInfo: Alarm information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AlarmInfo: str
        :param IsWoodpeckerCluster: Whether it is a Woodpecker cluster
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IsWoodpeckerCluster: int
        :param VpcName: VPC name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type VpcName: str
        :param SubnetName: Subnet name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SubnetName: str
        :param UniqVpcId: VPC ID string
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UniqVpcId: str
        :param UniqSubnetId: Subnet ID string
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UniqSubnetId: str
        :param ClusterClass: Cluster type
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ClusterClass: str
        :param IsMultiZoneCluster: Whether it is a multi-AZ cluster
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IsMultiZoneCluster: bool
        """
        self.ClusterId = None
        self.StatusDesc = None
        self.ClusterName = None
        self.ZoneId = None
        self.AppId = None
        self.AddTime = None
        self.RunTime = None
        self.MasterIp = None
        self.EmrVersion = None
        self.ChargeType = None
        self.Id = None
        self.ProductId = None
        self.ProjectId = None
        self.RegionId = None
        self.SubnetId = None
        self.VpcId = None
        self.Zone = None
        self.Status = None
        self.Tags = None
        self.AlarmInfo = None
        self.IsWoodpeckerCluster = None
        self.VpcName = None
        self.SubnetName = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.ClusterClass = None
        self.IsMultiZoneCluster = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.StatusDesc = params.get("StatusDesc")
        self.ClusterName = params.get("ClusterName")
        self.ZoneId = params.get("ZoneId")
        self.AppId = params.get("AppId")
        self.AddTime = params.get("AddTime")
        self.RunTime = params.get("RunTime")
        self.MasterIp = params.get("MasterIp")
        self.EmrVersion = params.get("EmrVersion")
        self.ChargeType = params.get("ChargeType")
        self.Id = params.get("Id")
        self.ProductId = params.get("ProductId")
        self.ProjectId = params.get("ProjectId")
        self.RegionId = params.get("RegionId")
        self.SubnetId = params.get("SubnetId")
        self.VpcId = params.get("VpcId")
        self.Zone = params.get("Zone")
        self.Status = params.get("Status")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AlarmInfo = params.get("AlarmInfo")
        self.IsWoodpeckerCluster = params.get("IsWoodpeckerCluster")
        self.VpcName = params.get("VpcName")
        self.SubnetName = params.get("SubnetName")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.ClusterClass = params.get("ClusterClass")
        self.IsMultiZoneCluster = params.get("IsMultiZoneCluster")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmrProductConfigOutter(AbstractModel):
    """EMR product configuration

    """

    def __init__(self):
        r"""
        :param SoftInfo: Software information
Note: this field may return null, indicating that no valid values can be obtained.
        :type SoftInfo: list of str
        :param MasterNodeSize: Number of master nodes
Note: this field may return null, indicating that no valid values can be obtained.
        :type MasterNodeSize: int
        :param CoreNodeSize: Number of core nodes
Note: this field may return null, indicating that no valid values can be obtained.
        :type CoreNodeSize: int
        :param TaskNodeSize: Number of task nodes
Note: this field may return null, indicating that no valid values can be obtained.
        :type TaskNodeSize: int
        :param ComNodeSize: Number of common nodes
Note: this field may return null, indicating that no valid values can be obtained.
        :type ComNodeSize: int
        :param MasterResource: Master node resource
Note: this field may return null, indicating that no valid values can be obtained.
        :type MasterResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`
        :param CoreResource: Core node resource
Note: this field may return null, indicating that no valid values can be obtained.
        :type CoreResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`
        :param TaskResource: Task node resource
Note: this field may return null, indicating that no valid values can be obtained.
        :type TaskResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`
        :param ComResource: Common node resource
Note: this field may return null, indicating that no valid values can be obtained.
        :type ComResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`
        :param OnCos: Whether COS is used
Note: this field may return null, indicating that no valid values can be obtained.
        :type OnCos: bool
        :param ChargeType: Billing mode
Note: this field may return null, indicating that no valid values can be obtained.
        :type ChargeType: int
        :param RouterNodeSize: Number of router nodes
Note: this field may return null, indicating that no valid values can be obtained.
        :type RouterNodeSize: int
        :param SupportHA: Whether HA is supported
Note: this field may return null, indicating that no valid values can be obtained.
        :type SupportHA: bool
        :param SecurityOn: Whether secure mode is supported
Note: this field may return null, indicating that no valid values can be obtained.
        :type SecurityOn: bool
        :param SecurityGroup: Security group name
Note: this field may return null, indicating that no valid values can be obtained.
        :type SecurityGroup: str
        :param CbsEncrypt: Whether to enable CBS encryption
Note: this field may return null, indicating that no valid values can be obtained.
        :type CbsEncrypt: int
        :param ApplicationRole: Custom application role
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type ApplicationRole: str
        :param SecurityGroups: Security groups
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type SecurityGroups: list of str
        :param PublicKeyId: SSH key ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type PublicKeyId: str
        """
        self.SoftInfo = None
        self.MasterNodeSize = None
        self.CoreNodeSize = None
        self.TaskNodeSize = None
        self.ComNodeSize = None
        self.MasterResource = None
        self.CoreResource = None
        self.TaskResource = None
        self.ComResource = None
        self.OnCos = None
        self.ChargeType = None
        self.RouterNodeSize = None
        self.SupportHA = None
        self.SecurityOn = None
        self.SecurityGroup = None
        self.CbsEncrypt = None
        self.ApplicationRole = None
        self.SecurityGroups = None
        self.PublicKeyId = None


    def _deserialize(self, params):
        self.SoftInfo = params.get("SoftInfo")
        self.MasterNodeSize = params.get("MasterNodeSize")
        self.CoreNodeSize = params.get("CoreNodeSize")
        self.TaskNodeSize = params.get("TaskNodeSize")
        self.ComNodeSize = params.get("ComNodeSize")
        if params.get("MasterResource") is not None:
            self.MasterResource = OutterResource()
            self.MasterResource._deserialize(params.get("MasterResource"))
        if params.get("CoreResource") is not None:
            self.CoreResource = OutterResource()
            self.CoreResource._deserialize(params.get("CoreResource"))
        if params.get("TaskResource") is not None:
            self.TaskResource = OutterResource()
            self.TaskResource._deserialize(params.get("TaskResource"))
        if params.get("ComResource") is not None:
            self.ComResource = OutterResource()
            self.ComResource._deserialize(params.get("ComResource"))
        self.OnCos = params.get("OnCos")
        self.ChargeType = params.get("ChargeType")
        self.RouterNodeSize = params.get("RouterNodeSize")
        self.SupportHA = params.get("SupportHA")
        self.SecurityOn = params.get("SecurityOn")
        self.SecurityGroup = params.get("SecurityGroup")
        self.CbsEncrypt = params.get("CbsEncrypt")
        self.ApplicationRole = params.get("ApplicationRole")
        self.SecurityGroups = params.get("SecurityGroups")
        self.PublicKeyId = params.get("PublicKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExternalService(AbstractModel):
    """Shared component information

    """

    def __init__(self):
        r"""
        :param ShareType: Shared component type, which can be EMR or CUSTOM
        :type ShareType: str
        :param CustomServiceDefineList: Custom parameters
        :type CustomServiceDefineList: list of CustomServiceDefine
        :param Service: Shared component name
        :type Service: str
        :param InstanceId: Shared component cluster
        :type InstanceId: str
        """
        self.ShareType = None
        self.CustomServiceDefineList = None
        self.Service = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.ShareType = params.get("ShareType")
        if params.get("CustomServiceDefineList") is not None:
            self.CustomServiceDefineList = []
            for item in params.get("CustomServiceDefineList"):
                obj = CustomServiceDefine()
                obj._deserialize(item)
                self.CustomServiceDefineList.append(obj)
        self.Service = params.get("Service")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filters(AbstractModel):
    """Custom query filter of the EMR cluster instance list

    """

    def __init__(self):
        r"""
        :param Name: Field name
        :type Name: str
        :param Values: Filters by the field value
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
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
        :param TimeUnit: Time unit of instance purchase duration. Valid values:
<li>s: seconds. When `PayMode` is 0, `TimeUnit` can only be `s`.</li>
        :type TimeUnit: str
        :param TimeSpan: Purchase duration of instance, which needs to be used together with `TimeUnit`.
<li>When `TimeUnit` is `s`, this parameter can only be filled with 3600, indicating a pay-as-you-go instance.</li>
<li>When `TimeUnit` is `m`, the number entered in this parameter indicates the purchase duration of the monthly-subscription instance; for example, 1 means one month</li>
        :type TimeSpan: int
        :param Currency: Currency.
        :type Currency: str
        :param PayMode: Instance billing mode. Valid values:
<li>0: pay-as-you-go.</li>
        :type PayMode: int
        :param SupportHA: Whether to enable high availability of node. Valid values:
<li>0: does not enable high availability of node.</li>
<li>1: enables high availability of node.</li>
        :type SupportHA: int
        :param Software: List of deployed components. Different required components need to be selected for different EMR product IDs (i.e., `ProductId`; for specific meanings, please see the `ProductId` field in the input parameter):
<li>When `ProductId` is 1, the required components include hadoop-2.7.3, knox-1.2.0, and zookeeper-3.4.9</li>
<li>When `ProductId` is 2, the required components include hadoop-2.7.3, knox-1.2.0, and zookeeper-3.4.9</li>
<li>When `ProductId` is 4, the required components include hadoop-2.8.4, knox-1.2.0, and zookeeper-3.4.9</li>
<li>When `ProductId` is 7, the required components include hadoop-3.1.2, knox-1.2.0, and zookeeper-3.4.9</li>
        :type Software: list of str
        :param ResourceSpec: Node specification queried for price.
        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.NewResourceSpec`
        :param Placement: Instance location. This parameter is used to specify the AZ, project, and other attributes of the instance.
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param VPCSettings: Configuration information of VPC. This parameter is used to specify the VPC ID, subnet ID, etc.
        :type VPCSettings: :class:`tencentcloud.emr.v20190103.models.VPCSettings`
        :param MetaType: Hive-shared metadatabase type. Valid values:
<li>EMR_DEFAULT_META: the cluster creates one by default.</li>
<li>EMR_EXIST_META: the cluster uses the specified EMR-MetaDB instance.</li>
<li>USER_CUSTOM_META: the cluster uses a custom MetaDB instance.</li>
        :type MetaType: str
        :param UnifyMetaInstanceId: EMR-MetaDB instance
        :type UnifyMetaInstanceId: str
        :param MetaDBInfo: Custom MetaDB instance information
        :type MetaDBInfo: :class:`tencentcloud.emr.v20190103.models.CustomMetaInfo`
        :param ProductId: Product ID. Different product IDs represent different EMR product versions. Valid values:
<li>1: EMR v1.3.1.</li>
<li>2: EMR v2.0.1.</li>
<li>4: EMR v2.1.0.</li>
<li>7: EMR v3.0.0.</li>
        :type ProductId: int
        :param SceneName: Scenario-based values:
Hadoop-Kudu
Hadoop-Zookeeper
Hadoop-Presto
Hadoop-Hbase
        :type SceneName: str
        :param ExternalService: Shared component information
        :type ExternalService: list of ExternalService
        :param VersionID: 
        :type VersionID: int
        :param MultiZoneSettings: AZ specs
        :type MultiZoneSettings: list of MultiZoneSetting
        """
        self.TimeUnit = None
        self.TimeSpan = None
        self.Currency = None
        self.PayMode = None
        self.SupportHA = None
        self.Software = None
        self.ResourceSpec = None
        self.Placement = None
        self.VPCSettings = None
        self.MetaType = None
        self.UnifyMetaInstanceId = None
        self.MetaDBInfo = None
        self.ProductId = None
        self.SceneName = None
        self.ExternalService = None
        self.VersionID = None
        self.MultiZoneSettings = None


    def _deserialize(self, params):
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.Currency = params.get("Currency")
        self.PayMode = params.get("PayMode")
        self.SupportHA = params.get("SupportHA")
        self.Software = params.get("Software")
        if params.get("ResourceSpec") is not None:
            self.ResourceSpec = NewResourceSpec()
            self.ResourceSpec._deserialize(params.get("ResourceSpec"))
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        if params.get("VPCSettings") is not None:
            self.VPCSettings = VPCSettings()
            self.VPCSettings._deserialize(params.get("VPCSettings"))
        self.MetaType = params.get("MetaType")
        self.UnifyMetaInstanceId = params.get("UnifyMetaInstanceId")
        if params.get("MetaDBInfo") is not None:
            self.MetaDBInfo = CustomMetaInfo()
            self.MetaDBInfo._deserialize(params.get("MetaDBInfo"))
        self.ProductId = params.get("ProductId")
        self.SceneName = params.get("SceneName")
        if params.get("ExternalService") is not None:
            self.ExternalService = []
            for item in params.get("ExternalService"):
                obj = ExternalService()
                obj._deserialize(item)
                self.ExternalService.append(obj)
        self.VersionID = params.get("VersionID")
        if params.get("MultiZoneSettings") is not None:
            self.MultiZoneSettings = []
            for item in params.get("MultiZoneSettings"):
                obj = MultiZoneSetting()
                obj._deserialize(item)
                self.MultiZoneSettings.append(obj)
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
        :param OriginalCost: Original price.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OriginalCost: float
        :param DiscountCost: Discounted price.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DiscountCost: float
        :param TimeUnit: Time unit of instance purchase duration. Valid values:
<li>s: seconds.</li>
Note: this field may return null, indicating that no valid values can be obtained.
        :type TimeUnit: str
        :param TimeSpan: Purchase duration of instance.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TimeSpan: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.OriginalCost = None
        self.DiscountCost = None
        self.TimeUnit = None
        self.TimeSpan = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalCost = params.get("OriginalCost")
        self.DiscountCost = params.get("DiscountCost")
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.RequestId = params.get("RequestId")


class InquiryPriceRenewInstanceRequest(AbstractModel):
    """InquiryPriceRenewInstance request structure.

    """

    def __init__(self):
        r"""
        :param TimeSpan: How long the instance will be renewed for, which needs to be used together with `TimeUnit`.
        :type TimeSpan: int
        :param ResourceIds: List of resource IDs of the node to be renewed. The resource ID is in the format of `emr-vm-xxxxxxxx`. A valid resource ID can be queried in the [console](https://console.cloud.tencent.com/emr/static/hardware).
        :type ResourceIds: list of str
        :param Placement: Location of the instance. This parameter is used to specify the AZ, project, and other attributes of the instance.
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param PayMode: Instance billing mode.
        :type PayMode: int
        :param TimeUnit: Unit of time for instance renewal.
        :type TimeUnit: str
        :param Currency: Currency.
        :type Currency: str
        :param ModifyPayMode: Whether to change from pay-as-you-go billing to monthly subscription billing. `0`: no; `1`: yes
        :type ModifyPayMode: int
        """
        self.TimeSpan = None
        self.ResourceIds = None
        self.Placement = None
        self.PayMode = None
        self.TimeUnit = None
        self.Currency = None
        self.ModifyPayMode = None


    def _deserialize(self, params):
        self.TimeSpan = params.get("TimeSpan")
        self.ResourceIds = params.get("ResourceIds")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.PayMode = params.get("PayMode")
        self.TimeUnit = params.get("TimeUnit")
        self.Currency = params.get("Currency")
        self.ModifyPayMode = params.get("ModifyPayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceRenewInstanceResponse(AbstractModel):
    """InquiryPriceRenewInstance response structure.

    """

    def __init__(self):
        r"""
        :param OriginalCost: Original price.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OriginalCost: float
        :param DiscountCost: Discounted price.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DiscountCost: float
        :param TimeUnit: Unit of time for instance renewal.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TimeUnit: str
        :param TimeSpan: How long the instance will be renewed for.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TimeSpan: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.OriginalCost = None
        self.DiscountCost = None
        self.TimeUnit = None
        self.TimeSpan = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalCost = params.get("OriginalCost")
        self.DiscountCost = params.get("DiscountCost")
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.RequestId = params.get("RequestId")


class InquiryPriceUpdateInstanceRequest(AbstractModel):
    """InquiryPriceUpdateInstance request structure.

    """

    def __init__(self):
        r"""
        :param TimeUnit: Time unit of scaling. Valid values:
<li>s: seconds. When `PayMode` is 0, `TimeUnit` can only be `s`.</li>
        :type TimeUnit: str
        :param TimeSpan: Duration of scaling, which needs to be used together with `TimeUnit`.
<li>When `PayMode` is 0, `TimeSpan` can only be 3,600.</li>
        :type TimeSpan: int
        :param UpdateSpec: Target node specification.
        :type UpdateSpec: :class:`tencentcloud.emr.v20190103.models.UpdateInstanceSettings`
        :param PayMode: Instance billing mode. Valid values:
<li>0: pay-as-you-go.</li>
        :type PayMode: int
        :param Placement: Instance location. This parameter is used to specify the AZ, project, and other attributes of the instance.
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param Currency: Currency.
        :type Currency: str
        """
        self.TimeUnit = None
        self.TimeSpan = None
        self.UpdateSpec = None
        self.PayMode = None
        self.Placement = None
        self.Currency = None


    def _deserialize(self, params):
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        if params.get("UpdateSpec") is not None:
            self.UpdateSpec = UpdateInstanceSettings()
            self.UpdateSpec._deserialize(params.get("UpdateSpec"))
        self.PayMode = params.get("PayMode")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.Currency = params.get("Currency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceUpdateInstanceResponse(AbstractModel):
    """InquiryPriceUpdateInstance response structure.

    """

    def __init__(self):
        r"""
        :param OriginalCost: Original price.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OriginalCost: float
        :param DiscountCost: Discounted price.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DiscountCost: float
        :param TimeUnit: Time unit of scaling. Valid values:
<li>s: seconds.</li>
Note: this field may return null, indicating that no valid values can be obtained.
        :type TimeUnit: str
        :param TimeSpan: Duration of scaling.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TimeSpan: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.OriginalCost = None
        self.DiscountCost = None
        self.TimeUnit = None
        self.TimeSpan = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalCost = params.get("OriginalCost")
        self.DiscountCost = params.get("DiscountCost")
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.RequestId = params.get("RequestId")


class LoginSettings(AbstractModel):
    """Login settings

    """

    def __init__(self):
        r"""
        :param Password: Password
        :type Password: str
        :param PublicKeyId: Public Key
        :type PublicKeyId: str
        """
        self.Password = None
        self.PublicKeyId = None


    def _deserialize(self, params):
        self.Password = params.get("Password")
        self.PublicKeyId = params.get("PublicKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourceScheduleConfigRequest(AbstractModel):
    """ModifyResourceScheduleConfig request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: EMR cluster ID
        :type InstanceId: str
        :param Key: Business identifier. `fair`: Edit fair configuration items; `fairPlan`: Edit the execution plan; `capacity`: Edit capacity configuration items.
        :type Key: str
        :param Value: Modified module information
        :type Value: str
        """
        self.InstanceId = None
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourceScheduleConfigResponse(AbstractModel):
    """ModifyResourceScheduleConfig response structure.

    """

    def __init__(self):
        r"""
        :param IsDraft: `true`: Draft, indicating the resource pool is not refreshed.
        :type IsDraft: bool
        :param ErrorMsg: Verification error information. If it is not null, the verification fails and thus the configuration fails.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ErrorMsg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.IsDraft = None
        self.ErrorMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsDraft = params.get("IsDraft")
        self.ErrorMsg = params.get("ErrorMsg")
        self.RequestId = params.get("RequestId")


class ModifyResourceSchedulerRequest(AbstractModel):
    """ModifyResourceScheduler request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: EMR cluster ID
        :type InstanceId: str
        :param OldValue: The original scheduler: `fair`
        :type OldValue: str
        :param NewValue: The new scheduler: `capacity`
        :type NewValue: str
        """
        self.InstanceId = None
        self.OldValue = None
        self.NewValue = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.OldValue = params.get("OldValue")
        self.NewValue = params.get("NewValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourceSchedulerResponse(AbstractModel):
    """ModifyResourceScheduler response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MultiDisk(AbstractModel):
    """Multi-cloud disk parameters

    """

    def __init__(self):
        r"""
        :param DiskType: Cloud disk type
<li>`CLOUD_SSD`: SSD</li>
<li>`CLOUD_PREMIUM`: Premium Cloud Storage</li>
<li>`CLOUD_HSSD`: Enhanced SSD</li>
        :type DiskType: str
        :param Volume: Cloud disk size
        :type Volume: int
        :param Count: Number of cloud disks of this type
        :type Count: int
        """
        self.DiskType = None
        self.Volume = None
        self.Count = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.Volume = params.get("Volume")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiDiskMC(AbstractModel):
    """Multi-cloud disk parameters

    """

    def __init__(self):
        r"""
        :param Count: Number of cloud disks in this type
Note: this field may return null, indicating that no valid values can be obtained.
        :type Count: int
        :param Type: Disk type
Note: this field may return null, indicating that no valid values can be obtained.
        :type Type: int
        :param Volume: Cloud disk size
Note: this field may return null, indicating that no valid values can be obtained.
        :type Volume: int
        """
        self.Count = None
        self.Type = None
        self.Volume = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.Type = params.get("Type")
        self.Volume = params.get("Volume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiZoneSetting(AbstractModel):
    """Parameter information of each AZ

    """

    def __init__(self):
        r"""
        :param ZoneTag: "master", "standby", "third-party"
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ZoneTag: str
        :param VPCSettings: None
        :type VPCSettings: :class:`tencentcloud.emr.v20190103.models.VPCSettings`
        :param Placement: None
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
        :param ResourceSpec: None
        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.NewResourceSpec`
        """
        self.ZoneTag = None
        self.VPCSettings = None
        self.Placement = None
        self.ResourceSpec = None


    def _deserialize(self, params):
        self.ZoneTag = params.get("ZoneTag")
        if params.get("VPCSettings") is not None:
            self.VPCSettings = VPCSettings()
            self.VPCSettings._deserialize(params.get("VPCSettings"))
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        if params.get("ResourceSpec") is not None:
            self.ResourceSpec = NewResourceSpec()
            self.ResourceSpec._deserialize(params.get("ResourceSpec"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NewResourceSpec(AbstractModel):
    """Resource description

    """

    def __init__(self):
        r"""
        :param MasterResourceSpec: Describes master node resource
        :type MasterResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`
        :param CoreResourceSpec: Describes core node resource
        :type CoreResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`
        :param TaskResourceSpec: Describes task node resource
        :type TaskResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`
        :param MasterCount: Number of master nodes
        :type MasterCount: int
        :param CoreCount: Number of core nodes
        :type CoreCount: int
        :param TaskCount: Number of task nodes
        :type TaskCount: int
        :param CommonResourceSpec: Describes common node resource
        :type CommonResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`
        :param CommonCount: Number of common nodes
        :type CommonCount: int
        """
        self.MasterResourceSpec = None
        self.CoreResourceSpec = None
        self.TaskResourceSpec = None
        self.MasterCount = None
        self.CoreCount = None
        self.TaskCount = None
        self.CommonResourceSpec = None
        self.CommonCount = None


    def _deserialize(self, params):
        if params.get("MasterResourceSpec") is not None:
            self.MasterResourceSpec = Resource()
            self.MasterResourceSpec._deserialize(params.get("MasterResourceSpec"))
        if params.get("CoreResourceSpec") is not None:
            self.CoreResourceSpec = Resource()
            self.CoreResourceSpec._deserialize(params.get("CoreResourceSpec"))
        if params.get("TaskResourceSpec") is not None:
            self.TaskResourceSpec = Resource()
            self.TaskResourceSpec._deserialize(params.get("TaskResourceSpec"))
        self.MasterCount = params.get("MasterCount")
        self.CoreCount = params.get("CoreCount")
        self.TaskCount = params.get("TaskCount")
        if params.get("CommonResourceSpec") is not None:
            self.CommonResourceSpec = Resource()
            self.CommonResourceSpec._deserialize(params.get("CommonResourceSpec"))
        self.CommonCount = params.get("CommonCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeHardwareInfo(AbstractModel):
    """Node hardware information

    """

    def __init__(self):
        r"""
        :param AppId: User `APPID`
Note: this field may return null, indicating that no valid values can be obtained.
        :type AppId: int
        :param SerialNo: Serial number
Note: this field may return null, indicating that no valid values can be obtained.
        :type SerialNo: str
        :param OrderNo: Machine instance ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type OrderNo: str
        :param WanIp: Public IP bound to master node
Note: this field may return null, indicating that no valid values can be obtained.
        :type WanIp: str
        :param Flag: Node type. 0: common node; 1: master node;
2: core node; 3: task node
Note: this field may return null, indicating that no valid values can be obtained.
        :type Flag: int
        :param Spec: Node specification
Note: this field may return null, indicating that no valid values can be obtained.
        :type Spec: str
        :param CpuNum: Number of node cores
Note: this field may return null, indicating that no valid values can be obtained.
        :type CpuNum: int
        :param MemSize: Node memory size
Note: this field may return null, indicating that no valid values can be obtained.
        :type MemSize: int
        :param MemDesc: Node memory description
Note: this field may return null, indicating that no valid values can be obtained.
        :type MemDesc: str
        :param RegionId: Node region
Note: this field may return null, indicating that no valid values can be obtained.
        :type RegionId: int
        :param ZoneId: Node AZ
Note: this field may return null, indicating that no valid values can be obtained.
        :type ZoneId: int
        :param ApplyTime: Application time
Note: this field may return null, indicating that no valid values can be obtained.
        :type ApplyTime: str
        :param FreeTime: Release time
Note: this field may return null, indicating that no valid values can be obtained.
        :type FreeTime: str
        :param DiskSize: Disk size
Note: this field may return null, indicating that no valid values can be obtained.
        :type DiskSize: str
        :param NameTag: Node description
Note: this field may return null, indicating that no valid values can be obtained.
        :type NameTag: str
        :param Services: Services deployed on node
Note: this field may return null, indicating that no valid values can be obtained.
        :type Services: str
        :param StorageType: Disk type
Note: this field may return null, indicating that no valid values can be obtained.
        :type StorageType: int
        :param RootSize: System disk size
Note: this field may return null, indicating that no valid values can be obtained.
        :type RootSize: int
        :param ChargeType: Payment type
Note: this field may return null, indicating that no valid values can be obtained.
        :type ChargeType: int
        :param CdbIp: Database IP
Note: this field may return null, indicating that no valid values can be obtained.
        :type CdbIp: str
        :param CdbPort: Database port
Note: this field may return null, indicating that no valid values can be obtained.
        :type CdbPort: int
        :param HwDiskSize: Disk capacity
Note: this field may return null, indicating that no valid values can be obtained.
        :type HwDiskSize: int
        :param HwDiskSizeDesc: Disk capacity description
Note: this field may return null, indicating that no valid values can be obtained.
        :type HwDiskSizeDesc: str
        :param HwMemSize: Memory capacity
Note: this field may return null, indicating that no valid values can be obtained.
        :type HwMemSize: int
        :param HwMemSizeDesc: Memory capacity description
Note: this field may return null, indicating that no valid values can be obtained.
        :type HwMemSizeDesc: str
        :param ExpireTime: Expiration time
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param EmrResourceId: Node resource ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type EmrResourceId: str
        :param IsAutoRenew: Renewal flag
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsAutoRenew: int
        :param DeviceClass: Device flag
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeviceClass: str
        :param Mutable: Support for configuration adjustment
Note: this field may return null, indicating that no valid values can be obtained.
        :type Mutable: int
        :param MCMultiDisk: Multi-cloud disk
Note: this field may return null, indicating that no valid values can be obtained.
        :type MCMultiDisk: list of MultiDiskMC
        :param CdbNodeInfo: Database information
Note: this field may return null, indicating that no valid values can be obtained.
        :type CdbNodeInfo: :class:`tencentcloud.emr.v20190103.models.CdbInfo`
        :param Ip: Private IP
Note: this field may return null, indicating that no valid values can be obtained.
        :type Ip: str
        :param Destroyable: Whether this node can be terminated. 1: yes, 0: no
Note: this field may return null, indicating that no valid values can be obtained.
        :type Destroyable: int
        :param Tags: Tags bound to node
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param AutoFlag: Wether the node is auto-scaling. 0 means common node. 1 means auto-scaling node.
        :type AutoFlag: int
        :param HardwareResourceType: Resource type. Valid values: host, pod
Note: this field may return null, indicating that no valid values can be obtained.
        :type HardwareResourceType: str
        :param IsDynamicSpec: Whether floating specification is used. `1`: yes; `0`: no
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type IsDynamicSpec: int
        :param DynamicPodSpec: Floating specification in JSON string
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DynamicPodSpec: str
        :param SupportModifyPayMode: Whether to support billing mode change. `0`: no; `1`: yes
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SupportModifyPayMode: int
        :param RootStorageType: System disk type
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RootStorageType: int
        :param Zone: AZ information
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Zone: str
        :param SubnetInfo: Subnet
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SubnetInfo: :class:`tencentcloud.emr.v20190103.models.SubnetInfo`
        :param Clients: Client
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Clients: str
        """
        self.AppId = None
        self.SerialNo = None
        self.OrderNo = None
        self.WanIp = None
        self.Flag = None
        self.Spec = None
        self.CpuNum = None
        self.MemSize = None
        self.MemDesc = None
        self.RegionId = None
        self.ZoneId = None
        self.ApplyTime = None
        self.FreeTime = None
        self.DiskSize = None
        self.NameTag = None
        self.Services = None
        self.StorageType = None
        self.RootSize = None
        self.ChargeType = None
        self.CdbIp = None
        self.CdbPort = None
        self.HwDiskSize = None
        self.HwDiskSizeDesc = None
        self.HwMemSize = None
        self.HwMemSizeDesc = None
        self.ExpireTime = None
        self.EmrResourceId = None
        self.IsAutoRenew = None
        self.DeviceClass = None
        self.Mutable = None
        self.MCMultiDisk = None
        self.CdbNodeInfo = None
        self.Ip = None
        self.Destroyable = None
        self.Tags = None
        self.AutoFlag = None
        self.HardwareResourceType = None
        self.IsDynamicSpec = None
        self.DynamicPodSpec = None
        self.SupportModifyPayMode = None
        self.RootStorageType = None
        self.Zone = None
        self.SubnetInfo = None
        self.Clients = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.SerialNo = params.get("SerialNo")
        self.OrderNo = params.get("OrderNo")
        self.WanIp = params.get("WanIp")
        self.Flag = params.get("Flag")
        self.Spec = params.get("Spec")
        self.CpuNum = params.get("CpuNum")
        self.MemSize = params.get("MemSize")
        self.MemDesc = params.get("MemDesc")
        self.RegionId = params.get("RegionId")
        self.ZoneId = params.get("ZoneId")
        self.ApplyTime = params.get("ApplyTime")
        self.FreeTime = params.get("FreeTime")
        self.DiskSize = params.get("DiskSize")
        self.NameTag = params.get("NameTag")
        self.Services = params.get("Services")
        self.StorageType = params.get("StorageType")
        self.RootSize = params.get("RootSize")
        self.ChargeType = params.get("ChargeType")
        self.CdbIp = params.get("CdbIp")
        self.CdbPort = params.get("CdbPort")
        self.HwDiskSize = params.get("HwDiskSize")
        self.HwDiskSizeDesc = params.get("HwDiskSizeDesc")
        self.HwMemSize = params.get("HwMemSize")
        self.HwMemSizeDesc = params.get("HwMemSizeDesc")
        self.ExpireTime = params.get("ExpireTime")
        self.EmrResourceId = params.get("EmrResourceId")
        self.IsAutoRenew = params.get("IsAutoRenew")
        self.DeviceClass = params.get("DeviceClass")
        self.Mutable = params.get("Mutable")
        if params.get("MCMultiDisk") is not None:
            self.MCMultiDisk = []
            for item in params.get("MCMultiDisk"):
                obj = MultiDiskMC()
                obj._deserialize(item)
                self.MCMultiDisk.append(obj)
        if params.get("CdbNodeInfo") is not None:
            self.CdbNodeInfo = CdbInfo()
            self.CdbNodeInfo._deserialize(params.get("CdbNodeInfo"))
        self.Ip = params.get("Ip")
        self.Destroyable = params.get("Destroyable")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AutoFlag = params.get("AutoFlag")
        self.HardwareResourceType = params.get("HardwareResourceType")
        self.IsDynamicSpec = params.get("IsDynamicSpec")
        self.DynamicPodSpec = params.get("DynamicPodSpec")
        self.SupportModifyPayMode = params.get("SupportModifyPayMode")
        self.RootStorageType = params.get("RootStorageType")
        self.Zone = params.get("Zone")
        if params.get("SubnetInfo") is not None:
            self.SubnetInfo = SubnetInfo()
            self.SubnetInfo._deserialize(params.get("SubnetInfo"))
        self.Clients = params.get("Clients")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutterResource(AbstractModel):
    """Resource details

    """

    def __init__(self):
        r"""
        :param Spec: Specification
Note: this field may return null, indicating that no valid values can be obtained.
        :type Spec: str
        :param SpecName: Specification name
Note: this field may return null, indicating that no valid values can be obtained.
        :type SpecName: str
        :param StorageType: Disk type
Note: this field may return null, indicating that no valid values can be obtained.
        :type StorageType: int
        :param DiskType: Disk type
Note: this field may return null, indicating that no valid values can be obtained.
        :type DiskType: str
        :param RootSize: System disk size
Note: this field may return null, indicating that no valid values can be obtained.
        :type RootSize: int
        :param MemSize: Memory size
Note: this field may return null, indicating that no valid values can be obtained.
        :type MemSize: int
        :param Cpu: Number of CPUs
Note: this field may return null, indicating that no valid values can be obtained.
        :type Cpu: int
        :param DiskSize: Disk size
Note: this field may return null, indicating that no valid values can be obtained.
        :type DiskSize: int
        :param InstanceType: Specification
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceType: str
        """
        self.Spec = None
        self.SpecName = None
        self.StorageType = None
        self.DiskType = None
        self.RootSize = None
        self.MemSize = None
        self.Cpu = None
        self.DiskSize = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.Spec = params.get("Spec")
        self.SpecName = params.get("SpecName")
        self.StorageType = params.get("StorageType")
        self.DiskType = params.get("DiskType")
        self.RootSize = params.get("RootSize")
        self.MemSize = params.get("MemSize")
        self.Cpu = params.get("Cpu")
        self.DiskSize = params.get("DiskSize")
        self.InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Placement(AbstractModel):
    """Location information of cluster instance

    """

    def __init__(self):
        r"""
        :param ProjectId: ID of the project to which the instance belongs. This parameter can be obtained from the `projectId` field in the return value of the `DescribeProject` API. If 0 is entered, the default project will be used.
        :type ProjectId: int
        :param Zone: AZ where the instance resides, such as ap-guangzhou-1. You can call the `DescribeZones` API and see the `Zone` field to get the value of this parameter.
        :type Zone: str
        """
        self.ProjectId = None
        self.Zone = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PreExecuteFileSettings(AbstractModel):
    """Pre-execution script configuration

    """

    def __init__(self):
        r"""
        :param Path: COS path to script, which has been disused
        :type Path: str
        :param Args: Execution script parameter
        :type Args: list of str
        :param Bucket: COS bucket name, which has been disused
        :type Bucket: str
        :param Region: COS region name, which has been disused
        :type Region: str
        :param Domain: COS domain data, which has been disused
        :type Domain: str
        :param RunOrder: Execution sequence
        :type RunOrder: int
        :param WhenRun: `resourceAfter` or `clusterAfter`
        :type WhenRun: str
        :param CosFileName: Script name, which has been disused
        :type CosFileName: str
        :param CosFileURI: COS address of script
        :type CosFileURI: str
        :param CosSecretId: COS `SecretId`
        :type CosSecretId: str
        :param CosSecretKey: COS `SecretKey`
        :type CosSecretKey: str
        :param AppId: COS `appid`, which has been disused
        :type AppId: str
        """
        self.Path = None
        self.Args = None
        self.Bucket = None
        self.Region = None
        self.Domain = None
        self.RunOrder = None
        self.WhenRun = None
        self.CosFileName = None
        self.CosFileURI = None
        self.CosSecretId = None
        self.CosSecretKey = None
        self.AppId = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Args = params.get("Args")
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.Domain = params.get("Domain")
        self.RunOrder = params.get("RunOrder")
        self.WhenRun = params.get("WhenRun")
        self.CosFileName = params.get("CosFileName")
        self.CosFileURI = params.get("CosFileURI")
        self.CosSecretId = params.get("CosSecretId")
        self.CosSecretKey = params.get("CosSecretKey")
        self.AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Resource(AbstractModel):
    """Resource details

    """

    def __init__(self):
        r"""
        :param Spec: Node specification description, such as CVM.SA2
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Spec: str
        :param StorageType: Storage type
Valid values:
<li>4: SSD</li>
<li>5: Premium Cloud Storage</li>
<li>6: Enhanced SSD</li>
<li>11: High-Throughput cloud disk</li>
<li>12: Tremendous SSD</li>
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type StorageType: int
        :param DiskType: Disk type
Valid values:
<li>`CLOUD_SSD`: SSD</li>
<li>`CLOUD_PREMIUM`: Premium Cloud Storage</li>
<li>`CLOUD_BASIC`: HDD</li>
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DiskType: str
        :param MemSize: Memory capacity in MB
Note: this field may return null, indicating that no valid values can be obtained.
        :type MemSize: int
        :param Cpu: Number of CPU cores
Note: this field may return null, indicating that no valid values can be obtained.
        :type Cpu: int
        :param DiskSize: Data disk capacity
Note: this field may return null, indicating that no valid values can be obtained.
        :type DiskSize: int
        :param RootSize: System disk capacity
Note: this field may return null, indicating that no valid values can be obtained.
        :type RootSize: int
        :param MultiDisks: List of cloud disks. When the data disk is a cloud disk, `DiskType` and `DiskSize` are used directly; `MultiDisks` will be used for the excessive part
Note: this field may return null, indicating that no valid values can be obtained.
        :type MultiDisks: list of MultiDisk
        :param Tags: List of tags to be bound
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param InstanceType: Specification type, such as S2.MEDIUM8
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type InstanceType: str
        :param LocalDiskNum: Number of local disks. This field has been disused.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type LocalDiskNum: int
        :param DiskNum: Number of local disks, such as 2
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DiskNum: int
        """
        self.Spec = None
        self.StorageType = None
        self.DiskType = None
        self.MemSize = None
        self.Cpu = None
        self.DiskSize = None
        self.RootSize = None
        self.MultiDisks = None
        self.Tags = None
        self.InstanceType = None
        self.LocalDiskNum = None
        self.DiskNum = None


    def _deserialize(self, params):
        self.Spec = params.get("Spec")
        self.StorageType = params.get("StorageType")
        self.DiskType = params.get("DiskType")
        self.MemSize = params.get("MemSize")
        self.Cpu = params.get("Cpu")
        self.DiskSize = params.get("DiskSize")
        self.RootSize = params.get("RootSize")
        if params.get("MultiDisks") is not None:
            self.MultiDisks = []
            for item in params.get("MultiDisks"):
                obj = MultiDisk()
                obj._deserialize(item)
                self.MultiDisks.append(obj)
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.InstanceType = params.get("InstanceType")
        self.LocalDiskNum = params.get("LocalDiskNum")
        self.DiskNum = params.get("DiskNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchItem(AbstractModel):
    """Search field

    """

    def __init__(self):
        r"""
        :param SearchType: Searchable type
        :type SearchType: str
        :param SearchValue: Searchable value
        :type SearchValue: str
        """
        self.SearchType = None
        self.SearchValue = None


    def _deserialize(self, params):
        self.SearchType = params.get("SearchType")
        self.SearchValue = params.get("SearchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShortNodeInfo(AbstractModel):
    """Node information

    """

    def __init__(self):
        r"""
        :param NodeType: Node type: Master/Core/Task/Router/Common
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type NodeType: str
        :param NodeSize: Number of nodes
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type NodeSize: int
        """
        self.NodeType = None
        self.NodeSize = None


    def _deserialize(self, params):
        self.NodeType = params.get("NodeType")
        self.NodeSize = params.get("NodeSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubnetInfo(AbstractModel):
    """Subnet information

    """

    def __init__(self):
        r"""
        :param SubnetName: Subnet information (name)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SubnetName: str
        :param SubnetId: Subnet information (ID)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SubnetId: str
        """
        self.SubnetName = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.SubnetName = params.get("SubnetName")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Tag

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateTasksRequest(AbstractModel):
    """TerminateTasks request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param ResourceIds: List of resource IDs of the node to be terminated. The resource ID is in the format of `emr-vm-xxxxxxxx`. A valid resource ID can be queried in the [console](https://console.cloud.tencent.com/emr/static/hardware).
        :type ResourceIds: list of str
        """
        self.InstanceId = None
        self.ResourceIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ResourceIds = params.get("ResourceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateTasksResponse(AbstractModel):
    """TerminateTasks response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TopologyInfo(AbstractModel):
    """Cluster node topology information

    """

    def __init__(self):
        r"""
        :param ZoneId: AZ ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ZoneId: int
        :param Zone: AZ information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Zone: str
        :param SubnetInfoList: Subnet information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SubnetInfoList: list of SubnetInfo
        :param NodeInfoList: Node information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type NodeInfoList: list of ShortNodeInfo
        """
        self.ZoneId = None
        self.Zone = None
        self.SubnetInfoList = None
        self.NodeInfoList = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Zone = params.get("Zone")
        if params.get("SubnetInfoList") is not None:
            self.SubnetInfoList = []
            for item in params.get("SubnetInfoList"):
                obj = SubnetInfo()
                obj._deserialize(item)
                self.SubnetInfoList.append(obj)
        if params.get("NodeInfoList") is not None:
            self.NodeInfoList = []
            for item in params.get("NodeInfoList"):
                obj = ShortNodeInfo()
                obj._deserialize(item)
                self.NodeInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateInstanceSettings(AbstractModel):
    """Target resource specification

    """

    def __init__(self):
        r"""
        :param Memory: Memory capacity in GB
        :type Memory: int
        :param CPUCores: Number of CPU cores
        :type CPUCores: int
        :param ResourceId: Machine resource ID (EMR resource identifier)
        :type ResourceId: str
        :param InstanceType: Target machine specification
        :type InstanceType: str
        """
        self.Memory = None
        self.CPUCores = None
        self.ResourceId = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.Memory = params.get("Memory")
        self.CPUCores = params.get("CPUCores")
        self.ResourceId = params.get("ResourceId")
        self.InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfoForUserManager(AbstractModel):
    """Added user information list

    """

    def __init__(self):
        r"""
        :param UserName: Username
        :type UserName: str
        :param UserGroup: The group to which the user belongs
        :type UserGroup: str
        :param PassWord: 
        :type PassWord: str
        :param ReMark: 
        :type ReMark: str
        """
        self.UserName = None
        self.UserGroup = None
        self.PassWord = None
        self.ReMark = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.UserGroup = params.get("UserGroup")
        self.PassWord = params.get("PassWord")
        self.ReMark = params.get("ReMark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserManagerFilter(AbstractModel):
    """User management list filter

    """

    def __init__(self):
        r"""
        :param UserName: Username
Note: This field may return null, indicating that no valid value can be obtained.
        :type UserName: str
        """
        self.UserName = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserManagerUserBriefInfo(AbstractModel):
    """Brief user information in user management

    """

    def __init__(self):
        r"""
        :param UserName: Username
        :type UserName: str
        :param UserGroup: The group to which the user belongs
        :type UserGroup: str
        :param UserType: `Manager` represents an admin, and `NormalUser` represents a general user.
        :type UserType: str
        :param CreateTime: Account creation time
Note: This field may return null, indicating that no valid value can be obtained.
        :type CreateTime: str
        :param SupportDownLoadKeyTab: Whether the corresponding Keytab file of the user is available for download. This parameter applies only to a Kerberos-enabled cluster.
        :type SupportDownLoadKeyTab: bool
        :param DownLoadKeyTabUrl: Download link of the Keytab file
Note: This field may return null, indicating that no valid value can be obtained.
        :type DownLoadKeyTabUrl: str
        """
        self.UserName = None
        self.UserGroup = None
        self.UserType = None
        self.CreateTime = None
        self.SupportDownLoadKeyTab = None
        self.DownLoadKeyTabUrl = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.UserGroup = params.get("UserGroup")
        self.UserType = params.get("UserType")
        self.CreateTime = params.get("CreateTime")
        self.SupportDownLoadKeyTab = params.get("SupportDownLoadKeyTab")
        self.DownLoadKeyTabUrl = params.get("DownLoadKeyTabUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VPCSettings(AbstractModel):
    """VPC parameters

    """

    def __init__(self):
        r"""
        :param VpcId: VPC ID
        :type VpcId: str
        :param SubnetId: Subnet ID
        :type SubnetId: str
        """
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        