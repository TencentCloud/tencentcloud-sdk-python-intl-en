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
        :param AccessGroupId: Permission group ID
        :type AccessGroupId: str
        :param AccessGroupName: Permission group name
        :type AccessGroupName: str
        :param Description: Permission group description
        :type Description: str
        :param CreateTime: Creation time
        :type CreateTime: str
        :param VpcType: VPC type (1: CVM; 2: BM 1.0)
        :type VpcType: int
        :param VpcId: VPC ID
        :type VpcId: str
        """
        self.AccessGroupId = None
        self.AccessGroupName = None
        self.Description = None
        self.CreateTime = None
        self.VpcType = None
        self.VpcId = None


    def _deserialize(self, params):
        self.AccessGroupId = params.get("AccessGroupId")
        self.AccessGroupName = params.get("AccessGroupName")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.VpcType = params.get("VpcType")
        self.VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessRule(AbstractModel):
    """Permission rule

    """

    def __init__(self):
        r"""
        :param AccessRuleId: Permission rule ID
        :type AccessRuleId: int
        :param Address: Permission rule address (IP range or IP)
        :type Address: str
        :param AccessMode: Permission rule access mode (1: read-only; 2: read-write)
        :type AccessMode: int
        :param Priority: Priority (value range: 1–100. The smaller the value, the higher the priority)
        :type Priority: int
        :param CreateTime: Creation time
        :type CreateTime: str
        """
        self.AccessRuleId = None
        self.Address = None
        self.AccessMode = None
        self.Priority = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.AccessRuleId = params.get("AccessRuleId")
        self.Address = params.get("Address")
        self.AccessMode = params.get("AccessMode")
        self.Priority = params.get("Priority")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateAccessGroupsRequest(AbstractModel):
    """AssociateAccessGroups request structure.

    """

    def __init__(self):
        r"""
        :param MountPointId: Mount point ID
        :type MountPointId: str
        :param AccessGroupIds: List of permission group IDs
        :type AccessGroupIds: list of str
        """
        self.MountPointId = None
        self.AccessGroupIds = None


    def _deserialize(self, params):
        self.MountPointId = params.get("MountPointId")
        self.AccessGroupIds = params.get("AccessGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateAccessGroupsResponse(AbstractModel):
    """AssociateAccessGroups response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAccessGroupRequest(AbstractModel):
    """CreateAccessGroup request structure.

    """

    def __init__(self):
        r"""
        :param AccessGroupName: Permission group name
        :type AccessGroupName: str
        :param VpcType: VPC type (1: CVM; 2: BM 1.0)
        :type VpcType: int
        :param VpcId: VPC ID
        :type VpcId: str
        :param Description: Permission group description, which is an empty string by default
        :type Description: str
        """
        self.AccessGroupName = None
        self.VpcType = None
        self.VpcId = None
        self.Description = None


    def _deserialize(self, params):
        self.AccessGroupName = params.get("AccessGroupName")
        self.VpcType = params.get("VpcType")
        self.VpcId = params.get("VpcId")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccessGroupResponse(AbstractModel):
    """CreateAccessGroup response structure.

    """

    def __init__(self):
        r"""
        :param AccessGroup: Permission group
        :type AccessGroup: :class:`tencentcloud.chdfs.v20201112.models.AccessGroup`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AccessGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccessGroup") is not None:
            self.AccessGroup = AccessGroup()
            self.AccessGroup._deserialize(params.get("AccessGroup"))
        self.RequestId = params.get("RequestId")


class CreateAccessRulesRequest(AbstractModel):
    """CreateAccessRules request structure.

    """

    def __init__(self):
        r"""
        :param AccessRules: Multiple permission rules (up to 10)
        :type AccessRules: list of AccessRule
        :param AccessGroupId: Permission group ID
        :type AccessGroupId: str
        """
        self.AccessRules = None
        self.AccessGroupId = None


    def _deserialize(self, params):
        if params.get("AccessRules") is not None:
            self.AccessRules = []
            for item in params.get("AccessRules"):
                obj = AccessRule()
                obj._deserialize(item)
                self.AccessRules.append(obj)
        self.AccessGroupId = params.get("AccessGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccessRulesResponse(AbstractModel):
    """CreateAccessRules response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateFileSystemRequest(AbstractModel):
    """CreateFileSystem request structure.

    """

    def __init__(self):
        r"""
        :param FileSystemName: File system name
        :type FileSystemName: str
        :param CapacityQuota: File system capacity (in bytes), which can range from 1 GB to 1 PB and must be an integer multiple of 1 GB
        :type CapacityQuota: int
        :param PosixAcl: Whether to verify POSIX ACL
        :type PosixAcl: bool
        :param Description: File system description, which is an empty string by default
        :type Description: str
        :param SuperUsers: List of superuser names, which is an empty array by default
        :type SuperUsers: list of str
        :param RootInodeUser: Username of the root directory Inode, which is `hadoop` by default
        :type RootInodeUser: str
        :param RootInodeGroup: Group name of the root directory Inode, which is `supergroup` by default
        :type RootInodeGroup: str
        """
        self.FileSystemName = None
        self.CapacityQuota = None
        self.PosixAcl = None
        self.Description = None
        self.SuperUsers = None
        self.RootInodeUser = None
        self.RootInodeGroup = None


    def _deserialize(self, params):
        self.FileSystemName = params.get("FileSystemName")
        self.CapacityQuota = params.get("CapacityQuota")
        self.PosixAcl = params.get("PosixAcl")
        self.Description = params.get("Description")
        self.SuperUsers = params.get("SuperUsers")
        self.RootInodeUser = params.get("RootInodeUser")
        self.RootInodeGroup = params.get("RootInodeGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFileSystemResponse(AbstractModel):
    """CreateFileSystem response structure.

    """

    def __init__(self):
        r"""
        :param FileSystem: File system
        :type FileSystem: :class:`tencentcloud.chdfs.v20201112.models.FileSystem`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FileSystem = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FileSystem") is not None:
            self.FileSystem = FileSystem()
            self.FileSystem._deserialize(params.get("FileSystem"))
        self.RequestId = params.get("RequestId")


class CreateLifeCycleRulesRequest(AbstractModel):
    """CreateLifeCycleRules request structure.

    """

    def __init__(self):
        r"""
        :param FileSystemId: File system ID
        :type FileSystemId: str
        :param LifeCycleRules: Multiple lifecycle rules (up to 10)
        :type LifeCycleRules: list of LifeCycleRule
        """
        self.FileSystemId = None
        self.LifeCycleRules = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        if params.get("LifeCycleRules") is not None:
            self.LifeCycleRules = []
            for item in params.get("LifeCycleRules"):
                obj = LifeCycleRule()
                obj._deserialize(item)
                self.LifeCycleRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLifeCycleRulesResponse(AbstractModel):
    """CreateLifeCycleRules response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateMountPointRequest(AbstractModel):
    """CreateMountPoint request structure.

    """

    def __init__(self):
        r"""
        :param MountPointName: Mount point name
        :type MountPointName: str
        :param FileSystemId: File system ID
        :type FileSystemId: str
        :param MountPointStatus: Mount point status (1: enabled; 2: disabled)
        :type MountPointStatus: int
        """
        self.MountPointName = None
        self.FileSystemId = None
        self.MountPointStatus = None


    def _deserialize(self, params):
        self.MountPointName = params.get("MountPointName")
        self.FileSystemId = params.get("FileSystemId")
        self.MountPointStatus = params.get("MountPointStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMountPointResponse(AbstractModel):
    """CreateMountPoint response structure.

    """

    def __init__(self):
        r"""
        :param MountPoint: Mount point
        :type MountPoint: :class:`tencentcloud.chdfs.v20201112.models.MountPoint`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MountPoint = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MountPoint") is not None:
            self.MountPoint = MountPoint()
            self.MountPoint._deserialize(params.get("MountPoint"))
        self.RequestId = params.get("RequestId")


class CreateRestoreTasksRequest(AbstractModel):
    """CreateRestoreTasks request structure.

    """

    def __init__(self):
        r"""
        :param FileSystemId: File system ID
        :type FileSystemId: str
        :param RestoreTasks: Multiple restoration tasks (up to 10)
        :type RestoreTasks: list of RestoreTask
        """
        self.FileSystemId = None
        self.RestoreTasks = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        if params.get("RestoreTasks") is not None:
            self.RestoreTasks = []
            for item in params.get("RestoreTasks"):
                obj = RestoreTask()
                obj._deserialize(item)
                self.RestoreTasks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRestoreTasksResponse(AbstractModel):
    """CreateRestoreTasks response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAccessGroupRequest(AbstractModel):
    """DeleteAccessGroup request structure.

    """

    def __init__(self):
        r"""
        :param AccessGroupId: Permission group ID
        :type AccessGroupId: str
        """
        self.AccessGroupId = None


    def _deserialize(self, params):
        self.AccessGroupId = params.get("AccessGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccessGroupResponse(AbstractModel):
    """DeleteAccessGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAccessRulesRequest(AbstractModel):
    """DeleteAccessRules request structure.

    """

    def __init__(self):
        r"""
        :param AccessRuleIds: Multiple permission rule IDs (up to 10)
        :type AccessRuleIds: list of int non-negative
        """
        self.AccessRuleIds = None


    def _deserialize(self, params):
        self.AccessRuleIds = params.get("AccessRuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccessRulesResponse(AbstractModel):
    """DeleteAccessRules response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteFileSystemRequest(AbstractModel):
    """DeleteFileSystem request structure.

    """

    def __init__(self):
        r"""
        :param FileSystemId: File system ID
        :type FileSystemId: str
        """
        self.FileSystemId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFileSystemResponse(AbstractModel):
    """DeleteFileSystem response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLifeCycleRulesRequest(AbstractModel):
    """DeleteLifeCycleRules request structure.

    """

    def __init__(self):
        r"""
        :param LifeCycleRuleIds: Multiple lifecycle rule IDs (up to 10)
        :type LifeCycleRuleIds: list of int non-negative
        """
        self.LifeCycleRuleIds = None


    def _deserialize(self, params):
        self.LifeCycleRuleIds = params.get("LifeCycleRuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLifeCycleRulesResponse(AbstractModel):
    """DeleteLifeCycleRules response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMountPointRequest(AbstractModel):
    """DeleteMountPoint request structure.

    """

    def __init__(self):
        r"""
        :param MountPointId: Mount point ID
        :type MountPointId: str
        """
        self.MountPointId = None


    def _deserialize(self, params):
        self.MountPointId = params.get("MountPointId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMountPointResponse(AbstractModel):
    """DeleteMountPoint response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccessGroupRequest(AbstractModel):
    """DescribeAccessGroup request structure.

    """

    def __init__(self):
        r"""
        :param AccessGroupId: Permission group ID
        :type AccessGroupId: str
        """
        self.AccessGroupId = None


    def _deserialize(self, params):
        self.AccessGroupId = params.get("AccessGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessGroupResponse(AbstractModel):
    """DescribeAccessGroup response structure.

    """

    def __init__(self):
        r"""
        :param AccessGroup: Permission group
        :type AccessGroup: :class:`tencentcloud.chdfs.v20201112.models.AccessGroup`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AccessGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccessGroup") is not None:
            self.AccessGroup = AccessGroup()
            self.AccessGroup._deserialize(params.get("AccessGroup"))
        self.RequestId = params.get("RequestId")


class DescribeAccessGroupsRequest(AbstractModel):
    """DescribeAccessGroups request structure.

    """

    def __init__(self):
        r"""
        :param VpcId: VPC ID
Note: either `VpcId` or `OwnerUin` can be specified as the input parameter
        :type VpcId: str
        :param OwnerUin: Resource owner `Uin`
        :type OwnerUin: int
        """
        self.VpcId = None
        self.OwnerUin = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.OwnerUin = params.get("OwnerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessGroupsResponse(AbstractModel):
    """DescribeAccessGroups response structure.

    """

    def __init__(self):
        r"""
        :param AccessGroups: List of permission groups
        :type AccessGroups: list of AccessGroup
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AccessGroups = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccessGroups") is not None:
            self.AccessGroups = []
            for item in params.get("AccessGroups"):
                obj = AccessGroup()
                obj._deserialize(item)
                self.AccessGroups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAccessRulesRequest(AbstractModel):
    """DescribeAccessRules request structure.

    """

    def __init__(self):
        r"""
        :param AccessGroupId: Permission group ID
        :type AccessGroupId: str
        """
        self.AccessGroupId = None


    def _deserialize(self, params):
        self.AccessGroupId = params.get("AccessGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessRulesResponse(AbstractModel):
    """DescribeAccessRules response structure.

    """

    def __init__(self):
        r"""
        :param AccessRules: List of permission rules
        :type AccessRules: list of AccessRule
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AccessRules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccessRules") is not None:
            self.AccessRules = []
            for item in params.get("AccessRules"):
                obj = AccessRule()
                obj._deserialize(item)
                self.AccessRules.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFileSystemRequest(AbstractModel):
    """DescribeFileSystem request structure.

    """

    def __init__(self):
        r"""
        :param FileSystemId: File system ID
        :type FileSystemId: str
        """
        self.FileSystemId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileSystemResponse(AbstractModel):
    """DescribeFileSystem response structure.

    """

    def __init__(self):
        r"""
        :param FileSystem: File system
        :type FileSystem: :class:`tencentcloud.chdfs.v20201112.models.FileSystem`
        :param CapacityUsed: Used capacity (in bytes), including STANDARD storage and ARCHIVE storage
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CapacityUsed: int
        :param ArchiveCapacityUsed: Used ARCHIVE storage capacity (in bytes)
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ArchiveCapacityUsed: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FileSystem = None
        self.CapacityUsed = None
        self.ArchiveCapacityUsed = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FileSystem") is not None:
            self.FileSystem = FileSystem()
            self.FileSystem._deserialize(params.get("FileSystem"))
        self.CapacityUsed = params.get("CapacityUsed")
        self.ArchiveCapacityUsed = params.get("ArchiveCapacityUsed")
        self.RequestId = params.get("RequestId")


class DescribeFileSystemsRequest(AbstractModel):
    """DescribeFileSystems request structure.

    """


class DescribeFileSystemsResponse(AbstractModel):
    """DescribeFileSystems response structure.

    """

    def __init__(self):
        r"""
        :param FileSystems: List of file systems
        :type FileSystems: list of FileSystem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FileSystems = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FileSystems") is not None:
            self.FileSystems = []
            for item in params.get("FileSystems"):
                obj = FileSystem()
                obj._deserialize(item)
                self.FileSystems.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLifeCycleRulesRequest(AbstractModel):
    """DescribeLifeCycleRules request structure.

    """

    def __init__(self):
        r"""
        :param FileSystemId: File system ID
        :type FileSystemId: str
        """
        self.FileSystemId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLifeCycleRulesResponse(AbstractModel):
    """DescribeLifeCycleRules response structure.

    """

    def __init__(self):
        r"""
        :param LifeCycleRules: List of lifecycle rules
        :type LifeCycleRules: list of LifeCycleRule
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LifeCycleRules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LifeCycleRules") is not None:
            self.LifeCycleRules = []
            for item in params.get("LifeCycleRules"):
                obj = LifeCycleRule()
                obj._deserialize(item)
                self.LifeCycleRules.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMountPointRequest(AbstractModel):
    """DescribeMountPoint request structure.

    """

    def __init__(self):
        r"""
        :param MountPointId: Mount point ID
        :type MountPointId: str
        """
        self.MountPointId = None


    def _deserialize(self, params):
        self.MountPointId = params.get("MountPointId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMountPointResponse(AbstractModel):
    """DescribeMountPoint response structure.

    """

    def __init__(self):
        r"""
        :param MountPoint: Mount point
        :type MountPoint: :class:`tencentcloud.chdfs.v20201112.models.MountPoint`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MountPoint = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MountPoint") is not None:
            self.MountPoint = MountPoint()
            self.MountPoint._deserialize(params.get("MountPoint"))
        self.RequestId = params.get("RequestId")


class DescribeMountPointsRequest(AbstractModel):
    """DescribeMountPoints request structure.

    """

    def __init__(self):
        r"""
        :param FileSystemId: File system ID
Note: only one of `AccessGroupId`, `FileSystemId`, and `OwnerUin` can be specified as the input parameter
        :type FileSystemId: str
        :param AccessGroupId: Permission group ID
        :type AccessGroupId: str
        :param OwnerUin: Resource owner `Uin`
        :type OwnerUin: int
        """
        self.FileSystemId = None
        self.AccessGroupId = None
        self.OwnerUin = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        self.AccessGroupId = params.get("AccessGroupId")
        self.OwnerUin = params.get("OwnerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMountPointsResponse(AbstractModel):
    """DescribeMountPoints response structure.

    """

    def __init__(self):
        r"""
        :param MountPoints: List of mount points
        :type MountPoints: list of MountPoint
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MountPoints = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MountPoints") is not None:
            self.MountPoints = []
            for item in params.get("MountPoints"):
                obj = MountPoint()
                obj._deserialize(item)
                self.MountPoints.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResourceTagsRequest(AbstractModel):
    """DescribeResourceTags request structure.

    """

    def __init__(self):
        r"""
        :param FileSystemId: File system ID
        :type FileSystemId: str
        """
        self.FileSystemId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceTagsResponse(AbstractModel):
    """DescribeResourceTags response structure.

    """

    def __init__(self):
        r"""
        :param Tags: List of resource tags
        :type Tags: list of Tag
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRestoreTasksRequest(AbstractModel):
    """DescribeRestoreTasks request structure.

    """

    def __init__(self):
        r"""
        :param FileSystemId: File system ID
        :type FileSystemId: str
        """
        self.FileSystemId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRestoreTasksResponse(AbstractModel):
    """DescribeRestoreTasks response structure.

    """

    def __init__(self):
        r"""
        :param RestoreTasks: List of restoration tasks
        :type RestoreTasks: list of RestoreTask
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RestoreTasks = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RestoreTasks") is not None:
            self.RestoreTasks = []
            for item in params.get("RestoreTasks"):
                obj = RestoreTask()
                obj._deserialize(item)
                self.RestoreTasks.append(obj)
        self.RequestId = params.get("RequestId")


class DisassociateAccessGroupsRequest(AbstractModel):
    """DisassociateAccessGroups request structure.

    """

    def __init__(self):
        r"""
        :param MountPointId: Mount point ID
        :type MountPointId: str
        :param AccessGroupIds: List of permission group IDs
        :type AccessGroupIds: list of str
        """
        self.MountPointId = None
        self.AccessGroupIds = None


    def _deserialize(self, params):
        self.MountPointId = params.get("MountPointId")
        self.AccessGroupIds = params.get("AccessGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateAccessGroupsResponse(AbstractModel):
    """DisassociateAccessGroups response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class FileSystem(AbstractModel):
    """File system

    """

    def __init__(self):
        r"""
        :param AppId: Resource owner `AppId`
        :type AppId: int
        :param FileSystemName: File system name
        :type FileSystemName: str
        :param Description: File system description
        :type Description: str
        :param Region: Region
        :type Region: str
        :param FileSystemId: File system ID
        :type FileSystemId: str
        :param CreateTime: Creation time
        :type CreateTime: str
        :param BlockSize: File system block size (in bytes)
        :type BlockSize: int
        :param CapacityQuota: File system capacity (in bytes)
        :type CapacityQuota: int
        :param Status: File system status (1: creating; 2: created successfully; 3: failed to create)
        :type Status: int
        :param SuperUsers: List of superuser names
        :type SuperUsers: list of str
        :param PosixAcl: POSIX permission control
        :type PosixAcl: bool
        """
        self.AppId = None
        self.FileSystemName = None
        self.Description = None
        self.Region = None
        self.FileSystemId = None
        self.CreateTime = None
        self.BlockSize = None
        self.CapacityQuota = None
        self.Status = None
        self.SuperUsers = None
        self.PosixAcl = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.FileSystemName = params.get("FileSystemName")
        self.Description = params.get("Description")
        self.Region = params.get("Region")
        self.FileSystemId = params.get("FileSystemId")
        self.CreateTime = params.get("CreateTime")
        self.BlockSize = params.get("BlockSize")
        self.CapacityQuota = params.get("CapacityQuota")
        self.Status = params.get("Status")
        self.SuperUsers = params.get("SuperUsers")
        self.PosixAcl = params.get("PosixAcl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LifeCycleRule(AbstractModel):
    """Lifecycle rule

    """

    def __init__(self):
        r"""
        :param LifeCycleRuleId: Lifecycle rule ID
        :type LifeCycleRuleId: int
        :param LifeCycleRuleName: Lifecycle rule name
        :type LifeCycleRuleName: str
        :param Path: Lifecycle rule path (directory or file)
        :type Path: str
        :param Transitions: List of lifecycle rule transitions
        :type Transitions: list of Transition
        :param Status: Lifecycle rule status (1: enabled; 2: disabled)
        :type Status: int
        :param CreateTime: Creation time
        :type CreateTime: str
        """
        self.LifeCycleRuleId = None
        self.LifeCycleRuleName = None
        self.Path = None
        self.Transitions = None
        self.Status = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.LifeCycleRuleId = params.get("LifeCycleRuleId")
        self.LifeCycleRuleName = params.get("LifeCycleRuleName")
        self.Path = params.get("Path")
        if params.get("Transitions") is not None:
            self.Transitions = []
            for item in params.get("Transitions"):
                obj = Transition()
                obj._deserialize(item)
                self.Transitions.append(obj)
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccessGroupRequest(AbstractModel):
    """ModifyAccessGroup request structure.

    """

    def __init__(self):
        r"""
        :param AccessGroupId: Permission group ID
        :type AccessGroupId: str
        :param AccessGroupName: Permission group name
        :type AccessGroupName: str
        :param Description: Permission group description
        :type Description: str
        """
        self.AccessGroupId = None
        self.AccessGroupName = None
        self.Description = None


    def _deserialize(self, params):
        self.AccessGroupId = params.get("AccessGroupId")
        self.AccessGroupName = params.get("AccessGroupName")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccessGroupResponse(AbstractModel):
    """ModifyAccessGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAccessRulesRequest(AbstractModel):
    """ModifyAccessRules request structure.

    """

    def __init__(self):
        r"""
        :param AccessRules: Multiple permission rules (up to 10)
        :type AccessRules: list of AccessRule
        """
        self.AccessRules = None


    def _deserialize(self, params):
        if params.get("AccessRules") is not None:
            self.AccessRules = []
            for item in params.get("AccessRules"):
                obj = AccessRule()
                obj._deserialize(item)
                self.AccessRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccessRulesResponse(AbstractModel):
    """ModifyAccessRules response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyFileSystemRequest(AbstractModel):
    """ModifyFileSystem request structure.

    """

    def __init__(self):
        r"""
        :param FileSystemId: File system ID
        :type FileSystemId: str
        :param FileSystemName: File system name
        :type FileSystemName: str
        :param Description: File system description
        :type Description: str
        :param CapacityQuota: File system capacity (in bytes), which can range from 1 GB to 1 PB and must be an integer multiple of 1 GB
Note: the file system capacity after change cannot be smaller than the currently used capacity
        :type CapacityQuota: int
        :param SuperUsers: List of superuser names, which can be an empty array
        :type SuperUsers: list of str
        :param PosixAcl: Whether to verify POSIX ACL
        :type PosixAcl: bool
        """
        self.FileSystemId = None
        self.FileSystemName = None
        self.Description = None
        self.CapacityQuota = None
        self.SuperUsers = None
        self.PosixAcl = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        self.FileSystemName = params.get("FileSystemName")
        self.Description = params.get("Description")
        self.CapacityQuota = params.get("CapacityQuota")
        self.SuperUsers = params.get("SuperUsers")
        self.PosixAcl = params.get("PosixAcl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFileSystemResponse(AbstractModel):
    """ModifyFileSystem response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLifeCycleRulesRequest(AbstractModel):
    """ModifyLifeCycleRules request structure.

    """

    def __init__(self):
        r"""
        :param LifeCycleRules: Multiple lifecycle rules (up to 10)
        :type LifeCycleRules: list of LifeCycleRule
        """
        self.LifeCycleRules = None


    def _deserialize(self, params):
        if params.get("LifeCycleRules") is not None:
            self.LifeCycleRules = []
            for item in params.get("LifeCycleRules"):
                obj = LifeCycleRule()
                obj._deserialize(item)
                self.LifeCycleRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLifeCycleRulesResponse(AbstractModel):
    """ModifyLifeCycleRules response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMountPointRequest(AbstractModel):
    """ModifyMountPoint request structure.

    """

    def __init__(self):
        r"""
        :param MountPointId: Mount point ID
        :type MountPointId: str
        :param MountPointName: Mount point name
        :type MountPointName: str
        :param MountPointStatus: Mount point status
        :type MountPointStatus: int
        """
        self.MountPointId = None
        self.MountPointName = None
        self.MountPointStatus = None


    def _deserialize(self, params):
        self.MountPointId = params.get("MountPointId")
        self.MountPointName = params.get("MountPointName")
        self.MountPointStatus = params.get("MountPointStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMountPointResponse(AbstractModel):
    """ModifyMountPoint response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyResourceTagsRequest(AbstractModel):
    """ModifyResourceTags request structure.

    """

    def __init__(self):
        r"""
        :param FileSystemId: File system ID
        :type FileSystemId: str
        :param Tags: Multiple resource tags, which can be an empty array
        :type Tags: list of Tag
        """
        self.FileSystemId = None
        self.Tags = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourceTagsResponse(AbstractModel):
    """ModifyResourceTags response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MountPoint(AbstractModel):
    """Mount point

    """

    def __init__(self):
        r"""
        :param MountPointId: Mount point ID
        :type MountPointId: str
        :param MountPointName: Mount point name
        :type MountPointName: str
        :param FileSystemId: File system ID
        :type FileSystemId: str
        :param Status: Mount point status (1: enabled; 2: disabled)
        :type Status: int
        :param CreateTime: Creation time
        :type CreateTime: str
        :param AccessGroupIds: List of IDs of the bound permission groups
        :type AccessGroupIds: list of str
        """
        self.MountPointId = None
        self.MountPointName = None
        self.FileSystemId = None
        self.Status = None
        self.CreateTime = None
        self.AccessGroupIds = None


    def _deserialize(self, params):
        self.MountPointId = params.get("MountPointId")
        self.MountPointName = params.get("MountPointName")
        self.FileSystemId = params.get("FileSystemId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.AccessGroupIds = params.get("AccessGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestoreTask(AbstractModel):
    """Restoration task

    """

    def __init__(self):
        r"""
        :param RestoreTaskId: Restoration task ID
        :type RestoreTaskId: int
        :param FilePath: Restoration task file path
        :type FilePath: str
        :param Type: Restoration task type (1: standard; 2: expedited; 3: bulk)
        :type Type: int
        :param Days: Validity period (in days) of the temporary copy generated during restoration
        :type Days: int
        :param Status: Restoration task status (1: binding file; 2: file binding completed; 3: restoring file; 4: file restoration completed)
        :type Status: int
        :param CreateTime: Creation time
        :type CreateTime: str
        """
        self.RestoreTaskId = None
        self.FilePath = None
        self.Type = None
        self.Days = None
        self.Status = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.RestoreTaskId = params.get("RestoreTaskId")
        self.FilePath = params.get("FilePath")
        self.Type = params.get("Type")
        self.Days = params.get("Days")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Resource tag.

    """

    def __init__(self):
        r"""
        :param Key: Tag key
        :type Key: str
        :param Value: Tag value
        :type Value: str
        """
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
        


class Transition(AbstractModel):
    """Lifecycle rule transition attribute

    """

    def __init__(self):
        r"""
        :param Days: Trigger time (in days)
        :type Days: int
        :param Type: Transition type (1: archive; 2: deletion)
        :type Type: int
        """
        self.Days = None
        self.Type = None


    def _deserialize(self, params):
        self.Days = params.get("Days")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        