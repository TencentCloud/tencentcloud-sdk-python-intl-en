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


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups request structure.

    """

    def __init__(self):
        """
        :param Product: Database engine name. Valid value: `mariadb`.
        :type Product: str
        :param SecurityGroupId: ID of the security group to be associated in the format of sg-efil73jd.
        :type SecurityGroupId: str
        :param InstanceIds: ID(s) of the instance(s) to be associated in the format of tdsql-lesecurk. You can specify multiple instances.
        :type InstanceIds: list of str
        """
        self.Product = None
        self.SecurityGroupId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.InstanceIds = params.get("InstanceIds")


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CloneAccountRequest(AbstractModel):
    """CloneAccount request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param SrcUser: Source user account name
        :type SrcUser: str
        :param SrcHost: Source user host
        :type SrcHost: str
        :param DstUser: Target user account name
        :type DstUser: str
        :param DstHost: Target user host
        :type DstHost: str
        :param DstDesc: Description of target account
        :type DstDesc: str
        """
        self.InstanceId = None
        self.SrcUser = None
        self.SrcHost = None
        self.DstUser = None
        self.DstHost = None
        self.DstDesc = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SrcUser = params.get("SrcUser")
        self.SrcHost = params.get("SrcHost")
        self.DstUser = params.get("DstUser")
        self.DstHost = params.get("DstHost")
        self.DstDesc = params.get("DstDesc")


class CloneAccountResponse(AbstractModel):
    """CloneAccount response structure.

    """

    def __init__(self):
        """
        :param FlowId: Async task flow ID.
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CloseDBExtranetAccessRequest(AbstractModel):
    """CloseDBExtranetAccess request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of instance for which to disable public network access. The ID is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :type InstanceId: str
        :param Ipv6Flag: Whether IPv6 is used. Default value: 0
        :type Ipv6Flag: int
        """
        self.InstanceId = None
        self.Ipv6Flag = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Ipv6Flag = params.get("Ipv6Flag")


class CloseDBExtranetAccessResponse(AbstractModel):
    """CloseDBExtranetAccess response structure.

    """

    def __init__(self):
        """
        :param FlowId: Async task ID. The task status can be queried through the `DescribeFlow` API.
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ConstraintRange(AbstractModel):
    """Range of constraint type values

    """

    def __init__(self):
        """
        :param Min: Minimum value when constraint type is `section`
        :type Min: str
        :param Max: Maximum value when constraint type is `section`
        :type Max: str
        """
        self.Min = None
        self.Max = None


    def _deserialize(self, params):
        self.Min = params.get("Min")
        self.Max = params.get("Max")


class CopyAccountPrivilegesRequest(AbstractModel):
    """CopyAccountPrivileges request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :type InstanceId: str
        :param SrcUserName: Source username
        :type SrcUserName: str
        :param SrcHost: Access host allowed for source user
        :type SrcHost: str
        :param DstUserName: Target username
        :type DstUserName: str
        :param DstHost: Access host allowed for target user
        :type DstHost: str
        :param SrcReadOnly: `ReadOnly` attribute of source account
        :type SrcReadOnly: str
        :param DstReadOnly: `ReadOnly` attribute of target account
        :type DstReadOnly: str
        """
        self.InstanceId = None
        self.SrcUserName = None
        self.SrcHost = None
        self.DstUserName = None
        self.DstHost = None
        self.SrcReadOnly = None
        self.DstReadOnly = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SrcUserName = params.get("SrcUserName")
        self.SrcHost = params.get("SrcHost")
        self.DstUserName = params.get("DstUserName")
        self.DstHost = params.get("DstHost")
        self.SrcReadOnly = params.get("SrcReadOnly")
        self.DstReadOnly = params.get("DstReadOnly")


class CopyAccountPrivilegesResponse(AbstractModel):
    """CopyAccountPrivileges response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAccountRequest(AbstractModel):
    """CreateAccount request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :type InstanceId: str
        :param UserName: Login username, which can contain 1-32 letters, digits, underscores, and hyphens.
        :type UserName: str
        :param Host: Host that can be logged in to, which is in the same format as the host of the MySQL account and supports wildcards, such as %, 10.%, and 10.20.%.
        :type Host: str
        :param Password: Account password, which can contain 6-32 letters, digits, and common symbols but not semicolons, single quotation marks, and double quotation marks.
        :type Password: str
        :param ReadOnly: Whether to create a read-only account. 0: no; 1: for the account's SQL requests, the secondary will be used first, and if it is unavailable, the primary will be used; 2: the secondary will be used first, and if it is unavailable, the operation will fail.
        :type ReadOnly: int
        :param Description: Account remarks, which can contain 0-256 letters, digits, and common symbols.
        :type Description: str
        :param DelayThresh: Determines whether the secondary is unavailable based on the passed-in time
        :type DelayThresh: int
        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.Password = None
        self.ReadOnly = None
        self.Description = None
        self.DelayThresh = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.Password = params.get("Password")
        self.ReadOnly = params.get("ReadOnly")
        self.Description = params.get("Description")
        self.DelayThresh = params.get("DelayThresh")


class CreateAccountResponse(AbstractModel):
    """CreateAccount response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, which is passed through from the input parameters.
        :type InstanceId: str
        :param UserName: Username, which is passed through from the input parameters.
        :type UserName: str
        :param Host: Host allowed for access, which is passed through from the input parameters.
        :type Host: str
        :param ReadOnly: Passed through from the input parameters.
        :type ReadOnly: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.ReadOnly = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.ReadOnly = params.get("ReadOnly")
        self.RequestId = params.get("RequestId")


class DBAccount(AbstractModel):
    """TencentDB account information

    """

    def __init__(self):
        """
        :param UserName: Username
        :type UserName: str
        :param Host: Host from which a user can log in (corresponding to the `host` field for a MySQL user; a user is uniquely identified by username and host; this parameter is in IP format and ends with % for IP range; % can be entered; if this parameter is left empty, % will be used by default)
        :type Host: str
        :param Description: User remarks
        :type Description: str
        :param CreateTime: Creation time
        :type CreateTime: str
        :param UpdateTime: Last updated time
        :type UpdateTime: str
        :param ReadOnly: Read-only flag. 0: no; 1: for the account's SQL requests, the secondary will be used first, and if it is unavailable, the primary will be used; 2: the secondary will be used first, and if it is unavailable, the operation will fail.
        :type ReadOnly: int
        :param DelayThresh: This field is meaningful for read-only accounts, indicating to select a secondary where the primary/secondary delay is below this value
Note: this field may return null, indicating that no valid values can be obtained.
        :type DelayThresh: int
        """
        self.UserName = None
        self.Host = None
        self.Description = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ReadOnly = None
        self.DelayThresh = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ReadOnly = params.get("ReadOnly")
        self.DelayThresh = params.get("DelayThresh")


class DBBackupTimeConfig(AbstractModel):
    """TencentDB instance backup time configuration information

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param StartBackupTime: Start time of daily backup window in the format of `mm:ss`, such as 22:00
        :type StartBackupTime: str
        :param EndBackupTime: End time of daily backup window in the format of `mm:ss`, such as 23:00
        :type EndBackupTime: str
        """
        self.InstanceId = None
        self.StartBackupTime = None
        self.EndBackupTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartBackupTime = params.get("StartBackupTime")
        self.EndBackupTime = params.get("EndBackupTime")


class DBInstance(AbstractModel):
    """TencentDB instance details.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, which uniquely identifies a TDSQL instance
        :type InstanceId: str
        :param InstanceName: Customizable instance name
        :type InstanceName: str
        :param AppId: Application ID of instance
        :type AppId: int
        :param ProjectId: Project ID of instance
        :type ProjectId: int
        :param Region: Instance region name, such as ap-shanghai
        :type Region: str
        :param Zone: Instance AZ name, such as ap-guangzhou-1
        :type Zone: str
        :param VpcId: VPC ID, which is 0 if the basic network is used
        :type VpcId: int
        :param SubnetId: Subnet ID, which is 0 if the basic network is used
        :type SubnetId: int
        :param Status: Instance status. 0: creating, 1: processing, 2: running, 3: instance not initialized, -1: instance isolated, -2: instance deleted
        :type Status: int
        :param Vip: Private IP address
        :type Vip: str
        :param Vport: Private network port
        :type Vport: int
        :param WanDomain: Domain name for public network access, which can be resolved by the public network
        :type WanDomain: str
        :param WanVip: Public IP address, which can be accessed over the public network
        :type WanVip: str
        :param WanPort: Public network port
        :type WanPort: int
        :param CreateTime: Instance creation time in the format of `2006-01-02 15:04:05`
        :type CreateTime: str
        :param UpdateTime: Last updated time of instance in the format of `2006-01-02 15:04:05`
        :type UpdateTime: str
        :param AutoRenewFlag: Auto-renewal flag. 0: no, 1: yes
        :type AutoRenewFlag: int
        :param PeriodEndTime: Instance expiration time in the format of `2006-01-02 15:04:05`
        :type PeriodEndTime: str
        :param Uin: Instance account
        :type Uin: str
        :param TdsqlVersion: TDSQL version information
        :type TdsqlVersion: str
        :param Memory: Instance memory size in GB
        :type Memory: int
        :param Storage: Instance storage capacity in GB
        :type Storage: int
        :param UniqueVpcId: VPC ID in string type
        :type UniqueVpcId: str
        :param UniqueSubnetId: VPC subnet ID in string type
        :type UniqueSubnetId: str
        :param OriginSerialId: Original ID of instance (this field is obsolete and should not be depended on)
        :type OriginSerialId: str
        :param NodeCount: Number of nodes. 2: one master and one slave, 3: one master and two slaves
        :type NodeCount: int
        :param IsTmp: Whether it is a temp instance. 0: no, non-zero value: yes
        :type IsTmp: int
        :param ExclusterId: Dedicated cluster ID. If this parameter is empty, the instance is a general instance
        :type ExclusterId: str
        :param Id: Numeric ID of instance (this field is obsolete and should not be depended on)
        :type Id: int
        :param Pid: Product type ID
        :type Pid: int
        :param Qps: Maximum QPS value
        :type Qps: int
        :param Paymode: Billing mode
Note: this field may return null, indicating that no valid values can be obtained.
        :type Paymode: str
        :param Locker: Async task flow ID when an async task is in progress on an instance
Note: this field may return null, indicating that no valid values can be obtained.
        :type Locker: int
        :param StatusDesc: Current instance running status description
Note: this field may return null, indicating that no valid values can be obtained.
        :type StatusDesc: str
        :param WanStatus: Public network access status. 0: not enabled, 1: enabled, 2: disabled, 3: enabling
        :type WanStatus: int
        :param IsAuditSupported: Whether the instance supports audit. 1: yes, 0: no
        :type IsAuditSupported: int
        :param Machine: Model
        :type Machine: str
        :param IsEncryptSupported: Whether data encryption is supported. 1: yes, 0: no
        :type IsEncryptSupported: int
        :param Cpu: Number of CPU cores of instance
        :type Cpu: int
        :param Ipv6Flag: Indicates whether the instance uses IPv6
Note: this field may return null, indicating that no valid values can be obtained.
        :type Ipv6Flag: int
        :param Vipv6: Private network IPv6 address
Note: this field may return null, indicating that no valid values can be obtained.
        :type Vipv6: str
        :param WanVipv6: Public network IPv6 address
Note: this field may return null, indicating that no valid values can be obtained.
        :type WanVipv6: str
        :param WanPortIpv6: Public network IPv6 port
Note: this field may return null, indicating that no valid values can be obtained.
        :type WanPortIpv6: int
        :param WanStatusIpv6: Public network IPv6 status
Note: this field may return null, indicating that no valid values can be obtained.
        :type WanStatusIpv6: int
        :param DbEngine: Database engine
Note: this field may return null, indicating that no valid values can be obtained.
        :type DbEngine: str
        :param DbVersion: Database version
Note: this field may return null, indicating that no valid values can be obtained.
        :type DbVersion: str
        :param DcnFlag: DCN type. Valid values: 0 (null), 1 (primary instance), 2 (disaster recovery instance)
Note: this field may return null, indicating that no valid values can be obtained.
        :type DcnFlag: int
        :param DcnStatus: DCN status. Valid values: 0 (null), 1 (creating), 2 (syncing), 3 (disconnected)
Note: this field may return null, indicating that no valid values can be obtained.
        :type DcnStatus: int
        :param DcnDstNum: The number of DCN disaster recovery instances
Note: this field may return null, indicating that no valid values can be obtained.
        :type DcnDstNum: int
        :param InstanceType: Instance type. Valid values: `1` (dedicated primary instance), `2` (primary instance), `3` (disaster recovery instance), and `4` (dedicated disaster recovery instance).
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceType: int
        """
        self.InstanceId = None
        self.InstanceName = None
        self.AppId = None
        self.ProjectId = None
        self.Region = None
        self.Zone = None
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.Vip = None
        self.Vport = None
        self.WanDomain = None
        self.WanVip = None
        self.WanPort = None
        self.CreateTime = None
        self.UpdateTime = None
        self.AutoRenewFlag = None
        self.PeriodEndTime = None
        self.Uin = None
        self.TdsqlVersion = None
        self.Memory = None
        self.Storage = None
        self.UniqueVpcId = None
        self.UniqueSubnetId = None
        self.OriginSerialId = None
        self.NodeCount = None
        self.IsTmp = None
        self.ExclusterId = None
        self.Id = None
        self.Pid = None
        self.Qps = None
        self.Paymode = None
        self.Locker = None
        self.StatusDesc = None
        self.WanStatus = None
        self.IsAuditSupported = None
        self.Machine = None
        self.IsEncryptSupported = None
        self.Cpu = None
        self.Ipv6Flag = None
        self.Vipv6 = None
        self.WanVipv6 = None
        self.WanPortIpv6 = None
        self.WanStatusIpv6 = None
        self.DbEngine = None
        self.DbVersion = None
        self.DcnFlag = None
        self.DcnStatus = None
        self.DcnDstNum = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.AppId = params.get("AppId")
        self.ProjectId = params.get("ProjectId")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.WanDomain = params.get("WanDomain")
        self.WanVip = params.get("WanVip")
        self.WanPort = params.get("WanPort")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.Uin = params.get("Uin")
        self.TdsqlVersion = params.get("TdsqlVersion")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.UniqueVpcId = params.get("UniqueVpcId")
        self.UniqueSubnetId = params.get("UniqueSubnetId")
        self.OriginSerialId = params.get("OriginSerialId")
        self.NodeCount = params.get("NodeCount")
        self.IsTmp = params.get("IsTmp")
        self.ExclusterId = params.get("ExclusterId")
        self.Id = params.get("Id")
        self.Pid = params.get("Pid")
        self.Qps = params.get("Qps")
        self.Paymode = params.get("Paymode")
        self.Locker = params.get("Locker")
        self.StatusDesc = params.get("StatusDesc")
        self.WanStatus = params.get("WanStatus")
        self.IsAuditSupported = params.get("IsAuditSupported")
        self.Machine = params.get("Machine")
        self.IsEncryptSupported = params.get("IsEncryptSupported")
        self.Cpu = params.get("Cpu")
        self.Ipv6Flag = params.get("Ipv6Flag")
        self.Vipv6 = params.get("Vipv6")
        self.WanVipv6 = params.get("WanVipv6")
        self.WanPortIpv6 = params.get("WanPortIpv6")
        self.WanStatusIpv6 = params.get("WanStatusIpv6")
        self.DbEngine = params.get("DbEngine")
        self.DbVersion = params.get("DbVersion")
        self.DcnFlag = params.get("DcnFlag")
        self.DcnStatus = params.get("DcnStatus")
        self.DcnDstNum = params.get("DcnDstNum")
        self.InstanceType = params.get("InstanceType")


class DBParamValue(AbstractModel):
    """TencentDB parameter information.

    """

    def __init__(self):
        """
        :param Param: Parameter name
        :type Param: str
        :param Value: Parameter value
        :type Value: str
        """
        self.Param = None
        self.Value = None


    def _deserialize(self, params):
        self.Param = params.get("Param")
        self.Value = params.get("Value")


class Database(AbstractModel):
    """Database information

    """

    def __init__(self):
        """
        :param DbName: Database name
        :type DbName: str
        """
        self.DbName = None


    def _deserialize(self, params):
        self.DbName = params.get("DbName")


class DeleteAccountRequest(AbstractModel):
    """DeleteAccount request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :type InstanceId: str
        :param UserName: Username
        :type UserName: str
        :param Host: Access host allowed for user
        :type Host: str
        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")


class DeleteAccountResponse(AbstractModel):
    """DeleteAccount response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccountPrivilegesRequest(AbstractModel):
    """DescribeAccountPrivileges request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :type InstanceId: str
        :param UserName: Login username.
        :type UserName: str
        :param Host: Access host allowed for user. An account is uniquely identified by username and host.
        :type Host: str
        :param DbName: Database name. `\*` indicates that global permissions will be queried (i.e., `\*.\*`), in which case the `Type` and `Object ` parameters will be ignored
        :type DbName: str
        :param Type: Type. Valid values: table, view, proc, func, \*. If `DbName` is a specific database name and `Type` is `\*`, the permissions of the database will be queried (i.e., `db.\*`), in which case the `Object` parameter will be ignored
        :type Type: str
        :param Object: Type name. For example, if `Type` is `table`, `Object` indicates a specific table name; if both `DbName` and `Type` are specific names, it indicates a specific object name and cannot be `\*` or empty
        :type Object: str
        :param ColName: If `Type` is `table` and `ColName` is `\*`, the permissions of the table will be queried; if `ColName` is a specific field name, the permissions of the corresponding field will be queried
        :type ColName: str
        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.DbName = None
        self.Type = None
        self.Object = None
        self.ColName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.DbName = params.get("DbName")
        self.Type = params.get("Type")
        self.Object = params.get("Object")
        self.ColName = params.get("ColName")


class DescribeAccountPrivilegesResponse(AbstractModel):
    """DescribeAccountPrivileges response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Privileges: Permission list.
        :type Privileges: list of str
        :param UserName: Database account username
        :type UserName: str
        :param Host: Database account host
        :type Host: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceId = None
        self.Privileges = None
        self.UserName = None
        self.Host = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Privileges = params.get("Privileges")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, which is passed through from the input parameters.
        :type InstanceId: str
        :param Users: Instance user list.
        :type Users: list of DBAccount
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceId = None
        self.Users = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Users") is not None:
            self.Users = []
            for item in params.get("Users"):
                obj = DBAccount()
                obj._deserialize(item)
                self.Users.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBackupTimeRequest(AbstractModel):
    """DescribeBackupTime request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class DescribeBackupTimeResponse(AbstractModel):
    """DescribeBackupTime response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of returned configurations
        :type TotalCount: int
        :param Items: Instance backup time configuration information
Note: this field may return null, indicating that no valid values can be obtained.
        :type Items: list of DBBackupTimeConfig
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = DBBackupTimeConfig()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: Queries by instance ID or IDs. Instance ID is in the format of `tdsql-ow728lmc`. Up to 100 instances can be queried in one request.
        :type InstanceIds: list of str
        :param SearchName: Search field name. Valid values: instancename (search by instance name), vip (search by private IP), all (search by instance ID, instance name, and private IP).
        :type SearchName: str
        :param SearchKey: Search keyword. Fuzzy search is supported. Multiple keywords should be separated by line breaks (`\n`).
        :type SearchKey: str
        :param ProjectIds: Queries by project ID
        :type ProjectIds: list of int
        :param IsFilterVpc: Whether to search by VPC
        :type IsFilterVpc: bool
        :param VpcId: VPC ID, which is valid when `IsFilterVpc` is 1
        :type VpcId: str
        :param SubnetId: VPC subnet ID, which is valid when `IsFilterVpc` is 1
        :type SubnetId: str
        :param OrderBy: Sort by field. Valid values: projectId, createtime, instancename
        :type OrderBy: str
        :param OrderByType: Sorting order. Valid values: desc, asc
        :type OrderByType: str
        :param Offset: Offset. Default value: 0
        :type Offset: int
        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param OriginSerialIds: Queries by `OriginSerialId`
        :type OriginSerialIds: list of str
        :param IsFilterExcluster: Identifies whether to use the `ExclusterType` field. false: no, true: yes
        :type IsFilterExcluster: bool
        :param ExclusterType: Instance cluster type. 1: non-dedicated cluster, 2: dedicated cluster, 0: all
        :type ExclusterType: int
        :param ExclusterIds: Filters instances by dedicated cluster ID in the format of `dbdc-4ih6uct9`
        :type ExclusterIds: list of str
        :param TagKeys: Tag key used in queries
        :type TagKeys: list of str
        :param FilterInstanceType: Instance types used in filtering. Valid values: 1 (dedicated instance), 2 (primary instance), 3 (disaster recovery instance). Multiple values should be separated by commas.
        :type FilterInstanceType: str
        """
        self.InstanceIds = None
        self.SearchName = None
        self.SearchKey = None
        self.ProjectIds = None
        self.IsFilterVpc = None
        self.VpcId = None
        self.SubnetId = None
        self.OrderBy = None
        self.OrderByType = None
        self.Offset = None
        self.Limit = None
        self.OriginSerialIds = None
        self.IsFilterExcluster = None
        self.ExclusterType = None
        self.ExclusterIds = None
        self.TagKeys = None
        self.FilterInstanceType = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.SearchName = params.get("SearchName")
        self.SearchKey = params.get("SearchKey")
        self.ProjectIds = params.get("ProjectIds")
        self.IsFilterVpc = params.get("IsFilterVpc")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OriginSerialIds = params.get("OriginSerialIds")
        self.IsFilterExcluster = params.get("IsFilterExcluster")
        self.ExclusterType = params.get("ExclusterType")
        self.ExclusterIds = params.get("ExclusterIds")
        self.TagKeys = params.get("TagKeys")
        self.FilterInstanceType = params.get("FilterInstanceType")


class DescribeDBInstancesResponse(AbstractModel):
    """DescribeDBInstances response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible instances
        :type TotalCount: int
        :param Instances: Instance details list
        :type Instances: list of DBInstance
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Instances = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = DBInstance()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBLogFilesRequest(AbstractModel):
    """DescribeDBLogFiles request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.
        :type InstanceId: str
        :param Type: Requested log type. Valid values: 1 (binlog), 2 (cold backup), 3 (errlog), 4 (slowlog).
        :type Type: int
        """
        self.InstanceId = None
        self.Type = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Type = params.get("Type")


class DescribeDBLogFilesResponse(AbstractModel):
    """DescribeDBLogFiles response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.
        :type InstanceId: str
        :param Type: Requested log type. Valid values: 1 (binlog), 2 (cold backup), 3 (errlog), 4 (slowlog).
        :type Type: int
        :param Total: Total number of requested logs
        :type Total: int
        :param Files: Information such as `uri`, `length`, and `mtime` (modification time)
        :type Files: list of LogFileInfo
        :param VpcPrefix: For an instance in a VPC, this prefix plus URI can be used as the download address
        :type VpcPrefix: str
        :param NormalPrefix: For an instance in a common network, this prefix plus URI can be used as the download address
        :type NormalPrefix: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceId = None
        self.Type = None
        self.Total = None
        self.Files = None
        self.VpcPrefix = None
        self.NormalPrefix = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Type = params.get("Type")
        self.Total = params.get("Total")
        if params.get("Files") is not None:
            self.Files = []
            for item in params.get("Files"):
                obj = LogFileInfo()
                obj._deserialize(item)
                self.Files.append(obj)
        self.VpcPrefix = params.get("VpcPrefix")
        self.NormalPrefix = params.get("NormalPrefix")
        self.RequestId = params.get("RequestId")


class DescribeDBParametersRequest(AbstractModel):
    """DescribeDBParameters request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeDBParametersResponse(AbstractModel):
    """DescribeDBParameters response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.
        :type InstanceId: str
        :param Params: Requests the current parameter values of database
        :type Params: list of ParamDesc
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceId = None
        self.Params = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Params") is not None:
            self.Params = []
            for item in params.get("Params"):
                obj = ParamDesc()
                obj._deserialize(item)
                self.Params.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBPerformanceDetailsRequest(AbstractModel):
    """DescribeDBPerformanceDetails request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.
        :type InstanceId: str
        :param StartTime: Start date in the format of `yyyy-mm-dd`
        :type StartTime: str
        :param EndTime: End date in the format of `yyyy-mm-dd`
        :type EndTime: str
        :param MetricName: Name of pulled metric. Valid values: long_query, select_total, update_total, insert_total, delete_total, mem_hit_rate, disk_iops, conn_active, is_master_switched, slave_delay
        :type MetricName: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")


class DescribeDBPerformanceDetailsResponse(AbstractModel):
    """DescribeDBPerformanceDetails response structure.

    """

    def __init__(self):
        """
        :param Master: Master node performance monitoring data
        :type Master: :class:`tencentcloud.mariadb.v20170312.models.PerformanceMonitorSet`
        :param Slave1: Slave 1 performance monitoring data
Note: this field may return null, indicating that no valid values can be obtained.
        :type Slave1: :class:`tencentcloud.mariadb.v20170312.models.PerformanceMonitorSet`
        :param Slave2: Slave 2 performance monitoring data. If the instance is one-primary-one-secondary, it does not have this field
Note: this field may return null, indicating that no valid values can be obtained.
        :type Slave2: :class:`tencentcloud.mariadb.v20170312.models.PerformanceMonitorSet`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Master = None
        self.Slave1 = None
        self.Slave2 = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Master") is not None:
            self.Master = PerformanceMonitorSet()
            self.Master._deserialize(params.get("Master"))
        if params.get("Slave1") is not None:
            self.Slave1 = PerformanceMonitorSet()
            self.Slave1._deserialize(params.get("Slave1"))
        if params.get("Slave2") is not None:
            self.Slave2 = PerformanceMonitorSet()
            self.Slave2._deserialize(params.get("Slave2"))
        self.RequestId = params.get("RequestId")


class DescribeDBPerformanceRequest(AbstractModel):
    """DescribeDBPerformance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.
        :type InstanceId: str
        :param StartTime: Start date in the format of `yyyy-mm-dd`
        :type StartTime: str
        :param EndTime: End date in the format of `yyyy-mm-dd`
        :type EndTime: str
        :param MetricName: Name of pulled metric. Valid values: long_query, select_total, update_total, insert_total, delete_total, mem_hit_rate, disk_iops, conn_active, is_master_switched, slave_delay
        :type MetricName: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")


class DescribeDBPerformanceResponse(AbstractModel):
    """DescribeDBPerformance response structure.

    """

    def __init__(self):
        """
        :param LongQuery: Number of slow queries
        :type LongQuery: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param SelectTotal: Number of SELECT operations
        :type SelectTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param UpdateTotal: Number of UPDATE operations
        :type UpdateTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param InsertTotal: Number of INSERT operations
        :type InsertTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param DeleteTotal: Number of DELETE operations
        :type DeleteTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param MemHitRate: Cache hit rate
        :type MemHitRate: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param DiskIops: Number of disk IOs per second
        :type DiskIops: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param ConnActive: Number of active connections
        :type ConnActive: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param IsMasterSwitched: Whether primary/secondary switch occurred. 1: yes, 0: no
        :type IsMasterSwitched: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param SlaveDelay: primary/secondary delay
        :type SlaveDelay: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LongQuery = None
        self.SelectTotal = None
        self.UpdateTotal = None
        self.InsertTotal = None
        self.DeleteTotal = None
        self.MemHitRate = None
        self.DiskIops = None
        self.ConnActive = None
        self.IsMasterSwitched = None
        self.SlaveDelay = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LongQuery") is not None:
            self.LongQuery = MonitorData()
            self.LongQuery._deserialize(params.get("LongQuery"))
        if params.get("SelectTotal") is not None:
            self.SelectTotal = MonitorData()
            self.SelectTotal._deserialize(params.get("SelectTotal"))
        if params.get("UpdateTotal") is not None:
            self.UpdateTotal = MonitorData()
            self.UpdateTotal._deserialize(params.get("UpdateTotal"))
        if params.get("InsertTotal") is not None:
            self.InsertTotal = MonitorData()
            self.InsertTotal._deserialize(params.get("InsertTotal"))
        if params.get("DeleteTotal") is not None:
            self.DeleteTotal = MonitorData()
            self.DeleteTotal._deserialize(params.get("DeleteTotal"))
        if params.get("MemHitRate") is not None:
            self.MemHitRate = MonitorData()
            self.MemHitRate._deserialize(params.get("MemHitRate"))
        if params.get("DiskIops") is not None:
            self.DiskIops = MonitorData()
            self.DiskIops._deserialize(params.get("DiskIops"))
        if params.get("ConnActive") is not None:
            self.ConnActive = MonitorData()
            self.ConnActive._deserialize(params.get("ConnActive"))
        if params.get("IsMasterSwitched") is not None:
            self.IsMasterSwitched = MonitorData()
            self.IsMasterSwitched._deserialize(params.get("IsMasterSwitched"))
        if params.get("SlaveDelay") is not None:
            self.SlaveDelay = MonitorData()
            self.SlaveDelay._deserialize(params.get("SlaveDelay"))
        self.RequestId = params.get("RequestId")


class DescribeDBResourceUsageDetailsRequest(AbstractModel):
    """DescribeDBResourceUsageDetails request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.
        :type InstanceId: str
        :param StartTime: Start date in the format of `yyyy-mm-dd`
        :type StartTime: str
        :param EndTime: End date in the format of `yyyy-mm-dd`
        :type EndTime: str
        :param MetricName: Name of pulled metric. Valid values: data_disk_available, binlog_disk_available, mem_available, cpu_usage_rate
        :type MetricName: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")


class DescribeDBResourceUsageDetailsResponse(AbstractModel):
    """DescribeDBResourceUsageDetails response structure.

    """

    def __init__(self):
        """
        :param Master: Master node resource usage monitoring node
        :type Master: :class:`tencentcloud.mariadb.v20170312.models.ResourceUsageMonitorSet`
        :param Slave1: Slave 1 resource usage monitoring node
Note: this field may return null, indicating that no valid values can be obtained.
        :type Slave1: :class:`tencentcloud.mariadb.v20170312.models.ResourceUsageMonitorSet`
        :param Slave2: Slave 2 resource usage monitoring node
Note: this field may return null, indicating that no valid values can be obtained.
        :type Slave2: :class:`tencentcloud.mariadb.v20170312.models.ResourceUsageMonitorSet`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Master = None
        self.Slave1 = None
        self.Slave2 = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Master") is not None:
            self.Master = ResourceUsageMonitorSet()
            self.Master._deserialize(params.get("Master"))
        if params.get("Slave1") is not None:
            self.Slave1 = ResourceUsageMonitorSet()
            self.Slave1._deserialize(params.get("Slave1"))
        if params.get("Slave2") is not None:
            self.Slave2 = ResourceUsageMonitorSet()
            self.Slave2._deserialize(params.get("Slave2"))
        self.RequestId = params.get("RequestId")


class DescribeDBResourceUsageRequest(AbstractModel):
    """DescribeDBResourceUsage request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.
        :type InstanceId: str
        :param StartTime: Start date in the format of `yyyy-mm-dd`
        :type StartTime: str
        :param EndTime: End date in the format of `yyyy-mm-dd`
        :type EndTime: str
        :param MetricName: Name of pulled metric. Valid values: data_disk_available, binlog_disk_available, mem_available, cpu_usage_rate
        :type MetricName: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")


class DescribeDBResourceUsageResponse(AbstractModel):
    """DescribeDBResourceUsage response structure.

    """

    def __init__(self):
        """
        :param BinlogDiskAvailable: Available capacity of binlog disk in GB
        :type BinlogDiskAvailable: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param DataDiskAvailable: Available disk capacity in GB
        :type DataDiskAvailable: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param CpuUsageRate: CPU utilization
        :type CpuUsageRate: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param MemAvailable: Available memory size in GB
        :type MemAvailable: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.BinlogDiskAvailable = None
        self.DataDiskAvailable = None
        self.CpuUsageRate = None
        self.MemAvailable = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BinlogDiskAvailable") is not None:
            self.BinlogDiskAvailable = MonitorData()
            self.BinlogDiskAvailable._deserialize(params.get("BinlogDiskAvailable"))
        if params.get("DataDiskAvailable") is not None:
            self.DataDiskAvailable = MonitorData()
            self.DataDiskAvailable._deserialize(params.get("DataDiskAvailable"))
        if params.get("CpuUsageRate") is not None:
            self.CpuUsageRate = MonitorData()
            self.CpuUsageRate._deserialize(params.get("CpuUsageRate"))
        if params.get("MemAvailable") is not None:
            self.MemAvailable = MonitorData()
            self.MemAvailable._deserialize(params.get("MemAvailable"))
        self.RequestId = params.get("RequestId")


class DescribeDBSecurityGroupsRequest(AbstractModel):
    """DescribeDBSecurityGroups request structure.

    """

    def __init__(self):
        """
        :param Product: Database engine name. Valid value: `mariadb`.
        :type Product: str
        :param InstanceId: Instance ID
        :type InstanceId: str
        """
        self.Product = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.InstanceId = params.get("InstanceId")


class DescribeDBSecurityGroupsResponse(AbstractModel):
    """DescribeDBSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param Groups: Security group details
        :type Groups: list of SecurityGroup
        :param VIP: Instance VIP
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type VIP: str
        :param VPort: Instance port
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type VPort: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Groups = None
        self.VIP = None
        self.VPort = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self.Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self.Groups.append(obj)
        self.VIP = params.get("VIP")
        self.VPort = params.get("VPort")
        self.RequestId = params.get("RequestId")


class DescribeDBSlowLogsRequest(AbstractModel):
    """DescribeDBSlowLogs request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.
        :type InstanceId: str
        :param Offset: Data entry number starting from which to return results
        :type Offset: int
        :param Limit: Number of results to be returned
        :type Limit: int
        :param StartTime: Query start time in the format of `2016-07-23 14:55:20`
        :type StartTime: str
        :param EndTime: Query end time in the format of `2016-08-22 14:55:20`
        :type EndTime: str
        :param Db: Specific name of database to be queried
        :type Db: str
        :param OrderBy: Sort by metric. Valid values: query_time_sum, query_count
        :type OrderBy: str
        :param OrderByType: Sorting order. Valid values: desc, asc
        :type OrderByType: str
        :param Slave: Whether to query slow queries of the secondary. 0: primary, 1: secondary
        :type Slave: int
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None
        self.StartTime = None
        self.EndTime = None
        self.Db = None
        self.OrderBy = None
        self.OrderByType = None
        self.Slave = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Db = params.get("Db")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        self.Slave = params.get("Slave")


class DescribeDBSlowLogsResponse(AbstractModel):
    """DescribeDBSlowLogs response structure.

    """

    def __init__(self):
        """
        :param Data: Slow query log data
        :type Data: list of SlowLogData
        :param LockTimeSum: Sum of all statement lock durations
        :type LockTimeSum: float
        :param QueryCount: Total number of statement queries
        :type QueryCount: int
        :param Total: Total number of results
        :type Total: int
        :param QueryTimeSum: Sum of all statement query durations
        :type QueryTimeSum: float
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.LockTimeSum = None
        self.QueryCount = None
        self.Total = None
        self.QueryTimeSum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SlowLogData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.LockTimeSum = params.get("LockTimeSum")
        self.QueryCount = params.get("QueryCount")
        self.Total = params.get("Total")
        self.QueryTimeSum = params.get("QueryTimeSum")
        self.RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    """DescribeDatabases request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of `dcdbt-ow7t8lmc`.
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeDatabasesResponse(AbstractModel):
    """DescribeDatabases response structure.

    """

    def __init__(self):
        """
        :param Databases: List of databases on instance.
        :type Databases: list of Database
        :param InstanceId: Passed through from the input parameters.
        :type InstanceId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Databases = None
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Databases") is not None:
            self.Databases = []
            for item in params.get("Databases"):
                obj = Database()
                obj._deserialize(item)
                self.Databases.append(obj)
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class DescribeFlowRequest(AbstractModel):
    """DescribeFlow request structure.

    """

    def __init__(self):
        """
        :param FlowId: Flow ID returned by async request API.
        :type FlowId: int
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")


class DescribeFlowResponse(AbstractModel):
    """DescribeFlow response structure.

    """

    def __init__(self):
        """
        :param Status: Flow status. 0: succeeded, 1: failed, 2: running
        :type Status: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeInstanceNodeInfoRequest(AbstractModel):
    """DescribeInstanceNodeInfo request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, such as tdsql-6ltok4u9
        :type InstanceId: str
        :param Limit: The maximum number of results returned at a time. By default, there is no upper limit to this value, that is, all results can be returned.
        :type Limit: int
        :param Offset: Offset of the returned results. Default value: `0`.
        :type Offset: int
        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeInstanceNodeInfoResponse(AbstractModel):
    """DescribeInstanceNodeInfo response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of nodes
        :type TotalCount: int
        :param NodesInfo: Node information
        :type NodesInfo: list of NodeInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.NodesInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("NodesInfo") is not None:
            self.NodesInfo = []
            for item in params.get("NodesInfo"):
                obj = NodeInfo()
                obj._deserialize(item)
                self.NodesInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLogFileRetentionPeriodRequest(AbstractModel):
    """DescribeLogFileRetentionPeriod request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeLogFileRetentionPeriodResponse(AbstractModel):
    """DescribeLogFileRetentionPeriod response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.
        :type InstanceId: str
        :param Days: Backup log retention days
        :type Days: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceId = None
        self.Days = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Days = params.get("Days")
        self.RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    """DescribeProjectSecurityGroups request structure.

    """

    def __init__(self):
        """
        :param Product: Database engine name. Valid value: `mariadb`.
        :type Product: str
        :param ProjectId: Project ID
        :type ProjectId: int
        """
        self.Product = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.ProjectId = params.get("ProjectId")


class DescribeProjectSecurityGroupsResponse(AbstractModel):
    """DescribeProjectSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param Groups: Security group details
        :type Groups: list of SecurityGroup
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Groups = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self.Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self.Groups.append(obj)
        self.RequestId = params.get("RequestId")


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups request structure.

    """

    def __init__(self):
        """
        :param Product: Database engine name. Valid value: `mariadb`.
        :type Product: str
        :param SecurityGroupId: Security group ID
        :type SecurityGroupId: str
        :param InstanceIds: Instance ID list, which is an array of one or more instance IDs.
        :type InstanceIds: list of str
        """
        self.Product = None
        self.SecurityGroupId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.InstanceIds = params.get("InstanceIds")


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class GrantAccountPrivilegesRequest(AbstractModel):
    """GrantAccountPrivileges request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :type InstanceId: str
        :param UserName: Login username.
        :type UserName: str
        :param Host: Access host allowed for user. An account is uniquely identified by username and host.
        :type Host: str
        :param DbName: Database name. `\*` indicates that global permissions will be set (i.e., `\*.\*`), in which case the `Type` and `Object ` parameters will be ignored. If `DbName` is not `\*`, the input parameter `Type` is required.
        :type DbName: str
        :param Privileges: Global permission. Valid values: SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, REFERENCES, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, EVENT, TRIGGER, SHOW DATABASES 
Database permission. Valid values: SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, REFERENCES, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, EVENT, TRIGGER 
Table/view permission. Valid values: SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, REFERENCES, INDEX, ALTER, CREATE VIEW, SHOW VIEW, TRIGGER 
Stored procedure/function permission. Valid values: ALTER ROUTINE, EXECUTE 
Field permission. Valid values: INSERT, REFERENCES, SELECT, UPDATE
        :type Privileges: list of str
        :param Type: Type. Valid values: table, view, proc, func, \*. If `DbName` is a specific database name and `Type` is `\*`, the permissions of the database will be set (i.e., `db.\*`), in which case the `Object` parameter will be ignored
        :type Type: str
        :param Object: Type name. For example, if `Type` is `table`, `Object` indicates a specific table name; if both `DbName` and `Type` are specific names, it indicates a specific object name and cannot be `\*` or empty
        :type Object: str
        :param ColName: If `Type` is `table` and `ColName` is `\*`, the permissions will be granted to the table; if `ColName` is a specific field name, the permissions will be granted to the field
        :type ColName: str
        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.DbName = None
        self.Privileges = None
        self.Type = None
        self.Object = None
        self.ColName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.DbName = params.get("DbName")
        self.Privileges = params.get("Privileges")
        self.Type = params.get("Type")
        self.Object = params.get("Object")
        self.ColName = params.get("ColName")


class GrantAccountPrivilegesResponse(AbstractModel):
    """GrantAccountPrivileges response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class InitDBInstancesRequest(AbstractModel):
    """InitDBInstances request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: List of IDs of instances to be initialized. The ID is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :type InstanceIds: list of str
        :param Params: Parameter list. Valid values: character_set_server (character set; required); lower_case_table_names (table name case sensitivity; required; 0: case-sensitive, 1: case-insensitive); innodb_page_size (InnoDB data page; default size: 16 KB); sync_mode (sync mode; 0: async; 1: strong sync; 2: downgradable strong sync; default value: strong sync).
        :type Params: list of DBParamValue
        """
        self.InstanceIds = None
        self.Params = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("Params") is not None:
            self.Params = []
            for item in params.get("Params"):
                obj = DBParamValue()
                obj._deserialize(item)
                self.Params.append(obj)


class InitDBInstancesResponse(AbstractModel):
    """InitDBInstances response structure.

    """

    def __init__(self):
        """
        :param FlowId: Async task ID. The task status can be queried through the `DescribeFlow` API.
        :type FlowId: int
        :param InstanceIds: Passed through from the input parameters.
        :type InstanceIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class LogFileInfo(AbstractModel):
    """Pulled log information

    """

    def __init__(self):
        """
        :param Mtime: Last modified time of log
        :type Mtime: int
        :param Length: File length
        :type Length: int
        :param Uri: Uniform resource identifier (URI) used during log download
        :type Uri: str
        :param FileName: Filename
        :type FileName: str
        """
        self.Mtime = None
        self.Length = None
        self.Uri = None
        self.FileName = None


    def _deserialize(self, params):
        self.Mtime = params.get("Mtime")
        self.Length = params.get("Length")
        self.Uri = params.get("Uri")
        self.FileName = params.get("FileName")


class ModifyAccountDescriptionRequest(AbstractModel):
    """ModifyAccountDescription request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :type InstanceId: str
        :param UserName: Login username.
        :type UserName: str
        :param Host: Access host allowed for user. An account is uniquely identified by username and host.
        :type Host: str
        :param Description: New account remarks, which can contain 0-256 characters.
        :type Description: str
        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.Description = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.Description = params.get("Description")


class ModifyAccountDescriptionResponse(AbstractModel):
    """ModifyAccountDescription response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBackupTimeRequest(AbstractModel):
    """ModifyBackupTime request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :type InstanceId: str
        :param StartBackupTime: Start time of daily backup window in the format of `mm:ss`, such as 22:00
        :type StartBackupTime: str
        :param EndBackupTime: End time of daily backup window in the format of `mm:ss`, such as 23:59
        :type EndBackupTime: str
        """
        self.InstanceId = None
        self.StartBackupTime = None
        self.EndBackupTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartBackupTime = params.get("StartBackupTime")
        self.EndBackupTime = params.get("EndBackupTime")


class ModifyBackupTimeResponse(AbstractModel):
    """ModifyBackupTime response structure.

    """

    def __init__(self):
        """
        :param Status: Setting status. 0: success
        :type Status: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceNameRequest(AbstractModel):
    """ModifyDBInstanceName request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of instance to be modified, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :type InstanceId: str
        :param InstanceName: New name of instance, which can contain letters, digits, underscores, and hyphens.
        :type InstanceName: str
        """
        self.InstanceId = None
        self.InstanceName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")


class ModifyDBInstanceNameResponse(AbstractModel):
    """ModifyDBInstanceName response structure.

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


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups request structure.

    """

    def __init__(self):
        """
        :param Product: Database engine name. Valid value: `mariadb`.
        :type Product: str
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param SecurityGroupIds: List of IDs of security groups to be modified, which is an array of one or more security group IDs.
        :type SecurityGroupIds: list of str
        """
        self.Product = None
        self.InstanceId = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.InstanceId = params.get("InstanceId")
        self.SecurityGroupIds = params.get("SecurityGroupIds")


class ModifyDBInstanceSecurityGroupsResponse(AbstractModel):
    """ModifyDBInstanceSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstancesProjectRequest(AbstractModel):
    """ModifyDBInstancesProject request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: List of IDs of instances to be modified. The ID is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :type InstanceIds: list of str
        :param ProjectId: ID of the project to be assigned, which can be obtained through the `DescribeProjects` API.
        :type ProjectId: int
        """
        self.InstanceIds = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.ProjectId = params.get("ProjectId")


class ModifyDBInstancesProjectResponse(AbstractModel):
    """ModifyDBInstancesProject response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBParametersRequest(AbstractModel):
    """ModifyDBParameters request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.
        :type InstanceId: str
        :param Params: Parameter list. Each element is a combination of `Param` and `Value`.
        :type Params: list of DBParamValue
        """
        self.InstanceId = None
        self.Params = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Params") is not None:
            self.Params = []
            for item in params.get("Params"):
                obj = DBParamValue()
                obj._deserialize(item)
                self.Params.append(obj)


class ModifyDBParametersResponse(AbstractModel):
    """ModifyDBParameters response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.
        :type InstanceId: str
        :param Result: Parameter modification result
        :type Result: list of ParamModifyResult
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceId = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = ParamModifyResult()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyLogFileRetentionPeriodRequest(AbstractModel):
    """ModifyLogFileRetentionPeriod request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.
        :type InstanceId: str
        :param Days: Retention days up to 30
        :type Days: int
        """
        self.InstanceId = None
        self.Days = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Days = params.get("Days")


class ModifyLogFileRetentionPeriodResponse(AbstractModel):
    """ModifyLogFileRetentionPeriod response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.
        :type InstanceId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class MonitorData(AbstractModel):
    """Monitoring data

    """

    def __init__(self):
        """
        :param StartTime: Start time in the format of `2018-03-24 23:59:59`
        :type StartTime: str
        :param EndTime: End time in the format of `2018-03-24 23:59:59`
        :type EndTime: str
        :param Data: Monitoring data
        :type Data: list of float
        """
        self.StartTime = None
        self.EndTime = None
        self.Data = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Data = params.get("Data")


class NodeInfo(AbstractModel):
    """Instance node information

    """

    def __init__(self):
        """
        :param NodeId: Node ID
        :type NodeId: str
        :param Role: Node role. Valid values: `master`, `slave`
        :type Role: str
        """
        self.NodeId = None
        self.Role = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.Role = params.get("Role")


class OpenDBExtranetAccessRequest(AbstractModel):
    """OpenDBExtranetAccess request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of instance for which to enable public network access. The ID is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :type InstanceId: str
        :param Ipv6Flag: Whether IPv6 is used. Default value: 0
        :type Ipv6Flag: int
        """
        self.InstanceId = None
        self.Ipv6Flag = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Ipv6Flag = params.get("Ipv6Flag")


class OpenDBExtranetAccessResponse(AbstractModel):
    """OpenDBExtranetAccess response structure.

    """

    def __init__(self):
        """
        :param FlowId: Async task ID. The task status can be queried through the `DescribeFlow` API.
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ParamConstraint(AbstractModel):
    """Parameter constraint

    """

    def __init__(self):
        """
        :param Type: Constraint type, such as `enum` and `section`
        :type Type: str
        :param Enum: List of valid values when constraint type is `enum`
        :type Enum: str
        :param Range: Range when constraint type is `section`
Note: this field may return null, indicating that no valid values can be obtained.
        :type Range: :class:`tencentcloud.mariadb.v20170312.models.ConstraintRange`
        :param String: List of valid values when constraint type is `string`
        :type String: str
        """
        self.Type = None
        self.Enum = None
        self.Range = None
        self.String = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Enum = params.get("Enum")
        if params.get("Range") is not None:
            self.Range = ConstraintRange()
            self.Range._deserialize(params.get("Range"))
        self.String = params.get("String")


class ParamDesc(AbstractModel):
    """Database parameter description

    """

    def __init__(self):
        """
        :param Param: Parameter name
        :type Param: str
        :param Value: Current parameter value
        :type Value: str
        :param SetValue: Previously set value, which is the same as `value` after the parameter takes effect.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SetValue: str
        :param Default: Default value
        :type Default: str
        :param Constraint: Parameter constraint
        :type Constraint: :class:`tencentcloud.mariadb.v20170312.models.ParamConstraint`
        :param HaveSetValue: Whether a value has been set. false: no, true: yes
        :type HaveSetValue: bool
        """
        self.Param = None
        self.Value = None
        self.SetValue = None
        self.Default = None
        self.Constraint = None
        self.HaveSetValue = None


    def _deserialize(self, params):
        self.Param = params.get("Param")
        self.Value = params.get("Value")
        self.SetValue = params.get("SetValue")
        self.Default = params.get("Default")
        if params.get("Constraint") is not None:
            self.Constraint = ParamConstraint()
            self.Constraint._deserialize(params.get("Constraint"))
        self.HaveSetValue = params.get("HaveSetValue")


class ParamModifyResult(AbstractModel):
    """Parameter modification result

    """

    def __init__(self):
        """
        :param Param: Renames a parameter
        :type Param: str
        :param Code: Result of parameter modification. 0: success, -1: failure, -2: invalid parameter value
        :type Code: int
        """
        self.Param = None
        self.Code = None


    def _deserialize(self, params):
        self.Param = params.get("Param")
        self.Code = params.get("Code")


class PerformanceMonitorSet(AbstractModel):
    """Set of database performance monitoring metrics

    """

    def __init__(self):
        """
        :param UpdateTotal: Number of UPDATE operations
        :type UpdateTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param DiskIops: Number of disk IOs per second
        :type DiskIops: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param ConnActive: Number of active connections
        :type ConnActive: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param MemHitRate: Cache hit rate
        :type MemHitRate: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param SlaveDelay: Primary/Secondary delay
        :type SlaveDelay: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param SelectTotal: Number of SELECT operations
        :type SelectTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param LongQuery: Number of slow queries
        :type LongQuery: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param DeleteTotal: Number of DELETE operations
        :type DeleteTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param InsertTotal: Number of INSERT operations
        :type InsertTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param IsMasterSwitched: Whether primary/Secondary switch occurred. 1: yes, 0: no
        :type IsMasterSwitched: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        """
        self.UpdateTotal = None
        self.DiskIops = None
        self.ConnActive = None
        self.MemHitRate = None
        self.SlaveDelay = None
        self.SelectTotal = None
        self.LongQuery = None
        self.DeleteTotal = None
        self.InsertTotal = None
        self.IsMasterSwitched = None


    def _deserialize(self, params):
        if params.get("UpdateTotal") is not None:
            self.UpdateTotal = MonitorData()
            self.UpdateTotal._deserialize(params.get("UpdateTotal"))
        if params.get("DiskIops") is not None:
            self.DiskIops = MonitorData()
            self.DiskIops._deserialize(params.get("DiskIops"))
        if params.get("ConnActive") is not None:
            self.ConnActive = MonitorData()
            self.ConnActive._deserialize(params.get("ConnActive"))
        if params.get("MemHitRate") is not None:
            self.MemHitRate = MonitorData()
            self.MemHitRate._deserialize(params.get("MemHitRate"))
        if params.get("SlaveDelay") is not None:
            self.SlaveDelay = MonitorData()
            self.SlaveDelay._deserialize(params.get("SlaveDelay"))
        if params.get("SelectTotal") is not None:
            self.SelectTotal = MonitorData()
            self.SelectTotal._deserialize(params.get("SelectTotal"))
        if params.get("LongQuery") is not None:
            self.LongQuery = MonitorData()
            self.LongQuery._deserialize(params.get("LongQuery"))
        if params.get("DeleteTotal") is not None:
            self.DeleteTotal = MonitorData()
            self.DeleteTotal._deserialize(params.get("DeleteTotal"))
        if params.get("InsertTotal") is not None:
            self.InsertTotal = MonitorData()
            self.InsertTotal._deserialize(params.get("InsertTotal"))
        if params.get("IsMasterSwitched") is not None:
            self.IsMasterSwitched = MonitorData()
            self.IsMasterSwitched._deserialize(params.get("IsMasterSwitched"))


class ResetAccountPasswordRequest(AbstractModel):
    """ResetAccountPassword request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.
        :type InstanceId: str
        :param UserName: Login username.
        :type UserName: str
        :param Host: Access host allowed for user. An account is uniquely identified by username and host.
        :type Host: str
        :param Password: New password, which can contain 6-32 letters, digits, and common symbols but not semicolons, single quotation marks, and double quotation marks.
        :type Password: str
        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.Password = params.get("Password")


class ResetAccountPasswordResponse(AbstractModel):
    """ResetAccountPassword response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResourceUsageMonitorSet(AbstractModel):
    """Set of database resource usage monitoring metrics

    """

    def __init__(self):
        """
        :param BinlogDiskAvailable: Available capacity of binlog disk in GB
        :type BinlogDiskAvailable: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param CpuUsageRate: CPU utilization
        :type CpuUsageRate: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param MemAvailable: Available memory size in GB
        :type MemAvailable: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param DataDiskAvailable: Available disk capacity in GB
        :type DataDiskAvailable: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        """
        self.BinlogDiskAvailable = None
        self.CpuUsageRate = None
        self.MemAvailable = None
        self.DataDiskAvailable = None


    def _deserialize(self, params):
        if params.get("BinlogDiskAvailable") is not None:
            self.BinlogDiskAvailable = MonitorData()
            self.BinlogDiskAvailable._deserialize(params.get("BinlogDiskAvailable"))
        if params.get("CpuUsageRate") is not None:
            self.CpuUsageRate = MonitorData()
            self.CpuUsageRate._deserialize(params.get("CpuUsageRate"))
        if params.get("MemAvailable") is not None:
            self.MemAvailable = MonitorData()
            self.MemAvailable._deserialize(params.get("MemAvailable"))
        if params.get("DataDiskAvailable") is not None:
            self.DataDiskAvailable = MonitorData()
            self.DataDiskAvailable._deserialize(params.get("DataDiskAvailable"))


class SecurityGroup(AbstractModel):
    """Security group details

    """

    def __init__(self):
        """
        :param ProjectId: Project ID
        :type ProjectId: int
        :param CreateTime: Creation time in the format of yyyy-mm-dd hh:mm:ss
        :type CreateTime: str
        :param SecurityGroupId: Security group ID
        :type SecurityGroupId: str
        :param SecurityGroupName: Security group name
        :type SecurityGroupName: str
        :param SecurityGroupRemark: Security group remarks
        :type SecurityGroupRemark: str
        :param Inbound: Inbound rule
        :type Inbound: list of SecurityGroupBound
        :param Outbound: Outbound rule
        :type Outbound: list of SecurityGroupBound
        """
        self.ProjectId = None
        self.CreateTime = None
        self.SecurityGroupId = None
        self.SecurityGroupName = None
        self.SecurityGroupRemark = None
        self.Inbound = None
        self.Outbound = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.CreateTime = params.get("CreateTime")
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.SecurityGroupName = params.get("SecurityGroupName")
        self.SecurityGroupRemark = params.get("SecurityGroupRemark")
        if params.get("Inbound") is not None:
            self.Inbound = []
            for item in params.get("Inbound"):
                obj = SecurityGroupBound()
                obj._deserialize(item)
                self.Inbound.append(obj)
        if params.get("Outbound") is not None:
            self.Outbound = []
            for item in params.get("Outbound"):
                obj = SecurityGroupBound()
                obj._deserialize(item)
                self.Outbound.append(obj)


class SecurityGroupBound(AbstractModel):
    """Security group inbound/outbound rule

    """

    def __init__(self):
        """
        :param Action: Policy, which can be `ACCEPT` or `DROP`
        :type Action: str
        :param CidrIp: Source IP or source IP range, such as 192.168.0.0/16
        :type CidrIp: str
        :param PortRange: Port
        :type PortRange: str
        :param IpProtocol: Network protocol. UDP and TCP are supported.
        :type IpProtocol: str
        """
        self.Action = None
        self.CidrIp = None
        self.PortRange = None
        self.IpProtocol = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.CidrIp = params.get("CidrIp")
        self.PortRange = params.get("PortRange")
        self.IpProtocol = params.get("IpProtocol")


class SlowLogData(AbstractModel):
    """Slow query entry information

    """

    def __init__(self):
        """
        :param CheckSum: Statement checksum for querying details
        :type CheckSum: str
        :param Db: Database name
        :type Db: str
        :param FingerPrint: Abstracted SQL statement
        :type FingerPrint: str
        :param LockTimeAvg: Average lock duration
        :type LockTimeAvg: str
        :param LockTimeMax: Maximum lock duration
        :type LockTimeMax: str
        :param LockTimeMin: Minimum lock duration
        :type LockTimeMin: str
        :param LockTimeSum: Sum of lock durations
        :type LockTimeSum: str
        :param QueryCount: Number of queries
        :type QueryCount: str
        :param QueryTimeAvg: Average query duration
        :type QueryTimeAvg: str
        :param QueryTimeMax: Maximum query duration
        :type QueryTimeMax: str
        :param QueryTimeMin: Minimum query duration
        :type QueryTimeMin: str
        :param QueryTimeSum: Sum of query durations
        :type QueryTimeSum: str
        :param RowsExaminedSum: Number of scanned rows
        :type RowsExaminedSum: str
        :param RowsSentSum: Number of sent rows
        :type RowsSentSum: str
        :param TsMax: Last execution time
        :type TsMax: str
        :param TsMin: First execution time
        :type TsMin: str
        :param User: Account
        :type User: str
        :param ExampleSql: Sample SQL
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExampleSql: str
        """
        self.CheckSum = None
        self.Db = None
        self.FingerPrint = None
        self.LockTimeAvg = None
        self.LockTimeMax = None
        self.LockTimeMin = None
        self.LockTimeSum = None
        self.QueryCount = None
        self.QueryTimeAvg = None
        self.QueryTimeMax = None
        self.QueryTimeMin = None
        self.QueryTimeSum = None
        self.RowsExaminedSum = None
        self.RowsSentSum = None
        self.TsMax = None
        self.TsMin = None
        self.User = None
        self.ExampleSql = None


    def _deserialize(self, params):
        self.CheckSum = params.get("CheckSum")
        self.Db = params.get("Db")
        self.FingerPrint = params.get("FingerPrint")
        self.LockTimeAvg = params.get("LockTimeAvg")
        self.LockTimeMax = params.get("LockTimeMax")
        self.LockTimeMin = params.get("LockTimeMin")
        self.LockTimeSum = params.get("LockTimeSum")
        self.QueryCount = params.get("QueryCount")
        self.QueryTimeAvg = params.get("QueryTimeAvg")
        self.QueryTimeMax = params.get("QueryTimeMax")
        self.QueryTimeMin = params.get("QueryTimeMin")
        self.QueryTimeSum = params.get("QueryTimeSum")
        self.RowsExaminedSum = params.get("RowsExaminedSum")
        self.RowsSentSum = params.get("RowsSentSum")
        self.TsMax = params.get("TsMax")
        self.TsMin = params.get("TsMin")
        self.User = params.get("User")
        self.ExampleSql = params.get("ExampleSql")