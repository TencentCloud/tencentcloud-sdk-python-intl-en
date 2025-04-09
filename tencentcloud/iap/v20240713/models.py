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


class CreateIAPUserOIDCConfigRequest(AbstractModel):
    """CreateIAPUserOIDCConfig request structure.

    """

    def __init__(self):
        r"""
        :param _IdentityUrl: OpenID Connect IdP URL. It corresponds to the value of the "issuer" field in the Openid-configuration provided by the enterprise IdP.
        :type IdentityUrl: str
        :param _ClientId: Client ID registered with the OpenID Connect IdP.
        :type ClientId: str
        :param _AuthorizationEndpoint: OpenID Connect IdP authorization endpoint. It corresponds to the value of the "authorization_endpoint" field in the Openid-configuration provided by the enterprise IdP.
        :type AuthorizationEndpoint: str
        :param _ResponseType: Authorization response type, which is always id_token.
        :type ResponseType: str
        :param _ResponseMode: Authorization response mode. Valid values: form_post (recommended); fragment.
        :type ResponseMode: str
        :param _MappingFiled: Mapping field name. It indicates which field in the id_token of the IdP is mapped to the username of a sub-user. It is usually the sub or name field.
        :type MappingFiled: str
        :param _IdentityKey: Signature public key, which is used to verify the OpenID Connect IdP's ID token and must be Base64-encoded. For the security of your account, we recommend you rotate it regularly.
        :type IdentityKey: str
        :param _Scope: Authorization information scope. Valid values: openid (default); email; profile.
        :type Scope: list of str
        :param _Description: Description
        :type Description: str
        """
        self._IdentityUrl = None
        self._ClientId = None
        self._AuthorizationEndpoint = None
        self._ResponseType = None
        self._ResponseMode = None
        self._MappingFiled = None
        self._IdentityKey = None
        self._Scope = None
        self._Description = None

    @property
    def IdentityUrl(self):
        """OpenID Connect IdP URL. It corresponds to the value of the "issuer" field in the Openid-configuration provided by the enterprise IdP.
        :rtype: str
        """
        return self._IdentityUrl

    @IdentityUrl.setter
    def IdentityUrl(self, IdentityUrl):
        self._IdentityUrl = IdentityUrl

    @property
    def ClientId(self):
        """Client ID registered with the OpenID Connect IdP.
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def AuthorizationEndpoint(self):
        """OpenID Connect IdP authorization endpoint. It corresponds to the value of the "authorization_endpoint" field in the Openid-configuration provided by the enterprise IdP.
        :rtype: str
        """
        return self._AuthorizationEndpoint

    @AuthorizationEndpoint.setter
    def AuthorizationEndpoint(self, AuthorizationEndpoint):
        self._AuthorizationEndpoint = AuthorizationEndpoint

    @property
    def ResponseType(self):
        """Authorization response type, which is always id_token.
        :rtype: str
        """
        return self._ResponseType

    @ResponseType.setter
    def ResponseType(self, ResponseType):
        self._ResponseType = ResponseType

    @property
    def ResponseMode(self):
        """Authorization response mode. Valid values: form_post (recommended); fragment.
        :rtype: str
        """
        return self._ResponseMode

    @ResponseMode.setter
    def ResponseMode(self, ResponseMode):
        self._ResponseMode = ResponseMode

    @property
    def MappingFiled(self):
        """Mapping field name. It indicates which field in the id_token of the IdP is mapped to the username of a sub-user. It is usually the sub or name field.
        :rtype: str
        """
        return self._MappingFiled

    @MappingFiled.setter
    def MappingFiled(self, MappingFiled):
        self._MappingFiled = MappingFiled

    @property
    def IdentityKey(self):
        """Signature public key, which is used to verify the OpenID Connect IdP's ID token and must be Base64-encoded. For the security of your account, we recommend you rotate it regularly.
        :rtype: str
        """
        return self._IdentityKey

    @IdentityKey.setter
    def IdentityKey(self, IdentityKey):
        self._IdentityKey = IdentityKey

    @property
    def Scope(self):
        """Authorization information scope. Valid values: openid (default); email; profile.
        :rtype: list of str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def Description(self):
        """Description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._IdentityUrl = params.get("IdentityUrl")
        self._ClientId = params.get("ClientId")
        self._AuthorizationEndpoint = params.get("AuthorizationEndpoint")
        self._ResponseType = params.get("ResponseType")
        self._ResponseMode = params.get("ResponseMode")
        self._MappingFiled = params.get("MappingFiled")
        self._IdentityKey = params.get("IdentityKey")
        self._Scope = params.get("Scope")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIAPUserOIDCConfigResponse(AbstractModel):
    """CreateIAPUserOIDCConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeIAPLoginSessionDurationRequest(AbstractModel):
    """DescribeIAPLoginSessionDuration request structure.

    """


class DescribeIAPLoginSessionDurationResponse(AbstractModel):
    """DescribeIAPLoginSessionDuration response structure.

    """

    def __init__(self):
        r"""
        :param _Duration: Login session duration.
        :type Duration: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Duration = None
        self._RequestId = None

    @property
    def Duration(self):
        """Login session duration.
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Duration = params.get("Duration")
        self._RequestId = params.get("RequestId")


class DescribeIAPUserOIDCConfigRequest(AbstractModel):
    """DescribeIAPUserOIDCConfig request structure.

    """


class DescribeIAPUserOIDCConfigResponse(AbstractModel):
    """DescribeIAPUserOIDCConfig response structure.

    """

    def __init__(self):
        r"""
        :param _ProviderType: IdP type. 13: IAP user OIDC IdP.
        :type ProviderType: int
        :param _IdentityUrl: IdP URL.
        :type IdentityUrl: str
        :param _IdentityKey: Public key for signature.
        :type IdentityKey: str
        :param _ClientId: Client ID.
        :type ClientId: str
        :param _Status: Status. 0: Not set; 2: Disabled; 11: Enabled.
        :type Status: int
        :param _Fingerprints: The verification fingerprint of the HTTPS CA certificate. English letters and digits are allowed, and each fingerprint is 40 characters long, with a maximum of 5 fingerprints.
        :type Fingerprints: list of str
        :param _EnableAutoPublicKey: Whether to enable the automatic use of the OIDC signature public key. 1: Yes, 2: No (default).
        :type EnableAutoPublicKey: int
        :param _AuthorizationEndpoint: Authorization endpoint.
        :type AuthorizationEndpoint: str
        :param _Scope: Authorization scope.
        :type Scope: list of str
        :param _ResponseType: Authorization response type.
        :type ResponseType: str
        :param _ResponseMode: Authorization response mode.
        :type ResponseMode: str
        :param _MappingFiled: Mapping field name.
        :type MappingFiled: str
        :param _Description: Description
        :type Description: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProviderType = None
        self._IdentityUrl = None
        self._IdentityKey = None
        self._ClientId = None
        self._Status = None
        self._Fingerprints = None
        self._EnableAutoPublicKey = None
        self._AuthorizationEndpoint = None
        self._Scope = None
        self._ResponseType = None
        self._ResponseMode = None
        self._MappingFiled = None
        self._Description = None
        self._RequestId = None

    @property
    def ProviderType(self):
        """IdP type. 13: IAP user OIDC IdP.
        :rtype: int
        """
        return self._ProviderType

    @ProviderType.setter
    def ProviderType(self, ProviderType):
        self._ProviderType = ProviderType

    @property
    def IdentityUrl(self):
        """IdP URL.
        :rtype: str
        """
        return self._IdentityUrl

    @IdentityUrl.setter
    def IdentityUrl(self, IdentityUrl):
        self._IdentityUrl = IdentityUrl

    @property
    def IdentityKey(self):
        """Public key for signature.
        :rtype: str
        """
        return self._IdentityKey

    @IdentityKey.setter
    def IdentityKey(self, IdentityKey):
        self._IdentityKey = IdentityKey

    @property
    def ClientId(self):
        """Client ID.
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def Status(self):
        """Status. 0: Not set; 2: Disabled; 11: Enabled.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Fingerprints(self):
        """The verification fingerprint of the HTTPS CA certificate. English letters and digits are allowed, and each fingerprint is 40 characters long, with a maximum of 5 fingerprints.
        :rtype: list of str
        """
        return self._Fingerprints

    @Fingerprints.setter
    def Fingerprints(self, Fingerprints):
        self._Fingerprints = Fingerprints

    @property
    def EnableAutoPublicKey(self):
        """Whether to enable the automatic use of the OIDC signature public key. 1: Yes, 2: No (default).
        :rtype: int
        """
        return self._EnableAutoPublicKey

    @EnableAutoPublicKey.setter
    def EnableAutoPublicKey(self, EnableAutoPublicKey):
        self._EnableAutoPublicKey = EnableAutoPublicKey

    @property
    def AuthorizationEndpoint(self):
        """Authorization endpoint.
        :rtype: str
        """
        return self._AuthorizationEndpoint

    @AuthorizationEndpoint.setter
    def AuthorizationEndpoint(self, AuthorizationEndpoint):
        self._AuthorizationEndpoint = AuthorizationEndpoint

    @property
    def Scope(self):
        """Authorization scope.
        :rtype: list of str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def ResponseType(self):
        """Authorization response type.
        :rtype: str
        """
        return self._ResponseType

    @ResponseType.setter
    def ResponseType(self, ResponseType):
        self._ResponseType = ResponseType

    @property
    def ResponseMode(self):
        """Authorization response mode.
        :rtype: str
        """
        return self._ResponseMode

    @ResponseMode.setter
    def ResponseMode(self, ResponseMode):
        self._ResponseMode = ResponseMode

    @property
    def MappingFiled(self):
        """Mapping field name.
        :rtype: str
        """
        return self._MappingFiled

    @MappingFiled.setter
    def MappingFiled(self, MappingFiled):
        self._MappingFiled = MappingFiled

    @property
    def Description(self):
        """Description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
        self._Fingerprints = params.get("Fingerprints")
        self._EnableAutoPublicKey = params.get("EnableAutoPublicKey")
        self._AuthorizationEndpoint = params.get("AuthorizationEndpoint")
        self._Scope = params.get("Scope")
        self._ResponseType = params.get("ResponseType")
        self._ResponseMode = params.get("ResponseMode")
        self._MappingFiled = params.get("MappingFiled")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class DisableIAPUserSSORequest(AbstractModel):
    """DisableIAPUserSSO request structure.

    """


class DisableIAPUserSSOResponse(AbstractModel):
    """DisableIAPUserSSO response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyIAPLoginSessionDurationRequest(AbstractModel):
    """ModifyIAPLoginSessionDuration request structure.

    """

    def __init__(self):
        r"""
        :param _Duration: Login session duration.
        :type Duration: int
        """
        self._Duration = None

    @property
    def Duration(self):
        """Login session duration.
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration


    def _deserialize(self, params):
        self._Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIAPLoginSessionDurationResponse(AbstractModel):
    """ModifyIAPLoginSessionDuration response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateIAPUserOIDCConfigRequest(AbstractModel):
    """UpdateIAPUserOIDCConfig request structure.

    """

    def __init__(self):
        r"""
        :param _IdentityUrl: OpenID Connect IdP URL. It corresponds to the value of the "issuer" field in the Openid-configuration provided by the enterprise IdP.
        :type IdentityUrl: str
        :param _ClientId: Client ID registered with the OpenID Connect IdP.
        :type ClientId: str
        :param _AuthorizationEndpoint: OpenID Connect IdP authorization endpoint. It corresponds to the value of the "authorization_endpoint" field in the Openid-configuration provided by the enterprise IdP.
        :type AuthorizationEndpoint: str
        :param _ResponseType: Authorization response type, which is always id_token.
        :type ResponseType: str
        :param _ResponseMode: Authorization response mode. Valid values: form_post (recommended); fragment.
        :type ResponseMode: str
        :param _MappingFiled: Mapping field name. It indicates which field in the id_token of the IdP is mapped to the username of a sub-user. It is usually the sub or name field.
        :type MappingFiled: str
        :param _IdentityKey: RSA signature public key in the JWKS format, which is used to verify the OpenID Connect IdP's ID token and must be Base64-encoded. For the security of your account, we recommend you rotate it regularly.
        :type IdentityKey: str
        :param _Scope: Authorization information scope. Valid values: openid (default); email; profile.
        :type Scope: list of str
        :param _Description: Description, with a length of 1 to 255 English or Chinese characters. It is empty by default.
        :type Description: str
        """
        self._IdentityUrl = None
        self._ClientId = None
        self._AuthorizationEndpoint = None
        self._ResponseType = None
        self._ResponseMode = None
        self._MappingFiled = None
        self._IdentityKey = None
        self._Scope = None
        self._Description = None

    @property
    def IdentityUrl(self):
        """OpenID Connect IdP URL. It corresponds to the value of the "issuer" field in the Openid-configuration provided by the enterprise IdP.
        :rtype: str
        """
        return self._IdentityUrl

    @IdentityUrl.setter
    def IdentityUrl(self, IdentityUrl):
        self._IdentityUrl = IdentityUrl

    @property
    def ClientId(self):
        """Client ID registered with the OpenID Connect IdP.
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def AuthorizationEndpoint(self):
        """OpenID Connect IdP authorization endpoint. It corresponds to the value of the "authorization_endpoint" field in the Openid-configuration provided by the enterprise IdP.
        :rtype: str
        """
        return self._AuthorizationEndpoint

    @AuthorizationEndpoint.setter
    def AuthorizationEndpoint(self, AuthorizationEndpoint):
        self._AuthorizationEndpoint = AuthorizationEndpoint

    @property
    def ResponseType(self):
        """Authorization response type, which is always id_token.
        :rtype: str
        """
        return self._ResponseType

    @ResponseType.setter
    def ResponseType(self, ResponseType):
        self._ResponseType = ResponseType

    @property
    def ResponseMode(self):
        """Authorization response mode. Valid values: form_post (recommended); fragment.
        :rtype: str
        """
        return self._ResponseMode

    @ResponseMode.setter
    def ResponseMode(self, ResponseMode):
        self._ResponseMode = ResponseMode

    @property
    def MappingFiled(self):
        """Mapping field name. It indicates which field in the id_token of the IdP is mapped to the username of a sub-user. It is usually the sub or name field.
        :rtype: str
        """
        return self._MappingFiled

    @MappingFiled.setter
    def MappingFiled(self, MappingFiled):
        self._MappingFiled = MappingFiled

    @property
    def IdentityKey(self):
        """RSA signature public key in the JWKS format, which is used to verify the OpenID Connect IdP's ID token and must be Base64-encoded. For the security of your account, we recommend you rotate it regularly.
        :rtype: str
        """
        return self._IdentityKey

    @IdentityKey.setter
    def IdentityKey(self, IdentityKey):
        self._IdentityKey = IdentityKey

    @property
    def Scope(self):
        """Authorization information scope. Valid values: openid (default); email; profile.
        :rtype: list of str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def Description(self):
        """Description, with a length of 1 to 255 English or Chinese characters. It is empty by default.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._IdentityUrl = params.get("IdentityUrl")
        self._ClientId = params.get("ClientId")
        self._AuthorizationEndpoint = params.get("AuthorizationEndpoint")
        self._ResponseType = params.get("ResponseType")
        self._ResponseMode = params.get("ResponseMode")
        self._MappingFiled = params.get("MappingFiled")
        self._IdentityKey = params.get("IdentityKey")
        self._Scope = params.get("Scope")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateIAPUserOIDCConfigResponse(AbstractModel):
    """UpdateIAPUserOIDCConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")