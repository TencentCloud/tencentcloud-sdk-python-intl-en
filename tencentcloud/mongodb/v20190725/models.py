# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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


class AddNodeList(AbstractModel):
    r"""Node details of the instance to be modified.

    """

    def __init__(self):
        r"""
        :param _Role: Roles of nodes to be added.
 - SECONDARY: Mongod node.
 - READONLY: read-only node.
 - MONGOS: Mongos node.
        :type Role: str
        :param _Zone: AZ corresponding to the node. For the currently supported AZs, see [Regions and AZs](https://www.tencentcloud.comom/document/product/240/3637?from_cn_redirect=1).
- Single AZ: All nodes are in the same AZ.
- Multiple AZs: The current standard specification involves three AZs. The primary and secondary nodes are not in the same AZ. Note: AZs corresponding to the nodes to be added should be specified. After addition, the number of nodes in any 2 AZs should be greater than that in the third AZ.
        :type Zone: str
        """
        self._Role = None
        self._Zone = None

    @property
    def Role(self):
        r"""Roles of nodes to be added.
 - SECONDARY: Mongod node.
 - READONLY: read-only node.
 - MONGOS: Mongos node.
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Zone(self):
        r"""AZ corresponding to the node. For the currently supported AZs, see [Regions and AZs](https://www.tencentcloud.comom/document/product/240/3637?from_cn_redirect=1).
- Single AZ: All nodes are in the same AZ.
- Multiple AZs: The current standard specification involves three AZs. The primary and secondary nodes are not in the same AZ. Note: AZs corresponding to the nodes to be added should be specified. After addition, the number of nodes in any 2 AZs should be greater than that in the third AZ.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignProjectRequest(AbstractModel):
    r"""AssignProject request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID list. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/MongoDB) and copy the instance ID from the instance list.
        :type InstanceIds: list of str
        :param _ProjectId: Project ID, the unique ID of the project created by the user. Go to the [project management](https://console.cloud.tencent.com/project) area of the account center in the console to copy the project ID.
        :type ProjectId: int
        """
        self._InstanceIds = None
        self._ProjectId = None

    @property
    def InstanceIds(self):
        r"""Instance ID list. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/MongoDB) and copy the instance ID from the instance list.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ProjectId(self):
        r"""Project ID, the unique ID of the project created by the user. Go to the [project management](https://console.cloud.tencent.com/project) area of the account center in the console to copy the project ID.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignProjectResponse(AbstractModel):
    r"""AssignProject response structure.

    """

    def __init__(self):
        r"""
        :param _FlowIds: Lists async task ids returned.
        :type FlowIds: list of int non-negative
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowIds = None
        self._RequestId = None

    @property
    def FlowIds(self):
        r"""Lists async task ids returned.
        :rtype: list of int non-negative
        """
        return self._FlowIds

    @FlowIds.setter
    def FlowIds(self, FlowIds):
        self._FlowIds = FlowIds

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowIds = params.get("FlowIds")
        self._RequestId = params.get("RequestId")


class Auth(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _Mask: Permission information of the current account.
- 0: no permissions.
- 1: read-only.
- 3: read-write.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Mask: int
        :param _NameSpace: Specifies the name of the database that has the current account permissions.
- \*: indicates all databases.
- db.name: indicates the database with a specific name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NameSpace: str
        """
        self._Mask = None
        self._NameSpace = None

    @property
    def Mask(self):
        r"""Permission information of the current account.
- 0: no permissions.
- 1: read-only.
- 3: read-write.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Mask

    @Mask.setter
    def Mask(self, Mask):
        self._Mask = Mask

    @property
    def NameSpace(self):
        r"""Specifies the name of the database that has the current account permissions.
- \*: indicates all databases.
- db.name: indicates the database with a specific name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NameSpace

    @NameSpace.setter
    def NameSpace(self, NameSpace):
        self._NameSpace = NameSpace


    def _deserialize(self, params):
        self._Mask = params.get("Mask")
        self._NameSpace = params.get("NameSpace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupDownloadTask(AbstractModel):
    r"""Backup download task information

    """

    def __init__(self):
        r"""
        :param _CreateTime: Task creation time.
        :type CreateTime: str
        :param _BackupName: Backup file name.
        :type BackupName: str
        :param _ReplicaSetId: Shard name.
        :type ReplicaSetId: str
        :param _BackupSize: Backup data size, in bytes.
        :type BackupSize: int
        :param _Status: Task status.
- 0: wait for execution.
- 1: downloading.
- 2: download completed.
- 3: download failed.
- 4: wait for retry.
        :type Status: int
        :param _Percent: Task progress percentage.
        :type Percent: int
        :param _TimeSpend: Duration, in seconds.
        :type TimeSpend: int
        :param _Url: Download link for backup data.
        :type Url: str
        :param _BackupMethod: Backup method.
- 0: logical backup.
- 1: physical backup.
- 3: snapshot backup.
**Note**:
1. The General Edition instance supports logical and physical backup. The Cloud Disk Edition instance supports physical and snapshot backup, but does not support logical backup currently.
2. Physical backup is not supported when storage encryption is enabled for the instance.
        :type BackupMethod: int
        :param _BackupDesc: Specified remarks for initiating backup tasks.
        :type BackupDesc: str
        :param _Region: Region information.
        :type Region: str
        :param _Bucket: Bucket information.
        :type Bucket: str
        """
        self._CreateTime = None
        self._BackupName = None
        self._ReplicaSetId = None
        self._BackupSize = None
        self._Status = None
        self._Percent = None
        self._TimeSpend = None
        self._Url = None
        self._BackupMethod = None
        self._BackupDesc = None
        self._Region = None
        self._Bucket = None

    @property
    def CreateTime(self):
        r"""Task creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def BackupName(self):
        r"""Backup file name.
        :rtype: str
        """
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def ReplicaSetId(self):
        r"""Shard name.
        :rtype: str
        """
        return self._ReplicaSetId

    @ReplicaSetId.setter
    def ReplicaSetId(self, ReplicaSetId):
        self._ReplicaSetId = ReplicaSetId

    @property
    def BackupSize(self):
        r"""Backup data size, in bytes.
        :rtype: int
        """
        return self._BackupSize

    @BackupSize.setter
    def BackupSize(self, BackupSize):
        self._BackupSize = BackupSize

    @property
    def Status(self):
        r"""Task status.
- 0: wait for execution.
- 1: downloading.
- 2: download completed.
- 3: download failed.
- 4: wait for retry.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Percent(self):
        r"""Task progress percentage.
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def TimeSpend(self):
        r"""Duration, in seconds.
        :rtype: int
        """
        return self._TimeSpend

    @TimeSpend.setter
    def TimeSpend(self, TimeSpend):
        self._TimeSpend = TimeSpend

    @property
    def Url(self):
        r"""Download link for backup data.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def BackupMethod(self):
        r"""Backup method.
- 0: logical backup.
- 1: physical backup.
- 3: snapshot backup.
**Note**:
1. The General Edition instance supports logical and physical backup. The Cloud Disk Edition instance supports physical and snapshot backup, but does not support logical backup currently.
2. Physical backup is not supported when storage encryption is enabled for the instance.
        :rtype: int
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BackupDesc(self):
        r"""Specified remarks for initiating backup tasks.
        :rtype: str
        """
        return self._BackupDesc

    @BackupDesc.setter
    def BackupDesc(self, BackupDesc):
        self._BackupDesc = BackupDesc

    @property
    def Region(self):
        r"""Region information.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        r"""Bucket information.
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._BackupName = params.get("BackupName")
        self._ReplicaSetId = params.get("ReplicaSetId")
        self._BackupSize = params.get("BackupSize")
        self._Status = params.get("Status")
        self._Percent = params.get("Percent")
        self._TimeSpend = params.get("TimeSpend")
        self._Url = params.get("Url")
        self._BackupMethod = params.get("BackupMethod")
        self._BackupDesc = params.get("BackupDesc")
        self._Region = params.get("Region")
        self._Bucket = params.get("Bucket")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupDownloadTaskStatus(AbstractModel):
    r"""Result of creating a backup download task.

    """

    def __init__(self):
        r"""
        :param _ReplicaSetId: Shard name.
        :type ReplicaSetId: str
        :param _Status: Current status of the task.
- 0: wait for execution.
- 1: downloading.
- 2: download completed.
- 3: download failed.
- 4: wait for retry.
        :type Status: int
        """
        self._ReplicaSetId = None
        self._Status = None

    @property
    def ReplicaSetId(self):
        r"""Shard name.
        :rtype: str
        """
        return self._ReplicaSetId

    @ReplicaSetId.setter
    def ReplicaSetId(self, ReplicaSetId):
        self._ReplicaSetId = ReplicaSetId

    @property
    def Status(self):
        r"""Current status of the task.
- 0: wait for execution.
- 1: downloading.
- 2: download completed.
- 3: download failed.
- 4: wait for retry.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ReplicaSetId = params.get("ReplicaSetId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupInfo(AbstractModel):
    r"""Backup information.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _BackupType: Backup method.
- 0: automatic backup.
- 1: manual backup.
        :type BackupType: int
        :param _BackupName: Backup file name.
        :type BackupName: str
        :param _BackupDesc: Backup task remarks.
        :type BackupDesc: str
        :param _BackupSize: Backup file size, in KB.
        :type BackupSize: int
        :param _StartTime: Backup start time.
        :type StartTime: str
        :param _EndTime: Backup end time.
        :type EndTime: str
        :param _Status: Backup status.
- 1: backing up.
- 2: backup successful.
        :type Status: int
        :param _BackupMethod: Backup method.
- 0: logical backup.
- 1: physical backup.
- 3: snapshot backup.
**Note:**
- The General Edition instance supports logical and physical backup. The Cloud Disk Edition instance supports physical and snapshot backup, but does not support logical backup currently.
- Physical backup is not supported when storage encryption is enabled for the instance.
        :type BackupMethod: int
        :param _BackId: Backup record ID.
        :type BackId: int
        :param _DeleteTime: Backup deletion time.
        :type DeleteTime: str
        :param _BackupRegion: Cross-region backup region.
        :type BackupRegion: str
        :param _RestoreTime: Rollback time supported by the backup.
        :type RestoreTime: str
        """
        self._InstanceId = None
        self._BackupType = None
        self._BackupName = None
        self._BackupDesc = None
        self._BackupSize = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._BackupMethod = None
        self._BackId = None
        self._DeleteTime = None
        self._BackupRegion = None
        self._RestoreTime = None

    @property
    def InstanceId(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupType(self):
        r"""Backup method.
- 0: automatic backup.
- 1: manual backup.
        :rtype: int
        """
        return self._BackupType

    @BackupType.setter
    def BackupType(self, BackupType):
        self._BackupType = BackupType

    @property
    def BackupName(self):
        r"""Backup file name.
        :rtype: str
        """
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def BackupDesc(self):
        r"""Backup task remarks.
        :rtype: str
        """
        return self._BackupDesc

    @BackupDesc.setter
    def BackupDesc(self, BackupDesc):
        self._BackupDesc = BackupDesc

    @property
    def BackupSize(self):
        r"""Backup file size, in KB.
        :rtype: int
        """
        return self._BackupSize

    @BackupSize.setter
    def BackupSize(self, BackupSize):
        self._BackupSize = BackupSize

    @property
    def StartTime(self):
        r"""Backup start time.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Backup end time.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        r"""Backup status.
- 1: backing up.
- 2: backup successful.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BackupMethod(self):
        r"""Backup method.
- 0: logical backup.
- 1: physical backup.
- 3: snapshot backup.
**Note:**
- The General Edition instance supports logical and physical backup. The Cloud Disk Edition instance supports physical and snapshot backup, but does not support logical backup currently.
- Physical backup is not supported when storage encryption is enabled for the instance.
        :rtype: int
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BackId(self):
        r"""Backup record ID.
        :rtype: int
        """
        return self._BackId

    @BackId.setter
    def BackId(self, BackId):
        self._BackId = BackId

    @property
    def DeleteTime(self):
        r"""Backup deletion time.
        :rtype: str
        """
        return self._DeleteTime

    @DeleteTime.setter
    def DeleteTime(self, DeleteTime):
        self._DeleteTime = DeleteTime

    @property
    def BackupRegion(self):
        r"""Cross-region backup region.
        :rtype: str
        """
        return self._BackupRegion

    @BackupRegion.setter
    def BackupRegion(self, BackupRegion):
        self._BackupRegion = BackupRegion

    @property
    def RestoreTime(self):
        r"""Rollback time supported by the backup.
        :rtype: str
        """
        return self._RestoreTime

    @RestoreTime.setter
    def RestoreTime(self, RestoreTime):
        self._RestoreTime = RestoreTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupType = params.get("BackupType")
        self._BackupName = params.get("BackupName")
        self._BackupDesc = params.get("BackupDesc")
        self._BackupSize = params.get("BackupSize")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._BackupMethod = params.get("BackupMethod")
        self._BackId = params.get("BackId")
        self._DeleteTime = params.get("DeleteTime")
        self._BackupRegion = params.get("BackupRegion")
        self._RestoreTime = params.get("RestoreTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClientConnection(AbstractModel):
    r"""Client connection information, including client IP and number of connections

    """

    def __init__(self):
        r"""
        :param _IP: IP address of the connected client.
        :type IP: str
        :param _Count: Number of connections corresponding to the client IP address.
        :type Count: int
        :param _InternalService: Whether it is an internal IP address.
        :type InternalService: bool
        """
        self._IP = None
        self._Count = None
        self._InternalService = None

    @property
    def IP(self):
        r"""IP address of the connected client.
        :rtype: str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Count(self):
        r"""Number of connections corresponding to the client IP address.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def InternalService(self):
        r"""Whether it is an internal IP address.
        :rtype: bool
        """
        return self._InternalService

    @InternalService.setter
    def InternalService(self, InternalService):
        self._InternalService = InternalService


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._Count = params.get("Count")
        self._InternalService = params.get("InternalService")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountUserRequest(AbstractModel):
    r"""CreateAccountUser request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. For example, cmgo-p8vn****. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/MongoDB), and copy the instance ID from the instance list.
        :type InstanceId: str
        :param _UserName: New account name. The format requirements are as follows:
- The value range for the character length is [1, 64].
- Allowed characters include uppercase letters, lowercase letters, digits (1–9), underscores (\_), and hyphens (-).
        :type UserName: str
        :param _Password: New account password. The password complexity requirements are as follows:
- The value range for the character length is [8, 32].
- It should include at least two of the following: letters, digits, and special characters (the exclamation mark (!), at sign (@), number sign (#), percent sign (%), caret (^), asterisk (*), parentheses (), and underscore (_)).
        :type Password: str
        :param _MongoUserPassword: Password corresponding to the mongouser account. mongouser is the default account of the system; it indicates the password set during instance creation.
        :type MongoUserPassword: str
        :param _UserDesc: Account remarks.
        :type UserDesc: str
        :param _AuthRole: Read/Write permission information of the account.
        :type AuthRole: list of Auth
        """
        self._InstanceId = None
        self._UserName = None
        self._Password = None
        self._MongoUserPassword = None
        self._UserDesc = None
        self._AuthRole = None

    @property
    def InstanceId(self):
        r"""Instance ID. For example, cmgo-p8vn****. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/MongoDB), and copy the instance ID from the instance list.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        r"""New account name. The format requirements are as follows:
- The value range for the character length is [1, 64].
- Allowed characters include uppercase letters, lowercase letters, digits (1–9), underscores (\_), and hyphens (-).
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        r"""New account password. The password complexity requirements are as follows:
- The value range for the character length is [8, 32].
- It should include at least two of the following: letters, digits, and special characters (the exclamation mark (!), at sign (@), number sign (#), percent sign (%), caret (^), asterisk (*), parentheses (), and underscore (_)).
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def MongoUserPassword(self):
        r"""Password corresponding to the mongouser account. mongouser is the default account of the system; it indicates the password set during instance creation.
        :rtype: str
        """
        return self._MongoUserPassword

    @MongoUserPassword.setter
    def MongoUserPassword(self, MongoUserPassword):
        self._MongoUserPassword = MongoUserPassword

    @property
    def UserDesc(self):
        r"""Account remarks.
        :rtype: str
        """
        return self._UserDesc

    @UserDesc.setter
    def UserDesc(self, UserDesc):
        self._UserDesc = UserDesc

    @property
    def AuthRole(self):
        r"""Read/Write permission information of the account.
        :rtype: list of Auth
        """
        return self._AuthRole

    @AuthRole.setter
    def AuthRole(self, AuthRole):
        self._AuthRole = AuthRole


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._MongoUserPassword = params.get("MongoUserPassword")
        self._UserDesc = params.get("UserDesc")
        if params.get("AuthRole") is not None:
            self._AuthRole = []
            for item in params.get("AuthRole"):
                obj = Auth()
                obj._deserialize(item)
                self._AuthRole.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountUserResponse(AbstractModel):
    r"""CreateAccountUser response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Creates a task ID.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Creates a task ID.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CreateBackupDBInstanceRequest(AbstractModel):
    r"""CreateBackupDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. For example, cmgo-p8vn****. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/MongoDB) and copy the instance ID from the instance list.
        :type InstanceId: str
        :param _BackupMethod: Sets the backup method.
- 0: logical backup.
- 1: physical backup.
- 3: snapshot backup.
**Note**:
1. The General Edition instance supports logical and physical backup. The Cloud Disk Edition instance supports physical and snapshot backup, but does not support logical backup currently.
2. Physical backup is not supported when storage encryption is enabled for the instance.
        :type BackupMethod: int
        :param _BackupRemark: Backup remarks information.
        :type BackupRemark: str
        """
        self._InstanceId = None
        self._BackupMethod = None
        self._BackupRemark = None

    @property
    def InstanceId(self):
        r"""Instance ID. For example, cmgo-p8vn****. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/MongoDB) and copy the instance ID from the instance list.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMethod(self):
        r"""Sets the backup method.
- 0: logical backup.
- 1: physical backup.
- 3: snapshot backup.
**Note**:
1. The General Edition instance supports logical and physical backup. The Cloud Disk Edition instance supports physical and snapshot backup, but does not support logical backup currently.
2. Physical backup is not supported when storage encryption is enabled for the instance.
        :rtype: int
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def BackupRemark(self):
        r"""Backup remarks information.
        :rtype: str
        """
        return self._BackupRemark

    @BackupRemark.setter
    def BackupRemark(self, BackupRemark):
        self._BackupRemark = BackupRemark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMethod = params.get("BackupMethod")
        self._BackupRemark = params.get("BackupRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupDBInstanceResponse(AbstractModel):
    r"""CreateBackupDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Request ID.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        r"""Request ID.
        :rtype: str
        """
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class CreateBackupDownloadTaskRequest(AbstractModel):
    r"""CreateBackupDownloadTask request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :type InstanceId: str
        :param _BackupName: Name of the backup file to be downloaded. The [DescribeDBBackups](https://www.tencentcloud.comom/document/product/240/38574?from_cn_redirect=1) API can be called to obtain it.
        :type BackupName: str
        :param _BackupSets: Specifies the node ID of the replica set to be downloaded or the shard node ID list of the sharded cluster.
- If the replica set instance ID is cmgo-p8vnipr5, for example, BackupSets.0=cmgo-p8vnipr5_0, full data can be downloaded.
- If the sharded cluster instance ID is cmgo-p8vnipr5, for example, BackupSets.0=cmgo-p8vnipr5_0&BackupSets.1=cmgo-p8vnipr5_1, download the data of Shard 0 and Shard 1. If a full download is needed for the sharded cluster, import all shard names as shown in the example.
        :type BackupSets: list of ReplicaSetInfo
        """
        self._InstanceId = None
        self._BackupName = None
        self._BackupSets = None

    @property
    def InstanceId(self):
        r"""Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupName(self):
        r"""Name of the backup file to be downloaded. The [DescribeDBBackups](https://www.tencentcloud.comom/document/product/240/38574?from_cn_redirect=1) API can be called to obtain it.
        :rtype: str
        """
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def BackupSets(self):
        r"""Specifies the node ID of the replica set to be downloaded or the shard node ID list of the sharded cluster.
- If the replica set instance ID is cmgo-p8vnipr5, for example, BackupSets.0=cmgo-p8vnipr5_0, full data can be downloaded.
- If the sharded cluster instance ID is cmgo-p8vnipr5, for example, BackupSets.0=cmgo-p8vnipr5_0&BackupSets.1=cmgo-p8vnipr5_1, download the data of Shard 0 and Shard 1. If a full download is needed for the sharded cluster, import all shard names as shown in the example.
        :rtype: list of ReplicaSetInfo
        """
        return self._BackupSets

    @BackupSets.setter
    def BackupSets(self, BackupSets):
        self._BackupSets = BackupSets


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupName = params.get("BackupName")
        if params.get("BackupSets") is not None:
            self._BackupSets = []
            for item in params.get("BackupSets"):
                obj = ReplicaSetInfo()
                obj._deserialize(item)
                self._BackupSets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupDownloadTaskResponse(AbstractModel):
    r"""CreateBackupDownloadTask response structure.

    """

    def __init__(self):
        r"""
        :param _Tasks: Status of the download task.
        :type Tasks: list of BackupDownloadTaskStatus
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Tasks = None
        self._RequestId = None

    @property
    def Tasks(self):
        r"""Status of the download task.
        :rtype: list of BackupDownloadTaskStatus
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = BackupDownloadTaskStatus()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class CreateDBInstanceHourRequest(AbstractModel):
    r"""CreateDBInstanceHour request structure.

    """

    def __init__(self):
        r"""
        :param _Memory: Instance memory size. Unit: GB. Call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API to obtain specific saleable memory specifications.
        :type Memory: int
        :param _Volume: Instance disk size. Unit: GB. Call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API to obtain the maximum and minimum disk sizes corresponding to each CPU specification.
        :type Volume: int
        :param _ReplicateSetNum:  - Specifies the number of replica sets during replica set instance creation. This parameter can only be set to 1.
 - Specifies the number of shards during sharded cluster instance creation. Call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API to query the range of shard quantity. The parameters MinReplicateSetNum and MaxReplicateSetNum in the returned data structure SpecItems correspond to the minimum value and maximum value, respectively.
        :type ReplicateSetNum: int
        :param _NodeNum:  - Specifies the number of primary and secondary nodes for each replica set during replica set instance creation. Call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API to obtain the maximum and minimum number of nodes supported for each replica set.
 - Specifies the number of primary and secondary nodes for each shard during sharded cluster instance creation. Call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API to obtain the maximum and minimum number of nodes supported for each shard.
        :type NodeNum: int
        :param _MongoVersion: Refers to version information. The [DescribeSpecInfo](https://www.tencentcloud.comom/document/product/240/38567?from_cn_redirect=1) API can be called to obtain detailed information about the supported versions.
- MONGO_40_WT: version of the MongoDB 4.0 WiredTiger storage engine.
- MONGO_42_WT: version of the MongoDB 4.2 WiredTiger storage engine.
- MONGO_44_WT: version of the MongoDB 4.4 WiredTiger storage engine.
- MONGO_50_WT: version of the MongoDB 5.0 WiredTiger storage engine.
- MONGO_60_WT: version of the MongoDB 6.0 WiredTiger storage engine.
- MONGO_70_WT: version of the MongoDB 7.0 WiredTiger storage engine.
        :type MongoVersion: str
        :param _MachineCode: Product specification type.
 - HIO10G: general high-I/O 10GE type.
 - HCD: cloud disk type.
        :type MachineCode: str
        :param _GoodsNum: Number of instances. The minimum value is 1, and the maximum value is 30.
        :type GoodsNum: int
        :param _Zone: AZ information in the format of ap-guangzhou-2
- For more information, query through the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API.
- If multi-AZ deployment is enabled, this parameter refers to the primary AZ and must be one of the values of `AvailabilityZoneList`.
        :type Zone: str
        :param _ClusterType: Instance architecture type
- REPLSET: Replica set
- SHARD: Sharded cluster
        :type ClusterType: str
        :param _VpcId: VPC ID.
- Only VPC configuration is supported, and a VPC in the same region as the instance should be selected. Log in to the [VPC console](https://console.cloud.tencent.com/vpc) to obtain the available VPC ID.
- After successful instance creation, VPCs can be changed. For detailed operations, see [Changing the Network](https://www.tencentcloud.comom/document/product/239/30910?from_cn_redirect=1).
        :type VpcId: str
        :param _SubnetId: Subnet ID of the VPC.
- A subnet should be specified within the selected VPC. Log in to the [VPC console](https://console.cloud.tencent.com/vpc) to obtain the available subnet ID.
- After successful instance creation, VPCs and subnets can be changed. For detailed operations, see [Changing the Network](https://www.tencentcloud.comom/document/product/239/30910?from_cn_redirect=1).
        :type SubnetId: str
        :param _Password: Instance password. The requirements are as follows:
 - The number of characters should be in the range of [8, 32].
 - Characters within the ranges [A,Z], [a,z], and [0,9] are allowed.
 - Special characters that can be entered include exclamation marks (!), at signs (@), number signs (#), percent signs (%), carets (^), asterisks (\*), brackets (()), and underscores (_).
 - It cannot contain only the same letters or digits.
        :type Password: str
        :param _ProjectId: Project ID. - The default project is used if this parameter is not specified.
 - The project ID can be obtained on the [project management page in the TencentDB for MongoDB console](https://console.cloud.tencent.com/project).
        :type ProjectId: int
        :param _Tags: Instance tag information
        :type Tags: list of TagInfo
        :param _Clone: Instance type.
- 1: formal instance.
- 3: read-only instance.
- 4: disaster recovery instance.
- 5. cloned instance. Note: For a cloned instance, RestoreTime is required.
        :type Clone: int
        :param _Father: Parent instance ID.
- This parameter is required when the value of the **Clone** parameter is set to 3 or 4, indicating a read-only or disaster recovery instance.
- Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the parent instance ID from the instance list.
        :type Father: str
        :param _SecurityGroup: Security group ID. Log in to the [security group console](https://console.cloud.tencent.com/vpc/security-group) to obtain the ID of the security group in the same region as the database instance.
        :type SecurityGroup: list of str
        :param _RestoreTime: Rollback time of the cloned instance
- This parameter is required for a cloned instance in the format of 2021-08-13 16:30:00.
- Time range for rollback: You can roll back data in the last 7 days.
        :type RestoreTime: str
        :param _InstanceName: Instance name. Only Chinese characters, letters, digits, underscores (_), and delimiters (-) are supported, with a length of 128 characters. When database instances are purchased in batches, the automatic ascending feature is supported through the custom naming pattern string and numeric suffix to set instance names efficiently.
- Basic mode: prefix + automatic ascending number (starting from 1 by default). Only a custom instance name prefix is required for **lnstanceName**. For example, it can be set to cmgo. If the purchase quantity is set to 5, after purchase, the instances will be sequentially named cmgo1, cmgo2, cmgo3, cmgo4, and cmgo5, respectively.
- Custom starting number mode: prefix + {R:x} (x is the custom starting number). Prefix{R:x} is required for **InstanceName**. For example, cmgo{R:3}. If the purchase quantity is set to 5, the instance names will be sequentially named cmgo3, cmgo4, cmgo5, cmgo6, and cmgo7.
- Composite pattern string: prefix 1{R:x} + prefix 2{R:y}+ ⋯ + fixed suffix, where x and y are the starting numbers of each prefix. A composite pattern string is required for **instanceName**. For example, cmgo{R:10}\_node{R:12}\_db. If the batch purchase quantity is set to 5, the instances will be sequentially named cmgo10\_node12\_db, cmgo11\_node13\_db, cmgo12\_node14\_db, cmgo13\_node15\_db, and cmgo14\_node16\_db.
        :type InstanceName: str
        :param _AvailabilityZoneList: Specifies the list of AZs during multi-AZ deployment of TencentDB for MongoDB instances.
- For instances in multi-AZ deployment mode, the **Zone** parameter specifies the primary AZ, and **AvailabilityZoneList** specifies all AZs, including the primary AZ. Format: [ap-guangzhou-2,ap-guangzhou-3,ap-guangzhou-4].
- The [DescribeSpecInfo](https://www.tencentcloud.comom/document/product/240/38567?from_cn_redirect=1) API can be called to obtain AZs planned for TencentDB for MongoDB instances in different regions, helping you specify valid AZs.
- Nodes in multi-AZ deployment mode can only be deployed in 3 different AZs. Deploying most nodes of a cluster in the same AZ is not supported. For example, a 3-node cluster does not support deploying 2 nodes in the same AZ.
        :type AvailabilityZoneList: list of str
        :param _MongosCpu: Number of Mongos node CPU cores. Valid values: 1, 2, 4, 8, and 16. This parameter is required during sharded cluster instance purchase.
        :type MongosCpu: int
        :param _MongosMemory: Mongos node memory size.
- This parameter is required during sharded cluster instance purchase.
- Unit: GB. 1-core 2 GB, 2-core 4 GB, 4-core 8 GB, 8-core 16 GB, and 16-core 32 GB are supported.
        :type MongosMemory: int
        :param _MongosNodeNum: Number of Mongos nodes. This parameter is required during sharded cluster instance purchase.
 - For instances in single-AZ deployment mode, the value range is [3,32].
 - For instances in multi-AZ deployment mode, the value range is [6,32].
        :type MongosNodeNum: int
        :param _ReadonlyNodeNum: Number of read-only nodes. Value ranges: [0,5].
        :type ReadonlyNodeNum: int
        :param _ReadonlyNodeAvailabilityZoneList: Array of AZs of read-only nodes. This parameter is required for instances in multi-AZ deployment mode when **ReadonlyNodeNum** is not set to **0**.
        :type ReadonlyNodeAvailabilityZoneList: list of str
        :param _HiddenZone: AZ where the hidden node resides, which is required in cross-AZ instance deployment.
        :type HiddenZone: str
        :param _ParamTemplateId: Parameter template ID.
- A parameter template is a collection of predefined parameter values that can be used to quickly configure new MongoDB instances. Proper use of parameter templates can significantly enhance the deployment efficiency and operational performance of the database.
- The [DescribeDBInstanceParamTpl](https://www.tencentcloud.comom/document/product/240/109155?from_cn_redirect=1) API can be called to obtain the parameter template ID. Select the parameter template ID corresponding to the instance version and architecture.
        :type ParamTemplateId: str
        """
        self._Memory = None
        self._Volume = None
        self._ReplicateSetNum = None
        self._NodeNum = None
        self._MongoVersion = None
        self._MachineCode = None
        self._GoodsNum = None
        self._Zone = None
        self._ClusterType = None
        self._VpcId = None
        self._SubnetId = None
        self._Password = None
        self._ProjectId = None
        self._Tags = None
        self._Clone = None
        self._Father = None
        self._SecurityGroup = None
        self._RestoreTime = None
        self._InstanceName = None
        self._AvailabilityZoneList = None
        self._MongosCpu = None
        self._MongosMemory = None
        self._MongosNodeNum = None
        self._ReadonlyNodeNum = None
        self._ReadonlyNodeAvailabilityZoneList = None
        self._HiddenZone = None
        self._ParamTemplateId = None

    @property
    def Memory(self):
        r"""Instance memory size. Unit: GB. Call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API to obtain specific saleable memory specifications.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        r"""Instance disk size. Unit: GB. Call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API to obtain the maximum and minimum disk sizes corresponding to each CPU specification.
        :rtype: int
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def ReplicateSetNum(self):
        r""" - Specifies the number of replica sets during replica set instance creation. This parameter can only be set to 1.
 - Specifies the number of shards during sharded cluster instance creation. Call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API to query the range of shard quantity. The parameters MinReplicateSetNum and MaxReplicateSetNum in the returned data structure SpecItems correspond to the minimum value and maximum value, respectively.
        :rtype: int
        """
        return self._ReplicateSetNum

    @ReplicateSetNum.setter
    def ReplicateSetNum(self, ReplicateSetNum):
        self._ReplicateSetNum = ReplicateSetNum

    @property
    def NodeNum(self):
        r""" - Specifies the number of primary and secondary nodes for each replica set during replica set instance creation. Call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API to obtain the maximum and minimum number of nodes supported for each replica set.
 - Specifies the number of primary and secondary nodes for each shard during sharded cluster instance creation. Call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API to obtain the maximum and minimum number of nodes supported for each shard.
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def MongoVersion(self):
        r"""Refers to version information. The [DescribeSpecInfo](https://www.tencentcloud.comom/document/product/240/38567?from_cn_redirect=1) API can be called to obtain detailed information about the supported versions.
- MONGO_40_WT: version of the MongoDB 4.0 WiredTiger storage engine.
- MONGO_42_WT: version of the MongoDB 4.2 WiredTiger storage engine.
- MONGO_44_WT: version of the MongoDB 4.4 WiredTiger storage engine.
- MONGO_50_WT: version of the MongoDB 5.0 WiredTiger storage engine.
- MONGO_60_WT: version of the MongoDB 6.0 WiredTiger storage engine.
- MONGO_70_WT: version of the MongoDB 7.0 WiredTiger storage engine.
        :rtype: str
        """
        return self._MongoVersion

    @MongoVersion.setter
    def MongoVersion(self, MongoVersion):
        self._MongoVersion = MongoVersion

    @property
    def MachineCode(self):
        r"""Product specification type.
 - HIO10G: general high-I/O 10GE type.
 - HCD: cloud disk type.
        :rtype: str
        """
        return self._MachineCode

    @MachineCode.setter
    def MachineCode(self, MachineCode):
        self._MachineCode = MachineCode

    @property
    def GoodsNum(self):
        r"""Number of instances. The minimum value is 1, and the maximum value is 30.
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Zone(self):
        r"""AZ information in the format of ap-guangzhou-2
- For more information, query through the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API.
- If multi-AZ deployment is enabled, this parameter refers to the primary AZ and must be one of the values of `AvailabilityZoneList`.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ClusterType(self):
        r"""Instance architecture type
- REPLSET: Replica set
- SHARD: Sharded cluster
        :rtype: str
        """
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def VpcId(self):
        r"""VPC ID.
- Only VPC configuration is supported, and a VPC in the same region as the instance should be selected. Log in to the [VPC console](https://console.cloud.tencent.com/vpc) to obtain the available VPC ID.
- After successful instance creation, VPCs can be changed. For detailed operations, see [Changing the Network](https://www.tencentcloud.comom/document/product/239/30910?from_cn_redirect=1).
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""Subnet ID of the VPC.
- A subnet should be specified within the selected VPC. Log in to the [VPC console](https://console.cloud.tencent.com/vpc) to obtain the available subnet ID.
- After successful instance creation, VPCs and subnets can be changed. For detailed operations, see [Changing the Network](https://www.tencentcloud.comom/document/product/239/30910?from_cn_redirect=1).
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Password(self):
        r"""Instance password. The requirements are as follows:
 - The number of characters should be in the range of [8, 32].
 - Characters within the ranges [A,Z], [a,z], and [0,9] are allowed.
 - Special characters that can be entered include exclamation marks (!), at signs (@), number signs (#), percent signs (%), carets (^), asterisks (\*), brackets (()), and underscores (_).
 - It cannot contain only the same letters or digits.
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ProjectId(self):
        r"""Project ID. - The default project is used if this parameter is not specified.
 - The project ID can be obtained on the [project management page in the TencentDB for MongoDB console](https://console.cloud.tencent.com/project).
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Tags(self):
        r"""Instance tag information
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Clone(self):
        r"""Instance type.
- 1: formal instance.
- 3: read-only instance.
- 4: disaster recovery instance.
- 5. cloned instance. Note: For a cloned instance, RestoreTime is required.
        :rtype: int
        """
        return self._Clone

    @Clone.setter
    def Clone(self, Clone):
        self._Clone = Clone

    @property
    def Father(self):
        r"""Parent instance ID.
- This parameter is required when the value of the **Clone** parameter is set to 3 or 4, indicating a read-only or disaster recovery instance.
- Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the parent instance ID from the instance list.
        :rtype: str
        """
        return self._Father

    @Father.setter
    def Father(self, Father):
        self._Father = Father

    @property
    def SecurityGroup(self):
        r"""Security group ID. Log in to the [security group console](https://console.cloud.tencent.com/vpc/security-group) to obtain the ID of the security group in the same region as the database instance.
        :rtype: list of str
        """
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def RestoreTime(self):
        r"""Rollback time of the cloned instance
- This parameter is required for a cloned instance in the format of 2021-08-13 16:30:00.
- Time range for rollback: You can roll back data in the last 7 days.
        :rtype: str
        """
        return self._RestoreTime

    @RestoreTime.setter
    def RestoreTime(self, RestoreTime):
        self._RestoreTime = RestoreTime

    @property
    def InstanceName(self):
        r"""Instance name. Only Chinese characters, letters, digits, underscores (_), and delimiters (-) are supported, with a length of 128 characters. When database instances are purchased in batches, the automatic ascending feature is supported through the custom naming pattern string and numeric suffix to set instance names efficiently.
- Basic mode: prefix + automatic ascending number (starting from 1 by default). Only a custom instance name prefix is required for **lnstanceName**. For example, it can be set to cmgo. If the purchase quantity is set to 5, after purchase, the instances will be sequentially named cmgo1, cmgo2, cmgo3, cmgo4, and cmgo5, respectively.
- Custom starting number mode: prefix + {R:x} (x is the custom starting number). Prefix{R:x} is required for **InstanceName**. For example, cmgo{R:3}. If the purchase quantity is set to 5, the instance names will be sequentially named cmgo3, cmgo4, cmgo5, cmgo6, and cmgo7.
- Composite pattern string: prefix 1{R:x} + prefix 2{R:y}+ ⋯ + fixed suffix, where x and y are the starting numbers of each prefix. A composite pattern string is required for **instanceName**. For example, cmgo{R:10}\_node{R:12}\_db. If the batch purchase quantity is set to 5, the instances will be sequentially named cmgo10\_node12\_db, cmgo11\_node13\_db, cmgo12\_node14\_db, cmgo13\_node15\_db, and cmgo14\_node16\_db.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AvailabilityZoneList(self):
        r"""Specifies the list of AZs during multi-AZ deployment of TencentDB for MongoDB instances.
- For instances in multi-AZ deployment mode, the **Zone** parameter specifies the primary AZ, and **AvailabilityZoneList** specifies all AZs, including the primary AZ. Format: [ap-guangzhou-2,ap-guangzhou-3,ap-guangzhou-4].
- The [DescribeSpecInfo](https://www.tencentcloud.comom/document/product/240/38567?from_cn_redirect=1) API can be called to obtain AZs planned for TencentDB for MongoDB instances in different regions, helping you specify valid AZs.
- Nodes in multi-AZ deployment mode can only be deployed in 3 different AZs. Deploying most nodes of a cluster in the same AZ is not supported. For example, a 3-node cluster does not support deploying 2 nodes in the same AZ.
        :rtype: list of str
        """
        return self._AvailabilityZoneList

    @AvailabilityZoneList.setter
    def AvailabilityZoneList(self, AvailabilityZoneList):
        self._AvailabilityZoneList = AvailabilityZoneList

    @property
    def MongosCpu(self):
        r"""Number of Mongos node CPU cores. Valid values: 1, 2, 4, 8, and 16. This parameter is required during sharded cluster instance purchase.
        :rtype: int
        """
        return self._MongosCpu

    @MongosCpu.setter
    def MongosCpu(self, MongosCpu):
        self._MongosCpu = MongosCpu

    @property
    def MongosMemory(self):
        r"""Mongos node memory size.
- This parameter is required during sharded cluster instance purchase.
- Unit: GB. 1-core 2 GB, 2-core 4 GB, 4-core 8 GB, 8-core 16 GB, and 16-core 32 GB are supported.
        :rtype: int
        """
        return self._MongosMemory

    @MongosMemory.setter
    def MongosMemory(self, MongosMemory):
        self._MongosMemory = MongosMemory

    @property
    def MongosNodeNum(self):
        r"""Number of Mongos nodes. This parameter is required during sharded cluster instance purchase.
 - For instances in single-AZ deployment mode, the value range is [3,32].
 - For instances in multi-AZ deployment mode, the value range is [6,32].
        :rtype: int
        """
        return self._MongosNodeNum

    @MongosNodeNum.setter
    def MongosNodeNum(self, MongosNodeNum):
        self._MongosNodeNum = MongosNodeNum

    @property
    def ReadonlyNodeNum(self):
        r"""Number of read-only nodes. Value ranges: [0,5].
        :rtype: int
        """
        return self._ReadonlyNodeNum

    @ReadonlyNodeNum.setter
    def ReadonlyNodeNum(self, ReadonlyNodeNum):
        self._ReadonlyNodeNum = ReadonlyNodeNum

    @property
    def ReadonlyNodeAvailabilityZoneList(self):
        r"""Array of AZs of read-only nodes. This parameter is required for instances in multi-AZ deployment mode when **ReadonlyNodeNum** is not set to **0**.
        :rtype: list of str
        """
        return self._ReadonlyNodeAvailabilityZoneList

    @ReadonlyNodeAvailabilityZoneList.setter
    def ReadonlyNodeAvailabilityZoneList(self, ReadonlyNodeAvailabilityZoneList):
        self._ReadonlyNodeAvailabilityZoneList = ReadonlyNodeAvailabilityZoneList

    @property
    def HiddenZone(self):
        r"""AZ where the hidden node resides, which is required in cross-AZ instance deployment.
        :rtype: str
        """
        return self._HiddenZone

    @HiddenZone.setter
    def HiddenZone(self, HiddenZone):
        self._HiddenZone = HiddenZone

    @property
    def ParamTemplateId(self):
        r"""Parameter template ID.
- A parameter template is a collection of predefined parameter values that can be used to quickly configure new MongoDB instances. Proper use of parameter templates can significantly enhance the deployment efficiency and operational performance of the database.
- The [DescribeDBInstanceParamTpl](https://www.tencentcloud.comom/document/product/240/109155?from_cn_redirect=1) API can be called to obtain the parameter template ID. Select the parameter template ID corresponding to the instance version and architecture.
        :rtype: str
        """
        return self._ParamTemplateId

    @ParamTemplateId.setter
    def ParamTemplateId(self, ParamTemplateId):
        self._ParamTemplateId = ParamTemplateId


    def _deserialize(self, params):
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._ReplicateSetNum = params.get("ReplicateSetNum")
        self._NodeNum = params.get("NodeNum")
        self._MongoVersion = params.get("MongoVersion")
        self._MachineCode = params.get("MachineCode")
        self._GoodsNum = params.get("GoodsNum")
        self._Zone = params.get("Zone")
        self._ClusterType = params.get("ClusterType")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Password = params.get("Password")
        self._ProjectId = params.get("ProjectId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Clone = params.get("Clone")
        self._Father = params.get("Father")
        self._SecurityGroup = params.get("SecurityGroup")
        self._RestoreTime = params.get("RestoreTime")
        self._InstanceName = params.get("InstanceName")
        self._AvailabilityZoneList = params.get("AvailabilityZoneList")
        self._MongosCpu = params.get("MongosCpu")
        self._MongosMemory = params.get("MongosMemory")
        self._MongosNodeNum = params.get("MongosNodeNum")
        self._ReadonlyNodeNum = params.get("ReadonlyNodeNum")
        self._ReadonlyNodeAvailabilityZoneList = params.get("ReadonlyNodeAvailabilityZoneList")
        self._HiddenZone = params.get("HiddenZone")
        self._ParamTemplateId = params.get("ParamTemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBInstanceHourResponse(AbstractModel):
    r"""CreateDBInstanceHour response structure.

    """

    def __init__(self):
        r"""
        :param _DealId: Order ID
        :type DealId: str
        :param _InstanceIds: List of IDs of the created instances
        :type InstanceIds: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealId = None
        self._InstanceIds = None
        self._RequestId = None

    @property
    def DealId(self):
        r"""Order ID
        :rtype: str
        """
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def InstanceIds(self):
        r"""List of IDs of the created instances
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._InstanceIds = params.get("InstanceIds")
        self._RequestId = params.get("RequestId")


class CreateDBInstanceRequest(AbstractModel):
    r"""CreateDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _NodeNum:  - Specifies the number of primary and secondary nodes for each replica set during replica set instance creation. Call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API to obtain the maximum and minimum number of nodes supported for each replica set.
 - Specifies the number of primary and secondary nodes for each shard during sharded cluster instance creation. Call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API to obtain the maximum and minimum number of nodes supported for each shard.
        :type NodeNum: int
        :param _Memory: Instance memory size. Unit: GB. Call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API to obtain specific saleable memory specifications.
        :type Memory: int
        :param _Volume: Instance disk size. Unit: GB. Call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API to obtain the maximum and minimum disk sizes corresponding to each CPU specification.
        :type Volume: int
        :param _MongoVersion: Refers to version information. The [DescribeSpecInfo](https://www.tencentcloud.comom/document/product/240/38567?from_cn_redirect=1) API can be called to obtain detailed information about the supported versions.
- MONGO_40_WT: version of the MongoDB 4.0 WiredTiger storage engine.
- MONGO_42_WT: version of the MongoDB 4.2 WiredTiger storage engine.
- MONGO_44_WT: version of the MongoDB 4.4 WiredTiger storage engine.
- MONGO_50_WT: version of the MongoDB 5.0 WiredTiger storage engine.
- MONGO_60_WT: version of the MongoDB 6.0 WiredTiger storage engine.
- MONGO_70_WT: version of the MongoDB 7.0 WiredTiger storage engine.
        :type MongoVersion: str
        :param _GoodsNum: Number of instances. The minimum value is 1, and the maximum value is 30.
        :type GoodsNum: int
        :param _Zone: AZ information. Format: ap-guangzhou-2.
 - Call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API to obtain the specific information.
 - This parameter indicates the primary AZ. If multi-AZ deployment is adopted, the value of Zone should be one of the values of AvailabilityZoneList.
        :type Zone: str
        :param _Period: Specifies the purchase duration during the instance purchase, in months. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, and 36.
        :type Period: int
        :param _MachineCode: Product specification type.
 - HIO10G: general high-I/O 10GE type.
 - HCD: cloud disk type.
        :type MachineCode: str
        :param _ClusterType: Instance architecture type.
 - REPLSET: replica set.
 - SHARD: sharded cluster.
        :type ClusterType: str
        :param _ReplicateSetNum:  - Specifies the number of replica sets during replica set instance creation. This parameter can only be set to 1.
 - Specifies the number of shards during sharded cluster instance creation. Call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API to query the range of shard quantity. The parameters MinReplicateSetNum and MaxReplicateSetNum in the returned data structure SpecItems correspond to the minimum value and maximum value, respectively.
        :type ReplicateSetNum: int
        :param _ProjectId: Project ID.  - The default project is used if this parameter is not specified.
 - The project ID can be obtained on the [project management page in the TencentDB for MongoDB console](https://console.cloud.tencent.com/project).
        :type ProjectId: int
        :param _VpcId: VPC ID.
- Only VPC configuration is supported, and a VPC in the same region as the instance should be selected. Log in to the [VPC console](https://console.cloud.tencent.com/vpc) to obtain the available VPC ID.
- After successful instance creation, VPCs can be changed. For detailed operations, see [Changing the Network](https://www.tencentcloud.comom/document/product/239/30910?from_cn_redirect=1).
        :type VpcId: str
        :param _SubnetId: Subnet ID of the VPC.
- A subnet should be specified within the selected VPC. Log in to the [VPC console](https://console.cloud.tencent.com/vpc) to obtain the available subnet ID.
- After successful instance creation, VPCs and subnets can be changed. For detailed operations, see [Changing the Network](https://www.tencentcloud.comom/document/product/239/30910?from_cn_redirect=1).
        :type SubnetId: str
        :param _Password: Instance password. The requirements are as follows:
 - The number of characters should be in the range of [8, 32].
 - Characters within the ranges [A,Z], [a,z], and [0,9] are allowed.
 - Special characters that can be entered include exclamation marks (!), at signs (@), number signs (#), percent signs (%), carets (^), asterisks (\*), brackets (()), and underscores (_).
 - It cannot contain only the same letters or digits.
        :type Password: str
        :param _Tags: Instance tag information.
        :type Tags: list of TagInfo
        :param _AutoRenewFlag: Automatic renewal flag.
 - 0: no automatic renewal.
 - 1: automatic renewal.
        :type AutoRenewFlag: int
        :param _AutoVoucher: Whether to automatically select a voucher.
 - 1: yes.
 - 0: no. Default value: 0.
        :type AutoVoucher: int
        :param _Clone: Instance type.
- 1: formal instance.
- 3: read-only instance.
- 4: disaster recovery instance.
- 5: cloned instance. Note: For a cloned instance, RestoreTime is required.
        :type Clone: int
        :param _Father: Parent instance ID.
- This parameter is required when the value of the **Clone** parameter is set to 3 or 4, indicating a read-only or disaster recovery instance.
- Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the parent instance ID from the instance list.
        :type Father: str
        :param _SecurityGroup: Security group ID. Log in to the [security group console](https://console.cloud.tencent.com/vpc/security-group) to obtain the ID of the security group in the same region as the database instance.
        :type SecurityGroup: list of str
        :param _RestoreTime: Rollback time of the cloned instance. It is required when the Clone value is 5 or 6. - This parameter is required for cloned instances. Format: 2021-08-13 16:30:00. - Rollback time range: Only data within the last 7 days can be rolled back.
        :type RestoreTime: str
        :param _InstanceName: Instance name. Only Chinese characters, letters, digits, underscores (_), and delimiters (-) are supported, with a length of 128 characters. When database instances are purchased in batches, the automatic ascending feature is supported through the custom naming pattern string and numeric suffix to set instance names efficiently.
- Basic mode: prefix + automatic ascending number (starting from 1 by default). Only a custom instance name prefix is required for **lnstanceName**. For example, it can be set to cmgo. If the purchase quantity is set to 5, after purchase, the instances will be sequentially named cmgo1, cmgo2, cmgo3, cmgo4, and cmgo5, respectively.
- Custom starting number mode: prefix + {R:x} (x is the custom starting number). Prefix{R:x} is required for **InstanceName**. For example, cmgo{R:3}. If the purchase quantity is set to 5, the instance names will be sequentially named cmgo3, cmgo4, cmgo5, cmgo6, and cmgo7.
- Composite pattern string: prefix 1{R:x} + prefix 2{R:y}+ ⋯ + fixed suffix, where x and y are the starting numbers of each prefix. A composite pattern string is required for **instanceName**. For example, cmgo{R:10}\_node{R:12}\_db. If the batch purchase quantity is set to 5, the instances will be sequentially named cmgo10\_node12\_db, cmgo11\_node13\_db, cmgo12\_node14\_db, cmgo13\_node15\_db, and cmgo14\_node16\_db.
        :type InstanceName: str
        :param _AvailabilityZoneList: Specifies the list of AZs during multi-AZ deployment of TencentDB for MongoDB instances.
 - For instances in multi-AZ deployment mode, the **Zone** parameter specifies the primary AZ, and **AvailabilityZoneList** specifies all AZs, including the primary AZ. Format: [ap-guangzhou-2,ap-guangzhou-3,ap-guangzhou-4].
 - The [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API can be called to obtain AZs planned for TencentDB for MongoDB instances in different regions, helping you specify valid AZs.
 - Nodes in multi-AZ deployment mode can only be deployed in 3 different AZs. Deploying most nodes of a cluster in the same AZ is not supported. For example, a 3-node cluster does not support deploying 2 nodes in the same AZ.
        :type AvailabilityZoneList: list of str
        :param _MongosCpu: Number of Mongos node CPU cores. Valid values: 1, 2, 4, 8, and 16. This parameter is required during sharded cluster instance purchase.
        :type MongosCpu: int
        :param _MongosMemory: Mongos node memory size.
 - This parameter is required during sharded cluster instance purchase.
 - Unit: GB. 1-core 2GB, 2-core 4GB, 4-core 8GB, 8-core 16GB, and 16-core 32GB are supported.
        :type MongosMemory: int
        :param _MongosNodeNum: Number of Mongos nodes. This parameter is required during sharded cluster instance purchase.
 - For instances in single-AZ deployment mode, the value range is [3,32].
 - For instances in multi-AZ deployment mode, the value range is [6,32].
        :type MongosNodeNum: int
        :param _ReadonlyNodeNum: Number of read-only nodes. Value ranges: [0,5].
        :type ReadonlyNodeNum: int
        :param _ReadonlyNodeAvailabilityZoneList: Array of AZs of read-only nodes. This parameter is required for instances in multi-AZ deployment mode when **ReadonlyNodeNum** is not set to **0**.
        :type ReadonlyNodeAvailabilityZoneList: list of str
        :param _HiddenZone: AZ of the hidden node. This parameter is required for instances in multi-AZ deployment mode.
        :type HiddenZone: str
        :param _ParamTemplateId: Parameter template ID.
- A parameter template is a collection of predefined parameter values that can be used to quickly configure new MongoDB instances. Proper use of parameter templates can significantly enhance the deployment efficiency and operational performance of the database.
- The [DescribeDBInstanceParamTpl](https://www.tencentcloud.comom/document/product/240/109155?from_cn_redirect=1) API can be called to obtain the parameter template ID. Select the parameter template ID corresponding to the instance version and architecture.
        :type ParamTemplateId: str
        """
        self._NodeNum = None
        self._Memory = None
        self._Volume = None
        self._MongoVersion = None
        self._GoodsNum = None
        self._Zone = None
        self._Period = None
        self._MachineCode = None
        self._ClusterType = None
        self._ReplicateSetNum = None
        self._ProjectId = None
        self._VpcId = None
        self._SubnetId = None
        self._Password = None
        self._Tags = None
        self._AutoRenewFlag = None
        self._AutoVoucher = None
        self._Clone = None
        self._Father = None
        self._SecurityGroup = None
        self._RestoreTime = None
        self._InstanceName = None
        self._AvailabilityZoneList = None
        self._MongosCpu = None
        self._MongosMemory = None
        self._MongosNodeNum = None
        self._ReadonlyNodeNum = None
        self._ReadonlyNodeAvailabilityZoneList = None
        self._HiddenZone = None
        self._ParamTemplateId = None

    @property
    def NodeNum(self):
        r""" - Specifies the number of primary and secondary nodes for each replica set during replica set instance creation. Call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API to obtain the maximum and minimum number of nodes supported for each replica set.
 - Specifies the number of primary and secondary nodes for each shard during sharded cluster instance creation. Call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API to obtain the maximum and minimum number of nodes supported for each shard.
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def Memory(self):
        r"""Instance memory size. Unit: GB. Call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API to obtain specific saleable memory specifications.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        r"""Instance disk size. Unit: GB. Call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API to obtain the maximum and minimum disk sizes corresponding to each CPU specification.
        :rtype: int
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def MongoVersion(self):
        r"""Refers to version information. The [DescribeSpecInfo](https://www.tencentcloud.comom/document/product/240/38567?from_cn_redirect=1) API can be called to obtain detailed information about the supported versions.
- MONGO_40_WT: version of the MongoDB 4.0 WiredTiger storage engine.
- MONGO_42_WT: version of the MongoDB 4.2 WiredTiger storage engine.
- MONGO_44_WT: version of the MongoDB 4.4 WiredTiger storage engine.
- MONGO_50_WT: version of the MongoDB 5.0 WiredTiger storage engine.
- MONGO_60_WT: version of the MongoDB 6.0 WiredTiger storage engine.
- MONGO_70_WT: version of the MongoDB 7.0 WiredTiger storage engine.
        :rtype: str
        """
        return self._MongoVersion

    @MongoVersion.setter
    def MongoVersion(self, MongoVersion):
        self._MongoVersion = MongoVersion

    @property
    def GoodsNum(self):
        r"""Number of instances. The minimum value is 1, and the maximum value is 30.
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def Zone(self):
        r"""AZ information. Format: ap-guangzhou-2.
 - Call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API to obtain the specific information.
 - This parameter indicates the primary AZ. If multi-AZ deployment is adopted, the value of Zone should be one of the values of AvailabilityZoneList.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Period(self):
        r"""Specifies the purchase duration during the instance purchase, in months. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, and 36.
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def MachineCode(self):
        r"""Product specification type.
 - HIO10G: general high-I/O 10GE type.
 - HCD: cloud disk type.
        :rtype: str
        """
        return self._MachineCode

    @MachineCode.setter
    def MachineCode(self, MachineCode):
        self._MachineCode = MachineCode

    @property
    def ClusterType(self):
        r"""Instance architecture type.
 - REPLSET: replica set.
 - SHARD: sharded cluster.
        :rtype: str
        """
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def ReplicateSetNum(self):
        r""" - Specifies the number of replica sets during replica set instance creation. This parameter can only be set to 1.
 - Specifies the number of shards during sharded cluster instance creation. Call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API to query the range of shard quantity. The parameters MinReplicateSetNum and MaxReplicateSetNum in the returned data structure SpecItems correspond to the minimum value and maximum value, respectively.
        :rtype: int
        """
        return self._ReplicateSetNum

    @ReplicateSetNum.setter
    def ReplicateSetNum(self, ReplicateSetNum):
        self._ReplicateSetNum = ReplicateSetNum

    @property
    def ProjectId(self):
        r"""Project ID.  - The default project is used if this parameter is not specified.
 - The project ID can be obtained on the [project management page in the TencentDB for MongoDB console](https://console.cloud.tencent.com/project).
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def VpcId(self):
        r"""VPC ID.
- Only VPC configuration is supported, and a VPC in the same region as the instance should be selected. Log in to the [VPC console](https://console.cloud.tencent.com/vpc) to obtain the available VPC ID.
- After successful instance creation, VPCs can be changed. For detailed operations, see [Changing the Network](https://www.tencentcloud.comom/document/product/239/30910?from_cn_redirect=1).
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""Subnet ID of the VPC.
- A subnet should be specified within the selected VPC. Log in to the [VPC console](https://console.cloud.tencent.com/vpc) to obtain the available subnet ID.
- After successful instance creation, VPCs and subnets can be changed. For detailed operations, see [Changing the Network](https://www.tencentcloud.comom/document/product/239/30910?from_cn_redirect=1).
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Password(self):
        r"""Instance password. The requirements are as follows:
 - The number of characters should be in the range of [8, 32].
 - Characters within the ranges [A,Z], [a,z], and [0,9] are allowed.
 - Special characters that can be entered include exclamation marks (!), at signs (@), number signs (#), percent signs (%), carets (^), asterisks (\*), brackets (()), and underscores (_).
 - It cannot contain only the same letters or digits.
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Tags(self):
        r"""Instance tag information.
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoRenewFlag(self):
        r"""Automatic renewal flag.
 - 0: no automatic renewal.
 - 1: automatic renewal.
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def AutoVoucher(self):
        r"""Whether to automatically select a voucher.
 - 1: yes.
 - 0: no. Default value: 0.
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def Clone(self):
        r"""Instance type.
- 1: formal instance.
- 3: read-only instance.
- 4: disaster recovery instance.
- 5: cloned instance. Note: For a cloned instance, RestoreTime is required.
        :rtype: int
        """
        return self._Clone

    @Clone.setter
    def Clone(self, Clone):
        self._Clone = Clone

    @property
    def Father(self):
        r"""Parent instance ID.
- This parameter is required when the value of the **Clone** parameter is set to 3 or 4, indicating a read-only or disaster recovery instance.
- Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the parent instance ID from the instance list.
        :rtype: str
        """
        return self._Father

    @Father.setter
    def Father(self, Father):
        self._Father = Father

    @property
    def SecurityGroup(self):
        r"""Security group ID. Log in to the [security group console](https://console.cloud.tencent.com/vpc/security-group) to obtain the ID of the security group in the same region as the database instance.
        :rtype: list of str
        """
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def RestoreTime(self):
        r"""Rollback time of the cloned instance. It is required when the Clone value is 5 or 6. - This parameter is required for cloned instances. Format: 2021-08-13 16:30:00. - Rollback time range: Only data within the last 7 days can be rolled back.
        :rtype: str
        """
        return self._RestoreTime

    @RestoreTime.setter
    def RestoreTime(self, RestoreTime):
        self._RestoreTime = RestoreTime

    @property
    def InstanceName(self):
        r"""Instance name. Only Chinese characters, letters, digits, underscores (_), and delimiters (-) are supported, with a length of 128 characters. When database instances are purchased in batches, the automatic ascending feature is supported through the custom naming pattern string and numeric suffix to set instance names efficiently.
- Basic mode: prefix + automatic ascending number (starting from 1 by default). Only a custom instance name prefix is required for **lnstanceName**. For example, it can be set to cmgo. If the purchase quantity is set to 5, after purchase, the instances will be sequentially named cmgo1, cmgo2, cmgo3, cmgo4, and cmgo5, respectively.
- Custom starting number mode: prefix + {R:x} (x is the custom starting number). Prefix{R:x} is required for **InstanceName**. For example, cmgo{R:3}. If the purchase quantity is set to 5, the instance names will be sequentially named cmgo3, cmgo4, cmgo5, cmgo6, and cmgo7.
- Composite pattern string: prefix 1{R:x} + prefix 2{R:y}+ ⋯ + fixed suffix, where x and y are the starting numbers of each prefix. A composite pattern string is required for **instanceName**. For example, cmgo{R:10}\_node{R:12}\_db. If the batch purchase quantity is set to 5, the instances will be sequentially named cmgo10\_node12\_db, cmgo11\_node13\_db, cmgo12\_node14\_db, cmgo13\_node15\_db, and cmgo14\_node16\_db.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AvailabilityZoneList(self):
        r"""Specifies the list of AZs during multi-AZ deployment of TencentDB for MongoDB instances.
 - For instances in multi-AZ deployment mode, the **Zone** parameter specifies the primary AZ, and **AvailabilityZoneList** specifies all AZs, including the primary AZ. Format: [ap-guangzhou-2,ap-guangzhou-3,ap-guangzhou-4].
 - The [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API can be called to obtain AZs planned for TencentDB for MongoDB instances in different regions, helping you specify valid AZs.
 - Nodes in multi-AZ deployment mode can only be deployed in 3 different AZs. Deploying most nodes of a cluster in the same AZ is not supported. For example, a 3-node cluster does not support deploying 2 nodes in the same AZ.
        :rtype: list of str
        """
        return self._AvailabilityZoneList

    @AvailabilityZoneList.setter
    def AvailabilityZoneList(self, AvailabilityZoneList):
        self._AvailabilityZoneList = AvailabilityZoneList

    @property
    def MongosCpu(self):
        r"""Number of Mongos node CPU cores. Valid values: 1, 2, 4, 8, and 16. This parameter is required during sharded cluster instance purchase.
        :rtype: int
        """
        return self._MongosCpu

    @MongosCpu.setter
    def MongosCpu(self, MongosCpu):
        self._MongosCpu = MongosCpu

    @property
    def MongosMemory(self):
        r"""Mongos node memory size.
 - This parameter is required during sharded cluster instance purchase.
 - Unit: GB. 1-core 2GB, 2-core 4GB, 4-core 8GB, 8-core 16GB, and 16-core 32GB are supported.
        :rtype: int
        """
        return self._MongosMemory

    @MongosMemory.setter
    def MongosMemory(self, MongosMemory):
        self._MongosMemory = MongosMemory

    @property
    def MongosNodeNum(self):
        r"""Number of Mongos nodes. This parameter is required during sharded cluster instance purchase.
 - For instances in single-AZ deployment mode, the value range is [3,32].
 - For instances in multi-AZ deployment mode, the value range is [6,32].
        :rtype: int
        """
        return self._MongosNodeNum

    @MongosNodeNum.setter
    def MongosNodeNum(self, MongosNodeNum):
        self._MongosNodeNum = MongosNodeNum

    @property
    def ReadonlyNodeNum(self):
        r"""Number of read-only nodes. Value ranges: [0,5].
        :rtype: int
        """
        return self._ReadonlyNodeNum

    @ReadonlyNodeNum.setter
    def ReadonlyNodeNum(self, ReadonlyNodeNum):
        self._ReadonlyNodeNum = ReadonlyNodeNum

    @property
    def ReadonlyNodeAvailabilityZoneList(self):
        r"""Array of AZs of read-only nodes. This parameter is required for instances in multi-AZ deployment mode when **ReadonlyNodeNum** is not set to **0**.
        :rtype: list of str
        """
        return self._ReadonlyNodeAvailabilityZoneList

    @ReadonlyNodeAvailabilityZoneList.setter
    def ReadonlyNodeAvailabilityZoneList(self, ReadonlyNodeAvailabilityZoneList):
        self._ReadonlyNodeAvailabilityZoneList = ReadonlyNodeAvailabilityZoneList

    @property
    def HiddenZone(self):
        r"""AZ of the hidden node. This parameter is required for instances in multi-AZ deployment mode.
        :rtype: str
        """
        return self._HiddenZone

    @HiddenZone.setter
    def HiddenZone(self, HiddenZone):
        self._HiddenZone = HiddenZone

    @property
    def ParamTemplateId(self):
        r"""Parameter template ID.
- A parameter template is a collection of predefined parameter values that can be used to quickly configure new MongoDB instances. Proper use of parameter templates can significantly enhance the deployment efficiency and operational performance of the database.
- The [DescribeDBInstanceParamTpl](https://www.tencentcloud.comom/document/product/240/109155?from_cn_redirect=1) API can be called to obtain the parameter template ID. Select the parameter template ID corresponding to the instance version and architecture.
        :rtype: str
        """
        return self._ParamTemplateId

    @ParamTemplateId.setter
    def ParamTemplateId(self, ParamTemplateId):
        self._ParamTemplateId = ParamTemplateId


    def _deserialize(self, params):
        self._NodeNum = params.get("NodeNum")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._MongoVersion = params.get("MongoVersion")
        self._GoodsNum = params.get("GoodsNum")
        self._Zone = params.get("Zone")
        self._Period = params.get("Period")
        self._MachineCode = params.get("MachineCode")
        self._ClusterType = params.get("ClusterType")
        self._ReplicateSetNum = params.get("ReplicateSetNum")
        self._ProjectId = params.get("ProjectId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Password = params.get("Password")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._AutoVoucher = params.get("AutoVoucher")
        self._Clone = params.get("Clone")
        self._Father = params.get("Father")
        self._SecurityGroup = params.get("SecurityGroup")
        self._RestoreTime = params.get("RestoreTime")
        self._InstanceName = params.get("InstanceName")
        self._AvailabilityZoneList = params.get("AvailabilityZoneList")
        self._MongosCpu = params.get("MongosCpu")
        self._MongosMemory = params.get("MongosMemory")
        self._MongosNodeNum = params.get("MongosNodeNum")
        self._ReadonlyNodeNum = params.get("ReadonlyNodeNum")
        self._ReadonlyNodeAvailabilityZoneList = params.get("ReadonlyNodeAvailabilityZoneList")
        self._HiddenZone = params.get("HiddenZone")
        self._ParamTemplateId = params.get("ParamTemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBInstanceResponse(AbstractModel):
    r"""CreateDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _DealId: Order ID.
        :type DealId: str
        :param _InstanceIds: List of IDs of created instances.
        :type InstanceIds: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealId = None
        self._InstanceIds = None
        self._RequestId = None

    @property
    def DealId(self):
        r"""Order ID.
        :rtype: str
        """
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def InstanceIds(self):
        r"""List of IDs of created instances.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._InstanceIds = params.get("InstanceIds")
        self._RequestId = params.get("RequestId")


class CreateLogDownloadTaskRequest(AbstractModel):
    r"""CreateLogDownloadTask request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _StartTime: Start time.
        :type StartTime: str
        :param _EndTime: End time.
        :type EndTime: str
        :param _NodeNames: Node name.
        :type NodeNames: list of str
        :param _LogComponents: Log category.
        :type LogComponents: list of str
        :param _LogLevels: Log level.
        :type LogLevels: list of str
        :param _LogIds: Log ID.
        :type LogIds: list of str
        :param _LogConnections: Log connection information.
        :type LogConnections: list of str
        :param _LogDetailParams: Filtering fields for log details.
        :type LogDetailParams: list of str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._NodeNames = None
        self._LogComponents = None
        self._LogLevels = None
        self._LogIds = None
        self._LogConnections = None
        self._LogDetailParams = None

    @property
    def InstanceId(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        r"""Start time.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def NodeNames(self):
        r"""Node name.
        :rtype: list of str
        """
        return self._NodeNames

    @NodeNames.setter
    def NodeNames(self, NodeNames):
        self._NodeNames = NodeNames

    @property
    def LogComponents(self):
        r"""Log category.
        :rtype: list of str
        """
        return self._LogComponents

    @LogComponents.setter
    def LogComponents(self, LogComponents):
        self._LogComponents = LogComponents

    @property
    def LogLevels(self):
        r"""Log level.
        :rtype: list of str
        """
        return self._LogLevels

    @LogLevels.setter
    def LogLevels(self, LogLevels):
        self._LogLevels = LogLevels

    @property
    def LogIds(self):
        r"""Log ID.
        :rtype: list of str
        """
        return self._LogIds

    @LogIds.setter
    def LogIds(self, LogIds):
        self._LogIds = LogIds

    @property
    def LogConnections(self):
        r"""Log connection information.
        :rtype: list of str
        """
        return self._LogConnections

    @LogConnections.setter
    def LogConnections(self, LogConnections):
        self._LogConnections = LogConnections

    @property
    def LogDetailParams(self):
        r"""Filtering fields for log details.
        :rtype: list of str
        """
        return self._LogDetailParams

    @LogDetailParams.setter
    def LogDetailParams(self, LogDetailParams):
        self._LogDetailParams = LogDetailParams


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._NodeNames = params.get("NodeNames")
        self._LogComponents = params.get("LogComponents")
        self._LogLevels = params.get("LogLevels")
        self._LogIds = params.get("LogIds")
        self._LogConnections = params.get("LogConnections")
        self._LogDetailParams = params.get("LogDetailParams")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLogDownloadTaskResponse(AbstractModel):
    r"""CreateLogDownloadTask response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Task status.
        :type Status: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""Task status.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class CurrentOp(AbstractModel):
    r"""Current operation on the TencentDB for MongoDB instance.

    """

    def __init__(self):
        r"""
        :param _OpId: Operation number.
        :type OpId: int
        :param _Ns: Namespace where the operation is located, in the format of db.collection.
        :type Ns: str
        :param _Query: Execution statement of the operation.
        :type Query: str
        :param _Op: Operation type.
- none: special status; idle connections or internal tasks.
- update: update data.
- insert: insertion operation.
- query: query operation.
- command: command operation.
- getmore: obtain more data.
- remove: deletion operation.
- killcursors: operation of releasing the query cursor.
        :type Op: str
        :param _ReplicaSetName: Name of the shard where the operation is performed.
        :type ReplicaSetName: str
        :param _NodeName: Name of the node where the operation is performed.
        :type NodeName: str
        :param _Operation: Detailed information about the operation.
        :type Operation: str
        :param _State: Node role.
- primary: primary node.
- secondary: secondary node.
        :type State: str
        :param _MicrosecsRunning: Execution time of the operation, in ms.
        :type MicrosecsRunning: int
        :param _ExecNode: Information about the node where the current operation is performed.
        :type ExecNode: str
        """
        self._OpId = None
        self._Ns = None
        self._Query = None
        self._Op = None
        self._ReplicaSetName = None
        self._NodeName = None
        self._Operation = None
        self._State = None
        self._MicrosecsRunning = None
        self._ExecNode = None

    @property
    def OpId(self):
        r"""Operation number.
        :rtype: int
        """
        return self._OpId

    @OpId.setter
    def OpId(self, OpId):
        self._OpId = OpId

    @property
    def Ns(self):
        r"""Namespace where the operation is located, in the format of db.collection.
        :rtype: str
        """
        return self._Ns

    @Ns.setter
    def Ns(self, Ns):
        self._Ns = Ns

    @property
    def Query(self):
        r"""Execution statement of the operation.
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Op(self):
        r"""Operation type.
- none: special status; idle connections or internal tasks.
- update: update data.
- insert: insertion operation.
- query: query operation.
- command: command operation.
- getmore: obtain more data.
- remove: deletion operation.
- killcursors: operation of releasing the query cursor.
        :rtype: str
        """
        return self._Op

    @Op.setter
    def Op(self, Op):
        self._Op = Op

    @property
    def ReplicaSetName(self):
        r"""Name of the shard where the operation is performed.
        :rtype: str
        """
        return self._ReplicaSetName

    @ReplicaSetName.setter
    def ReplicaSetName(self, ReplicaSetName):
        self._ReplicaSetName = ReplicaSetName

    @property
    def NodeName(self):
        r"""Name of the node where the operation is performed.
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def Operation(self):
        r"""Detailed information about the operation.
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def State(self):
        r"""Node role.
- primary: primary node.
- secondary: secondary node.
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def MicrosecsRunning(self):
        r"""Execution time of the operation, in ms.
        :rtype: int
        """
        return self._MicrosecsRunning

    @MicrosecsRunning.setter
    def MicrosecsRunning(self, MicrosecsRunning):
        self._MicrosecsRunning = MicrosecsRunning

    @property
    def ExecNode(self):
        r"""Information about the node where the current operation is performed.
        :rtype: str
        """
        return self._ExecNode

    @ExecNode.setter
    def ExecNode(self, ExecNode):
        self._ExecNode = ExecNode


    def _deserialize(self, params):
        self._OpId = params.get("OpId")
        self._Ns = params.get("Ns")
        self._Query = params.get("Query")
        self._Op = params.get("Op")
        self._ReplicaSetName = params.get("ReplicaSetName")
        self._NodeName = params.get("NodeName")
        self._Operation = params.get("Operation")
        self._State = params.get("State")
        self._MicrosecsRunning = params.get("MicrosecsRunning")
        self._ExecNode = params.get("ExecNode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBInstanceInfo(AbstractModel):
    r"""Instance information

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Region: Region information
        :type Region: str
        """
        self._InstanceId = None
        self._Region = None

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Region(self):
        r"""Region information
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBInstancePrice(AbstractModel):
    r"""Instance price

    """

    def __init__(self):
        r"""
        :param _UnitPrice: Unit price of the instance, in USD.
        :type UnitPrice: float
        :param _OriginalPrice: Original price of the instance, in USD.
        :type OriginalPrice: float
        :param _DiscountPrice: Discount price of the instance, in USD.
        :type DiscountPrice: float
        """
        self._UnitPrice = None
        self._OriginalPrice = None
        self._DiscountPrice = None

    @property
    def UnitPrice(self):
        r"""Unit price of the instance, in USD.
        :rtype: float
        """
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def OriginalPrice(self):
        r"""Original price of the instance, in USD.
        :rtype: float
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def DiscountPrice(self):
        r"""Discount price of the instance, in USD.
        :rtype: float
        """
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice


    def _deserialize(self, params):
        self._UnitPrice = params.get("UnitPrice")
        self._OriginalPrice = params.get("OriginalPrice")
        self._DiscountPrice = params.get("DiscountPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountUserRequest(AbstractModel):
    r"""DeleteAccountUser request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Specifies the instance ID for the account to be deleted. For example, cmgo-p8vn****. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.

        :type InstanceId: str
        :param _UserName: Configures the name of the account to be deleted.
        :type UserName: str
        :param _MongoUserPassword: Configures the password corresponding to the mongouser account. mongouser is the default account of the system. Enter the password corresponding to it.
        :type MongoUserPassword: str
        """
        self._InstanceId = None
        self._UserName = None
        self._MongoUserPassword = None

    @property
    def InstanceId(self):
        r"""Specifies the instance ID for the account to be deleted. For example, cmgo-p8vn****. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.

        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        r"""Configures the name of the account to be deleted.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def MongoUserPassword(self):
        r"""Configures the password corresponding to the mongouser account. mongouser is the default account of the system. Enter the password corresponding to it.
        :rtype: str
        """
        return self._MongoUserPassword

    @MongoUserPassword.setter
    def MongoUserPassword(self, MongoUserPassword):
        self._MongoUserPassword = MongoUserPassword


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._MongoUserPassword = params.get("MongoUserPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountUserResponse(AbstractModel):
    r"""DeleteAccountUser response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Account deletion task ID.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Account deletion task ID.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class DeleteLogDownloadTaskRequest(AbstractModel):
    r"""DeleteLogDownloadTask request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _TaskId: Task ID.
        :type TaskId: str
        """
        self._InstanceId = None
        self._TaskId = None

    @property
    def InstanceId(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TaskId(self):
        r"""Task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLogDownloadTaskResponse(AbstractModel):
    r"""DeleteLogDownloadTask response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Task status. 0: successful.
        :type Status: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""Task status. 0: successful.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeAsyncRequestInfoRequest(AbstractModel):
    r"""DescribeAsyncRequestInfo request structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Specifies the ID of the asynchronous request to be queried. When an asynchronous process is involved in the API operation (such as [CreateBackupDBInstance](https://www.tencentcloud.comom/document/product/240/46599?from_cn_redirect=1)), the response value of AsyncRequestId is the ID to be filled in for this parameter.
        :type AsyncRequestId: str
        """
        self._AsyncRequestId = None

    @property
    def AsyncRequestId(self):
        r"""Specifies the ID of the asynchronous request to be queried. When an asynchronous process is involved in the API operation (such as [CreateBackupDBInstance](https://www.tencentcloud.comom/document/product/240/46599?from_cn_redirect=1)), the response value of AsyncRequestId is the ID to be filled in for this parameter.
        :rtype: str
        """
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAsyncRequestInfoResponse(AbstractModel):
    r"""DescribeAsyncRequestInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Status. Valid values: `initial` (initializing), `running`, `paused` (paused due to failure), `undoed` (rolled back due to failure), `failed` (ended due to failure), `success`
        :type Status: str
        :param _StartTime: Task execution start time.
        :type StartTime: str
        :param _EndTime: Task execution end time.
        :type EndTime: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._StartTime = None
        self._EndTime = None
        self._RequestId = None

    @property
    def Status(self):
        r"""Status. Valid values: `initial` (initializing), `running`, `paused` (paused due to failure), `undoed` (rolled back due to failure), `failed` (ended due to failure), `success`
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        r"""Task execution start time.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Task execution end time.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RequestId = params.get("RequestId")


class DescribeBackupDownloadTaskRequest(AbstractModel):
    r"""DescribeBackupDownloadTask request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :type InstanceId: str
        :param _BackupName: Specifies the backup file name for filtering download tasks of the specified file. The [DescribeDBBackups](https://www.tencentcloud.comom/document/product/240/38574?from_cn_redirect=1) API can be called to obtain the backup file name.
        :type BackupName: str
        :param _StartTime: Specifies the task within the query time range, and StartTime specifies the start time. If not specified, there are no limitations on the start time by default.
        :type StartTime: str
        :param _EndTime: Specifies the task within the query time range, and EndTime specifies the end time. If not specified, there are no limitations on the end time by default.
        :type EndTime: str
        :param _Limit: Number of entries returned for this query. Value range: 1–100. The default value is 20.
        :type Limit: int
        :param _Offset: Specifies the number of pages returned for this query. The default value is 0.
        :type Offset: int
        :param _OrderBy: Sorting field.
- createTime: sort by the creation time of the backup download task. The default value is createTime.
- finishTime: sort by the completion time of the backup download task.
        :type OrderBy: str
        :param _OrderByType: Sorting method.
- asc: ascending order.
- desc: descending order. The default value is desc.
        :type OrderByType: str
        :param _Status: Specifies the task status for filtering download tasks. If this parameter is not configured, tasks of all status types will be returned.
- 0: wait for execution.
- 1: downloading.
- 2: download completed.
- 3: download failed.
- 4: wait for retry.
        :type Status: list of int
        """
        self._InstanceId = None
        self._BackupName = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None
        self._Status = None

    @property
    def InstanceId(self):
        r"""Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupName(self):
        r"""Specifies the backup file name for filtering download tasks of the specified file. The [DescribeDBBackups](https://www.tencentcloud.comom/document/product/240/38574?from_cn_redirect=1) API can be called to obtain the backup file name.
        :rtype: str
        """
        return self._BackupName

    @BackupName.setter
    def BackupName(self, BackupName):
        self._BackupName = BackupName

    @property
    def StartTime(self):
        r"""Specifies the task within the query time range, and StartTime specifies the start time. If not specified, there are no limitations on the start time by default.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Specifies the task within the query time range, and EndTime specifies the end time. If not specified, there are no limitations on the end time by default.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        r"""Number of entries returned for this query. Value range: 1–100. The default value is 20.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Specifies the number of pages returned for this query. The default value is 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""Sorting field.
- createTime: sort by the creation time of the backup download task. The default value is createTime.
- finishTime: sort by the completion time of the backup download task.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""Sorting method.
- asc: ascending order.
- desc: descending order. The default value is desc.
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Status(self):
        r"""Specifies the task status for filtering download tasks. If this parameter is not configured, tasks of all status types will be returned.
- 0: wait for execution.
- 1: downloading.
- 2: download completed.
- 3: download failed.
- 4: wait for retry.
        :rtype: list of int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupName = params.get("BackupName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupDownloadTaskResponse(AbstractModel):
    r"""DescribeBackupDownloadTask response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: All entries that meet the query conditions.
        :type TotalCount: int
        :param _Tasks: Download task list.
        :type Tasks: list of BackupDownloadTask
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""All entries that meet the query conditions.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tasks(self):
        r"""Download task list.
        :rtype: list of BackupDownloadTask
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = BackupDownloadTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBackupRulesRequest(AbstractModel):
    r"""DescribeBackupRules request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Specifies the instance ID. For example, cmgo-p8vn****. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Specifies the instance ID. For example, cmgo-p8vn****. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :rtype: str
        """
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
        


class DescribeBackupRulesResponse(AbstractModel):
    r"""DescribeBackupRules response structure.

    """

    def __init__(self):
        r"""
        :param _BackupSaveTime: Retention period for backup data, in days.
        :type BackupSaveTime: int
        :param _BackupTime: Automatic backup start time.
        :type BackupTime: int
        :param _BackupMethod: Backup method.
- 0: logical backup.
- 1: physical backup.
        :type BackupMethod: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BackupSaveTime = None
        self._BackupTime = None
        self._BackupMethod = None
        self._RequestId = None

    @property
    def BackupSaveTime(self):
        r"""Retention period for backup data, in days.
        :rtype: int
        """
        return self._BackupSaveTime

    @BackupSaveTime.setter
    def BackupSaveTime(self, BackupSaveTime):
        self._BackupSaveTime = BackupSaveTime

    @property
    def BackupTime(self):
        r"""Automatic backup start time.
        :rtype: int
        """
        return self._BackupTime

    @BackupTime.setter
    def BackupTime(self, BackupTime):
        self._BackupTime = BackupTime

    @property
    def BackupMethod(self):
        r"""Backup method.
- 0: logical backup.
- 1: physical backup.
        :rtype: int
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BackupSaveTime = params.get("BackupSaveTime")
        self._BackupTime = params.get("BackupTime")
        self._BackupMethod = params.get("BackupMethod")
        self._RequestId = params.get("RequestId")


class DescribeClientConnectionsRequest(AbstractModel):
    r"""DescribeClientConnections request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Specifies the ID of the instance to be queried. For example, cmgo-p8vn****. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/MongoDB) and copy the instance ID from the instance list.

        :type InstanceId: str
        :param _Limit: Number of entries returned per request. Minimum value: 1. Maximum value: 1000. Default value: 1000.
        :type Limit: int
        :param _Offset: Offset. Default value: 0. Offset = Limit x (page number - 1).
        :type Offset: int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        r"""Specifies the ID of the instance to be queried. For example, cmgo-p8vn****. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/MongoDB) and copy the instance ID from the instance list.

        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        r"""Number of entries returned per request. Minimum value: 1. Maximum value: 1000. Default value: 1000.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset. Default value: 0. Offset = Limit x (page number - 1).
        :rtype: int
        """
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
        


class DescribeClientConnectionsResponse(AbstractModel):
    r"""DescribeClientConnections response structure.

    """

    def __init__(self):
        r"""
        :param _Clients: Client connection information, including the numbers of connections of the client IP address and the database access IP address.
        :type Clients: list of ClientConnection
        :param _TotalCount: The total number of records that meet the query condition, which can be used for paginated queries.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Clients = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Clients(self):
        r"""Client connection information, including the numbers of connections of the client IP address and the database access IP address.
        :rtype: list of ClientConnection
        """
        return self._Clients

    @Clients.setter
    def Clients(self, Clients):
        self._Clients = Clients

    @property
    def TotalCount(self):
        r"""The total number of records that meet the query condition, which can be used for paginated queries.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Clients") is not None:
            self._Clients = []
            for item in params.get("Clients"):
                obj = ClientConnection()
                obj._deserialize(item)
                self._Clients.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCurrentOpRequest(AbstractModel):
    r"""DescribeCurrentOp request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Specifies the instance ID to be queried. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :type InstanceId: str
        :param _Ns: Namespace where the operation belongs, in the format of db.collection.
        :type Ns: str
        :param _MillisecondRunning: Sets the query and filtering condition to the execution time of the operation task.
- The default value is 0, and the value range is [0, 3600000], in milliseconds.
- The result will return the operation whose execution time exceeds the set time.
        :type MillisecondRunning: int
        :param _Op: Sets the query and filtering condition to the type of the operation task. Valid values:
- none: special status; idle connections or internal tasks.
- update: update data.
- insert: insertion operation.
- query: query operation.
- command: command operation.
- getmore: obtain more data.
- remove: deletion operation.
- killcursors: operation of releasing the query cursor.
        :type Op: str
        :param _ReplicaSetName: Filtering condition, such as the shard name.
        :type ReplicaSetName: str
        :param _State: Sets the query and filtering condition to the node role.
- primary: primary node.
- secondary: secondary node.
        :type State: str
        :param _Limit: Number of entries returned per request. The default value is 100, and the value range is [0, 100].
        :type Limit: int
        :param _Offset: Offset. The default value is 0, and the value range is [0, 10000].
        :type Offset: int
        :param _OrderBy: Sorting field of the returned result set. Currently, sorting by MicrosecsRunning (execution time of the operation task) is supported.
        :type OrderBy: str
        :param _OrderByType: Sorting method of the returned result set.
- ASC: ascending order. The default value is ASC, which indicates sorting in ascending order.
- DESC: descending order.
        :type OrderByType: str
        """
        self._InstanceId = None
        self._Ns = None
        self._MillisecondRunning = None
        self._Op = None
        self._ReplicaSetName = None
        self._State = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def InstanceId(self):
        r"""Specifies the instance ID to be queried. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ns(self):
        r"""Namespace where the operation belongs, in the format of db.collection.
        :rtype: str
        """
        return self._Ns

    @Ns.setter
    def Ns(self, Ns):
        self._Ns = Ns

    @property
    def MillisecondRunning(self):
        r"""Sets the query and filtering condition to the execution time of the operation task.
- The default value is 0, and the value range is [0, 3600000], in milliseconds.
- The result will return the operation whose execution time exceeds the set time.
        :rtype: int
        """
        return self._MillisecondRunning

    @MillisecondRunning.setter
    def MillisecondRunning(self, MillisecondRunning):
        self._MillisecondRunning = MillisecondRunning

    @property
    def Op(self):
        r"""Sets the query and filtering condition to the type of the operation task. Valid values:
- none: special status; idle connections or internal tasks.
- update: update data.
- insert: insertion operation.
- query: query operation.
- command: command operation.
- getmore: obtain more data.
- remove: deletion operation.
- killcursors: operation of releasing the query cursor.
        :rtype: str
        """
        return self._Op

    @Op.setter
    def Op(self, Op):
        self._Op = Op

    @property
    def ReplicaSetName(self):
        r"""Filtering condition, such as the shard name.
        :rtype: str
        """
        return self._ReplicaSetName

    @ReplicaSetName.setter
    def ReplicaSetName(self, ReplicaSetName):
        self._ReplicaSetName = ReplicaSetName

    @property
    def State(self):
        r"""Sets the query and filtering condition to the node role.
- primary: primary node.
- secondary: secondary node.
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Limit(self):
        r"""Number of entries returned per request. The default value is 100, and the value range is [0, 100].
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset. The default value is 0, and the value range is [0, 10000].
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""Sorting field of the returned result set. Currently, sorting by MicrosecsRunning (execution time of the operation task) is supported.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""Sorting method of the returned result set.
- ASC: ascending order. The default value is ASC, which indicates sorting in ascending order.
- DESC: descending order.
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Ns = params.get("Ns")
        self._MillisecondRunning = params.get("MillisecondRunning")
        self._Op = params.get("Op")
        self._ReplicaSetName = params.get("ReplicaSetName")
        self._State = params.get("State")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCurrentOpResponse(AbstractModel):
    r"""DescribeCurrentOp response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of operations meeting the query conditions.
        :type TotalCount: int
        :param _CurrentOps: List of the current operations.
        :type CurrentOps: list of CurrentOp
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._CurrentOps = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of operations meeting the query conditions.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def CurrentOps(self):
        r"""List of the current operations.
        :rtype: list of CurrentOp
        """
        return self._CurrentOps

    @CurrentOps.setter
    def CurrentOps(self, CurrentOps):
        self._CurrentOps = CurrentOps

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("CurrentOps") is not None:
            self._CurrentOps = []
            for item in params.get("CurrentOps"):
                obj = CurrentOp()
                obj._deserialize(item)
                self._CurrentOps.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBBackupsRequest(AbstractModel):
    r"""DescribeDBBackups request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :type InstanceId: str
        :param _BackupMethod: Backup method.
- 0: logical backup.
- 1: physical backup.
- 3: snapshot backup.
**Note**:
1. The General Edition instance supports logical and physical backup. The Cloud Disk Edition instance supports physical and snapshot backup, but does not support logical backup currently.
2. Physical backup is not supported when storage encryption is enabled for the instance.
        :type BackupMethod: int
        :param _Limit: Number of entries per page. Maximum value: `100`. If this parameter is left empty, all entries will be returned.
        :type Limit: int
        :param _Offset: Pagination offset, starting from `0`. Default value: `0`.
        :type Offset: int
        """
        self._InstanceId = None
        self._BackupMethod = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        r"""Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def BackupMethod(self):
        r"""Backup method.
- 0: logical backup.
- 1: physical backup.
- 3: snapshot backup.
**Note**:
1. The General Edition instance supports logical and physical backup. The Cloud Disk Edition instance supports physical and snapshot backup, but does not support logical backup currently.
2. Physical backup is not supported when storage encryption is enabled for the instance.
        :rtype: int
        """
        return self._BackupMethod

    @BackupMethod.setter
    def BackupMethod(self, BackupMethod):
        self._BackupMethod = BackupMethod

    @property
    def Limit(self):
        r"""Number of entries per page. Maximum value: `100`. If this parameter is left empty, all entries will be returned.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Pagination offset, starting from `0`. Default value: `0`.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._BackupMethod = params.get("BackupMethod")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBBackupsResponse(AbstractModel):
    r"""DescribeDBBackups response structure.

    """

    def __init__(self):
        r"""
        :param _BackupList: Backup list.
        :type BackupList: list of BackupInfo
        :param _TotalCount: Number of backups.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BackupList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def BackupList(self):
        r"""Backup list.
        :rtype: list of BackupInfo
        """
        return self._BackupList

    @BackupList.setter
    def BackupList(self, BackupList):
        self._BackupList = BackupList

    @property
    def TotalCount(self):
        r"""Number of backups.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BackupList") is not None:
            self._BackupList = []
            for item in params.get("BackupList"):
                obj = BackupInfo()
                obj._deserialize(item)
                self._BackupList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceDealRequest(AbstractModel):
    r"""DescribeDBInstanceDeal request structure.

    """

    def __init__(self):
        r"""
        :param _DealId: Order ID.
- Pay-as-you-go instance. It can be obtained through the output parameter **DealId** of the [CreateDBInstanceHour](https://www.tencentcloud.comom/document/product/240/38570?from_cn_redirect=1) API.
- Yearly/monthly subscription instance. It can be obtained through the output parameter **DealId** of the [CreateDBInstance](https://www.tencentcloud.comom/document/product/240/38571?from_cn_redirect=1) API.
        :type DealId: str
        """
        self._DealId = None

    @property
    def DealId(self):
        r"""Order ID.
- Pay-as-you-go instance. It can be obtained through the output parameter **DealId** of the [CreateDBInstanceHour](https://www.tencentcloud.comom/document/product/240/38570?from_cn_redirect=1) API.
- Yearly/monthly subscription instance. It can be obtained through the output parameter **DealId** of the [CreateDBInstance](https://www.tencentcloud.comom/document/product/240/38571?from_cn_redirect=1) API.
        :rtype: str
        """
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceDealResponse(AbstractModel):
    r"""DescribeDBInstanceDeal response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Order status.
- 1: unpaid.
- 2: paid.
- 3: delivering.
- 4: delivered successfully.
- 5: delivery failed.
- 6: refund.
- 7: order closed.
- 8: closed due to unpaid timeout.
        :type Status: int
        :param _OriginalPrice: Original price of the order, in USD.
        :type OriginalPrice: float
        :param _DiscountPrice: Discount price of the order, in USD.
        :type DiscountPrice: float
        :param _Action: Order operation behavior.
- purchase: newly purchased.
- renew: renewed.
- upgrade: configuration upgraded.
- downgrade: configuration downgraded.
- refund: return and refund.
        :type Action: str
        :param _InstanceId: Instance ID of the current order.
        :type InstanceId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._OriginalPrice = None
        self._DiscountPrice = None
        self._Action = None
        self._InstanceId = None
        self._RequestId = None

    @property
    def Status(self):
        r"""Order status.
- 1: unpaid.
- 2: paid.
- 3: delivering.
- 4: delivered successfully.
- 5: delivery failed.
- 6: refund.
- 7: order closed.
- 8: closed due to unpaid timeout.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OriginalPrice(self):
        r"""Original price of the order, in USD.
        :rtype: float
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def DiscountPrice(self):
        r"""Discount price of the order, in USD.
        :rtype: float
        """
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def Action(self):
        r"""Order operation behavior.
- purchase: newly purchased.
- renew: renewed.
- upgrade: configuration upgraded.
- downgrade: configuration downgraded.
- refund: return and refund.
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def InstanceId(self):
        r"""Instance ID of the current order.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._OriginalPrice = params.get("OriginalPrice")
        self._DiscountPrice = params.get("DiscountPrice")
        self._Action = params.get("Action")
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceNamespaceRequest(AbstractModel):
    r"""DescribeDBInstanceNamespace request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Specifies the instance ID for querying the database. Batch querying is supported. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/MongoDB) and copy the instance ID from the instance list.
        :type InstanceId: str
        :param _DbName: Specifies the database name for querying. If this parameter is left blank, a list of all databases of the current instance is returned.
        :type DbName: str
        """
        self._InstanceId = None
        self._DbName = None

    @property
    def InstanceId(self):
        r"""Specifies the instance ID for querying the database. Batch querying is supported. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/MongoDB) and copy the instance ID from the instance list.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DbName(self):
        r"""Specifies the database name for querying. If this parameter is left blank, a list of all databases of the current instance is returned.
        :rtype: str
        """
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DbName = params.get("DbName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceNamespaceResponse(AbstractModel):
    r"""DescribeDBInstanceNamespace response structure.

    """

    def __init__(self):
        r"""
        :param _Databases: List of databases of the queried instance. If no database is specified for querying with DbName, a list of databases of only the queried instance is returned instead of the information indicated by Collections.
        :type Databases: list of str
        :param _Collections: Queried collection information. If DbName is specified, a list of collections of only this database is returned.
        :type Collections: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Databases = None
        self._Collections = None
        self._RequestId = None

    @property
    def Databases(self):
        r"""List of databases of the queried instance. If no database is specified for querying with DbName, a list of databases of only the queried instance is returned instead of the information indicated by Collections.
        :rtype: list of str
        """
        return self._Databases

    @Databases.setter
    def Databases(self, Databases):
        self._Databases = Databases

    @property
    def Collections(self):
        r"""Queried collection information. If DbName is specified, a list of collections of only this database is returned.
        :rtype: list of str
        """
        return self._Collections

    @Collections.setter
    def Collections(self, Collections):
        self._Collections = Collections

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Databases = params.get("Databases")
        self._Collections = params.get("Collections")
        self._RequestId = params.get("RequestId")


class DescribeDBInstanceNodePropertyRequest(AbstractModel):
    r"""DescribeDBInstanceNodeProperty request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :type InstanceId: str
        :param _NodeIds: Node ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), go to Node Management, and copy the node ID.
        :type NodeIds: list of str
        :param _Roles: Node role. Valid values:
- PRIMARY: primary node.
- SECONDARY: secondary node.
- READONLY: read-only node.
- ARBITER: arbitration node.
        :type Roles: list of str
        :param _OnlyHidden: Whether the node is a hidden node. Default value: false.
        :type OnlyHidden: bool
        :param _Priority: Priority of the node for electing it as the new primary node. Value range: [0, 100]. A larger value indicates a higher priority.
        :type Priority: int
        :param _Votes: Node voting right.- 1: The node has the right to vote.
- 0: The node does not have the right to vote.
        :type Votes: int
        :param _Tags: Node tag.
        :type Tags: list of NodeTag
        """
        self._InstanceId = None
        self._NodeIds = None
        self._Roles = None
        self._OnlyHidden = None
        self._Priority = None
        self._Votes = None
        self._Tags = None

    @property
    def InstanceId(self):
        r"""Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NodeIds(self):
        r"""Node ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), go to Node Management, and copy the node ID.
        :rtype: list of str
        """
        return self._NodeIds

    @NodeIds.setter
    def NodeIds(self, NodeIds):
        self._NodeIds = NodeIds

    @property
    def Roles(self):
        r"""Node role. Valid values:
- PRIMARY: primary node.
- SECONDARY: secondary node.
- READONLY: read-only node.
- ARBITER: arbitration node.
        :rtype: list of str
        """
        return self._Roles

    @Roles.setter
    def Roles(self, Roles):
        self._Roles = Roles

    @property
    def OnlyHidden(self):
        r"""Whether the node is a hidden node. Default value: false.
        :rtype: bool
        """
        return self._OnlyHidden

    @OnlyHidden.setter
    def OnlyHidden(self, OnlyHidden):
        self._OnlyHidden = OnlyHidden

    @property
    def Priority(self):
        r"""Priority of the node for electing it as the new primary node. Value range: [0, 100]. A larger value indicates a higher priority.
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Votes(self):
        r"""Node voting right.- 1: The node has the right to vote.
- 0: The node does not have the right to vote.
        :rtype: int
        """
        return self._Votes

    @Votes.setter
    def Votes(self, Votes):
        self._Votes = Votes

    @property
    def Tags(self):
        r"""Node tag.
        :rtype: list of NodeTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NodeIds = params.get("NodeIds")
        self._Roles = params.get("Roles")
        self._OnlyHidden = params.get("OnlyHidden")
        self._Priority = params.get("Priority")
        self._Votes = params.get("Votes")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = NodeTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceNodePropertyResponse(AbstractModel):
    r"""DescribeDBInstanceNodeProperty response structure.

    """

    def __init__(self):
        r"""
        :param _Mongos: Mongos node attributes.
        :type Mongos: list of NodeProperty
        :param _ReplicateSets: Replica set node information.
        :type ReplicateSets: list of ReplicateSetInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Mongos = None
        self._ReplicateSets = None
        self._RequestId = None

    @property
    def Mongos(self):
        r"""Mongos node attributes.
        :rtype: list of NodeProperty
        """
        return self._Mongos

    @Mongos.setter
    def Mongos(self, Mongos):
        self._Mongos = Mongos

    @property
    def ReplicateSets(self):
        r"""Replica set node information.
        :rtype: list of ReplicateSetInfo
        """
        return self._ReplicateSets

    @ReplicateSets.setter
    def ReplicateSets(self, ReplicateSets):
        self._ReplicateSets = ReplicateSets

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Mongos") is not None:
            self._Mongos = []
            for item in params.get("Mongos"):
                obj = NodeProperty()
                obj._deserialize(item)
                self._Mongos.append(obj)
        if params.get("ReplicateSets") is not None:
            self._ReplicateSets = []
            for item in params.get("ReplicateSets"):
                obj = ReplicateSetInfo()
                obj._deserialize(item)
                self._ReplicateSets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    r"""DescribeDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID list. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :type InstanceIds: list of str
        :param _InstanceType: Specifies the instance type for querying. Valid values:
- 0: all instances.
- 1: formal instance.
- 2: temporary instance.
- 3: read-only instance.
- -1: the query range includes the formal, read-only, and disaster recovery instances simultaneously.
        :type InstanceType: int
        :param _ClusterType: Specifies the cluster type of the instance to be queried. Valid values:
- 0: replica set instance.
- 1: sharded cluster instance.
- -1: replica set and sharded cluster instance.
        :type ClusterType: int
        :param _Status: Specifies the current status of the instance to be queried. Valid values:
- 0: to be initialized.
- 1: processing, such as specification changes and parameter modifications.
- 2: running normally.
- -2: isolated (yearly/monthly subscription).
- -3: isolated (pay-as-you-go).
        :type Status: list of int
        :param _VpcId: VPC ID.
 - You do not need to specify this parameter for basic networks.
 - Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/MongoDB), click a VPC name in the instance list, and obtain the ID on the **VPC** page.
        :type VpcId: str
        :param _SubnetId: VPC subnet ID.
 - You do not need to specify this parameter for basic networks.
 - Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/MongoDB), click a VPC name in the instance list, and obtain the subnet ID on the **VPC** page.
        :type SubnetId: str
        :param _PayMode: Billing type. Valid value: 0 (pay-as-you-go)
        :type PayMode: int
        :param _Limit: Number of entries returned per request. The default value is 20, and the value range is (1, 100].
        :type Limit: int
        :param _Offset: Offset. Default value: `0`.
        :type Offset: int
        :param _OrderBy: Configures the field for sorting returned results. Currently, "ProjectId", "InstanceName", and "CreateTime" are supported for sorting.
        :type OrderBy: str
        :param _OrderByType: Configures the method for sorting returned results.
 - ASC: ascending order.
 - DESC: descending order.
        :type OrderByType: str
        :param _ProjectIds: Project ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/MongoDB) and select Project Management in the account information drop-down menu at the top right corner to query projects.
        :type ProjectIds: list of int non-negative
        :param _SearchKey: Specifies the keyword for search. Specific instance IDs, instance names, or private IP addresses are supported.
        :type SearchKey: str
        :param _Tags: Tag information, including the tag key and tag value.
        :type Tags: list of TagInfo
        """
        self._InstanceIds = None
        self._InstanceType = None
        self._ClusterType = None
        self._Status = None
        self._VpcId = None
        self._SubnetId = None
        self._PayMode = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None
        self._OrderByType = None
        self._ProjectIds = None
        self._SearchKey = None
        self._Tags = None

    @property
    def InstanceIds(self):
        r"""Instance ID list. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceType(self):
        r"""Specifies the instance type for querying. Valid values:
- 0: all instances.
- 1: formal instance.
- 2: temporary instance.
- 3: read-only instance.
- -1: the query range includes the formal, read-only, and disaster recovery instances simultaneously.
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ClusterType(self):
        r"""Specifies the cluster type of the instance to be queried. Valid values:
- 0: replica set instance.
- 1: sharded cluster instance.
- -1: replica set and sharded cluster instance.
        :rtype: int
        """
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def Status(self):
        r"""Specifies the current status of the instance to be queried. Valid values:
- 0: to be initialized.
- 1: processing, such as specification changes and parameter modifications.
- 2: running normally.
- -2: isolated (yearly/monthly subscription).
- -3: isolated (pay-as-you-go).
        :rtype: list of int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def VpcId(self):
        r"""VPC ID.
 - You do not need to specify this parameter for basic networks.
 - Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/MongoDB), click a VPC name in the instance list, and obtain the ID on the **VPC** page.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""VPC subnet ID.
 - You do not need to specify this parameter for basic networks.
 - Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/MongoDB), click a VPC name in the instance list, and obtain the subnet ID on the **VPC** page.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def PayMode(self):
        r"""Billing type. Valid value: 0 (pay-as-you-go)
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Limit(self):
        r"""Number of entries returned per request. The default value is 20, and the value range is (1, 100].
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset. Default value: `0`.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        r"""Configures the field for sorting returned results. Currently, "ProjectId", "InstanceName", and "CreateTime" are supported for sorting.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""Configures the method for sorting returned results.
 - ASC: ascending order.
 - DESC: descending order.
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def ProjectIds(self):
        r"""Project ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/MongoDB) and select Project Management in the account information drop-down menu at the top right corner to query projects.
        :rtype: list of int non-negative
        """
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def SearchKey(self):
        r"""Specifies the keyword for search. Specific instance IDs, instance names, or private IP addresses are supported.
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def Tags(self):
        r"""Tag information, including the tag key and tag value.
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceType = params.get("InstanceType")
        self._ClusterType = params.get("ClusterType")
        self._Status = params.get("Status")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._PayMode = params.get("PayMode")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._ProjectIds = params.get("ProjectIds")
        self._SearchKey = params.get("SearchKey")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstancesResponse(AbstractModel):
    r"""DescribeDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible instances
        :type TotalCount: int
        :param _InstanceDetails: List of instance details
        :type InstanceDetails: list of InstanceDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceDetails = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of eligible instances
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceDetails(self):
        r"""List of instance details
        :rtype: list of InstanceDetail
        """
        return self._InstanceDetails

    @InstanceDetails.setter
    def InstanceDetails(self, InstanceDetails):
        self._InstanceDetails = InstanceDetails

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceDetails") is not None:
            self._InstanceDetails = []
            for item in params.get("InstanceDetails"):
                obj = InstanceDetail()
                obj._deserialize(item)
                self._InstanceDetails.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDetailedSlowLogsRequest(AbstractModel):
    r"""DescribeDetailedSlowLogs request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :type InstanceId: str
        :param _StartTime: Specifies the start time for querying slow logs. - Format: yyyy-mm-dd hh:mm:ss. For example, 2019-06-01 10:00:00. - The query start and end time interval cannot exceed 24 hours. Only slow logs within the last 7 days can be queried.
        :type StartTime: str
        :param _EndTime: Specifies the end time for querying slow logs.
- Format: yyyy-mm-dd hh:mm:ss. For example, 2019-06-02 12:00:00.
- The query start and end time interval cannot exceed 24 hours. Only slow logs within the last 7 days can be queried.
        :type EndTime: str
        :param _ExecTime: Specifies the threshold for querying slow logs, in milliseconds. It indicates that the execution time of the slow log query exceeds this value. The default value is 100.
        :type ExecTime: int
        :param _Commands: Specifies the command type for querying slow logs.
        :type Commands: list of str
        :param _Texts: Full-text search keyword. The logical operator among multiple keywords is OR.
        :type Texts: list of str
        :param _NodeNames: Specifies the node name for querying slow logs. The [DescribeDBInstanceNodeProperty](https://www.tencentcloud.comom/document/product/240/82022?from_cn_redirect=1) API can be called to query the node name.
        :type NodeNames: list of str
        :param _QueryHash: Specifies the queryHash value to be queried.
        :type QueryHash: list of str
        :param _Offset: Pagination offset. The default value is 0, and the value range is [0, 100].

        :type Offset: int
        :param _Limit: Number of returned entries. The default value is 20, and the value range is [0, 10000].
        :type Limit: int
        :param _OrderBy: Specifies the sorting condition for slow logs.
- StartTime: sort by the generation time of slow logs.
- ExecTime: sort by the execution time of slow logs.
        :type OrderBy: str
        :param _OrderByType: Specifies the sorting method.
- desc: descending order.
- asc: ascending order.
        :type OrderByType: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._ExecTime = None
        self._Commands = None
        self._Texts = None
        self._NodeNames = None
        self._QueryHash = None
        self._Offset = None
        self._Limit = None
        self._OrderBy = None
        self._OrderByType = None

    @property
    def InstanceId(self):
        r"""Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        r"""Specifies the start time for querying slow logs. - Format: yyyy-mm-dd hh:mm:ss. For example, 2019-06-01 10:00:00. - The query start and end time interval cannot exceed 24 hours. Only slow logs within the last 7 days can be queried.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Specifies the end time for querying slow logs.
- Format: yyyy-mm-dd hh:mm:ss. For example, 2019-06-02 12:00:00.
- The query start and end time interval cannot exceed 24 hours. Only slow logs within the last 7 days can be queried.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ExecTime(self):
        r"""Specifies the threshold for querying slow logs, in milliseconds. It indicates that the execution time of the slow log query exceeds this value. The default value is 100.
        :rtype: int
        """
        return self._ExecTime

    @ExecTime.setter
    def ExecTime(self, ExecTime):
        self._ExecTime = ExecTime

    @property
    def Commands(self):
        r"""Specifies the command type for querying slow logs.
        :rtype: list of str
        """
        return self._Commands

    @Commands.setter
    def Commands(self, Commands):
        self._Commands = Commands

    @property
    def Texts(self):
        r"""Full-text search keyword. The logical operator among multiple keywords is OR.
        :rtype: list of str
        """
        return self._Texts

    @Texts.setter
    def Texts(self, Texts):
        self._Texts = Texts

    @property
    def NodeNames(self):
        r"""Specifies the node name for querying slow logs. The [DescribeDBInstanceNodeProperty](https://www.tencentcloud.comom/document/product/240/82022?from_cn_redirect=1) API can be called to query the node name.
        :rtype: list of str
        """
        return self._NodeNames

    @NodeNames.setter
    def NodeNames(self, NodeNames):
        self._NodeNames = NodeNames

    @property
    def QueryHash(self):
        r"""Specifies the queryHash value to be queried.
        :rtype: list of str
        """
        return self._QueryHash

    @QueryHash.setter
    def QueryHash(self, QueryHash):
        self._QueryHash = QueryHash

    @property
    def Offset(self):
        r"""Pagination offset. The default value is 0, and the value range is [0, 100].

        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of returned entries. The default value is 20, and the value range is [0, 10000].
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderBy(self):
        r"""Specifies the sorting condition for slow logs.
- StartTime: sort by the generation time of slow logs.
- ExecTime: sort by the execution time of slow logs.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""Specifies the sorting method.
- desc: descending order.
- asc: ascending order.
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ExecTime = params.get("ExecTime")
        self._Commands = params.get("Commands")
        self._Texts = params.get("Texts")
        self._NodeNames = params.get("NodeNames")
        self._QueryHash = params.get("QueryHash")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDetailedSlowLogsResponse(AbstractModel):
    r"""DescribeDetailedSlowLogs response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of slow logs that meet the conditions.
        :type TotalCount: int
        :param _DetailedSlowLogs: Slow log details.
        :type DetailedSlowLogs: list of SlowLogItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._DetailedSlowLogs = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of slow logs that meet the conditions.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DetailedSlowLogs(self):
        r"""Slow log details.
        :rtype: list of SlowLogItem
        """
        return self._DetailedSlowLogs

    @DetailedSlowLogs.setter
    def DetailedSlowLogs(self, DetailedSlowLogs):
        self._DetailedSlowLogs = DetailedSlowLogs

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DetailedSlowLogs") is not None:
            self._DetailedSlowLogs = []
            for item in params.get("DetailedSlowLogs"):
                obj = SlowLogItem()
                obj._deserialize(item)
                self._DetailedSlowLogs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceParamsRequest(AbstractModel):
    r"""DescribeInstanceParams request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Specifies the instance ID for querying the parameter list. For example, cmgo-p8vn****. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/MongoDB) and copy the instance ID from the instance list.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Specifies the instance ID for querying the parameter list. For example, cmgo-p8vn****. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/MongoDB) and copy the instance ID from the instance list.
        :rtype: str
        """
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
    r"""DescribeInstanceParams response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceEnumParam: Collection of parameters whose values are of the Enum type.
        :type InstanceEnumParam: list of InstanceEnumParam
        :param _InstanceIntegerParam: Collection of parameters whose values are of the Integer type.
        :type InstanceIntegerParam: list of InstanceIntegerParam
        :param _InstanceTextParam: Collection of parameters whose values are of the Text type.
        :type InstanceTextParam: list of InstanceTextParam
        :param _InstanceMultiParam: Collection of parameters whose values are of different types.
        :type InstanceMultiParam: list of InstanceMultiParam
        :param _TotalCount: Number of modifiable parameters supported by the current instance.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceEnumParam = None
        self._InstanceIntegerParam = None
        self._InstanceTextParam = None
        self._InstanceMultiParam = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def InstanceEnumParam(self):
        r"""Collection of parameters whose values are of the Enum type.
        :rtype: list of InstanceEnumParam
        """
        return self._InstanceEnumParam

    @InstanceEnumParam.setter
    def InstanceEnumParam(self, InstanceEnumParam):
        self._InstanceEnumParam = InstanceEnumParam

    @property
    def InstanceIntegerParam(self):
        r"""Collection of parameters whose values are of the Integer type.
        :rtype: list of InstanceIntegerParam
        """
        return self._InstanceIntegerParam

    @InstanceIntegerParam.setter
    def InstanceIntegerParam(self, InstanceIntegerParam):
        self._InstanceIntegerParam = InstanceIntegerParam

    @property
    def InstanceTextParam(self):
        r"""Collection of parameters whose values are of the Text type.
        :rtype: list of InstanceTextParam
        """
        return self._InstanceTextParam

    @InstanceTextParam.setter
    def InstanceTextParam(self, InstanceTextParam):
        self._InstanceTextParam = InstanceTextParam

    @property
    def InstanceMultiParam(self):
        r"""Collection of parameters whose values are of different types.
        :rtype: list of InstanceMultiParam
        """
        return self._InstanceMultiParam

    @InstanceMultiParam.setter
    def InstanceMultiParam(self, InstanceMultiParam):
        self._InstanceMultiParam = InstanceMultiParam

    @property
    def TotalCount(self):
        r"""Number of modifiable parameters supported by the current instance.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
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
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeInstanceSSLRequest(AbstractModel):
    r"""DescribeInstanceSSL request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID, in the format of cmgo-p8vnipr5. It is the same as the format of the instance ID displayed on the TencentDB for MongoDB console page.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Instance ID, in the format of cmgo-p8vnipr5. It is the same as the format of the instance ID displayed on the TencentDB for MongoDB console page.
        :rtype: str
        """
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
        


class DescribeInstanceSSLResponse(AbstractModel):
    r"""DescribeInstanceSSL response structure.

    """

    def __init__(self):
        r"""
        :param _Status: SSL enabling status. 0 indicates disabled; 1 indicates enabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _ExpiredTime: Certificate expiration time, in the format of 2023-05-01 12:00:00.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpiredTime: str
        :param _CertUrl: Certificate download URL.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertUrl: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._ExpiredTime = None
        self._CertUrl = None
        self._RequestId = None

    @property
    def Status(self):
        r"""SSL enabling status. 0 indicates disabled; 1 indicates enabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ExpiredTime(self):
        r"""Certificate expiration time, in the format of 2023-05-01 12:00:00.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def CertUrl(self):
        r"""Certificate download URL.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CertUrl

    @CertUrl.setter
    def CertUrl(self, CertUrl):
        self._CertUrl = CertUrl

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ExpiredTime = params.get("ExpiredTime")
        self._CertUrl = params.get("CertUrl")
        self._RequestId = params.get("RequestId")


class DescribeLogDownloadTasksRequest(AbstractModel):
    r"""DescribeLogDownloadTasks request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _Limit: Number of queries.
        :type Limit: int
        :param _Offset: Page number.
        :type Offset: int
        :param _StartTime: Start time of the download task.
        :type StartTime: str
        :param _EndTime: End time of the download task.
        :type EndTime: str
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None
        self._StartTime = None
        self._EndTime = None

    @property
    def InstanceId(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        r"""Number of queries.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Page number.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def StartTime(self):
        r"""Start time of the download task.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time of the download task.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogDownloadTasksResponse(AbstractModel):
    r"""DescribeLogDownloadTasks response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Quantity.
        :type TotalCount: int
        :param _Tasks: Task list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tasks: list of Task
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Quantity.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tasks(self):
        r"""Task list.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Task
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMongodbLogsRequest(AbstractModel):
    r"""DescribeMongodbLogs request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb#/), and copy the instance ID from the instance list.
        :type InstanceId: str
        :param _StartTime: Start time for querying logs.
- Format: yyyy-mm-dd hh:mm:ss. For example, 2019-06-01 10:00:00.
- Query time range: Only log data within the last 7 days can be queried.
        :type StartTime: str
        :param _EndTime: End time for querying logs.
- Format: yyyy-mm-dd hh:mm:ss. For example, 2019-06-01 10:00:00.
- Query time range: Only log data within the last 7 days can be queried.
        :type EndTime: str
        :param _NodeNames: Node ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and go to the **Node Management** page to obtain the ID of the node to be queried.
        :type NodeNames: list of str
        :param _LogComponents: Log category.
- Log categories include but are not limited to COMMAND, ACCESS, CONTROL, FTDC, INDEX, NETWORK, QUERY, REPL, SHARDING, STORAGE, RECOVERY, JOURNAL, and WRITE. The specific supported categories may vary depending on the MongoDB version. For details, see Log Messages (https://www.mongodb.com/zh-cn/docs/v5.0/reference/log-messages/#log-message-examples).
- Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and view the **log category** on the **Error Log** tab of the **Log Management** page.
        :type LogComponents: list of str
        :param _LogLevels: Log level.
- The log levels are ranked by severity from high to low: FATAL, ERROR, and WARNING.
-Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and view the **log level** on the **Error Log** tab of the **Log Management** page.
        :type LogLevels: list of str
        :param _LogIds: Log ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and view the **log ID** on the **Error Log** tab of the **Log Management** page.
        :type LogIds: list of str
        :param _LogConnections: Log connection information. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and view the **log connection information** on the **Error Log** tab of the **Log Management** page.
        :type LogConnections: list of str
        :param _LogDetailParams: Specifies the field for filtering the logs.
        :type LogDetailParams: list of str
        :param _Offset: Offset. The minimum value is 0, and the maximum value is 10000. The default value is 0.
        :type Offset: int
        :param _Limit: Pagination size. The minimum value is 1, and the maximum value is 100. The default value is 20.
        :type Limit: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._NodeNames = None
        self._LogComponents = None
        self._LogLevels = None
        self._LogIds = None
        self._LogConnections = None
        self._LogDetailParams = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        r"""Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb#/), and copy the instance ID from the instance list.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        r"""Start time for querying logs.
- Format: yyyy-mm-dd hh:mm:ss. For example, 2019-06-01 10:00:00.
- Query time range: Only log data within the last 7 days can be queried.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time for querying logs.
- Format: yyyy-mm-dd hh:mm:ss. For example, 2019-06-01 10:00:00.
- Query time range: Only log data within the last 7 days can be queried.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def NodeNames(self):
        r"""Node ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and go to the **Node Management** page to obtain the ID of the node to be queried.
        :rtype: list of str
        """
        return self._NodeNames

    @NodeNames.setter
    def NodeNames(self, NodeNames):
        self._NodeNames = NodeNames

    @property
    def LogComponents(self):
        r"""Log category.
- Log categories include but are not limited to COMMAND, ACCESS, CONTROL, FTDC, INDEX, NETWORK, QUERY, REPL, SHARDING, STORAGE, RECOVERY, JOURNAL, and WRITE. The specific supported categories may vary depending on the MongoDB version. For details, see Log Messages (https://www.mongodb.com/zh-cn/docs/v5.0/reference/log-messages/#log-message-examples).
- Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and view the **log category** on the **Error Log** tab of the **Log Management** page.
        :rtype: list of str
        """
        return self._LogComponents

    @LogComponents.setter
    def LogComponents(self, LogComponents):
        self._LogComponents = LogComponents

    @property
    def LogLevels(self):
        r"""Log level.
- The log levels are ranked by severity from high to low: FATAL, ERROR, and WARNING.
-Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and view the **log level** on the **Error Log** tab of the **Log Management** page.
        :rtype: list of str
        """
        return self._LogLevels

    @LogLevels.setter
    def LogLevels(self, LogLevels):
        self._LogLevels = LogLevels

    @property
    def LogIds(self):
        r"""Log ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and view the **log ID** on the **Error Log** tab of the **Log Management** page.
        :rtype: list of str
        """
        return self._LogIds

    @LogIds.setter
    def LogIds(self, LogIds):
        self._LogIds = LogIds

    @property
    def LogConnections(self):
        r"""Log connection information. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and view the **log connection information** on the **Error Log** tab of the **Log Management** page.
        :rtype: list of str
        """
        return self._LogConnections

    @LogConnections.setter
    def LogConnections(self, LogConnections):
        self._LogConnections = LogConnections

    @property
    def LogDetailParams(self):
        r"""Specifies the field for filtering the logs.
        :rtype: list of str
        """
        return self._LogDetailParams

    @LogDetailParams.setter
    def LogDetailParams(self, LogDetailParams):
        self._LogDetailParams = LogDetailParams

    @property
    def Offset(self):
        r"""Offset. The minimum value is 0, and the maximum value is 10000. The default value is 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Pagination size. The minimum value is 1, and the maximum value is 100. The default value is 20.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._NodeNames = params.get("NodeNames")
        self._LogComponents = params.get("LogComponents")
        self._LogLevels = params.get("LogLevels")
        self._LogIds = params.get("LogIds")
        self._LogConnections = params.get("LogConnections")
        self._LogDetailParams = params.get("LogDetailParams")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMongodbLogsResponse(AbstractModel):
    r"""DescribeMongodbLogs response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of logs.
        :type TotalCount: int
        :param _LogList: List of log details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogList: list of LogInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._LogList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of logs.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LogList(self):
        r"""List of log details.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of LogInfo
        """
        return self._LogList

    @LogList.setter
    def LogList(self, LogList):
        self._LogList = LogList

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("LogList") is not None:
            self._LogList = []
            for item in params.get("LogList"):
                obj = LogInfo()
                obj._deserialize(item)
                self._LogList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSecurityGroupRequest(AbstractModel):
    r"""DescribeSecurityGroup request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :rtype: str
        """
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
        


class DescribeSecurityGroupResponse(AbstractModel):
    r"""DescribeSecurityGroup response structure.

    """

    def __init__(self):
        r"""
        :param _Groups: Information on security groups bound to the instance.
        :type Groups: list of SecurityGroup
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Groups = None
        self._RequestId = None

    @property
    def Groups(self):
        r"""Information on security groups bound to the instance.
        :rtype: list of SecurityGroup
        """
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        self._RequestId = params.get("RequestId")


class DescribeSlowLogPatternsRequest(AbstractModel):
    r"""DescribeSlowLogPatterns request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :type InstanceId: str
        :param _StartTime: Slow log start time.
- Format: yyyy-mm-dd hh:mm:ss. For example, 2019-06-01 10:00:00.
- The query start and end time interval cannot exceed 24 hours. Only slow logs within the last 7 days can be queried.
        :type StartTime: str
        :param _EndTime: Slow log end time.
- Format: yyyy-mm-dd hh:mm:ss. For example, 2019-06-02 12:00:00.
- The query start and end time interval cannot exceed 24 hours. Only slow logs within the last 7 days can be queried.
        :type EndTime: str
        :param _SlowMS: Threshold of slow log execution time in milliseconds. Minimum value: 100. Slow logs whose execution time exceeds the threshold will be returned.
        :type SlowMS: int
        :param _Offset: Offset. Minimum value: 0. Maximum value: 10000. Default value: 0.
        :type Offset: int
        :param _Limit: Number of entries per page. Minimum value: 1. Maximum value: 100. Default value: 20.
        :type Limit: int
        :param _Format: Slow log format, which can be JSON. If this parameter is left empty, the slow log will be returned in its native format.
        :type Format: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._SlowMS = None
        self._Offset = None
        self._Limit = None
        self._Format = None

    @property
    def InstanceId(self):
        r"""Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        r"""Slow log start time.
- Format: yyyy-mm-dd hh:mm:ss. For example, 2019-06-01 10:00:00.
- The query start and end time interval cannot exceed 24 hours. Only slow logs within the last 7 days can be queried.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Slow log end time.
- Format: yyyy-mm-dd hh:mm:ss. For example, 2019-06-02 12:00:00.
- The query start and end time interval cannot exceed 24 hours. Only slow logs within the last 7 days can be queried.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SlowMS(self):
        r"""Threshold of slow log execution time in milliseconds. Minimum value: 100. Slow logs whose execution time exceeds the threshold will be returned.
        :rtype: int
        """
        return self._SlowMS

    @SlowMS.setter
    def SlowMS(self, SlowMS):
        self._SlowMS = SlowMS

    @property
    def Offset(self):
        r"""Offset. Minimum value: 0. Maximum value: 10000. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of entries per page. Minimum value: 1. Maximum value: 100. Default value: 20.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Format(self):
        r"""Slow log format, which can be JSON. If this parameter is left empty, the slow log will be returned in its native format.
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SlowMS = params.get("SlowMS")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogPatternsResponse(AbstractModel):
    r"""DescribeSlowLogPatterns response structure.

    """

    def __init__(self):
        r"""
        :param _Count: Total number of slow logs
        :type Count: int
        :param _SlowLogPatterns: Slow log statistics
        :type SlowLogPatterns: list of SlowLogPattern
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Count = None
        self._SlowLogPatterns = None
        self._RequestId = None

    @property
    def Count(self):
        r"""Total number of slow logs
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def SlowLogPatterns(self):
        r"""Slow log statistics
        :rtype: list of SlowLogPattern
        """
        return self._SlowLogPatterns

    @SlowLogPatterns.setter
    def SlowLogPatterns(self, SlowLogPatterns):
        self._SlowLogPatterns = SlowLogPatterns

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        if params.get("SlowLogPatterns") is not None:
            self._SlowLogPatterns = []
            for item in params.get("SlowLogPatterns"):
                obj = SlowLogPattern()
                obj._deserialize(item)
                self._SlowLogPatterns.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSlowLogsRequest(AbstractModel):
    r"""DescribeSlowLogs request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :type InstanceId: str
        :param _StartTime: Slow log start time.
- Format: yyyy-mm-dd hh:mm:ss. For example, 2019-06-01 10:00:00.
- The query start and end time interval cannot exceed 24 hours. Only slow logs within the last 7 days can be queried.
        :type StartTime: str
        :param _EndTime: Slow log end time.
- Format: yyyy-mm-dd hh:mm:ss. For example, 2019-06-02 12:00:00.- The query start and end time interval cannot exceed 24 hours. Only slow logs within the last 7 days can be queried.
        :type EndTime: str
        :param _SlowMS: Threshold of slow log execution time in milliseconds. Minimum value: 100. Slow logs whose execution time exceeds the threshold will be returned.
        :type SlowMS: int
        :param _Offset: Offset. Minimum value: 0. Maximum value: 10000. Default value: 0.
        :type Offset: int
        :param _Limit: Number of entries per page. Minimum value: 1. Maximum value: 100. Default value: 20.
        :type Limit: int
        :param _Format: Return format of slow log. The original slow log format is returned by default, and the format can be set to JSON on versions 4.4 and later.
        :type Format: str
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._SlowMS = None
        self._Offset = None
        self._Limit = None
        self._Format = None

    @property
    def InstanceId(self):
        r"""Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        r"""Slow log start time.
- Format: yyyy-mm-dd hh:mm:ss. For example, 2019-06-01 10:00:00.
- The query start and end time interval cannot exceed 24 hours. Only slow logs within the last 7 days can be queried.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Slow log end time.
- Format: yyyy-mm-dd hh:mm:ss. For example, 2019-06-02 12:00:00.- The query start and end time interval cannot exceed 24 hours. Only slow logs within the last 7 days can be queried.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SlowMS(self):
        r"""Threshold of slow log execution time in milliseconds. Minimum value: 100. Slow logs whose execution time exceeds the threshold will be returned.
        :rtype: int
        """
        return self._SlowMS

    @SlowMS.setter
    def SlowMS(self, SlowMS):
        self._SlowMS = SlowMS

    @property
    def Offset(self):
        r"""Offset. Minimum value: 0. Maximum value: 10000. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of entries per page. Minimum value: 1. Maximum value: 100. Default value: 20.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Format(self):
        r"""Return format of slow log. The original slow log format is returned by default, and the format can be set to JSON on versions 4.4 and later.
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SlowMS = params.get("SlowMS")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogsResponse(AbstractModel):
    r"""DescribeSlowLogs response structure.

    """

    def __init__(self):
        r"""
        :param _Count: Total number of slow logs.
        :type Count: int
        :param _SlowLogs: Slow log details.
        :type SlowLogs: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Count = None
        self._SlowLogs = None
        self._RequestId = None

    @property
    def Count(self):
        r"""Total number of slow logs.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def SlowLogs(self):
        r"""Slow log details.
        :rtype: list of str
        """
        return self._SlowLogs

    @SlowLogs.setter
    def SlowLogs(self, SlowLogs):
        self._SlowLogs = SlowLogs

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._SlowLogs = params.get("SlowLogs")
        self._RequestId = params.get("RequestId")


class DescribeSpecInfoRequest(AbstractModel):
    r"""DescribeSpecInfo request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: AZ to be queried. For currently supported AZs, see [Regions and AZs](https://www.tencentcloud.comom/document/product/240/3637?from_cn_redirect=1).
        :type Zone: str
        """
        self._Zone = None

    @property
    def Zone(self):
        r"""AZ to be queried. For currently supported AZs, see [Regions and AZs](https://www.tencentcloud.comom/document/product/240/3637?from_cn_redirect=1).
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpecInfoResponse(AbstractModel):
    r"""DescribeSpecInfo response structure.

    """

    def __init__(self):
        r"""
        :param _SpecInfoList: List of sales specification information on the instance.
        :type SpecInfoList: list of SpecificationInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SpecInfoList = None
        self._RequestId = None

    @property
    def SpecInfoList(self):
        r"""List of sales specification information on the instance.
        :rtype: list of SpecificationInfo
        """
        return self._SpecInfoList

    @SpecInfoList.setter
    def SpecInfoList(self, SpecInfoList):
        self._SpecInfoList = SpecInfoList

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SpecInfoList") is not None:
            self._SpecInfoList = []
            for item in params.get("SpecInfoList"):
                obj = SpecificationInfo()
                obj._deserialize(item)
                self._SpecInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class EnableTransparentDataEncryptionRequest(AbstractModel):
    r"""EnableTransparentDataEncryption request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. For example, cmgo-p8vn****. Log in to the[TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb) to copy the instance ID from the instance list. Currently, the supported general versions include 4.4 and 5.0, and Cloud Disk Edition is not supported.
        :type InstanceId: str
        :param _KmsRegion:  Region where the [Key Management Service (KMS)](https://www.tencentcloud.comom/document/product/573/18809?from_cn_redirect=1) instance is located. For example, ap-shanghai.
        :type KmsRegion: str
        :param _KeyId: Key ID. If the parameter is left unspecified, there is no specific key ID, Tencent Cloud will generate the key automatically.
        :type KeyId: str
        """
        self._InstanceId = None
        self._KmsRegion = None
        self._KeyId = None

    @property
    def InstanceId(self):
        r"""Instance ID. For example, cmgo-p8vn****. Log in to the[TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb) to copy the instance ID from the instance list. Currently, the supported general versions include 4.4 and 5.0, and Cloud Disk Edition is not supported.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def KmsRegion(self):
        r""" Region where the [Key Management Service (KMS)](https://www.tencentcloud.comom/document/product/573/18809?from_cn_redirect=1) instance is located. For example, ap-shanghai.
        :rtype: str
        """
        return self._KmsRegion

    @KmsRegion.setter
    def KmsRegion(self, KmsRegion):
        self._KmsRegion = KmsRegion

    @property
    def KeyId(self):
        r"""Key ID. If the parameter is left unspecified, there is no specific key ID, Tencent Cloud will generate the key automatically.
        :rtype: str
        """
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._KmsRegion = params.get("KmsRegion")
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableTransparentDataEncryptionResponse(AbstractModel):
    r"""EnableTransparentDataEncryption response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Asynchronous process ID for enabling TDE, which is used for querying the process status.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Asynchronous process ID for enabling TDE, which is used for querying the process status.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class FlushInstanceRouterConfigRequest(AbstractModel):
    r"""FlushInstanceRouterConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Instance ID
        :rtype: str
        """
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
        


class FlushInstanceRouterConfigResponse(AbstractModel):
    r"""FlushInstanceRouterConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class InquirePriceCreateDBInstancesRequest(AbstractModel):
    r"""InquirePriceCreateDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: Region and AZ information of the instance. For details, see [Regions and AZs](https://www.tencentcloud.comom/document/product/240/3637?from_cn_redirect=1).
        :type Zone: str
        :param _NodeNum: -Specifies the number of primary and secondary nodes for each replica set during replica set instance creation. call the [DescribeSpecInfo](https://www.tencentcloud.comom/document/product/240/38567?from_cn_redirect=1) API to obtain the maximum and minimum number of nodes supported for each replica set.
- Specifies the number of primary and secondary nodes for each shard during sharded cluster instance creation. Call the [DescribeSpecInfo](https://www.tencentcloud.comom/document/product/240/38567?from_cn_redirect=1) API to obtain the maximum and minimum number of nodes supported for each shard.
        :type NodeNum: int
        :param _Memory: Instance memory size.

 - Unit: GB.
 - For the value range, call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API. The CPU and Memory parameters in the returned data structure SpecItems correspond to the number of CPU cores and the memory specification, respectively.
        :type Memory: int
        :param _Volume: Instance disk size.
 - Unit: GB.
 - For the value range, call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API. The MinStorage and MaxStorage parameters in the returned data structure SpecItems correspond to the minimum and maximum disk specifications, respectively.
        :type Volume: int
        :param _MongoVersion: Instance version information. The [DescribeSpecInfo](https://www.tencentcloud.comom/document/product/240/38567?from_cn_redirect=1) API can be called to obtain specific supported versions. The MongoVersionCode parameter in the returned data structure SpecItems indicates the information on versions supported by instances. The corresponding relationship between version information and version number is as follows:
- MONGO_40_WT: version of the MongoDB 4.0 WiredTiger storage engine.
- MONGO_42_WT: version of the MongoDB 4.2 WiredTiger storage engine.
- MONGO_44_WT: version of the MongoDB 4.4 WiredTiger storage engine.
- MONGO_50_WT: version of the MongoDB 5.0 WiredTiger storage engine.
- MONGO_60_WT: version of the MongoDB 6.0 WiredTiger storage engine.
- MONGO_70_WT: version of the MongoDB 7.0 WiredTiger storage engine.
        :type MongoVersion: str
        :param _MachineCode: Product specification type.
 - HIO10G: general high-I/O 10GE type.
 - HCD: cloud disk.
        :type MachineCode: str
        :param _GoodsNum: Number of instances. Minimum value: 1. Maximum value: 10.
        :type GoodsNum: int
        :param _ClusterType: Instance type.

 - REPLSET: replica set.
 - SHARD: sharded cluster.
        :type ClusterType: str
        :param _ReplicateSetNum:  - Specifies the number of replica sets during replica set instance creation. This parameter can only be set to 1.
 - Specifies the number of shards during sharded cluster instance creation. Call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API to query the range of shard quantity. The parameters MinReplicateSetNum and MaxReplicateSetNum in the returned data structure SpecItems correspond to the minimum value and maximum value, respectively.
        :type ReplicateSetNum: int
        :param _Period:  - When the monthly subscription mode is selected, that is, when <b>InstanceChargeType</b> is set to <b>PREPAID</b>, this parameter is required for specifying the purchase duration of instances. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, and 36. Unit: months.
 - When pay-as-you-go is selected, that is, when <b>InstanceChargeType</b> is set to **POSTPAID_BY_HOUR**, this parameter only can be set to 1.
        :type Period: int
        :param _InstanceChargeType: Instance payment method.
 - PREPAID: monthly subscription.
 - POSTPAID_BY_HOUR: pay-as-you-go.
        :type InstanceChargeType: str
        :param _MongosCpu: Number of Mongos node CPU cores. Valid values: 1, 2, 4, 8, and 16. This parameter is required during sharded cluster instance purchase. If this parameter is left blank, the default value 2 is used.
        :type MongosCpu: int
        :param _MongosMemory: Mongos node memory size. - This parameter is required during sharded cluster instance purchase. - Unit: GB. Valid values: 2 (for 1 core), 4 (for 2 cores), 8 (for 4 cores), 16 (for 8 cores), and 32 (for 16 cores). If this parameter is left blank, the default value 4 is used.
        :type MongosMemory: int
        :param _MongosNum: Specifies the number of Mongos nodes. Value range: [3,32]. For querying the price of sharded cluster instances, this parameter is required. If it is left blank, the default value 3 is used.
        :type MongosNum: int
        :param _ConfigServerCpu: Specifies the number of ConfigServer CPU cores. The value is fixed as 1.
        :type ConfigServerCpu: int
        :param _ConfigServerMemory: Specifies the ConfigServer memory size. The value is fixed as 2. Unit: GB. This parameter can be left blank.
        :type ConfigServerMemory: int
        :param _ConfigServerVolume: Specifies the ConfigServer disk size. The value is fixed as 20. Unit: GB. This parameter can be left blank.
        :type ConfigServerVolume: int
        """
        self._Zone = None
        self._NodeNum = None
        self._Memory = None
        self._Volume = None
        self._MongoVersion = None
        self._MachineCode = None
        self._GoodsNum = None
        self._ClusterType = None
        self._ReplicateSetNum = None
        self._Period = None
        self._InstanceChargeType = None
        self._MongosCpu = None
        self._MongosMemory = None
        self._MongosNum = None
        self._ConfigServerCpu = None
        self._ConfigServerMemory = None
        self._ConfigServerVolume = None

    @property
    def Zone(self):
        r"""Region and AZ information of the instance. For details, see [Regions and AZs](https://www.tencentcloud.comom/document/product/240/3637?from_cn_redirect=1).
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def NodeNum(self):
        r"""-Specifies the number of primary and secondary nodes for each replica set during replica set instance creation. call the [DescribeSpecInfo](https://www.tencentcloud.comom/document/product/240/38567?from_cn_redirect=1) API to obtain the maximum and minimum number of nodes supported for each replica set.
- Specifies the number of primary and secondary nodes for each shard during sharded cluster instance creation. Call the [DescribeSpecInfo](https://www.tencentcloud.comom/document/product/240/38567?from_cn_redirect=1) API to obtain the maximum and minimum number of nodes supported for each shard.
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def Memory(self):
        r"""Instance memory size.

 - Unit: GB.
 - For the value range, call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API. The CPU and Memory parameters in the returned data structure SpecItems correspond to the number of CPU cores and the memory specification, respectively.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        r"""Instance disk size.
 - Unit: GB.
 - For the value range, call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API. The MinStorage and MaxStorage parameters in the returned data structure SpecItems correspond to the minimum and maximum disk specifications, respectively.
        :rtype: int
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def MongoVersion(self):
        r"""Instance version information. The [DescribeSpecInfo](https://www.tencentcloud.comom/document/product/240/38567?from_cn_redirect=1) API can be called to obtain specific supported versions. The MongoVersionCode parameter in the returned data structure SpecItems indicates the information on versions supported by instances. The corresponding relationship between version information and version number is as follows:
- MONGO_40_WT: version of the MongoDB 4.0 WiredTiger storage engine.
- MONGO_42_WT: version of the MongoDB 4.2 WiredTiger storage engine.
- MONGO_44_WT: version of the MongoDB 4.4 WiredTiger storage engine.
- MONGO_50_WT: version of the MongoDB 5.0 WiredTiger storage engine.
- MONGO_60_WT: version of the MongoDB 6.0 WiredTiger storage engine.
- MONGO_70_WT: version of the MongoDB 7.0 WiredTiger storage engine.
        :rtype: str
        """
        return self._MongoVersion

    @MongoVersion.setter
    def MongoVersion(self, MongoVersion):
        self._MongoVersion = MongoVersion

    @property
    def MachineCode(self):
        r"""Product specification type.
 - HIO10G: general high-I/O 10GE type.
 - HCD: cloud disk.
        :rtype: str
        """
        return self._MachineCode

    @MachineCode.setter
    def MachineCode(self, MachineCode):
        self._MachineCode = MachineCode

    @property
    def GoodsNum(self):
        r"""Number of instances. Minimum value: 1. Maximum value: 10.
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def ClusterType(self):
        r"""Instance type.

 - REPLSET: replica set.
 - SHARD: sharded cluster.
        :rtype: str
        """
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def ReplicateSetNum(self):
        r""" - Specifies the number of replica sets during replica set instance creation. This parameter can only be set to 1.
 - Specifies the number of shards during sharded cluster instance creation. Call the [DescribeSpecInfo](https://intl.cloud.tencent.com/document/product/240/38567?from_cn_redirect=1) API to query the range of shard quantity. The parameters MinReplicateSetNum and MaxReplicateSetNum in the returned data structure SpecItems correspond to the minimum value and maximum value, respectively.
        :rtype: int
        """
        return self._ReplicateSetNum

    @ReplicateSetNum.setter
    def ReplicateSetNum(self, ReplicateSetNum):
        self._ReplicateSetNum = ReplicateSetNum

    @property
    def Period(self):
        r""" - When the monthly subscription mode is selected, that is, when <b>InstanceChargeType</b> is set to <b>PREPAID</b>, this parameter is required for specifying the purchase duration of instances. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, and 36. Unit: months.
 - When pay-as-you-go is selected, that is, when <b>InstanceChargeType</b> is set to **POSTPAID_BY_HOUR**, this parameter only can be set to 1.
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def InstanceChargeType(self):
        r"""Instance payment method.
 - PREPAID: monthly subscription.
 - POSTPAID_BY_HOUR: pay-as-you-go.
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def MongosCpu(self):
        r"""Number of Mongos node CPU cores. Valid values: 1, 2, 4, 8, and 16. This parameter is required during sharded cluster instance purchase. If this parameter is left blank, the default value 2 is used.
        :rtype: int
        """
        return self._MongosCpu

    @MongosCpu.setter
    def MongosCpu(self, MongosCpu):
        self._MongosCpu = MongosCpu

    @property
    def MongosMemory(self):
        r"""Mongos node memory size. - This parameter is required during sharded cluster instance purchase. - Unit: GB. Valid values: 2 (for 1 core), 4 (for 2 cores), 8 (for 4 cores), 16 (for 8 cores), and 32 (for 16 cores). If this parameter is left blank, the default value 4 is used.
        :rtype: int
        """
        return self._MongosMemory

    @MongosMemory.setter
    def MongosMemory(self, MongosMemory):
        self._MongosMemory = MongosMemory

    @property
    def MongosNum(self):
        r"""Specifies the number of Mongos nodes. Value range: [3,32]. For querying the price of sharded cluster instances, this parameter is required. If it is left blank, the default value 3 is used.
        :rtype: int
        """
        return self._MongosNum

    @MongosNum.setter
    def MongosNum(self, MongosNum):
        self._MongosNum = MongosNum

    @property
    def ConfigServerCpu(self):
        r"""Specifies the number of ConfigServer CPU cores. The value is fixed as 1.
        :rtype: int
        """
        return self._ConfigServerCpu

    @ConfigServerCpu.setter
    def ConfigServerCpu(self, ConfigServerCpu):
        self._ConfigServerCpu = ConfigServerCpu

    @property
    def ConfigServerMemory(self):
        r"""Specifies the ConfigServer memory size. The value is fixed as 2. Unit: GB. This parameter can be left blank.
        :rtype: int
        """
        return self._ConfigServerMemory

    @ConfigServerMemory.setter
    def ConfigServerMemory(self, ConfigServerMemory):
        self._ConfigServerMemory = ConfigServerMemory

    @property
    def ConfigServerVolume(self):
        r"""Specifies the ConfigServer disk size. The value is fixed as 20. Unit: GB. This parameter can be left blank.
        :rtype: int
        """
        return self._ConfigServerVolume

    @ConfigServerVolume.setter
    def ConfigServerVolume(self, ConfigServerVolume):
        self._ConfigServerVolume = ConfigServerVolume


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._NodeNum = params.get("NodeNum")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._MongoVersion = params.get("MongoVersion")
        self._MachineCode = params.get("MachineCode")
        self._GoodsNum = params.get("GoodsNum")
        self._ClusterType = params.get("ClusterType")
        self._ReplicateSetNum = params.get("ReplicateSetNum")
        self._Period = params.get("Period")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._MongosCpu = params.get("MongosCpu")
        self._MongosMemory = params.get("MongosMemory")
        self._MongosNum = params.get("MongosNum")
        self._ConfigServerCpu = params.get("ConfigServerCpu")
        self._ConfigServerMemory = params.get("ConfigServerMemory")
        self._ConfigServerVolume = params.get("ConfigServerVolume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateDBInstancesResponse(AbstractModel):
    r"""InquirePriceCreateDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _Price: Price.
        :type Price: :class:`tencentcloud.mongodb.v20190725.models.DBInstancePrice`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        r"""Price.
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DBInstancePrice`
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = DBInstancePrice()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InquirePriceModifyDBInstanceSpecRequest(AbstractModel):
    r"""InquirePriceModifyDBInstanceSpec request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. For example, cmgo-p8vn****. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :type InstanceId: str
        :param _Memory: Instance memory size after configuration changes, in GB. The [DescribeSpecInfo](https://www.tencentcloud.comom/document/product/240/38567?from_cn_redirect=1) API can be called to obtain the specific sales specifications for memory.
        :type Memory: int
        :param _Volume: Instance disk size after configuration changes, in GB. The [DescribeSpecInfo](https://www.tencentcloud.comom/document/product/240/38567?from_cn_redirect=1) API can be called to obtain the maximum and minimum disk sizes corresponding to each CPU specification.
        :type Volume: int
        :param _NodeNum: Number of instance nodes. The [DescribeSpecInfo](https://www.tencentcloud.comom/document/product/240/38567?from_cn_redirect=1) API can be called to obtain the number of instance nodes.
- Replica set instance, which refers to the number of primary and secondary nodes for the instance after configuration changes.
- Sharded cluster instance, which refers to the number of primary and secondary nodes per shard for the instance after configuration changes.
**Note**: Do not initiate tasks of adjusting the number of nodes and shards and the node specifications simultaneously.
        :type NodeNum: int
        :param _ReplicateSetNum: Sharded cluster instance, which refers to the number of shards for the instance after configuration changes. Value range: [2, 36].
**Note**: The number of shards after changes cannot be less than the current number. Do not initiate tasks of adjusting the number of nodes and shards and the node specifications simultaneously.
        :type ReplicateSetNum: int
        """
        self._InstanceId = None
        self._Memory = None
        self._Volume = None
        self._NodeNum = None
        self._ReplicateSetNum = None

    @property
    def InstanceId(self):
        r"""Instance ID. For example, cmgo-p8vn****. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Memory(self):
        r"""Instance memory size after configuration changes, in GB. The [DescribeSpecInfo](https://www.tencentcloud.comom/document/product/240/38567?from_cn_redirect=1) API can be called to obtain the specific sales specifications for memory.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        r"""Instance disk size after configuration changes, in GB. The [DescribeSpecInfo](https://www.tencentcloud.comom/document/product/240/38567?from_cn_redirect=1) API can be called to obtain the maximum and minimum disk sizes corresponding to each CPU specification.
        :rtype: int
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def NodeNum(self):
        r"""Number of instance nodes. The [DescribeSpecInfo](https://www.tencentcloud.comom/document/product/240/38567?from_cn_redirect=1) API can be called to obtain the number of instance nodes.
- Replica set instance, which refers to the number of primary and secondary nodes for the instance after configuration changes.
- Sharded cluster instance, which refers to the number of primary and secondary nodes per shard for the instance after configuration changes.
**Note**: Do not initiate tasks of adjusting the number of nodes and shards and the node specifications simultaneously.
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def ReplicateSetNum(self):
        r"""Sharded cluster instance, which refers to the number of shards for the instance after configuration changes. Value range: [2, 36].
**Note**: The number of shards after changes cannot be less than the current number. Do not initiate tasks of adjusting the number of nodes and shards and the node specifications simultaneously.
        :rtype: int
        """
        return self._ReplicateSetNum

    @ReplicateSetNum.setter
    def ReplicateSetNum(self, ReplicateSetNum):
        self._ReplicateSetNum = ReplicateSetNum


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._NodeNum = params.get("NodeNum")
        self._ReplicateSetNum = params.get("ReplicateSetNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceModifyDBInstanceSpecResponse(AbstractModel):
    r"""InquirePriceModifyDBInstanceSpec response structure.

    """

    def __init__(self):
        r"""
        :param _Price: Price.
        :type Price: :class:`tencentcloud.mongodb.v20190725.models.DBInstancePrice`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        r"""Price.
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DBInstancePrice`
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = DBInstancePrice()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InquirePriceRenewDBInstancesRequest(AbstractModel):
    r"""InquirePriceRenewDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/MongoDB) and copy the instance ID from the instance list. Up to 5 instances can be queried at a time.
        :type InstanceIds: list of str
        :param _InstanceChargePrepaid: The parameter setting for the prepaid mode (monthly subscription mode). This parameter can specify the renewal period, whether to set automatic renewal, and other attributes of the monthly subscription instance.
        :type InstanceChargePrepaid: :class:`tencentcloud.mongodb.v20190725.models.InstanceChargePrepaid`
        """
        self._InstanceIds = None
        self._InstanceChargePrepaid = None

    @property
    def InstanceIds(self):
        r"""Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/MongoDB) and copy the instance ID from the instance list. Up to 5 instances can be queried at a time.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceChargePrepaid(self):
        r"""The parameter setting for the prepaid mode (monthly subscription mode). This parameter can specify the renewal period, whether to set automatic renewal, and other attributes of the monthly subscription instance.
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.InstanceChargePrepaid`
        """
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceRenewDBInstancesResponse(AbstractModel):
    r"""InquirePriceRenewDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _Price: Price.
        :type Price: :class:`tencentcloud.mongodb.v20190725.models.DBInstancePrice`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        r"""Price.
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DBInstancePrice`
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = DBInstancePrice()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InstanceChargePrepaid(AbstractModel):
    r"""Description on the billing mode of an instance

    """

    def __init__(self):
        r"""
        :param _Period: Instance purchase duration. Unit: months. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, and 36. Default value: 1.
        :type Period: int
        :param _RenewFlag: Automatic renewal flag. Valid values:
 - NOTIFY_AND_AUTO_RENEW: A notification is sent upon expiration, and the instance is renewed automatically. If the account balance is sufficient, the instance will be renewed automatically on a monthly basis after expiration.
 - NOTIFY_AND_MANUAL_RENEW: A notification is sent upon expiration, but the instance is not renewed automatically. Default value: NOTIFY_AND_MANUAL_RENEW.
 - DISABLE_NOTIFY_AND_MANUAL_RENEW: No notification is sent upon expiration, and the instance is not renewed automatically.
        :type RenewFlag: str
        """
        self._Period = None
        self._RenewFlag = None

    @property
    def Period(self):
        r"""Instance purchase duration. Unit: months. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, and 36. Default value: 1.
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        r"""Automatic renewal flag. Valid values:
 - NOTIFY_AND_AUTO_RENEW: A notification is sent upon expiration, and the instance is renewed automatically. If the account balance is sufficient, the instance will be renewed automatically on a monthly basis after expiration.
 - NOTIFY_AND_MANUAL_RENEW: A notification is sent upon expiration, but the instance is not renewed automatically. Default value: NOTIFY_AND_MANUAL_RENEW.
 - DISABLE_NOTIFY_AND_MANUAL_RENEW: No notification is sent upon expiration, and the instance is not renewed automatically.
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDetail(AbstractModel):
    r"""Instance details.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _PayMode: Billing type. Valid value: 0 (pay-as-you-go)
        :type PayMode: int
        :param _ProjectId: Project ID.
        :type ProjectId: int
        :param _ClusterType: Cluster type.
- 0: replica set instance.
- 1: sharded cluster instance.
        :type ClusterType: int
        :param _Region: Region information
        :type Region: str
        :param _Zone: AZ information
        :type Zone: str
        :param _NetType: Network type.
- 0: basic network.
- 1: VPC.
        :type NetType: int
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: Subnet ID of VPC
        :type SubnetId: str
        :param _Status: Instance status.
- 0: to be initialized.
- 1: processing, such as specification changes and parameter modifications.
- 2: running normally.
- -2: isolated (yearly/monthly subscription).
- -3: isolated (pay-as-you-go).
        :type Status: int
        :param _Vip: Instance IP
        :type Vip: str
        :param _Vport: Port number
        :type Vport: int
        :param _CreateTime: Instance creation time
        :type CreateTime: str
        :param _DeadLine: Instance expiration time
        :type DeadLine: str
        :param _MongoVersion: Storage engine version information on instances.
- MONGO_36_WT: version of the MongoDB 3.6 WiredTiger storage engine.
- MONGO_40_WT: version of the MongoDB 4.0 WiredTiger storage engine.
- MONGO_42_WT: version of the MongoDB 4.2 WiredTiger storage engine.
- MONGO_44_WT: version of the MongoDB 4.4 WiredTiger storage engine.
- MONGO_50_WT: version of the MongoDB 5.0 WiredTiger storage engine.
- MONGO_60_WT: version of the MongoDB 6.0 WiredTiger storage engine.
- MONGO_70_WT: version of the MongoDB 7.0 WiredTiger storage engine.
        :type MongoVersion: str
        :param _Memory: Instance memory specification, in MB.
        :type Memory: int
        :param _Volume: Instance disk specification, in MB.
        :type Volume: int
        :param _CpuNum: Number of the instance CPU cores.
        :type CpuNum: int
        :param _MachineType: Instance machine type.
- HIO10G: general HIO 10GE type.
- HCD: Cloud Disk Edition type.
        :type MachineType: str
        :param _SecondaryNum: Number of secondary nodes of an instance
        :type SecondaryNum: int
        :param _ReplicationSetNum: Number of instance shards
        :type ReplicationSetNum: int
        :param _AutoRenewFlag: Automatic renewal flag for the instance.
- 0: manual renewal.
- 1: automatic renewal.
- 2: no renewal after confirmation.
        :type AutoRenewFlag: int
        :param _UsedVolume: Used capacity, in MB.
        :type UsedVolume: int
        :param _MaintenanceStart: Start time of the maintenance time
        :type MaintenanceStart: str
        :param _MaintenanceEnd: End time of the maintenance time
        :type MaintenanceEnd: str
        :param _ReplicaSets: Shard information
        :type ReplicaSets: list of ShardInfo
        :param _ReadonlyInstances: Information of read-only instances
        :type ReadonlyInstances: list of DBInstanceInfo
        :param _StandbyInstances: Information of disaster recovery instances
        :type StandbyInstances: list of DBInstanceInfo
        :param _CloneInstances: Information of temp instances
        :type CloneInstances: list of DBInstanceInfo
        :param _RelatedInstance: Information of associated instances. For a regular instance, this field represents the information of its temp instance; for a temp instance, this field represents the information of its regular instance; and for a read-only instance or a disaster recovery instance, this field represents the information of its primary instance.
        :type RelatedInstance: :class:`tencentcloud.mongodb.v20190725.models.DBInstanceInfo`
        :param _Tags: Instance tag information set
        :type Tags: list of TagInfo
        :param _InstanceVer: Instance version
        :type InstanceVer: int
        :param _ClusterVer: Instance version
        :type ClusterVer: int
        :param _Protocol: Protocol information: mongodb.
        :type Protocol: int
        :param _InstanceType: Instance type.
- 0: all instances.
- 1: formal instance.
- 2: temporary instance.
- 3: read-only instance.
- -1: include the formal, read-only, and disaster recovery instance simultaneously.
        :type InstanceType: int
        :param _InstanceStatusDesc: Instance status description.
        :type InstanceStatusDesc: str
        :param _RealInstanceId: Physical instance ID corresponding to the instance. The instances that have been rolled back and replaced have different InstanceIds and RealInstanceIds, which need to be obtained through the physical ID in scenarios such as obtaining monitoring data from Barad.
        :type RealInstanceId: str
        :param _MongosNodeNum: Number of Mongos nodes.
        :type MongosNodeNum: int
        :param _MongosMemory: Mongos node memory, in MB.
        :type MongosMemory: int
        :param _MongosCpuNum: Number of Mongos node CPU cores.
        :type MongosCpuNum: int
        :param _ConfigServerNodeNum: Number of ConfigServer nodes.
        :type ConfigServerNodeNum: int
        :param _ConfigServerMemory: Config Server node memory, in MB.
        :type ConfigServerMemory: int
        :param _ConfigServerVolume: Config Server node disk size, in MB.
        :type ConfigServerVolume: int
        :param _ConfigServerCpuNum: Number of ConfigServer node CPU cores.
        :type ConfigServerCpuNum: int
        :param _ReadonlyNodeNum: Number of read-only nodes.
        :type ReadonlyNodeNum: int
        """
        self._InstanceId = None
        self._InstanceName = None
        self._PayMode = None
        self._ProjectId = None
        self._ClusterType = None
        self._Region = None
        self._Zone = None
        self._NetType = None
        self._VpcId = None
        self._SubnetId = None
        self._Status = None
        self._Vip = None
        self._Vport = None
        self._CreateTime = None
        self._DeadLine = None
        self._MongoVersion = None
        self._Memory = None
        self._Volume = None
        self._CpuNum = None
        self._MachineType = None
        self._SecondaryNum = None
        self._ReplicationSetNum = None
        self._AutoRenewFlag = None
        self._UsedVolume = None
        self._MaintenanceStart = None
        self._MaintenanceEnd = None
        self._ReplicaSets = None
        self._ReadonlyInstances = None
        self._StandbyInstances = None
        self._CloneInstances = None
        self._RelatedInstance = None
        self._Tags = None
        self._InstanceVer = None
        self._ClusterVer = None
        self._Protocol = None
        self._InstanceType = None
        self._InstanceStatusDesc = None
        self._RealInstanceId = None
        self._MongosNodeNum = None
        self._MongosMemory = None
        self._MongosCpuNum = None
        self._ConfigServerNodeNum = None
        self._ConfigServerMemory = None
        self._ConfigServerVolume = None
        self._ConfigServerCpuNum = None
        self._ReadonlyNodeNum = None

    @property
    def InstanceId(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""Instance name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def PayMode(self):
        r"""Billing type. Valid value: 0 (pay-as-you-go)
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ProjectId(self):
        r"""Project ID.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ClusterType(self):
        r"""Cluster type.
- 0: replica set instance.
- 1: sharded cluster instance.
        :rtype: int
        """
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def Region(self):
        r"""Region information
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        r"""AZ information
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def NetType(self):
        r"""Network type.
- 0: basic network.
- 1: VPC.
        :rtype: int
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def VpcId(self):
        r"""VPC ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""Subnet ID of VPC
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Status(self):
        r"""Instance status.
- 0: to be initialized.
- 1: processing, such as specification changes and parameter modifications.
- 2: running normally.
- -2: isolated (yearly/monthly subscription).
- -3: isolated (pay-as-you-go).
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Vip(self):
        r"""Instance IP
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        r"""Port number
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def CreateTime(self):
        r"""Instance creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DeadLine(self):
        r"""Instance expiration time
        :rtype: str
        """
        return self._DeadLine

    @DeadLine.setter
    def DeadLine(self, DeadLine):
        self._DeadLine = DeadLine

    @property
    def MongoVersion(self):
        r"""Storage engine version information on instances.
- MONGO_36_WT: version of the MongoDB 3.6 WiredTiger storage engine.
- MONGO_40_WT: version of the MongoDB 4.0 WiredTiger storage engine.
- MONGO_42_WT: version of the MongoDB 4.2 WiredTiger storage engine.
- MONGO_44_WT: version of the MongoDB 4.4 WiredTiger storage engine.
- MONGO_50_WT: version of the MongoDB 5.0 WiredTiger storage engine.
- MONGO_60_WT: version of the MongoDB 6.0 WiredTiger storage engine.
- MONGO_70_WT: version of the MongoDB 7.0 WiredTiger storage engine.
        :rtype: str
        """
        return self._MongoVersion

    @MongoVersion.setter
    def MongoVersion(self, MongoVersion):
        self._MongoVersion = MongoVersion

    @property
    def Memory(self):
        r"""Instance memory specification, in MB.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        r"""Instance disk specification, in MB.
        :rtype: int
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def CpuNum(self):
        r"""Number of the instance CPU cores.
        :rtype: int
        """
        return self._CpuNum

    @CpuNum.setter
    def CpuNum(self, CpuNum):
        self._CpuNum = CpuNum

    @property
    def MachineType(self):
        r"""Instance machine type.
- HIO10G: general HIO 10GE type.
- HCD: Cloud Disk Edition type.
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType

    @property
    def SecondaryNum(self):
        r"""Number of secondary nodes of an instance
        :rtype: int
        """
        return self._SecondaryNum

    @SecondaryNum.setter
    def SecondaryNum(self, SecondaryNum):
        self._SecondaryNum = SecondaryNum

    @property
    def ReplicationSetNum(self):
        r"""Number of instance shards
        :rtype: int
        """
        return self._ReplicationSetNum

    @ReplicationSetNum.setter
    def ReplicationSetNum(self, ReplicationSetNum):
        self._ReplicationSetNum = ReplicationSetNum

    @property
    def AutoRenewFlag(self):
        r"""Automatic renewal flag for the instance.
- 0: manual renewal.
- 1: automatic renewal.
- 2: no renewal after confirmation.
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def UsedVolume(self):
        r"""Used capacity, in MB.
        :rtype: int
        """
        return self._UsedVolume

    @UsedVolume.setter
    def UsedVolume(self, UsedVolume):
        self._UsedVolume = UsedVolume

    @property
    def MaintenanceStart(self):
        r"""Start time of the maintenance time
        :rtype: str
        """
        return self._MaintenanceStart

    @MaintenanceStart.setter
    def MaintenanceStart(self, MaintenanceStart):
        self._MaintenanceStart = MaintenanceStart

    @property
    def MaintenanceEnd(self):
        r"""End time of the maintenance time
        :rtype: str
        """
        return self._MaintenanceEnd

    @MaintenanceEnd.setter
    def MaintenanceEnd(self, MaintenanceEnd):
        self._MaintenanceEnd = MaintenanceEnd

    @property
    def ReplicaSets(self):
        r"""Shard information
        :rtype: list of ShardInfo
        """
        return self._ReplicaSets

    @ReplicaSets.setter
    def ReplicaSets(self, ReplicaSets):
        self._ReplicaSets = ReplicaSets

    @property
    def ReadonlyInstances(self):
        r"""Information of read-only instances
        :rtype: list of DBInstanceInfo
        """
        return self._ReadonlyInstances

    @ReadonlyInstances.setter
    def ReadonlyInstances(self, ReadonlyInstances):
        self._ReadonlyInstances = ReadonlyInstances

    @property
    def StandbyInstances(self):
        r"""Information of disaster recovery instances
        :rtype: list of DBInstanceInfo
        """
        return self._StandbyInstances

    @StandbyInstances.setter
    def StandbyInstances(self, StandbyInstances):
        self._StandbyInstances = StandbyInstances

    @property
    def CloneInstances(self):
        r"""Information of temp instances
        :rtype: list of DBInstanceInfo
        """
        return self._CloneInstances

    @CloneInstances.setter
    def CloneInstances(self, CloneInstances):
        self._CloneInstances = CloneInstances

    @property
    def RelatedInstance(self):
        r"""Information of associated instances. For a regular instance, this field represents the information of its temp instance; for a temp instance, this field represents the information of its regular instance; and for a read-only instance or a disaster recovery instance, this field represents the information of its primary instance.
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DBInstanceInfo`
        """
        return self._RelatedInstance

    @RelatedInstance.setter
    def RelatedInstance(self, RelatedInstance):
        self._RelatedInstance = RelatedInstance

    @property
    def Tags(self):
        r"""Instance tag information set
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceVer(self):
        r"""Instance version
        :rtype: int
        """
        return self._InstanceVer

    @InstanceVer.setter
    def InstanceVer(self, InstanceVer):
        self._InstanceVer = InstanceVer

    @property
    def ClusterVer(self):
        r"""Instance version
        :rtype: int
        """
        return self._ClusterVer

    @ClusterVer.setter
    def ClusterVer(self, ClusterVer):
        self._ClusterVer = ClusterVer

    @property
    def Protocol(self):
        r"""Protocol information: mongodb.
        :rtype: int
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def InstanceType(self):
        r"""Instance type.
- 0: all instances.
- 1: formal instance.
- 2: temporary instance.
- 3: read-only instance.
- -1: include the formal, read-only, and disaster recovery instance simultaneously.
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceStatusDesc(self):
        r"""Instance status description.
        :rtype: str
        """
        return self._InstanceStatusDesc

    @InstanceStatusDesc.setter
    def InstanceStatusDesc(self, InstanceStatusDesc):
        self._InstanceStatusDesc = InstanceStatusDesc

    @property
    def RealInstanceId(self):
        r"""Physical instance ID corresponding to the instance. The instances that have been rolled back and replaced have different InstanceIds and RealInstanceIds, which need to be obtained through the physical ID in scenarios such as obtaining monitoring data from Barad.
        :rtype: str
        """
        return self._RealInstanceId

    @RealInstanceId.setter
    def RealInstanceId(self, RealInstanceId):
        self._RealInstanceId = RealInstanceId

    @property
    def MongosNodeNum(self):
        r"""Number of Mongos nodes.
        :rtype: int
        """
        return self._MongosNodeNum

    @MongosNodeNum.setter
    def MongosNodeNum(self, MongosNodeNum):
        self._MongosNodeNum = MongosNodeNum

    @property
    def MongosMemory(self):
        r"""Mongos node memory, in MB.
        :rtype: int
        """
        return self._MongosMemory

    @MongosMemory.setter
    def MongosMemory(self, MongosMemory):
        self._MongosMemory = MongosMemory

    @property
    def MongosCpuNum(self):
        r"""Number of Mongos node CPU cores.
        :rtype: int
        """
        return self._MongosCpuNum

    @MongosCpuNum.setter
    def MongosCpuNum(self, MongosCpuNum):
        self._MongosCpuNum = MongosCpuNum

    @property
    def ConfigServerNodeNum(self):
        r"""Number of ConfigServer nodes.
        :rtype: int
        """
        return self._ConfigServerNodeNum

    @ConfigServerNodeNum.setter
    def ConfigServerNodeNum(self, ConfigServerNodeNum):
        self._ConfigServerNodeNum = ConfigServerNodeNum

    @property
    def ConfigServerMemory(self):
        r"""Config Server node memory, in MB.
        :rtype: int
        """
        return self._ConfigServerMemory

    @ConfigServerMemory.setter
    def ConfigServerMemory(self, ConfigServerMemory):
        self._ConfigServerMemory = ConfigServerMemory

    @property
    def ConfigServerVolume(self):
        r"""Config Server node disk size, in MB.
        :rtype: int
        """
        return self._ConfigServerVolume

    @ConfigServerVolume.setter
    def ConfigServerVolume(self, ConfigServerVolume):
        self._ConfigServerVolume = ConfigServerVolume

    @property
    def ConfigServerCpuNum(self):
        r"""Number of ConfigServer node CPU cores.
        :rtype: int
        """
        return self._ConfigServerCpuNum

    @ConfigServerCpuNum.setter
    def ConfigServerCpuNum(self, ConfigServerCpuNum):
        self._ConfigServerCpuNum = ConfigServerCpuNum

    @property
    def ReadonlyNodeNum(self):
        r"""Number of read-only nodes.
        :rtype: int
        """
        return self._ReadonlyNodeNum

    @ReadonlyNodeNum.setter
    def ReadonlyNodeNum(self, ReadonlyNodeNum):
        self._ReadonlyNodeNum = ReadonlyNodeNum


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._PayMode = params.get("PayMode")
        self._ProjectId = params.get("ProjectId")
        self._ClusterType = params.get("ClusterType")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._NetType = params.get("NetType")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Status = params.get("Status")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._CreateTime = params.get("CreateTime")
        self._DeadLine = params.get("DeadLine")
        self._MongoVersion = params.get("MongoVersion")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._CpuNum = params.get("CpuNum")
        self._MachineType = params.get("MachineType")
        self._SecondaryNum = params.get("SecondaryNum")
        self._ReplicationSetNum = params.get("ReplicationSetNum")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._UsedVolume = params.get("UsedVolume")
        self._MaintenanceStart = params.get("MaintenanceStart")
        self._MaintenanceEnd = params.get("MaintenanceEnd")
        if params.get("ReplicaSets") is not None:
            self._ReplicaSets = []
            for item in params.get("ReplicaSets"):
                obj = ShardInfo()
                obj._deserialize(item)
                self._ReplicaSets.append(obj)
        if params.get("ReadonlyInstances") is not None:
            self._ReadonlyInstances = []
            for item in params.get("ReadonlyInstances"):
                obj = DBInstanceInfo()
                obj._deserialize(item)
                self._ReadonlyInstances.append(obj)
        if params.get("StandbyInstances") is not None:
            self._StandbyInstances = []
            for item in params.get("StandbyInstances"):
                obj = DBInstanceInfo()
                obj._deserialize(item)
                self._StandbyInstances.append(obj)
        if params.get("CloneInstances") is not None:
            self._CloneInstances = []
            for item in params.get("CloneInstances"):
                obj = DBInstanceInfo()
                obj._deserialize(item)
                self._CloneInstances.append(obj)
        if params.get("RelatedInstance") is not None:
            self._RelatedInstance = DBInstanceInfo()
            self._RelatedInstance._deserialize(params.get("RelatedInstance"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceVer = params.get("InstanceVer")
        self._ClusterVer = params.get("ClusterVer")
        self._Protocol = params.get("Protocol")
        self._InstanceType = params.get("InstanceType")
        self._InstanceStatusDesc = params.get("InstanceStatusDesc")
        self._RealInstanceId = params.get("RealInstanceId")
        self._MongosNodeNum = params.get("MongosNodeNum")
        self._MongosMemory = params.get("MongosMemory")
        self._MongosCpuNum = params.get("MongosCpuNum")
        self._ConfigServerNodeNum = params.get("ConfigServerNodeNum")
        self._ConfigServerMemory = params.get("ConfigServerMemory")
        self._ConfigServerVolume = params.get("ConfigServerVolume")
        self._ConfigServerCpuNum = params.get("ConfigServerCpuNum")
        self._ReadonlyNodeNum = params.get("ReadonlyNodeNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceEnableSSLRequest(AbstractModel):
    r"""InstanceEnableSSL request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _Enable: Configures whether to enable SSL for access.
- true: enabled.
- false: disabled.
        :type Enable: bool
        """
        self._InstanceId = None
        self._Enable = None

    @property
    def InstanceId(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Enable(self):
        r"""Configures whether to enable SSL for access.
- true: enabled.
- false: disabled.
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceEnableSSLResponse(AbstractModel):
    r"""InstanceEnableSSL response structure.

    """

    def __init__(self):
        r"""
        :param _Status: SSL enabling status.
- 0: disabled.
- 1: enabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _ExpiredTime: Certificate file expiration time, in the format of 2023-05-01 12:00:00.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpiredTime: str
        :param _CertUrl: Download URL of the certificate file.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertUrl: str
        :param _FlowId: Process ID.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._ExpiredTime = None
        self._CertUrl = None
        self._FlowId = None
        self._RequestId = None

    @property
    def Status(self):
        r"""SSL enabling status.
- 0: disabled.
- 1: enabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ExpiredTime(self):
        r"""Certificate file expiration time, in the format of 2023-05-01 12:00:00.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def CertUrl(self):
        r"""Download URL of the certificate file.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CertUrl

    @CertUrl.setter
    def CertUrl(self, CertUrl):
        self._CertUrl = CertUrl

    @property
    def FlowId(self):
        r"""Process ID.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ExpiredTime = params.get("ExpiredTime")
        self._CertUrl = params.get("CertUrl")
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class InstanceEnumParam(AbstractModel):
    r"""The collection of modifiable enum parameters of an instance.

    """

    def __init__(self):
        r"""
        :param _CurrentValue: Current parameter value.
        :type CurrentValue: str
        :param _DefaultValue: Default parameter value.
        :type DefaultValue: str
        :param _EnumValue: Enumerated values, which indicate all supported values.
        :type EnumValue: list of str
        :param _NeedRestart: Whether a restart is required for the parameters to take effect after modification.
 - 1: Restart is required for the parameters to take effect.
 - 0: Restart is not required. Once set, the parameters take effect immediately.
        :type NeedRestart: str
        :param _ParamName: Parameter name.
        :type ParamName: str
        :param _Tips: Parameter description.
        :type Tips: list of str
        :param _ValueType: Parameter type description.
        :type ValueType: str
        :param _Status: Whether the parameter values are used during running.
 - 1. parameter values used during running.
 - 0: parameter values not used during running.
        :type Status: int
        """
        self._CurrentValue = None
        self._DefaultValue = None
        self._EnumValue = None
        self._NeedRestart = None
        self._ParamName = None
        self._Tips = None
        self._ValueType = None
        self._Status = None

    @property
    def CurrentValue(self):
        r"""Current parameter value.
        :rtype: str
        """
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def DefaultValue(self):
        r"""Default parameter value.
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def EnumValue(self):
        r"""Enumerated values, which indicate all supported values.
        :rtype: list of str
        """
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def NeedRestart(self):
        r"""Whether a restart is required for the parameters to take effect after modification.
 - 1: Restart is required for the parameters to take effect.
 - 0: Restart is not required. Once set, the parameters take effect immediately.
        :rtype: str
        """
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def ParamName(self):
        r"""Parameter name.
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def Tips(self):
        r"""Parameter description.
        :rtype: list of str
        """
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def ValueType(self):
        r"""Parameter type description.
        :rtype: str
        """
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def Status(self):
        r"""Whether the parameter values are used during running.
 - 1. parameter values used during running.
 - 0: parameter values not used during running.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._CurrentValue = params.get("CurrentValue")
        self._DefaultValue = params.get("DefaultValue")
        self._EnumValue = params.get("EnumValue")
        self._NeedRestart = params.get("NeedRestart")
        self._ParamName = params.get("ParamName")
        self._Tips = params.get("Tips")
        self._ValueType = params.get("ValueType")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceIntegerParam(AbstractModel):
    r"""Collection of modifiable instance parameters of the Integer type.

    """

    def __init__(self):
        r"""
        :param _CurrentValue: Current parameter value.
        :type CurrentValue: str
        :param _DefaultValue: Default parameter value.
        :type DefaultValue: str
        :param _Max: Maximum parameter value.
        :type Max: str
        :param _Min: Minimum value.
        :type Min: str
        :param _NeedRestart: Whether a restart is required for the parameters to take effect after modification.
 - 1: Restart is required for the parameters to take effect.
 - 0: Restart is not required. Once set, the parameters take effect immediately.
        :type NeedRestart: str
        :param _ParamName: Parameter name.
        :type ParamName: str
        :param _Tips: Parameter description.
        :type Tips: list of str
        :param _ValueType: Parameter type.
        :type ValueType: str
        :param _Status: Whether the parameter values are used during running.
 - 1. parameter values used during running.
 - 0: parameter values not used during running.
        :type Status: int
        :param _Unit: Redundant field. It can be ignored.
        :type Unit: str
        """
        self._CurrentValue = None
        self._DefaultValue = None
        self._Max = None
        self._Min = None
        self._NeedRestart = None
        self._ParamName = None
        self._Tips = None
        self._ValueType = None
        self._Status = None
        self._Unit = None

    @property
    def CurrentValue(self):
        r"""Current parameter value.
        :rtype: str
        """
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def DefaultValue(self):
        r"""Default parameter value.
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def Max(self):
        r"""Maximum parameter value.
        :rtype: str
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Min(self):
        r"""Minimum value.
        :rtype: str
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def NeedRestart(self):
        r"""Whether a restart is required for the parameters to take effect after modification.
 - 1: Restart is required for the parameters to take effect.
 - 0: Restart is not required. Once set, the parameters take effect immediately.
        :rtype: str
        """
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def ParamName(self):
        r"""Parameter name.
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def Tips(self):
        r"""Parameter description.
        :rtype: list of str
        """
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def ValueType(self):
        r"""Parameter type.
        :rtype: str
        """
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def Status(self):
        r"""Whether the parameter values are used during running.
 - 1. parameter values used during running.
 - 0: parameter values not used during running.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Unit(self):
        r"""Redundant field. It can be ignored.
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit


    def _deserialize(self, params):
        self._CurrentValue = params.get("CurrentValue")
        self._DefaultValue = params.get("DefaultValue")
        self._Max = params.get("Max")
        self._Min = params.get("Min")
        self._NeedRestart = params.get("NeedRestart")
        self._ParamName = params.get("ParamName")
        self._Tips = params.get("Tips")
        self._ValueType = params.get("ValueType")
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
    r"""The collection of modifiable string parameters of an instance which are used to represent time ranges.

    """

    def __init__(self):
        r"""
        :param _CurrentValue: Current parameter value.
        :type CurrentValue: str
        :param _DefaultValue: Default parameter value.
        :type DefaultValue: str
        :param _EnumValue: Reference value range.
        :type EnumValue: list of str
        :param _NeedRestart: Whether a restart is required for the parameters to take effect after modification.
 - 1: Restart is required for the parameters to take effect.
 - 0: Restart is not required. Once set, the parameters take effect immediately.
        :type NeedRestart: str
        :param _ParamName: Parameter name.
        :type ParamName: str
        :param _Status: Whether the parameter values are used during running.
 - 1. parameter values used during running.
 - 0: parameter values not used during running.
        :type Status: int
        :param _Tips: Parameter description.
        :type Tips: list of str
        :param _ValueType: Describes the type of the current values. Default value: multi.
        :type ValueType: str
        """
        self._CurrentValue = None
        self._DefaultValue = None
        self._EnumValue = None
        self._NeedRestart = None
        self._ParamName = None
        self._Status = None
        self._Tips = None
        self._ValueType = None

    @property
    def CurrentValue(self):
        r"""Current parameter value.
        :rtype: str
        """
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def DefaultValue(self):
        r"""Default parameter value.
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def EnumValue(self):
        r"""Reference value range.
        :rtype: list of str
        """
        return self._EnumValue

    @EnumValue.setter
    def EnumValue(self, EnumValue):
        self._EnumValue = EnumValue

    @property
    def NeedRestart(self):
        r"""Whether a restart is required for the parameters to take effect after modification.
 - 1: Restart is required for the parameters to take effect.
 - 0: Restart is not required. Once set, the parameters take effect immediately.
        :rtype: str
        """
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def ParamName(self):
        r"""Parameter name.
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def Status(self):
        r"""Whether the parameter values are used during running.
 - 1. parameter values used during running.
 - 0: parameter values not used during running.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Tips(self):
        r"""Parameter description.
        :rtype: list of str
        """
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def ValueType(self):
        r"""Describes the type of the current values. Default value: multi.
        :rtype: str
        """
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType


    def _deserialize(self, params):
        self._CurrentValue = params.get("CurrentValue")
        self._DefaultValue = params.get("DefaultValue")
        self._EnumValue = params.get("EnumValue")
        self._NeedRestart = params.get("NeedRestart")
        self._ParamName = params.get("ParamName")
        self._Status = params.get("Status")
        self._Tips = params.get("Tips")
        self._ValueType = params.get("ValueType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTextParam(AbstractModel):
    r"""Collection of modifiable instance parameters whose values are of the Text type.

    """

    def __init__(self):
        r"""
        :param _CurrentValue: Current parameter value.
        :type CurrentValue: str
        :param _DefaultValue: Default parameter value.
        :type DefaultValue: str
        :param _NeedRestart: Whether a restart is required after the parameter values are modified.
        :type NeedRestart: str
        :param _ParamName: Parameter name.
        :type ParamName: str
        :param _TextValue: Corresponding values of the Text-type parameters.
        :type TextValue: str
        :param _Tips: Parameter description.
        :type Tips: list of str
        :param _ValueType: Parameter type description.
        :type ValueType: str
        :param _Status: Whether the parameter values are used during running.
 - 1. parameter values used during running.
 - 0: parameter values not used during running.
        :type Status: str
        """
        self._CurrentValue = None
        self._DefaultValue = None
        self._NeedRestart = None
        self._ParamName = None
        self._TextValue = None
        self._Tips = None
        self._ValueType = None
        self._Status = None

    @property
    def CurrentValue(self):
        r"""Current parameter value.
        :rtype: str
        """
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def DefaultValue(self):
        r"""Default parameter value.
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def NeedRestart(self):
        r"""Whether a restart is required after the parameter values are modified.
        :rtype: str
        """
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def ParamName(self):
        r"""Parameter name.
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def TextValue(self):
        r"""Corresponding values of the Text-type parameters.
        :rtype: str
        """
        return self._TextValue

    @TextValue.setter
    def TextValue(self, TextValue):
        self._TextValue = TextValue

    @property
    def Tips(self):
        r"""Parameter description.
        :rtype: list of str
        """
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def ValueType(self):
        r"""Parameter type description.
        :rtype: str
        """
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def Status(self):
        r"""Whether the parameter values are used during running.
 - 1. parameter values used during running.
 - 0: parameter values not used during running.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._CurrentValue = params.get("CurrentValue")
        self._DefaultValue = params.get("DefaultValue")
        self._NeedRestart = params.get("NeedRestart")
        self._ParamName = params.get("ParamName")
        self._TextValue = params.get("TextValue")
        self._Tips = params.get("Tips")
        self._ValueType = params.get("ValueType")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDBInstanceRequest(AbstractModel):
    r"""IsolateDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the ID of the instance to be isolated from the instance list.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the ID of the instance to be isolated from the instance list.
        :rtype: str
        """
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
        


class IsolateDBInstanceResponse(AbstractModel):
    r"""IsolateDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        r"""Async task request ID, which can be used to query the execution result of an async task.
        :rtype: str
        """
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class KillOpsRequest(AbstractModel):
    r"""KillOps request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :type InstanceId: str
        :param _Operations: Operation to be terminated.
        :type Operations: list of Operation
        """
        self._InstanceId = None
        self._Operations = None

    @property
    def InstanceId(self):
        r"""Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Operations(self):
        r"""Operation to be terminated.
        :rtype: list of Operation
        """
        return self._Operations

    @Operations.setter
    def Operations(self, Operations):
        self._Operations = Operations


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Operations") is not None:
            self._Operations = []
            for item in params.get("Operations"):
                obj = Operation()
                obj._deserialize(item)
                self._Operations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KillOpsResponse(AbstractModel):
    r"""KillOps response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class LogInfo(AbstractModel):
    r"""Log details.

    """

    def __init__(self):
        r"""
        :param _LogComponent: Log category.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogComponent: str
        :param _LogLevel: Log level.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogLevel: str
        :param _LogTime: Log generation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogTime: str
        :param _LogDetail: Log details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogDetail: str
        :param _LogConnection: Log connection information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogConnection: str
        :param _LogId: Log ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogId: str
        """
        self._LogComponent = None
        self._LogLevel = None
        self._LogTime = None
        self._LogDetail = None
        self._LogConnection = None
        self._LogId = None

    @property
    def LogComponent(self):
        r"""Log category.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LogComponent

    @LogComponent.setter
    def LogComponent(self, LogComponent):
        self._LogComponent = LogComponent

    @property
    def LogLevel(self):
        r"""Log level.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LogLevel

    @LogLevel.setter
    def LogLevel(self, LogLevel):
        self._LogLevel = LogLevel

    @property
    def LogTime(self):
        r"""Log generation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LogTime

    @LogTime.setter
    def LogTime(self, LogTime):
        self._LogTime = LogTime

    @property
    def LogDetail(self):
        r"""Log details.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LogDetail

    @LogDetail.setter
    def LogDetail(self, LogDetail):
        self._LogDetail = LogDetail

    @property
    def LogConnection(self):
        r"""Log connection information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LogConnection

    @LogConnection.setter
    def LogConnection(self, LogConnection):
        self._LogConnection = LogConnection

    @property
    def LogId(self):
        r"""Log ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LogId

    @LogId.setter
    def LogId(self, LogId):
        self._LogId = LogId


    def _deserialize(self, params):
        self._LogComponent = params.get("LogComponent")
        self._LogLevel = params.get("LogLevel")
        self._LogTime = params.get("LogTime")
        self._LogDetail = params.get("LogDetail")
        self._LogConnection = params.get("LogConnection")
        self._LogId = params.get("LogId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceNetworkAddressRequest(AbstractModel):
    r"""ModifyDBInstanceNetworkAddress request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Specifies the ID of the instance for modifying the network. For example, cmgo-p8vn****. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/MongoDB) and copy the instance ID from the instance list.

        :type InstanceId: str
        :param _OldIpExpiredTime: Retention period of the original IP address.
 - Unit: minutes. 0 means that the IP address is immediately repossessed.
 - The original IP address will be released after a scheduled period. Both the original and new IP addresses are accessible before release.

        :type OldIpExpiredTime: int
        :param _NewUniqVpcId: VPC ID after the switch. If the instance is using a basic network, this field is not required. The [DescribeDBInstances](https://www.tencentcloud.comom/document/product/240/38568?from_cn_redirect=1) API can be called to obtain the VPC ID.
        :type NewUniqVpcId: str
        :param _NewUniqSubnetId: VPC subnet ID after the switch. If the instance is using a basic network, this field is not required. The [DescribeDBInstances](https://www.tencentcloud.comom/document/product/240/38568?from_cn_redirect=1) API can be called to obtain the subnet ID of the VPC.
        :type NewUniqSubnetId: str
        :param _NetworkAddresses: IP address information, including the new IP address and the original IP address.
        :type NetworkAddresses: list of ModifyNetworkAddress
        """
        self._InstanceId = None
        self._OldIpExpiredTime = None
        self._NewUniqVpcId = None
        self._NewUniqSubnetId = None
        self._NetworkAddresses = None

    @property
    def InstanceId(self):
        r"""Specifies the ID of the instance for modifying the network. For example, cmgo-p8vn****. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/MongoDB) and copy the instance ID from the instance list.

        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OldIpExpiredTime(self):
        r"""Retention period of the original IP address.
 - Unit: minutes. 0 means that the IP address is immediately repossessed.
 - The original IP address will be released after a scheduled period. Both the original and new IP addresses are accessible before release.

        :rtype: int
        """
        return self._OldIpExpiredTime

    @OldIpExpiredTime.setter
    def OldIpExpiredTime(self, OldIpExpiredTime):
        self._OldIpExpiredTime = OldIpExpiredTime

    @property
    def NewUniqVpcId(self):
        r"""VPC ID after the switch. If the instance is using a basic network, this field is not required. The [DescribeDBInstances](https://www.tencentcloud.comom/document/product/240/38568?from_cn_redirect=1) API can be called to obtain the VPC ID.
        :rtype: str
        """
        return self._NewUniqVpcId

    @NewUniqVpcId.setter
    def NewUniqVpcId(self, NewUniqVpcId):
        self._NewUniqVpcId = NewUniqVpcId

    @property
    def NewUniqSubnetId(self):
        r"""VPC subnet ID after the switch. If the instance is using a basic network, this field is not required. The [DescribeDBInstances](https://www.tencentcloud.comom/document/product/240/38568?from_cn_redirect=1) API can be called to obtain the subnet ID of the VPC.
        :rtype: str
        """
        return self._NewUniqSubnetId

    @NewUniqSubnetId.setter
    def NewUniqSubnetId(self, NewUniqSubnetId):
        self._NewUniqSubnetId = NewUniqSubnetId

    @property
    def NetworkAddresses(self):
        r"""IP address information, including the new IP address and the original IP address.
        :rtype: list of ModifyNetworkAddress
        """
        return self._NetworkAddresses

    @NetworkAddresses.setter
    def NetworkAddresses(self, NetworkAddresses):
        self._NetworkAddresses = NetworkAddresses


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._OldIpExpiredTime = params.get("OldIpExpiredTime")
        self._NewUniqVpcId = params.get("NewUniqVpcId")
        self._NewUniqSubnetId = params.get("NewUniqSubnetId")
        if params.get("NetworkAddresses") is not None:
            self._NetworkAddresses = []
            for item in params.get("NetworkAddresses"):
                obj = ModifyNetworkAddress()
                obj._deserialize(item)
                self._NetworkAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceNetworkAddressResponse(AbstractModel):
    r"""ModifyDBInstanceNetworkAddress response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: ID of the asynchronous process task for modifying the network information.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""ID of the asynchronous process task for modifying the network information.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupRequest(AbstractModel):
    r"""ModifyDBInstanceSecurityGroup request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :type InstanceId: str
        :param _SecurityGroupIds: Target security group ID. Log in to the [security group console](https://console.cloud.tencent.com/vpc/security-group) page to copy the target security group ID.
**Note**: This input parameter performs a full replacement on all existing collections but not an incremental update. To modify it, import the expected full collections.
        :type SecurityGroupIds: list of str
        """
        self._InstanceId = None
        self._SecurityGroupIds = None

    @property
    def InstanceId(self):
        r"""Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SecurityGroupIds(self):
        r"""Target security group ID. Log in to the [security group console](https://console.cloud.tencent.com/vpc/security-group) page to copy the target security group ID.
**Note**: This input parameter performs a full replacement on all existing collections but not an incremental update. To modify it, import the expected full collections.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSecurityGroupResponse(AbstractModel):
    r"""ModifyDBInstanceSecurityGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDBInstanceSpecRequest(AbstractModel):
    r"""ModifyDBInstanceSpec request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :type InstanceId: str
        :param _Memory: Memory size after instance configuration changes, in GB. If this parameter is left blank, the default value is the current memory size of the instance. For the currently supported memory specifications, see [Product Specifications](https://www.tencentcloud.comom/document/product/240/64125?from_cn_redirect=1).
**Note**: Memory and disk configurations should be upgraded or downgraded simultaneously, meaning that Memory and Volume should be modified at the same time.
        :type Memory: int
        :param _Volume: Hard disk size after instance configuration changes, in GB. If this parameter is left blank, the default value is the current disk size of the instance. For the currently supported disk capacity, see [Product Specifications](https://www.tencentcloud.comom/document/product/240/64125?from_cn_redirect=1).
- Memory and disk configurations should be upgraded or downgraded at the same time, meaning that Memory and Volume should be modified at the same time.
- During configuration downgrade, the disk capacity after changes should be greater than 1.2 times the used disk capacity.
        :type Volume: int
        :param _OplogSize: (Deprecated) Use the independent API ResizeOplog.

Oplog size after instance configuration modification.
 - Unit: GB.
 - By default, the capacity occupied by Oplog is 10% of the disk capacity. The range of capacity occupied by Oplog supported by the system is [10%,90%] of the disk capacity.
        :type OplogSize: int
        :param _NodeNum: Number of Mongod nodes after instance changes (excluding read-only nodes).
- Number of replica set nodes. The value range of the number of nodes can be obtained through the response parameters MinNodeNum and MaxNodeNum of the [DescribeSpecInfo ](https://www.tencentcloud.comom/document/product/240/38567?from_cn_redirect=1) API.
- Number of nodes per shard in a sharded cluster. The value range of the number of nodes can be obtained through the response parameters MinReplicateSetNodeNum and MaxReplicateSetNodeNum of the [DescribeSpecInfo ](https://www.tencentcloud.comom/document/product/240/38567?from_cn_redirect=1) API.
**Note**: When the CPU and memory specifications of Mongod or Mongos nodes are changed, this parameter is not required, or enter the current number of Mongod or Mongos nodes (excluding read-only nodes).
        :type NodeNum: int
        :param _ReplicateSetNum: Number of shards after instance changes.
- The value range for the number of instance shards can be obtained through the response parameters **MinReplicateSetNum** and **MaxReplicateSetNum** of the [DescribeSpecInfo](https://www.tencentcloud.comom/document/product/240/38567?from_cn_redirect=1) API.
- The number of instance shards can only be increased and cannot be decreased.
        :type ReplicateSetNum: int
        :param _InMaintenance: Switch time for instance configuration modification.
 - 0: Execute the configuration modification task immediately after the adjustment is completed. Default value: 0.
 - 1: Execute the configuration modification task within the maintenance window.
**Note**: Adjusting the number of nodes and shards is unsupported <b>within the maintenance window</b>.
        :type InMaintenance: int
        :param _MongosMemory: Memory size of the Mongos node after sharded cluster instance configuration changes, in GB. For the specifications supported by the instance, see [Product Specifications](https://www.tencentcloud.comom/document/product/240/64125?from_cn_redirect=1).
        :type MongosMemory: str
        :param _AddNodeList: List of nodes to be added, containing the node type and AZ information.
        :type AddNodeList: list of AddNodeList
        :param _RemoveNodeList: Deletes the node list.
**Note**: According to the consistency principle for nodes of each shard on a sharded cluster instance, specify the nodes on shard 0 for node deletion from the sharded cluster instance. For example, cmgo-9nl1czif_0-node-readonly0 will delete the first read-only node of each shard.
        :type RemoveNodeList: list of RemoveNodeList
        """
        self._InstanceId = None
        self._Memory = None
        self._Volume = None
        self._OplogSize = None
        self._NodeNum = None
        self._ReplicateSetNum = None
        self._InMaintenance = None
        self._MongosMemory = None
        self._AddNodeList = None
        self._RemoveNodeList = None

    @property
    def InstanceId(self):
        r"""Instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Memory(self):
        r"""Memory size after instance configuration changes, in GB. If this parameter is left blank, the default value is the current memory size of the instance. For the currently supported memory specifications, see [Product Specifications](https://www.tencentcloud.comom/document/product/240/64125?from_cn_redirect=1).
**Note**: Memory and disk configurations should be upgraded or downgraded simultaneously, meaning that Memory and Volume should be modified at the same time.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        r"""Hard disk size after instance configuration changes, in GB. If this parameter is left blank, the default value is the current disk size of the instance. For the currently supported disk capacity, see [Product Specifications](https://www.tencentcloud.comom/document/product/240/64125?from_cn_redirect=1).
- Memory and disk configurations should be upgraded or downgraded at the same time, meaning that Memory and Volume should be modified at the same time.
- During configuration downgrade, the disk capacity after changes should be greater than 1.2 times the used disk capacity.
        :rtype: int
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def OplogSize(self):
        warnings.warn("parameter `OplogSize` is deprecated", DeprecationWarning) 

        r"""(Deprecated) Use the independent API ResizeOplog.

Oplog size after instance configuration modification.
 - Unit: GB.
 - By default, the capacity occupied by Oplog is 10% of the disk capacity. The range of capacity occupied by Oplog supported by the system is [10%,90%] of the disk capacity.
        :rtype: int
        """
        return self._OplogSize

    @OplogSize.setter
    def OplogSize(self, OplogSize):
        warnings.warn("parameter `OplogSize` is deprecated", DeprecationWarning) 

        self._OplogSize = OplogSize

    @property
    def NodeNum(self):
        r"""Number of Mongod nodes after instance changes (excluding read-only nodes).
- Number of replica set nodes. The value range of the number of nodes can be obtained through the response parameters MinNodeNum and MaxNodeNum of the [DescribeSpecInfo ](https://www.tencentcloud.comom/document/product/240/38567?from_cn_redirect=1) API.
- Number of nodes per shard in a sharded cluster. The value range of the number of nodes can be obtained through the response parameters MinReplicateSetNodeNum and MaxReplicateSetNodeNum of the [DescribeSpecInfo ](https://www.tencentcloud.comom/document/product/240/38567?from_cn_redirect=1) API.
**Note**: When the CPU and memory specifications of Mongod or Mongos nodes are changed, this parameter is not required, or enter the current number of Mongod or Mongos nodes (excluding read-only nodes).
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def ReplicateSetNum(self):
        r"""Number of shards after instance changes.
- The value range for the number of instance shards can be obtained through the response parameters **MinReplicateSetNum** and **MaxReplicateSetNum** of the [DescribeSpecInfo](https://www.tencentcloud.comom/document/product/240/38567?from_cn_redirect=1) API.
- The number of instance shards can only be increased and cannot be decreased.
        :rtype: int
        """
        return self._ReplicateSetNum

    @ReplicateSetNum.setter
    def ReplicateSetNum(self, ReplicateSetNum):
        self._ReplicateSetNum = ReplicateSetNum

    @property
    def InMaintenance(self):
        r"""Switch time for instance configuration modification.
 - 0: Execute the configuration modification task immediately after the adjustment is completed. Default value: 0.
 - 1: Execute the configuration modification task within the maintenance window.
**Note**: Adjusting the number of nodes and shards is unsupported <b>within the maintenance window</b>.
        :rtype: int
        """
        return self._InMaintenance

    @InMaintenance.setter
    def InMaintenance(self, InMaintenance):
        self._InMaintenance = InMaintenance

    @property
    def MongosMemory(self):
        r"""Memory size of the Mongos node after sharded cluster instance configuration changes, in GB. For the specifications supported by the instance, see [Product Specifications](https://www.tencentcloud.comom/document/product/240/64125?from_cn_redirect=1).
        :rtype: str
        """
        return self._MongosMemory

    @MongosMemory.setter
    def MongosMemory(self, MongosMemory):
        self._MongosMemory = MongosMemory

    @property
    def AddNodeList(self):
        r"""List of nodes to be added, containing the node type and AZ information.
        :rtype: list of AddNodeList
        """
        return self._AddNodeList

    @AddNodeList.setter
    def AddNodeList(self, AddNodeList):
        self._AddNodeList = AddNodeList

    @property
    def RemoveNodeList(self):
        r"""Deletes the node list.
**Note**: According to the consistency principle for nodes of each shard on a sharded cluster instance, specify the nodes on shard 0 for node deletion from the sharded cluster instance. For example, cmgo-9nl1czif_0-node-readonly0 will delete the first read-only node of each shard.
        :rtype: list of RemoveNodeList
        """
        return self._RemoveNodeList

    @RemoveNodeList.setter
    def RemoveNodeList(self, RemoveNodeList):
        self._RemoveNodeList = RemoveNodeList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._OplogSize = params.get("OplogSize")
        self._NodeNum = params.get("NodeNum")
        self._ReplicateSetNum = params.get("ReplicateSetNum")
        self._InMaintenance = params.get("InMaintenance")
        self._MongosMemory = params.get("MongosMemory")
        if params.get("AddNodeList") is not None:
            self._AddNodeList = []
            for item in params.get("AddNodeList"):
                obj = AddNodeList()
                obj._deserialize(item)
                self._AddNodeList.append(obj)
        if params.get("RemoveNodeList") is not None:
            self._RemoveNodeList = []
            for item in params.get("RemoveNodeList"):
                obj = RemoveNodeList()
                obj._deserialize(item)
                self._RemoveNodeList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSpecResponse(AbstractModel):
    r"""ModifyDBInstanceSpec response structure.

    """

    def __init__(self):
        r"""
        :param _DealId: Order ID.
        :type DealId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealId = None
        self._RequestId = None

    @property
    def DealId(self):
        r"""Order ID.
        :rtype: str
        """
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealId = params.get("DealId")
        self._RequestId = params.get("RequestId")


class ModifyInstanceParamsRequest(AbstractModel):
    r"""ModifyInstanceParams request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Specifies the instance ID. For example, cmgo-p8vn****. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.

        :type InstanceId: str
        :param _InstanceParams: Specifies the parameter name and value to be modified. For details about the currently supported parameter names and the corresponding valid values, see [DescribeInstanceParams](https://www.tencentcloud.comom/document/product/240/65903?from_cn_redirect=1).
        :type InstanceParams: list of ModifyMongoDBParamType
        :param _ModifyType: Operation type. Valid values:
- IMMEDIATELY: immediate adjustment.
- DELAY: delayed adjustment. It is an optional field. The default value is immediate adjustment if this parameter is left unspecified.
        :type ModifyType: str
        """
        self._InstanceId = None
        self._InstanceParams = None
        self._ModifyType = None

    @property
    def InstanceId(self):
        r"""Specifies the instance ID. For example, cmgo-p8vn****. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.

        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceParams(self):
        r"""Specifies the parameter name and value to be modified. For details about the currently supported parameter names and the corresponding valid values, see [DescribeInstanceParams](https://www.tencentcloud.comom/document/product/240/65903?from_cn_redirect=1).
        :rtype: list of ModifyMongoDBParamType
        """
        return self._InstanceParams

    @InstanceParams.setter
    def InstanceParams(self, InstanceParams):
        self._InstanceParams = InstanceParams

    @property
    def ModifyType(self):
        r"""Operation type. Valid values:
- IMMEDIATELY: immediate adjustment.
- DELAY: delayed adjustment. It is an optional field. The default value is immediate adjustment if this parameter is left unspecified.
        :rtype: str
        """
        return self._ModifyType

    @ModifyType.setter
    def ModifyType(self, ModifyType):
        self._ModifyType = ModifyType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("InstanceParams") is not None:
            self._InstanceParams = []
            for item in params.get("InstanceParams"):
                obj = ModifyMongoDBParamType()
                obj._deserialize(item)
                self._InstanceParams.append(obj)
        self._ModifyType = params.get("ModifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceParamsResponse(AbstractModel):
    r"""ModifyInstanceParams response structure.

    """

    def __init__(self):
        r"""
        :param _Changed: Whether the modification on the parameter configuration takes effect.
- true: the modified parameter value has taken effect.
- false: execution failed.

        :type Changed: bool
        :param _TaskId: This parameter is temporarily meaningless (to be compatible with the earlier versions, reserve this parameter at the frontend).
        :type TaskId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Changed = None
        self._TaskId = None
        self._RequestId = None

    @property
    def Changed(self):
        r"""Whether the modification on the parameter configuration takes effect.
- true: the modified parameter value has taken effect.
- false: execution failed.

        :rtype: bool
        """
        return self._Changed

    @Changed.setter
    def Changed(self, Changed):
        self._Changed = Changed

    @property
    def TaskId(self):
        r"""This parameter is temporarily meaningless (to be compatible with the earlier versions, reserve this parameter at the frontend).
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Changed = params.get("Changed")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyMongoDBParamType(AbstractModel):
    r"""Modifies the request parameters of a TencentDB for MongoDB instance.

    """

    def __init__(self):
        r"""
        :param _Key: Parameter name to be modified. Strictly refer to the parameter names supported by the current instance, which are obtained through DescribeInstanceParams.
        :type Key: str
        :param _Value: Corresponding value of the parameter name to be modified. Strictly refer to the value ranges corresponding to the parameters obtained through DescribeInstanceParams.
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""Parameter name to be modified. Strictly refer to the parameter names supported by the current instance, which are obtained through DescribeInstanceParams.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""Corresponding value of the parameter name to be modified. Strictly refer to the value ranges corresponding to the parameters obtained through DescribeInstanceParams.
        :rtype: str
        """
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
        


class ModifyNetworkAddress(AbstractModel):
    r"""Database IP to be modified

    """

    def __init__(self):
        r"""
        :param _NewIPAddress: New IP
        :type NewIPAddress: str
        :param _OldIpAddress: Old IP
        :type OldIpAddress: str
        """
        self._NewIPAddress = None
        self._OldIpAddress = None

    @property
    def NewIPAddress(self):
        r"""New IP
        :rtype: str
        """
        return self._NewIPAddress

    @NewIPAddress.setter
    def NewIPAddress(self, NewIPAddress):
        self._NewIPAddress = NewIPAddress

    @property
    def OldIpAddress(self):
        r"""Old IP
        :rtype: str
        """
        return self._OldIpAddress

    @OldIpAddress.setter
    def OldIpAddress(self, OldIpAddress):
        self._OldIpAddress = OldIpAddress


    def _deserialize(self, params):
        self._NewIPAddress = params.get("NewIPAddress")
        self._OldIpAddress = params.get("OldIpAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeProperty(AbstractModel):
    r"""Node attributes.

    """

    def __init__(self):
        r"""
        :param _Zone: Node AZ.
        :type Zone: str
        :param _NodeName: Node name.
        :type NodeName: str
        :param _Address: Node access address.
        :type Address: str
        :param _WanServiceAddress: Public network access address (IP address or domain name) of the node. The example value is an IP address.
        :type WanServiceAddress: str
        :param _Role: Node role.
- PRIMARY: primary node.
- SECONDARY: secondary node.
- READONLY: read-only node.
- ARBITER: arbitration node.
        :type Role: str
        :param _Hidden: Whether the node is a hidden node.
- true: a hidden node.
- false: not a hidden node.
        :type Hidden: bool
        :param _Status: Node status.
- NORMAL: running normally.
- STARTUP: starting.
- STARTUP2: starting and processing the intermediate data.
- RECOVERING: recovering and not available.
- DOWN: offline.
- UNKNOWN: unknown status.
- ROLLBACK: rolling back.
- REMOVED: removed.
        :type Status: str
        :param _SlaveDelay: Delay time of primary-secondary synchronization, in seconds.
        :type SlaveDelay: int
        :param _Priority: Node priority. Value range: [0, 100]. A larger value indicates a higher priority.
        :type Priority: int
        :param _Votes: Node voting right.
- 1: The node has the right to vote.
- 0: The node does not have the right to vote.
        :type Votes: int
        :param _Tags: Node tag.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of NodeTag
        :param _ReplicateSetId: Replica set ID.
        :type ReplicateSetId: str
        """
        self._Zone = None
        self._NodeName = None
        self._Address = None
        self._WanServiceAddress = None
        self._Role = None
        self._Hidden = None
        self._Status = None
        self._SlaveDelay = None
        self._Priority = None
        self._Votes = None
        self._Tags = None
        self._ReplicateSetId = None

    @property
    def Zone(self):
        r"""Node AZ.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def NodeName(self):
        r"""Node name.
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def Address(self):
        r"""Node access address.
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def WanServiceAddress(self):
        r"""Public network access address (IP address or domain name) of the node. The example value is an IP address.
        :rtype: str
        """
        return self._WanServiceAddress

    @WanServiceAddress.setter
    def WanServiceAddress(self, WanServiceAddress):
        self._WanServiceAddress = WanServiceAddress

    @property
    def Role(self):
        r"""Node role.
- PRIMARY: primary node.
- SECONDARY: secondary node.
- READONLY: read-only node.
- ARBITER: arbitration node.
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Hidden(self):
        r"""Whether the node is a hidden node.
- true: a hidden node.
- false: not a hidden node.
        :rtype: bool
        """
        return self._Hidden

    @Hidden.setter
    def Hidden(self, Hidden):
        self._Hidden = Hidden

    @property
    def Status(self):
        r"""Node status.
- NORMAL: running normally.
- STARTUP: starting.
- STARTUP2: starting and processing the intermediate data.
- RECOVERING: recovering and not available.
- DOWN: offline.
- UNKNOWN: unknown status.
- ROLLBACK: rolling back.
- REMOVED: removed.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SlaveDelay(self):
        r"""Delay time of primary-secondary synchronization, in seconds.
        :rtype: int
        """
        return self._SlaveDelay

    @SlaveDelay.setter
    def SlaveDelay(self, SlaveDelay):
        self._SlaveDelay = SlaveDelay

    @property
    def Priority(self):
        r"""Node priority. Value range: [0, 100]. A larger value indicates a higher priority.
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Votes(self):
        r"""Node voting right.
- 1: The node has the right to vote.
- 0: The node does not have the right to vote.
        :rtype: int
        """
        return self._Votes

    @Votes.setter
    def Votes(self, Votes):
        self._Votes = Votes

    @property
    def Tags(self):
        r"""Node tag.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of NodeTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ReplicateSetId(self):
        r"""Replica set ID.
        :rtype: str
        """
        return self._ReplicateSetId

    @ReplicateSetId.setter
    def ReplicateSetId(self, ReplicateSetId):
        self._ReplicateSetId = ReplicateSetId


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._NodeName = params.get("NodeName")
        self._Address = params.get("Address")
        self._WanServiceAddress = params.get("WanServiceAddress")
        self._Role = params.get("Role")
        self._Hidden = params.get("Hidden")
        self._Status = params.get("Status")
        self._SlaveDelay = params.get("SlaveDelay")
        self._Priority = params.get("Priority")
        self._Votes = params.get("Votes")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = NodeTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._ReplicateSetId = params.get("ReplicateSetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeTag(AbstractModel):
    r"""Node tag.

    """

    def __init__(self):
        r"""
        :param _TagKey: Node tag key.
        :type TagKey: str
        :param _TagValue: Node tag value.
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""Node tag key.
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""Node tag value.
        :rtype: str
        """
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
        


class OfflineIsolatedDBInstanceRequest(AbstractModel):
    r"""OfflineIsolatedDBInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. Log in to the [TencentDB for MongoDB console recycle bin](https://console.cloud.tencent.com/mongodb/recycle), and copy the ID of the instance to be eliminated from the instance list.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Instance ID. Log in to the [TencentDB for MongoDB console recycle bin](https://console.cloud.tencent.com/mongodb/recycle), and copy the ID of the instance to be eliminated from the instance list.
        :rtype: str
        """
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
        


class OfflineIsolatedDBInstanceResponse(AbstractModel):
    r"""OfflineIsolatedDBInstance response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Async task request ID, which can be used to query the execution result of an async task.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        r"""Async task request ID, which can be used to query the execution result of an async task.
        :rtype: str
        """
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class Operation(AbstractModel):
    r"""Operation to be terminated.

    """

    def __init__(self):
        r"""
        :param _ReplicaSetName: Name of the shard where the operation is performed. The [DescribeCurrentOp](https://www.tencentcloud.comom/document/product/240/48120?from_cn_redirect=1) API can be called to query the shard name.
        :type ReplicaSetName: str
        :param _NodeName: Name of the node where the operation is performed. The [DescribeCurrentOp](https://www.tencentcloud.comom/document/product/240/48120?from_cn_redirect=1) API can be called to query the node name.
        :type NodeName: str
        :param _OpId: Operation number. The [DescribeCurrentOp](https://www.tencentcloud.comom/document/product/240/48120?from_cn_redirect=1) API can be called to query the operation number.
        :type OpId: int
        """
        self._ReplicaSetName = None
        self._NodeName = None
        self._OpId = None

    @property
    def ReplicaSetName(self):
        r"""Name of the shard where the operation is performed. The [DescribeCurrentOp](https://www.tencentcloud.comom/document/product/240/48120?from_cn_redirect=1) API can be called to query the shard name.
        :rtype: str
        """
        return self._ReplicaSetName

    @ReplicaSetName.setter
    def ReplicaSetName(self, ReplicaSetName):
        self._ReplicaSetName = ReplicaSetName

    @property
    def NodeName(self):
        r"""Name of the node where the operation is performed. The [DescribeCurrentOp](https://www.tencentcloud.comom/document/product/240/48120?from_cn_redirect=1) API can be called to query the node name.
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def OpId(self):
        r"""Operation number. The [DescribeCurrentOp](https://www.tencentcloud.comom/document/product/240/48120?from_cn_redirect=1) API can be called to query the operation number.
        :rtype: int
        """
        return self._OpId

    @OpId.setter
    def OpId(self, OpId):
        self._OpId = OpId


    def _deserialize(self, params):
        self._ReplicaSetName = params.get("ReplicaSetName")
        self._NodeName = params.get("NodeName")
        self._OpId = params.get("OpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveNodeList(AbstractModel):
    r"""Node details of the instance to be modified.

    """

    def __init__(self):
        r"""
        :param _Role: Roles of nodes to be deleted.
 - SECONDARY: Mongod secondary node.
 - READONLY: read-only node.
 - MONGOS: Mongos node.
        :type Role: str
        :param _NodeName: IDs of nodes to be deleted. For a sharded cluster instance, specify the names of nodes to be deleted on one shard. Nodes with the same names on other shards will also be deleted.
- Obtaining method: Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), go to the **Node Management** tab, and obtain the **node ID**.
- Note: For a sharded cluster instance, specify the IDs of nodes on shard 0. For example, cmgo-6hfk\*\*\*\*\_0-node-primary.
        :type NodeName: str
        :param _Zone: AZ corresponding to the node. For the currently supported AZs, see [Regions and AZs](https://www.tencentcloud.comom/document/product/240/3637?from_cn_redirect=1).
- Single AZ: all nodes are in the same AZ.
- Multiple AZs: The current standard specification involves three AZs. The primary and secondary nodes are not in the same AZ. Note: AZs corresponding to the nodes to be deleted should be specified. After deletion, the number of nodes in any 2 AZs should be larger than that in the third AZ.
        :type Zone: str
        """
        self._Role = None
        self._NodeName = None
        self._Zone = None

    @property
    def Role(self):
        r"""Roles of nodes to be deleted.
 - SECONDARY: Mongod secondary node.
 - READONLY: read-only node.
 - MONGOS: Mongos node.
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def NodeName(self):
        r"""IDs of nodes to be deleted. For a sharded cluster instance, specify the names of nodes to be deleted on one shard. Nodes with the same names on other shards will also be deleted.
- Obtaining method: Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), go to the **Node Management** tab, and obtain the **node ID**.
- Note: For a sharded cluster instance, specify the IDs of nodes on shard 0. For example, cmgo-6hfk\*\*\*\*\_0-node-primary.
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def Zone(self):
        r"""AZ corresponding to the node. For the currently supported AZs, see [Regions and AZs](https://www.tencentcloud.comom/document/product/240/3637?from_cn_redirect=1).
- Single AZ: all nodes are in the same AZ.
- Multiple AZs: The current standard specification involves three AZs. The primary and secondary nodes are not in the same AZ. Note: AZs corresponding to the nodes to be deleted should be specified. After deletion, the number of nodes in any 2 AZs should be larger than that in the third AZ.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._NodeName = params.get("NodeName")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenameInstanceRequest(AbstractModel):
    r"""RenameInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID. Format: cmgo-p8vnipr5. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/MongoDB#/) and copy the instance ID from the instance list.
        :type InstanceId: str
        :param _NewName: Custom instance name. It can contain any character, with a length from 1 to 128 characters.
        :type NewName: str
        """
        self._InstanceId = None
        self._NewName = None

    @property
    def InstanceId(self):
        r"""Instance ID. Format: cmgo-p8vnipr5. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/MongoDB#/) and copy the instance ID from the instance list.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NewName(self):
        r"""Custom instance name. It can contain any character, with a length from 1 to 128 characters.
        :rtype: str
        """
        return self._NewName

    @NewName.setter
    def NewName(self, NewName):
        self._NewName = NewName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NewName = params.get("NewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenameInstanceResponse(AbstractModel):
    r"""RenameInstance response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RenewDBInstancesRequest(AbstractModel):
    r"""RenewDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Specifies the ID or IDs of one or multiple instances to be renewed.
- It can be obtained through the response parameter **InstanceId** of the [DescribeDBInstances](https://www.tencentcloud.comom/document/product/240/38568?from_cn_redirect=1) API.
- The maximum number of instances for each renewal request is 100.
        :type InstanceIds: list of str
        :param _InstanceChargePrepaid: The parameter setting for the prepaid mode (monthly subscription mode). This parameter can specify the renewal period, whether to set automatic renewal, and other attributes of the monthly subscription instance. This parameter is mandatory in monthly subscription.
        :type InstanceChargePrepaid: :class:`tencentcloud.mongodb.v20190725.models.InstanceChargePrepaid`
        """
        self._InstanceIds = None
        self._InstanceChargePrepaid = None

    @property
    def InstanceIds(self):
        r"""Specifies the ID or IDs of one or multiple instances to be renewed.
- It can be obtained through the response parameter **InstanceId** of the [DescribeDBInstances](https://www.tencentcloud.comom/document/product/240/38568?from_cn_redirect=1) API.
- The maximum number of instances for each renewal request is 100.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceChargePrepaid(self):
        r"""The parameter setting for the prepaid mode (monthly subscription mode). This parameter can specify the renewal period, whether to set automatic renewal, and other attributes of the monthly subscription instance. This parameter is mandatory in monthly subscription.
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.InstanceChargePrepaid`
        """
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDBInstancesResponse(AbstractModel):
    r"""RenewDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ReplicaSetInfo(AbstractModel):
    r"""Shard information.

    """

    def __init__(self):
        r"""
        :param _ReplicaSetId: Replica set ID.
        :type ReplicaSetId: str
        """
        self._ReplicaSetId = None

    @property
    def ReplicaSetId(self):
        r"""Replica set ID.
        :rtype: str
        """
        return self._ReplicaSetId

    @ReplicaSetId.setter
    def ReplicaSetId(self, ReplicaSetId):
        self._ReplicaSetId = ReplicaSetId


    def _deserialize(self, params):
        self._ReplicaSetId = params.get("ReplicaSetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplicateSetInfo(AbstractModel):
    r"""Replica set information.

    """

    def __init__(self):
        r"""
        :param _Nodes: Node attributes.
        :type Nodes: list of NodeProperty
        """
        self._Nodes = None

    @property
    def Nodes(self):
        r"""Node attributes.
        :rtype: list of NodeProperty
        """
        return self._Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self._Nodes = Nodes


    def _deserialize(self, params):
        if params.get("Nodes") is not None:
            self._Nodes = []
            for item in params.get("Nodes"):
                obj = NodeProperty()
                obj._deserialize(item)
                self._Nodes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetDBInstancePasswordRequest(AbstractModel):
    r"""ResetDBInstancePassword request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Specifies the instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :type InstanceId: str
        :param _UserName: Specifies the account name for which the password needs to be changed. The [DescribeAccountUsers](https://www.tencentcloud.comom/document/product/240/80800?from_cn_redirect=1) API can be called to obtain the account list and copy the account name for which the password needs to be changed.
        :type UserName: str
        :param _Password: Specifies a new password for the account. Password complexity requirements:
- It should contain 8–32 characters.
- It should contain at least two types of the following: letters, digits, and special characters (!@#%^\*()\_).
        :type Password: str
        """
        self._InstanceId = None
        self._UserName = None
        self._Password = None

    @property
    def InstanceId(self):
        r"""Specifies the instance ID. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        r"""Specifies the account name for which the password needs to be changed. The [DescribeAccountUsers](https://www.tencentcloud.comom/document/product/240/80800?from_cn_redirect=1) API can be called to obtain the account list and copy the account name for which the password needs to be changed.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        r"""Specifies a new password for the account. Password complexity requirements:
- It should contain 8–32 characters.
- It should contain at least two types of the following: letters, digits, and special characters (!@#%^\*()\_).
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetDBInstancePasswordResponse(AbstractModel):
    r"""ResetDBInstancePassword response structure.

    """

    def __init__(self):
        r"""
        :param _AsyncRequestId: Task request ID.
        :type AsyncRequestId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AsyncRequestId = None
        self._RequestId = None

    @property
    def AsyncRequestId(self):
        r"""Task request ID.
        :rtype: str
        """
        return self._AsyncRequestId

    @AsyncRequestId.setter
    def AsyncRequestId(self, AsyncRequestId):
        self._AsyncRequestId = AsyncRequestId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AsyncRequestId = params.get("AsyncRequestId")
        self._RequestId = params.get("RequestId")


class SecurityGroup(AbstractModel):
    r"""Security group information

    """

    def __init__(self):
        r"""
        :param _ProjectId: Associated project ID.
        :type ProjectId: int
        :param _CreateTime: Security group creation time.
        :type CreateTime: str
        :param _Inbound: Security group inbound rule.
        :type Inbound: list of SecurityGroupBound
        :param _Outbound: Security group outbound rule.
        :type Outbound: list of SecurityGroupBound
        :param _SecurityGroupId: Security group ID.
        :type SecurityGroupId: str
        :param _SecurityGroupName: Security group name.
        :type SecurityGroupName: str
        :param _SecurityGroupRemark: Security group remarks.
        :type SecurityGroupRemark: str
        """
        self._ProjectId = None
        self._CreateTime = None
        self._Inbound = None
        self._Outbound = None
        self._SecurityGroupId = None
        self._SecurityGroupName = None
        self._SecurityGroupRemark = None

    @property
    def ProjectId(self):
        r"""Associated project ID.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CreateTime(self):
        r"""Security group creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Inbound(self):
        r"""Security group inbound rule.
        :rtype: list of SecurityGroupBound
        """
        return self._Inbound

    @Inbound.setter
    def Inbound(self, Inbound):
        self._Inbound = Inbound

    @property
    def Outbound(self):
        r"""Security group outbound rule.
        :rtype: list of SecurityGroupBound
        """
        return self._Outbound

    @Outbound.setter
    def Outbound(self, Outbound):
        self._Outbound = Outbound

    @property
    def SecurityGroupId(self):
        r"""Security group ID.
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupName(self):
        r"""Security group name.
        :rtype: str
        """
        return self._SecurityGroupName

    @SecurityGroupName.setter
    def SecurityGroupName(self, SecurityGroupName):
        self._SecurityGroupName = SecurityGroupName

    @property
    def SecurityGroupRemark(self):
        r"""Security group remarks.
        :rtype: str
        """
        return self._SecurityGroupRemark

    @SecurityGroupRemark.setter
    def SecurityGroupRemark(self, SecurityGroupRemark):
        self._SecurityGroupRemark = SecurityGroupRemark


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CreateTime = params.get("CreateTime")
        if params.get("Inbound") is not None:
            self._Inbound = []
            for item in params.get("Inbound"):
                obj = SecurityGroupBound()
                obj._deserialize(item)
                self._Inbound.append(obj)
        if params.get("Outbound") is not None:
            self._Outbound = []
            for item in params.get("Outbound"):
                obj = SecurityGroupBound()
                obj._deserialize(item)
                self._Outbound.append(obj)
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._SecurityGroupName = params.get("SecurityGroupName")
        self._SecurityGroupRemark = params.get("SecurityGroupRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupBound(AbstractModel):
    r"""Security group rule

    """

    def __init__(self):
        r"""
        :param _Action: Execution policy.
- ACCEPT: allow. Access requests for the port can be released.
- DROP: reject. Data packets are discarded without any response.
        :type Action: str
        :param _CidrIp: Inbound IP address or IP range for database access.
        :type CidrIp: str
        :param _PortRange: Port for database access.
        :type PortRange: str
        :param _IpProtocol: Transport layer protocol: TCP.
        :type IpProtocol: str
        :param _Id: Security group ID.
        :type Id: str
        :param _AddressModule: Parameter template ID for the IP address or IP address group. Log in to the [parameter template console](https://console.cloud.tencent.com/vpc/template/ip) to obtain the parameter template IP address details.
        :type AddressModule: str
        :param _ServiceModule: Parameter template ID for the protocol port or protocol port group. Log in to the [parameter template console](https://console.cloud.tencent.com/vpc/template/protoport) to obtain the parameter template protocol port details.
        :type ServiceModule: str
        :param _Desc: Security group description information.
        :type Desc: str
        """
        self._Action = None
        self._CidrIp = None
        self._PortRange = None
        self._IpProtocol = None
        self._Id = None
        self._AddressModule = None
        self._ServiceModule = None
        self._Desc = None

    @property
    def Action(self):
        r"""Execution policy.
- ACCEPT: allow. Access requests for the port can be released.
- DROP: reject. Data packets are discarded without any response.
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def CidrIp(self):
        r"""Inbound IP address or IP range for database access.
        :rtype: str
        """
        return self._CidrIp

    @CidrIp.setter
    def CidrIp(self, CidrIp):
        self._CidrIp = CidrIp

    @property
    def PortRange(self):
        r"""Port for database access.
        :rtype: str
        """
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def IpProtocol(self):
        r"""Transport layer protocol: TCP.
        :rtype: str
        """
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def Id(self):
        r"""Security group ID.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AddressModule(self):
        r"""Parameter template ID for the IP address or IP address group. Log in to the [parameter template console](https://console.cloud.tencent.com/vpc/template/ip) to obtain the parameter template IP address details.
        :rtype: str
        """
        return self._AddressModule

    @AddressModule.setter
    def AddressModule(self, AddressModule):
        self._AddressModule = AddressModule

    @property
    def ServiceModule(self):
        r"""Parameter template ID for the protocol port or protocol port group. Log in to the [parameter template console](https://console.cloud.tencent.com/vpc/template/protoport) to obtain the parameter template protocol port details.
        :rtype: str
        """
        return self._ServiceModule

    @ServiceModule.setter
    def ServiceModule(self, ServiceModule):
        self._ServiceModule = ServiceModule

    @property
    def Desc(self):
        r"""Security group description information.
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._CidrIp = params.get("CidrIp")
        self._PortRange = params.get("PortRange")
        self._IpProtocol = params.get("IpProtocol")
        self._Id = params.get("Id")
        self._AddressModule = params.get("AddressModule")
        self._ServiceModule = params.get("ServiceModule")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAccountUserPrivilegeRequest(AbstractModel):
    r"""SetAccountUserPrivilege request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Specifies the instance ID for the account to be configured. For example, cmgo-p8vn****. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/MongoDB), and copy the instance ID from the instance list.
        :type InstanceId: str
        :param _UserName: Sets the account name to access the instance. The setting requirements are as follows: The name should be started with a letter and its length should be 1–64 characters. Only uppercase letters, lowercase letters, digits (1–9), underscores (_), and hyphens (-) can be entered.
        :type UserName: str
        :param _AuthRole: Sets the permission information.
        :type AuthRole: list of Auth
        """
        self._InstanceId = None
        self._UserName = None
        self._AuthRole = None

    @property
    def InstanceId(self):
        r"""Specifies the instance ID for the account to be configured. For example, cmgo-p8vn****. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/MongoDB), and copy the instance ID from the instance list.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        r"""Sets the account name to access the instance. The setting requirements are as follows: The name should be started with a letter and its length should be 1–64 characters. Only uppercase letters, lowercase letters, digits (1–9), underscores (_), and hyphens (-) can be entered.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def AuthRole(self):
        r"""Sets the permission information.
        :rtype: list of Auth
        """
        return self._AuthRole

    @AuthRole.setter
    def AuthRole(self, AuthRole):
        self._AuthRole = AuthRole


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        if params.get("AuthRole") is not None:
            self._AuthRole = []
            for item in params.get("AuthRole"):
                obj = Auth()
                obj._deserialize(item)
                self._AuthRole.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAccountUserPrivilegeResponse(AbstractModel):
    r"""SetAccountUserPrivilege response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Task ID.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Task ID.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class SetDBInstanceDeletionProtectionRequest(AbstractModel):
    r"""SetDBInstanceDeletionProtection request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Instance ID list, in the format of cmgo-p8vnipr5. It is the same as the format of the instance ID displayed on the TencentDB for MongoDB console page.
        :type InstanceIds: list of str
        :param _EnableDeletionProtection: Instance termination protection switch. Valid values: 0 - disabled; 1 - enabled.
        :type EnableDeletionProtection: int
        """
        self._InstanceIds = None
        self._EnableDeletionProtection = None

    @property
    def InstanceIds(self):
        r"""Instance ID list, in the format of cmgo-p8vnipr5. It is the same as the format of the instance ID displayed on the TencentDB for MongoDB console page.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def EnableDeletionProtection(self):
        r"""Instance termination protection switch. Valid values: 0 - disabled; 1 - enabled.
        :rtype: int
        """
        return self._EnableDeletionProtection

    @EnableDeletionProtection.setter
    def EnableDeletionProtection(self, EnableDeletionProtection):
        self._EnableDeletionProtection = EnableDeletionProtection


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._EnableDeletionProtection = params.get("EnableDeletionProtection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetDBInstanceDeletionProtectionResponse(AbstractModel):
    r"""SetDBInstanceDeletionProtection response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SetInstanceMaintenanceRequest(AbstractModel):
    r"""SetInstanceMaintenance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Specifies the instance ID. For example, cmgo-p8vn****. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.

        :type InstanceId: str
        :param _MaintenanceStart: Start time of the maintenance window. The value range is any hour or half-hour between 00:00 and 23:00, such as 00:00 or 00:30.
        :type MaintenanceStart: str
        :param _MaintenanceEnd: End time of the maintenance window.
- The value range is any hour or half-hour between 00:00 and 23:00. The minimum value of maintenance time is 30 minutes, and the maximum value is 3 hours.
- The end time should be later than the start time.
        :type MaintenanceEnd: str
        """
        self._InstanceId = None
        self._MaintenanceStart = None
        self._MaintenanceEnd = None

    @property
    def InstanceId(self):
        r"""Specifies the instance ID. For example, cmgo-p8vn****. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.

        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MaintenanceStart(self):
        r"""Start time of the maintenance window. The value range is any hour or half-hour between 00:00 and 23:00, such as 00:00 or 00:30.
        :rtype: str
        """
        return self._MaintenanceStart

    @MaintenanceStart.setter
    def MaintenanceStart(self, MaintenanceStart):
        self._MaintenanceStart = MaintenanceStart

    @property
    def MaintenanceEnd(self):
        r"""End time of the maintenance window.
- The value range is any hour or half-hour between 00:00 and 23:00. The minimum value of maintenance time is 30 minutes, and the maximum value is 3 hours.
- The end time should be later than the start time.
        :rtype: str
        """
        return self._MaintenanceEnd

    @MaintenanceEnd.setter
    def MaintenanceEnd(self, MaintenanceEnd):
        self._MaintenanceEnd = MaintenanceEnd


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._MaintenanceStart = params.get("MaintenanceStart")
        self._MaintenanceEnd = params.get("MaintenanceEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetInstanceMaintenanceResponse(AbstractModel):
    r"""SetInstanceMaintenance response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ShardInfo(AbstractModel):
    r"""Details of an instance shard

    """

    def __init__(self):
        r"""
        :param _UsedVolume: Used shard capacity
        :type UsedVolume: float
        :param _ReplicaSetId: Shard ID
        :type ReplicaSetId: str
        :param _ReplicaSetName: Shard name
        :type ReplicaSetName: str
        :param _Memory: Shard memory size in MB
        :type Memory: int
        :param _Volume: Shard disk size in MB
        :type Volume: int
        :param _OplogSize: Shard oplog size in MB
        :type OplogSize: int
        :param _SecondaryNum: Number of secondary nodes of a shard
        :type SecondaryNum: int
        :param _RealReplicaSetId: Shard physical ID
        :type RealReplicaSetId: str
        """
        self._UsedVolume = None
        self._ReplicaSetId = None
        self._ReplicaSetName = None
        self._Memory = None
        self._Volume = None
        self._OplogSize = None
        self._SecondaryNum = None
        self._RealReplicaSetId = None

    @property
    def UsedVolume(self):
        r"""Used shard capacity
        :rtype: float
        """
        return self._UsedVolume

    @UsedVolume.setter
    def UsedVolume(self, UsedVolume):
        self._UsedVolume = UsedVolume

    @property
    def ReplicaSetId(self):
        r"""Shard ID
        :rtype: str
        """
        return self._ReplicaSetId

    @ReplicaSetId.setter
    def ReplicaSetId(self, ReplicaSetId):
        self._ReplicaSetId = ReplicaSetId

    @property
    def ReplicaSetName(self):
        r"""Shard name
        :rtype: str
        """
        return self._ReplicaSetName

    @ReplicaSetName.setter
    def ReplicaSetName(self, ReplicaSetName):
        self._ReplicaSetName = ReplicaSetName

    @property
    def Memory(self):
        r"""Shard memory size in MB
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Volume(self):
        r"""Shard disk size in MB
        :rtype: int
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def OplogSize(self):
        r"""Shard oplog size in MB
        :rtype: int
        """
        return self._OplogSize

    @OplogSize.setter
    def OplogSize(self, OplogSize):
        self._OplogSize = OplogSize

    @property
    def SecondaryNum(self):
        r"""Number of secondary nodes of a shard
        :rtype: int
        """
        return self._SecondaryNum

    @SecondaryNum.setter
    def SecondaryNum(self, SecondaryNum):
        self._SecondaryNum = SecondaryNum

    @property
    def RealReplicaSetId(self):
        r"""Shard physical ID
        :rtype: str
        """
        return self._RealReplicaSetId

    @RealReplicaSetId.setter
    def RealReplicaSetId(self, RealReplicaSetId):
        self._RealReplicaSetId = RealReplicaSetId


    def _deserialize(self, params):
        self._UsedVolume = params.get("UsedVolume")
        self._ReplicaSetId = params.get("ReplicaSetId")
        self._ReplicaSetName = params.get("ReplicaSetName")
        self._Memory = params.get("Memory")
        self._Volume = params.get("Volume")
        self._OplogSize = params.get("OplogSize")
        self._SecondaryNum = params.get("SecondaryNum")
        self._RealReplicaSetId = params.get("RealReplicaSetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogItem(AbstractModel):
    r"""Slow log details.

    """

    def __init__(self):
        r"""
        :param _Log: Slow log details.
        :type Log: str
        :param _NodeName: Node name.
        :type NodeName: str
        :param _QueryHash: Queries the hash value.
        :type QueryHash: str
        """
        self._Log = None
        self._NodeName = None
        self._QueryHash = None

    @property
    def Log(self):
        r"""Slow log details.
        :rtype: str
        """
        return self._Log

    @Log.setter
    def Log(self, Log):
        self._Log = Log

    @property
    def NodeName(self):
        r"""Node name.
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def QueryHash(self):
        r"""Queries the hash value.
        :rtype: str
        """
        return self._QueryHash

    @QueryHash.setter
    def QueryHash(self, QueryHash):
        self._QueryHash = QueryHash


    def _deserialize(self, params):
        self._Log = params.get("Log")
        self._NodeName = params.get("NodeName")
        self._QueryHash = params.get("QueryHash")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogPattern(AbstractModel):
    r"""Slow log statistics of MongoDB database

    """

    def __init__(self):
        r"""
        :param _Pattern: Slow log output format: database name.table name.command.
        :type Pattern: str
        :param _QueryHash: queryHash value carried during slow log recording. It can be used to identify a query type.
        :type QueryHash: str
        :param _MaxTime: Maximum execution time, in milliseconds.
        :type MaxTime: int
        :param _AverageTime: Average execution time, in milliseconds.
        :type AverageTime: int
        :param _Total: Number of slow logs.
        :type Total: int
        """
        self._Pattern = None
        self._QueryHash = None
        self._MaxTime = None
        self._AverageTime = None
        self._Total = None

    @property
    def Pattern(self):
        r"""Slow log output format: database name.table name.command.
        :rtype: str
        """
        return self._Pattern

    @Pattern.setter
    def Pattern(self, Pattern):
        self._Pattern = Pattern

    @property
    def QueryHash(self):
        r"""queryHash value carried during slow log recording. It can be used to identify a query type.
        :rtype: str
        """
        return self._QueryHash

    @QueryHash.setter
    def QueryHash(self, QueryHash):
        self._QueryHash = QueryHash

    @property
    def MaxTime(self):
        r"""Maximum execution time, in milliseconds.
        :rtype: int
        """
        return self._MaxTime

    @MaxTime.setter
    def MaxTime(self, MaxTime):
        self._MaxTime = MaxTime

    @property
    def AverageTime(self):
        r"""Average execution time, in milliseconds.
        :rtype: int
        """
        return self._AverageTime

    @AverageTime.setter
    def AverageTime(self, AverageTime):
        self._AverageTime = AverageTime

    @property
    def Total(self):
        r"""Number of slow logs.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._Pattern = params.get("Pattern")
        self._QueryHash = params.get("QueryHash")
        self._MaxTime = params.get("MaxTime")
        self._AverageTime = params.get("AverageTime")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecItem(AbstractModel):
    r"""TencentDB for MongoDB instance sales specification.

    """

    def __init__(self):
        r"""
        :param _SpecCode: Specification information identifier. Format: mongo.HIO10G.128G. It consists of three parts: node type, specification type, and memory specification.
- Node type: **mongo** indicates a Mongod node; **mongos** indicates a Mongos node; **cfgstr** indicates a ConfigServer node.
- Specification type: **HIO10G** indicates the general HIO 10GE type; **HCD** indicates the Cloud Disk Edition type.
- Memory specification, in GB. Valid values: 4, 8, 16, 32, 64, 128, 240, and 512. 128g indicates 128 GB.
        :type SpecCode: str
        :param _Status: Saleable specification status flag. Valid values are as follows:
 - 0: selling stopped.
 - 1: available for sale.
        :type Status: int
        :param _Cpu: Computing resource specification, indicating the number of CPU cores.
        :type Cpu: int
        :param _Memory: Memory specification. Unit: MB.
        :type Memory: int
        :param _DefaultStorage: Default disk specification. Unit: MB.
        :type DefaultStorage: int
        :param _MaxStorage: Maximum disk specification. Unit: MB.
        :type MaxStorage: int
        :param _MinStorage: Minimum disk specification. Unit: MB.
        :type MinStorage: int
        :param _Qps: Maximum number of requests per second. Unit: requests/second.
        :type Qps: int
        :param _Conns: Maximum number of connections supported for the specification.
        :type Conns: int
        :param _MongoVersionCode: Storage engine version information on instances.
- MONGO_40_WT: version of the MongoDB 4.0 WiredTiger storage engine.
- MONGO_42_WT: version of the MongoDB 4.2 WiredTiger storage engine.
- MONGO_44_WT: version of the MongoDB 4.4 WiredTiger storage engine.
- MONGO_50_WT: version of the MongoDB 5.0 WiredTiger storage engine.
- MONGO_60_WT: version of the MongoDB 6.0 WiredTiger storage engine.
- MONGO_70_WT: version of the MongoDB 7.0 WiredTiger storage engine.
        :type MongoVersionCode: str
        :param _MongoVersionValue: Digital version corresponding to the instance version.
        :type MongoVersionValue: int
        :param _Version: Instance version information. Valid values: 4.2, 4.4, 5.0, 6.0, and 7.0.
        :type Version: str
        :param _EngineName: Storage engine.
        :type EngineName: str
        :param _ClusterType: Cluster type. Valid values are as follows:
 - 1: sharded cluster.
 - 0: replica set cluster.
        :type ClusterType: int
        :param _MinNodeNum: Minimum number of nodes for each replica set.
        :type MinNodeNum: int
        :param _MaxNodeNum: Maximum number of nodes for each replica set.
        :type MaxNodeNum: int
        :param _MinReplicateSetNum: Minimum number of shards.
        :type MinReplicateSetNum: int
        :param _MaxReplicateSetNum: Maximum number of shards.
        :type MaxReplicateSetNum: int
        :param _MinReplicateSetNodeNum: Minimum number of nodes for each shard.
        :type MinReplicateSetNodeNum: int
        :param _MaxReplicateSetNodeNum: Maximum number of nodes for each shard.
        :type MaxReplicateSetNodeNum: int
        :param _MachineType: Cluster specification type. Valid values are as follows:
 - HIO10G: general high-I/O 10GE type.
 - HCD: cloud disk type.
        :type MachineType: str
        """
        self._SpecCode = None
        self._Status = None
        self._Cpu = None
        self._Memory = None
        self._DefaultStorage = None
        self._MaxStorage = None
        self._MinStorage = None
        self._Qps = None
        self._Conns = None
        self._MongoVersionCode = None
        self._MongoVersionValue = None
        self._Version = None
        self._EngineName = None
        self._ClusterType = None
        self._MinNodeNum = None
        self._MaxNodeNum = None
        self._MinReplicateSetNum = None
        self._MaxReplicateSetNum = None
        self._MinReplicateSetNodeNum = None
        self._MaxReplicateSetNodeNum = None
        self._MachineType = None

    @property
    def SpecCode(self):
        r"""Specification information identifier. Format: mongo.HIO10G.128G. It consists of three parts: node type, specification type, and memory specification.
- Node type: **mongo** indicates a Mongod node; **mongos** indicates a Mongos node; **cfgstr** indicates a ConfigServer node.
- Specification type: **HIO10G** indicates the general HIO 10GE type; **HCD** indicates the Cloud Disk Edition type.
- Memory specification, in GB. Valid values: 4, 8, 16, 32, 64, 128, 240, and 512. 128g indicates 128 GB.
        :rtype: str
        """
        return self._SpecCode

    @SpecCode.setter
    def SpecCode(self, SpecCode):
        self._SpecCode = SpecCode

    @property
    def Status(self):
        r"""Saleable specification status flag. Valid values are as follows:
 - 0: selling stopped.
 - 1: available for sale.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Cpu(self):
        r"""Computing resource specification, indicating the number of CPU cores.
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        r"""Memory specification. Unit: MB.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def DefaultStorage(self):
        r"""Default disk specification. Unit: MB.
        :rtype: int
        """
        return self._DefaultStorage

    @DefaultStorage.setter
    def DefaultStorage(self, DefaultStorage):
        self._DefaultStorage = DefaultStorage

    @property
    def MaxStorage(self):
        r"""Maximum disk specification. Unit: MB.
        :rtype: int
        """
        return self._MaxStorage

    @MaxStorage.setter
    def MaxStorage(self, MaxStorage):
        self._MaxStorage = MaxStorage

    @property
    def MinStorage(self):
        r"""Minimum disk specification. Unit: MB.
        :rtype: int
        """
        return self._MinStorage

    @MinStorage.setter
    def MinStorage(self, MinStorage):
        self._MinStorage = MinStorage

    @property
    def Qps(self):
        r"""Maximum number of requests per second. Unit: requests/second.
        :rtype: int
        """
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def Conns(self):
        r"""Maximum number of connections supported for the specification.
        :rtype: int
        """
        return self._Conns

    @Conns.setter
    def Conns(self, Conns):
        self._Conns = Conns

    @property
    def MongoVersionCode(self):
        r"""Storage engine version information on instances.
- MONGO_40_WT: version of the MongoDB 4.0 WiredTiger storage engine.
- MONGO_42_WT: version of the MongoDB 4.2 WiredTiger storage engine.
- MONGO_44_WT: version of the MongoDB 4.4 WiredTiger storage engine.
- MONGO_50_WT: version of the MongoDB 5.0 WiredTiger storage engine.
- MONGO_60_WT: version of the MongoDB 6.0 WiredTiger storage engine.
- MONGO_70_WT: version of the MongoDB 7.0 WiredTiger storage engine.
        :rtype: str
        """
        return self._MongoVersionCode

    @MongoVersionCode.setter
    def MongoVersionCode(self, MongoVersionCode):
        self._MongoVersionCode = MongoVersionCode

    @property
    def MongoVersionValue(self):
        r"""Digital version corresponding to the instance version.
        :rtype: int
        """
        return self._MongoVersionValue

    @MongoVersionValue.setter
    def MongoVersionValue(self, MongoVersionValue):
        self._MongoVersionValue = MongoVersionValue

    @property
    def Version(self):
        r"""Instance version information. Valid values: 4.2, 4.4, 5.0, 6.0, and 7.0.
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def EngineName(self):
        r"""Storage engine.
        :rtype: str
        """
        return self._EngineName

    @EngineName.setter
    def EngineName(self, EngineName):
        self._EngineName = EngineName

    @property
    def ClusterType(self):
        r"""Cluster type. Valid values are as follows:
 - 1: sharded cluster.
 - 0: replica set cluster.
        :rtype: int
        """
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def MinNodeNum(self):
        r"""Minimum number of nodes for each replica set.
        :rtype: int
        """
        return self._MinNodeNum

    @MinNodeNum.setter
    def MinNodeNum(self, MinNodeNum):
        self._MinNodeNum = MinNodeNum

    @property
    def MaxNodeNum(self):
        r"""Maximum number of nodes for each replica set.
        :rtype: int
        """
        return self._MaxNodeNum

    @MaxNodeNum.setter
    def MaxNodeNum(self, MaxNodeNum):
        self._MaxNodeNum = MaxNodeNum

    @property
    def MinReplicateSetNum(self):
        r"""Minimum number of shards.
        :rtype: int
        """
        return self._MinReplicateSetNum

    @MinReplicateSetNum.setter
    def MinReplicateSetNum(self, MinReplicateSetNum):
        self._MinReplicateSetNum = MinReplicateSetNum

    @property
    def MaxReplicateSetNum(self):
        r"""Maximum number of shards.
        :rtype: int
        """
        return self._MaxReplicateSetNum

    @MaxReplicateSetNum.setter
    def MaxReplicateSetNum(self, MaxReplicateSetNum):
        self._MaxReplicateSetNum = MaxReplicateSetNum

    @property
    def MinReplicateSetNodeNum(self):
        r"""Minimum number of nodes for each shard.
        :rtype: int
        """
        return self._MinReplicateSetNodeNum

    @MinReplicateSetNodeNum.setter
    def MinReplicateSetNodeNum(self, MinReplicateSetNodeNum):
        self._MinReplicateSetNodeNum = MinReplicateSetNodeNum

    @property
    def MaxReplicateSetNodeNum(self):
        r"""Maximum number of nodes for each shard.
        :rtype: int
        """
        return self._MaxReplicateSetNodeNum

    @MaxReplicateSetNodeNum.setter
    def MaxReplicateSetNodeNum(self, MaxReplicateSetNodeNum):
        self._MaxReplicateSetNodeNum = MaxReplicateSetNodeNum

    @property
    def MachineType(self):
        r"""Cluster specification type. Valid values are as follows:
 - HIO10G: general high-I/O 10GE type.
 - HCD: cloud disk type.
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType


    def _deserialize(self, params):
        self._SpecCode = params.get("SpecCode")
        self._Status = params.get("Status")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._DefaultStorage = params.get("DefaultStorage")
        self._MaxStorage = params.get("MaxStorage")
        self._MinStorage = params.get("MinStorage")
        self._Qps = params.get("Qps")
        self._Conns = params.get("Conns")
        self._MongoVersionCode = params.get("MongoVersionCode")
        self._MongoVersionValue = params.get("MongoVersionValue")
        self._Version = params.get("Version")
        self._EngineName = params.get("EngineName")
        self._ClusterType = params.get("ClusterType")
        self._MinNodeNum = params.get("MinNodeNum")
        self._MaxNodeNum = params.get("MaxNodeNum")
        self._MinReplicateSetNum = params.get("MinReplicateSetNum")
        self._MaxReplicateSetNum = params.get("MaxReplicateSetNum")
        self._MinReplicateSetNodeNum = params.get("MinReplicateSetNodeNum")
        self._MaxReplicateSetNodeNum = params.get("MaxReplicateSetNodeNum")
        self._MachineType = params.get("MachineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecificationInfo(AbstractModel):
    r"""Instance specification information.

    """

    def __init__(self):
        r"""
        :param _Region: Region information.
        :type Region: str
        :param _Zone: AZ information.
        :type Zone: str
        :param _SpecItems: Sales specification information.
        :type SpecItems: list of SpecItem
        :param _SupportMultiAZ: Whether cross-AZ deployment is supported.
- 1: supported.
- 0: not supported.
        :type SupportMultiAZ: int
        """
        self._Region = None
        self._Zone = None
        self._SpecItems = None
        self._SupportMultiAZ = None

    @property
    def Region(self):
        r"""Region information.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        r"""AZ information.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SpecItems(self):
        r"""Sales specification information.
        :rtype: list of SpecItem
        """
        return self._SpecItems

    @SpecItems.setter
    def SpecItems(self, SpecItems):
        self._SpecItems = SpecItems

    @property
    def SupportMultiAZ(self):
        r"""Whether cross-AZ deployment is supported.
- 1: supported.
- 0: not supported.
        :rtype: int
        """
        return self._SupportMultiAZ

    @SupportMultiAZ.setter
    def SupportMultiAZ(self, SupportMultiAZ):
        self._SupportMultiAZ = SupportMultiAZ


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        if params.get("SpecItems") is not None:
            self._SpecItems = []
            for item in params.get("SpecItems"):
                obj = SpecItem()
                obj._deserialize(item)
                self._SpecItems.append(obj)
        self._SupportMultiAZ = params.get("SupportMultiAZ")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    r"""Instance tag information

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
        r"""Tag key
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""Tag value
        :rtype: str
        """
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
        


class Task(AbstractModel):
    r"""Log download task description.

    """

    def __init__(self):
        r"""
        :param _TaskType: Download task type. 0: slow log; 1: error log.
        :type TaskType: int
        :param _TaskId: Task ID.
        :type TaskId: str
        :param _CreateTime: Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _UpdateTime: Update time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param _FileSize: File size.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FileSize: int
        :param _Status: Task status. 0: initialized; 1: running; 2: successful; 3: failed.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _Percent: Percentage.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Percent: int
        :param _Url: Download URL.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Url: str
        """
        self._TaskType = None
        self._TaskId = None
        self._CreateTime = None
        self._UpdateTime = None
        self._FileSize = None
        self._Status = None
        self._Percent = None
        self._Url = None

    @property
    def TaskType(self):
        r"""Download task type. 0: slow log; 1: error log.
        :rtype: int
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def TaskId(self):
        r"""Task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def CreateTime(self):
        r"""Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""Update time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def FileSize(self):
        r"""File size.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def Status(self):
        r"""Task status. 0: initialized; 1: running; 2: successful; 3: failed.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Percent(self):
        r"""Percentage.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def Url(self):
        r"""Download URL.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._TaskType = params.get("TaskType")
        self._TaskId = params.get("TaskId")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._FileSize = params.get("FileSize")
        self._Status = params.get("Status")
        self._Percent = params.get("Percent")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateDBInstancesRequest(AbstractModel):
    r"""TerminateDBInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Specifies the ID of the pre-isolated instance. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Specifies the ID of the pre-isolated instance. Log in to the [TencentDB for MongoDB console](https://console.cloud.tencent.com/mongodb), and copy the instance ID from the instance list.
        :rtype: str
        """
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
        


class TerminateDBInstancesResponse(AbstractModel):
    r"""TerminateDBInstances response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpgradeDBInstanceKernelVersionRequest(AbstractModel):
    r"""UpgradeDBInstanceKernelVersion request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: List of instance IDs, which are in the format of cmgo-p8vnipr5. It is the same as the format of the instance ID displayed on the TencentDB for MongoDB console page.
        :type InstanceId: str
        :param _InMaintenance: Whether to perform the upgrade during the maintenance period. 0 - no; 1 - yes.
        :type InMaintenance: int
        """
        self._InstanceId = None
        self._InMaintenance = None

    @property
    def InstanceId(self):
        r"""List of instance IDs, which are in the format of cmgo-p8vnipr5. It is the same as the format of the instance ID displayed on the TencentDB for MongoDB console page.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InMaintenance(self):
        r"""Whether to perform the upgrade during the maintenance period. 0 - no; 1 - yes.
        :rtype: int
        """
        return self._InMaintenance

    @InMaintenance.setter
    def InMaintenance(self, InMaintenance):
        self._InMaintenance = InMaintenance


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InMaintenance = params.get("InMaintenance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDBInstanceKernelVersionResponse(AbstractModel):
    r"""UpgradeDBInstanceKernelVersion response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Asynchronous process task ID.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Asynchronous process task ID.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class UpgradeDbInstanceVersionRequest(AbstractModel):
    r"""UpgradeDbInstanceVersion request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: List of instance IDs, which are in the format of cmgo-p8vnipr5. It is the same as the format of the instance ID displayed on the TencentDB for MongoDB console page.
        :type InstanceId: str
        :param _MongoVersion: Newly upgraded database version. Currently, it only supports MONGO_40_WT (version of the MongoDB 4.0 WiredTiger storage engine) and MONGO_42_WT (version of the MongoDB 4.2 WiredTiger storage engine).
        :type MongoVersion: str
        :param _InMaintenance: Whether to perform the upgrade during the maintenance period. 0 - upgrade now; 1 - upgrade during the maintenance period.
        :type InMaintenance: int
        """
        self._InstanceId = None
        self._MongoVersion = None
        self._InMaintenance = None

    @property
    def InstanceId(self):
        r"""List of instance IDs, which are in the format of cmgo-p8vnipr5. It is the same as the format of the instance ID displayed on the TencentDB for MongoDB console page.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MongoVersion(self):
        r"""Newly upgraded database version. Currently, it only supports MONGO_40_WT (version of the MongoDB 4.0 WiredTiger storage engine) and MONGO_42_WT (version of the MongoDB 4.2 WiredTiger storage engine).
        :rtype: str
        """
        return self._MongoVersion

    @MongoVersion.setter
    def MongoVersion(self, MongoVersion):
        self._MongoVersion = MongoVersion

    @property
    def InMaintenance(self):
        r"""Whether to perform the upgrade during the maintenance period. 0 - upgrade now; 1 - upgrade during the maintenance period.
        :rtype: int
        """
        return self._InMaintenance

    @InMaintenance.setter
    def InMaintenance(self, InMaintenance):
        self._InMaintenance = InMaintenance


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._MongoVersion = params.get("MongoVersion")
        self._InMaintenance = params.get("InMaintenance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDbInstanceVersionResponse(AbstractModel):
    r"""UpgradeDbInstanceVersion response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Asynchronous process task ID.
        :type FlowId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Asynchronous process task ID.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")