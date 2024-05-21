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


class AccessKey(AbstractModel):
    """Access key list

    """

    def __init__(self):
        r"""
        :param _AccessKeyId: Access key ID
        :type AccessKeyId: str
        :param _Status: Key status. Valid values: Active (activated), Inactive (not activated)
        :type Status: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        """
        self._AccessKeyId = None
        self._Status = None
        self._CreateTime = None

    @property
    def AccessKeyId(self):
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId

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
        self._AccessKeyId = params.get("AccessKeyId")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessKeyDetail(AbstractModel):
    """Access key

    """

    def __init__(self):
        r"""
        :param _AccessKeyId: Access key ID
        :type AccessKeyId: str
        :param _SecretAccessKey: Access key, which is visible only when it is created. Keep it properly.
        :type SecretAccessKey: str
        :param _Status: Key status. Valid values: `Active` (activated), `Inactive` (not activated).
        :type Status: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        """
        self._AccessKeyId = None
        self._SecretAccessKey = None
        self._Status = None
        self._CreateTime = None

    @property
    def AccessKeyId(self):
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId

    @property
    def SecretAccessKey(self):
        return self._SecretAccessKey

    @SecretAccessKey.setter
    def SecretAccessKey(self, SecretAccessKey):
        self._SecretAccessKey = SecretAccessKey

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
        self._AccessKeyId = params.get("AccessKeyId")
        self._SecretAccessKey = params.get("SecretAccessKey")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserRequest(AbstractModel):
    """AddUser request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Sub-user username
        :type Name: str
        :param _Remark: Sub-user remarks
        :type Remark: str
        :param _ConsoleLogin: Whether or not the sub-user is allowed to log in to the console. 0: No; 1: Yes.
        :type ConsoleLogin: int
        :param _UseApi: Whether or not to generate keys for sub-users. 0: No; 1: Yes.
        :type UseApi: int
        :param _Password: Sub-user's console login password. If no password rules have been set, the password must have a minimum of 8 characters containing uppercase letters, lowercase letters, digits, and special characters by default. This parameter will be valid only when the sub-user is allowed to log in to the console. If it is not specified and console login is allowed, the system will automatically generate a random 32-character password that contains uppercase letters, lowercase letters, digits, and special characters.
        :type Password: str
        :param _NeedResetPassword: If the sub-user needs to reset their password when they next log in to the console. 0: No; 1: Yes.
        :type NeedResetPassword: int
        :param _PhoneNum: Mobile number
        :type PhoneNum: str
        :param _CountryCode: Country/Area Code
        :type CountryCode: str
        :param _Email: Email
        :type Email: str
        """
        self._Name = None
        self._Remark = None
        self._ConsoleLogin = None
        self._UseApi = None
        self._Password = None
        self._NeedResetPassword = None
        self._PhoneNum = None
        self._CountryCode = None
        self._Email = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ConsoleLogin(self):
        return self._ConsoleLogin

    @ConsoleLogin.setter
    def ConsoleLogin(self, ConsoleLogin):
        self._ConsoleLogin = ConsoleLogin

    @property
    def UseApi(self):
        return self._UseApi

    @UseApi.setter
    def UseApi(self, UseApi):
        self._UseApi = UseApi

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def NeedResetPassword(self):
        return self._NeedResetPassword

    @NeedResetPassword.setter
    def NeedResetPassword(self, NeedResetPassword):
        self._NeedResetPassword = NeedResetPassword

    @property
    def PhoneNum(self):
        return self._PhoneNum

    @PhoneNum.setter
    def PhoneNum(self, PhoneNum):
        self._PhoneNum = PhoneNum

    @property
    def CountryCode(self):
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._ConsoleLogin = params.get("ConsoleLogin")
        self._UseApi = params.get("UseApi")
        self._Password = params.get("Password")
        self._NeedResetPassword = params.get("NeedResetPassword")
        self._PhoneNum = params.get("PhoneNum")
        self._CountryCode = params.get("CountryCode")
        self._Email = params.get("Email")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserResponse(AbstractModel):
    """AddUser response structure.

    """

    def __init__(self):
        r"""
        :param _Uin: Sub-user UIN
        :type Uin: int
        :param _Name: Sub-user username
        :type Name: str
        :param _Password: If the combination of input parameters indicates that a random password should be generated, the generated password is returned
        :type Password: str
        :param _SecretId: Sub-user's key ID
        :type SecretId: str
        :param _SecretKey: Sub-user's secret key
        :type SecretKey: str
        :param _Uid: Sub-user UID
        :type Uid: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Uin = None
        self._Name = None
        self._Password = None
        self._SecretId = None
        self._SecretKey = None
        self._Uid = None
        self._RequestId = None

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def SecretId(self):
        return self._SecretId

    @SecretId.setter
    def SecretId(self, SecretId):
        self._SecretId = SecretId

    @property
    def SecretKey(self):
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def Uid(self):
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._Name = params.get("Name")
        self._Password = params.get("Password")
        self._SecretId = params.get("SecretId")
        self._SecretKey = params.get("SecretKey")
        self._Uid = params.get("Uid")
        self._RequestId = params.get("RequestId")


class AddUserToGroupRequest(AbstractModel):
    """AddUserToGroup request structure.

    """

    def __init__(self):
        r"""
        :param _Info: The association between the user group ID and the sub-user UIN/UID.
        :type Info: list of GroupIdOfUidInfo
        """
        self._Info = None

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self._Info = []
            for item in params.get("Info"):
                obj = GroupIdOfUidInfo()
                obj._deserialize(item)
                self._Info.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserToGroupResponse(AbstractModel):
    """AddUserToGroup response structure.

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


class AttachEntityOfPolicy(AbstractModel):
    """The entity associated with the policy

    """

    def __init__(self):
        r"""
        :param _Id: Entity ID
        :type Id: str
        :param _Name: Entity Name
Note: This field may return null, indicating that no valid value was found.
        :type Name: str
        :param _Uin: Entity UIN
Note: This field may return null, indicating that no valid value was found.
        :type Uin: int
        :param _RelatedType: Type of entity association. 1: Associate by users; 2: Associate by User Groups
        :type RelatedType: int
        :param _AttachmentTime: Policy association time
Note: this field may return `null`, indicating that no valid value was found.
        :type AttachmentTime: str
        """
        self._Id = None
        self._Name = None
        self._Uin = None
        self._RelatedType = None
        self._AttachmentTime = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def RelatedType(self):
        return self._RelatedType

    @RelatedType.setter
    def RelatedType(self, RelatedType):
        self._RelatedType = RelatedType

    @property
    def AttachmentTime(self):
        return self._AttachmentTime

    @AttachmentTime.setter
    def AttachmentTime(self, AttachmentTime):
        self._AttachmentTime = AttachmentTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Uin = params.get("Uin")
        self._RelatedType = params.get("RelatedType")
        self._AttachmentTime = params.get("AttachmentTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachGroupPolicyRequest(AbstractModel):
    """AttachGroupPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID
        :type PolicyId: int
        :param _AttachGroupId: User Group ID
        :type AttachGroupId: int
        """
        self._PolicyId = None
        self._AttachGroupId = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def AttachGroupId(self):
        return self._AttachGroupId

    @AttachGroupId.setter
    def AttachGroupId(self, AttachGroupId):
        self._AttachGroupId = AttachGroupId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._AttachGroupId = params.get("AttachGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachGroupPolicyResponse(AbstractModel):
    """AttachGroupPolicy response structure.

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


class AttachPolicyInfo(AbstractModel):
    """Associated policy

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID
        :type PolicyId: int
        :param _PolicyName: Policy name
Note: This field may return null, indicating that no valid value was found.
        :type PolicyName: str
        :param _AddTime: Time created
Note: This field may return null, indicating that no valid value was found.
        :type AddTime: str
        :param _CreateMode: How the policy was created: 1: Via console; 2: Via syntax
Note: This field may return null, indicating that no valid value was found.
        :type CreateMode: int
        :param _PolicyType: Valid values: `user` and `QCS`
Note: This field may return null, indicating that no valid value was found.
        :type PolicyType: str
        :param _Remark: Policy remarks
        :type Remark: str
        :param _OperateOwnerUin: Root account of the operator associating the policy
Note: this field may return null, indicating that no valid values can be obtained.
        :type OperateOwnerUin: str
        :param _OperateUin: The ID of the account associating the policy. If `UinType` is 0, this indicates that this is a sub-account `UIN`. If `UinType` is 1, this indicates this is a role ID
        :type OperateUin: str
        :param _OperateUinType: If `UinType` is 0, `OperateUin` indicates that this is a sub-account `UIN`. If `UinType` is 1, `OperateUin` indicates that this is a role ID
        :type OperateUinType: int
        :param _Deactived: Queries if the policy has been deactivated
Note: this field may return null, indicating that no valid values can be obtained.
        :type Deactived: int
        :param _DeactivedDetail: List of deprecated products
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeactivedDetail: list of str
        """
        self._PolicyId = None
        self._PolicyName = None
        self._AddTime = None
        self._CreateMode = None
        self._PolicyType = None
        self._Remark = None
        self._OperateOwnerUin = None
        self._OperateUin = None
        self._OperateUinType = None
        self._Deactived = None
        self._DeactivedDetail = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def CreateMode(self):
        return self._CreateMode

    @CreateMode.setter
    def CreateMode(self, CreateMode):
        self._CreateMode = CreateMode

    @property
    def PolicyType(self):
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def OperateOwnerUin(self):
        return self._OperateOwnerUin

    @OperateOwnerUin.setter
    def OperateOwnerUin(self, OperateOwnerUin):
        self._OperateOwnerUin = OperateOwnerUin

    @property
    def OperateUin(self):
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin

    @property
    def OperateUinType(self):
        return self._OperateUinType

    @OperateUinType.setter
    def OperateUinType(self, OperateUinType):
        self._OperateUinType = OperateUinType

    @property
    def Deactived(self):
        return self._Deactived

    @Deactived.setter
    def Deactived(self, Deactived):
        self._Deactived = Deactived

    @property
    def DeactivedDetail(self):
        return self._DeactivedDetail

    @DeactivedDetail.setter
    def DeactivedDetail(self, DeactivedDetail):
        self._DeactivedDetail = DeactivedDetail


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._AddTime = params.get("AddTime")
        self._CreateMode = params.get("CreateMode")
        self._PolicyType = params.get("PolicyType")
        self._Remark = params.get("Remark")
        self._OperateOwnerUin = params.get("OperateOwnerUin")
        self._OperateUin = params.get("OperateUin")
        self._OperateUinType = params.get("OperateUinType")
        self._Deactived = params.get("Deactived")
        self._DeactivedDetail = params.get("DeactivedDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachRolePolicyRequest(AbstractModel):
    """AttachRolePolicy request structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID. Either `PolicyId` or `PolicyName` must be entered
        :type PolicyId: int
        :param _AttachRoleId: Role ID, used to specify a role. Input either `AttachRoleId` or `AttachRoleName`
        :type AttachRoleId: str
        :param _AttachRoleName: Role name, used to specify a role. Input either `AttachRoleId` or `AttachRoleName`
        :type AttachRoleName: str
        :param _PolicyName: Policy name. Either `PolicyId` or `PolicyName` must be entered
        :type PolicyName: str
        """
        self._PolicyId = None
        self._AttachRoleId = None
        self._AttachRoleName = None
        self._PolicyName = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def AttachRoleId(self):
        return self._AttachRoleId

    @AttachRoleId.setter
    def AttachRoleId(self, AttachRoleId):
        self._AttachRoleId = AttachRoleId

    @property
    def AttachRoleName(self):
        return self._AttachRoleName

    @AttachRoleName.setter
    def AttachRoleName(self, AttachRoleName):
        self._AttachRoleName = AttachRoleName

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._AttachRoleId = params.get("AttachRoleId")
        self._AttachRoleName = params.get("AttachRoleName")
        self._PolicyName = params.get("PolicyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachRolePolicyResponse(AbstractModel):
    """AttachRolePolicy response structure.

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


class AttachUserPolicyRequest(AbstractModel):
    """AttachUserPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID
        :type PolicyId: int
        :param _AttachUin: Sub-account UIN
        :type AttachUin: int
        """
        self._PolicyId = None
        self._AttachUin = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def AttachUin(self):
        return self._AttachUin

    @AttachUin.setter
    def AttachUin(self, AttachUin):
        self._AttachUin = AttachUin


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._AttachUin = params.get("AttachUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachUserPolicyResponse(AbstractModel):
    """AttachUserPolicy response structure.

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


class AttachedPolicyOfRole(AbstractModel):
    """Policy associated with the role

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID
        :type PolicyId: int
        :param _PolicyName: Policy name
        :type PolicyName: str
        :param _AddTime: Time of association
        :type AddTime: str
        :param _PolicyType: Policy type. `User` indicates custom policy; `QCS` indicates preset policy
Note: This field may return null, indicating that no valid value was found.
        :type PolicyType: str
        :param _CreateMode: Policy creation method. 1: indicates the policy was created based on product function or item permission; other values indicate the policy was created based on the policy syntax
        :type CreateMode: int
        :param _Deactived: Whether the product has been deprecated (0: no; 1: yes)
Note: this field may return null, indicating that no valid values can be obtained.
        :type Deactived: int
        :param _DeactivedDetail: List of deprecated products
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeactivedDetail: list of str
        :param _Description: Policy description
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        """
        self._PolicyId = None
        self._PolicyName = None
        self._AddTime = None
        self._PolicyType = None
        self._CreateMode = None
        self._Deactived = None
        self._DeactivedDetail = None
        self._Description = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def PolicyType(self):
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def CreateMode(self):
        return self._CreateMode

    @CreateMode.setter
    def CreateMode(self, CreateMode):
        self._CreateMode = CreateMode

    @property
    def Deactived(self):
        return self._Deactived

    @Deactived.setter
    def Deactived(self, Deactived):
        self._Deactived = Deactived

    @property
    def DeactivedDetail(self):
        return self._DeactivedDetail

    @DeactivedDetail.setter
    def DeactivedDetail(self, DeactivedDetail):
        self._DeactivedDetail = DeactivedDetail

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._AddTime = params.get("AddTime")
        self._PolicyType = params.get("PolicyType")
        self._CreateMode = params.get("CreateMode")
        self._Deactived = params.get("Deactived")
        self._DeactivedDetail = params.get("DeactivedDetail")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachedUserPolicy(AbstractModel):
    """Details of policies associated with the user

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID.
        :type PolicyId: str
        :param _PolicyName: Policy name.
        :type PolicyName: str
        :param _Description: Policy description.
        :type Description: str
        :param _AddTime: Creation time.
        :type AddTime: str
        :param _StrategyType: Policy type (`1`: custom policy; `2`: preset policy).
        :type StrategyType: str
        :param _CreateMode: Creation mode (`1`: create by product feature or project permission; other values: create by policy syntax).
        :type CreateMode: str
        :param _Groups: Information on policies inherited from the user group.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Groups: list of AttachedUserPolicyGroupInfo
        :param _Deactived: Whether the product has been deprecated (`0`: no; `1`: yes).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Deactived: int
        :param _DeactivedDetail: List of deprecated products.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DeactivedDetail: list of str
        """
        self._PolicyId = None
        self._PolicyName = None
        self._Description = None
        self._AddTime = None
        self._StrategyType = None
        self._CreateMode = None
        self._Groups = None
        self._Deactived = None
        self._DeactivedDetail = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def StrategyType(self):
        return self._StrategyType

    @StrategyType.setter
    def StrategyType(self, StrategyType):
        self._StrategyType = StrategyType

    @property
    def CreateMode(self):
        return self._CreateMode

    @CreateMode.setter
    def CreateMode(self, CreateMode):
        self._CreateMode = CreateMode

    @property
    def Groups(self):
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def Deactived(self):
        return self._Deactived

    @Deactived.setter
    def Deactived(self, Deactived):
        self._Deactived = Deactived

    @property
    def DeactivedDetail(self):
        return self._DeactivedDetail

    @DeactivedDetail.setter
    def DeactivedDetail(self, DeactivedDetail):
        self._DeactivedDetail = DeactivedDetail


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._Description = params.get("Description")
        self._AddTime = params.get("AddTime")
        self._StrategyType = params.get("StrategyType")
        self._CreateMode = params.get("CreateMode")
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = AttachedUserPolicyGroupInfo()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._Deactived = params.get("Deactived")
        self._DeactivedDetail = params.get("DeactivedDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachedUserPolicyGroupInfo(AbstractModel):
    """Information on policies that are associated with the user and inherited from the user group

    """

    def __init__(self):
        r"""
        :param _GroupId: Group ID.
        :type GroupId: int
        :param _GroupName: Group name.
        :type GroupName: str
        """
        self._GroupId = None
        self._GroupName = None

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


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumeCustomMFATokenRequest(AbstractModel):
    """ConsumeCustomMFAToken request structure.

    """

    def __init__(self):
        r"""
        :param _MFAToken: Custom multi-factor verification Token
        :type MFAToken: str
        """
        self._MFAToken = None

    @property
    def MFAToken(self):
        return self._MFAToken

    @MFAToken.setter
    def MFAToken(self, MFAToken):
        self._MFAToken = MFAToken


    def _deserialize(self, params):
        self._MFAToken = params.get("MFAToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumeCustomMFATokenResponse(AbstractModel):
    """ConsumeCustomMFAToken response structure.

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


class CreateAccessKeyRequest(AbstractModel):
    """CreateAccessKey request structure.

    """

    def __init__(self):
        r"""
        :param _TargetUin: UIN of the specified user. If this parameter is left empty, the access key will be created for the current user by default.
        :type TargetUin: int
        """
        self._TargetUin = None

    @property
    def TargetUin(self):
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin


    def _deserialize(self, params):
        self._TargetUin = params.get("TargetUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccessKeyResponse(AbstractModel):
    """CreateAccessKey response structure.

    """

    def __init__(self):
        r"""
        :param _AccessKey: Access key
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccessKey: :class:`tencentcloud.cam.v20190116.models.AccessKeyDetail`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AccessKey = None
        self._RequestId = None

    @property
    def AccessKey(self):
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AccessKey") is not None:
            self._AccessKey = AccessKeyDetail()
            self._AccessKey._deserialize(params.get("AccessKey"))
        self._RequestId = params.get("RequestId")


class CreateGroupRequest(AbstractModel):
    """CreateGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GroupName: User Group name
        :type GroupName: str
        :param _Remark: User Group description
        :type Remark: str
        """
        self._GroupName = None
        self._Remark = None

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGroupResponse(AbstractModel):
    """CreateGroup response structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: User Group ID
        :type GroupId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class CreateOIDCConfigRequest(AbstractModel):
    """CreateOIDCConfig request structure.

    """

    def __init__(self):
        r"""
        :param _IdentityUrl: IdP URL.
        :type IdentityUrl: str
        :param _IdentityKey: Public key for signature, which must be Base64-encoded.
        :type IdentityKey: str
        :param _ClientId: Client ID.
        :type ClientId: list of str
        :param _Name: Name.
        :type Name: str
        :param _Description: Description.
        :type Description: str
        """
        self._IdentityUrl = None
        self._IdentityKey = None
        self._ClientId = None
        self._Name = None
        self._Description = None

    @property
    def IdentityUrl(self):
        return self._IdentityUrl

    @IdentityUrl.setter
    def IdentityUrl(self, IdentityUrl):
        self._IdentityUrl = IdentityUrl

    @property
    def IdentityKey(self):
        return self._IdentityKey

    @IdentityKey.setter
    def IdentityKey(self, IdentityKey):
        self._IdentityKey = IdentityKey

    @property
    def ClientId(self):
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

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


    def _deserialize(self, params):
        self._IdentityUrl = params.get("IdentityUrl")
        self._IdentityKey = params.get("IdentityKey")
        self._ClientId = params.get("ClientId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOIDCConfigResponse(AbstractModel):
    """CreateOIDCConfig response structure.

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


class CreatePolicyRequest(AbstractModel):
    """CreatePolicy request structure.

    """

    def __init__(self):
        r"""
        :param _PolicyName: Policy name
        :type PolicyName: str
        :param _PolicyDocument: Policy document, such as `{"version":"2.0","statement":[{"action":"name/sts:AssumeRole","effect":"allow","principal":{"service":["cloudaudit.cloud.tencent.com","cls.cloud.tencent.com"]}}]}`, where `principal` is used to specify the resources that the role is authorized to access. For more information on this parameter, please see the `RoleInfo` output parameter of the [GetRole](https://intl.cloud.tencent.com/document/product/598/36221?from_cn_redirect=1) API
        :type PolicyDocument: str
        :param _Description: Policy description
        :type Description: str
        """
        self._PolicyName = None
        self._PolicyDocument = None
        self._Description = None

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def PolicyDocument(self):
        return self._PolicyDocument

    @PolicyDocument.setter
    def PolicyDocument(self, PolicyDocument):
        self._PolicyDocument = PolicyDocument

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._PolicyName = params.get("PolicyName")
        self._PolicyDocument = params.get("PolicyDocument")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePolicyResponse(AbstractModel):
    """CreatePolicy response structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: ID of newly added policy
        :type PolicyId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PolicyId = None
        self._RequestId = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._RequestId = params.get("RequestId")


class CreatePolicyVersionRequest(AbstractModel):
    """CreatePolicyVersion request structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID
        :type PolicyId: int
        :param _PolicyDocument: The policy document to use as the content for the new version
        :type PolicyDocument: str
        :param _SetAsDefault: Specifies whether to set this version as the default version
        :type SetAsDefault: bool
        """
        self._PolicyId = None
        self._PolicyDocument = None
        self._SetAsDefault = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyDocument(self):
        return self._PolicyDocument

    @PolicyDocument.setter
    def PolicyDocument(self, PolicyDocument):
        self._PolicyDocument = PolicyDocument

    @property
    def SetAsDefault(self):
        return self._SetAsDefault

    @SetAsDefault.setter
    def SetAsDefault(self, SetAsDefault):
        self._SetAsDefault = SetAsDefault


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._PolicyDocument = params.get("PolicyDocument")
        self._SetAsDefault = params.get("SetAsDefault")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePolicyVersionResponse(AbstractModel):
    """CreatePolicyVersion response structure.

    """

    def __init__(self):
        r"""
        :param _VersionId: Policy version ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type VersionId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._VersionId = None
        self._RequestId = None

    @property
    def VersionId(self):
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VersionId = params.get("VersionId")
        self._RequestId = params.get("RequestId")


class CreateRoleRequest(AbstractModel):
    """CreateRole request structure.

    """

    def __init__(self):
        r"""
        :param _RoleName: Role name
        :type RoleName: str
        :param _PolicyDocument: Policy document
        :type PolicyDocument: str
        :param _Description: Role description
        :type Description: str
        :param _ConsoleLogin: Whether login is allowed. 1: yes, 0: no
        :type ConsoleLogin: int
        :param _SessionDuration: The maximum validity period of the temporary key for creating a role (range: 0-43200)
        :type SessionDuration: int
        :param _Tags: Tags bound to the role.
        :type Tags: list of RoleTags
        """
        self._RoleName = None
        self._PolicyDocument = None
        self._Description = None
        self._ConsoleLogin = None
        self._SessionDuration = None
        self._Tags = None

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def PolicyDocument(self):
        return self._PolicyDocument

    @PolicyDocument.setter
    def PolicyDocument(self, PolicyDocument):
        self._PolicyDocument = PolicyDocument

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ConsoleLogin(self):
        return self._ConsoleLogin

    @ConsoleLogin.setter
    def ConsoleLogin(self, ConsoleLogin):
        self._ConsoleLogin = ConsoleLogin

    @property
    def SessionDuration(self):
        return self._SessionDuration

    @SessionDuration.setter
    def SessionDuration(self, SessionDuration):
        self._SessionDuration = SessionDuration

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._RoleName = params.get("RoleName")
        self._PolicyDocument = params.get("PolicyDocument")
        self._Description = params.get("Description")
        self._ConsoleLogin = params.get("ConsoleLogin")
        self._SessionDuration = params.get("SessionDuration")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = RoleTags()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRoleResponse(AbstractModel):
    """CreateRole response structure.

    """

    def __init__(self):
        r"""
        :param _RoleId: Role ID
Note: This field may return null, indicating that no valid value was found.
        :type RoleId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RoleId = None
        self._RequestId = None

    @property
    def RoleId(self):
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RoleId = params.get("RoleId")
        self._RequestId = params.get("RequestId")


class CreateSAMLProviderRequest(AbstractModel):
    """CreateSAMLProvider request structure.

    """

    def __init__(self):
        r"""
        :param _Name: SAML identity provider name
        :type Name: str
        :param _Description: SAML identity provider description
        :type Description: str
        :param _SAMLMetadataDocument: SAML identity provider metadata document (Base64)
        :type SAMLMetadataDocument: str
        """
        self._Name = None
        self._Description = None
        self._SAMLMetadataDocument = None

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
    def SAMLMetadataDocument(self):
        return self._SAMLMetadataDocument

    @SAMLMetadataDocument.setter
    def SAMLMetadataDocument(self, SAMLMetadataDocument):
        self._SAMLMetadataDocument = SAMLMetadataDocument


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._SAMLMetadataDocument = params.get("SAMLMetadataDocument")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSAMLProviderResponse(AbstractModel):
    """CreateSAMLProvider response structure.

    """

    def __init__(self):
        r"""
        :param _ProviderArn: SAML identity provider resource descriptor
        :type ProviderArn: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProviderArn = None
        self._RequestId = None

    @property
    def ProviderArn(self):
        return self._ProviderArn

    @ProviderArn.setter
    def ProviderArn(self, ProviderArn):
        self._ProviderArn = ProviderArn

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProviderArn = params.get("ProviderArn")
        self._RequestId = params.get("RequestId")


class CreateServiceLinkedRoleRequest(AbstractModel):
    """CreateServiceLinkedRole request structure.

    """

    def __init__(self):
        r"""
        :param _QCSServiceName: Authorized service, i.e., Tencent Cloud service entity with this role attached.
        :type QCSServiceName: list of str
        :param _CustomSuffix: Custom suffix. A string you provide, which is combined with the service-provided prefix to form the complete role name.
        :type CustomSuffix: str
        :param _Description: Role description.
        :type Description: str
        :param _Tags: Tags bound to the role.
        :type Tags: list of RoleTags
        """
        self._QCSServiceName = None
        self._CustomSuffix = None
        self._Description = None
        self._Tags = None

    @property
    def QCSServiceName(self):
        return self._QCSServiceName

    @QCSServiceName.setter
    def QCSServiceName(self, QCSServiceName):
        self._QCSServiceName = QCSServiceName

    @property
    def CustomSuffix(self):
        return self._CustomSuffix

    @CustomSuffix.setter
    def CustomSuffix(self, CustomSuffix):
        self._CustomSuffix = CustomSuffix

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._QCSServiceName = params.get("QCSServiceName")
        self._CustomSuffix = params.get("CustomSuffix")
        self._Description = params.get("Description")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = RoleTags()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServiceLinkedRoleResponse(AbstractModel):
    """CreateServiceLinkedRole response structure.

    """

    def __init__(self):
        r"""
        :param _RoleId: Role ID
        :type RoleId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RoleId = None
        self._RequestId = None

    @property
    def RoleId(self):
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RoleId = params.get("RoleId")
        self._RequestId = params.get("RequestId")


class CreateUserOIDCConfigRequest(AbstractModel):
    """CreateUserOIDCConfig request structure.

    """

    def __init__(self):
        r"""
        :param _IdentityUrl: OpenID Connect IdP URL.
It corresponds to the value of the `issuer` field in the `Openid-configuration` provided by the enterprise IdP.
        :type IdentityUrl: str
        :param _IdentityKey: Signature public key, which is used to verify the OpenID Connect IdP's ID token and must be Base64-encoded. For the security of your account, we recommend you rotate it regularly.
        :type IdentityKey: str
        :param _ClientId: Client ID registered with the OpenID Connect IdP.
        :type ClientId: str
        :param _AuthorizationEndpoint: OpenID Connect IdP authorization endpoint. It corresponds to the value of the `authorization_endpoint` field in the `Openid-configuration` provided by the enterprise IdP.
        :type AuthorizationEndpoint: str
        :param _ResponseType: Authorization response type, which is always `id_token`.
        :type ResponseType: str
        :param _ResponseMode: Authorization response mode. Valid values: form_post (recommended); fragment.
        :type ResponseMode: str
        :param _MappingFiled: Mapping field name. It indicates which field in the `id_token` of the IdP is mapped to the username of a sub-user. It is usually the `sub` or `name` field
        :type MappingFiled: str
        :param _Scope: Authorization information scope. Valid values: openid (default); email; profile.
        :type Scope: list of str
        :param _Description: Description
        :type Description: str
        """
        self._IdentityUrl = None
        self._IdentityKey = None
        self._ClientId = None
        self._AuthorizationEndpoint = None
        self._ResponseType = None
        self._ResponseMode = None
        self._MappingFiled = None
        self._Scope = None
        self._Description = None

    @property
    def IdentityUrl(self):
        return self._IdentityUrl

    @IdentityUrl.setter
    def IdentityUrl(self, IdentityUrl):
        self._IdentityUrl = IdentityUrl

    @property
    def IdentityKey(self):
        return self._IdentityKey

    @IdentityKey.setter
    def IdentityKey(self, IdentityKey):
        self._IdentityKey = IdentityKey

    @property
    def ClientId(self):
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def AuthorizationEndpoint(self):
        return self._AuthorizationEndpoint

    @AuthorizationEndpoint.setter
    def AuthorizationEndpoint(self, AuthorizationEndpoint):
        self._AuthorizationEndpoint = AuthorizationEndpoint

    @property
    def ResponseType(self):
        return self._ResponseType

    @ResponseType.setter
    def ResponseType(self, ResponseType):
        self._ResponseType = ResponseType

    @property
    def ResponseMode(self):
        return self._ResponseMode

    @ResponseMode.setter
    def ResponseMode(self, ResponseMode):
        self._ResponseMode = ResponseMode

    @property
    def MappingFiled(self):
        return self._MappingFiled

    @MappingFiled.setter
    def MappingFiled(self, MappingFiled):
        self._MappingFiled = MappingFiled

    @property
    def Scope(self):
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._IdentityUrl = params.get("IdentityUrl")
        self._IdentityKey = params.get("IdentityKey")
        self._ClientId = params.get("ClientId")
        self._AuthorizationEndpoint = params.get("AuthorizationEndpoint")
        self._ResponseType = params.get("ResponseType")
        self._ResponseMode = params.get("ResponseMode")
        self._MappingFiled = params.get("MappingFiled")
        self._Scope = params.get("Scope")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserOIDCConfigResponse(AbstractModel):
    """CreateUserOIDCConfig response structure.

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


class CreateUserSAMLConfigRequest(AbstractModel):
    """CreateUserSAMLConfig request structure.

    """

    def __init__(self):
        r"""
        :param _SAMLMetadataDocument: SAML metadata document, which must be Base64 encoded.
        :type SAMLMetadataDocument: str
        """
        self._SAMLMetadataDocument = None

    @property
    def SAMLMetadataDocument(self):
        return self._SAMLMetadataDocument

    @SAMLMetadataDocument.setter
    def SAMLMetadataDocument(self, SAMLMetadataDocument):
        self._SAMLMetadataDocument = SAMLMetadataDocument


    def _deserialize(self, params):
        self._SAMLMetadataDocument = params.get("SAMLMetadataDocument")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserSAMLConfigResponse(AbstractModel):
    """CreateUserSAMLConfig response structure.

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


class DeleteAccessKeyRequest(AbstractModel):
    """DeleteAccessKey request structure.

    """

    def __init__(self):
        r"""
        :param _AccessKeyId: ID of the specified access key that needs to be deleted
        :type AccessKeyId: str
        :param _TargetUin: UIN of the specified user. If this parameter is left empty, the access key will be deleted for the current user by default.
        :type TargetUin: int
        """
        self._AccessKeyId = None
        self._TargetUin = None

    @property
    def AccessKeyId(self):
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId

    @property
    def TargetUin(self):
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin


    def _deserialize(self, params):
        self._AccessKeyId = params.get("AccessKeyId")
        self._TargetUin = params.get("TargetUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccessKeyResponse(AbstractModel):
    """DeleteAccessKey response structure.

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


class DeleteGroupRequest(AbstractModel):
    """DeleteGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: User Group ID
        :type GroupId: int
        """
        self._GroupId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGroupResponse(AbstractModel):
    """DeleteGroup response structure.

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


class DeleteOIDCConfigRequest(AbstractModel):
    """DeleteOIDCConfig request structure.

    """

    def __init__(self):
        r"""
        :param _Name: OIDC IdP name.
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOIDCConfigResponse(AbstractModel):
    """DeleteOIDCConfig response structure.

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


class DeletePolicyRequest(AbstractModel):
    """DeletePolicy request structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: Array. Array elements are policy IDs. Policies can be deleted in a batch
        :type PolicyId: list of int non-negative
        """
        self._PolicyId = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePolicyResponse(AbstractModel):
    """DeletePolicy response structure.

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


class DeletePolicyVersionRequest(AbstractModel):
    """DeletePolicyVersion request structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID
        :type PolicyId: int
        :param _VersionId: Policy version ID
        :type VersionId: list of int non-negative
        """
        self._PolicyId = None
        self._VersionId = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def VersionId(self):
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePolicyVersionResponse(AbstractModel):
    """DeletePolicyVersion response structure.

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


class DeleteRolePermissionsBoundaryRequest(AbstractModel):
    """DeleteRolePermissionsBoundary request structure.

    """

    def __init__(self):
        r"""
        :param _RoleId: Role ID (either it or the role name must be entered)
        :type RoleId: str
        :param _RoleName: Role name (either it or the role ID must be entered)
        :type RoleName: str
        """
        self._RoleId = None
        self._RoleName = None

    @property
    def RoleId(self):
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName


    def _deserialize(self, params):
        self._RoleId = params.get("RoleId")
        self._RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRolePermissionsBoundaryResponse(AbstractModel):
    """DeleteRolePermissionsBoundary response structure.

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


class DeleteRoleRequest(AbstractModel):
    """DeleteRole request structure.

    """

    def __init__(self):
        r"""
        :param _RoleId: Role ID, used to specify a role. Input either `RoleId` or `RoleName`
        :type RoleId: str
        :param _RoleName: Role name, used to specify a role. Input either `RoleId` or `RoleName`
        :type RoleName: str
        """
        self._RoleId = None
        self._RoleName = None

    @property
    def RoleId(self):
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName


    def _deserialize(self, params):
        self._RoleId = params.get("RoleId")
        self._RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRoleResponse(AbstractModel):
    """DeleteRole response structure.

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


class DeleteSAMLProviderRequest(AbstractModel):
    """DeleteSAMLProvider request structure.

    """

    def __init__(self):
        r"""
        :param _Name: SAML identity provider name
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSAMLProviderResponse(AbstractModel):
    """DeleteSAMLProvider response structure.

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


class DeleteServiceLinkedRoleRequest(AbstractModel):
    """DeleteServiceLinkedRole request structure.

    """

    def __init__(self):
        r"""
        :param _RoleName: Name of the service-linked role to be deleted.
        :type RoleName: str
        """
        self._RoleName = None

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName


    def _deserialize(self, params):
        self._RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteServiceLinkedRoleResponse(AbstractModel):
    """DeleteServiceLinkedRole response structure.

    """

    def __init__(self):
        r"""
        :param _DeletionTaskId: Deletion task identifier, which can be used to check the status of a service-linked role deletion.
        :type DeletionTaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DeletionTaskId = None
        self._RequestId = None

    @property
    def DeletionTaskId(self):
        return self._DeletionTaskId

    @DeletionTaskId.setter
    def DeletionTaskId(self, DeletionTaskId):
        self._DeletionTaskId = DeletionTaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeletionTaskId = params.get("DeletionTaskId")
        self._RequestId = params.get("RequestId")


class DeleteUserPermissionsBoundaryRequest(AbstractModel):
    """DeleteUserPermissionsBoundary request structure.

    """

    def __init__(self):
        r"""
        :param _TargetUin: Sub-account `Uin`
        :type TargetUin: int
        """
        self._TargetUin = None

    @property
    def TargetUin(self):
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin


    def _deserialize(self, params):
        self._TargetUin = params.get("TargetUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserPermissionsBoundaryResponse(AbstractModel):
    """DeleteUserPermissionsBoundary response structure.

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


class DeleteUserRequest(AbstractModel):
    """DeleteUser request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Sub-user username
        :type Name: str
        :param _Force: Whether to forcibly delete the sub-user. The default input parameter is `0`. `0`: do not delete the user if the user has undeleted API keys; `1`: first delete the API keys then delete the user if the user has undeleted API keys. To delete API keys, you need to have cam:DeleteApiKey permission, which enables you to delete both enabled and disabled API keys. If you do not have this permission, you will not be able to delete API keys and the user.
        :type Force: int
        """
        self._Name = None
        self._Force = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Force(self):
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserResponse(AbstractModel):
    """DeleteUser response structure.

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


class DescribeOIDCConfigRequest(AbstractModel):
    """DescribeOIDCConfig request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Name.
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOIDCConfigResponse(AbstractModel):
    """DescribeOIDCConfig response structure.

    """

    def __init__(self):
        r"""
        :param _ProviderType: IdP type. 11: Role IdP.
        :type ProviderType: int
        :param _IdentityUrl: IdP URL.
        :type IdentityUrl: str
        :param _IdentityKey: Public key for signature.
        :type IdentityKey: str
        :param _ClientId: Client ID.
        :type ClientId: list of str
        :param _Status: Status. 0: Not set; 2: Disabled; 11: Enabled.
        :type Status: int
        :param _Description: Description.
        :type Description: str
        :param _Name: Name.
        :type Name: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProviderType = None
        self._IdentityUrl = None
        self._IdentityKey = None
        self._ClientId = None
        self._Status = None
        self._Description = None
        self._Name = None
        self._RequestId = None

    @property
    def ProviderType(self):
        return self._ProviderType

    @ProviderType.setter
    def ProviderType(self, ProviderType):
        self._ProviderType = ProviderType

    @property
    def IdentityUrl(self):
        return self._IdentityUrl

    @IdentityUrl.setter
    def IdentityUrl(self, IdentityUrl):
        self._IdentityUrl = IdentityUrl

    @property
    def IdentityKey(self):
        return self._IdentityKey

    @IdentityKey.setter
    def IdentityKey(self, IdentityKey):
        self._IdentityKey = IdentityKey

    @property
    def ClientId(self):
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

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
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProviderType = params.get("ProviderType")
        self._IdentityUrl = params.get("IdentityUrl")
        self._IdentityKey = params.get("IdentityKey")
        self._ClientId = params.get("ClientId")
        self._Status = params.get("Status")
        self._Description = params.get("Description")
        self._Name = params.get("Name")
        self._RequestId = params.get("RequestId")


class DescribeRoleListRequest(AbstractModel):
    """DescribeRoleList request structure.

    """

    def __init__(self):
        r"""
        :param _Page: Page number, beginning from 1
        :type Page: int
        :param _Rp: Number of lines per page, no greater than 200
        :type Rp: int
        :param _Tags: A parameter used to filter the list of roles under a tag.
        :type Tags: list of RoleTags
        """
        self._Page = None
        self._Rp = None
        self._Tags = None

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Rp(self):
        return self._Rp

    @Rp.setter
    def Rp(self, Rp):
        self._Rp = Rp

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Page = params.get("Page")
        self._Rp = params.get("Rp")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = RoleTags()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoleListResponse(AbstractModel):
    """DescribeRoleList response structure.

    """

    def __init__(self):
        r"""
        :param _List: Role details list
Note: This field may return null, indicating that no valid value was found.
        :type List: list of RoleInfo
        :param _TotalNum: Total number of roles
        :type TotalNum: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._List = None
        self._TotalNum = None
        self._RequestId = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = RoleInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._TotalNum = params.get("TotalNum")
        self._RequestId = params.get("RequestId")


class DescribeSafeAuthFlagCollRequest(AbstractModel):
    """DescribeSafeAuthFlagColl request structure.

    """

    def __init__(self):
        r"""
        :param _SubUin: Sub-account
        :type SubUin: int
        """
        self._SubUin = None

    @property
    def SubUin(self):
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin


    def _deserialize(self, params):
        self._SubUin = params.get("SubUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSafeAuthFlagCollResponse(AbstractModel):
    """DescribeSafeAuthFlagColl response structure.

    """

    def __init__(self):
        r"""
        :param _LoginFlag: Login protection settings
        :type LoginFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionFlag`
        :param _ActionFlag: Sensitive operation protection settings
        :type ActionFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionFlag`
        :param _OffsiteFlag: Suspicious login location protection settings
        :type OffsiteFlag: :class:`tencentcloud.cam.v20190116.models.OffsiteFlag`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LoginFlag = None
        self._ActionFlag = None
        self._OffsiteFlag = None
        self._RequestId = None

    @property
    def LoginFlag(self):
        return self._LoginFlag

    @LoginFlag.setter
    def LoginFlag(self, LoginFlag):
        self._LoginFlag = LoginFlag

    @property
    def ActionFlag(self):
        return self._ActionFlag

    @ActionFlag.setter
    def ActionFlag(self, ActionFlag):
        self._ActionFlag = ActionFlag

    @property
    def OffsiteFlag(self):
        return self._OffsiteFlag

    @OffsiteFlag.setter
    def OffsiteFlag(self, OffsiteFlag):
        self._OffsiteFlag = OffsiteFlag

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LoginFlag") is not None:
            self._LoginFlag = LoginActionFlag()
            self._LoginFlag._deserialize(params.get("LoginFlag"))
        if params.get("ActionFlag") is not None:
            self._ActionFlag = LoginActionFlag()
            self._ActionFlag._deserialize(params.get("ActionFlag"))
        if params.get("OffsiteFlag") is not None:
            self._OffsiteFlag = OffsiteFlag()
            self._OffsiteFlag._deserialize(params.get("OffsiteFlag"))
        self._RequestId = params.get("RequestId")


class DescribeSafeAuthFlagIntlRequest(AbstractModel):
    """DescribeSafeAuthFlagIntl request structure.

    """


class DescribeSafeAuthFlagIntlResponse(AbstractModel):
    """DescribeSafeAuthFlagIntl response structure.

    """

    def __init__(self):
        r"""
        :param _LoginFlag: Login protection settings
        :type LoginFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionFlagIntl`
        :param _ActionFlag: Sensitive operation protection settings
        :type ActionFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionFlagIntl`
        :param _OffsiteFlag: Suspicious login location protection settings
        :type OffsiteFlag: :class:`tencentcloud.cam.v20190116.models.OffsiteFlag`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LoginFlag = None
        self._ActionFlag = None
        self._OffsiteFlag = None
        self._RequestId = None

    @property
    def LoginFlag(self):
        return self._LoginFlag

    @LoginFlag.setter
    def LoginFlag(self, LoginFlag):
        self._LoginFlag = LoginFlag

    @property
    def ActionFlag(self):
        return self._ActionFlag

    @ActionFlag.setter
    def ActionFlag(self, ActionFlag):
        self._ActionFlag = ActionFlag

    @property
    def OffsiteFlag(self):
        return self._OffsiteFlag

    @OffsiteFlag.setter
    def OffsiteFlag(self, OffsiteFlag):
        self._OffsiteFlag = OffsiteFlag

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LoginFlag") is not None:
            self._LoginFlag = LoginActionFlagIntl()
            self._LoginFlag._deserialize(params.get("LoginFlag"))
        if params.get("ActionFlag") is not None:
            self._ActionFlag = LoginActionFlagIntl()
            self._ActionFlag._deserialize(params.get("ActionFlag"))
        if params.get("OffsiteFlag") is not None:
            self._OffsiteFlag = OffsiteFlag()
            self._OffsiteFlag._deserialize(params.get("OffsiteFlag"))
        self._RequestId = params.get("RequestId")


class DescribeSubAccountsRequest(AbstractModel):
    """DescribeSubAccounts request structure.

    """

    def __init__(self):
        r"""
        :param _FilterSubAccountUin: List of sub-user UINs. Up to 50 UINs are supported.
        :type FilterSubAccountUin: list of int non-negative
        """
        self._FilterSubAccountUin = None

    @property
    def FilterSubAccountUin(self):
        return self._FilterSubAccountUin

    @FilterSubAccountUin.setter
    def FilterSubAccountUin(self, FilterSubAccountUin):
        self._FilterSubAccountUin = FilterSubAccountUin


    def _deserialize(self, params):
        self._FilterSubAccountUin = params.get("FilterSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubAccountsResponse(AbstractModel):
    """DescribeSubAccounts response structure.

    """

    def __init__(self):
        r"""
        :param _SubAccounts: Sub-user list
        :type SubAccounts: list of SubAccountUser
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SubAccounts = None
        self._RequestId = None

    @property
    def SubAccounts(self):
        return self._SubAccounts

    @SubAccounts.setter
    def SubAccounts(self, SubAccounts):
        self._SubAccounts = SubAccounts

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SubAccounts") is not None:
            self._SubAccounts = []
            for item in params.get("SubAccounts"):
                obj = SubAccountUser()
                obj._deserialize(item)
                self._SubAccounts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserOIDCConfigRequest(AbstractModel):
    """DescribeUserOIDCConfig request structure.

    """


class DescribeUserOIDCConfigResponse(AbstractModel):
    """DescribeUserOIDCConfig response structure.

    """

    def __init__(self):
        r"""
        :param _ProviderType: IdP type. 12: user OIDC IdP
        :type ProviderType: int
        :param _IdentityUrl: IdP URL
        :type IdentityUrl: str
        :param _IdentityKey: Signature public key
        :type IdentityKey: str
        :param _ClientId: Client ID
        :type ClientId: str
        :param _Status: Status. 0: not set; 2: disabled; 11: enabled.
        :type Status: int
        :param _AuthorizationEndpoint: Authorization endpoint
        :type AuthorizationEndpoint: str
        :param _Scope: Authorization scope
        :type Scope: list of str
        :param _ResponseType: Authorization response type
        :type ResponseType: str
        :param _ResponseMode: Authorization response mode
        :type ResponseMode: str
        :param _MappingFiled: Mapping field name
        :type MappingFiled: str
        :param _Description: Description
        :type Description: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProviderType = None
        self._IdentityUrl = None
        self._IdentityKey = None
        self._ClientId = None
        self._Status = None
        self._AuthorizationEndpoint = None
        self._Scope = None
        self._ResponseType = None
        self._ResponseMode = None
        self._MappingFiled = None
        self._Description = None
        self._RequestId = None

    @property
    def ProviderType(self):
        return self._ProviderType

    @ProviderType.setter
    def ProviderType(self, ProviderType):
        self._ProviderType = ProviderType

    @property
    def IdentityUrl(self):
        return self._IdentityUrl

    @IdentityUrl.setter
    def IdentityUrl(self, IdentityUrl):
        self._IdentityUrl = IdentityUrl

    @property
    def IdentityKey(self):
        return self._IdentityKey

    @IdentityKey.setter
    def IdentityKey(self, IdentityKey):
        self._IdentityKey = IdentityKey

    @property
    def ClientId(self):
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AuthorizationEndpoint(self):
        return self._AuthorizationEndpoint

    @AuthorizationEndpoint.setter
    def AuthorizationEndpoint(self, AuthorizationEndpoint):
        self._AuthorizationEndpoint = AuthorizationEndpoint

    @property
    def Scope(self):
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def ResponseType(self):
        return self._ResponseType

    @ResponseType.setter
    def ResponseType(self, ResponseType):
        self._ResponseType = ResponseType

    @property
    def ResponseMode(self):
        return self._ResponseMode

    @ResponseMode.setter
    def ResponseMode(self, ResponseMode):
        self._ResponseMode = ResponseMode

    @property
    def MappingFiled(self):
        return self._MappingFiled

    @MappingFiled.setter
    def MappingFiled(self, MappingFiled):
        self._MappingFiled = MappingFiled

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProviderType = params.get("ProviderType")
        self._IdentityUrl = params.get("IdentityUrl")
        self._IdentityKey = params.get("IdentityKey")
        self._ClientId = params.get("ClientId")
        self._Status = params.get("Status")
        self._AuthorizationEndpoint = params.get("AuthorizationEndpoint")
        self._Scope = params.get("Scope")
        self._ResponseType = params.get("ResponseType")
        self._ResponseMode = params.get("ResponseMode")
        self._MappingFiled = params.get("MappingFiled")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class DescribeUserSAMLConfigRequest(AbstractModel):
    """DescribeUserSAMLConfig request structure.

    """


class DescribeUserSAMLConfigResponse(AbstractModel):
    """DescribeUserSAMLConfig response structure.

    """

    def __init__(self):
        r"""
        :param _SAMLMetadata: SAML metadata document.
        :type SAMLMetadata: str
        :param _Status: Status. `0`: not set, `1`: enabled, `2`: disabled.
        :type Status: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SAMLMetadata = None
        self._Status = None
        self._RequestId = None

    @property
    def SAMLMetadata(self):
        return self._SAMLMetadata

    @SAMLMetadata.setter
    def SAMLMetadata(self, SAMLMetadata):
        self._SAMLMetadata = SAMLMetadata

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
        self._SAMLMetadata = params.get("SAMLMetadata")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DetachGroupPolicyRequest(AbstractModel):
    """DetachGroupPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID
        :type PolicyId: int
        :param _DetachGroupId: User Group ID
        :type DetachGroupId: int
        """
        self._PolicyId = None
        self._DetachGroupId = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def DetachGroupId(self):
        return self._DetachGroupId

    @DetachGroupId.setter
    def DetachGroupId(self, DetachGroupId):
        self._DetachGroupId = DetachGroupId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._DetachGroupId = params.get("DetachGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachGroupPolicyResponse(AbstractModel):
    """DetachGroupPolicy response structure.

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


class DetachRolePolicyRequest(AbstractModel):
    """DetachRolePolicy request structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID. Either `PolicyId` or `PolicyName` must be entered
        :type PolicyId: int
        :param _DetachRoleId: Role ID, which is used to specify a role. The input parameter is either `DetachRoleId` or `DetachRoleName`.
        :type DetachRoleId: str
        :param _DetachRoleName: Role name, which is used to specify a role. The input parameter is either `DetachRoleId` or `DetachRoleName`.
        :type DetachRoleName: str
        :param _PolicyName: Policy name. Either `PolicyId` or `PolicyName` must be entered
        :type PolicyName: str
        """
        self._PolicyId = None
        self._DetachRoleId = None
        self._DetachRoleName = None
        self._PolicyName = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def DetachRoleId(self):
        return self._DetachRoleId

    @DetachRoleId.setter
    def DetachRoleId(self, DetachRoleId):
        self._DetachRoleId = DetachRoleId

    @property
    def DetachRoleName(self):
        return self._DetachRoleName

    @DetachRoleName.setter
    def DetachRoleName(self, DetachRoleName):
        self._DetachRoleName = DetachRoleName

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._DetachRoleId = params.get("DetachRoleId")
        self._DetachRoleName = params.get("DetachRoleName")
        self._PolicyName = params.get("PolicyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachRolePolicyResponse(AbstractModel):
    """DetachRolePolicy response structure.

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


class DetachUserPolicyRequest(AbstractModel):
    """DetachUserPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID
        :type PolicyId: int
        :param _DetachUin: Sub-account UIN
        :type DetachUin: int
        """
        self._PolicyId = None
        self._DetachUin = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def DetachUin(self):
        return self._DetachUin

    @DetachUin.setter
    def DetachUin(self, DetachUin):
        self._DetachUin = DetachUin


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._DetachUin = params.get("DetachUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachUserPolicyResponse(AbstractModel):
    """DetachUserPolicy response structure.

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


class DisableUserSSORequest(AbstractModel):
    """DisableUserSSO request structure.

    """


class DisableUserSSOResponse(AbstractModel):
    """DisableUserSSO response structure.

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


class GetAccountSummaryRequest(AbstractModel):
    """GetAccountSummary request structure.

    """


class GetAccountSummaryResponse(AbstractModel):
    """GetAccountSummary response structure.

    """

    def __init__(self):
        r"""
        :param _Policies: Number of policies
        :type Policies: int
        :param _Roles: Number of roles
        :type Roles: int
        :param _Idps: Number of identity providers
        :type Idps: int
        :param _User: Number of sub-accounts
        :type User: int
        :param _Group: Number of groups
        :type Group: int
        :param _Member: Total number of grouped users
        :type Member: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Policies = None
        self._Roles = None
        self._Idps = None
        self._User = None
        self._Group = None
        self._Member = None
        self._RequestId = None

    @property
    def Policies(self):
        return self._Policies

    @Policies.setter
    def Policies(self, Policies):
        self._Policies = Policies

    @property
    def Roles(self):
        return self._Roles

    @Roles.setter
    def Roles(self, Roles):
        self._Roles = Roles

    @property
    def Idps(self):
        return self._Idps

    @Idps.setter
    def Idps(self, Idps):
        self._Idps = Idps

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Member(self):
        return self._Member

    @Member.setter
    def Member(self, Member):
        self._Member = Member

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Policies = params.get("Policies")
        self._Roles = params.get("Roles")
        self._Idps = params.get("Idps")
        self._User = params.get("User")
        self._Group = params.get("Group")
        self._Member = params.get("Member")
        self._RequestId = params.get("RequestId")


class GetCustomMFATokenInfoRequest(AbstractModel):
    """GetCustomMFATokenInfo request structure.

    """

    def __init__(self):
        r"""
        :param _MFAToken: Custom multi-factor verification Token
        :type MFAToken: str
        """
        self._MFAToken = None

    @property
    def MFAToken(self):
        return self._MFAToken

    @MFAToken.setter
    def MFAToken(self, MFAToken):
        self._MFAToken = MFAToken


    def _deserialize(self, params):
        self._MFAToken = params.get("MFAToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCustomMFATokenInfoResponse(AbstractModel):
    """GetCustomMFATokenInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Uin: Account ID corresponding to the custom multi-factor verification Token
        :type Uin: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Uin = None
        self._RequestId = None

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._RequestId = params.get("RequestId")


class GetGroupRequest(AbstractModel):
    """GetGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: User Group ID
        :type GroupId: int
        """
        self._GroupId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGroupResponse(AbstractModel):
    """GetGroup response structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: User Group ID
        :type GroupId: int
        :param _GroupName: User Group name
        :type GroupName: str
        :param _GroupNum: Number of members in the User Group
        :type GroupNum: int
        :param _Remark: User Group description
        :type Remark: str
        :param _CreateTime: Time User Group created
        :type CreateTime: str
        :param _UserInfo: User Group member information
        :type UserInfo: list of GroupMemberInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GroupId = None
        self._GroupName = None
        self._GroupNum = None
        self._Remark = None
        self._CreateTime = None
        self._UserInfo = None
        self._RequestId = None

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
    def GroupNum(self):
        return self._GroupNum

    @GroupNum.setter
    def GroupNum(self, GroupNum):
        self._GroupNum = GroupNum

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UserInfo(self):
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._GroupNum = params.get("GroupNum")
        self._Remark = params.get("Remark")
        self._CreateTime = params.get("CreateTime")
        if params.get("UserInfo") is not None:
            self._UserInfo = []
            for item in params.get("UserInfo"):
                obj = GroupMemberInfo()
                obj._deserialize(item)
                self._UserInfo.append(obj)
        self._RequestId = params.get("RequestId")


class GetPolicyRequest(AbstractModel):
    """GetPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID
        :type PolicyId: int
        """
        self._PolicyId = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPolicyResponse(AbstractModel):
    """GetPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _PolicyName: Policy name
Note: This field may return null, indicating that no valid value was found.
        :type PolicyName: str
        :param _Description: Policy description
Note: This field may return null, indicating that no valid value was found.
        :type Description: str
        :param _Type: 1: Custom policy; 2: Preset policy
Note: This field may return null, indicating that no valid value was found.
        :type Type: int
        :param _AddTime: Time created
Note: This field may return null, indicating that no valid value was found.
        :type AddTime: str
        :param _UpdateTime: Time of latest update
Note: This field may return null, indicating that no valid value was found.
        :type UpdateTime: str
        :param _PolicyDocument: Policy document
Note: This field may return null, indicating that no valid value was found.
        :type PolicyDocument: str
        :param _PresetAlias: Remarks
Note: this field may return null, indicating that no valid values can be obtained.
        :type PresetAlias: str
        :param _IsServiceLinkedRolePolicy: Whether it is a service-linked policy
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsServiceLinkedRolePolicy: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PolicyName = None
        self._Description = None
        self._Type = None
        self._AddTime = None
        self._UpdateTime = None
        self._PolicyDocument = None
        self._PresetAlias = None
        self._IsServiceLinkedRolePolicy = None
        self._RequestId = None

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def PolicyDocument(self):
        return self._PolicyDocument

    @PolicyDocument.setter
    def PolicyDocument(self, PolicyDocument):
        self._PolicyDocument = PolicyDocument

    @property
    def PresetAlias(self):
        return self._PresetAlias

    @PresetAlias.setter
    def PresetAlias(self, PresetAlias):
        self._PresetAlias = PresetAlias

    @property
    def IsServiceLinkedRolePolicy(self):
        return self._IsServiceLinkedRolePolicy

    @IsServiceLinkedRolePolicy.setter
    def IsServiceLinkedRolePolicy(self, IsServiceLinkedRolePolicy):
        self._IsServiceLinkedRolePolicy = IsServiceLinkedRolePolicy

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PolicyName = params.get("PolicyName")
        self._Description = params.get("Description")
        self._Type = params.get("Type")
        self._AddTime = params.get("AddTime")
        self._UpdateTime = params.get("UpdateTime")
        self._PolicyDocument = params.get("PolicyDocument")
        self._PresetAlias = params.get("PresetAlias")
        self._IsServiceLinkedRolePolicy = params.get("IsServiceLinkedRolePolicy")
        self._RequestId = params.get("RequestId")


class GetPolicyVersionRequest(AbstractModel):
    """GetPolicyVersion request structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID
        :type PolicyId: int
        :param _VersionId: Policy version, which can be obtained through `ListPolicyVersions`.
        :type VersionId: int
        """
        self._PolicyId = None
        self._VersionId = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def VersionId(self):
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPolicyVersionResponse(AbstractModel):
    """GetPolicyVersion response structure.

    """

    def __init__(self):
        r"""
        :param _PolicyVersion: Policy version details
Note: this field may return null, indicating that no valid values can be obtained.
        :type PolicyVersion: :class:`tencentcloud.cam.v20190116.models.PolicyVersionDetail`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PolicyVersion = None
        self._RequestId = None

    @property
    def PolicyVersion(self):
        return self._PolicyVersion

    @PolicyVersion.setter
    def PolicyVersion(self, PolicyVersion):
        self._PolicyVersion = PolicyVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PolicyVersion") is not None:
            self._PolicyVersion = PolicyVersionDetail()
            self._PolicyVersion._deserialize(params.get("PolicyVersion"))
        self._RequestId = params.get("RequestId")


class GetRoleRequest(AbstractModel):
    """GetRole request structure.

    """

    def __init__(self):
        r"""
        :param _RoleId: Role ID, used to specify role. Input either `RoleId` or `RoleName`
        :type RoleId: str
        :param _RoleName: Role name, used to specify role. Input either `RoleId` or `RoleName`
        :type RoleName: str
        """
        self._RoleId = None
        self._RoleName = None

    @property
    def RoleId(self):
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName


    def _deserialize(self, params):
        self._RoleId = params.get("RoleId")
        self._RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRoleResponse(AbstractModel):
    """GetRole response structure.

    """

    def __init__(self):
        r"""
        :param _RoleInfo: Role details
        :type RoleInfo: :class:`tencentcloud.cam.v20190116.models.RoleInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RoleInfo = None
        self._RequestId = None

    @property
    def RoleInfo(self):
        return self._RoleInfo

    @RoleInfo.setter
    def RoleInfo(self, RoleInfo):
        self._RoleInfo = RoleInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RoleInfo") is not None:
            self._RoleInfo = RoleInfo()
            self._RoleInfo._deserialize(params.get("RoleInfo"))
        self._RequestId = params.get("RequestId")


class GetSAMLProviderRequest(AbstractModel):
    """GetSAMLProvider request structure.

    """

    def __init__(self):
        r"""
        :param _Name: SAML identity provider name
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSAMLProviderResponse(AbstractModel):
    """GetSAMLProvider response structure.

    """

    def __init__(self):
        r"""
        :param _Name: SAML identity provider name
        :type Name: str
        :param _Description: SAML identity provider description
        :type Description: str
        :param _CreateTime: Time SAML identity provider created
        :type CreateTime: str
        :param _ModifyTime: Time SAML identity provider last modified
        :type ModifyTime: str
        :param _SAMLMetadata: SAML identity provider metadata document
        :type SAMLMetadata: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Name = None
        self._Description = None
        self._CreateTime = None
        self._ModifyTime = None
        self._SAMLMetadata = None
        self._RequestId = None

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
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def SAMLMetadata(self):
        return self._SAMLMetadata

    @SAMLMetadata.setter
    def SAMLMetadata(self, SAMLMetadata):
        self._SAMLMetadata = SAMLMetadata

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._SAMLMetadata = params.get("SAMLMetadata")
        self._RequestId = params.get("RequestId")


class GetSecurityLastUsedRequest(AbstractModel):
    """GetSecurityLastUsed request structure.

    """

    def __init__(self):
        r"""
        :param _SecretIdList: Key ID list query. Up to 10 key IDs can be queried.
        :type SecretIdList: list of str
        """
        self._SecretIdList = None

    @property
    def SecretIdList(self):
        return self._SecretIdList

    @SecretIdList.setter
    def SecretIdList(self, SecretIdList):
        self._SecretIdList = SecretIdList


    def _deserialize(self, params):
        self._SecretIdList = params.get("SecretIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSecurityLastUsedResponse(AbstractModel):
    """GetSecurityLastUsed response structure.

    """

    def __init__(self):
        r"""
        :param _SecretIdLastUsedRows: List of key ID’s recent usage records.
        :type SecretIdLastUsedRows: list of SecretIdLastUsed
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecretIdLastUsedRows = None
        self._RequestId = None

    @property
    def SecretIdLastUsedRows(self):
        return self._SecretIdLastUsedRows

    @SecretIdLastUsedRows.setter
    def SecretIdLastUsedRows(self, SecretIdLastUsedRows):
        self._SecretIdLastUsedRows = SecretIdLastUsedRows

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SecretIdLastUsedRows") is not None:
            self._SecretIdLastUsedRows = []
            for item in params.get("SecretIdLastUsedRows"):
                obj = SecretIdLastUsed()
                obj._deserialize(item)
                self._SecretIdLastUsedRows.append(obj)
        self._RequestId = params.get("RequestId")


class GetServiceLinkedRoleDeletionStatusRequest(AbstractModel):
    """GetServiceLinkedRoleDeletionStatus request structure.

    """

    def __init__(self):
        r"""
        :param _DeletionTaskId: Deletion task ID
        :type DeletionTaskId: str
        """
        self._DeletionTaskId = None

    @property
    def DeletionTaskId(self):
        return self._DeletionTaskId

    @DeletionTaskId.setter
    def DeletionTaskId(self, DeletionTaskId):
        self._DeletionTaskId = DeletionTaskId


    def _deserialize(self, params):
        self._DeletionTaskId = params.get("DeletionTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetServiceLinkedRoleDeletionStatusResponse(AbstractModel):
    """GetServiceLinkedRoleDeletionStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Status: NOT_STARTED, IN_PROGRESS, SUCCEEDED, FAILED
        :type Status: str
        :param _Reason: Reasons why the deletion failed.
        :type Reason: str
        :param _ServiceType: Service type
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceType: str
        :param _ServiceName: Service name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceName: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._Reason = None
        self._ServiceType = None
        self._ServiceName = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Reason = params.get("Reason")
        self._ServiceType = params.get("ServiceType")
        self._ServiceName = params.get("ServiceName")
        self._RequestId = params.get("RequestId")


class GetUserAppIdRequest(AbstractModel):
    """GetUserAppId request structure.

    """


class GetUserAppIdResponse(AbstractModel):
    """GetUserAppId response structure.

    """

    def __init__(self):
        r"""
        :param _Uin: UIN of the current account.
        :type Uin: str
        :param _OwnerUin: OwnerUin of the current account.
        :type OwnerUin: str
        :param _AppId: AppId of the current account.
        :type AppId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Uin = None
        self._OwnerUin = None
        self._AppId = None
        self._RequestId = None

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._OwnerUin = params.get("OwnerUin")
        self._AppId = params.get("AppId")
        self._RequestId = params.get("RequestId")


class GetUserRequest(AbstractModel):
    """GetUser request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Sub-user username
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetUserResponse(AbstractModel):
    """GetUser response structure.

    """

    def __init__(self):
        r"""
        :param _Uin: Sub-user UIN
        :type Uin: int
        :param _Name: Sub-user username
        :type Name: str
        :param _Uid: Sub-user UID
        :type Uid: int
        :param _Remark: Sub-user remarks
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Remark: str
        :param _ConsoleLogin: Whether the sub-user can log in to the console. `0`: No; `1`: Yes.
        :type ConsoleLogin: int
        :param _PhoneNum: Mobile number
        :type PhoneNum: str
        :param _CountryCode: Country/Area code
        :type CountryCode: str
        :param _Email: Email
        :type Email: str
        :param _RecentlyLoginIP: Last login IP
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecentlyLoginIP: str
        :param _RecentlyLoginTime: Last login time
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecentlyLoginTime: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Uin = None
        self._Name = None
        self._Uid = None
        self._Remark = None
        self._ConsoleLogin = None
        self._PhoneNum = None
        self._CountryCode = None
        self._Email = None
        self._RecentlyLoginIP = None
        self._RecentlyLoginTime = None
        self._RequestId = None

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Uid(self):
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ConsoleLogin(self):
        return self._ConsoleLogin

    @ConsoleLogin.setter
    def ConsoleLogin(self, ConsoleLogin):
        self._ConsoleLogin = ConsoleLogin

    @property
    def PhoneNum(self):
        return self._PhoneNum

    @PhoneNum.setter
    def PhoneNum(self, PhoneNum):
        self._PhoneNum = PhoneNum

    @property
    def CountryCode(self):
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def RecentlyLoginIP(self):
        return self._RecentlyLoginIP

    @RecentlyLoginIP.setter
    def RecentlyLoginIP(self, RecentlyLoginIP):
        self._RecentlyLoginIP = RecentlyLoginIP

    @property
    def RecentlyLoginTime(self):
        return self._RecentlyLoginTime

    @RecentlyLoginTime.setter
    def RecentlyLoginTime(self, RecentlyLoginTime):
        self._RecentlyLoginTime = RecentlyLoginTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._Name = params.get("Name")
        self._Uid = params.get("Uid")
        self._Remark = params.get("Remark")
        self._ConsoleLogin = params.get("ConsoleLogin")
        self._PhoneNum = params.get("PhoneNum")
        self._CountryCode = params.get("CountryCode")
        self._Email = params.get("Email")
        self._RecentlyLoginIP = params.get("RecentlyLoginIP")
        self._RecentlyLoginTime = params.get("RecentlyLoginTime")
        self._RequestId = params.get("RequestId")


class GroupIdOfUidInfo(AbstractModel):
    """Information on the association between a sub-user and a User Group

    """

    def __init__(self):
        r"""
        :param _GroupId: User Group ID
        :type GroupId: int
        :param _Uid: Sub-user UID
        :type Uid: int
        :param _Uin: Sub-user UIN. For UIN and UID, at least one of them is required.
        :type Uin: int
        """
        self._GroupId = None
        self._Uid = None
        self._Uin = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Uid(self):
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._Uid = params.get("Uid")
        self._Uin = params.get("Uin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfo(AbstractModel):
    """User Group information

    """

    def __init__(self):
        r"""
        :param _GroupId: User group ID
        :type GroupId: int
        :param _GroupName: User Group name
        :type GroupName: str
        :param _CreateTime: Time User Group created
        :type CreateTime: str
        :param _Remark: User Group description
        :type Remark: str
        """
        self._GroupId = None
        self._GroupName = None
        self._CreateTime = None
        self._Remark = None

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
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._CreateTime = params.get("CreateTime")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupMemberInfo(AbstractModel):
    """User Group user information

    """

    def __init__(self):
        r"""
        :param _Uid: Sub-user UID
        :type Uid: int
        :param _Uin: Sub-user UIN
        :type Uin: int
        :param _Name: Sub-user name
        :type Name: str
        :param _PhoneNum: Mobile number
        :type PhoneNum: str
        :param _CountryCode: Mobile number country/area code
        :type CountryCode: str
        :param _PhoneFlag: Whether the mobile phone has been verified. `0`: No; `1`: Yes.
        :type PhoneFlag: int
        :param _Email: Email address
        :type Email: str
        :param _EmailFlag: Whether the email has been verified. `0`: No; `1`: Yes.
        :type EmailFlag: int
        :param _UserType: User type. `1`: Global collaborator; `2`: Project collaborator; `3`: Message recipient.
        :type UserType: int
        :param _CreateTime: Time policy created
        :type CreateTime: str
        :param _IsReceiverOwner: Whether the user is the primary message recipient. `0`: No; `1`: Yes.
        :type IsReceiverOwner: int
        """
        self._Uid = None
        self._Uin = None
        self._Name = None
        self._PhoneNum = None
        self._CountryCode = None
        self._PhoneFlag = None
        self._Email = None
        self._EmailFlag = None
        self._UserType = None
        self._CreateTime = None
        self._IsReceiverOwner = None

    @property
    def Uid(self):
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PhoneNum(self):
        return self._PhoneNum

    @PhoneNum.setter
    def PhoneNum(self, PhoneNum):
        self._PhoneNum = PhoneNum

    @property
    def CountryCode(self):
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def PhoneFlag(self):
        return self._PhoneFlag

    @PhoneFlag.setter
    def PhoneFlag(self, PhoneFlag):
        self._PhoneFlag = PhoneFlag

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def EmailFlag(self):
        return self._EmailFlag

    @EmailFlag.setter
    def EmailFlag(self, EmailFlag):
        self._EmailFlag = EmailFlag

    @property
    def UserType(self):
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def IsReceiverOwner(self):
        return self._IsReceiverOwner

    @IsReceiverOwner.setter
    def IsReceiverOwner(self, IsReceiverOwner):
        self._IsReceiverOwner = IsReceiverOwner


    def _deserialize(self, params):
        self._Uid = params.get("Uid")
        self._Uin = params.get("Uin")
        self._Name = params.get("Name")
        self._PhoneNum = params.get("PhoneNum")
        self._CountryCode = params.get("CountryCode")
        self._PhoneFlag = params.get("PhoneFlag")
        self._Email = params.get("Email")
        self._EmailFlag = params.get("EmailFlag")
        self._UserType = params.get("UserType")
        self._CreateTime = params.get("CreateTime")
        self._IsReceiverOwner = params.get("IsReceiverOwner")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAccessKeysRequest(AbstractModel):
    """ListAccessKeys request structure.

    """

    def __init__(self):
        r"""
        :param _TargetUin: `UIN` of the specified user. If this parameter is left empty, access keys of the current user will be listed by default
        :type TargetUin: int
        """
        self._TargetUin = None

    @property
    def TargetUin(self):
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin


    def _deserialize(self, params):
        self._TargetUin = params.get("TargetUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAccessKeysResponse(AbstractModel):
    """ListAccessKeys response structure.

    """

    def __init__(self):
        r"""
        :param _AccessKeys: Access key list
Note: this field may return null, indicating that no valid values can be obtained.
        :type AccessKeys: list of AccessKey
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AccessKeys = None
        self._RequestId = None

    @property
    def AccessKeys(self):
        return self._AccessKeys

    @AccessKeys.setter
    def AccessKeys(self, AccessKeys):
        self._AccessKeys = AccessKeys

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AccessKeys") is not None:
            self._AccessKeys = []
            for item in params.get("AccessKeys"):
                obj = AccessKey()
                obj._deserialize(item)
                self._AccessKeys.append(obj)
        self._RequestId = params.get("RequestId")


class ListAttachedGroupPoliciesRequest(AbstractModel):
    """ListAttachedGroupPolicies request structure.

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: User group ID
        :type TargetGroupId: int
        :param _Page: Page number, which starts from 1. Default is 1
        :type Page: int
        :param _Rp: Number of entries per page; 20 by default
        :type Rp: int
        :param _Keyword: Search by keyword
        :type Keyword: str
        """
        self._TargetGroupId = None
        self._Page = None
        self._Rp = None
        self._Keyword = None

    @property
    def TargetGroupId(self):
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Rp(self):
        return self._Rp

    @Rp.setter
    def Rp(self, Rp):
        self._Rp = Rp

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        self._Page = params.get("Page")
        self._Rp = params.get("Rp")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAttachedGroupPoliciesResponse(AbstractModel):
    """ListAttachedGroupPolicies response structure.

    """

    def __init__(self):
        r"""
        :param _TotalNum: Total number of policies
        :type TotalNum: int
        :param _List: Policy list
        :type List: list of AttachPolicyInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalNum = None
        self._List = None
        self._RequestId = None

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalNum = params.get("TotalNum")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = AttachPolicyInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListAttachedRolePoliciesRequest(AbstractModel):
    """ListAttachedRolePolicies request structure.

    """

    def __init__(self):
        r"""
        :param _Page: Page number, beginning from 1
        :type Page: int
        :param _Rp: Number of lines per page, no more than 200
        :type Rp: int
        :param _RoleId: Role ID, used to specify a role. Input either `RoleId` or `RoleName`
        :type RoleId: str
        :param _RoleName: Role name, used to specify a role. Input either `RoleId` or `RoleName`
        :type RoleName: str
        :param _PolicyType: Filter according to policy type. `User` indicates querying custom policies only. `QCS` indicates querying preset policies only
        :type PolicyType: str
        :param _Keyword: Search by keyword
        :type Keyword: str
        """
        self._Page = None
        self._Rp = None
        self._RoleId = None
        self._RoleName = None
        self._PolicyType = None
        self._Keyword = None

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Rp(self):
        return self._Rp

    @Rp.setter
    def Rp(self, Rp):
        self._Rp = Rp

    @property
    def RoleId(self):
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def PolicyType(self):
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._Page = params.get("Page")
        self._Rp = params.get("Rp")
        self._RoleId = params.get("RoleId")
        self._RoleName = params.get("RoleName")
        self._PolicyType = params.get("PolicyType")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAttachedRolePoliciesResponse(AbstractModel):
    """ListAttachedRolePolicies response structure.

    """

    def __init__(self):
        r"""
        :param _List: List of policies associated with the role
        :type List: list of AttachedPolicyOfRole
        :param _TotalNum: Total number of policies associated with the role
        :type TotalNum: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._List = None
        self._TotalNum = None
        self._RequestId = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = AttachedPolicyOfRole()
                obj._deserialize(item)
                self._List.append(obj)
        self._TotalNum = params.get("TotalNum")
        self._RequestId = params.get("RequestId")


class ListAttachedUserAllPoliciesRequest(AbstractModel):
    """ListAttachedUserAllPolicies request structure.

    """

    def __init__(self):
        r"""
        :param _TargetUin: Target user ID.
        :type TargetUin: int
        :param _Rp: The number of policies displayed on each page. Value range: 1-200.
        :type Rp: int
        :param _Page: Page number. Value range: 1-200.
        :type Page: int
        :param _AttachType: `0`: return policies that are directly associated and inherited from the user group; `1`: return policies that are directly associated; `2`: return policies inherited from the user group.
        :type AttachType: int
        :param _StrategyType: Policy type.
        :type StrategyType: int
        :param _Keyword: Keyword for searching.
        :type Keyword: str
        """
        self._TargetUin = None
        self._Rp = None
        self._Page = None
        self._AttachType = None
        self._StrategyType = None
        self._Keyword = None

    @property
    def TargetUin(self):
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin

    @property
    def Rp(self):
        return self._Rp

    @Rp.setter
    def Rp(self, Rp):
        self._Rp = Rp

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def AttachType(self):
        return self._AttachType

    @AttachType.setter
    def AttachType(self, AttachType):
        self._AttachType = AttachType

    @property
    def StrategyType(self):
        return self._StrategyType

    @StrategyType.setter
    def StrategyType(self, StrategyType):
        self._StrategyType = StrategyType

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._TargetUin = params.get("TargetUin")
        self._Rp = params.get("Rp")
        self._Page = params.get("Page")
        self._AttachType = params.get("AttachType")
        self._StrategyType = params.get("StrategyType")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAttachedUserAllPoliciesResponse(AbstractModel):
    """ListAttachedUserAllPolicies response structure.

    """

    def __init__(self):
        r"""
        :param _PolicyList: Policy list.
        :type PolicyList: list of AttachedUserPolicy
        :param _TotalNum: Total number of policies.
        :type TotalNum: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PolicyList = None
        self._TotalNum = None
        self._RequestId = None

    @property
    def PolicyList(self):
        return self._PolicyList

    @PolicyList.setter
    def PolicyList(self, PolicyList):
        self._PolicyList = PolicyList

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PolicyList") is not None:
            self._PolicyList = []
            for item in params.get("PolicyList"):
                obj = AttachedUserPolicy()
                obj._deserialize(item)
                self._PolicyList.append(obj)
        self._TotalNum = params.get("TotalNum")
        self._RequestId = params.get("RequestId")


class ListAttachedUserPoliciesRequest(AbstractModel):
    """ListAttachedUserPolicies request structure.

    """

    def __init__(self):
        r"""
        :param _TargetUin: Sub-account UIN
        :type TargetUin: int
        :param _Page: Page number, which starts from 1. Default is 1
        :type Page: int
        :param _Rp: Number of entries per page; 20 by default
        :type Rp: int
        """
        self._TargetUin = None
        self._Page = None
        self._Rp = None

    @property
    def TargetUin(self):
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Rp(self):
        return self._Rp

    @Rp.setter
    def Rp(self, Rp):
        self._Rp = Rp


    def _deserialize(self, params):
        self._TargetUin = params.get("TargetUin")
        self._Page = params.get("Page")
        self._Rp = params.get("Rp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAttachedUserPoliciesResponse(AbstractModel):
    """ListAttachedUserPolicies response structure.

    """

    def __init__(self):
        r"""
        :param _TotalNum: Total number of policies
        :type TotalNum: int
        :param _List: Policy list
        :type List: list of AttachPolicyInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalNum = None
        self._List = None
        self._RequestId = None

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalNum = params.get("TotalNum")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = AttachPolicyInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListCollaboratorsRequest(AbstractModel):
    """ListCollaborators request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of entries per page. Default value: 20
        :type Limit: int
        :param _Offset: Pagination start value. Default value: 0
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

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
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListCollaboratorsResponse(AbstractModel):
    """ListCollaborators response structure.

    """

    def __init__(self):
        r"""
        :param _TotalNum: Total number
        :type TotalNum: int
        :param _Data: Collaborator information
        :type Data: list of SubAccountInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalNum = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

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
        self._TotalNum = params.get("TotalNum")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SubAccountInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ListEntitiesForPolicyRequest(AbstractModel):
    """ListEntitiesForPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID
        :type PolicyId: int
        :param _Page: Page number, which starts from 1. Default is 1
        :type Page: int
        :param _Rp: Number of entries per page; 20 by default
        :type Rp: int
        :param _EntityFilter: Valid values: `All`, `User`, `Group`, and `Role`. `All` means all entity types will be returned; `User` means only sub-accounts will be returned; `Group` means only User Groups will be returned; `Role` means only roles will be returned. `All` is the default value.
        :type EntityFilter: str
        """
        self._PolicyId = None
        self._Page = None
        self._Rp = None
        self._EntityFilter = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Rp(self):
        return self._Rp

    @Rp.setter
    def Rp(self, Rp):
        self._Rp = Rp

    @property
    def EntityFilter(self):
        return self._EntityFilter

    @EntityFilter.setter
    def EntityFilter(self, EntityFilter):
        self._EntityFilter = EntityFilter


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._Page = params.get("Page")
        self._Rp = params.get("Rp")
        self._EntityFilter = params.get("EntityFilter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListEntitiesForPolicyResponse(AbstractModel):
    """ListEntitiesForPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _TotalNum: Number of entities
Note: This field may return null, indicating that no valid value was found.
        :type TotalNum: int
        :param _List: Entity list
Note: This field may return null, indicating that no valid value was found.
        :type List: list of AttachEntityOfPolicy
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalNum = None
        self._List = None
        self._RequestId = None

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalNum = params.get("TotalNum")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = AttachEntityOfPolicy()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListGroupsForUserRequest(AbstractModel):
    """ListGroupsForUser request structure.

    """

    def __init__(self):
        r"""
        :param _Uid: Sub-user UID
        :type Uid: int
        :param _Rp: Number of entries per page; default is 20
        :type Rp: int
        :param _Page: Page number; default is 1
        :type Page: int
        :param _SubUin: Sub-account UIN
        :type SubUin: int
        """
        self._Uid = None
        self._Rp = None
        self._Page = None
        self._SubUin = None

    @property
    def Uid(self):
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def Rp(self):
        return self._Rp

    @Rp.setter
    def Rp(self, Rp):
        self._Rp = Rp

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def SubUin(self):
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin


    def _deserialize(self, params):
        self._Uid = params.get("Uid")
        self._Rp = params.get("Rp")
        self._Page = params.get("Page")
        self._SubUin = params.get("SubUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListGroupsForUserResponse(AbstractModel):
    """ListGroupsForUser response structure.

    """

    def __init__(self):
        r"""
        :param _TotalNum: Total number of User Groups to which the sub-user has been added
        :type TotalNum: int
        :param _GroupInfo: User Group information
        :type GroupInfo: list of GroupInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalNum = None
        self._GroupInfo = None
        self._RequestId = None

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def GroupInfo(self):
        return self._GroupInfo

    @GroupInfo.setter
    def GroupInfo(self, GroupInfo):
        self._GroupInfo = GroupInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalNum = params.get("TotalNum")
        if params.get("GroupInfo") is not None:
            self._GroupInfo = []
            for item in params.get("GroupInfo"):
                obj = GroupInfo()
                obj._deserialize(item)
                self._GroupInfo.append(obj)
        self._RequestId = params.get("RequestId")


class ListGroupsRequest(AbstractModel):
    """ListGroups request structure.

    """

    def __init__(self):
        r"""
        :param _Page: Page number; default is 1
        :type Page: int
        :param _Rp: Number of entries per page; default is 20
        :type Rp: int
        :param _Keyword: Filter by User Group name
        :type Keyword: str
        """
        self._Page = None
        self._Rp = None
        self._Keyword = None

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Rp(self):
        return self._Rp

    @Rp.setter
    def Rp(self, Rp):
        self._Rp = Rp

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._Page = params.get("Page")
        self._Rp = params.get("Rp")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListGroupsResponse(AbstractModel):
    """ListGroups response structure.

    """

    def __init__(self):
        r"""
        :param _TotalNum: Total number of User Groups
        :type TotalNum: int
        :param _GroupInfo: User group information array
        :type GroupInfo: list of GroupInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalNum = None
        self._GroupInfo = None
        self._RequestId = None

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def GroupInfo(self):
        return self._GroupInfo

    @GroupInfo.setter
    def GroupInfo(self, GroupInfo):
        self._GroupInfo = GroupInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalNum = params.get("TotalNum")
        if params.get("GroupInfo") is not None:
            self._GroupInfo = []
            for item in params.get("GroupInfo"):
                obj = GroupInfo()
                obj._deserialize(item)
                self._GroupInfo.append(obj)
        self._RequestId = params.get("RequestId")


class ListPoliciesRequest(AbstractModel):
    """ListPolicies request structure.

    """

    def __init__(self):
        r"""
        :param _Rp: Number of entries per page: must be greater than 0 and no greater than 200. Default is 20
        :type Rp: int
        :param _Page: Page number. Starts from 1 and cannot be greater than 200. Default is 1
        :type Page: int
        :param _Scope: Valid values: `All`, `QCS`, and `Local`. `All` means all policies will be returned; `QCS` means only preset policies will be returned; `Local` means only custom policies will be returned. `All` is the default value
        :type Scope: str
        :param _Keyword: Filter by policy name
        :type Keyword: str
        """
        self._Rp = None
        self._Page = None
        self._Scope = None
        self._Keyword = None

    @property
    def Rp(self):
        return self._Rp

    @Rp.setter
    def Rp(self, Rp):
        self._Rp = Rp

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Scope(self):
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._Rp = params.get("Rp")
        self._Page = params.get("Page")
        self._Scope = params.get("Scope")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListPoliciesResponse(AbstractModel):
    """ListPolicies response structure.

    """

    def __init__(self):
        r"""
        :param _TotalNum: Total number of policies
        :type TotalNum: int
        :param _List: Policy array. Each array contains fields including `policyId`, `policyName`, `addTime`, `type`, `description`, and `createMode`. 
policyId: policy ID 
policyName: policy name
addTime: policy creation time
type: 1: custom policy, 2: preset policy 
description: policy description 
createMode: 1 indicates a policy created based on business permissions, while other values indicate that the policy syntax can be viewed and the policy can be updated using the policy syntax
Attachments: number of associated users
ServiceType: the product the policy is associated with
IsAttached: this value should not be null when querying if a marked entity has been associated with a policy. 0 indicates that no policy has been associated, and 1 indicates that a policy has been associated
        :type List: list of StrategyInfo
        :param _ServiceTypeList: Reserved field
Note: This field may return null, indicating that no valid value was found.
        :type ServiceTypeList: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalNum = None
        self._List = None
        self._ServiceTypeList = None
        self._RequestId = None

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def ServiceTypeList(self):
        return self._ServiceTypeList

    @ServiceTypeList.setter
    def ServiceTypeList(self, ServiceTypeList):
        self._ServiceTypeList = ServiceTypeList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalNum = params.get("TotalNum")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = StrategyInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._ServiceTypeList = params.get("ServiceTypeList")
        self._RequestId = params.get("RequestId")


class ListPolicyVersionsRequest(AbstractModel):
    """ListPolicyVersions request structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID
        :type PolicyId: int
        """
        self._PolicyId = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListPolicyVersionsResponse(AbstractModel):
    """ListPolicyVersions response structure.

    """

    def __init__(self):
        r"""
        :param _Versions: Policy version list
Note: this field may return null, indicating that no valid values can be obtained.
        :type Versions: list of PolicyVersionItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Versions = None
        self._RequestId = None

    @property
    def Versions(self):
        return self._Versions

    @Versions.setter
    def Versions(self, Versions):
        self._Versions = Versions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Versions") is not None:
            self._Versions = []
            for item in params.get("Versions"):
                obj = PolicyVersionItem()
                obj._deserialize(item)
                self._Versions.append(obj)
        self._RequestId = params.get("RequestId")


class ListSAMLProvidersRequest(AbstractModel):
    """ListSAMLProviders request structure.

    """


class ListSAMLProvidersResponse(AbstractModel):
    """ListSAMLProviders response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of SAML identity providers
        :type TotalCount: int
        :param _SAMLProviderSet: List of SAML identity providers
        :type SAMLProviderSet: list of SAMLProviderInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._SAMLProviderSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SAMLProviderSet(self):
        return self._SAMLProviderSet

    @SAMLProviderSet.setter
    def SAMLProviderSet(self, SAMLProviderSet):
        self._SAMLProviderSet = SAMLProviderSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("SAMLProviderSet") is not None:
            self._SAMLProviderSet = []
            for item in params.get("SAMLProviderSet"):
                obj = SAMLProviderInfo()
                obj._deserialize(item)
                self._SAMLProviderSet.append(obj)
        self._RequestId = params.get("RequestId")


class ListUsersForGroupRequest(AbstractModel):
    """ListUsersForGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: User group ID
        :type GroupId: int
        :param _Page: Page number; default is 1
        :type Page: int
        :param _Rp: Number of entries per page; default is 20
        :type Rp: int
        """
        self._GroupId = None
        self._Page = None
        self._Rp = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Rp(self):
        return self._Rp

    @Rp.setter
    def Rp(self, Rp):
        self._Rp = Rp


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._Page = params.get("Page")
        self._Rp = params.get("Rp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUsersForGroupResponse(AbstractModel):
    """ListUsersForGroup response structure.

    """

    def __init__(self):
        r"""
        :param _TotalNum: Total number of users associated with the User Group
        :type TotalNum: int
        :param _UserInfo: Sub-user information
        :type UserInfo: list of GroupMemberInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalNum = None
        self._UserInfo = None
        self._RequestId = None

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def UserInfo(self):
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalNum = params.get("TotalNum")
        if params.get("UserInfo") is not None:
            self._UserInfo = []
            for item in params.get("UserInfo"):
                obj = GroupMemberInfo()
                obj._deserialize(item)
                self._UserInfo.append(obj)
        self._RequestId = params.get("RequestId")


class ListUsersRequest(AbstractModel):
    """ListUsers request structure.

    """


class ListUsersResponse(AbstractModel):
    """ListUsers response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Sub-user information
        :type Data: list of SubAccountInfo
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
                obj = SubAccountInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class LoginActionFlag(AbstractModel):
    """Login and sensitive operation flag

    """

    def __init__(self):
        r"""
        :param _Phone: Phone
        :type Phone: int
        :param _Token: Hard token
        :type Token: int
        :param _Stoken: Soft token
        :type Stoken: int
        :param _Wechat: WeChat
        :type Wechat: int
        :param _Custom: Custom
        :type Custom: int
        :param _Mail: Mail
        :type Mail: int
        :param _U2FToken: U2F token
        :type U2FToken: int
        """
        self._Phone = None
        self._Token = None
        self._Stoken = None
        self._Wechat = None
        self._Custom = None
        self._Mail = None
        self._U2FToken = None

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def Stoken(self):
        return self._Stoken

    @Stoken.setter
    def Stoken(self, Stoken):
        self._Stoken = Stoken

    @property
    def Wechat(self):
        return self._Wechat

    @Wechat.setter
    def Wechat(self, Wechat):
        self._Wechat = Wechat

    @property
    def Custom(self):
        return self._Custom

    @Custom.setter
    def Custom(self, Custom):
        self._Custom = Custom

    @property
    def Mail(self):
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail

    @property
    def U2FToken(self):
        return self._U2FToken

    @U2FToken.setter
    def U2FToken(self, U2FToken):
        self._U2FToken = U2FToken


    def _deserialize(self, params):
        self._Phone = params.get("Phone")
        self._Token = params.get("Token")
        self._Stoken = params.get("Stoken")
        self._Wechat = params.get("Wechat")
        self._Custom = params.get("Custom")
        self._Mail = params.get("Mail")
        self._U2FToken = params.get("U2FToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginActionFlagIntl(AbstractModel):
    """Login and sensitive operation flag

    """

    def __init__(self):
        r"""
        :param _Phone: Mobile number
        :type Phone: int
        :param _Token: Hard token
        :type Token: int
        :param _Stoken: Soft token
        :type Stoken: int
        :param _Wechat: WeChat
        :type Wechat: int
        :param _Custom: Custom
        :type Custom: int
        :param _Mail: Email
        :type Mail: int
        """
        self._Phone = None
        self._Token = None
        self._Stoken = None
        self._Wechat = None
        self._Custom = None
        self._Mail = None

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def Stoken(self):
        return self._Stoken

    @Stoken.setter
    def Stoken(self, Stoken):
        self._Stoken = Stoken

    @property
    def Wechat(self):
        return self._Wechat

    @Wechat.setter
    def Wechat(self, Wechat):
        self._Wechat = Wechat

    @property
    def Custom(self):
        return self._Custom

    @Custom.setter
    def Custom(self, Custom):
        self._Custom = Custom

    @property
    def Mail(self):
        return self._Mail

    @Mail.setter
    def Mail(self, Mail):
        self._Mail = Mail


    def _deserialize(self, params):
        self._Phone = params.get("Phone")
        self._Token = params.get("Token")
        self._Stoken = params.get("Stoken")
        self._Wechat = params.get("Wechat")
        self._Custom = params.get("Custom")
        self._Mail = params.get("Mail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginActionMfaFlag(AbstractModel):
    """Login and sensitive operation flag

    """

    def __init__(self):
        r"""
        :param _Phone: Mobile phone
        :type Phone: int
        :param _Stoken: Soft token
        :type Stoken: int
        :param _Wechat: WeChat
        :type Wechat: int
        """
        self._Phone = None
        self._Stoken = None
        self._Wechat = None

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Stoken(self):
        return self._Stoken

    @Stoken.setter
    def Stoken(self, Stoken):
        self._Stoken = Stoken

    @property
    def Wechat(self):
        return self._Wechat

    @Wechat.setter
    def Wechat(self, Wechat):
        self._Wechat = Wechat


    def _deserialize(self, params):
        self._Phone = params.get("Phone")
        self._Stoken = params.get("Stoken")
        self._Wechat = params.get("Wechat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OffsiteFlag(AbstractModel):
    """Suspicious login location settings

    """

    def __init__(self):
        r"""
        :param _VerifyFlag: Verification flag
        :type VerifyFlag: int
        :param _NotifyPhone: Phone notification
        :type NotifyPhone: int
        :param _NotifyEmail: Email notification
        :type NotifyEmail: int
        :param _NotifyWechat: WeChat notification
        :type NotifyWechat: int
        :param _Tips: Alert
        :type Tips: int
        """
        self._VerifyFlag = None
        self._NotifyPhone = None
        self._NotifyEmail = None
        self._NotifyWechat = None
        self._Tips = None

    @property
    def VerifyFlag(self):
        return self._VerifyFlag

    @VerifyFlag.setter
    def VerifyFlag(self, VerifyFlag):
        self._VerifyFlag = VerifyFlag

    @property
    def NotifyPhone(self):
        return self._NotifyPhone

    @NotifyPhone.setter
    def NotifyPhone(self, NotifyPhone):
        self._NotifyPhone = NotifyPhone

    @property
    def NotifyEmail(self):
        return self._NotifyEmail

    @NotifyEmail.setter
    def NotifyEmail(self, NotifyEmail):
        self._NotifyEmail = NotifyEmail

    @property
    def NotifyWechat(self):
        return self._NotifyWechat

    @NotifyWechat.setter
    def NotifyWechat(self, NotifyWechat):
        self._NotifyWechat = NotifyWechat

    @property
    def Tips(self):
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips


    def _deserialize(self, params):
        self._VerifyFlag = params.get("VerifyFlag")
        self._NotifyPhone = params.get("NotifyPhone")
        self._NotifyEmail = params.get("NotifyEmail")
        self._NotifyWechat = params.get("NotifyWechat")
        self._Tips = params.get("Tips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolicyVersionDetail(AbstractModel):
    """Policy version details

    """

    def __init__(self):
        r"""
        :param _VersionId: Policy version ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type VersionId: int
        :param _CreateDate: Policy version creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateDate: str
        :param _IsDefaultVersion: Whether it is the operative version. 0: no, 1: yes
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsDefaultVersion: int
        :param _Document: Policy syntax text
Note: this field may return null, indicating that no valid values can be obtained.
        :type Document: str
        """
        self._VersionId = None
        self._CreateDate = None
        self._IsDefaultVersion = None
        self._Document = None

    @property
    def VersionId(self):
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def CreateDate(self):
        return self._CreateDate

    @CreateDate.setter
    def CreateDate(self, CreateDate):
        self._CreateDate = CreateDate

    @property
    def IsDefaultVersion(self):
        return self._IsDefaultVersion

    @IsDefaultVersion.setter
    def IsDefaultVersion(self, IsDefaultVersion):
        self._IsDefaultVersion = IsDefaultVersion

    @property
    def Document(self):
        return self._Document

    @Document.setter
    def Document(self, Document):
        self._Document = Document


    def _deserialize(self, params):
        self._VersionId = params.get("VersionId")
        self._CreateDate = params.get("CreateDate")
        self._IsDefaultVersion = params.get("IsDefaultVersion")
        self._Document = params.get("Document")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolicyVersionItem(AbstractModel):
    """Policy version list element structure

    """

    def __init__(self):
        r"""
        :param _VersionId: Policy version ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type VersionId: int
        :param _CreateDate: Policy version creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateDate: str
        :param _IsDefaultVersion: Whether it is the operative version. 0: no, 1: yes
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsDefaultVersion: int
        """
        self._VersionId = None
        self._CreateDate = None
        self._IsDefaultVersion = None

    @property
    def VersionId(self):
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def CreateDate(self):
        return self._CreateDate

    @CreateDate.setter
    def CreateDate(self, CreateDate):
        self._CreateDate = CreateDate

    @property
    def IsDefaultVersion(self):
        return self._IsDefaultVersion

    @IsDefaultVersion.setter
    def IsDefaultVersion(self, IsDefaultVersion):
        self._IsDefaultVersion = IsDefaultVersion


    def _deserialize(self, params):
        self._VersionId = params.get("VersionId")
        self._CreateDate = params.get("CreateDate")
        self._IsDefaultVersion = params.get("IsDefaultVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutRolePermissionsBoundaryRequest(AbstractModel):
    """PutRolePermissionsBoundary request structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID
        :type PolicyId: int
        :param _RoleId: Role ID (either it or the role name must be entered)
        :type RoleId: str
        :param _RoleName: Role name (either it or the role ID must be entered)
        :type RoleName: str
        """
        self._PolicyId = None
        self._RoleId = None
        self._RoleName = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def RoleId(self):
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._RoleId = params.get("RoleId")
        self._RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutRolePermissionsBoundaryResponse(AbstractModel):
    """PutRolePermissionsBoundary response structure.

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


class PutUserPermissionsBoundaryRequest(AbstractModel):
    """PutUserPermissionsBoundary request structure.

    """

    def __init__(self):
        r"""
        :param _TargetUin: Sub-account `Uin`
        :type TargetUin: int
        :param _PolicyId: Policy ID
        :type PolicyId: int
        """
        self._TargetUin = None
        self._PolicyId = None

    @property
    def TargetUin(self):
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._TargetUin = params.get("TargetUin")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutUserPermissionsBoundaryResponse(AbstractModel):
    """PutUserPermissionsBoundary response structure.

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


class RemoveUserFromGroupRequest(AbstractModel):
    """RemoveUserFromGroup request structure.

    """

    def __init__(self):
        r"""
        :param _Info: The user’s UIN/UID to be deleted and the array corresponding to the user group ID.
        :type Info: list of GroupIdOfUidInfo
        """
        self._Info = None

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self._Info = []
            for item in params.get("Info"):
                obj = GroupIdOfUidInfo()
                obj._deserialize(item)
                self._Info.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserFromGroupResponse(AbstractModel):
    """RemoveUserFromGroup response structure.

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


class RoleInfo(AbstractModel):
    """Role details

    """

    def __init__(self):
        r"""
        :param _RoleId: Role ID
        :type RoleId: str
        :param _RoleName: Role name
        :type RoleName: str
        :param _PolicyDocument: Role policy document
        :type PolicyDocument: str
        :param _Description: Role description
        :type Description: str
        :param _AddTime: Time role created
        :type AddTime: str
        :param _UpdateTime: Time role last updated
        :type UpdateTime: str
        :param _ConsoleLogin: If login is allowed for the role
        :type ConsoleLogin: int
        :param _RoleType: User role. Valid values: `user`, `system`, `service_linked`
Note: this field may return null, indicating that no valid values can be obtained.
        :type RoleType: str
        :param _SessionDuration: Valid period
Note: this field may return null, indicating that no valid values can be obtained.
        :type SessionDuration: int
        :param _DeletionTaskId: Task identifier for deleting a service-linked role 
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeletionTaskId: str
        :param _Tags: Tags.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Tags: list of RoleTags
        """
        self._RoleId = None
        self._RoleName = None
        self._PolicyDocument = None
        self._Description = None
        self._AddTime = None
        self._UpdateTime = None
        self._ConsoleLogin = None
        self._RoleType = None
        self._SessionDuration = None
        self._DeletionTaskId = None
        self._Tags = None

    @property
    def RoleId(self):
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def PolicyDocument(self):
        return self._PolicyDocument

    @PolicyDocument.setter
    def PolicyDocument(self, PolicyDocument):
        self._PolicyDocument = PolicyDocument

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ConsoleLogin(self):
        return self._ConsoleLogin

    @ConsoleLogin.setter
    def ConsoleLogin(self, ConsoleLogin):
        self._ConsoleLogin = ConsoleLogin

    @property
    def RoleType(self):
        return self._RoleType

    @RoleType.setter
    def RoleType(self, RoleType):
        self._RoleType = RoleType

    @property
    def SessionDuration(self):
        return self._SessionDuration

    @SessionDuration.setter
    def SessionDuration(self, SessionDuration):
        self._SessionDuration = SessionDuration

    @property
    def DeletionTaskId(self):
        return self._DeletionTaskId

    @DeletionTaskId.setter
    def DeletionTaskId(self, DeletionTaskId):
        self._DeletionTaskId = DeletionTaskId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._RoleId = params.get("RoleId")
        self._RoleName = params.get("RoleName")
        self._PolicyDocument = params.get("PolicyDocument")
        self._Description = params.get("Description")
        self._AddTime = params.get("AddTime")
        self._UpdateTime = params.get("UpdateTime")
        self._ConsoleLogin = params.get("ConsoleLogin")
        self._RoleType = params.get("RoleType")
        self._SessionDuration = params.get("SessionDuration")
        self._DeletionTaskId = params.get("DeletionTaskId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = RoleTags()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoleTags(AbstractModel):
    """Role tag type

    """

    def __init__(self):
        r"""
        :param _Key: Tag key.
        :type Key: str
        :param _Value: Tag value.
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
        


class SAMLProviderInfo(AbstractModel):
    """SAML identity provider

    """

    def __init__(self):
        r"""
        :param _Name: SAML identity provider name
        :type Name: str
        :param _Description: SAML identity provider description
        :type Description: str
        :param _CreateTime: Time SAML identity provider created
        :type CreateTime: str
        :param _ModifyTime: Time SAML identity provider last modified
        :type ModifyTime: str
        """
        self._Name = None
        self._Description = None
        self._CreateTime = None
        self._ModifyTime = None

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
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecretIdLastUsed(AbstractModel):
    """The last time the key was used.

    """

    def __init__(self):
        r"""
        :param _SecretId: Key ID.
        :type SecretId: str
        :param _LastUsedDate: The date when the key ID was last used (the value is obtained one day later).
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type LastUsedDate: str
        :param _LastSecretUsedDate: The most recent date the key was accessed
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastSecretUsedDate: int
        """
        self._SecretId = None
        self._LastUsedDate = None
        self._LastSecretUsedDate = None

    @property
    def SecretId(self):
        return self._SecretId

    @SecretId.setter
    def SecretId(self, SecretId):
        self._SecretId = SecretId

    @property
    def LastUsedDate(self):
        return self._LastUsedDate

    @LastUsedDate.setter
    def LastUsedDate(self, LastUsedDate):
        self._LastUsedDate = LastUsedDate

    @property
    def LastSecretUsedDate(self):
        return self._LastSecretUsedDate

    @LastSecretUsedDate.setter
    def LastSecretUsedDate(self, LastSecretUsedDate):
        self._LastSecretUsedDate = LastSecretUsedDate


    def _deserialize(self, params):
        self._SecretId = params.get("SecretId")
        self._LastUsedDate = params.get("LastUsedDate")
        self._LastSecretUsedDate = params.get("LastSecretUsedDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetDefaultPolicyVersionRequest(AbstractModel):
    """SetDefaultPolicyVersion request structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID
        :type PolicyId: int
        :param _VersionId: Policy version, which can be obtained through `ListPolicyVersions`.
        :type VersionId: int
        """
        self._PolicyId = None
        self._VersionId = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def VersionId(self):
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetDefaultPolicyVersionResponse(AbstractModel):
    """SetDefaultPolicyVersion response structure.

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


class SetMfaFlagRequest(AbstractModel):
    """SetMfaFlag request structure.

    """

    def __init__(self):
        r"""
        :param _OpUin: Sets user UIN
        :type OpUin: int
        :param _LoginFlag: Sets login protection
        :type LoginFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionMfaFlag`
        :param _ActionFlag: Sets operation protection
        :type ActionFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionMfaFlag`
        """
        self._OpUin = None
        self._LoginFlag = None
        self._ActionFlag = None

    @property
    def OpUin(self):
        return self._OpUin

    @OpUin.setter
    def OpUin(self, OpUin):
        self._OpUin = OpUin

    @property
    def LoginFlag(self):
        return self._LoginFlag

    @LoginFlag.setter
    def LoginFlag(self, LoginFlag):
        self._LoginFlag = LoginFlag

    @property
    def ActionFlag(self):
        return self._ActionFlag

    @ActionFlag.setter
    def ActionFlag(self, ActionFlag):
        self._ActionFlag = ActionFlag


    def _deserialize(self, params):
        self._OpUin = params.get("OpUin")
        if params.get("LoginFlag") is not None:
            self._LoginFlag = LoginActionMfaFlag()
            self._LoginFlag._deserialize(params.get("LoginFlag"))
        if params.get("ActionFlag") is not None:
            self._ActionFlag = LoginActionMfaFlag()
            self._ActionFlag._deserialize(params.get("ActionFlag"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetMfaFlagResponse(AbstractModel):
    """SetMfaFlag response structure.

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


class StrategyInfo(AbstractModel):
    """Policy information

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID
        :type PolicyId: int
        :param _PolicyName: Policy name
        :type PolicyName: str
        :param _AddTime: Time policy created
Note: This field may return null, indicating that no valid value was found.
        :type AddTime: str
        :param _Type: Policy type. 1: Custom policy; 2: Preset policy
        :type Type: int
        :param _Description: Policy description
Note: This field may return null, indicating that no valid value was found.
        :type Description: str
        :param _CreateMode: How the policy was created: 1: Via console; 2: Via syntax
        :type CreateMode: int
        :param _Attachments: Number of associated users
        :type Attachments: int
        :param _ServiceType: Product associated with the policy
Note: This field may return null, indicating that no valid value was found.
        :type ServiceType: str
        :param _IsAttached: This value should not be null when querying whether a marked entity has been associated with a policy. 0 indicates that no policy has been associated, while 1 indicates that a policy has been associated
        :type IsAttached: int
        :param _Deactived: Queries if the policy has been deactivated
Note: this field may return null, indicating that no valid values can be obtained.
        :type Deactived: int
        :param _DeactivedDetail: List of deprecated products
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeactivedDetail: list of str
        :param _IsServiceLinkedPolicy: The deletion task identifier used to check the deletion status of the service-linked role
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsServiceLinkedPolicy: int
        :param _AttachEntityCount: The number of entities associated with the policy.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AttachEntityCount: int
        :param _AttachEntityBoundaryCount: The number of entities associated with the permission boundary.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AttachEntityBoundaryCount: int
        :param _UpdateTime: The last edited time.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UpdateTime: str
        """
        self._PolicyId = None
        self._PolicyName = None
        self._AddTime = None
        self._Type = None
        self._Description = None
        self._CreateMode = None
        self._Attachments = None
        self._ServiceType = None
        self._IsAttached = None
        self._Deactived = None
        self._DeactivedDetail = None
        self._IsServiceLinkedPolicy = None
        self._AttachEntityCount = None
        self._AttachEntityBoundaryCount = None
        self._UpdateTime = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateMode(self):
        return self._CreateMode

    @CreateMode.setter
    def CreateMode(self, CreateMode):
        self._CreateMode = CreateMode

    @property
    def Attachments(self):
        return self._Attachments

    @Attachments.setter
    def Attachments(self, Attachments):
        self._Attachments = Attachments

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def IsAttached(self):
        return self._IsAttached

    @IsAttached.setter
    def IsAttached(self, IsAttached):
        self._IsAttached = IsAttached

    @property
    def Deactived(self):
        return self._Deactived

    @Deactived.setter
    def Deactived(self, Deactived):
        self._Deactived = Deactived

    @property
    def DeactivedDetail(self):
        return self._DeactivedDetail

    @DeactivedDetail.setter
    def DeactivedDetail(self, DeactivedDetail):
        self._DeactivedDetail = DeactivedDetail

    @property
    def IsServiceLinkedPolicy(self):
        return self._IsServiceLinkedPolicy

    @IsServiceLinkedPolicy.setter
    def IsServiceLinkedPolicy(self, IsServiceLinkedPolicy):
        self._IsServiceLinkedPolicy = IsServiceLinkedPolicy

    @property
    def AttachEntityCount(self):
        return self._AttachEntityCount

    @AttachEntityCount.setter
    def AttachEntityCount(self, AttachEntityCount):
        self._AttachEntityCount = AttachEntityCount

    @property
    def AttachEntityBoundaryCount(self):
        return self._AttachEntityBoundaryCount

    @AttachEntityBoundaryCount.setter
    def AttachEntityBoundaryCount(self, AttachEntityBoundaryCount):
        self._AttachEntityBoundaryCount = AttachEntityBoundaryCount

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._AddTime = params.get("AddTime")
        self._Type = params.get("Type")
        self._Description = params.get("Description")
        self._CreateMode = params.get("CreateMode")
        self._Attachments = params.get("Attachments")
        self._ServiceType = params.get("ServiceType")
        self._IsAttached = params.get("IsAttached")
        self._Deactived = params.get("Deactived")
        self._DeactivedDetail = params.get("DeactivedDetail")
        self._IsServiceLinkedPolicy = params.get("IsServiceLinkedPolicy")
        self._AttachEntityCount = params.get("AttachEntityCount")
        self._AttachEntityBoundaryCount = params.get("AttachEntityBoundaryCount")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubAccountInfo(AbstractModel):
    """Sub-user information

    """

    def __init__(self):
        r"""
        :param _Uin: Sub-user user ID
        :type Uin: int
        :param _Name: Sub-user username
        :type Name: str
        :param _Uid: Sub-user UID
        :type Uid: int
        :param _Remark: Sub-user remarks
        :type Remark: str
        :param _ConsoleLogin: If sub-user can log in to the console
        :type ConsoleLogin: int
        :param _PhoneNum: Mobile number
        :type PhoneNum: str
        :param _CountryCode: Country/Area code
        :type CountryCode: str
        :param _Email: Email
        :type Email: str
        :param _CreateTime: Creation time
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _NickName: Nickname.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type NickName: str
        """
        self._Uin = None
        self._Name = None
        self._Uid = None
        self._Remark = None
        self._ConsoleLogin = None
        self._PhoneNum = None
        self._CountryCode = None
        self._Email = None
        self._CreateTime = None
        self._NickName = None

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Uid(self):
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ConsoleLogin(self):
        return self._ConsoleLogin

    @ConsoleLogin.setter
    def ConsoleLogin(self, ConsoleLogin):
        self._ConsoleLogin = ConsoleLogin

    @property
    def PhoneNum(self):
        return self._PhoneNum

    @PhoneNum.setter
    def PhoneNum(self, PhoneNum):
        self._PhoneNum = PhoneNum

    @property
    def CountryCode(self):
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def NickName(self):
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._Name = params.get("Name")
        self._Uid = params.get("Uid")
        self._Remark = params.get("Remark")
        self._ConsoleLogin = params.get("ConsoleLogin")
        self._PhoneNum = params.get("PhoneNum")
        self._CountryCode = params.get("CountryCode")
        self._Email = params.get("Email")
        self._CreateTime = params.get("CreateTime")
        self._NickName = params.get("NickName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubAccountUser(AbstractModel):
    """Sub-user information

    """

    def __init__(self):
        r"""
        :param _Uin: Sub-user ID
        :type Uin: int
        :param _Name: Sub-user name
        :type Name: str
        :param _Uid: Sub-user UID. UID is the unique identifier of a user who is a message recipient, while UIN is a unique identifier of a user.
        :type Uid: int
        :param _Remark: Sub-user remarks
        :type Remark: str
        :param _CreateTime: Creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _UserType: User type (1: root account; 2: sub-user; 3: WeCom sub-user; 4: collaborator; 5: message recipient)
        :type UserType: int
        :param _LastLoginIp: 
        :type LastLoginIp: str
        :param _LastLoginTime: 
        :type LastLoginTime: str
        """
        self._Uin = None
        self._Name = None
        self._Uid = None
        self._Remark = None
        self._CreateTime = None
        self._UserType = None
        self._LastLoginIp = None
        self._LastLoginTime = None

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Uid(self):
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UserType(self):
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def LastLoginIp(self):
        return self._LastLoginIp

    @LastLoginIp.setter
    def LastLoginIp(self, LastLoginIp):
        self._LastLoginIp = LastLoginIp

    @property
    def LastLoginTime(self):
        return self._LastLoginTime

    @LastLoginTime.setter
    def LastLoginTime(self, LastLoginTime):
        self._LastLoginTime = LastLoginTime


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._Name = params.get("Name")
        self._Uid = params.get("Uid")
        self._Remark = params.get("Remark")
        self._CreateTime = params.get("CreateTime")
        self._UserType = params.get("UserType")
        self._LastLoginIp = params.get("LastLoginIp")
        self._LastLoginTime = params.get("LastLoginTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagRoleRequest(AbstractModel):
    """TagRole request structure.

    """

    def __init__(self):
        r"""
        :param _Tags: Tag.
        :type Tags: list of RoleTags
        :param _RoleName: Role name. Specify either the role name or role ID.
        :type RoleName: str
        :param _RoleId: Role ID. Specify either the role ID or role name.
        :type RoleId: str
        """
        self._Tags = None
        self._RoleName = None
        self._RoleId = None

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def RoleId(self):
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId


    def _deserialize(self, params):
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = RoleTags()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RoleName = params.get("RoleName")
        self._RoleId = params.get("RoleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagRoleResponse(AbstractModel):
    """TagRole response structure.

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


class UntagRoleRequest(AbstractModel):
    """UntagRole request structure.

    """

    def __init__(self):
        r"""
        :param _TagKeys: Tag key.
        :type TagKeys: list of str
        :param _RoleName: Role name. Specify either the role name or role ID.
        :type RoleName: str
        :param _RoleId: Role ID. Specify either the role ID or role name.
        :type RoleId: str
        """
        self._TagKeys = None
        self._RoleName = None
        self._RoleId = None

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def RoleId(self):
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId


    def _deserialize(self, params):
        self._TagKeys = params.get("TagKeys")
        self._RoleName = params.get("RoleName")
        self._RoleId = params.get("RoleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UntagRoleResponse(AbstractModel):
    """UntagRole response structure.

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


class UpdateAccessKeyRequest(AbstractModel):
    """UpdateAccessKey request structure.

    """

    def __init__(self):
        r"""
        :param _AccessKeyId: ID of the specified access key that needs to be updated
        :type AccessKeyId: str
        :param _Status: Key status. Valid values: `Active` (activated), `Inactive` (not activated).
        :type Status: str
        :param _TargetUin: UIN of the specified user. If this parameter is left empty, the access key will be updated for the current user by default.
        :type TargetUin: int
        """
        self._AccessKeyId = None
        self._Status = None
        self._TargetUin = None

    @property
    def AccessKeyId(self):
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TargetUin(self):
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin


    def _deserialize(self, params):
        self._AccessKeyId = params.get("AccessKeyId")
        self._Status = params.get("Status")
        self._TargetUin = params.get("TargetUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAccessKeyResponse(AbstractModel):
    """UpdateAccessKey response structure.

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


class UpdateAssumeRolePolicyRequest(AbstractModel):
    """UpdateAssumeRolePolicy request structure.

    """

    def __init__(self):
        r"""
        :param _PolicyDocument: Policy document
        :type PolicyDocument: str
        :param _RoleId: Role ID, used to specify a role. Input either `RoleId` or `RoleName`
        :type RoleId: str
        :param _RoleName: Role name, used to specify a role. Input either `RoleId` or `RoleName`
        :type RoleName: str
        """
        self._PolicyDocument = None
        self._RoleId = None
        self._RoleName = None

    @property
    def PolicyDocument(self):
        return self._PolicyDocument

    @PolicyDocument.setter
    def PolicyDocument(self, PolicyDocument):
        self._PolicyDocument = PolicyDocument

    @property
    def RoleId(self):
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName


    def _deserialize(self, params):
        self._PolicyDocument = params.get("PolicyDocument")
        self._RoleId = params.get("RoleId")
        self._RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAssumeRolePolicyResponse(AbstractModel):
    """UpdateAssumeRolePolicy response structure.

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


class UpdateGroupRequest(AbstractModel):
    """UpdateGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: User Group ID
        :type GroupId: int
        :param _GroupName: User Group name
        :type GroupName: str
        :param _Remark: User Group description
        :type Remark: str
        """
        self._GroupId = None
        self._GroupName = None
        self._Remark = None

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
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGroupResponse(AbstractModel):
    """UpdateGroup response structure.

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


class UpdateOIDCConfigRequest(AbstractModel):
    """UpdateOIDCConfig request structure.

    """

    def __init__(self):
        r"""
        :param _IdentityUrl: IdP URL.
        :type IdentityUrl: str
        :param _IdentityKey: Public key for signature, which must be Base64-encoded.
        :type IdentityKey: str
        :param _ClientId: Client ID.
        :type ClientId: list of str
        :param _Name: Name.
        :type Name: str
        :param _Description: Description.
        :type Description: str
        """
        self._IdentityUrl = None
        self._IdentityKey = None
        self._ClientId = None
        self._Name = None
        self._Description = None

    @property
    def IdentityUrl(self):
        return self._IdentityUrl

    @IdentityUrl.setter
    def IdentityUrl(self, IdentityUrl):
        self._IdentityUrl = IdentityUrl

    @property
    def IdentityKey(self):
        return self._IdentityKey

    @IdentityKey.setter
    def IdentityKey(self, IdentityKey):
        self._IdentityKey = IdentityKey

    @property
    def ClientId(self):
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

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


    def _deserialize(self, params):
        self._IdentityUrl = params.get("IdentityUrl")
        self._IdentityKey = params.get("IdentityKey")
        self._ClientId = params.get("ClientId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOIDCConfigResponse(AbstractModel):
    """UpdateOIDCConfig response structure.

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


class UpdatePolicyRequest(AbstractModel):
    """UpdatePolicy request structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID. Either `PolicyId` or `PolicyName` must be entered
        :type PolicyId: int
        :param _PolicyName: Policy name. Either `PolicyName` or `PolicyId` must be entered
        :type PolicyName: str
        :param _Description: Policy description
        :type Description: str
        :param _PolicyDocument: Policy documentation, for example: `{"version":"2.0","statement":[{"action":"name/sts:AssumeRole","effect":"allow","principal":{"service":["cloudaudit.cloud.tencent.com","cls.cloud.tencent.com"]}}]}`, where `principal` is used to specify the service that is authorized to use the role. For more information about this parameter, see **RoleInfo** under **Output Parameters** in the [GetRole](https://intl.cloud.tencent.com/document/product/598/36221?from_cn_redirect=1).
        :type PolicyDocument: str
        :param _Alias: Preset policy remark
        :type Alias: str
        """
        self._PolicyId = None
        self._PolicyName = None
        self._Description = None
        self._PolicyDocument = None
        self._Alias = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def PolicyDocument(self):
        return self._PolicyDocument

    @PolicyDocument.setter
    def PolicyDocument(self, PolicyDocument):
        self._PolicyDocument = PolicyDocument

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._Description = params.get("Description")
        self._PolicyDocument = params.get("PolicyDocument")
        self._Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePolicyResponse(AbstractModel):
    """UpdatePolicy response structure.

    """

    def __init__(self):
        r"""
        :param _PolicyId: Policy ID, which will be returned only if the input parameter is `PolicyName`
Note: this field may return null, indicating that no valid values can be obtained.
        :type PolicyId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PolicyId = None
        self._RequestId = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._RequestId = params.get("RequestId")


class UpdateRoleConsoleLoginRequest(AbstractModel):
    """UpdateRoleConsoleLogin request structure.

    """

    def __init__(self):
        r"""
        :param _ConsoleLogin: Whether login is allowed. 1: yes, 0: no
        :type ConsoleLogin: int
        :param _RoleId: Role ID. Use either `RoleId` or `RoleName` as the input parameter.
        :type RoleId: int
        :param _RoleName: Role name. Use either `RoleId` or `RoleName` as the input parameter.
        :type RoleName: str
        """
        self._ConsoleLogin = None
        self._RoleId = None
        self._RoleName = None

    @property
    def ConsoleLogin(self):
        return self._ConsoleLogin

    @ConsoleLogin.setter
    def ConsoleLogin(self, ConsoleLogin):
        self._ConsoleLogin = ConsoleLogin

    @property
    def RoleId(self):
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName


    def _deserialize(self, params):
        self._ConsoleLogin = params.get("ConsoleLogin")
        self._RoleId = params.get("RoleId")
        self._RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRoleConsoleLoginResponse(AbstractModel):
    """UpdateRoleConsoleLogin response structure.

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


class UpdateRoleDescriptionRequest(AbstractModel):
    """UpdateRoleDescription request structure.

    """

    def __init__(self):
        r"""
        :param _Description: Role description
        :type Description: str
        :param _RoleId: Role ID, used to specify a role. Input either `RoleId` or `RoleName`
        :type RoleId: str
        :param _RoleName: Role name, used to specify a role. Input either `RoleId` or `RoleName`
        :type RoleName: str
        """
        self._Description = None
        self._RoleId = None
        self._RoleName = None

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RoleId(self):
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName


    def _deserialize(self, params):
        self._Description = params.get("Description")
        self._RoleId = params.get("RoleId")
        self._RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRoleDescriptionResponse(AbstractModel):
    """UpdateRoleDescription response structure.

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


class UpdateSAMLProviderRequest(AbstractModel):
    """UpdateSAMLProvider request structure.

    """

    def __init__(self):
        r"""
        :param _Name: SAML identity provider name
        :type Name: str
        :param _Description: SAML identity provider description
        :type Description: str
        :param _SAMLMetadataDocument: SAML identity provider metadata document (Base64)
        :type SAMLMetadataDocument: str
        """
        self._Name = None
        self._Description = None
        self._SAMLMetadataDocument = None

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
    def SAMLMetadataDocument(self):
        return self._SAMLMetadataDocument

    @SAMLMetadataDocument.setter
    def SAMLMetadataDocument(self, SAMLMetadataDocument):
        self._SAMLMetadataDocument = SAMLMetadataDocument


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._SAMLMetadataDocument = params.get("SAMLMetadataDocument")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateSAMLProviderResponse(AbstractModel):
    """UpdateSAMLProvider response structure.

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


class UpdateUserOIDCConfigRequest(AbstractModel):
    """UpdateUserOIDCConfig request structure.

    """

    def __init__(self):
        r"""
        :param _IdentityUrl: OpenID Connect IdP URL.
It corresponds to the value of the `issuer` field in the `Openid-configuration` provided by the enterprise IdP.
        :type IdentityUrl: str
        :param _IdentityKey: Signature public key, which is used to verify the OpenID Connect IdP's ID token and must be Base64-encoded. For the security of your account, we recommend you rotate it regularly.
        :type IdentityKey: str
        :param _ClientId: Client ID registered with the OpenID Connect IdP.
        :type ClientId: str
        :param _AuthorizationEndpoint: OpenID Connect IdP authorization endpoint. It corresponds to the value of the `authorization_endpoint` field in the `Openid-configuration` provided by the enterprise IdP.
        :type AuthorizationEndpoint: str
        :param _ResponseType: Authorization response type, which is always `id_token`.
        :type ResponseType: str
        :param _ResponseMode: Authorization response mode. Valid values: form_post (recommended); fragment.
        :type ResponseMode: str
        :param _MappingFiled: Mapping field name. It indicates which field in the `id_token` of the IdP is mapped to the username of a sub-user. It is usually the `sub` or `name` field
        :type MappingFiled: str
        :param _Scope: Authorization information scope. Valid values: openid (default); email; profile.
        :type Scope: list of str
        :param _Description: Description
        :type Description: str
        """
        self._IdentityUrl = None
        self._IdentityKey = None
        self._ClientId = None
        self._AuthorizationEndpoint = None
        self._ResponseType = None
        self._ResponseMode = None
        self._MappingFiled = None
        self._Scope = None
        self._Description = None

    @property
    def IdentityUrl(self):
        return self._IdentityUrl

    @IdentityUrl.setter
    def IdentityUrl(self, IdentityUrl):
        self._IdentityUrl = IdentityUrl

    @property
    def IdentityKey(self):
        return self._IdentityKey

    @IdentityKey.setter
    def IdentityKey(self, IdentityKey):
        self._IdentityKey = IdentityKey

    @property
    def ClientId(self):
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def AuthorizationEndpoint(self):
        return self._AuthorizationEndpoint

    @AuthorizationEndpoint.setter
    def AuthorizationEndpoint(self, AuthorizationEndpoint):
        self._AuthorizationEndpoint = AuthorizationEndpoint

    @property
    def ResponseType(self):
        return self._ResponseType

    @ResponseType.setter
    def ResponseType(self, ResponseType):
        self._ResponseType = ResponseType

    @property
    def ResponseMode(self):
        return self._ResponseMode

    @ResponseMode.setter
    def ResponseMode(self, ResponseMode):
        self._ResponseMode = ResponseMode

    @property
    def MappingFiled(self):
        return self._MappingFiled

    @MappingFiled.setter
    def MappingFiled(self, MappingFiled):
        self._MappingFiled = MappingFiled

    @property
    def Scope(self):
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._IdentityUrl = params.get("IdentityUrl")
        self._IdentityKey = params.get("IdentityKey")
        self._ClientId = params.get("ClientId")
        self._AuthorizationEndpoint = params.get("AuthorizationEndpoint")
        self._ResponseType = params.get("ResponseType")
        self._ResponseMode = params.get("ResponseMode")
        self._MappingFiled = params.get("MappingFiled")
        self._Scope = params.get("Scope")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserOIDCConfigResponse(AbstractModel):
    """UpdateUserOIDCConfig response structure.

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


class UpdateUserRequest(AbstractModel):
    """UpdateUser request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Sub-user username
        :type Name: str
        :param _Remark: Sub-user remarks
        :type Remark: str
        :param _ConsoleLogin: Whether or not the sub-user is allowed to log in to the console. 0: No; 1: Yes.
        :type ConsoleLogin: int
        :param _Password: Sub-user's console login password. If no password rules have been set, the password must have a minimum of 8 characters containing uppercase letters, lowercase letters, digits, and special characters by default. This parameter will be valid only when the sub-user is allowed to log in to the console. If it is not specified and console login is allowed, the system will automatically generate a random 32-character password that contains uppercase letters, lowercase letters, digits, and special characters.
        :type Password: str
        :param _NeedResetPassword: If the sub-user needs to reset their password when they next log in to the console. 0: No; 1: Yes.
        :type NeedResetPassword: int
        :param _PhoneNum: Mobile number
        :type PhoneNum: str
        :param _CountryCode: Country/Area Code
        :type CountryCode: str
        :param _Email: Email
        :type Email: str
        """
        self._Name = None
        self._Remark = None
        self._ConsoleLogin = None
        self._Password = None
        self._NeedResetPassword = None
        self._PhoneNum = None
        self._CountryCode = None
        self._Email = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ConsoleLogin(self):
        return self._ConsoleLogin

    @ConsoleLogin.setter
    def ConsoleLogin(self, ConsoleLogin):
        self._ConsoleLogin = ConsoleLogin

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def NeedResetPassword(self):
        return self._NeedResetPassword

    @NeedResetPassword.setter
    def NeedResetPassword(self, NeedResetPassword):
        self._NeedResetPassword = NeedResetPassword

    @property
    def PhoneNum(self):
        return self._PhoneNum

    @PhoneNum.setter
    def PhoneNum(self, PhoneNum):
        self._PhoneNum = PhoneNum

    @property
    def CountryCode(self):
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._ConsoleLogin = params.get("ConsoleLogin")
        self._Password = params.get("Password")
        self._NeedResetPassword = params.get("NeedResetPassword")
        self._PhoneNum = params.get("PhoneNum")
        self._CountryCode = params.get("CountryCode")
        self._Email = params.get("Email")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserResponse(AbstractModel):
    """UpdateUser response structure.

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


class UpdateUserSAMLConfigRequest(AbstractModel):
    """UpdateUserSAMLConfig request structure.

    """

    def __init__(self):
        r"""
        :param _Operate: Type of the modification operation. `enable`: enable, `disable`: disable, `updateSAML`: modify metadata document.
        :type Operate: str
        :param _SAMLMetadataDocument: Metadata document, which must be Base64 encoded. This parameter is required only when the value of `Operate` is `updateSAML`.
        :type SAMLMetadataDocument: str
        """
        self._Operate = None
        self._SAMLMetadataDocument = None

    @property
    def Operate(self):
        return self._Operate

    @Operate.setter
    def Operate(self, Operate):
        self._Operate = Operate

    @property
    def SAMLMetadataDocument(self):
        return self._SAMLMetadataDocument

    @SAMLMetadataDocument.setter
    def SAMLMetadataDocument(self, SAMLMetadataDocument):
        self._SAMLMetadataDocument = SAMLMetadataDocument


    def _deserialize(self, params):
        self._Operate = params.get("Operate")
        self._SAMLMetadataDocument = params.get("SAMLMetadataDocument")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserSAMLConfigResponse(AbstractModel):
    """UpdateUserSAMLConfig response structure.

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