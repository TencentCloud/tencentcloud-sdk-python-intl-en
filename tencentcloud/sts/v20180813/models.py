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


class AssumeRoleRequest(AbstractModel):
    """AssumeRole request structure.

    """

    def __init__(self):
        r"""
        :param RoleArn: Resource descriptions of a role, which can be obtained by clicking the role name in the [CAM console](https://console.cloud.tencent.com/cam/role).
General role:
qcs::cam::uin/12345678:role/4611686018427397919, qcs::cam::uin/12345678:roleName/testRoleName
Service role:
qcs::cam::uin/12345678:role/tencentcloudServiceRole/4611686018427397920, qcs::cam::uin/12345678:role/tencentcloudServiceRoleName/testServiceRoleName
        :type RoleArn: str
        :param RoleSessionName: User-defined temporary session name.
It can contain 2-128 letters, digits, and symbols (=,.@_-). Regex: [\w+=,.@_-]*
        :type RoleSessionName: str
        :param DurationSeconds: Specifies the validity period of credentials in seconds. Default value: 7200. Maximum value: 43200
        :type DurationSeconds: int
        :param Policy: Policy description
Note:
1. The policy needs to be URL-encoded (if you request a TencentCloud API through the GET method, all parameters must be URL-encoded again in accordance with [Signature v3](https://intl.cloud.tencent.com/document/api/598/33159?from_cn_redirect=1#1.-.E6.8B.BC.E6.8E.A5.E8.A7.84.E8.8C.83.E8.AF.B7.E6.B1.82.E4.B8.B2) before the request is sent).
2. For the policy syntax, please see CAM's [Syntax Logic](https://intl.cloud.tencent.com/document/product/598/10603?from_cn_redirect=1).
3. The policy cannot contain the `principal` element.
        :type Policy: str
        :param ExternalId: External role ID, which can be obtained by clicking the role name in the [CAM console](https://console.cloud.tencent.com/cam/role).
It can contain 2-128 letters, digits, and symbols (=,.@:/-). Regex: [\w+=,.@:\/-]*
        :type ExternalId: str
        :param Tags: List of session tags. Up to 50 tags are allowed. The tag keys can not duplicate.
        :type Tags: list of Tag
        """
        self.RoleArn = None
        self.RoleSessionName = None
        self.DurationSeconds = None
        self.Policy = None
        self.ExternalId = None
        self.Tags = None


    def _deserialize(self, params):
        self.RoleArn = params.get("RoleArn")
        self.RoleSessionName = params.get("RoleSessionName")
        self.DurationSeconds = params.get("DurationSeconds")
        self.Policy = params.get("Policy")
        self.ExternalId = params.get("ExternalId")
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
        


class AssumeRoleResponse(AbstractModel):
    """AssumeRole response structure.

    """

    def __init__(self):
        r"""
        :param Credentials: Temporary security credentials
        :type Credentials: :class:`tencentcloud.sts.v20180813.models.Credentials`
        :param ExpiredTime: Credentials expiration time. A Unix timestamp will be returned which is accurate to the second
        :type ExpiredTime: int
        :param Expiration: Credentials expiration time in UTC time in ISO 8601 format.
        :type Expiration: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Credentials = None
        self.ExpiredTime = None
        self.Expiration = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Credentials") is not None:
            self.Credentials = Credentials()
            self.Credentials._deserialize(params.get("Credentials"))
        self.ExpiredTime = params.get("ExpiredTime")
        self.Expiration = params.get("Expiration")
        self.RequestId = params.get("RequestId")


class AssumeRoleWithSAMLRequest(AbstractModel):
    """AssumeRoleWithSAML request structure.

    """

    def __init__(self):
        r"""
        :param SAMLAssertion: Base64-encoded SAML assertion
        :type SAMLAssertion: str
        :param PrincipalArn: Principal access description name
        :type PrincipalArn: str
        :param RoleArn: Role access description name
        :type RoleArn: str
        :param RoleSessionName: Session name
        :type RoleSessionName: str
        :param DurationSeconds: The validity period of the temporary credentials in seconds. Default value: 7,200s. Maximum value: 43,200s.
        :type DurationSeconds: int
        """
        self.SAMLAssertion = None
        self.PrincipalArn = None
        self.RoleArn = None
        self.RoleSessionName = None
        self.DurationSeconds = None


    def _deserialize(self, params):
        self.SAMLAssertion = params.get("SAMLAssertion")
        self.PrincipalArn = params.get("PrincipalArn")
        self.RoleArn = params.get("RoleArn")
        self.RoleSessionName = params.get("RoleSessionName")
        self.DurationSeconds = params.get("DurationSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssumeRoleWithSAMLResponse(AbstractModel):
    """AssumeRoleWithSAML response structure.

    """

    def __init__(self):
        r"""
        :param Credentials: An object consists of the `Token`, `TmpSecretId`, and `TmpSecretId`
        :type Credentials: :class:`tencentcloud.sts.v20180813.models.Credentials`
        :param ExpiredTime: Credentials expiration time. A Unix timestamp will be returned which is accurate to the second
        :type ExpiredTime: int
        :param Expiration: Credentials expiration time in UTC time in ISO 8601 format.
        :type Expiration: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Credentials = None
        self.ExpiredTime = None
        self.Expiration = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Credentials") is not None:
            self.Credentials = Credentials()
            self.Credentials._deserialize(params.get("Credentials"))
        self.ExpiredTime = params.get("ExpiredTime")
        self.Expiration = params.get("Expiration")
        self.RequestId = params.get("RequestId")


class AssumeRoleWithWebIdentityRequest(AbstractModel):
    """AssumeRoleWithWebIdentity request structure.

    """

    def __init__(self):
        r"""
        :param ProviderId: Identity provider name
        :type ProviderId: str
        :param WebIdentityToken: OIDC token issued by the IdP
        :type WebIdentityToken: str
        :param RoleArn: Role access description name
        :type RoleArn: str
        :param RoleSessionName: Session name
        :type RoleSessionName: str
        :param DurationSeconds: The validity period of the temporary credential in seconds. Default value: 7,200s. Maximum value: 43,200s.
        :type DurationSeconds: int
        """
        self.ProviderId = None
        self.WebIdentityToken = None
        self.RoleArn = None
        self.RoleSessionName = None
        self.DurationSeconds = None


    def _deserialize(self, params):
        self.ProviderId = params.get("ProviderId")
        self.WebIdentityToken = params.get("WebIdentityToken")
        self.RoleArn = params.get("RoleArn")
        self.RoleSessionName = params.get("RoleSessionName")
        self.DurationSeconds = params.get("DurationSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssumeRoleWithWebIdentityResponse(AbstractModel):
    """AssumeRoleWithWebIdentity response structure.

    """

    def __init__(self):
        r"""
        :param ExpiredTime: Expiration time of the temporary credential (timestamp)
        :type ExpiredTime: int
        :param Expiration: Expiration time of the temporary credential
        :type Expiration: str
        :param Credentials: Temporary credential
        :type Credentials: :class:`tencentcloud.sts.v20180813.models.Credentials`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ExpiredTime = None
        self.Expiration = None
        self.Credentials = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ExpiredTime = params.get("ExpiredTime")
        self.Expiration = params.get("Expiration")
        if params.get("Credentials") is not None:
            self.Credentials = Credentials()
            self.Credentials._deserialize(params.get("Credentials"))
        self.RequestId = params.get("RequestId")


class Credentials(AbstractModel):
    """Temporary credentials

    """

    def __init__(self):
        r"""
        :param Token: Token, which contains up to 4,096 bytes depending on the associated policies.
        :type Token: str
        :param TmpSecretId: Temporary credentials key ID, which contains up to 1,024 bytes.
        :type TmpSecretId: str
        :param TmpSecretKey: Temporary credentials key, which contains up to 1,024 bytes.
        :type TmpSecretKey: str
        """
        self.Token = None
        self.TmpSecretId = None
        self.TmpSecretKey = None


    def _deserialize(self, params):
        self.Token = params.get("Token")
        self.TmpSecretId = params.get("TmpSecretId")
        self.TmpSecretKey = params.get("TmpSecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCallerIdentityRequest(AbstractModel):
    """GetCallerIdentity request structure.

    """


class GetCallerIdentityResponse(AbstractModel):
    """GetCallerIdentity response structure.

    """

    def __init__(self):
        r"""
        :param Arn: ARN of the current caller.
        :type Arn: str
        :param AccountId: Root account UIN of the current caller.
        :type AccountId: str
        :param UserId: User ID.
1. If the caller is a Tencent Cloud account, the UIN of the current account is returned.
2. If the caller is a role, `roleId:roleSessionName` is returned.
3. If the caller is a federated user, `uin:federatedUserName` is returned.
        :type UserId: str
        :param PrincipalId: Account UIN.
1. If the caller is a Tencent Cloud account, the UIN of the current account is returned.
2. If the caller is a role, the UIN of the account that applies for the role is returned.
        :type PrincipalId: str
        :param Type: Identity type.
        :type Type: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Arn = None
        self.AccountId = None
        self.UserId = None
        self.PrincipalId = None
        self.Type = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Arn = params.get("Arn")
        self.AccountId = params.get("AccountId")
        self.UserId = params.get("UserId")
        self.PrincipalId = params.get("PrincipalId")
        self.Type = params.get("Type")
        self.RequestId = params.get("RequestId")


class GetFederationTokenRequest(AbstractModel):
    """GetFederationToken request structure.

    """

    def __init__(self):
        r"""
        :param Name: The customizable name of the caller, consisting of letters
        :type Name: str
        :param Policy: Policy description
Note:
1. The policy needs to be URL-encoded (if you request a TencentCloud API through the GET method, all parameters must be URL-encoded again in accordance with [Signature v3](https://intl.cloud.tencent.com/document/api/598/33159?from_cn_redirect=1#1.-.E6.8B.BC.E6.8E.A5.E8.A7.84.E8.8C.83.E8.AF.B7.E6.B1.82.E4.B8.B2) before the request is sent).
2. For the policy syntax, please see CAM's [Syntax Logic](https://intl.cloud.tencent.com/document/product/598/10603?from_cn_redirect=1).
3. The policy cannot contain the `principal` element.
        :type Policy: str
        :param DurationSeconds: The validity period of temporary credentials in seconds. Default value: 1,800s. Maximum value for a root account: 7,200s. Maximum value for a sub-account: 129,600s.
        :type DurationSeconds: int
        """
        self.Name = None
        self.Policy = None
        self.DurationSeconds = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Policy = params.get("Policy")
        self.DurationSeconds = params.get("DurationSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFederationTokenResponse(AbstractModel):
    """GetFederationToken response structure.

    """

    def __init__(self):
        r"""
        :param Credentials: Temporary credentials
        :type Credentials: :class:`tencentcloud.sts.v20180813.models.Credentials`
        :param ExpiredTime: Temporary credentials expiration time. A Unix timestamp will be returned which is accurate to the second
        :type ExpiredTime: int
        :param Expiration: Credentials expiration time in UTC time in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Expiration: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Credentials = None
        self.ExpiredTime = None
        self.Expiration = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Credentials") is not None:
            self.Credentials = Credentials()
            self.Credentials._deserialize(params.get("Credentials"))
        self.ExpiredTime = params.get("ExpiredTime")
        self.Expiration = params.get("Expiration")
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """Information on tags

    """

    def __init__(self):
        r"""
        :param Key: Tag key. It’s up to 128 characters and case-sensitive.
        :type Key: str
        :param Value: Tag value. It’s up to 256 characters and case-sensitive.
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
        