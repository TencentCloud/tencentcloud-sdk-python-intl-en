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


class AccessGroup(AbstractModel):
    """Permission group

    """

    def __init__(self):
        r"""
        :param _AccessGroupId: Permission group ID
        :type AccessGroupId: str
        :param _AccessGroupName: Permission group name
        :type AccessGroupName: str
        :param _Description: Permission group description
        :type Description: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _VpcType: VPC type (1: CVM; 2: BM 1.0)
        :type VpcType: int
        :param _VpcId: VPC ID
        :type VpcId: str
        """
        self._AccessGroupId = None
        self._AccessGroupName = None
        self._Description = None
        self._CreateTime = None
        self._VpcType = None
        self._VpcId = None

    @property
    def AccessGroupId(self):
        return self._AccessGroupId

    @AccessGroupId.setter
    def AccessGroupId(self, AccessGroupId):
        self._AccessGroupId = AccessGroupId

    @property
    def AccessGroupName(self):
        return self._AccessGroupName

    @AccessGroupName.setter
    def AccessGroupName(self, AccessGroupName):
        self._AccessGroupName = AccessGroupName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def VpcType(self):
        return self._VpcType

    @VpcType.setter
    def VpcType(self, VpcType):
        self._VpcType = VpcType

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        self._AccessGroupId = params.get("AccessGroupId")
        self._AccessGroupName = params.get("AccessGroupName")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._VpcType = params.get("VpcType")
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessRule(AbstractModel):
    """Permission rule

    """

    def __init__(self):
        r"""
        :param _AccessRuleId: Permission rule ID
        :type AccessRuleId: int
        :param _Address: Permission rule address (IP range or IP)
        :type Address: str
        :param _AccessMode: Permission rule access mode (1: read-only; 2: read-write)
        :type AccessMode: int
        :param _Priority: Priority (value range: 1–100. The smaller the value, the higher the priority)
        :type Priority: int
        :param _CreateTime: Creation time
        :type CreateTime: str
        """
        self._AccessRuleId = None
        self._Address = None
        self._AccessMode = None
        self._Priority = None
        self._CreateTime = None

    @property
    def AccessRuleId(self):
        return self._AccessRuleId

    @AccessRuleId.setter
    def AccessRuleId(self, AccessRuleId):
        self._AccessRuleId = AccessRuleId

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def AccessMode(self):
        return self._AccessMode

    @AccessMode.setter
    def AccessMode(self, AccessMode):
        self._AccessMode = AccessMode

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._AccessRuleId = params.get("AccessRuleId")
        self._Address = params.get("Address")
        self._AccessMode = params.get("AccessMode")
        self._Priority = params.get("Priority")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateAccessGroupsRequest(AbstractModel):
    """AssociateAccessGroups request structure.

    """

    def __init__(self):
        r"""
        :param _MountPointId: Mount point ID
        :type MountPointId: str
        :param _AccessGroupIds: List of permission group IDs
        :type AccessGroupIds: list of str
        """
        self._MountPointId = None
        self._AccessGroupIds = None

    @property
    def MountPointId(self):
        return self._MountPointId

    @MountPointId.setter
    def MountPointId(self, MountPointId):
        self._MountPointId = MountPointId

    @property
    def AccessGroupIds(self):
        return self._AccessGroupIds

    @AccessGroupIds.setter
    def AccessGroupIds(self, AccessGroupIds):
        self._AccessGroupIds = AccessGroupIds


    def _deserialize(self, params):
        self._MountPointId = params.get("MountPointId")
        self._AccessGroupIds = params.get("AccessGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateAccessGroupsResponse(AbstractModel):
    """AssociateAccessGroups response structure.

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


class CreateAccessGroupRequest(AbstractModel):
    """CreateAccessGroup request structure.

    """

    def __init__(self):
        r"""
        :param _AccessGroupName: Permission group name
        :type AccessGroupName: str
        :param _VpcType: VPC type (1: CVM; 2: BM 1.0)
        :type VpcType: int
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _Description: Permission group description, which is an empty string by default
        :type Description: str
        """
        self._AccessGroupName = None
        self._VpcType = None
        self._VpcId = None
        self._Description = None

    @property
    def AccessGroupName(self):
        return self._AccessGroupName

    @AccessGroupName.setter
    def AccessGroupName(self, AccessGroupName):
        self._AccessGroupName = AccessGroupName

    @property
    def VpcType(self):
        return self._VpcType

    @VpcType.setter
    def VpcType(self, VpcType):
        self._VpcType = VpcType

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._AccessGroupName = params.get("AccessGroupName")
        self._VpcType = params.get("VpcType")
        self._VpcId = params.get("VpcId")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccessGroupResponse(AbstractModel):
    """CreateAccessGroup response structure.

    """

    def __init__(self):
        r"""
        :param _AccessGroup: Permission group
        :type AccessGroup: :class:`tencentcloud.chdfs.v20201112.models.AccessGroup`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AccessGroup = None
        self._RequestId = None

    @property
    def AccessGroup(self):
        return self._AccessGroup

    @AccessGroup.setter
    def AccessGroup(self, AccessGroup):
        self._AccessGroup = AccessGroup

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AccessGroup") is not None:
            self._AccessGroup = AccessGroup()
            self._AccessGroup._deserialize(params.get("AccessGroup"))
        self._RequestId = params.get("RequestId")


class CreateAccessRulesRequest(AbstractModel):
    """CreateAccessRules request structure.

    """

    def __init__(self):
        r"""
        :param _AccessRules: Multiple permission rules (up to 10)
        :type AccessRules: list of AccessRule
        :param _AccessGroupId: Permission group ID
        :type AccessGroupId: str
        """
        self._AccessRules = None
        self._AccessGroupId = None

    @property
    def AccessRules(self):
        return self._AccessRules

    @AccessRules.setter
    def AccessRules(self, AccessRules):
        self._AccessRules = AccessRules

    @property
    def AccessGroupId(self):
        return self._AccessGroupId

    @AccessGroupId.setter
    def AccessGroupId(self, AccessGroupId):
        self._AccessGroupId = AccessGroupId


    def _deserialize(self, params):
        if params.get("AccessRules") is not None:
            self._AccessRules = []
            for item in params.get("AccessRules"):
                obj = AccessRule()
                obj._deserialize(item)
                self._AccessRules.append(obj)
        self._AccessGroupId = params.get("AccessGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccessRulesResponse(AbstractModel):
    """CreateAccessRules response structure.

    """

    def __init__(self):
        r"""
        :param _AccessRules: List of permission rules
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccessRules: list of AccessRule
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AccessRules = None
        self._RequestId = None

    @property
    def AccessRules(self):
        return self._AccessRules

    @AccessRules.setter
    def AccessRules(self, AccessRules):
        self._AccessRules = AccessRules

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AccessRules") is not None:
            self._AccessRules = []
            for item in params.get("AccessRules"):
                obj = AccessRule()
                obj._deserialize(item)
                self._AccessRules.append(obj)
        self._RequestId = params.get("RequestId")


class CreateFileSystemRequest(AbstractModel):
    """CreateFileSystem request structure.

    """

    def __init__(self):
        r"""
        :param _FileSystemName: File system name
        :type FileSystemName: str
        :param _CapacityQuota: File system capacity (in bytes), which can range from 1 GB to 1 PB and must be an integer multiple of 1 GB
        :type CapacityQuota: int
        :param _PosixAcl: Whether to verify POSIX ACL
        :type PosixAcl: bool
        :param _Description: File system description, which is an empty string by default
        :type Description: str
        :param _SuperUsers: List of superuser names, which is an empty array by default
        :type SuperUsers: list of str
        :param _RootInodeUser: Username of the root directory Inode, which is `hadoop` by default
        :type RootInodeUser: str
        :param _RootInodeGroup: Group name of the root directory Inode, which is `supergroup` by default
        :type RootInodeGroup: str
        :param _EnableRanger: Whether to enable verification of Ranger service addresses
        :type EnableRanger: bool
        :param _RangerServiceAddresses: List of Ranger service addresses (empty array by default)
        :type RangerServiceAddresses: list of str
        :param _Tags: Multiple resource tags, which can be an empty array
        :type Tags: list of Tag
        """
        self._FileSystemName = None
        self._CapacityQuota = None
        self._PosixAcl = None
        self._Description = None
        self._SuperUsers = None
        self._RootInodeUser = None
        self._RootInodeGroup = None
        self._EnableRanger = None
        self._RangerServiceAddresses = None
        self._Tags = None

    @property
    def FileSystemName(self):
        return self._FileSystemName

    @FileSystemName.setter
    def FileSystemName(self, FileSystemName):
        self._FileSystemName = FileSystemName

    @property
    def CapacityQuota(self):
        return self._CapacityQuota

    @CapacityQuota.setter
    def CapacityQuota(self, CapacityQuota):
        self._CapacityQuota = CapacityQuota

    @property
    def PosixAcl(self):
        return self._PosixAcl

    @PosixAcl.setter
    def PosixAcl(self, PosixAcl):
        self._PosixAcl = PosixAcl

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SuperUsers(self):
        return self._SuperUsers

    @SuperUsers.setter
    def SuperUsers(self, SuperUsers):
        self._SuperUsers = SuperUsers

    @property
    def RootInodeUser(self):
        return self._RootInodeUser

    @RootInodeUser.setter
    def RootInodeUser(self, RootInodeUser):
        self._RootInodeUser = RootInodeUser

    @property
    def RootInodeGroup(self):
        return self._RootInodeGroup

    @RootInodeGroup.setter
    def RootInodeGroup(self, RootInodeGroup):
        self._RootInodeGroup = RootInodeGroup

    @property
    def EnableRanger(self):
        return self._EnableRanger

    @EnableRanger.setter
    def EnableRanger(self, EnableRanger):
        self._EnableRanger = EnableRanger

    @property
    def RangerServiceAddresses(self):
        return self._RangerServiceAddresses

    @RangerServiceAddresses.setter
    def RangerServiceAddresses(self, RangerServiceAddresses):
        self._RangerServiceAddresses = RangerServiceAddresses

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._FileSystemName = params.get("FileSystemName")
        self._CapacityQuota = params.get("CapacityQuota")
        self._PosixAcl = params.get("PosixAcl")
        self._Description = params.get("Description")
        self._SuperUsers = params.get("SuperUsers")
        self._RootInodeUser = params.get("RootInodeUser")
        self._RootInodeGroup = params.get("RootInodeGroup")
        self._EnableRanger = params.get("EnableRanger")
        self._RangerServiceAddresses = params.get("RangerServiceAddresses")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFileSystemResponse(AbstractModel):
    """CreateFileSystem response structure.

    """

    def __init__(self):
        r"""
        :param _FileSystem: File system
        :type FileSystem: :class:`tencentcloud.chdfs.v20201112.models.FileSystem`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FileSystem = None
        self._RequestId = None

    @property
    def FileSystem(self):
        return self._FileSystem

    @FileSystem.setter
    def FileSystem(self, FileSystem):
        self._FileSystem = FileSystem

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FileSystem") is not None:
            self._FileSystem = FileSystem()
            self._FileSystem._deserialize(params.get("FileSystem"))
        self._RequestId = params.get("RequestId")


class CreateLifeCycleRulesRequest(AbstractModel):
    """CreateLifeCycleRules request structure.

    """

    def __init__(self):
        r"""
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        :param _LifeCycleRules: Multiple lifecycle rules (up to 10)
        :type LifeCycleRules: list of LifeCycleRule
        """
        self._FileSystemId = None
        self._LifeCycleRules = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def LifeCycleRules(self):
        return self._LifeCycleRules

    @LifeCycleRules.setter
    def LifeCycleRules(self, LifeCycleRules):
        self._LifeCycleRules = LifeCycleRules


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        if params.get("LifeCycleRules") is not None:
            self._LifeCycleRules = []
            for item in params.get("LifeCycleRules"):
                obj = LifeCycleRule()
                obj._deserialize(item)
                self._LifeCycleRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLifeCycleRulesResponse(AbstractModel):
    """CreateLifeCycleRules response structure.

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


class CreateMountPointRequest(AbstractModel):
    """CreateMountPoint request structure.

    """

    def __init__(self):
        r"""
        :param _MountPointName: Mount point name
        :type MountPointName: str
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        :param _MountPointStatus: Mount point status (1: enabled; 2: disabled)
        :type MountPointStatus: int
        """
        self._MountPointName = None
        self._FileSystemId = None
        self._MountPointStatus = None

    @property
    def MountPointName(self):
        return self._MountPointName

    @MountPointName.setter
    def MountPointName(self, MountPointName):
        self._MountPointName = MountPointName

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def MountPointStatus(self):
        return self._MountPointStatus

    @MountPointStatus.setter
    def MountPointStatus(self, MountPointStatus):
        self._MountPointStatus = MountPointStatus


    def _deserialize(self, params):
        self._MountPointName = params.get("MountPointName")
        self._FileSystemId = params.get("FileSystemId")
        self._MountPointStatus = params.get("MountPointStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMountPointResponse(AbstractModel):
    """CreateMountPoint response structure.

    """

    def __init__(self):
        r"""
        :param _MountPoint: Mount point
        :type MountPoint: :class:`tencentcloud.chdfs.v20201112.models.MountPoint`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MountPoint = None
        self._RequestId = None

    @property
    def MountPoint(self):
        return self._MountPoint

    @MountPoint.setter
    def MountPoint(self, MountPoint):
        self._MountPoint = MountPoint

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MountPoint") is not None:
            self._MountPoint = MountPoint()
            self._MountPoint._deserialize(params.get("MountPoint"))
        self._RequestId = params.get("RequestId")


class CreateRestoreTasksRequest(AbstractModel):
    """CreateRestoreTasks request structure.

    """

    def __init__(self):
        r"""
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        :param _RestoreTasks: Multiple restoration tasks (up to 10)
        :type RestoreTasks: list of RestoreTask
        """
        self._FileSystemId = None
        self._RestoreTasks = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def RestoreTasks(self):
        return self._RestoreTasks

    @RestoreTasks.setter
    def RestoreTasks(self, RestoreTasks):
        self._RestoreTasks = RestoreTasks


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        if params.get("RestoreTasks") is not None:
            self._RestoreTasks = []
            for item in params.get("RestoreTasks"):
                obj = RestoreTask()
                obj._deserialize(item)
                self._RestoreTasks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRestoreTasksResponse(AbstractModel):
    """CreateRestoreTasks response structure.

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


class DeleteAccessGroupRequest(AbstractModel):
    """DeleteAccessGroup request structure.

    """

    def __init__(self):
        r"""
        :param _AccessGroupId: Permission group ID
        :type AccessGroupId: str
        """
        self._AccessGroupId = None

    @property
    def AccessGroupId(self):
        return self._AccessGroupId

    @AccessGroupId.setter
    def AccessGroupId(self, AccessGroupId):
        self._AccessGroupId = AccessGroupId


    def _deserialize(self, params):
        self._AccessGroupId = params.get("AccessGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccessGroupResponse(AbstractModel):
    """DeleteAccessGroup response structure.

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


class DeleteAccessRulesRequest(AbstractModel):
    """DeleteAccessRules request structure.

    """

    def __init__(self):
        r"""
        :param _AccessRuleIds: Multiple permission rule IDs (up to 10)
        :type AccessRuleIds: list of int non-negative
        """
        self._AccessRuleIds = None

    @property
    def AccessRuleIds(self):
        return self._AccessRuleIds

    @AccessRuleIds.setter
    def AccessRuleIds(self, AccessRuleIds):
        self._AccessRuleIds = AccessRuleIds


    def _deserialize(self, params):
        self._AccessRuleIds = params.get("AccessRuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccessRulesResponse(AbstractModel):
    """DeleteAccessRules response structure.

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


class DeleteFileSystemRequest(AbstractModel):
    """DeleteFileSystem request structure.

    """

    def __init__(self):
        r"""
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        """
        self._FileSystemId = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFileSystemResponse(AbstractModel):
    """DeleteFileSystem response structure.

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


class DeleteLifeCycleRulesRequest(AbstractModel):
    """DeleteLifeCycleRules request structure.

    """

    def __init__(self):
        r"""
        :param _LifeCycleRuleIds: Multiple lifecycle rule IDs (up to 10)
        :type LifeCycleRuleIds: list of int non-negative
        """
        self._LifeCycleRuleIds = None

    @property
    def LifeCycleRuleIds(self):
        return self._LifeCycleRuleIds

    @LifeCycleRuleIds.setter
    def LifeCycleRuleIds(self, LifeCycleRuleIds):
        self._LifeCycleRuleIds = LifeCycleRuleIds


    def _deserialize(self, params):
        self._LifeCycleRuleIds = params.get("LifeCycleRuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLifeCycleRulesResponse(AbstractModel):
    """DeleteLifeCycleRules response structure.

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


class DeleteMountPointRequest(AbstractModel):
    """DeleteMountPoint request structure.

    """

    def __init__(self):
        r"""
        :param _MountPointId: Mount point ID
        :type MountPointId: str
        """
        self._MountPointId = None

    @property
    def MountPointId(self):
        return self._MountPointId

    @MountPointId.setter
    def MountPointId(self, MountPointId):
        self._MountPointId = MountPointId


    def _deserialize(self, params):
        self._MountPointId = params.get("MountPointId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMountPointResponse(AbstractModel):
    """DeleteMountPoint response structure.

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


class DescribeAccessGroupRequest(AbstractModel):
    """DescribeAccessGroup request structure.

    """

    def __init__(self):
        r"""
        :param _AccessGroupId: Permission group ID
        :type AccessGroupId: str
        """
        self._AccessGroupId = None

    @property
    def AccessGroupId(self):
        return self._AccessGroupId

    @AccessGroupId.setter
    def AccessGroupId(self, AccessGroupId):
        self._AccessGroupId = AccessGroupId


    def _deserialize(self, params):
        self._AccessGroupId = params.get("AccessGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessGroupResponse(AbstractModel):
    """DescribeAccessGroup response structure.

    """

    def __init__(self):
        r"""
        :param _AccessGroup: Permission group
        :type AccessGroup: :class:`tencentcloud.chdfs.v20201112.models.AccessGroup`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AccessGroup = None
        self._RequestId = None

    @property
    def AccessGroup(self):
        return self._AccessGroup

    @AccessGroup.setter
    def AccessGroup(self, AccessGroup):
        self._AccessGroup = AccessGroup

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AccessGroup") is not None:
            self._AccessGroup = AccessGroup()
            self._AccessGroup._deserialize(params.get("AccessGroup"))
        self._RequestId = params.get("RequestId")


class DescribeAccessGroupsRequest(AbstractModel):
    """DescribeAccessGroups request structure.

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC ID
Note: either `VpcId` or `OwnerUin` can be specified as the input parameter
        :type VpcId: str
        :param _OwnerUin: Resource owner `Uin`
        :type OwnerUin: int
        """
        self._VpcId = None
        self._OwnerUin = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._OwnerUin = params.get("OwnerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessGroupsResponse(AbstractModel):
    """DescribeAccessGroups response structure.

    """

    def __init__(self):
        r"""
        :param _AccessGroups: List of permission groups
        :type AccessGroups: list of AccessGroup
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AccessGroups = None
        self._RequestId = None

    @property
    def AccessGroups(self):
        return self._AccessGroups

    @AccessGroups.setter
    def AccessGroups(self, AccessGroups):
        self._AccessGroups = AccessGroups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AccessGroups") is not None:
            self._AccessGroups = []
            for item in params.get("AccessGroups"):
                obj = AccessGroup()
                obj._deserialize(item)
                self._AccessGroups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAccessRulesRequest(AbstractModel):
    """DescribeAccessRules request structure.

    """

    def __init__(self):
        r"""
        :param _AccessGroupId: Permission group ID
        :type AccessGroupId: str
        """
        self._AccessGroupId = None

    @property
    def AccessGroupId(self):
        return self._AccessGroupId

    @AccessGroupId.setter
    def AccessGroupId(self, AccessGroupId):
        self._AccessGroupId = AccessGroupId


    def _deserialize(self, params):
        self._AccessGroupId = params.get("AccessGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessRulesResponse(AbstractModel):
    """DescribeAccessRules response structure.

    """

    def __init__(self):
        r"""
        :param _AccessRules: List of permission rules
        :type AccessRules: list of AccessRule
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AccessRules = None
        self._RequestId = None

    @property
    def AccessRules(self):
        return self._AccessRules

    @AccessRules.setter
    def AccessRules(self, AccessRules):
        self._AccessRules = AccessRules

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AccessRules") is not None:
            self._AccessRules = []
            for item in params.get("AccessRules"):
                obj = AccessRule()
                obj._deserialize(item)
                self._AccessRules.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFileSystemRequest(AbstractModel):
    """DescribeFileSystem request structure.

    """

    def __init__(self):
        r"""
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        """
        self._FileSystemId = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileSystemResponse(AbstractModel):
    """DescribeFileSystem response structure.

    """

    def __init__(self):
        r"""
        :param _FileSystem: File system
        :type FileSystem: :class:`tencentcloud.chdfs.v20201112.models.FileSystem`
        :param _CapacityUsed: Used capacity of the file system, in bytes
Note: this field may return `null`, indicating that no valid value was found.
        :type CapacityUsed: int
        :param _ArchiveCapacityUsed: Used ARCHIVE capacity of COS, in bytes
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ArchiveCapacityUsed: int
        :param _StandardCapacityUsed: Used STANDARD capacity of COS, in bytes
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type StandardCapacityUsed: int
        :param _DegradeCapacityUsed: Used STANDARD_IA capacity of COS, in bytes
Note: this field may return `null`, indicating that no valid value was found.
        :type DegradeCapacityUsed: int
        :param _DeepArchiveCapacityUsed: COS DEEP ARCHIVE storage usage, in bytes
Note: This field may return null, indicating that no valid values can be obtained.
        :type DeepArchiveCapacityUsed: int
        :param _IntelligentCapacityUsed: COS INTELLIGENT TIERING storage usage, in bytes
Note: This field may return null, indicating that no valid values can be obtained.
        :type IntelligentCapacityUsed: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FileSystem = None
        self._CapacityUsed = None
        self._ArchiveCapacityUsed = None
        self._StandardCapacityUsed = None
        self._DegradeCapacityUsed = None
        self._DeepArchiveCapacityUsed = None
        self._IntelligentCapacityUsed = None
        self._RequestId = None

    @property
    def FileSystem(self):
        return self._FileSystem

    @FileSystem.setter
    def FileSystem(self, FileSystem):
        self._FileSystem = FileSystem

    @property
    def CapacityUsed(self):
        return self._CapacityUsed

    @CapacityUsed.setter
    def CapacityUsed(self, CapacityUsed):
        self._CapacityUsed = CapacityUsed

    @property
    def ArchiveCapacityUsed(self):
        return self._ArchiveCapacityUsed

    @ArchiveCapacityUsed.setter
    def ArchiveCapacityUsed(self, ArchiveCapacityUsed):
        self._ArchiveCapacityUsed = ArchiveCapacityUsed

    @property
    def StandardCapacityUsed(self):
        return self._StandardCapacityUsed

    @StandardCapacityUsed.setter
    def StandardCapacityUsed(self, StandardCapacityUsed):
        self._StandardCapacityUsed = StandardCapacityUsed

    @property
    def DegradeCapacityUsed(self):
        return self._DegradeCapacityUsed

    @DegradeCapacityUsed.setter
    def DegradeCapacityUsed(self, DegradeCapacityUsed):
        self._DegradeCapacityUsed = DegradeCapacityUsed

    @property
    def DeepArchiveCapacityUsed(self):
        return self._DeepArchiveCapacityUsed

    @DeepArchiveCapacityUsed.setter
    def DeepArchiveCapacityUsed(self, DeepArchiveCapacityUsed):
        self._DeepArchiveCapacityUsed = DeepArchiveCapacityUsed

    @property
    def IntelligentCapacityUsed(self):
        return self._IntelligentCapacityUsed

    @IntelligentCapacityUsed.setter
    def IntelligentCapacityUsed(self, IntelligentCapacityUsed):
        self._IntelligentCapacityUsed = IntelligentCapacityUsed

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FileSystem") is not None:
            self._FileSystem = FileSystem()
            self._FileSystem._deserialize(params.get("FileSystem"))
        self._CapacityUsed = params.get("CapacityUsed")
        self._ArchiveCapacityUsed = params.get("ArchiveCapacityUsed")
        self._StandardCapacityUsed = params.get("StandardCapacityUsed")
        self._DegradeCapacityUsed = params.get("DegradeCapacityUsed")
        self._DeepArchiveCapacityUsed = params.get("DeepArchiveCapacityUsed")
        self._IntelligentCapacityUsed = params.get("IntelligentCapacityUsed")
        self._RequestId = params.get("RequestId")


class DescribeFileSystemsRequest(AbstractModel):
    """DescribeFileSystems request structure.

    """


class DescribeFileSystemsResponse(AbstractModel):
    """DescribeFileSystems response structure.

    """

    def __init__(self):
        r"""
        :param _FileSystems: List of file systems
        :type FileSystems: list of FileSystem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FileSystems = None
        self._RequestId = None

    @property
    def FileSystems(self):
        return self._FileSystems

    @FileSystems.setter
    def FileSystems(self, FileSystems):
        self._FileSystems = FileSystems

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FileSystems") is not None:
            self._FileSystems = []
            for item in params.get("FileSystems"):
                obj = FileSystem()
                obj._deserialize(item)
                self._FileSystems.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLifeCycleRulesRequest(AbstractModel):
    """DescribeLifeCycleRules request structure.

    """

    def __init__(self):
        r"""
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        """
        self._FileSystemId = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLifeCycleRulesResponse(AbstractModel):
    """DescribeLifeCycleRules response structure.

    """

    def __init__(self):
        r"""
        :param _LifeCycleRules: List of lifecycle rules
        :type LifeCycleRules: list of LifeCycleRule
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LifeCycleRules = None
        self._RequestId = None

    @property
    def LifeCycleRules(self):
        return self._LifeCycleRules

    @LifeCycleRules.setter
    def LifeCycleRules(self, LifeCycleRules):
        self._LifeCycleRules = LifeCycleRules

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LifeCycleRules") is not None:
            self._LifeCycleRules = []
            for item in params.get("LifeCycleRules"):
                obj = LifeCycleRule()
                obj._deserialize(item)
                self._LifeCycleRules.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMountPointRequest(AbstractModel):
    """DescribeMountPoint request structure.

    """

    def __init__(self):
        r"""
        :param _MountPointId: Mount point ID
        :type MountPointId: str
        """
        self._MountPointId = None

    @property
    def MountPointId(self):
        return self._MountPointId

    @MountPointId.setter
    def MountPointId(self, MountPointId):
        self._MountPointId = MountPointId


    def _deserialize(self, params):
        self._MountPointId = params.get("MountPointId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMountPointResponse(AbstractModel):
    """DescribeMountPoint response structure.

    """

    def __init__(self):
        r"""
        :param _MountPoint: Mount point
        :type MountPoint: :class:`tencentcloud.chdfs.v20201112.models.MountPoint`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MountPoint = None
        self._RequestId = None

    @property
    def MountPoint(self):
        return self._MountPoint

    @MountPoint.setter
    def MountPoint(self, MountPoint):
        self._MountPoint = MountPoint

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MountPoint") is not None:
            self._MountPoint = MountPoint()
            self._MountPoint._deserialize(params.get("MountPoint"))
        self._RequestId = params.get("RequestId")


class DescribeMountPointsRequest(AbstractModel):
    """DescribeMountPoints request structure.

    """

    def __init__(self):
        r"""
        :param _FileSystemId: File system ID
Note: only one of `AccessGroupId`, `FileSystemId`, and `OwnerUin` can be specified as the input parameter
        :type FileSystemId: str
        :param _AccessGroupId: Permission group ID
        :type AccessGroupId: str
        :param _OwnerUin: Resource owner `Uin`
        :type OwnerUin: int
        """
        self._FileSystemId = None
        self._AccessGroupId = None
        self._OwnerUin = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def AccessGroupId(self):
        return self._AccessGroupId

    @AccessGroupId.setter
    def AccessGroupId(self, AccessGroupId):
        self._AccessGroupId = AccessGroupId

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._AccessGroupId = params.get("AccessGroupId")
        self._OwnerUin = params.get("OwnerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMountPointsResponse(AbstractModel):
    """DescribeMountPoints response structure.

    """

    def __init__(self):
        r"""
        :param _MountPoints: List of mount points
        :type MountPoints: list of MountPoint
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MountPoints = None
        self._RequestId = None

    @property
    def MountPoints(self):
        return self._MountPoints

    @MountPoints.setter
    def MountPoints(self, MountPoints):
        self._MountPoints = MountPoints

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MountPoints") is not None:
            self._MountPoints = []
            for item in params.get("MountPoints"):
                obj = MountPoint()
                obj._deserialize(item)
                self._MountPoints.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourceTagsRequest(AbstractModel):
    """DescribeResourceTags request structure.

    """

    def __init__(self):
        r"""
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        """
        self._FileSystemId = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceTagsResponse(AbstractModel):
    """DescribeResourceTags response structure.

    """

    def __init__(self):
        r"""
        :param _Tags: List of resource tags
        :type Tags: list of Tag
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Tags = None
        self._RequestId = None

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRestoreTasksRequest(AbstractModel):
    """DescribeRestoreTasks request structure.

    """

    def __init__(self):
        r"""
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        """
        self._FileSystemId = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRestoreTasksResponse(AbstractModel):
    """DescribeRestoreTasks response structure.

    """

    def __init__(self):
        r"""
        :param _RestoreTasks: List of restoration tasks
        :type RestoreTasks: list of RestoreTask
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RestoreTasks = None
        self._RequestId = None

    @property
    def RestoreTasks(self):
        return self._RestoreTasks

    @RestoreTasks.setter
    def RestoreTasks(self, RestoreTasks):
        self._RestoreTasks = RestoreTasks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RestoreTasks") is not None:
            self._RestoreTasks = []
            for item in params.get("RestoreTasks"):
                obj = RestoreTask()
                obj._deserialize(item)
                self._RestoreTasks.append(obj)
        self._RequestId = params.get("RequestId")


class DisassociateAccessGroupsRequest(AbstractModel):
    """DisassociateAccessGroups request structure.

    """

    def __init__(self):
        r"""
        :param _MountPointId: Mount point ID
        :type MountPointId: str
        :param _AccessGroupIds: List of permission group IDs
        :type AccessGroupIds: list of str
        """
        self._MountPointId = None
        self._AccessGroupIds = None

    @property
    def MountPointId(self):
        return self._MountPointId

    @MountPointId.setter
    def MountPointId(self, MountPointId):
        self._MountPointId = MountPointId

    @property
    def AccessGroupIds(self):
        return self._AccessGroupIds

    @AccessGroupIds.setter
    def AccessGroupIds(self, AccessGroupIds):
        self._AccessGroupIds = AccessGroupIds


    def _deserialize(self, params):
        self._MountPointId = params.get("MountPointId")
        self._AccessGroupIds = params.get("AccessGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateAccessGroupsResponse(AbstractModel):
    """DisassociateAccessGroups response structure.

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


class FileSystem(AbstractModel):
    """File system

    """

    def __init__(self):
        r"""
        :param _AppId: Resource owner `AppId`
        :type AppId: int
        :param _FileSystemName: File system name
        :type FileSystemName: str
        :param _Description: File system description
        :type Description: str
        :param _Region: Region
        :type Region: str
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _BlockSize: File system block size (in bytes)
        :type BlockSize: int
        :param _CapacityQuota: File system capacity (in bytes)
        :type CapacityQuota: int
        :param _Status: File system status (1: creating; 2: created successfully; 3: failed to create)
        :type Status: int
        :param _SuperUsers: List of superuser names
        :type SuperUsers: list of str
        :param _PosixAcl: POSIX permission control
        :type PosixAcl: bool
        :param _EnableRanger: Whether to enable verification of Ranger service addresses
Note: this field may return `null`, indicating that no valid value was found.
        :type EnableRanger: bool
        :param _RangerServiceAddresses: List of Ranger service addresses
Note: this field may return `null`, indicating that no valid value was found.
        :type RangerServiceAddresses: list of str
        """
        self._AppId = None
        self._FileSystemName = None
        self._Description = None
        self._Region = None
        self._FileSystemId = None
        self._CreateTime = None
        self._BlockSize = None
        self._CapacityQuota = None
        self._Status = None
        self._SuperUsers = None
        self._PosixAcl = None
        self._EnableRanger = None
        self._RangerServiceAddresses = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def FileSystemName(self):
        return self._FileSystemName

    @FileSystemName.setter
    def FileSystemName(self, FileSystemName):
        self._FileSystemName = FileSystemName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def BlockSize(self):
        return self._BlockSize

    @BlockSize.setter
    def BlockSize(self, BlockSize):
        self._BlockSize = BlockSize

    @property
    def CapacityQuota(self):
        return self._CapacityQuota

    @CapacityQuota.setter
    def CapacityQuota(self, CapacityQuota):
        self._CapacityQuota = CapacityQuota

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SuperUsers(self):
        return self._SuperUsers

    @SuperUsers.setter
    def SuperUsers(self, SuperUsers):
        self._SuperUsers = SuperUsers

    @property
    def PosixAcl(self):
        return self._PosixAcl

    @PosixAcl.setter
    def PosixAcl(self, PosixAcl):
        self._PosixAcl = PosixAcl

    @property
    def EnableRanger(self):
        return self._EnableRanger

    @EnableRanger.setter
    def EnableRanger(self, EnableRanger):
        self._EnableRanger = EnableRanger

    @property
    def RangerServiceAddresses(self):
        return self._RangerServiceAddresses

    @RangerServiceAddresses.setter
    def RangerServiceAddresses(self, RangerServiceAddresses):
        self._RangerServiceAddresses = RangerServiceAddresses


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._FileSystemName = params.get("FileSystemName")
        self._Description = params.get("Description")
        self._Region = params.get("Region")
        self._FileSystemId = params.get("FileSystemId")
        self._CreateTime = params.get("CreateTime")
        self._BlockSize = params.get("BlockSize")
        self._CapacityQuota = params.get("CapacityQuota")
        self._Status = params.get("Status")
        self._SuperUsers = params.get("SuperUsers")
        self._PosixAcl = params.get("PosixAcl")
        self._EnableRanger = params.get("EnableRanger")
        self._RangerServiceAddresses = params.get("RangerServiceAddresses")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LifeCycleRule(AbstractModel):
    """Lifecycle rule

    """

    def __init__(self):
        r"""
        :param _LifeCycleRuleId: Lifecycle rule ID
        :type LifeCycleRuleId: int
        :param _LifeCycleRuleName: Lifecycle rule name
        :type LifeCycleRuleName: str
        :param _Path: Lifecycle rule path (directory or file)
        :type Path: str
        :param _Transitions: List of lifecycle rule transitions
        :type Transitions: list of Transition
        :param _Status: Lifecycle rule status (1: enabled; 2: disabled)
        :type Status: int
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _Summary: Detailed storage usage of the current lifecycle rule path
        :type Summary: :class:`tencentcloud.chdfs.v20201112.models.Summary`
        :param _LastSummaryTime: Update time of `Summary`
        :type LastSummaryTime: str
        """
        self._LifeCycleRuleId = None
        self._LifeCycleRuleName = None
        self._Path = None
        self._Transitions = None
        self._Status = None
        self._CreateTime = None
        self._Summary = None
        self._LastSummaryTime = None

    @property
    def LifeCycleRuleId(self):
        return self._LifeCycleRuleId

    @LifeCycleRuleId.setter
    def LifeCycleRuleId(self, LifeCycleRuleId):
        self._LifeCycleRuleId = LifeCycleRuleId

    @property
    def LifeCycleRuleName(self):
        return self._LifeCycleRuleName

    @LifeCycleRuleName.setter
    def LifeCycleRuleName(self, LifeCycleRuleName):
        self._LifeCycleRuleName = LifeCycleRuleName

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Transitions(self):
        return self._Transitions

    @Transitions.setter
    def Transitions(self, Transitions):
        self._Transitions = Transitions

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Summary(self):
        return self._Summary

    @Summary.setter
    def Summary(self, Summary):
        self._Summary = Summary

    @property
    def LastSummaryTime(self):
        return self._LastSummaryTime

    @LastSummaryTime.setter
    def LastSummaryTime(self, LastSummaryTime):
        self._LastSummaryTime = LastSummaryTime


    def _deserialize(self, params):
        self._LifeCycleRuleId = params.get("LifeCycleRuleId")
        self._LifeCycleRuleName = params.get("LifeCycleRuleName")
        self._Path = params.get("Path")
        if params.get("Transitions") is not None:
            self._Transitions = []
            for item in params.get("Transitions"):
                obj = Transition()
                obj._deserialize(item)
                self._Transitions.append(obj)
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        if params.get("Summary") is not None:
            self._Summary = Summary()
            self._Summary._deserialize(params.get("Summary"))
        self._LastSummaryTime = params.get("LastSummaryTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccessGroupRequest(AbstractModel):
    """ModifyAccessGroup request structure.

    """

    def __init__(self):
        r"""
        :param _AccessGroupId: Permission group ID
        :type AccessGroupId: str
        :param _AccessGroupName: Permission group name
        :type AccessGroupName: str
        :param _Description: Permission group description
        :type Description: str
        """
        self._AccessGroupId = None
        self._AccessGroupName = None
        self._Description = None

    @property
    def AccessGroupId(self):
        return self._AccessGroupId

    @AccessGroupId.setter
    def AccessGroupId(self, AccessGroupId):
        self._AccessGroupId = AccessGroupId

    @property
    def AccessGroupName(self):
        return self._AccessGroupName

    @AccessGroupName.setter
    def AccessGroupName(self, AccessGroupName):
        self._AccessGroupName = AccessGroupName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._AccessGroupId = params.get("AccessGroupId")
        self._AccessGroupName = params.get("AccessGroupName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccessGroupResponse(AbstractModel):
    """ModifyAccessGroup response structure.

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


class ModifyAccessRulesRequest(AbstractModel):
    """ModifyAccessRules request structure.

    """

    def __init__(self):
        r"""
        :param _AccessRules: Multiple permission rules (up to 10)
        :type AccessRules: list of AccessRule
        """
        self._AccessRules = None

    @property
    def AccessRules(self):
        return self._AccessRules

    @AccessRules.setter
    def AccessRules(self, AccessRules):
        self._AccessRules = AccessRules


    def _deserialize(self, params):
        if params.get("AccessRules") is not None:
            self._AccessRules = []
            for item in params.get("AccessRules"):
                obj = AccessRule()
                obj._deserialize(item)
                self._AccessRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccessRulesResponse(AbstractModel):
    """ModifyAccessRules response structure.

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


class ModifyFileSystemRequest(AbstractModel):
    """ModifyFileSystem request structure.

    """

    def __init__(self):
        r"""
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        :param _FileSystemName: File system name
        :type FileSystemName: str
        :param _Description: File system description
        :type Description: str
        :param _CapacityQuota: File system capacity (in bytes), which can range from 1 GB to 1 PB and must be an integer multiple of 1 GB
Note: the file system capacity after change cannot be smaller than the currently used capacity
        :type CapacityQuota: int
        :param _SuperUsers: List of superuser names, which can be an empty array
        :type SuperUsers: list of str
        :param _PosixAcl: Whether to verify POSIX ACL
        :type PosixAcl: bool
        :param _EnableRanger: Whether to enable verification of Ranger service addresses
        :type EnableRanger: bool
        :param _RangerServiceAddresses: List of Ranger service addresses, which can be an empty array
        :type RangerServiceAddresses: list of str
        """
        self._FileSystemId = None
        self._FileSystemName = None
        self._Description = None
        self._CapacityQuota = None
        self._SuperUsers = None
        self._PosixAcl = None
        self._EnableRanger = None
        self._RangerServiceAddresses = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def FileSystemName(self):
        return self._FileSystemName

    @FileSystemName.setter
    def FileSystemName(self, FileSystemName):
        self._FileSystemName = FileSystemName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CapacityQuota(self):
        return self._CapacityQuota

    @CapacityQuota.setter
    def CapacityQuota(self, CapacityQuota):
        self._CapacityQuota = CapacityQuota

    @property
    def SuperUsers(self):
        return self._SuperUsers

    @SuperUsers.setter
    def SuperUsers(self, SuperUsers):
        self._SuperUsers = SuperUsers

    @property
    def PosixAcl(self):
        return self._PosixAcl

    @PosixAcl.setter
    def PosixAcl(self, PosixAcl):
        self._PosixAcl = PosixAcl

    @property
    def EnableRanger(self):
        return self._EnableRanger

    @EnableRanger.setter
    def EnableRanger(self, EnableRanger):
        self._EnableRanger = EnableRanger

    @property
    def RangerServiceAddresses(self):
        return self._RangerServiceAddresses

    @RangerServiceAddresses.setter
    def RangerServiceAddresses(self, RangerServiceAddresses):
        self._RangerServiceAddresses = RangerServiceAddresses


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._FileSystemName = params.get("FileSystemName")
        self._Description = params.get("Description")
        self._CapacityQuota = params.get("CapacityQuota")
        self._SuperUsers = params.get("SuperUsers")
        self._PosixAcl = params.get("PosixAcl")
        self._EnableRanger = params.get("EnableRanger")
        self._RangerServiceAddresses = params.get("RangerServiceAddresses")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFileSystemResponse(AbstractModel):
    """ModifyFileSystem response structure.

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


class ModifyLifeCycleRulesRequest(AbstractModel):
    """ModifyLifeCycleRules request structure.

    """

    def __init__(self):
        r"""
        :param _LifeCycleRules: Multiple lifecycle rules (up to 10)
        :type LifeCycleRules: list of LifeCycleRule
        """
        self._LifeCycleRules = None

    @property
    def LifeCycleRules(self):
        return self._LifeCycleRules

    @LifeCycleRules.setter
    def LifeCycleRules(self, LifeCycleRules):
        self._LifeCycleRules = LifeCycleRules


    def _deserialize(self, params):
        if params.get("LifeCycleRules") is not None:
            self._LifeCycleRules = []
            for item in params.get("LifeCycleRules"):
                obj = LifeCycleRule()
                obj._deserialize(item)
                self._LifeCycleRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLifeCycleRulesResponse(AbstractModel):
    """ModifyLifeCycleRules response structure.

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


class ModifyMountPointRequest(AbstractModel):
    """ModifyMountPoint request structure.

    """

    def __init__(self):
        r"""
        :param _MountPointId: Mount point ID
        :type MountPointId: str
        :param _MountPointName: Mount point name
        :type MountPointName: str
        :param _MountPointStatus: Mount point status
        :type MountPointStatus: int
        """
        self._MountPointId = None
        self._MountPointName = None
        self._MountPointStatus = None

    @property
    def MountPointId(self):
        return self._MountPointId

    @MountPointId.setter
    def MountPointId(self, MountPointId):
        self._MountPointId = MountPointId

    @property
    def MountPointName(self):
        return self._MountPointName

    @MountPointName.setter
    def MountPointName(self, MountPointName):
        self._MountPointName = MountPointName

    @property
    def MountPointStatus(self):
        return self._MountPointStatus

    @MountPointStatus.setter
    def MountPointStatus(self, MountPointStatus):
        self._MountPointStatus = MountPointStatus


    def _deserialize(self, params):
        self._MountPointId = params.get("MountPointId")
        self._MountPointName = params.get("MountPointName")
        self._MountPointStatus = params.get("MountPointStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMountPointResponse(AbstractModel):
    """ModifyMountPoint response structure.

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


class ModifyResourceTagsRequest(AbstractModel):
    """ModifyResourceTags request structure.

    """

    def __init__(self):
        r"""
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        :param _Tags: Multiple resource tags, which can be an empty array
        :type Tags: list of Tag
        """
        self._FileSystemId = None
        self._Tags = None

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourceTagsResponse(AbstractModel):
    """ModifyResourceTags response structure.

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


class MountPoint(AbstractModel):
    """Mount point

    """

    def __init__(self):
        r"""
        :param _MountPointId: Mount point ID
        :type MountPointId: str
        :param _MountPointName: Mount point name
        :type MountPointName: str
        :param _FileSystemId: File system ID
        :type FileSystemId: str
        :param _Status: Mount point status (1: enabled; 2: disabled)
        :type Status: int
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _AccessGroupIds: List of IDs of the bound permission groups
        :type AccessGroupIds: list of str
        """
        self._MountPointId = None
        self._MountPointName = None
        self._FileSystemId = None
        self._Status = None
        self._CreateTime = None
        self._AccessGroupIds = None

    @property
    def MountPointId(self):
        return self._MountPointId

    @MountPointId.setter
    def MountPointId(self, MountPointId):
        self._MountPointId = MountPointId

    @property
    def MountPointName(self):
        return self._MountPointName

    @MountPointName.setter
    def MountPointName(self, MountPointName):
        self._MountPointName = MountPointName

    @property
    def FileSystemId(self):
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def AccessGroupIds(self):
        return self._AccessGroupIds

    @AccessGroupIds.setter
    def AccessGroupIds(self, AccessGroupIds):
        self._AccessGroupIds = AccessGroupIds


    def _deserialize(self, params):
        self._MountPointId = params.get("MountPointId")
        self._MountPointName = params.get("MountPointName")
        self._FileSystemId = params.get("FileSystemId")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._AccessGroupIds = params.get("AccessGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestoreTask(AbstractModel):
    """Restoration task

    """

    def __init__(self):
        r"""
        :param _RestoreTaskId: Restoration task ID
        :type RestoreTaskId: int
        :param _FilePath: Restoration task file path
        :type FilePath: str
        :param _Type: Restoration task type (`1`: standard; `2`: expedited; `3`: bulk, with only the expedited type available currently)
        :type Type: int
        :param _Days: Validity period (in days) of the temporary copy generated during restoration
        :type Days: int
        :param _Status: Restoration task status (1: binding file; 2: file binding completed; 3: restoring file; 4: file restoration completed)
        :type Status: int
        :param _CreateTime: Creation time
        :type CreateTime: str
        """
        self._RestoreTaskId = None
        self._FilePath = None
        self._Type = None
        self._Days = None
        self._Status = None
        self._CreateTime = None

    @property
    def RestoreTaskId(self):
        return self._RestoreTaskId

    @RestoreTaskId.setter
    def RestoreTaskId(self, RestoreTaskId):
        self._RestoreTaskId = RestoreTaskId

    @property
    def FilePath(self):
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Days(self):
        return self._Days

    @Days.setter
    def Days(self, Days):
        self._Days = Days

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._RestoreTaskId = params.get("RestoreTaskId")
        self._FilePath = params.get("FilePath")
        self._Type = params.get("Type")
        self._Days = params.get("Days")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Summary(AbstractModel):
    """Details about the storage usage of the current lifecycle rule path

    """

    def __init__(self):
        r"""
        :param _CapacityUsed: Capacity usage in bytes
Note: This field may return null, indicating that no valid values can be obtained.
        :type CapacityUsed: int
        :param _StandardCapacityUsed: COS STANDARD storage usage in bytes
Note: This field may return null, indicating that no valid values can be obtained.
        :type StandardCapacityUsed: int
        :param _DegradeCapacityUsed: COS STANDARD_IA storage usage in bytes
Note: This field may return null, indicating that no valid values can be obtained.
        :type DegradeCapacityUsed: int
        :param _ArchiveCapacityUsed: COS ARCHIVE storage usage in bytes
Note: This field may return null, indicating that no valid values can be obtained.
        :type ArchiveCapacityUsed: int
        :param _DeepArchiveCapacityUsed: COS DEEP ARCHIVE storage usage in bytes
Note: This field may return null, indicating that no valid values can be obtained.
        :type DeepArchiveCapacityUsed: int
        :param _IntelligentCapacityUsed: COS INTELLIGENT TIERING storage usage in bytes
Note: This field may return null, indicating that no valid values can be obtained.
        :type IntelligentCapacityUsed: int
        """
        self._CapacityUsed = None
        self._StandardCapacityUsed = None
        self._DegradeCapacityUsed = None
        self._ArchiveCapacityUsed = None
        self._DeepArchiveCapacityUsed = None
        self._IntelligentCapacityUsed = None

    @property
    def CapacityUsed(self):
        return self._CapacityUsed

    @CapacityUsed.setter
    def CapacityUsed(self, CapacityUsed):
        self._CapacityUsed = CapacityUsed

    @property
    def StandardCapacityUsed(self):
        return self._StandardCapacityUsed

    @StandardCapacityUsed.setter
    def StandardCapacityUsed(self, StandardCapacityUsed):
        self._StandardCapacityUsed = StandardCapacityUsed

    @property
    def DegradeCapacityUsed(self):
        return self._DegradeCapacityUsed

    @DegradeCapacityUsed.setter
    def DegradeCapacityUsed(self, DegradeCapacityUsed):
        self._DegradeCapacityUsed = DegradeCapacityUsed

    @property
    def ArchiveCapacityUsed(self):
        return self._ArchiveCapacityUsed

    @ArchiveCapacityUsed.setter
    def ArchiveCapacityUsed(self, ArchiveCapacityUsed):
        self._ArchiveCapacityUsed = ArchiveCapacityUsed

    @property
    def DeepArchiveCapacityUsed(self):
        return self._DeepArchiveCapacityUsed

    @DeepArchiveCapacityUsed.setter
    def DeepArchiveCapacityUsed(self, DeepArchiveCapacityUsed):
        self._DeepArchiveCapacityUsed = DeepArchiveCapacityUsed

    @property
    def IntelligentCapacityUsed(self):
        return self._IntelligentCapacityUsed

    @IntelligentCapacityUsed.setter
    def IntelligentCapacityUsed(self, IntelligentCapacityUsed):
        self._IntelligentCapacityUsed = IntelligentCapacityUsed


    def _deserialize(self, params):
        self._CapacityUsed = params.get("CapacityUsed")
        self._StandardCapacityUsed = params.get("StandardCapacityUsed")
        self._DegradeCapacityUsed = params.get("DegradeCapacityUsed")
        self._ArchiveCapacityUsed = params.get("ArchiveCapacityUsed")
        self._DeepArchiveCapacityUsed = params.get("DeepArchiveCapacityUsed")
        self._IntelligentCapacityUsed = params.get("IntelligentCapacityUsed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Resource tag.

    """

    def __init__(self):
        r"""
        :param _Key: Tag key
        :type Key: str
        :param _Value: Tag value
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
        


class Transition(AbstractModel):
    """Lifecycle rule transition attribute

    """

    def __init__(self):
        r"""
        :param _Days: Trigger time (in days)
        :type Days: int
        :param _Type: Transition type (`1`: ARCHIVE; `2`: Delete; `3`: STANDARD_IA; `4`: DEEP ARCHIVE; `5`: INTELLIGENT TIERING)
        :type Type: int
        """
        self._Days = None
        self._Type = None

    @property
    def Days(self):
        return self._Days

    @Days.setter
    def Days(self, Days):
        self._Days = Days

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Days = params.get("Days")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        