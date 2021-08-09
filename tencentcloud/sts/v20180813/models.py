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
        """
        :param RoleArn: Role resource description, such as qcs::cam::uin/12345678:role/4611686018427397919, qcs::cam::uin/12345678:roleName/testRoleName\n        :type RoleArn: str\n        :param RoleSessionName: User-defined temporary session name\n        :type RoleSessionName: str\n        :param DurationSeconds: Specifies the validity period of credentials in seconds. Default value: 7200. Maximum value: 43200\n        :type DurationSeconds: int\n        :param Policy: Policy description
Note:
1. The policy needs to be URL-encoded (if you request a TencentCloud API through the GET method, all parameters must be URL-encoded again in accordance with [Signature v3](https://cloud.tencent.com/document/api/598/33159#1.-.E6.8B.BC.E6.8E.A5.E8.A7.84.E8.8C.83.E8.AF.B7.E6.B1.82.E4.B8.B2) before the request is sent).
2. For the policy syntax, please see CAM’s [Syntax Logic](https://cloud.tencent.com/document/product/598/10603).
3. The policy cannot contain the `principal` element.\n        :type Policy: str\n        """
        self.RoleArn = None
        self.RoleSessionName = None
        self.DurationSeconds = None
        self.Policy = None


    def _deserialize(self, params):
        self.RoleArn = params.get("RoleArn")
        self.RoleSessionName = params.get("RoleSessionName")
        self.DurationSeconds = params.get("DurationSeconds")
        self.Policy = params.get("Policy")
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
        """
        :param Credentials: Temporary security credentials\n        :type Credentials: :class:`tencentcloud.sts.v20180813.models.Credentials`\n        :param ExpiredTime: Credentials expiration time. A Unix timestamp will be returned which is accurate to the second\n        :type ExpiredTime: int\n        :param Expiration: Credentials expiration time in UTC time in ISO 8601 format.\n        :type Expiration: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param SAMLAssertion: Base64-encoded SAML assertion\n        :type SAMLAssertion: str\n        :param PrincipalArn: Principal access description name\n        :type PrincipalArn: str\n        :param RoleArn: Role access description name\n        :type RoleArn: str\n        :param RoleSessionName: Session name\n        :type RoleSessionName: str\n        :param DurationSeconds: Specifies the validity period of credentials in seconds. Default value: 7200. Maximum value: 7200\n        :type DurationSeconds: int\n        """
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
        """
        :param Credentials: An object consists of the `Token`, `TmpSecretId`, and `TmpSecretId`\n        :type Credentials: :class:`tencentcloud.sts.v20180813.models.Credentials`\n        :param ExpiredTime: Credentials expiration time. A Unix timestamp will be returned which is accurate to the second\n        :type ExpiredTime: int\n        :param Expiration: Credentials expiration time in UTC time in ISO 8601 format.\n        :type Expiration: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class Credentials(AbstractModel):
    """Temporary credentials

    """

    def __init__(self):
        """
        :param Token: token\n        :type Token: str\n        :param TmpSecretId: Temporary credentials secret ID\n        :type TmpSecretId: str\n        :param TmpSecretKey: Temporary credentials secret key\n        :type TmpSecretKey: str\n        """
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
        


class GetFederationTokenRequest(AbstractModel):
    """GetFederationToken request structure.

    """

    def __init__(self):
        """
        :param Name: The customizable name of the caller, consisting of letters\n        :type Name: str\n        :param Policy: Policy description
Note:
1. The policy needs to be URL-encoded (if you request a TencentCloud API through the GET method, all parameters must be URL-encoded again in accordance with [Signature v3](https://cloud.tencent.com/document/api/598/33159#1.-.E6.8B.BC.E6.8E.A5.E8.A7.84.E8.8C.83.E8.AF.B7.E6.B1.82.E4.B8.B2) before the request is sent).
2. For the policy syntax, please see CAM’s [Syntax Logic](https://cloud.tencent.com/document/product/598/10603).
3. The policy cannot contain the `principal` element.\n        :type Policy: str\n        :param DurationSeconds: Specifies the validity period of credentials in seconds. Default value: 1800. Maximum value: 7200\n        :type DurationSeconds: int\n        """
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
        """
        :param Credentials: Temporary credentials\n        :type Credentials: :class:`tencentcloud.sts.v20180813.models.Credentials`\n        :param ExpiredTime: Temporary credentials expiration time. A Unix timestamp will be returned which is accurate to the second\n        :type ExpiredTime: int\n        :param Expiration: Credentials expiration time in UTC time in ISO 8601 format.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Expiration: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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