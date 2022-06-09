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
        :param AccessKeyId: Access key ID
        :type AccessKeyId: str
        :param Status: Key status. Valid values: Active (activated), Inactive (not activated)
        :type Status: str
        :param CreateTime: Creation time
        :type CreateTime: str
        """
        self.AccessKeyId = None
        self.Status = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.AccessKeyId = params.get("AccessKeyId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserRequest(AbstractModel):
    """AddUser request structure.

    """

    def __init__(self):
        r"""
        :param Name: Sub-user username
        :type Name: str
        :param Remark: Sub-user remarks
        :type Remark: str
        :param ConsoleLogin: Whether or not the sub-user is allowed to log in to the console. 0: No; 1: Yes.
        :type ConsoleLogin: int
        :param UseApi: Whether or not to generate keys for sub-users. 0: No; 1: Yes.
        :type UseApi: int
        :param Password: Sub-user's console login password. If no password rules have been set, the password must have a minimum of 8 characters containing uppercase letters, lowercase letters, digits, and special characters by default. This parameter will be valid only when the sub-user is allowed to log in to the console. If it is not specified and console login is allowed, the system will automatically generate a random 32-character password that contains uppercase letters, lowercase letters, digits, and special characters.
        :type Password: str
        :param NeedResetPassword: If the sub-user needs to reset their password when they next log in to the console. 0: No; 1: Yes.
        :type NeedResetPassword: int
        :param PhoneNum: Mobile number
        :type PhoneNum: str
        :param CountryCode: Country/Area Code
        :type CountryCode: str
        :param Email: Email
        :type Email: str
        """
        self.Name = None
        self.Remark = None
        self.ConsoleLogin = None
        self.UseApi = None
        self.Password = None
        self.NeedResetPassword = None
        self.PhoneNum = None
        self.CountryCode = None
        self.Email = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.UseApi = params.get("UseApi")
        self.Password = params.get("Password")
        self.NeedResetPassword = params.get("NeedResetPassword")
        self.PhoneNum = params.get("PhoneNum")
        self.CountryCode = params.get("CountryCode")
        self.Email = params.get("Email")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserResponse(AbstractModel):
    """AddUser response structure.

    """

    def __init__(self):
        r"""
        :param Uin: Sub-user UIN
        :type Uin: int
        :param Name: Sub-user username
        :type Name: str
        :param Password: If the combination of input parameters indicates that a random password should be generated, the generated password is returned
        :type Password: str
        :param SecretId: Sub-user's key ID
        :type SecretId: str
        :param SecretKey: Sub-user's secret key
        :type SecretKey: str
        :param Uid: Sub-user UID
        :type Uid: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Uin = None
        self.Name = None
        self.Password = None
        self.SecretId = None
        self.SecretKey = None
        self.Uid = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.Password = params.get("Password")
        self.SecretId = params.get("SecretId")
        self.SecretKey = params.get("SecretKey")
        self.Uid = params.get("Uid")
        self.RequestId = params.get("RequestId")


class AddUserToGroupRequest(AbstractModel):
    """AddUserToGroup request structure.

    """

    def __init__(self):
        r"""
        :param Info: The association between the user group ID and the sub-user UIN/UID.
        :type Info: list of GroupIdOfUidInfo
        """
        self.Info = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = []
            for item in params.get("Info"):
                obj = GroupIdOfUidInfo()
                obj._deserialize(item)
                self.Info.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserToGroupResponse(AbstractModel):
    """AddUserToGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachEntityOfPolicy(AbstractModel):
    """The entity associated with the policy

    """

    def __init__(self):
        r"""
        :param Id: Entity ID
        :type Id: str
        :param Name: Entity Name
Note: This field may return null, indicating that no valid value was found.
        :type Name: str
        :param Uin: Entity UIN
Note: This field may return null, indicating that no valid value was found.
        :type Uin: int
        :param RelatedType: Type of entity association. 1: Associate by users; 2: Associate by User Groups
        :type RelatedType: int
        :param AttachmentTime: Policy association time
Note: this field may return `null`, indicating that no valid value was found.
        :type AttachmentTime: str
        """
        self.Id = None
        self.Name = None
        self.Uin = None
        self.RelatedType = None
        self.AttachmentTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Uin = params.get("Uin")
        self.RelatedType = params.get("RelatedType")
        self.AttachmentTime = params.get("AttachmentTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachGroupPolicyRequest(AbstractModel):
    """AttachGroupPolicy request structure.

    """

    def __init__(self):
        r"""
        :param PolicyId: Policy ID
        :type PolicyId: int
        :param AttachGroupId: User Group ID
        :type AttachGroupId: int
        """
        self.PolicyId = None
        self.AttachGroupId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.AttachGroupId = params.get("AttachGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachGroupPolicyResponse(AbstractModel):
    """AttachGroupPolicy response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachPolicyInfo(AbstractModel):
    """Associated policy

    """

    def __init__(self):
        r"""
        :param PolicyId: Policy ID
        :type PolicyId: int
        :param PolicyName: Policy name
Note: This field may return null, indicating that no valid value was found.
        :type PolicyName: str
        :param AddTime: Time created
Note: This field may return null, indicating that no valid value was found.
        :type AddTime: str
        :param CreateMode: How the policy was created: 1: Via console; 2: Via syntax
Note: This field may return null, indicating that no valid value was found.
        :type CreateMode: int
        :param PolicyType: Valid values: `user` and `QCS`
Note: This field may return null, indicating that no valid value was found.
        :type PolicyType: str
        :param Remark: Policy remarks
        :type Remark: str
        :param OperateOwnerUin: Root account of the operator associating the policy
Note: this field may return null, indicating that no valid values can be obtained.
        :type OperateOwnerUin: str
        :param OperateUin: The ID of the account associating the policy. If `UinType` is 0, this indicates that this is a sub-account `UIN`. If `UinType` is 1, this indicates this is a role ID
        :type OperateUin: str
        :param OperateUinType: If `UinType` is 0, `OperateUin` indicates that this is a sub-account `UIN`. If `UinType` is 1, `OperateUin` indicates that this is a role ID
        :type OperateUinType: int
        :param Deactived: Queries if the policy has been deactivated
Note: this field may return null, indicating that no valid values can be obtained.
        :type Deactived: int
        :param DeactivedDetail: List of deprecated products
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeactivedDetail: list of str
        """
        self.PolicyId = None
        self.PolicyName = None
        self.AddTime = None
        self.CreateMode = None
        self.PolicyType = None
        self.Remark = None
        self.OperateOwnerUin = None
        self.OperateUin = None
        self.OperateUinType = None
        self.Deactived = None
        self.DeactivedDetail = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.AddTime = params.get("AddTime")
        self.CreateMode = params.get("CreateMode")
        self.PolicyType = params.get("PolicyType")
        self.Remark = params.get("Remark")
        self.OperateOwnerUin = params.get("OperateOwnerUin")
        self.OperateUin = params.get("OperateUin")
        self.OperateUinType = params.get("OperateUinType")
        self.Deactived = params.get("Deactived")
        self.DeactivedDetail = params.get("DeactivedDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachRolePolicyRequest(AbstractModel):
    """AttachRolePolicy request structure.

    """

    def __init__(self):
        r"""
        :param PolicyId: Policy ID. Either `PolicyId` or `PolicyName` must be entered
        :type PolicyId: int
        :param AttachRoleId: Role ID, used to specify a role. Input either `AttachRoleId` or `AttachRoleName`
        :type AttachRoleId: str
        :param AttachRoleName: Role name, used to specify a role. Input either `AttachRoleId` or `AttachRoleName`
        :type AttachRoleName: str
        :param PolicyName: Policy name. Either `PolicyId` or `PolicyName` must be entered
        :type PolicyName: str
        """
        self.PolicyId = None
        self.AttachRoleId = None
        self.AttachRoleName = None
        self.PolicyName = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.AttachRoleId = params.get("AttachRoleId")
        self.AttachRoleName = params.get("AttachRoleName")
        self.PolicyName = params.get("PolicyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachRolePolicyResponse(AbstractModel):
    """AttachRolePolicy response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachUserPolicyRequest(AbstractModel):
    """AttachUserPolicy request structure.

    """

    def __init__(self):
        r"""
        :param PolicyId: Policy ID
        :type PolicyId: int
        :param AttachUin: Sub-account UIN
        :type AttachUin: int
        """
        self.PolicyId = None
        self.AttachUin = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.AttachUin = params.get("AttachUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachUserPolicyResponse(AbstractModel):
    """AttachUserPolicy response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachedPolicyOfRole(AbstractModel):
    """Policy associated with the role

    """

    def __init__(self):
        r"""
        :param PolicyId: Policy ID
        :type PolicyId: int
        :param PolicyName: Policy name
        :type PolicyName: str
        :param AddTime: Time of association
        :type AddTime: str
        :param PolicyType: Policy type. `User` indicates custom policy; `QCS` indicates preset policy
Note: This field may return null, indicating that no valid value was found.
        :type PolicyType: str
        :param CreateMode: Policy creation method. 1: indicates the policy was created based on product function or item permission; other values indicate the policy was created based on the policy syntax
        :type CreateMode: int
        :param Deactived: Whether the product has been deprecated (0: no; 1: yes)
Note: this field may return null, indicating that no valid values can be obtained.
        :type Deactived: int
        :param DeactivedDetail: List of deprecated products
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeactivedDetail: list of str
        :param Description: Policy description
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        """
        self.PolicyId = None
        self.PolicyName = None
        self.AddTime = None
        self.PolicyType = None
        self.CreateMode = None
        self.Deactived = None
        self.DeactivedDetail = None
        self.Description = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.AddTime = params.get("AddTime")
        self.PolicyType = params.get("PolicyType")
        self.CreateMode = params.get("CreateMode")
        self.Deactived = params.get("Deactived")
        self.DeactivedDetail = params.get("DeactivedDetail")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachedUserPolicy(AbstractModel):
    """Details of policies associated with the user

    """

    def __init__(self):
        r"""
        :param PolicyId: Policy ID.
        :type PolicyId: str
        :param PolicyName: Policy name.
        :type PolicyName: str
        :param Description: Policy description.
        :type Description: str
        :param AddTime: Creation time.
        :type AddTime: str
        :param StrategyType: Policy type (`1`: custom policy; `2`: preset policy).
        :type StrategyType: str
        :param CreateMode: Creation mode (`1`: create by product feature or project permission; other values: create by policy syntax).
        :type CreateMode: str
        :param Groups: Information on policies inherited from the user group.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Groups: list of AttachedUserPolicyGroupInfo
        :param Deactived: Whether the product has been deprecated (`0`: no; `1`: yes).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Deactived: int
        :param DeactivedDetail: List of deprecated products.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DeactivedDetail: list of str
        """
        self.PolicyId = None
        self.PolicyName = None
        self.Description = None
        self.AddTime = None
        self.StrategyType = None
        self.CreateMode = None
        self.Groups = None
        self.Deactived = None
        self.DeactivedDetail = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.Description = params.get("Description")
        self.AddTime = params.get("AddTime")
        self.StrategyType = params.get("StrategyType")
        self.CreateMode = params.get("CreateMode")
        if params.get("Groups") is not None:
            self.Groups = []
            for item in params.get("Groups"):
                obj = AttachedUserPolicyGroupInfo()
                obj._deserialize(item)
                self.Groups.append(obj)
        self.Deactived = params.get("Deactived")
        self.DeactivedDetail = params.get("DeactivedDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachedUserPolicyGroupInfo(AbstractModel):
    """Information on policies that are associated with the user and inherited from the user group

    """

    def __init__(self):
        r"""
        :param GroupId: Group ID.
        :type GroupId: int
        :param GroupName: Group name.
        :type GroupName: str
        """
        self.GroupId = None
        self.GroupName = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumeCustomMFATokenRequest(AbstractModel):
    """ConsumeCustomMFAToken request structure.

    """

    def __init__(self):
        r"""
        :param MFAToken: Custom multi-factor verification Token
        :type MFAToken: str
        """
        self.MFAToken = None


    def _deserialize(self, params):
        self.MFAToken = params.get("MFAToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumeCustomMFATokenResponse(AbstractModel):
    """ConsumeCustomMFAToken response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateGroupRequest(AbstractModel):
    """CreateGroup request structure.

    """

    def __init__(self):
        r"""
        :param GroupName: User Group name
        :type GroupName: str
        :param Remark: User Group description
        :type Remark: str
        """
        self.GroupName = None
        self.Remark = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGroupResponse(AbstractModel):
    """CreateGroup response structure.

    """

    def __init__(self):
        r"""
        :param GroupId: User Group ID
        :type GroupId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")


class CreateOIDCConfigRequest(AbstractModel):
    """CreateOIDCConfig request structure.

    """

    def __init__(self):
        r"""
        :param IdentityUrl: IdP URL.
        :type IdentityUrl: str
        :param IdentityKey: Public key for signature, which must be Base64-encoded.
        :type IdentityKey: str
        :param ClientId: Client ID.
        :type ClientId: list of str
        :param Name: Name.
        :type Name: str
        :param Description: Description.
        :type Description: str
        """
        self.IdentityUrl = None
        self.IdentityKey = None
        self.ClientId = None
        self.Name = None
        self.Description = None


    def _deserialize(self, params):
        self.IdentityUrl = params.get("IdentityUrl")
        self.IdentityKey = params.get("IdentityKey")
        self.ClientId = params.get("ClientId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOIDCConfigResponse(AbstractModel):
    """CreateOIDCConfig response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreatePolicyRequest(AbstractModel):
    """CreatePolicy request structure.

    """

    def __init__(self):
        r"""
        :param PolicyName: Policy name
        :type PolicyName: str
        :param PolicyDocument: Policy document, such as `{"version":"2.0","statement":[{"action":"name/sts:AssumeRole","effect":"allow","principal":{"service":["cloudaudit.cloud.tencent.com","cls.cloud.tencent.com"]}}]}`, where `principal` is used to specify the resources that the role is authorized to access. For more information on this parameter, please see the `RoleInfo` output parameter of the [GetRole](https://intl.cloud.tencent.com/document/product/598/36221?from_cn_redirect=1) API
        :type PolicyDocument: str
        :param Description: Policy description
        :type Description: str
        """
        self.PolicyName = None
        self.PolicyDocument = None
        self.Description = None


    def _deserialize(self, params):
        self.PolicyName = params.get("PolicyName")
        self.PolicyDocument = params.get("PolicyDocument")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePolicyResponse(AbstractModel):
    """CreatePolicy response structure.

    """

    def __init__(self):
        r"""
        :param PolicyId: ID of newly added policy
        :type PolicyId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.RequestId = params.get("RequestId")


class CreatePolicyVersionRequest(AbstractModel):
    """CreatePolicyVersion request structure.

    """

    def __init__(self):
        r"""
        :param PolicyId: Policy ID
        :type PolicyId: int
        :param PolicyDocument: The policy document to use as the content for the new version
        :type PolicyDocument: str
        :param SetAsDefault: Specifies whether to set this version as the default version
        :type SetAsDefault: bool
        """
        self.PolicyId = None
        self.PolicyDocument = None
        self.SetAsDefault = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyDocument = params.get("PolicyDocument")
        self.SetAsDefault = params.get("SetAsDefault")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePolicyVersionResponse(AbstractModel):
    """CreatePolicyVersion response structure.

    """

    def __init__(self):
        r"""
        :param VersionId: Policy version ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type VersionId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.VersionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VersionId = params.get("VersionId")
        self.RequestId = params.get("RequestId")


class CreateRoleRequest(AbstractModel):
    """CreateRole request structure.

    """

    def __init__(self):
        r"""
        :param RoleName: Role name
        :type RoleName: str
        :param PolicyDocument: Policy document
        :type PolicyDocument: str
        :param Description: Role description
        :type Description: str
        :param ConsoleLogin: Whether login is allowed. 1: yes, 0: no
        :type ConsoleLogin: int
        :param SessionDuration: The maximum validity period of the temporary key for creating a role (range: 0-43200)
        :type SessionDuration: int
        :param Tags: Tags bound to the role.
        :type Tags: list of RoleTags
        """
        self.RoleName = None
        self.PolicyDocument = None
        self.Description = None
        self.ConsoleLogin = None
        self.SessionDuration = None
        self.Tags = None


    def _deserialize(self, params):
        self.RoleName = params.get("RoleName")
        self.PolicyDocument = params.get("PolicyDocument")
        self.Description = params.get("Description")
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.SessionDuration = params.get("SessionDuration")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = RoleTags()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRoleResponse(AbstractModel):
    """CreateRole response structure.

    """

    def __init__(self):
        r"""
        :param RoleId: Role ID
Note: This field may return null, indicating that no valid value was found.
        :type RoleId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RoleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RoleId = params.get("RoleId")
        self.RequestId = params.get("RequestId")


class CreateSAMLProviderRequest(AbstractModel):
    """CreateSAMLProvider request structure.

    """

    def __init__(self):
        r"""
        :param Name: SAML identity provider name
        :type Name: str
        :param Description: SAML identity provider description
        :type Description: str
        :param SAMLMetadataDocument: SAML identity provider metadata document (Base64)
        :type SAMLMetadataDocument: str
        """
        self.Name = None
        self.Description = None
        self.SAMLMetadataDocument = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.SAMLMetadataDocument = params.get("SAMLMetadataDocument")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSAMLProviderResponse(AbstractModel):
    """CreateSAMLProvider response structure.

    """

    def __init__(self):
        r"""
        :param ProviderArn: SAML identity provider resource descriptor
        :type ProviderArn: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ProviderArn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProviderArn = params.get("ProviderArn")
        self.RequestId = params.get("RequestId")


class CreateServiceLinkedRoleRequest(AbstractModel):
    """CreateServiceLinkedRole request structure.

    """

    def __init__(self):
        r"""
        :param QCSServiceName: Authorized service, i.e., Tencent Cloud service entity with this role attached.
        :type QCSServiceName: list of str
        :param CustomSuffix: Custom suffix. A string you provide, which is combined with the service-provided prefix to form the complete role name.
        :type CustomSuffix: str
        :param Description: Role description.
        :type Description: str
        :param Tags: Tags bound to the role.
        :type Tags: list of RoleTags
        """
        self.QCSServiceName = None
        self.CustomSuffix = None
        self.Description = None
        self.Tags = None


    def _deserialize(self, params):
        self.QCSServiceName = params.get("QCSServiceName")
        self.CustomSuffix = params.get("CustomSuffix")
        self.Description = params.get("Description")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = RoleTags()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServiceLinkedRoleResponse(AbstractModel):
    """CreateServiceLinkedRole response structure.

    """

    def __init__(self):
        r"""
        :param RoleId: Role ID
        :type RoleId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RoleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RoleId = params.get("RoleId")
        self.RequestId = params.get("RequestId")


class CreateUserOIDCConfigRequest(AbstractModel):
    """CreateUserOIDCConfig request structure.

    """

    def __init__(self):
        r"""
        :param IdentityUrl: OpenID Connect IdP URL.
It corresponds to the value of the `issuer` field in the `Openid-configuration` provided by the enterprise IdP.
        :type IdentityUrl: str
        :param IdentityKey: Signature public key, which is used to verify the OpenID Connect IdP's ID token and must be Base64-encoded. For the security of your account, we recommend you rotate it regularly.
        :type IdentityKey: str
        :param ClientId: Client ID registered with the OpenID Connect IdP.
        :type ClientId: str
        :param AuthorizationEndpoint: OpenID Connect IdP authorization endpoint. It corresponds to the value of the `authorization_endpoint` field in the `Openid-configuration` provided by the enterprise IdP.
        :type AuthorizationEndpoint: str
        :param ResponseType: Authorization response type, which is always `id_token`.
        :type ResponseType: str
        :param ResponseMode: Authorization response mode. Valid values: form_post (recommended); fragment.
        :type ResponseMode: str
        :param MappingFiled: Mapping field name. It indicates which field in the `id_token` of the IdP is mapped to the username of a sub-user. It is usually the `sub` or `name` field
        :type MappingFiled: str
        :param Scope: Authorization information scope. Valid values: openid (default); email; profile.
        :type Scope: list of str
        :param Description: Description
        :type Description: str
        """
        self.IdentityUrl = None
        self.IdentityKey = None
        self.ClientId = None
        self.AuthorizationEndpoint = None
        self.ResponseType = None
        self.ResponseMode = None
        self.MappingFiled = None
        self.Scope = None
        self.Description = None


    def _deserialize(self, params):
        self.IdentityUrl = params.get("IdentityUrl")
        self.IdentityKey = params.get("IdentityKey")
        self.ClientId = params.get("ClientId")
        self.AuthorizationEndpoint = params.get("AuthorizationEndpoint")
        self.ResponseType = params.get("ResponseType")
        self.ResponseMode = params.get("ResponseMode")
        self.MappingFiled = params.get("MappingFiled")
        self.Scope = params.get("Scope")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserOIDCConfigResponse(AbstractModel):
    """CreateUserOIDCConfig response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateUserSAMLConfigRequest(AbstractModel):
    """CreateUserSAMLConfig request structure.

    """

    def __init__(self):
        r"""
        :param SAMLMetadataDocument: SAML metadata document, which must be Base64 encoded.
        :type SAMLMetadataDocument: str
        """
        self.SAMLMetadataDocument = None


    def _deserialize(self, params):
        self.SAMLMetadataDocument = params.get("SAMLMetadataDocument")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserSAMLConfigResponse(AbstractModel):
    """CreateUserSAMLConfig response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteGroupRequest(AbstractModel):
    """DeleteGroup request structure.

    """

    def __init__(self):
        r"""
        :param GroupId: User Group ID
        :type GroupId: int
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGroupResponse(AbstractModel):
    """DeleteGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteOIDCConfigRequest(AbstractModel):
    """DeleteOIDCConfig request structure.

    """

    def __init__(self):
        r"""
        :param Name: OIDC IdP name.
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOIDCConfigResponse(AbstractModel):
    """DeleteOIDCConfig response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePolicyRequest(AbstractModel):
    """DeletePolicy request structure.

    """

    def __init__(self):
        r"""
        :param PolicyId: Array. Array elements are policy IDs. Policies can be deleted in a batch
        :type PolicyId: list of int non-negative
        """
        self.PolicyId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePolicyResponse(AbstractModel):
    """DeletePolicy response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePolicyVersionRequest(AbstractModel):
    """DeletePolicyVersion request structure.

    """

    def __init__(self):
        r"""
        :param PolicyId: Policy ID
        :type PolicyId: int
        :param VersionId: Policy version ID
        :type VersionId: list of int non-negative
        """
        self.PolicyId = None
        self.VersionId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePolicyVersionResponse(AbstractModel):
    """DeletePolicyVersion response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRolePermissionsBoundaryRequest(AbstractModel):
    """DeleteRolePermissionsBoundary request structure.

    """

    def __init__(self):
        r"""
        :param RoleId: Role ID (either it or the role name must be entered)
        :type RoleId: str
        :param RoleName: Role name (either it or the role ID must be entered)
        :type RoleName: str
        """
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRolePermissionsBoundaryResponse(AbstractModel):
    """DeleteRolePermissionsBoundary response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRoleRequest(AbstractModel):
    """DeleteRole request structure.

    """

    def __init__(self):
        r"""
        :param RoleId: Role ID, used to specify a role. Input either `RoleId` or `RoleName`
        :type RoleId: str
        :param RoleName: Role name, used to specify a role. Input either `RoleId` or `RoleName`
        :type RoleName: str
        """
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRoleResponse(AbstractModel):
    """DeleteRole response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSAMLProviderRequest(AbstractModel):
    """DeleteSAMLProvider request structure.

    """

    def __init__(self):
        r"""
        :param Name: SAML identity provider name
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSAMLProviderResponse(AbstractModel):
    """DeleteSAMLProvider response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteServiceLinkedRoleRequest(AbstractModel):
    """DeleteServiceLinkedRole request structure.

    """

    def __init__(self):
        r"""
        :param RoleName: Name of the service-linked role to be deleted.
        :type RoleName: str
        """
        self.RoleName = None


    def _deserialize(self, params):
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteServiceLinkedRoleResponse(AbstractModel):
    """DeleteServiceLinkedRole response structure.

    """

    def __init__(self):
        r"""
        :param DeletionTaskId: Deletion task identifier, which can be used to check the status of a service-linked role deletion.
        :type DeletionTaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DeletionTaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeletionTaskId = params.get("DeletionTaskId")
        self.RequestId = params.get("RequestId")


class DeleteUserPermissionsBoundaryRequest(AbstractModel):
    """DeleteUserPermissionsBoundary request structure.

    """

    def __init__(self):
        r"""
        :param TargetUin: Sub-account `Uin`
        :type TargetUin: int
        """
        self.TargetUin = None


    def _deserialize(self, params):
        self.TargetUin = params.get("TargetUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserPermissionsBoundaryResponse(AbstractModel):
    """DeleteUserPermissionsBoundary response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteUserRequest(AbstractModel):
    """DeleteUser request structure.

    """

    def __init__(self):
        r"""
        :param Name: Sub-user username
        :type Name: str
        :param Force: Whether to forcibly delete the sub-user. The default input parameter is `0`. `0`: do not delete the user if the user has undeleted API keys; `1`: first delete the API keys then delete the user if the user has undeleted API keys. To delete API keys, you need to have cam:DeleteApiKey permission, which enables you to delete both enabled and disabled API keys. If you do not have this permission, you will not be able to delete API keys and the user.
        :type Force: int
        """
        self.Name = None
        self.Force = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserResponse(AbstractModel):
    """DeleteUser response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeOIDCConfigRequest(AbstractModel):
    """DescribeOIDCConfig request structure.

    """

    def __init__(self):
        r"""
        :param Name: Name.
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOIDCConfigResponse(AbstractModel):
    """DescribeOIDCConfig response structure.

    """

    def __init__(self):
        r"""
        :param ProviderType: IdP type. 11: Role IdP.
        :type ProviderType: int
        :param IdentityUrl: IdP URL.
        :type IdentityUrl: str
        :param IdentityKey: Public key for signature.
        :type IdentityKey: str
        :param ClientId: Client ID.
        :type ClientId: list of str
        :param Status: Status. 0: Not set; 2: Disabled; 11: Enabled.
        :type Status: int
        :param Description: Description.
        :type Description: str
        :param Name: Name.
        :type Name: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ProviderType = None
        self.IdentityUrl = None
        self.IdentityKey = None
        self.ClientId = None
        self.Status = None
        self.Description = None
        self.Name = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProviderType = params.get("ProviderType")
        self.IdentityUrl = params.get("IdentityUrl")
        self.IdentityKey = params.get("IdentityKey")
        self.ClientId = params.get("ClientId")
        self.Status = params.get("Status")
        self.Description = params.get("Description")
        self.Name = params.get("Name")
        self.RequestId = params.get("RequestId")


class DescribeRoleListRequest(AbstractModel):
    """DescribeRoleList request structure.

    """

    def __init__(self):
        r"""
        :param Page: Page number, beginning from 1
        :type Page: int
        :param Rp: Number of lines per page, no greater than 200
        :type Rp: int
        :param Tags: A parameter used to filter the list of roles under a tag.
        :type Tags: list of RoleTags
        """
        self.Page = None
        self.Rp = None
        self.Tags = None


    def _deserialize(self, params):
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = RoleTags()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoleListResponse(AbstractModel):
    """DescribeRoleList response structure.

    """

    def __init__(self):
        r"""
        :param List: Role details list
Note: This field may return null, indicating that no valid value was found.
        :type List: list of RoleInfo
        :param TotalNum: Total number of roles
        :type TotalNum: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.List = None
        self.TotalNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = RoleInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.RequestId = params.get("RequestId")


class DescribeSafeAuthFlagCollRequest(AbstractModel):
    """DescribeSafeAuthFlagColl request structure.

    """

    def __init__(self):
        r"""
        :param SubUin: Sub-account
        :type SubUin: int
        """
        self.SubUin = None


    def _deserialize(self, params):
        self.SubUin = params.get("SubUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSafeAuthFlagCollResponse(AbstractModel):
    """DescribeSafeAuthFlagColl response structure.

    """

    def __init__(self):
        r"""
        :param LoginFlag: Login protection settings
        :type LoginFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionFlag`
        :param ActionFlag: Sensitive operation protection settings
        :type ActionFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionFlag`
        :param OffsiteFlag: Suspicious login location protection settings
        :type OffsiteFlag: :class:`tencentcloud.cam.v20190116.models.OffsiteFlag`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LoginFlag = None
        self.ActionFlag = None
        self.OffsiteFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoginFlag") is not None:
            self.LoginFlag = LoginActionFlag()
            self.LoginFlag._deserialize(params.get("LoginFlag"))
        if params.get("ActionFlag") is not None:
            self.ActionFlag = LoginActionFlag()
            self.ActionFlag._deserialize(params.get("ActionFlag"))
        if params.get("OffsiteFlag") is not None:
            self.OffsiteFlag = OffsiteFlag()
            self.OffsiteFlag._deserialize(params.get("OffsiteFlag"))
        self.RequestId = params.get("RequestId")


class DescribeSafeAuthFlagIntlRequest(AbstractModel):
    """DescribeSafeAuthFlagIntl request structure.

    """


class DescribeSafeAuthFlagIntlResponse(AbstractModel):
    """DescribeSafeAuthFlagIntl response structure.

    """

    def __init__(self):
        r"""
        :param LoginFlag: Login protection settings
        :type LoginFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionFlagIntl`
        :param ActionFlag: Sensitive operation protection settings
        :type ActionFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionFlagIntl`
        :param OffsiteFlag: Suspicious login location protection settings
        :type OffsiteFlag: :class:`tencentcloud.cam.v20190116.models.OffsiteFlag`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LoginFlag = None
        self.ActionFlag = None
        self.OffsiteFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoginFlag") is not None:
            self.LoginFlag = LoginActionFlagIntl()
            self.LoginFlag._deserialize(params.get("LoginFlag"))
        if params.get("ActionFlag") is not None:
            self.ActionFlag = LoginActionFlagIntl()
            self.ActionFlag._deserialize(params.get("ActionFlag"))
        if params.get("OffsiteFlag") is not None:
            self.OffsiteFlag = OffsiteFlag()
            self.OffsiteFlag._deserialize(params.get("OffsiteFlag"))
        self.RequestId = params.get("RequestId")


class DescribeSubAccountsRequest(AbstractModel):
    """DescribeSubAccounts request structure.

    """

    def __init__(self):
        r"""
        :param FilterSubAccountUin: List of sub-user UINs. Up to 50 UINs are supported.
        :type FilterSubAccountUin: list of int non-negative
        """
        self.FilterSubAccountUin = None


    def _deserialize(self, params):
        self.FilterSubAccountUin = params.get("FilterSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubAccountsResponse(AbstractModel):
    """DescribeSubAccounts response structure.

    """

    def __init__(self):
        r"""
        :param SubAccounts: Sub-user list
        :type SubAccounts: list of SubAccountUser
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SubAccounts = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SubAccounts") is not None:
            self.SubAccounts = []
            for item in params.get("SubAccounts"):
                obj = SubAccountUser()
                obj._deserialize(item)
                self.SubAccounts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserOIDCConfigRequest(AbstractModel):
    """DescribeUserOIDCConfig request structure.

    """


class DescribeUserOIDCConfigResponse(AbstractModel):
    """DescribeUserOIDCConfig response structure.

    """

    def __init__(self):
        r"""
        :param ProviderType: IdP type. 12: user OIDC IdP
        :type ProviderType: int
        :param IdentityUrl: IdP URL
        :type IdentityUrl: str
        :param IdentityKey: Signature public key
        :type IdentityKey: str
        :param ClientId: Client ID
        :type ClientId: str
        :param Status: Status. 0: not set; 2: disabled; 11: enabled.
        :type Status: int
        :param AuthorizationEndpoint: Authorization endpoint
        :type AuthorizationEndpoint: str
        :param Scope: Authorization scope
        :type Scope: list of str
        :param ResponseType: Authorization response type
        :type ResponseType: str
        :param ResponseMode: Authorization response mode
        :type ResponseMode: str
        :param MappingFiled: Mapping field name
        :type MappingFiled: str
        :param Description: Description
        :type Description: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ProviderType = None
        self.IdentityUrl = None
        self.IdentityKey = None
        self.ClientId = None
        self.Status = None
        self.AuthorizationEndpoint = None
        self.Scope = None
        self.ResponseType = None
        self.ResponseMode = None
        self.MappingFiled = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProviderType = params.get("ProviderType")
        self.IdentityUrl = params.get("IdentityUrl")
        self.IdentityKey = params.get("IdentityKey")
        self.ClientId = params.get("ClientId")
        self.Status = params.get("Status")
        self.AuthorizationEndpoint = params.get("AuthorizationEndpoint")
        self.Scope = params.get("Scope")
        self.ResponseType = params.get("ResponseType")
        self.ResponseMode = params.get("ResponseMode")
        self.MappingFiled = params.get("MappingFiled")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class DescribeUserSAMLConfigRequest(AbstractModel):
    """DescribeUserSAMLConfig request structure.

    """


class DescribeUserSAMLConfigResponse(AbstractModel):
    """DescribeUserSAMLConfig response structure.

    """

    def __init__(self):
        r"""
        :param SAMLMetadata: SAML metadata document.
        :type SAMLMetadata: str
        :param Status: Status. `0`: not set, `1`: enabled, `2`: disabled.
        :type Status: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SAMLMetadata = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SAMLMetadata = params.get("SAMLMetadata")
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DetachGroupPolicyRequest(AbstractModel):
    """DetachGroupPolicy request structure.

    """

    def __init__(self):
        r"""
        :param PolicyId: Policy ID
        :type PolicyId: int
        :param DetachGroupId: User Group ID
        :type DetachGroupId: int
        """
        self.PolicyId = None
        self.DetachGroupId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.DetachGroupId = params.get("DetachGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachGroupPolicyResponse(AbstractModel):
    """DetachGroupPolicy response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DetachRolePolicyRequest(AbstractModel):
    """DetachRolePolicy request structure.

    """

    def __init__(self):
        r"""
        :param PolicyId: Policy ID. Either `PolicyId` or `PolicyName` must be entered
        :type PolicyId: int
        :param DetachRoleId: Role ID, used to specify a role. Input either `AttachRoleId` or `AttachRoleName`
        :type DetachRoleId: str
        :param DetachRoleName: Role name, used to specify a role. Input either `AttachRoleId` or `AttachRoleName`
        :type DetachRoleName: str
        :param PolicyName: Policy name. Either `PolicyId` or `PolicyName` must be entered
        :type PolicyName: str
        """
        self.PolicyId = None
        self.DetachRoleId = None
        self.DetachRoleName = None
        self.PolicyName = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.DetachRoleId = params.get("DetachRoleId")
        self.DetachRoleName = params.get("DetachRoleName")
        self.PolicyName = params.get("PolicyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachRolePolicyResponse(AbstractModel):
    """DetachRolePolicy response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DetachUserPolicyRequest(AbstractModel):
    """DetachUserPolicy request structure.

    """

    def __init__(self):
        r"""
        :param PolicyId: Policy ID
        :type PolicyId: int
        :param DetachUin: Sub-account UIN
        :type DetachUin: int
        """
        self.PolicyId = None
        self.DetachUin = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.DetachUin = params.get("DetachUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachUserPolicyResponse(AbstractModel):
    """DetachUserPolicy response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableUserSSORequest(AbstractModel):
    """DisableUserSSO request structure.

    """


class DisableUserSSOResponse(AbstractModel):
    """DisableUserSSO response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class GetAccountSummaryRequest(AbstractModel):
    """GetAccountSummary request structure.

    """


class GetAccountSummaryResponse(AbstractModel):
    """GetAccountSummary response structure.

    """

    def __init__(self):
        r"""
        :param Policies: Number of policies
        :type Policies: int
        :param Roles: Number of roles
        :type Roles: int
        :param Idps: Number of identity providers
        :type Idps: int
        :param User: Number of sub-accounts
        :type User: int
        :param Group: Number of groups
        :type Group: int
        :param Member: Total number of grouped users
        :type Member: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Policies = None
        self.Roles = None
        self.Idps = None
        self.User = None
        self.Group = None
        self.Member = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Policies = params.get("Policies")
        self.Roles = params.get("Roles")
        self.Idps = params.get("Idps")
        self.User = params.get("User")
        self.Group = params.get("Group")
        self.Member = params.get("Member")
        self.RequestId = params.get("RequestId")


class GetCustomMFATokenInfoRequest(AbstractModel):
    """GetCustomMFATokenInfo request structure.

    """

    def __init__(self):
        r"""
        :param MFAToken: Custom multi-factor verification Token
        :type MFAToken: str
        """
        self.MFAToken = None


    def _deserialize(self, params):
        self.MFAToken = params.get("MFAToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCustomMFATokenInfoResponse(AbstractModel):
    """GetCustomMFATokenInfo response structure.

    """

    def __init__(self):
        r"""
        :param Uin: Account ID corresponding to the custom multi-factor verification Token
        :type Uin: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Uin = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.RequestId = params.get("RequestId")


class GetGroupRequest(AbstractModel):
    """GetGroup request structure.

    """

    def __init__(self):
        r"""
        :param GroupId: User Group ID
        :type GroupId: int
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGroupResponse(AbstractModel):
    """GetGroup response structure.

    """

    def __init__(self):
        r"""
        :param GroupId: User Group ID
        :type GroupId: int
        :param GroupName: User Group name
        :type GroupName: str
        :param GroupNum: Number of members in the User Group
        :type GroupNum: int
        :param Remark: User Group description
        :type Remark: str
        :param CreateTime: Time User Group created
        :type CreateTime: str
        :param UserInfo: User Group member information
        :type UserInfo: list of GroupMemberInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.GroupId = None
        self.GroupName = None
        self.GroupNum = None
        self.Remark = None
        self.CreateTime = None
        self.UserInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.GroupNum = params.get("GroupNum")
        self.Remark = params.get("Remark")
        self.CreateTime = params.get("CreateTime")
        if params.get("UserInfo") is not None:
            self.UserInfo = []
            for item in params.get("UserInfo"):
                obj = GroupMemberInfo()
                obj._deserialize(item)
                self.UserInfo.append(obj)
        self.RequestId = params.get("RequestId")


class GetPolicyRequest(AbstractModel):
    """GetPolicy request structure.

    """

    def __init__(self):
        r"""
        :param PolicyId: Policy ID
        :type PolicyId: int
        """
        self.PolicyId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPolicyResponse(AbstractModel):
    """GetPolicy response structure.

    """

    def __init__(self):
        r"""
        :param PolicyName: Policy name
Note: This field may return null, indicating that no valid value was found.
        :type PolicyName: str
        :param Description: Policy description
Note: This field may return null, indicating that no valid value was found.
        :type Description: str
        :param Type: 1: Custom policy; 2: Preset policy
Note: This field may return null, indicating that no valid value was found.
        :type Type: int
        :param AddTime: Time created
Note: This field may return null, indicating that no valid value was found.
        :type AddTime: str
        :param UpdateTime: Time of latest update
Note: This field may return null, indicating that no valid value was found.
        :type UpdateTime: str
        :param PolicyDocument: Policy document
Note: This field may return null, indicating that no valid value was found.
        :type PolicyDocument: str
        :param PresetAlias: Remarks
Note: this field may return null, indicating that no valid values can be obtained.
        :type PresetAlias: str
        :param IsServiceLinkedRolePolicy: Whether it is a service-linked policy
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsServiceLinkedRolePolicy: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PolicyName = None
        self.Description = None
        self.Type = None
        self.AddTime = None
        self.UpdateTime = None
        self.PolicyDocument = None
        self.PresetAlias = None
        self.IsServiceLinkedRolePolicy = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyName = params.get("PolicyName")
        self.Description = params.get("Description")
        self.Type = params.get("Type")
        self.AddTime = params.get("AddTime")
        self.UpdateTime = params.get("UpdateTime")
        self.PolicyDocument = params.get("PolicyDocument")
        self.PresetAlias = params.get("PresetAlias")
        self.IsServiceLinkedRolePolicy = params.get("IsServiceLinkedRolePolicy")
        self.RequestId = params.get("RequestId")


class GetPolicyVersionRequest(AbstractModel):
    """GetPolicyVersion request structure.

    """

    def __init__(self):
        r"""
        :param PolicyId: Policy ID
        :type PolicyId: int
        :param VersionId: Policy version, which can be obtained through `ListPolicyVersions`.
        :type VersionId: int
        """
        self.PolicyId = None
        self.VersionId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPolicyVersionResponse(AbstractModel):
    """GetPolicyVersion response structure.

    """

    def __init__(self):
        r"""
        :param PolicyVersion: Policy version details
Note: this field may return null, indicating that no valid values can be obtained.
        :type PolicyVersion: :class:`tencentcloud.cam.v20190116.models.PolicyVersionDetail`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PolicyVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PolicyVersion") is not None:
            self.PolicyVersion = PolicyVersionDetail()
            self.PolicyVersion._deserialize(params.get("PolicyVersion"))
        self.RequestId = params.get("RequestId")


class GetRoleRequest(AbstractModel):
    """GetRole request structure.

    """

    def __init__(self):
        r"""
        :param RoleId: Role ID, used to specify role. Input either `RoleId` or `RoleName`
        :type RoleId: str
        :param RoleName: Role name, used to specify role. Input either `RoleId` or `RoleName`
        :type RoleName: str
        """
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRoleResponse(AbstractModel):
    """GetRole response structure.

    """

    def __init__(self):
        r"""
        :param RoleInfo: Role details
        :type RoleInfo: :class:`tencentcloud.cam.v20190116.models.RoleInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RoleInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RoleInfo") is not None:
            self.RoleInfo = RoleInfo()
            self.RoleInfo._deserialize(params.get("RoleInfo"))
        self.RequestId = params.get("RequestId")


class GetSAMLProviderRequest(AbstractModel):
    """GetSAMLProvider request structure.

    """

    def __init__(self):
        r"""
        :param Name: SAML identity provider name
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSAMLProviderResponse(AbstractModel):
    """GetSAMLProvider response structure.

    """

    def __init__(self):
        r"""
        :param Name: SAML identity provider name
        :type Name: str
        :param Description: SAML identity provider description
        :type Description: str
        :param CreateTime: Time SAML identity provider created
        :type CreateTime: str
        :param ModifyTime: Time SAML identity provider last modified
        :type ModifyTime: str
        :param SAMLMetadata: SAML identity provider metadata document
        :type SAMLMetadata: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Name = None
        self.Description = None
        self.CreateTime = None
        self.ModifyTime = None
        self.SAMLMetadata = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.SAMLMetadata = params.get("SAMLMetadata")
        self.RequestId = params.get("RequestId")


class GetSecurityLastUsedRequest(AbstractModel):
    """GetSecurityLastUsed request structure.

    """

    def __init__(self):
        r"""
        :param SecretIdList: Key ID list query. Up to 10 key IDs can be queried.
        :type SecretIdList: list of str
        """
        self.SecretIdList = None


    def _deserialize(self, params):
        self.SecretIdList = params.get("SecretIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSecurityLastUsedResponse(AbstractModel):
    """GetSecurityLastUsed response structure.

    """

    def __init__(self):
        r"""
        :param SecretIdLastUsedRows: List of key ID’s recent usage records.
        :type SecretIdLastUsedRows: list of SecretIdLastUsed
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SecretIdLastUsedRows = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecretIdLastUsedRows") is not None:
            self.SecretIdLastUsedRows = []
            for item in params.get("SecretIdLastUsedRows"):
                obj = SecretIdLastUsed()
                obj._deserialize(item)
                self.SecretIdLastUsedRows.append(obj)
        self.RequestId = params.get("RequestId")


class GetServiceLinkedRoleDeletionStatusRequest(AbstractModel):
    """GetServiceLinkedRoleDeletionStatus request structure.

    """

    def __init__(self):
        r"""
        :param DeletionTaskId: Deletion task ID
        :type DeletionTaskId: str
        """
        self.DeletionTaskId = None


    def _deserialize(self, params):
        self.DeletionTaskId = params.get("DeletionTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetServiceLinkedRoleDeletionStatusResponse(AbstractModel):
    """GetServiceLinkedRoleDeletionStatus response structure.

    """

    def __init__(self):
        r"""
        :param Status: Status: NOT_STARTED, IN_PROGRESS, SUCCEEDED, FAILED
        :type Status: str
        :param Reason: Reasons why the deletion failed.
        :type Reason: str
        :param ServiceType: Service type
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceType: str
        :param ServiceName: Service name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceName: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.Reason = None
        self.ServiceType = None
        self.ServiceName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Reason = params.get("Reason")
        self.ServiceType = params.get("ServiceType")
        self.ServiceName = params.get("ServiceName")
        self.RequestId = params.get("RequestId")


class GetUserAppIdRequest(AbstractModel):
    """GetUserAppId request structure.

    """


class GetUserAppIdResponse(AbstractModel):
    """GetUserAppId response structure.

    """

    def __init__(self):
        r"""
        :param Uin: UIN of the current account.
        :type Uin: str
        :param OwnerUin: OwnerUin of the current account.
        :type OwnerUin: str
        :param AppId: AppId of the current account.
        :type AppId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Uin = None
        self.OwnerUin = None
        self.AppId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.OwnerUin = params.get("OwnerUin")
        self.AppId = params.get("AppId")
        self.RequestId = params.get("RequestId")


class GetUserRequest(AbstractModel):
    """GetUser request structure.

    """

    def __init__(self):
        r"""
        :param Name: Sub-user username
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetUserResponse(AbstractModel):
    """GetUser response structure.

    """

    def __init__(self):
        r"""
        :param Uin: Sub-user UIN
        :type Uin: int
        :param Name: Sub-user username
        :type Name: str
        :param Uid: Sub-user UID
        :type Uid: int
        :param Remark: Sub-user remarks
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Remark: str
        :param ConsoleLogin: Whether the sub-user can log in to the console. `0`: No; `1`: Yes.
        :type ConsoleLogin: int
        :param PhoneNum: Mobile number
        :type PhoneNum: str
        :param CountryCode: Country/Area code
        :type CountryCode: str
        :param Email: Email
        :type Email: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Uin = None
        self.Name = None
        self.Uid = None
        self.Remark = None
        self.ConsoleLogin = None
        self.PhoneNum = None
        self.CountryCode = None
        self.Email = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.Uid = params.get("Uid")
        self.Remark = params.get("Remark")
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.PhoneNum = params.get("PhoneNum")
        self.CountryCode = params.get("CountryCode")
        self.Email = params.get("Email")
        self.RequestId = params.get("RequestId")


class GroupIdOfUidInfo(AbstractModel):
    """Information on the association between a sub-user and a User Group

    """

    def __init__(self):
        r"""
        :param GroupId: User Group ID
        :type GroupId: int
        :param Uid: Sub-user UID
        :type Uid: int
        :param Uin: Sub-user UIN. For UIN and UID, at least one of them is required.
        :type Uin: int
        """
        self.GroupId = None
        self.Uid = None
        self.Uin = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Uid = params.get("Uid")
        self.Uin = params.get("Uin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfo(AbstractModel):
    """User Group information

    """

    def __init__(self):
        r"""
        :param GroupId: User group ID
        :type GroupId: int
        :param GroupName: User Group name
        :type GroupName: str
        :param CreateTime: Time User Group created
        :type CreateTime: str
        :param Remark: User Group description
        :type Remark: str
        """
        self.GroupId = None
        self.GroupName = None
        self.CreateTime = None
        self.Remark = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.CreateTime = params.get("CreateTime")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupMemberInfo(AbstractModel):
    """User Group user information

    """

    def __init__(self):
        r"""
        :param Uid: Sub-user UID
        :type Uid: int
        :param Uin: Sub-user UIN
        :type Uin: int
        :param Name: Sub-user name
        :type Name: str
        :param PhoneNum: Mobile number
        :type PhoneNum: str
        :param CountryCode: Mobile number country/area code
        :type CountryCode: str
        :param PhoneFlag: Whether the mobile phone has been verified. `0`: No; `1`: Yes.
        :type PhoneFlag: int
        :param Email: Email address
        :type Email: str
        :param EmailFlag: Whether the email has been verified. `0`: No; `1`: Yes.
        :type EmailFlag: int
        :param UserType: User type. `1`: Global collaborator; `2`: Project collaborator; `3`: Message recipient.
        :type UserType: int
        :param CreateTime: Time policy created
        :type CreateTime: str
        :param IsReceiverOwner: Whether the user is the primary message recipient. `0`: No; `1`: Yes.
        :type IsReceiverOwner: int
        """
        self.Uid = None
        self.Uin = None
        self.Name = None
        self.PhoneNum = None
        self.CountryCode = None
        self.PhoneFlag = None
        self.Email = None
        self.EmailFlag = None
        self.UserType = None
        self.CreateTime = None
        self.IsReceiverOwner = None


    def _deserialize(self, params):
        self.Uid = params.get("Uid")
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.PhoneNum = params.get("PhoneNum")
        self.CountryCode = params.get("CountryCode")
        self.PhoneFlag = params.get("PhoneFlag")
        self.Email = params.get("Email")
        self.EmailFlag = params.get("EmailFlag")
        self.UserType = params.get("UserType")
        self.CreateTime = params.get("CreateTime")
        self.IsReceiverOwner = params.get("IsReceiverOwner")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAccessKeysRequest(AbstractModel):
    """ListAccessKeys request structure.

    """

    def __init__(self):
        r"""
        :param TargetUin: `UIN` of the specified user. If this parameter is left empty, access keys of the current user will be listed by default
        :type TargetUin: int
        """
        self.TargetUin = None


    def _deserialize(self, params):
        self.TargetUin = params.get("TargetUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAccessKeysResponse(AbstractModel):
    """ListAccessKeys response structure.

    """

    def __init__(self):
        r"""
        :param AccessKeys: Access key list
Note: this field may return null, indicating that no valid values can be obtained.
        :type AccessKeys: list of AccessKey
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AccessKeys = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccessKeys") is not None:
            self.AccessKeys = []
            for item in params.get("AccessKeys"):
                obj = AccessKey()
                obj._deserialize(item)
                self.AccessKeys.append(obj)
        self.RequestId = params.get("RequestId")


class ListAttachedGroupPoliciesRequest(AbstractModel):
    """ListAttachedGroupPolicies request structure.

    """

    def __init__(self):
        r"""
        :param TargetGroupId: User group ID
        :type TargetGroupId: int
        :param Page: Page number, which starts from 1. Default is 1
        :type Page: int
        :param Rp: Number of entries per page; 20 by default
        :type Rp: int
        :param Keyword: Search by keyword
        :type Keyword: str
        """
        self.TargetGroupId = None
        self.Page = None
        self.Rp = None
        self.Keyword = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAttachedGroupPoliciesResponse(AbstractModel):
    """ListAttachedGroupPolicies response structure.

    """

    def __init__(self):
        r"""
        :param TotalNum: Total number of policies
        :type TotalNum: int
        :param List: Policy list
        :type List: list of AttachPolicyInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalNum = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = AttachPolicyInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class ListAttachedRolePoliciesRequest(AbstractModel):
    """ListAttachedRolePolicies request structure.

    """

    def __init__(self):
        r"""
        :param Page: Page number, beginning from 1
        :type Page: int
        :param Rp: Number of lines per page, no more than 200
        :type Rp: int
        :param RoleId: Role ID, used to specify a role. Input either `RoleId` or `RoleName`
        :type RoleId: str
        :param RoleName: Role name, used to specify a role. Input either `RoleId` or `RoleName`
        :type RoleName: str
        :param PolicyType: Filter according to policy type. `User` indicates querying custom policies only. `QCS` indicates querying preset policies only
        :type PolicyType: str
        :param Keyword: Search by keyword
        :type Keyword: str
        """
        self.Page = None
        self.Rp = None
        self.RoleId = None
        self.RoleName = None
        self.PolicyType = None
        self.Keyword = None


    def _deserialize(self, params):
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        self.PolicyType = params.get("PolicyType")
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAttachedRolePoliciesResponse(AbstractModel):
    """ListAttachedRolePolicies response structure.

    """

    def __init__(self):
        r"""
        :param List: List of policies associated with the role
        :type List: list of AttachedPolicyOfRole
        :param TotalNum: Total number of policies associated with the role
        :type TotalNum: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.List = None
        self.TotalNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = AttachedPolicyOfRole()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.RequestId = params.get("RequestId")


class ListAttachedUserAllPoliciesRequest(AbstractModel):
    """ListAttachedUserAllPolicies request structure.

    """

    def __init__(self):
        r"""
        :param TargetUin: Target user ID.
        :type TargetUin: int
        :param Rp: The number of policies displayed on each page. Value range: 1-200.
        :type Rp: int
        :param Page: Page number. Value range: 1-200.
        :type Page: int
        :param AttachType: `0`: return policies that are directly associated and inherited from the user group; `1`: return policies that are directly associated; `2`: return policies inherited from the user group.
        :type AttachType: int
        :param StrategyType: Policy type.
        :type StrategyType: int
        :param Keyword: Keyword for searching.
        :type Keyword: str
        """
        self.TargetUin = None
        self.Rp = None
        self.Page = None
        self.AttachType = None
        self.StrategyType = None
        self.Keyword = None


    def _deserialize(self, params):
        self.TargetUin = params.get("TargetUin")
        self.Rp = params.get("Rp")
        self.Page = params.get("Page")
        self.AttachType = params.get("AttachType")
        self.StrategyType = params.get("StrategyType")
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAttachedUserAllPoliciesResponse(AbstractModel):
    """ListAttachedUserAllPolicies response structure.

    """

    def __init__(self):
        r"""
        :param PolicyList: Policy list.
        :type PolicyList: list of AttachedUserPolicy
        :param TotalNum: Total number of policies.
        :type TotalNum: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PolicyList = None
        self.TotalNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PolicyList") is not None:
            self.PolicyList = []
            for item in params.get("PolicyList"):
                obj = AttachedUserPolicy()
                obj._deserialize(item)
                self.PolicyList.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.RequestId = params.get("RequestId")


class ListAttachedUserPoliciesRequest(AbstractModel):
    """ListAttachedUserPolicies request structure.

    """

    def __init__(self):
        r"""
        :param TargetUin: Sub-account UIN
        :type TargetUin: int
        :param Page: Page number, which starts from 1. Default is 1
        :type Page: int
        :param Rp: Number of entries per page; 20 by default
        :type Rp: int
        """
        self.TargetUin = None
        self.Page = None
        self.Rp = None


    def _deserialize(self, params):
        self.TargetUin = params.get("TargetUin")
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAttachedUserPoliciesResponse(AbstractModel):
    """ListAttachedUserPolicies response structure.

    """

    def __init__(self):
        r"""
        :param TotalNum: Total number of policies
        :type TotalNum: int
        :param List: Policy list
        :type List: list of AttachPolicyInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalNum = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = AttachPolicyInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class ListCollaboratorsRequest(AbstractModel):
    """ListCollaborators request structure.

    """

    def __init__(self):
        r"""
        :param Limit: Number of entries per page. Default value: 20
        :type Limit: int
        :param Offset: Pagination start value. Default value: 0
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListCollaboratorsResponse(AbstractModel):
    """ListCollaborators response structure.

    """

    def __init__(self):
        r"""
        :param TotalNum: Total number
        :type TotalNum: int
        :param Data: Collaborator information
        :type Data: list of SubAccountInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalNum = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SubAccountInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class ListEntitiesForPolicyRequest(AbstractModel):
    """ListEntitiesForPolicy request structure.

    """

    def __init__(self):
        r"""
        :param PolicyId: Policy ID
        :type PolicyId: int
        :param Page: Page number, which starts from 1. Default is 1
        :type Page: int
        :param Rp: Number of entries per page; 20 by default
        :type Rp: int
        :param EntityFilter: Valid values: `All`, `User`, `Group`, and `Role`. `All` means all entity types will be returned; `User` means only sub-accounts will be returned; `Group` means only User Groups will be returned; `Role` means only roles will be returned. `All` is the default value.
        :type EntityFilter: str
        """
        self.PolicyId = None
        self.Page = None
        self.Rp = None
        self.EntityFilter = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")
        self.EntityFilter = params.get("EntityFilter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListEntitiesForPolicyResponse(AbstractModel):
    """ListEntitiesForPolicy response structure.

    """

    def __init__(self):
        r"""
        :param TotalNum: Number of entities
Note: This field may return null, indicating that no valid value was found.
        :type TotalNum: int
        :param List: Entity list
Note: This field may return null, indicating that no valid value was found.
        :type List: list of AttachEntityOfPolicy
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalNum = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = AttachEntityOfPolicy()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class ListGroupsForUserRequest(AbstractModel):
    """ListGroupsForUser request structure.

    """

    def __init__(self):
        r"""
        :param Uid: Sub-user UID
        :type Uid: int
        :param Rp: Number of entries per page; default is 20
        :type Rp: int
        :param Page: Page number; default is 1
        :type Page: int
        :param SubUin: Sub-account UIN
        :type SubUin: int
        """
        self.Uid = None
        self.Rp = None
        self.Page = None
        self.SubUin = None


    def _deserialize(self, params):
        self.Uid = params.get("Uid")
        self.Rp = params.get("Rp")
        self.Page = params.get("Page")
        self.SubUin = params.get("SubUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListGroupsForUserResponse(AbstractModel):
    """ListGroupsForUser response structure.

    """

    def __init__(self):
        r"""
        :param TotalNum: Total number of User Groups to which the sub-user has been added
        :type TotalNum: int
        :param GroupInfo: User Group information
        :type GroupInfo: list of GroupInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalNum = None
        self.GroupInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("GroupInfo") is not None:
            self.GroupInfo = []
            for item in params.get("GroupInfo"):
                obj = GroupInfo()
                obj._deserialize(item)
                self.GroupInfo.append(obj)
        self.RequestId = params.get("RequestId")


class ListGroupsRequest(AbstractModel):
    """ListGroups request structure.

    """

    def __init__(self):
        r"""
        :param Page: Page number; default is 1
        :type Page: int
        :param Rp: Number of entries per page; default is 20
        :type Rp: int
        :param Keyword: Filter by User Group name
        :type Keyword: str
        """
        self.Page = None
        self.Rp = None
        self.Keyword = None


    def _deserialize(self, params):
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListGroupsResponse(AbstractModel):
    """ListGroups response structure.

    """

    def __init__(self):
        r"""
        :param TotalNum: Total number of User Groups
        :type TotalNum: int
        :param GroupInfo: User group information array
        :type GroupInfo: list of GroupInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalNum = None
        self.GroupInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("GroupInfo") is not None:
            self.GroupInfo = []
            for item in params.get("GroupInfo"):
                obj = GroupInfo()
                obj._deserialize(item)
                self.GroupInfo.append(obj)
        self.RequestId = params.get("RequestId")


class ListPoliciesRequest(AbstractModel):
    """ListPolicies request structure.

    """

    def __init__(self):
        r"""
        :param Rp: Number of entries per page: must be greater than 0 and no greater than 200. Default is 20
        :type Rp: int
        :param Page: Page number. Starts from 1 and cannot be greater than 200. Default is 1
        :type Page: int
        :param Scope: Valid values: `All`, `QCS`, and `Local`. `All` means all policies will be returned; `QCS` means only preset policies will be returned; `Local` means only custom policies will be returned. `All` is the default value
        :type Scope: str
        :param Keyword: Filter by policy name
        :type Keyword: str
        """
        self.Rp = None
        self.Page = None
        self.Scope = None
        self.Keyword = None


    def _deserialize(self, params):
        self.Rp = params.get("Rp")
        self.Page = params.get("Page")
        self.Scope = params.get("Scope")
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListPoliciesResponse(AbstractModel):
    """ListPolicies response structure.

    """

    def __init__(self):
        r"""
        :param TotalNum: Total number of policies
        :type TotalNum: int
        :param List: Policy array. Each array contains fields including `policyId`, `policyName`, `addTime`, `type`, `description`, and `createMode`. 
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
        :param ServiceTypeList: Reserved field
Note: This field may return null, indicating that no valid value was found.
        :type ServiceTypeList: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalNum = None
        self.List = None
        self.ServiceTypeList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = StrategyInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.ServiceTypeList = params.get("ServiceTypeList")
        self.RequestId = params.get("RequestId")


class ListPolicyVersionsRequest(AbstractModel):
    """ListPolicyVersions request structure.

    """

    def __init__(self):
        r"""
        :param PolicyId: Policy ID
        :type PolicyId: int
        """
        self.PolicyId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListPolicyVersionsResponse(AbstractModel):
    """ListPolicyVersions response structure.

    """

    def __init__(self):
        r"""
        :param Versions: Policy version list
Note: this field may return null, indicating that no valid values can be obtained.
        :type Versions: list of PolicyVersionItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Versions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Versions") is not None:
            self.Versions = []
            for item in params.get("Versions"):
                obj = PolicyVersionItem()
                obj._deserialize(item)
                self.Versions.append(obj)
        self.RequestId = params.get("RequestId")


class ListSAMLProvidersRequest(AbstractModel):
    """ListSAMLProviders request structure.

    """


class ListSAMLProvidersResponse(AbstractModel):
    """ListSAMLProviders response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of SAML identity providers
        :type TotalCount: int
        :param SAMLProviderSet: List of SAML identity providers
        :type SAMLProviderSet: list of SAMLProviderInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.SAMLProviderSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SAMLProviderSet") is not None:
            self.SAMLProviderSet = []
            for item in params.get("SAMLProviderSet"):
                obj = SAMLProviderInfo()
                obj._deserialize(item)
                self.SAMLProviderSet.append(obj)
        self.RequestId = params.get("RequestId")


class ListUsersForGroupRequest(AbstractModel):
    """ListUsersForGroup request structure.

    """

    def __init__(self):
        r"""
        :param GroupId: User group ID
        :type GroupId: int
        :param Page: Page number; default is 1
        :type Page: int
        :param Rp: Number of entries per page; default is 20
        :type Rp: int
        """
        self.GroupId = None
        self.Page = None
        self.Rp = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUsersForGroupResponse(AbstractModel):
    """ListUsersForGroup response structure.

    """

    def __init__(self):
        r"""
        :param TotalNum: Total number of users associated with the User Group
        :type TotalNum: int
        :param UserInfo: Sub-user information
        :type UserInfo: list of GroupMemberInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalNum = None
        self.UserInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("UserInfo") is not None:
            self.UserInfo = []
            for item in params.get("UserInfo"):
                obj = GroupMemberInfo()
                obj._deserialize(item)
                self.UserInfo.append(obj)
        self.RequestId = params.get("RequestId")


class ListUsersRequest(AbstractModel):
    """ListUsers request structure.

    """


class ListUsersResponse(AbstractModel):
    """ListUsers response structure.

    """

    def __init__(self):
        r"""
        :param Data: Sub-user information
        :type Data: list of SubAccountInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SubAccountInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class LoginActionFlag(AbstractModel):
    """Login and sensitive operation flag

    """

    def __init__(self):
        r"""
        :param Phone: Phone
        :type Phone: int
        :param Token: Hard token
        :type Token: int
        :param Stoken: Soft token
        :type Stoken: int
        :param Wechat: WeChat
        :type Wechat: int
        :param Custom: Custom
        :type Custom: int
        """
        self.Phone = None
        self.Token = None
        self.Stoken = None
        self.Wechat = None
        self.Custom = None


    def _deserialize(self, params):
        self.Phone = params.get("Phone")
        self.Token = params.get("Token")
        self.Stoken = params.get("Stoken")
        self.Wechat = params.get("Wechat")
        self.Custom = params.get("Custom")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginActionFlagIntl(AbstractModel):
    """Login and sensitive operation flag

    """

    def __init__(self):
        r"""
        :param Phone: Mobile number
        :type Phone: int
        :param Token: Hard token
        :type Token: int
        :param Stoken: Soft token
        :type Stoken: int
        :param Wechat: WeChat
        :type Wechat: int
        :param Custom: Custom
        :type Custom: int
        :param Mail: Email
        :type Mail: int
        """
        self.Phone = None
        self.Token = None
        self.Stoken = None
        self.Wechat = None
        self.Custom = None
        self.Mail = None


    def _deserialize(self, params):
        self.Phone = params.get("Phone")
        self.Token = params.get("Token")
        self.Stoken = params.get("Stoken")
        self.Wechat = params.get("Wechat")
        self.Custom = params.get("Custom")
        self.Mail = params.get("Mail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginActionMfaFlag(AbstractModel):
    """Login and sensitive operation flag

    """

    def __init__(self):
        r"""
        :param Phone: Mobile phone
        :type Phone: int
        :param Stoken: Soft token
        :type Stoken: int
        :param Wechat: WeChat
        :type Wechat: int
        """
        self.Phone = None
        self.Stoken = None
        self.Wechat = None


    def _deserialize(self, params):
        self.Phone = params.get("Phone")
        self.Stoken = params.get("Stoken")
        self.Wechat = params.get("Wechat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OffsiteFlag(AbstractModel):
    """Suspicious login location settings

    """

    def __init__(self):
        r"""
        :param VerifyFlag: Verification flag
        :type VerifyFlag: int
        :param NotifyPhone: Phone notification
        :type NotifyPhone: int
        :param NotifyEmail: Email notification
        :type NotifyEmail: int
        :param NotifyWechat: WeChat notification
        :type NotifyWechat: int
        :param Tips: Alert
        :type Tips: int
        """
        self.VerifyFlag = None
        self.NotifyPhone = None
        self.NotifyEmail = None
        self.NotifyWechat = None
        self.Tips = None


    def _deserialize(self, params):
        self.VerifyFlag = params.get("VerifyFlag")
        self.NotifyPhone = params.get("NotifyPhone")
        self.NotifyEmail = params.get("NotifyEmail")
        self.NotifyWechat = params.get("NotifyWechat")
        self.Tips = params.get("Tips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolicyVersionDetail(AbstractModel):
    """Policy version details

    """

    def __init__(self):
        r"""
        :param VersionId: Policy version ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type VersionId: int
        :param CreateDate: Policy version creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateDate: str
        :param IsDefaultVersion: Whether it is the operative version. 0: no, 1: yes
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsDefaultVersion: int
        :param Document: Policy syntax text
Note: this field may return null, indicating that no valid values can be obtained.
        :type Document: str
        """
        self.VersionId = None
        self.CreateDate = None
        self.IsDefaultVersion = None
        self.Document = None


    def _deserialize(self, params):
        self.VersionId = params.get("VersionId")
        self.CreateDate = params.get("CreateDate")
        self.IsDefaultVersion = params.get("IsDefaultVersion")
        self.Document = params.get("Document")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolicyVersionItem(AbstractModel):
    """Policy version list element structure

    """

    def __init__(self):
        r"""
        :param VersionId: Policy version ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type VersionId: int
        :param CreateDate: Policy version creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateDate: str
        :param IsDefaultVersion: Whether it is the operative version. 0: no, 1: yes
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsDefaultVersion: int
        """
        self.VersionId = None
        self.CreateDate = None
        self.IsDefaultVersion = None


    def _deserialize(self, params):
        self.VersionId = params.get("VersionId")
        self.CreateDate = params.get("CreateDate")
        self.IsDefaultVersion = params.get("IsDefaultVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutRolePermissionsBoundaryRequest(AbstractModel):
    """PutRolePermissionsBoundary request structure.

    """

    def __init__(self):
        r"""
        :param PolicyId: Policy ID
        :type PolicyId: int
        :param RoleId: Role ID (either it or the role name must be entered)
        :type RoleId: str
        :param RoleName: Role name (either it or the role ID must be entered)
        :type RoleName: str
        """
        self.PolicyId = None
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutRolePermissionsBoundaryResponse(AbstractModel):
    """PutRolePermissionsBoundary response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PutUserPermissionsBoundaryRequest(AbstractModel):
    """PutUserPermissionsBoundary request structure.

    """

    def __init__(self):
        r"""
        :param TargetUin: Sub-account `Uin`
        :type TargetUin: int
        :param PolicyId: Policy ID
        :type PolicyId: int
        """
        self.TargetUin = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.TargetUin = params.get("TargetUin")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutUserPermissionsBoundaryResponse(AbstractModel):
    """PutUserPermissionsBoundary response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RemoveUserFromGroupRequest(AbstractModel):
    """RemoveUserFromGroup request structure.

    """

    def __init__(self):
        r"""
        :param Info: The user’s UIN/UID to be deleted and the array corresponding to the user group ID.
        :type Info: list of GroupIdOfUidInfo
        """
        self.Info = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = []
            for item in params.get("Info"):
                obj = GroupIdOfUidInfo()
                obj._deserialize(item)
                self.Info.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserFromGroupResponse(AbstractModel):
    """RemoveUserFromGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RoleInfo(AbstractModel):
    """Role details

    """

    def __init__(self):
        r"""
        :param RoleId: Role ID
        :type RoleId: str
        :param RoleName: Role name
        :type RoleName: str
        :param PolicyDocument: Role policy document
        :type PolicyDocument: str
        :param Description: Role description
        :type Description: str
        :param AddTime: Time role created
        :type AddTime: str
        :param UpdateTime: Time role last updated
        :type UpdateTime: str
        :param ConsoleLogin: If login is allowed for the role
        :type ConsoleLogin: int
        :param RoleType: User role. Valid values: `user`, `system`, `service_linked`
Note: this field may return null, indicating that no valid values can be obtained.
        :type RoleType: str
        :param SessionDuration: Valid period
Note: this field may return null, indicating that no valid values can be obtained.
        :type SessionDuration: int
        :param DeletionTaskId: Task identifier for deleting a service-linked role 
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeletionTaskId: str
        :param Tags: Tags.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Tags: list of RoleTags
        """
        self.RoleId = None
        self.RoleName = None
        self.PolicyDocument = None
        self.Description = None
        self.AddTime = None
        self.UpdateTime = None
        self.ConsoleLogin = None
        self.RoleType = None
        self.SessionDuration = None
        self.DeletionTaskId = None
        self.Tags = None


    def _deserialize(self, params):
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        self.PolicyDocument = params.get("PolicyDocument")
        self.Description = params.get("Description")
        self.AddTime = params.get("AddTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.RoleType = params.get("RoleType")
        self.SessionDuration = params.get("SessionDuration")
        self.DeletionTaskId = params.get("DeletionTaskId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = RoleTags()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoleTags(AbstractModel):
    """Role tag type

    """

    def __init__(self):
        r"""
        :param Key: Tag key.
        :type Key: str
        :param Value: Tag value.
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
        


class SAMLProviderInfo(AbstractModel):
    """SAML identity provider

    """

    def __init__(self):
        r"""
        :param Name: SAML identity provider name
        :type Name: str
        :param Description: SAML identity provider description
        :type Description: str
        :param CreateTime: Time SAML identity provider created
        :type CreateTime: str
        :param ModifyTime: Time SAML identity provider last modified
        :type ModifyTime: str
        """
        self.Name = None
        self.Description = None
        self.CreateTime = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecretIdLastUsed(AbstractModel):
    """The last time the key was used.

    """

    def __init__(self):
        r"""
        :param SecretId: Key ID.
        :type SecretId: str
        :param LastUsedDate: The date when the key ID was last used (the value is obtained one day later).
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type LastUsedDate: str
        """
        self.SecretId = None
        self.LastUsedDate = None


    def _deserialize(self, params):
        self.SecretId = params.get("SecretId")
        self.LastUsedDate = params.get("LastUsedDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetDefaultPolicyVersionRequest(AbstractModel):
    """SetDefaultPolicyVersion request structure.

    """

    def __init__(self):
        r"""
        :param PolicyId: Policy ID
        :type PolicyId: int
        :param VersionId: Policy version, which can be obtained through `ListPolicyVersions`.
        :type VersionId: int
        """
        self.PolicyId = None
        self.VersionId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetDefaultPolicyVersionResponse(AbstractModel):
    """SetDefaultPolicyVersion response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetMfaFlagRequest(AbstractModel):
    """SetMfaFlag request structure.

    """

    def __init__(self):
        r"""
        :param OpUin: Sets user UIN
        :type OpUin: int
        :param LoginFlag: Sets login protection
        :type LoginFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionMfaFlag`
        :param ActionFlag: Sets operation protection
        :type ActionFlag: :class:`tencentcloud.cam.v20190116.models.LoginActionMfaFlag`
        """
        self.OpUin = None
        self.LoginFlag = None
        self.ActionFlag = None


    def _deserialize(self, params):
        self.OpUin = params.get("OpUin")
        if params.get("LoginFlag") is not None:
            self.LoginFlag = LoginActionMfaFlag()
            self.LoginFlag._deserialize(params.get("LoginFlag"))
        if params.get("ActionFlag") is not None:
            self.ActionFlag = LoginActionMfaFlag()
            self.ActionFlag._deserialize(params.get("ActionFlag"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetMfaFlagResponse(AbstractModel):
    """SetMfaFlag response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StrategyInfo(AbstractModel):
    """Policy information

    """

    def __init__(self):
        r"""
        :param PolicyId: Policy ID
        :type PolicyId: int
        :param PolicyName: Policy name
        :type PolicyName: str
        :param AddTime: Time policy created
Note: This field may return null, indicating that no valid value was found.
        :type AddTime: str
        :param Type: Policy type. 1: Custom policy; 2: Preset policy
        :type Type: int
        :param Description: Policy description
Note: This field may return null, indicating that no valid value was found.
        :type Description: str
        :param CreateMode: How the policy was created: 1: Via console; 2: Via syntax
        :type CreateMode: int
        :param Attachments: Number of associated users
        :type Attachments: int
        :param ServiceType: Product associated with the policy
Note: This field may return null, indicating that no valid value was found.
        :type ServiceType: str
        :param IsAttached: This value should not be null when querying whether a marked entity has been associated with a policy. 0 indicates that no policy has been associated, while 1 indicates that a policy has been associated
        :type IsAttached: int
        :param Deactived: Queries if the policy has been deactivated
Note: this field may return null, indicating that no valid values can be obtained.
        :type Deactived: int
        :param DeactivedDetail: List of deprecated products
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeactivedDetail: list of str
        :param IsServiceLinkedPolicy: The deletion task identifier used to check the deletion status of the service-linked role
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsServiceLinkedPolicy: int
        :param AttachEntityCount: The number of entities associated with the policy.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AttachEntityCount: int
        :param AttachEntityBoundaryCount: The number of entities associated with the permission boundary.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AttachEntityBoundaryCount: int
        :param UpdateTime: The last edited time.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UpdateTime: str
        """
        self.PolicyId = None
        self.PolicyName = None
        self.AddTime = None
        self.Type = None
        self.Description = None
        self.CreateMode = None
        self.Attachments = None
        self.ServiceType = None
        self.IsAttached = None
        self.Deactived = None
        self.DeactivedDetail = None
        self.IsServiceLinkedPolicy = None
        self.AttachEntityCount = None
        self.AttachEntityBoundaryCount = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.AddTime = params.get("AddTime")
        self.Type = params.get("Type")
        self.Description = params.get("Description")
        self.CreateMode = params.get("CreateMode")
        self.Attachments = params.get("Attachments")
        self.ServiceType = params.get("ServiceType")
        self.IsAttached = params.get("IsAttached")
        self.Deactived = params.get("Deactived")
        self.DeactivedDetail = params.get("DeactivedDetail")
        self.IsServiceLinkedPolicy = params.get("IsServiceLinkedPolicy")
        self.AttachEntityCount = params.get("AttachEntityCount")
        self.AttachEntityBoundaryCount = params.get("AttachEntityBoundaryCount")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubAccountInfo(AbstractModel):
    """Sub-user information

    """

    def __init__(self):
        r"""
        :param Uin: Sub-user user ID
        :type Uin: int
        :param Name: Sub-user username
        :type Name: str
        :param Uid: Sub-user UID
        :type Uid: int
        :param Remark: Sub-user remarks
        :type Remark: str
        :param ConsoleLogin: If sub-user can log in to the console
        :type ConsoleLogin: int
        :param PhoneNum: Mobile number
        :type PhoneNum: str
        :param CountryCode: Country/Area code
        :type CountryCode: str
        :param Email: Email
        :type Email: str
        :param CreateTime: Creation time
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param NickName: Nickname.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type NickName: str
        """
        self.Uin = None
        self.Name = None
        self.Uid = None
        self.Remark = None
        self.ConsoleLogin = None
        self.PhoneNum = None
        self.CountryCode = None
        self.Email = None
        self.CreateTime = None
        self.NickName = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.Uid = params.get("Uid")
        self.Remark = params.get("Remark")
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.PhoneNum = params.get("PhoneNum")
        self.CountryCode = params.get("CountryCode")
        self.Email = params.get("Email")
        self.CreateTime = params.get("CreateTime")
        self.NickName = params.get("NickName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubAccountUser(AbstractModel):
    """Sub-user information

    """

    def __init__(self):
        r"""
        :param Uin: Sub-user ID
        :type Uin: int
        :param Name: Sub-user name
        :type Name: str
        :param Uid: Sub-user UID. UID is the unique identifier of a user who is a message recipient, while UIN is a unique identifier of a user.
        :type Uid: int
        :param Remark: Sub-user remarks
        :type Remark: str
        :param CreateTime: Creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param UserType: User type (1: root account; 2: sub-user; 3: WeCom sub-user; 4: collaborator; 5: message recipient)
        :type UserType: int
        :param LastLoginIp: 
        :type LastLoginIp: str
        :param LastLoginTime: 
        :type LastLoginTime: str
        """
        self.Uin = None
        self.Name = None
        self.Uid = None
        self.Remark = None
        self.CreateTime = None
        self.UserType = None
        self.LastLoginIp = None
        self.LastLoginTime = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.Uid = params.get("Uid")
        self.Remark = params.get("Remark")
        self.CreateTime = params.get("CreateTime")
        self.UserType = params.get("UserType")
        self.LastLoginIp = params.get("LastLoginIp")
        self.LastLoginTime = params.get("LastLoginTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagRoleRequest(AbstractModel):
    """TagRole request structure.

    """

    def __init__(self):
        r"""
        :param Tags: Tag.
        :type Tags: list of RoleTags
        :param RoleName: Role name. Specify either the role name or role ID.
        :type RoleName: str
        :param RoleId: Role ID. Specify either the role ID or role name.
        :type RoleId: str
        """
        self.Tags = None
        self.RoleName = None
        self.RoleId = None


    def _deserialize(self, params):
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = RoleTags()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RoleName = params.get("RoleName")
        self.RoleId = params.get("RoleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagRoleResponse(AbstractModel):
    """TagRole response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UntagRoleRequest(AbstractModel):
    """UntagRole request structure.

    """

    def __init__(self):
        r"""
        :param TagKeys: Tag key.
        :type TagKeys: list of str
        :param RoleName: Role name. Specify either the role name or role ID.
        :type RoleName: str
        :param RoleId: Role ID. Specify either the role ID or role name.
        :type RoleId: str
        """
        self.TagKeys = None
        self.RoleName = None
        self.RoleId = None


    def _deserialize(self, params):
        self.TagKeys = params.get("TagKeys")
        self.RoleName = params.get("RoleName")
        self.RoleId = params.get("RoleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UntagRoleResponse(AbstractModel):
    """UntagRole response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateAssumeRolePolicyRequest(AbstractModel):
    """UpdateAssumeRolePolicy request structure.

    """

    def __init__(self):
        r"""
        :param PolicyDocument: Policy document
        :type PolicyDocument: str
        :param RoleId: Role ID, used to specify a role. Input either `RoleId` or `RoleName`
        :type RoleId: str
        :param RoleName: Role name, used to specify a role. Input either `RoleId` or `RoleName`
        :type RoleName: str
        """
        self.PolicyDocument = None
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.PolicyDocument = params.get("PolicyDocument")
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAssumeRolePolicyResponse(AbstractModel):
    """UpdateAssumeRolePolicy response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateGroupRequest(AbstractModel):
    """UpdateGroup request structure.

    """

    def __init__(self):
        r"""
        :param GroupId: User Group ID
        :type GroupId: int
        :param GroupName: User Group name
        :type GroupName: str
        :param Remark: User Group description
        :type Remark: str
        """
        self.GroupId = None
        self.GroupName = None
        self.Remark = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGroupResponse(AbstractModel):
    """UpdateGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateOIDCConfigRequest(AbstractModel):
    """UpdateOIDCConfig request structure.

    """

    def __init__(self):
        r"""
        :param IdentityUrl: IdP URL.
        :type IdentityUrl: str
        :param IdentityKey: Public key for signature, which must be Base64-encoded.
        :type IdentityKey: str
        :param ClientId: Client ID.
        :type ClientId: list of str
        :param Name: Name.
        :type Name: str
        :param Description: Description.
        :type Description: str
        """
        self.IdentityUrl = None
        self.IdentityKey = None
        self.ClientId = None
        self.Name = None
        self.Description = None


    def _deserialize(self, params):
        self.IdentityUrl = params.get("IdentityUrl")
        self.IdentityKey = params.get("IdentityKey")
        self.ClientId = params.get("ClientId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOIDCConfigResponse(AbstractModel):
    """UpdateOIDCConfig response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdatePolicyRequest(AbstractModel):
    """UpdatePolicy request structure.

    """

    def __init__(self):
        r"""
        :param PolicyId: Policy ID. Either `PolicyId` or `PolicyName` must be entered
        :type PolicyId: int
        :param PolicyName: Policy name. Either `PolicyName` or `PolicyId` must be entered
        :type PolicyName: str
        :param Description: Policy description
        :type Description: str
        :param PolicyDocument: Policy documentation, for example: `{"version":"2.0","statement":[{"action":"name/sts:AssumeRole","effect":"allow","principal":{"service":["cloudaudit.cloud.tencent.com","cls.cloud.tencent.com"]}}]}`, where `principal` is used to specify the service that is authorized to use the role. For more information about this parameter, see **RoleInfo** under **Output Parameters** in the [GetRole](https://intl.cloud.tencent.com/document/product/598/36221?from_cn_redirect=1).
        :type PolicyDocument: str
        :param Alias: Preset policy remark
        :type Alias: str
        """
        self.PolicyId = None
        self.PolicyName = None
        self.Description = None
        self.PolicyDocument = None
        self.Alias = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.Description = params.get("Description")
        self.PolicyDocument = params.get("PolicyDocument")
        self.Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePolicyResponse(AbstractModel):
    """UpdatePolicy response structure.

    """

    def __init__(self):
        r"""
        :param PolicyId: Policy ID, which will be returned only if the input parameter is `PolicyName`
Note: this field may return null, indicating that no valid values can be obtained.
        :type PolicyId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.RequestId = params.get("RequestId")


class UpdateRoleConsoleLoginRequest(AbstractModel):
    """UpdateRoleConsoleLogin request structure.

    """

    def __init__(self):
        r"""
        :param ConsoleLogin: Whether login is allowed. 1: yes, 0: no
        :type ConsoleLogin: int
        :param RoleId: Role ID. Use either `RoleId` or `RoleName` as the input parameter.
        :type RoleId: int
        :param RoleName: Role name. Use either `RoleId` or `RoleName` as the input parameter.
        :type RoleName: str
        """
        self.ConsoleLogin = None
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRoleConsoleLoginResponse(AbstractModel):
    """UpdateRoleConsoleLogin response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateRoleDescriptionRequest(AbstractModel):
    """UpdateRoleDescription request structure.

    """

    def __init__(self):
        r"""
        :param Description: Role description
        :type Description: str
        :param RoleId: Role ID, used to specify a role. Input either `RoleId` or `RoleName`
        :type RoleId: str
        :param RoleName: Role name, used to specify a role. Input either `RoleId` or `RoleName`
        :type RoleName: str
        """
        self.Description = None
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.Description = params.get("Description")
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRoleDescriptionResponse(AbstractModel):
    """UpdateRoleDescription response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateSAMLProviderRequest(AbstractModel):
    """UpdateSAMLProvider request structure.

    """

    def __init__(self):
        r"""
        :param Name: SAML identity provider name
        :type Name: str
        :param Description: SAML identity provider description
        :type Description: str
        :param SAMLMetadataDocument: SAML identity provider metadata document (Base64)
        :type SAMLMetadataDocument: str
        """
        self.Name = None
        self.Description = None
        self.SAMLMetadataDocument = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.SAMLMetadataDocument = params.get("SAMLMetadataDocument")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateSAMLProviderResponse(AbstractModel):
    """UpdateSAMLProvider response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateUserOIDCConfigRequest(AbstractModel):
    """UpdateUserOIDCConfig request structure.

    """

    def __init__(self):
        r"""
        :param IdentityUrl: OpenID Connect IdP URL.
It corresponds to the value of the `issuer` field in the `Openid-configuration` provided by the enterprise IdP.
        :type IdentityUrl: str
        :param IdentityKey: Signature public key, which is used to verify the OpenID Connect IdP's ID token and must be Base64-encoded. For the security of your account, we recommend you rotate it regularly.
        :type IdentityKey: str
        :param ClientId: Client ID registered with the OpenID Connect IdP.
        :type ClientId: str
        :param AuthorizationEndpoint: OpenID Connect IdP authorization endpoint. It corresponds to the value of the `authorization_endpoint` field in the `Openid-configuration` provided by the enterprise IdP.
        :type AuthorizationEndpoint: str
        :param ResponseType: Authorization response type, which is always `id_token`.
        :type ResponseType: str
        :param ResponseMode: Authorization response mode. Valid values: form_post (recommended); fragment.
        :type ResponseMode: str
        :param MappingFiled: Mapping field name. It indicates which field in the `id_token` of the IdP is mapped to the username of a sub-user. It is usually the `sub` or `name` field
        :type MappingFiled: str
        :param Scope: Authorization information scope. Valid values: openid (default); email; profile.
        :type Scope: list of str
        :param Description: Description
        :type Description: str
        """
        self.IdentityUrl = None
        self.IdentityKey = None
        self.ClientId = None
        self.AuthorizationEndpoint = None
        self.ResponseType = None
        self.ResponseMode = None
        self.MappingFiled = None
        self.Scope = None
        self.Description = None


    def _deserialize(self, params):
        self.IdentityUrl = params.get("IdentityUrl")
        self.IdentityKey = params.get("IdentityKey")
        self.ClientId = params.get("ClientId")
        self.AuthorizationEndpoint = params.get("AuthorizationEndpoint")
        self.ResponseType = params.get("ResponseType")
        self.ResponseMode = params.get("ResponseMode")
        self.MappingFiled = params.get("MappingFiled")
        self.Scope = params.get("Scope")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserOIDCConfigResponse(AbstractModel):
    """UpdateUserOIDCConfig response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateUserRequest(AbstractModel):
    """UpdateUser request structure.

    """

    def __init__(self):
        r"""
        :param Name: Sub-user username
        :type Name: str
        :param Remark: Sub-user remarks
        :type Remark: str
        :param ConsoleLogin: Whether or not the sub-user is allowed to log in to the console. 0: No; 1: Yes.
        :type ConsoleLogin: int
        :param Password: Sub-user's console login password. If no password rules have been set, the password must have a minimum of 8 characters containing uppercase letters, lowercase letters, digits, and special characters by default. This parameter will be valid only when the sub-user is allowed to log in to the console. If it is not specified and console login is allowed, the system will automatically generate a random 32-character password that contains uppercase letters, lowercase letters, digits, and special characters.
        :type Password: str
        :param NeedResetPassword: If the sub-user needs to reset their password when they next log in to the console. 0: No; 1: Yes.
        :type NeedResetPassword: int
        :param PhoneNum: Mobile number
        :type PhoneNum: str
        :param CountryCode: Country/Area Code
        :type CountryCode: str
        :param Email: Email
        :type Email: str
        """
        self.Name = None
        self.Remark = None
        self.ConsoleLogin = None
        self.Password = None
        self.NeedResetPassword = None
        self.PhoneNum = None
        self.CountryCode = None
        self.Email = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.Password = params.get("Password")
        self.NeedResetPassword = params.get("NeedResetPassword")
        self.PhoneNum = params.get("PhoneNum")
        self.CountryCode = params.get("CountryCode")
        self.Email = params.get("Email")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserResponse(AbstractModel):
    """UpdateUser response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateUserSAMLConfigRequest(AbstractModel):
    """UpdateUserSAMLConfig request structure.

    """

    def __init__(self):
        r"""
        :param Operate: Type of the modification operation. `enable`: enable, `disable`: disable, `updateSAML`: modify metadata document.
        :type Operate: str
        :param SAMLMetadataDocument: Metadata document, which must be Base64 encoded. This parameter is required only when the value of `Operate` is `updateSAML`.
        :type SAMLMetadataDocument: str
        """
        self.Operate = None
        self.SAMLMetadataDocument = None


    def _deserialize(self, params):
        self.Operate = params.get("Operate")
        self.SAMLMetadataDocument = params.get("SAMLMetadataDocument")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserSAMLConfigResponse(AbstractModel):
    """UpdateUserSAMLConfig response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")