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


class COSSettings(AbstractModel):
    """COS-related configuration

    """

    def __init__(self):
        """
        :param CosSecretId: COS `SecretId`\n        :type CosSecretId: str\n        :param CosSecretKey: COS `SecrectKey`\n        :type CosSecretKey: str\n        :param LogOnCosPath: COS path to log\n        :type LogOnCosPath: str\n        """
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
        """
        :param InstanceName: Database instance
Note: this field may return null, indicating that no valid values can be obtained.\n        :type InstanceName: str\n        :param Ip: Database IP
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Ip: str\n        :param Port: Database port
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Port: int\n        :param MemSize: Database memory specification
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MemSize: int\n        :param Volume: Database disk specification
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Volume: int\n        :param Service: Service flag
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Service: str\n        :param ExpireTime: Expiration time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ExpireTime: str\n        :param ApplyTime: Application time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ApplyTime: str\n        :param PayType: Payment type
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PayType: int\n        :param ExpireFlag: Expiration flag
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ExpireFlag: bool\n        :param Status: Database status
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Status: int\n        :param IsAutoRenew: Renewal flag
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsAutoRenew: int\n        :param SerialNo: Database string
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SerialNo: str\n        :param ZoneId: ZoneId
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ZoneId: int\n        :param RegionId: RegionId
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RegionId: int\n        """
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
        


class ClusterInstancesInfo(AbstractModel):
    """Cluster instance information

    """

    def __init__(self):
        """
        :param Id: ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Id: int\n        :param ClusterId: Cluster ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ClusterId: str\n        :param Ftitle: Title
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Ftitle: str\n        :param ClusterName: Cluster name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ClusterName: str\n        :param RegionId: Region ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RegionId: int\n        :param ZoneId: Region ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ZoneId: int\n        :param AppId: User APPID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AppId: int\n        :param Uin: User UIN
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Uin: str\n        :param ProjectId: Project ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProjectId: int\n        :param VpcId: Cluster `VPCID`
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VpcId: int\n        :param SubnetId: Subnet ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SubnetId: int\n        :param Status: Instance status code. Value range:
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
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Status: int\n        :param AddTime: Creation time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AddTime: str\n        :param RunTime: Execution duration
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RunTime: str\n        :param Config: Cluster product configuration information
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Config: :class:`tencentcloud.emr.v20190103.models.EmrProductConfigOutter`\n        :param MasterIp: Public IP of master node
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MasterIp: str\n        :param EmrVersion: EMR version
Note: this field may return null, indicating that no valid values can be obtained.\n        :type EmrVersion: str\n        :param ChargeType: Billing mode
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ChargeType: int\n        :param TradeVersion: Transaction version
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TradeVersion: int\n        :param ResourceOrderId: Resource order ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ResourceOrderId: int\n        :param IsTradeCluster: Whether this is a paid cluster
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsTradeCluster: int\n        :param AlarmInfo: Alarm information for cluster error
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AlarmInfo: str\n        :param IsWoodpeckerCluster: Whether the new architecture is used
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsWoodpeckerCluster: int\n        :param MetaDb: Metadatabase information
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MetaDb: str\n        :param Tags: Tag information
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Tags: list of Tag\n        :param HiveMetaDb: Hive metadata
Note: this field may return null, indicating that no valid values can be obtained.\n        :type HiveMetaDb: str\n        :param ServiceClass: Cluster type: EMR, CLICKHOUSE, DRUID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServiceClass: str\n        :param AliasInfo: Alias serialization of all nodes in cluster
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AliasInfo: str\n        :param ProductId: Cluster version ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ProductId: int\n        :param Zone: Availability zone
Note: this field may return `null`, indicating that no valid value can be obtained.\n        :type Zone: str\n        """
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
<li>30: EMR v2.6.0</li>\n        :type ProductId: int\n        :param VPCSettings: Configuration information of VPC. This parameter is used to specify the VPC ID, subnet ID, etc.\n        :type VPCSettings: :class:`tencentcloud.emr.v20190103.models.VPCSettings`\n        :param Software: List of deployed components. The list of component options varies by EMR product ID (i.e., `ProductId`; for specific meanings, please see the `ProductId` input parameter). For more information, please see [Component Version](https://intl.cloud.tencent.com/document/product/589/20279?from_cn_redirect=1).
Enter an instance value: `hive` or `flink`.\n        :type Software: list of str\n        :param ResourceSpec: Node resource specification.\n        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.NewResourceSpec`\n        :param SupportHA: Whether to enable high node availability. Valid values:
<li>0: does not enable high availability of node.</li>
<li>1: enables high availability of node.</li>\n        :type SupportHA: int\n        :param InstanceName: Instance name.
<li>Length limit: 6-36 characters.</li>
<li>Only letters, numbers, dashes (-), and underscores (_) are supported.</li>\n        :type InstanceName: str\n        :param PayMode: Instance billing mode. Valid values:
<li>0: pay-as-you-go.</li>\n        :type PayMode: int\n        :param Placement: Instance location. This parameter is used to specify the AZ, project, and other attributes of the instance.\n        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`\n        :param TimeSpan: Purchase duration of instance, which needs to be used together with `TimeUnit`.
<li>When `TimeUnit` is `s`, this parameter can only be filled with 3600, indicating a pay-as-you-go instance.</li>
<li>When `TimeUnit` is `m`, the number entered in this parameter indicates the purchase duration of the monthly-subscription instance; for example, 1 means one month</li>\n        :type TimeSpan: int\n        :param TimeUnit: Time unit of instance purchase duration. Valid values:
<li>s: seconds. When `PayMode` is 0, `TimeUnit` can only be `s`.</li>
<li>m: month. When `PayMode` is 1, `TimeUnit` can only be `m`.</li>\n        :type TimeUnit: str\n        :param LoginSettings: Instance login settings. This parameter allows you to set the login password or key for your purchased node.
<li>If the key is set, the password will be only used for login to the native component WebUI.</li>
<li>If the key is not set, the password will be used for login to all purchased nodes and the native component WebUI.</li>\n        :type LoginSettings: :class:`tencentcloud.emr.v20190103.models.LoginSettings`\n        :param COSSettings: Parameter required for enabling COS access.\n        :type COSSettings: :class:`tencentcloud.emr.v20190103.models.COSSettings`\n        :param SgId: Security group to which an instance belongs in the format of `sg-xxxxxxxx`. This parameter can be obtained from the `SecurityGroupId` field in the return value of the [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808) API.\n        :type SgId: str\n        :param PreExecutedFileSettings: [Bootstrap action](https://intl.cloud.tencent.com/document/product/589/35656?from_cn_redirect=1) script settings\n        :type PreExecutedFileSettings: list of PreExecuteFileSettings\n        :param AutoRenew: Whether auto-renewal is enabled. Valid values:
<li>0: auto-renewal not enabled.</li>
<li>1: auto-renewal enabled.</li>\n        :type AutoRenew: int\n        :param ClientToken: Client token.\n        :type ClientToken: str\n        :param NeedMasterWan: Whether to enable public IP access for master node. Valid values:
<li>NEED_MASTER_WAN: enables public IP for master node.</li>
<li>NOT_NEED_MASTER_WAN: does not enable.</li>Public IP is enabled for master node by default.\n        :type NeedMasterWan: str\n        :param RemoteLoginAtCreate: Whether to enable remote public network login, i.e., port 22. When `SgId` is not empty, this parameter does not take effect.\n        :type RemoteLoginAtCreate: int\n        :param CheckSecurity: Whether to enable secure cluster. 0: no; other values: yes.\n        :type CheckSecurity: int\n        :param ExtendFsField: Accesses to external file system.\n        :type ExtendFsField: str\n        :param Tags: Tag description list. This parameter is used to bind a tag to a resource instance.\n        :type Tags: list of Tag\n        :param DisasterRecoverGroupIds: List of spread placement group IDs. Only one can be specified currently.
This parameter can be obtained in the `SecurityGroupId` field in the return value of the [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/product/213/15486?from_cn_redirect=1) API.\n        :type DisasterRecoverGroupIds: list of str\n        :param CbsEncrypt: CBS disk encryption at the cluster level. 0: not encrypted, 1: encrypted\n        :type CbsEncrypt: int\n        :param MetaType: Hive-shared metadatabase type. Valid values:
<li>EMR_DEFAULT_META: the cluster creates one by default.</li>
<li>EMR_EXIST_META: the cluster uses the specified EMR-MetaDB instance.</li>
<li>USER_CUSTOM_META: the cluster uses a custom MetaDB instance.</li>\n        :type MetaType: str\n        :param UnifyMetaInstanceId: EMR-MetaDB instance\n        :type UnifyMetaInstanceId: str\n        :param MetaDBInfo: Custom MetaDB instance information\n        :type MetaDBInfo: :class:`tencentcloud.emr.v20190103.models.CustomMetaInfo`\n        :param ApplicationRole: Custom application role.\n        :type ApplicationRole: str\n        """
        self.ProductId = None
        self.VPCSettings = None
        self.Software = None
        self.ResourceSpec = None
        self.SupportHA = None
        self.InstanceName = None
        self.PayMode = None
        self.Placement = None
        self.TimeSpan = None
        self.TimeUnit = None
        self.LoginSettings = None
        self.COSSettings = None
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


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        if params.get("VPCSettings") is not None:
            self.VPCSettings = VPCSettings()
            self.VPCSettings._deserialize(params.get("VPCSettings"))
        self.Software = params.get("Software")
        if params.get("ResourceSpec") is not None:
            self.ResourceSpec = NewResourceSpec()
            self.ResourceSpec._deserialize(params.get("ResourceSpec"))
        self.SupportHA = params.get("SupportHA")
        self.InstanceName = params.get("InstanceName")
        self.PayMode = params.get("PayMode")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnit = params.get("TimeUnit")
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        if params.get("COSSettings") is not None:
            self.COSSettings = COSSettings()
            self.COSSettings._deserialize(params.get("COSSettings"))
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
        :param InstanceId: Instance ID
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type InstanceId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class CustomMetaInfo(AbstractModel):
    """User-created Hive-MetaDB instance information

    """

    def __init__(self):
        """
        :param MetaDataJdbcUrl: JDBC connection to custom MetaDB instance beginning with `jdbc:mysql://`\n        :type MetaDataJdbcUrl: str\n        :param MetaDataUser: Custom MetaDB instance username\n        :type MetaDataUser: str\n        :param MetaDataPass: Custom MetaDB instance password\n        :type MetaDataPass: str\n        """
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
        


class DescribeClusterNodesRequest(AbstractModel):
    """DescribeClusterNodes request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Cluster instance ID in the format of emr-xxxxxxxx\n        :type InstanceId: str\n        :param NodeFlag: Node flag. Valid values:
<li>all: gets the information of nodes in all types except TencentDB information.</li>
<li>master: gets master node information.</li>
<li>core: gets core node information.</li>
<li>task: gets task node information.</li>
<li>common: gets common node information.</li>
<li>router: gets router node information.</li>
<li>db: gets TencentDB information in normal status.</li>
Note: only the above values are supported for the time being. Entering other values will cause errors.\n        :type NodeFlag: str\n        :param Offset: Page number. Default value: 0, indicating the first page.\n        :type Offset: int\n        :param Limit: Number of returned results per page. Default value: 100. Maximum value: 100\n        :type Limit: int\n        :param HardwareResourceType: Resource type. Valid values: all, host, pod. Default value: all\n        :type HardwareResourceType: str\n        :param SearchFields: Searchable field\n        :type SearchFields: list of SearchItem\n        """
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
        """
        :param TotalCnt: Total number of queried nodes\n        :type TotalCnt: int\n        :param NodeList: List of node details
Note: this field may return null, indicating that no valid values can be obtained.\n        :type NodeList: list of NodeHardwareInfo\n        :param TagKeys: List of tag keys owned by user
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TagKeys: list of str\n        :param HardwareResourceTypeList: Resource type list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type HardwareResourceTypeList: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances request structure.

    """

    def __init__(self):
        """
        :param DisplayStrategy: Cluster filtering policy. Valid values:
<li>clusterList: queries the list of clusters except terminated ones.</li>
<li>monitorManage: queries the list of clusters except those that have been terminated, are being created, or failed to be created.</li>
<li>cloudHardwareManage/componentManage: reserved fields with the same meaning as `monitorManage`.</li>\n        :type DisplayStrategy: str\n        :param InstanceIds: Queries by one or more instance IDs in the format of `emr-xxxxxxxx`. For the format of this parameter, please see the `id.N` section in [API Overview](https://intl.cloud.tencent.com/document/api/213/15688). If no instance ID is entered, the list of all instances under this `APPID` will be returned.\n        :type InstanceIds: list of str\n        :param Offset: Page number. Default value: 0, indicating the first page.\n        :type Offset: int\n        :param Limit: Number of returned results per page. Default value: 10. Maximum value: 100\n        :type Limit: int\n        :param ProjectId: ID of the project to which the instance belongs. This parameter can be obtained from the `projectId` field in the return value of the `DescribeProject` API. If this value is -1, the list of all instances will be returned.\n        :type ProjectId: int\n        :param OrderField: Sorting field. Valid values:
<li>clusterId: sorts by cluster ID.</li>
<li>addTime: sorts by instance creation time.</li>
<li>status: sorts by instance status code.</li>\n        :type OrderField: str\n        :param Asc: Sorts according to `OrderField` in ascending or descending order. Valid values:
<li>0: descending order.</li>
<li>1: ascending order.</li>Default value: 0.\n        :type Asc: int\n        """
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
        """
        :param TotalCnt: Number of eligible instances.\n        :type TotalCnt: int\n        :param ClusterList: List of EMR instance details.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ClusterList: list of ClusterInstancesInfo\n        :param TagKeys: List of tag keys associated to an instance.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TagKeys: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DynamicPodSpec(AbstractModel):
    """Pod floating specification

    """

    def __init__(self):
        """
        :param RequestCpu: Minimum number of CPU cores\n        :type RequestCpu: float\n        :param LimitCpu: Maximum number of CPU cores\n        :type LimitCpu: float\n        :param RequestMemory: Minimum memory in MB\n        :type RequestMemory: float\n        :param LimitMemory: Maximum memory in MB\n        :type LimitMemory: float\n        """
        self.RequestCpu = None
        self.LimitCpu = None
        self.RequestMemory = None
        self.LimitMemory = None


    def _deserialize(self, params):
        self.RequestCpu = params.get("RequestCpu")
        self.LimitCpu = params.get("LimitCpu")
        self.RequestMemory = params.get("RequestMemory")
        self.LimitMemory = params.get("LimitMemory")
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
        """
        :param SoftInfo: Software information
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SoftInfo: list of str\n        :param MasterNodeSize: Number of master nodes
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MasterNodeSize: int\n        :param CoreNodeSize: Number of core nodes
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CoreNodeSize: int\n        :param TaskNodeSize: Number of task nodes
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TaskNodeSize: int\n        :param ComNodeSize: Number of common nodes
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ComNodeSize: int\n        :param MasterResource: Master node resource
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MasterResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`\n        :param CoreResource: Core node resource
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CoreResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`\n        :param TaskResource: Task node resource
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TaskResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`\n        :param ComResource: Common node resource
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ComResource: :class:`tencentcloud.emr.v20190103.models.OutterResource`\n        :param OnCos: Whether COS is used
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OnCos: bool\n        :param ChargeType: Billing mode
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ChargeType: int\n        :param RouterNodeSize: Number of router nodes
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RouterNodeSize: int\n        :param SupportHA: Whether HA is supported
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SupportHA: bool\n        :param SecurityOn: Whether secure mode is supported
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SecurityOn: bool\n        :param SecurityGroup: Security group name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SecurityGroup: str\n        :param CbsEncrypt: Whether to enable CBS encryption
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CbsEncrypt: int\n        :param ApplicationRole: Custom application role
Note: this field may return `null`, indicating that no valid value can be obtained.\n        :type ApplicationRole: str\n        :param SecurityGroups: Security groups
Note: this field may return `null`, indicating that no valid value can be obtained.\n        :type SecurityGroups: list of str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostVolumeContext(AbstractModel):
    """Pod `HostPath` mounting method description

    """

    def __init__(self):
        """
        :param VolumePath: Directory in the pod for mounting the host, which is the mount point of resources for the host. The specified mount point corresponds to the host path and is used as the data storage directory in the pod.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VolumePath: str\n        """
        self.VolumePath = None


    def _deserialize(self, params):
        self.VolumePath = params.get("VolumePath")
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
        """
        :param TimeUnit: Time unit of instance purchase duration. Valid values:
<li>s: seconds. When `PayMode` is 0, `TimeUnit` can only be `s`.</li>\n        :type TimeUnit: str\n        :param TimeSpan: Purchase duration of instance, which needs to be used together with `TimeUnit`.
<li>When `TimeUnit` is `s`, this parameter can only be filled with 3600, indicating a pay-as-you-go instance.</li>
<li>When `TimeUnit` is `m`, the number entered in this parameter indicates the purchase duration of the monthly-subscription instance; for example, 1 means one month</li>\n        :type TimeSpan: int\n        :param ResourceSpec: Node specification queried for price.\n        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.NewResourceSpec`\n        :param Currency: Currency.\n        :type Currency: str\n        :param PayMode: Instance billing mode. Valid values:
<li>0: pay-as-you-go.</li>\n        :type PayMode: int\n        :param SupportHA: Whether to enable high availability of node. Valid values:
<li>0: does not enable high availability of node.</li>
<li>1: enables high availability of node.</li>\n        :type SupportHA: int\n        :param Software: List of deployed components. Different required components need to be selected for different EMR product IDs (i.e., `ProductId`; for specific meanings, please see the `ProductId` field in the input parameter):
<li>When `ProductId` is 1, the required components include hadoop-2.7.3, knox-1.2.0, and zookeeper-3.4.9</li>
<li>When `ProductId` is 2, the required components include hadoop-2.7.3, knox-1.2.0, and zookeeper-3.4.9</li>
<li>When `ProductId` is 4, the required components include hadoop-2.8.4, knox-1.2.0, and zookeeper-3.4.9</li>
<li>When `ProductId` is 7, the required components include hadoop-3.1.2, knox-1.2.0, and zookeeper-3.4.9</li>\n        :type Software: list of str\n        :param Placement: Instance location. This parameter is used to specify the AZ, project, and other attributes of the instance.\n        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`\n        :param VPCSettings: Configuration information of VPC. This parameter is used to specify the VPC ID, subnet ID, etc.\n        :type VPCSettings: :class:`tencentcloud.emr.v20190103.models.VPCSettings`\n        :param MetaType: Hive-shared metadatabase type. Valid values:
<li>EMR_DEFAULT_META: the cluster creates one by default.</li>
<li>EMR_EXIST_META: the cluster uses the specified EMR-MetaDB instance.</li>
<li>USER_CUSTOM_META: the cluster uses a custom MetaDB instance.</li>\n        :type MetaType: str\n        :param UnifyMetaInstanceId: EMR-MetaDB instance\n        :type UnifyMetaInstanceId: str\n        :param MetaDBInfo: Custom MetaDB instance information\n        :type MetaDBInfo: :class:`tencentcloud.emr.v20190103.models.CustomMetaInfo`\n        :param ProductId: Product ID. Different product IDs represent different EMR product versions. Valid values:
<li>1: EMR v1.3.1.</li>
<li>2: EMR v2.0.1.</li>
<li>4: EMR v2.1.0.</li>
<li>7: EMR v3.0.0.</li>\n        :type ProductId: int\n        """
        self.TimeUnit = None
        self.TimeSpan = None
        self.ResourceSpec = None
        self.Currency = None
        self.PayMode = None
        self.SupportHA = None
        self.Software = None
        self.Placement = None
        self.VPCSettings = None
        self.MetaType = None
        self.UnifyMetaInstanceId = None
        self.MetaDBInfo = None
        self.ProductId = None


    def _deserialize(self, params):
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        if params.get("ResourceSpec") is not None:
            self.ResourceSpec = NewResourceSpec()
            self.ResourceSpec._deserialize(params.get("ResourceSpec"))
        self.Currency = params.get("Currency")
        self.PayMode = params.get("PayMode")
        self.SupportHA = params.get("SupportHA")
        self.Software = params.get("Software")
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
        """
        :param OriginalCost: Original price.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OriginalCost: float\n        :param DiscountCost: Discounted price.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DiscountCost: float\n        :param TimeUnit: Time unit of instance purchase duration. Valid values:
<li>s: seconds.</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TimeUnit: str\n        :param TimeSpan: Purchase duration of instance.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TimeSpan: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param TimeSpan: How long the instance will be renewed for, which needs to be used together with `TimeUnit`.\n        :type TimeSpan: int\n        :param ResourceIds: List of resource IDs of the node to be renewed. The resource ID is in the format of `emr-vm-xxxxxxxx`. A valid resource ID can be queried in the [console](https://console.cloud.tencent.com/emr/static/hardware).\n        :type ResourceIds: list of str\n        :param Placement: Location of the instance. This parameter is used to specify the AZ, project, and other attributes of the instance.\n        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`\n        :param PayMode: Instance billing mode.\n        :type PayMode: int\n        :param TimeUnit: Unit of time for instance renewal.\n        :type TimeUnit: str\n        :param Currency: Currency.\n        :type Currency: str\n        :param ModifyPayMode: Whether to change from pay-as-you-go billing to monthly subscription billing. `0`: no; `1`: yes\n        :type ModifyPayMode: int\n        """
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
        """
        :param OriginalCost: Original price.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OriginalCost: float\n        :param DiscountCost: Discounted price.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DiscountCost: float\n        :param TimeUnit: Unit of time for instance renewal.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TimeUnit: str\n        :param TimeSpan: How long the instance will be renewed for.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TimeSpan: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class InquiryPriceScaleOutInstanceRequest(AbstractModel):
    """InquiryPriceScaleOutInstance request structure.

    """

    def __init__(self):
        """
        :param TimeUnit: Time unit of scale-out. Valid values:
<li>s: seconds. When `PayMode` is 0, `TimeUnit` can only be `s`.</li>\n        :type TimeUnit: str\n        :param TimeSpan: Duration of scale-out, which needs to be used together with `TimeUnit`.
<li>When `PayMode` is 0, `TimeSpan` can only be 3,600.</li>\n        :type TimeSpan: int\n        :param ZoneId: ID of the AZ where an instance resides.\n        :type ZoneId: int\n        :param PayMode: Instance billing mode. Valid values:
<li>0: pay-as-you-go.</li>\n        :type PayMode: int\n        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param CoreCount: Number of core nodes added.\n        :type CoreCount: int\n        :param TaskCount: Number of task nodes added.\n        :type TaskCount: int\n        :param Currency: Currency.\n        :type Currency: str\n        :param RouterCount: Number of router nodes added.\n        :type RouterCount: int\n        :param MasterCount: Number of master nodes to add\n        :type MasterCount: int\n        """
        self.TimeUnit = None
        self.TimeSpan = None
        self.ZoneId = None
        self.PayMode = None
        self.InstanceId = None
        self.CoreCount = None
        self.TaskCount = None
        self.Currency = None
        self.RouterCount = None
        self.MasterCount = None


    def _deserialize(self, params):
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.ZoneId = params.get("ZoneId")
        self.PayMode = params.get("PayMode")
        self.InstanceId = params.get("InstanceId")
        self.CoreCount = params.get("CoreCount")
        self.TaskCount = params.get("TaskCount")
        self.Currency = params.get("Currency")
        self.RouterCount = params.get("RouterCount")
        self.MasterCount = params.get("MasterCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceScaleOutInstanceResponse(AbstractModel):
    """InquiryPriceScaleOutInstance response structure.

    """

    def __init__(self):
        """
        :param OriginalCost: Original price.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OriginalCost: str\n        :param DiscountCost: Discounted price.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DiscountCost: str\n        :param Unit: Time unit of scale-out. Valid values:
<li>s: seconds.</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Unit: str\n        :param PriceSpec: Node specification queried for price.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PriceSpec: :class:`tencentcloud.emr.v20190103.models.PriceResource`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.OriginalCost = None
        self.DiscountCost = None
        self.Unit = None
        self.PriceSpec = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalCost = params.get("OriginalCost")
        self.DiscountCost = params.get("DiscountCost")
        self.Unit = params.get("Unit")
        if params.get("PriceSpec") is not None:
            self.PriceSpec = PriceResource()
            self.PriceSpec._deserialize(params.get("PriceSpec"))
        self.RequestId = params.get("RequestId")


class InquiryPriceUpdateInstanceRequest(AbstractModel):
    """InquiryPriceUpdateInstance request structure.

    """

    def __init__(self):
        """
        :param TimeUnit: Time unit of scaling. Valid values:
<li>s: seconds. When `PayMode` is 0, `TimeUnit` can only be `s`.</li>\n        :type TimeUnit: str\n        :param TimeSpan: Duration of scaling, which needs to be used together with `TimeUnit`.
<li>When `PayMode` is 0, `TimeSpan` can only be 3,600.</li>\n        :type TimeSpan: int\n        :param UpdateSpec: Target node specification.\n        :type UpdateSpec: :class:`tencentcloud.emr.v20190103.models.UpdateInstanceSettings`\n        :param PayMode: Instance billing mode. Valid values:
<li>0: pay-as-you-go.</li>\n        :type PayMode: int\n        :param Placement: Instance location. This parameter is used to specify the AZ, project, and other attributes of the instance.\n        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`\n        :param Currency: Currency.\n        :type Currency: str\n        """
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
        """
        :param OriginalCost: Original price.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OriginalCost: float\n        :param DiscountCost: Discounted price.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DiscountCost: float\n        :param TimeUnit: Time unit of scaling. Valid values:
<li>s: seconds.</li>
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TimeUnit: str\n        :param TimeSpan: Duration of scaling.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TimeSpan: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param Password: Password\n        :type Password: str\n        :param PublicKeyId: Public Key\n        :type PublicKeyId: str\n        """
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
        


class MultiDisk(AbstractModel):
    """Multi-cloud disk parameters

    """

    def __init__(self):
        """
        :param DiskType: Cloud disk type
<li>`CLOUD_SSD`: SSD</li>
<li>`CLOUD_PREMIUM`: Premium Cloud Storage</li>
<li>`CLOUD_HSSD`: Enhanced SSD</li>\n        :type DiskType: str\n        :param Volume: Cloud disk size\n        :type Volume: int\n        :param Count: Number of cloud disks of this type\n        :type Count: int\n        """
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
        """
        :param Count: Number of cloud disks in this type
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Count: int\n        :param Type: Disk type
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Type: int\n        :param Volume: Cloud disk size
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Volume: int\n        """
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
        


class NewResourceSpec(AbstractModel):
    """Resource description

    """

    def __init__(self):
        """
        :param MasterResourceSpec: Describes master node resource\n        :type MasterResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`\n        :param CoreResourceSpec: Describes core node resource\n        :type CoreResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`\n        :param TaskResourceSpec: Describes task node resource\n        :type TaskResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`\n        :param MasterCount: Number of master nodes\n        :type MasterCount: int\n        :param CoreCount: Number of core nodes\n        :type CoreCount: int\n        :param TaskCount: Number of task nodes\n        :type TaskCount: int\n        :param CommonResourceSpec: Describes common node resource\n        :type CommonResourceSpec: :class:`tencentcloud.emr.v20190103.models.Resource`\n        :param CommonCount: Number of common nodes\n        :type CommonCount: int\n        """
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
        """
        :param AppId: User `APPID`
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AppId: int\n        :param SerialNo: Serial number
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SerialNo: str\n        :param OrderNo: Machine instance ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OrderNo: str\n        :param WanIp: Public IP bound to master node
Note: this field may return null, indicating that no valid values can be obtained.\n        :type WanIp: str\n        :param Flag: Node type. 0: common node; 1: master node;
2: core node; 3: task node
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Flag: int\n        :param Spec: Node specification
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Spec: str\n        :param CpuNum: Number of node cores
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CpuNum: int\n        :param MemSize: Node memory size
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MemSize: int\n        :param MemDesc: Node memory description
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MemDesc: str\n        :param RegionId: Node region
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RegionId: int\n        :param ZoneId: Node AZ
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ZoneId: int\n        :param ApplyTime: Application time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ApplyTime: str\n        :param FreeTime: Release time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FreeTime: str\n        :param DiskSize: Disk size
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DiskSize: str\n        :param NameTag: Node description
Note: this field may return null, indicating that no valid values can be obtained.\n        :type NameTag: str\n        :param Services: Services deployed on node
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Services: str\n        :param StorageType: Disk type
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StorageType: int\n        :param RootSize: System disk size
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RootSize: int\n        :param ChargeType: Payment type
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ChargeType: int\n        :param CdbIp: Database IP
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CdbIp: str\n        :param CdbPort: Database port
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CdbPort: int\n        :param HwDiskSize: Disk capacity
Note: this field may return null, indicating that no valid values can be obtained.\n        :type HwDiskSize: int\n        :param HwDiskSizeDesc: Disk capacity description
Note: this field may return null, indicating that no valid values can be obtained.\n        :type HwDiskSizeDesc: str\n        :param HwMemSize: Memory capacity
Note: this field may return null, indicating that no valid values can be obtained.\n        :type HwMemSize: int\n        :param HwMemSizeDesc: Memory capacity description
Note: this field may return null, indicating that no valid values can be obtained.\n        :type HwMemSizeDesc: str\n        :param ExpireTime: Expiration time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ExpireTime: str\n        :param EmrResourceId: Node resource ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type EmrResourceId: str\n        :param IsAutoRenew: Renewal flag
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsAutoRenew: int\n        :param DeviceClass: Device flag
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DeviceClass: str\n        :param Mutable: Support for configuration adjustment
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Mutable: int\n        :param MCMultiDisk: Multi-cloud disk
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MCMultiDisk: list of MultiDiskMC\n        :param CdbNodeInfo: Database information
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CdbNodeInfo: :class:`tencentcloud.emr.v20190103.models.CdbInfo`\n        :param Ip: Private IP
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Ip: str\n        :param Destroyable: Whether this node can be terminated. 1: yes, 0: no
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Destroyable: int\n        :param Tags: Tags bound to node
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Tags: list of Tag\n        :param AutoFlag: Wether the node is auto-scaling. 0 means common node. 1 means auto-scaling node.\n        :type AutoFlag: int\n        :param HardwareResourceType: Resource type. Valid values: host, pod
Note: this field may return null, indicating that no valid values can be obtained.\n        :type HardwareResourceType: str\n        :param IsDynamicSpec: Whether floating specification is used. `1`: yes; `0`: no
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type IsDynamicSpec: int\n        :param DynamicPodSpec: Floating specification in JSON string
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type DynamicPodSpec: str\n        :param SupportModifyPayMode: Whether to support billing mode change. `0`: no; `1`: yes
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type SupportModifyPayMode: int\n        """
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
        """
        :param Spec: Specification
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Spec: str\n        :param SpecName: Specification name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SpecName: str\n        :param StorageType: Disk type
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StorageType: int\n        :param DiskType: Disk type
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DiskType: str\n        :param RootSize: System disk size
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RootSize: int\n        :param MemSize: Memory size
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MemSize: int\n        :param Cpu: Number of CPUs
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Cpu: int\n        :param DiskSize: Disk size
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DiskSize: int\n        :param InstanceType: Specification
Note: this field may return null, indicating that no valid values can be obtained.\n        :type InstanceType: str\n        """
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
        


class PersistentVolumeContext(AbstractModel):
    """Pod `PVC` storage method description

    """

    def __init__(self):
        """
        :param DiskSize: Disk size in GB
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DiskSize: int\n        :param DiskType: Disk type. Valid values: CLOUD_PREMIUM, CLOUD_SSD
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DiskType: str\n        :param DiskNum: Number of disks
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DiskNum: int\n        """
        self.DiskSize = None
        self.DiskType = None
        self.DiskNum = None


    def _deserialize(self, params):
        self.DiskSize = params.get("DiskSize")
        self.DiskType = params.get("DiskType")
        self.DiskNum = params.get("DiskNum")
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
        """
        :param ProjectId: ID of the project to which the instance belongs. This parameter can be obtained from the `projectId` field in the return value of the `DescribeProject` API. If 0 is entered, the default project will be used.\n        :type ProjectId: int\n        :param Zone: AZ where the instance resides, such as ap-guangzhou-1. You can call the `DescribeZones` API and see the `Zone` field to get the value of this parameter.\n        :type Zone: str\n        """
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
        


class PodParameter(AbstractModel):
    """Custom pod permission and parameter

    """

    def __init__(self):
        """
        :param ClusterId: TKE or EKS cluster ID\n        :type ClusterId: str\n        :param Config: Custom permission
Example:
{
  "apiVersion": "v1",
  "clusters": [
    {
      "cluster": {
        "certificate-authority-data": "xxxxxx==",
        "server": "https://xxxxx.com"
      },
      "name": "cls-xxxxx"
    }
  ],
  "contexts": [
    {
      "context": {
        "cluster": "cls-xxxxx",
        "user": "100014xxxxx"
      },
      "name": "cls-a44yhcxxxxxxxxxx"
    }
  ],
  "current-context": "cls-a4xxxx-context-default",
  "kind": "Config",
  "preferences": {},
  "users": [
    {
      "name": "100014xxxxx",
      "user": {
        "client-certificate-data": "xxxxxx",
        "client-key-data": "xxxxxx"
      }
    }
  ]
}\n        :type Config: str\n        :param Parameter: Custom parameter
Example:
{
    "apiVersion": "apps/v1",
    "kind": "Deployment",
    "metadata": {
      "name": "test-deployment",
      "labels": {
        "app": "test"
      }
    },
    "spec": {
      "replicas": 3,
      "selector": {
        "matchLabels": {
          "app": "test-app"
        }
      },
      "template": {
        "metadata": {
          "annotations": {
            "your-organization.com/department-v1": "test-example-v1",
            "your-organization.com/department-v2": "test-example-v2"
          },
          "labels": {
            "app": "test-app",
            "environment": "production"
          }
        },
        "spec": {
          "nodeSelector": {
            "your-organization/node-test": "test-node"
          },
          "containers": [
            {
              "name": "nginx",
              "image": "nginx:1.14.2",
              "ports": [
                {
                  "containerPort": 80
                }
              ]
            }
          ],
          "affinity": {
            "nodeAffinity": {
              "requiredDuringSchedulingIgnoredDuringExecution": {
                "nodeSelectorTerms": [
                  {
                    "matchExpressions": [
                      {
                        "key": "disk-type",
                        "operator": "In",
                        "values": [
                          "ssd",
                          "sas"
                        ]
                      },
                      {
                        "key": "cpu-num",
                        "operator": "Gt",
                        "values": [
                          "6"
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          }
        }
      }
    }
  }\n        :type Parameter: str\n        """
        self.ClusterId = None
        self.Config = None
        self.Parameter = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Config = params.get("Config")
        self.Parameter = params.get("Parameter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodSpec(AbstractModel):
    """Resource description for container resource expansion

    """

    def __init__(self):
        """
        :param ResourceProviderIdentifier: Identifier of external resource provider, such as "cls-a1cd23fa".\n        :type ResourceProviderIdentifier: str\n        :param ResourceProviderType: Type of external resource provider, such as "tke". Currently, only "tke" is supported.\n        :type ResourceProviderType: str\n        :param NodeType: Purpose of the resource, i.e., node type, which currently can only be "TASK".\n        :type NodeType: str\n        :param Cpu: Number of CPU cores.\n        :type Cpu: int\n        :param Memory: Memory size in GB.\n        :type Memory: int\n        :param DataVolumes: Mount point of resources for the host. The specified mount point corresponds to the host path and is used as the data storage directory in the pod. (This parameter has been disused)\n        :type DataVolumes: list of str\n        :param CpuType: EKS cluster - CPU type. Valid values: "intel", "amd"\n        :type CpuType: str\n        :param PodVolumes: Pod node data directory mounting information.\n        :type PodVolumes: list of PodVolume\n        :param IsDynamicSpec: Whether floating specification is used. `1`: yes; `0`: no\n        :type IsDynamicSpec: int\n        :param DynamicPodSpec: Floating specification
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type DynamicPodSpec: :class:`tencentcloud.emr.v20190103.models.DynamicPodSpec`\n        :param VpcId: Unique VPC ID
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type VpcId: str\n        :param SubnetId: Unique VPC subnet ID
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type SubnetId: str\n        """
        self.ResourceProviderIdentifier = None
        self.ResourceProviderType = None
        self.NodeType = None
        self.Cpu = None
        self.Memory = None
        self.DataVolumes = None
        self.CpuType = None
        self.PodVolumes = None
        self.IsDynamicSpec = None
        self.DynamicPodSpec = None
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.ResourceProviderIdentifier = params.get("ResourceProviderIdentifier")
        self.ResourceProviderType = params.get("ResourceProviderType")
        self.NodeType = params.get("NodeType")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.DataVolumes = params.get("DataVolumes")
        self.CpuType = params.get("CpuType")
        if params.get("PodVolumes") is not None:
            self.PodVolumes = []
            for item in params.get("PodVolumes"):
                obj = PodVolume()
                obj._deserialize(item)
                self.PodVolumes.append(obj)
        self.IsDynamicSpec = params.get("IsDynamicSpec")
        if params.get("DynamicPodSpec") is not None:
            self.DynamicPodSpec = DynamicPodSpec()
            self.DynamicPodSpec._deserialize(params.get("DynamicPodSpec"))
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodVolume(AbstractModel):
    """Pod storage device description.

    """

    def __init__(self):
        """
        :param VolumeType: Storage type. Valid values: "pvc", "hostpath".
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VolumeType: str\n        :param PVCVolume: This field will take effect if `VolumeType` is `pvc`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PVCVolume: :class:`tencentcloud.emr.v20190103.models.PersistentVolumeContext`\n        :param HostVolume: This field will take effect if `VolumeType` is `hostpath`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type HostVolume: :class:`tencentcloud.emr.v20190103.models.HostVolumeContext`\n        """
        self.VolumeType = None
        self.PVCVolume = None
        self.HostVolume = None


    def _deserialize(self, params):
        self.VolumeType = params.get("VolumeType")
        if params.get("PVCVolume") is not None:
            self.PVCVolume = PersistentVolumeContext()
            self.PVCVolume._deserialize(params.get("PVCVolume"))
        if params.get("HostVolume") is not None:
            self.HostVolume = HostVolumeContext()
            self.HostVolume._deserialize(params.get("HostVolume"))
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
        """
        :param Path: COS path to script, which has been disused\n        :type Path: str\n        :param Args: Execution script parameter\n        :type Args: list of str\n        :param Bucket: COS bucket name, which has been disused\n        :type Bucket: str\n        :param Region: COS region name, which has been disused\n        :type Region: str\n        :param Domain: COS domain data, which has been disused\n        :type Domain: str\n        :param RunOrder: Execution sequence\n        :type RunOrder: int\n        :param WhenRun: `resourceAfter` or `clusterAfter`\n        :type WhenRun: str\n        :param CosFileName: Script name, which has been disused\n        :type CosFileName: str\n        :param CosFileURI: COS address of script\n        :type CosFileURI: str\n        :param CosSecretId: COS `SecretId`\n        :type CosSecretId: str\n        :param CosSecretKey: COS `SecretKey`\n        :type CosSecretKey: str\n        :param AppId: COS `appid`, which has been disused\n        :type AppId: str\n        """
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
        


class PriceResource(AbstractModel):
    """Resource queried for price

    """

    def __init__(self):
        """
        :param Spec: Target specification
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Spec: str\n        :param StorageType: Disk type
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StorageType: int\n        :param DiskType: Disk type
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DiskType: str\n        :param RootSize: System disk size
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RootSize: int\n        :param MemSize: Memory size
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MemSize: int\n        :param Cpu: Number of cores
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Cpu: int\n        :param DiskSize: Disk size
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DiskSize: int\n        :param MultiDisks: List of cloud disks
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MultiDisks: list of MultiDisk\n        :param DiskCnt: Number of disks
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DiskCnt: int\n        :param InstanceType: Specification
Note: this field may return null, indicating that no valid values can be obtained.\n        :type InstanceType: str\n        :param Tags: Tag
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Tags: list of Tag\n        :param DiskNum: Number of disks
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DiskNum: int\n        :param LocalDiskNum: Number of local disks
Note: this field may return null, indicating that no valid values can be obtained.\n        :type LocalDiskNum: int\n        """
        self.Spec = None
        self.StorageType = None
        self.DiskType = None
        self.RootSize = None
        self.MemSize = None
        self.Cpu = None
        self.DiskSize = None
        self.MultiDisks = None
        self.DiskCnt = None
        self.InstanceType = None
        self.Tags = None
        self.DiskNum = None
        self.LocalDiskNum = None


    def _deserialize(self, params):
        self.Spec = params.get("Spec")
        self.StorageType = params.get("StorageType")
        self.DiskType = params.get("DiskType")
        self.RootSize = params.get("RootSize")
        self.MemSize = params.get("MemSize")
        self.Cpu = params.get("Cpu")
        self.DiskSize = params.get("DiskSize")
        if params.get("MultiDisks") is not None:
            self.MultiDisks = []
            for item in params.get("MultiDisks"):
                obj = MultiDisk()
                obj._deserialize(item)
                self.MultiDisks.append(obj)
        self.DiskCnt = params.get("DiskCnt")
        self.InstanceType = params.get("InstanceType")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.DiskNum = params.get("DiskNum")
        self.LocalDiskNum = params.get("LocalDiskNum")
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
        """
        :param Spec: Node specification description, such as CVM.SA2
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type Spec: str\n        :param StorageType: Storage type
Valid values:
<li>4: SSD</li>
<li>5: Premium Cloud Storage</li>
<li>6: Enhanced SSD</li>
<li>11: High-Throughput cloud disk</li>
<li>12: Tremendous SSD</li>
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type StorageType: int\n        :param DiskType: Disk type
Valid values:
<li>`CLOUD_SSD`: SSD</li>
<li>`CLOUD_PREMIUM`: Premium Cloud Storage</li>
<li>`CLOUD_BASIC`: HDD</li>
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type DiskType: str\n        :param MemSize: Memory capacity in MB
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MemSize: int\n        :param Cpu: Number of CPU cores
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Cpu: int\n        :param DiskSize: Data disk capacity
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DiskSize: int\n        :param RootSize: System disk capacity
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RootSize: int\n        :param MultiDisks: List of cloud disks. When the data disk is a cloud disk, `DiskType` and `DiskSize` are used directly; `MultiDisks` will be used for the excessive part
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MultiDisks: list of MultiDisk\n        :param Tags: List of tags to be bound
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Tags: list of Tag\n        :param InstanceType: Specification type, such as S2.MEDIUM8
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type InstanceType: str\n        :param LocalDiskNum: Number of local disks. This field has been disused.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type LocalDiskNum: int\n        :param DiskNum: Number of local disks, such as 2
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type DiskNum: int\n        """
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
        


class ScaleOutInstanceRequest(AbstractModel):
    """ScaleOutInstance request structure.

    """

    def __init__(self):
        """
        :param TimeUnit: Time unit of scale-out. Valid values:
<li>s: seconds. When `PayMode` is 0, `TimeUnit` can only be `s`.</li>
<li>m: month. When `PayMode` is 1, `TimeUnit` can only be `m`.</li>\n        :type TimeUnit: str\n        :param TimeSpan: Duration of scale-out, which needs to be used together with `TimeUnit`.\n        :type TimeSpan: int\n        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param PayMode: Instance billing mode. Valid values:
<li>0: pay-as-you-go.</li>\n        :type PayMode: int\n        :param ClientToken: Client token.\n        :type ClientToken: str\n        :param PreExecutedFileSettings: Bootstrap script settings.\n        :type PreExecutedFileSettings: list of PreExecuteFileSettings\n        :param TaskCount: Number of task nodes added.\n        :type TaskCount: int\n        :param CoreCount: Number of core nodes added.\n        :type CoreCount: int\n        :param UnNecessaryNodeList: Process not required during scale-out.\n        :type UnNecessaryNodeList: list of int non-negative\n        :param RouterCount: Number of router nodes added.\n        :type RouterCount: int\n        :param SoftDeployInfo: Deployed service.
<li>`SoftDeployInfo` and `ServiceNodeInfo` are in the same group and mutually exclusive with `UnNecessaryNodeList`.</li>
<li>The combination of `SoftDeployInfo` and `ServiceNodeInfo` is recommended.</li>\n        :type SoftDeployInfo: list of int non-negative\n        :param ServiceNodeInfo: Started process.\n        :type ServiceNodeInfo: list of int non-negative\n        :param DisasterRecoverGroupIds: List of spread placement group IDs. Only one can be specified currently.\n        :type DisasterRecoverGroupIds: list of str\n        :param Tags: List of tags bound to added nodes.\n        :type Tags: list of Tag\n        :param HardwareResourceType: Resource type selected for scaling. Valid values: `host` (general CVM resource), `pod` (resource provided by TKE or EKS cluster)\n        :type HardwareResourceType: str\n        :param PodSpec: Specified information such as pod specification and source for expansion with pod resources\n        :type PodSpec: :class:`tencentcloud.emr.v20190103.models.PodSpec`\n        :param ClickHouseClusterName: Machine group name selected for ClickHouse cluster scaling-out\n        :type ClickHouseClusterName: str\n        :param ClickHouseClusterType: Machine group type selected for ClickHouse cluster scaling-out. new: creates a group; old: selects an existing group\n        :type ClickHouseClusterType: str\n        :param YarnNodeLabel: YARN node label specified for rule-based scaling-out\n        :type YarnNodeLabel: str\n        :param PodParameter: Custom pod permission and parameter\n        :type PodParameter: :class:`tencentcloud.emr.v20190103.models.PodParameter`\n        :param MasterCount: Number of master nodes to be added
When a ClickHouse cluster is scaled, this parameter does not take effect.
When a Kafka cluster is scaled, this parameter does not take effect.
When `HardwareResourceType` is `pod`, this parameter does not take effect.\n        :type MasterCount: int\n        :param StartServiceAfterScaleOut: Whether to start the service after scaling. `true`: yes; `false`: no\n        :type StartServiceAfterScaleOut: str\n        """
        self.TimeUnit = None
        self.TimeSpan = None
        self.InstanceId = None
        self.PayMode = None
        self.ClientToken = None
        self.PreExecutedFileSettings = None
        self.TaskCount = None
        self.CoreCount = None
        self.UnNecessaryNodeList = None
        self.RouterCount = None
        self.SoftDeployInfo = None
        self.ServiceNodeInfo = None
        self.DisasterRecoverGroupIds = None
        self.Tags = None
        self.HardwareResourceType = None
        self.PodSpec = None
        self.ClickHouseClusterName = None
        self.ClickHouseClusterType = None
        self.YarnNodeLabel = None
        self.PodParameter = None
        self.MasterCount = None
        self.StartServiceAfterScaleOut = None


    def _deserialize(self, params):
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.InstanceId = params.get("InstanceId")
        self.PayMode = params.get("PayMode")
        self.ClientToken = params.get("ClientToken")
        if params.get("PreExecutedFileSettings") is not None:
            self.PreExecutedFileSettings = []
            for item in params.get("PreExecutedFileSettings"):
                obj = PreExecuteFileSettings()
                obj._deserialize(item)
                self.PreExecutedFileSettings.append(obj)
        self.TaskCount = params.get("TaskCount")
        self.CoreCount = params.get("CoreCount")
        self.UnNecessaryNodeList = params.get("UnNecessaryNodeList")
        self.RouterCount = params.get("RouterCount")
        self.SoftDeployInfo = params.get("SoftDeployInfo")
        self.ServiceNodeInfo = params.get("ServiceNodeInfo")
        self.DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.HardwareResourceType = params.get("HardwareResourceType")
        if params.get("PodSpec") is not None:
            self.PodSpec = PodSpec()
            self.PodSpec._deserialize(params.get("PodSpec"))
        self.ClickHouseClusterName = params.get("ClickHouseClusterName")
        self.ClickHouseClusterType = params.get("ClickHouseClusterType")
        self.YarnNodeLabel = params.get("YarnNodeLabel")
        if params.get("PodParameter") is not None:
            self.PodParameter = PodParameter()
            self.PodParameter._deserialize(params.get("PodParameter"))
        self.MasterCount = params.get("MasterCount")
        self.StartServiceAfterScaleOut = params.get("StartServiceAfterScaleOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleOutInstanceResponse(AbstractModel):
    """ScaleOutInstance response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param DealNames: Order number.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DealNames: list of str\n        :param ClientToken: Client token.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ClientToken: str\n        :param FlowId: Scaling workflow ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FlowId: int\n        :param BillId: Big order number.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type BillId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.InstanceId = None
        self.DealNames = None
        self.ClientToken = None
        self.FlowId = None
        self.BillId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DealNames = params.get("DealNames")
        self.ClientToken = params.get("ClientToken")
        self.FlowId = params.get("FlowId")
        self.BillId = params.get("BillId")
        self.RequestId = params.get("RequestId")


class SearchItem(AbstractModel):
    """Search field

    """

    def __init__(self):
        """
        :param SearchType: Searchable type\n        :type SearchType: str\n        :param SearchValue: Searchable value\n        :type SearchValue: str\n        """
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
        


class Tag(AbstractModel):
    """Tag

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
        


class TerminateInstanceRequest(AbstractModel):
    """TerminateInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param ResourceIds: ID of terminated node. This parameter is reserved and does not need to be configured.\n        :type ResourceIds: list of str\n        """
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
        


class TerminateInstanceResponse(AbstractModel):
    """TerminateInstance response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TerminateTasksRequest(AbstractModel):
    """TerminateTasks request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param ResourceIds: List of resource IDs of the node to be terminated. The resource ID is in the format of `emr-vm-xxxxxxxx`. A valid resource ID can be queried in the [console](https://console.cloud.tencent.com/emr/static/hardware).\n        :type ResourceIds: list of str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateInstanceSettings(AbstractModel):
    """Target resource specification

    """

    def __init__(self):
        """
        :param Memory: Memory capacity in GB\n        :type Memory: int\n        :param CPUCores: Number of CPU cores\n        :type CPUCores: int\n        :param ResourceId: Machine resource ID (EMR resource identifier)\n        :type ResourceId: str\n        :param InstanceType: Target machine specification\n        :type InstanceType: str\n        """
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
        


class VPCSettings(AbstractModel):
    """VPC parameters

    """

    def __init__(self):
        """
        :param VpcId: VPC ID\n        :type VpcId: str\n        :param SubnetId: Subnet ID\n        :type SubnetId: str\n        """
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
        