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
        :param _RoleArn: Resource descriptions of a role, which can be obtained by clicking the role name in the [CAM console](https://console.cloud.tencent.com/cam/role).
General role:
qcs::cam::uin/12345678:role/4611686018427397919, qcs::cam::uin/12345678:roleName/testRoleName
Service role:
qcs::cam::uin/12345678:role/tencentcloudServiceRole/4611686018427397920, qcs::cam::uin/12345678:role/tencentcloudServiceRoleName/testServiceRoleName
        :type RoleArn: str
        :param _RoleSessionName: User-defined temporary session name.
It can contain 2-128 letters, digits, and symbols (=,.@_-). Regex: [\w+=,.@_-]*
        :type RoleSessionName: str
        :param _DurationSeconds: Specifies the validity period of credentials in seconds. Default value: 7200. Maximum value: 43200
        :type DurationSeconds: int
        :param _Policy: Policy description
Note:
1. The policy needs to be URL-encoded (if you request a TencentCloud API through the GET method, all parameters must be URL-encoded again in accordance with [Signature v3](https://intl.cloud.tencent.com/document/api/598/33159?from_cn_redirect=1#1.-.E6.8B.BC.E6.8E.A5.E8.A7.84.E8.8C.83.E8.AF.B7.E6.B1.82.E4.B8.B2) before the request is sent).
2. For the policy syntax, please see CAM's [Syntax Logic](https://intl.cloud.tencent.com/document/product/598/10603?from_cn_redirect=1).
3. The policy cannot contain the `principal` element.
        :type Policy: str
        :param _ExternalId: External role ID, which can be obtained by clicking the role name in the [CAM console](https://console.cloud.tencent.com/cam/role).
It can contain 2-128 letters, digits, and symbols (=,.@:/-). Regex: [\w+=,.@:\/-]*
        :type ExternalId: str
        :param _Tags: List of session tags. Up to 50 tags are allowed. The tag keys can not duplicate.
        :type Tags: list of Tag
        :param _SourceIdentity: UIN of the initiator
        :type SourceIdentity: str
        """
        self._RoleArn = None
        self._RoleSessionName = None
        self._DurationSeconds = None
        self._Policy = None
        self._ExternalId = None
        self._Tags = None
        self._SourceIdentity = None

    @property
    def RoleArn(self):
        """Resource descriptions of a role, which can be obtained by clicking the role name in the [CAM console](https://console.cloud.tencent.com/cam/role).
General role:
qcs::cam::uin/12345678:role/4611686018427397919, qcs::cam::uin/12345678:roleName/testRoleName
Service role:
qcs::cam::uin/12345678:role/tencentcloudServiceRole/4611686018427397920, qcs::cam::uin/12345678:role/tencentcloudServiceRoleName/testServiceRoleName
        :rtype: str
        """
        return self._RoleArn

    @RoleArn.setter
    def RoleArn(self, RoleArn):
        self._RoleArn = RoleArn

    @property
    def RoleSessionName(self):
        """User-defined temporary session name.
It can contain 2-128 letters, digits, and symbols (=,.@_-). Regex: [\w+=,.@_-]*
        :rtype: str
        """
        return self._RoleSessionName

    @RoleSessionName.setter
    def RoleSessionName(self, RoleSessionName):
        self._RoleSessionName = RoleSessionName

    @property
    def DurationSeconds(self):
        """Specifies the validity period of credentials in seconds. Default value: 7200. Maximum value: 43200
        :rtype: int
        """
        return self._DurationSeconds

    @DurationSeconds.setter
    def DurationSeconds(self, DurationSeconds):
        self._DurationSeconds = DurationSeconds

    @property
    def Policy(self):
        """Policy description
Note:
1. The policy needs to be URL-encoded (if you request a TencentCloud API through the GET method, all parameters must be URL-encoded again in accordance with [Signature v3](https://intl.cloud.tencent.com/document/api/598/33159?from_cn_redirect=1#1.-.E6.8B.BC.E6.8E.A5.E8.A7.84.E8.8C.83.E8.AF.B7.E6.B1.82.E4.B8.B2) before the request is sent).
2. For the policy syntax, please see CAM's [Syntax Logic](https://intl.cloud.tencent.com/document/product/598/10603?from_cn_redirect=1).
3. The policy cannot contain the `principal` element.
        :rtype: str
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def ExternalId(self):
        """External role ID, which can be obtained by clicking the role name in the [CAM console](https://console.cloud.tencent.com/cam/role).
It can contain 2-128 letters, digits, and symbols (=,.@:/-). Regex: [\w+=,.@:\/-]*
        :rtype: str
        """
        return self._ExternalId

    @ExternalId.setter
    def ExternalId(self, ExternalId):
        self._ExternalId = ExternalId

    @property
    def Tags(self):
        """List of session tags. Up to 50 tags are allowed. The tag keys can not duplicate.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SourceIdentity(self):
        """UIN of the initiator
        :rtype: str
        """
        return self._SourceIdentity

    @SourceIdentity.setter
    def SourceIdentity(self, SourceIdentity):
        self._SourceIdentity = SourceIdentity


    def _deserialize(self, params):
        self._RoleArn = params.get("RoleArn")
        self._RoleSessionName = params.get("RoleSessionName")
        self._DurationSeconds = params.get("DurationSeconds")
        self._Policy = params.get("Policy")
        self._ExternalId = params.get("ExternalId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._SourceIdentity = params.get("SourceIdentity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssumeRoleResponse(AbstractModel):
    """AssumeRole response structure.

    """

    def __init__(self):
        r"""
        :param _Credentials: Temporary security credentials
        :type Credentials: :class:`tencentcloud.sts.v20180813.models.Credentials`
        :param _ExpiredTime: Credentials expiration time. A Unix timestamp will be returned which is accurate to the second
        :type ExpiredTime: int
        :param _Expiration: Credentials expiration time in UTC time in ISO 8601 format.
        :type Expiration: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Credentials = None
        self._ExpiredTime = None
        self._Expiration = None
        self._RequestId = None

    @property
    def Credentials(self):
        """Temporary security credentials
        :rtype: :class:`tencentcloud.sts.v20180813.models.Credentials`
        """
        return self._Credentials

    @Credentials.setter
    def Credentials(self, Credentials):
        self._Credentials = Credentials

    @property
    def ExpiredTime(self):
        """Credentials expiration time. A Unix timestamp will be returned which is accurate to the second
        :rtype: int
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def Expiration(self):
        """Credentials expiration time in UTC time in ISO 8601 format.
        :rtype: str
        """
        return self._Expiration

    @Expiration.setter
    def Expiration(self, Expiration):
        self._Expiration = Expiration

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Credentials") is not None:
            self._Credentials = Credentials()
            self._Credentials._deserialize(params.get("Credentials"))
        self._ExpiredTime = params.get("ExpiredTime")
        self._Expiration = params.get("Expiration")
        self._RequestId = params.get("RequestId")


class AssumeRoleWithSAMLRequest(AbstractModel):
    """AssumeRoleWithSAML request structure.

    """

    def __init__(self):
        r"""
        :param _SAMLAssertion: Base64-encoded SAML assertion
        :type SAMLAssertion: str
        :param _PrincipalArn: Principal access description name
        :type PrincipalArn: str
        :param _RoleArn: Role access description name
        :type RoleArn: str
        :param _RoleSessionName: Session name
        :type RoleSessionName: str
        :param _DurationSeconds: The validity period of the temporary credentials in seconds. Default value: 7,200s. Maximum value: 43,200s.
        :type DurationSeconds: int
        """
        self._SAMLAssertion = None
        self._PrincipalArn = None
        self._RoleArn = None
        self._RoleSessionName = None
        self._DurationSeconds = None

    @property
    def SAMLAssertion(self):
        """Base64-encoded SAML assertion
        :rtype: str
        """
        return self._SAMLAssertion

    @SAMLAssertion.setter
    def SAMLAssertion(self, SAMLAssertion):
        self._SAMLAssertion = SAMLAssertion

    @property
    def PrincipalArn(self):
        """Principal access description name
        :rtype: str
        """
        return self._PrincipalArn

    @PrincipalArn.setter
    def PrincipalArn(self, PrincipalArn):
        self._PrincipalArn = PrincipalArn

    @property
    def RoleArn(self):
        """Role access description name
        :rtype: str
        """
        return self._RoleArn

    @RoleArn.setter
    def RoleArn(self, RoleArn):
        self._RoleArn = RoleArn

    @property
    def RoleSessionName(self):
        """Session name
        :rtype: str
        """
        return self._RoleSessionName

    @RoleSessionName.setter
    def RoleSessionName(self, RoleSessionName):
        self._RoleSessionName = RoleSessionName

    @property
    def DurationSeconds(self):
        """The validity period of the temporary credentials in seconds. Default value: 7,200s. Maximum value: 43,200s.
        :rtype: int
        """
        return self._DurationSeconds

    @DurationSeconds.setter
    def DurationSeconds(self, DurationSeconds):
        self._DurationSeconds = DurationSeconds


    def _deserialize(self, params):
        self._SAMLAssertion = params.get("SAMLAssertion")
        self._PrincipalArn = params.get("PrincipalArn")
        self._RoleArn = params.get("RoleArn")
        self._RoleSessionName = params.get("RoleSessionName")
        self._DurationSeconds = params.get("DurationSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssumeRoleWithSAMLResponse(AbstractModel):
    """AssumeRoleWithSAML response structure.

    """

    def __init__(self):
        r"""
        :param _Credentials: An object consists of the `Token`, `TmpSecretId`, and `TmpSecretId`
        :type Credentials: :class:`tencentcloud.sts.v20180813.models.Credentials`
        :param _ExpiredTime: Credentials expiration time. A Unix timestamp will be returned which is accurate to the second
        :type ExpiredTime: int
        :param _Expiration: Credentials expiration time in UTC time in ISO 8601 format.
        :type Expiration: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Credentials = None
        self._ExpiredTime = None
        self._Expiration = None
        self._RequestId = None

    @property
    def Credentials(self):
        """An object consists of the `Token`, `TmpSecretId`, and `TmpSecretId`
        :rtype: :class:`tencentcloud.sts.v20180813.models.Credentials`
        """
        return self._Credentials

    @Credentials.setter
    def Credentials(self, Credentials):
        self._Credentials = Credentials

    @property
    def ExpiredTime(self):
        """Credentials expiration time. A Unix timestamp will be returned which is accurate to the second
        :rtype: int
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def Expiration(self):
        """Credentials expiration time in UTC time in ISO 8601 format.
        :rtype: str
        """
        return self._Expiration

    @Expiration.setter
    def Expiration(self, Expiration):
        self._Expiration = Expiration

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Credentials") is not None:
            self._Credentials = Credentials()
            self._Credentials._deserialize(params.get("Credentials"))
        self._ExpiredTime = params.get("ExpiredTime")
        self._Expiration = params.get("Expiration")
        self._RequestId = params.get("RequestId")


class AssumeRoleWithWebIdentityRequest(AbstractModel):
    """AssumeRoleWithWebIdentity request structure.

    """

    def __init__(self):
        r"""
        :param _ProviderId: Identity provider name
        :type ProviderId: str
        :param _WebIdentityToken: OIDC token issued by the IdP
        :type WebIdentityToken: str
        :param _RoleArn: Role access description name
        :type RoleArn: str
        :param _RoleSessionName: Session name
        :type RoleSessionName: str
        :param _DurationSeconds: The validity period of the temporary credential in seconds. Default value: 7,200s. Maximum value: 43,200s.
        :type DurationSeconds: int
        """
        self._ProviderId = None
        self._WebIdentityToken = None
        self._RoleArn = None
        self._RoleSessionName = None
        self._DurationSeconds = None

    @property
    def ProviderId(self):
        """Identity provider name
        :rtype: str
        """
        return self._ProviderId

    @ProviderId.setter
    def ProviderId(self, ProviderId):
        self._ProviderId = ProviderId

    @property
    def WebIdentityToken(self):
        """OIDC token issued by the IdP
        :rtype: str
        """
        return self._WebIdentityToken

    @WebIdentityToken.setter
    def WebIdentityToken(self, WebIdentityToken):
        self._WebIdentityToken = WebIdentityToken

    @property
    def RoleArn(self):
        """Role access description name
        :rtype: str
        """
        return self._RoleArn

    @RoleArn.setter
    def RoleArn(self, RoleArn):
        self._RoleArn = RoleArn

    @property
    def RoleSessionName(self):
        """Session name
        :rtype: str
        """
        return self._RoleSessionName

    @RoleSessionName.setter
    def RoleSessionName(self, RoleSessionName):
        self._RoleSessionName = RoleSessionName

    @property
    def DurationSeconds(self):
        """The validity period of the temporary credential in seconds. Default value: 7,200s. Maximum value: 43,200s.
        :rtype: int
        """
        return self._DurationSeconds

    @DurationSeconds.setter
    def DurationSeconds(self, DurationSeconds):
        self._DurationSeconds = DurationSeconds


    def _deserialize(self, params):
        self._ProviderId = params.get("ProviderId")
        self._WebIdentityToken = params.get("WebIdentityToken")
        self._RoleArn = params.get("RoleArn")
        self._RoleSessionName = params.get("RoleSessionName")
        self._DurationSeconds = params.get("DurationSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssumeRoleWithWebIdentityResponse(AbstractModel):
    """AssumeRoleWithWebIdentity response structure.

    """

    def __init__(self):
        r"""
        :param _ExpiredTime: Expiration time of the temporary credential (timestamp)
        :type ExpiredTime: int
        :param _Expiration: Expiration time of the temporary credential
        :type Expiration: str
        :param _Credentials: Temporary credential
        :type Credentials: :class:`tencentcloud.sts.v20180813.models.Credentials`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ExpiredTime = None
        self._Expiration = None
        self._Credentials = None
        self._RequestId = None

    @property
    def ExpiredTime(self):
        """Expiration time of the temporary credential (timestamp)
        :rtype: int
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def Expiration(self):
        """Expiration time of the temporary credential
        :rtype: str
        """
        return self._Expiration

    @Expiration.setter
    def Expiration(self, Expiration):
        self._Expiration = Expiration

    @property
    def Credentials(self):
        """Temporary credential
        :rtype: :class:`tencentcloud.sts.v20180813.models.Credentials`
        """
        return self._Credentials

    @Credentials.setter
    def Credentials(self, Credentials):
        self._Credentials = Credentials

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ExpiredTime = params.get("ExpiredTime")
        self._Expiration = params.get("Expiration")
        if params.get("Credentials") is not None:
            self._Credentials = Credentials()
            self._Credentials._deserialize(params.get("Credentials"))
        self._RequestId = params.get("RequestId")


class Credentials(AbstractModel):
    """Temporary credentials

    """

    def __init__(self):
        r"""
        :param _Token: Token, which contains up to 4,096 bytes depending on the associated policies.
        :type Token: str
        :param _TmpSecretId: Temporary credentials key ID, which contains up to 1,024 bytes.
        :type TmpSecretId: str
        :param _TmpSecretKey: Temporary credentials key, which contains up to 1,024 bytes.
        :type TmpSecretKey: str
        """
        self._Token = None
        self._TmpSecretId = None
        self._TmpSecretKey = None

    @property
    def Token(self):
        """Token, which contains up to 4,096 bytes depending on the associated policies.
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def TmpSecretId(self):
        """Temporary credentials key ID, which contains up to 1,024 bytes.
        :rtype: str
        """
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        """Temporary credentials key, which contains up to 1,024 bytes.
        :rtype: str
        """
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey


    def _deserialize(self, params):
        self._Token = params.get("Token")
        self._TmpSecretId = params.get("TmpSecretId")
        self._TmpSecretKey = params.get("TmpSecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
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
        :param _Arn: ARN of the current caller.
        :type Arn: str
        :param _AccountId: Root account UIN of the current caller.
        :type AccountId: str
        :param _UserId: User ID.
1. If the caller is a Tencent Cloud account, the UIN of the current account is returned.
2. If the caller is a role, `roleId:roleSessionName` is returned.
3. If the caller is a federated user, `uin:federatedUserName` is returned.
        :type UserId: str
        :param _PrincipalId: Account UIN.
1. If the caller is a Tencent Cloud account, the UIN of the current account is returned.
2. If the caller is a role, the UIN of the account that applies for the role is returned.
        :type PrincipalId: str
        :param _Type: Identity type.
        :type Type: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Arn = None
        self._AccountId = None
        self._UserId = None
        self._PrincipalId = None
        self._Type = None
        self._RequestId = None

    @property
    def Arn(self):
        """ARN of the current caller.
        :rtype: str
        """
        return self._Arn

    @Arn.setter
    def Arn(self, Arn):
        self._Arn = Arn

    @property
    def AccountId(self):
        """Root account UIN of the current caller.
        :rtype: str
        """
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId

    @property
    def UserId(self):
        """User ID.
1. If the caller is a Tencent Cloud account, the UIN of the current account is returned.
2. If the caller is a role, `roleId:roleSessionName` is returned.
3. If the caller is a federated user, `uin:federatedUserName` is returned.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PrincipalId(self):
        """Account UIN.
1. If the caller is a Tencent Cloud account, the UIN of the current account is returned.
2. If the caller is a role, the UIN of the account that applies for the role is returned.
        :rtype: str
        """
        return self._PrincipalId

    @PrincipalId.setter
    def PrincipalId(self, PrincipalId):
        self._PrincipalId = PrincipalId

    @property
    def Type(self):
        """Identity type.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Arn = params.get("Arn")
        self._AccountId = params.get("AccountId")
        self._UserId = params.get("UserId")
        self._PrincipalId = params.get("PrincipalId")
        self._Type = params.get("Type")
        self._RequestId = params.get("RequestId")


class GetFederationTokenRequest(AbstractModel):
    """GetFederationToken request structure.

    """

    def __init__(self):
        r"""
        :param _Name: The customizable name of the caller, consisting of letters
        :type Name: str
        :param _Policy: Policy description
Note:
1. The policy needs to be URL-encoded (if you request a TencentCloud API through the GET method, all parameters must be URL-encoded again in accordance with [Signature v3](https://intl.cloud.tencent.com/document/api/598/33159?from_cn_redirect=1#1.-.E6.8B.BC.E6.8E.A5.E8.A7.84.E8.8C.83.E8.AF.B7.E6.B1.82.E4.B8.B2) before the request is sent).
2. For the policy syntax, please see CAM's [Syntax Logic](https://intl.cloud.tencent.com/document/product/598/10603?from_cn_redirect=1).
3. The policy cannot contain the `principal` element.
        :type Policy: str
        :param _DurationSeconds: The validity period of temporary credentials in seconds. Default value: 1,800s. Maximum value for a root account: 7,200s. Maximum value for a sub-account: 129,600s.
        :type DurationSeconds: int
        """
        self._Name = None
        self._Policy = None
        self._DurationSeconds = None

    @property
    def Name(self):
        """The customizable name of the caller, consisting of letters
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Policy(self):
        """Policy description
Note:
1. The policy needs to be URL-encoded (if you request a TencentCloud API through the GET method, all parameters must be URL-encoded again in accordance with [Signature v3](https://intl.cloud.tencent.com/document/api/598/33159?from_cn_redirect=1#1.-.E6.8B.BC.E6.8E.A5.E8.A7.84.E8.8C.83.E8.AF.B7.E6.B1.82.E4.B8.B2) before the request is sent).
2. For the policy syntax, please see CAM's [Syntax Logic](https://intl.cloud.tencent.com/document/product/598/10603?from_cn_redirect=1).
3. The policy cannot contain the `principal` element.
        :rtype: str
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def DurationSeconds(self):
        """The validity period of temporary credentials in seconds. Default value: 1,800s. Maximum value for a root account: 7,200s. Maximum value for a sub-account: 129,600s.
        :rtype: int
        """
        return self._DurationSeconds

    @DurationSeconds.setter
    def DurationSeconds(self, DurationSeconds):
        self._DurationSeconds = DurationSeconds


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Policy = params.get("Policy")
        self._DurationSeconds = params.get("DurationSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFederationTokenResponse(AbstractModel):
    """GetFederationToken response structure.

    """

    def __init__(self):
        r"""
        :param _Credentials: Temporary credentials
        :type Credentials: :class:`tencentcloud.sts.v20180813.models.Credentials`
        :param _ExpiredTime: Temporary credentials expiration time. A Unix timestamp will be returned which is accurate to the second
        :type ExpiredTime: int
        :param _Expiration: Credentials expiration time in UTC time in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Expiration: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Credentials = None
        self._ExpiredTime = None
        self._Expiration = None
        self._RequestId = None

    @property
    def Credentials(self):
        """Temporary credentials
        :rtype: :class:`tencentcloud.sts.v20180813.models.Credentials`
        """
        return self._Credentials

    @Credentials.setter
    def Credentials(self, Credentials):
        self._Credentials = Credentials

    @property
    def ExpiredTime(self):
        """Temporary credentials expiration time. A Unix timestamp will be returned which is accurate to the second
        :rtype: int
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def Expiration(self):
        """Credentials expiration time in UTC time in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Expiration

    @Expiration.setter
    def Expiration(self, Expiration):
        self._Expiration = Expiration

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Credentials") is not None:
            self._Credentials = Credentials()
            self._Credentials._deserialize(params.get("Credentials"))
        self._ExpiredTime = params.get("ExpiredTime")
        self._Expiration = params.get("Expiration")
        self._RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """Information on tags

    """

    def __init__(self):
        r"""
        :param _Key: Tag key. It’s up to 128 characters and case-sensitive.
        :type Key: str
        :param _Value: Tag value. It’s up to 256 characters and case-sensitive.
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """Tag key. It’s up to 128 characters and case-sensitive.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """Tag value. It’s up to 256 characters and case-sensitive.
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
        