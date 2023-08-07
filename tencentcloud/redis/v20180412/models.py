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
        :param _InstanceId: Instance ID 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _AccountName: Account name 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type AccountName: str
        :param _Remark: Account description information 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param _Privilege: Read/write permission policy. Valid values: `r` (read-only),  `w` (write-only),  `rw`  (read/write). 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type Privilege: str
        :param _ReadonlyPolicy: Read-only routing policy. Valid values: `master` (master node),  `replication`  (replica node). 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type ReadonlyPolicy: list of str
        :param _Status: Sub-account status. Valid values:  `1` (being changed),  `2` (valid). `4` (deleted). 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        """
        self._InstanceId = None
        self._AccountName = None
        self._Remark = None
        self._Privilege = None
        self._ReadonlyPolicy = None
        self._Status = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Privilege(self):
        return self._Privilege

    @Privilege.setter
    def Privilege(self, Privilege):
        self._Privilege = Privilege

    @property
    def ReadonlyPolicy(self):
        return self._ReadonlyPolicy

    @ReadonlyPolicy.setter
    def ReadonlyPolicy(self, ReadonlyPolicy):
        self._ReadonlyPolicy = ReadonlyPolicy

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AccountName = params.get("AccountName")
        self._Remark = params.get("Remark")
        self._Privilege = params.get("Privilege")
        self._ReadonlyPolicy = params.get("ReadonlyPolicy")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateWanAddressRequest(AbstractModel):
    """AllocateWanAddress request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class AllocateWanAddressResponse(AbstractModel):
    """AllocateWanAddress response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task ID
        :type FlowId: int
        :param _WanStatus: Status of enabling public network access
        :type WanStatus: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._WanStatus = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def WanStatus(self):
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._WanStatus = params.get("WanStatus")
        self._RequestId = params.get("RequestId")


class ApplyParamsTemplateRequest(AbstractModel):
    """ApplyParamsTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: List of instance IDs
        :type InstanceIds: list of str
        :param _TemplateId: ID of the parameter template to be applied
        :type TemplateId: str
        """
        self._InstanceIds = None
        self._TemplateId = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyParamsTemplateResponse(AbstractModel):
    """ApplyParamsTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _TaskIds: Task ID
        :type TaskIds: list of int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskIds = None
        self._RequestId = None

    @property
    def TaskIds(self):
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskIds = params.get("TaskIds")
        self._RequestId = params.get("RequestId")


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _Product: Database engine name, which is `redis` for this API.
        :type Product: str
        :param _SecurityGroupId: ID of the security group to be associated in the format of sg-efil73jd.
        :type SecurityGroupId: str
        :param _InstanceIds: ID(s) of the instance(s) to be associated in the format of ins-lesecurk. You can specify multiple instances.
        :type InstanceIds: list of str
        """
        self._Product = None
        self._SecurityGroupId = None
        self._InstanceIds = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class BackupDownloadInfo(AbstractModel):
    """Backup download information

    """

    def __init__(self):
        r"""
        :param _FileName: Backup file name
        :type FileName: str
        :param _FileSize: Backup file size in bytes. If the parameter value is `0`, the backup file size is unknown.
        :type FileSize: int
        :param _DownloadUrl: Address (valid for six hours) used to download the backup file over the public network
        :type DownloadUrl: str
        :param _InnerDownloadUrl: Address (valid for six hours) used to download the backup file over the private network
        :type InnerDownloadUrl: str
        """
        self._FileName = None
        self._FileSize = None
        self._DownloadUrl = None
        self._InnerDownloadUrl = None

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def DownloadUrl(self):
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def InnerDownloadUrl(self):
        return self._InnerDownloadUrl

    @InnerDownloadUrl.setter
    def InnerDownloadUrl(self, InnerDownloadUrl):
        self._InnerDownloadUrl = InnerDownloadUrl


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._DownloadUrl = params.get("DownloadUrl")
        self._InnerDownloadUrl = params.get("InnerDownloadUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupLimitVpcItem(AbstractModel):
    """The VPC that corresponds to the configured download address of the backup file

    """

    def __init__(self):
        r"""
        :param _Region: The region of the VPC that corresponds to the download address of the backup file
        :type Region: str
        :param _VpcList: The list of VPCs that correspond to the download addresses of the backup files
        :type VpcList: list of str
        """
        self._Region = None
        self._VpcList = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcList(self):
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._VpcList = params.get("VpcList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BigKeyInfo(AbstractModel):
    """Big key details

    """

    def __init__(self):
        r"""
        :param _DB: Database
        :type DB: int
        :param _Key: Big key
        :type Key: str
        :param _Type: Type
        :type Type: str
        :param _Size: Size
        :type Size: int
        :param _Updatetime: Data timestamp
        :type Updatetime: int
        """
        self._DB = None
        self._Key = None
        self._Type = None
        self._Size = None
        self._Updatetime = None

    @property
    def DB(self):
        return self._DB

    @DB.setter
    def DB(self, DB):
        self._DB = DB

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Updatetime(self):
        return self._Updatetime

    @Updatetime.setter
    def Updatetime(self, Updatetime):
        self._Updatetime = Updatetime


    def _deserialize(self, params):
        self._DB = params.get("DB")
        self._Key = params.get("Key")
        self._Type = params.get("Type")
        self._Size = params.get("Size")
        self._Updatetime = params.get("Updatetime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BigKeyTypeInfo(AbstractModel):
    """Big key type distribution details

    """

    def __init__(self):
        r"""
        :param _Type: Type
        :type Type: str
        :param _Count: Count
        :type Count: int
        :param _Size: Size
        :type Size: int
        :param _Updatetime: Timestamp
        :type Updatetime: int
        """
        self._Type = None
        self._Count = None
        self._Size = None
        self._Updatetime = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Updatetime(self):
        return self._Updatetime

    @Updatetime.setter
    def Updatetime(self, Updatetime):
        self._Updatetime = Updatetime


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Count = params.get("Count")
        self._Size = params.get("Size")
        self._Updatetime = params.get("Updatetime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeInstanceRoleRequest(AbstractModel):
    """ChangeInstanceRole request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Replication group ID
        :type GroupId: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceRole: Instance role. Valid values: `rw` (read-write), `r`( read-only).
        :type InstanceRole: str
        """
        self._GroupId = None
        self._InstanceId = None
        self._InstanceRole = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceRole(self):
        return self._InstanceRole

    @InstanceRole.setter
    def InstanceRole(self, InstanceRole):
        self._InstanceRole = InstanceRole


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._InstanceId = params.get("InstanceId")
        self._InstanceRole = params.get("InstanceRole")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeInstanceRoleResponse(AbstractModel):
    """ChangeInstanceRole response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Async task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ChangeMasterInstanceRequest(AbstractModel):
    """ChangeMasterInstance request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Replication group ID, such as `crs-rpl-m3zt****`. It is the unique identifier automatically assigned by the system when creating a replication group. Log in to the [TencentDB for Redis console](https://console.cloud.tencent.com/redis/replication), and get it in the global replication list.

        :type GroupId: str
        :param _InstanceId: ID of the read-only instance to be promoted to the master instance, such as `crs-xjhsdj****`. Log in to the the [TencentDB for Redis console](https://console.cloud.tencent.com/redis), and copy it in the instance list.


        :type InstanceId: str
        :param _ForceSwitch: Whether to promote the read-only instance to the master instance forcibly. Valid values:
- `true`: Yes
- `false`: No
        :type ForceSwitch: bool
        """
        self._GroupId = None
        self._InstanceId = None
        self._ForceSwitch = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ForceSwitch(self):
        return self._ForceSwitch

    @ForceSwitch.setter
    def ForceSwitch(self, ForceSwitch):
        self._ForceSwitch = ForceSwitch


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._InstanceId = params.get("InstanceId")
        self._ForceSwitch = params.get("ForceSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeMasterInstanceResponse(AbstractModel):
    """ChangeMasterInstance response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Async task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ChangeReplicaToMasterRequest(AbstractModel):
    """ChangeReplicaToMaster request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of the specified instance,  such as  "crs-xjhsdj****" Log in to the [Redis console](https://console.cloud.tencent.com/redis) and copy the instance ID in the instance list.

        :type InstanceId: str
        :param _GroupId: ID of the replica node group. You can get more ID information of the multi-AZ replica node group though the [DescribeInstanceZoneInfo](https://intl.cloud.tencent.com/document/product/239/50312?from_cn_redirect=1) API.  This parameter is not required for a single-AZ replica node group.
        :type GroupId: int
        """
        self._InstanceId = None
        self._GroupId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeReplicaToMasterResponse(AbstractModel):
    """ChangeReplicaToMaster response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Async task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CleanUpInstanceRequest(AbstractModel):
    """CleanUpInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class CleanUpInstanceResponse(AbstractModel):
    """CleanUpInstance response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ClearInstanceRequest(AbstractModel):
    """ClearInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Password: Redis instance password (this parameter is required for password-enabled instances but not for password-free instances)
        :type Password: str
        """
        self._InstanceId = None
        self._Password = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearInstanceResponse(AbstractModel):
    """ClearInstance response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CloneInstancesRequest(AbstractModel):
    """CloneInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ID of the source instance to be cloned, such as "crs-xjhsdj****". Log in to the [Redis console](https://console.cloud.tencent.com/redis) and copy the instance ID in the instance list.
        :type InstanceId: str
        :param _GoodsNum: The number of clone instances at a time
- The maximum number of monthly subscribed instances is 100 for each purchase.
- The maximum number of pay-as-you-go instances is 30 for each purchase.
        :type GoodsNum: int
        :param _ZoneId: ID of the AZ where the clone instance resides. For more information, see [Regions and AZs](https://intl.cloud.tencent.com/document/product/239/4106?from_cn_redirect=1).
        :type ZoneId: int
        :param _BillingMode: Billing mode. Valid values: <ul><li>`0` (Pay-as-you-go) </li><li>`1` (Monthly subscription) </li></ul>
        :type BillingMode: int
        :param _Period: Purchase duration of an instance. <ul><li>Unit: Month</li><li>Valid values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `24`, `36`, `48`, `60` (for monthly subscription mode).</li><li> Valid value: `1` (for pay-as-you-go mode).</li></ul>
        :type Period: int
        :param _SecurityGroupIdList: Security group ID, which can be obtained on the <b>Security Group</b> page in the console.
        :type SecurityGroupIdList: list of str
        :param _BackupId: Backup ID of the clone instance, which can be obtained through the [DescribeInstanceBackups](https://intl.cloud.tencent.com/document/product/239/20011?from_cn_redirect=1) API.
        :type BackupId: str
        :param _NoAuth: Whether the clone instance supports password-free access. Valid values: <ul><li>`true` (Yes)</li><li>`false` (No. When SSL or public network is enabled). Default value: `false`.</li></ul>
        :type NoAuth: bool
        :param _VpcId: The VPC ID of the clone instance. If this parameter is not passed in, the classic network will be selected by default.
        :type VpcId: str
        :param _SubnetId: The VPC subnet ID to which the clone instance belongs, which is not required for the classic network.
        :type SubnetId: str
        :param _InstanceName: Name of the clone instance. <br>Enter up to 60 letters, digits, hyphens, and underscores.</br>
        :type InstanceName: str
        :param _Password: The access password of the clone instance. <ul><li>When the input parameter <b>NoAuth</b> is <b>true</b>, this parameter is not required. </li><li>When the instance is Redis 2.8, 4.0, or 5.0, the password must contain 8–30 characters in at least two of the following types: lowercase letters, uppercase letters, digits, and special characters `()`~!@#$%^&*-+=_|{}[]:;<>,.?/` and cannot start with `/`.</li><li>When the instance is CKV 3.2, the password must and can only contain 8–30 letters and digits.</li></ul>
        :type Password: str
        :param _AutoRenew: The auto-renewal flag. Valid values <ul><li>`0`: Manual renewal (default). </li><li>`1`: Auto-renewal. </li><li>`2`: Not auto-renewal (set by user).</ul>
        :type AutoRenew: int
        :param _VPort: Customized port. Valid range: 1024-65535. Default value: `6379`.
        :type VPort: int
        :param _NodeSet: Node information of an instance. <ul><li>Currently supported type and AZ information of a node to be configured (master node or replica node) For more information, see [RedisNodeInfo](https://intl.cloud.tencent.com/document/product/239/20022?from_cn_redirect=1#RedisNodeInfo).</li><li>This parameter is not required for single-AZ deployment.</li></ul>
        :type NodeSet: list of RedisNodeInfo
        :param _ProjectId: Project ID. Log in to the [Redis console](https://console.cloud.tencent.com/redis#/), and find the project ID in <b>Account Center</b> > <b>Project Management</b> in the top-right corner.
        :type ProjectId: int
        :param _ResourceTags: Tag to be bound for the clone instance
        :type ResourceTags: list of ResourceTag
        :param _TemplateId: The parameter template ID associated with the clone instance
- If this parameter is not configured, the system will automatically adapt the corresponding default template based on the selected compatible version and architecture.
- You can query the parameter template list of the instance to get the template ID through the [DescribeParamTemplates](https://intl.cloud.tencent.com/document/product/239/58750?from_cn_redirect=1) API.
        :type TemplateId: str
        :param _AlarmPolicyList: The alarm policy ID of the instance to be cloned. Log in to the [Tencent Cloud Observable Platform console](https://console.cloud.tencent.com/monitor/alarm2/policy), and get the policy ID in <b>Alarm Management</b> > <b>Policy Management</b>.
        :type AlarmPolicyList: list of str
        """
        self._InstanceId = None
        self._GoodsNum = None
        self._ZoneId = None
        self._BillingMode = None
        self._Period = None
        self._SecurityGroupIdList = None
        self._BackupId = None
        self._NoAuth = None
        self._VpcId = None
        self._SubnetId = None
        self._InstanceName = None
        self._Password = None
        self._AutoRenew = None
        self._VPort = None
        self._NodeSet = None
        self._ProjectId = None
        self._ResourceTags = None
        self._TemplateId = None
        self._AlarmPolicyList = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def BillingMode(self):
        return self._BillingMode

    @BillingMode.setter
    def BillingMode(self, BillingMode):
        self._BillingMode = BillingMode

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def SecurityGroupIdList(self):
        return self._SecurityGroupIdList

    @SecurityGroupIdList.setter
    def SecurityGroupIdList(self, SecurityGroupIdList):
        self._SecurityGroupIdList = SecurityGroupIdList

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def NoAuth(self):
        return self._NoAuth

    @NoAuth.setter
    def NoAuth(self, NoAuth):
        self._NoAuth = NoAuth

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def AutoRenew(self):
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def VPort(self):
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def NodeSet(self):
        return self._NodeSet

    @NodeSet.setter
    def NodeSet(self, NodeSet):
        self._NodeSet = NodeSet

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def AlarmPolicyList(self):
        return self._AlarmPolicyList

    @AlarmPolicyList.setter
    def AlarmPolicyList(self, AlarmPolicyList):
        self._AlarmPolicyList = AlarmPolicyList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._GoodsNum = params.get("GoodsNum")
        self._ZoneId = params.get("ZoneId")
        self._BillingMode = params.get("BillingMode")
        self._Period = params.get("Period")
        self._SecurityGroupIdList = params.get("SecurityGroupIdList")
        self._BackupId = params.get("BackupId")
        self._NoAuth = params.get("NoAuth")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._InstanceName = params.get("InstanceName")
        self._Password = params.get("Password")
        self._AutoRenew = params.get("AutoRenew")
        self._VPort = params.get("VPort")
        if params.get("NodeSet") is not None:
            self._NodeSet = []
            for item in params.get("NodeSet"):
                obj = RedisNodeInfo()
                obj._deserialize(item)
                self._NodeSet.append(obj)
        self._ProjectId = params.get("ProjectId")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._TemplateId = params.get("TemplateId")
        self._AlarmPolicyList = params.get("AlarmPolicyList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneInstancesResponse(AbstractModel):
    """CloneInstances response structure.

    """

    def __init__(self):
        r"""
        :param _DealId: Request task ID
        :type DealId: str
        :param _InstanceIds: Clone instance ID
        :type InstanceIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealId = None
        self._InstanceIds = None
        self._RequestId = None

    @property
    def DealId(self):
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._InstanceIds = params.get("InstanceIds")
        self._RequestId = params.get("RequestId")


class CloseSSLRequest(AbstractModel):
    """CloseSSL request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class CloseSSLResponse(AbstractModel):
    """CloseSSL response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CommandTake(AbstractModel):
    """Command duration

    """

    def __init__(self):
        r"""
        :param _Cmd: Command
        :type Cmd: str
        :param _Took: Duration
        :type Took: int
        """
        self._Cmd = None
        self._Took = None

    @property
    def Cmd(self):
        return self._Cmd

    @Cmd.setter
    def Cmd(self, Cmd):
        self._Cmd = Cmd

    @property
    def Took(self):
        return self._Took

    @Took.setter
    def Took(self, Took):
        self._Took = Took


    def _deserialize(self, params):
        self._Cmd = params.get("Cmd")
        self._Took = params.get("Took")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceAccountRequest(AbstractModel):
    """CreateInstanceAccount request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _AccountName: Sub-account name
        :type AccountName: str
        :param _AccountPassword: 1. The password must contain 8–30 characters. A password of 12 or more characters is recommended.
2. It cannot start with a slash (/).
3. It must contain characters in at least two of the following types:
    a. Lowercase letters (a–z)
    b. Uppercase letters (A–Z)
    c. Digits (0–9)
    d. ()`~!@#$%^&*-+=_|{}[]:;<>,.?/
        :type AccountPassword: str
        :param _ReadonlyPolicy: Routing policy. Valid values: master (master node); replication (replica node)
        :type ReadonlyPolicy: list of str
        :param _Privilege: Read/Write policy. Valid values: r (read-only); rw (read/write).
        :type Privilege: str
        :param _Remark: Sub-account description information
        :type Remark: str
        """
        self._InstanceId = None
        self._AccountName = None
        self._AccountPassword = None
        self._ReadonlyPolicy = None
        self._Privilege = None
        self._Remark = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def AccountPassword(self):
        return self._AccountPassword

    @AccountPassword.setter
    def AccountPassword(self, AccountPassword):
        self._AccountPassword = AccountPassword

    @property
    def ReadonlyPolicy(self):
        return self._ReadonlyPolicy

    @ReadonlyPolicy.setter
    def ReadonlyPolicy(self, ReadonlyPolicy):
        self._ReadonlyPolicy = ReadonlyPolicy

    @property
    def Privilege(self):
        return self._Privilege

    @Privilege.setter
    def Privilege(self, Privilege):
        self._Privilege = Privilege

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AccountName = params.get("AccountName")
        self._AccountPassword = params.get("AccountPassword")
        self._ReadonlyPolicy = params.get("ReadonlyPolicy")
        self._Privilege = params.get("Privilege")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceAccountResponse(AbstractModel):
    """CreateInstanceAccount response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateInstancesRequest(AbstractModel):
    """CreateInstances request structure.

    """

    def __init__(self):
        r"""
        :param _TypeId: Instance type
<ul><li>`2`: Redis 2.8 Memory Edition (Standard Architecture). </li><li>`3`: CKV 3.2 Memory Edition (Standard Architecture). </li><li>`4`: CKV 3.2 Memory Edition (Cluster Architecture). </li><li>`6`: Redis 4.0 Memory Edition (Standard Architecture). </li><li>`7`: Redis 4.0 Memory Edition (Cluster Architecture). </li><li>`8`: Redis 5.0 Memory Edition (Standard Architecture). </li><li>`9`: Redis 5.0 Memory Edition (Cluster Architecture). </li><li>`15`: Redis 6.2 Memory Edition (Standard Architecture). </li><li>`16`: Redis 6.2 Memory Edition (Cluster Architecture).</li></ul>
        :type TypeId: int
        :param _MemSize: Memory capacity in MB, which must be an integer multiple of 1024. For specific specifications, query the sales specifications in all regions through the [DescribeProductInfo](https://intl.cloud.tencent.com/document/api/239/30600?from_cn_redirect=1) API.
- When **TypeId** is a standard architecture, **MemSize** is the total memory capacity of the instance;
- When **TypeId** is a cluster architecture, **MemSize** is the single-shard memory capacity.
        :type MemSize: int
        :param _GoodsNum: The number of instances for each purchase. For details, query the sales specifications in all regions through the [DescribeProductInfo](https://intl.cloud.tencent.com/document/api/239/30600?from_cn_redirect=1) API.
        :type GoodsNum: int
        :param _Period: The purchase duration of an instance
- If `BillingMode` is `1`, that is, when the billing mode is monthly subscription, you need to set this parameter to specify the duration of the purchased instance. Unit: month. Value range: [1,2,3,4,5,6,7,8,9,10,11,12,24,36].
- If `BillingMode` is `0`, that is, when the billing mode is pay-as-you-go, you need to set this parameter to `1`.
        :type Period: int
        :param _BillingMode: Billing mode. 0: pay-as-you-go
        :type BillingMode: int
        :param _ZoneId: ID of the AZ where the instance resides. For more information, see [Regions and AZs](https://intl.cloud.tencent.com/document/product/239/4106?from_cn_redirect=1).
        :type ZoneId: int
        :param _Password: Instance access password
- When the input parameter `NoAuth` is `true`, it means that the instance access is set to be password-free, and the `Password` field does not need to be configured; otherwise, `Password` is a required parameter.
- When the instance type `TypeId` is Redis 2.8 Memory Edition (Standard Architecture), Redis 4.0, 5.0, 6.0 (regardless of architecture), the password must contains 8-30 characters in at least two of the following types: lowercase letters, uppercase letters, digits, and symbols (()`~!@#$%^&*-+=_|{}[]:;<>,.?/), and it cannot start with a slash (/).
- When the instance type **TypeId** is CKV 3.2 Memory Edition (regardless of architecture), the password contains 8-30 letters and digits and excludes other characters.
        :type Password: str
        :param _VpcId: VPC ID. If this parameter is not passed in, the classic network will be selected by default. You can query the specific VPC ID in the [VPC console](https://console.cloud.tencent.com/vpc).
        :type VpcId: str
        :param _SubnetId: VPC subnet ID. This parameter is not required for the classic network. You can get the specific subnet ID by querying the subnet list in the [VPC console](https://console.cloud.tencent.com/vpc).
        :type SubnetId: str
        :param _ProjectId: Project ID. Log in to the [Redis console](https://console.cloud.tencent.com/redis#/), go to the account information menu in the top-right corner, and select **Project Management** to query the project ID.
        :type ProjectId: int
        :param _AutoRenew: Auto-renewal flag
- `0`: Manual renewal (default).
- `1`: Auto-renewal.
- `2`: Not auto-renewal (set by user).
        :type AutoRenew: int
        :param _SecurityGroupIdList: Array of security group IDs. Get the security group ID of the instance through the [DescribeInstanceSecurityGroup](https://intl.cloud.tencent.com/document/product/239/34447?from_cn_redirect=1) API.
        :type SecurityGroupIdList: list of str
        :param _VPort: User-defined network port. Default value: `6379`. Range: [1024,65535].
        :type VPort: int
        :param _RedisShardNum: Quantity of instance shards
- This parameter is not required for instances of Standard Edition.
- For instances of Cluster Edition, the range of shard quantity is [1, 3, 5, 8, 12, 16, 24, 32, 40, 48, 64, 80, 96, 128].
        :type RedisShardNum: int
        :param _RedisReplicasNum: Quantity of instance replicas
- For Redis Memory Edition 4.0, 5.0, 6.2 (regardless of architecture), the range of replica quantity is [1,5].
- For Redis 2.8 Standard Edition and CKV Standard Edition, the replica quantity is `1`.
        :type RedisReplicasNum: int
        :param _ReplicasReadonly: Whether to support read-only replicas.
- Redis 2.8 Standard Edition and CKV Standard Edition don’t support read-only replicas.
- If read-only replicas are enabled, read/write separation will be automatically enabled for an instance, with write requests routed to the master node and read requests to the replica node.
- To enable read-only replicas, we recommend that you create two or more replicas.
        :type ReplicasReadonly: bool
        :param _InstanceName: Instance name, which can contain up to 60 letters, digits, hyphens, and underscores.
        :type InstanceName: str
        :param _NoAuth: Whether to support password-free access for an instance
- `true`: The instance access is password-free.
- `false`: The instance access is password-enabled. Default value: `false`. Only instances in a VPC support the password-free access.
        :type NoAuth: bool
        :param _NodeSet: The node information of the instance, including node ID, type, and AZ. For more information, see [RedisNodeInfo](https://intl.cloud.tencent.com/document/product/239/20022?from_cn_redirect=1).
Node information of an instance. Currently, information about the node type (master or replica) and node AZ can be passed in. This parameter is not required for instances deployed in a single AZ.
        :type NodeSet: list of RedisNodeInfo
        :param _ResourceTags: The tag for an instance
        :type ResourceTags: list of ResourceTag
        :param _ZoneName: Name of the AZ where the instance resides. For more information, see [Regions and AZs](https://intl.cloud.tencent.com/document/product/239/4106?from_cn_redirect=1).
        :type ZoneName: str
        :param _TemplateId: The parameter template ID associated with the instance
- If this parameter is not configured, the system will automatically adapt the corresponding default template based on the selected compatible version and architecture.
- Query the list of parameter templates of an instance to get the template ID through the [DescribeParamTemplates](https://intl.cloud.tencent.com/document/product/239/58750?from_cn_redirect=1) API.
        :type TemplateId: str
        :param _DryRun: An internal parameter used to indicate whether to check when creating an instance.
- `false`: Default value. Send a normal request and create an instance if all the requirements are met.
- `true`: Send a check request and create no instance.
        :type DryRun: bool
        :param _ProductVersion: The product edition of the instance
- `local`: Local Disk Edition.
- `cloud`: Cloud Disk Edition.
- `cdc`: Dedicated Cluster Edition. Default value: `local`.
        :type ProductVersion: str
        :param _RedisClusterId: Exclusive cluster ID. When `ProductVersion` is set to `cdc`, this parameter is required.
        :type RedisClusterId: str
        """
        self._TypeId = None
        self._MemSize = None
        self._GoodsNum = None
        self._Period = None
        self._BillingMode = None
        self._ZoneId = None
        self._Password = None
        self._VpcId = None
        self._SubnetId = None
        self._ProjectId = None
        self._AutoRenew = None
        self._SecurityGroupIdList = None
        self._VPort = None
        self._RedisShardNum = None
        self._RedisReplicasNum = None
        self._ReplicasReadonly = None
        self._InstanceName = None
        self._NoAuth = None
        self._NodeSet = None
        self._ResourceTags = None
        self._ZoneName = None
        self._TemplateId = None
        self._DryRun = None
        self._ProductVersion = None
        self._RedisClusterId = None

    @property
    def TypeId(self):
        return self._TypeId

    @TypeId.setter
    def TypeId(self, TypeId):
        self._TypeId = TypeId

    @property
    def MemSize(self):
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def BillingMode(self):
        return self._BillingMode

    @BillingMode.setter
    def BillingMode(self, BillingMode):
        self._BillingMode = BillingMode

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AutoRenew(self):
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def SecurityGroupIdList(self):
        return self._SecurityGroupIdList

    @SecurityGroupIdList.setter
    def SecurityGroupIdList(self, SecurityGroupIdList):
        self._SecurityGroupIdList = SecurityGroupIdList

    @property
    def VPort(self):
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def RedisShardNum(self):
        return self._RedisShardNum

    @RedisShardNum.setter
    def RedisShardNum(self, RedisShardNum):
        self._RedisShardNum = RedisShardNum

    @property
    def RedisReplicasNum(self):
        return self._RedisReplicasNum

    @RedisReplicasNum.setter
    def RedisReplicasNum(self, RedisReplicasNum):
        self._RedisReplicasNum = RedisReplicasNum

    @property
    def ReplicasReadonly(self):
        return self._ReplicasReadonly

    @ReplicasReadonly.setter
    def ReplicasReadonly(self, ReplicasReadonly):
        self._ReplicasReadonly = ReplicasReadonly

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def NoAuth(self):
        return self._NoAuth

    @NoAuth.setter
    def NoAuth(self, NoAuth):
        self._NoAuth = NoAuth

    @property
    def NodeSet(self):
        return self._NodeSet

    @NodeSet.setter
    def NodeSet(self, NodeSet):
        self._NodeSet = NodeSet

    @property
    def ResourceTags(self):
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def ProductVersion(self):
        return self._ProductVersion

    @ProductVersion.setter
    def ProductVersion(self, ProductVersion):
        self._ProductVersion = ProductVersion

    @property
    def RedisClusterId(self):
        return self._RedisClusterId

    @RedisClusterId.setter
    def RedisClusterId(self, RedisClusterId):
        self._RedisClusterId = RedisClusterId


    def _deserialize(self, params):
        self._TypeId = params.get("TypeId")
        self._MemSize = params.get("MemSize")
        self._GoodsNum = params.get("GoodsNum")
        self._Period = params.get("Period")
        self._BillingMode = params.get("BillingMode")
        self._ZoneId = params.get("ZoneId")
        self._Password = params.get("Password")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._ProjectId = params.get("ProjectId")
        self._AutoRenew = params.get("AutoRenew")
        self._SecurityGroupIdList = params.get("SecurityGroupIdList")
        self._VPort = params.get("VPort")
        self._RedisShardNum = params.get("RedisShardNum")
        self._RedisReplicasNum = params.get("RedisReplicasNum")
        self._ReplicasReadonly = params.get("ReplicasReadonly")
        self._InstanceName = params.get("InstanceName")
        self._NoAuth = params.get("NoAuth")
        if params.get("NodeSet") is not None:
            self._NodeSet = []
            for item in params.get("NodeSet"):
                obj = RedisNodeInfo()
                obj._deserialize(item)
                self._NodeSet.append(obj)
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._ZoneName = params.get("ZoneName")
        self._TemplateId = params.get("TemplateId")
        self._DryRun = params.get("DryRun")
        self._ProductVersion = params.get("ProductVersion")
        self._RedisClusterId = params.get("RedisClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstancesResponse(AbstractModel):
    """CreateInstances response structure.

    """

    def __init__(self):
        r"""
        :param _DealId: Transaction ID
        :type DealId: str
        :param _InstanceIds: Instance ID
        :type InstanceIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealId = None
        self._InstanceIds = None
        self._RequestId = None

    @property
    def DealId(self):
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._InstanceIds = params.get("InstanceIds")
        self._RequestId = params.get("RequestId")


class CreateParamTemplateRequest(AbstractModel):
    """CreateParamTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Parameter template name.
        :type Name: str
        :param _Description: Parameter template description.
        :type Description: str
        :param _ProductType: Instance type. Valid values: `1` (Redis 2.8 Memory Edition in cluster architecture), `2` (Redis 2.8 Memory Edition in standard architecture), `3` (CKV 3.2 Memory Edition in standard architecture), `4` (CKV 3.2 Memory Edition in cluster architecture), `5` (Redis 2.8 Memory Edition in standalone architecture), `6` (Redis 4.0 Memory Edition in standard architecture), `7` (Redis 4.0 Memory Edition in cluster architecture), `8` (Redis 5.0 Memory Edition in standard architecture), `9` (Redis 5.0 Memory Edition in cluster architecture). If `TempateId` is specified, this parameter can be left blank; otherwise, it is required.
        :type ProductType: int
        :param _TemplateId: ID of the source parameter template.
        :type TemplateId: str
        :param _ParamList: Parameter list.
        :type ParamList: list of InstanceParam
        """
        self._Name = None
        self._Description = None
        self._ProductType = None
        self._TemplateId = None
        self._ParamList = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ProductType(self):
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def ParamList(self):
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._ProductType = params.get("ProductType")
        self._TemplateId = params.get("TemplateId")
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = InstanceParam()
                obj._deserialize(item)
                self._ParamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateParamTemplateResponse(AbstractModel):
    """CreateParamTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Parameter template ID.
        :type TemplateId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TemplateId = None
        self._RequestId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._RequestId = params.get("RequestId")


class DelayDistribution(AbstractModel):
    """Delay distribution details

    """

    def __init__(self):
        r"""
        :param _Ladder: The delay distribution. The mapping between delay range and `Ladder` value is as follows:  - `1`: [0ms,1ms]. - `5`: [1ms,5ms]. - `10`: [5ms,10ms]. - `50`: [10ms,50ms]. - `200`:  [50ms,200ms]. - `-1`: [200ms,∞].
        :type Ladder: int
        :param _Size: The number of commands with delay falling within the current delay range -
        :type Size: int
        :param _Updatetime: Modification time
        :type Updatetime: int
        """
        self._Ladder = None
        self._Size = None
        self._Updatetime = None

    @property
    def Ladder(self):
        return self._Ladder

    @Ladder.setter
    def Ladder(self, Ladder):
        self._Ladder = Ladder

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Updatetime(self):
        return self._Updatetime

    @Updatetime.setter
    def Updatetime(self, Updatetime):
        self._Updatetime = Updatetime


    def _deserialize(self, params):
        self._Ladder = params.get("Ladder")
        self._Size = params.get("Size")
        self._Updatetime = params.get("Updatetime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceAccountRequest(AbstractModel):
    """DeleteInstanceAccount request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _AccountName: Sub-account name
        :type AccountName: str
        """
        self._InstanceId = None
        self._AccountName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AccountName = params.get("AccountName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceAccountResponse(AbstractModel):
    """DeleteInstanceAccount response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteParamTemplateRequest(AbstractModel):
    """DeleteParamTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Parameter template ID.
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteParamTemplateResponse(AbstractModel):
    """DeleteParamTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAutoBackupConfigRequest(AbstractModel):
    """DescribeAutoBackupConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of the specified instance,  such as  "crs-xjhsdj****" Log in to the [Redis console](https://console.cloud.tencent.com/redis) and copy the instance ID in the instance list.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class DescribeAutoBackupConfigResponse(AbstractModel):
    """DescribeAutoBackupConfig response structure.

    """

    def __init__(self):
        r"""
        :param _AutoBackupType: This parameter is retained due to compatibility and can be ignored.
        :type AutoBackupType: int
        :param _WeekDays: Backup cycle, which will be daily by default. Valid values: `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, `Sunday`.
        :type WeekDays: list of str
        :param _TimePeriod: Time period for backup task initialization
        :type TimePeriod: str
        :param _BackupStorageDays: Retention time of full backup files in days.  Default value: `7`.  To retain the files for more days, [submit a ticket](https://console.cloud.tencent.com/workorder/category) for application.
        :type BackupStorageDays: int
        :param _BinlogStorageDays: This parameter has been disused.
        :type BinlogStorageDays: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AutoBackupType = None
        self._WeekDays = None
        self._TimePeriod = None
        self._BackupStorageDays = None
        self._BinlogStorageDays = None
        self._RequestId = None

    @property
    def AutoBackupType(self):
        return self._AutoBackupType

    @AutoBackupType.setter
    def AutoBackupType(self, AutoBackupType):
        self._AutoBackupType = AutoBackupType

    @property
    def WeekDays(self):
        return self._WeekDays

    @WeekDays.setter
    def WeekDays(self, WeekDays):
        self._WeekDays = WeekDays

    @property
    def TimePeriod(self):
        return self._TimePeriod

    @TimePeriod.setter
    def TimePeriod(self, TimePeriod):
        self._TimePeriod = TimePeriod

    @property
    def BackupStorageDays(self):
        return self._BackupStorageDays

    @BackupStorageDays.setter
    def BackupStorageDays(self, BackupStorageDays):
        self._BackupStorageDays = BackupStorageDays

    @property
    def BinlogStorageDays(self):
        return self._BinlogStorageDays

    @BinlogStorageDays.setter
    def BinlogStorageDays(self, BinlogStorageDays):
        self._BinlogStorageDays = BinlogStorageDays

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AutoBackupType = params.get("AutoBackupType")
        self._WeekDays = params.get("WeekDays")
        self._TimePeriod = params.get("TimePeriod")
        self._BackupStorageDays = params.get("BackupStorageDays")
        self._BinlogStorageDays = params.get("BinlogStorageDays")
        self._RequestId = params.get("RequestId")


class DescribeBackupDownloadRestrictionRequest(AbstractModel):
    """DescribeBackupDownloadRestriction request structure.

    """


class DescribeBackupDownloadRestrictionResponse(AbstractModel):
    """DescribeBackupDownloadRestriction response structure.

    """

    def __init__(self):
        r"""
        :param _LimitType: Type of the network restrictions for downloading backup files. Valid values:

- `NoLimit`: Backup files can be downloaded over both public and private networks.
- `LimitOnlyIntranet`: Backup files can be downloaded only at private network addresses auto-assigned by Tencent Cloud.
- `Customize`: Backup files can be downloaded only in the customized VPC.
        :type LimitType: str
        :param _VpcComparisonSymbol: Only `In` can be passed in for this parameter, indicating that backup files can be downloaded in the custom `LimitVpc`.
        :type VpcComparisonSymbol: str
        :param _IpComparisonSymbol: Whether backups can be downloaded at the custom `LimitIp` address.

- `In`: Download is allowed for the custom IP.
- `NotIn`: Download is not allowed for the custom IP.
        :type IpComparisonSymbol: str
        :param _LimitVpc: VPC ID of the custom backup file download address, which will be displayed if `LimitType` is `Customize`.
        :type LimitVpc: list of BackupLimitVpcItem
        :param _LimitIp: VPC ID of the custom backup file download address, which will be displayed if `LimitType` is `Customize`.
        :type LimitIp: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LimitType = None
        self._VpcComparisonSymbol = None
        self._IpComparisonSymbol = None
        self._LimitVpc = None
        self._LimitIp = None
        self._RequestId = None

    @property
    def LimitType(self):
        return self._LimitType

    @LimitType.setter
    def LimitType(self, LimitType):
        self._LimitType = LimitType

    @property
    def VpcComparisonSymbol(self):
        return self._VpcComparisonSymbol

    @VpcComparisonSymbol.setter
    def VpcComparisonSymbol(self, VpcComparisonSymbol):
        self._VpcComparisonSymbol = VpcComparisonSymbol

    @property
    def IpComparisonSymbol(self):
        return self._IpComparisonSymbol

    @IpComparisonSymbol.setter
    def IpComparisonSymbol(self, IpComparisonSymbol):
        self._IpComparisonSymbol = IpComparisonSymbol

    @property
    def LimitVpc(self):
        return self._LimitVpc

    @LimitVpc.setter
    def LimitVpc(self, LimitVpc):
        self._LimitVpc = LimitVpc

    @property
    def LimitIp(self):
        return self._LimitIp

    @LimitIp.setter
    def LimitIp(self, LimitIp):
        self._LimitIp = LimitIp

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LimitType = params.get("LimitType")
        self._VpcComparisonSymbol = params.get("VpcComparisonSymbol")
        self._IpComparisonSymbol = params.get("IpComparisonSymbol")
        if params.get("LimitVpc") is not None:
            self._LimitVpc = []
            for item in params.get("LimitVpc"):
                obj = BackupLimitVpcItem()
                obj._deserialize(item)
                self._LimitVpc.append(obj)
        self._LimitIp = params.get("LimitIp")
        self._RequestId = params.get("RequestId")


class DescribeBackupUrlRequest(AbstractModel):
    """DescribeBackupUrl request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _BackupId: Backup ID, which can be obtained through the `RedisBackupSet` parameter returned by the [DescribeInstanceBackups](https://intl.cloud.tencent.com/document/product/239/20011?from_cn_redirect=1) API.
        :type BackupId: str
        :param _LimitType: Type of the network restriction for downloading backup files. If this parameter is not configured, the user-defined configuration will be used.

- `NoLimit`: Backup files can be downloaded over both public and private networks.
- `LimitOnlyIntranet`: Backup files can be downloaded only at private network addresses auto-assigned by Tencent Cloud.
- `Customize`: Backup files can be downloaded only in the customized VPC.
        :type LimitType: str
        :param _VpcComparisonSymbol: Only `In` can be passed in for this parameter, indicating that backup files can be downloaded in the custom `LimitVpc`.
        :type VpcComparisonSymbol: str
        :param _IpComparisonSymbol: Whether backups can be downloaded at the custom `LimitIp` address.

- `In` (default value): Download is allowed for the custom IP.
- `NotIn`: Download is not allowed for the custom IP.
        :type IpComparisonSymbol: str
        :param _LimitVpc: VPC ID of the custom backup file download address, which is required if `LimitType` is `Customize`.
        :type LimitVpc: list of BackupLimitVpcItem
        :param _LimitIp: VPC IP of the custom backup file download address, which is required if `LimitType` is `Customize`.
        :type LimitIp: list of str
        """
        self._InstanceId = None
        self._BackupId = None
        self._LimitType = None
        self._VpcComparisonSymbol = None
        self._IpComparisonSymbol = None
        self._LimitVpc = None
        self._LimitIp = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def LimitType(self):
        return self._LimitType

    @LimitType.setter
    def LimitType(self, LimitType):
        self._LimitType = LimitType

    @property
    def VpcComparisonSymbol(self):
        return self._VpcComparisonSymbol

    @VpcComparisonSymbol.setter
    def VpcComparisonSymbol(self, VpcComparisonSymbol):
        self._VpcComparisonSymbol = VpcComparisonSymbol

    @property
    def IpComparisonSymbol(self):
        return self._IpComparisonSymbol

    @IpComparisonSymbol.setter
    def IpComparisonSymbol(self, IpComparisonSymbol):
        self._IpComparisonSymbol = IpComparisonSymbol

    @property
    def LimitVpc(self):
        return self._LimitVpc

    @LimitVpc.setter
    def LimitVpc(self, LimitVpc):
        self._LimitVpc = LimitVpc

    @property
    def LimitIp(self):
        return self._LimitIp

    @LimitIp.setter
    def LimitIp(self, LimitIp):
        self._LimitIp = LimitIp


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupId = params.get("BackupId")
        self._LimitType = params.get("LimitType")
        self._VpcComparisonSymbol = params.get("VpcComparisonSymbol")
        self._IpComparisonSymbol = params.get("IpComparisonSymbol")
        if params.get("LimitVpc") is not None:
            self._LimitVpc = []
            for item in params.get("LimitVpc"):
                obj = BackupLimitVpcItem()
                obj._deserialize(item)
                self._LimitVpc.append(obj)
        self._LimitIp = params.get("LimitIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupUrlResponse(AbstractModel):
    """DescribeBackupUrl response structure.

    """

    def __init__(self):
        r"""
        :param _DownloadUrl: Public network download address (valid for six hours). This field will be disused soon.
        :type DownloadUrl: list of str
        :param _InnerDownloadUrl: Private network download address (valid for six hours). This field will be disused soon.
        :type InnerDownloadUrl: list of str
        :param _Filenames: Filename. This field will be disused soon.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Filenames: list of str
        :param _BackupInfos: List of backup file information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupInfos: list of BackupDownloadInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DownloadUrl = None
        self._InnerDownloadUrl = None
        self._Filenames = None
        self._BackupInfos = None
        self._RequestId = None

    @property
    def DownloadUrl(self):
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def InnerDownloadUrl(self):
        return self._InnerDownloadUrl

    @InnerDownloadUrl.setter
    def InnerDownloadUrl(self, InnerDownloadUrl):
        self._InnerDownloadUrl = InnerDownloadUrl

    @property
    def Filenames(self):
        return self._Filenames

    @Filenames.setter
    def Filenames(self, Filenames):
        self._Filenames = Filenames

    @property
    def BackupInfos(self):
        return self._BackupInfos

    @BackupInfos.setter
    def BackupInfos(self, BackupInfos):
        self._BackupInfos = BackupInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DownloadUrl = params.get("DownloadUrl")
        self._InnerDownloadUrl = params.get("InnerDownloadUrl")
        self._Filenames = params.get("Filenames")
        if params.get("BackupInfos") is not None:
            self._BackupInfos = []
            for item in params.get("BackupInfos"):
                obj = BackupDownloadInfo()
                obj._deserialize(item)
                self._BackupInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBandwidthRangeRequest(AbstractModel):
    """DescribeBandwidthRange request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class DescribeBandwidthRangeResponse(AbstractModel):
    """DescribeBandwidthRange response structure.

    """

    def __init__(self):
        r"""
        :param _BaseBandwidth: Standard bandwidth, which is the bandwidth allocated by the system to each node when an instance is purchased.
        :type BaseBandwidth: int
        :param _AddBandwidth: The additional bandwidth of the instance. If the standard bandwidth does not meet your needs, you can increase the bandwidth on your own. <ul><li>If read-only replica is enabled, the total instance bandwidth = additional bandwidth * shard quantity + standard bandwidth * shard quantity * Max ([read-only replica quantity, 1]). The shard quantity in the standard architecture is 1. </li><li>If read-only replica is not enabled, the total instance bandwidth = additional bandwidth * shard quantity + standard bandwidth * shard quantity. The shard quantity in the standard architecture is 1.</li></ul>
        :type AddBandwidth: int
        :param _MinAddBandwidth: The lower limit for additional bandwidth
        :type MinAddBandwidth: int
        :param _MaxAddBandwidth: The upper limit for additional bandwidth
        :type MaxAddBandwidth: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BaseBandwidth = None
        self._AddBandwidth = None
        self._MinAddBandwidth = None
        self._MaxAddBandwidth = None
        self._RequestId = None

    @property
    def BaseBandwidth(self):
        return self._BaseBandwidth

    @BaseBandwidth.setter
    def BaseBandwidth(self, BaseBandwidth):
        self._BaseBandwidth = BaseBandwidth

    @property
    def AddBandwidth(self):
        return self._AddBandwidth

    @AddBandwidth.setter
    def AddBandwidth(self, AddBandwidth):
        self._AddBandwidth = AddBandwidth

    @property
    def MinAddBandwidth(self):
        return self._MinAddBandwidth

    @MinAddBandwidth.setter
    def MinAddBandwidth(self, MinAddBandwidth):
        self._MinAddBandwidth = MinAddBandwidth

    @property
    def MaxAddBandwidth(self):
        return self._MaxAddBandwidth

    @MaxAddBandwidth.setter
    def MaxAddBandwidth(self, MaxAddBandwidth):
        self._MaxAddBandwidth = MaxAddBandwidth

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BaseBandwidth = params.get("BaseBandwidth")
        self._AddBandwidth = params.get("AddBandwidth")
        self._MinAddBandwidth = params.get("MinAddBandwidth")
        self._MaxAddBandwidth = params.get("MaxAddBandwidth")
        self._RequestId = params.get("RequestId")


class DescribeCommonDBInstancesRequest(AbstractModel):
    """DescribeCommonDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _VpcIds: List of VPC IDs
        :type VpcIds: list of int
        :param _SubnetIds: List of subnet IDs
        :type SubnetIds: list of int
        :param _PayMode: List of billing modes. 0: monthly subscription; 1: pay-as-you-go
        :type PayMode: int
        :param _InstanceIds: List of instance IDs
        :type InstanceIds: list of str
        :param _InstanceNames: List of instance names
        :type InstanceNames: list of str
        :param _Status: List of instance status
        :type Status: list of str
        :param _OrderBy: Sorting field
        :type OrderBy: str
        :param _OrderByType: Sorting order
        :type OrderByType: str
        :param _Vips: List of instance VIPs
        :type Vips: list of str
        :param _UniqVpcIds: List of VPC IDs
        :type UniqVpcIds: list of str
        :param _UniqSubnetIds: List of unique subnet IDs
        :type UniqSubnetIds: list of str
        :param _Limit: Quantity limit. Recommended default value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0
        :type Offset: int
        """
        self._VpcIds = None
        self._SubnetIds = None
        self._PayMode = None
        self._InstanceIds = None
        self._InstanceNames = None
        self._Status = None
        self._OrderBy = None
        self._OrderByType = None
        self._Vips = None
        self._UniqVpcIds = None
        self._UniqSubnetIds = None
        self._Limit = None
        self._Offset = None

    @property
    def VpcIds(self):
        return self._VpcIds

    @VpcIds.setter
    def VpcIds(self, VpcIds):
        self._VpcIds = VpcIds

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceNames(self):
        return self._InstanceNames

    @InstanceNames.setter
    def InstanceNames(self, InstanceNames):
        self._InstanceNames = InstanceNames

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Vips(self):
        return self._Vips

    @Vips.setter
    def Vips(self, Vips):
        self._Vips = Vips

    @property
    def UniqVpcIds(self):
        return self._UniqVpcIds

    @UniqVpcIds.setter
    def UniqVpcIds(self, UniqVpcIds):
        self._UniqVpcIds = UniqVpcIds

    @property
    def UniqSubnetIds(self):
        return self._UniqSubnetIds

    @UniqSubnetIds.setter
    def UniqSubnetIds(self, UniqSubnetIds):
        self._UniqSubnetIds = UniqSubnetIds

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._VpcIds = params.get("VpcIds")
        self._SubnetIds = params.get("SubnetIds")
        self._PayMode = params.get("PayMode")
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceNames = params.get("InstanceNames")
        self._Status = params.get("Status")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._Vips = params.get("Vips")
        self._UniqVpcIds = params.get("UniqVpcIds")
        self._UniqSubnetIds = params.get("UniqSubnetIds")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCommonDBInstancesResponse(AbstractModel):
    """DescribeCommonDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of instances
        :type TotalCount: int
        :param _InstanceDetails: Instance information
        :type InstanceDetails: list of RedisCommonInstanceList
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceDetails = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceDetails(self):
        return self._InstanceDetails

    @InstanceDetails.setter
    def InstanceDetails(self, InstanceDetails):
        self._InstanceDetails = InstanceDetails

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceDetails") is not None:
            self._InstanceDetails = []
            for item in params.get("InstanceDetails"):
                obj = RedisCommonInstanceList()
                obj._deserialize(item)
                self._InstanceDetails.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBSecurityGroupsRequest(AbstractModel):
    """DescribeDBSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _Product: Database engine name, which is `redis` for this API.
        :type Product: str
        :param _InstanceId: ID of the specified instance,  such as  "crs-xjhsdj****" Log in to the [Redis console](https://console.cloud.tencent.com/redis) and copy the instance ID in the instance list.

        :type InstanceId: str
        """
        self._Product = None
        self._InstanceId = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSecurityGroupsResponse(AbstractModel):
    """DescribeDBSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _Groups: Security group rules
        :type Groups: list of SecurityGroup
        :param _VIP: Private IPv4 address of an instance
        :type VIP: str
        :param _VPort: Private network port
        :type VPort: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Groups = None
        self._VIP = None
        self._VPort = None
        self._RequestId = None

    @property
    def Groups(self):
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def VIP(self):
        return self._VIP

    @VIP.setter
    def VIP(self, VIP):
        self._VIP = VIP

    @property
    def VPort(self):
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._VIP = params.get("VIP")
        self._VPort = params.get("VPort")
        self._RequestId = params.get("RequestId")


class DescribeInstanceAccountRequest(AbstractModel):
    """DescribeInstanceAccount request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of a specified instance,  such as  "crs-xjhsdj****" Log in to the [Redis console](https://console.cloud.tencent.com/redis) and copy the instance ID in the instance list.
        :type InstanceId: str
        :param _Limit: Number of entries per page
        :type Limit: int
        :param _Offset: Pagination offset,  which is an integral multiple of `Limit`.  Calculation formula:  `offset` = `limit` * (page number - 1).
        :type Offset: int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceAccountResponse(AbstractModel):
    """DescribeInstanceAccount response structure.

    """

    def __init__(self):
        r"""
        :param _Accounts: Account details 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type Accounts: list of Account
        :param _TotalCount: Number of accounts 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Accounts = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Accounts(self):
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self._Accounts.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeInstanceBackupsRequest(AbstractModel):
    """DescribeInstanceBackups request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of backups returned per page. Default value: `20`. Maximum value: `100`.
        :type Limit: int
        :param _Offset: Pagination offset, which is an integral multiple of `Limit`. `offset` = `limit` * (page number - 1).
        :type Offset: int
        :param _InstanceId: ID of the instance to be operated on, which can be obtained through the `InstanceId` field in the return value of the `DescribeInstance` API.
        :type InstanceId: str
        :param _BeginTime: Start time in the format of yyyy-MM-dd HH:mm:ss, such as 2017-02-08 16:46:34. This parameter is used to query the list of instance backups started during the [beginTime, endTime] range.
        :type BeginTime: str
        :param _EndTime: End time in the format of yyyy-MM-dd HH:mm:ss, such as 2017-02-08 19:09:26. This parameter is used to query the list of instance backups started during the [beginTime, endTime] range.
        :type EndTime: str
        :param _Status: Backup task status:
`1`: The backup is in the process.
`2`: The backup is normal.
`3`: The backup is being converted to an RDB file.
`4`: Conversion to RDB has been completed.
`-1`: The backup expired.
`-2`: The backup has been deleted.
        :type Status: list of int
        :param _InstanceName: Instance name, which can be fuzzily searched.
        :type InstanceName: str
        """
        self._Limit = None
        self._Offset = None
        self._InstanceId = None
        self._BeginTime = None
        self._EndTime = None
        self._Status = None
        self._InstanceName = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._InstanceId = params.get("InstanceId")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceBackupsResponse(AbstractModel):
    """DescribeInstanceBackups response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of backups.
        :type TotalCount: int
        :param _BackupSet: Array of instance backups.
        :type BackupSet: list of RedisBackupSet
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._BackupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BackupSet(self):
        return self._BackupSet

    @BackupSet.setter
    def BackupSet(self, BackupSet):
        self._BackupSet = BackupSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("BackupSet") is not None:
            self._BackupSet = []
            for item in params.get("BackupSet"):
                obj = RedisBackupSet()
                obj._deserialize(item)
                self._BackupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceDTSInfoRequest(AbstractModel):
    """DescribeInstanceDTSInfo request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class DescribeInstanceDTSInfoResponse(AbstractModel):
    """DescribeInstanceDTSInfo response structure.

    """

    def __init__(self):
        r"""
        :param _JobId: DTS task ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobId: str
        :param _JobName: DTS task name
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobName: str
        :param _Status: Task status. Valid values: 1 (Creating), 3 (Checking), 4 (CheckPass), 5 (CheckNotPass), 7 (Running), 8 (ReadyComplete), 9 (Success), 10 (Failed), 11 (Stopping), 12 (Completing)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _StatusDesc: Status description
Note: This field may return null, indicating that no valid values can be obtained.
        :type StatusDesc: str
        :param _Offset: Sync latency in bytes
Note: This field may return null, indicating that no valid values can be obtained.
        :type Offset: int
        :param _CutDownTime: Disconnection time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CutDownTime: str
        :param _SrcInfo: Source instance information
Note: This field may return null, indicating that no valid values can be obtained.
        :type SrcInfo: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceDTSInstanceInfo`
        :param _DstInfo: Target instance information
Note: This field may return null, indicating that no valid values can be obtained.
        :type DstInfo: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceDTSInstanceInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._JobId = None
        self._JobName = None
        self._Status = None
        self._StatusDesc = None
        self._Offset = None
        self._CutDownTime = None
        self._SrcInfo = None
        self._DstInfo = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def CutDownTime(self):
        return self._CutDownTime

    @CutDownTime.setter
    def CutDownTime(self, CutDownTime):
        self._CutDownTime = CutDownTime

    @property
    def SrcInfo(self):
        return self._SrcInfo

    @SrcInfo.setter
    def SrcInfo(self, SrcInfo):
        self._SrcInfo = SrcInfo

    @property
    def DstInfo(self):
        return self._DstInfo

    @DstInfo.setter
    def DstInfo(self, DstInfo):
        self._DstInfo = DstInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._Offset = params.get("Offset")
        self._CutDownTime = params.get("CutDownTime")
        if params.get("SrcInfo") is not None:
            self._SrcInfo = DescribeInstanceDTSInstanceInfo()
            self._SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("DstInfo") is not None:
            self._DstInfo = DescribeInstanceDTSInstanceInfo()
            self._DstInfo._deserialize(params.get("DstInfo"))
        self._RequestId = params.get("RequestId")


class DescribeInstanceDTSInstanceInfo(AbstractModel):
    """Details of instances in the DTS task

    """

    def __init__(self):
        r"""
        :param _RegionId: Region ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionId: int
        :param _InstanceId: Instance ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _SetId: Repository ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type SetId: int
        :param _ZoneId: AZ ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneId: int
        :param _Type: Instance type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: int
        :param _InstanceName: Instance name
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param _Vip: Instance access address
Note: This field may return null, indicating that no valid values can be obtained.
        :type Vip: str
        :param _Status: Status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        """
        self._RegionId = None
        self._InstanceId = None
        self._SetId = None
        self._ZoneId = None
        self._Type = None
        self._InstanceName = None
        self._Vip = None
        self._Status = None

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SetId(self):
        return self._SetId

    @SetId.setter
    def SetId(self, SetId):
        self._SetId = SetId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._InstanceId = params.get("InstanceId")
        self._SetId = params.get("SetId")
        self._ZoneId = params.get("ZoneId")
        self._Type = params.get("Type")
        self._InstanceName = params.get("InstanceName")
        self._Vip = params.get("Vip")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceDealDetailRequest(AbstractModel):
    """DescribeInstanceDealDetail request structure.

    """

    def __init__(self):
        r"""
        :param _DealIds: Array of order transaction IDs, i.e., the `DealId` output parameter of the [CreateInstances](https://intl.cloud.tencent.com/document/api/239/20026?from_cn_redirect=1) API.
        :type DealIds: list of str
        """
        self._DealIds = None

    @property
    def DealIds(self):
        return self._DealIds

    @DealIds.setter
    def DealIds(self, DealIds):
        self._DealIds = DealIds


    def _deserialize(self, params):
        self._DealIds = params.get("DealIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceDealDetailResponse(AbstractModel):
    """DescribeInstanceDealDetail response structure.

    """

    def __init__(self):
        r"""
        :param _DealDetails: Order details
        :type DealDetails: list of TradeDealDetail
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealDetails = None
        self._RequestId = None

    @property
    def DealDetails(self):
        return self._DealDetails

    @DealDetails.setter
    def DealDetails(self, DealDetails):
        self._DealDetails = DealDetails

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DealDetails") is not None:
            self._DealDetails = []
            for item in params.get("DealDetails"):
                obj = TradeDealDetail()
                obj._deserialize(item)
                self._DealDetails.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceMonitorBigKeyRequest(AbstractModel):
    """DescribeInstanceMonitorBigKey request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ReqType: Request type. 1: string type; 2: all types
        :type ReqType: int
        :param _Date: Time, such as "20190219"
        :type Date: str
        """
        self._InstanceId = None
        self._ReqType = None
        self._Date = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ReqType(self):
        return self._ReqType

    @ReqType.setter
    def ReqType(self, ReqType):
        self._ReqType = ReqType

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ReqType = params.get("ReqType")
        self._Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorBigKeyResponse(AbstractModel):
    """DescribeInstanceMonitorBigKey response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Big key details
        :type Data: list of BigKeyInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = BigKeyInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceMonitorBigKeySizeDistRequest(AbstractModel):
    """DescribeInstanceMonitorBigKeySizeDist request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Date: Time, such as "20190219"
        :type Date: str
        """
        self._InstanceId = None
        self._Date = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorBigKeySizeDistResponse(AbstractModel):
    """DescribeInstanceMonitorBigKeySizeDist response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Big key size distribution details
        :type Data: list of DelayDistribution
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DelayDistribution()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceMonitorBigKeyTypeDistRequest(AbstractModel):
    """DescribeInstanceMonitorBigKeyTypeDist request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Date: Time, such as "20190219"
        :type Date: str
        """
        self._InstanceId = None
        self._Date = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorBigKeyTypeDistResponse(AbstractModel):
    """DescribeInstanceMonitorBigKeyTypeDist response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Big key type distribution details
        :type Data: list of BigKeyTypeInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = BigKeyTypeInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceMonitorHotKeyRequest(AbstractModel):
    """DescribeInstanceMonitorHotKey request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _SpanType: Time span. 1: real time; 2: past 30 minutes; 3: past 6 hours; 4: past 24 hours
        :type SpanType: int
        """
        self._InstanceId = None
        self._SpanType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SpanType(self):
        return self._SpanType

    @SpanType.setter
    def SpanType(self, SpanType):
        self._SpanType = SpanType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SpanType = params.get("SpanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorHotKeyResponse(AbstractModel):
    """DescribeInstanceMonitorHotKey response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Hot key details
        :type Data: list of HotKeyInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = HotKeyInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceMonitorSIPRequest(AbstractModel):
    """DescribeInstanceMonitorSIP request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class DescribeInstanceMonitorSIPResponse(AbstractModel):
    """DescribeInstanceMonitorSIP response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Access source information
        :type Data: list of SourceInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SourceInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceMonitorTookDistRequest(AbstractModel):
    """DescribeInstanceMonitorTookDist request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Date: Time, such as "20190219"
        :type Date: str
        :param _SpanType: Time span. 1: real time; 2: last 30 minutes; 3: last 6 hours; 4: last 24 hours
        :type SpanType: int
        """
        self._InstanceId = None
        self._Date = None
        self._SpanType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def SpanType(self):
        return self._SpanType

    @SpanType.setter
    def SpanType(self, SpanType):
        self._SpanType = SpanType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Date = params.get("Date")
        self._SpanType = params.get("SpanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorTookDistResponse(AbstractModel):
    """DescribeInstanceMonitorTookDist response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Latency distribution information
        :type Data: list of DelayDistribution
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DelayDistribution()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceMonitorTopNCmdRequest(AbstractModel):
    """DescribeInstanceMonitorTopNCmd request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _SpanType: Time span. 1: real time; 2: last 30 minutes; 3: last 6 hours; 4: last 24 hours
        :type SpanType: int
        """
        self._InstanceId = None
        self._SpanType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SpanType(self):
        return self._SpanType

    @SpanType.setter
    def SpanType(self, SpanType):
        self._SpanType = SpanType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SpanType = params.get("SpanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorTopNCmdResponse(AbstractModel):
    """DescribeInstanceMonitorTopNCmd response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Access command information
        :type Data: list of SourceCommand
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SourceCommand()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceMonitorTopNCmdTookRequest(AbstractModel):
    """DescribeInstanceMonitorTopNCmdTook request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _SpanType: Time span. 1: real time; 2: last 30 minutes; 3: last 6 hours; 4: last 24 hours
        :type SpanType: int
        """
        self._InstanceId = None
        self._SpanType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SpanType(self):
        return self._SpanType

    @SpanType.setter
    def SpanType(self, SpanType):
        self._SpanType = SpanType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SpanType = params.get("SpanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorTopNCmdTookResponse(AbstractModel):
    """DescribeInstanceMonitorTopNCmdTook response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Duration details
        :type Data: list of CommandTake
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CommandTake()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceNodeInfoRequest(AbstractModel):
    """DescribeInstanceNodeInfo request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of a specified instance,  such as  "crs-xjhsdj****" Log in to the [Redis console](https://console.cloud.tencent.com/redis) and copy the instance ID in the instance list.
        :type InstanceId: str
        :param _Limit: List size Size of node information returned per page.  Default value: `20`. Maximum value: `1000`.  This field has been disused.
        :type Limit: int
        :param _Offset: Pagination offset, which is an integral multiple of `Limit`. Calculation formula:  `offset` = `limit` * (page number - 1). This field has been disused.
        :type Offset: int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceNodeInfoResponse(AbstractModel):
    """DescribeInstanceNodeInfo response structure.

    """

    def __init__(self):
        r"""
        :param _ProxyCount: The number of proxy nodes
        :type ProxyCount: int
        :param _Proxy: Proxy node information 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type Proxy: list of ProxyNodes
        :param _RedisCount: The number of Redis nodes
        :type RedisCount: int
        :param _Redis: Redis node information 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type Redis: list of RedisNodes
        :param _TendisCount: This parameter has been disused.
        :type TendisCount: int
        :param _Tendis: This parameter has been disused. 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type Tendis: list of TendisNodes
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProxyCount = None
        self._Proxy = None
        self._RedisCount = None
        self._Redis = None
        self._TendisCount = None
        self._Tendis = None
        self._RequestId = None

    @property
    def ProxyCount(self):
        return self._ProxyCount

    @ProxyCount.setter
    def ProxyCount(self, ProxyCount):
        self._ProxyCount = ProxyCount

    @property
    def Proxy(self):
        return self._Proxy

    @Proxy.setter
    def Proxy(self, Proxy):
        self._Proxy = Proxy

    @property
    def RedisCount(self):
        return self._RedisCount

    @RedisCount.setter
    def RedisCount(self, RedisCount):
        self._RedisCount = RedisCount

    @property
    def Redis(self):
        return self._Redis

    @Redis.setter
    def Redis(self, Redis):
        self._Redis = Redis

    @property
    def TendisCount(self):
        return self._TendisCount

    @TendisCount.setter
    def TendisCount(self, TendisCount):
        self._TendisCount = TendisCount

    @property
    def Tendis(self):
        return self._Tendis

    @Tendis.setter
    def Tendis(self, Tendis):
        self._Tendis = Tendis

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProxyCount = params.get("ProxyCount")
        if params.get("Proxy") is not None:
            self._Proxy = []
            for item in params.get("Proxy"):
                obj = ProxyNodes()
                obj._deserialize(item)
                self._Proxy.append(obj)
        self._RedisCount = params.get("RedisCount")
        if params.get("Redis") is not None:
            self._Redis = []
            for item in params.get("Redis"):
                obj = RedisNodes()
                obj._deserialize(item)
                self._Redis.append(obj)
        self._TendisCount = params.get("TendisCount")
        if params.get("Tendis") is not None:
            self._Tendis = []
            for item in params.get("Tendis"):
                obj = TendisNodes()
                obj._deserialize(item)
                self._Tendis.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceParamRecordsRequest(AbstractModel):
    """DescribeInstanceParamRecords request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Limit: Maximum number of results returned per page
        :type Limit: int
        :param _Offset: Offset, which is an integral multiple of `Limit`.
        :type Offset: int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceParamRecordsResponse(AbstractModel):
    """DescribeInstanceParamRecords response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of modifications.
        :type TotalCount: int
        :param _InstanceParamHistory: Information of modifications.
        :type InstanceParamHistory: list of InstanceParamHistory
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceParamHistory = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceParamHistory(self):
        return self._InstanceParamHistory

    @InstanceParamHistory.setter
    def InstanceParamHistory(self, InstanceParamHistory):
        self._InstanceParamHistory = InstanceParamHistory

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceParamHistory") is not None:
            self._InstanceParamHistory = []
            for item in params.get("InstanceParamHistory"):
                obj = InstanceParamHistory()
                obj._deserialize(item)
                self._InstanceParamHistory.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceParamsRequest(AbstractModel):
    """DescribeInstanceParams request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of a specified instance,  such as  "crs-xjhsdj****" Log in to the [Redis console](https://console.cloud.tencent.com/redis) and copy the instance ID in the instance list.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class DescribeInstanceParamsResponse(AbstractModel):
    """DescribeInstanceParams response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of the parameter lists
        :type TotalCount: int
        :param _InstanceEnumParam: Instance parameter in Enum type
        :type InstanceEnumParam: list of InstanceEnumParam
        :param _InstanceIntegerParam: Instance parameter in Integer type
        :type InstanceIntegerParam: list of InstanceIntegerParam
        :param _InstanceTextParam: Instance parameter in Char type
        :type InstanceTextParam: list of InstanceTextParam
        :param _InstanceMultiParam: Instance parameter in Multi type
        :type InstanceMultiParam: list of InstanceMultiParam
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceEnumParam = None
        self._InstanceIntegerParam = None
        self._InstanceTextParam = None
        self._InstanceMultiParam = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceEnumParam(self):
        return self._InstanceEnumParam

    @InstanceEnumParam.setter
    def InstanceEnumParam(self, InstanceEnumParam):
        self._InstanceEnumParam = InstanceEnumParam

    @property
    def InstanceIntegerParam(self):
        return self._InstanceIntegerParam

    @InstanceIntegerParam.setter
    def InstanceIntegerParam(self, InstanceIntegerParam):
        self._InstanceIntegerParam = InstanceIntegerParam

    @property
    def InstanceTextParam(self):
        return self._InstanceTextParam

    @InstanceTextParam.setter
    def InstanceTextParam(self, InstanceTextParam):
        self._InstanceTextParam = InstanceTextParam

    @property
    def InstanceMultiParam(self):
        return self._InstanceMultiParam

    @InstanceMultiParam.setter
    def InstanceMultiParam(self, InstanceMultiParam):
        self._InstanceMultiParam = InstanceMultiParam

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceEnumParam") is not None:
            self._InstanceEnumParam = []
            for item in params.get("InstanceEnumParam"):
                obj = InstanceEnumParam()
                obj._deserialize(item)
                self._InstanceEnumParam.append(obj)
        if params.get("InstanceIntegerParam") is not None:
            self._InstanceIntegerParam = []
            for item in params.get("InstanceIntegerParam"):
                obj = InstanceIntegerParam()
                obj._deserialize(item)
                self._InstanceIntegerParam.append(obj)
        if params.get("InstanceTextParam") is not None:
            self._InstanceTextParam = []
            for item in params.get("InstanceTextParam"):
                obj = InstanceTextParam()
                obj._deserialize(item)
                self._InstanceTextParam.append(obj)
        if params.get("InstanceMultiParam") is not None:
            self._InstanceMultiParam = []
            for item in params.get("InstanceMultiParam"):
                obj = InstanceMultiParam()
                obj._deserialize(item)
                self._InstanceMultiParam.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceSecurityGroupRequest(AbstractModel):
    """DescribeInstanceSecurityGroup request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: List of instance IDs,  such as "crs-f2ho5rsz\n".
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceSecurityGroupResponse(AbstractModel):
    """DescribeInstanceSecurityGroup response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceSecurityGroupsDetail: Security group information of an instance
        :type InstanceSecurityGroupsDetail: list of InstanceSecurityGroupDetail
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceSecurityGroupsDetail = None
        self._RequestId = None

    @property
    def InstanceSecurityGroupsDetail(self):
        return self._InstanceSecurityGroupsDetail

    @InstanceSecurityGroupsDetail.setter
    def InstanceSecurityGroupsDetail(self, InstanceSecurityGroupsDetail):
        self._InstanceSecurityGroupsDetail = InstanceSecurityGroupsDetail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceSecurityGroupsDetail") is not None:
            self._InstanceSecurityGroupsDetail = []
            for item in params.get("InstanceSecurityGroupsDetail"):
                obj = InstanceSecurityGroupDetail()
                obj._deserialize(item)
                self._InstanceSecurityGroupsDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceShardsRequest(AbstractModel):
    """DescribeInstanceShards request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of a specified instance,  such as  "crs-xjhsdj****" Log in to the [Redis console](https://console.cloud.tencent.com/redis) and copy the instance ID in the instance list.
        :type InstanceId: str
        :param _FilterSlave: Whether to filter out the replica node information. Valid values: `true` (yes),  `false` (no).
        :type FilterSlave: bool
        """
        self._InstanceId = None
        self._FilterSlave = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FilterSlave(self):
        return self._FilterSlave

    @FilterSlave.setter
    def FilterSlave(self, FilterSlave):
        self._FilterSlave = FilterSlave


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._FilterSlave = params.get("FilterSlave")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceShardsResponse(AbstractModel):
    """DescribeInstanceShards response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceShards: List information of the instance shards, which includes  node information, node ID, key count, used capacity, and capacity slope.
        :type InstanceShards: list of InstanceClusterShard
        :param _TotalCount: Number of instance shard nodes
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceShards = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def InstanceShards(self):
        return self._InstanceShards

    @InstanceShards.setter
    def InstanceShards(self, InstanceShards):
        self._InstanceShards = InstanceShards

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceShards") is not None:
            self._InstanceShards = []
            for item in params.get("InstanceShards"):
                obj = InstanceClusterShard()
                obj._deserialize(item)
                self._InstanceShards.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeInstanceZoneInfoRequest(AbstractModel):
    """DescribeInstanceZoneInfo request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of a specified instance,  such as  "crs-xjhsdj****" Log in to the [Redis console](https://console.cloud.tencent.com/redis) and copy the instance ID in the instance list.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class DescribeInstanceZoneInfoResponse(AbstractModel):
    """DescribeInstanceZoneInfo response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of instance node groups
        :type TotalCount: int
        :param _ReplicaGroups: List of instance node groups
        :type ReplicaGroups: list of ReplicaGroup
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ReplicaGroups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ReplicaGroups(self):
        return self._ReplicaGroups

    @ReplicaGroups.setter
    def ReplicaGroups(self, ReplicaGroups):
        self._ReplicaGroups = ReplicaGroups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ReplicaGroups") is not None:
            self._ReplicaGroups = []
            for item in params.get("ReplicaGroups"):
                obj = ReplicaGroup()
                obj._deserialize(item)
                self._ReplicaGroups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of instances returned per page. Default value: `20`. Maximum value: `1000`.
        :type Limit: int
        :param _Offset: Pagination offset, which is an integral multiple of `Limit`. Calculation formula:  `offset` = `limit` * (page number - 1).
        :type Offset: int
        :param _InstanceId: ID of a specified instance,  such as  "crs-xjhsdj****" Log in to the [Redis console](https://console.cloud.tencent.com/redis) and copy the instance ID in the instance list.


        :type InstanceId: str
        :param _OrderBy: Instance list sorting criteria. The enumerated values are as listed below:  <ul><li>`projectId`:  Project ID.  </li><li>`createtime`:  Instance creation time.  </li><li>`instancename`:  Instance name.  </li><li>`type`:  Instance type. </li><li>`curDeadline`:  Instance expiration time. </li></ul>
        :type OrderBy: str
        :param _OrderType: Instance sorting order. <ul><li>`1`: Descending. </li><li>`0`: Ascending. Default value: `1`.</li></ul>
        :type OrderType: int
        :param _VpcIds: Array of VPC IDs such as 47525. If this parameter is not passed in or the array is empty, the classic network will be selected by default. This parameter is retained and can be ignored. It is set based on `UniqVpcIds` parameter format.
        :type VpcIds: list of str
        :param _SubnetIds: Array of VPC subnet IDs such as 56854. This parameter is retained and can be ignored. It is set based on `UniqSubnetIds` parameter format.
        :type SubnetIds: list of str
        :param _SearchKey: Keywords for fuzzy query. which can be used to fuzzy query an instance by its ID or name.
        :type SearchKey: str
        :param _ProjectIds: Array of project IDs
        :type ProjectIds: list of int
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _UniqVpcIds: Array of VPC IDs such as vpc-sad23jfdfk. If this parameter is not passed in or or the array is empty, the classic network will be selected by default.
        :type UniqVpcIds: list of str
        :param _UniqSubnetIds: Array of VPC subnet IDs such as subnet-fdj24n34j2
        :type UniqSubnetIds: list of str
        :param _RegionIds: Array of region IDs (disused). The corresponding region can be queried through the common parameter `Region`.
        :type RegionIds: list of int
        :param _Status: Instance status. <ul><li>`0`: Uninitialized. </li><li>`1`: In the process. </li><li>`2`: Running. </li><li>`-2`: Isolated. </li><li>`-3`: To be deleted. </li></ul>
        :type Status: list of int
        :param _TypeVersion: Instance architecture. <ul><li>`1`: Standalone edition. </li><li>`2`: Master-replica edition. </li><li>`3`: Cluster edition. </li></ul>
        :type TypeVersion: int
        :param _EngineName: Storage engine information. Valid values: `Redis-2.8`, `Redis-4.0`, `Redis-5.0`, `Redis-6.0` or `CKV`.
        :type EngineName: str
        :param _AutoRenew: Renewal mode. Valid values:  <ul><li>`0`:  Manual renewal </li><li>`1`:  Auto-renewal </li><li>`2`:  No renewal upon expiration </ul>
        :type AutoRenew: list of int
        :param _BillingMode: Billing mode. Only pay-as-you-go billing is supported.
        :type BillingMode: str
        :param _Type: Instance type. Valid values:  - `2`: Redis 2.8 Memory Edition (Standard Architecture). - `3`: CKV 3.2 Memory Edition (Standard Architecture). - `4`: CKV 3.2 Memory Edition (Cluster Architecture). - `5`: Redis 2.8 Memory Edition (Standalone). - `6`: Redis 4.0 Memory Edition (Standard Architecture). - `7`: Redis 4.0 Memory Edition (Cluster Architecture). - `8`: Redis 5.0 Memory Edition (Standard Architecture). - `9`: Redis 5.0 Memory Edition (Cluster Architecture). - `15`: Redis 6.2 Memory Edition (Standard Architecture). - `16`: Redis 6.2 Memory Edition (Cluster Architecture).
        :type Type: int
        :param _SearchKeys: Array of the search keywords, which can query the instance by its ID, name, IP address.
        :type SearchKeys: list of str
        :param _TypeList: Internal parameter, which can be ignored.
        :type TypeList: list of int
        :param _MonitorVersion: Internal parameter, which can be ignored.
        :type MonitorVersion: str
        :param _InstanceTags: Resources filter by tag key and value. If this parameter is not specified or is an empty array, resources will not be filtered.
        :type InstanceTags: list of InstanceTagInfo
        :param _TagKeys: Resources filter by tag key. If this parameter is not specified or is an empty array, resources will not be filtered.
        :type TagKeys: list of str
        :param _ProductVersions: Instance product version.  If this parameter is not passed in or the array is empty, the instances will not be filtered based this parameter by default.  <ul><li>`local`:  Local disk edition.  </li><li>`cdc`:  Dedicated cluster edition.  </li></ul>
        :type ProductVersions: list of str
        :param _InstanceIds: Batch query of the specified instances ID. The number of results returned is based on `Limit`.
        :type InstanceIds: list of str
        :param _AzMode: AZ deployment mode. <ul><li>`singleaz`: Single-AZ. </li><li>`1`: Multi-AZ. </li></ul>
        :type AzMode: str
        """
        self._Limit = None
        self._Offset = None
        self._InstanceId = None
        self._OrderBy = None
        self._OrderType = None
        self._VpcIds = None
        self._SubnetIds = None
        self._SearchKey = None
        self._ProjectIds = None
        self._InstanceName = None
        self._UniqVpcIds = None
        self._UniqSubnetIds = None
        self._RegionIds = None
        self._Status = None
        self._TypeVersion = None
        self._EngineName = None
        self._AutoRenew = None
        self._BillingMode = None
        self._Type = None
        self._SearchKeys = None
        self._TypeList = None
        self._MonitorVersion = None
        self._InstanceTags = None
        self._TagKeys = None
        self._ProductVersions = None
        self._InstanceIds = None
        self._AzMode = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderType(self):
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def VpcIds(self):
        return self._VpcIds

    @VpcIds.setter
    def VpcIds(self, VpcIds):
        self._VpcIds = VpcIds

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def UniqVpcIds(self):
        return self._UniqVpcIds

    @UniqVpcIds.setter
    def UniqVpcIds(self, UniqVpcIds):
        self._UniqVpcIds = UniqVpcIds

    @property
    def UniqSubnetIds(self):
        return self._UniqSubnetIds

    @UniqSubnetIds.setter
    def UniqSubnetIds(self, UniqSubnetIds):
        self._UniqSubnetIds = UniqSubnetIds

    @property
    def RegionIds(self):
        return self._RegionIds

    @RegionIds.setter
    def RegionIds(self, RegionIds):
        self._RegionIds = RegionIds

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TypeVersion(self):
        return self._TypeVersion

    @TypeVersion.setter
    def TypeVersion(self, TypeVersion):
        self._TypeVersion = TypeVersion

    @property
    def EngineName(self):
        return self._EngineName

    @EngineName.setter
    def EngineName(self, EngineName):
        self._EngineName = EngineName

    @property
    def AutoRenew(self):
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew

    @property
    def BillingMode(self):
        return self._BillingMode

    @BillingMode.setter
    def BillingMode(self, BillingMode):
        self._BillingMode = BillingMode

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SearchKeys(self):
        return self._SearchKeys

    @SearchKeys.setter
    def SearchKeys(self, SearchKeys):
        self._SearchKeys = SearchKeys

    @property
    def TypeList(self):
        return self._TypeList

    @TypeList.setter
    def TypeList(self, TypeList):
        self._TypeList = TypeList

    @property
    def MonitorVersion(self):
        return self._MonitorVersion

    @MonitorVersion.setter
    def MonitorVersion(self, MonitorVersion):
        self._MonitorVersion = MonitorVersion

    @property
    def InstanceTags(self):
        return self._InstanceTags

    @InstanceTags.setter
    def InstanceTags(self, InstanceTags):
        self._InstanceTags = InstanceTags

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def ProductVersions(self):
        return self._ProductVersions

    @ProductVersions.setter
    def ProductVersions(self, ProductVersions):
        self._ProductVersions = ProductVersions

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def AzMode(self):
        return self._AzMode

    @AzMode.setter
    def AzMode(self, AzMode):
        self._AzMode = AzMode


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._InstanceId = params.get("InstanceId")
        self._OrderBy = params.get("OrderBy")
        self._OrderType = params.get("OrderType")
        self._VpcIds = params.get("VpcIds")
        self._SubnetIds = params.get("SubnetIds")
        self._SearchKey = params.get("SearchKey")
        self._ProjectIds = params.get("ProjectIds")
        self._InstanceName = params.get("InstanceName")
        self._UniqVpcIds = params.get("UniqVpcIds")
        self._UniqSubnetIds = params.get("UniqSubnetIds")
        self._RegionIds = params.get("RegionIds")
        self._Status = params.get("Status")
        self._TypeVersion = params.get("TypeVersion")
        self._EngineName = params.get("EngineName")
        self._AutoRenew = params.get("AutoRenew")
        self._BillingMode = params.get("BillingMode")
        self._Type = params.get("Type")
        self._SearchKeys = params.get("SearchKeys")
        self._TypeList = params.get("TypeList")
        self._MonitorVersion = params.get("MonitorVersion")
        if params.get("InstanceTags") is not None:
            self._InstanceTags = []
            for item in params.get("InstanceTags"):
                obj = InstanceTagInfo()
                obj._deserialize(item)
                self._InstanceTags.append(obj)
        self._TagKeys = params.get("TagKeys")
        self._ProductVersions = params.get("ProductVersions")
        self._InstanceIds = params.get("InstanceIds")
        self._AzMode = params.get("AzMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of instances
        :type TotalCount: int
        :param _InstanceSet: List of instance details
        :type InstanceSet: list of InstanceSet
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceSet(self):
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = InstanceSet()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMaintenanceWindowRequest(AbstractModel):
    """DescribeMaintenanceWindow request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class DescribeMaintenanceWindowResponse(AbstractModel):
    """DescribeMaintenanceWindow response structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time of the maintenance window, such as 17:00.
        :type StartTime: str
        :param _EndTime: End time of the maintenance window, such as 19:00.
        :type EndTime: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._StartTime = None
        self._EndTime = None
        self._RequestId = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RequestId = params.get("RequestId")


class DescribeParamTemplateInfoRequest(AbstractModel):
    """DescribeParamTemplateInfo request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: The parameter template ID for query. Get parameter template list information through the [DescribeParamTemplates](https://intl.cloud.tencent.com/document/product/239/58750?from_cn_redirect=1) API.
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeParamTemplateInfoResponse(AbstractModel):
    """DescribeParamTemplateInfo response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Quantity of parameters in the parameter template
        :type TotalCount: int
        :param _TemplateId: Parameter template ID.
        :type TemplateId: str
        :param _Name: Parameter template name.
        :type Name: str
        :param _ProductType: Product type
- `2`: Redis 2.8 Memory Edition (Standard Architecture).
- `3`: CKV 3.2 Memory Edition (Standard Architecture).
- `4`: CKV 3.2 Memory Edition (Cluster Architecture).
- `5`: Redis 2.8 Memory Edition (Standalone).
- `6`: Redis 4.0 Memory Edition (Standard Architecture).
- `7`: Redis 4.0 Memory Edition (Cluster Architecture).
- `8`: Redis 5.0 Memory Edition (Standard Architecture).
- `9`: Redis 5.0 Memory Edition (Cluster Architecture).
- `15`: Redis 6.2 Memory Edition (Standard Architecture).
- `16`: Redis 6.2 Memory Edition (Cluster Architecture).
        :type ProductType: int
        :param _Description: Parameter template description
        :type Description: str
        :param _Items: Parameter details, including parameter name, current value, default value, maximum value, minimum value, enumeration value and other information.
        :type Items: list of ParameterDetail
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TemplateId = None
        self._Name = None
        self._ProductType = None
        self._Description = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ProductType(self):
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._TemplateId = params.get("TemplateId")
        self._Name = params.get("Name")
        self._ProductType = params.get("ProductType")
        self._Description = params.get("Description")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ParameterDetail()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeParamTemplatesRequest(AbstractModel):
    """DescribeParamTemplates request structure.

    """

    def __init__(self):
        r"""
        :param _ProductTypes: Array of instance types. Valid values: `1` (Redis 2.8 Memory Edition in cluster architecture), `2` (Redis 2.8 Memory Edition in standard architecture), `3` (CKV 3.2 Memory Edition in standard architecture), `4` (CKV 3.2 Memory Edition in cluster architecture), `5` (Redis 2.8 Memory Edition in standalone architecture), `6` (Redis 4.0 Memory Edition in standard architecture), `7` (Redis 4.0 Memory Edition in cluster architecture), `8` (Redis 5.0 Memory Edition in standard architecture), `9` (Redis 5.0 Memory Edition in cluster architecture).
        :type ProductTypes: list of int
        :param _TemplateNames: Array of template names.
        :type TemplateNames: list of str
        :param _TemplateIds: Array of template IDs.
        :type TemplateIds: list of str
        """
        self._ProductTypes = None
        self._TemplateNames = None
        self._TemplateIds = None

    @property
    def ProductTypes(self):
        return self._ProductTypes

    @ProductTypes.setter
    def ProductTypes(self, ProductTypes):
        self._ProductTypes = ProductTypes

    @property
    def TemplateNames(self):
        return self._TemplateNames

    @TemplateNames.setter
    def TemplateNames(self, TemplateNames):
        self._TemplateNames = TemplateNames

    @property
    def TemplateIds(self):
        return self._TemplateIds

    @TemplateIds.setter
    def TemplateIds(self, TemplateIds):
        self._TemplateIds = TemplateIds


    def _deserialize(self, params):
        self._ProductTypes = params.get("ProductTypes")
        self._TemplateNames = params.get("TemplateNames")
        self._TemplateIds = params.get("TemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeParamTemplatesResponse(AbstractModel):
    """DescribeParamTemplates response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of parameter templates of the user.
        :type TotalCount: int
        :param _Items: Parameter template details.
        :type Items: list of ParamTemplateInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ParamTemplateInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProductInfoRequest(AbstractModel):
    """DescribeProductInfo request structure.

    """


class DescribeProductInfoResponse(AbstractModel):
    """DescribeProductInfo response structure.

    """

    def __init__(self):
        r"""
        :param _RegionSet: Sale information of a region.
        :type RegionSet: list of RegionConf
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RegionSet = None
        self._RequestId = None

    @property
    def RegionSet(self):
        return self._RegionSet

    @RegionSet.setter
    def RegionSet(self, RegionSet):
        self._RegionSet = RegionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RegionSet") is not None:
            self._RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionConf()
                obj._deserialize(item)
                self._RegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupRequest(AbstractModel):
    """DescribeProjectSecurityGroup request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: 0: default project; -1: all projects; >0: specified project
        :type ProjectId: int
        :param _SecurityGroupId: Security group ID
        :type SecurityGroupId: str
        """
        self._ProjectId = None
        self._SecurityGroupId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._SecurityGroupId = params.get("SecurityGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectSecurityGroupResponse(AbstractModel):
    """DescribeProjectSecurityGroup response structure.

    """

    def __init__(self):
        r"""
        :param _SecurityGroupDetails: Security group of the project
        :type SecurityGroupDetails: list of SecurityGroupDetail
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecurityGroupDetails = None
        self._RequestId = None

    @property
    def SecurityGroupDetails(self):
        return self._SecurityGroupDetails

    @SecurityGroupDetails.setter
    def SecurityGroupDetails(self, SecurityGroupDetails):
        self._SecurityGroupDetails = SecurityGroupDetails

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SecurityGroupDetails") is not None:
            self._SecurityGroupDetails = []
            for item in params.get("SecurityGroupDetails"):
                obj = SecurityGroupDetail()
                obj._deserialize(item)
                self._SecurityGroupDetails.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    """DescribeProjectSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _Product: Database engine name, which is `redis` for this API.
        :type Product: str
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _Offset: Offset, which is an integral multiple of `Limit`.
        :type Offset: int
        :param _Limit: The number of security groups to be pulled. Default value: `20`.
        :type Limit: int
        :param _SearchKey: Search criteria. You can enter a security group ID or name.
        :type SearchKey: str
        """
        self._Product = None
        self._ProjectId = None
        self._Offset = None
        self._Limit = None
        self._SearchKey = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._ProjectId = params.get("ProjectId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectSecurityGroupsResponse(AbstractModel):
    """DescribeProjectSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _Groups: Security group rules.
        :type Groups: list of SecurityGroup
        :param _Total: Total number of eligible security groups.
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Groups = None
        self._Total = None
        self._RequestId = None

    @property
    def Groups(self):
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeProxySlowLogRequest(AbstractModel):
    """DescribeProxySlowLog request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of a specified instance,  such as  "crs-xjhsdj****" Log in to the [Redis console](https://console.cloud.tencent.com/redis) and copy the instance ID in the instance list.

        :type InstanceId: str
        :param _BeginTime: Start time of slow query
        :type BeginTime: str
        :param _EndTime: End time of slow query
        :type EndTime: str
        :param _MinQueryTime: Slow query threshold  in milliseconds
        :type MinQueryTime: int
        :param _Limit: Number of results per page.  Default value: `20`. Value range: [20,1000].
        :type Limit: int
        :param _Offset: Offset, which is an integral multiple of `Limit`.
        :type Offset: int
        """
        self._InstanceId = None
        self._BeginTime = None
        self._EndTime = None
        self._MinQueryTime = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MinQueryTime(self):
        return self._MinQueryTime

    @MinQueryTime.setter
    def MinQueryTime(self, MinQueryTime):
        self._MinQueryTime = MinQueryTime

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._MinQueryTime = params.get("MinQueryTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxySlowLogResponse(AbstractModel):
    """DescribeProxySlowLog response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of slow queries
        :type TotalCount: int
        :param _InstanceProxySlowLogDetail: Slow query details
        :type InstanceProxySlowLogDetail: list of InstanceProxySlowlogDetail
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceProxySlowLogDetail = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceProxySlowLogDetail(self):
        return self._InstanceProxySlowLogDetail

    @InstanceProxySlowLogDetail.setter
    def InstanceProxySlowLogDetail(self, InstanceProxySlowLogDetail):
        self._InstanceProxySlowLogDetail = InstanceProxySlowLogDetail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceProxySlowLogDetail") is not None:
            self._InstanceProxySlowLogDetail = []
            for item in params.get("InstanceProxySlowLogDetail"):
                obj = InstanceProxySlowlogDetail()
                obj._deserialize(item)
                self._InstanceProxySlowLogDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeReplicationGroupRequest(AbstractModel):
    """DescribeReplicationGroup request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of instances returned per page. Default value: `20`.
        :type Limit: int
        :param _Offset: Pagination offset, which is an integral multiple of `Limit`. `offset` = `limit` * (page number - 1).
        :type Offset: int
        :param _GroupId: ID of the specified replication group, such as `crs-rpl-m3zt****`. Log in to the [TencentDB for Redis console](https://console.cloud.tencent.com/redis/replication), and get it in the global replication group list.
        :type GroupId: str
        :param _SearchKey: Keyword for fuzzy query, which can be a replication group ID or name. Log in to the [TencentDB for Redis console](https://console.cloud.tencent.com/redis/replication), and get them in the global replication group list.
        :type SearchKey: str
        """
        self._Limit = None
        self._Offset = None
        self._GroupId = None
        self._SearchKey = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._GroupId = params.get("GroupId")
        self._SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReplicationGroupResponse(AbstractModel):
    """DescribeReplicationGroup response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of replication groups
        :type TotalCount: int
        :param _Groups: Replication group information
        :type Groups: list of Groups
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Groups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Groups(self):
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = Groups()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSSLStatusRequest(AbstractModel):
    """DescribeSSLStatus request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class DescribeSSLStatusResponse(AbstractModel):
    """DescribeSSLStatus response structure.

    """

    def __init__(self):
        r"""
        :param _CertDownloadUrl: Download address for SSL certificate
        :type CertDownloadUrl: str
        :param _UrlExpiredTime: Expiration time of the certificate download address
        :type UrlExpiredTime: str
        :param _SSLConfig: Whether the SSL is enabled for the identified instance.
- `true`: Enabled
- `false`: Disabled
        :type SSLConfig: bool
        :param _FeatureSupport: Whether SSL is supported for the identified instance.
-`true`: Supported
-`false`: Not supported
        :type FeatureSupport: bool
        :param _Status: Status of SSL configuration
- `1`: Configuring
- `2`: Configured successfully
        :type Status: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CertDownloadUrl = None
        self._UrlExpiredTime = None
        self._SSLConfig = None
        self._FeatureSupport = None
        self._Status = None
        self._RequestId = None

    @property
    def CertDownloadUrl(self):
        return self._CertDownloadUrl

    @CertDownloadUrl.setter
    def CertDownloadUrl(self, CertDownloadUrl):
        self._CertDownloadUrl = CertDownloadUrl

    @property
    def UrlExpiredTime(self):
        return self._UrlExpiredTime

    @UrlExpiredTime.setter
    def UrlExpiredTime(self, UrlExpiredTime):
        self._UrlExpiredTime = UrlExpiredTime

    @property
    def SSLConfig(self):
        return self._SSLConfig

    @SSLConfig.setter
    def SSLConfig(self, SSLConfig):
        self._SSLConfig = SSLConfig

    @property
    def FeatureSupport(self):
        return self._FeatureSupport

    @FeatureSupport.setter
    def FeatureSupport(self, FeatureSupport):
        self._FeatureSupport = FeatureSupport

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertDownloadUrl = params.get("CertDownloadUrl")
        self._UrlExpiredTime = params.get("UrlExpiredTime")
        self._SSLConfig = params.get("SSLConfig")
        self._FeatureSupport = params.get("FeatureSupport")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeSlowLogRequest(AbstractModel):
    """DescribeSlowLog request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of a specified instance,  such as  "crs-xjhsdj****" Log in to the [Redis console](https://console.cloud.tencent.com/redis) and copy the instance ID in the instance list.

        :type InstanceId: str
        :param _BeginTime: Start time for prequerying a slow log
        :type BeginTime: str
        :param _EndTime: End time for prequerying a slow log
        :type EndTime: str
        :param _MinQueryTime: The average execution time threshold of slow query  in microseconds
        :type MinQueryTime: int
        :param _Limit: Number of slow queries displayed per page. Default value: `20`. Value range:  [20,1000].
        :type Limit: int
        :param _Offset: Slow query offset, which is an integral multiple of `Limit`. Calculation formula:  `offset` = `limit` * (page number - 1).
        :type Offset: int
        :param _Role: Node role. <ul><li>`Master`: Master node</li><li>`Slave`: Replica node</li></ul>
        :type Role: str
        """
        self._InstanceId = None
        self._BeginTime = None
        self._EndTime = None
        self._MinQueryTime = None
        self._Limit = None
        self._Offset = None
        self._Role = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MinQueryTime(self):
        return self._MinQueryTime

    @MinQueryTime.setter
    def MinQueryTime(self, MinQueryTime):
        self._MinQueryTime = MinQueryTime

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._MinQueryTime = params.get("MinQueryTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogResponse(AbstractModel):
    """DescribeSlowLog response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of slow queries
        :type TotalCount: int
        :param _InstanceSlowlogDetail: Slow query details
        :type InstanceSlowlogDetail: list of InstanceSlowlogDetail
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceSlowlogDetail = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceSlowlogDetail(self):
        return self._InstanceSlowlogDetail

    @InstanceSlowlogDetail.setter
    def InstanceSlowlogDetail(self, InstanceSlowlogDetail):
        self._InstanceSlowlogDetail = InstanceSlowlogDetail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceSlowlogDetail") is not None:
            self._InstanceSlowlogDetail = []
            for item in params.get("InstanceSlowlogDetail"):
                obj = InstanceSlowlogDetail()
                obj._deserialize(item)
                self._InstanceSlowlogDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTaskInfoRequest(AbstractModel):
    """DescribeTaskInfo request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: int
        """
        self._TaskId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskInfoResponse(AbstractModel):
    """DescribeTaskInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Task status. Valid values: 
- `preparing`: To be run
- `running`: Running
- `succeed`: Succeeded
- `failed`: Failed
- `Error`: Error occurred while running
        :type Status: str
        :param _StartTime: Task start time
        :type StartTime: str
        :param _TaskType: Task type, including `Create`, `Configure`, `Disable Instance`, `Clear Instance`, `Reset Password`, `Upgrade Version`, `Back up Instance`, `Modify Network`, `Migrate to New AZ` and `Promote to Master`.
        :type TaskType: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _TaskMessage: Message returned by task execution, which will be an error message when execution fails or be empty when the status is `running `or `succeed-`.
        :type TaskMessage: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._StartTime = None
        self._TaskType = None
        self._InstanceId = None
        self._TaskMessage = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TaskMessage(self):
        return self._TaskMessage

    @TaskMessage.setter
    def TaskMessage(self, TaskMessage):
        self._TaskMessage = TaskMessage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._TaskType = params.get("TaskType")
        self._InstanceId = params.get("InstanceId")
        self._TaskMessage = params.get("TaskMessage")
        self._RequestId = params.get("RequestId")


class DescribeTaskListRequest(AbstractModel):
    """DescribeTaskList request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of a specified instance,  such as  "crs-xjhsdj****" Log in to the [Redis console](https://console.cloud.tencent.com/redis) and copy the instance ID in the instance list.
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _Limit: Number of taskss returned per page.  Default value: `20`. Maximum value: `100`.
        :type Limit: int
        :param _Offset: Pagination offset, which is an integral multiple of `Limit`. Calculation formula:  `offset` = `limit` * (page number - 1).
        :type Offset: int
        :param _ProjectIds: Project ID Log in to the [Redis console](https://console.cloud.tencent.com/redis#/), go to the account information menu in the top-right corner, and select **Project Management** to query the project ID.
        :type ProjectIds: list of int
        :param _TaskTypes: Task type. Valid values:  - `FLOW_CREATE`: Create an instance. - `FLOW_MODIFYCONNECTIONCONFIG`: Adjust the number of bandwidth connections. - `FLOW_MODIFYINSTANCEPASSWORDFREE`: Modify the process of password-free access. - `FLOW_CLEARNETWORK`: Returning VPC - `FLOW_SETPWD`: Set the access password. - `FLOW_EXPORSHR`: Expand or reduce the capacity. - `FLOW_UpgradeArch`: Upgrade the instance architecture. - `FLOW_MODIFYINSTANCEPARAMS`: Modify the instance parameters. - `FLOW_MODIFYINSTACEREADONLY`: Modify read-only process. - `FLOW_CLOSE`: Disable the instance. - `FLOW_DELETE`: Delete the instance. - `FLOW_OPEN_WAN`: Enable the public network. - `FLOW_FLOW_CLEAN`: Clear the instance. - `FLOW_MODIFYINSTANCEACCOUNT`: Modify the instance account. - `FLOW_ENABLEINSTANCE_REPLICATE`: Enable the replica read-only feature. - `FLOW_DISABLEINSTANCE_REPLICATE`: Disable the replica read-only feature. - `FLOW_SWITCHINSTANCEVIP`: Swap the VIPs of instances. - FLOW_CHANGE_REPLICA_TO_MSTER: Promote the replica node to the mater node. - `FLOW_BACKUPINSTANCE`: Back up an instance.
        :type TaskTypes: list of str
        :param _BeginTime: Start time for executing a task,  in the format of  “2020-10-12 00:00:00”.
        :type BeginTime: str
        :param _EndTime: End time for executing a task,  in the format of  “2021-12-30 20:59:35”.
        :type EndTime: str
        :param _TaskStatus: This parameter is only for internal use and can be ignored.
        :type TaskStatus: list of int
        :param _Result: Task execution status. Valid values: - `0` (initilized) - `1` (executing) - `2` (completed) - `4` (failed)
        :type Result: list of int
        :param _OperatorUin: The field `OperatorUin` has been disused and replaced by `OperateUin`.
        :type OperatorUin: list of int
        :param _OperateUin: Operator account ID or UIN
        :type OperateUin: list of str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Limit = None
        self._Offset = None
        self._ProjectIds = None
        self._TaskTypes = None
        self._BeginTime = None
        self._EndTime = None
        self._TaskStatus = None
        self._Result = None
        self._OperatorUin = None
        self._OperateUin = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def TaskTypes(self):
        return self._TaskTypes

    @TaskTypes.setter
    def TaskTypes(self, TaskTypes):
        self._TaskTypes = TaskTypes

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def OperatorUin(self):
        return self._OperatorUin

    @OperatorUin.setter
    def OperatorUin(self, OperatorUin):
        self._OperatorUin = OperatorUin

    @property
    def OperateUin(self):
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._ProjectIds = params.get("ProjectIds")
        self._TaskTypes = params.get("TaskTypes")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._TaskStatus = params.get("TaskStatus")
        self._Result = params.get("Result")
        self._OperatorUin = params.get("OperatorUin")
        self._OperateUin = params.get("OperateUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskListResponse(AbstractModel):
    """DescribeTaskList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of tasks
        :type TotalCount: int
        :param _Tasks: Task details
        :type Tasks: list of TaskInfoDetail
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = TaskInfoDetail()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTendisSlowLogRequest(AbstractModel):
    """DescribeTendisSlowLog request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID in the format of crs-ngvou0i1
        :type InstanceId: str
        :param _BeginTime: Start time in the format of 2019-09-08 12:12:41
        :type BeginTime: str
        :param _EndTime: End time in the format of 2019-09-09 12:12:41
        :type EndTime: str
        :param _MinQueryTime: Slow query threshold in ms
        :type MinQueryTime: int
        :param _Limit: Maximum number of results returned per page. Default value: 20.
        :type Limit: int
        :param _Offset: Offset, which is an integral multiple of `Limit`.
        :type Offset: int
        """
        self._InstanceId = None
        self._BeginTime = None
        self._EndTime = None
        self._MinQueryTime = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MinQueryTime(self):
        return self._MinQueryTime

    @MinQueryTime.setter
    def MinQueryTime(self, MinQueryTime):
        self._MinQueryTime = MinQueryTime

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._MinQueryTime = params.get("MinQueryTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTendisSlowLogResponse(AbstractModel):
    """DescribeTendisSlowLog response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of slow queries
        :type TotalCount: int
        :param _TendisSlowLogDetail: Slow query details
        :type TendisSlowLogDetail: list of TendisSlowLogDetail
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TendisSlowLogDetail = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TendisSlowLogDetail(self):
        return self._TendisSlowLogDetail

    @TendisSlowLogDetail.setter
    def TendisSlowLogDetail(self, TendisSlowLogDetail):
        self._TendisSlowLogDetail = TendisSlowLogDetail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TendisSlowLogDetail") is not None:
            self._TendisSlowLogDetail = []
            for item in params.get("TendisSlowLogDetail"):
                obj = TendisSlowLogDetail()
                obj._deserialize(item)
                self._TendisSlowLogDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DestroyPostpaidInstanceRequest(AbstractModel):
    """DestroyPostpaidInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class DestroyPostpaidInstanceResponse(AbstractModel):
    """DestroyPostpaidInstance response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DestroyPrepaidInstanceRequest(AbstractModel):
    """DestroyPrepaidInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class DestroyPrepaidInstanceResponse(AbstractModel):
    """DestroyPrepaidInstance response structure.

    """

    def __init__(self):
        r"""
        :param _DealId: Order ID
        :type DealId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealId = None
        self._RequestId = None

    @property
    def DealId(self):
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._RequestId = params.get("RequestId")


class DisableReplicaReadonlyRequest(AbstractModel):
    """DisableReplicaReadonly request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class DisableReplicaReadonlyResponse(AbstractModel):
    """DisableReplicaReadonly response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _Product: Database engine name, which is `redis` for this API.
        :type Product: str
        :param _SecurityGroupId: Security group ID
        :type SecurityGroupId: str
        :param _InstanceIds: List of instance IDs, which is an array of one or more instance IDs.
        :type InstanceIds: list of str
        """
        self._Product = None
        self._SecurityGroupId = None
        self._InstanceIds = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class EnableReplicaReadonlyRequest(AbstractModel):
    """EnableReplicaReadonly request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ReadonlyPolicy: Account routing policy. If `master` or `replication` is entered, it means to route to the master or replica node; if this parameter is left empty, it means to write into the master node and read from the replica node by default.
        :type ReadonlyPolicy: list of str
        """
        self._InstanceId = None
        self._ReadonlyPolicy = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ReadonlyPolicy(self):
        return self._ReadonlyPolicy

    @ReadonlyPolicy.setter
    def ReadonlyPolicy(self, ReadonlyPolicy):
        self._ReadonlyPolicy = ReadonlyPolicy


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ReadonlyPolicy = params.get("ReadonlyPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableReplicaReadonlyResponse(AbstractModel):
    """EnableReplicaReadonly response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Valid values: `ERROR`, `OK`. This field has been disused.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _TaskId: Task ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._TaskId = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class Groups(AbstractModel):
    """Replication group info

    """

    def __init__(self):
        r"""
        :param _AppId: User APPID, which is the unique application ID that matches an account. Some Tencent Cloud products use this APPID.
        :type AppId: int
        :param _RegionId: Region ID. Valid values:
- `1`: Guangzhou 
- `4`: Shanghai 
- `5`: Hong Kong (China) 
- `6`: Toronto 
- `7`: Shanghai Finance 
- `8`: Beijing 
- `9`: Singapore
- `11`: Shenzhen Finance
- `15`: Silicon Valley (West US)
- `16`: Chengdu 
- `17`: Germany 
- `18`: South Korea 
- `19`: Chongqing 
- `21`: India 
- `22`: Virginia (East US)
- `23`: Thailand 
- `25`: Japan
        :type RegionId: int
        :param _GroupId: Replication group ID in the format of "crs-rpl-deind****"
        :type GroupId: str
        :param _GroupName: Replication group name
Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupName: str
        :param _Status: Status of replication group
- `37`: Associating replication group
- `38`: Reconnecting to replication group
- `51`: Disassociating replication group
- `52`: Switching with master instance in replication group
- `53`: Modifying the roles
        :type Status: int
        :param _InstanceCount: Number of replication groups
        :type InstanceCount: int
        :param _Instances: Instance information in replication groups
Note: This field may return null, indicating that no valid values can be obtained.
        :type Instances: list of Instances
        :param _Remark: Remarks
Note: This field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        """
        self._AppId = None
        self._RegionId = None
        self._GroupId = None
        self._GroupName = None
        self._Status = None
        self._InstanceCount = None
        self._Instances = None
        self._Remark = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def Instances(self):
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._RegionId = params.get("RegionId")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._Status = params.get("Status")
        self._InstanceCount = params.get("InstanceCount")
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = Instances()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HotKeyInfo(AbstractModel):
    """Hot key details

    """

    def __init__(self):
        r"""
        :param _Key: Hot key
        :type Key: str
        :param _Type: Type
        :type Type: str
        :param _Count: Count
        :type Count: int
        """
        self._Key = None
        self._Type = None
        self._Count = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Type = params.get("Type")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Inbound(AbstractModel):
    """Security group inbound rule

    """

    def __init__(self):
        r"""
        :param _Action: Policy. Valid values: ACCEPT, DROP.
        :type Action: str
        :param _AddressModule: All the addresses that the address group ID represents.
        :type AddressModule: str
        :param _CidrIp: Source IP or IP address range, such as 192.168.0.0/16.
        :type CidrIp: str
        :param _Desc: Description.
        :type Desc: str
        :param _IpProtocol: Network protocol, such as UDP and TCP.
        :type IpProtocol: str
        :param _PortRange: Port.
        :type PortRange: str
        :param _ServiceModule: All the protocols and ports that the service group ID represents.
        :type ServiceModule: str
        :param _Id: All the addresses that the security group ID represents.
        :type Id: str
        """
        self._Action = None
        self._AddressModule = None
        self._CidrIp = None
        self._Desc = None
        self._IpProtocol = None
        self._PortRange = None
        self._ServiceModule = None
        self._Id = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def AddressModule(self):
        return self._AddressModule

    @AddressModule.setter
    def AddressModule(self, AddressModule):
        self._AddressModule = AddressModule

    @property
    def CidrIp(self):
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def IpProtocol(self):
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def PortRange(self):
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def ServiceModule(self):
        return self._ServiceModule

    @ServiceModule.setter
    def ServiceModule(self, ServiceModule):
        self._ServiceModule = ServiceModule

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._AddressModule = params.get("AddressModule")
        self._CidrIp = params.get("CidrIp")
        self._Desc = params.get("Desc")
        self._IpProtocol = params.get("IpProtocol")
        self._PortRange = params.get("PortRange")
        self._ServiceModule = params.get("ServiceModule")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateInstanceRequest(AbstractModel):
    """InquiryPriceCreateInstance request structure.

    """

    def __init__(self):
        r"""
        :param _TypeId: Instance type. Valid values: `2` (Redis 2.8 memory edition in standard architecture), `3` (CKV 3.2 memory edition in standard architecture), `4` (CKV 3.2 memory edition in cluster architecture), `6` (Redis 4.0 memory edition in standard architecture), `7` (Redis 4.0 memory edition in cluster architecture), `8` (Redis 5.0 memory edition in standard architecture), `9` (Redis 5.0 memory edition in cluster architecture).
        :type TypeId: int
        :param _MemSize: Memory capacity in MB, which must be a multiple of 1,024. It is subject to the purchasable specifications returned by the [DescribeProductInfo API](https://intl.cloud.tencent.com/document/api/239/30600?from_cn_redirect=1).
If `TypeId` indicates the standard architecture, `MemSize` indicates the total memory capacity of an instance; if `TypeId` indicates the cluster architecture, `MemSize` indicates the memory capacity per shard.
        :type MemSize: int
        :param _GoodsNum: Number of instances. The actual quantity purchasable at a time is subject to the specifications returned by the [DescribeProductInfo API](https://intl.cloud.tencent.com/document/api/239/30600?from_cn_redirect=1).
        :type GoodsNum: int
        :param _Period: Length of purchase in months, which is required when creating a monthly-subscribed instance. Value range: [1,2,3,4,5,6,7,8,9,10,11,12,24,36]. For pay-as-you-go instances, set the parameter to `1`.
        :type Period: int
        :param _BillingMode: Billing mode. Valid values: `0` (pay-as-you-go), `1` (monthly subscription).
        :type BillingMode: int
        :param _ZoneId: ID of the AZ where the instance resides. For more information, see [Regions and AZs](https://intl.cloud.tencent.com/document/product/239/4106?from_cn_redirect=1).
        :type ZoneId: int
        :param _RedisShardNum: Instance shard quantity. This field is not required by Redis 2.8 standard architecture, CKV standard architecture, Redis 2.8 standalone edition, and Redis 4.0 standard architecture.
        :type RedisShardNum: int
        :param _RedisReplicasNum: Instance replica quantity. This field is not required by Redis 2.8 standard architecture, CKV standard architecture, and Redis 2.8 standalone edition.
        :type RedisReplicasNum: int
        :param _ReplicasReadonly: Whether to support read-only replicas. This field is not required by Redis 2.8 standard architecture, CKV standard architecture, and Redis 2.8 standalone edition.
        :type ReplicasReadonly: bool
        :param _ZoneName: Name of the AZ where the instance resides. For more information, see [Regions and AZs](https://intl.cloud.tencent.com/document/product/239/4106?from_cn_redirect=1).
        :type ZoneName: str
        :param _ProductVersion: Valid values: `local` (local disk edition), `cloud` (cloud disk edition), `cdc` (dedicated cluster edition). Default value: `local` (local disk edition)
        :type ProductVersion: str
        """
        self._TypeId = None
        self._MemSize = None
        self._GoodsNum = None
        self._Period = None
        self._BillingMode = None
        self._ZoneId = None
        self._RedisShardNum = None
        self._RedisReplicasNum = None
        self._ReplicasReadonly = None
        self._ZoneName = None
        self._ProductVersion = None

    @property
    def TypeId(self):
        return self._TypeId

    @TypeId.setter
    def TypeId(self, TypeId):
        self._TypeId = TypeId

    @property
    def MemSize(self):
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def BillingMode(self):
        return self._BillingMode

    @BillingMode.setter
    def BillingMode(self, BillingMode):
        self._BillingMode = BillingMode

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RedisShardNum(self):
        return self._RedisShardNum

    @RedisShardNum.setter
    def RedisShardNum(self, RedisShardNum):
        self._RedisShardNum = RedisShardNum

    @property
    def RedisReplicasNum(self):
        return self._RedisReplicasNum

    @RedisReplicasNum.setter
    def RedisReplicasNum(self, RedisReplicasNum):
        self._RedisReplicasNum = RedisReplicasNum

    @property
    def ReplicasReadonly(self):
        return self._ReplicasReadonly

    @ReplicasReadonly.setter
    def ReplicasReadonly(self, ReplicasReadonly):
        self._ReplicasReadonly = ReplicasReadonly

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ProductVersion(self):
        return self._ProductVersion

    @ProductVersion.setter
    def ProductVersion(self, ProductVersion):
        self._ProductVersion = ProductVersion


    def _deserialize(self, params):
        self._TypeId = params.get("TypeId")
        self._MemSize = params.get("MemSize")
        self._GoodsNum = params.get("GoodsNum")
        self._Period = params.get("Period")
        self._BillingMode = params.get("BillingMode")
        self._ZoneId = params.get("ZoneId")
        self._RedisShardNum = params.get("RedisShardNum")
        self._RedisReplicasNum = params.get("RedisReplicasNum")
        self._ReplicasReadonly = params.get("ReplicasReadonly")
        self._ZoneName = params.get("ZoneName")
        self._ProductVersion = params.get("ProductVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateInstanceResponse(AbstractModel):
    """InquiryPriceCreateInstance response structure.

    """

    def __init__(self):
        r"""
        :param _Price: Price. Unit: USD (accurate down to the cent)
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Price: float
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Price = params.get("Price")
        self._RequestId = params.get("RequestId")


class InquiryPriceUpgradeInstanceRequest(AbstractModel):
    """InquiryPriceUpgradeInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _MemSize: Shard size in MB.
        :type MemSize: int
        :param _RedisShardNum: Number of shards. This parameter can be left blank for Redis 2.8 in standard architecture, CKV in standard architecture, and Redis 2.8 in standalone architecture.
        :type RedisShardNum: int
        :param _RedisReplicasNum: Number of replicas. This parameter can be left blank for Redis 2.8 in standard architecture, CKV in standard architecture, and Redis 2.8 in standalone architecture.
        :type RedisReplicasNum: int
        """
        self._InstanceId = None
        self._MemSize = None
        self._RedisShardNum = None
        self._RedisReplicasNum = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MemSize(self):
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def RedisShardNum(self):
        return self._RedisShardNum

    @RedisShardNum.setter
    def RedisShardNum(self, RedisShardNum):
        self._RedisShardNum = RedisShardNum

    @property
    def RedisReplicasNum(self):
        return self._RedisReplicasNum

    @RedisReplicasNum.setter
    def RedisReplicasNum(self, RedisReplicasNum):
        self._RedisReplicasNum = RedisReplicasNum


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._MemSize = params.get("MemSize")
        self._RedisShardNum = params.get("RedisShardNum")
        self._RedisReplicasNum = params.get("RedisReplicasNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceUpgradeInstanceResponse(AbstractModel):
    """InquiryPriceUpgradeInstance response structure.

    """

    def __init__(self):
        r"""
        :param _Price: Price. Unit: USD
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Price: float
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Price = params.get("Price")
        self._RequestId = params.get("RequestId")


class InstanceClusterNode(AbstractModel):
    """Instance node type

    """

    def __init__(self):
        r"""
        :param _Name: Node name
        :type Name: str
        :param _RunId: ID of the runtime node of an instance
        :type RunId: str
        :param _Role: Cluster role. Valid values:  - `0` (master) - `1` (replica)
        :type Role: int
        :param _Status: Node status. Valid values:  - `0` (read/write) - `1` (read) - `2` (backup)
        :type Status: int
        :param _Connected: Service status. Valid values: `0` (down), `1` (on).
        :type Connected: int
        :param _CreateTime: Node creation time
        :type CreateTime: str
        :param _DownTime: Node elimination time
        :type DownTime: str
        :param _Slots: Node slot distribution range
        :type Slots: str
        :param _Keys: Distribution of node keys
        :type Keys: int
        :param _Qps: Node QPS Number of executions per second on sharded nodes Unit: Counts/sec
        :type Qps: int
        :param _QpsSlope: QPS slope of a node
        :type QpsSlope: float
        :param _Storage: Node storage
        :type Storage: int
        :param _StorageSlope: Node storage slope
        :type StorageSlope: float
        """
        self._Name = None
        self._RunId = None
        self._Role = None
        self._Status = None
        self._Connected = None
        self._CreateTime = None
        self._DownTime = None
        self._Slots = None
        self._Keys = None
        self._Qps = None
        self._QpsSlope = None
        self._Storage = None
        self._StorageSlope = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RunId(self):
        return self._RunId

    @RunId.setter
    def RunId(self, RunId):
        self._RunId = RunId

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Connected(self):
        return self._Connected

    @Connected.setter
    def Connected(self, Connected):
        self._Connected = Connected

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DownTime(self):
        return self._DownTime

    @DownTime.setter
    def DownTime(self, DownTime):
        self._DownTime = DownTime

    @property
    def Slots(self):
        return self._Slots

    @Slots.setter
    def Slots(self, Slots):
        self._Slots = Slots

    @property
    def Keys(self):
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def Qps(self):
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def QpsSlope(self):
        return self._QpsSlope

    @QpsSlope.setter
    def QpsSlope(self, QpsSlope):
        self._QpsSlope = QpsSlope

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def StorageSlope(self):
        return self._StorageSlope

    @StorageSlope.setter
    def StorageSlope(self, StorageSlope):
        self._StorageSlope = StorageSlope


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._RunId = params.get("RunId")
        self._Role = params.get("Role")
        self._Status = params.get("Status")
        self._Connected = params.get("Connected")
        self._CreateTime = params.get("CreateTime")
        self._DownTime = params.get("DownTime")
        self._Slots = params.get("Slots")
        self._Keys = params.get("Keys")
        self._Qps = params.get("Qps")
        self._QpsSlope = params.get("QpsSlope")
        self._Storage = params.get("Storage")
        self._StorageSlope = params.get("StorageSlope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceClusterShard(AbstractModel):
    """Information list of instance shards

    """

    def __init__(self):
        r"""
        :param _ShardName: The name of a shard node
        :type ShardName: str
        :param _ShardId: The serial number of a shard node
        :type ShardId: str
        :param _Role: The role of a shard node
- `0`: Master node.
- `1`: Replica node.
        :type Role: int
        :param _Keys: Number of keys
        :type Keys: int
        :param _Slots: Slot information
        :type Slots: str
        :param _Storage: Used Capacity
        :type Storage: int
        :param _StorageSlope: Capacity slope
        :type StorageSlope: float
        :param _Runid: Instance runtime node ID
        :type Runid: str
        :param _Connected: Service status
- `0`: Down.
- `1`: On.
        :type Connected: int
        """
        self._ShardName = None
        self._ShardId = None
        self._Role = None
        self._Keys = None
        self._Slots = None
        self._Storage = None
        self._StorageSlope = None
        self._Runid = None
        self._Connected = None

    @property
    def ShardName(self):
        return self._ShardName

    @ShardName.setter
    def ShardName(self, ShardName):
        self._ShardName = ShardName

    @property
    def ShardId(self):
        return self._ShardId

    @ShardId.setter
    def ShardId(self, ShardId):
        self._ShardId = ShardId

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Keys(self):
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def Slots(self):
        return self._Slots

    @Slots.setter
    def Slots(self, Slots):
        self._Slots = Slots

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def StorageSlope(self):
        return self._StorageSlope

    @StorageSlope.setter
    def StorageSlope(self, StorageSlope):
        self._StorageSlope = StorageSlope

    @property
    def Runid(self):
        return self._Runid

    @Runid.setter
    def Runid(self, Runid):
        self._Runid = Runid

    @property
    def Connected(self):
        return self._Connected

    @Connected.setter
    def Connected(self, Connected):
        self._Connected = Connected


    def _deserialize(self, params):
        self._ShardName = params.get("ShardName")
        self._ShardId = params.get("ShardId")
        self._Role = params.get("Role")
        self._Keys = params.get("Keys")
        self._Slots = params.get("Slots")
        self._Storage = params.get("Storage")
        self._StorageSlope = params.get("StorageSlope")
        self._Runid = params.get("Runid")
        self._Connected = params.get("Connected")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceEnumParam(AbstractModel):
    """Description of the instance parameter in Enum type

    """

    def __init__(self):
        r"""
        :param _ParamName: Parameter name
        :type ParamName: str
        :param _ValueType: Parameter type, such as `Enum`.
        :type ValueType: str
        :param _NeedRestart: Whether to restart the database after modifying the parameters. Valid values: - `true` (required) - `false` (not required)
        :type NeedRestart: str
        :param _DefaultValue: Default value of the parameter
        :type DefaultValue: str
        :param _CurrentValue: Current value
        :type CurrentValue: str
        :param _Tips: Description
        :type Tips: str
        :param _EnumValue: Acceptable values for the parameter
        :type EnumValue: list of str
        :param _Status: Parameter modification status. Valid values: - `1` (modifying) - `2` (modified)
        :type Status: int
        """
        self._ParamName = None
        self._ValueType = None
        self._NeedRestart = None
        self._DefaultValue = None
        self._CurrentValue = None
        self._Tips = None
        self._EnumValue = None
        self._Status = None

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ValueType(self):
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def NeedRestart(self):
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def DefaultValue(self):
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Tips(self):
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def EnumValue(self):
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._ValueType = params.get("ValueType")
        self._NeedRestart = params.get("NeedRestart")
        self._DefaultValue = params.get("DefaultValue")
        self._CurrentValue = params.get("CurrentValue")
        self._Tips = params.get("Tips")
        self._EnumValue = params.get("EnumValue")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceIntegerParam(AbstractModel):
    """Description of the instance parameter in Integer type

    """

    def __init__(self):
        r"""
        :param _ParamName: Parameter name
        :type ParamName: str
        :param _ValueType: Parameter type: Integer
        :type ValueType: str
        :param _NeedRestart: Whether restart is required after a modification is made. Valid values: true, false
        :type NeedRestart: str
        :param _DefaultValue: Default value of the parameter
        :type DefaultValue: str
        :param _CurrentValue: Current value
        :type CurrentValue: str
        :param _Tips: Parameter description
        :type Tips: str
        :param _Min: Minimum value of the parameter
        :type Min: str
        :param _Max: Maximum value of the parameter
        :type Max: str
        :param _Status: Parameter status. 1: modifying; 2: modified
        :type Status: int
        :param _Unit: Parameter unit
Note: This field may return null, indicating that no valid values can be obtained.
        :type Unit: str
        """
        self._ParamName = None
        self._ValueType = None
        self._NeedRestart = None
        self._DefaultValue = None
        self._CurrentValue = None
        self._Tips = None
        self._Min = None
        self._Max = None
        self._Status = None
        self._Unit = None

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ValueType(self):
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def NeedRestart(self):
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def DefaultValue(self):
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Tips(self):
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def Min(self):
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._ValueType = params.get("ValueType")
        self._NeedRestart = params.get("NeedRestart")
        self._DefaultValue = params.get("DefaultValue")
        self._CurrentValue = params.get("CurrentValue")
        self._Tips = params.get("Tips")
        self._Min = params.get("Min")
        self._Max = params.get("Max")
        self._Status = params.get("Status")
        self._Unit = params.get("Unit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceMultiParam(AbstractModel):
    """Description of the instance parameter in Multi type

    """

    def __init__(self):
        r"""
        :param _ParamName: Parameter name
        :type ParamName: str
        :param _ValueType: Parameter Type such as  `MULTI`
        :type ValueType: str
        :param _NeedRestart: Whether to restart the database after modifying the parameter. Valid values:  - `true` (required) - `false` (not required)
        :type NeedRestart: str
        :param _DefaultValue: Default value of the parameter
        :type DefaultValue: str
        :param _CurrentValue: Current value
        :type CurrentValue: str
        :param _Tips: Description
        :type Tips: str
        :param _EnumValue: Description
        :type EnumValue: list of str
        :param _Status: Parameter modification status. Valid values: - `1` (modifying) - `2` (modified)
        :type Status: int
        """
        self._ParamName = None
        self._ValueType = None
        self._NeedRestart = None
        self._DefaultValue = None
        self._CurrentValue = None
        self._Tips = None
        self._EnumValue = None
        self._Status = None

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ValueType(self):
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def NeedRestart(self):
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def DefaultValue(self):
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Tips(self):
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def EnumValue(self):
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._ValueType = params.get("ValueType")
        self._NeedRestart = params.get("NeedRestart")
        self._DefaultValue = params.get("DefaultValue")
        self._CurrentValue = params.get("CurrentValue")
        self._Tips = params.get("Tips")
        self._EnumValue = params.get("EnumValue")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNode(AbstractModel):
    """Instance node

    """

    def __init__(self):
        r"""
        :param _Id: Instance ID
        :type Id: int
        :param _InstanceClusterNode: Node details
        :type InstanceClusterNode: list of InstanceClusterNode
        """
        self._Id = None
        self._InstanceClusterNode = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def InstanceClusterNode(self):
        return self._InstanceClusterNode

    @InstanceClusterNode.setter
    def InstanceClusterNode(self, InstanceClusterNode):
        self._InstanceClusterNode = InstanceClusterNode


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("InstanceClusterNode") is not None:
            self._InstanceClusterNode = []
            for item in params.get("InstanceClusterNode"):
                obj = InstanceClusterNode()
                obj._deserialize(item)
                self._InstanceClusterNode.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceParam(AbstractModel):
    """Instance parameter

    """

    def __init__(self):
        r"""
        :param _Key: Parameter name, such as “timeout”. For supported custom parameters, see <a href="https://www.tencentcloud.com/document/product/239/39796">Setting Instance Parameters</a>
        :type Key: str
        :param _Value: Current parameter value. For example, if you set the current value of “timeout” to 120 (in seconds), the client connections that remain idle longer than 120 seconds will be closed. For more information on parameter values, see <a href="https://www.tencentcloud.com/document/product/239/39796">Setting Instance Parameters</a>
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
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
        


class InstanceParamHistory(AbstractModel):
    """History of instance parameter modifications

    """

    def __init__(self):
        r"""
        :param _ParamName: Parameter name
        :type ParamName: str
        :param _PreValue: The value of the parameter before modification
        :type PreValue: str
        :param _NewValue: The value of the parameter after modification
        :type NewValue: str
        :param _Status: Parameter configuration status
- `1`: The parameter configuration is being modified.
- `2`: The parameter configuration has been modified successfully.
- `3`: Failed to modify the parameter configuration.
        :type Status: int
        :param _ModifyTime: Modification time
        :type ModifyTime: str
        """
        self._ParamName = None
        self._PreValue = None
        self._NewValue = None
        self._Status = None
        self._ModifyTime = None

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def PreValue(self):
        return self._PreValue

    @PreValue.setter
    def PreValue(self, PreValue):
        self._PreValue = PreValue

    @property
    def NewValue(self):
        return self._NewValue

    @NewValue.setter
    def NewValue(self, NewValue):
        self._NewValue = NewValue

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._PreValue = params.get("PreValue")
        self._NewValue = params.get("NewValue")
        self._Status = params.get("Status")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceProxySlowlogDetail(AbstractModel):
    """Proxy slow query details

    """

    def __init__(self):
        r"""
        :param _Duration: Slow query duration in milliseconds
        :type Duration: int
        :param _Client: Client address
        :type Client: str
        :param _Command: Slow query command
        :type Command: str
        :param _CommandLine: Detailed command line information of slow query
        :type CommandLine: str
        :param _ExecuteTime: Execution time
        :type ExecuteTime: str
        """
        self._Duration = None
        self._Client = None
        self._Command = None
        self._CommandLine = None
        self._ExecuteTime = None

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Client(self):
        return self._Client

    @Client.setter
    def Client(self, Client):
        self._Client = Client

    @property
    def Command(self):
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def CommandLine(self):
        return self._CommandLine

    @CommandLine.setter
    def CommandLine(self, CommandLine):
        self._CommandLine = CommandLine

    @property
    def ExecuteTime(self):
        return self._ExecuteTime

    @ExecuteTime.setter
    def ExecuteTime(self, ExecuteTime):
        self._ExecuteTime = ExecuteTime


    def _deserialize(self, params):
        self._Duration = params.get("Duration")
        self._Client = params.get("Client")
        self._Command = params.get("Command")
        self._CommandLine = params.get("CommandLine")
        self._ExecuteTime = params.get("ExecuteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceSecurityGroupDetail(AbstractModel):
    """Security group information of the instance

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _SecurityGroupDetails: Security group information, which includes  security group ID, name, outbound and inbound rules.
        :type SecurityGroupDetails: list of SecurityGroupDetail
        """
        self._InstanceId = None
        self._SecurityGroupDetails = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SecurityGroupDetails(self):
        return self._SecurityGroupDetails

    @SecurityGroupDetails.setter
    def SecurityGroupDetails(self, SecurityGroupDetails):
        self._SecurityGroupDetails = SecurityGroupDetails


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("SecurityGroupDetails") is not None:
            self._SecurityGroupDetails = []
            for item in params.get("SecurityGroupDetails"):
                obj = SecurityGroupDetail()
                obj._deserialize(item)
                self._SecurityGroupDetails.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceSet(AbstractModel):
    """List of instance details

    """

    def __init__(self):
        r"""
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Appid: User APPID, which is the unique application ID that matches an account. Some Tencent Cloud products use this APPID.

        :type Appid: int
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _RegionId: Region ID. <ul><li>`1`: Guangzhou. </li><li>`4`: Shanghai. </li><li>`5`: Hong Kong (China). </li><li>`6`: Toronto. </li> <li>`7`: Shanghai Finance. </li> <li>`8`: Beijing. </li> <li>`9`: Singapore. </li> <li>`11`: Shenzhen Finance. </li> <li>`15`: West US (Silicon Valley). </li><li>`16`: Chengdu. </li><li>`17`: Frankfurt. </li><li>`18`: Seoul. </li><li>`19`: Chongqing. </li><li>`21`: Mumbai. </li><li>`22`: East US (Virginia). </li><li>`23`: Bangkok. </li><li>`24`: Moscow. </li><li>`25`: Tokyo. </li></ul>
        :type RegionId: int
        :param _ZoneId: Region ID
        :type ZoneId: int
        :param _VpcId: VPC ID, such as `75101`.
        :type VpcId: int
        :param _SubnetId: Subnet ID, such as `46315`.
        :type SubnetId: int
        :param _Status: Current instance status. <ul><li>`0`: To be initialized. </li><li>`1`: In the process. </li><li>`2`: Running. </li><li>`-2`: Isolated. </li><li>`-3`: To be deleted. </li></ul>
        :type Status: int
        :param _WanIp: Instance VIP
        :type WanIp: str
        :param _Port: Port number of an instance
        :type Port: int
        :param _Createtime: Instance creation time in the format of "2020-01-15 10:20:00"
        :type Createtime: str
        :param _Size: Instance memory capacity in MB (1 MB = 1024 KB)
        :type Size: float
        :param _SizeUsed: This field has been disused. You can use the TCOP’s [GetMonitorData](https://intl.cloud.tencent.com/document/product/248/31014?from_cn_redirect=1) API to query the capacity used by the instance.
        :type SizeUsed: float
        :param _Type: Instance type
- `2`: Redis 2.8 Memory Edition (Standard Architecture).
- `3`: CKV 3.2 Memory Edition (Standard Architecture).
- `4`: CKV 3.2 Memory Edition (Cluster Architecture).
- `5`: Redis 2.8 Memory Edition (Standalone).
- `6`: Redis 4.0 Memory Edition (Standard Architecture).
- `7`: Redis 4.0 Memory Edition (Cluster Architecture).
- `8`: Redis 5.0 Memory Edition (Standard Architecture).
- `9`: Redis 5.0 Memory Edition (Cluster Architecture).
- `15`: Redis 6.2 Memory Edition (Standard Architecture).
- `16`: Redis 6.2 Memory Edition (Cluster Architecture).
        :type Type: int
        :param _AutoRenewFlag: Whether to set the auto-renewal flag for an instance. <ul><li>`1`: Auto-renewal set. </li><li>`0`: Auto-renewal not set.</li></ul>
        :type AutoRenewFlag: int
        :param _DeadlineTime: The time when a monthly subscribed instance expires
        :type DeadlineTime: str
        :param _Engine: Engine: Redis community edition, Tencent Cloud CKV
        :type Engine: str
        :param _ProductType: Product type. <ul><li>`standalone`: Standard edition. </li><li>`cluster`: Cluster edition. </li></ul>
        :type ProductType: str
        :param _UniqVpcId: VPC ID, such as vpc-fk33jsf43kgv.
        :type UniqVpcId: str
        :param _UniqSubnetId: VPC subnet ID, such as subnet-fd3j6l35mm0.
        :type UniqSubnetId: str
        :param _BillingMode: Billing mode. Only pay-as-you-go billing is supported.
        :type BillingMode: int
        :param _InstanceTitle: Description of an instance status, such as "Running".
        :type InstanceTitle: str
        :param _OfflineTime: The default termination time for isolated instances in the format of "2020-02-15 10:20:00". By default, a pay-as-you-go instance will be terminated after two hours of isolation, and a monthly subscribed instance will be terminated after seven days by default.
        :type OfflineTime: str
        :param _SubStatus: Sub-status returned for an instance in process
        :type SubStatus: int
        :param _Tags: Anti-affinity tag
        :type Tags: list of str
        :param _InstanceNode: Instance node information
        :type InstanceNode: list of InstanceNode
        :param _RedisShardSize: Shard size
        :type RedisShardSize: int
        :param _RedisShardNum: Number of shards
        :type RedisShardNum: int
        :param _RedisReplicasNum: Number of replicas
        :type RedisReplicasNum: int
        :param _PriceId: Billing ID
        :type PriceId: int
        :param _CloseTime: The time when an instance start to be isolated
        :type CloseTime: str
        :param _SlaveReadWeight: Read weight of a replica node
        :type SlaveReadWeight: int
        :param _InstanceTags: Instance tag information
Note: This field may return null, indicating that no valid value can be obtained.
        :type InstanceTags: list of InstanceTagInfo
        :param _ProjectName: Project name
Note: This field may return null, indicating that no valid value can be obtained.
        :type ProjectName: str
        :param _NoAuth: Whether an instance is password-free. <ul><li>`true`: Yes. </li><li>`false`: No. </li></ul>
Note: This field may return null, indicating that no valid value can be obtained.
        :type NoAuth: bool
        :param _ClientLimit: Number of client connections
Note: This field may return null, indicating that no valid value can be obtained.
        :type ClientLimit: int
        :param _DtsStatus: DTS status (internal parameter, which can be ignored)
Note: This field may return null, indicating that no valid value can be obtained.
        :type DtsStatus: int
        :param _NetLimit: Upper shard bandwidth limit in MB
Note: This field may return null, indicating that no valid value can be obtained.
        :type NetLimit: int
        :param _PasswordFree: Password-free instance flag (internal parameter, which can be ignored)
Note: This field may return null, indicating that no valid value can be obtained.
        :type PasswordFree: int
        :param _Vip6: Internal parameter, which can be ignored.
Note: This field may return null, indicating that no valid value can be obtained.
        :type Vip6: str
        :param _ReadOnly: Read-only instance flag (internal parameter, which can be ignored)
Note: This field may return null, indicating that no valid value can be obtained.
        :type ReadOnly: int
        :param _RemainBandwidthDuration: Internal parameter, which can be ignored.
Note: This field may return null, indicating that no valid value can be obtained.
        :type RemainBandwidthDuration: str
        :param _DiskSize: This parameter can be ignored for Redis instance.
Note: This field may return null, indicating that no valid value can be obtained.
        :type DiskSize: int
        :param _MonitorVersion: Monitoring granularity. <ul><li>`1m`: Monitoring at one-minute granularity. This granularity has been disused. For more information, see [1-Minute Granularity Will Be Disused](https://www.tencentcloud.com/document/product/239/50440).</li><li>`5s`: Monitoring at five-second granularity.</li></ul>
Note: This field may return null, indicating that no valid values can be obtained.
        :type MonitorVersion: str
        :param _ClientLimitMin: The minimum number of max client connections
Note: This field may return null, indicating that no valid value can be obtained.
        :type ClientLimitMin: int
        :param _ClientLimitMax: The maximum number of max client connections
Note: This field may return null, indicating that no valid value can be obtained.
        :type ClientLimitMax: int
        :param _NodeSet: Instance node details
Note: This field may return null, indicating that no valid value can be obtained.
        :type NodeSet: list of RedisNodeInfo
        :param _Region: Information of the region where the instance is deployed, such as `ap-guangzhou`.
Note: This field may return null, indicating that no valid value can be obtained.
        :type Region: str
        :param _WanAddress: Public IP
Note: This field may return null, indicating that no valid value can be obtained.
        :type WanAddress: str
        :param _PolarisServer: Polaris service address, which is for internal use.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PolarisServer: str
        :param _CurrentProxyVersion: The current proxy version of an instance
Note: This field may return null, indicating that no valid value can be obtained.
        :type CurrentProxyVersion: str
        :param _CurrentRedisVersion: The current cache minor version of an instance
Note: This field may return null, indicating that no valid value can be obtained.
        :type CurrentRedisVersion: str
        :param _UpgradeProxyVersion: Proxy version, which can be upgraded for the instance
Note: This field may return null, indicating that no valid value can be obtained.
        :type UpgradeProxyVersion: str
        :param _UpgradeRedisVersion: Cache minor version, which can be upgraded for the instance
Note: This field may return null, indicating that no valid value can be obtained.
        :type UpgradeRedisVersion: str
        """
        self._InstanceName = None
        self._InstanceId = None
        self._Appid = None
        self._ProjectId = None
        self._RegionId = None
        self._ZoneId = None
        self._VpcId = None
        self._SubnetId = None
        self._Status = None
        self._WanIp = None
        self._Port = None
        self._Createtime = None
        self._Size = None
        self._SizeUsed = None
        self._Type = None
        self._AutoRenewFlag = None
        self._DeadlineTime = None
        self._Engine = None
        self._ProductType = None
        self._UniqVpcId = None
        self._UniqSubnetId = None
        self._BillingMode = None
        self._InstanceTitle = None
        self._OfflineTime = None
        self._SubStatus = None
        self._Tags = None
        self._InstanceNode = None
        self._RedisShardSize = None
        self._RedisShardNum = None
        self._RedisReplicasNum = None
        self._PriceId = None
        self._CloseTime = None
        self._SlaveReadWeight = None
        self._InstanceTags = None
        self._ProjectName = None
        self._NoAuth = None
        self._ClientLimit = None
        self._DtsStatus = None
        self._NetLimit = None
        self._PasswordFree = None
        self._Vip6 = None
        self._ReadOnly = None
        self._RemainBandwidthDuration = None
        self._DiskSize = None
        self._MonitorVersion = None
        self._ClientLimitMin = None
        self._ClientLimitMax = None
        self._NodeSet = None
        self._Region = None
        self._WanAddress = None
        self._PolarisServer = None
        self._CurrentProxyVersion = None
        self._CurrentRedisVersion = None
        self._UpgradeProxyVersion = None
        self._UpgradeRedisVersion = None

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Appid(self):
        return self._Appid

    @Appid.setter
    def Appid(self, Appid):
        self._Appid = Appid

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def WanIp(self):
        return self._WanIp

    @WanIp.setter
    def WanIp(self, WanIp):
        self._WanIp = WanIp

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Createtime(self):
        return self._Createtime

    @Createtime.setter
    def Createtime(self, Createtime):
        self._Createtime = Createtime

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def SizeUsed(self):
        return self._SizeUsed

    @SizeUsed.setter
    def SizeUsed(self, SizeUsed):
        self._SizeUsed = SizeUsed

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def DeadlineTime(self):
        return self._DeadlineTime

    @DeadlineTime.setter
    def DeadlineTime(self, DeadlineTime):
        self._DeadlineTime = DeadlineTime

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def ProductType(self):
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def BillingMode(self):
        return self._BillingMode

    @BillingMode.setter
    def BillingMode(self, BillingMode):
        self._BillingMode = BillingMode

    @property
    def InstanceTitle(self):
        return self._InstanceTitle

    @InstanceTitle.setter
    def InstanceTitle(self, InstanceTitle):
        self._InstanceTitle = InstanceTitle

    @property
    def OfflineTime(self):
        return self._OfflineTime

    @OfflineTime.setter
    def OfflineTime(self, OfflineTime):
        self._OfflineTime = OfflineTime

    @property
    def SubStatus(self):
        return self._SubStatus

    @SubStatus.setter
    def SubStatus(self, SubStatus):
        self._SubStatus = SubStatus

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceNode(self):
        return self._InstanceNode

    @InstanceNode.setter
    def InstanceNode(self, InstanceNode):
        self._InstanceNode = InstanceNode

    @property
    def RedisShardSize(self):
        return self._RedisShardSize

    @RedisShardSize.setter
    def RedisShardSize(self, RedisShardSize):
        self._RedisShardSize = RedisShardSize

    @property
    def RedisShardNum(self):
        return self._RedisShardNum

    @RedisShardNum.setter
    def RedisShardNum(self, RedisShardNum):
        self._RedisShardNum = RedisShardNum

    @property
    def RedisReplicasNum(self):
        return self._RedisReplicasNum

    @RedisReplicasNum.setter
    def RedisReplicasNum(self, RedisReplicasNum):
        self._RedisReplicasNum = RedisReplicasNum

    @property
    def PriceId(self):
        return self._PriceId

    @PriceId.setter
    def PriceId(self, PriceId):
        self._PriceId = PriceId

    @property
    def CloseTime(self):
        return self._CloseTime

    @CloseTime.setter
    def CloseTime(self, CloseTime):
        self._CloseTime = CloseTime

    @property
    def SlaveReadWeight(self):
        return self._SlaveReadWeight

    @SlaveReadWeight.setter
    def SlaveReadWeight(self, SlaveReadWeight):
        self._SlaveReadWeight = SlaveReadWeight

    @property
    def InstanceTags(self):
        return self._InstanceTags

    @InstanceTags.setter
    def InstanceTags(self, InstanceTags):
        self._InstanceTags = InstanceTags

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def NoAuth(self):
        return self._NoAuth

    @NoAuth.setter
    def NoAuth(self, NoAuth):
        self._NoAuth = NoAuth

    @property
    def ClientLimit(self):
        return self._ClientLimit

    @ClientLimit.setter
    def ClientLimit(self, ClientLimit):
        self._ClientLimit = ClientLimit

    @property
    def DtsStatus(self):
        return self._DtsStatus

    @DtsStatus.setter
    def DtsStatus(self, DtsStatus):
        self._DtsStatus = DtsStatus

    @property
    def NetLimit(self):
        return self._NetLimit

    @NetLimit.setter
    def NetLimit(self, NetLimit):
        self._NetLimit = NetLimit

    @property
    def PasswordFree(self):
        return self._PasswordFree

    @PasswordFree.setter
    def PasswordFree(self, PasswordFree):
        self._PasswordFree = PasswordFree

    @property
    def Vip6(self):
        return self._Vip6

    @Vip6.setter
    def Vip6(self, Vip6):
        self._Vip6 = Vip6

    @property
    def ReadOnly(self):
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly

    @property
    def RemainBandwidthDuration(self):
        return self._RemainBandwidthDuration

    @RemainBandwidthDuration.setter
    def RemainBandwidthDuration(self, RemainBandwidthDuration):
        self._RemainBandwidthDuration = RemainBandwidthDuration

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def MonitorVersion(self):
        return self._MonitorVersion

    @MonitorVersion.setter
    def MonitorVersion(self, MonitorVersion):
        self._MonitorVersion = MonitorVersion

    @property
    def ClientLimitMin(self):
        return self._ClientLimitMin

    @ClientLimitMin.setter
    def ClientLimitMin(self, ClientLimitMin):
        self._ClientLimitMin = ClientLimitMin

    @property
    def ClientLimitMax(self):
        return self._ClientLimitMax

    @ClientLimitMax.setter
    def ClientLimitMax(self, ClientLimitMax):
        self._ClientLimitMax = ClientLimitMax

    @property
    def NodeSet(self):
        return self._NodeSet

    @NodeSet.setter
    def NodeSet(self, NodeSet):
        self._NodeSet = NodeSet

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def WanAddress(self):
        return self._WanAddress

    @WanAddress.setter
    def WanAddress(self, WanAddress):
        self._WanAddress = WanAddress

    @property
    def PolarisServer(self):
        return self._PolarisServer

    @PolarisServer.setter
    def PolarisServer(self, PolarisServer):
        self._PolarisServer = PolarisServer

    @property
    def CurrentProxyVersion(self):
        return self._CurrentProxyVersion

    @CurrentProxyVersion.setter
    def CurrentProxyVersion(self, CurrentProxyVersion):
        self._CurrentProxyVersion = CurrentProxyVersion

    @property
    def CurrentRedisVersion(self):
        return self._CurrentRedisVersion

    @CurrentRedisVersion.setter
    def CurrentRedisVersion(self, CurrentRedisVersion):
        self._CurrentRedisVersion = CurrentRedisVersion

    @property
    def UpgradeProxyVersion(self):
        return self._UpgradeProxyVersion

    @UpgradeProxyVersion.setter
    def UpgradeProxyVersion(self, UpgradeProxyVersion):
        self._UpgradeProxyVersion = UpgradeProxyVersion

    @property
    def UpgradeRedisVersion(self):
        return self._UpgradeRedisVersion

    @UpgradeRedisVersion.setter
    def UpgradeRedisVersion(self, UpgradeRedisVersion):
        self._UpgradeRedisVersion = UpgradeRedisVersion


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._InstanceId = params.get("InstanceId")
        self._Appid = params.get("Appid")
        self._ProjectId = params.get("ProjectId")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Status = params.get("Status")
        self._WanIp = params.get("WanIp")
        self._Port = params.get("Port")
        self._Createtime = params.get("Createtime")
        self._Size = params.get("Size")
        self._SizeUsed = params.get("SizeUsed")
        self._Type = params.get("Type")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._DeadlineTime = params.get("DeadlineTime")
        self._Engine = params.get("Engine")
        self._ProductType = params.get("ProductType")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._BillingMode = params.get("BillingMode")
        self._InstanceTitle = params.get("InstanceTitle")
        self._OfflineTime = params.get("OfflineTime")
        self._SubStatus = params.get("SubStatus")
        self._Tags = params.get("Tags")
        if params.get("InstanceNode") is not None:
            self._InstanceNode = []
            for item in params.get("InstanceNode"):
                obj = InstanceNode()
                obj._deserialize(item)
                self._InstanceNode.append(obj)
        self._RedisShardSize = params.get("RedisShardSize")
        self._RedisShardNum = params.get("RedisShardNum")
        self._RedisReplicasNum = params.get("RedisReplicasNum")
        self._PriceId = params.get("PriceId")
        self._CloseTime = params.get("CloseTime")
        self._SlaveReadWeight = params.get("SlaveReadWeight")
        if params.get("InstanceTags") is not None:
            self._InstanceTags = []
            for item in params.get("InstanceTags"):
                obj = InstanceTagInfo()
                obj._deserialize(item)
                self._InstanceTags.append(obj)
        self._ProjectName = params.get("ProjectName")
        self._NoAuth = params.get("NoAuth")
        self._ClientLimit = params.get("ClientLimit")
        self._DtsStatus = params.get("DtsStatus")
        self._NetLimit = params.get("NetLimit")
        self._PasswordFree = params.get("PasswordFree")
        self._Vip6 = params.get("Vip6")
        self._ReadOnly = params.get("ReadOnly")
        self._RemainBandwidthDuration = params.get("RemainBandwidthDuration")
        self._DiskSize = params.get("DiskSize")
        self._MonitorVersion = params.get("MonitorVersion")
        self._ClientLimitMin = params.get("ClientLimitMin")
        self._ClientLimitMax = params.get("ClientLimitMax")
        if params.get("NodeSet") is not None:
            self._NodeSet = []
            for item in params.get("NodeSet"):
                obj = RedisNodeInfo()
                obj._deserialize(item)
                self._NodeSet.append(obj)
        self._Region = params.get("Region")
        self._WanAddress = params.get("WanAddress")
        self._PolarisServer = params.get("PolarisServer")
        self._CurrentProxyVersion = params.get("CurrentProxyVersion")
        self._CurrentRedisVersion = params.get("CurrentRedisVersion")
        self._UpgradeProxyVersion = params.get("UpgradeProxyVersion")
        self._UpgradeRedisVersion = params.get("UpgradeRedisVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceSlowlogDetail(AbstractModel):
    """Slow log details

    """

    def __init__(self):
        r"""
        :param _Duration: Slow log duration
        :type Duration: int
        :param _Client: Client address
        :type Client: str
        :param _Command: Command
        :type Command: str
        :param _CommandLine: Command line details
        :type CommandLine: str
        :param _ExecuteTime: Execution duration
        :type ExecuteTime: str
        :param _Node: Node ID
        :type Node: str
        """
        self._Duration = None
        self._Client = None
        self._Command = None
        self._CommandLine = None
        self._ExecuteTime = None
        self._Node = None

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Client(self):
        return self._Client

    @Client.setter
    def Client(self, Client):
        self._Client = Client

    @property
    def Command(self):
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def CommandLine(self):
        return self._CommandLine

    @CommandLine.setter
    def CommandLine(self, CommandLine):
        self._CommandLine = CommandLine

    @property
    def ExecuteTime(self):
        return self._ExecuteTime

    @ExecuteTime.setter
    def ExecuteTime(self, ExecuteTime):
        self._ExecuteTime = ExecuteTime

    @property
    def Node(self):
        return self._Node

    @Node.setter
    def Node(self, Node):
        self._Node = Node


    def _deserialize(self, params):
        self._Duration = params.get("Duration")
        self._Client = params.get("Client")
        self._Command = params.get("Command")
        self._CommandLine = params.get("CommandLine")
        self._ExecuteTime = params.get("ExecuteTime")
        self._Node = params.get("Node")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTagInfo(AbstractModel):
    """Instance tag information

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
        :type TagKey: str
        :param _TagValue: Tag value
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
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
        


class InstanceTextParam(AbstractModel):
    """Description of instance parameter in Char type

    """

    def __init__(self):
        r"""
        :param _ParamName: Parameter name
        :type ParamName: str
        :param _ValueType: Parameter type such as  `Text`.
        :type ValueType: str
        :param _NeedRestart: Whether to restart the database after modifying the parameter. Valid values:  - `true` (required) - `false` (not required)
        :type NeedRestart: str
        :param _DefaultValue: Default value of the parameter
        :type DefaultValue: str
        :param _CurrentValue: Current value
        :type CurrentValue: str
        :param _Tips: Description
        :type Tips: str
        :param _TextValue: Acceptable values of the parameter
        :type TextValue: list of str
        :param _Status: Parameter modification status. Valid values: - `1` (modifying) - `2` (modified)
        :type Status: int
        """
        self._ParamName = None
        self._ValueType = None
        self._NeedRestart = None
        self._DefaultValue = None
        self._CurrentValue = None
        self._Tips = None
        self._TextValue = None
        self._Status = None

    @property
    def ParamName(self):
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ValueType(self):
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def NeedRestart(self):
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def DefaultValue(self):
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Tips(self):
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def TextValue(self):
        return self._TextValue

    @TextValue.setter
    def TextValue(self, TextValue):
        self._TextValue = TextValue

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._ValueType = params.get("ValueType")
        self._NeedRestart = params.get("NeedRestart")
        self._DefaultValue = params.get("DefaultValue")
        self._CurrentValue = params.get("CurrentValue")
        self._Tips = params.get("Tips")
        self._TextValue = params.get("TextValue")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Instances(AbstractModel):
    """Instances in replication group

    """

    def __init__(self):
        r"""
        :param _AppId: User APPID, which is the unique application ID that matches an account. Some Tencent Cloud products use this APPID.
        :type AppId: int
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _RegionId: Region ID. <ul><li>`1`: Guangzhou. </li><li>`4`: Shanghai. </li><li>`5`: Hong Kong (China). </li> <li>`6`: Toronto. </li> <li>`7`: Shanghai Finance. </li> <li>`8`: Beijing. </li> <li>`9`: Singapore. </li> <li>`11`: Shenzhen Finance. </li> <li>`15`: West US (Silicon Valley). </li> </ul>
        :type RegionId: int
        :param _ZoneId: Region ID
        :type ZoneId: int
        :param _RedisReplicasNum: Number of replicas
        :type RedisReplicasNum: int
        :param _RedisShardNum: Number of shards
        :type RedisShardNum: int
        :param _RedisShardSize: Shard memory size.
        :type RedisShardSize: int
        :param _DiskSize: Instance disk size
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskSize: int
        :param _Engine: Engine: Redis Community Edition, Tencent Cloud CKV.
        :type Engine: str
        :param _Role: Read-write permission of the instance. <ul><li>`rw`: Read/Write. </li><li>`r`: Read-only. </li></ul>
        :type Role: str
        :param _Vip: Instance VIP
        :type Vip: str
        :param _Vip6: Internal parameter, which can be ignored.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Vip6: str
        :param _VpcID: VPC ID, such as `75101`.
        :type VpcID: int
        :param _VPort: Instance port
        :type VPort: int
        :param _Status: Instance status. <ul><li>`0`: Uninitialized. </li><li>`1`: In the process. </li><li>`2`: Running. </li><li>`-2`: Isolated. </li><li>`-3`: To be deleted. </li></ul>
        :type Status: int
        :param _GrocerySysId: Repository ID
        :type GrocerySysId: int
        :param _ProductType: Instance type
- `2`: Redis 2.8 Memory Edition (Standard Architecture).
- `3`: CKV 3.2 Memory Edition (Standard Architecture).
- `4`: CKV 3.2 Memory Edition (Cluster Architecture)
- `5`: Redis 2.8 Memory Edition (Standalone)
- `6`: Redis 4.0 Memory Edition (Standard Architecture).
- `7`: Redis 4.0 Memory Edition (Cluster Architecture)
- `8`: Redis 5.0 Memory Edition (Standard Architecture).
- `9`: Redis 5.0 Memory Edition (Cluster Architecture)
- `15`: Redis 6.2 Memory Edition (Standard Architecture).
- `16`: Redis 6.2 Memory Edition (Cluster Architecture)
        :type ProductType: int
        :param _CreateTime: The time when the instance was added to the replication group.
        :type CreateTime: str
        :param _UpdateTime: The time when instances in the replication group were updated.
        :type UpdateTime: str
        """
        self._AppId = None
        self._InstanceId = None
        self._InstanceName = None
        self._RegionId = None
        self._ZoneId = None
        self._RedisReplicasNum = None
        self._RedisShardNum = None
        self._RedisShardSize = None
        self._DiskSize = None
        self._Engine = None
        self._Role = None
        self._Vip = None
        self._Vip6 = None
        self._VpcID = None
        self._VPort = None
        self._Status = None
        self._GrocerySysId = None
        self._ProductType = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RedisReplicasNum(self):
        return self._RedisReplicasNum

    @RedisReplicasNum.setter
    def RedisReplicasNum(self, RedisReplicasNum):
        self._RedisReplicasNum = RedisReplicasNum

    @property
    def RedisShardNum(self):
        return self._RedisShardNum

    @RedisShardNum.setter
    def RedisShardNum(self, RedisShardNum):
        self._RedisShardNum = RedisShardNum

    @property
    def RedisShardSize(self):
        return self._RedisShardSize

    @RedisShardSize.setter
    def RedisShardSize(self, RedisShardSize):
        self._RedisShardSize = RedisShardSize

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vip6(self):
        return self._Vip6

    @Vip6.setter
    def Vip6(self, Vip6):
        self._Vip6 = Vip6

    @property
    def VpcID(self):
        return self._VpcID

    @VpcID.setter
    def VpcID(self, VpcID):
        self._VpcID = VpcID

    @property
    def VPort(self):
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def GrocerySysId(self):
        return self._GrocerySysId

    @GrocerySysId.setter
    def GrocerySysId(self, GrocerySysId):
        self._GrocerySysId = GrocerySysId

    @property
    def ProductType(self):
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._RedisReplicasNum = params.get("RedisReplicasNum")
        self._RedisShardNum = params.get("RedisShardNum")
        self._RedisShardSize = params.get("RedisShardSize")
        self._DiskSize = params.get("DiskSize")
        self._Engine = params.get("Engine")
        self._Role = params.get("Role")
        self._Vip = params.get("Vip")
        self._Vip6 = params.get("Vip6")
        self._VpcID = params.get("VpcID")
        self._VPort = params.get("VPort")
        self._Status = params.get("Status")
        self._GrocerySysId = params.get("GrocerySysId")
        self._ProductType = params.get("ProductType")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KillMasterGroupRequest(AbstractModel):
    """KillMasterGroup request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of a specified instance,  such as  "crs-xjhsdj****" Log in to the [Redis console](https://console.cloud.tencent.com/redis) and copy the instance ID in the instance list.
        :type InstanceId: str
        :param _Password: A parameter used to configure the access password for a specified instance. If password-free authentication is enabled, this parameter will not be required. Required password strength. - It must contains 8-30 characters. We recommend that you use a password of more than 12 characters. - It must contain at least two of the following types: lowercase letters, uppercase letters, digits, and symbols (()`~!@#$%^&*-+=_|{}[]:;<>,.?/), and it cannot start with a slash (/).
        :type Password: str
        :param _ShardIds: Shard ID of a sharded cluster
        :type ShardIds: list of int
        """
        self._InstanceId = None
        self._Password = None
        self._ShardIds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ShardIds(self):
        return self._ShardIds

    @ShardIds.setter
    def ShardIds(self, ShardIds):
        self._ShardIds = ShardIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Password = params.get("Password")
        self._ShardIds = params.get("ShardIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KillMasterGroupResponse(AbstractModel):
    """KillMasterGroup response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Async task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ManualBackupInstanceRequest(AbstractModel):
    """ManualBackupInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of a specified instance,  such as  "crs-xjhsdj****" Log in to the [Redis console](https://console.cloud.tencent.com/redis) and copy the instance ID in the instance list.
        :type InstanceId: str
        :param _Remark: Remarks for manual backup task
        :type Remark: str
        :param _StorageDays: Retention period of backup data in days.  Default value: 7 days.  Value range: [0,1825].  If the value exceeds 7 days, [submit a ticket](https://console.cloud.tencent.com/workorder/category) for application. - If this parameter is not configured, it will set to be the same as the period of automatic backup retention. - If automatic backup is not set, the default value will be 7 days.
        :type StorageDays: int
        """
        self._InstanceId = None
        self._Remark = None
        self._StorageDays = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def StorageDays(self):
        return self._StorageDays

    @StorageDays.setter
    def StorageDays(self, StorageDays):
        self._StorageDays = StorageDays


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Remark = params.get("Remark")
        self._StorageDays = params.get("StorageDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManualBackupInstanceResponse(AbstractModel):
    """ManualBackupInstance response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModfiyInstancePasswordRequest(AbstractModel):
    """ModfiyInstancePassword request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, such as "crs-xjhsdj****". Log in to the [Redis console](https://console.cloud.tencent.com/redis) and copy the instance ID in the instance list.
        :type InstanceId: str
        :param _OldPassword: Old password of an instance
        :type OldPassword: str
        :param _Password: New instance password, which has the following requirements:
- It must contain 8-30 characters, preferably 12 or more.
- It cannot start with a slash (/)
- It must contain two of the following three types: lowercase letters, uppercase letters, and symbols (()~!@#$%^&*-+=_|{}[]:;<>,.?/)
        :type Password: str
        """
        self._InstanceId = None
        self._OldPassword = None
        self._Password = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OldPassword(self):
        return self._OldPassword

    @OldPassword.setter
    def OldPassword(self, OldPassword):
        self._OldPassword = OldPassword

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._OldPassword = params.get("OldPassword")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModfiyInstancePasswordResponse(AbstractModel):
    """ModfiyInstancePassword response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyAutoBackupConfigRequest(AbstractModel):
    """ModifyAutoBackupConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of a specified instance,  such as  "crs-xjhsdj****" Log in to the [Redis console](https://console.cloud.tencent.com/redis) and copy the instance ID in the instance list.

        :type InstanceId: str
        :param _WeekDays: Automatic backup cycle. Valid values: `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, `Sunday`. This parameter currently cannot be modified.
        :type WeekDays: list of str
        :param _TimePeriod: Automatic backup time in the format of 00:00-01:00, 01:00-02:00... 23:00-00:00.
        :type TimePeriod: str
        :param _AutoBackupType: Automatic backup type.  Valid value:  `1` (scheduled backup).
        :type AutoBackupType: int
        """
        self._InstanceId = None
        self._WeekDays = None
        self._TimePeriod = None
        self._AutoBackupType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def WeekDays(self):
        return self._WeekDays

    @WeekDays.setter
    def WeekDays(self, WeekDays):
        self._WeekDays = WeekDays

    @property
    def TimePeriod(self):
        return self._TimePeriod

    @TimePeriod.setter
    def TimePeriod(self, TimePeriod):
        self._TimePeriod = TimePeriod

    @property
    def AutoBackupType(self):
        return self._AutoBackupType

    @AutoBackupType.setter
    def AutoBackupType(self, AutoBackupType):
        self._AutoBackupType = AutoBackupType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._WeekDays = params.get("WeekDays")
        self._TimePeriod = params.get("TimePeriod")
        self._AutoBackupType = params.get("AutoBackupType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoBackupConfigResponse(AbstractModel):
    """ModifyAutoBackupConfig response structure.

    """

    def __init__(self):
        r"""
        :param _AutoBackupType: Automatic backup type.  Valid value:  `1` (scheduled backup).
        :type AutoBackupType: int
        :param _WeekDays: Automatic backup cycle. Valid values: `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, `Sunday`.
        :type WeekDays: list of str
        :param _TimePeriod: Time period for automatic scheduled backup  in the format of  “00:00-01:00, 01:00-02:00...... 23:00-00:00”.
        :type TimePeriod: str
        :param _BackupStorageDays: Retention time of full backup files in days
        :type BackupStorageDays: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AutoBackupType = None
        self._WeekDays = None
        self._TimePeriod = None
        self._BackupStorageDays = None
        self._RequestId = None

    @property
    def AutoBackupType(self):
        return self._AutoBackupType

    @AutoBackupType.setter
    def AutoBackupType(self, AutoBackupType):
        self._AutoBackupType = AutoBackupType

    @property
    def WeekDays(self):
        return self._WeekDays

    @WeekDays.setter
    def WeekDays(self, WeekDays):
        self._WeekDays = WeekDays

    @property
    def TimePeriod(self):
        return self._TimePeriod

    @TimePeriod.setter
    def TimePeriod(self, TimePeriod):
        self._TimePeriod = TimePeriod

    @property
    def BackupStorageDays(self):
        return self._BackupStorageDays

    @BackupStorageDays.setter
    def BackupStorageDays(self, BackupStorageDays):
        self._BackupStorageDays = BackupStorageDays

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AutoBackupType = params.get("AutoBackupType")
        self._WeekDays = params.get("WeekDays")
        self._TimePeriod = params.get("TimePeriod")
        self._BackupStorageDays = params.get("BackupStorageDays")
        self._RequestId = params.get("RequestId")


class ModifyBackupDownloadRestrictionRequest(AbstractModel):
    """ModifyBackupDownloadRestriction request structure.

    """

    def __init__(self):
        r"""
        :param _LimitType: Type of the network restrictions for downloading backup files. Valid values:

- `NoLimit`: Backup files can be downloaded over both public and private networks.
- `LimitOnlyIntranet`: Backup files can be downloaded only at private network addresses auto-assigned by Tencent Cloud.
- `Customize`: Backup files can be downloaded only in the customized VPC.
        :type LimitType: str
        :param _VpcComparisonSymbol: Only `In` can be passed in for this parameter, indicating that backup files can be downloaded in the custom `LimitVpc`.
        :type VpcComparisonSymbol: str
        :param _IpComparisonSymbol: Whether backups can be downloaded at the custom `LimitIp` address.

- `In`: Download is allowed for the custom IP.
- `NotIn`: Download is not allowed for the custom IP.
        :type IpComparisonSymbol: str
        :param _LimitVpc: VPC ID of the custom backup file download address, which is required if `LimitType` is `Customize`.
        :type LimitVpc: list of BackupLimitVpcItem
        :param _LimitIp: VPC IP of the custom backup file download address, which is required if `LimitType` is `Customize`.

        :type LimitIp: list of str
        """
        self._LimitType = None
        self._VpcComparisonSymbol = None
        self._IpComparisonSymbol = None
        self._LimitVpc = None
        self._LimitIp = None

    @property
    def LimitType(self):
        return self._LimitType

    @LimitType.setter
    def LimitType(self, LimitType):
        self._LimitType = LimitType

    @property
    def VpcComparisonSymbol(self):
        return self._VpcComparisonSymbol

    @VpcComparisonSymbol.setter
    def VpcComparisonSymbol(self, VpcComparisonSymbol):
        self._VpcComparisonSymbol = VpcComparisonSymbol

    @property
    def IpComparisonSymbol(self):
        return self._IpComparisonSymbol

    @IpComparisonSymbol.setter
    def IpComparisonSymbol(self, IpComparisonSymbol):
        self._IpComparisonSymbol = IpComparisonSymbol

    @property
    def LimitVpc(self):
        return self._LimitVpc

    @LimitVpc.setter
    def LimitVpc(self, LimitVpc):
        self._LimitVpc = LimitVpc

    @property
    def LimitIp(self):
        return self._LimitIp

    @LimitIp.setter
    def LimitIp(self, LimitIp):
        self._LimitIp = LimitIp


    def _deserialize(self, params):
        self._LimitType = params.get("LimitType")
        self._VpcComparisonSymbol = params.get("VpcComparisonSymbol")
        self._IpComparisonSymbol = params.get("IpComparisonSymbol")
        if params.get("LimitVpc") is not None:
            self._LimitVpc = []
            for item in params.get("LimitVpc"):
                obj = BackupLimitVpcItem()
                obj._deserialize(item)
                self._LimitVpc.append(obj)
        self._LimitIp = params.get("LimitIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupDownloadRestrictionResponse(AbstractModel):
    """ModifyBackupDownloadRestriction response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param _Product: Database engine name, which is `redis` for this API.
        :type Product: str
        :param _SecurityGroupIds: List of IDs of security groups to be modified, which is an array of one or more security group IDs.
        :type SecurityGroupIds: list of str
        :param _InstanceId: Instance ID in the format of cdb-c1nl9rpv or cdbro-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB console.
        :type InstanceId: str
        """
        self._Product = None
        self._SecurityGroupIds = None
        self._InstanceId = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSecurityGroupsResponse(AbstractModel):
    """ModifyDBInstanceSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyInstanceAccountRequest(AbstractModel):
    """ModifyInstanceAccount request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _AccountName: Sub-account name. If the root account is to be modified, enter `root`.
        :type AccountName: str
        :param _AccountPassword: Sub-account password
        :type AccountPassword: str
        :param _Remark: Sub-account description information
        :type Remark: str
        :param _ReadonlyPolicy: Routing policy. Valid values: master (master node); replication (replica node)
        :type ReadonlyPolicy: list of str
        :param _Privilege: Sub-account read/write policy. Valid values: r (read-only); w (write-only); rw (read/write).
        :type Privilege: str
        :param _NoAuth: true: make the root account password-free. This is applicable to root accounts only. Sub-accounts cannot be made password-free.
        :type NoAuth: bool
        """
        self._InstanceId = None
        self._AccountName = None
        self._AccountPassword = None
        self._Remark = None
        self._ReadonlyPolicy = None
        self._Privilege = None
        self._NoAuth = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def AccountPassword(self):
        return self._AccountPassword

    @AccountPassword.setter
    def AccountPassword(self, AccountPassword):
        self._AccountPassword = AccountPassword

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ReadonlyPolicy(self):
        return self._ReadonlyPolicy

    @ReadonlyPolicy.setter
    def ReadonlyPolicy(self, ReadonlyPolicy):
        self._ReadonlyPolicy = ReadonlyPolicy

    @property
    def Privilege(self):
        return self._Privilege

    @Privilege.setter
    def Privilege(self, Privilege):
        self._Privilege = Privilege

    @property
    def NoAuth(self):
        return self._NoAuth

    @NoAuth.setter
    def NoAuth(self, NoAuth):
        self._NoAuth = NoAuth


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AccountName = params.get("AccountName")
        self._AccountPassword = params.get("AccountPassword")
        self._Remark = params.get("Remark")
        self._ReadonlyPolicy = params.get("ReadonlyPolicy")
        self._Privilege = params.get("Privilege")
        self._NoAuth = params.get("NoAuth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceAccountResponse(AbstractModel):
    """ModifyInstanceAccount response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceParamsRequest(AbstractModel):
    """ModifyInstanceParams request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceParams: List of instance parameters modified
        :type InstanceParams: list of InstanceParam
        """
        self._InstanceId = None
        self._InstanceParams = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceParams(self):
        return self._InstanceParams

    @InstanceParams.setter
    def InstanceParams(self, InstanceParams):
        self._InstanceParams = InstanceParams


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("InstanceParams") is not None:
            self._InstanceParams = []
            for item in params.get("InstanceParams"):
                obj = InstanceParam()
                obj._deserialize(item)
                self._InstanceParams.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceParamsResponse(AbstractModel):
    """ModifyInstanceParams response structure.

    """

    def __init__(self):
        r"""
        :param _Changed: Whether the parameter is modified successfully. <br><li>`True`: Yes<br><li>`False`: No<br>
        :type Changed: bool
        :param _TaskId: ID of the task
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Changed = None
        self._TaskId = None
        self._RequestId = None

    @property
    def Changed(self):
        return self._Changed

    @Changed.setter
    def Changed(self, Changed):
        self._Changed = Changed

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Changed = params.get("Changed")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceReadOnlyRequest(AbstractModel):
    """ModifyInstanceReadOnly request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InputMode: Instance input mode. Valid values: `0` (read/write), `1` (read-only)
        :type InputMode: str
        """
        self._InstanceId = None
        self._InputMode = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InputMode(self):
        return self._InputMode

    @InputMode.setter
    def InputMode(self, InputMode):
        self._InputMode = InputMode


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InputMode = params.get("InputMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceReadOnlyResponse(AbstractModel):
    """ModifyInstanceReadOnly response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceRequest(AbstractModel):
    """ModifyInstance request structure.

    """

    def __init__(self):
        r"""
        :param _Operation: Instance modification type. rename: rename an instance; modifyProject: modify the project of an instance; modifyAutoRenew: modify the auto-renewal flag of an instance.
        :type Operation: str
        :param _InstanceIds: Instance ID
        :type InstanceIds: list of str
        :param _InstanceNames: New name of the instance
        :type InstanceNames: list of str
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _AutoRenews: Auto-renewal flag. 0: default status (manual renewal); 1: auto-renewal enabled; 2: auto-renewal disabled
        :type AutoRenews: list of int
        :param _InstanceId: Disused
        :type InstanceId: str
        :param _InstanceName: Disused
        :type InstanceName: str
        :param _AutoRenew: Disused
        :type AutoRenew: int
        """
        self._Operation = None
        self._InstanceIds = None
        self._InstanceNames = None
        self._ProjectId = None
        self._AutoRenews = None
        self._InstanceId = None
        self._InstanceName = None
        self._AutoRenew = None

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceNames(self):
        return self._InstanceNames

    @InstanceNames.setter
    def InstanceNames(self, InstanceNames):
        self._InstanceNames = InstanceNames

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AutoRenews(self):
        return self._AutoRenews

    @AutoRenews.setter
    def AutoRenews(self, AutoRenews):
        self._AutoRenews = AutoRenews

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AutoRenew(self):
        return self._AutoRenew

    @AutoRenew.setter
    def AutoRenew(self, AutoRenew):
        self._AutoRenew = AutoRenew


    def _deserialize(self, params):
        self._Operation = params.get("Operation")
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceNames = params.get("InstanceNames")
        self._ProjectId = params.get("ProjectId")
        self._AutoRenews = params.get("AutoRenews")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._AutoRenew = params.get("AutoRenew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceResponse(AbstractModel):
    """ModifyInstance response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyMaintenanceWindowRequest(AbstractModel):
    """ModifyMaintenanceWindow request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _StartTime: Maintenance start time, such as 17:00
        :type StartTime: str
        :param _EndTime: Maintenance end time, such as 19:00
        :type EndTime: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMaintenanceWindowResponse(AbstractModel):
    """ModifyMaintenanceWindow response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Modification status. Valid values: success, failed.
        :type Status: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ModifyNetworkConfigRequest(AbstractModel):
    """ModifyNetworkConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Operation: Network change type. Valid values:
- `changeVip`: VPC change, including the private IPv4 address and port.
- `changeVpc`: Subnet change.
- `changeBaseToVpc`: Change from classic network to VPC.
- `changeVPort`: Port change.
        :type Operation: str
        :param _Vip: Private IPv4 address of the instance, which is required if `Operation` is `changeVip`.
        :type Vip: str
        :param _VpcId: VPC ID after the change, which is required if `Operation` is `changeVpc` or `changeBaseToVpc`.
        :type VpcId: str
        :param _SubnetId: Subnet ID after the change, which is required if `Operation` is `changeVpc` or `changeBaseToVpc`.
        :type SubnetId: str
        :param _Recycle: Retention period of the original private IPv4 address
- Unit: Days.
- Valid values: `0`, `1`, `2`, `3`, `7`, `15`.

**Note**: You can set the retention period of the original address only in the latest SDK. In earlier SDKs, the original address is released immediately. To view the SDK version, go to [SDK Center](https://intl.cloud.tencent.com/document/sdk?from_cn_redirect=1).
        :type Recycle: int
        :param _VPort: Network port after the change, which is required if `Operation` is `changeVPort` or `changeVip`. Value range: [1024,65535].
        :type VPort: int
        """
        self._InstanceId = None
        self._Operation = None
        self._Vip = None
        self._VpcId = None
        self._SubnetId = None
        self._Recycle = None
        self._VPort = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Recycle(self):
        return self._Recycle

    @Recycle.setter
    def Recycle(self, Recycle):
        self._Recycle = Recycle

    @property
    def VPort(self):
        return self._VPort

    @VPort.setter
    def VPort(self, VPort):
        self._VPort = VPort


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Operation = params.get("Operation")
        self._Vip = params.get("Vip")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Recycle = params.get("Recycle")
        self._VPort = params.get("VPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNetworkConfigResponse(AbstractModel):
    """ModifyNetworkConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Execution status. Ignore this parameter.
        :type Status: bool
        :param _SubnetId: New subnet ID of the instance
        :type SubnetId: str
        :param _VpcId: New VPC ID of the instance
        :type VpcId: str
        :param _Vip: New private IPv4 address of the instance
        :type Vip: str
        :param _TaskId: Task ID, which can be used to query the task execution status through the `DescribeTaskInfo` API.
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._SubnetId = None
        self._VpcId = None
        self._Vip = None
        self._TaskId = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._SubnetId = params.get("SubnetId")
        self._VpcId = params.get("VpcId")
        self._Vip = params.get("Vip")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyParamTemplateRequest(AbstractModel):
    """ModifyParamTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: ID of the source parameter template.
        :type TemplateId: str
        :param _Name: New name after the parameter template is modified.
        :type Name: str
        :param _Description: New description after the parameter template is modified.
        :type Description: str
        :param _ParamList: New parameter list after the parameter template is modified.
        :type ParamList: list of InstanceParam
        """
        self._TemplateId = None
        self._Name = None
        self._Description = None
        self._ParamList = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ParamList(self):
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = InstanceParam()
                obj._deserialize(item)
                self._ParamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyParamTemplateResponse(AbstractModel):
    """ModifyParamTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class OpenSSLRequest(AbstractModel):
    """OpenSSL request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class OpenSSLResponse(AbstractModel):
    """OpenSSL response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class Outbound(AbstractModel):
    """Security group outbound rule

    """

    def __init__(self):
        r"""
        :param _Action: Policy. Valid values: ACCEPT, DROP.
        :type Action: str
        :param _AddressModule: All the addresses that the address group ID represents.
        :type AddressModule: str
        :param _CidrIp: Source IP or IP address range, such as 192.168.0.0/16.
        :type CidrIp: str
        :param _Desc: Description.
        :type Desc: str
        :param _IpProtocol: Network protocol, such as UDP and TCP.
        :type IpProtocol: str
        :param _PortRange: Port.
        :type PortRange: str
        :param _ServiceModule: All the protocols and ports that the service group ID represents.
        :type ServiceModule: str
        :param _Id: All the addresses that the security group ID represents.
        :type Id: str
        """
        self._Action = None
        self._AddressModule = None
        self._CidrIp = None
        self._Desc = None
        self._IpProtocol = None
        self._PortRange = None
        self._ServiceModule = None
        self._Id = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def AddressModule(self):
        return self._AddressModule

    @AddressModule.setter
    def AddressModule(self, AddressModule):
        self._AddressModule = AddressModule

    @property
    def CidrIp(self):
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def IpProtocol(self):
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def PortRange(self):
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def ServiceModule(self):
        return self._ServiceModule

    @ServiceModule.setter
    def ServiceModule(self, ServiceModule):
        self._ServiceModule = ServiceModule

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._AddressModule = params.get("AddressModule")
        self._CidrIp = params.get("CidrIp")
        self._Desc = params.get("Desc")
        self._IpProtocol = params.get("IpProtocol")
        self._PortRange = params.get("PortRange")
        self._ServiceModule = params.get("ServiceModule")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamTemplateInfo(AbstractModel):
    """Parameter template information

    """

    def __init__(self):
        r"""
        :param _TemplateId: Parameter template ID
        :type TemplateId: str
        :param _Name: Parameter template name
        :type Name: str
        :param _Description: Parameter template description
        :type Description: str
        :param _ProductType: Instance type
- `2`: Redis 2.8 Memory Edition (Standard Architecture).
- `3`: CKV 3.2 Memory Edition (Standard Architecture).
- `4`: CKV 3.2 Memory Edition (Cluster Architecture).
- `5`: Redis 2.8 Memory Edition (Standalone).
- `6`: Redis 4.0 Memory Edition (Standard Architecture).
- `7`: Redis 4.0 Memory Edition (Cluster Architecture).
- `8`: Redis 5.0 Memory Edition (Standard Architecture).
- `9`: Redis 5.0 Memory Edition (Cluster Architecture).
- `15`: Redis 6.2 Memory Edition (Standard Architecture).
- `16`: Redis 6.2 Memory Edition (Cluster Architecture).
        :type ProductType: int
        """
        self._TemplateId = None
        self._Name = None
        self._Description = None
        self._ProductType = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ProductType(self):
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._ProductType = params.get("ProductType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParameterDetail(AbstractModel):
    """Details of the parameters in the parameter template

    """

    def __init__(self):
        r"""
        :param _Name: Parameter name
        :type Name: str
        :param _ParamType: Parameter Type
        :type ParamType: str
        :param _Default: Default value of the parameter
        :type Default: str
        :param _Description: Parameter description
        :type Description: str
        :param _CurrentValue: Current value of the parameter
        :type CurrentValue: str
        :param _NeedReboot: Whether to restart the database for the modified parameters to take effect
- `0`: No restart.
- `1`: Restart required.
        :type NeedReboot: int
        :param _Max: Maximum value of the parameter
Note: This field may return null, indicating that no valid values can be obtained.
        :type Max: str
        :param _Min: Minimum value of the parameter
Note: This field may return null, indicating that no valid values can be obtained.
        :type Min: str
        :param _EnumValue: Enumerated values of the parameter. It is null if the parameter is non-enumerated
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnumValue: list of str
        """
        self._Name = None
        self._ParamType = None
        self._Default = None
        self._Description = None
        self._CurrentValue = None
        self._NeedReboot = None
        self._Max = None
        self._Min = None
        self._EnumValue = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ParamType(self):
        return self._ParamType

    @ParamType.setter
    def ParamType(self, ParamType):
        self._ParamType = ParamType

    @property
    def Default(self):
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CurrentValue(self):
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def NeedReboot(self):
        return self._NeedReboot

    @NeedReboot.setter
    def NeedReboot(self, NeedReboot):
        self._NeedReboot = NeedReboot

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Min(self):
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def EnumValue(self):
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ParamType = params.get("ParamType")
        self._Default = params.get("Default")
        self._Description = params.get("Description")
        self._CurrentValue = params.get("CurrentValue")
        self._NeedReboot = params.get("NeedReboot")
        self._Max = params.get("Max")
        self._Min = params.get("Min")
        self._EnumValue = params.get("EnumValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductConf(AbstractModel):
    """Product information

    """

    def __init__(self):
        r"""
        :param _Type: Product type
- `2`: Redis 2.8 Memory Edition (Standard Architecture).
- `3`: CKV 3.2 Memory Edition (Standard Architecture).
- `4`: CKV 3.2 Memory Edition (Cluster Architecture).
- `5`: Redis 2.8 Memory Edition (Standalone).
- `6`: Redis 4.0 Memory Edition (Standard Architecture).
- `7`: Redis 4.0 Memory Edition (Cluster Architecture).
- `8`: Redis 5.0 Memory Edition (Standard Architecture).
- `9`: Redis 5.0 Memory Edition (Cluster Architecture).
- `15`: Redis 6.2 Memory Edition (Standard Architecture).
- `16`: Redis 6.2 Memory Edition (Cluster Architecture).
        :type Type: int
        :param _TypeName: Product names, including Redis Master-Replica Edition, Redis Standalone Edition, Redis 4.0 Cluster Edition, CKV Master-Replica Edition, and CKV Standalone Edition.
        :type TypeName: str
        :param _MinBuyNum: Minimum purchasable quantity
        :type MinBuyNum: int
        :param _MaxBuyNum: Maximum purchasable quantity
        :type MaxBuyNum: int
        :param _Saleout: Whether a product is sold out
- `true`: Sold out.
- `false`: Not sold out.
        :type Saleout: bool
        :param _Engine: Product engines, including Tencent Cloud CKV and Redis Community Edition.
        :type Engine: str
        :param _Version: Compatible versions, including Redis 2.8, 3.2, 4.0, 5.0, and 6.2.
        :type Version: str
        :param _TotalSize: Total capacity in GB
        :type TotalSize: list of str
        :param _ShardSize: Shard size in GB
        :type ShardSize: list of str
        :param _ReplicaNum: Quantity of replicas
        :type ReplicaNum: list of str
        :param _ShardNum: Quantity of shards
        :type ShardNum: list of str
        :param _PayMode: Supported billing modes
- `1`: Monthly subscription.
- `0`: Pay-as-you-go.
        :type PayMode: str
        :param _EnableRepicaReadOnly: Whether to support read-only replicas
- `true`: Supported.
-`false`: Not supported.
        :type EnableRepicaReadOnly: bool
        """
        self._Type = None
        self._TypeName = None
        self._MinBuyNum = None
        self._MaxBuyNum = None
        self._Saleout = None
        self._Engine = None
        self._Version = None
        self._TotalSize = None
        self._ShardSize = None
        self._ReplicaNum = None
        self._ShardNum = None
        self._PayMode = None
        self._EnableRepicaReadOnly = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TypeName(self):
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def MinBuyNum(self):
        return self._MinBuyNum

    @MinBuyNum.setter
    def MinBuyNum(self, MinBuyNum):
        self._MinBuyNum = MinBuyNum

    @property
    def MaxBuyNum(self):
        return self._MaxBuyNum

    @MaxBuyNum.setter
    def MaxBuyNum(self, MaxBuyNum):
        self._MaxBuyNum = MaxBuyNum

    @property
    def Saleout(self):
        return self._Saleout

    @Saleout.setter
    def Saleout(self, Saleout):
        self._Saleout = Saleout

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def TotalSize(self):
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize

    @property
    def ShardSize(self):
        return self._ShardSize

    @ShardSize.setter
    def ShardSize(self, ShardSize):
        self._ShardSize = ShardSize

    @property
    def ReplicaNum(self):
        return self._ReplicaNum

    @ReplicaNum.setter
    def ReplicaNum(self, ReplicaNum):
        self._ReplicaNum = ReplicaNum

    @property
    def ShardNum(self):
        return self._ShardNum

    @ShardNum.setter
    def ShardNum(self, ShardNum):
        self._ShardNum = ShardNum

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def EnableRepicaReadOnly(self):
        return self._EnableRepicaReadOnly

    @EnableRepicaReadOnly.setter
    def EnableRepicaReadOnly(self, EnableRepicaReadOnly):
        self._EnableRepicaReadOnly = EnableRepicaReadOnly


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._TypeName = params.get("TypeName")
        self._MinBuyNum = params.get("MinBuyNum")
        self._MaxBuyNum = params.get("MaxBuyNum")
        self._Saleout = params.get("Saleout")
        self._Engine = params.get("Engine")
        self._Version = params.get("Version")
        self._TotalSize = params.get("TotalSize")
        self._ShardSize = params.get("ShardSize")
        self._ReplicaNum = params.get("ReplicaNum")
        self._ShardNum = params.get("ShardNum")
        self._PayMode = params.get("PayMode")
        self._EnableRepicaReadOnly = params.get("EnableRepicaReadOnly")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyNodes(AbstractModel):
    """Proxy node information

    """

    def __init__(self):
        r"""
        :param _NodeId: Node ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type NodeId: str
        :param _ZoneId: AZ ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneId: int
        """
        self._NodeId = None
        self._ZoneId = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisBackupSet(AbstractModel):
    """Array of instance backups

    """

    def __init__(self):
        r"""
        :param _StartTime: Backup start time
        :type StartTime: str
        :param _BackupId: Backup task ID
        :type BackupId: str
        :param _BackupType: Backup type. Valid values:  `1` (Automatic backup in the early morning initiated by the system.) `0`: Manual backup initiated by the user.
        :type BackupType: str
        :param _Status: Backup status. Valid values:  - `1`: The backup is locked by another process. - `2`: The backup is normal and not locked by any process. - `-1`: The backup is expired. - `3`: The backup is being exported. - `4`: Exported the backup successfully.
        :type Status: int
        :param _Remark: Backup remarks
        :type Remark: str
        :param _Locked: Whether the backup is locked. Valid values:  - `0` (no) - `1` (yes)
        :type Locked: int
        :param _BackupSize: Internal field, which can be ignored.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupSize: int
        :param _FullBackup: Internal field, which can be ignored.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FullBackup: int
        :param _InstanceType: Internal field, which can be ignored.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceType: int
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _Region: The region where the local backup resides.
        :type Region: str
        :param _EndTime: Backup end time
        :type EndTime: str
        :param _FileType: Backup file type
        :type FileType: str
        :param _ExpireTime: Backup file expiration time
        :type ExpireTime: str
        """
        self._StartTime = None
        self._BackupId = None
        self._BackupType = None
        self._Status = None
        self._Remark = None
        self._Locked = None
        self._BackupSize = None
        self._FullBackup = None
        self._InstanceType = None
        self._InstanceId = None
        self._InstanceName = None
        self._Region = None
        self._EndTime = None
        self._FileType = None
        self._ExpireTime = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def BackupType(self):
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Locked(self):
        return self._Locked

    @Locked.setter
    def Locked(self, Locked):
        self._Locked = Locked

    @property
    def BackupSize(self):
        return self._BackupSize

    @BackupSize.setter
    def BackupSize(self, BackupSize):
        self._BackupSize = BackupSize

    @property
    def FullBackup(self):
        return self._FullBackup

    @FullBackup.setter
    def FullBackup(self, FullBackup):
        self._FullBackup = FullBackup

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._BackupId = params.get("BackupId")
        self._BackupType = params.get("BackupType")
        self._Status = params.get("Status")
        self._Remark = params.get("Remark")
        self._Locked = params.get("Locked")
        self._BackupSize = params.get("BackupSize")
        self._FullBackup = params.get("FullBackup")
        self._InstanceType = params.get("InstanceType")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Region = params.get("Region")
        self._EndTime = params.get("EndTime")
        self._FileType = params.get("FileType")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisCommonInstanceList(AbstractModel):
    """Instance information

    """

    def __init__(self):
        r"""
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _AppId: User APPID, which is the unique application ID that matches an account. Some Tencent Cloud products use this APPID.
        :type AppId: int
        :param _ProjectId: Project ID of the instance
        :type ProjectId: int
        :param _Region: Instance region
        :type Region: str
        :param _Zone: Instance AZ
        :type Zone: str
        :param _VpcId: Instance VPC ID
        :type VpcId: str
        :param _SubnetId: VPC subnet ID
        :type SubnetId: str
        :param _Status: Instance status information
- `1`: Task running.
- `2`: Instance running.
- `-2`: Instance isolated.
- `-3`: Instance being eliminated.
- `-4`: Instance eliminated.
        :type Status: str
        :param _Vips: Private network IP address of an instance
        :type Vips: list of str
        :param _Vport: Instance network port
        :type Vport: int
        :param _Createtime: Instance creation time
        :type Createtime: str
        :param _PayMode: Billing type
- `0`: Pay-as-you-go.
- `1`: Monthly subscription.
        :type PayMode: int
        :param _NetType: Network Type
- `0`: Classic network.
- `1`: VPC.
        :type NetType: int
        """
        self._InstanceName = None
        self._InstanceId = None
        self._AppId = None
        self._ProjectId = None
        self._Region = None
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._Status = None
        self._Vips = None
        self._Vport = None
        self._Createtime = None
        self._PayMode = None
        self._NetType = None

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Vips(self):
        return self._Vips

    @Vips.setter
    def Vips(self, Vips):
        self._Vips = Vips

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Createtime(self):
        return self._Createtime

    @Createtime.setter
    def Createtime(self, Createtime):
        self._Createtime = Createtime

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._InstanceId = params.get("InstanceId")
        self._AppId = params.get("AppId")
        self._ProjectId = params.get("ProjectId")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Status = params.get("Status")
        self._Vips = params.get("Vips")
        self._Vport = params.get("Vport")
        self._Createtime = params.get("Createtime")
        self._PayMode = params.get("PayMode")
        self._NetType = params.get("NetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisNode(AbstractModel):
    """Running information of Redis nodes

    """

    def __init__(self):
        r"""
        :param _Keys: Number of keys on Redis nodes
        :type Keys: int
        :param _Slot: Slot distribution range for Redis node.  Value range:  0-5460.
        :type Slot: str
        :param _NodeId: Node sequence ID
        :type NodeId: str
        :param _Status: Node status
        :type Status: str
        :param _Role: Node role
        :type Role: str
        """
        self._Keys = None
        self._Slot = None
        self._NodeId = None
        self._Status = None
        self._Role = None

    @property
    def Keys(self):
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def Slot(self):
        return self._Slot

    @Slot.setter
    def Slot(self, Slot):
        self._Slot = Slot

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role


    def _deserialize(self, params):
        self._Keys = params.get("Keys")
        self._Slot = params.get("Slot")
        self._NodeId = params.get("NodeId")
        self._Status = params.get("Status")
        self._Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisNodeInfo(AbstractModel):
    """Master or replica node information of the TencentDB for Redis instance.

    """

    def __init__(self):
        r"""
        :param _NodeType: Node type. <ul><li>`0`: Master node.</li><li>`1`: Replica node.</li></ul>
        :type NodeType: int
        :param _NodeId: ID of the master or replica node <ul><li>This parameter is optional when the [CreateInstances](https://intl.cloud.tencent.com/document/product/239/20026?from_cn_redirect=1) API is used to create a TencentDB for Redis instance, but it is required when the [UpgradeInstance](https://intl.cloud.tencent.com/document/product/239/20013?from_cn_redirect=1) API is used to adjust the configuration of an instance by deleting a replica.  </li><li>You can use the [DescribeInstances](https://intl.cloud.tencent.com/document/product/239/20018?from_cn_redirect=1) API to get the node ID of integer type. </li></ul> </li></ul>
        :type NodeId: int
        :param _ZoneId: ID of the AZ of the master or replica node
        :type ZoneId: int
        :param _ZoneName: Name of the AZ of the master or replica node
        :type ZoneName: str
        """
        self._NodeType = None
        self._NodeId = None
        self._ZoneId = None
        self._ZoneName = None

    @property
    def NodeType(self):
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName


    def _deserialize(self, params):
        self._NodeType = params.get("NodeType")
        self._NodeId = params.get("NodeId")
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisNodes(AbstractModel):
    """Redis node information

    """

    def __init__(self):
        r"""
        :param _NodeId: Node ID
        :type NodeId: str
        :param _NodeRole: Node role
        :type NodeRole: str
        :param _ClusterId: Shard ID
        :type ClusterId: int
        :param _ZoneId: AZ ID
        :type ZoneId: int
        """
        self._NodeId = None
        self._NodeRole = None
        self._ClusterId = None
        self._ZoneId = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeRole(self):
        return self._NodeRole

    @NodeRole.setter
    def NodeRole(self, NodeRole):
        self._NodeRole = NodeRole

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._NodeRole = params.get("NodeRole")
        self._ClusterId = params.get("ClusterId")
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionConf(AbstractModel):
    """Region information

    """

    def __init__(self):
        r"""
        :param _RegionId: Region ID
        :type RegionId: str
        :param _RegionName: Region name
        :type RegionName: str
        :param _RegionShortName: Region abbreviation
        :type RegionShortName: str
        :param _Area: Name of the area where a region is located
        :type Area: str
        :param _ZoneSet: AZ information
        :type ZoneSet: list of ZoneCapacityConf
        """
        self._RegionId = None
        self._RegionName = None
        self._RegionShortName = None
        self._Area = None
        self._ZoneSet = None

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionShortName(self):
        return self._RegionShortName

    @RegionShortName.setter
    def RegionShortName(self, RegionShortName):
        self._RegionShortName = RegionShortName

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def ZoneSet(self):
        return self._ZoneSet

    @ZoneSet.setter
    def ZoneSet(self, ZoneSet):
        self._ZoneSet = ZoneSet


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._RegionShortName = params.get("RegionShortName")
        self._Area = params.get("Area")
        if params.get("ZoneSet") is not None:
            self._ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = ZoneCapacityConf()
                obj._deserialize(item)
                self._ZoneSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseWanAddressRequest(AbstractModel):
    """ReleaseWanAddress request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class ReleaseWanAddressResponse(AbstractModel):
    """ReleaseWanAddress response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task ID
        :type FlowId: int
        :param _WanStatus: Status of disabling public network access
        :type WanStatus: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._WanStatus = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def WanStatus(self):
        return self._WanStatus

    @WanStatus.setter
    def WanStatus(self, WanStatus):
        self._WanStatus = WanStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._WanStatus = params.get("WanStatus")
        self._RequestId = params.get("RequestId")


class RemoveReplicationInstanceRequest(AbstractModel):
    """RemoveReplicationInstance request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Replication group ID
        :type GroupId: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _SyncType: Data sync type. Valid values: `true` (strong sync is required), `false` (strong sync is not required, only the master instance can be deleted).
        :type SyncType: bool
        """
        self._GroupId = None
        self._InstanceId = None
        self._SyncType = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SyncType(self):
        return self._SyncType

    @SyncType.setter
    def SyncType(self, SyncType):
        self._SyncType = SyncType


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._InstanceId = params.get("InstanceId")
        self._SyncType = params.get("SyncType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveReplicationInstanceResponse(AbstractModel):
    """RemoveReplicationInstance response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Async task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class RenewInstanceRequest(AbstractModel):
    """RenewInstance request structure.

    """

    def __init__(self):
        r"""
        :param _Period: Validity period in months
        :type Period: int
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ModifyPayMode: The parameter used to determine whether to modify the billing mode. <ul><li>If you want to change the billing mode from pay-as-you-go to monthly subscription, specify this parameter as <b>prepaid</b>. </li><li>If the current instance is monthly subscribed, this parameter is not required. </li></ul>
        :type ModifyPayMode: str
        """
        self._Period = None
        self._InstanceId = None
        self._ModifyPayMode = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ModifyPayMode(self):
        return self._ModifyPayMode

    @ModifyPayMode.setter
    def ModifyPayMode(self, ModifyPayMode):
        self._ModifyPayMode = ModifyPayMode


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._InstanceId = params.get("InstanceId")
        self._ModifyPayMode = params.get("ModifyPayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstanceResponse(AbstractModel):
    """RenewInstance response structure.

    """

    def __init__(self):
        r"""
        :param _DealId: Transaction ID
        :type DealId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealId = None
        self._RequestId = None

    @property
    def DealId(self):
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._RequestId = params.get("RequestId")


class ReplicaGroup(AbstractModel):
    """Information of the instance node group

    """

    def __init__(self):
        r"""
        :param _GroupId: Node group ID
        :type GroupId: int
        :param _GroupName: Node group name, which is empty for the master node
        :type GroupName: str
        :param _ZoneId: Node AZ ID, such as ap-guangzhou-1
        :type ZoneId: str
        :param _Role: Node group type. Valid values: master (master node group); replica (replica node group)
        :type Role: str
        :param _RedisNodes: List of nodes in the node group
        :type RedisNodes: list of RedisNode
        """
        self._GroupId = None
        self._GroupName = None
        self._ZoneId = None
        self._Role = None
        self._RedisNodes = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def RedisNodes(self):
        return self._RedisNodes

    @RedisNodes.setter
    def RedisNodes(self, RedisNodes):
        self._RedisNodes = RedisNodes


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._ZoneId = params.get("ZoneId")
        self._Role = params.get("Role")
        if params.get("RedisNodes") is not None:
            self._RedisNodes = []
            for item in params.get("RedisNodes"):
                obj = RedisNode()
                obj._deserialize(item)
                self._RedisNodes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetPasswordRequest(AbstractModel):
    """ResetPassword request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Redis instance ID
        :type InstanceId: str
        :param _Password: Password reset (this parameter can be left blank when switching to password-free instance mode and is required in other cases)
        :type Password: str
        :param _NoAuth: Whether to switch to password-free instance mode. false: switch to password-enabled instance mode; true: switch to password-free instance mode. Default value: false.
        :type NoAuth: bool
        """
        self._InstanceId = None
        self._Password = None
        self._NoAuth = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def NoAuth(self):
        return self._NoAuth

    @NoAuth.setter
    def NoAuth(self, NoAuth):
        self._NoAuth = NoAuth


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Password = params.get("Password")
        self._NoAuth = params.get("NoAuth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetPasswordResponse(AbstractModel):
    """ResetPassword response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID (this parameter is the task ID when changing a password. If you are switching between password-free and password-enabled instance mode, you can leave this parameter alone)
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ResourceTag(AbstractModel):
    """Tag bound to the instance purchased via API

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
        :type TagKey: str
        :param _TagValue: The value corresponding to the tag key
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
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
        


class RestoreInstanceRequest(AbstractModel):
    """RestoreInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of the instance to be operated on, which can be obtained through the `InstanceId` field in the return value of the `DescribeInstances` API.
        :type InstanceId: str
        :param _BackupId: Backup ID, which can be obtained through the `backupId` field in the return value of the `GetRedisBackupList` API.
        :type BackupId: str
        :param _Password: Instance password, which needs to be validated during instance restoration (this parameter is not required for password-free instances)
        :type Password: str
        """
        self._InstanceId = None
        self._BackupId = None
        self._Password = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupId(self):
        return self._BackupId

    @BackupId.setter
    def BackupId(self, BackupId):
        self._BackupId = BackupId

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupId = params.get("BackupId")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestoreInstanceResponse(AbstractModel):
    """RestoreInstance response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID, which can be used to query the task execution status through the `DescribeTaskInfo` API.
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class SecurityGroup(AbstractModel):
    """Security group rules

    """

    def __init__(self):
        r"""
        :param _CreateTime: Creation time in the format of yyyy-mm-dd hh:mm:ss.
        :type CreateTime: str
        :param _ProjectId: Project ID.
        :type ProjectId: int
        :param _SecurityGroupId: Security group ID.
        :type SecurityGroupId: str
        :param _SecurityGroupName: Security group name.
        :type SecurityGroupName: str
        :param _SecurityGroupRemark: Security group remarks.
        :type SecurityGroupRemark: str
        :param _Outbound: Outbound rule.
        :type Outbound: list of Outbound
        :param _Inbound: Inbound rule.
        :type Inbound: list of Inbound
        """
        self._CreateTime = None
        self._ProjectId = None
        self._SecurityGroupId = None
        self._SecurityGroupName = None
        self._SecurityGroupRemark = None
        self._Outbound = None
        self._Inbound = None

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupName(self):
        return self._SecurityGroupName

    @SecurityGroupName.setter
    def SecurityGroupName(self, SecurityGroupName):
        self._SecurityGroupName = SecurityGroupName

    @property
    def SecurityGroupRemark(self):
        return self._SecurityGroupRemark

    @SecurityGroupRemark.setter
    def SecurityGroupRemark(self, SecurityGroupRemark):
        self._SecurityGroupRemark = SecurityGroupRemark

    @property
    def Outbound(self):
        return self._Outbound

    @Outbound.setter
    def Outbound(self, Outbound):
        self._Outbound = Outbound

    @property
    def Inbound(self):
        return self._Inbound

    @Inbound.setter
    def Inbound(self, Inbound):
        self._Inbound = Inbound


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._ProjectId = params.get("ProjectId")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._SecurityGroupName = params.get("SecurityGroupName")
        self._SecurityGroupRemark = params.get("SecurityGroupRemark")
        if params.get("Outbound") is not None:
            self._Outbound = []
            for item in params.get("Outbound"):
                obj = Outbound()
                obj._deserialize(item)
                self._Outbound.append(obj)
        if params.get("Inbound") is not None:
            self._Inbound = []
            for item in params.get("Inbound"):
                obj = Inbound()
                obj._deserialize(item)
                self._Inbound.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupDetail(AbstractModel):
    """Security group details

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _CreateTime: Security group creation time
        :type CreateTime: str
        :param _SecurityGroupId: Security group ID
        :type SecurityGroupId: str
        :param _SecurityGroupName: Security group name
        :type SecurityGroupName: str
        :param _SecurityGroupRemark: Security group remarks
        :type SecurityGroupRemark: str
        :param _InboundRule: Inbound rules of the security group, which control the access source to the database.
        :type InboundRule: list of SecurityGroupsInboundAndOutbound
        :param _OutboundRule: Security group outbound rule
        :type OutboundRule: list of SecurityGroupsInboundAndOutbound
        """
        self._ProjectId = None
        self._CreateTime = None
        self._SecurityGroupId = None
        self._SecurityGroupName = None
        self._SecurityGroupRemark = None
        self._InboundRule = None
        self._OutboundRule = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SecurityGroupId(self):
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupName(self):
        return self._SecurityGroupName

    @SecurityGroupName.setter
    def SecurityGroupName(self, SecurityGroupName):
        self._SecurityGroupName = SecurityGroupName

    @property
    def SecurityGroupRemark(self):
        return self._SecurityGroupRemark

    @SecurityGroupRemark.setter
    def SecurityGroupRemark(self, SecurityGroupRemark):
        self._SecurityGroupRemark = SecurityGroupRemark

    @property
    def InboundRule(self):
        return self._InboundRule

    @InboundRule.setter
    def InboundRule(self, InboundRule):
        self._InboundRule = InboundRule

    @property
    def OutboundRule(self):
        return self._OutboundRule

    @OutboundRule.setter
    def OutboundRule(self, OutboundRule):
        self._OutboundRule = OutboundRule


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CreateTime = params.get("CreateTime")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._SecurityGroupName = params.get("SecurityGroupName")
        self._SecurityGroupRemark = params.get("SecurityGroupRemark")
        if params.get("InboundRule") is not None:
            self._InboundRule = []
            for item in params.get("InboundRule"):
                obj = SecurityGroupsInboundAndOutbound()
                obj._deserialize(item)
                self._InboundRule.append(obj)
        if params.get("OutboundRule") is not None:
            self._OutboundRule = []
            for item in params.get("OutboundRule"):
                obj = SecurityGroupsInboundAndOutbound()
                obj._deserialize(item)
                self._OutboundRule.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupsInboundAndOutbound(AbstractModel):
    """Security group inbound/outbound rules

    """

    def __init__(self):
        r"""
        :param _Action: Identify whether the IP and port for accessing the database are allowed
        :type Action: str
        :param _Ip: IP address for accessing the database
        :type Ip: str
        :param _Port: Port number
        :type Port: str
        :param _Proto: Protocol type
        :type Proto: str
        """
        self._Action = None
        self._Ip = None
        self._Port = None
        self._Proto = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Proto(self):
        return self._Proto

    @Proto.setter
    def Proto(self, Proto):
        self._Proto = Proto


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._Proto = params.get("Proto")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SourceCommand(AbstractModel):
    """Access command

    """

    def __init__(self):
        r"""
        :param _Cmd: Command
        :type Cmd: str
        :param _Count: Number of executions
        :type Count: int
        """
        self._Cmd = None
        self._Count = None

    @property
    def Cmd(self):
        return self._Cmd

    @Cmd.setter
    def Cmd(self, Cmd):
        self._Cmd = Cmd

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Cmd = params.get("Cmd")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SourceInfo(AbstractModel):
    """Access source information

    """

    def __init__(self):
        r"""
        :param _Ip: Source IP
        :type Ip: str
        :param _Conn: Number of connections
        :type Conn: int
        :param _Cmd: Command
        :type Cmd: int
        """
        self._Ip = None
        self._Conn = None
        self._Cmd = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Conn(self):
        return self._Conn

    @Conn.setter
    def Conn(self, Conn):
        self._Conn = Conn

    @property
    def Cmd(self):
        return self._Cmd

    @Cmd.setter
    def Cmd(self, Cmd):
        self._Cmd = Cmd


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Conn = params.get("Conn")
        self._Cmd = params.get("Cmd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartupInstanceRequest(AbstractModel):
    """StartupInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class StartupInstanceResponse(AbstractModel):
    """StartupInstance response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class SwitchInstanceVipRequest(AbstractModel):
    """SwitchInstanceVip request structure.

    """

    def __init__(self):
        r"""
        :param _SrcInstanceId: Source instance ID
        :type SrcInstanceId: str
        :param _DstInstanceId: Target instance ID
        :type DstInstanceId: str
        :param _TimeDelay: The time that lapses in seconds since DTS is disconnected between the source instance and the target instance. If the DTS disconnection time period is greater than TimeDelay, the VIP will not be switched. We recommend you set an acceptable value based on the actual business conditions.
        :type TimeDelay: int
        :param _ForceSwitch: Whether to force the switch when DTS is disconnected. 1: yes; 0: no.
        :type ForceSwitch: int
        :param _SwitchTime: now: switch now; syncComplete: switch after sync is completed
        :type SwitchTime: str
        """
        self._SrcInstanceId = None
        self._DstInstanceId = None
        self._TimeDelay = None
        self._ForceSwitch = None
        self._SwitchTime = None

    @property
    def SrcInstanceId(self):
        return self._SrcInstanceId

    @SrcInstanceId.setter
    def SrcInstanceId(self, SrcInstanceId):
        self._SrcInstanceId = SrcInstanceId

    @property
    def DstInstanceId(self):
        return self._DstInstanceId

    @DstInstanceId.setter
    def DstInstanceId(self, DstInstanceId):
        self._DstInstanceId = DstInstanceId

    @property
    def TimeDelay(self):
        return self._TimeDelay

    @TimeDelay.setter
    def TimeDelay(self, TimeDelay):
        self._TimeDelay = TimeDelay

    @property
    def ForceSwitch(self):
        return self._ForceSwitch

    @ForceSwitch.setter
    def ForceSwitch(self, ForceSwitch):
        self._ForceSwitch = ForceSwitch

    @property
    def SwitchTime(self):
        return self._SwitchTime

    @SwitchTime.setter
    def SwitchTime(self, SwitchTime):
        self._SwitchTime = SwitchTime


    def _deserialize(self, params):
        self._SrcInstanceId = params.get("SrcInstanceId")
        self._DstInstanceId = params.get("DstInstanceId")
        self._TimeDelay = params.get("TimeDelay")
        self._ForceSwitch = params.get("ForceSwitch")
        self._SwitchTime = params.get("SwitchTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchInstanceVipResponse(AbstractModel):
    """SwitchInstanceVip response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class SwitchProxyRequest(AbstractModel):
    """SwitchProxy request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _ProxyID: Instance ProxyID
        :type ProxyID: str
        """
        self._InstanceId = None
        self._ProxyID = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProxyID(self):
        return self._ProxyID

    @ProxyID.setter
    def ProxyID(self, ProxyID):
        self._ProxyID = ProxyID


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ProxyID = params.get("ProxyID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchProxyResponse(AbstractModel):
    """SwitchProxy response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class TaskInfoDetail(AbstractModel):
    """Task details

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type TaskId: int
        :param _StartTime: Task start time 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param _TaskType: Task type. Valid values:  - `FLOW_CREATE`: Create an instance. - `FLOW_MODIFYCONNECTIONCONFIG`: Adjust the number of bandwidth connections. - `FLOW_MODIFYINSTANCEPASSWORDFREE`: Modify the process of password-free access. - `FLOW_CLEARNETWORK`: Returning VPC - `FLOW_SETPWD`: Set the access password. - `FLOW_EXPORSHR`: Expand or reduce the capacity. - `FLOW_UpgradeArch`: Upgrade the instance architecture. - `FLOW_MODIFYINSTANCEPARAMS`: Modify the instance parameters. - `FLOW_MODIFYINSTACEREADONLY`: Modify read-only process. - `FLOW_CLOSE`: Disable the instance. - `FLOW_DELETE`: Delete the instance. - `FLOW_OPEN_WAN`: Enable the public network. - `FLOW_FLOW_CLEAN`: Clear the instance. - `FLOW_MODIFYINSTANCEACCOUNT`: Modify the instance account. - `FLOW_ENABLEINSTANCE_REPLICATE`: Enable the replica read-only feature. - `FLOW_DISABLEINSTANCE_REPLICATE`: Disable the replica read-only feature. - `FLOW_SWITCHINSTANCEVIP`: Swap the VIPs of instances. - FLOW_CHANGE_REPLICA_TO_MSTER: Promote the replica node to the mater node. Backup instance 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type TaskType: str
        :param _InstanceName: Instance name 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param _InstanceId: Instance ID 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _ProjectId: Project ID 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type ProjectId: int
        :param _Progress: Task progress 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type Progress: float
        :param _EndTime: Task end time 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        :param _Result: Task execution status. Valid values: - `0` (initilized) - `1` (executing) - `2` (completed) - `4` (failed) 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type Result: int
        """
        self._TaskId = None
        self._StartTime = None
        self._TaskType = None
        self._InstanceName = None
        self._InstanceId = None
        self._ProjectId = None
        self._Progress = None
        self._EndTime = None
        self._Result = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._StartTime = params.get("StartTime")
        self._TaskType = params.get("TaskType")
        self._InstanceName = params.get("InstanceName")
        self._InstanceId = params.get("InstanceId")
        self._ProjectId = params.get("ProjectId")
        self._Progress = params.get("Progress")
        self._EndTime = params.get("EndTime")
        self._Result = params.get("Result")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TendisNodes(AbstractModel):
    """Tendis node information

    """

    def __init__(self):
        r"""
        :param _NodeId: Node ID
        :type NodeId: str
        :param _NodeRole: Node role
        :type NodeRole: str
        """
        self._NodeId = None
        self._NodeRole = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeRole(self):
        return self._NodeRole

    @NodeRole.setter
    def NodeRole(self, NodeRole):
        self._NodeRole = NodeRole


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._NodeRole = params.get("NodeRole")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TendisSlowLogDetail(AbstractModel):
    """Tendis slow query details

    """

    def __init__(self):
        r"""
        :param _ExecuteTime: Execution time
        :type ExecuteTime: str
        :param _Duration: Duration of the slow query (ms)
        :type Duration: int
        :param _Command: Command
        :type Command: str
        :param _CommandLine: Command line details
        :type CommandLine: str
        :param _Node: Node ID
        :type Node: str
        """
        self._ExecuteTime = None
        self._Duration = None
        self._Command = None
        self._CommandLine = None
        self._Node = None

    @property
    def ExecuteTime(self):
        return self._ExecuteTime

    @ExecuteTime.setter
    def ExecuteTime(self, ExecuteTime):
        self._ExecuteTime = ExecuteTime

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Command(self):
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def CommandLine(self):
        return self._CommandLine

    @CommandLine.setter
    def CommandLine(self, CommandLine):
        self._CommandLine = CommandLine

    @property
    def Node(self):
        return self._Node

    @Node.setter
    def Node(self, Node):
        self._Node = Node


    def _deserialize(self, params):
        self._ExecuteTime = params.get("ExecuteTime")
        self._Duration = params.get("Duration")
        self._Command = params.get("Command")
        self._CommandLine = params.get("CommandLine")
        self._Node = params.get("Node")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TradeDealDetail(AbstractModel):
    """Order transaction information

    """

    def __init__(self):
        r"""
        :param _DealId: Order ID, which is used when a TencentCloud API is called.
        :type DealId: str
        :param _DealName: Long order ID, which is used when an order issue is submitted for assistance.
        :type DealName: str
        :param _ZoneId: AZ ID
        :type ZoneId: int
        :param _GoodsNum: Number of instances associated with the order
        :type GoodsNum: int
        :param _Creater: Creator UIN
        :type Creater: str
        :param _CreatTime: Order creation time
        :type CreatTime: str
        :param _OverdueTime: Order timeout period
        :type OverdueTime: str
        :param _EndTime: Order completion time
        :type EndTime: str
        :param _Status: Order status. 1: unpaid; 2: paid but not delivered; 3: In delivery; 4: successfully delivered; 5: delivery failed; 6: refunded; 7: order closed; 8: order expired; 9: order invalidated; 10: product invalidated; 11: requested payment rejected; 12: paying
        :type Status: int
        :param _Description: Order status description
        :type Description: str
        :param _Price: Actual total price of the order in 0.01 CNY
        :type Price: int
        :param _InstanceIds: Instance ID
        :type InstanceIds: list of str
        """
        self._DealId = None
        self._DealName = None
        self._ZoneId = None
        self._GoodsNum = None
        self._Creater = None
        self._CreatTime = None
        self._OverdueTime = None
        self._EndTime = None
        self._Status = None
        self._Description = None
        self._Price = None
        self._InstanceIds = None

    @property
    def DealId(self):
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Creater(self):
        return self._Creater

    @Creater.setter
    def Creater(self, Creater):
        self._Creater = Creater

    @property
    def CreatTime(self):
        return self._CreatTime

    @CreatTime.setter
    def CreatTime(self, CreatTime):
        self._CreatTime = CreatTime

    @property
    def OverdueTime(self):
        return self._OverdueTime

    @OverdueTime.setter
    def OverdueTime(self, OverdueTime):
        self._OverdueTime = OverdueTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._DealName = params.get("DealName")
        self._ZoneId = params.get("ZoneId")
        self._GoodsNum = params.get("GoodsNum")
        self._Creater = params.get("Creater")
        self._CreatTime = params.get("CreatTime")
        self._OverdueTime = params.get("OverdueTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._Description = params.get("Description")
        self._Price = params.get("Price")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceRequest(AbstractModel):
    """UpgradeInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: The ID of instance to be modified.
        :type InstanceId: str
        :param _MemSize: New memory size of an instance shard. <ul><li>Unit: MB. </li><li>You can only modify one of the three parameters at a time: `MemSize`, `RedisShardNum`, and `RedisReplicasNum`. To modify one of them, you need to enter the other two, which are consistent with the original configuration specifications of the instance. </li><li>In case of capacity reduction, the new specification must be at least 1.3 times the used capacity; otherwise, the operation will fail.</li></ul>
        :type MemSize: int
        :param _RedisShardNum: New number of instance shards. <ul><li>This parameter is not required for standard architecture instances, but for cluster architecture instances. </li><li>For cluster architecture, you can only modify one of the three parameters at a time: `MemSize`, `RedisShardNum`, and `RedisReplicasNum`. To modify one of them, you need to enter the other two, which are consistent with the original configuration specifications of the instance. </li></ul>
        :type RedisShardNum: int
        :param _RedisReplicasNum: New replica quantity. <ul><li>You can only modify one of the three parameters at a time: `MemSize`, `RedisShardNum`, and `RedisReplicasNum`. To modify one of them, you need to enter the other two, which are consistent with the original configuration specifications of the instance. </li></ul>To modify the number of replicas in a multi-AZ instance, `NodeSet` must be passed in.</li></ul>
        :type RedisReplicasNum: int
        :param _NodeSet: Additional information for adding replicas for multi-AZ instances, including replica AZ and type (`NodeType` is `1`). This parameter is not required for single-AZ instances.
        :type NodeSet: list of RedisNodeInfo
        """
        self._InstanceId = None
        self._MemSize = None
        self._RedisShardNum = None
        self._RedisReplicasNum = None
        self._NodeSet = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MemSize(self):
        return self._MemSize

    @MemSize.setter
    def MemSize(self, MemSize):
        self._MemSize = MemSize

    @property
    def RedisShardNum(self):
        return self._RedisShardNum

    @RedisShardNum.setter
    def RedisShardNum(self, RedisShardNum):
        self._RedisShardNum = RedisShardNum

    @property
    def RedisReplicasNum(self):
        return self._RedisReplicasNum

    @RedisReplicasNum.setter
    def RedisReplicasNum(self, RedisReplicasNum):
        self._RedisReplicasNum = RedisReplicasNum

    @property
    def NodeSet(self):
        return self._NodeSet

    @NodeSet.setter
    def NodeSet(self, NodeSet):
        self._NodeSet = NodeSet


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._MemSize = params.get("MemSize")
        self._RedisShardNum = params.get("RedisShardNum")
        self._RedisReplicasNum = params.get("RedisReplicasNum")
        if params.get("NodeSet") is not None:
            self._NodeSet = []
            for item in params.get("NodeSet"):
                obj = RedisNodeInfo()
                obj._deserialize(item)
                self._NodeSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceResponse(AbstractModel):
    """UpgradeInstance response structure.

    """

    def __init__(self):
        r"""
        :param _DealId: Order ID
        :type DealId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealId = None
        self._RequestId = None

    @property
    def DealId(self):
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._RequestId = params.get("RequestId")


class UpgradeInstanceVersionRequest(AbstractModel):
    """UpgradeInstanceVersion request structure.

    """

    def __init__(self):
        r"""
        :param _TargetInstanceType: Target instance type after the change, which is the same as the `TypeId` of the [CreateInstances](https://intl.cloud.tencent.com/document/api/239/20026?from_cn_redirect=1) API.
- For Redis 4.0 or later, a standard architecture instance can be upgraded to a cluster architecture instance on the same version; for example, you can upgrade from Redis 4.0 Standard Architecture to Redis 4.0 Cluster Architecture.
- Cross-version architecture upgrade is not supported; for example, you cannot upgrade from Redis 4.0 Standard Architecture to Redis 5.0 Cluster Architecture.
- The architecture of Redis 2.8 cannot be upgraded.
- Cluster architecture cannot be downgraded to standard architecture.

        :type TargetInstanceType: str
        :param _SwitchOption: Switch time. Valid values:
- `1`: Switch in the maintenance time.
- `2` (default value): Switch now.
        :type SwitchOption: int
        :param _InstanceId: ID of the specified instance, such as `crs-xjhsdj****`. Log in to the [Redis console](https://console.cloud.tencent.com/redis#/), and copy it in the instance list.
        :type InstanceId: str
        """
        self._TargetInstanceType = None
        self._SwitchOption = None
        self._InstanceId = None

    @property
    def TargetInstanceType(self):
        return self._TargetInstanceType

    @TargetInstanceType.setter
    def TargetInstanceType(self, TargetInstanceType):
        self._TargetInstanceType = TargetInstanceType

    @property
    def SwitchOption(self):
        return self._SwitchOption

    @SwitchOption.setter
    def SwitchOption(self, SwitchOption):
        self._SwitchOption = SwitchOption

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._TargetInstanceType = params.get("TargetInstanceType")
        self._SwitchOption = params.get("SwitchOption")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceVersionResponse(AbstractModel):
    """UpgradeInstanceVersion response structure.

    """

    def __init__(self):
        r"""
        :param _DealId: Order ID
        :type DealId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealId = None
        self._RequestId = None

    @property
    def DealId(self):
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._RequestId = params.get("RequestId")


class UpgradeProxyVersionRequest(AbstractModel):
    """UpgradeProxyVersion request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _CurrentProxyVersion: The current proxy version
        :type CurrentProxyVersion: str
        :param _UpgradeProxyVersion: Upgradeable redis version
        :type UpgradeProxyVersion: str
        :param _InstanceTypeUpgradeNow: `1` (upgrade immediately), `0` (upgrade during maintenance time)
        :type InstanceTypeUpgradeNow: int
        """
        self._InstanceId = None
        self._CurrentProxyVersion = None
        self._UpgradeProxyVersion = None
        self._InstanceTypeUpgradeNow = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CurrentProxyVersion(self):
        return self._CurrentProxyVersion

    @CurrentProxyVersion.setter
    def CurrentProxyVersion(self, CurrentProxyVersion):
        self._CurrentProxyVersion = CurrentProxyVersion

    @property
    def UpgradeProxyVersion(self):
        return self._UpgradeProxyVersion

    @UpgradeProxyVersion.setter
    def UpgradeProxyVersion(self, UpgradeProxyVersion):
        self._UpgradeProxyVersion = UpgradeProxyVersion

    @property
    def InstanceTypeUpgradeNow(self):
        return self._InstanceTypeUpgradeNow

    @InstanceTypeUpgradeNow.setter
    def InstanceTypeUpgradeNow(self, InstanceTypeUpgradeNow):
        self._InstanceTypeUpgradeNow = InstanceTypeUpgradeNow


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._CurrentProxyVersion = params.get("CurrentProxyVersion")
        self._UpgradeProxyVersion = params.get("UpgradeProxyVersion")
        self._InstanceTypeUpgradeNow = params.get("InstanceTypeUpgradeNow")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeProxyVersionResponse(AbstractModel):
    """UpgradeProxyVersion response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class UpgradeSmallVersionRequest(AbstractModel):
    """UpgradeSmallVersion request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _CurrentRedisVersion: The current redis version
        :type CurrentRedisVersion: str
        :param _UpgradeRedisVersion: Upgradeable redis version
        :type UpgradeRedisVersion: str
        :param _InstanceTypeUpgradeNow: `1` (upgrade immediately), `0` (upgrade during maintenance time)
        :type InstanceTypeUpgradeNow: int
        """
        self._InstanceId = None
        self._CurrentRedisVersion = None
        self._UpgradeRedisVersion = None
        self._InstanceTypeUpgradeNow = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CurrentRedisVersion(self):
        return self._CurrentRedisVersion

    @CurrentRedisVersion.setter
    def CurrentRedisVersion(self, CurrentRedisVersion):
        self._CurrentRedisVersion = CurrentRedisVersion

    @property
    def UpgradeRedisVersion(self):
        return self._UpgradeRedisVersion

    @UpgradeRedisVersion.setter
    def UpgradeRedisVersion(self, UpgradeRedisVersion):
        self._UpgradeRedisVersion = UpgradeRedisVersion

    @property
    def InstanceTypeUpgradeNow(self):
        return self._InstanceTypeUpgradeNow

    @InstanceTypeUpgradeNow.setter
    def InstanceTypeUpgradeNow(self, InstanceTypeUpgradeNow):
        self._InstanceTypeUpgradeNow = InstanceTypeUpgradeNow


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._CurrentRedisVersion = params.get("CurrentRedisVersion")
        self._UpgradeRedisVersion = params.get("UpgradeRedisVersion")
        self._InstanceTypeUpgradeNow = params.get("InstanceTypeUpgradeNow")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeSmallVersionResponse(AbstractModel):
    """UpgradeSmallVersion response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Async task ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class UpgradeVersionToMultiAvailabilityZonesRequest(AbstractModel):
    """UpgradeVersionToMultiAvailabilityZones request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _UpgradeProxyAndRedisServer: Whether to support “Reading Local Nodes Only” feature after upgrading to multi-AZ deployment.
ul><li>`true`: The “Read Local Nodes Only” feature is supported. During the upgrade, you need to upgrade the proxy version and Redis kernel minor version simultaneously, which will involve data migration and may take hours to complete. </li><li>`false`: The “Read Local Nodes Only” feature is not supported. Upgrading to multi-AZ deployment will involve metadata migration only without affecting the service, which generally take less than three minutes to complete.</li></ul>
        :type UpgradeProxyAndRedisServer: bool
        """
        self._InstanceId = None
        self._UpgradeProxyAndRedisServer = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UpgradeProxyAndRedisServer(self):
        return self._UpgradeProxyAndRedisServer

    @UpgradeProxyAndRedisServer.setter
    def UpgradeProxyAndRedisServer(self, UpgradeProxyAndRedisServer):
        self._UpgradeProxyAndRedisServer = UpgradeProxyAndRedisServer


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UpgradeProxyAndRedisServer = params.get("UpgradeProxyAndRedisServer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeVersionToMultiAvailabilityZonesResponse(AbstractModel):
    """UpgradeVersionToMultiAvailabilityZones response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task ID
        :type FlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ZoneCapacityConf(AbstractModel):
    """Product information in the availability zone

    """

    def __init__(self):
        r"""
        :param _ZoneId: AZ ID, such as ap-guangzhou-3
        :type ZoneId: str
        :param _ZoneName: AZ name
        :type ZoneName: str
        :param _IsSaleout: Whether a product is sold out in an AZ
        :type IsSaleout: bool
        :param _IsDefault: Whether it is a default AZ
        :type IsDefault: bool
        :param _NetWorkType: Network type. basenet: basic network; vpcnet: VPC
        :type NetWorkType: list of str
        :param _ProductSet: Information of an AZ, such as product specifications in it
        :type ProductSet: list of ProductConf
        :param _OldZoneId: AZ ID, such as 100003
        :type OldZoneId: int
        """
        self._ZoneId = None
        self._ZoneName = None
        self._IsSaleout = None
        self._IsDefault = None
        self._NetWorkType = None
        self._ProductSet = None
        self._OldZoneId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def IsSaleout(self):
        return self._IsSaleout

    @IsSaleout.setter
    def IsSaleout(self, IsSaleout):
        self._IsSaleout = IsSaleout

    @property
    def IsDefault(self):
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def NetWorkType(self):
        return self._NetWorkType

    @NetWorkType.setter
    def NetWorkType(self, NetWorkType):
        self._NetWorkType = NetWorkType

    @property
    def ProductSet(self):
        return self._ProductSet

    @ProductSet.setter
    def ProductSet(self, ProductSet):
        self._ProductSet = ProductSet

    @property
    def OldZoneId(self):
        return self._OldZoneId

    @OldZoneId.setter
    def OldZoneId(self, OldZoneId):
        self._OldZoneId = OldZoneId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._IsSaleout = params.get("IsSaleout")
        self._IsDefault = params.get("IsDefault")
        self._NetWorkType = params.get("NetWorkType")
        if params.get("ProductSet") is not None:
            self._ProductSet = []
            for item in params.get("ProductSet"):
                obj = ProductConf()
                obj._deserialize(item)
                self._ProductSet.append(obj)
        self._OldZoneId = params.get("OldZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        