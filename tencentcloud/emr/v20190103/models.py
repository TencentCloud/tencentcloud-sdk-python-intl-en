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


class COSSettings(AbstractModel):
    """COS-related configuration

    """

    def __init__(self):
        """
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


class CdbInfo(AbstractModel):
    """Output parameters

    """

    def __init__(self):
        """
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


class ClusterInstancesInfo(AbstractModel):
    """Cluster instance information

    """

    def __init__(self):
        """
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


class CreateInstanceRequest(AbstractModel):
    """CreateInstance request structure.

    """

    def __init__(self):
        """
        :param ProductId: Product ID. Different product IDs represent different EMR product versions. Valid values:
<li>1: EMR v1.3.1.</li>
<li>2: EMR v2.0.1.</li>
<li>4: EMR v2.1.0.</li>
<li>7: EMR v3.0.0.</li>
        :type ProductId: int
        :param VPCSettings: Configuration information of VPC. This parameter is used to specify the VPC ID, subnet ID, etc.
        :type VPCSettings: :class:`tencentcloud.emr.v20190103.models.VPCSettings`
        :param Software: List of deployed components. Different required components need to be selected for different EMR product IDs (i.e., `ProductId`; for specific meanings, please see the `ProductId` field in the input parameter):
<li>When `ProductId` is 1, the required components include hadoop-2.7.3, knox-1.2.0, and zookeeper-3.4.9</li>
<li>When `ProductId` is 2, the required components include hadoop-2.7.3, knox-1.2.0, and zookeeper-3.4.9</li>
<li>When `ProductId` is 4, the required components include hadoop-2.8.4, knox-1.2.0, and zookeeper-3.4.9</li>
<li>When `ProductId` is 7, the required components include hadoop-3.1.2, knox-1.2.0, and zookeeper-3.4.9</li>
        :type Software: list of str
        :param ResourceSpec: Node resource specification.
        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.NewResourceSpec`
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
        :param Placement: Instance location. This parameter is used to specify the AZ, project, and other attributes of the instance.
        :type Placement: :class:`tencentcloud.emr.v20190103.models.Placement`
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
        :param COSSettings: Parameter required for enabling COS access.
        :type COSSettings: :class:`tencentcloud.emr.v20190103.models.COSSettings`
        :param SgId: Security group to which an instance belongs in the format of `sg-xxxxxxxx`. This parameter can be obtained from the `SecurityGroupId` field in the return value of the [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808) API.
        :type SgId: str
        :param PreExecutedFileSettings: Bootstrap script settings.
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
        """
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


class CreateInstanceResponse(AbstractModel):
    """CreateInstance response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CustomMetaInfo(AbstractModel):
    """User-created Hive-MetaDB instance information

    """

    def __init__(self):
        """
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


class DescribeClusterNodesRequest(AbstractModel):
    """DescribeClusterNodes request structure.

    """

    def __init__(self):
        """
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


class DescribeClusterNodesResponse(AbstractModel):
    """DescribeClusterNodes response structure.

    """

    def __init__(self):
        """
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


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances request structure.

    """

    def __init__(self):
        """
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


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances response structure.

    """

    def __init__(self):
        """
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


class EmrProductConfigOutter(AbstractModel):
    """EMR product configuration

    """

    def __init__(self):
        """
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


class HostVolumeContext(AbstractModel):
    """Pod `HostPath` mounting method description

    """

    def __init__(self):
        """
        :param VolumePath: Directory in the pod for mounting the host, which is the mount point of resources for the host. The specified mount point corresponds to the host path and is used as the data storage directory in the pod.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VolumePath: str
        """
        self.VolumePath = None


    def _deserialize(self, params):
        self.VolumePath = params.get("VolumePath")


class InquiryPriceCreateInstanceRequest(AbstractModel):
    """InquiryPriceCreateInstance request structure.

    """

    def __init__(self):
        """
        :param TimeUnit: Time unit of instance purchase duration. Valid values:
<li>s: seconds. When `PayMode` is 0, `TimeUnit` can only be `s`.</li>
        :type TimeUnit: str
        :param TimeSpan: Purchase duration of instance, which needs to be used together with `TimeUnit`.
<li>When `TimeUnit` is `s`, this parameter can only be filled with 3600, indicating a pay-as-you-go instance.</li>
<li>When `TimeUnit` is `m`, the number entered in this parameter indicates the purchase duration of the monthly-subscription instance; for example, 1 means one month</li>
        :type TimeSpan: int
        :param ResourceSpec: Node specification queried for price.
        :type ResourceSpec: :class:`tencentcloud.emr.v20190103.models.NewResourceSpec`
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
        """
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


class InquiryPriceCreateInstanceResponse(AbstractModel):
    """InquiryPriceCreateInstance response structure.

    """

    def __init__(self):
        """
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
        """
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
        """
        self.TimeSpan = None
        self.ResourceIds = None
        self.Placement = None
        self.PayMode = None
        self.TimeUnit = None
        self.Currency = None


    def _deserialize(self, params):
        self.TimeSpan = params.get("TimeSpan")
        self.ResourceIds = params.get("ResourceIds")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.PayMode = params.get("PayMode")
        self.TimeUnit = params.get("TimeUnit")
        self.Currency = params.get("Currency")


class InquiryPriceRenewInstanceResponse(AbstractModel):
    """InquiryPriceRenewInstance response structure.

    """

    def __init__(self):
        """
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


class InquiryPriceScaleOutInstanceRequest(AbstractModel):
    """InquiryPriceScaleOutInstance request structure.

    """

    def __init__(self):
        """
        :param TimeUnit: Time unit of scale-out. Valid values:
<li>s: seconds. When `PayMode` is 0, `TimeUnit` can only be `s`.</li>
        :type TimeUnit: str
        :param TimeSpan: Duration of scale-out, which needs to be used together with `TimeUnit`.
<li>When `PayMode` is 0, `TimeSpan` can only be 3,600.</li>
        :type TimeSpan: int
        :param ZoneId: ID of the AZ where an instance resides.
        :type ZoneId: int
        :param PayMode: Instance billing mode. Valid values:
<li>0: pay-as-you-go.</li>
        :type PayMode: int
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param CoreCount: Number of core nodes added.
        :type CoreCount: int
        :param TaskCount: Number of task nodes added.
        :type TaskCount: int
        :param Currency: Currency.
        :type Currency: str
        :param RouterCount: Number of router nodes added.
        :type RouterCount: int
        """
        self.TimeUnit = None
        self.TimeSpan = None
        self.ZoneId = None
        self.PayMode = None
        self.InstanceId = None
        self.CoreCount = None
        self.TaskCount = None
        self.Currency = None
        self.RouterCount = None


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


class InquiryPriceScaleOutInstanceResponse(AbstractModel):
    """InquiryPriceScaleOutInstance response structure.

    """

    def __init__(self):
        """
        :param OriginalCost: Original price.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OriginalCost: str
        :param DiscountCost: Discounted price.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DiscountCost: str
        :param Unit: Time unit of scale-out. Valid values:
<li>s: seconds.</li>
Note: this field may return null, indicating that no valid values can be obtained.
        :type Unit: str
        :param PriceSpec: Node specification queried for price.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PriceSpec: :class:`tencentcloud.emr.v20190103.models.PriceResource`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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


class InquiryPriceUpdateInstanceResponse(AbstractModel):
    """InquiryPriceUpdateInstance response structure.

    """

    def __init__(self):
        """
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
        """
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


class MultiDisk(AbstractModel):
    """Multi-cloud disk parameters

    """

    def __init__(self):
        """
        :param DiskType: Cloud disk type. Valid values: CLOUD_PREMIUM, CLOUD_SSD, CLOUD_BASIC
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


class MultiDiskMC(AbstractModel):
    """Multi-cloud disk parameters

    """

    def __init__(self):
        """
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


class NewResourceSpec(AbstractModel):
    """Resource description

    """

    def __init__(self):
        """
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


class NodeHardwareInfo(AbstractModel):
    """Node hardware information

    """

    def __init__(self):
        """
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


class OutterResource(AbstractModel):
    """Resource details

    """

    def __init__(self):
        """
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


class PersistentVolumeContext(AbstractModel):
    """Pod `PVC` storage method description

    """

    def __init__(self):
        """
        :param DiskSize: Disk size in GB
Note: this field may return null, indicating that no valid values can be obtained.
        :type DiskSize: int
        :param DiskType: Disk type. Valid values: CLOUD_PREMIUM, CLOUD_SSD
Note: this field may return null, indicating that no valid values can be obtained.
        :type DiskType: str
        :param DiskNum: Number of disks
Note: this field may return null, indicating that no valid values can be obtained.
        :type DiskNum: int
        """
        self.DiskSize = None
        self.DiskType = None
        self.DiskNum = None


    def _deserialize(self, params):
        self.DiskSize = params.get("DiskSize")
        self.DiskType = params.get("DiskType")
        self.DiskNum = params.get("DiskNum")


class Placement(AbstractModel):
    """Location information of cluster instance

    """

    def __init__(self):
        """
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


class PodSpec(AbstractModel):
    """Resource description for container resource expansion

    """

    def __init__(self):
        """
        :param ResourceProviderIdentifier: Identifier of external resource provider, such as "cls-a1cd23fa".
        :type ResourceProviderIdentifier: str
        :param ResourceProviderType: Type of external resource provider, such as "tke". Currently, only "tke" is supported.
        :type ResourceProviderType: str
        :param NodeType: Purpose of the resource, i.e., node type, which currently can only be "TASK".
        :type NodeType: str
        :param Cpu: Number of CPU cores.
        :type Cpu: int
        :param Memory: Memory size in GB.
        :type Memory: int
        :param DataVolumes: Mount point of resources for the host. The specified mount point corresponds to the host path and is used as the data storage directory in the pod. (This parameter has been disused)
        :type DataVolumes: list of str
        :param CpuType: EKS cluster - CPU type. Valid values: "intel", "amd"
        :type CpuType: str
        :param PodVolumes: Pod node data directory mounting information.
        :type PodVolumes: list of PodVolume
        """
        self.ResourceProviderIdentifier = None
        self.ResourceProviderType = None
        self.NodeType = None
        self.Cpu = None
        self.Memory = None
        self.DataVolumes = None
        self.CpuType = None
        self.PodVolumes = None


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


class PodVolume(AbstractModel):
    """Pod storage device description.

    """

    def __init__(self):
        """
        :param VolumeType: Storage type. Valid values: "pvc", "hostpath".
Note: this field may return null, indicating that no valid values can be obtained.
        :type VolumeType: str
        :param PVCVolume: This field will take effect if `VolumeType` is `pvc`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PVCVolume: :class:`tencentcloud.emr.v20190103.models.PersistentVolumeContext`
        :param HostVolume: This field will take effect if `VolumeType` is `hostpath`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type HostVolume: :class:`tencentcloud.emr.v20190103.models.HostVolumeContext`
        """
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


class PreExecuteFileSettings(AbstractModel):
    """Pre-execution script configuration

    """

    def __init__(self):
        """
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


class PriceResource(AbstractModel):
    """Resource queried for price

    """

    def __init__(self):
        """
        :param Spec: Target specification
Note: this field may return null, indicating that no valid values can be obtained.
        :type Spec: str
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
        :param Cpu: Number of cores
Note: this field may return null, indicating that no valid values can be obtained.
        :type Cpu: int
        :param DiskSize: Disk size
Note: this field may return null, indicating that no valid values can be obtained.
        :type DiskSize: int
        :param MultiDisks: List of cloud disks
Note: this field may return null, indicating that no valid values can be obtained.
        :type MultiDisks: list of MultiDisk
        :param DiskCnt: Number of disks
Note: this field may return null, indicating that no valid values can be obtained.
        :type DiskCnt: int
        :param InstanceType: Specification
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceType: str
        :param Tags: Tag
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param DiskNum: Number of disks
Note: this field may return null, indicating that no valid values can be obtained.
        :type DiskNum: int
        :param LocalDiskNum: Number of local disks
Note: this field may return null, indicating that no valid values can be obtained.
        :type LocalDiskNum: int
        """
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


class Resource(AbstractModel):
    """Resource details

    """

    def __init__(self):
        """
        :param Spec: Node specification description
Note: this field may return null, indicating that no valid values can be obtained.
        :type Spec: str
        :param StorageType: Storage class
Note: this field may return null, indicating that no valid values can be obtained.
        :type StorageType: int
        :param DiskType: Disk type
Note: this field may return null, indicating that no valid values can be obtained.
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
        :param InstanceType: Specification type
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceType: str
        :param LocalDiskNum: Number of local disks
Note: this field may return null, indicating that no valid values can be obtained.
        :type LocalDiskNum: int
        :param DiskNum: Number of disks
Note: this field may return null, indicating that no valid values can be obtained.
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


class ScaleOutInstanceRequest(AbstractModel):
    """ScaleOutInstance request structure.

    """

    def __init__(self):
        """
        :param TimeUnit: Time unit of scale-out. Valid values:
<li>s: seconds. When `PayMode` is 0, `TimeUnit` can only be `s`.</li>
<li>m: month. When `PayMode` is 1, `TimeUnit` can only be `m`.</li>
        :type TimeUnit: str
        :param TimeSpan: Duration of scale-out, which needs to be used together with `TimeUnit`.
        :type TimeSpan: int
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param PayMode: Instance billing mode. Valid values:
<li>0: pay-as-you-go.</li>
        :type PayMode: int
        :param ClientToken: Client token.
        :type ClientToken: str
        :param PreExecutedFileSettings: Bootstrap script settings.
        :type PreExecutedFileSettings: list of PreExecuteFileSettings
        :param TaskCount: Number of task nodes added.
        :type TaskCount: int
        :param CoreCount: Number of core nodes added.
        :type CoreCount: int
        :param UnNecessaryNodeList: Process not required during scale-out.
        :type UnNecessaryNodeList: list of int non-negative
        :param RouterCount: Number of router nodes added.
        :type RouterCount: int
        :param SoftDeployInfo: Deployed service.
<li>`SoftDeployInfo` and `ServiceNodeInfo` are in the same group and mutually exclusive with `UnNecessaryNodeList`.</li>
<li>The combination of `SoftDeployInfo` and `ServiceNodeInfo` is recommended.</li>
        :type SoftDeployInfo: list of int non-negative
        :param ServiceNodeInfo: Started process.
        :type ServiceNodeInfo: list of int non-negative
        :param DisasterRecoverGroupIds: List of spread placement group IDs. Only one can be specified currently.
        :type DisasterRecoverGroupIds: list of str
        :param Tags: List of tags bound to added nodes.
        :type Tags: list of Tag
        :param HardwareResourceType: Resource type selected for expansion. Valid values: host (general CVM resource), pod (resource provided by TKE cluster)
        :type HardwareResourceType: str
        :param PodSpec: Specified information such as pod specification and source for expansion with pod resources
        :type PodSpec: :class:`tencentcloud.emr.v20190103.models.PodSpec`
        :param ClickHouseClusterName: Machine group name selected for ClickHouse cluster scaling-out
        :type ClickHouseClusterName: str
        :param ClickHouseClusterType: Machine group type selected for ClickHouse cluster scaling-out. new: creates a group; old: selects an existing group
        :type ClickHouseClusterType: str
        :param YarnNodeLabel: YARN node label specified for rule-based scaling-out
        :type YarnNodeLabel: str
        """
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


class ScaleOutInstanceResponse(AbstractModel):
    """ScaleOutInstance response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param DealNames: Order number.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DealNames: list of str
        :param ClientToken: Client token.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClientToken: str
        :param FlowId: Scaling workflow ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FlowId: int
        :param BillId: Big order number.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BillId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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


class Tag(AbstractModel):
    """Tag

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


class TerminateInstanceRequest(AbstractModel):
    """TerminateInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param ResourceIds: ID of terminated node. This parameter is reserved and does not need to be configured.
        :type ResourceIds: list of str
        """
        self.InstanceId = None
        self.ResourceIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ResourceIds = params.get("ResourceIds")


class TerminateInstanceResponse(AbstractModel):
    """TerminateInstance response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TerminateTasksRequest(AbstractModel):
    """TerminateTasks request structure.

    """

    def __init__(self):
        """
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


class TerminateTasksResponse(AbstractModel):
    """TerminateTasks response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateInstanceSettings(AbstractModel):
    """Target resource specification

    """

    def __init__(self):
        """
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


class VPCSettings(AbstractModel):
    """VPC parameters

    """

    def __init__(self):
        """
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