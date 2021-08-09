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
    """TencentDB account information

    """

    def __init__(self):
        """
        :param User: Account name\n        :type User: str\n        :param Host: Host address\n        :type Host: str\n        """
        self.User = None
        self.Host = None


    def _deserialize(self, params):
        self.User = params.get("User")
        self.Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups request structure.

    """

    def __init__(self):
        """
        :param Product: Database engine name. Valid value: `mariadb`.\n        :type Product: str\n        :param SecurityGroupId: ID of the security group to be associated in the format of sg-efil73jd.\n        :type SecurityGroupId: str\n        :param InstanceIds: ID(s) of the instance(s) to be associated in the format of tdsql-lesecurk. You can specify multiple instances.\n        :type InstanceIds: list of str\n        """
        self.Product = None
        self.SecurityGroupId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CancelDcnJobRequest(AbstractModel):
    """CancelDcnJob request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Disaster recovery instance ID\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelDcnJobResponse(AbstractModel):
    """CancelDcnJob response structure.

    """

    def __init__(self):
        """
        :param FlowId: Task ID\n        :type FlowId: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CloneAccountRequest(AbstractModel):
    """CloneAccount request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param SrcUser: Source user account name\n        :type SrcUser: str\n        :param SrcHost: Source user host\n        :type SrcHost: str\n        :param DstUser: Target user account name\n        :type DstUser: str\n        :param DstHost: Target user host\n        :type DstHost: str\n        :param DstDesc: Description of target account\n        :type DstDesc: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneAccountResponse(AbstractModel):
    """CloneAccount response structure.

    """

    def __init__(self):
        """
        :param FlowId: Async task flow ID.\n        :type FlowId: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: ID of instance for which to disable public network access. The ID is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.\n        :type InstanceId: str\n        :param Ipv6Flag: Whether IPv6 is used. Default value: 0\n        :type Ipv6Flag: int\n        """
        self.InstanceId = None
        self.Ipv6Flag = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Ipv6Flag = params.get("Ipv6Flag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseDBExtranetAccessResponse(AbstractModel):
    """CloseDBExtranetAccess response structure.

    """

    def __init__(self):
        """
        :param FlowId: Async task ID. The task status can be queried through the `DescribeFlow` API.\n        :type FlowId: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ColumnPrivilege(AbstractModel):
    """Column permission information

    """

    def __init__(self):
        """
        :param Database: Database name\n        :type Database: str\n        :param Table: Table name\n        :type Table: str\n        :param Column: Column name\n        :type Column: str\n        :param Privileges: Permission information\n        :type Privileges: list of str\n        """
        self.Database = None
        self.Table = None
        self.Column = None
        self.Privileges = None


    def _deserialize(self, params):
        self.Database = params.get("Database")
        self.Table = params.get("Table")
        self.Column = params.get("Column")
        self.Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConstraintRange(AbstractModel):
    """Range of constraint type values

    """

    def __init__(self):
        """
        :param Min: Minimum value when constraint type is `section`\n        :type Min: str\n        :param Max: Maximum value when constraint type is `section`\n        :type Max: str\n        """
        self.Min = None
        self.Max = None


    def _deserialize(self, params):
        self.Min = params.get("Min")
        self.Max = params.get("Max")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyAccountPrivilegesRequest(AbstractModel):
    """CopyAccountPrivileges request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.\n        :type InstanceId: str\n        :param SrcUserName: Source username\n        :type SrcUserName: str\n        :param SrcHost: Access host allowed for source user\n        :type SrcHost: str\n        :param DstUserName: Target username\n        :type DstUserName: str\n        :param DstHost: Access host allowed for target user\n        :type DstHost: str\n        :param SrcReadOnly: `ReadOnly` attribute of source account\n        :type SrcReadOnly: str\n        :param DstReadOnly: `ReadOnly` attribute of target account\n        :type DstReadOnly: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyAccountPrivilegesResponse(AbstractModel):
    """CopyAccountPrivileges response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAccountRequest(AbstractModel):
    """CreateAccount request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.\n        :type InstanceId: str\n        :param UserName: Login username, which can contain 1-32 letters, digits, underscores, and hyphens.\n        :type UserName: str\n        :param Host: Host that can be logged in to, which is in the same format as the host of the MySQL account and supports wildcards, such as %, 10.%, and 10.20.%.\n        :type Host: str\n        :param Password: Account password, which can contain 6-32 letters, digits, and common symbols but not semicolons, single quotation marks, and double quotation marks.\n        :type Password: str\n        :param ReadOnly: Whether to create a read-only account. 0: no; 1: for the account's SQL requests, the secondary will be used first, and if it is unavailable, the primary will be used; 2: the secondary will be used first, and if it is unavailable, the operation will fail.\n        :type ReadOnly: int\n        :param Description: Account remarks, which can contain 0-256 letters, digits, and common symbols.\n        :type Description: str\n        :param DelayThresh: Determines whether the secondary is unavailable based on the passed-in time\n        :type DelayThresh: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountResponse(AbstractModel):
    """CreateAccount response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, which is passed through from the input parameters.\n        :type InstanceId: str\n        :param UserName: Username, which is passed through from the input parameters.\n        :type UserName: str\n        :param Host: Host allowed for access, which is passed through from the input parameters.\n        :type Host: str\n        :param ReadOnly: Passed through from the input parameters.\n        :type ReadOnly: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param UserName: Username\n        :type UserName: str\n        :param Host: Host from which a user can log in (corresponding to the `host` field for a MySQL user; a user is uniquely identified by username and host; this parameter is in IP format and ends with % for IP range; % can be entered; if this parameter is left empty, % will be used by default)\n        :type Host: str\n        :param Description: User remarks\n        :type Description: str\n        :param CreateTime: Creation time\n        :type CreateTime: str\n        :param UpdateTime: Last updated time\n        :type UpdateTime: str\n        :param ReadOnly: Read-only flag. 0: no; 1: for the account's SQL requests, the secondary will be used first, and if it is unavailable, the primary will be used; 2: the secondary will be used first, and if it is unavailable, the operation will fail.\n        :type ReadOnly: int\n        :param DelayThresh: This field is meaningful for read-only accounts, indicating to select a secondary where the primary/secondary delay is below this value
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DelayThresh: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBBackupTimeConfig(AbstractModel):
    """TencentDB instance backup time configuration information

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param StartBackupTime: Start time of daily backup window in the format of `mm:ss`, such as 22:00\n        :type StartBackupTime: str\n        :param EndBackupTime: End time of daily backup window in the format of `mm:ss`, such as 23:00\n        :type EndBackupTime: str\n        """
        self.InstanceId = None
        self.StartBackupTime = None
        self.EndBackupTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartBackupTime = params.get("StartBackupTime")
        self.EndBackupTime = params.get("EndBackupTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBInstance(AbstractModel):
    """TencentDB instance details.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, which uniquely identifies a TDSQL instance\n        :type InstanceId: str\n        :param InstanceName: Customizable instance name\n        :type InstanceName: str\n        :param AppId: Application ID of instance\n        :type AppId: int\n        :param ProjectId: Project ID of instance\n        :type ProjectId: int\n        :param Region: Instance region name, such as ap-shanghai\n        :type Region: str\n        :param Zone: Instance AZ name, such as ap-guangzhou-1\n        :type Zone: str\n        :param VpcId: VPC ID, which is 0 if the basic network is used\n        :type VpcId: int\n        :param SubnetId: Subnet ID, which is 0 if the basic network is used\n        :type SubnetId: int\n        :param Status: Instance status. Valid values: `0` (creating), `1` (running task), `2` (running), `3` (uninitialized), `-1` (isolated), `4` (initializing), `5` (eliminating), `6` (restarting), `7` (migrating data)\n        :type Status: int\n        :param Vip: Private IP address\n        :type Vip: str\n        :param Vport: Private network port\n        :type Vport: int\n        :param WanDomain: Domain name for public network access, which can be resolved by the public network\n        :type WanDomain: str\n        :param WanVip: Public IP address, which can be accessed over the public network\n        :type WanVip: str\n        :param WanPort: Public network port\n        :type WanPort: int\n        :param CreateTime: Instance creation time in the format of `2006-01-02 15:04:05`\n        :type CreateTime: str\n        :param UpdateTime: Last updated time of instance in the format of `2006-01-02 15:04:05`\n        :type UpdateTime: str\n        :param AutoRenewFlag: Auto-renewal flag. 0: no, 1: yes\n        :type AutoRenewFlag: int\n        :param PeriodEndTime: Instance expiration time in the format of `2006-01-02 15:04:05`\n        :type PeriodEndTime: str\n        :param Uin: Instance account\n        :type Uin: str\n        :param TdsqlVersion: TDSQL version information\n        :type TdsqlVersion: str\n        :param Memory: Instance memory size in GB\n        :type Memory: int\n        :param Storage: Instance storage capacity in GB\n        :type Storage: int\n        :param UniqueVpcId: VPC ID in string type\n        :type UniqueVpcId: str\n        :param UniqueSubnetId: VPC subnet ID in string type\n        :type UniqueSubnetId: str\n        :param OriginSerialId: Original ID of instance (this field is obsolete and should not be depended on)\n        :type OriginSerialId: str\n        :param NodeCount: Number of nodes. 2: one master and one slave, 3: one master and two slaves\n        :type NodeCount: int\n        :param IsTmp: Whether it is a temp instance. 0: no, non-zero value: yes\n        :type IsTmp: int\n        :param ExclusterId: Dedicated cluster ID. If this parameter is empty, the instance is a general instance\n        :type ExclusterId: str\n        :param Id: Numeric ID of instance (this field is obsolete and should not be depended on)\n        :type Id: int\n        :param Pid: Product type ID\n        :type Pid: int\n        :param Qps: Maximum QPS value\n        :type Qps: int\n        :param Paymode: Billing mode
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Paymode: str\n        :param Locker: Async task flow ID when an async task is in progress on an instance
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Locker: int\n        :param StatusDesc: Current instance running status description
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StatusDesc: str\n        :param WanStatus: Public network access status. 0: not enabled, 1: enabled, 2: disabled, 3: enabling\n        :type WanStatus: int\n        :param IsAuditSupported: Whether the instance supports audit. 1: yes, 0: no\n        :type IsAuditSupported: int\n        :param Machine: Model\n        :type Machine: str\n        :param IsEncryptSupported: Whether data encryption is supported. 1: yes, 0: no\n        :type IsEncryptSupported: int\n        :param Cpu: Number of CPU cores of instance\n        :type Cpu: int\n        :param Ipv6Flag: Indicates whether the instance uses IPv6
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Ipv6Flag: int\n        :param Vipv6: Private network IPv6 address
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Vipv6: str\n        :param WanVipv6: Public network IPv6 address
Note: this field may return null, indicating that no valid values can be obtained.\n        :type WanVipv6: str\n        :param WanPortIpv6: Public network IPv6 port
Note: this field may return null, indicating that no valid values can be obtained.\n        :type WanPortIpv6: int\n        :param WanStatusIpv6: Public network IPv6 status
Note: this field may return null, indicating that no valid values can be obtained.\n        :type WanStatusIpv6: int\n        :param DbEngine: Database engine
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DbEngine: str\n        :param DbVersion: Database version
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DbVersion: str\n        :param DcnFlag: DCN type. Valid values: 0 (null), 1 (primary instance), 2 (disaster recovery instance)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DcnFlag: int\n        :param DcnStatus: DCN status. Valid values: 0 (null), 1 (creating), 2 (syncing), 3 (disconnected)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DcnStatus: int\n        :param DcnDstNum: The number of DCN disaster recovery instances
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DcnDstNum: int\n        :param InstanceType: Instance type. Valid values: `1` (dedicated primary instance), `2` (primary instance), `3` (disaster recovery instance), and `4` (dedicated disaster recovery instance).
Note: this field may return null, indicating that no valid values can be obtained.\n        :type InstanceType: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBParamValue(AbstractModel):
    """TencentDB parameter information.

    """

    def __init__(self):
        """
        :param Param: Parameter name\n        :type Param: str\n        :param Value: Parameter value\n        :type Value: str\n        """
        self.Param = None
        self.Value = None


    def _deserialize(self, params):
        self.Param = params.get("Param")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Database(AbstractModel):
    """Database information

    """

    def __init__(self):
        """
        :param DbName: Database name\n        :type DbName: str\n        """
        self.DbName = None


    def _deserialize(self, params):
        self.DbName = params.get("DbName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabasePrivilege(AbstractModel):
    """Database permission

    """

    def __init__(self):
        """
        :param Privileges: Permission information\n        :type Privileges: list of str\n        :param Database: Database name\n        :type Database: str\n        """
        self.Privileges = None
        self.Database = None


    def _deserialize(self, params):
        self.Privileges = params.get("Privileges")
        self.Database = params.get("Database")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DcnDetailItem(AbstractModel):
    """DCN details

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param InstanceName: Instance name\n        :type InstanceName: str\n        :param Region: Region where the instance resides\n        :type Region: str\n        :param Zone: Availability zone where the instance resides\n        :type Zone: str\n        :param Vip: Instance IP address\n        :type Vip: str\n        :param Vipv6: Instance IPv6 address\n        :type Vipv6: str\n        :param Vport: Instance port\n        :type Vport: int\n        :param Status: Instance status\n        :type Status: int\n        :param StatusDesc: Instance status description\n        :type StatusDesc: str\n        :param DcnFlag: DCN flag. Valid values: `1` (primary), `2` (disaster recovery)\n        :type DcnFlag: int\n        :param DcnStatus: DCN status. Valid values: `0` (none), `1` (creating), `2` (syncing), `3` (disconnected)\n        :type DcnStatus: int\n        :param Cpu: Number of CPU cores of the instance\n        :type Cpu: int\n        :param Memory: Instance memory capacity in GB\n        :type Memory: int\n        :param Storage: Instance storage capacity in GB\n        :type Storage: int\n        :param PayMode: Billing mode\n        :type PayMode: int\n        :param CreateTime: Creation time of the instance in the format of 2006-01-02 15:04:05\n        :type CreateTime: str\n        :param PeriodEndTime: Expiration time of the instance in the format of 2006-01-02 15:04:05\n        :type PeriodEndTime: str\n        :param InstanceType: Instance type. Valid values: `1` (dedicated primary instance), `2` (non-dedicated primary instance), `3` (non-dedicated disaster recovery instance), `4` (dedicated disaster recovery instance)\n        :type InstanceType: int\n        """
        self.InstanceId = None
        self.InstanceName = None
        self.Region = None
        self.Zone = None
        self.Vip = None
        self.Vipv6 = None
        self.Vport = None
        self.Status = None
        self.StatusDesc = None
        self.DcnFlag = None
        self.DcnStatus = None
        self.Cpu = None
        self.Memory = None
        self.Storage = None
        self.PayMode = None
        self.CreateTime = None
        self.PeriodEndTime = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.Vip = params.get("Vip")
        self.Vipv6 = params.get("Vipv6")
        self.Vport = params.get("Vport")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.DcnFlag = params.get("DcnFlag")
        self.DcnStatus = params.get("DcnStatus")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.PayMode = params.get("PayMode")
        self.CreateTime = params.get("CreateTime")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountRequest(AbstractModel):
    """DeleteAccount request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.\n        :type InstanceId: str\n        :param UserName: Username\n        :type UserName: str\n        :param Host: Access host allowed for user\n        :type Host: str\n        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountResponse(AbstractModel):
    """DeleteAccount response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccountPrivilegesRequest(AbstractModel):
    """DescribeAccountPrivileges request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.\n        :type InstanceId: str\n        :param UserName: Login username.\n        :type UserName: str\n        :param Host: Access host allowed for user. An account is uniquely identified by username and host.\n        :type Host: str\n        :param DbName: Database name. `\*` indicates that global permissions will be queried (i.e., `\*.\*`), in which case the `Type` and `Object ` parameters will be ignored\n        :type DbName: str\n        :param Type: Type. Valid values: table, view, proc, func, \*. If `DbName` is a specific database name and `Type` is `\*`, the permissions of the database will be queried (i.e., `db.\*`), in which case the `Object` parameter will be ignored\n        :type Type: str\n        :param Object: Type name. For example, if `Type` is `table`, `Object` indicates a specific table name; if both `DbName` and `Type` are specific names, it indicates a specific object name and cannot be `\*` or empty\n        :type Object: str\n        :param ColName: If `Type` is `table` and `ColName` is `\*`, the permissions of the table will be queried; if `ColName` is a specific field name, the permissions of the corresponding field will be queried\n        :type ColName: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountPrivilegesResponse(AbstractModel):
    """DescribeAccountPrivileges response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param Privileges: Permission list.\n        :type Privileges: list of str\n        :param UserName: Database account username\n        :type UserName: str\n        :param Host: Database account host\n        :type Host: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, which is passed through from the input parameters.\n        :type InstanceId: str\n        :param Users: Instance user list.\n        :type Users: list of DBAccount\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceIds: Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.\n        :type InstanceIds: list of str\n        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupTimeResponse(AbstractModel):
    """DescribeBackupTime response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of returned configurations\n        :type TotalCount: int\n        :param Items: Instance backup time configuration information
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Items: list of DBBackupTimeConfig\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceIds: Queries by instance ID or IDs. Instance ID is in the format of `tdsql-ow728lmc`. Up to 100 instances can be queried in one request.\n        :type InstanceIds: list of str\n        :param SearchName: Search field name. Valid values: instancename (search by instance name), vip (search by private IP), all (search by instance ID, instance name, and private IP).\n        :type SearchName: str\n        :param SearchKey: Search keyword. Fuzzy search is supported. Multiple keywords should be separated by line breaks (`\n`).\n        :type SearchKey: str\n        :param ProjectIds: Queries by project ID\n        :type ProjectIds: list of int\n        :param IsFilterVpc: Whether to search by VPC\n        :type IsFilterVpc: bool\n        :param VpcId: VPC ID, which is valid when `IsFilterVpc` is 1\n        :type VpcId: str\n        :param SubnetId: VPC subnet ID, which is valid when `IsFilterVpc` is 1\n        :type SubnetId: str\n        :param OrderBy: Sort by field. Valid values: projectId, createtime, instancename\n        :type OrderBy: str\n        :param OrderByType: Sorting order. Valid values: desc, asc\n        :type OrderByType: str\n        :param Offset: Offset. Default value: 0\n        :type Offset: int\n        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100.\n        :type Limit: int\n        :param OriginSerialIds: Queries by `OriginSerialId`\n        :type OriginSerialIds: list of str\n        :param IsFilterExcluster: Identifies whether to use the `ExclusterType` field. false: no, true: yes\n        :type IsFilterExcluster: bool\n        :param ExclusterType: Instance cluster type. 1: non-dedicated cluster, 2: dedicated cluster, 0: all\n        :type ExclusterType: int\n        :param ExclusterIds: Filters instances by dedicated cluster ID in the format of `dbdc-4ih6uct9`\n        :type ExclusterIds: list of str\n        :param TagKeys: Tag key used in queries\n        :type TagKeys: list of str\n        :param FilterInstanceType: Instance types used in filtering. Valid values: 1 (dedicated instance), 2 (primary instance), 3 (disaster recovery instance). Multiple values should be separated by commas.\n        :type FilterInstanceType: str\n        :param Status: Use this filter to include instances in specific statuses\n        :type Status: list of int\n        :param ExcludeStatus: Use this filter to exclude instances in specific statuses\n        :type ExcludeStatus: list of int\n        """
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
        self.Status = None
        self.ExcludeStatus = None


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
        self.Status = params.get("Status")
        self.ExcludeStatus = params.get("ExcludeStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstancesResponse(AbstractModel):
    """DescribeDBInstances response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible instances\n        :type TotalCount: int\n        :param Instances: Instance details list\n        :type Instances: list of DBInstance\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.\n        :type InstanceId: str\n        :param Type: Requested log type. Valid values: 1 (binlog), 2 (cold backup), 3 (errlog), 4 (slowlog).\n        :type Type: int\n        """
        self.InstanceId = None
        self.Type = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBLogFilesResponse(AbstractModel):
    """DescribeDBLogFiles response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.\n        :type InstanceId: str\n        :param Type: Requested log type. Valid values: 1 (binlog), 2 (cold backup), 3 (errlog), 4 (slowlog).\n        :type Type: int\n        :param Total: Total number of requested logs\n        :type Total: int\n        :param Files: Information such as `uri`, `length`, and `mtime` (modification time)\n        :type Files: list of LogFileInfo\n        :param VpcPrefix: For an instance in a VPC, this prefix plus URI can be used as the download address\n        :type VpcPrefix: str\n        :param NormalPrefix: For an instance in a common network, this prefix plus URI can be used as the download address\n        :type NormalPrefix: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBParametersResponse(AbstractModel):
    """DescribeDBParameters response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.\n        :type InstanceId: str\n        :param Params: Requests the current parameter values of database\n        :type Params: list of ParamDesc\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.\n        :type InstanceId: str\n        :param StartTime: Start date in the format of `yyyy-mm-dd`\n        :type StartTime: str\n        :param EndTime: End date in the format of `yyyy-mm-dd`\n        :type EndTime: str\n        :param MetricName: Name of pulled metric. Valid values: long_query, select_total, update_total, insert_total, delete_total, mem_hit_rate, disk_iops, conn_active, is_master_switched, slave_delay\n        :type MetricName: str\n        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBPerformanceDetailsResponse(AbstractModel):
    """DescribeDBPerformanceDetails response structure.

    """

    def __init__(self):
        """
        :param Master: Master node performance monitoring data\n        :type Master: :class:`tencentcloud.mariadb.v20170312.models.PerformanceMonitorSet`\n        :param Slave1: Slave 1 performance monitoring data
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Slave1: :class:`tencentcloud.mariadb.v20170312.models.PerformanceMonitorSet`\n        :param Slave2: Slave 2 performance monitoring data. If the instance is one-primary-one-secondary, it does not have this field
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Slave2: :class:`tencentcloud.mariadb.v20170312.models.PerformanceMonitorSet`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.\n        :type InstanceId: str\n        :param StartTime: Start date in the format of `yyyy-mm-dd`\n        :type StartTime: str\n        :param EndTime: End date in the format of `yyyy-mm-dd`\n        :type EndTime: str\n        :param MetricName: Name of pulled metric. Valid values: long_query, select_total, update_total, insert_total, delete_total, mem_hit_rate, disk_iops, conn_active, is_master_switched, slave_delay\n        :type MetricName: str\n        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBPerformanceResponse(AbstractModel):
    """DescribeDBPerformance response structure.

    """

    def __init__(self):
        """
        :param LongQuery: Number of slow queries\n        :type LongQuery: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param SelectTotal: Number of SELECT operations\n        :type SelectTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param UpdateTotal: Number of UPDATE operations\n        :type UpdateTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param InsertTotal: Number of INSERT operations\n        :type InsertTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param DeleteTotal: Number of DELETE operations\n        :type DeleteTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param MemHitRate: Cache hit rate\n        :type MemHitRate: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param DiskIops: Number of disk IOs per second\n        :type DiskIops: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param ConnActive: Number of active connections\n        :type ConnActive: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param IsMasterSwitched: Whether primary/secondary switch occurred. 1: yes, 0: no\n        :type IsMasterSwitched: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param SlaveDelay: primary/secondary delay\n        :type SlaveDelay: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.\n        :type InstanceId: str\n        :param StartTime: Start date in the format of `yyyy-mm-dd`\n        :type StartTime: str\n        :param EndTime: End date in the format of `yyyy-mm-dd`\n        :type EndTime: str\n        :param MetricName: Name of pulled metric. Valid values: data_disk_available, binlog_disk_available, mem_available, cpu_usage_rate\n        :type MetricName: str\n        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBResourceUsageDetailsResponse(AbstractModel):
    """DescribeDBResourceUsageDetails response structure.

    """

    def __init__(self):
        """
        :param Master: Master node resource usage monitoring node\n        :type Master: :class:`tencentcloud.mariadb.v20170312.models.ResourceUsageMonitorSet`\n        :param Slave1: Slave 1 resource usage monitoring node
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Slave1: :class:`tencentcloud.mariadb.v20170312.models.ResourceUsageMonitorSet`\n        :param Slave2: Slave 2 resource usage monitoring node
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Slave2: :class:`tencentcloud.mariadb.v20170312.models.ResourceUsageMonitorSet`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.\n        :type InstanceId: str\n        :param StartTime: Start date in the format of `yyyy-mm-dd`\n        :type StartTime: str\n        :param EndTime: End date in the format of `yyyy-mm-dd`\n        :type EndTime: str\n        :param MetricName: Name of pulled metric. Valid values: data_disk_available, binlog_disk_available, mem_available, cpu_usage_rate\n        :type MetricName: str\n        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBResourceUsageResponse(AbstractModel):
    """DescribeDBResourceUsage response structure.

    """

    def __init__(self):
        """
        :param BinlogDiskAvailable: Available capacity of binlog disk in GB\n        :type BinlogDiskAvailable: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param DataDiskAvailable: Available disk capacity in GB\n        :type DataDiskAvailable: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param CpuUsageRate: CPU utilization\n        :type CpuUsageRate: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param MemAvailable: Available memory size in GB\n        :type MemAvailable: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Product: Database engine name. Valid value: `mariadb`.\n        :type Product: str\n        :param InstanceId: Instance ID\n        :type InstanceId: str\n        """
        self.Product = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSecurityGroupsResponse(AbstractModel):
    """DescribeDBSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param Groups: Security group details\n        :type Groups: list of SecurityGroup\n        :param VIP: Instance VIP
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type VIP: str\n        :param VPort: Instance port
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type VPort: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.\n        :type InstanceId: str\n        :param Offset: Data entry number starting from which to return results\n        :type Offset: int\n        :param Limit: Number of results to be returned\n        :type Limit: int\n        :param StartTime: Query start time in the format of `2016-07-23 14:55:20`\n        :type StartTime: str\n        :param EndTime: Query end time in the format of `2016-08-22 14:55:20`\n        :type EndTime: str\n        :param Db: Specific name of database to be queried\n        :type Db: str\n        :param OrderBy: Sort by metric. Valid values: query_time_sum, query_count\n        :type OrderBy: str\n        :param OrderByType: Sorting order. Valid values: desc, asc\n        :type OrderByType: str\n        :param Slave: Whether to query slow queries of the secondary. 0: primary, 1: secondary\n        :type Slave: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSlowLogsResponse(AbstractModel):
    """DescribeDBSlowLogs response structure.

    """

    def __init__(self):
        """
        :param Data: Slow query log data\n        :type Data: list of SlowLogData\n        :param LockTimeSum: Sum of all statement lock durations\n        :type LockTimeSum: float\n        :param QueryCount: Total number of statement queries\n        :type QueryCount: int\n        :param Total: Total number of results\n        :type Total: int\n        :param QueryTimeSum: Sum of all statement query durations\n        :type QueryTimeSum: float\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID in the format of `dcdbt-ow7t8lmc`.\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabasesResponse(AbstractModel):
    """DescribeDatabases response structure.

    """

    def __init__(self):
        """
        :param Databases: List of databases on instance.\n        :type Databases: list of Database\n        :param InstanceId: Passed through from the input parameters.\n        :type InstanceId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DescribeDcnDetailRequest(AbstractModel):
    """DescribeDcnDetail request structure.

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
        


class DescribeDcnDetailResponse(AbstractModel):
    """DescribeDcnDetail response structure.

    """

    def __init__(self):
        """
        :param DcnDetails: DCN synchronization details\n        :type DcnDetails: list of DcnDetailItem\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.DcnDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DcnDetails") is not None:
            self.DcnDetails = []
            for item in params.get("DcnDetails"):
                obj = DcnDetailItem()
                obj._deserialize(item)
                self.DcnDetails.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFlowRequest(AbstractModel):
    """DescribeFlow request structure.

    """

    def __init__(self):
        """
        :param FlowId: Flow ID returned by async request API.\n        :type FlowId: int\n        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowResponse(AbstractModel):
    """DescribeFlow response structure.

    """

    def __init__(self):
        """
        :param Status: Flow status. 0: succeeded, 1: failed, 2: running\n        :type Status: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID, such as tdsql-6ltok4u9\n        :type InstanceId: str\n        :param Limit: The maximum number of results returned at a time. By default, there is no upper limit to this value, that is, all results can be returned.\n        :type Limit: int\n        :param Offset: Offset of the returned results. Default value: `0`.\n        :type Offset: int\n        """
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
        """
        :param TotalCount: Total number of nodes\n        :type TotalCount: int\n        :param NodesInfo: Node information\n        :type NodesInfo: list of NodeInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogFileRetentionPeriodResponse(AbstractModel):
    """DescribeLogFileRetentionPeriod response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.\n        :type InstanceId: str\n        :param Days: Backup log retention days\n        :type Days: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Product: Database engine name. Valid value: `mariadb`.\n        :type Product: str\n        :param ProjectId: Project ID\n        :type ProjectId: int\n        """
        self.Product = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectSecurityGroupsResponse(AbstractModel):
    """DescribeProjectSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param Groups: Security group details\n        :type Groups: list of SecurityGroup\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DestroyHourDBInstanceRequest(AbstractModel):
    """DestroyHourDBInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of tdsql-avw0207d. It is the same as the instance ID displayed in the TencentDB console.\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyHourDBInstanceResponse(AbstractModel):
    """DestroyHourDBInstance response structure.

    """

    def __init__(self):
        """
        :param FlowId: Async task ID, which can be used in the [DescribeFlow](https://intl.cloud.tencent.com/document/product/237/16177?from_cn_redirect=1) API to query the async task result.\n        :type FlowId: int\n        :param InstanceId: Instance ID, which is the same as the request parameter `InstanceId`.\n        :type InstanceId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.FlowId = None
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups request structure.

    """

    def __init__(self):
        """
        :param Product: Database engine name. Valid value: `mariadb`.\n        :type Product: str\n        :param SecurityGroupId: Security group ID\n        :type SecurityGroupId: str\n        :param InstanceIds: Instance ID list, which is an array of one or more instance IDs.\n        :type InstanceIds: list of str\n        """
        self.Product = None
        self.SecurityGroupId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class FunctionPrivilege(AbstractModel):
    """Function permission information

    """

    def __init__(self):
        """
        :param Database: Database name\n        :type Database: str\n        :param FunctionName: Function name\n        :type FunctionName: str\n        :param Privileges: Permission information\n        :type Privileges: list of str\n        """
        self.Database = None
        self.FunctionName = None
        self.Privileges = None


    def _deserialize(self, params):
        self.Database = params.get("Database")
        self.FunctionName = params.get("FunctionName")
        self.Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrantAccountPrivilegesRequest(AbstractModel):
    """GrantAccountPrivileges request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.\n        :type InstanceId: str\n        :param UserName: Login username.\n        :type UserName: str\n        :param Host: Access host allowed for user. An account is uniquely identified by username and host.\n        :type Host: str\n        :param DbName: Database name. `\*` indicates that global permissions will be set (i.e., `\*.\*`), in which case the `Type` and `Object ` parameters will be ignored. If `DbName` is not `\*`, the input parameter `Type` is required.\n        :type DbName: str\n        :param Privileges: Global permission. Valid values: SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, REFERENCES, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, EVENT, TRIGGER, SHOW DATABASES 
Database permission. Valid values: SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, REFERENCES, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, EVENT, TRIGGER 
Table/view permission. Valid values: SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, REFERENCES, INDEX, ALTER, CREATE VIEW, SHOW VIEW, TRIGGER 
Stored procedure/function permission. Valid values: ALTER ROUTINE, EXECUTE 
Field permission. Valid values: INSERT, REFERENCES, SELECT, UPDATE\n        :type Privileges: list of str\n        :param Type: Type. Valid values: table, view, proc, func, \*. If `DbName` is a specific database name and `Type` is `\*`, the permissions of the database will be set (i.e., `db.\*`), in which case the `Object` parameter will be ignored\n        :type Type: str\n        :param Object: Type name. For example, if `Type` is `table`, `Object` indicates a specific table name; if both `DbName` and `Type` are specific names, it indicates a specific object name and cannot be `\*` or empty\n        :type Object: str\n        :param ColName: If `Type` is `table` and `ColName` is `\*`, the permissions will be granted to the table; if `ColName` is a specific field name, the permissions will be granted to the field\n        :type ColName: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrantAccountPrivilegesResponse(AbstractModel):
    """GrantAccountPrivileges response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class InitDBInstancesRequest(AbstractModel):
    """InitDBInstances request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: List of IDs of instances to be initialized. The ID is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.\n        :type InstanceIds: list of str\n        :param Params: Parameter list. Valid values: character_set_server (character set; required); lower_case_table_names (table name case sensitivity; required; 0: case-sensitive, 1: case-insensitive); innodb_page_size (InnoDB data page; default size: 16 KB); sync_mode (sync mode; 0: async; 1: strong sync; 2: downgradable strong sync; default value: strong sync).\n        :type Params: list of DBParamValue\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InitDBInstancesResponse(AbstractModel):
    """InitDBInstances response structure.

    """

    def __init__(self):
        """
        :param FlowId: Async task ID. The task status can be queried through the `DescribeFlow` API.\n        :type FlowId: int\n        :param InstanceIds: Passed through from the input parameters.\n        :type InstanceIds: list of str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Mtime: Last modified time of log\n        :type Mtime: int\n        :param Length: File length\n        :type Length: int\n        :param Uri: Uniform resource identifier (URI) used during log download\n        :type Uri: str\n        :param FileName: Filename\n        :type FileName: str\n        """
        self.Mtime = None
        self.Length = None
        self.Uri = None
        self.FileName = None


    def _deserialize(self, params):
        self.Mtime = params.get("Mtime")
        self.Length = params.get("Length")
        self.Uri = params.get("Uri")
        self.FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountDescriptionRequest(AbstractModel):
    """ModifyAccountDescription request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.\n        :type InstanceId: str\n        :param UserName: Login username.\n        :type UserName: str\n        :param Host: Access host allowed for user. An account is uniquely identified by username and host.\n        :type Host: str\n        :param Description: New account remarks, which can contain 0-256 characters.\n        :type Description: str\n        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.Description = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountDescriptionResponse(AbstractModel):
    """ModifyAccountDescription response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAccountPrivilegesRequest(AbstractModel):
    """ModifyAccountPrivileges request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of tdsql-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB console.\n        :type InstanceId: str\n        :param Accounts: Database account, including username and host address.\n        :type Accounts: list of Account\n        :param GlobalPrivileges: Global permission. Valid values of `GlobalPrivileges`: `"SELECT"`, `"INSERT"`, `"UPDATE"`, `"DELETE"`, `"CREATE"`, `"PROCESS"`, `"DROP"`, `"REFERENCES"`, `"INDEX"`, `"ALTER"`, `"SHOW DATABASES"`, `"CREATE TEMPORARY TABLES"`, `"LOCK TABLES"`, `"EXECUTE"`, `"CREATE VIEW"`, `"SHOW VIEW"`, `"CREATE ROUTINE"`, `"ALTER ROUTINE"`, `"EVENT"`, `"TRIGGER"`.
Note: if the parameter is left empty, no change will be made to the granted global permissions. To clear the granted global permissions, set the parameter to an empty array.\n        :type GlobalPrivileges: list of str\n        :param DatabasePrivileges: Database permission. Valid values of `Privileges`: `"SELECT"`, `"INSERT"`, `"UPDATE"`, `"DELETE"`, `"CREATE"`, `"DROP"`, `"REFERENCES"`, `"INDEX"`, `"ALTER"`, `"CREATE TEMPORARY TABLES"`, `"LOCK TABLES"`, `"EXECUTE"`, `"CREATE VIEW"`, `"SHOW VIEW"`, `"CREATE ROUTINE"`, `"ALTER ROUTINE"`, `"EVENT"`, `"TRIGGER"`.
Note: if the parameter is left empty, no change will be made to the granted database permissions. To clear the granted database permissions, set `Privileges` to an empty array.\n        :type DatabasePrivileges: list of DatabasePrivilege\n        :param TablePrivileges: Table permission. Valid values of `Privileges`: `"SELECT"`, `"INSERT"`, `"UPDATE"`, `"DELETE"`, `"CREATE"`, `"DROP"`, `"REFERENCES"`, `"INDEX"`, `"ALTER"`, `"CREATE VIEW"`, `"SHOW VIEW"`, `"TRIGGER"`.
Note: if the parameter is left empty, no change will be made to the granted table permissions. To clear the granted table permissions, set `Privileges` to an empty array.\n        :type TablePrivileges: list of TablePrivilege\n        :param ColumnPrivileges: Column permission. Valid values of `Privileges`: `"SELECT"`, `"INSERT"`, `"UPDATE"`, `"REFERENCES"`.
Note: if the parameter is left empty, no change will be made to the granted column permissions. To clear the granted column permissions, set `Privileges` to an empty array.\n        :type ColumnPrivileges: list of ColumnPrivilege\n        :param ViewPrivileges: View permission. Valid values of `Privileges`: `"SELECT"`, `"INSERT"`, `"UPDATE"`, `"DELETE"`, `"CREATE"`, `"DROP"`, `"REFERENCES"`, `"INDEX"`, `"ALTER"`, `"CREATE VIEW"`, `"SHOW VIEW"`, `"TRIGGER"`.
Note: if the parameter is left empty, no change will be made to the granted view permissions. To clear the granted view permissions, set `Privileges` to an empty array.\n        :type ViewPrivileges: list of ViewPrivileges\n        :param FunctionPrivileges: Function permissions. Valid values of `Privileges`: `"ALTER ROUTINE"`, `"EXECUTE"`.
Note: if the parameter is left empty, no change will be made to the granted function permissions. To clear the granted function permissions, set `Privileges` to an empty array.\n        :type FunctionPrivileges: list of FunctionPrivilege\n        :param ProcedurePrivileges: Stored procedure permission. Valid values of `Privileges`: `"ALTER ROUTINE"`, `"EXECUTE"`.
Note: if the parameter is left empty, no change will be made to the granted stored procedure permissions. To clear the granted stored procedure permissions, set `Privileges` to an empty array.\n        :type ProcedurePrivileges: list of ProcedurePrivilege\n        """
        self.InstanceId = None
        self.Accounts = None
        self.GlobalPrivileges = None
        self.DatabasePrivileges = None
        self.TablePrivileges = None
        self.ColumnPrivileges = None
        self.ViewPrivileges = None
        self.FunctionPrivileges = None
        self.ProcedurePrivileges = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.GlobalPrivileges = params.get("GlobalPrivileges")
        if params.get("DatabasePrivileges") is not None:
            self.DatabasePrivileges = []
            for item in params.get("DatabasePrivileges"):
                obj = DatabasePrivilege()
                obj._deserialize(item)
                self.DatabasePrivileges.append(obj)
        if params.get("TablePrivileges") is not None:
            self.TablePrivileges = []
            for item in params.get("TablePrivileges"):
                obj = TablePrivilege()
                obj._deserialize(item)
                self.TablePrivileges.append(obj)
        if params.get("ColumnPrivileges") is not None:
            self.ColumnPrivileges = []
            for item in params.get("ColumnPrivileges"):
                obj = ColumnPrivilege()
                obj._deserialize(item)
                self.ColumnPrivileges.append(obj)
        if params.get("ViewPrivileges") is not None:
            self.ViewPrivileges = []
            for item in params.get("ViewPrivileges"):
                obj = ViewPrivileges()
                obj._deserialize(item)
                self.ViewPrivileges.append(obj)
        if params.get("FunctionPrivileges") is not None:
            self.FunctionPrivileges = []
            for item in params.get("FunctionPrivileges"):
                obj = FunctionPrivilege()
                obj._deserialize(item)
                self.FunctionPrivileges.append(obj)
        if params.get("ProcedurePrivileges") is not None:
            self.ProcedurePrivileges = []
            for item in params.get("ProcedurePrivileges"):
                obj = ProcedurePrivilege()
                obj._deserialize(item)
                self.ProcedurePrivileges.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountPrivilegesResponse(AbstractModel):
    """ModifyAccountPrivileges response structure.

    """

    def __init__(self):
        """
        :param FlowId: Async task ID, which can be used in the [DescribeFlow](https://intl.cloud.tencent.com/document/product/237/16177?from_cn_redirect=1) API to query the async task result.\n        :type FlowId: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ModifyBackupTimeRequest(AbstractModel):
    """ModifyBackupTime request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.\n        :type InstanceId: str\n        :param StartBackupTime: Start time of daily backup window in the format of `mm:ss`, such as 22:00\n        :type StartBackupTime: str\n        :param EndBackupTime: End time of daily backup window in the format of `mm:ss`, such as 23:59\n        :type EndBackupTime: str\n        """
        self.InstanceId = None
        self.StartBackupTime = None
        self.EndBackupTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartBackupTime = params.get("StartBackupTime")
        self.EndBackupTime = params.get("EndBackupTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupTimeResponse(AbstractModel):
    """ModifyBackupTime response structure.

    """

    def __init__(self):
        """
        :param Status: Setting status. 0: success\n        :type Status: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: ID of instance to be modified, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.\n        :type InstanceId: str\n        :param InstanceName: New name of instance, which can contain letters, digits, underscores, and hyphens.\n        :type InstanceName: str\n        """
        self.InstanceId = None
        self.InstanceName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceNameResponse(AbstractModel):
    """ModifyDBInstanceName response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Product: Database engine name. Valid value: `mariadb`.\n        :type Product: str\n        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param SecurityGroupIds: List of IDs of security groups to be modified, which is an array of one or more security group IDs.\n        :type SecurityGroupIds: list of str\n        """
        self.Product = None
        self.InstanceId = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.InstanceId = params.get("InstanceId")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSecurityGroupsResponse(AbstractModel):
    """ModifyDBInstanceSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstancesProjectRequest(AbstractModel):
    """ModifyDBInstancesProject request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: List of IDs of instances to be modified. The ID is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.\n        :type InstanceIds: list of str\n        :param ProjectId: ID of the project to be assigned, which can be obtained through the `DescribeProjects` API.\n        :type ProjectId: int\n        """
        self.InstanceIds = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstancesProjectResponse(AbstractModel):
    """ModifyDBInstancesProject response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBParametersRequest(AbstractModel):
    """ModifyDBParameters request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.\n        :type InstanceId: str\n        :param Params: Parameter list. Each element is a combination of `Param` and `Value`.\n        :type Params: list of DBParamValue\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBParametersResponse(AbstractModel):
    """ModifyDBParameters response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.\n        :type InstanceId: str\n        :param Result: Parameter modification result\n        :type Result: list of ParamModifyResult\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.\n        :type InstanceId: str\n        :param Days: Retention days up to 30\n        :type Days: int\n        """
        self.InstanceId = None
        self.Days = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Days = params.get("Days")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLogFileRetentionPeriodResponse(AbstractModel):
    """ModifyLogFileRetentionPeriod response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of `tdsql-ow728lmc`.\n        :type InstanceId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param StartTime: Start time in the format of `2018-03-24 23:59:59`\n        :type StartTime: str\n        :param EndTime: End time in the format of `2018-03-24 23:59:59`\n        :type EndTime: str\n        :param Data: Monitoring data\n        :type Data: list of float\n        """
        self.StartTime = None
        self.EndTime = None
        self.Data = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeInfo(AbstractModel):
    """Instance node information

    """

    def __init__(self):
        """
        :param NodeId: Node ID\n        :type NodeId: str\n        :param Role: Node role. Valid values: `master`, `slave`\n        :type Role: str\n        """
        self.NodeId = None
        self.Role = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenDBExtranetAccessRequest(AbstractModel):
    """OpenDBExtranetAccess request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of instance for which to enable public network access. The ID is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.\n        :type InstanceId: str\n        :param Ipv6Flag: Whether IPv6 is used. Default value: 0\n        :type Ipv6Flag: int\n        """
        self.InstanceId = None
        self.Ipv6Flag = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Ipv6Flag = params.get("Ipv6Flag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenDBExtranetAccessResponse(AbstractModel):
    """OpenDBExtranetAccess response structure.

    """

    def __init__(self):
        """
        :param FlowId: Async task ID. The task status can be queried through the `DescribeFlow` API.\n        :type FlowId: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Type: Constraint type, such as `enum` and `section`\n        :type Type: str\n        :param Enum: List of valid values when constraint type is `enum`\n        :type Enum: str\n        :param Range: Range when constraint type is `section`
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Range: :class:`tencentcloud.mariadb.v20170312.models.ConstraintRange`\n        :param String: List of valid values when constraint type is `string`\n        :type String: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamDesc(AbstractModel):
    """Database parameter description

    """

    def __init__(self):
        """
        :param Param: Parameter name\n        :type Param: str\n        :param Value: Current parameter value\n        :type Value: str\n        :param SetValue: Previously set value, which is the same as `value` after the parameter takes effect.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SetValue: str\n        :param Default: Default value\n        :type Default: str\n        :param Constraint: Parameter constraint\n        :type Constraint: :class:`tencentcloud.mariadb.v20170312.models.ParamConstraint`\n        :param HaveSetValue: Whether a value has been set. false: no, true: yes\n        :type HaveSetValue: bool\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamModifyResult(AbstractModel):
    """Parameter modification result

    """

    def __init__(self):
        """
        :param Param: Renames a parameter\n        :type Param: str\n        :param Code: Result of parameter modification. 0: success, -1: failure, -2: invalid parameter value\n        :type Code: int\n        """
        self.Param = None
        self.Code = None


    def _deserialize(self, params):
        self.Param = params.get("Param")
        self.Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PerformanceMonitorSet(AbstractModel):
    """Set of database performance monitoring metrics

    """

    def __init__(self):
        """
        :param UpdateTotal: Number of UPDATE operations\n        :type UpdateTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param DiskIops: Number of disk IOs per second\n        :type DiskIops: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param ConnActive: Number of active connections\n        :type ConnActive: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param MemHitRate: Cache hit rate\n        :type MemHitRate: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param SlaveDelay: Primary/Secondary delay\n        :type SlaveDelay: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param SelectTotal: Number of SELECT operations\n        :type SelectTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param LongQuery: Number of slow queries\n        :type LongQuery: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param DeleteTotal: Number of DELETE operations\n        :type DeleteTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param InsertTotal: Number of INSERT operations\n        :type InsertTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param IsMasterSwitched: Whether primary/Secondary switch occurred. 1: yes, 0: no\n        :type IsMasterSwitched: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcedurePrivilege(AbstractModel):
    """Stored procedure permission information

    """

    def __init__(self):
        """
        :param Database: Database name\n        :type Database: str\n        :param Procedure: Stored procedure name\n        :type Procedure: str\n        :param Privileges: Permission information\n        :type Privileges: list of str\n        """
        self.Database = None
        self.Procedure = None
        self.Privileges = None


    def _deserialize(self, params):
        self.Database = params.get("Database")
        self.Procedure = params.get("Procedure")
        self.Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAccountPasswordRequest(AbstractModel):
    """ResetAccountPassword request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, which is in the format of `tdsql-ow728lmc` and can be obtained through the `DescribeDBInstances` API.\n        :type InstanceId: str\n        :param UserName: Login username.\n        :type UserName: str\n        :param Host: Access host allowed for user. An account is uniquely identified by username and host.\n        :type Host: str\n        :param Password: New password, which can contain 6-32 letters, digits, and common symbols but not semicolons, single quotation marks, and double quotation marks.\n        :type Password: str\n        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAccountPasswordResponse(AbstractModel):
    """ResetAccountPassword response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResourceUsageMonitorSet(AbstractModel):
    """Set of database resource usage monitoring metrics

    """

    def __init__(self):
        """
        :param BinlogDiskAvailable: Available capacity of binlog disk in GB\n        :type BinlogDiskAvailable: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param CpuUsageRate: CPU utilization\n        :type CpuUsageRate: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param MemAvailable: Available memory size in GB\n        :type MemAvailable: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param DataDiskAvailable: Available disk capacity in GB\n        :type DataDiskAvailable: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroup(AbstractModel):
    """Security group details

    """

    def __init__(self):
        """
        :param ProjectId: Project ID\n        :type ProjectId: int\n        :param CreateTime: Creation time in the format of yyyy-mm-dd hh:mm:ss\n        :type CreateTime: str\n        :param SecurityGroupId: Security group ID\n        :type SecurityGroupId: str\n        :param SecurityGroupName: Security group name\n        :type SecurityGroupName: str\n        :param SecurityGroupRemark: Security group remarks\n        :type SecurityGroupRemark: str\n        :param Inbound: Inbound rule\n        :type Inbound: list of SecurityGroupBound\n        :param Outbound: Outbound rule\n        :type Outbound: list of SecurityGroupBound\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupBound(AbstractModel):
    """Security group inbound/outbound rule

    """

    def __init__(self):
        """
        :param Action: Policy, which can be `ACCEPT` or `DROP`\n        :type Action: str\n        :param CidrIp: Source IP or source IP range, such as 192.168.0.0/16\n        :type CidrIp: str\n        :param PortRange: Port\n        :type PortRange: str\n        :param IpProtocol: Network protocol. UDP and TCP are supported.\n        :type IpProtocol: str\n        """
        self.Action = None
        self.CidrIp = None
        self.PortRange = None
        self.IpProtocol = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.CidrIp = params.get("CidrIp")
        self.PortRange = params.get("PortRange")
        self.IpProtocol = params.get("IpProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogData(AbstractModel):
    """Slow query entry information

    """

    def __init__(self):
        """
        :param CheckSum: Statement checksum for querying details\n        :type CheckSum: str\n        :param Db: Database name\n        :type Db: str\n        :param FingerPrint: Abstracted SQL statement\n        :type FingerPrint: str\n        :param LockTimeAvg: Average lock duration\n        :type LockTimeAvg: str\n        :param LockTimeMax: Maximum lock duration\n        :type LockTimeMax: str\n        :param LockTimeMin: Minimum lock duration\n        :type LockTimeMin: str\n        :param LockTimeSum: Sum of lock durations\n        :type LockTimeSum: str\n        :param QueryCount: Number of queries\n        :type QueryCount: str\n        :param QueryTimeAvg: Average query duration\n        :type QueryTimeAvg: str\n        :param QueryTimeMax: Maximum query duration\n        :type QueryTimeMax: str\n        :param QueryTimeMin: Minimum query duration\n        :type QueryTimeMin: str\n        :param QueryTimeSum: Sum of query durations\n        :type QueryTimeSum: str\n        :param RowsExaminedSum: Number of scanned rows\n        :type RowsExaminedSum: str\n        :param RowsSentSum: Number of sent rows\n        :type RowsSentSum: str\n        :param TsMax: Last execution time\n        :type TsMax: str\n        :param TsMin: First execution time\n        :type TsMin: str\n        :param User: Account\n        :type User: str\n        :param ExampleSql: Sample SQL
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ExampleSql: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TablePrivilege(AbstractModel):
    """Table permission

    """

    def __init__(self):
        """
        :param Database: Database name\n        :type Database: str\n        :param Table: Table name\n        :type Table: str\n        :param Privileges: Permission information\n        :type Privileges: list of str\n        """
        self.Database = None
        self.Table = None
        self.Privileges = None


    def _deserialize(self, params):
        self.Database = params.get("Database")
        self.Table = params.get("Table")
        self.Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ViewPrivileges(AbstractModel):
    """View permission information

    """

    def __init__(self):
        """
        :param Database: Database name\n        :type Database: str\n        :param View: View name\n        :type View: str\n        :param Privileges: Permission information\n        :type Privileges: list of str\n        """
        self.Database = None
        self.View = None
        self.Privileges = None


    def _deserialize(self, params):
        self.Database = params.get("Database")
        self.View = params.get("View")
        self.Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        