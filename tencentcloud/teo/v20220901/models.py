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


class AccelerateMainland(AbstractModel):
    """Cross-MLC-border acceleration.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable Cross-MLC-border acceleration. Valid values: 
<li>`on`: Enable;</li>
<li>`off`: Disable.</li>
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccelerateType(AbstractModel):
    """Acceleration type

    """

    def __init__(self):
        r"""
        :param _Switch: Acceleration switch. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccelerationDomain(AbstractModel):
    """Accelerated domain name

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site.
        :type ZoneId: str
        :param _DomainName: Accelerated domain name
        :type DomainName: str
        :param _DomainStatus: Status of the accelerated domain name. Values:
<li>`online`: Activated</li>
<li>`process`: Being deployed</li>
<li>`offline`: Disabled</li>
<li>`forbidden`: Blocked</li>
<li>`init`: Pending activation</li>
        :type DomainStatus: str
        :param _OriginDetail: Details of the origin.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginDetail: :class:`tencentcloud.teo.v20220901.models.OriginDetail`
        :param _OriginProtocol: Origin-pull protocol configuration. Values:
<li>`FOLLOW`: Follow the protocol of origin</li>
<li>`HTTP`: Send requests to the origin over HTTP</li>
<li>`HTTPS`: Send requests to the origin over HTTPS</li>
Note: This field may return·null, indicating that no valid values can be obtained.
        :type OriginProtocol: str
        :param _HttpOriginPort: The port used for HTTP origin-pull requests
Note: This field may return·null, indicating that no valid values can be obtained.
        :type HttpOriginPort: int
        :param _HttpsOriginPort: The port used for HTTPS origin-pull requests
Note: This field may return·null, indicating that no valid values can be obtained.
        :type HttpsOriginPort: int
        :param _IPv6Status: IPv6 status. Values:
<li>`follow`: Follow the IPv6 configuration of the site</li>
<li>`on`: Enable</li>
<li>`off`: Disable</li>
Note: This field may return·null, indicating that no valid values can be obtained.
        :type IPv6Status: str
        :param _Cname: The CNAME address.
        :type Cname: str
        :param _IdentificationStatus: Ownership verification status. Values: <li>`pending`: Pending verification</li> <li>`finished`: Verified</li>	
Note: This field may return null, indicating that no valid values can be obtained.
        :type IdentificationStatus: str
        :param _CreatedOn: Creation time of the accelerated domain name.
        :type CreatedOn: str
        :param _ModifiedOn: Modification time of the accelerated domain name.
        :type ModifiedOn: str
        :param _OwnershipVerification: Information required to verify the ownership of a domain name.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type OwnershipVerification: :class:`tencentcloud.teo.v20220901.models.OwnershipVerification`
        :param _Certificate: Domain name certificate information
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Certificate: :class:`tencentcloud.teo.v20220901.models.AccelerationDomainCertificate`
        """
        self._ZoneId = None
        self._DomainName = None
        self._DomainStatus = None
        self._OriginDetail = None
        self._OriginProtocol = None
        self._HttpOriginPort = None
        self._HttpsOriginPort = None
        self._IPv6Status = None
        self._Cname = None
        self._IdentificationStatus = None
        self._CreatedOn = None
        self._ModifiedOn = None
        self._OwnershipVerification = None
        self._Certificate = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def DomainStatus(self):
        return self._DomainStatus

    @DomainStatus.setter
    def DomainStatus(self, DomainStatus):
        self._DomainStatus = DomainStatus

    @property
    def OriginDetail(self):
        return self._OriginDetail

    @OriginDetail.setter
    def OriginDetail(self, OriginDetail):
        self._OriginDetail = OriginDetail

    @property
    def OriginProtocol(self):
        return self._OriginProtocol

    @OriginProtocol.setter
    def OriginProtocol(self, OriginProtocol):
        self._OriginProtocol = OriginProtocol

    @property
    def HttpOriginPort(self):
        return self._HttpOriginPort

    @HttpOriginPort.setter
    def HttpOriginPort(self, HttpOriginPort):
        self._HttpOriginPort = HttpOriginPort

    @property
    def HttpsOriginPort(self):
        return self._HttpsOriginPort

    @HttpsOriginPort.setter
    def HttpsOriginPort(self, HttpsOriginPort):
        self._HttpsOriginPort = HttpsOriginPort

    @property
    def IPv6Status(self):
        return self._IPv6Status

    @IPv6Status.setter
    def IPv6Status(self, IPv6Status):
        self._IPv6Status = IPv6Status

    @property
    def Cname(self):
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def IdentificationStatus(self):
        return self._IdentificationStatus

    @IdentificationStatus.setter
    def IdentificationStatus(self, IdentificationStatus):
        self._IdentificationStatus = IdentificationStatus

    @property
    def CreatedOn(self):
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def ModifiedOn(self):
        return self._ModifiedOn

    @ModifiedOn.setter
    def ModifiedOn(self, ModifiedOn):
        self._ModifiedOn = ModifiedOn

    @property
    def OwnershipVerification(self):
        return self._OwnershipVerification

    @OwnershipVerification.setter
    def OwnershipVerification(self, OwnershipVerification):
        self._OwnershipVerification = OwnershipVerification

    @property
    def Certificate(self):
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._DomainName = params.get("DomainName")
        self._DomainStatus = params.get("DomainStatus")
        if params.get("OriginDetail") is not None:
            self._OriginDetail = OriginDetail()
            self._OriginDetail._deserialize(params.get("OriginDetail"))
        self._OriginProtocol = params.get("OriginProtocol")
        self._HttpOriginPort = params.get("HttpOriginPort")
        self._HttpsOriginPort = params.get("HttpsOriginPort")
        self._IPv6Status = params.get("IPv6Status")
        self._Cname = params.get("Cname")
        self._IdentificationStatus = params.get("IdentificationStatus")
        self._CreatedOn = params.get("CreatedOn")
        self._ModifiedOn = params.get("ModifiedOn")
        if params.get("OwnershipVerification") is not None:
            self._OwnershipVerification = OwnershipVerification()
            self._OwnershipVerification._deserialize(params.get("OwnershipVerification"))
        if params.get("Certificate") is not None:
            self._Certificate = AccelerationDomainCertificate()
            self._Certificate._deserialize(params.get("Certificate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccelerationDomainCertificate(AbstractModel):
    """Information of the acceleration domain name certificate.

    """

    def __init__(self):
        r"""
        :param _Mode: Certificate configuration mode. Values: <li>`disable`: Do not configure the certificate;</li><li>`eofreecert`: Use a free certificate provided by EdgeOne; </li><li>`sslcert`: Configure an SSL certificate.</li>
        :type Mode: str
        :param _List: List of certificates
Note: This field may return·null, indicating that no valid values can be obtained.
        :type List: list of CertificateInfo
        """
        self._Mode = None
        self._List = None

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = CertificateInfo()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclCondition(AbstractModel):
    """The condition that makes up an access control rule

    """

    def __init__(self):
        r"""
        :param _MatchFrom: Filters: 
<li>`host`: Request domain name;</li>
<li>`sip`: Client IP;</li>
<li>`ua`: User-Agent;</li>
<li>`cookie`: Cookie;</li>
<li>`cgi`: CGI script;</li>
<li>`xff`: XFF header;</li></li>
<li>`url`: Request URL;<li></li>
<li>`accept`: Request content type;</li>
<li>`method`: Request method<;/li>
<li>`header`: Request header;</li>
<li>`app_proto`: Application layer protocol;</li>
<li>`sip_proto`: Network layer protocol;</li>
<li>`uabot`: UA rules (only available in custom bot rules);</li>
<li>`idcid`: IDC rules (only available in custom bot rules);</li>
<li>`sipbot`: Search engine rules (only available in custom bot rules);</li>
<li>`portrait`: Client reputation (only available in custom bot rules);</li>
<li>`header_seq`: Header sequence (only available in custom bot rules);</li>
<li>`hdr`: Request body (only available in custom Web protection rules). </li>
        :type MatchFrom: str
        :param _MatchParam: The parameter of the field. When `MatchFrom = header`, the key contained in the header can be passed.
        :type MatchParam: str
        :param _Operator: The logical operator. Values:
<li>`equal`: Value equals</li>
<li>`not_equal`: Value not equals</li>
<li>`include`: String contains</li>
<li>`not_include`: String not contains</li>
<li>`match`: IP matches</li>
<li>`not_match`: IP not matches</li>
<li>`include_area`: Regions contain</li>
<li>`is_empty`: Value left empty</li>
<li>`not_exists`: Key fields not exist</li>
<li>`regexp`: Regex matches</li>
<li>`len_gt`: Value greater than</li>
<li>`len_lt`: Value smaller than</li>
<li>`len_eq`: Value equals</li>
<li>`match_prefix`: Prefix matches</li>
<li>`match_suffix`: Suffix matches</li>
<li>`wildcard`: Wildcard</li>
        :type Operator: str
        :param _MatchContent: The content to match.
        :type MatchContent: str
        """
        self._MatchFrom = None
        self._MatchParam = None
        self._Operator = None
        self._MatchContent = None

    @property
    def MatchFrom(self):
        return self._MatchFrom

    @MatchFrom.setter
    def MatchFrom(self, MatchFrom):
        self._MatchFrom = MatchFrom

    @property
    def MatchParam(self):
        return self._MatchParam

    @MatchParam.setter
    def MatchParam(self, MatchParam):
        self._MatchParam = MatchParam

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def MatchContent(self):
        return self._MatchContent

    @MatchContent.setter
    def MatchContent(self, MatchContent):
        self._MatchContent = MatchContent


    def _deserialize(self, params):
        self._MatchFrom = params.get("MatchFrom")
        self._MatchParam = params.get("MatchParam")
        self._Operator = params.get("Operator")
        self._MatchContent = params.get("MatchContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclConfig(AbstractModel):
    """ACL configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Switch. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param _AclUserRules: The custom rule.
        :type AclUserRules: list of AclUserRule
        :param _Customizes: Custom managed rules
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Customizes: list of AclUserRule
        """
        self._Switch = None
        self._AclUserRules = None
        self._Customizes = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def AclUserRules(self):
        return self._AclUserRules

    @AclUserRules.setter
    def AclUserRules(self, AclUserRules):
        self._AclUserRules = AclUserRules

    @property
    def Customizes(self):
        return self._Customizes

    @Customizes.setter
    def Customizes(self, Customizes):
        self._Customizes = Customizes


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("AclUserRules") is not None:
            self._AclUserRules = []
            for item in params.get("AclUserRules"):
                obj = AclUserRule()
                obj._deserialize(item)
                self._AclUserRules.append(obj)
        if params.get("Customizes") is not None:
            self._Customizes = []
            for item in params.get("Customizes"):
                obj = AclUserRule()
                obj._deserialize(item)
                self._Customizes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclUserRule(AbstractModel):
    """The custom rule

    """

    def __init__(self):
        r"""
        :param _RuleName: The rule name.
        :type RuleName: str
        :param _Action: The action. Values:
<li>`trans`: Allow</li>
<li>`drop`: Block the request</li>
<li>`monitor`: Observe</li>
<li>`ban`: Block the IP</li>
<li>`redirect`: Redirect the request</li>
<li>`page`: Return the specified page</li>
<li>`alg`: JavaScript challenge</li>
        :type Action: str
        :param _RuleStatus: The rule status. Values:
<li>`on`: Enabled</li>
<li>`off`: Disabled</li>
        :type RuleStatus: str
        :param _AclConditions: The custom rule.
        :type AclConditions: list of AclCondition
        :param _RulePriority: The rule priority. Value range: 0-100.
        :type RulePriority: int
        :param _RuleID: Rule ID, which is only used as an output parameter.
        :type RuleID: int
        :param _UpdateTime: The update time, which is only used as an output parameter.
        :type UpdateTime: str
        :param _PunishTime: IP ban duration. Range: 0-2 days. It's required when `Action=ban`. 
        :type PunishTime: int
        :param _PunishTimeUnit: The unit of the IP ban duration. Values:
<li>`second`: Second</li>
<li>`minutes`: Minute</li>
<li>`hour`: Hour</li>Default value: `second`.
        :type PunishTimeUnit: str
        :param _Name: Name of the custom return page. It's required when `Action=page`.	
        :type Name: str
        :param _PageId: (Disused) ID of the custom return page. The default value is 0, which means that the system default blocking page is used. 
        :type PageId: int
        :param _CustomResponseId: ID of custom response. The ID can be obtained via the `DescribeCustomErrorPages` API. It's required when `Action=page`.	
        :type CustomResponseId: str
        :param _ResponseCode: The response code to trigger the return page. It's required when `Action=page`. Value: 100-600. 3xx response codes are not supported. Default value: 567.
        :type ResponseCode: int
        :param _RedirectUrl: The redirection URL. It's required when `Action=redirect`.	
        :type RedirectUrl: str
        """
        self._RuleName = None
        self._Action = None
        self._RuleStatus = None
        self._AclConditions = None
        self._RulePriority = None
        self._RuleID = None
        self._UpdateTime = None
        self._PunishTime = None
        self._PunishTimeUnit = None
        self._Name = None
        self._PageId = None
        self._CustomResponseId = None
        self._ResponseCode = None
        self._RedirectUrl = None

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RuleStatus(self):
        return self._RuleStatus

    @RuleStatus.setter
    def RuleStatus(self, RuleStatus):
        self._RuleStatus = RuleStatus

    @property
    def AclConditions(self):
        return self._AclConditions

    @AclConditions.setter
    def AclConditions(self, AclConditions):
        self._AclConditions = AclConditions

    @property
    def RulePriority(self):
        return self._RulePriority

    @RulePriority.setter
    def RulePriority(self, RulePriority):
        self._RulePriority = RulePriority

    @property
    def RuleID(self):
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def PunishTime(self):
        return self._PunishTime

    @PunishTime.setter
    def PunishTime(self, PunishTime):
        self._PunishTime = PunishTime

    @property
    def PunishTimeUnit(self):
        return self._PunishTimeUnit

    @PunishTimeUnit.setter
    def PunishTimeUnit(self, PunishTimeUnit):
        self._PunishTimeUnit = PunishTimeUnit

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PageId(self):
        return self._PageId

    @PageId.setter
    def PageId(self, PageId):
        self._PageId = PageId

    @property
    def CustomResponseId(self):
        return self._CustomResponseId

    @CustomResponseId.setter
    def CustomResponseId(self, CustomResponseId):
        self._CustomResponseId = CustomResponseId

    @property
    def ResponseCode(self):
        return self._ResponseCode

    @ResponseCode.setter
    def ResponseCode(self, ResponseCode):
        self._ResponseCode = ResponseCode

    @property
    def RedirectUrl(self):
        return self._RedirectUrl

    @RedirectUrl.setter
    def RedirectUrl(self, RedirectUrl):
        self._RedirectUrl = RedirectUrl


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        self._Action = params.get("Action")
        self._RuleStatus = params.get("RuleStatus")
        if params.get("AclConditions") is not None:
            self._AclConditions = []
            for item in params.get("AclConditions"):
                obj = AclCondition()
                obj._deserialize(item)
                self._AclConditions.append(obj)
        self._RulePriority = params.get("RulePriority")
        self._RuleID = params.get("RuleID")
        self._UpdateTime = params.get("UpdateTime")
        self._PunishTime = params.get("PunishTime")
        self._PunishTimeUnit = params.get("PunishTimeUnit")
        self._Name = params.get("Name")
        self._PageId = params.get("PageId")
        self._CustomResponseId = params.get("CustomResponseId")
        self._ResponseCode = params.get("ResponseCode")
        self._RedirectUrl = params.get("RedirectUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Action(AbstractModel):
    """Rule engine action. Each feature supports only one of the following three action types. The `RuleAction` array can be of only one of the following types. For all details, see [DescribeRulesSetting](https://intl.cloud.tencent.com/document/product/1552/80618?from_cn_redirect=1).

    """

    def __init__(self):
        r"""
        :param _NormalAction: Common feature operations. The options for this category include:
<li> Access URL overriding (AccessUrlRedirect);</li>
<li> Origin URL overriding (UpstreamUrlRedirect);</li>
<li> QUIC;</li>
<li> WebSocket;</li>
<li> Video dragging (VideoSeek);</li>
<li> Token authentication (Authentication);</li>
<li> Custom CacheKey (CacheKey);</li>
<li> Node caching TTL (Cache);</li>
<li> Browser caching TTL (MaxAge);</li>
<li> Offline caching (OfflineCache);</li>
<li> Smart routing (SmartRouting);</li>
<li> Range-based origin pull (RangeOriginPull);</li>
<li> HTTP/2 origin pull (UpstreamHttp2);</li>
<li> Host header overriding (HostHeader);</li>
<li> Forced HTTPS (ForceRedirect);</li>
<li> HTTPS origin pull (OriginPullProtocol);</li>
<li> Cache pre-refresh (CachePrefresh);</li>
<li> Smart compression (Compression);</li>
<li> Hsts;</li>
<li> ClientIpHeader;</li>
<li> SslTlsSecureConf;</li>
<li> OcspStapling;</li>
<li> HTTP/2 access (Http2);</li>
<li> Redirection during origin pull (UpstreamFollowRedirect);</li>
<li> Modifying origin server (Origin);</li>
<li> Layer 7 origin pull timeout (HTTPUpstreamTimeout);</li>
<li> HTTP response (HttpResponse).</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type NormalAction: :class:`tencentcloud.teo.v20220901.models.NormalAction`
        :param _RewriteAction: Feature operation with a request/response header. Features of this type include:
<li>`RequestHeader`: HTTP request header modification.</li>
<li>`ResponseHeader`: HTTP response header modification.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type RewriteAction: :class:`tencentcloud.teo.v20220901.models.RewriteAction`
        :param _CodeAction: Feature operation with a status code. Features of this type include:
<li>`ErrorPage`: Custom error page.</li>
<li>`StatusCodeCache`: Status code cache TTL.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type CodeAction: :class:`tencentcloud.teo.v20220901.models.CodeAction`
        """
        self._NormalAction = None
        self._RewriteAction = None
        self._CodeAction = None

    @property
    def NormalAction(self):
        return self._NormalAction

    @NormalAction.setter
    def NormalAction(self, NormalAction):
        self._NormalAction = NormalAction

    @property
    def RewriteAction(self):
        return self._RewriteAction

    @RewriteAction.setter
    def RewriteAction(self, RewriteAction):
        self._RewriteAction = RewriteAction

    @property
    def CodeAction(self):
        return self._CodeAction

    @CodeAction.setter
    def CodeAction(self, CodeAction):
        self._CodeAction = CodeAction


    def _deserialize(self, params):
        if params.get("NormalAction") is not None:
            self._NormalAction = NormalAction()
            self._NormalAction._deserialize(params.get("NormalAction"))
        if params.get("RewriteAction") is not None:
            self._RewriteAction = RewriteAction()
            self._RewriteAction._deserialize(params.get("RewriteAction"))
        if params.get("CodeAction") is not None:
            self._CodeAction = CodeAction()
            self._CodeAction._deserialize(params.get("CodeAction"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedFilter(AbstractModel):
    """Key-value pair filters for conditional filtering queries and fuzzy queries, such as filtering ID, name, and status.
    If more than one filter exists, the logical relationship between these filters is `AND`.
    If one filter has multiple values, the logical relationship between these values is `OR`.

    """

    def __init__(self):
        r"""
        :param _Name: Field to be filtered.
        :type Name: str
        :param _Values: Value of the filtered field.
        :type Values: list of str
        :param _Fuzzy: Whether to enable fuzzy query.
        :type Fuzzy: bool
        """
        self._Name = None
        self._Values = None
        self._Fuzzy = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Fuzzy(self):
        return self._Fuzzy

    @Fuzzy.setter
    def Fuzzy(self, Fuzzy):
        self._Fuzzy = Fuzzy


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        self._Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRule(AbstractModel):
    """AI rule engine

    """

    def __init__(self):
        r"""
        :param _Mode: The status of the AI rule engine. Values:
<li>`smart_status_close`: Disabled</li>
<li>`smart_status_open`: Block</li>
<li>`smart_status_observe`: Observe</li>
        :type Mode: str
        """
        self._Mode = None

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlgDetectJS(AbstractModel):
    """Validate client behavior.

    """

    def __init__(self):
        r"""
        :param _Name: Method to validate client behavior.
        :type Name: str
        :param _WorkLevel: Proof-of-work strength. Values:
<li>`low` (default): Low</li>
<li>`middle`: Medium</li>
<li>`high`: High</li>
        :type WorkLevel: str
        :param _ExecuteMode: Implement a delay before executing JS in milliseconds. Value range: 0-1000. Default value: 500.
        :type ExecuteMode: int
        :param _InvalidStatTime: The period threshold for validating the result "Client JS disabled" in seconds. Value range: 5-3600. Default value: 10.
        :type InvalidStatTime: int
        :param _InvalidThreshold: The number of times for the result "Client JS disabled" occurred in the specified period. Value range: 1-100000000. Default value: 30.
        :type InvalidThreshold: int
        :param _AlgDetectResults: Client behavior validation results.
        :type AlgDetectResults: list of AlgDetectResult
        """
        self._Name = None
        self._WorkLevel = None
        self._ExecuteMode = None
        self._InvalidStatTime = None
        self._InvalidThreshold = None
        self._AlgDetectResults = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def WorkLevel(self):
        return self._WorkLevel

    @WorkLevel.setter
    def WorkLevel(self, WorkLevel):
        self._WorkLevel = WorkLevel

    @property
    def ExecuteMode(self):
        return self._ExecuteMode

    @ExecuteMode.setter
    def ExecuteMode(self, ExecuteMode):
        self._ExecuteMode = ExecuteMode

    @property
    def InvalidStatTime(self):
        return self._InvalidStatTime

    @InvalidStatTime.setter
    def InvalidStatTime(self, InvalidStatTime):
        self._InvalidStatTime = InvalidStatTime

    @property
    def InvalidThreshold(self):
        return self._InvalidThreshold

    @InvalidThreshold.setter
    def InvalidThreshold(self, InvalidThreshold):
        self._InvalidThreshold = InvalidThreshold

    @property
    def AlgDetectResults(self):
        return self._AlgDetectResults

    @AlgDetectResults.setter
    def AlgDetectResults(self, AlgDetectResults):
        self._AlgDetectResults = AlgDetectResults


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._WorkLevel = params.get("WorkLevel")
        self._ExecuteMode = params.get("ExecuteMode")
        self._InvalidStatTime = params.get("InvalidStatTime")
        self._InvalidThreshold = params.get("InvalidThreshold")
        if params.get("AlgDetectResults") is not None:
            self._AlgDetectResults = []
            for item in params.get("AlgDetectResults"):
                obj = AlgDetectResult()
                obj._deserialize(item)
                self._AlgDetectResults.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlgDetectResult(AbstractModel):
    """Active bot detection results.

    """

    def __init__(self):
        r"""
        :param _Result: The validation result. Values:
<li>`invalid`: Invalid Cookie</li>
<li>`cookie_empty`: No Cookie/Cookie expired</li>
<li>`js_empty`: Client JS disabled</li>
<li>`low`: Low-risk session</li>
<li>`middle`: Medium-risk session</li>
<li>`high`: High-risk session</li>
<li>`timeout`: JS validation timed out</li>
<li>`not_browser`: Invalid browser</li>
<li>`is_bot`: Bot client</li>
        :type Result: str
        :param _Action: The action. Values:
<li>`drop`: Block</li>
<li>`monitor`: Observe</li>
<li>`silence`: Drop w/o response</li>
<li>`shortdelay`: Add short latency</li>
<li>`longdelay`: Add long latency</li>
        :type Action: str
        """
        self._Result = None
        self._Action = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Action = params.get("Action")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlgDetectRule(AbstractModel):
    """Active bot detection rule.

    """

    def __init__(self):
        r"""
        :param _RuleID: ID of the rule.
        :type RuleID: int
        :param _RuleName: Name of the rule.
        :type RuleName: str
        :param _Switch: Whether to enable the rule.
        :type Switch: str
        :param _AlgConditions: Condition specified for the rule.
        :type AlgConditions: list of AclCondition
        :param _AlgDetectSession: Validate Cookie when the condition is satisfied.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AlgDetectSession: :class:`tencentcloud.teo.v20220901.models.AlgDetectSession`
        :param _AlgDetectJS: Validate client behavior when the condition is satisfied.
        :type AlgDetectJS: list of AlgDetectJS
        :param _UpdateTime: The update time, which is only used as an output parameter.
        :type UpdateTime: str
        """
        self._RuleID = None
        self._RuleName = None
        self._Switch = None
        self._AlgConditions = None
        self._AlgDetectSession = None
        self._AlgDetectJS = None
        self._UpdateTime = None

    @property
    def RuleID(self):
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def AlgConditions(self):
        return self._AlgConditions

    @AlgConditions.setter
    def AlgConditions(self, AlgConditions):
        self._AlgConditions = AlgConditions

    @property
    def AlgDetectSession(self):
        return self._AlgDetectSession

    @AlgDetectSession.setter
    def AlgDetectSession(self, AlgDetectSession):
        self._AlgDetectSession = AlgDetectSession

    @property
    def AlgDetectJS(self):
        return self._AlgDetectJS

    @AlgDetectJS.setter
    def AlgDetectJS(self, AlgDetectJS):
        self._AlgDetectJS = AlgDetectJS

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._RuleID = params.get("RuleID")
        self._RuleName = params.get("RuleName")
        self._Switch = params.get("Switch")
        if params.get("AlgConditions") is not None:
            self._AlgConditions = []
            for item in params.get("AlgConditions"):
                obj = AclCondition()
                obj._deserialize(item)
                self._AlgConditions.append(obj)
        if params.get("AlgDetectSession") is not None:
            self._AlgDetectSession = AlgDetectSession()
            self._AlgDetectSession._deserialize(params.get("AlgDetectSession"))
        if params.get("AlgDetectJS") is not None:
            self._AlgDetectJS = []
            for item in params.get("AlgDetectJS"):
                obj = AlgDetectJS()
                obj._deserialize(item)
                self._AlgDetectJS.append(obj)
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlgDetectSession(AbstractModel):
    """Validate Cookie.

    """

    def __init__(self):
        r"""
        :param _Name: Method to validate Cookie.
        :type Name: str
        :param _DetectMode: The validation mode. Values:
<li>`detect`: Validate only</li>
<li>`update_detect` (default): Update Cookie and validate</li>
        :type DetectMode: str
        :param _SessionAnalyzeSwitch: Whether to enable Cookie-based session check. The default value is `off`. Values:
<li>`off`: Disable</li>
<li>`on`: Enable</li>
        :type SessionAnalyzeSwitch: str
        :param _InvalidStatTime: The period threshold for validating the result "No Cookie/Cookie expired" in seconds. Value range: 5-3600. Default value: 10.
        :type InvalidStatTime: int
        :param _InvalidThreshold: The number of times for the result "No Cookie/Cookie expired" occurred in the specified period. Value range: 1-100000000. Default value: 300.
        :type InvalidThreshold: int
        :param _AlgDetectResults: Cookie validation results.
        :type AlgDetectResults: list of AlgDetectResult
        :param _SessionBehaviors: Cookie-based session check results.
        :type SessionBehaviors: list of AlgDetectResult
        """
        self._Name = None
        self._DetectMode = None
        self._SessionAnalyzeSwitch = None
        self._InvalidStatTime = None
        self._InvalidThreshold = None
        self._AlgDetectResults = None
        self._SessionBehaviors = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DetectMode(self):
        return self._DetectMode

    @DetectMode.setter
    def DetectMode(self, DetectMode):
        self._DetectMode = DetectMode

    @property
    def SessionAnalyzeSwitch(self):
        return self._SessionAnalyzeSwitch

    @SessionAnalyzeSwitch.setter
    def SessionAnalyzeSwitch(self, SessionAnalyzeSwitch):
        self._SessionAnalyzeSwitch = SessionAnalyzeSwitch

    @property
    def InvalidStatTime(self):
        return self._InvalidStatTime

    @InvalidStatTime.setter
    def InvalidStatTime(self, InvalidStatTime):
        self._InvalidStatTime = InvalidStatTime

    @property
    def InvalidThreshold(self):
        return self._InvalidThreshold

    @InvalidThreshold.setter
    def InvalidThreshold(self, InvalidThreshold):
        self._InvalidThreshold = InvalidThreshold

    @property
    def AlgDetectResults(self):
        return self._AlgDetectResults

    @AlgDetectResults.setter
    def AlgDetectResults(self, AlgDetectResults):
        self._AlgDetectResults = AlgDetectResults

    @property
    def SessionBehaviors(self):
        return self._SessionBehaviors

    @SessionBehaviors.setter
    def SessionBehaviors(self, SessionBehaviors):
        self._SessionBehaviors = SessionBehaviors


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._DetectMode = params.get("DetectMode")
        self._SessionAnalyzeSwitch = params.get("SessionAnalyzeSwitch")
        self._InvalidStatTime = params.get("InvalidStatTime")
        self._InvalidThreshold = params.get("InvalidThreshold")
        if params.get("AlgDetectResults") is not None:
            self._AlgDetectResults = []
            for item in params.get("AlgDetectResults"):
                obj = AlgDetectResult()
                obj._deserialize(item)
                self._AlgDetectResults.append(obj)
        if params.get("SessionBehaviors") is not None:
            self._SessionBehaviors = []
            for item in params.get("SessionBehaviors"):
                obj = AlgDetectResult()
                obj._deserialize(item)
                self._SessionBehaviors.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AliasDomain(AbstractModel):
    """Information of the alias domain name

    """

    def __init__(self):
        r"""
        :param _AliasName: The alias domain name.
        :type AliasName: str
        :param _ZoneId: The site ID.
        :type ZoneId: str
        :param _TargetName: The target domain name.
        :type TargetName: str
        :param _Status: Status of the alias domain name. Values:
<li>`active`: Activated</li>
<li>`pending`: Deploying</li>
<li>`conflict`: Reclaimed</li>
<li>`stop`: Stopped</li>
        :type Status: str
        :param _ForbidMode: The blocking mode. Values:
<li>`0`: Not blocked</li>
<li>`11`: Blocked due to regulatory compliance</li>
<li>`14`: Blocked due to ICP filing not obtained</li>
        :type ForbidMode: int
        :param _CreatedOn: Creation time of the alias domain name.
        :type CreatedOn: str
        :param _ModifiedOn: Modification time of the alias domain name.
        :type ModifiedOn: str
        """
        self._AliasName = None
        self._ZoneId = None
        self._TargetName = None
        self._Status = None
        self._ForbidMode = None
        self._CreatedOn = None
        self._ModifiedOn = None

    @property
    def AliasName(self):
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def TargetName(self):
        return self._TargetName

    @TargetName.setter
    def TargetName(self, TargetName):
        self._TargetName = TargetName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ForbidMode(self):
        return self._ForbidMode

    @ForbidMode.setter
    def ForbidMode(self, ForbidMode):
        self._ForbidMode = ForbidMode

    @property
    def CreatedOn(self):
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def ModifiedOn(self):
        return self._ModifiedOn

    @ModifiedOn.setter
    def ModifiedOn(self, ModifiedOn):
        self._ModifiedOn = ModifiedOn


    def _deserialize(self, params):
        self._AliasName = params.get("AliasName")
        self._ZoneId = params.get("ZoneId")
        self._TargetName = params.get("TargetName")
        self._Status = params.get("Status")
        self._ForbidMode = params.get("ForbidMode")
        self._CreatedOn = params.get("CreatedOn")
        self._ModifiedOn = params.get("ModifiedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationProxy(AbstractModel):
    """Application proxy instance

    """

    def __init__(self):
        r"""
        :param _ZoneId: The site ID.
        :type ZoneId: str
        :param _ZoneName: The site name.
        :type ZoneName: str
        :param _ProxyId: The proxy ID.
        :type ProxyId: str
        :param _ProxyName: The domain name or subdomain name when `ProxyType=hostname`.
The instance name when `ProxyType=instance`.
        :type ProxyName: str
        :param _ProxyType: The proxy type. Values:
<li>`hostname`: The proxy is created by subdomain name.</li>
<li>`instance`: The proxy is created by instance.</li>
        :type ProxyType: str
        :param _PlatType: The scheduling mode. Values:
<li>`ip`: Schedule via Anycast IP.</li>
<li>`domain`: Schedule via CNAME.</li>
        :type PlatType: str
        :param _Area: Acceleration region. Values:
<li>`mainland`: Chinese mainland.</li>
<li>`overseas`: Global (outside the Chinese mainland);</li>
Default value: overseas.
        :type Area: str
        :param _SecurityType: Whether to enable security protection. Values:
<li>`0`: Disable security protection.</li>
<li>`1`: Enable security protection.</li>
        :type SecurityType: int
        :param _AccelerateType: Whether to enable acceleration. Values:
<li>`0`: Disable acceleration.</li>
<li>`1`: Enable acceleration.</li>
        :type AccelerateType: int
        :param _SessionPersistTime: The session persistence duration.
        :type SessionPersistTime: int
        :param _Status: The rule status. Values:
<li>`online`: Enabled</li>
<li>`offline`: Disabled</li>
<li>`progress`: Deploying</li>
<li>`stopping`: Disabling</li>
<li>`fail`: Failed to deploy or disable</li>
        :type Status: str
        :param _BanStatus: The blocking status of the proxy. Values:
<li>`banned`: Blocked</li>
<li>`banning`: Blocking</li>
<li>`recover`: Unblocked</li>
<li>`recovering`: Unblocking</li>
        :type BanStatus: str
        :param _ScheduleValue: Scheduling information.
        :type ScheduleValue: list of str
        :param _HostId: When `ProxyType=hostname`:
This field indicates the unique ID of the subdomain name.
        :type HostId: str
        :param _Ipv6: The IPv6 access configuration.
        :type Ipv6: :class:`tencentcloud.teo.v20220901.models.Ipv6`
        :param _UpdateTime: The update time.
        :type UpdateTime: str
        :param _ApplicationProxyRules: List of rules.
        :type ApplicationProxyRules: list of ApplicationProxyRule
        :param _AccelerateMainland: Cross-MLC-border acceleration.
        :type AccelerateMainland: :class:`tencentcloud.teo.v20220901.models.AccelerateMainland`
        """
        self._ZoneId = None
        self._ZoneName = None
        self._ProxyId = None
        self._ProxyName = None
        self._ProxyType = None
        self._PlatType = None
        self._Area = None
        self._SecurityType = None
        self._AccelerateType = None
        self._SessionPersistTime = None
        self._Status = None
        self._BanStatus = None
        self._ScheduleValue = None
        self._HostId = None
        self._Ipv6 = None
        self._UpdateTime = None
        self._ApplicationProxyRules = None
        self._AccelerateMainland = None

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
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def ProxyName(self):
        return self._ProxyName

    @ProxyName.setter
    def ProxyName(self, ProxyName):
        self._ProxyName = ProxyName

    @property
    def ProxyType(self):
        return self._ProxyType

    @ProxyType.setter
    def ProxyType(self, ProxyType):
        self._ProxyType = ProxyType

    @property
    def PlatType(self):
        return self._PlatType

    @PlatType.setter
    def PlatType(self, PlatType):
        self._PlatType = PlatType

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def SecurityType(self):
        return self._SecurityType

    @SecurityType.setter
    def SecurityType(self, SecurityType):
        self._SecurityType = SecurityType

    @property
    def AccelerateType(self):
        return self._AccelerateType

    @AccelerateType.setter
    def AccelerateType(self, AccelerateType):
        self._AccelerateType = AccelerateType

    @property
    def SessionPersistTime(self):
        return self._SessionPersistTime

    @SessionPersistTime.setter
    def SessionPersistTime(self, SessionPersistTime):
        self._SessionPersistTime = SessionPersistTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BanStatus(self):
        return self._BanStatus

    @BanStatus.setter
    def BanStatus(self, BanStatus):
        self._BanStatus = BanStatus

    @property
    def ScheduleValue(self):
        return self._ScheduleValue

    @ScheduleValue.setter
    def ScheduleValue(self, ScheduleValue):
        self._ScheduleValue = ScheduleValue

    @property
    def HostId(self):
        return self._HostId

    @HostId.setter
    def HostId(self, HostId):
        self._HostId = HostId

    @property
    def Ipv6(self):
        return self._Ipv6

    @Ipv6.setter
    def Ipv6(self, Ipv6):
        self._Ipv6 = Ipv6

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ApplicationProxyRules(self):
        return self._ApplicationProxyRules

    @ApplicationProxyRules.setter
    def ApplicationProxyRules(self, ApplicationProxyRules):
        self._ApplicationProxyRules = ApplicationProxyRules

    @property
    def AccelerateMainland(self):
        return self._AccelerateMainland

    @AccelerateMainland.setter
    def AccelerateMainland(self, AccelerateMainland):
        self._AccelerateMainland = AccelerateMainland


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._ProxyId = params.get("ProxyId")
        self._ProxyName = params.get("ProxyName")
        self._ProxyType = params.get("ProxyType")
        self._PlatType = params.get("PlatType")
        self._Area = params.get("Area")
        self._SecurityType = params.get("SecurityType")
        self._AccelerateType = params.get("AccelerateType")
        self._SessionPersistTime = params.get("SessionPersistTime")
        self._Status = params.get("Status")
        self._BanStatus = params.get("BanStatus")
        self._ScheduleValue = params.get("ScheduleValue")
        self._HostId = params.get("HostId")
        if params.get("Ipv6") is not None:
            self._Ipv6 = Ipv6()
            self._Ipv6._deserialize(params.get("Ipv6"))
        self._UpdateTime = params.get("UpdateTime")
        if params.get("ApplicationProxyRules") is not None:
            self._ApplicationProxyRules = []
            for item in params.get("ApplicationProxyRules"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self._ApplicationProxyRules.append(obj)
        if params.get("AccelerateMainland") is not None:
            self._AccelerateMainland = AccelerateMainland()
            self._AccelerateMainland._deserialize(params.get("AccelerateMainland"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationProxyRule(AbstractModel):
    """Application proxy rule

    """

    def __init__(self):
        r"""
        :param _Proto: Protocol. Valid values:
<li>TCP: TCP protocol;</li>
<li>UDP: UDP protocol.</li>
        :type Proto: str
        :param _Port: Port. Supported formats:
<li>A single port, such as 80.</li>
<li>A port range, such as 81-82, indicating two ports 81 and 82.</li>
Note: Up to 20 ports can be input for each rule.
        :type Port: list of str
        :param _OriginType: Origin server type. Valid values:
<li>custom: manually added;</li>
<li>loadbalancer: cloud load balancer;</li>
<li>origins: origin server group.</li>
        :type OriginType: str
        :param _OriginValue: Origin server information.
<li>When OriginType is custom, it indicates one or more origin servers, such as `["8.8.8.8","9.9.9.9"]` or `OriginValue=["test.com"]`;</li>
<li>When OriginType is loadbalancer, it indicates a cloud load balancer, such as ["lb-xdffsfasdfs"];</li>
<li>When OriginType is origins, it requires one and only one element, indicating the origin server group ID, such as ["origin-537f5b41-162a-11ed-abaa-525400c5da15"].</li>
        :type OriginValue: list of str
        :param _RuleId: Rule ID.
        :type RuleId: str
        :param _Status: Status. Valid values:
<li>online: enabled;</li>
<li>offline: disabled;</li>
<li>progress: deploying;</li>
<li>stopping: disabling;</li>
<li>fail: deployment or disabling failed.</li>
        :type Status: str
        :param _ForwardClientIp: Passing the client IP address. Valid values:
<li>TOA: passing via TOA, available only when Proto = TCP;</li>
<li>PPV1: passing via Proxy Protocol V1, available only when Proto = TCP;</li>
<li>PPV2: passing via Proxy Protocol V2;</li>
<li>OFF: no passing.</li>Default value: OFF.
        :type ForwardClientIp: str
        :param _SessionPersist: Whether to enable session persistence. Valid values:
<li>true: Enable;</li>
<li>false: Disable.</li>Default value: false.
        :type SessionPersist: bool
        :param _SessionPersistTime: Duration for session persistence. The value takes effect only when SessionPersist is true.
Note: This field may return null, which indicates a failure to obtain a valid value.
        :type SessionPersistTime: int
        :param _OriginPort: Origin server port. Supported formats:
<li>A single port, such as 80.</li>
<li>A port range, such as 81-82, indicating two ports 81 and 82.</li>
        :type OriginPort: str
        :param _RuleTag: Rule tag.
Note: This field may return null, which indicates a failure to obtain a valid value.
        :type RuleTag: str
        """
        self._Proto = None
        self._Port = None
        self._OriginType = None
        self._OriginValue = None
        self._RuleId = None
        self._Status = None
        self._ForwardClientIp = None
        self._SessionPersist = None
        self._SessionPersistTime = None
        self._OriginPort = None
        self._RuleTag = None

    @property
    def Proto(self):
        return self._Proto

    @Proto.setter
    def Proto(self, Proto):
        self._Proto = Proto

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def OriginType(self):
        return self._OriginType

    @OriginType.setter
    def OriginType(self, OriginType):
        self._OriginType = OriginType

    @property
    def OriginValue(self):
        return self._OriginValue

    @OriginValue.setter
    def OriginValue(self, OriginValue):
        self._OriginValue = OriginValue

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ForwardClientIp(self):
        return self._ForwardClientIp

    @ForwardClientIp.setter
    def ForwardClientIp(self, ForwardClientIp):
        self._ForwardClientIp = ForwardClientIp

    @property
    def SessionPersist(self):
        return self._SessionPersist

    @SessionPersist.setter
    def SessionPersist(self, SessionPersist):
        self._SessionPersist = SessionPersist

    @property
    def SessionPersistTime(self):
        return self._SessionPersistTime

    @SessionPersistTime.setter
    def SessionPersistTime(self, SessionPersistTime):
        self._SessionPersistTime = SessionPersistTime

    @property
    def OriginPort(self):
        return self._OriginPort

    @OriginPort.setter
    def OriginPort(self, OriginPort):
        self._OriginPort = OriginPort

    @property
    def RuleTag(self):
        return self._RuleTag

    @RuleTag.setter
    def RuleTag(self, RuleTag):
        self._RuleTag = RuleTag


    def _deserialize(self, params):
        self._Proto = params.get("Proto")
        self._Port = params.get("Port")
        self._OriginType = params.get("OriginType")
        self._OriginValue = params.get("OriginValue")
        self._RuleId = params.get("RuleId")
        self._Status = params.get("Status")
        self._ForwardClientIp = params.get("ForwardClientIp")
        self._SessionPersist = params.get("SessionPersist")
        self._SessionPersistTime = params.get("SessionPersistTime")
        self._OriginPort = params.get("OriginPort")
        self._RuleTag = params.get("RuleTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AscriptionInfo(AbstractModel):
    """The site ownership information

    """

    def __init__(self):
        r"""
        :param _Subdomain: 
        :type Subdomain: str
        :param _RecordType: The record type.
        :type RecordType: str
        :param _RecordValue: The record value.
        :type RecordValue: str
        """
        self._Subdomain = None
        self._RecordType = None
        self._RecordValue = None

    @property
    def Subdomain(self):
        return self._Subdomain

    @Subdomain.setter
    def Subdomain(self, Subdomain):
        self._Subdomain = Subdomain

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RecordValue(self):
        return self._RecordValue

    @RecordValue.setter
    def RecordValue(self, RecordValue):
        self._RecordValue = RecordValue


    def _deserialize(self, params):
        self._Subdomain = params.get("Subdomain")
        self._RecordType = params.get("RecordType")
        self._RecordValue = params.get("RecordValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillingData(AbstractModel):
    """Billing data item

    """

    def __init__(self):
        r"""
        :param _Time: Time.
        :type Time: str
        :param _Value: Value.
        :type Value: int
        """
        self._Time = None
        self._Value = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillingDataFilter(AbstractModel):
    """Billing data filter criteria.

    """

    def __init__(self):
        r"""
        :param _Type: Parameter name.
        :type Type: str
        :param _Value: Parameter value.
        :type Value: str
        """
        self._Type = None
        self._Value = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindSecurityTemplateToEntityRequest(AbstractModel):
    """BindSecurityTemplateToEntity request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID of the policy template to be bound to or unbound from.
        :type ZoneId: str
        :param _Entities: List of domain names to bind to/unbind from a policy template
        :type Entities: list of str
        :param _Operate: Action options. Values include:
<li>`bind`: Bind the domain names to the specified policy template </li>
<li>`unbind-keep-policy`: Unbind a domain name from a policy template and keep the current policy when unbinding</li>
<li>`unbind-use-default`: Unbind domain names from policy templates and use default blank policy.</li> Note: Only one domain name can be unbound at one time. When `Operate` is `unbind-keep-policy` or `unbind-use-default`, there can only be one domain name specified in `Entities`.
        :type Operate: str
        :param _TemplateId: Specifies the ID of the policy template or the site's global policy to be bound or unbound.
- To bind to a policy template, or unbind from it, specify the policy template ID.
- To bind to the site's global policy, or unbind from it, use the @ZoneLevel@domain parameter value.

Note: After unbinding, the domain name will use an independent policy and rule quota will be calculated separately. Please make sure there is sufficient rule quota before unbinding.
        :type TemplateId: str
        :param _OverWrite: Whether to replace the existing policy template bound with the domain name. Values: 
<li>`true`: Replace the template bound to the domain. </li>
<li>`false`: Do not replace the template.</li> Note: In this case, the API returns an error if there is already a policy template bound to the specified domain name.
        :type OverWrite: bool
        """
        self._ZoneId = None
        self._Entities = None
        self._Operate = None
        self._TemplateId = None
        self._OverWrite = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Entities(self):
        return self._Entities

    @Entities.setter
    def Entities(self, Entities):
        self._Entities = Entities

    @property
    def Operate(self):
        return self._Operate

    @Operate.setter
    def Operate(self, Operate):
        self._Operate = Operate

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def OverWrite(self):
        return self._OverWrite

    @OverWrite.setter
    def OverWrite(self, OverWrite):
        self._OverWrite = OverWrite


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Entities = params.get("Entities")
        self._Operate = params.get("Operate")
        self._TemplateId = params.get("TemplateId")
        self._OverWrite = params.get("OverWrite")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindSecurityTemplateToEntityResponse(AbstractModel):
    """BindSecurityTemplateToEntity response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class BindSharedCNAMEMap(AbstractModel):
    """Bindings between a shared CNAME and connected domain names

    """

    def __init__(self):
        r"""
        :param _SharedCNAME: The shared CNAME to be bound with or unbound from.
        :type SharedCNAME: str
        :param _DomainNames: Acceleration domains (up to 20).
        :type DomainNames: list of str
        """
        self._SharedCNAME = None
        self._DomainNames = None

    @property
    def SharedCNAME(self):
        return self._SharedCNAME

    @SharedCNAME.setter
    def SharedCNAME(self, SharedCNAME):
        self._SharedCNAME = SharedCNAME

    @property
    def DomainNames(self):
        return self._DomainNames

    @DomainNames.setter
    def DomainNames(self, DomainNames):
        self._DomainNames = DomainNames


    def _deserialize(self, params):
        self._SharedCNAME = params.get("SharedCNAME")
        self._DomainNames = params.get("DomainNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindSharedCNAMERequest(AbstractModel):
    """BindSharedCNAME request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site related with the acceleration domain name.	
        :type ZoneId: str
        :param _BindType: Action type. Values:
<li>`bind`: To bind</li>
<li>`unbind`: To unbind</li>
        :type BindType: str
        :param _BindSharedCNAMEMaps: Bindings between domain names and a shared CNAME
        :type BindSharedCNAMEMaps: list of BindSharedCNAMEMap
        """
        self._ZoneId = None
        self._BindType = None
        self._BindSharedCNAMEMaps = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def BindType(self):
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType

    @property
    def BindSharedCNAMEMaps(self):
        return self._BindSharedCNAMEMaps

    @BindSharedCNAMEMaps.setter
    def BindSharedCNAMEMaps(self, BindSharedCNAMEMaps):
        self._BindSharedCNAMEMaps = BindSharedCNAMEMaps


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._BindType = params.get("BindType")
        if params.get("BindSharedCNAMEMaps") is not None:
            self._BindSharedCNAMEMaps = []
            for item in params.get("BindSharedCNAMEMaps"):
                obj = BindSharedCNAMEMap()
                obj._deserialize(item)
                self._BindSharedCNAMEMaps.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindSharedCNAMEResponse(AbstractModel):
    """BindSharedCNAME response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class BindZoneToPlanRequest(AbstractModel):
    """BindZoneToPlan request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site to be bound.
        :type ZoneId: str
        :param _PlanId: ID of the target plan.
        :type PlanId: str
        """
        self._ZoneId = None
        self._PlanId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._PlanId = params.get("PlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindZoneToPlanResponse(AbstractModel):
    """BindZoneToPlan response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class BotConfig(AbstractModel):
    """Bot security configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable bot security. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param _BotManagedRule: The settings of the bot managed rule. If it is null, the settings that were last configured will be used.
        :type BotManagedRule: :class:`tencentcloud.teo.v20220901.models.BotManagedRule`
        :param _BotPortraitRule: The settings of the client reputation rule. If it is null, the settings that were last configured will be used.
        :type BotPortraitRule: :class:`tencentcloud.teo.v20220901.models.BotPortraitRule`
        :param _IntelligenceRule: The bot intelligence settings. If it is null, the settings that were last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IntelligenceRule: :class:`tencentcloud.teo.v20220901.models.IntelligenceRule`
        :param _BotUserRules: Settings of the custom bot rule. If it is null, the settings that were last configured will be used.
        :type BotUserRules: list of BotUserRule
        :param _AlgDetectRule: Active bot detection rule.
        :type AlgDetectRule: list of AlgDetectRule
        :param _Customizes: Settings of the bot managed rule. It is only used for output.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Customizes: list of BotUserRule
        """
        self._Switch = None
        self._BotManagedRule = None
        self._BotPortraitRule = None
        self._IntelligenceRule = None
        self._BotUserRules = None
        self._AlgDetectRule = None
        self._Customizes = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def BotManagedRule(self):
        return self._BotManagedRule

    @BotManagedRule.setter
    def BotManagedRule(self, BotManagedRule):
        self._BotManagedRule = BotManagedRule

    @property
    def BotPortraitRule(self):
        return self._BotPortraitRule

    @BotPortraitRule.setter
    def BotPortraitRule(self, BotPortraitRule):
        self._BotPortraitRule = BotPortraitRule

    @property
    def IntelligenceRule(self):
        return self._IntelligenceRule

    @IntelligenceRule.setter
    def IntelligenceRule(self, IntelligenceRule):
        self._IntelligenceRule = IntelligenceRule

    @property
    def BotUserRules(self):
        return self._BotUserRules

    @BotUserRules.setter
    def BotUserRules(self, BotUserRules):
        self._BotUserRules = BotUserRules

    @property
    def AlgDetectRule(self):
        return self._AlgDetectRule

    @AlgDetectRule.setter
    def AlgDetectRule(self, AlgDetectRule):
        self._AlgDetectRule = AlgDetectRule

    @property
    def Customizes(self):
        return self._Customizes

    @Customizes.setter
    def Customizes(self, Customizes):
        self._Customizes = Customizes


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("BotManagedRule") is not None:
            self._BotManagedRule = BotManagedRule()
            self._BotManagedRule._deserialize(params.get("BotManagedRule"))
        if params.get("BotPortraitRule") is not None:
            self._BotPortraitRule = BotPortraitRule()
            self._BotPortraitRule._deserialize(params.get("BotPortraitRule"))
        if params.get("IntelligenceRule") is not None:
            self._IntelligenceRule = IntelligenceRule()
            self._IntelligenceRule._deserialize(params.get("IntelligenceRule"))
        if params.get("BotUserRules") is not None:
            self._BotUserRules = []
            for item in params.get("BotUserRules"):
                obj = BotUserRule()
                obj._deserialize(item)
                self._BotUserRules.append(obj)
        if params.get("AlgDetectRule") is not None:
            self._AlgDetectRule = []
            for item in params.get("AlgDetectRule"):
                obj = AlgDetectRule()
                obj._deserialize(item)
                self._AlgDetectRule.append(obj)
        if params.get("Customizes") is not None:
            self._Customizes = []
            for item in params.get("Customizes"):
                obj = BotUserRule()
                obj._deserialize(item)
                self._Customizes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotExtendAction(AbstractModel):
    """Bot extended actions

    """

    def __init__(self):
        r"""
        :param _Action: Action. Valid values: 
<li>`monitor`: Observe;</li>
<li>`alg`: JavaScript challenge;</li>
<li>`captcha`: Managed challenge;</li>
<li>`random`: Actions are executed based on the percentage specified in `ExtendActions`;</li>
<li>`silence`: Silence;</li>
<li>`shortdelay`: Add short latency;</li>
<li>`longdelay`: Add long latency.</li>
        :type Action: str
        :param _Percent: The probability for triggering the action. Value range: 0-100.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Percent: int
        """
        self._Action = None
        self._Percent = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Percent(self):
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._Percent = params.get("Percent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotManagedRule(AbstractModel):
    """Bot managed rules. The rule IDs can be obtained from the output of DescribeBotManagedRules.

    """

    def __init__(self):
        r"""
        :param _Action: The rule action. Values:
<li>`drop`: Block</li>
<li>`trans`: Allow</li>
<li>`alg`: JavaScript challenge</li>
<li>`monitor`: Observe</li>
        :type Action: str
        :param _RuleID: The rule ID, which is only used as an output parameter.
        :type RuleID: int
        :param _TransManagedIds: The ID of the rule that applies the "Allow" action.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TransManagedIds: list of int
        :param _AlgManagedIds: The ID of the rule that applies the "JavaScript challenge" action.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AlgManagedIds: list of int
        :param _CapManagedIds: The ID of the rule that applies the "Managed challenge" action.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CapManagedIds: list of int
        :param _MonManagedIds: The ID of the rule that applies the "Observe" action.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MonManagedIds: list of int
        :param _DropManagedIds: The ID of the rule that applies the "Block" action.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DropManagedIds: list of int
        """
        self._Action = None
        self._RuleID = None
        self._TransManagedIds = None
        self._AlgManagedIds = None
        self._CapManagedIds = None
        self._MonManagedIds = None
        self._DropManagedIds = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RuleID(self):
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def TransManagedIds(self):
        return self._TransManagedIds

    @TransManagedIds.setter
    def TransManagedIds(self, TransManagedIds):
        self._TransManagedIds = TransManagedIds

    @property
    def AlgManagedIds(self):
        return self._AlgManagedIds

    @AlgManagedIds.setter
    def AlgManagedIds(self, AlgManagedIds):
        self._AlgManagedIds = AlgManagedIds

    @property
    def CapManagedIds(self):
        return self._CapManagedIds

    @CapManagedIds.setter
    def CapManagedIds(self, CapManagedIds):
        self._CapManagedIds = CapManagedIds

    @property
    def MonManagedIds(self):
        return self._MonManagedIds

    @MonManagedIds.setter
    def MonManagedIds(self, MonManagedIds):
        self._MonManagedIds = MonManagedIds

    @property
    def DropManagedIds(self):
        return self._DropManagedIds

    @DropManagedIds.setter
    def DropManagedIds(self, DropManagedIds):
        self._DropManagedIds = DropManagedIds


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._RuleID = params.get("RuleID")
        self._TransManagedIds = params.get("TransManagedIds")
        self._AlgManagedIds = params.get("AlgManagedIds")
        self._CapManagedIds = params.get("CapManagedIds")
        self._MonManagedIds = params.get("MonManagedIds")
        self._DropManagedIds = params.get("DropManagedIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotPortraitRule(AbstractModel):
    """Bot user portrait rules

    """

    def __init__(self):
        r"""
        :param _Switch: Switch. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param _RuleID: The rule ID, which is only used as an output parameter.
        :type RuleID: int
        :param _AlgManagedIds: The ID of the rule that applies the "JavaScript challenge" action.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AlgManagedIds: list of int
        :param _CapManagedIds: The ID of the rule that applies the "Managed challenge" action.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CapManagedIds: list of int
        :param _MonManagedIds: The ID of the rule that applies the "Observe" action.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MonManagedIds: list of int
        :param _DropManagedIds: The ID of the rule that applies the "Block" action.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DropManagedIds: list of int
        """
        self._Switch = None
        self._RuleID = None
        self._AlgManagedIds = None
        self._CapManagedIds = None
        self._MonManagedIds = None
        self._DropManagedIds = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def RuleID(self):
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def AlgManagedIds(self):
        return self._AlgManagedIds

    @AlgManagedIds.setter
    def AlgManagedIds(self, AlgManagedIds):
        self._AlgManagedIds = AlgManagedIds

    @property
    def CapManagedIds(self):
        return self._CapManagedIds

    @CapManagedIds.setter
    def CapManagedIds(self, CapManagedIds):
        self._CapManagedIds = CapManagedIds

    @property
    def MonManagedIds(self):
        return self._MonManagedIds

    @MonManagedIds.setter
    def MonManagedIds(self, MonManagedIds):
        self._MonManagedIds = MonManagedIds

    @property
    def DropManagedIds(self):
        return self._DropManagedIds

    @DropManagedIds.setter
    def DropManagedIds(self, DropManagedIds):
        self._DropManagedIds = DropManagedIds


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._RuleID = params.get("RuleID")
        self._AlgManagedIds = params.get("AlgManagedIds")
        self._CapManagedIds = params.get("CapManagedIds")
        self._MonManagedIds = params.get("MonManagedIds")
        self._DropManagedIds = params.get("DropManagedIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotUserRule(AbstractModel):
    """Custom bot rules

    """

    def __init__(self):
        r"""
        :param _RuleName: 
        :type RuleName: str
        :param _Action: The action. Values:
<li>`drop`: Block the request</li>
<li>`monitor`: Observe</li>
<li>`trans`: Allow</li>
<li>`redirect`: Redirect the request</li>
<li>`page`: Return the specified page</li>
<li>`alg`: JavaScript challenge</li>
<li>`captcha`: Managed challenge</li>
<li>`random`: Handle the request randomly by the weight</li>
<li>`silence`: Keep the connection but do not response to the client</li>
<li>`shortdelay`: Add a short latency period</li>
<li>`longdelay`: Add a long latency period</li>
        :type Action: str
        :param _RuleStatus: The rule status. Values:
<li>`on`: Enabled</li>
<li>`off`: Disabled</li>Default value: `on`
        :type RuleStatus: str
        :param _AclConditions: Details of the rule.
        :type AclConditions: list of AclCondition
        :param _RulePriority: The rule weight. Value range: 0-100.
        :type RulePriority: int
        :param _RuleID: Rule ID, which is only used as an output parameter.
        :type RuleID: int
        :param _ExtendActions: [Currently unavailable] Specify the random action and percentage.
        :type ExtendActions: list of BotExtendAction
        :param _FreqFields: The filter. Values:
<li>`sip`: Client IP</li>
This parameter is left empty by default.
        :type FreqFields: list of str
        :param _UpdateTime: The update time, which is only used as an output parameter.
        :type UpdateTime: str
        :param _FreqScope: Query scope. Values:
<li>`source_to_eo`: (Response) Traffic going from the origin to EdgeOne.</li>
<li>`client_to_eo`: (Request) Traffic going from the client to EdgeOne.</li>
Default: `source_to_eo`.
        :type FreqScope: list of str
        :param _Name: Name of the custom return page. It's required when `Action=page`.
        :type Name: str
        :param _CustomResponseId: ID of custom response. The ID can be obtained via the `DescribeCustomErrorPages` API. It's required when `Action=page`.	
        :type CustomResponseId: str
        :param _ResponseCode: The response code to trigger the return page. It's required when `Action=page`. Value: 100-600. 3xx response codes are not supported. Default value: 567.
        :type ResponseCode: int
        :param _RedirectUrl: The redirection URL. It's required when `Action=redirect`.
        :type RedirectUrl: str
        """
        self._RuleName = None
        self._Action = None
        self._RuleStatus = None
        self._AclConditions = None
        self._RulePriority = None
        self._RuleID = None
        self._ExtendActions = None
        self._FreqFields = None
        self._UpdateTime = None
        self._FreqScope = None
        self._Name = None
        self._CustomResponseId = None
        self._ResponseCode = None
        self._RedirectUrl = None

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RuleStatus(self):
        return self._RuleStatus

    @RuleStatus.setter
    def RuleStatus(self, RuleStatus):
        self._RuleStatus = RuleStatus

    @property
    def AclConditions(self):
        return self._AclConditions

    @AclConditions.setter
    def AclConditions(self, AclConditions):
        self._AclConditions = AclConditions

    @property
    def RulePriority(self):
        return self._RulePriority

    @RulePriority.setter
    def RulePriority(self, RulePriority):
        self._RulePriority = RulePriority

    @property
    def RuleID(self):
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def ExtendActions(self):
        return self._ExtendActions

    @ExtendActions.setter
    def ExtendActions(self, ExtendActions):
        self._ExtendActions = ExtendActions

    @property
    def FreqFields(self):
        return self._FreqFields

    @FreqFields.setter
    def FreqFields(self, FreqFields):
        self._FreqFields = FreqFields

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def FreqScope(self):
        return self._FreqScope

    @FreqScope.setter
    def FreqScope(self, FreqScope):
        self._FreqScope = FreqScope

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CustomResponseId(self):
        return self._CustomResponseId

    @CustomResponseId.setter
    def CustomResponseId(self, CustomResponseId):
        self._CustomResponseId = CustomResponseId

    @property
    def ResponseCode(self):
        return self._ResponseCode

    @ResponseCode.setter
    def ResponseCode(self, ResponseCode):
        self._ResponseCode = ResponseCode

    @property
    def RedirectUrl(self):
        return self._RedirectUrl

    @RedirectUrl.setter
    def RedirectUrl(self, RedirectUrl):
        self._RedirectUrl = RedirectUrl


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        self._Action = params.get("Action")
        self._RuleStatus = params.get("RuleStatus")
        if params.get("AclConditions") is not None:
            self._AclConditions = []
            for item in params.get("AclConditions"):
                obj = AclCondition()
                obj._deserialize(item)
                self._AclConditions.append(obj)
        self._RulePriority = params.get("RulePriority")
        self._RuleID = params.get("RuleID")
        if params.get("ExtendActions") is not None:
            self._ExtendActions = []
            for item in params.get("ExtendActions"):
                obj = BotExtendAction()
                obj._deserialize(item)
                self._ExtendActions.append(obj)
        self._FreqFields = params.get("FreqFields")
        self._UpdateTime = params.get("UpdateTime")
        self._FreqScope = params.get("FreqScope")
        self._Name = params.get("Name")
        self._CustomResponseId = params.get("CustomResponseId")
        self._ResponseCode = params.get("ResponseCode")
        self._RedirectUrl = params.get("RedirectUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CC(AbstractModel):
    """CC configuration item.

    """

    def __init__(self):
        r"""
        :param _Switch: WAF switch. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param _PolicyId: ID of the policy
        :type PolicyId: int
        """
        self._Switch = None
        self._PolicyId = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CLSTopic(AbstractModel):
    """The configuration information of real-time log delivery to Tencent Cloud CLS

    """

    def __init__(self):
        r"""
        :param _LogSetId: The ID of the Tencent Cloud CLS log set.
        :type LogSetId: str
        :param _TopicId: The ID of the Tencent Cloud CLS log topic.
        :type TopicId: str
        :param _LogSetRegion: The region of the Tencent Cloud CLS log set.
        :type LogSetRegion: str
        """
        self._LogSetId = None
        self._TopicId = None
        self._LogSetRegion = None

    @property
    def LogSetId(self):
        return self._LogSetId

    @LogSetId.setter
    def LogSetId(self, LogSetId):
        self._LogSetId = LogSetId

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def LogSetRegion(self):
        return self._LogSetRegion

    @LogSetRegion.setter
    def LogSetRegion(self, LogSetRegion):
        self._LogSetRegion = LogSetRegion


    def _deserialize(self, params):
        self._LogSetId = params.get("LogSetId")
        self._TopicId = params.get("TopicId")
        self._LogSetRegion = params.get("LogSetRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Cache(AbstractModel):
    """Cache time settings

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable cache configuration. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param _CacheTime: Cache expiration time setting.
Unit: second. The maximum value is 365 days.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CacheTime: int
        :param _IgnoreCacheControl: Whether to enable force cache. Values:
<li>`on`: Enable</li>
<li>`off`: Disable </li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IgnoreCacheControl: str
        """
        self._Switch = None
        self._CacheTime = None
        self._IgnoreCacheControl = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def CacheTime(self):
        return self._CacheTime

    @CacheTime.setter
    def CacheTime(self, CacheTime):
        self._CacheTime = CacheTime

    @property
    def IgnoreCacheControl(self):
        warnings.warn("parameter `IgnoreCacheControl` is deprecated", DeprecationWarning) 

        return self._IgnoreCacheControl

    @IgnoreCacheControl.setter
    def IgnoreCacheControl(self, IgnoreCacheControl):
        warnings.warn("parameter `IgnoreCacheControl` is deprecated", DeprecationWarning) 

        self._IgnoreCacheControl = IgnoreCacheControl


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._CacheTime = params.get("CacheTime")
        self._IgnoreCacheControl = params.get("IgnoreCacheControl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfig(AbstractModel):
    """Cache rule configuration.

    """

    def __init__(self):
        r"""
        :param _Cache: Cache configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type Cache: :class:`tencentcloud.teo.v20220901.models.Cache`
        :param _NoCache: No-cache configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type NoCache: :class:`tencentcloud.teo.v20220901.models.NoCache`
        :param _FollowOrigin: Follows the origin server configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type FollowOrigin: :class:`tencentcloud.teo.v20220901.models.FollowOrigin`
        """
        self._Cache = None
        self._NoCache = None
        self._FollowOrigin = None

    @property
    def Cache(self):
        return self._Cache

    @Cache.setter
    def Cache(self, Cache):
        self._Cache = Cache

    @property
    def NoCache(self):
        return self._NoCache

    @NoCache.setter
    def NoCache(self, NoCache):
        self._NoCache = NoCache

    @property
    def FollowOrigin(self):
        return self._FollowOrigin

    @FollowOrigin.setter
    def FollowOrigin(self, FollowOrigin):
        self._FollowOrigin = FollowOrigin


    def _deserialize(self, params):
        if params.get("Cache") is not None:
            self._Cache = Cache()
            self._Cache._deserialize(params.get("Cache"))
        if params.get("NoCache") is not None:
            self._NoCache = NoCache()
            self._NoCache._deserialize(params.get("NoCache"))
        if params.get("FollowOrigin") is not None:
            self._FollowOrigin = FollowOrigin()
            self._FollowOrigin._deserialize(params.get("FollowOrigin"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheKey(AbstractModel):
    """The cache key configuration.

    """

    def __init__(self):
        r"""
        :param _FullUrlCache: Whether to enable full-path cache. Values:
<li>`on`: Enable full-path cache (i.e., disable Ignore Query String).</li>
<li>`off`: Disable full-path cache (i.e., enable Ignore Query String).</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type FullUrlCache: str
        :param _IgnoreCase: Whether to ignore case in the cache key. Values:
<li>`on`: Ignore</li>
<li>`off`: Not ignore</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IgnoreCase: str
        :param _QueryString: Request parameter contained in `CacheKey`. 
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type QueryString: :class:`tencentcloud.teo.v20220901.models.QueryString`
        """
        self._FullUrlCache = None
        self._IgnoreCase = None
        self._QueryString = None

    @property
    def FullUrlCache(self):
        return self._FullUrlCache

    @FullUrlCache.setter
    def FullUrlCache(self, FullUrlCache):
        self._FullUrlCache = FullUrlCache

    @property
    def IgnoreCase(self):
        return self._IgnoreCase

    @IgnoreCase.setter
    def IgnoreCase(self, IgnoreCase):
        self._IgnoreCase = IgnoreCase

    @property
    def QueryString(self):
        return self._QueryString

    @QueryString.setter
    def QueryString(self, QueryString):
        self._QueryString = QueryString


    def _deserialize(self, params):
        self._FullUrlCache = params.get("FullUrlCache")
        self._IgnoreCase = params.get("IgnoreCase")
        if params.get("QueryString") is not None:
            self._QueryString = QueryString()
            self._QueryString._deserialize(params.get("QueryString"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CachePrefresh(AbstractModel):
    """Cache prefresh

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable cache prefresh. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param _Percent: The cache prefresh percentage. Values: 1-99
Note: This field may return null, indicating that no valid values can be obtained.
        :type Percent: int
        """
        self._Switch = None
        self._Percent = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Percent(self):
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Percent = params.get("Percent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheTag(AbstractModel):
    """The information attached when the node cache purge type is set to purge_cache_tag.

    """

    def __init__(self):
        r"""
        :param _Domains: List of domain names to purge cache for.
        :type Domains: list of str
        """
        self._Domains = None

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains


    def _deserialize(self, params):
        self._Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertificateInfo(AbstractModel):
    """HTTPS server certificate configuration

    """

    def __init__(self):
        r"""
        :param _CertId: ID of the server certificate.
        :type CertId: str
        :param _Alias: Alias of the certificate.
        :type Alias: str
        :param _Type: Type of the certificate. Values:
<li>`default`: Default certificate</li>
<li>`upload`: Specified certificate</li>
<li>`managed`: Tencent Cloud-managed certificate</li>
        :type Type: str
        :param _ExpireTime: The certificate expiration time.
        :type ExpireTime: str
        :param _DeployTime: Time when the certificate is deployed.
        :type DeployTime: str
        :param _SignAlgo: Signature algorithm.
        :type SignAlgo: str
        :param _Status: Status of the certificate. Values:
u200c<li>`deployed`: The deployment has completed</li>
u200c<li>`processing`: Deployment in progress</li>
u200c<li>`applying`: Application in progress</li>
u200c<li>`failed`: Application rejected</li>
<li>`issued`: Binding failed.</li>
        :type Status: str
        """
        self._CertId = None
        self._Alias = None
        self._Type = None
        self._ExpireTime = None
        self._DeployTime = None
        self._SignAlgo = None
        self._Status = None

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def DeployTime(self):
        return self._DeployTime

    @DeployTime.setter
    def DeployTime(self, DeployTime):
        self._DeployTime = DeployTime

    @property
    def SignAlgo(self):
        return self._SignAlgo

    @SignAlgo.setter
    def SignAlgo(self, SignAlgo):
        self._SignAlgo = SignAlgo

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._Alias = params.get("Alias")
        self._Type = params.get("Type")
        self._ExpireTime = params.get("ExpireTime")
        self._DeployTime = params.get("DeployTime")
        self._SignAlgo = params.get("SignAlgo")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCnameStatusRequest(AbstractModel):
    """CheckCnameStatus request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID.
        :type ZoneId: str
        :param _RecordNames: List of accelerated domain names.
        :type RecordNames: list of str
        """
        self._ZoneId = None
        self._RecordNames = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RecordNames(self):
        return self._RecordNames

    @RecordNames.setter
    def RecordNames(self, RecordNames):
        self._RecordNames = RecordNames


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RecordNames = params.get("RecordNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCnameStatusResponse(AbstractModel):
    """CheckCnameStatus response structure.

    """

    def __init__(self):
        r"""
        :param _CnameStatus: CNAME status of accelerated domain names.
        :type CnameStatus: list of CnameStatus
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CnameStatus = None
        self._RequestId = None

    @property
    def CnameStatus(self):
        return self._CnameStatus

    @CnameStatus.setter
    def CnameStatus(self, CnameStatus):
        self._CnameStatus = CnameStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CnameStatus") is not None:
            self._CnameStatus = []
            for item in params.get("CnameStatus"):
                obj = CnameStatus()
                obj._deserialize(item)
                self._CnameStatus.append(obj)
        self._RequestId = params.get("RequestId")


class ClientIpCountry(AbstractModel):
    """Location information of the client IP carried in origin-pull. It is formatted as a two-letter ISO-3166-1 country/region code.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable configuration. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param _HeaderName: Name of the request header that contains the client IP region. It is valid when `Switch=on`. 
The default value `EO-Client-IPCountry` is used when it is not specified.
        :type HeaderName: str
        """
        self._Switch = None
        self._HeaderName = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def HeaderName(self):
        return self._HeaderName

    @HeaderName.setter
    def HeaderName(self, HeaderName):
        self._HeaderName = HeaderName


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._HeaderName = params.get("HeaderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClientIpHeader(AbstractModel):
    """The client IP header configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable the configuration. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param _HeaderName: Name of the request header that contains the client IP for origin-pull. 
The default value `X-Forwarded-IP` is used when it is not specified. 
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type HeaderName: str
        """
        self._Switch = None
        self._HeaderName = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def HeaderName(self):
        return self._HeaderName

    @HeaderName.setter
    def HeaderName(self, HeaderName):
        self._HeaderName = HeaderName


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._HeaderName = params.get("HeaderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CnameStatus(AbstractModel):
    """CNAME status

    """

    def __init__(self):
        r"""
        :param _RecordName: The domain name.
        :type RecordName: str
        :param _Cname: The CNAME address.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Cname: str
        :param _Status: The CNAME status. Values:
<li>`active`: Activated</li>
<li>`moved`: Not activated </li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        """
        self._RecordName = None
        self._Cname = None
        self._Status = None

    @property
    def RecordName(self):
        return self._RecordName

    @RecordName.setter
    def RecordName(self, RecordName):
        self._RecordName = RecordName

    @property
    def Cname(self):
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._RecordName = params.get("RecordName")
        self._Cname = params.get("Cname")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeAction(AbstractModel):
    """Rule engine action with a status code

    """

    def __init__(self):
        r"""
        :param _Action: Feature name. For details, see [DescribeRulesSetting](https://intl.cloud.tencent.com/document/product/1552/80618?from_cn_redirect=1) API
        :type Action: str
        :param _Parameters: Operation parameter.
        :type Parameters: list of RuleCodeActionParams
        """
        self._Action = None
        self._Parameters = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Parameters(self):
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters


    def _deserialize(self, params):
        self._Action = params.get("Action")
        if params.get("Parameters") is not None:
            self._Parameters = []
            for item in params.get("Parameters"):
                obj = RuleCodeActionParams()
                obj._deserialize(item)
                self._Parameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Compression(AbstractModel):
    """Smart compression configuration.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable smart compression. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param _Algorithms: Compression algorithm. Values:
<li>`brotli`: Brotli algorithm</li>
<li>`gzip`: Gzip algorithm</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Algorithms: list of str
        """
        self._Switch = None
        self._Algorithms = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Algorithms(self):
        return self._Algorithms

    @Algorithms.setter
    def Algorithms(self, Algorithms):
        self._Algorithms = Algorithms


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Algorithms = params.get("Algorithms")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigGroupVersionInfo(AbstractModel):
    """Version information about the configuration group.

    """

    def __init__(self):
        r"""
        :param _VersionId: Version ID.
        :type VersionId: str
        :param _VersionNumber: Version No.
        :type VersionNumber: str
        :param _GroupId: Configuraration group ID.
        :type GroupId: str
        :param _GroupType: Configuration group type. Valid values: 
<li>l7_acceleration: L7 acceleration configuration group. </li>
<li>edge_functions: Edge function configuration group. </li>
        :type GroupType: str
        :param _Description: Version description.
        :type Description: str
        :param _Status: Version status. Valid values: 
<li>creating: Being created.</li>
<li>inactive: Not effective.</li>
<li>active: Effective. </li>
        :type Status: str
        :param _CreateTime: Version creation time. The time format follows the ISO 8601 standard and is represented in Coordinated Universal Time (UTC).
        :type CreateTime: str
        """
        self._VersionId = None
        self._VersionNumber = None
        self._GroupId = None
        self._GroupType = None
        self._Description = None
        self._Status = None
        self._CreateTime = None

    @property
    def VersionId(self):
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def VersionNumber(self):
        return self._VersionNumber

    @VersionNumber.setter
    def VersionNumber(self, VersionNumber):
        self._VersionNumber = VersionNumber

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupType(self):
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

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
        self._VersionId = params.get("VersionId")
        self._VersionNumber = params.get("VersionNumber")
        self._GroupId = params.get("GroupId")
        self._GroupType = params.get("GroupType")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccelerationDomainRequest(AbstractModel):
    """CreateAccelerationDomain request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site related with the acceleration domain name.
        :type ZoneId: str
        :param _DomainName: Acceleration domain name
        :type DomainName: str
        :param _OriginInfo: Details of the origin.
        :type OriginInfo: :class:`tencentcloud.teo.v20220901.models.OriginInfo`
        :param _OriginProtocol: Origin-pull protocol configuration. Values:
<li>`FOLLOW`: Follow the protocol of origin</li>
<li>`HTTP`: Send requests to the origin over HTTP</li>
<li>`HTTPS`: Send requests to the origin over HTTPS</li>
<li>Default: `FOLLOW`</li>
        :type OriginProtocol: str
        :param _HttpOriginPort: Ports for HTTP origin-pull requests. Range: 1-65535. It takes effect when `OriginProtocol=FOLLOW/HTTP`. Port 80 is used if it's not specified. 
        :type HttpOriginPort: int
        :param _HttpsOriginPort: Ports for HTTPS origin-pull requests. Range: 1-65535. It takes effect when `OriginProtocol=FOLLOW/HTTPS`. Port 443 is used if it's not specified. 
        :type HttpsOriginPort: int
        :param _IPv6Status: IPv6 status. Values:
<li>`follow`: Follow the IPv6 configuration of the site</li>
<li>`on`: Enable</li>
<li>`off`: Disable</li>
<li>Default: `follow`</li>
        :type IPv6Status: str
        """
        self._ZoneId = None
        self._DomainName = None
        self._OriginInfo = None
        self._OriginProtocol = None
        self._HttpOriginPort = None
        self._HttpsOriginPort = None
        self._IPv6Status = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def OriginInfo(self):
        return self._OriginInfo

    @OriginInfo.setter
    def OriginInfo(self, OriginInfo):
        self._OriginInfo = OriginInfo

    @property
    def OriginProtocol(self):
        return self._OriginProtocol

    @OriginProtocol.setter
    def OriginProtocol(self, OriginProtocol):
        self._OriginProtocol = OriginProtocol

    @property
    def HttpOriginPort(self):
        return self._HttpOriginPort

    @HttpOriginPort.setter
    def HttpOriginPort(self, HttpOriginPort):
        self._HttpOriginPort = HttpOriginPort

    @property
    def HttpsOriginPort(self):
        return self._HttpsOriginPort

    @HttpsOriginPort.setter
    def HttpsOriginPort(self, HttpsOriginPort):
        self._HttpsOriginPort = HttpsOriginPort

    @property
    def IPv6Status(self):
        return self._IPv6Status

    @IPv6Status.setter
    def IPv6Status(self, IPv6Status):
        self._IPv6Status = IPv6Status


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._DomainName = params.get("DomainName")
        if params.get("OriginInfo") is not None:
            self._OriginInfo = OriginInfo()
            self._OriginInfo._deserialize(params.get("OriginInfo"))
        self._OriginProtocol = params.get("OriginProtocol")
        self._HttpOriginPort = params.get("HttpOriginPort")
        self._HttpsOriginPort = params.get("HttpsOriginPort")
        self._IPv6Status = params.get("IPv6Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccelerationDomainResponse(AbstractModel):
    """CreateAccelerationDomain response structure.

    """

    def __init__(self):
        r"""
        :param _OwnershipVerification: Use the information returned by this parameter to verify the ownership of a domain name. For details, see [Ownership Verification](https://intl.cloud.tencent.com/document/product/1552/70789?from_cn_redirect=1).
Note: This field may return·null, indicating that no valid values can be obtained.
        :type OwnershipVerification: :class:`tencentcloud.teo.v20220901.models.OwnershipVerification`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OwnershipVerification = None
        self._RequestId = None

    @property
    def OwnershipVerification(self):
        return self._OwnershipVerification

    @OwnershipVerification.setter
    def OwnershipVerification(self, OwnershipVerification):
        self._OwnershipVerification = OwnershipVerification

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("OwnershipVerification") is not None:
            self._OwnershipVerification = OwnershipVerification()
            self._OwnershipVerification._deserialize(params.get("OwnershipVerification"))
        self._RequestId = params.get("RequestId")


class CreateAliasDomainRequest(AbstractModel):
    """CreateAliasDomain request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: The site ID.
        :type ZoneId: str
        :param _AliasName: The alias domain name.
        :type AliasName: str
        :param _TargetName: The target domain name.
        :type TargetName: str
        :param _CertType: Certificate configuration. Values:
<li>`none`: (Default) Do not configure</li>
<li>`hosting`: Managed SSL certificate</li>
        :type CertType: str
        :param _CertId: The certificate ID. This field is required when `CertType=hosting`.
        :type CertId: list of str
        """
        self._ZoneId = None
        self._AliasName = None
        self._TargetName = None
        self._CertType = None
        self._CertId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def AliasName(self):
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName

    @property
    def TargetName(self):
        return self._TargetName

    @TargetName.setter
    def TargetName(self, TargetName):
        self._TargetName = TargetName

    @property
    def CertType(self):
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._AliasName = params.get("AliasName")
        self._TargetName = params.get("TargetName")
        self._CertType = params.get("CertType")
        self._CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAliasDomainResponse(AbstractModel):
    """CreateAliasDomain response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class CreateApplicationProxyRequest(AbstractModel):
    """CreateApplicationProxy request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID.
        :type ZoneId: str
        :param _ProxyName: Domain name or subdomain name when `ProxyType=hostname`; 
Instance name when `ProxyType=instance`.
        :type ProxyName: str
        :param _PlatType: The scheduling mode. Values:
<li>`ip`: Schedule via Anycast IP.</li>
<li>`domain`: Schedule via CNAME.</li>
        :type PlatType: str
        :param _SecurityType: Whether to enable security protection. Values:
<li>`0`: Disable security protection.</li>
<li>`1`: Enable security protection.</li>
        :type SecurityType: int
        :param _AccelerateType: Whether to enable acceleration. Values:
<li>`0`: Disable acceleration.</li>
<li>`1`: Enable acceleration.</li>
        :type AccelerateType: int
        :param _ProxyType: Layer 4 proxy mode, with value: <li>instance: instance mode.</li>If not specified, the default value instance will be used.
        :type ProxyType: str
        :param _SessionPersistTime: The session persistence duration. Value range: 30-3600 (in seconds).
If not specified, this field uses the default value 600.
        :type SessionPersistTime: int
        :param _Ipv6: Ipv6 access configuration. 
IPv6 access is disabled if it is not specified.
        :type Ipv6: :class:`tencentcloud.teo.v20220901.models.Ipv6`
        :param _ApplicationProxyRules: The rule details.
If this field is not specified, an application proxy rule will not be created.
        :type ApplicationProxyRules: list of ApplicationProxyRule
        :param _AccelerateMainland: Cross-MLC-border acceleration. It is disabled if this parameter is not specified.
        :type AccelerateMainland: :class:`tencentcloud.teo.v20220901.models.AccelerateMainland`
        """
        self._ZoneId = None
        self._ProxyName = None
        self._PlatType = None
        self._SecurityType = None
        self._AccelerateType = None
        self._ProxyType = None
        self._SessionPersistTime = None
        self._Ipv6 = None
        self._ApplicationProxyRules = None
        self._AccelerateMainland = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyName(self):
        return self._ProxyName

    @ProxyName.setter
    def ProxyName(self, ProxyName):
        self._ProxyName = ProxyName

    @property
    def PlatType(self):
        return self._PlatType

    @PlatType.setter
    def PlatType(self, PlatType):
        self._PlatType = PlatType

    @property
    def SecurityType(self):
        return self._SecurityType

    @SecurityType.setter
    def SecurityType(self, SecurityType):
        self._SecurityType = SecurityType

    @property
    def AccelerateType(self):
        return self._AccelerateType

    @AccelerateType.setter
    def AccelerateType(self, AccelerateType):
        self._AccelerateType = AccelerateType

    @property
    def ProxyType(self):
        return self._ProxyType

    @ProxyType.setter
    def ProxyType(self, ProxyType):
        self._ProxyType = ProxyType

    @property
    def SessionPersistTime(self):
        return self._SessionPersistTime

    @SessionPersistTime.setter
    def SessionPersistTime(self, SessionPersistTime):
        self._SessionPersistTime = SessionPersistTime

    @property
    def Ipv6(self):
        return self._Ipv6

    @Ipv6.setter
    def Ipv6(self, Ipv6):
        self._Ipv6 = Ipv6

    @property
    def ApplicationProxyRules(self):
        return self._ApplicationProxyRules

    @ApplicationProxyRules.setter
    def ApplicationProxyRules(self, ApplicationProxyRules):
        self._ApplicationProxyRules = ApplicationProxyRules

    @property
    def AccelerateMainland(self):
        return self._AccelerateMainland

    @AccelerateMainland.setter
    def AccelerateMainland(self, AccelerateMainland):
        self._AccelerateMainland = AccelerateMainland


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyName = params.get("ProxyName")
        self._PlatType = params.get("PlatType")
        self._SecurityType = params.get("SecurityType")
        self._AccelerateType = params.get("AccelerateType")
        self._ProxyType = params.get("ProxyType")
        self._SessionPersistTime = params.get("SessionPersistTime")
        if params.get("Ipv6") is not None:
            self._Ipv6 = Ipv6()
            self._Ipv6._deserialize(params.get("Ipv6"))
        if params.get("ApplicationProxyRules") is not None:
            self._ApplicationProxyRules = []
            for item in params.get("ApplicationProxyRules"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self._ApplicationProxyRules.append(obj)
        if params.get("AccelerateMainland") is not None:
            self._AccelerateMainland = AccelerateMainland()
            self._AccelerateMainland._deserialize(params.get("AccelerateMainland"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationProxyResponse(AbstractModel):
    """CreateApplicationProxy response structure.

    """

    def __init__(self):
        r"""
        :param _ProxyId: The L4 application proxy ID.
        :type ProxyId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProxyId = None
        self._RequestId = None

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._RequestId = params.get("RequestId")


class CreateApplicationProxyRuleRequest(AbstractModel):
    """CreateApplicationProxyRule request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: The site ID.
        :type ZoneId: str
        :param _ProxyId: The proxy ID.
        :type ProxyId: str
        :param _Proto: The protocol. Values:
<li>`TCP`: TCP protocol</li>
<li>`UDP`: UDP protocol</li>
        :type Proto: str
        :param _Port: The access port, which can be:
<li>A single port, such as 80</li>
<li>A port range, such as 81-90</li>
        :type Port: list of str
        :param _OriginType: Origin server type. Valid values:<li>custom: Manually added;</li>
<li>loadbalancer: Cloud Load Balancer;</li><li>origins: Origin server group.</li>
        :type OriginType: str
        :param _OriginValue: Details of the origin server:<li>When OriginType is custom, it indicates one or more origin servers, such as ["8.8.8.8","9.9.9.9"] or OriginValue=["test.com"];</li><li>When OriginType is loadbalancer, it indicates a single Cloud Load Balancer, such as ["lb-xdffsfasdfs"];</li><li>When OriginType is origins, it requires one and only one element, which represents an origin server group ID, such as ["origin-537f5b41-162a-11ed-abaa-525400c5da15"].</li>
        :type OriginValue: list of str
        :param _ForwardClientIp: Passes the client IP. Values:
<li>`TOA`: Pass the client IP via TOA (available only when `Proto=TCP`).</li>
<li>`PPV1`: Pass the client IP via Proxy Protocol V1 (available only when `Proto=TCP`).</li>
<li>`PPV2`: Pass the client IP via Proxy Protocol V2.</li>
<li>`OFF`: Not pass the client IP.</li>Default value: OFF.
        :type ForwardClientIp: str
        :param _SessionPersist: Whether to enable session persistence. Values:
<li>`true`: Enable.</li>
<li>`false`: Disable.</li>Default value: false.
        :type SessionPersist: bool
        :param _SessionPersistTime: Duration for the persistent session. The value takes effect only when `SessionPersist = true`.
        :type SessionPersistTime: int
        :param _OriginPort: The origin port, which can be:
<li>A single port, such as 80</li>
<li>A port range, such as 81-82</li>
        :type OriginPort: str
        :param _RuleTag: Rule tag. This parameter is left empty by default.
        :type RuleTag: str
        """
        self._ZoneId = None
        self._ProxyId = None
        self._Proto = None
        self._Port = None
        self._OriginType = None
        self._OriginValue = None
        self._ForwardClientIp = None
        self._SessionPersist = None
        self._SessionPersistTime = None
        self._OriginPort = None
        self._RuleTag = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def Proto(self):
        return self._Proto

    @Proto.setter
    def Proto(self, Proto):
        self._Proto = Proto

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def OriginType(self):
        return self._OriginType

    @OriginType.setter
    def OriginType(self, OriginType):
        self._OriginType = OriginType

    @property
    def OriginValue(self):
        return self._OriginValue

    @OriginValue.setter
    def OriginValue(self, OriginValue):
        self._OriginValue = OriginValue

    @property
    def ForwardClientIp(self):
        return self._ForwardClientIp

    @ForwardClientIp.setter
    def ForwardClientIp(self, ForwardClientIp):
        self._ForwardClientIp = ForwardClientIp

    @property
    def SessionPersist(self):
        return self._SessionPersist

    @SessionPersist.setter
    def SessionPersist(self, SessionPersist):
        self._SessionPersist = SessionPersist

    @property
    def SessionPersistTime(self):
        return self._SessionPersistTime

    @SessionPersistTime.setter
    def SessionPersistTime(self, SessionPersistTime):
        self._SessionPersistTime = SessionPersistTime

    @property
    def OriginPort(self):
        return self._OriginPort

    @OriginPort.setter
    def OriginPort(self, OriginPort):
        self._OriginPort = OriginPort

    @property
    def RuleTag(self):
        return self._RuleTag

    @RuleTag.setter
    def RuleTag(self, RuleTag):
        self._RuleTag = RuleTag


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        self._Proto = params.get("Proto")
        self._Port = params.get("Port")
        self._OriginType = params.get("OriginType")
        self._OriginValue = params.get("OriginValue")
        self._ForwardClientIp = params.get("ForwardClientIp")
        self._SessionPersist = params.get("SessionPersist")
        self._SessionPersistTime = params.get("SessionPersistTime")
        self._OriginPort = params.get("OriginPort")
        self._RuleTag = params.get("RuleTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationProxyRuleResponse(AbstractModel):
    """CreateApplicationProxyRule response structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: The rule ID.
        :type RuleId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleId = None
        self._RequestId = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class CreateCLSIndexRequest(AbstractModel):
    """CreateCLSIndex request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _TaskId: The ID of the real-time log delivery task.
        :type TaskId: str
        """
        self._ZoneId = None
        self._TaskId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCLSIndexResponse(AbstractModel):
    """CreateCLSIndex response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class CreateConfigGroupVersionRequest(AbstractModel):
    """CreateConfigGroupVersion request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _GroupId: GroupId of the version to be created.
        :type GroupId: str
        :param _Content: Configuration content to be imported. It is required to be in JSON format and encoded in UTF-8. Please refer to the example below for the configuration file content.
        :type Content: str
        :param _Description: Version description. The maximum length allowed is 50 characters. This field can be used to provide details about the application scenarios of this version.
        :type Description: str
        """
        self._ZoneId = None
        self._GroupId = None
        self._Content = None
        self._Description = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._GroupId = params.get("GroupId")
        self._Content = params.get("Content")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConfigGroupVersionResponse(AbstractModel):
    """CreateConfigGroupVersion response structure.

    """

    def __init__(self):
        r"""
        :param _VersionId: Version ID.
        :type VersionId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class CreateCustomizeErrorPageRequest(AbstractModel):
    """CreateCustomizeErrorPage request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _Name: Custom error page name. The name must be 2-30 characters long.
        :type Name: str
        :param _ContentType: Custom error page type, with values:<li>text/html; </li><li>application/json;</li><li>text/plain;</li><li>text/xml.</li>
        :type ContentType: str
        :param _Description: Custom error page description, not exceeding 60 characters.
        :type Description: str
        :param _Content: Custom error page content, not exceeding 2 KB.
        :type Content: str
        """
        self._ZoneId = None
        self._Name = None
        self._ContentType = None
        self._Description = None
        self._Content = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ContentType(self):
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Name = params.get("Name")
        self._ContentType = params.get("ContentType")
        self._Description = params.get("Description")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomizeErrorPageResponse(AbstractModel):
    """CreateCustomizeErrorPage response structure.

    """

    def __init__(self):
        r"""
        :param _PageId: Page ID.
        :type PageId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PageId = None
        self._RequestId = None

    @property
    def PageId(self):
        return self._PageId

    @PageId.setter
    def PageId(self, PageId):
        self._PageId = PageId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PageId = params.get("PageId")
        self._RequestId = params.get("RequestId")


class CreateFunctionRequest(AbstractModel):
    """CreateFunction request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _Name: Function name, which can contain up to 30 characters, including lowercase letters, digits, and hyphens. It should start and end with a digit or a letter.
        :type Name: str
        :param _Content: Function content, which currently only supports JavaScript code. Its maximum size is 5 MB.
        :type Content: str
        :param _Remark: Function description, which can contain up to 60 characters.
        :type Remark: str
        """
        self._ZoneId = None
        self._Name = None
        self._Content = None
        self._Remark = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Name = params.get("Name")
        self._Content = params.get("Content")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFunctionResponse(AbstractModel):
    """CreateFunction response structure.

    """

    def __init__(self):
        r"""
        :param _FunctionId: Function ID.
        :type FunctionId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FunctionId = None
        self._RequestId = None

    @property
    def FunctionId(self):
        return self._FunctionId

    @FunctionId.setter
    def FunctionId(self, FunctionId):
        self._FunctionId = FunctionId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FunctionId = params.get("FunctionId")
        self._RequestId = params.get("RequestId")


class CreateFunctionRuleRequest(AbstractModel):
    """CreateFunctionRule request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _FunctionRuleConditions: Rule condition list. There is an OR relationship between different conditions of the same trigger rule.
        :type FunctionRuleConditions: list of FunctionRuleCondition
        :param _FunctionId: Function ID, specifying a function executed when a trigger rule condition is met.
        :type FunctionId: str
        :param _Remark: Rule description, which can contain up to 60 characters.
        :type Remark: str
        """
        self._ZoneId = None
        self._FunctionRuleConditions = None
        self._FunctionId = None
        self._Remark = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def FunctionRuleConditions(self):
        return self._FunctionRuleConditions

    @FunctionRuleConditions.setter
    def FunctionRuleConditions(self, FunctionRuleConditions):
        self._FunctionRuleConditions = FunctionRuleConditions

    @property
    def FunctionId(self):
        return self._FunctionId

    @FunctionId.setter
    def FunctionId(self, FunctionId):
        self._FunctionId = FunctionId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("FunctionRuleConditions") is not None:
            self._FunctionRuleConditions = []
            for item in params.get("FunctionRuleConditions"):
                obj = FunctionRuleCondition()
                obj._deserialize(item)
                self._FunctionRuleConditions.append(obj)
        self._FunctionId = params.get("FunctionId")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFunctionRuleResponse(AbstractModel):
    """CreateFunctionRule response structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: Rule ID.
        :type RuleId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleId = None
        self._RequestId = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class CreateL4ProxyRequest(AbstractModel):
    """CreateL4Proxy request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _ProxyName: Name of the L4 proxy instance, which can contain 1-50 characters, including a-z, 0-9, and hyphens (-). However, hyphens (-) cannot be used individually or consecutively and should not be placed at the beginning or end of the name. Modification is not allowed after creation.

        :type ProxyName: str
        :param _Area: Acceleration zone of the L4 proxy instance.
<li>mainland: Chinese mainland availability zone;</li>
<li>overseas: global availability zone (excluding the Chinese mainland);</li>
<li>global: global availability zone.</li>
        :type Area: str
        :param _Ipv6: Whether to enable IPv6 access. If this parameter is not input, the default value `off` is used. This configuration can be enabled only in certain acceleration zones and security protection configurations. For details, see [Creating an L4 Proxy Instance] (https://intl.cloud.tencent.com/document/product/1552/90025?from_cn_redirect=1). Valid values:
<li>on: Enable;</li>
<li>off: Disable.</li>


        :type Ipv6: str
        :param _StaticIp: Whether to enable static IP. If this parameter is not input, the default value `off` is used. This configuration can be enabled only in certain acceleration zones and security protection configurations. For details, see [Creating an L4 Proxy Instance] (https://intl.cloud.tencent.com/document/product/1552/90025?from_cn_redirect=1). Valid values:
<li>on: Enable;</li>
<li>off: Disable.</li>

        :type StaticIp: str
        :param _AccelerateMainland: Whether to enable network optimization for the Chinese mainland. If this parameter is not input, the default value `off` is used. This configuration can be enabled only in certain acceleration zones and security protection configurations. For details, see [Creating an L4 Proxy Instance] (https://intl.cloud.tencent.com/document/product/1552/90025?from_cn_redirect=1). Valid values:
<li>on: Enable;</li>
<li>off: Disable.</li>

        :type AccelerateMainland: str
        :param _DDosProtectionConfig: Configuration of L3/L4 DDoS protection. If this parameter is not input, the default platform protection option is used. For details, see [Exclusive DDoS Protection Usage] (https://intl.cloud.tencent.com/document/product/1552/95994?from_cn_redirect=1).
        :type DDosProtectionConfig: :class:`tencentcloud.teo.v20220901.models.DDosProtectionConfig`
        """
        self._ZoneId = None
        self._ProxyName = None
        self._Area = None
        self._Ipv6 = None
        self._StaticIp = None
        self._AccelerateMainland = None
        self._DDosProtectionConfig = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyName(self):
        return self._ProxyName

    @ProxyName.setter
    def ProxyName(self, ProxyName):
        self._ProxyName = ProxyName

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Ipv6(self):
        return self._Ipv6

    @Ipv6.setter
    def Ipv6(self, Ipv6):
        self._Ipv6 = Ipv6

    @property
    def StaticIp(self):
        return self._StaticIp

    @StaticIp.setter
    def StaticIp(self, StaticIp):
        self._StaticIp = StaticIp

    @property
    def AccelerateMainland(self):
        return self._AccelerateMainland

    @AccelerateMainland.setter
    def AccelerateMainland(self, AccelerateMainland):
        self._AccelerateMainland = AccelerateMainland

    @property
    def DDosProtectionConfig(self):
        return self._DDosProtectionConfig

    @DDosProtectionConfig.setter
    def DDosProtectionConfig(self, DDosProtectionConfig):
        self._DDosProtectionConfig = DDosProtectionConfig


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyName = params.get("ProxyName")
        self._Area = params.get("Area")
        self._Ipv6 = params.get("Ipv6")
        self._StaticIp = params.get("StaticIp")
        self._AccelerateMainland = params.get("AccelerateMainland")
        if params.get("DDosProtectionConfig") is not None:
            self._DDosProtectionConfig = DDosProtectionConfig()
            self._DDosProtectionConfig._deserialize(params.get("DDosProtectionConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL4ProxyResponse(AbstractModel):
    """CreateL4Proxy response structure.

    """

    def __init__(self):
        r"""
        :param _ProxyId: L4 instance ID.
        :type ProxyId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProxyId = None
        self._RequestId = None

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._RequestId = params.get("RequestId")


class CreateL4ProxyRulesRequest(AbstractModel):
    """CreateL4ProxyRules request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _ProxyId: Layer 4 proxy instance ID.
        :type ProxyId: str
        :param _L4ProxyRules: List of forwarding rules. A single request supports up to 200 forwarding rules.
Note: When L4ProxyRule is used here, Protocol, PortRange, OriginType, OriginValue, and OriginPortRange are required fields; ClientIPPassThroughMode, SessionPersist, SessionPersistTime, and RuleTag are optional fields; do not fill in RuleId and Status.
        :type L4ProxyRules: list of L4ProxyRule
        """
        self._ZoneId = None
        self._ProxyId = None
        self._L4ProxyRules = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def L4ProxyRules(self):
        return self._L4ProxyRules

    @L4ProxyRules.setter
    def L4ProxyRules(self, L4ProxyRules):
        self._L4ProxyRules = L4ProxyRules


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        if params.get("L4ProxyRules") is not None:
            self._L4ProxyRules = []
            for item in params.get("L4ProxyRules"):
                obj = L4ProxyRule()
                obj._deserialize(item)
                self._L4ProxyRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL4ProxyRulesResponse(AbstractModel):
    """CreateL4ProxyRules response structure.

    """

    def __init__(self):
        r"""
        :param _L4ProxyRuleIds: IDs of newly added forwarding rules, returned as an array.
        :type L4ProxyRuleIds: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._L4ProxyRuleIds = None
        self._RequestId = None

    @property
    def L4ProxyRuleIds(self):
        return self._L4ProxyRuleIds

    @L4ProxyRuleIds.setter
    def L4ProxyRuleIds(self, L4ProxyRuleIds):
        self._L4ProxyRuleIds = L4ProxyRuleIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._L4ProxyRuleIds = params.get("L4ProxyRuleIds")
        self._RequestId = params.get("RequestId")


class CreateOriginGroupRequest(AbstractModel):
    """CreateOriginGroup request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _Name: Origin group name. It can contain 1 to 200 characters ([a-z], [A-Z], [0-9] and [_-]).
        :type Name: str
        :param _Type: (Required) Origin group type. Values:
<li>`GENERAL`: General origin groups. It supports IPs and domain names. It can be referenced by DNS, Rule Engine, Layer 4 Proxy and General LoadBalancer. </li>
<li>`HTTP`: HTTP-specific origin groups. It supports IPs/domain names and object storage buckets. It can be referenced by acceleration domain names, rule engines and HTTP LoadBalancer. It cannot be referenced by L4 proxies. </li>
        :type Type: str
        :param _Records: (Required) Origins in the origin group.
        :type Records: list of OriginRecord
        :param _HostHeader: Host header used for origin-pull. It only works when `Type=HTTP`. The `HostHeader` specified in `RuleEngine` takes a higher priority over this configuration.
        :type HostHeader: str
        """
        self._ZoneId = None
        self._Name = None
        self._Type = None
        self._Records = None
        self._HostHeader = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Records(self):
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def HostHeader(self):
        return self._HostHeader

    @HostHeader.setter
    def HostHeader(self, HostHeader):
        self._HostHeader = HostHeader


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = OriginRecord()
                obj._deserialize(item)
                self._Records.append(obj)
        self._HostHeader = params.get("HostHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOriginGroupResponse(AbstractModel):
    """CreateOriginGroup response structure.

    """

    def __init__(self):
        r"""
        :param _OriginGroupId: The ID of the origin group.
        :type OriginGroupId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OriginGroupId = None
        self._RequestId = None

    @property
    def OriginGroupId(self):
        return self._OriginGroupId

    @OriginGroupId.setter
    def OriginGroupId(self, OriginGroupId):
        self._OriginGroupId = OriginGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginGroupId = params.get("OriginGroupId")
        self._RequestId = params.get("RequestId")


class CreatePlanForZoneRequest(AbstractModel):
    """CreatePlanForZone request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site.
        :type ZoneId: str
        :param _PlanType: The plan option. Values:
<li>`sta`: Standard plan that supports content delivery network outside the Chinese mainland.</li>
<li>`sta_with_bot`: Standard plan that supports content delivery network outside the Chinese mainland and bot management.</li>
<li>`sta_cm`: Standard plan that supports content delivery network inside the Chinese mainland.</li>
<li>`sta_cm_with_bot`: Standard plan that supports content delivery network inside the Chinese mainland and bot management.</li>
<li>`sta_global`: Standard plan that supports content delivery network over the globe.</li>
<li>`sta_global_with_bot`: Standard plan that supports content delivery network over the globe and bot management.</li>
<li>`ent`: Enterprise plan that supports content delivery network outside the Chinese mainland.</li>
<li>`ent_with_bot`: Enterprise plan that supports content delivery network outside the Chinese mainland and bot management.</li>
<li>`ent_cm`: Enterprise plan that supports content delivery network inside the Chinese mainland.</li>
<li>`ent_cm_with_bot`: Enterprise plan that supports content delivery network inside the Chinese mainland and bot management.</li>
<li>`ent_global`: Enterprise plan that supports content delivery network over the globe.</li>
<li>`ent_global_with_bot`: Enterprise plan that supports content delivery network over the globe and bot management.</li>To get the available plan options for your account, view the output from <a href="https://intl.cloud.tencent.com/document/product/1552/80606?from_cn_redirect=1">DescribeAvailablePlans</a>.
        :type PlanType: str
        """
        self._ZoneId = None
        self._PlanType = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def PlanType(self):
        return self._PlanType

    @PlanType.setter
    def PlanType(self, PlanType):
        self._PlanType = PlanType


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._PlanType = params.get("PlanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePlanForZoneResponse(AbstractModel):
    """CreatePlanForZone response structure.

    """

    def __init__(self):
        r"""
        :param _ResourceNames: List of purchased resources.
        :type ResourceNames: list of str
        :param _DealNames: List or order numbers.
        :type DealNames: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ResourceNames = None
        self._DealNames = None
        self._RequestId = None

    @property
    def ResourceNames(self):
        return self._ResourceNames

    @ResourceNames.setter
    def ResourceNames(self, ResourceNames):
        self._ResourceNames = ResourceNames

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResourceNames = params.get("ResourceNames")
        self._DealNames = params.get("DealNames")
        self._RequestId = params.get("RequestId")


class CreatePlanRequest(AbstractModel):
    """CreatePlan request structure.

    """

    def __init__(self):
        r"""
        :param _PlanType: Type of the subscribed plan. Valid values: <li>personal: Personal plan in prepaid mode;</li><li>basic: Basic plan in prepaid mode;</li><li>standard: Standard plan in prepaid mode;</li><li>enterprise: Enterprise plan in pay-as-you-go mode.</li>When subscribing to a prepaid plan, please ensure that your account balance is sufficient. If the balance is insufficient, an order to be paid will be generated.
For an overview of billing, see [EdgeOne Billing Overview](https://intl.cloud.tencent.com/document/product/1552/94156?from_cn_redirect=1).
For differences between plans, refer to [EdgeOne Billing Plan Comparison](https://intl.cloud.tencent.com/document/product/1552/94165?from_cn_redirect=1).
        :type PlanType: str
        :param _AutoUseVoucher: Whether to automatically use a voucher. Valid values: <li>true: Yes;</li><li>false: No.</li>This parameter is valid only when PlanType is personal, basic, or standard.
If this field is not specified, the default value 'false' will be used.
        :type AutoUseVoucher: str
        :param _PrepaidPlanParam: Parameters for subscribing to a prepaid plan. When PlanType is personal, basic, or standard, this parameter is optional and can be used to specify the subscription duration of the plan and enable auto-renewal.
If this field is not specified, the default plan duration is 1 month, with auto-renewal disabled.
        :type PrepaidPlanParam: :class:`tencentcloud.teo.v20220901.models.PrepaidPlanParam`
        """
        self._PlanType = None
        self._AutoUseVoucher = None
        self._PrepaidPlanParam = None

    @property
    def PlanType(self):
        return self._PlanType

    @PlanType.setter
    def PlanType(self, PlanType):
        self._PlanType = PlanType

    @property
    def AutoUseVoucher(self):
        return self._AutoUseVoucher

    @AutoUseVoucher.setter
    def AutoUseVoucher(self, AutoUseVoucher):
        self._AutoUseVoucher = AutoUseVoucher

    @property
    def PrepaidPlanParam(self):
        return self._PrepaidPlanParam

    @PrepaidPlanParam.setter
    def PrepaidPlanParam(self, PrepaidPlanParam):
        self._PrepaidPlanParam = PrepaidPlanParam


    def _deserialize(self, params):
        self._PlanType = params.get("PlanType")
        self._AutoUseVoucher = params.get("AutoUseVoucher")
        if params.get("PrepaidPlanParam") is not None:
            self._PrepaidPlanParam = PrepaidPlanParam()
            self._PrepaidPlanParam._deserialize(params.get("PrepaidPlanParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePlanResponse(AbstractModel):
    """CreatePlan response structure.

    """

    def __init__(self):
        r"""
        :param _PlanId: Plan ID, formatted as edgeone-2unuvzjmmn2q.
        :type PlanId: str
        :param _DealName: Order number.
        :type DealName: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PlanId = None
        self._DealName = None
        self._RequestId = None

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class CreatePrefetchTaskRequest(AbstractModel):
    """CreatePrefetchTask request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site.
        :type ZoneId: str
        :param _Targets: List of resources to be preheated. Each element format is similar to the following:
http://www.example.com/example.txt. The parameter value is currently required.
Note: The number of tasks that can be submitted is limited by the quota of a billing package. For details, see [Billing Overview] (https://intl.cloud.tencent.com/document/product/1552/77380?from_cn_redirect=1).
        :type Targets: list of str
        :param _EncodeUrl: Whether to encode a URL according to RFC3986. Enable this field when the URL contains non-ASCII characters.
        :type EncodeUrl: bool
        :param _Headers: HTTP header information
        :type Headers: list of Header
        """
        self._ZoneId = None
        self._Targets = None
        self._EncodeUrl = None
        self._Headers = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def EncodeUrl(self):
        return self._EncodeUrl

    @EncodeUrl.setter
    def EncodeUrl(self, EncodeUrl):
        self._EncodeUrl = EncodeUrl

    @property
    def Headers(self):
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Targets = params.get("Targets")
        self._EncodeUrl = params.get("EncodeUrl")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = Header()
                obj._deserialize(item)
                self._Headers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrefetchTaskResponse(AbstractModel):
    """CreatePrefetchTask response structure.

    """

    def __init__(self):
        r"""
        :param _JobId: ID of the task.
        :type JobId: str
        :param _FailedList: List of failed tasks.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FailedList: list of FailReason
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._JobId = None
        self._FailedList = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def FailedList(self):
        return self._FailedList

    @FailedList.setter
    def FailedList(self, FailedList):
        self._FailedList = FailedList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        if params.get("FailedList") is not None:
            self._FailedList = []
            for item in params.get("FailedList"):
                obj = FailReason()
                obj._deserialize(item)
                self._FailedList.append(obj)
        self._RequestId = params.get("RequestId")


class CreatePurgeTaskRequest(AbstractModel):
    """CreatePurgeTask request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site.
        :type ZoneId: str
        :param _Type: Type of cache purging. Values:
<li>`purge_url`: Purge by the URL</li>
<li>`purge_prefix`: Purge by the directory</li>
<li>`purge_host`: Purge by the hostname</li>
<li>`purge_all`: Purge all caches</li>
<li>`purge_cache_tag`: Purge by the cache-tag </li>For more details, see [Cache Purge](https://intl.cloud.tencent.com/document/product/1552/70759?from_cn_redirect=1).
        :type Type: str
        :param _Method: Node cache purge method, valid for directory, hostname, and all cache refreshes. Valid values: <li>invalidate: Refreshes only resources that were updated under the directory; </li><li>delete: Refreshes all node resources, regardless of whether they were updated. </li>Default value: invalidate.
        :type Method: str
        :param _Targets: List of resources for which cache is to be purged. Each element format depends on the cache purge type and you can refer to the API examples for details. <li>The number of tasks that can be submitted at a time is limited by the quota of a billing package. For details, see [Billing Overview] (https://intl.cloud.tencent.com/document/product/1552/77380?from_cn_redirect=1).</li>
        :type Targets: list of str
        :param _EncodeUrl: Specifies whether to transcode non-ASCII URLs according to RFC3986.
Note that if it’s enabled, the purging is based on the converted URLs.
        :type EncodeUrl: bool
        :param _CacheTag: The information attached when the node cache purge type is set to purge_cache_tag.
        :type CacheTag: :class:`tencentcloud.teo.v20220901.models.CacheTag`
        """
        self._ZoneId = None
        self._Type = None
        self._Method = None
        self._Targets = None
        self._EncodeUrl = None
        self._CacheTag = None

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
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def EncodeUrl(self):
        warnings.warn("parameter `EncodeUrl` is deprecated", DeprecationWarning) 

        return self._EncodeUrl

    @EncodeUrl.setter
    def EncodeUrl(self, EncodeUrl):
        warnings.warn("parameter `EncodeUrl` is deprecated", DeprecationWarning) 

        self._EncodeUrl = EncodeUrl

    @property
    def CacheTag(self):
        return self._CacheTag

    @CacheTag.setter
    def CacheTag(self, CacheTag):
        self._CacheTag = CacheTag


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Type = params.get("Type")
        self._Method = params.get("Method")
        self._Targets = params.get("Targets")
        self._EncodeUrl = params.get("EncodeUrl")
        if params.get("CacheTag") is not None:
            self._CacheTag = CacheTag()
            self._CacheTag._deserialize(params.get("CacheTag"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePurgeTaskResponse(AbstractModel):
    """CreatePurgeTask response structure.

    """

    def __init__(self):
        r"""
        :param _JobId: ID of the task.
        :type JobId: str
        :param _FailedList: List of failed tasks and reasons.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FailedList: list of FailReason
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._JobId = None
        self._FailedList = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def FailedList(self):
        return self._FailedList

    @FailedList.setter
    def FailedList(self, FailedList):
        self._FailedList = FailedList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        if params.get("FailedList") is not None:
            self._FailedList = []
            for item in params.get("FailedList"):
                obj = FailReason()
                obj._deserialize(item)
                self._FailedList.append(obj)
        self._RequestId = params.get("RequestId")


class CreateRealtimeLogDeliveryTaskRequest(AbstractModel):
    """CreateRealtimeLogDeliveryTask request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _TaskName: Name of a real-time log shipping task, which can contain up to 200 characters, including digits, English letters, hyphens (-) and underscores (_).
        :type TaskName: str
        :param _TaskType: Type of a real-time log shipping task. Valid values:
<li>cls: push to Tencent Cloud CLS;</li>
<li>custom_endpoint: push to a custom HTTP(S) address;</li>
<li>s3: push to an AWS S3-compatible bucket address.</li>
        :type TaskType: str
        :param _EntityList: List of entities (L7 domain names or L4 proxy instances) corresponding to a real-time log shipping task. Valid value examples:
<li>L7 domain name: domain.example.com;</li>
<li>L4 proxy instance: sid-2s69eb5wcms7.</li>
        :type EntityList: list of str
        :param _LogType: Data shipping type. Valid values:
<li>domain: site acceleration logs;</li>
<li>application: L4 proxy logs;</li>
<li>web-rateLiming: rate limit and CC attack defense logs;</li>
<li>web-attack: managed rule logs;</li>
<li>web-rule: custom rule logs;</li>
<li>web-bot: Bot management logs.</li>
        :type LogType: str
        :param _Area: Data shipping area. Valid values:
<li>mainland: within the Chinese mainland;</li>
<li>overseas: global (excluding the Chinese mainland).</li>
        :type Area: str
        :param _Fields: List of predefined fields for shipping.
        :type Fields: list of str
        :param _CustomFields: List of custom fields for shipping. It supports extracting specified field values from HTTP request headers, response headers, and cookies. The name of each custom field must be unique and the maximum number of fields is 200.
        :type CustomFields: list of CustomField
        :param _DeliveryConditions: Filter criteria of log shipping. If this parameter is not input, all logs will be shipped.
        :type DeliveryConditions: list of DeliveryCondition
        :param _Sample: Sampling ratio in permille. Value range: 1-1000. For example, 605 indicates a sampling ratio of 60.5%. If this parameter is not input, the sampling ratio is 100%.
        :type Sample: int
        :param _LogFormat: Output format for log delivery. If this field is not specified, the default format is used, which works as follows:
<li>When TaskType is 'custom_endpoint', the default format is an array of JSON objects, with each JSON object representing a log entry;</li>
<li>When TaskType is 's3', the default format is JSON Lines;</li>Specifically, when TaskType is 'cls', the only allowed value for LogFormat.FormatType is 'json', and other parameters in LogFormat will be ignored. It is recommended not to transfer LogFormat.
        :type LogFormat: :class:`tencentcloud.teo.v20220901.models.LogFormat`
        :param _CLS: Configuration information of CLS. This parameter is required when TaskType is cls.
        :type CLS: :class:`tencentcloud.teo.v20220901.models.CLSTopic`
        :param _CustomEndpoint: Configuration information of the custom HTTP service. This parameter is required when TaskType is custom_endpoint.
        :type CustomEndpoint: :class:`tencentcloud.teo.v20220901.models.CustomEndpoint`
        :param _S3: Configuration information of the AWS S3-compatible bucket. This parameter is required when TaskType is s3.
        :type S3: :class:`tencentcloud.teo.v20220901.models.S3`
        """
        self._ZoneId = None
        self._TaskName = None
        self._TaskType = None
        self._EntityList = None
        self._LogType = None
        self._Area = None
        self._Fields = None
        self._CustomFields = None
        self._DeliveryConditions = None
        self._Sample = None
        self._LogFormat = None
        self._CLS = None
        self._CustomEndpoint = None
        self._S3 = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def EntityList(self):
        return self._EntityList

    @EntityList.setter
    def EntityList(self, EntityList):
        self._EntityList = EntityList

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Fields(self):
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields

    @property
    def CustomFields(self):
        return self._CustomFields

    @CustomFields.setter
    def CustomFields(self, CustomFields):
        self._CustomFields = CustomFields

    @property
    def DeliveryConditions(self):
        return self._DeliveryConditions

    @DeliveryConditions.setter
    def DeliveryConditions(self, DeliveryConditions):
        self._DeliveryConditions = DeliveryConditions

    @property
    def Sample(self):
        return self._Sample

    @Sample.setter
    def Sample(self, Sample):
        self._Sample = Sample

    @property
    def LogFormat(self):
        return self._LogFormat

    @LogFormat.setter
    def LogFormat(self, LogFormat):
        self._LogFormat = LogFormat

    @property
    def CLS(self):
        return self._CLS

    @CLS.setter
    def CLS(self, CLS):
        self._CLS = CLS

    @property
    def CustomEndpoint(self):
        return self._CustomEndpoint

    @CustomEndpoint.setter
    def CustomEndpoint(self, CustomEndpoint):
        self._CustomEndpoint = CustomEndpoint

    @property
    def S3(self):
        return self._S3

    @S3.setter
    def S3(self, S3):
        self._S3 = S3


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._TaskName = params.get("TaskName")
        self._TaskType = params.get("TaskType")
        self._EntityList = params.get("EntityList")
        self._LogType = params.get("LogType")
        self._Area = params.get("Area")
        self._Fields = params.get("Fields")
        if params.get("CustomFields") is not None:
            self._CustomFields = []
            for item in params.get("CustomFields"):
                obj = CustomField()
                obj._deserialize(item)
                self._CustomFields.append(obj)
        if params.get("DeliveryConditions") is not None:
            self._DeliveryConditions = []
            for item in params.get("DeliveryConditions"):
                obj = DeliveryCondition()
                obj._deserialize(item)
                self._DeliveryConditions.append(obj)
        self._Sample = params.get("Sample")
        if params.get("LogFormat") is not None:
            self._LogFormat = LogFormat()
            self._LogFormat._deserialize(params.get("LogFormat"))
        if params.get("CLS") is not None:
            self._CLS = CLSTopic()
            self._CLS._deserialize(params.get("CLS"))
        if params.get("CustomEndpoint") is not None:
            self._CustomEndpoint = CustomEndpoint()
            self._CustomEndpoint._deserialize(params.get("CustomEndpoint"))
        if params.get("S3") is not None:
            self._S3 = S3()
            self._S3._deserialize(params.get("S3"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRealtimeLogDeliveryTaskResponse(AbstractModel):
    """CreateRealtimeLogDeliveryTask response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: ID of the successfully created task.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class CreateRuleRequest(AbstractModel):
    """CreateRule request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site
        :type ZoneId: str
        :param _RuleName: The rule name (1 to 255 characters)
        :type RuleName: str
        :param _Status: Rule status. Values:
<li>`enable`: Enabled</li>
<li>`disable`: Disabled</li>
        :type Status: str
        :param _Rules: The rule content.
        :type Rules: list of Rule
        :param _Tags: Tag of the rule.
        :type Tags: list of str
        """
        self._ZoneId = None
        self._RuleName = None
        self._Status = None
        self._Rules = None
        self._Tags = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RuleName = params.get("RuleName")
        self._Status = params.get("Status")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = Rule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRuleResponse(AbstractModel):
    """CreateRule response structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleId = None
        self._RequestId = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class CreateSecurityIPGroupRequest(AbstractModel):
    """CreateSecurityIPGroup request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID.
        :type ZoneId: str
        :param _IPGroup: IP group information.
        :type IPGroup: :class:`tencentcloud.teo.v20220901.models.IPGroup`
        """
        self._ZoneId = None
        self._IPGroup = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def IPGroup(self):
        return self._IPGroup

    @IPGroup.setter
    def IPGroup(self, IPGroup):
        self._IPGroup = IPGroup


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("IPGroup") is not None:
            self._IPGroup = IPGroup()
            self._IPGroup._deserialize(params.get("IPGroup"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityIPGroupResponse(AbstractModel):
    """CreateSecurityIPGroup response structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: IP group ID.
        :type GroupId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class CreateSharedCNAMERequest(AbstractModel):
    """CreateSharedCNAME request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site to which the shared CNAME belongs.	
        :type ZoneId: str
        :param _SharedCNAMEPrefix: Shared CNAME prefix. Enter a valid domain name prefix, such as "test-api" and "test-api.com". A maximum of 50 characters are allowed. 

Complete format of the shared CNAME: '<Custom prefix>+<A 12-character random string in ZoneId>+share.dnse[0-5].com'. 

For example, if the prefix is example.com, EdgeOne will create the shared CNAME: example.com.sai2ig51kaa5.share.dnse2.com.
        :type SharedCNAMEPrefix: str
        :param _Description: Description. It supports 1-50 characters.
        :type Description: str
        """
        self._ZoneId = None
        self._SharedCNAMEPrefix = None
        self._Description = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def SharedCNAMEPrefix(self):
        return self._SharedCNAMEPrefix

    @SharedCNAMEPrefix.setter
    def SharedCNAMEPrefix(self, SharedCNAMEPrefix):
        self._SharedCNAMEPrefix = SharedCNAMEPrefix

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._SharedCNAMEPrefix = params.get("SharedCNAMEPrefix")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSharedCNAMEResponse(AbstractModel):
    """CreateSharedCNAME response structure.

    """

    def __init__(self):
        r"""
        :param _SharedCNAME: Shared CNAME. Format: '<Custom prefix>+<A 12-character random string in ZoneId>+share.dnse[0-5].com'.
        :type SharedCNAME: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SharedCNAME = None
        self._RequestId = None

    @property
    def SharedCNAME(self):
        return self._SharedCNAME

    @SharedCNAME.setter
    def SharedCNAME(self, SharedCNAME):
        self._SharedCNAME = SharedCNAME

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SharedCNAME = params.get("SharedCNAME")
        self._RequestId = params.get("RequestId")


class CreateZoneRequest(AbstractModel):
    """CreateZone request structure.

    """

    def __init__(self):
        r"""
        :param _Type: Site access type. If this parameter is not input, the default value `partial` is used. Valid values of this parameter are as follows:
<li>partial: CNAME access;</li>
<li>full: NS access;</li>
<li>noDomainAccess: access with no domain name.</li>
<li>dnsPodAccess: DNSPod hosted access. To use this access mode, your domain name should have been hosted on DNSPod.</li>
        :type Type: str
        :param _ZoneName: Site name. For sites connected via CNAME/NS, pass in the secondary domain name (example.com). Leave it blank if the site is connected without a domain name. 
        :type ZoneName: str
        :param _Area: The acceleration area of the L7 domain name when `Type` is `partial` or `full`. When Type is `noDomainAccess`, please leave it blank.
<li>`global`: Global AZs</li>
<li>`mainland`: AZs in the Chinese mainland</li>
<li>`overseas`: (Default) AZs outside the Chinese mainland </li>
        :type Area: str
        :param _PlanId: ID of the plan to which you want to bind the site. If you don't have an EdgeOne plan, purchase one in the EdgeOne console.
        :type PlanId: str
        :param _AliasZoneName: The site alias. It allows up to 20 characters, including [0-9], [a-z], [A-Z] and [-_]. For details, see [Glossary](https://intl.cloud.tencent.com/document/product/1552/70202?from_cn_redirect=1). If you don't want to use it, just leave it blank.
        :type AliasZoneName: str
        :param _Tags: Tags of the site. To create tags, go to the [Tag Console](https://console.cloud.tencent.com/tag/taglist).
        :type Tags: list of Tag
        :param _AllowDuplicates: Whether to allow duplicate sites. Values:
<li>`true`: Duplicate sites are allowed.</li>
<li>`false`: Duplicate sites are not allowed.</li>If it is left empty, the default value `false` is used.
        :type AllowDuplicates: bool
        :param _JumpStart: Whether to skip scanning the existing DNS records of the site. Default value: false.
        :type JumpStart: bool
        """
        self._Type = None
        self._ZoneName = None
        self._Area = None
        self._PlanId = None
        self._AliasZoneName = None
        self._Tags = None
        self._AllowDuplicates = None
        self._JumpStart = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def AliasZoneName(self):
        return self._AliasZoneName

    @AliasZoneName.setter
    def AliasZoneName(self, AliasZoneName):
        self._AliasZoneName = AliasZoneName

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AllowDuplicates(self):
        warnings.warn("parameter `AllowDuplicates` is deprecated", DeprecationWarning) 

        return self._AllowDuplicates

    @AllowDuplicates.setter
    def AllowDuplicates(self, AllowDuplicates):
        warnings.warn("parameter `AllowDuplicates` is deprecated", DeprecationWarning) 

        self._AllowDuplicates = AllowDuplicates

    @property
    def JumpStart(self):
        warnings.warn("parameter `JumpStart` is deprecated", DeprecationWarning) 

        return self._JumpStart

    @JumpStart.setter
    def JumpStart(self, JumpStart):
        warnings.warn("parameter `JumpStart` is deprecated", DeprecationWarning) 

        self._JumpStart = JumpStart


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._ZoneName = params.get("ZoneName")
        self._Area = params.get("Area")
        self._PlanId = params.get("PlanId")
        self._AliasZoneName = params.get("AliasZoneName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AllowDuplicates = params.get("AllowDuplicates")
        self._JumpStart = params.get("JumpStart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateZoneResponse(AbstractModel):
    """CreateZone response structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID.
        :type ZoneId: str
        :param _OwnershipVerification: Site ownership verification information. After the site is created, you need to complete the ownership verification before the site can serve normally.

If `Type=partial`, add TXT records to your DNS provider or add files to the root DNS server, and then call [VerifyOwnership]() to complete verification. For more information, see [Ownership Verification](https://intl.cloud.tencent.com/document/product/1552/70789?from_cn_redirect=1).

If `Type = full`, switch the DNS server as instructed by [Modifying DNS Server](https://intl.cloud.tencent.com/document/product/1552/90452?from_cn_redirect=1). Then call [VerifyOwnership]() to check the result.

If `Type = noDomainAccess`, leave it blank. No action is required.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type OwnershipVerification: :class:`tencentcloud.teo.v20220901.models.OwnershipVerification`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ZoneId = None
        self._OwnershipVerification = None
        self._RequestId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def OwnershipVerification(self):
        return self._OwnershipVerification

    @OwnershipVerification.setter
    def OwnershipVerification(self, OwnershipVerification):
        self._OwnershipVerification = OwnershipVerification

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("OwnershipVerification") is not None:
            self._OwnershipVerification = OwnershipVerification()
            self._OwnershipVerification._deserialize(params.get("OwnershipVerification"))
        self._RequestId = params.get("RequestId")


class CustomEndpoint(AbstractModel):
    """The configuration information of real-time log delivery to a custom HTTP(S) interface

    """

    def __init__(self):
        r"""
        :param _Url: Address of the custom HTTP API for real-time log shipping. Currently, only HTTP and HTTPS protocols are supported.
        :type Url: str
        :param _AccessId: Custom SecretId used for generating an encrypted signature. This parameter is required if the origin server needs authentication.
        :type AccessId: str
        :param _AccessKey: Custom SecretKey used for generating an encrypted signature. This parameter is required if the origin server needs authentication.
        :type AccessKey: str
        :param _CompressType: Type of data compression. Valid values:<li>gzip: gzip compression.</li>If this parameter is not input, compression is disabled.
        :type CompressType: str
        :param _Protocol: Type of the application layer protocol used in POST requests for log shipping. Valid values: 
<li>http: HTTP protocol;</li>
<li>https: HTTPS protocol.</li>If this parameter is not input, the protocol type is parsed from the URL field.	
        :type Protocol: str
        :param _Headers: Custom request header carried in log shipping. For a header carried by default in EdgeOne log pushing, such as Content-Type, the header value you input will overwrite the default value. The header value references a single variable ${batchSize} to obtain the number of log entries included in each POST request.
        :type Headers: list of Header
        """
        self._Url = None
        self._AccessId = None
        self._AccessKey = None
        self._CompressType = None
        self._Protocol = None
        self._Headers = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def AccessId(self):
        return self._AccessId

    @AccessId.setter
    def AccessId(self, AccessId):
        self._AccessId = AccessId

    @property
    def AccessKey(self):
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def CompressType(self):
        return self._CompressType

    @CompressType.setter
    def CompressType(self, CompressType):
        self._CompressType = CompressType

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Headers(self):
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._AccessId = params.get("AccessId")
        self._AccessKey = params.get("AccessKey")
        self._CompressType = params.get("CompressType")
        self._Protocol = params.get("Protocol")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = Header()
                obj._deserialize(item)
                self._Headers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomErrorPage(AbstractModel):
    """Custom error code page structure.

    """

    def __init__(self):
        r"""
        :param _PageId: Custom error page ID.
        :type PageId: str
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _Name: Custom error page name.
        :type Name: str
        :param _ContentType: Custom error page type.
        :type ContentType: str
        :param _Description: Custom error page description.
        :type Description: str
        :param _Content: Custom error page content.
        :type Content: str
        :param _References: Custom error page reference.
        :type References: list of ErrorPageReference
        """
        self._PageId = None
        self._ZoneId = None
        self._Name = None
        self._ContentType = None
        self._Description = None
        self._Content = None
        self._References = None

    @property
    def PageId(self):
        return self._PageId

    @PageId.setter
    def PageId(self, PageId):
        self._PageId = PageId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ContentType(self):
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def References(self):
        return self._References

    @References.setter
    def References(self, References):
        self._References = References


    def _deserialize(self, params):
        self._PageId = params.get("PageId")
        self._ZoneId = params.get("ZoneId")
        self._Name = params.get("Name")
        self._ContentType = params.get("ContentType")
        self._Description = params.get("Description")
        self._Content = params.get("Content")
        if params.get("References") is not None:
            self._References = []
            for item in params.get("References"):
                obj = ErrorPageReference()
                obj._deserialize(item)
                self._References.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomField(AbstractModel):
    """The custom log field in a real-time log delivery task

    """

    def __init__(self):
        r"""
        :param _Name: Extracts data from specified positions in HTTP requests and responses. Valid values:
<li>ReqHeader: Extract a specified field value from an HTTP request header;</li>
<li>RspHeader: Extract a specified field value from an HTTP response header;</li>
<li>cookie: Extract a specified field value from a cookie.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _Value: Indicates the name of the parameter from which a value needs to be extracted, such as Accept-Language.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: str
        :param _Enabled: Indicates whether to deliver this field. If not filled in, this field will not be delivered.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Enabled: bool
        """
        self._Name = None
        self._Value = None
        self._Enabled = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoS(AbstractModel):
    """DDoS mitigation configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Switch. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSAttackEvent(AbstractModel):
    """Information of the DDoS attacker

    """

    def __init__(self):
        r"""
        :param _EventId: The event ID.
        :type EventId: str
        :param _AttackType: The attack type.
        :type AttackType: str
        :param _AttackStatus: The attack status.
        :type AttackStatus: int
        :param _AttackMaxBandWidth: The maximum attack bandwidth.
        :type AttackMaxBandWidth: int
        :param _AttackPacketMaxRate: The peak attack packet rate.
        :type AttackPacketMaxRate: int
        :param _AttackStartTime: The attack start time recorded in seconds.
        :type AttackStartTime: int
        :param _AttackEndTime: The attack end time recorded in seconds.
        :type AttackEndTime: int
        :param _PolicyId: The DDoS policy ID. 
Note: This field may return `null`, indicating that no valid value was found.
        :type PolicyId: int
        :param _ZoneId: The site ID. 
Note: This field may return `null`, indicating that no valid value was found.
        :type ZoneId: str
        :param _Area: Geolocation scope. Values: 
<li>`overseas`: Regions outside the Chinese mainland</li>
<li>`mainland`: Chinese mainland</li>
Note: This field may return `null`, indicating that no valid value was found.
        :type Area: str
        :param _DDoSBlockData: The blocking time of a DDoS attack. 
Note: This field may return `null`, indicating that no valid value was found.
        :type DDoSBlockData: list of DDoSBlockData
        """
        self._EventId = None
        self._AttackType = None
        self._AttackStatus = None
        self._AttackMaxBandWidth = None
        self._AttackPacketMaxRate = None
        self._AttackStartTime = None
        self._AttackEndTime = None
        self._PolicyId = None
        self._ZoneId = None
        self._Area = None
        self._DDoSBlockData = None

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def AttackType(self):
        return self._AttackType

    @AttackType.setter
    def AttackType(self, AttackType):
        self._AttackType = AttackType

    @property
    def AttackStatus(self):
        return self._AttackStatus

    @AttackStatus.setter
    def AttackStatus(self, AttackStatus):
        self._AttackStatus = AttackStatus

    @property
    def AttackMaxBandWidth(self):
        return self._AttackMaxBandWidth

    @AttackMaxBandWidth.setter
    def AttackMaxBandWidth(self, AttackMaxBandWidth):
        self._AttackMaxBandWidth = AttackMaxBandWidth

    @property
    def AttackPacketMaxRate(self):
        return self._AttackPacketMaxRate

    @AttackPacketMaxRate.setter
    def AttackPacketMaxRate(self, AttackPacketMaxRate):
        self._AttackPacketMaxRate = AttackPacketMaxRate

    @property
    def AttackStartTime(self):
        return self._AttackStartTime

    @AttackStartTime.setter
    def AttackStartTime(self, AttackStartTime):
        self._AttackStartTime = AttackStartTime

    @property
    def AttackEndTime(self):
        return self._AttackEndTime

    @AttackEndTime.setter
    def AttackEndTime(self, AttackEndTime):
        self._AttackEndTime = AttackEndTime

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def DDoSBlockData(self):
        return self._DDoSBlockData

    @DDoSBlockData.setter
    def DDoSBlockData(self, DDoSBlockData):
        self._DDoSBlockData = DDoSBlockData


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._AttackType = params.get("AttackType")
        self._AttackStatus = params.get("AttackStatus")
        self._AttackMaxBandWidth = params.get("AttackMaxBandWidth")
        self._AttackPacketMaxRate = params.get("AttackPacketMaxRate")
        self._AttackStartTime = params.get("AttackStartTime")
        self._AttackEndTime = params.get("AttackEndTime")
        self._PolicyId = params.get("PolicyId")
        self._ZoneId = params.get("ZoneId")
        self._Area = params.get("Area")
        if params.get("DDoSBlockData") is not None:
            self._DDoSBlockData = []
            for item in params.get("DDoSBlockData"):
                obj = DDoSBlockData()
                obj._deserialize(item)
                self._DDoSBlockData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSBlockData(AbstractModel):
    """DDoS blocking details

    """

    def __init__(self):
        r"""
        :param _StartTime: The start time recorded in UNIX timestamp.
        :type StartTime: int
        :param _EndTime: The end time recorded in UNIX timestamp. `0` indicates the blocking is ongoing.
        :type EndTime: int
        :param _BlockArea: The regions blocked.
        :type BlockArea: str
        """
        self._StartTime = None
        self._EndTime = None
        self._BlockArea = None

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
    def BlockArea(self):
        return self._BlockArea

    @BlockArea.setter
    def BlockArea(self, BlockArea):
        self._BlockArea = BlockArea


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._BlockArea = params.get("BlockArea")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDosProtectionConfig(AbstractModel):
    """Exclusive DDoS protection specifications configuration applicable to Layer 4 proxy or web site service.

    """

    def __init__(self):
        r"""
        :param _LevelMainland: Dedicated anti-DDoS specifications in the Chinese mainland. For details, refer to [Dedicated Anti-DDoS Related Fees](https://intl.cloud.tencent.com/document/product/1552/94162?from_cn_redirect=1).
<li>PLATFORM: uses the default protection. Dedicated anti-DDoS is not enabled;</li>
<li>BASE30_MAX300: uses dedicated anti-DDoS, which provides 30 Gbps guaranteed protection bandwidth and up to 300 Gbps elastic protection bandwidth;</li>
<li>BASE60_MAX600: uses dedicated anti-DDoS, which provides 60 Gbps guaranteed protection bandwidth and up to 600 Gbps elastic protection bandwidth. </li>If this field is not specified, the default value 'PLATFORM' will be used.
        :type LevelMainland: str
        :param _MaxBandwidthMainland: Configuration of elastic protection bandwidth for exclusive DDoS protection in the Chinese mainland.Valid only when exclusive DDoS protection in the Chinese mainland is enabled (refer to the LevelMainland parameter configuration), and the value has the following limitations:<li>When exclusive DDoS protection is enabled in the Chinese mainland and the 30 Gbps baseline protection bandwidth is used (the LevelMainland parameter value is BASE30_MAX300): the value range is 30 to 300 in Gbps;</li><li>When exclusive DDoS protection is enabled in the Chinese mainland and the 60 Gbps baseline protection bandwidth is used (the LevelMainland parameter value is BASE60_MAX600): the value range is 60 to 600 in Gbps;</li><li>When the default protection of the platform is used (the LevelMainland parameter value is PLATFORM): configuration is not supported, and the value of this parameter is invalid.</li>
        :type MaxBandwidthMainland: int
        :param _LevelOverseas: Dedicated anti-DDoS specifications in global regions (excluding the Chinese mainland).
<li>PLATFORM: uses the default protection. Dedicated anti-DDoS is not enabled;</li>
<li>ANYCAST300: uses dedicated anti-DDoS, which provides 300 Gbps protection bandwidth;</li>
<li>ANYCAST_ALLIN: uses dedicated anti-DDoS, which provides all available protection resources. </li>If this field is not specified, the default value 'PLATFORM' will be used.
        :type LevelOverseas: str
        """
        self._LevelMainland = None
        self._MaxBandwidthMainland = None
        self._LevelOverseas = None

    @property
    def LevelMainland(self):
        return self._LevelMainland

    @LevelMainland.setter
    def LevelMainland(self, LevelMainland):
        self._LevelMainland = LevelMainland

    @property
    def MaxBandwidthMainland(self):
        return self._MaxBandwidthMainland

    @MaxBandwidthMainland.setter
    def MaxBandwidthMainland(self, MaxBandwidthMainland):
        self._MaxBandwidthMainland = MaxBandwidthMainland

    @property
    def LevelOverseas(self):
        return self._LevelOverseas

    @LevelOverseas.setter
    def LevelOverseas(self, LevelOverseas):
        self._LevelOverseas = LevelOverseas


    def _deserialize(self, params):
        self._LevelMainland = params.get("LevelMainland")
        self._MaxBandwidthMainland = params.get("MaxBandwidthMainland")
        self._LevelOverseas = params.get("LevelOverseas")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DefaultServerCertInfo(AbstractModel):
    """HTTPS server certificate configuration

    """

    def __init__(self):
        r"""
        :param _CertId: ID of the server certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertId: str
        :param _Alias: Alias of the certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Alias: str
        :param _Type: Type of the certificate. Values:
<li>`default`: Default certificate;</li>
<li>`upload`: Custom certificate;</li>
<li>`managed`: Tencent Cloud-managed certificate.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param _ExpireTime: Time when the certificate expires.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param _EffectiveTime: Time when the certificate takes effect.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EffectiveTime: str
        :param _CommonName: Common name of the certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CommonName: str
        :param _SubjectAltName: Domain names added to the SAN certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubjectAltName: list of str
        :param _Status: Deployment status. Values:
<li>`processing`: Deployment in progress</li>
<li>`deployed`: Deployed</li>
<li>`failed`: Deployment failed</li>
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Status: str
        :param _Message: Failure description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param _SignAlgo: Certificate algorithm.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SignAlgo: str
        """
        self._CertId = None
        self._Alias = None
        self._Type = None
        self._ExpireTime = None
        self._EffectiveTime = None
        self._CommonName = None
        self._SubjectAltName = None
        self._Status = None
        self._Message = None
        self._SignAlgo = None

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def EffectiveTime(self):
        return self._EffectiveTime

    @EffectiveTime.setter
    def EffectiveTime(self, EffectiveTime):
        self._EffectiveTime = EffectiveTime

    @property
    def CommonName(self):
        return self._CommonName

    @CommonName.setter
    def CommonName(self, CommonName):
        self._CommonName = CommonName

    @property
    def SubjectAltName(self):
        return self._SubjectAltName

    @SubjectAltName.setter
    def SubjectAltName(self, SubjectAltName):
        self._SubjectAltName = SubjectAltName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def SignAlgo(self):
        return self._SignAlgo

    @SignAlgo.setter
    def SignAlgo(self, SignAlgo):
        self._SignAlgo = SignAlgo


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._Alias = params.get("Alias")
        self._Type = params.get("Type")
        self._ExpireTime = params.get("ExpireTime")
        self._EffectiveTime = params.get("EffectiveTime")
        self._CommonName = params.get("CommonName")
        self._SubjectAltName = params.get("SubjectAltName")
        self._Status = params.get("Status")
        self._Message = params.get("Message")
        self._SignAlgo = params.get("SignAlgo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccelerationDomainsRequest(AbstractModel):
    """DeleteAccelerationDomains request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site related with the accelerated domain name.
        :type ZoneId: str
        :param _DomainNames: List of accelerated domain names to be deleted.
        :type DomainNames: list of str
        :param _Force: Whether to forcibly delete a domain name if it is associated with resources (such as alias domain names and traffic scheduling policies). 
<li>`true`: Delete the domain name and all associated resources.</li>
<li>`false`: Do not delete the domain name and all associated resources.</li>If it’s not specified, the default value `false` is used.
        :type Force: bool
        """
        self._ZoneId = None
        self._DomainNames = None
        self._Force = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def DomainNames(self):
        return self._DomainNames

    @DomainNames.setter
    def DomainNames(self, DomainNames):
        self._DomainNames = DomainNames

    @property
    def Force(self):
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._DomainNames = params.get("DomainNames")
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccelerationDomainsResponse(AbstractModel):
    """DeleteAccelerationDomains response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DeleteAliasDomainRequest(AbstractModel):
    """DeleteAliasDomain request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: The site ID.
        :type ZoneId: str
        :param _AliasNames: The alias domain name to be deleted. If it is left empty, the delete operation is not performed.
        :type AliasNames: list of str
        """
        self._ZoneId = None
        self._AliasNames = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def AliasNames(self):
        return self._AliasNames

    @AliasNames.setter
    def AliasNames(self, AliasNames):
        self._AliasNames = AliasNames


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._AliasNames = params.get("AliasNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAliasDomainResponse(AbstractModel):
    """DeleteAliasDomain response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DeleteApplicationProxyRequest(AbstractModel):
    """DeleteApplicationProxy request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: The site ID.
        :type ZoneId: str
        :param _ProxyId: The proxy ID.
        :type ProxyId: str
        """
        self._ZoneId = None
        self._ProxyId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationProxyResponse(AbstractModel):
    """DeleteApplicationProxy response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DeleteApplicationProxyRuleRequest(AbstractModel):
    """DeleteApplicationProxyRule request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: The site ID.
        :type ZoneId: str
        :param _ProxyId: The proxy ID.
        :type ProxyId: str
        :param _RuleId: The rule ID.
        :type RuleId: str
        """
        self._ZoneId = None
        self._ProxyId = None
        self._RuleId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationProxyRuleResponse(AbstractModel):
    """DeleteApplicationProxyRule response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DeleteCustomErrorPageRequest(AbstractModel):
    """DeleteCustomErrorPage request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _PageId: Custom page ID.
        :type PageId: str
        """
        self._ZoneId = None
        self._PageId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def PageId(self):
        return self._PageId

    @PageId.setter
    def PageId(self, PageId):
        self._PageId = PageId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._PageId = params.get("PageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomErrorPageResponse(AbstractModel):
    """DeleteCustomErrorPage response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DeleteFunctionRequest(AbstractModel):
    """DeleteFunction request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _FunctionId: Function ID.
        :type FunctionId: str
        """
        self._ZoneId = None
        self._FunctionId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def FunctionId(self):
        return self._FunctionId

    @FunctionId.setter
    def FunctionId(self, FunctionId):
        self._FunctionId = FunctionId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._FunctionId = params.get("FunctionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFunctionResponse(AbstractModel):
    """DeleteFunction response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DeleteFunctionRulesRequest(AbstractModel):
    """DeleteFunctionRules request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _RuleIds: Rule ID list.
        :type RuleIds: list of str
        """
        self._ZoneId = None
        self._RuleIds = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RuleIds(self):
        return self._RuleIds

    @RuleIds.setter
    def RuleIds(self, RuleIds):
        self._RuleIds = RuleIds


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RuleIds = params.get("RuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFunctionRulesResponse(AbstractModel):
    """DeleteFunctionRules response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DeleteL4ProxyRequest(AbstractModel):
    """DeleteL4Proxy request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _ProxyId: Layer 4 proxy instance ID.
        :type ProxyId: str
        """
        self._ZoneId = None
        self._ProxyId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteL4ProxyResponse(AbstractModel):
    """DeleteL4Proxy response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DeleteL4ProxyRulesRequest(AbstractModel):
    """DeleteL4ProxyRules request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _ProxyId: Layer 4 proxy instance ID.
        :type ProxyId: str
        :param _RuleIds: List of forwarding rule IDs. It supports up to 200 forwarding rules at a time.
        :type RuleIds: list of str
        """
        self._ZoneId = None
        self._ProxyId = None
        self._RuleIds = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def RuleIds(self):
        return self._RuleIds

    @RuleIds.setter
    def RuleIds(self, RuleIds):
        self._RuleIds = RuleIds


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        self._RuleIds = params.get("RuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteL4ProxyRulesResponse(AbstractModel):
    """DeleteL4ProxyRules response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DeleteOriginGroupRequest(AbstractModel):
    """DeleteOriginGroup request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _GroupId: Origin server group ID. This parameter is required.
        :type GroupId: str
        """
        self._ZoneId = None
        self._GroupId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOriginGroupResponse(AbstractModel):
    """DeleteOriginGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DeleteRealtimeLogDeliveryTaskRequest(AbstractModel):
    """DeleteRealtimeLogDeliveryTask request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _TaskId: The ID of the real-time log delivery task.
        :type TaskId: str
        """
        self._ZoneId = None
        self._TaskId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRealtimeLogDeliveryTaskResponse(AbstractModel):
    """DeleteRealtimeLogDeliveryTask response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DeleteRulesRequest(AbstractModel):
    """DeleteRules request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site
        :type ZoneId: str
        :param _RuleIds: IDs of the rules to be deleted.
        :type RuleIds: list of str
        """
        self._ZoneId = None
        self._RuleIds = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RuleIds(self):
        return self._RuleIds

    @RuleIds.setter
    def RuleIds(self, RuleIds):
        self._RuleIds = RuleIds


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RuleIds = params.get("RuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRulesResponse(AbstractModel):
    """DeleteRules response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DeleteSecurityIPGroupRequest(AbstractModel):
    """DeleteSecurityIPGroup request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID.
        :type ZoneId: str
        :param _GroupId: IP group ID.
        :type GroupId: int
        """
        self._ZoneId = None
        self._GroupId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityIPGroupResponse(AbstractModel):
    """DeleteSecurityIPGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DeleteSharedCNAMERequest(AbstractModel):
    """DeleteSharedCNAME request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site to which the shared CNAME belongs.
        :type ZoneId: str
        :param _SharedCNAME: The shared CNAME to be deleted
        :type SharedCNAME: str
        """
        self._ZoneId = None
        self._SharedCNAME = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def SharedCNAME(self):
        return self._SharedCNAME

    @SharedCNAME.setter
    def SharedCNAME(self, SharedCNAME):
        self._SharedCNAME = SharedCNAME


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._SharedCNAME = params.get("SharedCNAME")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSharedCNAMEResponse(AbstractModel):
    """DeleteSharedCNAME response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DeleteZoneRequest(AbstractModel):
    """DeleteZone request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: The site ID.
        :type ZoneId: str
        """
        self._ZoneId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteZoneResponse(AbstractModel):
    """DeleteZone response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DeliveryCondition(AbstractModel):
    """Real-time log delivery conditions used to define the scope of log delivery. The relationship between items in a DeliveryCondition array is "or", whereas the relationship between items in an inner Conditions array is "and".

    """

    def __init__(self):
        r"""
        :param _Conditions: Log filter criteria. The detailed filter criteria are as follows:
<li>EdgeResponseStatusCode: Filter by response status code returned from the EdgeOne node to the client.<br>?? Supported operators: equal, great, less, great_equal, less_equal<br>?? Valid values: any integer greater than or equal to 0</li>
<li>OriginResponseStatusCode: Filter by response status code of the origin server.<br>?? Supported operators: equal, great, less, great_equal, less_equal.<br>?? Valid values: any integer greater than or equal to -1</li>
<li>SecurityAction: Filter by final action after the request matches a security rule.<br>?? Supported operator: equal<br>?? Options:<br>?? -: unknown/not matched<br>?? Monitor: observation<br>?? JSChallenge: JavaScript challenge<br>?? Deny: blocking<br>?? Allow: allowing<br>?? BlockIP: IP blocking<br>?? Redirect: redirection<br>?? ReturnCustomPage: returning to a custom page<br>?? ManagedChallenge: managed challenge<br>?? Silence: silence<br>?? LongDelay: response after a long delay<br>?? ShortDelay: response after a short delay</li>
<li>SecurityModule: Filter by name of the security module finally handling the request.<br>??Supported operator: equal<br>??Options:<br>?? -: unknown/not matched<br>?? CustomRule: Custom Rules in Web Protection<br>?? RateLimitingCustomRule: Rate Limiting Rules in Web Protection<br>?? ManagedRule: Managed Rules in Web Protection<br>?? L7DDoS: CC Attack Defense in Web Protection<br>?? BotManagement: Bot Basic Management in Bot Management<br>?? BotClientReputation: Client Reputation Analysis in Bot Management<br>?? BotBehaviorAnalysis: Bot Intelligent Analysis in Bot Management<br>?? BotCustomRule: Custom Bot Rules in Bot Management<br>?? BotActiveDetection: Active Detection in Bot Management</li>
        :type Conditions: list of QueryCondition
        """
        self._Conditions = None

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions


    def _deserialize(self, params):
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = QueryCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployConfigGroupVersionRequest(AbstractModel):
    """DeployConfigGroupVersion request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _EnvId: Environment ID. Please specify the environment ID to which the version should be released.
        :type EnvId: str
        :param _ConfigGroupVersionInfos: Version information required for release. Multiple versions of different configuration groups can be modified simultaneously, while each group allows modifying only one version at a time.
        :type ConfigGroupVersionInfos: list of ConfigGroupVersionInfo
        :param _Description: Change description. It is used to describe the content and reasons for this change. A maximum of 100 characters are supported.
        :type Description: str
        """
        self._ZoneId = None
        self._EnvId = None
        self._ConfigGroupVersionInfos = None
        self._Description = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ConfigGroupVersionInfos(self):
        return self._ConfigGroupVersionInfos

    @ConfigGroupVersionInfos.setter
    def ConfigGroupVersionInfos(self, ConfigGroupVersionInfos):
        self._ConfigGroupVersionInfos = ConfigGroupVersionInfos

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._EnvId = params.get("EnvId")
        if params.get("ConfigGroupVersionInfos") is not None:
            self._ConfigGroupVersionInfos = []
            for item in params.get("ConfigGroupVersionInfos"):
                obj = ConfigGroupVersionInfo()
                obj._deserialize(item)
                self._ConfigGroupVersionInfos.append(obj)
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployConfigGroupVersionResponse(AbstractModel):
    """DeployConfigGroupVersion response structure.

    """

    def __init__(self):
        r"""
        :param _RecordId: Release record ID.
        :type RecordId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RecordId = None
        self._RequestId = None

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RecordId = params.get("RecordId")
        self._RequestId = params.get("RequestId")


class DeployRecord(AbstractModel):
    """Version release record details for the configuration group.

    """

    def __init__(self):
        r"""
        :param _ConfigGroupVersionInfos: Details about the released version.
        :type ConfigGroupVersionInfos: list of ConfigGroupVersionInfo
        :param _DeployTime: Release time. The time format follows the ISO 8601 standard and is represented in Coordinated Universal Time (UTC).
        :type DeployTime: str
        :param _Status: Release status. Valid values: 
<li>deploying: Being released.</li>
<li>failure: Release failed.</li>
<li>success: Released successfully. </li>
        :type Status: str
        :param _Message: Release result information.
        :type Message: str
        :param _RecordId: Release record ID. 
Note: this field may return null, indicating that no valid values can be obtained.
        :type RecordId: str
        :param _Description: Change description.
        :type Description: str
        """
        self._ConfigGroupVersionInfos = None
        self._DeployTime = None
        self._Status = None
        self._Message = None
        self._RecordId = None
        self._Description = None

    @property
    def ConfigGroupVersionInfos(self):
        return self._ConfigGroupVersionInfos

    @ConfigGroupVersionInfos.setter
    def ConfigGroupVersionInfos(self, ConfigGroupVersionInfos):
        self._ConfigGroupVersionInfos = ConfigGroupVersionInfos

    @property
    def DeployTime(self):
        return self._DeployTime

    @DeployTime.setter
    def DeployTime(self, DeployTime):
        self._DeployTime = DeployTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        if params.get("ConfigGroupVersionInfos") is not None:
            self._ConfigGroupVersionInfos = []
            for item in params.get("ConfigGroupVersionInfos"):
                obj = ConfigGroupVersionInfo()
                obj._deserialize(item)
                self._ConfigGroupVersionInfos.append(obj)
        self._DeployTime = params.get("DeployTime")
        self._Status = params.get("Status")
        self._Message = params.get("Message")
        self._RecordId = params.get("RecordId")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccelerationDomainsRequest(AbstractModel):
    """DescribeAccelerationDomains request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site related with the acceleration domain name.
        :type ZoneId: str
        :param _Offset: Offset for paginated queries. Default value: 0.
        :type Offset: int
        :param _Limit: Limit on paginated queries. Default value: 20. Maximum value: 200.
        :type Limit: int
        :param _Filters: Filter criteria. The maximum number of Filters.Values is 20. If this parameter is not input, all domain name information under the current zone-id will be returned. The detailed filter criteria are as follows:
<li>domain-name: Filter by acceleration domain name;</li>
<li>origin-type: Filter by origin server type;</li>
<li>origin: Filter by primary origin server address;</li>
<li>backup-origin: Filter by replica origin server address;</li>
<li>domain-cname: Filter by CNAME;</li>
<li>share-cname: Filter by shared CNAME.</li>
        :type Filters: list of AdvancedFilter
        :param _Order: Sort the returned results according to this field. Values include:
<li>`created_on`: Creation time of the acceleration domain name</li>
<li>`domain-name`: (Default) Acceleration domain name.</li> 
        :type Order: str
        :param _Direction: Sort direction. If the field value is number, sort by the numeric value. If the field value is text, sort by the ascill code. Values include:
<li>`asc`: Ascending order.</li>
<li>`desc`: Descending order.</li> Default value: `asc`.
        :type Direction: str
        :param _Match: The match mode. Values:
<li>`all`: Return all matches.</li>
<li>`any`: Return any match.</li>Default value: `all`.
        :type Match: str
        """
        self._ZoneId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._Order = None
        self._Direction = None
        self._Match = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Direction(self):
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Match(self):
        return self._Match

    @Match.setter
    def Match(self, Match):
        self._Match = Match


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Order = params.get("Order")
        self._Direction = params.get("Direction")
        self._Match = params.get("Match")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccelerationDomainsResponse(AbstractModel):
    """DescribeAccelerationDomains response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total of matched alias domain names.
        :type TotalCount: int
        :param _AccelerationDomains: Information of all matched acceleration domain names
        :type AccelerationDomains: list of AccelerationDomain
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._AccelerationDomains = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AccelerationDomains(self):
        return self._AccelerationDomains

    @AccelerationDomains.setter
    def AccelerationDomains(self, AccelerationDomains):
        self._AccelerationDomains = AccelerationDomains

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AccelerationDomains") is not None:
            self._AccelerationDomains = []
            for item in params.get("AccelerationDomains"):
                obj = AccelerationDomain()
                obj._deserialize(item)
                self._AccelerationDomains.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAliasDomainsRequest(AbstractModel):
    """DescribeAliasDomains request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: The site ID.
        :type ZoneId: str
        :param _Offset: The page offset. Default value: 0
        :type Offset: int
        :param _Limit: The paginated query limit. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param _Filters: Filter conditions. The maximum value for Filters.Values is 20. The detailed conditions are as follows:
<li>target-name: Filter by the target domain name;</li>
<li>alias-name: Filter by the alias of the domain name.</li>Fuzzy queries are only supported for the field name alias-name.
        :type Filters: list of AdvancedFilter
        """
        self._ZoneId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAliasDomainsResponse(AbstractModel):
    """DescribeAliasDomains response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total eligible alias domain names.
        :type TotalCount: int
        :param _AliasDomains: Information of the eligible alias domain names.
        :type AliasDomains: list of AliasDomain
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._AliasDomains = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AliasDomains(self):
        return self._AliasDomains

    @AliasDomains.setter
    def AliasDomains(self, AliasDomains):
        self._AliasDomains = AliasDomains

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AliasDomains") is not None:
            self._AliasDomains = []
            for item in params.get("AliasDomains"):
                obj = AliasDomain()
                obj._deserialize(item)
                self._AliasDomains.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeApplicationProxiesRequest(AbstractModel):
    """DescribeApplicationProxies request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID. This parameter is required.
        :type ZoneId: str
        :param _Filters: Filters. Each filter can have up to 20 entries. Details: <li>proxy-id<br>   Filter by the <strong>Proxy ID</strong>, such as: `proxy-ev2sawbwfd`. <br>   Type: String<br>   Required: No</li><li>zone-id<br>   Filter by the <strong>Site ID</strong>, such as `zone-vawer2vadg`. <br>   Type: String<br>   Required: No</li><li>rule-tag<br>   Filter by the <strong>Rule tag</strong>, such as `rule-service-1`. <br>   Type: String<br>   Required: No</li>
        :type Filters: list of Filter
        :param _Offset: The paginated query offset. Default value: 0
        :type Offset: int
        :param _Limit: The paginated query limit. Default value: 20. Maximum value: 1000.
        :type Limit: int
        """
        self._ZoneId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationProxiesResponse(AbstractModel):
    """DescribeApplicationProxies response structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationProxies: List of application proxies.
        :type ApplicationProxies: list of ApplicationProxy
        :param _TotalCount: Total number of records.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ApplicationProxies = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ApplicationProxies(self):
        return self._ApplicationProxies

    @ApplicationProxies.setter
    def ApplicationProxies(self, ApplicationProxies):
        self._ApplicationProxies = ApplicationProxies

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
        if params.get("ApplicationProxies") is not None:
            self._ApplicationProxies = []
            for item in params.get("ApplicationProxies"):
                obj = ApplicationProxy()
                obj._deserialize(item)
                self._ApplicationProxies.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeAvailablePlansRequest(AbstractModel):
    """DescribeAvailablePlans request structure.

    """


class DescribeAvailablePlansResponse(AbstractModel):
    """DescribeAvailablePlans response structure.

    """

    def __init__(self):
        r"""
        :param _PlanInfo: Plans available for the current user
Note: This field may return null, indicating that no valid values can be obtained.
        :type PlanInfo: list of PlanInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PlanInfo = None
        self._RequestId = None

    @property
    def PlanInfo(self):
        return self._PlanInfo

    @PlanInfo.setter
    def PlanInfo(self, PlanInfo):
        self._PlanInfo = PlanInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PlanInfo") is not None:
            self._PlanInfo = []
            for item in params.get("PlanInfo"):
                obj = PlanInfo()
                obj._deserialize(item)
                self._PlanInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBillingDataRequest(AbstractModel):
    """DescribeBillingData request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time.
        :type StartTime: str
        :param _EndTime: End time.
        :type EndTime: str
        :param _ZoneIds: Site ID set. This parameter is required.
        :type ZoneIds: list of str
        :param _MetricName: Metric list. Valid values:
<li>acc_flux: content acceleration traffic, in bytes;</li>
<li>smt_flux: smart acceleration traffic, in bytes;</li>
<li>l4_flux: L4 acceleration traffic, in bytes;</li>
<li>sec_flux: exclusive protection traffic, in bytes;</li>
<li>zxctg_flux: network optimization traffic in the Chinese mainland, in bytes;</li>
<li>acc_bandwidth: content acceleration bandwidth, in bps;</li>
<li>smt_bandwidth: smart acceleration bandwidth, in bps;</li>
<li>l4_bandwidth: L4 acceleration bandwidth, in bps;</li>
<li>sec_bandwidth: exclusive protection bandwidth, in bps;</li>
<li>zxctg_bandwidth: network optimization bandwidth in the Chinese mainland, in bps;</li>
<li>sec_request_clean: number of HTTP/HTTPS requests;</li>
<li>smt_request_clean: number of smart acceleration requests;</li>
<li>quic_request: number of QUIC requests;</li>
<li>bot_request_clean: number of Bot requests;</li>
<li>cls_count: number of real-time log entries pushed;</li>
<li>ddos_bandwidth: elastic DDoS protection bandwidth, in bps.</li>
        :type MetricName: str
        :param _Interval: Time granularity of the query. Valid values:
<li>5min: 5 minutes;</li>
<li>hour: 1 hour;</li>
<li>day: 1 day.</li>
        :type Interval: str
        :param _Filters: Filter criteria. The detailed values of filter criteria are as follows:
<li>host: Filter by domain name, such as test.example.com.<br></li>
<li>proxy-id: Filter by L4 proxy instance ID, such as sid-2rugn89bkla9.<br></li>
<li>region-id: Filter by billing region. Options:<br>  CH: Chinese mainland<br>  AF: Africa<br>  AS1: Asia-Pacific Region 1<br>  AS2: Asia-Pacific Region 2<br>  AS3: Asia-Pacific Region 3<br>  EU: Europe<br>  MidEast: Middle East<br>  NA: North America<br>  SA: South America</li>
        :type Filters: list of BillingDataFilter
        """
        self._StartTime = None
        self._EndTime = None
        self._ZoneIds = None
        self._MetricName = None
        self._Interval = None
        self._Filters = None

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
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ZoneIds = params.get("ZoneIds")
        self._MetricName = params.get("MetricName")
        self._Interval = params.get("Interval")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = BillingDataFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillingDataResponse(AbstractModel):
    """DescribeBillingData response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data point list.
Note: This field may return null, which indicates a failure to obtain a valid value.
        :type Data: list of BillingData
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
                obj = BillingData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConfigGroupVersionDetailRequest(AbstractModel):
    """DescribeConfigGroupVersionDetail request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _VersionId: Version ID.
        :type VersionId: str
        """
        self._ZoneId = None
        self._VersionId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VersionId(self):
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigGroupVersionDetailResponse(AbstractModel):
    """DescribeConfigGroupVersionDetail response structure.

    """

    def __init__(self):
        r"""
        :param _ConfigGroupVersionInfo: Version information.
        :type ConfigGroupVersionInfo: :class:`tencentcloud.teo.v20220901.models.ConfigGroupVersionInfo`
        :param _Content: Version file content. It is returned in JSON format.
        :type Content: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ConfigGroupVersionInfo = None
        self._Content = None
        self._RequestId = None

    @property
    def ConfigGroupVersionInfo(self):
        return self._ConfigGroupVersionInfo

    @ConfigGroupVersionInfo.setter
    def ConfigGroupVersionInfo(self, ConfigGroupVersionInfo):
        self._ConfigGroupVersionInfo = ConfigGroupVersionInfo

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ConfigGroupVersionInfo") is not None:
            self._ConfigGroupVersionInfo = ConfigGroupVersionInfo()
            self._ConfigGroupVersionInfo._deserialize(params.get("ConfigGroupVersionInfo"))
        self._Content = params.get("Content")
        self._RequestId = params.get("RequestId")


class DescribeConfigGroupVersionsRequest(AbstractModel):
    """DescribeConfigGroupVersions request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _GroupId: Configuraration group ID.
        :type GroupId: str
        :param _Filters: Filtering condition. The maximum value of Filters.Values is 20. If this parameter is not specified, all version information for the selected configuration group is returned. Detailed filtering conditions: 
<li>version-id: Filter by version ID.</li>
        :type Filters: list of AdvancedFilter
        :param _Offset: Paging query offset. The default value is 0.
        :type Offset: int
        :param _Limit: Limited entries in paging queries. The default value is 20 and the maximum value is 100. 
        :type Limit: int
        """
        self._ZoneId = None
        self._GroupId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._GroupId = params.get("GroupId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigGroupVersionsResponse(AbstractModel):
    """DescribeConfigGroupVersions response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total versions.
        :type TotalCount: int
        :param _ConfigGroupVersionInfos: Version information list.
        :type ConfigGroupVersionInfos: list of ConfigGroupVersionInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ConfigGroupVersionInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ConfigGroupVersionInfos(self):
        return self._ConfigGroupVersionInfos

    @ConfigGroupVersionInfos.setter
    def ConfigGroupVersionInfos(self, ConfigGroupVersionInfos):
        self._ConfigGroupVersionInfos = ConfigGroupVersionInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ConfigGroupVersionInfos") is not None:
            self._ConfigGroupVersionInfos = []
            for item in params.get("ConfigGroupVersionInfos"):
                obj = ConfigGroupVersionInfo()
                obj._deserialize(item)
                self._ConfigGroupVersionInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeContentQuotaRequest(AbstractModel):
    """DescribeContentQuota request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site.
        :type ZoneId: str
        """
        self._ZoneId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeContentQuotaResponse(AbstractModel):
    """DescribeContentQuota response structure.

    """

    def __init__(self):
        r"""
        :param _PurgeQuota: Purging quotas.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PurgeQuota: list of Quota
        :param _PrefetchQuota: Pre-warming quotas.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PrefetchQuota: list of Quota
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PurgeQuota = None
        self._PrefetchQuota = None
        self._RequestId = None

    @property
    def PurgeQuota(self):
        return self._PurgeQuota

    @PurgeQuota.setter
    def PurgeQuota(self, PurgeQuota):
        self._PurgeQuota = PurgeQuota

    @property
    def PrefetchQuota(self):
        return self._PrefetchQuota

    @PrefetchQuota.setter
    def PrefetchQuota(self, PrefetchQuota):
        self._PrefetchQuota = PrefetchQuota

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PurgeQuota") is not None:
            self._PurgeQuota = []
            for item in params.get("PurgeQuota"):
                obj = Quota()
                obj._deserialize(item)
                self._PurgeQuota.append(obj)
        if params.get("PrefetchQuota") is not None:
            self._PrefetchQuota = []
            for item in params.get("PrefetchQuota"):
                obj = Quota()
                obj._deserialize(item)
                self._PrefetchQuota.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCustomErrorPagesRequest(AbstractModel):
    """DescribeCustomErrorPages request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _Filters: Filter criteria. The maximum number of Filters.Values is 20. The detailed Name values of filter criteria are as follows:
<li>page-id: Filter by page ID;</li>
<li>name: Filter by page name;</li>
<li>description: Filter by page description;</li>
<li>content-type: Filter by page type.</li>
        :type Filters: list of AdvancedFilter
        :param _Offset: The offset of paginated query. Default value: 0.
        :type Offset: int
        :param _Limit: The limit of paginated query. Default value: 20. Maximum value: 1,000.  
        :type Limit: int
        """
        self._ZoneId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomErrorPagesResponse(AbstractModel):
    """DescribeCustomErrorPages response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of custom error pages.
        :type TotalCount: int
        :param _ErrorPages: Custom error page data list.
        :type ErrorPages: list of CustomErrorPage
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ErrorPages = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ErrorPages(self):
        return self._ErrorPages

    @ErrorPages.setter
    def ErrorPages(self, ErrorPages):
        self._ErrorPages = ErrorPages

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ErrorPages") is not None:
            self._ErrorPages = []
            for item in params.get("ErrorPages"):
                obj = CustomErrorPage()
                obj._deserialize(item)
                self._ErrorPages.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDDoSAttackDataRequest(AbstractModel):
    """DescribeDDoSAttackData request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time of the query period.
        :type StartTime: str
        :param _EndTime: End time of the query period.
        :type EndTime: str
        :param _MetricNames: Statistical metrics.
<li>`ddos_attackMaxBandwidth`: Peak attack bandwidth;</li>
<li>`ddos_attackMaxPackageRate`: Peak attack packet rate;</li>
<li>`ddos_attackBandwidth`: Time-series data of attack bandwidth;</li>
<li>`ddos_attackPackageRate`: Time-series data of attack packet rate.</li>
        :type MetricNames: list of str
        :param _ZoneIds: ZoneId set. This parameter is required.
        :type ZoneIds: list of str
        :param _PolicyIds: IDs of DDoS policies to be queried. All policies will be selected if this field is not specified.
        :type PolicyIds: list of int
        :param _Interval: The query granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minutes;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day</li>If this field is not specified, the granularity is determined based on the query period. <br>Period ≤ 1 hour: `min`; <br>1 hour < Period ≤ 2 days: `5min`; <br>2 days < Period ≤ 7 days: `hour`; <br>Period > 7 days: `day`.
        :type Interval: str
        :param _Area: Geolocation scope. Values:
<li>`overseas`: Regions outside the Chinese mainland</li>
<li>`mainland`: Chinese mainland</li>
<li>`global`: Global </li>If this field is not specified, the default value `global` is used.
        :type Area: str
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricNames = None
        self._ZoneIds = None
        self._PolicyIds = None
        self._Interval = None
        self._Area = None

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
    def MetricNames(self):
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def PolicyIds(self):
        return self._PolicyIds

    @PolicyIds.setter
    def PolicyIds(self, PolicyIds):
        self._PolicyIds = PolicyIds

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricNames = params.get("MetricNames")
        self._ZoneIds = params.get("ZoneIds")
        self._PolicyIds = params.get("PolicyIds")
        self._Interval = params.get("Interval")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAttackDataResponse(AbstractModel):
    """DescribeDDoSAttackData response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of query results.
        :type TotalCount: int
        :param _Data: List of DDoS attack data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of SecEntry
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SecEntry()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDDoSAttackEventRequest(AbstractModel):
    """DescribeDDoSAttackEvent request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time. Time range: 30 days.
        :type StartTime: str
        :param _EndTime: End time. Time range: 30 days.
        :type EndTime: str
        :param _PolicyIds: List of DDoS policy IDs. All policies are selected if this field is not specified.
        :type PolicyIds: list of int
        :param _ZoneIds: ZoneId set. This parameter is required.
        :type ZoneIds: list of str
        :param _Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param _Offset: The page offset. Default value: 0.
        :type Offset: int
        :param _ShowDetail: Parameter to show attack details. If it is configured as false, only the number of attacks is returned without details. If it is configured as true, attack details are returned.
        :type ShowDetail: bool
        :param _Area: Geolocation scope. Values: 
<li>`overseas`: Regions outside the Chinese mainland</li>
<li>`mainland`: Chinese mainland</li>
<li>`global`: Global</li>If this field is not specified, the default value `global` is used.
        :type Area: str
        :param _OrderBy: The sorting field. Values: 
<li>`MaxBandWidth`: Peak bandwidth</li>
<li>`AttackStartTime` Start time of the attack</li>If this field is not specified, the default value `AttackStartTime` is used.
        :type OrderBy: str
        :param _OrderType: The sorting method. Values: 
<Li>`asc`: Ascending</li>
<li>`desc`: Descending</li>If this field is not specified, the default value `desc` is used.
        :type OrderType: str
        """
        self._StartTime = None
        self._EndTime = None
        self._PolicyIds = None
        self._ZoneIds = None
        self._Limit = None
        self._Offset = None
        self._ShowDetail = None
        self._Area = None
        self._OrderBy = None
        self._OrderType = None

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
    def PolicyIds(self):
        return self._PolicyIds

    @PolicyIds.setter
    def PolicyIds(self, PolicyIds):
        self._PolicyIds = PolicyIds

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

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
    def ShowDetail(self):
        return self._ShowDetail

    @ShowDetail.setter
    def ShowDetail(self, ShowDetail):
        self._ShowDetail = ShowDetail

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

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


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PolicyIds = params.get("PolicyIds")
        self._ZoneIds = params.get("ZoneIds")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._ShowDetail = params.get("ShowDetail")
        self._Area = params.get("Area")
        self._OrderBy = params.get("OrderBy")
        self._OrderType = params.get("OrderType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAttackEventResponse(AbstractModel):
    """DescribeDDoSAttackEvent response structure.

    """

    def __init__(self):
        r"""
        :param _Data: List of DDoS attack data. 
Note: This field may return `null`, indicating that no valid value was found.
        :type Data: list of DDoSAttackEvent
        :param _TotalCount: Total number of query results.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DDoSAttackEvent()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDDoSAttackTopDataRequest(AbstractModel):
    """DescribeDDoSAttackTopData request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: The start time.
        :type StartTime: str
        :param _EndTime: The end time.
        :type EndTime: str
        :param _MetricName: The statistical metric. Values:
<li>`ddos_attackFlux_protocol`: Rank protocols by the attack traffic.</li>
<li>`ddos_attackPackageNum_protocol`: Rank protocols by the number of attack packets.</li>
<li>`ddos_attackNum_attackType`: Rank attack types by the number of attacks.</li>
<li>`ddos_attackNum_sregion`: Rank attacker regions by the number of attacks.</li>
<li>`ddos_attackFlux_sip`: Rank attacker IPs by the number of attacks.</li>
<li>`ddos_attackFlux_sregion`: Rank attacker regions by the number of attacks.</li>
        :type MetricName: str
        :param _ZoneIds: Site ID set. This parameter is required.
        :type ZoneIds: list of str
        :param _PolicyIds: The list of DDoS policy IDs to be specified. All policies will be selected if this field is not specified.
        :type PolicyIds: list of int
        :param _AttackType: The attack type. Values:
<li>`flood`: Flood;</li>
<li>`icmpFlood`: ICMP flood;</li>
<li>`all`: All attack types.</li>This field will be set to the default value `all` if not specified.
        :type AttackType: str
        :param _ProtocolType: The protocol type. Values:
<li>`tcp`: TCP protocol;</li>
<li>`udp`: UDP protocol;</li>
<li>`all`: All protocol types.</li>This field will be set to the default value `all` if not specified.
        :type ProtocolType: str
        :param _Port: The port number.
        :type Port: int
        :param _Limit: Queries the top n rows of data. Top 10 rows of data will be queried if this field is not specified.
        :type Limit: int
        :param _Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None
        self._ZoneIds = None
        self._PolicyIds = None
        self._AttackType = None
        self._ProtocolType = None
        self._Port = None
        self._Limit = None
        self._Area = None

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
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def PolicyIds(self):
        return self._PolicyIds

    @PolicyIds.setter
    def PolicyIds(self, PolicyIds):
        self._PolicyIds = PolicyIds

    @property
    def AttackType(self):
        return self._AttackType

    @AttackType.setter
    def AttackType(self, AttackType):
        self._AttackType = AttackType

    @property
    def ProtocolType(self):
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
        self._ZoneIds = params.get("ZoneIds")
        self._PolicyIds = params.get("PolicyIds")
        self._AttackType = params.get("AttackType")
        self._ProtocolType = params.get("ProtocolType")
        self._Port = params.get("Port")
        self._Limit = params.get("Limit")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAttackTopDataResponse(AbstractModel):
    """DescribeDDoSAttackTopData response structure.

    """

    def __init__(self):
        r"""
        :param _Data: The list of top-ranked DDoS attack data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TopEntry
        :param _TotalCount: Total number of query results.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TopEntry()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDefaultCertificatesRequest(AbstractModel):
    """DescribeDefaultCertificates request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _Filters: Filter criteria. Each filter criteria can have up to 5 entries.
<li>`zone-id`: <br>Filter by <strong>site ID</strong>, such as zone-xxx<br>   Type: String<br>   Required: No</li>
        :type Filters: list of Filter
        :param _Offset: Offset for paginated queries. Default value: `0`
        :type Offset: int
        :param _Limit: Limit on paginated queries. Default value: `20`. Maximum value: `100`.
        :type Limit: int
        """
        self._ZoneId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDefaultCertificatesResponse(AbstractModel):
    """DescribeDefaultCertificates response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of certificates
        :type TotalCount: int
        :param _DefaultServerCertInfo: List of default certificates
        :type DefaultServerCertInfo: list of DefaultServerCertInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._DefaultServerCertInfo = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DefaultServerCertInfo(self):
        return self._DefaultServerCertInfo

    @DefaultServerCertInfo.setter
    def DefaultServerCertInfo(self, DefaultServerCertInfo):
        self._DefaultServerCertInfo = DefaultServerCertInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DefaultServerCertInfo") is not None:
            self._DefaultServerCertInfo = []
            for item in params.get("DefaultServerCertInfo"):
                obj = DefaultServerCertInfo()
                obj._deserialize(item)
                self._DefaultServerCertInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeployHistoryRequest(AbstractModel):
    """DescribeDeployHistory request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _EnvId: Environment ID.
        :type EnvId: str
        :param _Filters: Filtering condition. The maximum value of Filters.Values is 20. Detailed filtering conditions: 
<li>record-id: Filter by release record ID. </li>
        :type Filters: list of AdvancedFilter
        """
        self._ZoneId = None
        self._EnvId = None
        self._Filters = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._EnvId = params.get("EnvId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeployHistoryResponse(AbstractModel):
    """DescribeDeployHistory response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total release records.
        :type TotalCount: int
        :param _Records: Release record details.
        :type Records: list of DeployRecord
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Records = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Records(self):
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = DeployRecord()
                obj._deserialize(item)
                self._Records.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEnvironmentsRequest(AbstractModel):
    """DescribeEnvironments request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        """
        self._ZoneId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvironmentsResponse(AbstractModel):
    """DescribeEnvironments response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total environments.
        :type TotalCount: int
        :param _EnvInfos: Environment list.
        :type EnvInfos: list of EnvInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._EnvInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def EnvInfos(self):
        return self._EnvInfos

    @EnvInfos.setter
    def EnvInfos(self, EnvInfos):
        self._EnvInfos = EnvInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("EnvInfos") is not None:
            self._EnvInfos = []
            for item in params.get("EnvInfos"):
                obj = EnvInfo()
                obj._deserialize(item)
                self._EnvInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFunctionRulesRequest(AbstractModel):
    """DescribeFunctionRules request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _Filters: Filter criteria list. There is an AND relationship between different criteria. The maximum number of Filters.Values is 20. The detailed filter criteria are as follows:
<li>rule-id: Exact match by [rule ID].</li>
<li>function-id: Exact match by [function ID].</li>
<li>remark: Fuzzy match by [rule description].</li>
        :type Filters: list of Filter
        """
        self._ZoneId = None
        self._Filters = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFunctionRulesResponse(AbstractModel):
    """DescribeFunctionRules response structure.

    """

    def __init__(self):
        r"""
        :param _FunctionRules: Rule details list.
        :type FunctionRules: list of FunctionRule
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FunctionRules = None
        self._RequestId = None

    @property
    def FunctionRules(self):
        return self._FunctionRules

    @FunctionRules.setter
    def FunctionRules(self, FunctionRules):
        self._FunctionRules = FunctionRules

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FunctionRules") is not None:
            self._FunctionRules = []
            for item in params.get("FunctionRules"):
                obj = FunctionRule()
                obj._deserialize(item)
                self._FunctionRules.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFunctionRuntimeEnvironmentRequest(AbstractModel):
    """DescribeFunctionRuntimeEnvironment request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _FunctionId: Function ID.
        :type FunctionId: str
        """
        self._ZoneId = None
        self._FunctionId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def FunctionId(self):
        return self._FunctionId

    @FunctionId.setter
    def FunctionId(self, FunctionId):
        self._FunctionId = FunctionId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._FunctionId = params.get("FunctionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFunctionRuntimeEnvironmentResponse(AbstractModel):
    """DescribeFunctionRuntimeEnvironment response structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentVariables: Environment variable list.
        :type EnvironmentVariables: list of FunctionEnvironmentVariable
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EnvironmentVariables = None
        self._RequestId = None

    @property
    def EnvironmentVariables(self):
        return self._EnvironmentVariables

    @EnvironmentVariables.setter
    def EnvironmentVariables(self, EnvironmentVariables):
        self._EnvironmentVariables = EnvironmentVariables

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EnvironmentVariables") is not None:
            self._EnvironmentVariables = []
            for item in params.get("EnvironmentVariables"):
                obj = FunctionEnvironmentVariable()
                obj._deserialize(item)
                self._EnvironmentVariables.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFunctionsRequest(AbstractModel):
    """DescribeFunctions request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _FunctionIds: Filter by function ID list.
        :type FunctionIds: list of str
        :param _Filters: Filter criteria list. There is an AND relationship between different criteria. The maximum number of Filters.Values is 20. The detailed filter criteria are as follows:
<li>name: Fuzzy match by [function name].</li>
<li>remark: Fuzzy match by [function description].</li>
        :type Filters: list of Filter
        :param _Offset: The offset of paginated query. Default value: 0.
        :type Offset: int
        :param _Limit: Number limit of paginated query. Default value: 20. Maximum value: 200.
        :type Limit: int
        """
        self._ZoneId = None
        self._FunctionIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def FunctionIds(self):
        return self._FunctionIds

    @FunctionIds.setter
    def FunctionIds(self, FunctionIds):
        self._FunctionIds = FunctionIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._FunctionIds = params.get("FunctionIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFunctionsResponse(AbstractModel):
    """DescribeFunctions response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of functions that meet the query condition.
        :type TotalCount: int
        :param _Functions: Information of all functions that meet the query condition.
        :type Functions: list of Function
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Functions = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Functions(self):
        return self._Functions

    @Functions.setter
    def Functions(self, Functions):
        self._Functions = Functions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Functions") is not None:
            self._Functions = []
            for item in params.get("Functions"):
                obj = Function()
                obj._deserialize(item)
                self._Functions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHostsSettingRequest(AbstractModel):
    """DescribeHostsSetting request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: The site ID.
        :type ZoneId: str
        :param _Offset: Offset for paginated queries. Default value: 0. Minimum value: 0.
        :type Offset: int
        :param _Limit: Limit on paginated queries. Default value: 100. Maximum value: 1000.
        :type Limit: int
        :param _Filters: Filter conditions. The maximum value for Filters.Values is 20. The detailed conditions are as follows:<li>host: Filter by domain name.</li>
        :type Filters: list of Filter
        """
        self._ZoneId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostsSettingResponse(AbstractModel):
    """DescribeHostsSetting response structure.

    """

    def __init__(self):
        r"""
        :param _DetailHosts: List of domain names.
        :type DetailHosts: list of DetailHost
        :param _TotalNumber: Number of domain names
        :type TotalNumber: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DetailHosts = None
        self._TotalNumber = None
        self._RequestId = None

    @property
    def DetailHosts(self):
        return self._DetailHosts

    @DetailHosts.setter
    def DetailHosts(self, DetailHosts):
        self._DetailHosts = DetailHosts

    @property
    def TotalNumber(self):
        return self._TotalNumber

    @TotalNumber.setter
    def TotalNumber(self, TotalNumber):
        self._TotalNumber = TotalNumber

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DetailHosts") is not None:
            self._DetailHosts = []
            for item in params.get("DetailHosts"):
                obj = DetailHost()
                obj._deserialize(item)
                self._DetailHosts.append(obj)
        self._TotalNumber = params.get("TotalNumber")
        self._RequestId = params.get("RequestId")


class DescribeIPRegionRequest(AbstractModel):
    """DescribeIPRegion request structure.

    """

    def __init__(self):
        r"""
        :param _IPs: List of IPs to be queried, supporting IPV4 and IPV6. Up to 100 can be queried.
        :type IPs: list of str
        """
        self._IPs = None

    @property
    def IPs(self):
        return self._IPs

    @IPs.setter
    def IPs(self, IPs):
        self._IPs = IPs


    def _deserialize(self, params):
        self._IPs = params.get("IPs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIPRegionResponse(AbstractModel):
    """DescribeIPRegion response structure.

    """

    def __init__(self):
        r"""
        :param _IPRegionInfo: List of IP attribution information.
        :type IPRegionInfo: list of IPRegionInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IPRegionInfo = None
        self._RequestId = None

    @property
    def IPRegionInfo(self):
        return self._IPRegionInfo

    @IPRegionInfo.setter
    def IPRegionInfo(self, IPRegionInfo):
        self._IPRegionInfo = IPRegionInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("IPRegionInfo") is not None:
            self._IPRegionInfo = []
            for item in params.get("IPRegionInfo"):
                obj = IPRegionInfo()
                obj._deserialize(item)
                self._IPRegionInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIdentificationsRequest(AbstractModel):
    """DescribeIdentifications request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Filter conditions. The maximum value for Filters.Values is 20. The detailed conditions are as follows:<li>zone-name: Filter by site name.</li>
        :type Filters: list of Filter
        :param _Offset: The page offset. Default value: 0
        :type Offset: int
        :param _Limit: The paginated query limit. Default value: 20. Maximum value: 1000.
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIdentificationsResponse(AbstractModel):
    """DescribeIdentifications response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible sites.
        :type TotalCount: int
        :param _Identifications: The site verification information.
        :type Identifications: list of Identification
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Identifications = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Identifications(self):
        return self._Identifications

    @Identifications.setter
    def Identifications(self, Identifications):
        self._Identifications = Identifications

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Identifications") is not None:
            self._Identifications = []
            for item in params.get("Identifications"):
                obj = Identification()
                obj._deserialize(item)
                self._Identifications.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeL4ProxyRequest(AbstractModel):
    """DescribeL4Proxy request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the zone where the Layer 4 proxy instance belongs.
        :type ZoneId: str
        :param _Offset: Paginated query offset. Defaults to 0 when not specified.
        :type Offset: int
        :param _Limit: Paginated query limit. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param _Filters: Filter criteria. The upper limit for Filters.Values is 20. If left empty, all Layer 4 proxy instance information under the current zone ID is returned. The detailed filter criteria are as follows: <li>proxy-id: Filters by Layer 4 proxy instance ID;</li>
<li>ddos-protection-type: Filters by security protection type;</li>

        :type Filters: list of Filter
        """
        self._ZoneId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL4ProxyResponse(AbstractModel):
    """DescribeL4Proxy response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The number of Layer 4 proxy instances.
        :type TotalCount: int
        :param _L4Proxies: List of Layer 4 proxy instances.
        :type L4Proxies: list of L4Proxy
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._L4Proxies = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def L4Proxies(self):
        return self._L4Proxies

    @L4Proxies.setter
    def L4Proxies(self, L4Proxies):
        self._L4Proxies = L4Proxies

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("L4Proxies") is not None:
            self._L4Proxies = []
            for item in params.get("L4Proxies"):
                obj = L4Proxy()
                obj._deserialize(item)
                self._L4Proxies.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeL4ProxyRulesRequest(AbstractModel):
    """DescribeL4ProxyRules request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _ProxyId: Layer 4 proxy instance ID.
        :type ProxyId: str
        :param _Offset: Paginated query offset. Defaults to 0 when not specified.
        :type Offset: int
        :param _Limit: Paginated query limit. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param _Filters: Filter criteria. The upper limit for Filters.Values is 20. All rule information under the current Layer 4 instance will be returned if left empty. The detailed filter criteria are as follows: <li>rule-tag: Filters rules under the Layer 4 proxy instance according to rule tag.</li>
        :type Filters: list of Filter
        """
        self._ZoneId = None
        self._ProxyId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL4ProxyRulesResponse(AbstractModel):
    """DescribeL4ProxyRules response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The total count of forwarding rules.
        :type TotalCount: int
        :param _L4ProxyRules: List of forwarding rules.	
        :type L4ProxyRules: list of L4ProxyRule
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._L4ProxyRules = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def L4ProxyRules(self):
        return self._L4ProxyRules

    @L4ProxyRules.setter
    def L4ProxyRules(self, L4ProxyRules):
        self._L4ProxyRules = L4ProxyRules

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("L4ProxyRules") is not None:
            self._L4ProxyRules = []
            for item in params.get("L4ProxyRules"):
                obj = L4ProxyRule()
                obj._deserialize(item)
                self._L4ProxyRules.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOriginGroupRequest(AbstractModel):
    """DescribeOriginGroup request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: (Required) Site ID
        :type ZoneId: str
        :param _Offset: The paginated query offset. Default value: 0
        :type Offset: int
        :param _Limit: Limit on paginated queries. Value range: 1-1000. Default value: 20.
        :type Limit: int
        :param _Filters: Filters. Each filter can have up to 20 entries. See below for details:
<li>`origin-group-id`<br>Filter by the <strong>origin group ID</strong>. Format: `origin-2ccgtb24-7dc5-46s2-9r3e-95825d53dwe3a`<br>Fuzzy query is not supported</li><li>`origin-group-name`<br>Filter by the <strong>origin group name</strong><br>Fuzzy query is supported. When fuzzy query is used, only one origin groupsource site group name is supported</li>
        :type Filters: list of AdvancedFilter
        """
        self._ZoneId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOriginGroupResponse(AbstractModel):
    """DescribeOriginGroup response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of records.
        :type TotalCount: int
        :param _OriginGroups: Origin group information.
        :type OriginGroups: list of OriginGroup
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._OriginGroups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def OriginGroups(self):
        return self._OriginGroups

    @OriginGroups.setter
    def OriginGroups(self, OriginGroups):
        self._OriginGroups = OriginGroups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("OriginGroups") is not None:
            self._OriginGroups = []
            for item in params.get("OriginGroups"):
                obj = OriginGroup()
                obj._deserialize(item)
                self._OriginGroups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOriginProtectionRequest(AbstractModel):
    """DescribeOriginProtection request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneIds: Set of site IDs to be queried. This is a required parameter.
        :type ZoneIds: list of str
        :param _Filters: Filter conditions. Each filter condition can have up to 20 entries. See below for details:
<li>`need-update`:<br>   Whether <strong>the intermediate IP update is needed for the site</strong>.<br>   Type: String<br>   Required: No<br>   Values:<br>   `true`: Update needed.<br>   `false`: Update not needed.<br></li>
<li>`plan-support`:<br>   Whether <strong>origin protection is supported in the plan</strong>.<br>   Type: String<br>   Required: No<br>   Values:<br>   `true`: Origin protection supported.<br>   `false`: Origin protection not supported.<br></li>
        :type Filters: list of Filter
        :param _Offset: Offset for paginated queries. Default value: 0.
        :type Offset: int
        :param _Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        """
        self._ZoneIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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


    def _deserialize(self, params):
        self._ZoneIds = params.get("ZoneIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOriginProtectionResponse(AbstractModel):
    """DescribeOriginProtection response structure.

    """

    def __init__(self):
        r"""
        :param _OriginProtectionInfo: Origin protection configuration.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type OriginProtectionInfo: list of OriginProtectionInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._OriginProtectionInfo = None
        self._RequestId = None

    @property
    def OriginProtectionInfo(self):
        return self._OriginProtectionInfo

    @OriginProtectionInfo.setter
    def OriginProtectionInfo(self, OriginProtectionInfo):
        self._OriginProtectionInfo = OriginProtectionInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("OriginProtectionInfo") is not None:
            self._OriginProtectionInfo = []
            for item in params.get("OriginProtectionInfo"):
                obj = OriginProtectionInfo()
                obj._deserialize(item)
                self._OriginProtectionInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOverviewL7DataRequest(AbstractModel):
    """DescribeOverviewL7Data request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time.
        :type StartTime: str
        :param _EndTime: End time.
        :type EndTime: str
        :param _MetricNames: Queried metric. Valid values:
<li>l7Flow_outFlux: EdgeOne response traffic;</li>
<li>l7Flow_inFlux: EdgeOne request traffic;</li>
<li>l7Flow_outBandwidth: EdgeOne response bandwidth;</li>
<li>l7Flow_inBandwidth: EdgeOne request traffic;</li>
<li>l7Flow_hit_outFlux: cache hit traffic;</li>
<li>l7Flow_request: number of access requests;</li>
<li>l7Flow_flux: upstream and downstream traffic of access requests;</li>
<li>l7Flow_bandwidth: upstream and downstream bandwidths of access requests.</li>
        :type MetricNames: list of str
        :param _ZoneIds: Site ID set. This parameter is required.
        :type ZoneIds: list of str
        :param _Domains: Queried domain name set. This parameter has been deprecated.
        :type Domains: list of str
        :param _Protocol: Protocol type of the query. Valid values:
<li>http: HTTP protocol;</li>
<li>https: HTTPS protocol;</li>
<li>http2: HTTP/2 protocol;</li>
<li>all: all protocols.</li>If this parameter is not input, the default value `all` is used. This parameter is not yet effective.
        :type Protocol: str
        :param _Interval: Time granularity of the query. Valid values:
<li>min: 1 minute;</li>
<li>5min: 5 minutes;</li>
<li>hour: 1 hour;</li>
<li>day: 1 day.</li>If this parameter is not input, the granularity will be automatically inferred based on the interval between the start time and end time. Specifically, the granularity value is min, 5min, hour, and day respectively for queries of data within 1 hour, within 2 days, within 7 days, and over 7 days.
        :type Interval: str
        :param _Filters: Filter criteria. The detailed Key values of filter criteria are as follows:
<li>socket:<br>   Filter by [<strong>HTTP protocol type</strong>].<br>   Valid values:<br>   HTTP: HTTP protocol; <br>   HTTPS: HTTPS protocol;<br>   QUIC: QUIC protocol.</li>
<li>domain<br>?? Filter by [<strong>domain name</strong>].</li>
<li>tagKey<br>?? Filter by [<strong>tag key</strong>].</li>
<li>tagValue<br>?? Filter by [<strong>tag value</strong>].</li>
        :type Filters: list of QueryCondition
        :param _Area: Data ownership area. Valid values:
<li>overseas: global (excluding the Chinese mainland) data;</li>
<li>mainland: Chinese mainland data;</li>
<li>global: global data.</li>If this parameter is not input, the default value `global` is used.
        :type Area: str
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricNames = None
        self._ZoneIds = None
        self._Domains = None
        self._Protocol = None
        self._Interval = None
        self._Filters = None
        self._Area = None

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
    def MetricNames(self):
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricNames = params.get("MetricNames")
        self._ZoneIds = params.get("ZoneIds")
        self._Domains = params.get("Domains")
        self._Protocol = params.get("Protocol")
        self._Interval = params.get("Interval")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOverviewL7DataResponse(AbstractModel):
    """DescribeOverviewL7Data response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of entries in the query result.
        :type TotalCount: int
        :param _Data: List of time series traffic data in L7 monitoring.
Note: This field may return null, which indicates a failure to obtain a valid value.
        :type Data: list of TimingDataRecord
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TimingDataRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrefetchTasksRequest(AbstractModel):
    """DescribePrefetchTasks request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID. This parameter is required.
        :type ZoneId: str
        :param _StartTime: Start time of the query. Either time or job-id is required.
        :type StartTime: str
        :param _EndTime: End time of the query. Either time or job-id is required.
        :type EndTime: str
        :param _Offset: Offset of paginated query. Default value: 0.
        :type Offset: int
        :param _Limit: Number limit of paginated query. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param _Filters: Filter criteria. The maximum number of Filters.Values is 20. The detailed filter criteria are as follows: <li>job-id: Filter by task ID in the format like 1379afjk91u32h. Multiple values and fuzzy queries are not supported.</li><li>target: Filter by target resource information in the format like http://www.qq.com/1.txt. Multiple values and fuzzy queries are not supported.</li><li>domains: Filter by domain name in the format like www.qq.com. Fuzzy queries are not supported.</li><li>statuses: Filter by task status. Fuzzy queries are not supported. Options:<br>??processing: processing<br>??success: successful<br>??failed: failed<br>??timeout: timed out<br>??invalid: invalid, that is, the response status code of the origin server is not 2xx. Please check the origin server service.</li>
        :type Filters: list of AdvancedFilter
        """
        self._ZoneId = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrefetchTasksResponse(AbstractModel):
    """DescribePrefetchTasks response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of items in the query condition.
        :type TotalCount: int
        :param _Tasks: Task result list.
        :type Tasks: list of Task
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
                obj = Task()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePurgeTasksRequest(AbstractModel):
    """DescribePurgeTasks request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID. This parameter is required.
        :type ZoneId: str
        :param _StartTime: Start time of the query. Either time or job-id is required.
        :type StartTime: str
        :param _EndTime: End time of the query. Either time or job-id is required.
        :type EndTime: str
        :param _Offset: Offset of paginated query. Default value: 0.
        :type Offset: int
        :param _Limit: Number limit of paginated query. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param _Filters: Filter criteria. The maximum number of Filters.Values is 20. The detailed filter criteria are as follows:
<li>job-id: Filter by task ID in the format like 1379afjk91u32h. Multiple values and fuzzy queries are not supported.</li>
<li>target: Filter by target resource information in the format like http://www.qq.com/1.txt or tag1. Multiple values are not supported yet. Fuzzy queries are supported.</li>
<li>domains: Filter by domain name in the format like www.qq.com. Fuzzy queries are not supported.</li>
<li>statuses: Filter by task status. Fuzzy queries are not supported. Options:<br>?? processing: processing<br>?? success: successful<br>?? failed: failed<br>?? timeout: timed out</li>
<li>type: Filter by cache clearance type. Multiple values and fuzzy queries are not supported yet. Options: <br>?? purge_url: URL<br>?? purge_prefix: prefix<br>?? purge_all: all cached content<br>?? purge_host: Hostname<br>?? purge_cache_tag: CacheTag</li>
        :type Filters: list of AdvancedFilter
        """
        self._ZoneId = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePurgeTasksResponse(AbstractModel):
    """DescribePurgeTasks response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of items in the query condition.
        :type TotalCount: int
        :param _Tasks: Task result list.
        :type Tasks: list of Task
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
                obj = Task()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRealtimeLogDeliveryTasksRequest(AbstractModel):
    """DescribeRealtimeLogDeliveryTasks request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _Offset: The offset of paginated query. Default value: 0.
        :type Offset: int
        :param _Limit: The limit of paginated query. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param _Filters: Filter conditions. The maximum value for Filters.Values is 20. If this field is not filled in, all the real-time log delivery task information under the current zone-id will be returned. Detailed filter conditions are as follows:
<li>task-id: Filter by real-time log delivery task ID. Fuzzy search is not supported.</li>
<li>task-name: Filter by real-time log delivery task name. Fuzzy search is supported, but only one real-time log delivery task name can be filled in for fuzzy search.</li>
<li>entity-list: Filter by entity corresponding to the real-time log delivery task. Fuzzy search is not supported. Example values: domain.example.com or sid-2s69eb5wcms7.</li>
<li>task-type: Filter by real-time log delivery task type. Fuzzy search is not supported. Optional values:<br>cls: Push to Tencent Cloud CLS;<br>custom_endpoint: Push to a user-defined HTTP(S) address;<br>s3: Push to an AWS S3-compatible bucket address.</li>
        :type Filters: list of AdvancedFilter
        """
        self._ZoneId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRealtimeLogDeliveryTasksResponse(AbstractModel):
    """DescribeRealtimeLogDeliveryTasks response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The number of real-time log delivery tasks which match the query conditions.
        :type TotalCount: int
        :param _RealtimeLogDeliveryTasks: The list of all real-time log delivery tasks which match the query conditions.
        :type RealtimeLogDeliveryTasks: list of RealtimeLogDeliveryTask
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RealtimeLogDeliveryTasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RealtimeLogDeliveryTasks(self):
        return self._RealtimeLogDeliveryTasks

    @RealtimeLogDeliveryTasks.setter
    def RealtimeLogDeliveryTasks(self, RealtimeLogDeliveryTasks):
        self._RealtimeLogDeliveryTasks = RealtimeLogDeliveryTasks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RealtimeLogDeliveryTasks") is not None:
            self._RealtimeLogDeliveryTasks = []
            for item in params.get("RealtimeLogDeliveryTasks"):
                obj = RealtimeLogDeliveryTask()
                obj._deserialize(item)
                self._RealtimeLogDeliveryTasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRulesRequest(AbstractModel):
    """DescribeRules request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site
        :type ZoneId: str
        :param _Filters: Filter conditions. Each filter condition can have up to 20 entries. See below for details:
<li>`rule-id`:<br>   Filter by the <strong>rule ID</strong><br>   Type: String<br>   Required: No</li>
        :type Filters: list of Filter
        """
        self._ZoneId = None
        self._Filters = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRulesResponse(AbstractModel):
    """DescribeRules response structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site
        :type ZoneId: str
        :param _RuleItems: List of rules. Rules are sorted in order of execution.
        :type RuleItems: list of RuleItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ZoneId = None
        self._RuleItems = None
        self._RequestId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RuleItems(self):
        return self._RuleItems

    @RuleItems.setter
    def RuleItems(self, RuleItems):
        self._RuleItems = RuleItems

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("RuleItems") is not None:
            self._RuleItems = []
            for item in params.get("RuleItems"):
                obj = RuleItem()
                obj._deserialize(item)
                self._RuleItems.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRulesSettingRequest(AbstractModel):
    """DescribeRulesSetting request structure.

    """


class DescribeRulesSettingResponse(AbstractModel):
    """DescribeRulesSetting response structure.

    """

    def __init__(self):
        r"""
        :param _Actions: List of the settings of the rule engine that can be used for request match and their detailed recommended configuration information.
        :type Actions: list of RulesSettingAction
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Actions = None
        self._RequestId = None

    @property
    def Actions(self):
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Actions") is not None:
            self._Actions = []
            for item in params.get("Actions"):
                obj = RulesSettingAction()
                obj._deserialize(item)
                self._Actions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSecurityIPGroupInfoRequest(AbstractModel):
    """DescribeSecurityIPGroupInfo request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID, used to specify the query scope.
        :type ZoneId: str
        :param _Limit: Maximum number of entries returned in a single response. Default value: 20. Maximum query entries: 1000.
        :type Limit: int
        :param _Offset: The starting entry offset for pagination queries. The default value is 0.
        :type Offset: int
        """
        self._ZoneId = None
        self._Limit = None
        self._Offset = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

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
        self._ZoneId = params.get("ZoneId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityIPGroupInfoResponse(AbstractModel):
    """DescribeSecurityIPGroupInfo response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The number of IP groups that meet the conditions.
        :type TotalCount: int
        :param _IPGroups: Detailed configuration information of the IP group, including the ID, name, and IP/network segment list of each IP group.
        :type IPGroups: list of IPGroup
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._IPGroups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def IPGroups(self):
        return self._IPGroups

    @IPGroups.setter
    def IPGroups(self, IPGroups):
        self._IPGroups = IPGroups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("IPGroups") is not None:
            self._IPGroups = []
            for item in params.get("IPGroups"):
                obj = IPGroup()
                obj._deserialize(item)
                self._IPGroups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSecurityIPGroupRequest(AbstractModel):
    """DescribeSecurityIPGroup request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID, used to specify the scope of the queried site.
        :type ZoneId: str
        :param _GroupIds: Specifies the ID of a security IP group.
<li>When this parameter is provided, only the configuration of the security IP group with the specified ID is queried.</li>
<li>When this parameter is not provided, information of all security IP groups under the site is returned.</li>
        :type GroupIds: list of int
        """
        self._ZoneId = None
        self._GroupIds = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._GroupIds = params.get("GroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityIPGroupResponse(AbstractModel):
    """DescribeSecurityIPGroup response structure.

    """

    def __init__(self):
        r"""
        :param _IPGroups: Detailed configuration information of security IP groups, including the ID, name, and IP/IP range list information of each security IP group.
        :type IPGroups: list of IPGroup
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IPGroups = None
        self._RequestId = None

    @property
    def IPGroups(self):
        return self._IPGroups

    @IPGroups.setter
    def IPGroups(self, IPGroups):
        self._IPGroups = IPGroups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("IPGroups") is not None:
            self._IPGroups = []
            for item in params.get("IPGroups"):
                obj = IPGroup()
                obj._deserialize(item)
                self._IPGroups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSecurityTemplateBindingsRequest(AbstractModel):
    """DescribeSecurityTemplateBindings request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site to query
        :type ZoneId: str
        :param _TemplateId: ID of the policy template to query.
        :type TemplateId: list of str
        """
        self._ZoneId = None
        self._TemplateId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityTemplateBindingsResponse(AbstractModel):
    """DescribeSecurityTemplateBindings response structure.

    """

    def __init__(self):
        r"""
        :param _SecurityTemplate: Bindings of the specified policy template.

When a domain name of a site is bound with the specified policy template, `TemplateScope` includes the `ZoneId` of the related site and the bindings of the domain name. 

Note: If the template is not bound with any domain name, and there is not any existing binding, `TemplateScope=0` is returned.

In the binding list, the same domain name may appear repeatedly in the `EntityStatus` list with different `Status`. For example, when a domain name is being bound to another policy template, it's marked both `online` and `pending`.
        :type SecurityTemplate: list of SecurityTemplateBinding
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecurityTemplate = None
        self._RequestId = None

    @property
    def SecurityTemplate(self):
        return self._SecurityTemplate

    @SecurityTemplate.setter
    def SecurityTemplate(self, SecurityTemplate):
        self._SecurityTemplate = SecurityTemplate

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SecurityTemplate") is not None:
            self._SecurityTemplate = []
            for item in params.get("SecurityTemplate"):
                obj = SecurityTemplateBinding()
                obj._deserialize(item)
                self._SecurityTemplate.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTimingL4DataRequest(AbstractModel):
    """DescribeTimingL4Data request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: The start time.
        :type StartTime: str
        :param _EndTime: The end time.
        :type EndTime: str
        :param _MetricNames: Query indicator. Values: 
<li>l4Flow_connections: Number of access connections;</li>
<li>l4Flow_flux: Total access traffic;</li>
<li>l4Flow_inFlux: Ingress access traffic;</li>
<li>l4Flow_outFlux: Egress access traffic. </li>
        :type MetricNames: list of str
        :param _ZoneIds: ZoneId set. This parameter is required.
        :type ZoneIds: list of str
        :param _ProxyIds: List of L4 proxy IDs. All L4 proxies will be selected if this field is not specified.
        :type ProxyIds: list of str
        :param _Interval: The query granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minutes;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the query period. <br>Period ≤ 1 hour: `min`; <br>1 hour < Period ≤ 2 days: `5min`; <br>2 days < period ≤ 7 days: `hour`; <br>Period > 7 days: `day`.
        :type Interval: str
        :param _Filters: Filter criteria. The detailed Key values of filter criteria are as follows:
<li>ruleId: Filter by forwarding rule ID.</li>
<li>proxyId: Filter by L4 proxy instance ID.</li>
        :type Filters: list of QueryCondition
        :param _Area: Geolocation scope. Values:
<li>`overseas`: Regions outside the Chinese mainland</li>
<li>`mainland`: Chinese mainland</li>
<li>`global`: Global</li>If this field is not specified, the default value `global` is used.
        :type Area: str
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricNames = None
        self._ZoneIds = None
        self._ProxyIds = None
        self._Interval = None
        self._Filters = None
        self._Area = None

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
    def MetricNames(self):
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def ProxyIds(self):
        return self._ProxyIds

    @ProxyIds.setter
    def ProxyIds(self, ProxyIds):
        self._ProxyIds = ProxyIds

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricNames = params.get("MetricNames")
        self._ZoneIds = params.get("ZoneIds")
        self._ProxyIds = params.get("ProxyIds")
        self._Interval = params.get("Interval")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimingL4DataResponse(AbstractModel):
    """DescribeTimingL4Data response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of query results.
        :type TotalCount: int
        :param _Data: The list of L4 traffic data recorded over time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TimingDataRecord
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TimingDataRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTimingL7AnalysisDataRequest(AbstractModel):
    """DescribeTimingL7AnalysisData request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: The start time.
        :type StartTime: str
        :param _EndTime: The end time.
        :type EndTime: str
        :param _MetricNames: Indicator list. Values: 
<li>l7Flow_outFlux: Edgeone response traffic;</li>
<li>l7Flow_inFlux: Edgeone request traffic;</li>
<li>l7Flow_outBandwidth: Edgeone response bandwidth;</li>
<li>l7Flow_inBandwidth: Edgeone request bandwidth;</li>
<li>l7Flow_request: Number of access requests;</li>
<li>l7Flow_flux: Uplink + downlink traffic of access requests;< li>
<li>l7Flow_bandwidth: Uplink + downlink bandwidth of access requests. </li>
        :type MetricNames: list of str
        :param _ZoneIds: ZoneId set. This parameter is required.
        :type ZoneIds: list of str
        :param _Interval: The query granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minutes;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the query period. <br>Period ≤ 1 hour: `min`; <br>1 hour < Period ≤ 2 days: `5min`; <br>2 days < period ≤ 7 days: `hour`; <br>Period > 7 days: `day`.
        :type Interval: str
        :param _Filters: Filters
<li>country<br>Filter by the <strong> Country/Region</strong>. The country/region follows <a href="https://baike.baidu.com/item/ISO%203166-1/5269555">ISO 3166</a> specification. </li>
<li>`province`<br>Filter by the <strong>specified province name</strong>. It’s only available when `Area` is `mainland`.</li>
<li>`isp`<br>:   Filter by the specified ISP. It’s only available when `Area` is `mainland`.<br>Values: <br>`2`: CTCC; <br>`26`: CUCC; <br>`1046`: CMCC; <br>`3947`: CTT; <br>`38`: CERNET; <br>`43`: GWBN; <br>`0`: Others.</li>
<li>`domain`<br>: Filter by the specified <strong>sub-domain name</strong>, such as `test.example.com`</li>
<li>`url`:<br>Filter by the specified <strong>URL path<strong> (such as `/content` or `content/test.jpg`).<br>If this parameter is specified, the max query period is the last 30 days.<br>The <a href="https://intl.cloud.tencent.com/document/product/1552/77380?from_cn_redirect=1#edgeone-.E5.A5.97.E9.A4.90">max data query scope stated in the service package specifications</a> of the site (if `ZoneIds` specified) becomes invalid.</li>
<li>`referer`:<br>Filter by the specified <strong>Referer header</strong>, such as `example.com`.<br>If this parameter is specified, the max query period is the last 30 days.<br>The<a href="https://intl.cloud.tencent.com/document/product/1552/77380?from_cn_redirect=1#edgeone-.E5.A5.97.E9.A4.90">max data query scope stated in the service package specifications</a> of the site (if `ZoneIds` specified) becomes invalid.</li>
<li>`resourceType`:<br>Filter by the specified <strong>resource file type</strong>, such as `jpg`, `css`. <br>Note that if this parameter is specified, the max data query period is the last 30 days. <br>The <a href="https://intl.cloud.tencent.com/document/product/1552/77380?from_cn_redirect=1#edgeone-.E5.A5.97.E9.A4.90">data query scope stated in the specifications of service package</a> related with the `ZoneIds` becomes invalid.</li>
<li>`protocol`:<br> Filter  by the specified <strong>HTTP protocol</strong> version <br>Values: <br>`HTTP/1.0`: HTTP 1.0;<br>`HTTP/1.1`: HTTP 1.1;<br>`HTTP/2.0`: HTTP 2.0;<br>`HTTP/3.0`: HTTP 3.0;<br>`WebSocket`: WebSocket.</li>
<li>`socket`:<br>Filter by the specified <strong>HTTP protocol</strong> type <br>Values: <br>`HTTP`: HTTP protocol;<br>`HTTPS`: HTTPS protocol;<br>`QUIC`: QUIC protocol.</li>
<li>statusCode<br> Filter by [strong> Status Code/strong>]. lt;br> If you only fill in statusCode parameter, you can query data of nearly 30 days at most; <br> If statusCode+Zonelds parameter is filled in at the same time, the supported query data range is the smaller of a href="https://intl.cloud.tencent.com/document/product/1552/77380?from_cn_redirect=1#edgeone-.E5.A5.97.E9.A4.90"> Maximum query range of data analysis/a> and 30 days supported by package. lt;br> The corresponding Value options are as follows: <br> 1XX: Status code of type 1xx; <br> 100:100 status code; <br> 101:101 status code; <br> 102:102 status code; <br> 2XX: Status code of type 2xx; <br> 200:200 status code; <br> 201:201 status code; <br> 202:202 status code; <br> 203:203 status code; <br> 204:204 status code; <br> 205:205 status code; <br> 206:206 status code; <br> 207:207 status code; <br> 3XX: Status code of type 3xx; <br> 300:300 status code; <br> 301:301 status code; <br> 302:302 status code; <br> 303:303 status code; <br> 304:304 status code; <br> 305:305 status code; <br> 307:307 status code; <br> 4XX: Status code of type 4xx; <br> 400:400 status code; <br> 401:401 status code; <br> 402:402 status code; <br> 403:403 status code; <br> 404:404 status code; <br> 405:405 status code; <br> 406:406 status code; <br> 407:407 status code; <br> 408:408 status code; <br> 409:409 status code; <br> 410:410 status code; <br> 411:411 status code; <br> 412:412 status code; <br> 412:413 Status Code; <br> 414:414 status code; <br> 415:415 status code; <br> 416:416 status code; <br> 417:417 status code; <br> 422:422 status code; <br> 423:423 status code; <br> 424:424 status code; <br> 426:426 status code; <br> 451:451 status code; <br> 5XX: Status code of type 5xx; <br> 500:500 status code; <br> 501:501 status code; <br> 502:502 status code; <br> 503:503 status code; <br> 504:504 status code; <br> 505:505 status code; <br> 506:506 status code; <br> 507:507 status code; <br> 510:510 status code; <br> 514:514 status code; <br> 544:544 Status Code.& lt</li>
<li>`browserType`:<br>Filter by the specified <strong>browser type</strong>. <br>If this parameter is specified, the max query period is the last 30 days.<br>The <a href="https://intl.cloud.tencent.com/document/product/1552/77380?from_cn_redirect=1#edgeone-.E5.A5.97.E9.A4.90">max data query scope stated in the service package specifications</a> of the site (if `ZoneIds` specified) becomes invalid.</li><br>Values: <br>`Firefox`: Firefox browser; <br>`Chrome`: Chrome browser; <br>`Safari`: Safari browser; <br>`MicrosoftEdge`: Microsoft Edge browser; <br>`IE`: IE browser; <br>`Opera`: Opera browser; <br>`QQBrowser`: QQ browser; <br>`LBBrowser`: LB browser; <br>`MaxthonBrowser`: Maxthon browser; <br>`SouGouBrowser`: Sogou browser; <br>`BIDUBrowser`: Baidu browser; <br>`TaoBrowser`: Tao browser; <br>`UBrowser`: UC browser; <br>`Other`: Other browsers; <br>`Empty`: The browser type is not specified; <br>`Bot`: Web crawler.</li>
<li>`deviceType`:<br>Filter by the <strong>device type</strong>.<br>If this parameter is specified, the max query period is the last 30 days.<br>The <a href="https://intl.cloud.tencent.com/document/product/1552/77380?from_cn_redirect=1#edgeone-.E5.A5.97.E9.A4.90">max data query scope stated in the service package specifications</a> of the site (if `ZoneIds` specified) becomes invalid.<br>Values:<br>`TV`: TV; <br>`Tablet`: Tablet;<br>`Mobile`: Mobile phone; <br>`Desktop`: Desktop device;<br>`Other`: Other device;<br>`Empty`: Device type not specified.</li>
<li>`operatingSystemType`:<br>Filter by the <strong>operating system</strong>.<br>If this parameter is specified, the max query period is the last 30 days.<br>The <a href="https://intl.cloud.tencent.com/document/product/1552/77380?from_cn_redirect=1#edgeone-.E5.A5.97.E9.A4.90">max data query scope stated in the service package specifications</a> of the site (if `ZoneIds` specified) becomes invalid.<br>Values: <br>`Linux`: Linux OS; <br>`MacOS`: Mac OS;<br>`Android`: Android OS;<br>`IOS`: iOS OS;<br>`Windows`: Windows OS;<br>`NetBSD`: NetBSD OS;<br>`ChromiumOS`: Chromium OS; <br>`Bot`: Web crawler:<br>`Other`: Other OS;   <br>`Empty`: The OS is not specified.</li>
<li>`tlsVersion`:<br>Filter by the <strong>TLS version</strong>. <br>If this parameter is specified, the max query period is the last 30 days.<br>The <a href="https://intl.cloud.tencent.com/document/product/1552/77380?from_cn_redirect=1#edgeone-.E5.A5.97.E9.A4.90">max data query scope stated in the service package specifications</a> of the site (if `ZoneIds` specified) becomes invalid.<br>Values: <br>`TLS1.0`: TLS 1.0;<br>`TLS1.1`: TLS 1.1; <br>`TLS1.2`: TLS 1.2;<br>`TLS1.3`: TLS 1.3.</li>
<li>`ipVersion`<br>Filter by the <strong>specified IP version. <br>Values: <br>`4`: IPv4; <br>`6`: IPv6.
<li>`tagKey`<br>Filter by the <strong>Tag Key</strong>. </li>
<li>`tagValue`<br>Filter by the <strong>Tag Value</strong>. </li>
        :type Filters: list of QueryCondition
        :param _Area: Geolocation scope. Values:
<li>`overseas`: Regions outside the Chinese mainland</li>
<li>`mainland`: Chinese mainland</li>
<li>`global`: Global</li>If this field is not specified, the default value `global` is used.
        :type Area: str
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricNames = None
        self._ZoneIds = None
        self._Interval = None
        self._Filters = None
        self._Area = None

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
    def MetricNames(self):
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricNames = params.get("MetricNames")
        self._ZoneIds = params.get("ZoneIds")
        self._Interval = params.get("Interval")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimingL7AnalysisDataResponse(AbstractModel):
    """DescribeTimingL7AnalysisData response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of query results.
        :type TotalCount: int
        :param _Data: The list of L7 traffic data recorded over time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TimingDataRecord
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TimingDataRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTimingL7CacheDataRequest(AbstractModel):
    """DescribeTimingL7CacheData request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: The start time.
        :type StartTime: str
        :param _EndTime: The end time.
        :type EndTime: str
        :param _MetricNames: The query metric. Values:
<li>`l7Cache_outFlux`: Response traffic.</li>
<li>`l7Cache_request`: Response requests.</li>
<li>`l7Cache_outBandwidth`: Response bandwidth.</li>
        :type MetricNames: list of str
        :param _ZoneIds: ZoneId set. This parameter is required.
        :type ZoneIds: list of str
        :param _Filters: Filter conditions. See below for details: 
<li>`domain`<br>   Filter by the <strong>sub-domain name</strong>, such as `test.example.com`<br>   Type: String<br>   Required: No</li>
<li>`url`<br>   Filter by the <strong>URL</strong>, such as `/content`. The query period cannot exceed 30 days. <br>   Type: String<br>   Required: No</li>
<li>`resourceType`<br>   Filter by the <strong>resource file type</strong>, such as `jpg`, `png`. The query period cannot exceed 30 days.<br>  Type: String<br>   Required: No</li>
<li>cacheType<br>  Filter by the <strong>cache hit result</strong>.<br> Type: String<br>   Required: No<br>   Values: <br>   `hit`: Cache hit; <br>   `dynamic`: Resource non-cacheable; <br>   `miss`: Cache miss</li>
<li>`statusCode`<br>   Filter by the <strong> status code</strong>. The query period  cannot exceed 30 days. <br>   Type: String<br>   Required: No<br>   Values: <br>   `1XX`: All 1xx status codes;<br>   `100`: 100 status code;<br>   `101`: 101 status code;<br>   `102`: 102 status code;<br>   `2XX`: All 2xx status codes;<br>   `200`: 200 status code;<br>   `201`: 201 status code;<br>   `202`: 202 status code;<br>   `203`: 203 status code;<br>   `204`: 204 status code;<br>   `205`: 205 status code;<br>   `206`: 206 status code;<br>   `207`: 207 status code;<br>   `3XX`: All 3xx status codes;<br>   `300`: 300 status code;<br>   `301`: 301 status code;<br>   `302`: 302 status code;<br>   `303`: 303 status code;<br>   `304`: 304 status code;<br>   `305`: 305 status code;<br>   `307`: 307 status code;<br>   `4XX`: All 4xx status codes;<br>   `400`: 400 status code;<br>   `401`: 401 status code;<br>   `402`: 402 status code;<br>   `403`: 403 status code;<br>   `404`: 404 status code;<br>   `405`: 405 status code;<br>   `406`: 406 status code;<br>   `407`: 407 status code;<br>   `408`: 408 status code;<br>   `409`: 409 status code;<br>   `410`: 410 status code;<br>   `411`: 411 status code;<br>   `412`: 412 status code;<br>   `412`: 413 status code;<br>   `414`: 414 status code;<br>   `415`: 415 status code;<br>   `416`: 416 status code;<br>   `417`: 417 status code;<br>  `422`: 422 status code;<br>   `423`: 423 status code;<br>   `424`: 424 status code;<br>   `426`: 426 status code;<br>   `451`: 451 status code;<br>   `5XX`: All 5xx status codes;<br>   `500`: 500 status code;<br>   `501`: 501 status code;<br>   `502`: 502 status code;<br>   `503`: 503 status code;<br>   `504`: 504 status code;<br>   `505`: 505 status code;<br>   `506`: 506 status code;<br>   `507`: 507 status code;<br>   `510`: 510 status code;<br>   `514`: 514 status code;<br>   `544`: 544 status code.</li>
<li>`tagKey`:<br>   Filter by the <strong>tag key</strong><br>   Type: String<br>   Required: No</li>
<li>`tagValue`<br>   Filter by the <strong>tag value</strong><br>   Type: String<br>   Required: No</li>
        :type Filters: list of QueryCondition
        :param _Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minutes;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param _Area: Geolocation scope. Values:
<li>`overseas`: Regions outside the Chinese mainland</li>
<li>`mainland`: Chinese mainland</li>
<li>`global`: Global</li>If this field is not specified, the default value `global` is used.
        :type Area: str
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricNames = None
        self._ZoneIds = None
        self._Filters = None
        self._Interval = None
        self._Area = None

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
    def MetricNames(self):
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricNames = params.get("MetricNames")
        self._ZoneIds = params.get("ZoneIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Interval = params.get("Interval")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimingL7CacheDataResponse(AbstractModel):
    """DescribeTimingL7CacheData response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of query results.
        :type TotalCount: int
        :param _Data: The list of cached L7 time-series data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TimingDataRecord
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TimingDataRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopL7AnalysisDataRequest(AbstractModel):
    """DescribeTopL7AnalysisData request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: The start time.
        :type StartTime: str
        :param _EndTime: The end time.
        :type EndTime: str
        :param _MetricName: Metrics to query. Valid values: 
<li>`l7Flow_outFlux_country`: Query traffic by country/region;</li>
<li>`l7Flow_outFlux_statusCode`: Query traffic by status code;</li>
<li>`l7Flow_outFlux_domain`: Query traffic by domain;</li>
<li>`l7Flow_outFlux_url`: Query traffic by URL;</li>
<li>`l7Flow_outFlux_resourceType`: Query traffic by resource type;</li>
<li>`l7Flow_outFlux_sip`: Query traffic by source IP;</li>
<li>`l7Flow_outFlux_referers`: Query traffic by refer information;</li>
<li>`l7Flow_outFlux_ua_device`: Query traffic by device;</li>
<li>`l7Flow_outFlux_ua_browser`: Query traffic by browser;</li>
<li>`l7Flow_outFlux_us_os`: Query traffic by OS;</li>
<li>`l7Flow_request_country`: Query requests by country/region;</li>
<li>`l7Flow_request_statusCode`: Query requests by status code;</li>
<li>`l7Flow_request_domain`: Query requests by domain;</li>
<li>`l7Flow_request_url`: Query requests by URL;</li>
<li>`l7Flow_request_resourceType`: Query requests by resource type;</li>
<li>`l7Flow_request_sip`: Query requests by source IP;</li>
<li>`l7Flow_request_referer`: Query requests by refer information;</li>
<li>`l7Flow_request_ua_device`: Query requests by device;</li>
<li>`l7Flow_request_ua_browser`: Query requests by browser;</li>
<li>`l7Flow_request_us_os`: Query requests by OS.</li>

        :type MetricName: str
        :param _ZoneIds: ZoneId set. This parameter is required.
        :type ZoneIds: list of str
        :param _Limit: Queries the top N data entries. Maximum value: 1000. Top 10 data entries will be queried if this field is not specified.
        :type Limit: int
        :param _Filters: Filters
<li>`country`<br>Filter by the <strong> Country/Region</strong>. The country/region follows <a href="https://baike.baidu.com/item/ISO%203166-1/5269555">ISO 3166</a> specification. </li>
<li>`province`<br>Filter by the <strong>specified province name</strong>. It’s only available when `Area` is `mainland`.</li>
<li>`isp`<br>:   Filter by the specified ISP. It’s only available when `Area` is `mainland`.<br>Values: <br>`2`: CTCC; <br>`26`: CUCC; <br>`1046`: CMCC; <br>`3947`: CTT; <br>`38`: CERNET; <br>`43`: GWBN; <br>`0`: Others.</li>
<li>`domain`<br>: Filter by the specified <strong>sub-domain name</strong>, such as `test.example.com`</li>
<li>`url`:<br>Filter by the <strong>specified URL Path (such as `/content` or `content/test.jpg`. <br>If this parameter is specified, the max query period is the last 30 days.<br>The <a href="https://intl.cloud.tencent.com/document/product/1552/77380?from_cn_redirect=1#edgeone-.E5.A5.97.E9.A4.90">max data query scope stated in the service package specifications</a> of the site (if `ZoneIds` specified) becomes invalid.</li>
<li>`referer`:<br>Filter by the specified <strong>Referer header</strong>, such as `example.com`.<br>If this parameter is specified, the max query period is the last 30 days.<br>The <a href="https://intl.cloud.tencent.com/document/product/1552/77380?from_cn_redirect=1#edgeone-.E5.A5.97.E9.A4.90">max data query scope stated in the service package specifications</a> of the site (if `ZoneIds` specified) becomes invalid.</li>
<li>`resourceType`:<br>Filter by the specified <strong>resource file type</strong>, such as `jpg`, `css`. <br>If this parameter is specified, the max query period is the last 30 days.<br>The <a href="https://intl.cloud.tencent.com/document/product/1552/77380?from_cn_redirect=1#edgeone-.E5.A5.97.E9.A4.90">max data query scope stated in the service package specifications</a> of the site (if `ZoneIds` specified) becomes invalid.</li>
<li>`protocol`:<br> Filter by the specified <strong>HTTP protocol</strong> version <br>Values: <br>`HTTP/1.0`: HTTP 1.0;<br>`HTTP/1.1`: HTTP 1.1;<br>`HTTP/2.0`: HTTP 2.0;<br>`HTTP/3.0`: HTTP 3.0;<br>`WebSocket`: WebSocket.</li>
<li>`socket`:<br>Filter by the specified <strong>HTTP protocol type</strong> <br>Values:<br>`HTTP`: HTTP protocol; <br>`HTTPS`: HTTPS protocol;<br>`QUIC`: QUIC protocol.
<li>`statusCode`:<br> Filter by the <strong> Status Code</strong><br>If this parameter is specified, the max query period is the last 30 days.<br>The <a href="https://intl.cloud.tencent.com/document/product/1552/77380?from_cn_redirect=1#edgeone-.E5.A5.97.E9.A4.90">max data query scope stated in the service package specifications</a> of the site (if `ZoneIds` specified) becomes invalid.<br>Values:<br>1XX: Status code of type 1xx <br>100: 100 status code <br>101: 101 status code <br>102: 102 status code <br>2XX: Status code of type 2xx <br>200: 200 status code <br>201: 201 status code <br>202: 202 status code <br>203: 203 status code <br>204: 204 status code <br>205: 205 status code <br>206: 206 status code <br>207: 207 status code <br>3XX: Status code of type 3xx <br>300: 300 status code <br>301: 301 status code <br>302: 302 status code <br>303: 303 status code <br>304: 304 status code <br>305: 305 status code <br>307: 307 status code <br>4XX: Status code of type 4xx <br>400: 400 status code <br>401: 401 status code <br>402: 402 status code <br>403: 403 status code <br>404: 404 status code <br>405: 405 status code <br>406: 406 status code <br>407: 407 status code <br>408: 408 status code <br>409: 409 status code <br>410: 410 status code <br>411: 411 status code <br>412: 412 status code <br>412: 413 Status Code <br>414: 414 status code <br>415: 415 status code <br>416: 416 status code <br>417: 417 status code <br>422: 422 status code <br>423: 423 status code <br>424: 424 status code <br>426: 426 status code <br>451: 451 status code <br>5XX: Status code of type 5xx <br>500: 500 status code <br>501: 501 status code <br>502:502 status code <br>503: 503 status code <br>504: 504 status code <br>505: 505 status code <br>506: 506 status code <br>507: 507 status code <br>510: 510 status code <br>514: 514 status code <br>544: 544 Status Code. </li>
<li>`browserType`:<br>Filter by the specified <strong>browser type</strong>. <br>If this parameter is specified, the max query period is the last 30 days.<br>The <a href="https://intl.cloud.tencent.com/document/product/1552/77380?from_cn_redirect=1#edgeone-.E5.A5.97.E9.A4.90">max data query scope stated in the service package specifications</a> of the site (if `ZoneIds` specified) becomes invalid.</li><br>Values: <br>`Firefox`: Firefox browser; <br>`Chrome`: Chrome browser; <br>`Safari`: Safari browser; <br>`MicrosoftEdge`: Microsoft Edge browser; <br>`IE`: IE browser; <br>`Opera`: Opera browser; <br>`QQBrowser`: QQ browser; <br>`LBBrowser`: LB browser; <br>`MaxthonBrowser`: Maxthon browser; <br>`SouGouBrowser`: Sogou browser; <br>`BIDUBrowser`: Baidu browser; <br>`TaoBrowser`: Tao browser; <br>`UBrowser`: UC browser; <br>`Other`: Other browsers; <br>`Empty`: The browser type is not specified; <br>`Bot`: Web crawler.</li>
<li>`deviceType`:<br>Filter by the <strong>device type</strong>.<br>If this parameter is specified, the max query period is the last 30 days.<br>The <a href="https://intl.cloud.tencent.com/document/product/1552/77380?from_cn_redirect=1#edgeone-.E5.A5.97.E9.A4.90">max data query scope stated in the service package specifications</a> of the site (if `ZoneIds` specified) becomes invalid.<br>Values:<br>`TV`: TV; <br>`Tablet`: Tablet;<br>`Mobile`: Mobile phone; <br>`Desktop`: Desktop device;<br>`Other`: Other device;<br>`Empty`: Device type not specified.</li>
<li>`operatingSystemType`:<br>Filter by the <strong>operating system</strong>.<br>If this parameter is specified, the max query period is the last 30 days.<br>The <a href="https://intl.cloud.tencent.com/document/product/1552/77380?from_cn_redirect=1#edgeone-.E5.A5.97.E9.A4.90">max data query scope stated in the service package specifications</a> of the site (if `ZoneIds` specified) becomes invalid.<br>Values: <br>`Linux`: Linux OS; <br>`MacOS`: Mac OS;<br>`Android`: Android OS;<br>`IOS`: iOS OS;<br>`Windows`: Windows OS;<br>`NetBSD`: NetBSD OS;<br>`ChromiumOS`: Chromium OS; <br>`Bot`: Web crawler:<br>`Other`: Other OS;   <br>`Empty`: The OS is not specified.</li>
<li>`tlsVersion`:<br>Filter by the <strong>TLS version</strong>. <br>If this parameter is specified, the max query period is the last 30 days.<br>The <a href="https://intl.cloud.tencent.com/document/product/1552/77380?from_cn_redirect=1#edgeone-.E5.A5.97.E9.A4.90">max data query scope stated in the service package specifications</a> of the site (if `ZoneIds` specified) becomes invalid.<br>Values: <br>`TLS1.0`: TLS 1.0;<br>`TLS1.1`: TLS 1.1; <br>`TLS1.2`: TLS 1.2;<br>`TLS1.3`: TLS 1.3.</li>
<li>`ipVersion`<br>Filter by the <strong>specified IP version. <br>Values: <br>`4`: IPv4; <br>`6`: IPv6.
<li>`tagKey`<br>Filter by the <strong>Tag Key</strong>. </li>
<li>`tagValue`<br>Filter by the <strong>Tag Value</strong>. </li>
        :type Filters: list of QueryCondition
        :param _Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param _Area: Geolocation scope. Values:
<li>`overseas`: Regions outside the Chinese mainland</li>
<li>`mainland`: Chinese mainland</li>
<li>`global`: Global</li>If this field is not specified, the default value `global` is used.
        :type Area: str
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None
        self._ZoneIds = None
        self._Limit = None
        self._Filters = None
        self._Interval = None
        self._Area = None

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
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
        self._ZoneIds = params.get("ZoneIds")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Interval = params.get("Interval")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopL7AnalysisDataResponse(AbstractModel):
    """DescribeTopL7AnalysisData response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of query results.
        :type TotalCount: int
        :param _Data: The list of top-ranked L7 traffic data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TopDataRecord
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TopDataRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopL7CacheDataRequest(AbstractModel):
    """DescribeTopL7CacheData request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: The start time.
        :type StartTime: str
        :param _EndTime: The end time.
        :type EndTime: str
        :param _MetricName: The query metric. Values:
<li>`l7Cache_outFlux_domain`: Host/Domain name;</li>
<li>`l7Cache_outFlux_url`: URL address;</li>
<li>`l7Cache_outFlux_resourceType`: Resource type;</li>
<li>`l7Cache_outFlux_statusCode`: Status code.</li>
        :type MetricName: str
        :param _ZoneIds: ZoneId set. This parameter is required.
        :type ZoneIds: list of str
        :param _Limit: The number of data entries to be queried. The maximum value is 1000. If it is not specified, the value 10 is used by default, indicating that the top 10 data entries.
        :type Limit: int
        :param _Filters: Filter conditions. See below for details: 
<li>`domain`<br>   Filter by the <strong>sub-domain name</strong>, such as `test.example.com`<br>   Type: String<br>   Required: No</li>
<li>`url`<br>   Filter by the <strong>URL</strong>, such as `/content`. The query period cannot exceed 30 days. <br>   Type: String<br>   Required: No</li>
<li>`resourceType`<br>   Filter by the <strong>resource file type</strong>, such as `jpg`, `png`. The query period cannot exceed 30 days.<br>  Type: String<br>   Required: No</li>
<li>cacheType<br>  Filter by the <strong>cache hit result</strong>.<br> Type: String<br>   Required: No<br>   Values: <br>   `hit`: Cache hit; <br>   `dynamic`: Resource non-cacheable; <br>   `miss`: Cache miss</li>
<li>`statusCode`<br>   Filter by the <strong> status code</strong>. The query period  cannot exceed 30 days. <br>   Type: String<br>   Required: No<br>   Values: <br>   `1XX`: All 1xx status codes;<br>   `100`: 100 status code;<br>   `101`: 101 status code;<br>   `102`: 102 status code;<br>   `2XX`: All 2xx status codes;<br>   `200`: 200 status code;<br>   `201`: 201 status code;<br>   `202`: 202 status code;<br>   `203`: 203 status code;<br>   `204`: 204 status code;<br>   `205`: 205 status code;<br>   `206`: 206 status code;<br>   `207`: 207 status code;<br>   `3XX`: All 3xx status codes;<br>   `300`: 300 status code;<br>   `301`: 301 status code;<br>   `302`: 302 status code;<br>   `303`: 303 status code;<br>   `304`: 304 status code;<br>   `305`: 305 status code;<br>   `307`: 307 status code;<br>   `4XX`: All 4xx status codes;<br>   `400`: 400 status code;<br>   `401`: 401 status code;<br>   `402`: 402 status code;<br>   `403`: 403 status code;<br>   `404`: 404 status code;<br>   `405`: 405 status code;<br>   `406`: 406 status code;<br>   `407`: 407 status code;<br>   `408`: 408 status code;<br>   `409`: 409 status code;<br>   `410`: 410 status code;<br>   `411`: 411 status code;<br>   `412`: 412 status code;<br>   `412`: 413 status code;<br>   `414`: 414 status code;<br>   `415`: 415 status code;<br>   `416`: 416 status code;<br>   `417`: 417 status code;<br>  `422`: 422 status code;<br>   `423`: 423 status code;<br>   `424`: 424 status code;<br>   `426`: 426 status code;<br>   `451`: 451 status code;<br>   `5XX`: All 5xx status codes;<br>   `500`: 500 status code;<br>   `501`: 501 status code;<br>   `502`: 502 status code;<br>   `503`: 503 status code;<br>   `504`: 504 status code;<br>   `505`: 505 status code;<br>   `506`: 506 status code;<br>   `507`: 507 status code;<br>   `510`: 510 status code;<br>   `514`: 514 status code;<br>   `544`: 544 status code.</li>
<li>`tagKey`:<br>   Filter by the <strong>tag key</strong><br>   Type: String<br>   Required: No</li>
<li>`tagValue`<br>   Filter by the <strong>tag value</strong><br>   Type: String<br>   Required: No</li>
        :type Filters: list of QueryCondition
        :param _Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minutes;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param _Area: Geolocation scope. Values:
<li>`overseas`: Regions outside the Chinese mainland</li>
<li>`mainland`: Chinese mainland</li>
<li>`global`: Global</li>If this field is not specified, the default value `global` is used.
        :type Area: str
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None
        self._ZoneIds = None
        self._Limit = None
        self._Filters = None
        self._Interval = None
        self._Area = None

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
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
        self._ZoneIds = params.get("ZoneIds")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Interval = params.get("Interval")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopL7CacheDataResponse(AbstractModel):
    """DescribeTopL7CacheData response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of query results.
        :type TotalCount: int
        :param _Data: The list of cached L7 top-ranked traffic data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TopDataRecord
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TopDataRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeZoneSettingRequest(AbstractModel):
    """DescribeZoneSetting request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: The site ID.
        :type ZoneId: str
        """
        self._ZoneId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneSettingResponse(AbstractModel):
    """DescribeZoneSetting response structure.

    """

    def __init__(self):
        r"""
        :param _ZoneSetting: The site configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneSetting: :class:`tencentcloud.teo.v20220901.models.ZoneSetting`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ZoneSetting = None
        self._RequestId = None

    @property
    def ZoneSetting(self):
        return self._ZoneSetting

    @ZoneSetting.setter
    def ZoneSetting(self, ZoneSetting):
        self._ZoneSetting = ZoneSetting

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ZoneSetting") is not None:
            self._ZoneSetting = ZoneSetting()
            self._ZoneSetting._deserialize(params.get("ZoneSetting"))
        self._RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: The page offset. Default value: 0
        :type Offset: int
        :param _Limit: Limit on paginated queries. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Filters: Filter conditions. Up to 20 values for each filter. If this parameter is not filled in, the information of all sites under the current account is returned. Detailed filtering conditions are as follows:
<li>`zone-name`: Site name </li><li>`zone-id`: Site ID, such as zone-2noz78a8ev6k</li><li>`status`: Site status </li><li>`tag-key`: Tag key </li><li>`tag-value`: Tag value </li>Only `zone-name` supports fuzzy query.
        :type Filters: list of AdvancedFilter
        :param _Order: Sort the returned results according to this field. Values include:
<li>`type`: Connection mode</li>
<li>`area`: Acceleration region</li>
<li>`create-time`: Creation time</li>
<li>`zone-name`: Site name</li>
<li>`use-time`: Last used time</li>
<li>`active-status` Effective status</li> Default value: `create-time`
        :type Order: str
        :param _Direction: Sort direction. If the field value is a number, sort by the numeric value. If the field value is text, sort by the ascill code. Values include:
<li>`asc`: From the smallest to largest</li>
<li>`desc`: From the largest to smallest.</li>Default value: `desc`
        :type Direction: str
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._Order = None
        self._Direction = None

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Direction(self):
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Order = params.get("Order")
        self._Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZonesResponse(AbstractModel):
    """DescribeZones response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible sites.
        :type TotalCount: int
        :param _Zones: Details of sites.
        :type Zones: list of Zone
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Zones = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Zones") is not None:
            self._Zones = []
            for item in params.get("Zones"):
                obj = Zone()
                obj._deserialize(item)
                self._Zones.append(obj)
        self._RequestId = params.get("RequestId")


class DestroyPlanRequest(AbstractModel):
    """DestroyPlan request structure.

    """

    def __init__(self):
        r"""
        :param _PlanId: Plan ID, in the format of edgeone-2wdo315m2y4c.
        :type PlanId: str
        """
        self._PlanId = None

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyPlanResponse(AbstractModel):
    """DestroyPlan response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DetailHost(AbstractModel):
    """Domain name configuration information

    """

    def __init__(self):
        r"""
        :param _ZoneId: The site ID.
        :type ZoneId: str
        :param _Status: The acceleration status. Values:
<li>`process`: In progress</li>
<li>`online`: Enabled</li>
<li>`offline`: Disabled</li>
        :type Status: str
        :param _Host: The domain name.
        :type Host: str
        :param _ZoneName: Name of the site
        :type ZoneName: str
        :param _Cname: The assigned CNAME
        :type Cname: str
        :param _Id: The resource ID.
        :type Id: str
        :param _InstanceId: The instance ID.
        :type InstanceId: str
        :param _Lock: The lock status.
        :type Lock: int
        :param _Mode: The domain name status.
        :type Mode: int
        :param _Area: The acceleration area of the domain name. Values:
<li>`global`: Global.</li>
<li>`mainland`: Chinese mainland.</li>
<li>`overseas`: Outside the Chinese mainland.</li>
        :type Area: str
        :param _AccelerateType: The acceleration type configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccelerateType: :class:`tencentcloud.teo.v20220901.models.AccelerateType`
        :param _Https: The HTTPS configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Https: :class:`tencentcloud.teo.v20220901.models.Https`
        :param _CacheConfig: The cache configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CacheConfig: :class:`tencentcloud.teo.v20220901.models.CacheConfig`
        :param _Origin: The origin configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Origin: :class:`tencentcloud.teo.v20220901.models.Origin`
        :param _SecurityType: The security type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SecurityType: :class:`tencentcloud.teo.v20220901.models.SecurityType`
        :param _CacheKey: The cache key configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CacheKey: :class:`tencentcloud.teo.v20220901.models.CacheKey`
        :param _Compression: The smart compression configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Compression: :class:`tencentcloud.teo.v20220901.models.Compression`
        :param _Waf: The WAF protection configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Waf: :class:`tencentcloud.teo.v20220901.models.Waf`
        :param _CC: The CC protection configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CC: :class:`tencentcloud.teo.v20220901.models.CC`
        :param _DDoS: DDoS mitigation configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type DDoS: :class:`tencentcloud.teo.v20220901.models.DDoS`
        :param _SmartRouting: The smart routing configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SmartRouting: :class:`tencentcloud.teo.v20220901.models.SmartRouting`
        :param _Ipv6: The IPv6 access configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Ipv6: :class:`tencentcloud.teo.v20220901.models.Ipv6`
        :param _ClientIpCountry: Whether to carry the location information of the client IP during origin-pull.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ClientIpCountry: :class:`tencentcloud.teo.v20220901.models.ClientIpCountry`
        """
        self._ZoneId = None
        self._Status = None
        self._Host = None
        self._ZoneName = None
        self._Cname = None
        self._Id = None
        self._InstanceId = None
        self._Lock = None
        self._Mode = None
        self._Area = None
        self._AccelerateType = None
        self._Https = None
        self._CacheConfig = None
        self._Origin = None
        self._SecurityType = None
        self._CacheKey = None
        self._Compression = None
        self._Waf = None
        self._CC = None
        self._DDoS = None
        self._SmartRouting = None
        self._Ipv6 = None
        self._ClientIpCountry = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def Cname(self):
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Lock(self):
        return self._Lock

    @Lock.setter
    def Lock(self, Lock):
        self._Lock = Lock

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def AccelerateType(self):
        return self._AccelerateType

    @AccelerateType.setter
    def AccelerateType(self, AccelerateType):
        self._AccelerateType = AccelerateType

    @property
    def Https(self):
        return self._Https

    @Https.setter
    def Https(self, Https):
        self._Https = Https

    @property
    def CacheConfig(self):
        return self._CacheConfig

    @CacheConfig.setter
    def CacheConfig(self, CacheConfig):
        self._CacheConfig = CacheConfig

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def SecurityType(self):
        return self._SecurityType

    @SecurityType.setter
    def SecurityType(self, SecurityType):
        self._SecurityType = SecurityType

    @property
    def CacheKey(self):
        return self._CacheKey

    @CacheKey.setter
    def CacheKey(self, CacheKey):
        self._CacheKey = CacheKey

    @property
    def Compression(self):
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression

    @property
    def Waf(self):
        return self._Waf

    @Waf.setter
    def Waf(self, Waf):
        self._Waf = Waf

    @property
    def CC(self):
        return self._CC

    @CC.setter
    def CC(self, CC):
        self._CC = CC

    @property
    def DDoS(self):
        return self._DDoS

    @DDoS.setter
    def DDoS(self, DDoS):
        self._DDoS = DDoS

    @property
    def SmartRouting(self):
        return self._SmartRouting

    @SmartRouting.setter
    def SmartRouting(self, SmartRouting):
        self._SmartRouting = SmartRouting

    @property
    def Ipv6(self):
        return self._Ipv6

    @Ipv6.setter
    def Ipv6(self, Ipv6):
        self._Ipv6 = Ipv6

    @property
    def ClientIpCountry(self):
        return self._ClientIpCountry

    @ClientIpCountry.setter
    def ClientIpCountry(self, ClientIpCountry):
        self._ClientIpCountry = ClientIpCountry


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Status = params.get("Status")
        self._Host = params.get("Host")
        self._ZoneName = params.get("ZoneName")
        self._Cname = params.get("Cname")
        self._Id = params.get("Id")
        self._InstanceId = params.get("InstanceId")
        self._Lock = params.get("Lock")
        self._Mode = params.get("Mode")
        self._Area = params.get("Area")
        if params.get("AccelerateType") is not None:
            self._AccelerateType = AccelerateType()
            self._AccelerateType._deserialize(params.get("AccelerateType"))
        if params.get("Https") is not None:
            self._Https = Https()
            self._Https._deserialize(params.get("Https"))
        if params.get("CacheConfig") is not None:
            self._CacheConfig = CacheConfig()
            self._CacheConfig._deserialize(params.get("CacheConfig"))
        if params.get("Origin") is not None:
            self._Origin = Origin()
            self._Origin._deserialize(params.get("Origin"))
        if params.get("SecurityType") is not None:
            self._SecurityType = SecurityType()
            self._SecurityType._deserialize(params.get("SecurityType"))
        if params.get("CacheKey") is not None:
            self._CacheKey = CacheKey()
            self._CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Compression") is not None:
            self._Compression = Compression()
            self._Compression._deserialize(params.get("Compression"))
        if params.get("Waf") is not None:
            self._Waf = Waf()
            self._Waf._deserialize(params.get("Waf"))
        if params.get("CC") is not None:
            self._CC = CC()
            self._CC._deserialize(params.get("CC"))
        if params.get("DDoS") is not None:
            self._DDoS = DDoS()
            self._DDoS._deserialize(params.get("DDoS"))
        if params.get("SmartRouting") is not None:
            self._SmartRouting = SmartRouting()
            self._SmartRouting._deserialize(params.get("SmartRouting"))
        if params.get("Ipv6") is not None:
            self._Ipv6 = Ipv6()
            self._Ipv6._deserialize(params.get("Ipv6"))
        if params.get("ClientIpCountry") is not None:
            self._ClientIpCountry = ClientIpCountry()
            self._ClientIpCountry._deserialize(params.get("ClientIpCountry"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiffIPWhitelist(AbstractModel):
    """Differences between the newest and existing intermediate IPs

    """

    def __init__(self):
        r"""
        :param _LatestIPWhitelist: The latest intermediate IPs.
        :type LatestIPWhitelist: :class:`tencentcloud.teo.v20220901.models.IPWhitelist`
        :param _AddedIPWhitelist: The intermediate IPs added to the existing list.
        :type AddedIPWhitelist: :class:`tencentcloud.teo.v20220901.models.IPWhitelist`
        :param _RemovedIPWhitelist: The intermediate IPs removed from the existing list.
        :type RemovedIPWhitelist: :class:`tencentcloud.teo.v20220901.models.IPWhitelist`
        :param _NoChangeIPWhitelist: The intermediate IPs that remain unchanged.
        :type NoChangeIPWhitelist: :class:`tencentcloud.teo.v20220901.models.IPWhitelist`
        """
        self._LatestIPWhitelist = None
        self._AddedIPWhitelist = None
        self._RemovedIPWhitelist = None
        self._NoChangeIPWhitelist = None

    @property
    def LatestIPWhitelist(self):
        return self._LatestIPWhitelist

    @LatestIPWhitelist.setter
    def LatestIPWhitelist(self, LatestIPWhitelist):
        self._LatestIPWhitelist = LatestIPWhitelist

    @property
    def AddedIPWhitelist(self):
        return self._AddedIPWhitelist

    @AddedIPWhitelist.setter
    def AddedIPWhitelist(self, AddedIPWhitelist):
        self._AddedIPWhitelist = AddedIPWhitelist

    @property
    def RemovedIPWhitelist(self):
        return self._RemovedIPWhitelist

    @RemovedIPWhitelist.setter
    def RemovedIPWhitelist(self, RemovedIPWhitelist):
        self._RemovedIPWhitelist = RemovedIPWhitelist

    @property
    def NoChangeIPWhitelist(self):
        return self._NoChangeIPWhitelist

    @NoChangeIPWhitelist.setter
    def NoChangeIPWhitelist(self, NoChangeIPWhitelist):
        self._NoChangeIPWhitelist = NoChangeIPWhitelist


    def _deserialize(self, params):
        if params.get("LatestIPWhitelist") is not None:
            self._LatestIPWhitelist = IPWhitelist()
            self._LatestIPWhitelist._deserialize(params.get("LatestIPWhitelist"))
        if params.get("AddedIPWhitelist") is not None:
            self._AddedIPWhitelist = IPWhitelist()
            self._AddedIPWhitelist._deserialize(params.get("AddedIPWhitelist"))
        if params.get("RemovedIPWhitelist") is not None:
            self._RemovedIPWhitelist = IPWhitelist()
            self._RemovedIPWhitelist._deserialize(params.get("RemovedIPWhitelist"))
        if params.get("NoChangeIPWhitelist") is not None:
            self._NoChangeIPWhitelist = IPWhitelist()
            self._NoChangeIPWhitelist._deserialize(params.get("NoChangeIPWhitelist"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DnsVerification(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _Subdomain: The host record.
        :type Subdomain: str
        :param _RecordType: The record type.
        :type RecordType: str
        :param _RecordValue: The record value.
        :type RecordValue: str
        """
        self._Subdomain = None
        self._RecordType = None
        self._RecordValue = None

    @property
    def Subdomain(self):
        return self._Subdomain

    @Subdomain.setter
    def Subdomain(self, Subdomain):
        self._Subdomain = Subdomain

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RecordValue(self):
        return self._RecordValue

    @RecordValue.setter
    def RecordValue(self, RecordValue):
        self._RecordValue = RecordValue


    def _deserialize(self, params):
        self._Subdomain = params.get("Subdomain")
        self._RecordType = params.get("RecordType")
        self._RecordValue = params.get("RecordValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadL4LogsRequest(AbstractModel):
    """DownloadL4Logs request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: The start time.
        :type StartTime: str
        :param _EndTime: The end time.
        :type EndTime: str
        :param _ZoneIds: ZoneId set. This parameter is required.
        :type ZoneIds: list of str
        :param _ProxyIds: List of L4 proxy instance IDs.
        :type ProxyIds: list of str
        :param _Limit: Limit on paginated queries. Default value: 20. Maximum value: 300.
        :type Limit: int
        :param _Offset: The page offset. Default value: 0.
        :type Offset: int
        """
        self._StartTime = None
        self._EndTime = None
        self._ZoneIds = None
        self._ProxyIds = None
        self._Limit = None
        self._Offset = None

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
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def ProxyIds(self):
        return self._ProxyIds

    @ProxyIds.setter
    def ProxyIds(self, ProxyIds):
        self._ProxyIds = ProxyIds

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
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ZoneIds = params.get("ZoneIds")
        self._ProxyIds = params.get("ProxyIds")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadL4LogsResponse(AbstractModel):
    """DownloadL4Logs response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of query results.
        :type TotalCount: int
        :param _Data: List of L4 logs.
        :type Data: list of L4OfflineLog
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = L4OfflineLog()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DownloadL7LogsRequest(AbstractModel):
    """DownloadL7Logs request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: The start time.
        :type StartTime: str
        :param _EndTime: The end time.
        :type EndTime: str
        :param _ZoneIds: ZoneId set. This parameter is required.
        :type ZoneIds: list of str
        :param _Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param _Limit: Limit on paginated queries. Default value: 20. Maximum value: 300.
        :type Limit: int
        :param _Offset: The page offset. Default value: 0.
        :type Offset: int
        """
        self._StartTime = None
        self._EndTime = None
        self._ZoneIds = None
        self._Domains = None
        self._Limit = None
        self._Offset = None

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
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

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
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ZoneIds = params.get("ZoneIds")
        self._Domains = params.get("Domains")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadL7LogsResponse(AbstractModel):
    """DownloadL7Logs response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of query results.
        :type TotalCount: int
        :param _Data: List of L7 logs.
        :type Data: list of L7OfflineLog
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = L7OfflineLog()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DropPageConfig(AbstractModel):
    """Block page configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable configuration. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param _WafDropPageDetail: The settings of the block page that applies managed rules. If it is null, the settings that were last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type WafDropPageDetail: :class:`tencentcloud.teo.v20220901.models.DropPageDetail`
        :param _AclDropPageDetail: The settings of the block page that applies custom rules. If it is null, the settings that were last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AclDropPageDetail: :class:`tencentcloud.teo.v20220901.models.DropPageDetail`
        """
        self._Switch = None
        self._WafDropPageDetail = None
        self._AclDropPageDetail = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def WafDropPageDetail(self):
        return self._WafDropPageDetail

    @WafDropPageDetail.setter
    def WafDropPageDetail(self, WafDropPageDetail):
        self._WafDropPageDetail = WafDropPageDetail

    @property
    def AclDropPageDetail(self):
        return self._AclDropPageDetail

    @AclDropPageDetail.setter
    def AclDropPageDetail(self, AclDropPageDetail):
        self._AclDropPageDetail = AclDropPageDetail


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("WafDropPageDetail") is not None:
            self._WafDropPageDetail = DropPageDetail()
            self._WafDropPageDetail._deserialize(params.get("WafDropPageDetail"))
        if params.get("AclDropPageDetail") is not None:
            self._AclDropPageDetail = DropPageDetail()
            self._AclDropPageDetail._deserialize(params.get("AclDropPageDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DropPageDetail(AbstractModel):
    """The configuration details of the block page

    """

    def __init__(self):
        r"""
        :param _PageId: The ID of the block page. Specify `0` to use the default block page. 
(Disused) If 0 is passed, the default block page will be used.
        :type PageId: int
        :param _StatusCode: The HTTP status code to trigger the block page. Range: 100-600, excluding 3xx codes. Code 566: Requests blocked by managed rules. Code 567: Requests blocked by web security rules (except managed rules).
        :type StatusCode: int
        :param _Name: The block page file or URL.
        :type Name: str
        :param _Type: Type of the block page. Values:
<li>`page`: Return the specified page.</li>

        :type Type: str
        :param _CustomResponseId: ID of custom response. The ID can be obtained via the `DescribeCustomErrorPages` API. It's required when `Type=page`.
        :type CustomResponseId: str
        """
        self._PageId = None
        self._StatusCode = None
        self._Name = None
        self._Type = None
        self._CustomResponseId = None

    @property
    def PageId(self):
        return self._PageId

    @PageId.setter
    def PageId(self, PageId):
        self._PageId = PageId

    @property
    def StatusCode(self):
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CustomResponseId(self):
        return self._CustomResponseId

    @CustomResponseId.setter
    def CustomResponseId(self, CustomResponseId):
        self._CustomResponseId = CustomResponseId


    def _deserialize(self, params):
        self._PageId = params.get("PageId")
        self._StatusCode = params.get("StatusCode")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._CustomResponseId = params.get("CustomResponseId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EntityStatus(AbstractModel):
    """Status of domain names bound with this template.

    """

    def __init__(self):
        r"""
        :param _Entity: Instance name. Only subdomain names are supported.
        :type Entity: str
        :param _Status: Instance configuration status. Values:
<li>`online`: Configuration has taken effect;</li><li>`fail`: Configuration failed;</li><li>`process`: Configuration is being delivered. </li>
        :type Status: str
        :param _Message: Message returned after the operation completed. 
        :type Message: str
        """
        self._Entity = None
        self._Status = None
        self._Message = None

    @property
    def Entity(self):
        return self._Entity

    @Entity.setter
    def Entity(self, Entity):
        self._Entity = Entity

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Entity = params.get("Entity")
        self._Status = params.get("Status")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvInfo(AbstractModel):
    """Environment information.

    """

    def __init__(self):
        r"""
        :param _EnvId: Environment ID.
        :type EnvId: str
        :param _EnvType: Environment type. Valid values: 
<li>production: Production environment.</li><li> staging: Test environment. </li>
        :type EnvType: str
        :param _Status: Environment status. Valid values: 
<li>creating: Being created.</li>
<li>running: The environment is stable, with version changes allowed.</li>
<li>version_deploying: The version is currently being deployed, with no more changes allowed. </li>
        :type Status: str
        :param _Scope: Effective scope of the configuration in the current environment. Valid values: 
<li>ALL: It takes effect on the entire network when EnvType is set to production.</li>
<li>It returns the IP address of the test node for host binding during testing when EnvType is set to staging. </li>
        :type Scope: list of str
        :param _CurrentConfigGroupVersionInfos: For the effective versions of each configuration group in the current environment, there are two possible scenarios based on the value of Status: 
<li>When Status is set to version_deploying, the returned value of this field represents the previously effective version. In other words, during the deployment of the new version, the effective version is the one that was in effect before any changes were made.</li>
<li>When Status is set to running, the value returned by this field is the currently effective version. </li>
        :type CurrentConfigGroupVersionInfos: list of ConfigGroupVersionInfo
        :param _CreateTime: Creation time. The time format follows the ISO 8601 standard and is represented in Coordinated Universal Time (UTC).
        :type CreateTime: str
        :param _UpdateTime: Update time. The time format follows the ISO 8601 standard and is represented in Coordinated Universal Time (UTC).
        :type UpdateTime: str
        """
        self._EnvId = None
        self._EnvType = None
        self._Status = None
        self._Scope = None
        self._CurrentConfigGroupVersionInfos = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def EnvType(self):
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Scope(self):
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def CurrentConfigGroupVersionInfos(self):
        return self._CurrentConfigGroupVersionInfos

    @CurrentConfigGroupVersionInfos.setter
    def CurrentConfigGroupVersionInfos(self, CurrentConfigGroupVersionInfos):
        self._CurrentConfigGroupVersionInfos = CurrentConfigGroupVersionInfos

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
        self._EnvId = params.get("EnvId")
        self._EnvType = params.get("EnvType")
        self._Status = params.get("Status")
        self._Scope = params.get("Scope")
        if params.get("CurrentConfigGroupVersionInfos") is not None:
            self._CurrentConfigGroupVersionInfos = []
            for item in params.get("CurrentConfigGroupVersionInfos"):
                obj = ConfigGroupVersionInfo()
                obj._deserialize(item)
                self._CurrentConfigGroupVersionInfos.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrorPageReference(AbstractModel):
    """Custom error page's referenced source

    """

    def __init__(self):
        r"""
        :param _BusinessId: Referenced business ID, such as the custom block rule ID.
        :type BusinessId: str
        """
        self._BusinessId = None

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId


    def _deserialize(self, params):
        self._BusinessId = params.get("BusinessId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExceptConfig(AbstractModel):
    """Exception rules, which are used to bypass specific rules

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable configuration. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param _ExceptUserRules: The settings of the exception rule. If it is null, the settings that were last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExceptUserRules: list of ExceptUserRule
        """
        self._Switch = None
        self._ExceptUserRules = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def ExceptUserRules(self):
        return self._ExceptUserRules

    @ExceptUserRules.setter
    def ExceptUserRules(self, ExceptUserRules):
        self._ExceptUserRules = ExceptUserRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("ExceptUserRules") is not None:
            self._ExceptUserRules = []
            for item in params.get("ExceptUserRules"):
                obj = ExceptUserRule()
                obj._deserialize(item)
                self._ExceptUserRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExceptUserRule(AbstractModel):
    """The settings of the exception rule

    """

    def __init__(self):
        r"""
        :param _RuleName: The rule name.
        :type RuleName: str
        :param _Action: The rule action. It only supports the value `skip`, which indicates skipping all managed rules.
        :type Action: str
        :param _RuleStatus: The rule status. Values:
<li>`on`: Enabled</li>
<li>`off`: Disabled</li>
        :type RuleStatus: str
        :param _RuleID: The rule ID, which is automatically created and only used as an output parameter.
        :type RuleID: int
        :param _UpdateTime: The update time. If it is null, the current date and time is recorded.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UpdateTime: str
        :param _ExceptUserRuleConditions: The matching condition.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExceptUserRuleConditions: list of ExceptUserRuleCondition
        :param _ExceptUserRuleScope: The scope to which the exception rule applies.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExceptUserRuleScope: :class:`tencentcloud.teo.v20220901.models.ExceptUserRuleScope`
        :param _RulePriority: The rule priority. Value range: 0-100. If it is null, it defaults to 0.
        :type RulePriority: int
        """
        self._RuleName = None
        self._Action = None
        self._RuleStatus = None
        self._RuleID = None
        self._UpdateTime = None
        self._ExceptUserRuleConditions = None
        self._ExceptUserRuleScope = None
        self._RulePriority = None

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RuleStatus(self):
        return self._RuleStatus

    @RuleStatus.setter
    def RuleStatus(self, RuleStatus):
        self._RuleStatus = RuleStatus

    @property
    def RuleID(self):
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ExceptUserRuleConditions(self):
        return self._ExceptUserRuleConditions

    @ExceptUserRuleConditions.setter
    def ExceptUserRuleConditions(self, ExceptUserRuleConditions):
        self._ExceptUserRuleConditions = ExceptUserRuleConditions

    @property
    def ExceptUserRuleScope(self):
        return self._ExceptUserRuleScope

    @ExceptUserRuleScope.setter
    def ExceptUserRuleScope(self, ExceptUserRuleScope):
        self._ExceptUserRuleScope = ExceptUserRuleScope

    @property
    def RulePriority(self):
        return self._RulePriority

    @RulePriority.setter
    def RulePriority(self, RulePriority):
        self._RulePriority = RulePriority


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        self._Action = params.get("Action")
        self._RuleStatus = params.get("RuleStatus")
        self._RuleID = params.get("RuleID")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("ExceptUserRuleConditions") is not None:
            self._ExceptUserRuleConditions = []
            for item in params.get("ExceptUserRuleConditions"):
                obj = ExceptUserRuleCondition()
                obj._deserialize(item)
                self._ExceptUserRuleConditions.append(obj)
        if params.get("ExceptUserRuleScope") is not None:
            self._ExceptUserRuleScope = ExceptUserRuleScope()
            self._ExceptUserRuleScope._deserialize(params.get("ExceptUserRuleScope"))
        self._RulePriority = params.get("RulePriority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExceptUserRuleCondition(AbstractModel):
    """The condition of the exception rule

    """

    def __init__(self):
        r"""
        :param _MatchFrom: The field to match. Values:
<li>`host`: Request domain name</li>
<li>`sip`: Client IP</li>
<li>`ua`: User-Agent</li>
<li>`cookie`: Cookie</li>
<li>`cgi`: CGI script</li>
<li>`xff`: XFF header</li>
<li>`url`: Request URL</li>
<li>`accept`: Request content type</li>
<li>`method`: Request method</li>
<li>`header`: Request header</li>
<li>`sip_proto`: Network layer protocol</li>
        :type MatchFrom: str
        :param _MatchParam: The parameter of the field. Only when `MatchFrom = header`, the key contained in the header can be passed.
        :type MatchParam: str
        :param _Operator: The logical operator. Values:
<li>`equal`: String equals</li>
<li>`not_equal`: Value not equals</li>
<li>`include`: String contains</li>
<li>`not_include`: String not contains</li>
<li>`match`: IP matches</li>
<li>`not_match`: IP not matches</li>
<li>`include_area`: Regions contain</li>
<li>`is_empty`: Value left empty</li>
<li>`not_exists`: Key fields not exist</li>
<li>`regexp`: Regex matches</li>
<li>`len_gt`: Value greater than</li>
<li>`len_lt`: Value smaller than</li>
<li>`len_eq`: Value equals</li>
<li>`match_prefix`: Prefix matches</li>
<li>`match_suffix`: Suffix matches</li>
<li>`wildcard`: Wildcard</li>
        :type Operator: str
        :param _MatchContent: The value of the parameter.
        :type MatchContent: str
        """
        self._MatchFrom = None
        self._MatchParam = None
        self._Operator = None
        self._MatchContent = None

    @property
    def MatchFrom(self):
        return self._MatchFrom

    @MatchFrom.setter
    def MatchFrom(self, MatchFrom):
        self._MatchFrom = MatchFrom

    @property
    def MatchParam(self):
        return self._MatchParam

    @MatchParam.setter
    def MatchParam(self, MatchParam):
        self._MatchParam = MatchParam

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def MatchContent(self):
        return self._MatchContent

    @MatchContent.setter
    def MatchContent(self, MatchContent):
        self._MatchContent = MatchContent


    def _deserialize(self, params):
        self._MatchFrom = params.get("MatchFrom")
        self._MatchParam = params.get("MatchParam")
        self._Operator = params.get("Operator")
        self._MatchContent = params.get("MatchContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExceptUserRuleScope(AbstractModel):
    """The scope to which the exception rule applies

    """

    def __init__(self):
        r"""
        :param _Type: Exception mode. Values:
<li>`complete`: Skip the exception rule for full requests.</li>
<li>`partial`: Skip the exception rule for partial requests.</li>
        :type Type: str
        :param _Modules: The module to be activated. Values:
<li>`waf`: Tencent Cloud-managed rules</li>
<li>`rate`: Rate limiting rules</li>
<li>`acl`: Custom rule</li>
<li>`cc`: CC attack defense</li>
<li>`bot`: Bot protection</li>
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Modules: list of str
        :param _PartialModules: Module settings of the exception rule. If it is null, the settings that were last configured will be used.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PartialModules: list of PartialModule
        :param _SkipConditions: Condition settings of the exception rule. If it is null, the settings that were last configured will be used.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SkipConditions: list of SkipCondition
        """
        self._Type = None
        self._Modules = None
        self._PartialModules = None
        self._SkipConditions = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Modules(self):
        return self._Modules

    @Modules.setter
    def Modules(self, Modules):
        self._Modules = Modules

    @property
    def PartialModules(self):
        return self._PartialModules

    @PartialModules.setter
    def PartialModules(self, PartialModules):
        self._PartialModules = PartialModules

    @property
    def SkipConditions(self):
        return self._SkipConditions

    @SkipConditions.setter
    def SkipConditions(self, SkipConditions):
        self._SkipConditions = SkipConditions


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Modules = params.get("Modules")
        if params.get("PartialModules") is not None:
            self._PartialModules = []
            for item in params.get("PartialModules"):
                obj = PartialModule()
                obj._deserialize(item)
                self._PartialModules.append(obj)
        if params.get("SkipConditions") is not None:
            self._SkipConditions = []
            for item in params.get("SkipConditions"):
                obj = SkipCondition()
                obj._deserialize(item)
                self._SkipConditions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FailReason(AbstractModel):
    """Failure reason

    """

    def __init__(self):
        r"""
        :param _Reason: Failure reason.
        :type Reason: str
        :param _Targets: List of resources failed to be processed. 
        :type Targets: list of str
        """
        self._Reason = None
        self._Targets = None

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._Reason = params.get("Reason")
        self._Targets = params.get("Targets")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileAscriptionInfo(AbstractModel):
    """Verification file, used to verify site ownership

    """

    def __init__(self):
        r"""
        :param _IdentifyPath: Directory of the verification file.
        :type IdentifyPath: str
        :param _IdentifyContent: Content of the verification file.
        :type IdentifyContent: str
        """
        self._IdentifyPath = None
        self._IdentifyContent = None

    @property
    def IdentifyPath(self):
        return self._IdentifyPath

    @IdentifyPath.setter
    def IdentifyPath(self, IdentifyPath):
        self._IdentifyPath = IdentifyPath

    @property
    def IdentifyContent(self):
        return self._IdentifyContent

    @IdentifyContent.setter
    def IdentifyContent(self, IdentifyContent):
        self._IdentifyContent = IdentifyContent


    def _deserialize(self, params):
        self._IdentifyPath = params.get("IdentifyPath")
        self._IdentifyContent = params.get("IdentifyContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileVerification(AbstractModel):
    """Information required for verifying via a file. It's applicable to sites connected via CNAMEs.

    """

    def __init__(self):
        r"""
        :param _Path: EdgeOne obtains the file verification information in the format of "Scheme + Host + URL Path", (e.g. https://www.example.com/.well-known/teo-verification/z12h416twn.txt). This field is the URL path section of the URL you need to create.
        :type Path: str
        :param _Content: Content of the verification file. The contents of this field need to be filled into the text file returned by `Path`.
        :type Content: str
        """
        self._Path = None
        self._Content = None

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Path = params.get("Path")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Key-value pair filters for conditional filtering queries, such as filtering ID, name, and status.
    If more than one filter exists, the logical relationship between these filters is `AND`.
    If multiple values exist in one filter, the logical relationship between these values under the same filter is `OR`.

    """

    def __init__(self):
        r"""
        :param _Name: Fields to be filtered.
        :type Name: str
        :param _Values: Value of the filtered field.
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FirstPartConfig(AbstractModel):
    """The configuration to detect slow attacks based on the transfer period the first 8 KB of requests

    """

    def __init__(self):
        r"""
        :param _Switch: Switch. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Switch: str
        :param _StatTime: The transfer period threshold of the first 8 KB. If the threshold is reached, it’s considered a slow attack. Default: `5`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type StatTime: int
        """
        self._Switch = None
        self._StatTime = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def StatTime(self):
        return self._StatTime

    @StatTime.setter
    def StatTime(self, StatTime):
        self._StatTime = StatTime


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._StatTime = params.get("StatTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FollowOrigin(AbstractModel):
    """The origin cache configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable the configuration of following the origin server. Valid values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param _DefaultCacheTime: Sets the default cache time when the origin server does not return the Cache-Control header.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DefaultCacheTime: int
        :param _DefaultCache: Specifies whether to enable cache when the origin server does not return the Cache-Control header.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DefaultCache: str
        :param _DefaultCacheStrategy: Specifies whether to use the default caching policy when Cache-Control is not returned from the origin
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DefaultCacheStrategy: str
        """
        self._Switch = None
        self._DefaultCacheTime = None
        self._DefaultCache = None
        self._DefaultCacheStrategy = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def DefaultCacheTime(self):
        return self._DefaultCacheTime

    @DefaultCacheTime.setter
    def DefaultCacheTime(self, DefaultCacheTime):
        self._DefaultCacheTime = DefaultCacheTime

    @property
    def DefaultCache(self):
        return self._DefaultCache

    @DefaultCache.setter
    def DefaultCache(self, DefaultCache):
        self._DefaultCache = DefaultCache

    @property
    def DefaultCacheStrategy(self):
        return self._DefaultCacheStrategy

    @DefaultCacheStrategy.setter
    def DefaultCacheStrategy(self, DefaultCacheStrategy):
        self._DefaultCacheStrategy = DefaultCacheStrategy


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._DefaultCacheTime = params.get("DefaultCacheTime")
        self._DefaultCache = params.get("DefaultCache")
        self._DefaultCacheStrategy = params.get("DefaultCacheStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForceRedirect(AbstractModel):
    """Force HTTPS redirect configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable force HTTPS redirect. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param _RedirectStatusCode: Redirect status code. Values:
<li>`301`: 301 redirect</li>
<li>`302`: 302 redirect</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type RedirectStatusCode: int
        """
        self._Switch = None
        self._RedirectStatusCode = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def RedirectStatusCode(self):
        return self._RedirectStatusCode

    @RedirectStatusCode.setter
    def RedirectStatusCode(self, RedirectStatusCode):
        self._RedirectStatusCode = RedirectStatusCode


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._RedirectStatusCode = params.get("RedirectStatusCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Function(AbstractModel):
    """Details of an edge function.

    """

    def __init__(self):
        r"""
        :param _FunctionId: Function ID.
        :type FunctionId: str
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _Name: Function name.
        :type Name: str
        :param _Remark: Function description.
        :type Remark: str
        :param _Content: Function content.
        :type Content: str
        :param _Domain: Default domain name of a function.
        :type Domain: str
        :param _CreateTime: Creation time, which adopts Coordinated Universal Time (UTC) and follows the date and time format of the ISO 8601 standard.
        :type CreateTime: str
        :param _UpdateTime: Modification time, which adopts Coordinated Universal Time (UTC) and follows the date and time format of the ISO 8601 standard.
        :type UpdateTime: str
        """
        self._FunctionId = None
        self._ZoneId = None
        self._Name = None
        self._Remark = None
        self._Content = None
        self._Domain = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def FunctionId(self):
        return self._FunctionId

    @FunctionId.setter
    def FunctionId(self, FunctionId):
        self._FunctionId = FunctionId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

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
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

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
        self._FunctionId = params.get("FunctionId")
        self._ZoneId = params.get("ZoneId")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._Content = params.get("Content")
        self._Domain = params.get("Domain")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FunctionEnvironmentVariable(AbstractModel):
    """Environment variables of an edge function

    """

    def __init__(self):
        r"""
        :param _Key: Variable name, which should be unique and can only contain uppercase and lowercase letters, digits, and special characters including at signs (@), periods (.), hyphens (-), and underscores (_). Its maximum size is 64 bytes.
        :type Key: str
        :param _Value: Variable value. Its maximum size is 5000 bytes. The default value is empty.
        :type Value: str
        :param _Type: Variable type. Valid values:
<li>string: string type;</li>
<li>json: JSON object type.</li>Default value: string.
        :type Type: str
        """
        self._Key = None
        self._Value = None
        self._Type = None

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

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FunctionRule(AbstractModel):
    """Trigger rules for an edge function

    """

    def __init__(self):
        r"""
        :param _RuleId: Rule ID.
        :type RuleId: str
        :param _FunctionRuleConditions: Rule condition list. There is an OR relationship between items in the list.
        :type FunctionRuleConditions: list of FunctionRuleCondition
        :param _FunctionId: Function ID, specifying a function executed when a trigger rule condition is met.
        :type FunctionId: str
        :param _Remark: Rule description.
        :type Remark: str
        :param _FunctionName: Function name.
        :type FunctionName: str
        :param _Priority: Priority of a trigger rule for a function. The larger the value, the higher the priority.
        :type Priority: int
        :param _CreateTime: Creation time, which adopts Coordinated Universal Time (UTC) and follows the date and time format of the ISO 8601 standard.
        :type CreateTime: str
        :param _UpdateTime: Update time, which adopts Coordinated Universal Time (UTC) and follows the date and time format of the ISO 8601 standard.
        :type UpdateTime: str
        """
        self._RuleId = None
        self._FunctionRuleConditions = None
        self._FunctionId = None
        self._Remark = None
        self._FunctionName = None
        self._Priority = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def FunctionRuleConditions(self):
        return self._FunctionRuleConditions

    @FunctionRuleConditions.setter
    def FunctionRuleConditions(self, FunctionRuleConditions):
        self._FunctionRuleConditions = FunctionRuleConditions

    @property
    def FunctionId(self):
        return self._FunctionId

    @FunctionId.setter
    def FunctionId(self, FunctionId):
        self._FunctionId = FunctionId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def FunctionName(self):
        return self._FunctionName

    @FunctionName.setter
    def FunctionName(self, FunctionName):
        self._FunctionName = FunctionName

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

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        if params.get("FunctionRuleConditions") is not None:
            self._FunctionRuleConditions = []
            for item in params.get("FunctionRuleConditions"):
                obj = FunctionRuleCondition()
                obj._deserialize(item)
                self._FunctionRuleConditions.append(obj)
        self._FunctionId = params.get("FunctionId")
        self._Remark = params.get("Remark")
        self._FunctionName = params.get("FunctionName")
        self._Priority = params.get("Priority")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FunctionRuleCondition(AbstractModel):
    """Condition of a trigger rule for an edge function.

    """

    def __init__(self):
        r"""
        :param _RuleConditions: Condition of a trigger rule for an edge function. This condition is considered met if all items in the list are met.
        :type RuleConditions: list of RuleCondition
        """
        self._RuleConditions = None

    @property
    def RuleConditions(self):
        return self._RuleConditions

    @RuleConditions.setter
    def RuleConditions(self, RuleConditions):
        self._RuleConditions = RuleConditions


    def _deserialize(self, params):
        if params.get("RuleConditions") is not None:
            self._RuleConditions = []
            for item in params.get("RuleConditions"):
                obj = RuleCondition()
                obj._deserialize(item)
                self._RuleConditions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Grpc(AbstractModel):
    """Configuration of gRPC support

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable gRPC support. Valid values: 
<li>`on`: Enable;</li>
<li>`off`: Disable.</li>
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HandleFunctionRuntimeEnvironmentRequest(AbstractModel):
    """HandleFunctionRuntimeEnvironment request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _FunctionId: Function ID.
        :type FunctionId: str
        :param _Operation: Operation type. Valid values:
<li>setEnvironmentVariable: Set an environment variable. If the environment variable exists, it will be modified; otherwise, it will be added.</li>
<li>deleteEnvironmentVariable: Delete an environment variable.</li>
<li>clearEnvironmentVariable: Clear an environment variable.</li>
<li>resetEnvironmentVariable: Reset an environment variable.</li>
        :type Operation: str
        :param _EnvironmentVariables: Environment variable list. The runtime environment of a function supports up to 64 variables. This parameter is required when the value of Operation is setEnvironmentVariable, deleteEnvironmentVariable, or resetEnvironmentVariable.
        :type EnvironmentVariables: list of FunctionEnvironmentVariable
        """
        self._ZoneId = None
        self._FunctionId = None
        self._Operation = None
        self._EnvironmentVariables = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def FunctionId(self):
        return self._FunctionId

    @FunctionId.setter
    def FunctionId(self, FunctionId):
        self._FunctionId = FunctionId

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def EnvironmentVariables(self):
        return self._EnvironmentVariables

    @EnvironmentVariables.setter
    def EnvironmentVariables(self, EnvironmentVariables):
        self._EnvironmentVariables = EnvironmentVariables


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._FunctionId = params.get("FunctionId")
        self._Operation = params.get("Operation")
        if params.get("EnvironmentVariables") is not None:
            self._EnvironmentVariables = []
            for item in params.get("EnvironmentVariables"):
                obj = FunctionEnvironmentVariable()
                obj._deserialize(item)
                self._EnvironmentVariables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HandleFunctionRuntimeEnvironmentResponse(AbstractModel):
    """HandleFunctionRuntimeEnvironment response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class Header(AbstractModel):
    """HTTP header, used as input for the CreatePrefetchTask API

    """

    def __init__(self):
        r"""
        :param _Name: HTTP header name.
        :type Name: str
        :param _Value: HTTP header value
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Hsts(AbstractModel):
    """HSTS configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable the configuration. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param _MaxAge: MaxAge (in seconds). The maximum value is 1 day. 
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type MaxAge: int
        :param _IncludeSubDomains: Whether to contain subdomain names. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IncludeSubDomains: str
        :param _Preload: Whether to enable preloading. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Preload: str
        """
        self._Switch = None
        self._MaxAge = None
        self._IncludeSubDomains = None
        self._Preload = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def MaxAge(self):
        return self._MaxAge

    @MaxAge.setter
    def MaxAge(self, MaxAge):
        self._MaxAge = MaxAge

    @property
    def IncludeSubDomains(self):
        return self._IncludeSubDomains

    @IncludeSubDomains.setter
    def IncludeSubDomains(self, IncludeSubDomains):
        self._IncludeSubDomains = IncludeSubDomains

    @property
    def Preload(self):
        return self._Preload

    @Preload.setter
    def Preload(self, Preload):
        self._Preload = Preload


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._MaxAge = params.get("MaxAge")
        self._IncludeSubDomains = params.get("IncludeSubDomains")
        self._Preload = params.get("Preload")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Https(AbstractModel):
    """Domain name HTTPS acceleration configuration. This is disabled by default.

    """

    def __init__(self):
        r"""
        :param _Http2: Whether to enable HTTP2. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Http2: str
        :param _OcspStapling: Whether to enable OCSP. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type OcspStapling: str
        :param _TlsVersion: TLS version. Valid values: 
<li>`TLSv1`: TLSv1 version;</li>
<li>`TLSV1.1`: TLSv1.1 version;</li>
<li>`TLSV1.2`: TLSv1.2 version;</li>
<li>`TLSv1.3`: TLSv1.3 version.</li>Only consecutive versions can be enabled at the same time. 
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TlsVersion: list of str
        :param _Hsts: HSTS Configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type Hsts: :class:`tencentcloud.teo.v20220901.models.Hsts`
        :param _CertInfo: The certificate configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertInfo: list of ServerCertInfo
        :param _ApplyType: Whether the certificate is managed by EdgeOne. Values:
<li>`apply`: Managed by EdgeOne.</li>
<li>`none`: Not managed by EdgeOne.</li>If it is left empty, the default value `none` is used.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ApplyType: str
        :param _CipherSuite: The cipher suite, with values:
<li>loose-v2023: Provides high compatibility with general security, and supports TLS 1.0-1.3 cipher suites;</li>
<li>general-v2023: Provides relatively high compatibility with moderate security, and supports TLS 1.2-1.3 cipher suites;</li>
<li>strict-v2023: Provides high security, disables all cipher suites with security risks, and supports TLS 1.2-1.3 cipher suites.</li>
Note: This field may return null, which indicates a failure to obtain a valid value.
        :type CipherSuite: str
        """
        self._Http2 = None
        self._OcspStapling = None
        self._TlsVersion = None
        self._Hsts = None
        self._CertInfo = None
        self._ApplyType = None
        self._CipherSuite = None

    @property
    def Http2(self):
        return self._Http2

    @Http2.setter
    def Http2(self, Http2):
        self._Http2 = Http2

    @property
    def OcspStapling(self):
        return self._OcspStapling

    @OcspStapling.setter
    def OcspStapling(self, OcspStapling):
        self._OcspStapling = OcspStapling

    @property
    def TlsVersion(self):
        return self._TlsVersion

    @TlsVersion.setter
    def TlsVersion(self, TlsVersion):
        self._TlsVersion = TlsVersion

    @property
    def Hsts(self):
        return self._Hsts

    @Hsts.setter
    def Hsts(self, Hsts):
        self._Hsts = Hsts

    @property
    def CertInfo(self):
        return self._CertInfo

    @CertInfo.setter
    def CertInfo(self, CertInfo):
        self._CertInfo = CertInfo

    @property
    def ApplyType(self):
        return self._ApplyType

    @ApplyType.setter
    def ApplyType(self, ApplyType):
        self._ApplyType = ApplyType

    @property
    def CipherSuite(self):
        return self._CipherSuite

    @CipherSuite.setter
    def CipherSuite(self, CipherSuite):
        self._CipherSuite = CipherSuite


    def _deserialize(self, params):
        self._Http2 = params.get("Http2")
        self._OcspStapling = params.get("OcspStapling")
        self._TlsVersion = params.get("TlsVersion")
        if params.get("Hsts") is not None:
            self._Hsts = Hsts()
            self._Hsts._deserialize(params.get("Hsts"))
        if params.get("CertInfo") is not None:
            self._CertInfo = []
            for item in params.get("CertInfo"):
                obj = ServerCertInfo()
                obj._deserialize(item)
                self._CertInfo.append(obj)
        self._ApplyType = params.get("ApplyType")
        self._CipherSuite = params.get("CipherSuite")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPGroup(AbstractModel):
    """IP range group

    """

    def __init__(self):
        r"""
        :param _GroupId: Group ID. Enter `0`.
        :type GroupId: int
        :param _Name: Group name.
        :type Name: str
        :param _Content: IP group content. Only supports IP and IP mask.
        :type Content: list of str
        """
        self._GroupId = None
        self._Name = None
        self._Content = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._Name = params.get("Name")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPRegionInfo(AbstractModel):
    """IP location information query

    """

    def __init__(self):
        r"""
        :param _IP: IP address, IPV4 or IPV6.
        :type IP: str
        :param _IsEdgeOneIP: Whether the IP belongs to an EdgeOne node. Valid values:
<li>yes: This IP belongs to an EdgeOne node;</li>
<li>no: This IP does not belong to an EdgeOne node.</li>
        :type IsEdgeOneIP: str
        """
        self._IP = None
        self._IsEdgeOneIP = None

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def IsEdgeOneIP(self):
        return self._IsEdgeOneIP

    @IsEdgeOneIP.setter
    def IsEdgeOneIP(self, IsEdgeOneIP):
        self._IsEdgeOneIP = IsEdgeOneIP


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._IsEdgeOneIP = params.get("IsEdgeOneIP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPWhitelist(AbstractModel):
    """Intermediate IPs

    """

    def __init__(self):
        r"""
        :param _IPv4: List of IPv4 addresses
        :type IPv4: list of str
        :param _IPv6: List of IPv6 addresses
        :type IPv6: list of str
        """
        self._IPv4 = None
        self._IPv6 = None

    @property
    def IPv4(self):
        return self._IPv4

    @IPv4.setter
    def IPv4(self, IPv4):
        self._IPv4 = IPv4

    @property
    def IPv6(self):
        return self._IPv6

    @IPv6.setter
    def IPv6(self, IPv6):
        self._IPv6 = IPv6


    def _deserialize(self, params):
        self._IPv4 = params.get("IPv4")
        self._IPv6 = params.get("IPv6")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Identification(AbstractModel):
    """The site verification information

    """

    def __init__(self):
        r"""
        :param _ZoneName: The site name.
        :type ZoneName: str
        :param _Domain: The subdomain name to be verified. To verify the ownership of a site, leave it blank.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Domain: str
        :param _Status: The verification status. Values:
<li>`pending`: The verification is ongoing.</li>
<li>`finished`: The verification completed.</li>
        :type Status: str
        :param _Ascription: Details of the DNS record.
        :type Ascription: :class:`tencentcloud.teo.v20220901.models.AscriptionInfo`
        :param _OriginalNameServers: The NS record of the domain name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginalNameServers: list of str
        :param _FileAscription: Details of the verification file.
        :type FileAscription: :class:`tencentcloud.teo.v20220901.models.FileAscriptionInfo`
        """
        self._ZoneName = None
        self._Domain = None
        self._Status = None
        self._Ascription = None
        self._OriginalNameServers = None
        self._FileAscription = None

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Ascription(self):
        return self._Ascription

    @Ascription.setter
    def Ascription(self, Ascription):
        self._Ascription = Ascription

    @property
    def OriginalNameServers(self):
        return self._OriginalNameServers

    @OriginalNameServers.setter
    def OriginalNameServers(self, OriginalNameServers):
        self._OriginalNameServers = OriginalNameServers

    @property
    def FileAscription(self):
        return self._FileAscription

    @FileAscription.setter
    def FileAscription(self, FileAscription):
        self._FileAscription = FileAscription


    def _deserialize(self, params):
        self._ZoneName = params.get("ZoneName")
        self._Domain = params.get("Domain")
        self._Status = params.get("Status")
        if params.get("Ascription") is not None:
            self._Ascription = AscriptionInfo()
            self._Ascription._deserialize(params.get("Ascription"))
        self._OriginalNameServers = params.get("OriginalNameServers")
        if params.get("FileAscription") is not None:
            self._FileAscription = FileAscriptionInfo()
            self._FileAscription._deserialize(params.get("FileAscription"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdentifyZoneRequest(AbstractModel):
    """IdentifyZone request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneName: The site name.
        :type ZoneName: str
        :param _Domain: A subdomain name under the site. Specify this field if you want to verify the ownership of a subdomain name. Otherwise you can leave it blank.

        :type Domain: str
        """
        self._ZoneName = None
        self._Domain = None

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._ZoneName = params.get("ZoneName")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdentifyZoneResponse(AbstractModel):
    """IdentifyZone response structure.

    """

    def __init__(self):
        r"""
        :param _Ascription: Details of the DNS record.
        :type Ascription: :class:`tencentcloud.teo.v20220901.models.AscriptionInfo`
        :param _FileAscription: Details of the verification file.
        :type FileAscription: :class:`tencentcloud.teo.v20220901.models.FileAscriptionInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Ascription = None
        self._FileAscription = None
        self._RequestId = None

    @property
    def Ascription(self):
        return self._Ascription

    @Ascription.setter
    def Ascription(self, Ascription):
        self._Ascription = Ascription

    @property
    def FileAscription(self):
        return self._FileAscription

    @FileAscription.setter
    def FileAscription(self, FileAscription):
        self._FileAscription = FileAscription

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Ascription") is not None:
            self._Ascription = AscriptionInfo()
            self._Ascription._deserialize(params.get("Ascription"))
        if params.get("FileAscription") is not None:
            self._FileAscription = FileAscriptionInfo()
            self._FileAscription._deserialize(params.get("FileAscription"))
        self._RequestId = params.get("RequestId")


class ImageOptimize(AbstractModel):
    """Image optimization configuration.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable configuration. Values: 
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IncreasePlanQuotaRequest(AbstractModel):
    """IncreasePlanQuota request structure.

    """

    def __init__(self):
        r"""
        :param _PlanId: Plan ID, formatted as edgeone-2unuvzjmmn2q.
        :type PlanId: str
        :param _QuotaType: The types of new plan quotas available include:<li> site: Number of sites;</li><li> precise_access_control_rule: the number of rules under "Web Protection - Custom Rules - Precision Matching Policy";</li><li> rate_limiting_rule: the number of rules under "Web Protection - Rate Limiting - Precision Rate Limiting Module". </li>
        :type QuotaType: str
        :param _QuotaNumber: Number of new quotas. The maximum number of quotas that can be added at one time is 100.
        :type QuotaNumber: int
        """
        self._PlanId = None
        self._QuotaType = None
        self._QuotaNumber = None

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def QuotaType(self):
        return self._QuotaType

    @QuotaType.setter
    def QuotaType(self, QuotaType):
        self._QuotaType = QuotaType

    @property
    def QuotaNumber(self):
        return self._QuotaNumber

    @QuotaNumber.setter
    def QuotaNumber(self, QuotaNumber):
        self._QuotaNumber = QuotaNumber


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._QuotaType = params.get("QuotaType")
        self._QuotaNumber = params.get("QuotaNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IncreasePlanQuotaResponse(AbstractModel):
    """IncreasePlanQuota response structure.

    """

    def __init__(self):
        r"""
        :param _DealName: Order number.
        :type DealName: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealName = None
        self._RequestId = None

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class IntelligenceRule(AbstractModel):
    """Bot intelligence rules

    """

    def __init__(self):
        r"""
        :param _Switch: Switch. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param _IntelligenceRuleItems: Items in a bot intelligence rule
Note: This field may return null, indicating that no valid values can be obtained.
        :type IntelligenceRuleItems: list of IntelligenceRuleItem
        """
        self._Switch = None
        self._IntelligenceRuleItems = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def IntelligenceRuleItems(self):
        return self._IntelligenceRuleItems

    @IntelligenceRuleItems.setter
    def IntelligenceRuleItems(self, IntelligenceRuleItems):
        self._IntelligenceRuleItems = IntelligenceRuleItems


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("IntelligenceRuleItems") is not None:
            self._IntelligenceRuleItems = []
            for item in params.get("IntelligenceRuleItems"):
                obj = IntelligenceRuleItem()
                obj._deserialize(item)
                self._IntelligenceRuleItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntelligenceRuleItem(AbstractModel):
    """Bot intelligence rule items

    """

    def __init__(self):
        r"""
        :param _Label: The tag to categorize bots. Values:
<li>`evil_bot`: Malicious bot</li>
<li>`suspect_bot`: Suspected bot</li>
<li>`good_bot`: Good bot</li>
<li>`normal`: Normal request</li>
        :type Label: str
        :param _Action: The action taken on bots. Values
<li>`drop`: Block</li>
<li>`trans`: Allow</li>
<li>`alg`: JavaScript challenge</li>
<li>`captcha`: Managed challenge</li>
<li>`monitor`: Observe</li>
        :type Action: str
        """
        self._Label = None
        self._Action = None

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Action = params.get("Action")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpTableConfig(AbstractModel):
    """IP/Region blocklist/allowlist configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Switch. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param _IpTableRules: The settings of the basic access control rule. If it is null, the settings that were last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IpTableRules: list of IpTableRule
        """
        self._Switch = None
        self._IpTableRules = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def IpTableRules(self):
        return self._IpTableRules

    @IpTableRules.setter
    def IpTableRules(self, IpTableRules):
        self._IpTableRules = IpTableRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("IpTableRules") is not None:
            self._IpTableRules = []
            for item in params.get("IpTableRules"):
                obj = IpTableRule()
                obj._deserialize(item)
                self._IpTableRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpTableRule(AbstractModel):
    """IP blocklist/allowlist rule details

    """

    def __init__(self):
        r"""
        :param _Action: The action. Values:
<li>`drop`: Block</li>
<li>`trans`: Allow</li>
<li>`monitor`: Observe</li>
        :type Action: str
        :param _MatchFrom: The matching dimension. Values:
<li>`ip`: Match by IP.</li>
<li>`area`: Match by IP region.</li>
        :type MatchFrom: str
        :param _Operator: Matching method. It defaults to `equal` if it’s left empty.
Values: 
<li>`is_empty`: The field is empty.</li>
<li>`not_exists`: The configuration item does not exist.</li>
<li>`include`: Include</li>
<li>`not_include`: Do not include</li>
<li>`equal`: Equal to</li>
<li>`not_equal`: Not equal to</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Operator: str
        :param _RuleID: The rule ID, which is only used as an output parameter.
        :type RuleID: int
        :param _UpdateTime: The update time, which is only used as an output parameter.
        :type UpdateTime: str
        :param _Status: The rule status. A null value indicates that the rule is enabled. Values:
<li>`on`: Enabled</li>
<li>`off`: Disabled</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _RuleName: The rule name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleName: str
        :param _MatchContent: Matching content. It’s not required when `Operator` is `is_emty` or `not_exists`. 
        :type MatchContent: str
        """
        self._Action = None
        self._MatchFrom = None
        self._Operator = None
        self._RuleID = None
        self._UpdateTime = None
        self._Status = None
        self._RuleName = None
        self._MatchContent = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def MatchFrom(self):
        return self._MatchFrom

    @MatchFrom.setter
    def MatchFrom(self, MatchFrom):
        self._MatchFrom = MatchFrom

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def RuleID(self):
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def MatchContent(self):
        return self._MatchContent

    @MatchContent.setter
    def MatchContent(self, MatchContent):
        self._MatchContent = MatchContent


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._MatchFrom = params.get("MatchFrom")
        self._Operator = params.get("Operator")
        self._RuleID = params.get("RuleID")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._RuleName = params.get("RuleName")
        self._MatchContent = params.get("MatchContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Ipv6(AbstractModel):
    """The IPv6 access configuration.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable IPv6 access. Valid values: 
<li>`on`: Enable;</li>
<li>`off`: Disable.</li>
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4OfflineLog(AbstractModel):
    """The L7 log details

    """

    def __init__(self):
        r"""
        :param _ProxyId: L4 proxy instance ID.
        :type ProxyId: str
        :param _Area: Log query area. Valid values:
<li>`mainland`: Chinese mainland;</li>
<li>`overseas`: Global (outside the Chinese mainland). </li>
        :type Area: str
        :param _LogPacketName: Log packet name.
        :type LogPacketName: str
        :param _Url: Log download address.
        :type Url: str
        :param _LogTime: (Disused) Log packaging time. 
        :type LogTime: int
        :param _LogStartTime: Start time of log packaging.
        :type LogStartTime: str
        :param _LogEndTime: End time of the log package.
        :type LogEndTime: str
        :param _Size: Log size (in bytes).
        :type Size: int
        """
        self._ProxyId = None
        self._Area = None
        self._LogPacketName = None
        self._Url = None
        self._LogTime = None
        self._LogStartTime = None
        self._LogEndTime = None
        self._Size = None

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def LogPacketName(self):
        return self._LogPacketName

    @LogPacketName.setter
    def LogPacketName(self, LogPacketName):
        self._LogPacketName = LogPacketName

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def LogTime(self):
        return self._LogTime

    @LogTime.setter
    def LogTime(self, LogTime):
        self._LogTime = LogTime

    @property
    def LogStartTime(self):
        return self._LogStartTime

    @LogStartTime.setter
    def LogStartTime(self, LogStartTime):
        self._LogStartTime = LogStartTime

    @property
    def LogEndTime(self):
        return self._LogEndTime

    @LogEndTime.setter
    def LogEndTime(self, LogEndTime):
        self._LogEndTime = LogEndTime

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._Area = params.get("Area")
        self._LogPacketName = params.get("LogPacketName")
        self._Url = params.get("Url")
        self._LogTime = params.get("LogTime")
        self._LogStartTime = params.get("LogStartTime")
        self._LogEndTime = params.get("LogEndTime")
        self._Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4Proxy(AbstractModel):
    """Layer 4 proxy instance.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _ProxyId: Layer 4 proxy instance ID.
        :type ProxyId: str
        :param _ProxyName: Layer 4 proxy instance name.
        :type ProxyName: str
        :param _Area: Acceleration zone of the Layer 4 proxy instance.<li>mainland: Availability zone in the Chinese mainland;</li><li>overseas: Global availability zone (excluding the Chinese mainland);</li><li>global: Global availability zone.</li>	
        :type Area: str
        :param _Cname: Access via CNAME.
        :type Cname: str
        :param _Ips: After the fixed IP address is enabled, this value will return the corresponding access IP address; if it is not enabled, this value will be empty.
        :type Ips: list of str
        :param _Status: Status of the Layer 4 proxy instance.<li>online: Enabled;</li>
<li>offline: Disabled;</li>
<li>progress: Deploying;</li>	
<li>stopping: Disabling;</li>
<li>banned: Blocked;</li>
<li>fail: Failed to deploy or disable.</li>	
        :type Status: str
        :param _Ipv6: Specifies whether to enable IPv6 access.<li>on: Enable;</li> <li>off: Disable.</li>
        :type Ipv6: str
        :param _StaticIp: Specifies whether to enable the fixed IP address.<li>on: Enable;</li> <li>off: Disable.</li>
        :type StaticIp: str
        :param _AccelerateMainland: Specifies whether to enable network optimization in the Chinese mainland.<li>on: Enable</li> <li>off: Disable</li>
        :type AccelerateMainland: str
        :param _DDosProtectionConfig: Security protection configuration.
Note: This field may return null, indicating that no valid value can be obtained.
        :type DDosProtectionConfig: :class:`tencentcloud.teo.v20220901.models.DDosProtectionConfig`
        :param _L4ProxyRuleCount: Number of forwarding rules under the Layer 4 proxy instance.
        :type L4ProxyRuleCount: int
        :param _UpdateTime: Latest modification time.
        :type UpdateTime: str
        """
        self._ZoneId = None
        self._ProxyId = None
        self._ProxyName = None
        self._Area = None
        self._Cname = None
        self._Ips = None
        self._Status = None
        self._Ipv6 = None
        self._StaticIp = None
        self._AccelerateMainland = None
        self._DDosProtectionConfig = None
        self._L4ProxyRuleCount = None
        self._UpdateTime = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def ProxyName(self):
        return self._ProxyName

    @ProxyName.setter
    def ProxyName(self, ProxyName):
        self._ProxyName = ProxyName

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Cname(self):
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def Ips(self):
        return self._Ips

    @Ips.setter
    def Ips(self, Ips):
        self._Ips = Ips

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Ipv6(self):
        return self._Ipv6

    @Ipv6.setter
    def Ipv6(self, Ipv6):
        self._Ipv6 = Ipv6

    @property
    def StaticIp(self):
        return self._StaticIp

    @StaticIp.setter
    def StaticIp(self, StaticIp):
        self._StaticIp = StaticIp

    @property
    def AccelerateMainland(self):
        return self._AccelerateMainland

    @AccelerateMainland.setter
    def AccelerateMainland(self, AccelerateMainland):
        self._AccelerateMainland = AccelerateMainland

    @property
    def DDosProtectionConfig(self):
        return self._DDosProtectionConfig

    @DDosProtectionConfig.setter
    def DDosProtectionConfig(self, DDosProtectionConfig):
        self._DDosProtectionConfig = DDosProtectionConfig

    @property
    def L4ProxyRuleCount(self):
        return self._L4ProxyRuleCount

    @L4ProxyRuleCount.setter
    def L4ProxyRuleCount(self, L4ProxyRuleCount):
        self._L4ProxyRuleCount = L4ProxyRuleCount

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        self._ProxyName = params.get("ProxyName")
        self._Area = params.get("Area")
        self._Cname = params.get("Cname")
        self._Ips = params.get("Ips")
        self._Status = params.get("Status")
        self._Ipv6 = params.get("Ipv6")
        self._StaticIp = params.get("StaticIp")
        self._AccelerateMainland = params.get("AccelerateMainland")
        if params.get("DDosProtectionConfig") is not None:
            self._DDosProtectionConfig = DDosProtectionConfig()
            self._DDosProtectionConfig._deserialize(params.get("DDosProtectionConfig"))
        self._L4ProxyRuleCount = params.get("L4ProxyRuleCount")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4ProxyRemoteAuth(AbstractModel):
    """L4 remote authentication information.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable L4 remote authentication. Valid values:
<li>on: Enable;</li>
<li>off: Disable.</li>
        :type Switch: str
        :param _Address: Remote authentication service address, in the format of domain/ip:port, such as example.auth.com:8888.

        :type Address: str
        :param _ServerFaultyBehavior: Default origin-pull behavior based on L4 forwarding rules after the remote authentication service is disabled. Valid values:
<li>reject: Block and deny access;</li>
<li>allow: Allow access.</li>
        :type ServerFaultyBehavior: str
        """
        self._Switch = None
        self._Address = None
        self._ServerFaultyBehavior = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def ServerFaultyBehavior(self):
        return self._ServerFaultyBehavior

    @ServerFaultyBehavior.setter
    def ServerFaultyBehavior(self, ServerFaultyBehavior):
        self._ServerFaultyBehavior = ServerFaultyBehavior


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Address = params.get("Address")
        self._ServerFaultyBehavior = params.get("ServerFaultyBehavior")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4ProxyRule(AbstractModel):
    """Details of Layer 4 proxy forwarding rules.

    """

    def __init__(self):
        r"""
        :param _RuleId: Forwarding rule ID.
Note: Do not fill in this parameter when L4ProxyRule is used as an input parameter in CreateL4ProxyRules; it must be filled in when L4ProxyRule is used as an input parameter in ModifyL4ProxyRules.
        :type RuleId: str
        :param _Protocol: Forwarding protocol. Valid values:
<li>TCP: TCP protocol;</li>
<li>UDP: UDP protocol.</li>
Note: This parameter must be filled in when L4ProxyRule is used as an input parameter in CreateL4ProxyRules; it is optional when L4ProxyRule is used as an input parameter in ModifyL4ProxyRules. If not specified, it will retain its existing value.
        :type Protocol: str
        :param _PortRange: Forwarding port, which can be set as follows:
<li>A single port, such as 80;</li>
<li>A range of ports, such as 81-85, representing ports 81, 82, 83, 84, 85.</li>
Note: This parameter must be filled in when L4ProxyRule is used as an input parameter in CreateL4ProxyRules; it is optional when L4ProxyRule is used as an input parameter in ModifyL4ProxyRules. If not specified, it will retain its existing value.
        :type PortRange: list of str
        :param _OriginType: Origin server type. Valid values:
<li>IP_DOMAIN: IP/Domain name origin server;</li>
<li>ORIGIN_GROUP: Origin server group;</li>
<li>LB: Cloud Load Balancer, currently only open to the allowlist.</li>
Note: This parameter must be filled in when L4ProxyRule is used as an input parameter in CreateL4ProxyRules; it is optional when L4ProxyRule is used as an input parameter in ModifyL4ProxyRules. If not specified, it will retain its existing value.
        :type OriginType: str
        :param _OriginValue: Origin server address.
<li>When OriginType is set to IP_DOMAIN, enter the IP address or domain name, such as 8.8.8.8 or test.com;</li>
<li>When OriginType is set to ORIGIN_GROUP, enter the origin server group ID, such as og-537y24vf5b41;</li>
<li>When OriginType is set to LB, enter the Cloud Load Balancer instance ID, such as lb-2qwk30xf7s9g.</li>
Note: This parameter must be filled in when L4ProxyRule is used as an input parameter in CreateL4ProxyRules; it is optional when L4ProxyRule is used as an input parameter in ModifyL4ProxyRules. If not specified, it will retain its existing value.
        :type OriginValue: list of str
        :param _OriginPortRange: Origin server port, which can be set as follows:<li>A single port, such as 80;</li>
<li>A range of ports, such as 81-85, representing ports 81, 82, 83, 84, 85. When inputting a range of ports, ensure that the length corresponds with that of the forwarding port range. For example, if the forwarding port range is 80-90, this port range should be 90-100.</li>
Note: This parameter must be filled in when L4ProxyRule is used as an input parameter in CreateL4ProxyRules; it is optional when L4ProxyRule is used as an input parameter in ModifyL4ProxyRules. If not specified, it will retain its existing value.
        :type OriginPortRange: str
        :param _ClientIPPassThroughMode: Transmission of the client IP address. Valid values:<li>TOA: Available only when Protocol=TCP;</li> 
<li>PPV1: Transmission via Proxy Protocol V1. Available only when Protocol=TCP;</li>
<li>PPV2: Transmission via Proxy Protocol V2;</li> 
<li>SPP: Transmission via Simple Proxy Protocol. Available only when Protocol=UDP;</li> 
<li>OFF: No transmission.</li>
Note: This parameter is optional when L4ProxyRule is used as an input parameter in CreateL4ProxyRules, and if not specified, the default value OFF will be used; it is optional when L4ProxyRule is used as an input parameter in ModifyL4ProxyRules. If not specified, it will retain its existing value.
        :type ClientIPPassThroughMode: str
        :param _SessionPersist: Specifies whether to enable session persistence. Valid values:
<li>on: Enable;</li>
<li>off: Disable.</li>
Note: This parameter is optional when L4ProxyRule is used as an input parameter in CreateL4ProxyRules, and if not specified, the default value off will be used; it is optional when L4ProxyRule is used as an input parameter in ModifyL4ProxyRules. If not specified, it will retain its existing value.
        :type SessionPersist: str
        :param _SessionPersistTime: Session persistence period, with a range of 30-3600, measured in seconds.
Note: This parameter is optional when L4ProxyRule is used as an input parameter in CreateL4ProxyRules. It is valid only when SessionPersist is set to on and defaults to 3600 if not specified. It is optional when L4ProxyRule is used as an input parameter in ModifyL4ProxyRules. If not specified, it will retain its existing value.
        :type SessionPersistTime: int
        :param _RuleTag: Rule tag. Accepts 1-50 arbitrary characters.
Note: This parameter is optional when L4ProxyRule is used as an input parameter in CreateL4ProxyRules; it is optional when L4ProxyRule is used as an input parameter in ModifyL4ProxyRules. If not specified, it will retain its existing value.
        :type RuleTag: str
        :param _Status: Rule status. Valid values:<li>online: Enabled;</li>
<li>offline: Disabled;</li>
<li>progress: Deploying;</li>
<li>stopping: Disabling;</li>
<li>fail: Failed to deploy or disable.</li>
Note: Do not set this parameter when L4ProxyRule is used as an input parameter in CreateL4ProxyRules and ModifyL4ProxyRules.
        :type Status: str
        :param _BuId: BuID.
        :type BuId: str
        :param _RemoteAuth: Remote authentication information.
Note: RemoteAuth cannot be used as an input parameter in CreateL4ProxyRules or ModifyL4ProxyRules. If this parameter is input, it will be ignored. If the returned data of DescribeL4ProxyRules is empty, it indicates that remote authentication is disabled.
Note: This field may return null, which indicates a failure to obtain a valid value.
        :type RemoteAuth: :class:`tencentcloud.teo.v20220901.models.L4ProxyRemoteAuth`
        """
        self._RuleId = None
        self._Protocol = None
        self._PortRange = None
        self._OriginType = None
        self._OriginValue = None
        self._OriginPortRange = None
        self._ClientIPPassThroughMode = None
        self._SessionPersist = None
        self._SessionPersistTime = None
        self._RuleTag = None
        self._Status = None
        self._BuId = None
        self._RemoteAuth = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def PortRange(self):
        return self._PortRange

    @PortRange.setter
    def PortRange(self, PortRange):
        self._PortRange = PortRange

    @property
    def OriginType(self):
        return self._OriginType

    @OriginType.setter
    def OriginType(self, OriginType):
        self._OriginType = OriginType

    @property
    def OriginValue(self):
        return self._OriginValue

    @OriginValue.setter
    def OriginValue(self, OriginValue):
        self._OriginValue = OriginValue

    @property
    def OriginPortRange(self):
        return self._OriginPortRange

    @OriginPortRange.setter
    def OriginPortRange(self, OriginPortRange):
        self._OriginPortRange = OriginPortRange

    @property
    def ClientIPPassThroughMode(self):
        return self._ClientIPPassThroughMode

    @ClientIPPassThroughMode.setter
    def ClientIPPassThroughMode(self, ClientIPPassThroughMode):
        self._ClientIPPassThroughMode = ClientIPPassThroughMode

    @property
    def SessionPersist(self):
        return self._SessionPersist

    @SessionPersist.setter
    def SessionPersist(self, SessionPersist):
        self._SessionPersist = SessionPersist

    @property
    def SessionPersistTime(self):
        return self._SessionPersistTime

    @SessionPersistTime.setter
    def SessionPersistTime(self, SessionPersistTime):
        self._SessionPersistTime = SessionPersistTime

    @property
    def RuleTag(self):
        return self._RuleTag

    @RuleTag.setter
    def RuleTag(self, RuleTag):
        self._RuleTag = RuleTag

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BuId(self):
        return self._BuId

    @BuId.setter
    def BuId(self, BuId):
        self._BuId = BuId

    @property
    def RemoteAuth(self):
        return self._RemoteAuth

    @RemoteAuth.setter
    def RemoteAuth(self, RemoteAuth):
        self._RemoteAuth = RemoteAuth


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._Protocol = params.get("Protocol")
        self._PortRange = params.get("PortRange")
        self._OriginType = params.get("OriginType")
        self._OriginValue = params.get("OriginValue")
        self._OriginPortRange = params.get("OriginPortRange")
        self._ClientIPPassThroughMode = params.get("ClientIPPassThroughMode")
        self._SessionPersist = params.get("SessionPersist")
        self._SessionPersistTime = params.get("SessionPersistTime")
        self._RuleTag = params.get("RuleTag")
        self._Status = params.get("Status")
        self._BuId = params.get("BuId")
        if params.get("RemoteAuth") is not None:
            self._RemoteAuth = L4ProxyRemoteAuth()
            self._RemoteAuth._deserialize(params.get("RemoteAuth"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7OfflineLog(AbstractModel):
    """Details of L7 logs.

    """

    def __init__(self):
        r"""
        :param _Domain: Log domain name.
        :type Domain: str
        :param _Area: Log query area. Valid values:
<li>`mainland`: Chinese mainland;</li>
<li>`overseas`: Global (outside the Chinese mainland). </li>
        :type Area: str
        :param _LogPacketName: Log packet name.	
        :type LogPacketName: str
        :param _Url: Log download address.	
        :type Url: str
        :param _LogTime: (Disused) Log packaging time. 
        :type LogTime: int
        :param _LogStartTime: Start time of log packaging.
        :type LogStartTime: str
        :param _LogEndTime: End time of the log package.
        :type LogEndTime: str
        :param _Size: Original log size (in bytes).
        :type Size: int
        """
        self._Domain = None
        self._Area = None
        self._LogPacketName = None
        self._Url = None
        self._LogTime = None
        self._LogStartTime = None
        self._LogEndTime = None
        self._Size = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def LogPacketName(self):
        return self._LogPacketName

    @LogPacketName.setter
    def LogPacketName(self, LogPacketName):
        self._LogPacketName = LogPacketName

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def LogTime(self):
        return self._LogTime

    @LogTime.setter
    def LogTime(self, LogTime):
        self._LogTime = LogTime

    @property
    def LogStartTime(self):
        return self._LogStartTime

    @LogStartTime.setter
    def LogStartTime(self, LogStartTime):
        self._LogStartTime = LogStartTime

    @property
    def LogEndTime(self):
        return self._LogEndTime

    @LogEndTime.setter
    def LogEndTime(self, LogEndTime):
        self._LogEndTime = LogEndTime

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Area = params.get("Area")
        self._LogPacketName = params.get("LogPacketName")
        self._Url = params.get("Url")
        self._LogTime = params.get("LogTime")
        self._LogStartTime = params.get("LogStartTime")
        self._LogEndTime = params.get("LogEndTime")
        self._Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogFormat(AbstractModel):
    """Output format for real-time log delivery. You can directly use the specified predefined log output format (JSON Lines / csv) through the FormatType parameter, or define a variant output format through additional parameters based on the predefined log output format.

    """

    def __init__(self):
        r"""
        :param _FormatType: Predefined output format for log shipping. Valid values:
<li>json: Use JSON Lines as the predefined log output format. In each log entry, fields are displayed as key-value pairs.</li>
<li>csv: Use the predefined log output format csv, where each log entry only is presented as field values only, excluding field names. </li>
        :type FormatType: str
        :param _BatchPrefix: A string added before each log delivery batch. Each log delivery batch may contain multiple log records.
        :type BatchPrefix: str
        :param _BatchSuffix: A string appended after each log delivery batch.
        :type BatchSuffix: str
        :param _RecordPrefix: A string added before each log record.
        :type RecordPrefix: str
        :param _RecordSuffix: A string appended after each log record.
        :type RecordSuffix: str
        :param _RecordDelimiter: A string inserted between log records as a separator. Valid values:
<li>\n: line break;</li>
<li>\t: tab character;</li>
<li>,: Half-width comma. </li>
        :type RecordDelimiter: str
        :param _FieldDelimiter: A string inserted between fields as a separator within a single log record. Valid values:
<li>\t: tab character;</li>
<li>,: half-width comma;</li>
<li>;: Half-width semicolon. </li>
        :type FieldDelimiter: str
        """
        self._FormatType = None
        self._BatchPrefix = None
        self._BatchSuffix = None
        self._RecordPrefix = None
        self._RecordSuffix = None
        self._RecordDelimiter = None
        self._FieldDelimiter = None

    @property
    def FormatType(self):
        return self._FormatType

    @FormatType.setter
    def FormatType(self, FormatType):
        self._FormatType = FormatType

    @property
    def BatchPrefix(self):
        return self._BatchPrefix

    @BatchPrefix.setter
    def BatchPrefix(self, BatchPrefix):
        self._BatchPrefix = BatchPrefix

    @property
    def BatchSuffix(self):
        return self._BatchSuffix

    @BatchSuffix.setter
    def BatchSuffix(self, BatchSuffix):
        self._BatchSuffix = BatchSuffix

    @property
    def RecordPrefix(self):
        return self._RecordPrefix

    @RecordPrefix.setter
    def RecordPrefix(self, RecordPrefix):
        self._RecordPrefix = RecordPrefix

    @property
    def RecordSuffix(self):
        return self._RecordSuffix

    @RecordSuffix.setter
    def RecordSuffix(self, RecordSuffix):
        self._RecordSuffix = RecordSuffix

    @property
    def RecordDelimiter(self):
        return self._RecordDelimiter

    @RecordDelimiter.setter
    def RecordDelimiter(self, RecordDelimiter):
        self._RecordDelimiter = RecordDelimiter

    @property
    def FieldDelimiter(self):
        return self._FieldDelimiter

    @FieldDelimiter.setter
    def FieldDelimiter(self, FieldDelimiter):
        self._FieldDelimiter = FieldDelimiter


    def _deserialize(self, params):
        self._FormatType = params.get("FormatType")
        self._BatchPrefix = params.get("BatchPrefix")
        self._BatchSuffix = params.get("BatchSuffix")
        self._RecordPrefix = params.get("RecordPrefix")
        self._RecordSuffix = params.get("RecordSuffix")
        self._RecordDelimiter = params.get("RecordDelimiter")
        self._FieldDelimiter = params.get("FieldDelimiter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaxAge(AbstractModel):
    """Browser cache rule configuration, which is used to set the default value of `MaxAge` and is disabled by default.

    """

    def __init__(self):
        r"""
        :param _FollowOrigin: Whether to follow the origin server. Values:
<li>`on`: Follow the origin server and ignore the field MaxAgeTime;</li>
<li>`off`: Do not follow the origin server and apply the field MaxAgeTime.</li>
        :type FollowOrigin: str
        :param _MaxAgeTime: Specifies the maximum amount of time (in seconds). The maximum value is 365 days.
Note: The value `0` means not to cache.
        :type MaxAgeTime: int
        """
        self._FollowOrigin = None
        self._MaxAgeTime = None

    @property
    def FollowOrigin(self):
        return self._FollowOrigin

    @FollowOrigin.setter
    def FollowOrigin(self, FollowOrigin):
        self._FollowOrigin = FollowOrigin

    @property
    def MaxAgeTime(self):
        return self._MaxAgeTime

    @MaxAgeTime.setter
    def MaxAgeTime(self, MaxAgeTime):
        self._MaxAgeTime = MaxAgeTime


    def _deserialize(self, params):
        self._FollowOrigin = params.get("FollowOrigin")
        self._MaxAgeTime = params.get("MaxAgeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccelerationDomainRequest(AbstractModel):
    """ModifyAccelerationDomain request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site related with the accelerated domain name.
        :type ZoneId: str
        :param _DomainName: Accelerated domain name
        :type DomainName: str
        :param _OriginInfo: Details of the origin.
        :type OriginInfo: :class:`tencentcloud.teo.v20220901.models.OriginInfo`
        :param _OriginProtocol: Origin-pull protocol configuration. Values:
<li>`FOLLOW`: Follow the protocol of origin</li>
<li>`HTTP`: Send requests to the origin over HTTP</li>
<li>`HTTPS`: Send requests to the origin over HTTPS</li>
<li>The original configuration applies if this field is not specified.</li>
        :type OriginProtocol: str
        :param _HttpOriginPort: Ports for HTTP origin-pull requests. Range: 1-65535. It takes effect when `OriginProtocol=FOLLOW/HTTP`. The original configuration is used if it's not specified.
        :type HttpOriginPort: int
        :param _HttpsOriginPort: Ports for HTTPS origin-pull requests. Range: 1-65535. It takes effect when `OriginProtocol=FOLLOW/HTTPS`. The original configuration is used if it's not specified.
        :type HttpsOriginPort: int
        :param _IPv6Status: IPv6 status. Values:
<li>`follow`: Follow the IPv6 configuration of the site</li>
<li>`on`: Enable</li>
<li>`off`: Disable</li>
<li>The original configuration applies if this field is not specified.</li>
        :type IPv6Status: str
        """
        self._ZoneId = None
        self._DomainName = None
        self._OriginInfo = None
        self._OriginProtocol = None
        self._HttpOriginPort = None
        self._HttpsOriginPort = None
        self._IPv6Status = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def OriginInfo(self):
        return self._OriginInfo

    @OriginInfo.setter
    def OriginInfo(self, OriginInfo):
        self._OriginInfo = OriginInfo

    @property
    def OriginProtocol(self):
        return self._OriginProtocol

    @OriginProtocol.setter
    def OriginProtocol(self, OriginProtocol):
        self._OriginProtocol = OriginProtocol

    @property
    def HttpOriginPort(self):
        return self._HttpOriginPort

    @HttpOriginPort.setter
    def HttpOriginPort(self, HttpOriginPort):
        self._HttpOriginPort = HttpOriginPort

    @property
    def HttpsOriginPort(self):
        return self._HttpsOriginPort

    @HttpsOriginPort.setter
    def HttpsOriginPort(self, HttpsOriginPort):
        self._HttpsOriginPort = HttpsOriginPort

    @property
    def IPv6Status(self):
        return self._IPv6Status

    @IPv6Status.setter
    def IPv6Status(self, IPv6Status):
        self._IPv6Status = IPv6Status


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._DomainName = params.get("DomainName")
        if params.get("OriginInfo") is not None:
            self._OriginInfo = OriginInfo()
            self._OriginInfo._deserialize(params.get("OriginInfo"))
        self._OriginProtocol = params.get("OriginProtocol")
        self._HttpOriginPort = params.get("HttpOriginPort")
        self._HttpsOriginPort = params.get("HttpsOriginPort")
        self._IPv6Status = params.get("IPv6Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccelerationDomainResponse(AbstractModel):
    """ModifyAccelerationDomain response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyAccelerationDomainStatusesRequest(AbstractModel):
    """ModifyAccelerationDomainStatuses request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site related with the accelerated domain name.
        :type ZoneId: str
        :param _DomainNames: List of accelerated domain names to be modified.
        :type DomainNames: list of str
        :param _Status: Status of the accelerated domain name. Values:
<li>`online`: Enabled</li>
<li>`offline`: Disabled</li>
        :type Status: str
        :param _Force: Whether to force suspension when the domain name has associated resources (such as alias domain names and traffic scheduling policies). Values:
<li>`true`: Suspend the domain name and all associated resources.</li>
<li>`true`: Do not suspend the domain name and all associated resources.</li>Default value: `false`.
        :type Force: bool
        """
        self._ZoneId = None
        self._DomainNames = None
        self._Status = None
        self._Force = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def DomainNames(self):
        return self._DomainNames

    @DomainNames.setter
    def DomainNames(self, DomainNames):
        self._DomainNames = DomainNames

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Force(self):
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._DomainNames = params.get("DomainNames")
        self._Status = params.get("Status")
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccelerationDomainStatusesResponse(AbstractModel):
    """ModifyAccelerationDomainStatuses response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyAliasDomainRequest(AbstractModel):
    """ModifyAliasDomain request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: The site ID.
        :type ZoneId: str
        :param _AliasName: The alias domain name.
        :type AliasName: str
        :param _TargetName: The target domain name.
        :type TargetName: str
        :param _CertType: Certificate configuration. Values:
<li>`none`: Off</li>
<li>`hosting`: Managed SSL certificate</li>
<li>`apply`: Free certificate</li>The original configuration will apply if this field is not specified.
        :type CertType: str
        :param _CertId: The certificate ID. This field is required when `CertType=hosting`.
        :type CertId: list of str
        """
        self._ZoneId = None
        self._AliasName = None
        self._TargetName = None
        self._CertType = None
        self._CertId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def AliasName(self):
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName

    @property
    def TargetName(self):
        return self._TargetName

    @TargetName.setter
    def TargetName(self, TargetName):
        self._TargetName = TargetName

    @property
    def CertType(self):
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._AliasName = params.get("AliasName")
        self._TargetName = params.get("TargetName")
        self._CertType = params.get("CertType")
        self._CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAliasDomainResponse(AbstractModel):
    """ModifyAliasDomain response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyAliasDomainStatusRequest(AbstractModel):
    """ModifyAliasDomainStatus request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: The site ID.
        :type ZoneId: str
        :param _Paused: Status of the alias domain name. Values:
<li>`false`: Enable the alias domain name.</li>
<li>`true`: Disable the alias domain name.</li>
        :type Paused: bool
        :param _AliasNames: The alias domain name you want to modify its status. If it is left empty, the modify operation is not performed.
        :type AliasNames: list of str
        """
        self._ZoneId = None
        self._Paused = None
        self._AliasNames = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Paused(self):
        return self._Paused

    @Paused.setter
    def Paused(self, Paused):
        self._Paused = Paused

    @property
    def AliasNames(self):
        return self._AliasNames

    @AliasNames.setter
    def AliasNames(self, AliasNames):
        self._AliasNames = AliasNames


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Paused = params.get("Paused")
        self._AliasNames = params.get("AliasNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAliasDomainStatusResponse(AbstractModel):
    """ModifyAliasDomainStatus response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyApplicationProxyRequest(AbstractModel):
    """ModifyApplicationProxy request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID.
        :type ZoneId: str
        :param _ProxyId: Proxy ID.
        :type ProxyId: str
        :param _ProxyName: Domain name or subdomain name when `ProxyType=hostname`; 
Instance name when `ProxyType=instance`.
        :type ProxyName: str
        :param _SessionPersistTime: The session persistence duration. Value range: 30-3600 (in seconds).
The original configuration will apply if this field is not specified.
        :type SessionPersistTime: int
        :param _ProxyType: L4 proxy mode. Valid values: 
<li>instance: Instance mode. </li>If it is not specified, instance is used by default.
        :type ProxyType: str
        :param _Ipv6: IPv6 access configuration. The original configuration will apply if it is not specified.
        :type Ipv6: :class:`tencentcloud.teo.v20220901.models.Ipv6`
        :param _AccelerateMainland: Cross-MLC-border acceleration. The original configuration will apply if it is not specified.
        :type AccelerateMainland: :class:`tencentcloud.teo.v20220901.models.AccelerateMainland`
        """
        self._ZoneId = None
        self._ProxyId = None
        self._ProxyName = None
        self._SessionPersistTime = None
        self._ProxyType = None
        self._Ipv6 = None
        self._AccelerateMainland = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def ProxyName(self):
        return self._ProxyName

    @ProxyName.setter
    def ProxyName(self, ProxyName):
        self._ProxyName = ProxyName

    @property
    def SessionPersistTime(self):
        return self._SessionPersistTime

    @SessionPersistTime.setter
    def SessionPersistTime(self, SessionPersistTime):
        self._SessionPersistTime = SessionPersistTime

    @property
    def ProxyType(self):
        return self._ProxyType

    @ProxyType.setter
    def ProxyType(self, ProxyType):
        self._ProxyType = ProxyType

    @property
    def Ipv6(self):
        return self._Ipv6

    @Ipv6.setter
    def Ipv6(self, Ipv6):
        self._Ipv6 = Ipv6

    @property
    def AccelerateMainland(self):
        return self._AccelerateMainland

    @AccelerateMainland.setter
    def AccelerateMainland(self, AccelerateMainland):
        self._AccelerateMainland = AccelerateMainland


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        self._ProxyName = params.get("ProxyName")
        self._SessionPersistTime = params.get("SessionPersistTime")
        self._ProxyType = params.get("ProxyType")
        if params.get("Ipv6") is not None:
            self._Ipv6 = Ipv6()
            self._Ipv6._deserialize(params.get("Ipv6"))
        if params.get("AccelerateMainland") is not None:
            self._AccelerateMainland = AccelerateMainland()
            self._AccelerateMainland._deserialize(params.get("AccelerateMainland"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyResponse(AbstractModel):
    """ModifyApplicationProxy response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyApplicationProxyRuleRequest(AbstractModel):
    """ModifyApplicationProxyRule request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: The site ID.
        :type ZoneId: str
        :param _ProxyId: The proxy ID.
        :type ProxyId: str
        :param _RuleId: The rule ID.
        :type RuleId: str
        :param _OriginType: Origin server type. Valid values:
<li>custom: Manually added;</li>
<li>origins: Origin server group.</li>
        :type OriginType: str
        :param _Port: The access port, which can be:
<li>A single port, such as 80</li>
<li>A port range, such as 81-90</li>
        :type Port: list of str
        :param _Proto: The protocol. Values:
<li>`TCP`: TCP protocol</li>
<li>`UDP`: UDP protocol</li>The original configuration will apply if this field is not specified.
        :type Proto: str
        :param _OriginValue: Origin server information:
<li>When `OriginType=custom`, it indicates one or more origin servers, such as ["8.8.8.8","9.9.9.9"] or ["test.com"].</li>
<li>When `OriginType=origins`, it indicates an origin group ID, such as ["origin-537f5b41-162a-11ed-abaa-525400c5da15"].</li>

The original configuration will apply if this field is not specified.
        :type OriginValue: list of str
        :param _ForwardClientIp: Passes the client IP. Values:
<li>`TOA`: Pass the client IP via TOA (available only when `Proto=TCP`).</li>
<li>`PPV1`: Pass the client IP via Proxy Protocol V1 (available only when `Proto=TCP`).</li>
<li>`PPV2`: Pass the client IP via Proxy Protocol V2.</li>
<li>`OFF`: Not pass the client IP.</li>If not specified, this field uses the default value OFF.
        :type ForwardClientIp: str
        :param _SessionPersist: Whether to enable session persistence. Values:
<li>`true`: Enable</li>
<li>`false`: Disable</li>If it is left empty, the default value `false` is used.
        :type SessionPersist: bool
        :param _SessionPersistTime: Duration for the persistent session. The value takes effect only when `SessionPersist = true`.
        :type SessionPersistTime: int
        :param _OriginPort: The origin port, which can be:
<li>A single port, such as 80</li>
<li>A port range, such as 81-82</li>
        :type OriginPort: str
        :param _RuleTag: Rule tag. The original configuration will apply if it is not specified.
        :type RuleTag: str
        """
        self._ZoneId = None
        self._ProxyId = None
        self._RuleId = None
        self._OriginType = None
        self._Port = None
        self._Proto = None
        self._OriginValue = None
        self._ForwardClientIp = None
        self._SessionPersist = None
        self._SessionPersistTime = None
        self._OriginPort = None
        self._RuleTag = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def OriginType(self):
        return self._OriginType

    @OriginType.setter
    def OriginType(self, OriginType):
        self._OriginType = OriginType

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

    @property
    def OriginValue(self):
        return self._OriginValue

    @OriginValue.setter
    def OriginValue(self, OriginValue):
        self._OriginValue = OriginValue

    @property
    def ForwardClientIp(self):
        return self._ForwardClientIp

    @ForwardClientIp.setter
    def ForwardClientIp(self, ForwardClientIp):
        self._ForwardClientIp = ForwardClientIp

    @property
    def SessionPersist(self):
        return self._SessionPersist

    @SessionPersist.setter
    def SessionPersist(self, SessionPersist):
        self._SessionPersist = SessionPersist

    @property
    def SessionPersistTime(self):
        return self._SessionPersistTime

    @SessionPersistTime.setter
    def SessionPersistTime(self, SessionPersistTime):
        self._SessionPersistTime = SessionPersistTime

    @property
    def OriginPort(self):
        return self._OriginPort

    @OriginPort.setter
    def OriginPort(self, OriginPort):
        self._OriginPort = OriginPort

    @property
    def RuleTag(self):
        return self._RuleTag

    @RuleTag.setter
    def RuleTag(self, RuleTag):
        self._RuleTag = RuleTag


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        self._RuleId = params.get("RuleId")
        self._OriginType = params.get("OriginType")
        self._Port = params.get("Port")
        self._Proto = params.get("Proto")
        self._OriginValue = params.get("OriginValue")
        self._ForwardClientIp = params.get("ForwardClientIp")
        self._SessionPersist = params.get("SessionPersist")
        self._SessionPersistTime = params.get("SessionPersistTime")
        self._OriginPort = params.get("OriginPort")
        self._RuleTag = params.get("RuleTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyRuleResponse(AbstractModel):
    """ModifyApplicationProxyRule response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyApplicationProxyRuleStatusRequest(AbstractModel):
    """ModifyApplicationProxyRuleStatus request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: The site ID.
        :type ZoneId: str
        :param _ProxyId: The proxy ID.
        :type ProxyId: str
        :param _RuleId: The rule ID.
        :type RuleId: str
        :param _Status: The rule status. Values:
<li>`offline`: Disabled</li>
<li>`online`: Enabled</li>
        :type Status: str
        """
        self._ZoneId = None
        self._ProxyId = None
        self._RuleId = None
        self._Status = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        self._RuleId = params.get("RuleId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyRuleStatusResponse(AbstractModel):
    """ModifyApplicationProxyRuleStatus response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyApplicationProxyStatusRequest(AbstractModel):
    """ModifyApplicationProxyStatus request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: The site ID.
        :type ZoneId: str
        :param _ProxyId: The proxy ID.
        :type ProxyId: str
        :param _Status: The proxy status. Values:
<li>`offline`: The proxy is disabled.</li>
<li>`online`: The proxy is enabled.</li>
        :type Status: str
        """
        self._ZoneId = None
        self._ProxyId = None
        self._Status = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyStatusResponse(AbstractModel):
    """ModifyApplicationProxyStatus response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyCustomErrorPageRequest(AbstractModel):
    """ModifyCustomErrorPage request structure.

    """

    def __init__(self):
        r"""
        :param _PageId: Custom error page ID.
        :type PageId: str
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _Name: Custom error page name. The name must be 2-60 characters long.
        :type Name: str
        :param _Description: Custom error page description, not exceeding 60 characters.
        :type Description: str
        :param _ContentType: Custom error page type, with values:<li>text/html. </li><li>application/json.</li><li>plain/text.</li><li>text/xml.</li>
        :type ContentType: str
        :param _Content: Custom error page content, not exceeding 2 KB.
        :type Content: str
        """
        self._PageId = None
        self._ZoneId = None
        self._Name = None
        self._Description = None
        self._ContentType = None
        self._Content = None

    @property
    def PageId(self):
        return self._PageId

    @PageId.setter
    def PageId(self, PageId):
        self._PageId = PageId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

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
    def ContentType(self):
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._PageId = params.get("PageId")
        self._ZoneId = params.get("ZoneId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._ContentType = params.get("ContentType")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomErrorPageResponse(AbstractModel):
    """ModifyCustomErrorPage response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyFunctionRequest(AbstractModel):
    """ModifyFunction request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _FunctionId: Function ID.
        :type FunctionId: str
        :param _Remark: Function description, which can contain up to 60 characters. If this parameter is not input, the original configuration is maintained.
        :type Remark: str
        :param _Content: Function content, which currently only supports JavaScript code. Its maximum size is 5 MB. If this parameter is not input, the original configuration is maintained.
        :type Content: str
        """
        self._ZoneId = None
        self._FunctionId = None
        self._Remark = None
        self._Content = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def FunctionId(self):
        return self._FunctionId

    @FunctionId.setter
    def FunctionId(self, FunctionId):
        self._FunctionId = FunctionId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._FunctionId = params.get("FunctionId")
        self._Remark = params.get("Remark")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFunctionResponse(AbstractModel):
    """ModifyFunction response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyFunctionRulePriorityRequest(AbstractModel):
    """ModifyFunctionRulePriority request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _RuleIds: Rule ID list. All rule IDs after priority adjustment must be input. Multiple rules are executed from top to bottom. If this parameter is not input, the original priority order is maintained.
        :type RuleIds: list of str
        """
        self._ZoneId = None
        self._RuleIds = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RuleIds(self):
        return self._RuleIds

    @RuleIds.setter
    def RuleIds(self, RuleIds):
        self._RuleIds = RuleIds


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RuleIds = params.get("RuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFunctionRulePriorityResponse(AbstractModel):
    """ModifyFunctionRulePriority response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyFunctionRuleRequest(AbstractModel):
    """ModifyFunctionRule request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _RuleId: Rule ID.
        :type RuleId: str
        :param _FunctionRuleConditions: Rule condition list. There is an OR relationship between different conditions of the same trigger rule. If this parameter is not input, the original configuration is maintained.
        :type FunctionRuleConditions: list of FunctionRuleCondition
        :param _FunctionId: Function ID, specifying a function executed when a trigger rule condition is met. If this parameter is not input, the original configuration is maintained.
        :type FunctionId: str
        :param _Remark: Rule description, which can contain up to 60 characters. If this parameter is not input, the original configuration is maintained.
        :type Remark: str
        """
        self._ZoneId = None
        self._RuleId = None
        self._FunctionRuleConditions = None
        self._FunctionId = None
        self._Remark = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def FunctionRuleConditions(self):
        return self._FunctionRuleConditions

    @FunctionRuleConditions.setter
    def FunctionRuleConditions(self, FunctionRuleConditions):
        self._FunctionRuleConditions = FunctionRuleConditions

    @property
    def FunctionId(self):
        return self._FunctionId

    @FunctionId.setter
    def FunctionId(self, FunctionId):
        self._FunctionId = FunctionId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RuleId = params.get("RuleId")
        if params.get("FunctionRuleConditions") is not None:
            self._FunctionRuleConditions = []
            for item in params.get("FunctionRuleConditions"):
                obj = FunctionRuleCondition()
                obj._deserialize(item)
                self._FunctionRuleConditions.append(obj)
        self._FunctionId = params.get("FunctionId")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFunctionRuleResponse(AbstractModel):
    """ModifyFunctionRule response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyHostsCertificateRequest(AbstractModel):
    """ModifyHostsCertificate request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site.
        :type ZoneId: str
        :param _Hosts: Domain names that you need to modify the certificate configuration
        :type Hosts: list of str
        :param _Mode: Certificate configuration mode. Values:
<li>`disable`: (Default) Do not configure the certificate</li>
<li>`eofreecert`: Use a free certificate provided by EdgeOne</li>
<li>`sslcert`: Configure an SSL certificate.</li>
        :type Mode: str
        :param _ServerCertInfo: ID of the SSL certificate. It takes effect when `mode=sslcert`. To check the certificate ID, go to the [SSL Certificate](https://console.cloud.tencent.com/certoview) console.
        :type ServerCertInfo: list of ServerCertInfo
        :param _ApplyType: Whether the certificate is managed by EdgeOne. Values:
<li>`none`: Not managed by EdgeOne</li>
<li>`apply`: Managed by EdgeOne</li>
Default value: `none`.
        :type ApplyType: str
        """
        self._ZoneId = None
        self._Hosts = None
        self._Mode = None
        self._ServerCertInfo = None
        self._ApplyType = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Hosts(self):
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def ServerCertInfo(self):
        return self._ServerCertInfo

    @ServerCertInfo.setter
    def ServerCertInfo(self, ServerCertInfo):
        self._ServerCertInfo = ServerCertInfo

    @property
    def ApplyType(self):
        warnings.warn("parameter `ApplyType` is deprecated", DeprecationWarning) 

        return self._ApplyType

    @ApplyType.setter
    def ApplyType(self, ApplyType):
        warnings.warn("parameter `ApplyType` is deprecated", DeprecationWarning) 

        self._ApplyType = ApplyType


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Hosts = params.get("Hosts")
        self._Mode = params.get("Mode")
        if params.get("ServerCertInfo") is not None:
            self._ServerCertInfo = []
            for item in params.get("ServerCertInfo"):
                obj = ServerCertInfo()
                obj._deserialize(item)
                self._ServerCertInfo.append(obj)
        self._ApplyType = params.get("ApplyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHostsCertificateResponse(AbstractModel):
    """ModifyHostsCertificate response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyL4ProxyRequest(AbstractModel):
    """ModifyL4Proxy request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _ProxyId: Application ID.
        :type ProxyId: str
        :param _Ipv6: Specifies whether to enable IPv6 access. If this parameter is not filled, this configuration will not be modified. This configuration can only be enabled in certain acceleration zones and security protection configurations. For details, see [Creating an L4 Proxy Instance] (https://intl.cloud.tencent.com/document/product/1552/90025?from_cn_redirect=1). Valid values:<li>on: Enable;</li> 
<li>off: Disable.</li>

        :type Ipv6: str
        :param _AccelerateMainland: Specifies whether to enable network optimization in the Chinese mainland. If this parameter is not filled, this configuration will not be modified. This configuration can only be enabled in certain acceleration zones and security protection configurations. For details, see [Creating an L4 Proxy Instance] (https://intl.cloud.tencent.com/document/product/1552/90025?from_cn_redirect=1). Valid values:<li>on: Enable;</li> 
<li>off: Disable.</li>
        :type AccelerateMainland: str
        """
        self._ZoneId = None
        self._ProxyId = None
        self._Ipv6 = None
        self._AccelerateMainland = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def Ipv6(self):
        return self._Ipv6

    @Ipv6.setter
    def Ipv6(self, Ipv6):
        self._Ipv6 = Ipv6

    @property
    def AccelerateMainland(self):
        return self._AccelerateMainland

    @AccelerateMainland.setter
    def AccelerateMainland(self, AccelerateMainland):
        self._AccelerateMainland = AccelerateMainland


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        self._Ipv6 = params.get("Ipv6")
        self._AccelerateMainland = params.get("AccelerateMainland")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL4ProxyResponse(AbstractModel):
    """ModifyL4Proxy response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyL4ProxyRulesRequest(AbstractModel):
    """ModifyL4ProxyRules request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _ProxyId: Layer 4 proxy instance ID.
        :type ProxyId: str
        :param _L4ProxyRules: List of forwarding rules. A single request supports up to 200 forwarding rules.
Note: When L4ProxyRule is used here, RuleId is a required field; Protocol, PortRange, OriginType, OriginValue, OriginPortRange, ClientIPPassThroughMode, SessionPersist, SessionPersistTime, and RuleTag are all optional fields. No modification is made when no value is specified for those fields. Status should not be filled.
        :type L4ProxyRules: list of L4ProxyRule
        """
        self._ZoneId = None
        self._ProxyId = None
        self._L4ProxyRules = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def L4ProxyRules(self):
        return self._L4ProxyRules

    @L4ProxyRules.setter
    def L4ProxyRules(self, L4ProxyRules):
        self._L4ProxyRules = L4ProxyRules


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        if params.get("L4ProxyRules") is not None:
            self._L4ProxyRules = []
            for item in params.get("L4ProxyRules"):
                obj = L4ProxyRule()
                obj._deserialize(item)
                self._L4ProxyRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL4ProxyRulesResponse(AbstractModel):
    """ModifyL4ProxyRules response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyL4ProxyRulesStatusRequest(AbstractModel):
    """ModifyL4ProxyRulesStatus request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _ProxyId: Layer 4 proxy instance ID.
        :type ProxyId: str
        :param _RuleIds: List of forwarding rule IDs. It supports up to 200 forwarding rules at a time.
        :type RuleIds: list of str
        :param _Status: Status of forwarding rules. Valid values:
<li>online: Enabled;</li>
<li>offline: Disabled.</li>
        :type Status: str
        """
        self._ZoneId = None
        self._ProxyId = None
        self._RuleIds = None
        self._Status = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def RuleIds(self):
        return self._RuleIds

    @RuleIds.setter
    def RuleIds(self, RuleIds):
        self._RuleIds = RuleIds

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        self._RuleIds = params.get("RuleIds")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL4ProxyRulesStatusResponse(AbstractModel):
    """ModifyL4ProxyRulesStatus response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyL4ProxyStatusRequest(AbstractModel):
    """ModifyL4ProxyStatus request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _ProxyId: Layer 4 proxy instance ID.
        :type ProxyId: str
        :param _Status: Layer 4 proxy instance status. Valid values:<li>online: Enabled;</li>
<li>offline: Disabled.</li>
        :type Status: str
        """
        self._ZoneId = None
        self._ProxyId = None
        self._Status = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL4ProxyStatusResponse(AbstractModel):
    """ModifyL4ProxyStatus response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyOriginGroupRequest(AbstractModel):
    """ModifyOriginGroup request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID
        :type ZoneId: str
        :param _GroupId: (Required) Origin group ID
        :type GroupId: str
        :param _Name: Origin group name. It can contain 1 to 200 characters ([a-z], [A-Z], [0-9] and [_-]). The original configuration applies if this field is not specified.	
        :type Name: str
        :param _Type: The origin grouptype. Values:
<li>`GENERAL`: General origin groups. It supports IPs and domain names. It can be referenced by DNS, Rule Engine, Layer 4 Proxy and General LoadBalancer.</li>
<li>`HTTP`: HTTP-specific origin groups. It supports IPs/domain names and object storage buckets. It can be referenced by acceleration domain names, rule engines and HTTP LoadBalancer. It cannot be referenced by L4 proxies. </li>The original configuration is used if it's not specified.
        :type Type: str
        :param _Records: Origin information. The original configuration is used if it's not specified.
        :type Records: list of OriginRecord
        :param _HostHeader: Host header used for origin-pull. It only works when `Type=HTTP`. If it's not specified, no specific Host header is configured. The `HostHeader` specified in `RuleEngine` takes a higher priority over this configuration. 
        :type HostHeader: str
        """
        self._ZoneId = None
        self._GroupId = None
        self._Name = None
        self._Type = None
        self._Records = None
        self._HostHeader = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Records(self):
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def HostHeader(self):
        return self._HostHeader

    @HostHeader.setter
    def HostHeader(self, HostHeader):
        self._HostHeader = HostHeader


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._GroupId = params.get("GroupId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = OriginRecord()
                obj._deserialize(item)
                self._Records.append(obj)
        self._HostHeader = params.get("HostHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOriginGroupResponse(AbstractModel):
    """ModifyOriginGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyPlanRequest(AbstractModel):
    """ModifyPlan request structure.

    """

    def __init__(self):
        r"""
        :param _PlanId: Plan ID, formatted as edgeone-2unuvzjmmn2q.
        :type PlanId: str
        :param _RenewFlag: Auto-renewal configuration item in a prepaid plan. If auto-renewal is enabled, the plan will be automatically renewed one day before it expires. This feature is only available for Personal, Basic, and Standard Edition Plans. If this field is not specified, the original configuration will be retained.
        :type RenewFlag: :class:`tencentcloud.teo.v20220901.models.RenewFlag`
        """
        self._PlanId = None
        self._RenewFlag = None

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        if params.get("RenewFlag") is not None:
            self._RenewFlag = RenewFlag()
            self._RenewFlag._deserialize(params.get("RenewFlag"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPlanResponse(AbstractModel):
    """ModifyPlan response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyRealtimeLogDeliveryTaskRequest(AbstractModel):
    """ModifyRealtimeLogDeliveryTask request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Zone ID.
        :type ZoneId: str
        :param _TaskId: The ID of the real-time log delivery task.
        :type TaskId: str
        :param _TaskName: The name of the real-time log delivery task, which is a combination of numbers, English letters, - and _, containing up to 200 characters. If this field is not filled in, the original configuration will be retained.
        :type TaskName: str
        :param _DeliveryStatus: The status of the real-time log delivery task. Valid values:
<li>`enabled`: Enabled;</li>
<li>`disabled`: Disabled.</li>If this field is not filled in, the original configuration will be retained.
        :type DeliveryStatus: str
        :param _EntityList: The list of entities (Layer 7 domains or Layer 4 proxy instances) corresponding to the real-time log delivery task. Valid value examples:
<li>Layer 7 domain: domain.example.com;</li>
<li>Layer 4 proxy instance: sid-2s69eb5wcms7.</li>If this field is not filled in, the original configuration will be retained.
        :type EntityList: list of str
        :param _Fields: The list of predefined fields for delivery. If this field is not filled in, the original configuration will be retained.
        :type Fields: list of str
        :param _CustomFields: The list of custom fields for delivery, supporting extracting specified field values from HTTP request headers, response headers, and cookies. Each custom field name must be unique and the maximum number of fields is 200. If this field is not filled in, the original configuration will be retained.
        :type CustomFields: list of CustomField
        :param _DeliveryConditions: Log delivery filter conditions. If this field is not filled in, all logs will be delivered.
        :type DeliveryConditions: list of DeliveryCondition
        :param _Sample: The sampling ratio in permille. Value range: 1 to 1000. For example, 605 represents a sampling ratio of 60.5%. If this field is not filled in, the original configuration will be retained.
        :type Sample: int
        :param _LogFormat: Output format for log delivery. If this field is not specified, the original configuration will be retained.Specifically, when TaskType is set to cls, the value of LogFormat.FormatType can only be json, and other parameters in LogFormat will be ignored. It is recommended not to input LogFormat.
        :type LogFormat: :class:`tencentcloud.teo.v20220901.models.LogFormat`
        :param _CustomEndpoint: The configuration information of the custom HTTP service. If this field is not filled in, the original configuration will be retained.
        :type CustomEndpoint: :class:`tencentcloud.teo.v20220901.models.CustomEndpoint`
        :param _S3: The configuration information of the AWS S3-compatible bucket. If this field is not filled in, the original configuration will be retained.
        :type S3: :class:`tencentcloud.teo.v20220901.models.S3`
        """
        self._ZoneId = None
        self._TaskId = None
        self._TaskName = None
        self._DeliveryStatus = None
        self._EntityList = None
        self._Fields = None
        self._CustomFields = None
        self._DeliveryConditions = None
        self._Sample = None
        self._LogFormat = None
        self._CustomEndpoint = None
        self._S3 = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def DeliveryStatus(self):
        return self._DeliveryStatus

    @DeliveryStatus.setter
    def DeliveryStatus(self, DeliveryStatus):
        self._DeliveryStatus = DeliveryStatus

    @property
    def EntityList(self):
        return self._EntityList

    @EntityList.setter
    def EntityList(self, EntityList):
        self._EntityList = EntityList

    @property
    def Fields(self):
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields

    @property
    def CustomFields(self):
        return self._CustomFields

    @CustomFields.setter
    def CustomFields(self, CustomFields):
        self._CustomFields = CustomFields

    @property
    def DeliveryConditions(self):
        return self._DeliveryConditions

    @DeliveryConditions.setter
    def DeliveryConditions(self, DeliveryConditions):
        self._DeliveryConditions = DeliveryConditions

    @property
    def Sample(self):
        return self._Sample

    @Sample.setter
    def Sample(self, Sample):
        self._Sample = Sample

    @property
    def LogFormat(self):
        return self._LogFormat

    @LogFormat.setter
    def LogFormat(self, LogFormat):
        self._LogFormat = LogFormat

    @property
    def CustomEndpoint(self):
        return self._CustomEndpoint

    @CustomEndpoint.setter
    def CustomEndpoint(self, CustomEndpoint):
        self._CustomEndpoint = CustomEndpoint

    @property
    def S3(self):
        return self._S3

    @S3.setter
    def S3(self, S3):
        self._S3 = S3


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._DeliveryStatus = params.get("DeliveryStatus")
        self._EntityList = params.get("EntityList")
        self._Fields = params.get("Fields")
        if params.get("CustomFields") is not None:
            self._CustomFields = []
            for item in params.get("CustomFields"):
                obj = CustomField()
                obj._deserialize(item)
                self._CustomFields.append(obj)
        if params.get("DeliveryConditions") is not None:
            self._DeliveryConditions = []
            for item in params.get("DeliveryConditions"):
                obj = DeliveryCondition()
                obj._deserialize(item)
                self._DeliveryConditions.append(obj)
        self._Sample = params.get("Sample")
        if params.get("LogFormat") is not None:
            self._LogFormat = LogFormat()
            self._LogFormat._deserialize(params.get("LogFormat"))
        if params.get("CustomEndpoint") is not None:
            self._CustomEndpoint = CustomEndpoint()
            self._CustomEndpoint._deserialize(params.get("CustomEndpoint"))
        if params.get("S3") is not None:
            self._S3 = S3()
            self._S3._deserialize(params.get("S3"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRealtimeLogDeliveryTaskResponse(AbstractModel):
    """ModifyRealtimeLogDeliveryTask response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyRuleRequest(AbstractModel):
    """ModifyRule request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site
        :type ZoneId: str
        :param _RuleName: The rule name. It is a string that can contain 1–255 characters.
        :type RuleName: str
        :param _Rules: The rule content.
        :type Rules: list of Rule
        :param _RuleId: The rule ID.
        :type RuleId: str
        :param _Status: Rule status. Values:
<li>`enable`: Enabled</li>
<li>`disable`: Disabled</li>
        :type Status: str
        :param _Tags: Tag of the rule.
        :type Tags: list of str
        """
        self._ZoneId = None
        self._RuleName = None
        self._Rules = None
        self._RuleId = None
        self._Status = None
        self._Tags = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RuleName = params.get("RuleName")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = Rule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._RuleId = params.get("RuleId")
        self._Status = params.get("Status")
        self._Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRuleResponse(AbstractModel):
    """ModifyRule response structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleId = None
        self._RequestId = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class ModifySecurityIPGroupRequest(AbstractModel):
    """ModifySecurityIPGroup request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID.
        :type ZoneId: str
        :param _IPGroup: IP group configuration.
        :type IPGroup: :class:`tencentcloud.teo.v20220901.models.IPGroup`
        :param _Mode: Operation type. Valid values: 
<li>`append`: Add information of `Content` to `IPGroup`;</li>
<li>`remove`: Delete information of `Content` from `IPGroup`;</li>
<li>`update`: Replace all information of `IPGroup` and modify the IPGroup name.</li>
        :type Mode: str
        """
        self._ZoneId = None
        self._IPGroup = None
        self._Mode = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def IPGroup(self):
        return self._IPGroup

    @IPGroup.setter
    def IPGroup(self, IPGroup):
        self._IPGroup = IPGroup

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("IPGroup") is not None:
            self._IPGroup = IPGroup()
            self._IPGroup._deserialize(params.get("IPGroup"))
        self._Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityIPGroupResponse(AbstractModel):
    """ModifySecurityIPGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifySecurityPolicyRequest(AbstractModel):
    """ModifySecurityPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: The site ID.
        :type ZoneId: str
        :param _SecurityConfig: Security configuration.
        :type SecurityConfig: :class:`tencentcloud.teo.v20220901.models.SecurityConfig`
        :param _Entity: Subdomain/application name.

Note: When both this parameter and the TemplateId parameter are specified, this parameter will not take effect. Do not specify this parameter and the TemplateId parameter at the same time.
        :type Entity: str
        :param _TemplateId: Specifies the policy template ID, or the site's global policy.
- To configure a policy template, specify the policy template ID.
- To configure the site's global policy, use the @ZoneLevel@Domain parameter value.

Note: When this parameter is used, the Entity parameter will not take effect. Do not use this parameter and the Entity parameter at the same time.
        :type TemplateId: str
        """
        self._ZoneId = None
        self._SecurityConfig = None
        self._Entity = None
        self._TemplateId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def SecurityConfig(self):
        return self._SecurityConfig

    @SecurityConfig.setter
    def SecurityConfig(self, SecurityConfig):
        self._SecurityConfig = SecurityConfig

    @property
    def Entity(self):
        return self._Entity

    @Entity.setter
    def Entity(self, Entity):
        self._Entity = Entity

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("SecurityConfig") is not None:
            self._SecurityConfig = SecurityConfig()
            self._SecurityConfig._deserialize(params.get("SecurityConfig"))
        self._Entity = params.get("Entity")
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityPolicyResponse(AbstractModel):
    """ModifySecurityPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyZoneRequest(AbstractModel):
    """ModifyZone request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: The site ID.
        :type ZoneId: str
        :param _Type: Site access method. Valid values:
<li>full: NS access.</li>
<li>partial: CNAME access. If the site is currently accessed with no domain name, it can be switched only to CNAME access.</li>
<li>dnsPodAccess: DNSPod hosted access. To use this access mode, your domain name should have been hosted on DNSPod.</li>If this parameter is not input, the original configuration is maintained.
        :type Type: str
        :param _VanityNameServers: The custom name servers. The original configuration applies if this field is not specified. It is not allowed to pass this field when a site is connected without using a domain name.
        :type VanityNameServers: :class:`tencentcloud.teo.v20220901.models.VanityNameServers`
        :param _AliasZoneName: The site alias. It can be up to 20 characters consisting of digits, letters, hyphens (-) and underscores (_).
        :type AliasZoneName: str
        :param _Area: The region where the site requests access. Values:
<li> `global`: Global coverage</li>
<li> `mainland`: Chinese mainland</li>
<li> `overseas`: Outside the Chinese mainland </li>It is not allowed to pass this field when a site is connected without using a domain name.
        :type Area: str
        :param _ZoneName: Name of the site. This field takes effect only when the site switches from domainless access to CNAME access.
        :type ZoneName: str
        """
        self._ZoneId = None
        self._Type = None
        self._VanityNameServers = None
        self._AliasZoneName = None
        self._Area = None
        self._ZoneName = None

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
    def VanityNameServers(self):
        return self._VanityNameServers

    @VanityNameServers.setter
    def VanityNameServers(self, VanityNameServers):
        self._VanityNameServers = VanityNameServers

    @property
    def AliasZoneName(self):
        return self._AliasZoneName

    @AliasZoneName.setter
    def AliasZoneName(self, AliasZoneName):
        self._AliasZoneName = AliasZoneName

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Type = params.get("Type")
        if params.get("VanityNameServers") is not None:
            self._VanityNameServers = VanityNameServers()
            self._VanityNameServers._deserialize(params.get("VanityNameServers"))
        self._AliasZoneName = params.get("AliasZoneName")
        self._Area = params.get("Area")
        self._ZoneName = params.get("ZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneResponse(AbstractModel):
    """ModifyZone response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyZoneSettingRequest(AbstractModel):
    """ModifyZoneSetting request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID to modify.
        :type ZoneId: str
        :param _CacheConfig: Cache expiration time configuration
The original configuration will apply if this field is not specified.
        :type CacheConfig: :class:`tencentcloud.teo.v20220901.models.CacheConfig`
        :param _CacheKey: The node cache key configuration.
The original configuration will apply if this field is not specified.
        :type CacheKey: :class:`tencentcloud.teo.v20220901.models.CacheKey`
        :param _MaxAge: The browser cache configuration.
The original configuration will apply if this field is not specified.
        :type MaxAge: :class:`tencentcloud.teo.v20220901.models.MaxAge`
        :param _OfflineCache: The offline cache configuration.
The original configuration will apply if this field is not specified.
        :type OfflineCache: :class:`tencentcloud.teo.v20220901.models.OfflineCache`
        :param _Quic: QUIC access configuration. 
The original configuration will apply if it is not specified.
        :type Quic: :class:`tencentcloud.teo.v20220901.models.Quic`
        :param _PostMaxSize: POST transport configuration. 
The original configuration will apply if it is not specified.
        :type PostMaxSize: :class:`tencentcloud.teo.v20220901.models.PostMaxSize`
        :param _Compression: The smart compression configuration.
The original configuration will apply if this field is not specified.
        :type Compression: :class:`tencentcloud.teo.v20220901.models.Compression`
        :param _UpstreamHttp2: HTTP2 origin-pull configuration. 
The original configuration will apply if it is not specified.
        :type UpstreamHttp2: :class:`tencentcloud.teo.v20220901.models.UpstreamHttp2`
        :param _ForceRedirect: Force HTTPS redirect configuration. 
The original configuration will apply if it is not specified.
        :type ForceRedirect: :class:`tencentcloud.teo.v20220901.models.ForceRedirect`
        :param _Https: HTTPS acceleration configuration. 
The original configuration will apply if it is not specified.
        :type Https: :class:`tencentcloud.teo.v20220901.models.Https`
        :param _Origin: The origin server configuration.
The original configuration will apply if this field is not specified.
        :type Origin: :class:`tencentcloud.teo.v20220901.models.Origin`
        :param _SmartRouting: The smart acceleration configuration.
The original configuration will apply if this field is not specified.
        :type SmartRouting: :class:`tencentcloud.teo.v20220901.models.SmartRouting`
        :param _WebSocket: WebSocket configuration. 
The original configuration will apply if it is not specified.
        :type WebSocket: :class:`tencentcloud.teo.v20220901.models.WebSocket`
        :param _ClientIpHeader: Origin-pull client IP header configuration. 
The original configuration will apply if it is not specified.
        :type ClientIpHeader: :class:`tencentcloud.teo.v20220901.models.ClientIpHeader`
        :param _CachePrefresh: The cache prefresh configuration.
The original configuration will apply if this field is not specified.
        :type CachePrefresh: :class:`tencentcloud.teo.v20220901.models.CachePrefresh`
        :param _Ipv6: Ipv6 access configuration. 
The original configuration will apply if it is not specified.
        :type Ipv6: :class:`tencentcloud.teo.v20220901.models.Ipv6`
        :param _ClientIpCountry: Whether to carry the location information of the client IP during origin-pull. 
The original configuration will apply if it is not specified.
        :type ClientIpCountry: :class:`tencentcloud.teo.v20220901.models.ClientIpCountry`
        :param _Grpc: Configuration of gRPC support. 
The original configuration will apply if it is not specified.
        :type Grpc: :class:`tencentcloud.teo.v20220901.models.Grpc`
        :param _ImageOptimize: Image optimization. 
It is disabled if this parameter is not specified.
        :type ImageOptimize: :class:`tencentcloud.teo.v20220901.models.ImageOptimize`
        :param _StandardDebug: Standard debugging configuration.
        :type StandardDebug: :class:`tencentcloud.teo.v20220901.models.StandardDebug`
        """
        self._ZoneId = None
        self._CacheConfig = None
        self._CacheKey = None
        self._MaxAge = None
        self._OfflineCache = None
        self._Quic = None
        self._PostMaxSize = None
        self._Compression = None
        self._UpstreamHttp2 = None
        self._ForceRedirect = None
        self._Https = None
        self._Origin = None
        self._SmartRouting = None
        self._WebSocket = None
        self._ClientIpHeader = None
        self._CachePrefresh = None
        self._Ipv6 = None
        self._ClientIpCountry = None
        self._Grpc = None
        self._ImageOptimize = None
        self._StandardDebug = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def CacheConfig(self):
        return self._CacheConfig

    @CacheConfig.setter
    def CacheConfig(self, CacheConfig):
        self._CacheConfig = CacheConfig

    @property
    def CacheKey(self):
        return self._CacheKey

    @CacheKey.setter
    def CacheKey(self, CacheKey):
        self._CacheKey = CacheKey

    @property
    def MaxAge(self):
        return self._MaxAge

    @MaxAge.setter
    def MaxAge(self, MaxAge):
        self._MaxAge = MaxAge

    @property
    def OfflineCache(self):
        return self._OfflineCache

    @OfflineCache.setter
    def OfflineCache(self, OfflineCache):
        self._OfflineCache = OfflineCache

    @property
    def Quic(self):
        return self._Quic

    @Quic.setter
    def Quic(self, Quic):
        self._Quic = Quic

    @property
    def PostMaxSize(self):
        return self._PostMaxSize

    @PostMaxSize.setter
    def PostMaxSize(self, PostMaxSize):
        self._PostMaxSize = PostMaxSize

    @property
    def Compression(self):
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression

    @property
    def UpstreamHttp2(self):
        return self._UpstreamHttp2

    @UpstreamHttp2.setter
    def UpstreamHttp2(self, UpstreamHttp2):
        self._UpstreamHttp2 = UpstreamHttp2

    @property
    def ForceRedirect(self):
        return self._ForceRedirect

    @ForceRedirect.setter
    def ForceRedirect(self, ForceRedirect):
        self._ForceRedirect = ForceRedirect

    @property
    def Https(self):
        return self._Https

    @Https.setter
    def Https(self, Https):
        self._Https = Https

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def SmartRouting(self):
        return self._SmartRouting

    @SmartRouting.setter
    def SmartRouting(self, SmartRouting):
        self._SmartRouting = SmartRouting

    @property
    def WebSocket(self):
        return self._WebSocket

    @WebSocket.setter
    def WebSocket(self, WebSocket):
        self._WebSocket = WebSocket

    @property
    def ClientIpHeader(self):
        return self._ClientIpHeader

    @ClientIpHeader.setter
    def ClientIpHeader(self, ClientIpHeader):
        self._ClientIpHeader = ClientIpHeader

    @property
    def CachePrefresh(self):
        return self._CachePrefresh

    @CachePrefresh.setter
    def CachePrefresh(self, CachePrefresh):
        self._CachePrefresh = CachePrefresh

    @property
    def Ipv6(self):
        return self._Ipv6

    @Ipv6.setter
    def Ipv6(self, Ipv6):
        self._Ipv6 = Ipv6

    @property
    def ClientIpCountry(self):
        return self._ClientIpCountry

    @ClientIpCountry.setter
    def ClientIpCountry(self, ClientIpCountry):
        self._ClientIpCountry = ClientIpCountry

    @property
    def Grpc(self):
        return self._Grpc

    @Grpc.setter
    def Grpc(self, Grpc):
        self._Grpc = Grpc

    @property
    def ImageOptimize(self):
        return self._ImageOptimize

    @ImageOptimize.setter
    def ImageOptimize(self, ImageOptimize):
        self._ImageOptimize = ImageOptimize

    @property
    def StandardDebug(self):
        return self._StandardDebug

    @StandardDebug.setter
    def StandardDebug(self, StandardDebug):
        self._StandardDebug = StandardDebug


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("CacheConfig") is not None:
            self._CacheConfig = CacheConfig()
            self._CacheConfig._deserialize(params.get("CacheConfig"))
        if params.get("CacheKey") is not None:
            self._CacheKey = CacheKey()
            self._CacheKey._deserialize(params.get("CacheKey"))
        if params.get("MaxAge") is not None:
            self._MaxAge = MaxAge()
            self._MaxAge._deserialize(params.get("MaxAge"))
        if params.get("OfflineCache") is not None:
            self._OfflineCache = OfflineCache()
            self._OfflineCache._deserialize(params.get("OfflineCache"))
        if params.get("Quic") is not None:
            self._Quic = Quic()
            self._Quic._deserialize(params.get("Quic"))
        if params.get("PostMaxSize") is not None:
            self._PostMaxSize = PostMaxSize()
            self._PostMaxSize._deserialize(params.get("PostMaxSize"))
        if params.get("Compression") is not None:
            self._Compression = Compression()
            self._Compression._deserialize(params.get("Compression"))
        if params.get("UpstreamHttp2") is not None:
            self._UpstreamHttp2 = UpstreamHttp2()
            self._UpstreamHttp2._deserialize(params.get("UpstreamHttp2"))
        if params.get("ForceRedirect") is not None:
            self._ForceRedirect = ForceRedirect()
            self._ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Https") is not None:
            self._Https = Https()
            self._Https._deserialize(params.get("Https"))
        if params.get("Origin") is not None:
            self._Origin = Origin()
            self._Origin._deserialize(params.get("Origin"))
        if params.get("SmartRouting") is not None:
            self._SmartRouting = SmartRouting()
            self._SmartRouting._deserialize(params.get("SmartRouting"))
        if params.get("WebSocket") is not None:
            self._WebSocket = WebSocket()
            self._WebSocket._deserialize(params.get("WebSocket"))
        if params.get("ClientIpHeader") is not None:
            self._ClientIpHeader = ClientIpHeader()
            self._ClientIpHeader._deserialize(params.get("ClientIpHeader"))
        if params.get("CachePrefresh") is not None:
            self._CachePrefresh = CachePrefresh()
            self._CachePrefresh._deserialize(params.get("CachePrefresh"))
        if params.get("Ipv6") is not None:
            self._Ipv6 = Ipv6()
            self._Ipv6._deserialize(params.get("Ipv6"))
        if params.get("ClientIpCountry") is not None:
            self._ClientIpCountry = ClientIpCountry()
            self._ClientIpCountry._deserialize(params.get("ClientIpCountry"))
        if params.get("Grpc") is not None:
            self._Grpc = Grpc()
            self._Grpc._deserialize(params.get("Grpc"))
        if params.get("ImageOptimize") is not None:
            self._ImageOptimize = ImageOptimize()
            self._ImageOptimize._deserialize(params.get("ImageOptimize"))
        if params.get("StandardDebug") is not None:
            self._StandardDebug = StandardDebug()
            self._StandardDebug._deserialize(params.get("StandardDebug"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneSettingResponse(AbstractModel):
    """ModifyZoneSetting response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class ModifyZoneStatusRequest(AbstractModel):
    """ModifyZoneStatus request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: The site ID.
        :type ZoneId: str
        :param _Paused: The site status. Values:
<li>`false`: Disabled</li>
<li>`true`: Enabled</li>
        :type Paused: bool
        """
        self._ZoneId = None
        self._Paused = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Paused(self):
        return self._Paused

    @Paused.setter
    def Paused(self, Paused):
        self._Paused = Paused


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Paused = params.get("Paused")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneStatusResponse(AbstractModel):
    """ModifyZoneStatus response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class NoCache(AbstractModel):
    """No-cache configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable no-cache configuration. Valid values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NormalAction(AbstractModel):
    """Common action of the rule engine

    """

    def __init__(self):
        r"""
        :param _Action: Feature name. For details, see [DescribeRulesSetting](https://intl.cloud.tencent.com/document/product/1552/80618?from_cn_redirect=1) API
        :type Action: str
        :param _Parameters: Parameter
        :type Parameters: list of RuleNormalActionParams
        """
        self._Action = None
        self._Parameters = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Parameters(self):
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters


    def _deserialize(self, params):
        self._Action = params.get("Action")
        if params.get("Parameters") is not None:
            self._Parameters = []
            for item in params.get("Parameters"):
                obj = RuleNormalActionParams()
                obj._deserialize(item)
                self._Parameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NsVerification(AbstractModel):
    """Information required for switching DNS servers. It's applicable to sites connected via NSs.

    """

    def __init__(self):
        r"""
        :param _NameServers: The DNS server address assigned to the user when connecting a site to EO via NS. You need to switch the NameServer of the domain name to this address.
        :type NameServers: list of str
        """
        self._NameServers = None

    @property
    def NameServers(self):
        return self._NameServers

    @NameServers.setter
    def NameServers(self, NameServers):
        self._NameServers = NameServers


    def _deserialize(self, params):
        self._NameServers = params.get("NameServers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineCache(AbstractModel):
    """Offline cache feature status switch.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether offline cache is enabled. Valid values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Origin(AbstractModel):
    """The origin server configuration.

    """

    def __init__(self):
        r"""
        :param _Origins: Primary origin server list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Origins: list of str
        :param _BackupOrigins: The list of backup origin servers.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupOrigins: list of str
        :param _OriginPullProtocol: Origin-pull protocol configuration. Values:
<li>`http`: Force HTTP for origin-pull.</li>
<li>`follow`: Follow protocol.</li>
<li>`https`: Force HTTPS for origin-pull.</li>
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OriginPullProtocol: str
        :param _CosPrivateAccess: Whether to allow private access to buckets when `OriginType=cos`. Valid values: 
<li>`on`: Private access;</li>
<li>`off`: Public access.</li>
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CosPrivateAccess: str
        """
        self._Origins = None
        self._BackupOrigins = None
        self._OriginPullProtocol = None
        self._CosPrivateAccess = None

    @property
    def Origins(self):
        return self._Origins

    @Origins.setter
    def Origins(self, Origins):
        self._Origins = Origins

    @property
    def BackupOrigins(self):
        return self._BackupOrigins

    @BackupOrigins.setter
    def BackupOrigins(self, BackupOrigins):
        self._BackupOrigins = BackupOrigins

    @property
    def OriginPullProtocol(self):
        return self._OriginPullProtocol

    @OriginPullProtocol.setter
    def OriginPullProtocol(self, OriginPullProtocol):
        self._OriginPullProtocol = OriginPullProtocol

    @property
    def CosPrivateAccess(self):
        return self._CosPrivateAccess

    @CosPrivateAccess.setter
    def CosPrivateAccess(self, CosPrivateAccess):
        self._CosPrivateAccess = CosPrivateAccess


    def _deserialize(self, params):
        self._Origins = params.get("Origins")
        self._BackupOrigins = params.get("BackupOrigins")
        self._OriginPullProtocol = params.get("OriginPullProtocol")
        self._CosPrivateAccess = params.get("CosPrivateAccess")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginDetail(AbstractModel):
    """Details of the origin.

    """

    def __init__(self):
        r"""
        :param _OriginType: Origin server type. Valid values:
<li>IP_DOMAIN: IPv4, IPv6, or domain name type origin server;</li>
<li>COS: Tencent Cloud COS origin server;</li>
<li>AWS_S3: AWS S3 COS origin server;</li>
<li>ORIGIN_GROUP: origin server group;</li>
<li>VOD: Video on Demand;</li>
<li>SPACE: origin server uninstallation, currently only available to the allowlist;</li>
<li>LB: load balancing. Currently only available to the allowlist. </li>
        :type OriginType: str
        :param _Origin: Origin server address, which varies with the value of OriginType:
<li>When OriginType = IP_DOMAIN, this parameter is an IPv4 address, an IPv6 address, or a domain name.</li>
<li>When OriginType = COS, this parameter is the access domain name of the COS bucket.</li>
<li>When OriginType = AWS_S3, this parameter is the access domain name of the S3 bucket.</li>
<li>When OriginType = ORIGIN_GROUP, this parameter is the origin server group ID.</li>
<li>When OriginType = VOD, this parameter is the VOD application ID.</li>
        :type Origin: str
        :param _BackupOrigin: Secondary origin group ID. This parameter is valid only when OriginType is ORIGIN_GROUP and a secondary origin group is configured.
        :type BackupOrigin: str
        :param _OriginGroupName: Primary origin group name. This parameter returns a value when OriginType is ORIGIN_GROUP.
        :type OriginGroupName: str
        :param _BackOriginGroupName: Secondary origin group name. This parameter is valid only when OriginType is ORIGIN_GROUP and a secondary origin group is configured.
        :type BackOriginGroupName: str
        :param _PrivateAccess: Whether access to the private object storage origin server is allowed. This parameter is valid only when the origin server type OriginType is COS or AWS_S3. Valid values:
<li>on: Enable private authentication;</li>
<li>off: Disable private authentication. </li>
If this field is not specified, the default value 'off' will be used.
        :type PrivateAccess: str
        :param _PrivateParameters: Private authentication parameter. This parameter is valid only when PrivateAccess is on.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PrivateParameters: list of PrivateParameter
        :param _VodeoSubAppId: MO sub-application ID
        :type VodeoSubAppId: int
        :param _VodeoDistributionRange: MO distribution range. Valid values: <li>All: all</li> <li>Bucket: bucket</li>
        :type VodeoDistributionRange: str
        :param _VodeoBucketId: MO bucket ID, required when the distribution range (DistributionRange) is bucket (Bucket)
        :type VodeoBucketId: str
        """
        self._OriginType = None
        self._Origin = None
        self._BackupOrigin = None
        self._OriginGroupName = None
        self._BackOriginGroupName = None
        self._PrivateAccess = None
        self._PrivateParameters = None
        self._VodeoSubAppId = None
        self._VodeoDistributionRange = None
        self._VodeoBucketId = None

    @property
    def OriginType(self):
        return self._OriginType

    @OriginType.setter
    def OriginType(self, OriginType):
        self._OriginType = OriginType

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def BackupOrigin(self):
        return self._BackupOrigin

    @BackupOrigin.setter
    def BackupOrigin(self, BackupOrigin):
        self._BackupOrigin = BackupOrigin

    @property
    def OriginGroupName(self):
        return self._OriginGroupName

    @OriginGroupName.setter
    def OriginGroupName(self, OriginGroupName):
        self._OriginGroupName = OriginGroupName

    @property
    def BackOriginGroupName(self):
        return self._BackOriginGroupName

    @BackOriginGroupName.setter
    def BackOriginGroupName(self, BackOriginGroupName):
        self._BackOriginGroupName = BackOriginGroupName

    @property
    def PrivateAccess(self):
        return self._PrivateAccess

    @PrivateAccess.setter
    def PrivateAccess(self, PrivateAccess):
        self._PrivateAccess = PrivateAccess

    @property
    def PrivateParameters(self):
        return self._PrivateParameters

    @PrivateParameters.setter
    def PrivateParameters(self, PrivateParameters):
        self._PrivateParameters = PrivateParameters

    @property
    def VodeoSubAppId(self):
        warnings.warn("parameter `VodeoSubAppId` is deprecated", DeprecationWarning) 

        return self._VodeoSubAppId

    @VodeoSubAppId.setter
    def VodeoSubAppId(self, VodeoSubAppId):
        warnings.warn("parameter `VodeoSubAppId` is deprecated", DeprecationWarning) 

        self._VodeoSubAppId = VodeoSubAppId

    @property
    def VodeoDistributionRange(self):
        warnings.warn("parameter `VodeoDistributionRange` is deprecated", DeprecationWarning) 

        return self._VodeoDistributionRange

    @VodeoDistributionRange.setter
    def VodeoDistributionRange(self, VodeoDistributionRange):
        warnings.warn("parameter `VodeoDistributionRange` is deprecated", DeprecationWarning) 

        self._VodeoDistributionRange = VodeoDistributionRange

    @property
    def VodeoBucketId(self):
        warnings.warn("parameter `VodeoBucketId` is deprecated", DeprecationWarning) 

        return self._VodeoBucketId

    @VodeoBucketId.setter
    def VodeoBucketId(self, VodeoBucketId):
        warnings.warn("parameter `VodeoBucketId` is deprecated", DeprecationWarning) 

        self._VodeoBucketId = VodeoBucketId


    def _deserialize(self, params):
        self._OriginType = params.get("OriginType")
        self._Origin = params.get("Origin")
        self._BackupOrigin = params.get("BackupOrigin")
        self._OriginGroupName = params.get("OriginGroupName")
        self._BackOriginGroupName = params.get("BackOriginGroupName")
        self._PrivateAccess = params.get("PrivateAccess")
        if params.get("PrivateParameters") is not None:
            self._PrivateParameters = []
            for item in params.get("PrivateParameters"):
                obj = PrivateParameter()
                obj._deserialize(item)
                self._PrivateParameters.append(obj)
        self._VodeoSubAppId = params.get("VodeoSubAppId")
        self._VodeoDistributionRange = params.get("VodeoDistributionRange")
        self._VodeoBucketId = params.get("VodeoBucketId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginGroup(AbstractModel):
    """Origin group information.

    """

    def __init__(self):
        r"""
        :param _GroupId: The ID of the origin group.
        :type GroupId: str
        :param _Name: The name of the origin group.
        :type Name: str
        :param _Type: The origin group type. Values:
<li>`GENERAL`: General origin group</li>
<li>`HTTP`: HTTP-specific origin group</li>
        :type Type: str
        :param _Records: Details of the origin record.
        :type Records: list of OriginRecord
        :param _References: List of instances referencing this origin group.	
        :type References: list of OriginGroupReference
        :param _CreateTime: Creation time of the origin group.
        :type CreateTime: str
        :param _UpdateTime: The update time of the origin group.
        :type UpdateTime: str
        :param _HostHeader: Origin-pull host header
Note: This field may return·null, indicating that no valid values can be obtained.
        :type HostHeader: str
        """
        self._GroupId = None
        self._Name = None
        self._Type = None
        self._Records = None
        self._References = None
        self._CreateTime = None
        self._UpdateTime = None
        self._HostHeader = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Records(self):
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def References(self):
        return self._References

    @References.setter
    def References(self, References):
        self._References = References

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

    @property
    def HostHeader(self):
        return self._HostHeader

    @HostHeader.setter
    def HostHeader(self, HostHeader):
        self._HostHeader = HostHeader


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = OriginRecord()
                obj._deserialize(item)
                self._Records.append(obj)
        if params.get("References") is not None:
            self._References = []
            for item in params.get("References"):
                obj = OriginGroupReference()
                obj._deserialize(item)
                self._References.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._HostHeader = params.get("HostHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginGroupReference(AbstractModel):
    """Services referencing this origin group

    """

    def __init__(self):
        r"""
        :param _InstanceType: Services referencing the origin group. Values:
<li>`AccelerationDomain`: Acceleration domain name</li>
<li>`RuleEngine`: Rules engine</li>
<li>`Loadbalance`: Load balancer</li>
<li>`ApplicationProxy`: L4 proxy</li>
        :type InstanceType: str
        :param _InstanceId: ID of the instances referencing the origin group
        :type InstanceId: str
        :param _InstanceName: Name of the instance referencing the origin group
        :type InstanceName: str
        """
        self._InstanceType = None
        self._InstanceId = None
        self._InstanceName = None

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


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginInfo(AbstractModel):
    """Details of the origin.

    """

    def __init__(self):
        r"""
        :param _OriginType: Origin server type, with values:
<li>IP_DOMAIN: IPv4, IPv6, or domain name type origin server;</li>
<li>COS: Tencent Cloud COS origin server;</li>
<li>AWS_S3: AWS S3 origin server;</li>
<li>ORIGIN_GROUP: origin server group type origin server;</li>
 <li>VOD: Video on Demand;</li>
<li>SPACE: origin server uninstallation. Currently only available to the allowlist;</li>
<li>LB: load balancing. Currently only available to the allowlist. </li>
        :type OriginType: str
        :param _Origin: Origin server address, which varies according to the value of OriginType:
<li>When OriginType = IP_DOMAIN, fill in an IPv4 address, an IPv6 address, or a domain name;</li>
<li>When OriginType = COS, fill in the access domain name of the COS bucket;</li>
<li>When OriginType = AWS_S3, fill in the access domain name of the S3 bucket;</li>
<li>When OriginType = ORIGIN_GROUP, fill in the origin server group ID;</li>
<li>When OriginType = VOD, fill in the VOD application ID;</li>
<li>When OriginType = LB, fill in the Cloud Load Balancer instance ID. This feature is currently only available to the allowlist;</li>
<li>When OriginType = SPACE, fill in the origin server uninstallation space ID. This feature is currently only available to the allowlist.</li>
        :type Origin: str
        :param _BackupOrigin: The ID of the secondary origin group. This parameter is valid only when OriginType is ORIGIN_GROUP. This field indicates the old version capability, which cannot be configured or modified on the control panel after being called. Please submit a ticket if required.
        :type BackupOrigin: str
        :param _PrivateAccess: Whether access to the private Cloud Object Storage origin server is allowed. This parameter is valid only when OriginType is COS or AWS_S3. Valid values:
<li>on: Enable private authentication;</li>
<li>off: Disable private authentication.</li>
If it is not specified, the default value is off.
        :type PrivateAccess: str
        :param _PrivateParameters: Private authentication parameter. This parameter is valid only when PrivateAccess is on.
        :type PrivateParameters: list of PrivateParameter
        :param _VodeoSubAppId: VODEO sub-application ID. This parameter is required when OriginType is VODEO.
        :type VodeoSubAppId: int
        :param _VodeoDistributionRange: VOD on EO distribution range. This parameter is required when OriginType = VODEO. The values are: 
<li>All: all buckets under the current application;</li> 
<li>Bucket: a specified bucket.</li>
        :type VodeoDistributionRange: str
        :param _VodeoBucketId: VODEO storage bucket ID. This parameter is required when OriginType is VODEO and VodeoDistributionRange is Bucket.
        :type VodeoBucketId: str
        """
        self._OriginType = None
        self._Origin = None
        self._BackupOrigin = None
        self._PrivateAccess = None
        self._PrivateParameters = None
        self._VodeoSubAppId = None
        self._VodeoDistributionRange = None
        self._VodeoBucketId = None

    @property
    def OriginType(self):
        return self._OriginType

    @OriginType.setter
    def OriginType(self, OriginType):
        self._OriginType = OriginType

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def BackupOrigin(self):
        return self._BackupOrigin

    @BackupOrigin.setter
    def BackupOrigin(self, BackupOrigin):
        self._BackupOrigin = BackupOrigin

    @property
    def PrivateAccess(self):
        return self._PrivateAccess

    @PrivateAccess.setter
    def PrivateAccess(self, PrivateAccess):
        self._PrivateAccess = PrivateAccess

    @property
    def PrivateParameters(self):
        return self._PrivateParameters

    @PrivateParameters.setter
    def PrivateParameters(self, PrivateParameters):
        self._PrivateParameters = PrivateParameters

    @property
    def VodeoSubAppId(self):
        warnings.warn("parameter `VodeoSubAppId` is deprecated", DeprecationWarning) 

        return self._VodeoSubAppId

    @VodeoSubAppId.setter
    def VodeoSubAppId(self, VodeoSubAppId):
        warnings.warn("parameter `VodeoSubAppId` is deprecated", DeprecationWarning) 

        self._VodeoSubAppId = VodeoSubAppId

    @property
    def VodeoDistributionRange(self):
        warnings.warn("parameter `VodeoDistributionRange` is deprecated", DeprecationWarning) 

        return self._VodeoDistributionRange

    @VodeoDistributionRange.setter
    def VodeoDistributionRange(self, VodeoDistributionRange):
        warnings.warn("parameter `VodeoDistributionRange` is deprecated", DeprecationWarning) 

        self._VodeoDistributionRange = VodeoDistributionRange

    @property
    def VodeoBucketId(self):
        warnings.warn("parameter `VodeoBucketId` is deprecated", DeprecationWarning) 

        return self._VodeoBucketId

    @VodeoBucketId.setter
    def VodeoBucketId(self, VodeoBucketId):
        warnings.warn("parameter `VodeoBucketId` is deprecated", DeprecationWarning) 

        self._VodeoBucketId = VodeoBucketId


    def _deserialize(self, params):
        self._OriginType = params.get("OriginType")
        self._Origin = params.get("Origin")
        self._BackupOrigin = params.get("BackupOrigin")
        self._PrivateAccess = params.get("PrivateAccess")
        if params.get("PrivateParameters") is not None:
            self._PrivateParameters = []
            for item in params.get("PrivateParameters"):
                obj = PrivateParameter()
                obj._deserialize(item)
                self._PrivateParameters.append(obj)
        self._VodeoSubAppId = params.get("VodeoSubAppId")
        self._VodeoDistributionRange = params.get("VodeoDistributionRange")
        self._VodeoBucketId = params.get("VodeoBucketId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginProtectionInfo(AbstractModel):
    """Origin protection configuration

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site.
        :type ZoneId: str
        :param _Hosts: List of domain names.
        :type Hosts: list of str
        :param _ProxyIds: List of proxy IDs.
        :type ProxyIds: list of str
        :param _CurrentIPWhitelist: The existing intermediate IPs.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CurrentIPWhitelist: :class:`tencentcloud.teo.v20220901.models.IPWhitelist`
        :param _NeedUpdate: Whether the intermediate IP update is needed for the site. Values:
<li>`true`: Update needed;</li>
<li>`false`: Update not needed.</li>
        :type NeedUpdate: bool
        :param _Status: Status of the origin protection configuration. Values:
<li>`online`: Origin protection is activated;</li>
<li>`offline`: Origin protection is disabled.</li>
<li>`nonactivate`: Origin protection is not activated. This value is returned only when the feature is not activated before it’s used.</li>
        :type Status: str
        :param _PlanSupport: Whether origin protection is supported in the plan. Values:
<li>`true`: Origin protection supported;</li>
<li>`false`: Origin protection not supported.</li>
        :type PlanSupport: bool
        :param _DiffIPWhitelist: Differences between the latest and existing intermediate IPs.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DiffIPWhitelist: :class:`tencentcloud.teo.v20220901.models.DiffIPWhitelist`
        """
        self._ZoneId = None
        self._Hosts = None
        self._ProxyIds = None
        self._CurrentIPWhitelist = None
        self._NeedUpdate = None
        self._Status = None
        self._PlanSupport = None
        self._DiffIPWhitelist = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Hosts(self):
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts

    @property
    def ProxyIds(self):
        return self._ProxyIds

    @ProxyIds.setter
    def ProxyIds(self, ProxyIds):
        self._ProxyIds = ProxyIds

    @property
    def CurrentIPWhitelist(self):
        return self._CurrentIPWhitelist

    @CurrentIPWhitelist.setter
    def CurrentIPWhitelist(self, CurrentIPWhitelist):
        self._CurrentIPWhitelist = CurrentIPWhitelist

    @property
    def NeedUpdate(self):
        return self._NeedUpdate

    @NeedUpdate.setter
    def NeedUpdate(self, NeedUpdate):
        self._NeedUpdate = NeedUpdate

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PlanSupport(self):
        return self._PlanSupport

    @PlanSupport.setter
    def PlanSupport(self, PlanSupport):
        self._PlanSupport = PlanSupport

    @property
    def DiffIPWhitelist(self):
        return self._DiffIPWhitelist

    @DiffIPWhitelist.setter
    def DiffIPWhitelist(self, DiffIPWhitelist):
        self._DiffIPWhitelist = DiffIPWhitelist


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Hosts = params.get("Hosts")
        self._ProxyIds = params.get("ProxyIds")
        if params.get("CurrentIPWhitelist") is not None:
            self._CurrentIPWhitelist = IPWhitelist()
            self._CurrentIPWhitelist._deserialize(params.get("CurrentIPWhitelist"))
        self._NeedUpdate = params.get("NeedUpdate")
        self._Status = params.get("Status")
        self._PlanSupport = params.get("PlanSupport")
        if params.get("DiffIPWhitelist") is not None:
            self._DiffIPWhitelist = DiffIPWhitelist()
            self._DiffIPWhitelist._deserialize(params.get("DiffIPWhitelist"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginRecord(AbstractModel):
    """Origin group record

    """

    def __init__(self):
        r"""
        :param _Record: The origin record value, which can be an IPv4/IPv6 address or a domain name.
        :type Record: str
        :param _Type: The origin type. Values:
<li>`IP_DOMAIN`: IPv4/IPv6 address or domain name</li>
<li>`COS`: COS bucket address</li>
<li>`AWS_S3`: AWS S3 bucket address
        :type Type: str
        :param _RecordId: The origin record ID.
        :type RecordId: str
        :param _Weight: Weight of an origin. Range: 0-100. If it is not specified, a random weight is assigned. If `0` is passed in, there is no traffic scheduled to this origin.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Weight: int
        :param _Private: Whether to enable private authentication. It is valid when `OriginType=COS/AWS_S3`. Values:
<li>`true`: Yes.</li>
<li>`false`: No.</li>Default: `false`.

        :type Private: bool
        :param _PrivateParameters: Private authentication parameters. This field is valid when `Private=true`.
        :type PrivateParameters: list of PrivateParameter
        """
        self._Record = None
        self._Type = None
        self._RecordId = None
        self._Weight = None
        self._Private = None
        self._PrivateParameters = None

    @property
    def Record(self):
        return self._Record

    @Record.setter
    def Record(self, Record):
        self._Record = Record

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Private(self):
        return self._Private

    @Private.setter
    def Private(self, Private):
        self._Private = Private

    @property
    def PrivateParameters(self):
        return self._PrivateParameters

    @PrivateParameters.setter
    def PrivateParameters(self, PrivateParameters):
        self._PrivateParameters = PrivateParameters


    def _deserialize(self, params):
        self._Record = params.get("Record")
        self._Type = params.get("Type")
        self._RecordId = params.get("RecordId")
        self._Weight = params.get("Weight")
        self._Private = params.get("Private")
        if params.get("PrivateParameters") is not None:
            self._PrivateParameters = []
            for item in params.get("PrivateParameters"):
                obj = PrivateParameter()
                obj._deserialize(item)
                self._PrivateParameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OwnershipVerification(AbstractModel):
    """Information of domain name ownership verification.

    """

    def __init__(self):
        r"""
        :param _DnsVerification: u200cInformation required for authentication using DNS resolution. It's applicable to sites connected via CNAME. See [Ownership Verification](https://intl.cloud.tencent.com/document/product/1552/70789?from_cn_redirect=1#7af6ecf8-afca-4e35-8811-b5797ed1bde5).
 
Note: This field may return·null, indicating that no valid values can be obtained.
        :type DnsVerification: :class:`tencentcloud.teo.v20220901.models.DnsVerification`
        :param _FileVerification: u200cInformation required for verifying via a file. It's applicable to sites connected via CNAMEs. See [Ownership Verification](https://intl.cloud.tencent.com/document/product/1552/70789?from_cn_redirect=1#7af6ecf8-afca-4e35-8811-b5797ed1bde5).
 
Note: This field may return·null, indicating that no valid values can be obtained.
        :type FileVerification: :class:`tencentcloud.teo.v20220901.models.FileVerification`
        :param _NsVerification: u200cInformation required for switching DNS servers. It's applicable to sites connected via NSs. For details, see [Modifying DNS Server](https://intl.cloud.tencent.com/document/product/1552/90452?from_cn_redirect=1).
Note: This field may return·null, indicating that no valid values can be obtained.
        :type NsVerification: :class:`tencentcloud.teo.v20220901.models.NsVerification`
        """
        self._DnsVerification = None
        self._FileVerification = None
        self._NsVerification = None

    @property
    def DnsVerification(self):
        return self._DnsVerification

    @DnsVerification.setter
    def DnsVerification(self, DnsVerification):
        self._DnsVerification = DnsVerification

    @property
    def FileVerification(self):
        return self._FileVerification

    @FileVerification.setter
    def FileVerification(self, FileVerification):
        self._FileVerification = FileVerification

    @property
    def NsVerification(self):
        return self._NsVerification

    @NsVerification.setter
    def NsVerification(self, NsVerification):
        self._NsVerification = NsVerification


    def _deserialize(self, params):
        if params.get("DnsVerification") is not None:
            self._DnsVerification = DnsVerification()
            self._DnsVerification._deserialize(params.get("DnsVerification"))
        if params.get("FileVerification") is not None:
            self._FileVerification = FileVerification()
            self._FileVerification._deserialize(params.get("FileVerification"))
        if params.get("NsVerification") is not None:
            self._NsVerification = NsVerification()
            self._NsVerification._deserialize(params.get("NsVerification"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PartialModule(AbstractModel):
    """Module settings of the exception rule

    """

    def __init__(self):
        r"""
        :param _Module: The module. Values:
<li>`waf`: Managed rules</li>
        :type Module: str
        :param _Include: List of managed rule IDs to be skipped.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Include: list of int
        """
        self._Module = None
        self._Include = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Include(self):
        return self._Include

    @Include.setter
    def Include(self, Include):
        self._Include = Include


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Include = params.get("Include")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlanInfo(AbstractModel):
    """EdgeOne plan information

    """

    def __init__(self):
        r"""
        :param _Currency: Settlement currency. Values:
<li>`CNY`: Settled by Chinese RMB;</li>
<li>`USD`: Settled by US dollars.</li>
        :type Currency: str
        :param _Flux: Traffic quota of the plan. It includes the traffic for security acceleration, content acceleration and smart acceleration. Unit: byte.
        :type Flux: int
        :param _Frequency: Settlement cycle. Values:
<li>`y`: Settled by year;</li>
<li>`m`: Settled by month;</li>
<li>`h`: Settled by hour;</li>
<li>`M`: Settled by minute;</li>
<li>`s`: Settled by second.</li>
        :type Frequency: str
        :param _PlanType: The plan option. Values:
<li>`sta`: Standard plan that supports content delivery network outside the Chinese mainland.</li>
<li>`sta_with_bot`: Standard plan that supports content delivery network outside the Chinese mainland and bot management.</li>
<li>`sta_cm`: Standard plan that supports content delivery network inside the Chinese mainland.</li>
<li>`sta_cm_with_bot`: Standard plan that supports content delivery network inside the Chinese mainland and bot management.</li>
<li>`sta`: Standard plan that supports content delivery network over the globe.</li>
<li>`sta_global_with_bot`: Standard plan that supports content delivery network over the globe and bot management.</li>
<li>`ent`: Enterprise plan that supports content delivery network outside the Chinese mainland.</li>
<li>`ent_with_bot`: Enterprise plan that supports content delivery network outside the Chinese mainland and bot management.</li>
<li>`ent_cm`: Enterprise plan that supports content delivery network inside the Chinese mainland.</li>
<li>`ent_cm_with_bot`: Enterprise plan that supports content delivery network inside the Chinese mainland and bot management.</li>
<li>`ent_global`: Enterprise plan that supports content delivery network over the globe.</li>
<li>`ent_global_with_bot`: Enterprise plan that supports content delivery network over the globe and bot management.</li>
        :type PlanType: str
        :param _Price: Plan price (in CNY fen/US cent). The price unit depends on the settlement currency.
        :type Price: float
        :param _Request: Quota on security acceleration requests
        :type Request: int
        :param _SiteNumber: Number of sites to be bound to the plan
        :type SiteNumber: int
        :param _Area: The acceleration region. Values:
<li>`mainland`: Chinese mainland</li>
<li>`overseas`: Global (Chinese mainland not included)</li>
<li>`global`: Global (Chinese mainland included)</li>
        :type Area: str
        """
        self._Currency = None
        self._Flux = None
        self._Frequency = None
        self._PlanType = None
        self._Price = None
        self._Request = None
        self._SiteNumber = None
        self._Area = None

    @property
    def Currency(self):
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def Flux(self):
        return self._Flux

    @Flux.setter
    def Flux(self, Flux):
        self._Flux = Flux

    @property
    def Frequency(self):
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency

    @property
    def PlanType(self):
        return self._PlanType

    @PlanType.setter
    def PlanType(self, PlanType):
        self._PlanType = PlanType

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def Request(self):
        return self._Request

    @Request.setter
    def Request(self, Request):
        self._Request = Request

    @property
    def SiteNumber(self):
        return self._SiteNumber

    @SiteNumber.setter
    def SiteNumber(self, SiteNumber):
        self._SiteNumber = SiteNumber

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._Currency = params.get("Currency")
        self._Flux = params.get("Flux")
        self._Frequency = params.get("Frequency")
        self._PlanType = params.get("PlanType")
        self._Price = params.get("Price")
        self._Request = params.get("Request")
        self._SiteNumber = params.get("SiteNumber")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PostMaxSize(AbstractModel):
    """Maximum size of the file uploaded for streaming via a POST request

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable POST upload limit (default limit: 32 MB). Valid values: 
<li>`on`: Enable;</li>
<li>`off`: Disable.</li>
        :type Switch: str
        :param _MaxSize: Maximum size. Value range: 1-500 MB.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxSize: int
        """
        self._Switch = None
        self._MaxSize = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrepaidPlanParam(AbstractModel):
    """Prepaid Plan Billing Parameters

    """

    def __init__(self):
        r"""
        :param _Period: Prepaid plan duration, unit: month. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36.

If this field is not specified, the default value '1' will be used.
        :type Period: int
        :param _RenewFlag: The auto-renewal flag for prepaid plan has the following values:
<li> on: Enable auto-renewal;</li>
<li> off: Disable auto-renewal. </li>
If this field is not specified, the default value 'off' will be used. When auto-renewal is enabled, it defaults to renewing for one month.
        :type RenewFlag: str
        """
        self._Period = None
        self._RenewFlag = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
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
        


class PrivateParameter(AbstractModel):
    """Private authentication parameters for Cloud Object Storage origin server

    """

    def __init__(self):
        r"""
        :param _Name: The name of the private authentication parameter. Valid values:
<li>AccessKeyId: Access Key ID for authentication;</li>
<li>SecretAccessKey: Secret Access Key for authentication;</li>
<li>SignatureVersion: Authentication version, v2 or v4;</li>
<li>Region: The region of the storage bucket.</li>
        :type Name: str
        :param _Value: The parameter value.
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCondition(AbstractModel):
    """The query condition

    """

    def __init__(self):
        r"""
        :param _Key: The key of QueryCondition.
        :type Key: str
        :param _Operator: The conditional operator. Values:
<li>`equals`: Equals</li>
<li>`notEquals`: Does not equal</li>
<li>`include`: Contains</li>
<li>`notInclude`: Does not contain</li>
<li>`startWith`: Starts with</li>
<li>`notStartWith`: Does not start with</li>
<li>`endWith`: Ends with</li>
<li>`notEndWith`: Does not end with</li>
        :type Operator: str
        :param _Value: The value of QueryCondition.
        :type Value: list of str
        """
        self._Key = None
        self._Operator = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Operator = params.get("Operator")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryString(AbstractModel):
    """Request parameter contained in `CacheKey`

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to use `QueryString` as part of `CacheKey`. Values:
<li>`on`: Yes</li>
<li>`off`: No</li>
        :type Switch: str
        :param _Action: Specifies how to use query strings in the cache key. Values:
<li>`includeCustom`: `Include partial query strings.</li>
<li>`excludeCustom`: Exclude partial query strings.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Action: str
        :param _Value: Array of query strings used/excluded
Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: list of str
        """
        self._Switch = None
        self._Action = None
        self._Value = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Action = params.get("Action")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Quic(AbstractModel):
    """QUIC configuration item

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable QUIC. Valid values: 
<li>`on`: Enable;</li>
<li>`off`: Disable.</li>
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Quota(AbstractModel):
    """Purging/Pre-warming available usage and quota

    """

    def __init__(self):
        r"""
        :param _Batch: 
        :type Batch: int
        :param _Daily: Daily submission quota limit.
        :type Daily: int
        :param _DailyAvailable: Remaining daily submission quota.
        :type DailyAvailable: int
        :param _Type: Type of cache purging/pre-warming. Values:
<li>`purge_prefix`: Purge by prefix</li>
<li>`purge_url`: Purge by URL</li>
<li>`purge_host`: Purge by hostname</li>
<li>`purge_all`: Purge all caches</li>
<li>`purge_cache_tag`: Purge by cache tag</li><li>`prefetch_url`: Pre-warm by URL</li>
        :type Type: str
        """
        self._Batch = None
        self._Daily = None
        self._DailyAvailable = None
        self._Type = None

    @property
    def Batch(self):
        return self._Batch

    @Batch.setter
    def Batch(self, Batch):
        self._Batch = Batch

    @property
    def Daily(self):
        return self._Daily

    @Daily.setter
    def Daily(self, Daily):
        self._Daily = Daily

    @property
    def DailyAvailable(self):
        return self._DailyAvailable

    @DailyAvailable.setter
    def DailyAvailable(self, DailyAvailable):
        self._DailyAvailable = DailyAvailable

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Batch = params.get("Batch")
        self._Daily = params.get("Daily")
        self._DailyAvailable = params.get("DailyAvailable")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitConfig(AbstractModel):
    """Rate limiting rules

    """

    def __init__(self):
        r"""
        :param _Switch: Switch. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param _RateLimitUserRules: The settings of the custom rate limiting rule. If it is null, the settings that were last configured will be used.
        :type RateLimitUserRules: list of RateLimitUserRule
        :param _RateLimitTemplate: The settings of the rate limiting template. If it is null, the settings that were last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RateLimitTemplate: :class:`tencentcloud.teo.v20220901.models.RateLimitTemplate`
        :param _RateLimitIntelligence: The client filtering settings. If it is null, the settings that were last configured will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RateLimitIntelligence: :class:`tencentcloud.teo.v20220901.models.RateLimitIntelligence`
        :param _RateLimitCustomizes: The custom rate limiting rules. If it is `null`, the previous settings is used.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RateLimitCustomizes: list of RateLimitUserRule
        """
        self._Switch = None
        self._RateLimitUserRules = None
        self._RateLimitTemplate = None
        self._RateLimitIntelligence = None
        self._RateLimitCustomizes = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def RateLimitUserRules(self):
        return self._RateLimitUserRules

    @RateLimitUserRules.setter
    def RateLimitUserRules(self, RateLimitUserRules):
        self._RateLimitUserRules = RateLimitUserRules

    @property
    def RateLimitTemplate(self):
        return self._RateLimitTemplate

    @RateLimitTemplate.setter
    def RateLimitTemplate(self, RateLimitTemplate):
        self._RateLimitTemplate = RateLimitTemplate

    @property
    def RateLimitIntelligence(self):
        return self._RateLimitIntelligence

    @RateLimitIntelligence.setter
    def RateLimitIntelligence(self, RateLimitIntelligence):
        self._RateLimitIntelligence = RateLimitIntelligence

    @property
    def RateLimitCustomizes(self):
        return self._RateLimitCustomizes

    @RateLimitCustomizes.setter
    def RateLimitCustomizes(self, RateLimitCustomizes):
        self._RateLimitCustomizes = RateLimitCustomizes


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("RateLimitUserRules") is not None:
            self._RateLimitUserRules = []
            for item in params.get("RateLimitUserRules"):
                obj = RateLimitUserRule()
                obj._deserialize(item)
                self._RateLimitUserRules.append(obj)
        if params.get("RateLimitTemplate") is not None:
            self._RateLimitTemplate = RateLimitTemplate()
            self._RateLimitTemplate._deserialize(params.get("RateLimitTemplate"))
        if params.get("RateLimitIntelligence") is not None:
            self._RateLimitIntelligence = RateLimitIntelligence()
            self._RateLimitIntelligence._deserialize(params.get("RateLimitIntelligence"))
        if params.get("RateLimitCustomizes") is not None:
            self._RateLimitCustomizes = []
            for item in params.get("RateLimitCustomizes"):
                obj = RateLimitUserRule()
                obj._deserialize(item)
                self._RateLimitCustomizes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitIntelligence(AbstractModel):
    """Client filtering

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable configuration. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param _Action: Action to be executed. Values:
<li>`monitor`: Observe</li>
<li>`alg`: Challenge</li>
        :type Action: str
        :param _RuleId: The rule ID, which is only used as a response parameter.
        :type RuleId: int
        """
        self._Switch = None
        self._Action = None
        self._RuleId = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Action = params.get("Action")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitTemplate(AbstractModel):
    """Rate limit template

    """

    def __init__(self):
        r"""
        :param _Mode: The mode. Values:
<li>`sup_loose`: Super loose</li>
<li>`loose`: Loose</li>
<li>`emergency`: Emergency</li>
<li>`normal`: Moderate</li>
<li>`strict`: Strict</li>
<li>`close`: Off</li>
        :type Mode: str
        :param _Action: The action. Values:
<li>`alg`: JavaScript challenge</li>
<li>`monitor`: Observe</li>If it is left empty, the default value `alg` is used.
        :type Action: str
        :param _RateLimitTemplateDetail: The settings of the rate limiting template. It is only used as an output parameter.
        :type RateLimitTemplateDetail: :class:`tencentcloud.teo.v20220901.models.RateLimitTemplateDetail`
        """
        self._Mode = None
        self._Action = None
        self._RateLimitTemplateDetail = None

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RateLimitTemplateDetail(self):
        return self._RateLimitTemplateDetail

    @RateLimitTemplateDetail.setter
    def RateLimitTemplateDetail(self, RateLimitTemplateDetail):
        self._RateLimitTemplateDetail = RateLimitTemplateDetail


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._Action = params.get("Action")
        if params.get("RateLimitTemplateDetail") is not None:
            self._RateLimitTemplateDetail = RateLimitTemplateDetail()
            self._RateLimitTemplateDetail._deserialize(params.get("RateLimitTemplateDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitTemplateDetail(AbstractModel):
    """The settings of the rate limiting template

    """

    def __init__(self):
        r"""
        :param _Mode: Template level name. Valid values:
<li>sup_loose: super loose;</li>
<li>loose: loose;</li>
<li>emergency: emergency;</li>
<li>normal: normal;</li>
<li>strict: strict;</li>
<li>close: disabled, effective only for precise rate limiting.</li>
Note: This field may return null, which indicates a failure to obtain a valid value.
        :type Mode: str
        :param _ID: Unique ID.
        :type ID: int
        :param _Action: Template action. Valid values:
<li>alg: JavaScript challenge;</li>
<li>monitor: observation.</li>
Note: This field may return null, which indicates a failure to obtain a valid value.
        :type Action: str
        :param _PunishTime: Penalty duration, in seconds. Value range: 0-2 days.
Note: This field may return null, which indicates a failure to obtain a valid value.
        :type PunishTime: int
        :param _Threshold: Statistical threshold, in times. Value range: 0-4294967294.
        :type Threshold: int
        :param _Period: Statistical cycle. Value range: 0-120 seconds.
        :type Period: int
        """
        self._Mode = None
        self._ID = None
        self._Action = None
        self._PunishTime = None
        self._Threshold = None
        self._Period = None

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def PunishTime(self):
        return self._PunishTime

    @PunishTime.setter
    def PunishTime(self, PunishTime):
        self._PunishTime = PunishTime

    @property
    def Threshold(self):
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._ID = params.get("ID")
        self._Action = params.get("Action")
        self._PunishTime = params.get("PunishTime")
        self._Threshold = params.get("Threshold")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitUserRule(AbstractModel):
    """Rate limit rule

    """

    def __init__(self):
        r"""
        :param _Threshold: The request threshold. Value range: 0-4294967294.
        :type Threshold: int
        :param _Period: The statistical period. The value can be 10, 20, 30, 40, 50, or 60 seconds.
        :type Period: int
        :param _RuleName: The rule name, which consists of only letters, digits, and underscores and cannot start with an underscore.
        :type RuleName: str
        :param _Action: Action. Values:<li>`monitor`: Observe;</li><li>`drop`: Block;</li><li>`redirect`: Redirect;</li><li>`page`: Return a specific page;</li><li>`alg`: JavaScript challenge. </li>	
        :type Action: str
        :param _PunishTime: The amount of time taken to perform the action. Value range: 0 seconds - 2 days.
        :type PunishTime: int
        :param _PunishTimeUnit: The time unit. Values:
<li>`second`: Second</li>
<li>`minutes`: Minute</li>
<li>`hour`: Hour</li>
        :type PunishTimeUnit: str
        :param _RuleStatus: The rule status. Values:
<li>`on`: Enabled</li>
<li>`off`: Disabled</li>Default value: `on`
        :type RuleStatus: str
        :param _AclConditions: The rule details.
        :type AclConditions: list of AclCondition
        :param _RulePriority: The rule weight. Value range: 0-100.
        :type RulePriority: int
        :param _RuleID: Rule ID, which is only used as an output parameter.
        :type RuleID: int
        :param _FreqFields: The filter. Values:
<li>`sip`: Client IP</li>
This parameter is left empty by default.
        :type FreqFields: list of str
        :param _UpdateTime: Update time. It is only used as a response parameter, and defaults to the current time. 
        :type UpdateTime: str
        :param _FreqScope: Query scope. Values:
<li>`source_to_eo`: (Response) Traffic going from the origin to EdgeOne.</li>
<li>`client_to_eo`: (Request) Traffic going from the client to EdgeOne.</li>
Default: `source_to_eo`.
        :type FreqScope: list of str
        :param _Name: Name of the custom return page. It's required when `Action=page`.
        :type Name: str
        :param _CustomResponseId: ID of custom response. The ID can be obtained via the `DescribeCustomErrorPages` API. It's required when `Action=page`.	
        :type CustomResponseId: str
        :param _ResponseCode: The response code to trigger the return page. It's required when `Action=page`. Value: 100-600. 3xx response codes are not supported. Default value: 567.
        :type ResponseCode: int
        :param _RedirectUrl: The redirection URL. It's required when `Action=redirect`.
        :type RedirectUrl: str
        """
        self._Threshold = None
        self._Period = None
        self._RuleName = None
        self._Action = None
        self._PunishTime = None
        self._PunishTimeUnit = None
        self._RuleStatus = None
        self._AclConditions = None
        self._RulePriority = None
        self._RuleID = None
        self._FreqFields = None
        self._UpdateTime = None
        self._FreqScope = None
        self._Name = None
        self._CustomResponseId = None
        self._ResponseCode = None
        self._RedirectUrl = None

    @property
    def Threshold(self):
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def PunishTime(self):
        return self._PunishTime

    @PunishTime.setter
    def PunishTime(self, PunishTime):
        self._PunishTime = PunishTime

    @property
    def PunishTimeUnit(self):
        return self._PunishTimeUnit

    @PunishTimeUnit.setter
    def PunishTimeUnit(self, PunishTimeUnit):
        self._PunishTimeUnit = PunishTimeUnit

    @property
    def RuleStatus(self):
        return self._RuleStatus

    @RuleStatus.setter
    def RuleStatus(self, RuleStatus):
        self._RuleStatus = RuleStatus

    @property
    def AclConditions(self):
        return self._AclConditions

    @AclConditions.setter
    def AclConditions(self, AclConditions):
        self._AclConditions = AclConditions

    @property
    def RulePriority(self):
        return self._RulePriority

    @RulePriority.setter
    def RulePriority(self, RulePriority):
        self._RulePriority = RulePriority

    @property
    def RuleID(self):
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def FreqFields(self):
        return self._FreqFields

    @FreqFields.setter
    def FreqFields(self, FreqFields):
        self._FreqFields = FreqFields

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def FreqScope(self):
        return self._FreqScope

    @FreqScope.setter
    def FreqScope(self, FreqScope):
        self._FreqScope = FreqScope

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CustomResponseId(self):
        return self._CustomResponseId

    @CustomResponseId.setter
    def CustomResponseId(self, CustomResponseId):
        self._CustomResponseId = CustomResponseId

    @property
    def ResponseCode(self):
        return self._ResponseCode

    @ResponseCode.setter
    def ResponseCode(self, ResponseCode):
        self._ResponseCode = ResponseCode

    @property
    def RedirectUrl(self):
        return self._RedirectUrl

    @RedirectUrl.setter
    def RedirectUrl(self, RedirectUrl):
        self._RedirectUrl = RedirectUrl


    def _deserialize(self, params):
        self._Threshold = params.get("Threshold")
        self._Period = params.get("Period")
        self._RuleName = params.get("RuleName")
        self._Action = params.get("Action")
        self._PunishTime = params.get("PunishTime")
        self._PunishTimeUnit = params.get("PunishTimeUnit")
        self._RuleStatus = params.get("RuleStatus")
        if params.get("AclConditions") is not None:
            self._AclConditions = []
            for item in params.get("AclConditions"):
                obj = AclCondition()
                obj._deserialize(item)
                self._AclConditions.append(obj)
        self._RulePriority = params.get("RulePriority")
        self._RuleID = params.get("RuleID")
        self._FreqFields = params.get("FreqFields")
        self._UpdateTime = params.get("UpdateTime")
        self._FreqScope = params.get("FreqScope")
        self._Name = params.get("Name")
        self._CustomResponseId = params.get("CustomResponseId")
        self._ResponseCode = params.get("ResponseCode")
        self._RedirectUrl = params.get("RedirectUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RealtimeLogDeliveryTask(AbstractModel):
    """Real-time log delivery task

    """

    def __init__(self):
        r"""
        :param _TaskId: ID of a real-time log shipping task.
        :type TaskId: str
        :param _TaskName: Name of a real-time log shipping task.
        :type TaskName: str
        :param _DeliveryStatus: Status of a real-time log shipping task. Valid values: <li>enabled: enabled;</li><li>disabled: disabled;</li><li>deleted: deleted abnormally. Check whether the destination log set/log topic of Tencent Cloud CLS has been deleted.</li>
        :type DeliveryStatus: str
        :param _TaskType: Type of a real-time log shipping task. Valid values:<li>cls: push to Tencent Cloud CLS;</li><li>custom_endpoint: push to a custom HTTP(S) address;</li><li>s3: push to an AWS S3-compatible bucket address.</li>
        :type TaskType: str
        :param _EntityList: List of entities (L7 domain names or L4 proxy instances) corresponding to a real-time log shipping task. Valid value examples: <li>L7 domain name: domain.example.com;</li><li>L4 proxy instance: sid-2s69eb5wcms7.</li>	
        :type EntityList: list of str
        :param _LogType: Data shipping type. Valid values: <li>domain: site acceleration logs;</li><li>application: L4 proxy logs;</li><li>web-rateLiming: rate limiting and CC attack defense logs;</li><li>web-attack: managed rule logs;</li><li>web-rule: custom rule logs;</li><li>web-bot: Bot management logs.</li>
        :type LogType: str
        :param _Area: Data shipping area. Valid values:<li>mainland: within the Chinese mainland;</li><li>overseas: global (excluding the Chinese mainland).</li>
        :type Area: str
        :param _Fields: List of predefined fields for shipping.
        :type Fields: list of str
        :param _CustomFields: List of custom fields for shipping.
        :type CustomFields: list of CustomField
        :param _DeliveryConditions: Filter criteria of log shipping.
        :type DeliveryConditions: list of DeliveryCondition
        :param _Sample: Sampling ratio in permille. Value range: 1-1000. For example, 605 indicates a sampling ratio of 60.5%.
        :type Sample: int
        :param _LogFormat: Output format for log delivery. When the output parameter is null, the default format is used, which works as follows:
<li>When TaskType is 'custom_endpoint', the default format is an array of JSON objects, with each JSON object representing a log entry;</li>
<li>When TaskType is 's3', the default format is JSON Lines. </li>
Note: This field may return 'null', which indicates a failure to obtain a valid value.
        :type LogFormat: :class:`tencentcloud.teo.v20220901.models.LogFormat`
        :param _CLS: Configuration information of the CLS.
Note: This field may return null, which indicates a failure to obtain a valid value.
        :type CLS: :class:`tencentcloud.teo.v20220901.models.CLSTopic`
        :param _CustomEndpoint: Configuration information of the custom HTTP service.
Note: This field may return null, which indicates a failure to obtain a valid value.
        :type CustomEndpoint: :class:`tencentcloud.teo.v20220901.models.CustomEndpoint`
        :param _S3: Configuration information of the AWS S3-compatible bucket.
Note: This field may return null, which indicates a failure to obtain a valid value.
        :type S3: :class:`tencentcloud.teo.v20220901.models.S3`
        :param _CreateTime: Creation time.
        :type CreateTime: str
        :param _UpdateTime: Update time.
        :type UpdateTime: str
        """
        self._TaskId = None
        self._TaskName = None
        self._DeliveryStatus = None
        self._TaskType = None
        self._EntityList = None
        self._LogType = None
        self._Area = None
        self._Fields = None
        self._CustomFields = None
        self._DeliveryConditions = None
        self._Sample = None
        self._LogFormat = None
        self._CLS = None
        self._CustomEndpoint = None
        self._S3 = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def DeliveryStatus(self):
        return self._DeliveryStatus

    @DeliveryStatus.setter
    def DeliveryStatus(self, DeliveryStatus):
        self._DeliveryStatus = DeliveryStatus

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def EntityList(self):
        return self._EntityList

    @EntityList.setter
    def EntityList(self, EntityList):
        self._EntityList = EntityList

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Fields(self):
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields

    @property
    def CustomFields(self):
        return self._CustomFields

    @CustomFields.setter
    def CustomFields(self, CustomFields):
        self._CustomFields = CustomFields

    @property
    def DeliveryConditions(self):
        return self._DeliveryConditions

    @DeliveryConditions.setter
    def DeliveryConditions(self, DeliveryConditions):
        self._DeliveryConditions = DeliveryConditions

    @property
    def Sample(self):
        return self._Sample

    @Sample.setter
    def Sample(self, Sample):
        self._Sample = Sample

    @property
    def LogFormat(self):
        return self._LogFormat

    @LogFormat.setter
    def LogFormat(self, LogFormat):
        self._LogFormat = LogFormat

    @property
    def CLS(self):
        return self._CLS

    @CLS.setter
    def CLS(self, CLS):
        self._CLS = CLS

    @property
    def CustomEndpoint(self):
        return self._CustomEndpoint

    @CustomEndpoint.setter
    def CustomEndpoint(self, CustomEndpoint):
        self._CustomEndpoint = CustomEndpoint

    @property
    def S3(self):
        return self._S3

    @S3.setter
    def S3(self, S3):
        self._S3 = S3

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
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._DeliveryStatus = params.get("DeliveryStatus")
        self._TaskType = params.get("TaskType")
        self._EntityList = params.get("EntityList")
        self._LogType = params.get("LogType")
        self._Area = params.get("Area")
        self._Fields = params.get("Fields")
        if params.get("CustomFields") is not None:
            self._CustomFields = []
            for item in params.get("CustomFields"):
                obj = CustomField()
                obj._deserialize(item)
                self._CustomFields.append(obj)
        if params.get("DeliveryConditions") is not None:
            self._DeliveryConditions = []
            for item in params.get("DeliveryConditions"):
                obj = DeliveryCondition()
                obj._deserialize(item)
                self._DeliveryConditions.append(obj)
        self._Sample = params.get("Sample")
        if params.get("LogFormat") is not None:
            self._LogFormat = LogFormat()
            self._LogFormat._deserialize(params.get("LogFormat"))
        if params.get("CLS") is not None:
            self._CLS = CLSTopic()
            self._CLS._deserialize(params.get("CLS"))
        if params.get("CustomEndpoint") is not None:
            self._CustomEndpoint = CustomEndpoint()
            self._CustomEndpoint._deserialize(params.get("CustomEndpoint"))
        if params.get("S3") is not None:
            self._S3 = S3()
            self._S3._deserialize(params.get("S3"))
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewFlag(AbstractModel):
    """Auto-renewal configuration item in a prepaid plan.

    """

    def __init__(self):
        r"""
        :param _Switch: The auto-renewal flag for prepaid plan has the following values:
<li> on: Enable auto-renewal;</li>
<li> off: Disable auto-renewal. </li>
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewPlanRequest(AbstractModel):
    """RenewPlan request structure.

    """

    def __init__(self):
        r"""
        :param _PlanId: Plan ID, formatted as edgeone-2unuvzjmmn2q.
        :type PlanId: str
        :param _Period: Renewal plan duration, unit: month. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36.
        :type Period: int
        :param _AutoUseVoucher: Whether to automatically use a voucher. Valid values: <li>true: Yes;</li><li>false: No. </li> If this field is not specified, the default value 'false' will be used.
        :type AutoUseVoucher: str
        """
        self._PlanId = None
        self._Period = None
        self._AutoUseVoucher = None

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def AutoUseVoucher(self):
        return self._AutoUseVoucher

    @AutoUseVoucher.setter
    def AutoUseVoucher(self, AutoUseVoucher):
        self._AutoUseVoucher = AutoUseVoucher


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._Period = params.get("Period")
        self._AutoUseVoucher = params.get("AutoUseVoucher")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewPlanResponse(AbstractModel):
    """RenewPlan response structure.

    """

    def __init__(self):
        r"""
        :param _DealName: Order number.
        :type DealName: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealName = None
        self._RequestId = None

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class Resource(AbstractModel):
    """Billable resource

    """

    def __init__(self):
        r"""
        :param _Id: The resource ID.
        :type Id: str
        :param _PayMode: Billing mode
`0`: Pay-as-you-go
        :type PayMode: int
        :param _CreateTime: The creation time.
        :type CreateTime: str
        :param _EnableTime: The effective time.
        :type EnableTime: str
        :param _ExpireTime: The expiration time.
        :type ExpireTime: str
        :param _Status: The plan status. Values:
<li>`normal`: Normal</li>
<li>`isolated`: Isolated</li>
<li>`destroyed`: Terminated</li>
        :type Status: str
        :param _Sv: Pricing query parameter
        :type Sv: list of Sv
        :param _AutoRenewFlag: Whether to enable auto-renewal. Values:
<li>`0`: Default status.</li>
<li>`1`: Enable auto-renewal.</li>
<li>`2`: Disable auto-renewal.</li>
        :type AutoRenewFlag: int
        :param _PlanId: ID of the resource associated with the plan.
        :type PlanId: str
        :param _Area: Applicable area. Values:
<li>`mainland`: Chinese mainland</li>
<li>`overseas`: Regions outside the Chinese mainland</li>
<li>`global`: Global</li>
        :type Area: str
        :param _Group: The resource type. Values:
<li>`plan`: Plan resources</li>
<li>`pay-as-you-go`: Pay-as-you-go resources </li>
<li>`value-added`: Value-added resources </li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Group: str
        :param _ZoneNumber: The sites that are associated with the current resources.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneNumber: int
        :param _Type: Resource tag type. Valid values:
<li>vodeo: vodeo resource.</li>
        :type Type: str
        """
        self._Id = None
        self._PayMode = None
        self._CreateTime = None
        self._EnableTime = None
        self._ExpireTime = None
        self._Status = None
        self._Sv = None
        self._AutoRenewFlag = None
        self._PlanId = None
        self._Area = None
        self._Group = None
        self._ZoneNumber = None
        self._Type = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EnableTime(self):
        return self._EnableTime

    @EnableTime.setter
    def EnableTime(self, EnableTime):
        self._EnableTime = EnableTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Sv(self):
        return self._Sv

    @Sv.setter
    def Sv(self, Sv):
        self._Sv = Sv

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def ZoneNumber(self):
        return self._ZoneNumber

    @ZoneNumber.setter
    def ZoneNumber(self, ZoneNumber):
        self._ZoneNumber = ZoneNumber

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._PayMode = params.get("PayMode")
        self._CreateTime = params.get("CreateTime")
        self._EnableTime = params.get("EnableTime")
        self._ExpireTime = params.get("ExpireTime")
        self._Status = params.get("Status")
        if params.get("Sv") is not None:
            self._Sv = []
            for item in params.get("Sv"):
                obj = Sv()
                obj._deserialize(item)
                self._Sv.append(obj)
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._PlanId = params.get("PlanId")
        self._Area = params.get("Area")
        self._Group = params.get("Group")
        self._ZoneNumber = params.get("ZoneNumber")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RewriteAction(AbstractModel):
    """Rule engine action for the HTTP request/response header

    """

    def __init__(self):
        r"""
        :param _Action: Feature name. For details, see [DescribeRulesSetting](https://intl.cloud.tencent.com/document/product/1552/80618?from_cn_redirect=1) API
        :type Action: str
        :param _Parameters: Parameter
        :type Parameters: list of RuleRewriteActionParams
        """
        self._Action = None
        self._Parameters = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Parameters(self):
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters


    def _deserialize(self, params):
        self._Action = params.get("Action")
        if params.get("Parameters") is not None:
            self._Parameters = []
            for item in params.get("Parameters"):
                obj = RuleRewriteActionParams()
                obj._deserialize(item)
                self._Parameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Rule(AbstractModel):
    """Rule item of the rule engine. The items in the `Conditions` array are in `OR` relationship, and the items in the inner `Conditions` list are in `AND` relationship.

    """

    def __init__(self):
        r"""
        :param _Conditions: Judgment condition for executing the feature.
Note: The feature can be executed if any condition in the array is met.
        :type Conditions: list of RuleAndConditions
        :param _Actions: Executed feature. Note: Actions and SubRules cannot be both empty.
        :type Actions: list of Action
        :param _SubRules: Nested rule. Note: SubRules and Actions cannot be both empty.
        :type SubRules: list of SubRuleItem
        """
        self._Conditions = None
        self._Actions = None
        self._SubRules = None

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def Actions(self):
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def SubRules(self):
        return self._SubRules

    @SubRules.setter
    def SubRules(self, SubRules):
        self._SubRules = SubRules


    def _deserialize(self, params):
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = RuleAndConditions()
                obj._deserialize(item)
                self._Conditions.append(obj)
        if params.get("Actions") is not None:
            self._Actions = []
            for item in params.get("Actions"):
                obj = Action()
                obj._deserialize(item)
                self._Actions.append(obj)
        if params.get("SubRules") is not None:
            self._SubRules = []
            for item in params.get("SubRules"):
                obj = SubRuleItem()
                obj._deserialize(item)
                self._SubRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleAndConditions(AbstractModel):
    """List of rule engine conditions in `AND` relationship

    """

    def __init__(self):
        r"""
        :param _Conditions: Rule engine condition. This condition will be considered met if all items in the array are met.
        :type Conditions: list of RuleCondition
        """
        self._Conditions = None

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions


    def _deserialize(self, params):
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = RuleCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleChoicePropertiesItem(AbstractModel):
    """Detailed settings of the rule engine that can be used for request match, which are optional parameter configuration items.

    """

    def __init__(self):
        r"""
        :param _Name: The parameter name.
        :type Name: str
        :param _Type: The parameter value type.
<li>CHOICE: The parameter value can be selected only from `Values`.</li>
<li>TOGGLE: The parameter value is of switch type and can be selected from `ChoicesValue`.</li>
<li>CUSTOM_NUM: The parameter value is a custom integer.</li>
<li>CUSTOM_STRING: The parameter value is a custom string.</li>
        :type Type: str
        :param _ChoicesValue: Valid parameter values.
Note: If `Type` is `CUSTOM_NUM` or `CUSTOM_STRING`, this parameter will be an empty array.
        :type ChoicesValue: list of str
        :param _Min: Minimum value. If both `Min` and `Max` are set to `0`, this parameter does not take effect.
        :type Min: int
        :param _Max: Maximum value. If both `Min` and `Max` are set to `0`, this parameter does not take effect.
        :type Max: int
        :param _IsMultiple: Whether multiple values can be selected or entered.
        :type IsMultiple: bool
        :param _IsAllowEmpty: Whether the parameter can be left empty.
        :type IsAllowEmpty: bool
        :param _ExtraParameter: Special parameter.
<li>NULL: Select `NormalAction` for `RuleAction`. </li>
<li>If the member parameter `Id` is `Action`, select `RewirteAction` for `RuleAction`.</li>
<li>If the member parameter `Id` is `StatusCode`, select `CodeAction` for `RuleAction`.</li>
        :type ExtraParameter: :class:`tencentcloud.teo.v20220901.models.RuleExtraParameter`
        """
        self._Name = None
        self._Type = None
        self._ChoicesValue = None
        self._Min = None
        self._Max = None
        self._IsMultiple = None
        self._IsAllowEmpty = None
        self._ExtraParameter = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ChoicesValue(self):
        return self._ChoicesValue

    @ChoicesValue.setter
    def ChoicesValue(self, ChoicesValue):
        self._ChoicesValue = ChoicesValue

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
    def IsMultiple(self):
        return self._IsMultiple

    @IsMultiple.setter
    def IsMultiple(self, IsMultiple):
        self._IsMultiple = IsMultiple

    @property
    def IsAllowEmpty(self):
        return self._IsAllowEmpty

    @IsAllowEmpty.setter
    def IsAllowEmpty(self, IsAllowEmpty):
        self._IsAllowEmpty = IsAllowEmpty

    @property
    def ExtraParameter(self):
        return self._ExtraParameter

    @ExtraParameter.setter
    def ExtraParameter(self, ExtraParameter):
        self._ExtraParameter = ExtraParameter


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._ChoicesValue = params.get("ChoicesValue")
        self._Min = params.get("Min")
        self._Max = params.get("Max")
        self._IsMultiple = params.get("IsMultiple")
        self._IsAllowEmpty = params.get("IsAllowEmpty")
        if params.get("ExtraParameter") is not None:
            self._ExtraParameter = RuleExtraParameter()
            self._ExtraParameter._deserialize(params.get("ExtraParameter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleCodeActionParams(AbstractModel):
    """Parameters of the action with the `StatusCode` field as the rule engine condition

    """

    def __init__(self):
        r"""
        :param _StatusCode: The status code.
        :type StatusCode: int
        :param _Name: The parameter name. For details, see [DescribeRulesSetting](https://intl.cloud.tencent.com/document/product/1552/80618?from_cn_redirect=1).
        :type Name: str
        :param _Values: The parameter value.
        :type Values: list of str
        """
        self._StatusCode = None
        self._Name = None
        self._Values = None

    @property
    def StatusCode(self):
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._StatusCode = params.get("StatusCode")
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleCondition(AbstractModel):
    """Rule engine condition parameters

    """

    def __init__(self):
        r"""
        :param _Operator: Operator. Valid values:
<li>`equals`: Equals</li>
<li>`notEquals`: Does not equal</li>
<li>`exist`: Exists</li>
<li>`notexist`: Does not exist</li>
        :type Operator: str
        :param _Target: Match type. Valid values: <li> filename: File name; </li> <li> extension: File extension; </li> <li> host: Host name; </li> <li> full_url: The complete URL path under the current site, which must include the HTTP protocol, host, and path; </li> <li> url: Request for the URL path under the current site; </li><li> client_country: Client country/region;</li> <li> query_string: The query string of the URL requested under the current site; </li> <li> request_header: HTTP request header; </li><li> client_ip: Client IP address. </li>
        :type Target: str
        :param _Values: The parameter values for match types. It is allowed to pass an empty array only when the match type is query_string or request_header and the operator value is Exist or Does Not Exist. The corresponding match types include:
<li> File extension: Extensions like jpg, txt, etc.;</li>
<li> File name: For example, foo in foo.jpg;</li>
<li> All: All requests for domain names under the site; </li>
<li> HOST: The host under the current site, for example, www.maxx55.com;</li>
<li> URL Path: Request for the URL path under the current site, for example, /example;</li>
<li> URL Full: The complete URL request under the current site, which must include the HTTP protocol, host, and path, for example, https://www.maxx55.cn/example;</li>
<li> Client country/region: Country/region codes compliant with the ISO3166 standard;</li>
<li> Query string: The parameter values in the query string of the URL requested under the current site, for example, cn and 1 in lang=cn&version=1; </li>
<li> HTTP request header: The value of the HTTP request header field, for example, zh-CN,zh;q=0.9 in Accept-Language:zh-CN,zh;q=0.9; </li>
<li> Client IP: The client IP address carried by the current request, supporting IPv4, IPv6, and an IP range. </li>
        :type Values: list of str
        :param _IgnoreCase: Whether the parameter value is case insensitive. Default value: false.
        :type IgnoreCase: bool
        :param _Name: The parameter name of the match type. This field is required only when `Target=query_string/request_header`.
<li>`query_string`: Name of the query string, such as "lang" and "version" in "lang=cn&version=1".</li>
<li>`request_header`: Name of the HTTP request header, such as "Accept-Language" in the "Accept-Language:zh-CN,zh;q=0.9" header.</li>
        :type Name: str
        :param _IgnoreNameCase: Whether the parameter name is case insensitive. Default value: `false`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IgnoreNameCase: bool
        """
        self._Operator = None
        self._Target = None
        self._Values = None
        self._IgnoreCase = None
        self._Name = None
        self._IgnoreNameCase = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Target(self):
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def IgnoreCase(self):
        return self._IgnoreCase

    @IgnoreCase.setter
    def IgnoreCase(self, IgnoreCase):
        self._IgnoreCase = IgnoreCase

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IgnoreNameCase(self):
        warnings.warn("parameter `IgnoreNameCase` is deprecated", DeprecationWarning) 

        return self._IgnoreNameCase

    @IgnoreNameCase.setter
    def IgnoreNameCase(self, IgnoreNameCase):
        warnings.warn("parameter `IgnoreNameCase` is deprecated", DeprecationWarning) 

        self._IgnoreNameCase = IgnoreNameCase


    def _deserialize(self, params):
        self._Operator = params.get("Operator")
        self._Target = params.get("Target")
        self._Values = params.get("Values")
        self._IgnoreCase = params.get("IgnoreCase")
        self._Name = params.get("Name")
        self._IgnoreNameCase = params.get("IgnoreNameCase")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleExtraParameter(AbstractModel):
    """Rule engine parameter details and special parameter types.

    """

    def __init__(self):
        r"""
        :param _Id: Parameter name. Valid values:
<li>`Action`: Required parameter for HTTP header modification when `RewirteAction` is selected for `RuleAction`.</li>
<li>`StatusCode`: Required parameter for the status code feature when `CodeAction` is selected for `RuleAction`.</li>
        :type Id: str
        :param _Type: Parameter value type.
<li>`CHOICE`: The parameter value can be selected only from `Values`.</li>
<li>`CUSTOM_NUM`: The parameter value is a custom integer.</li>
<li>`CUSTOM_STRING`: The parameter value is a custom string.</li>
        :type Type: str
        :param _Choices: Valid values.
Note: If the value of `Id` is `StatusCode`, values in the array are all integer values. When entering a parameter value, enter the integer value of the string.
        :type Choices: list of str
        """
        self._Id = None
        self._Type = None
        self._Choices = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Choices(self):
        return self._Choices

    @Choices.setter
    def Choices(self, Choices):
        self._Choices = Choices


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        self._Choices = params.get("Choices")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleItem(AbstractModel):
    """Rule details of the rule engine

    """

    def __init__(self):
        r"""
        :param _RuleId: The rule ID.
        :type RuleId: str
        :param _RuleName: The rule name. It is a string that can contain 1–255 characters.
        :type RuleName: str
        :param _Status: Rule status. Values:
<li>`enable`: Enabled</li>
<li>`disable`: Disabled</li>
        :type Status: str
        :param _Rules: The rule content.
        :type Rules: list of Rule
        :param _RulePriority: The rule priority. The greater the value, the higher the priority. The minimum value is `1`.
        :type RulePriority: int
        :param _Tags: Tag of the rule.
        :type Tags: list of str
        """
        self._RuleId = None
        self._RuleName = None
        self._Status = None
        self._Rules = None
        self._RulePriority = None
        self._Tags = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def RulePriority(self):
        return self._RulePriority

    @RulePriority.setter
    def RulePriority(self, RulePriority):
        self._RulePriority = RulePriority

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._Status = params.get("Status")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = Rule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._RulePriority = params.get("RulePriority")
        self._Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleNormalActionParams(AbstractModel):
    """Common action parameter of a rule engine condition

    """

    def __init__(self):
        r"""
        :param _Name: The parameter name. For details, see [DescribeRulesSetting](https://intl.cloud.tencent.com/document/product/1552/80618?from_cn_redirect=1).
        :type Name: str
        :param _Values: The parameter value.
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleRewriteActionParams(AbstractModel):
    """Parameter of the action for the HTTP request/response header of a rule engine condition.

    """

    def __init__(self):
        r"""
        :param _Action: Feature parameter name. For details, see [DescribeRulesSetting](https://intl.cloud.tencent.com/document/product/1552/80618?from_cn_redirect=1).
<li>`add`: Add the HTTP header.</li>
<li>`set`: Rewrite the HTTP header.</li>
<li>`del`: Delete the HTTP header.</li>
        :type Action: str
        :param _Name: Parameter name
        :type Name: str
        :param _Values: Parameter value
        :type Values: list of str
        """
        self._Action = None
        self._Name = None
        self._Values = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RulesProperties(AbstractModel):
    """Detailed settings of the rule engine that can be used for request match.

    """

    def __init__(self):
        r"""
        :param _Name: Parameter name.
        :type Name: str
        :param _Min: Minimum value. If both `Min` and `Max` are set to `0`, this parameter does not take effect.
        :type Min: int
        :param _ChoicesValue: Valid parameter values.
Note: If `Type` is `CUSTOM_NUM` or `CUSTOM_STRING`, this parameter will be an empty array.
        :type ChoicesValue: list of str
        :param _Type: The parameter value type.
<li>`CHOICE`: `If Type=CHOICE`, choose a value in `ChoiceValue`.</li>
<li>`TOGGLE`: If `Type=TOGGLE`, choose `on` or `off` from `ChoicesValue`.</li>
<li>`OBJECT`: Specify an object. If this is specified, `ChoiceProperties` includes attributes of the specified object. See [Example 2. Create a rule with Type=OBJECT](https://intl.cloud.tencent.com/document/product/1552/80622?from_cn_redirect=1#.E7.A4.BA.E4.BE.8B2-.E5.8F.82.E6.95.B0.E4.B8.BA-OBJECT-.E7.B1.BB.E5.9E.8B.E7.9A.84.E5.88.9B.E5.BB.BA)</li>
<li>`CUSTOM_NUM`: (Integer) Custom value.</li>
<li>`CUSTOM_STRING`: (String) Custom value.</li>
        :type Type: str
        :param _Max: Maximum value. If both `Min` and `Max` are set to `0`, this parameter does not take effect.
        :type Max: int
        :param _IsMultiple: Whether multiple values can be selected or entered.
        :type IsMultiple: bool
        :param _IsAllowEmpty: Whether the parameter can be left empty.
        :type IsAllowEmpty: bool
        :param _ChoiceProperties: Associated configuration parameters of this parameter, which are required for API call.
Note: This parameter will be an empty array if no special parameters are added as optional parameters.
        :type ChoiceProperties: list of RuleChoicePropertiesItem
        :param _ExtraParameter: <li>NULL: No special parameters when `NormalAction` is selected for `RuleAction`.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExtraParameter: :class:`tencentcloud.teo.v20220901.models.RuleExtraParameter`
        """
        self._Name = None
        self._Min = None
        self._ChoicesValue = None
        self._Type = None
        self._Max = None
        self._IsMultiple = None
        self._IsAllowEmpty = None
        self._ChoiceProperties = None
        self._ExtraParameter = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Min(self):
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def ChoicesValue(self):
        return self._ChoicesValue

    @ChoicesValue.setter
    def ChoicesValue(self, ChoicesValue):
        self._ChoicesValue = ChoicesValue

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def IsMultiple(self):
        return self._IsMultiple

    @IsMultiple.setter
    def IsMultiple(self, IsMultiple):
        self._IsMultiple = IsMultiple

    @property
    def IsAllowEmpty(self):
        return self._IsAllowEmpty

    @IsAllowEmpty.setter
    def IsAllowEmpty(self, IsAllowEmpty):
        self._IsAllowEmpty = IsAllowEmpty

    @property
    def ChoiceProperties(self):
        return self._ChoiceProperties

    @ChoiceProperties.setter
    def ChoiceProperties(self, ChoiceProperties):
        self._ChoiceProperties = ChoiceProperties

    @property
    def ExtraParameter(self):
        return self._ExtraParameter

    @ExtraParameter.setter
    def ExtraParameter(self, ExtraParameter):
        self._ExtraParameter = ExtraParameter


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Min = params.get("Min")
        self._ChoicesValue = params.get("ChoicesValue")
        self._Type = params.get("Type")
        self._Max = params.get("Max")
        self._IsMultiple = params.get("IsMultiple")
        self._IsAllowEmpty = params.get("IsAllowEmpty")
        if params.get("ChoiceProperties") is not None:
            self._ChoiceProperties = []
            for item in params.get("ChoiceProperties"):
                obj = RuleChoicePropertiesItem()
                obj._deserialize(item)
                self._ChoiceProperties.append(obj)
        if params.get("ExtraParameter") is not None:
            self._ExtraParameter = RuleExtraParameter()
            self._ExtraParameter._deserialize(params.get("ExtraParameter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RulesSettingAction(AbstractModel):
    """List of the settings of the rule engine that can be used for request match and their detailed information.

    """

    def __init__(self):
        r"""
        :param _Action: Feature name. Valid values:
<li>Access URL rewrite (`AccessUrlRedirect`).</li>
<li>Origin-pull URL rewrite (`UpstreamUrlRedirect`).</li>
<li>Custom error page
(`ErrorPage`).</li>
<li>QUIC (`QUIC`).</li>
<li>WebSocket (`WebSocket`).</li>
<li>Video dragging (`VideoSeek`).</li>
<li>Token authentication (`Authentication`).</li>
<li>`CacheKey`: Custom cache key.</li>
<li>`Cache`: Node cache TTL.</li>
<li>`MaxAge`: Browser cache TTL.</li>
<li>`OfflineCache`: Offline cache.</li>
<li>`SmartRouting`: Smart acceleration.</li>
<li>`RangeOriginPull`: Range GETs.</li>
<li>`UpstreamHttp2`: HTTP/2 forwarding.</li>
<li>`HostHeader`: Host header rewrite.</li>
<li>`ForceRedirect`: Force HTTPS.</li>
<li>`OriginPullProtocol`: Origin-pull HTTPS.</li>
<li>`CachePrefresh`: Cache prefresh.</li>
<li>`Compression`: Smart compression.</li>
<li>`RequestHeader`: HTTP request header modification.</li>
<li>HTTP response header modification (`ResponseHeader`).</li>
<li>Status code cache TTL (`StatusCodeCache`).</li>
<li>`Hsts`.</li>
<li>`ClientIpHeader`.</li>
<li>`TlsVersion`.</li>
<li>`OcspStapling`.</li>
        :type Action: str
        :param _Properties: Parameter information
        :type Properties: list of RulesProperties
        """
        self._Action = None
        self._Properties = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Properties(self):
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties


    def _deserialize(self, params):
        self._Action = params.get("Action")
        if params.get("Properties") is not None:
            self._Properties = []
            for item in params.get("Properties"):
                obj = RulesProperties()
                obj._deserialize(item)
                self._Properties.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class S3(AbstractModel):
    """The configuration information of real-time log delivery to an AWS S3 compatible bucket

    """

    def __init__(self):
        r"""
        :param _Endpoint: The URL without bucket name or path, for example: `https://storage.googleapis.com`, `https://s3.ap-northeast-2.amazonaws.com`, and `https://cos.ap-nanjing.myqcloud.com`.
        :type Endpoint: str
        :param _Region: The region where the bucket is located, for example: `ap-northeast-2`.
        :type Region: str
        :param _Bucket: The bucket name and log storage directory, for example: `your_bucket_name/EO-logs/`. If the directory does not exist in the bucket, it will be created automatically.
        :type Bucket: str
        :param _AccessId: The Access Key ID used to access the bucket.
        :type AccessId: str
        :param _AccessKey: The secret key used to access the bucket.
        :type AccessKey: str
        :param _CompressType: The data compress type. Valid values:<li>gzip: gzip compression.</li>If this field is not filled in, compression is disabled.
        :type CompressType: str
        """
        self._Endpoint = None
        self._Region = None
        self._Bucket = None
        self._AccessId = None
        self._AccessKey = None
        self._CompressType = None

    @property
    def Endpoint(self):
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def AccessId(self):
        return self._AccessId

    @AccessId.setter
    def AccessId(self, AccessId):
        self._AccessId = AccessId

    @property
    def AccessKey(self):
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def CompressType(self):
        return self._CompressType

    @CompressType.setter
    def CompressType(self, CompressType):
        self._CompressType = CompressType


    def _deserialize(self, params):
        self._Endpoint = params.get("Endpoint")
        self._Region = params.get("Region")
        self._Bucket = params.get("Bucket")
        self._AccessId = params.get("AccessId")
        self._AccessKey = params.get("AccessKey")
        self._CompressType = params.get("CompressType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecEntry(AbstractModel):
    """Returned value of security data entry

    """

    def __init__(self):
        r"""
        :param _Key: The query dimension value.
        :type Key: str
        :param _Value: The details.
        :type Value: list of SecEntryValue
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
        if params.get("Value") is not None:
            self._Value = []
            for item in params.get("Value"):
                obj = SecEntryValue()
                obj._deserialize(item)
                self._Value.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecEntryValue(AbstractModel):
    """The security data queried by metric

    """

    def __init__(self):
        r"""
        :param _Metric: The metric name.
        :type Metric: str
        :param _Detail: The time-series data details.
        :type Detail: list of TimingDataItem
        :param _Max: The maximum value.
        :type Max: int
        :param _Avg: The average value.
        :type Avg: float
        :param _Sum: Sum
        :type Sum: float
        """
        self._Metric = None
        self._Detail = None
        self._Max = None
        self._Avg = None
        self._Sum = None

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Avg(self):
        return self._Avg

    @Avg.setter
    def Avg(self, Avg):
        self._Avg = Avg

    @property
    def Sum(self):
        return self._Sum

    @Sum.setter
    def Sum(self, Sum):
        self._Sum = Sum


    def _deserialize(self, params):
        self._Metric = params.get("Metric")
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = TimingDataItem()
                obj._deserialize(item)
                self._Detail.append(obj)
        self._Max = params.get("Max")
        self._Avg = params.get("Avg")
        self._Sum = params.get("Sum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityConfig(AbstractModel):
    """Security configuration

    """

    def __init__(self):
        r"""
        :param _WafConfig: Managed rule. If the parameter is null or not filled, the configuration last set will be used by default.
Note: This field may return null, indicating that no valid value can be obtained.
        :type WafConfig: :class:`tencentcloud.teo.v20220901.models.WafConfig`
        :param _RateLimitConfig: Rate limiting. If the parameter is null or not filled, the configuration last set will be used by default.
Note: This field may return null, indicating that no valid value can be obtained.
        :type RateLimitConfig: :class:`tencentcloud.teo.v20220901.models.RateLimitConfig`
        :param _AclConfig: Custom rule. If the parameter is null or not filled, the configuration last set will be used by default.
Note: This field may return null, indicating that no valid value can be obtained.
        :type AclConfig: :class:`tencentcloud.teo.v20220901.models.AclConfig`
        :param _BotConfig: Bot configuration. If the parameter is null or not filled, the configuration last set will be used by default.
Note: This field may return null, indicating that no valid value can be obtained.
        :type BotConfig: :class:`tencentcloud.teo.v20220901.models.BotConfig`
        :param _SwitchConfig: Switch setting of the 7-layer protection. If the parameter is null or not filled, the configuration last set will be used by default.Note: This field may return null, indicating that no valid value can be obtained.
        :type SwitchConfig: :class:`tencentcloud.teo.v20220901.models.SwitchConfig`
        :param _IpTableConfig: Basic access control. If the parameter is null or not filled, the configuration last set will be used by default.
Note: This field may return null, indicating that no valid value can be obtained.
        :type IpTableConfig: :class:`tencentcloud.teo.v20220901.models.IpTableConfig`
        :param _ExceptConfig: Exception rule configuration. If the parameter is null or not filled, the configuration last set will be used by default.Note: This field may return null, indicating that no valid value can be obtained.
        :type ExceptConfig: :class:`tencentcloud.teo.v20220901.models.ExceptConfig`
        :param _DropPageConfig: Custom block page settings. If the parameter is null or not filled, the configuration last set will be used by default.Note: This field may return null, indicating that no valid value can be obtained.
        :type DropPageConfig: :class:`tencentcloud.teo.v20220901.models.DropPageConfig`
        :param _TemplateConfig: Security template settings
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TemplateConfig: :class:`tencentcloud.teo.v20220901.models.TemplateConfig`
        :param _SlowPostConfig: Settings for slow attack defense. If the parameter is null or not filled, the configuration last set will be used by default.Note: This field may return null, indicating that no valid value can be obtained.
        :type SlowPostConfig: :class:`tencentcloud.teo.v20220901.models.SlowPostConfig`
        """
        self._WafConfig = None
        self._RateLimitConfig = None
        self._AclConfig = None
        self._BotConfig = None
        self._SwitchConfig = None
        self._IpTableConfig = None
        self._ExceptConfig = None
        self._DropPageConfig = None
        self._TemplateConfig = None
        self._SlowPostConfig = None

    @property
    def WafConfig(self):
        return self._WafConfig

    @WafConfig.setter
    def WafConfig(self, WafConfig):
        self._WafConfig = WafConfig

    @property
    def RateLimitConfig(self):
        return self._RateLimitConfig

    @RateLimitConfig.setter
    def RateLimitConfig(self, RateLimitConfig):
        self._RateLimitConfig = RateLimitConfig

    @property
    def AclConfig(self):
        return self._AclConfig

    @AclConfig.setter
    def AclConfig(self, AclConfig):
        self._AclConfig = AclConfig

    @property
    def BotConfig(self):
        return self._BotConfig

    @BotConfig.setter
    def BotConfig(self, BotConfig):
        self._BotConfig = BotConfig

    @property
    def SwitchConfig(self):
        return self._SwitchConfig

    @SwitchConfig.setter
    def SwitchConfig(self, SwitchConfig):
        self._SwitchConfig = SwitchConfig

    @property
    def IpTableConfig(self):
        return self._IpTableConfig

    @IpTableConfig.setter
    def IpTableConfig(self, IpTableConfig):
        self._IpTableConfig = IpTableConfig

    @property
    def ExceptConfig(self):
        return self._ExceptConfig

    @ExceptConfig.setter
    def ExceptConfig(self, ExceptConfig):
        self._ExceptConfig = ExceptConfig

    @property
    def DropPageConfig(self):
        return self._DropPageConfig

    @DropPageConfig.setter
    def DropPageConfig(self, DropPageConfig):
        self._DropPageConfig = DropPageConfig

    @property
    def TemplateConfig(self):
        return self._TemplateConfig

    @TemplateConfig.setter
    def TemplateConfig(self, TemplateConfig):
        self._TemplateConfig = TemplateConfig

    @property
    def SlowPostConfig(self):
        return self._SlowPostConfig

    @SlowPostConfig.setter
    def SlowPostConfig(self, SlowPostConfig):
        self._SlowPostConfig = SlowPostConfig


    def _deserialize(self, params):
        if params.get("WafConfig") is not None:
            self._WafConfig = WafConfig()
            self._WafConfig._deserialize(params.get("WafConfig"))
        if params.get("RateLimitConfig") is not None:
            self._RateLimitConfig = RateLimitConfig()
            self._RateLimitConfig._deserialize(params.get("RateLimitConfig"))
        if params.get("AclConfig") is not None:
            self._AclConfig = AclConfig()
            self._AclConfig._deserialize(params.get("AclConfig"))
        if params.get("BotConfig") is not None:
            self._BotConfig = BotConfig()
            self._BotConfig._deserialize(params.get("BotConfig"))
        if params.get("SwitchConfig") is not None:
            self._SwitchConfig = SwitchConfig()
            self._SwitchConfig._deserialize(params.get("SwitchConfig"))
        if params.get("IpTableConfig") is not None:
            self._IpTableConfig = IpTableConfig()
            self._IpTableConfig._deserialize(params.get("IpTableConfig"))
        if params.get("ExceptConfig") is not None:
            self._ExceptConfig = ExceptConfig()
            self._ExceptConfig._deserialize(params.get("ExceptConfig"))
        if params.get("DropPageConfig") is not None:
            self._DropPageConfig = DropPageConfig()
            self._DropPageConfig._deserialize(params.get("DropPageConfig"))
        if params.get("TemplateConfig") is not None:
            self._TemplateConfig = TemplateConfig()
            self._TemplateConfig._deserialize(params.get("TemplateConfig"))
        if params.get("SlowPostConfig") is not None:
            self._SlowPostConfig = SlowPostConfig()
            self._SlowPostConfig._deserialize(params.get("SlowPostConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityTemplateBinding(AbstractModel):
    """Bindings of a security policy template

    """

    def __init__(self):
        r"""
        :param _TemplateId: template ID
        :type TemplateId: str
        :param _TemplateScope: Binding status of the template.
        :type TemplateScope: list of TemplateScope
        """
        self._TemplateId = None
        self._TemplateScope = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateScope(self):
        return self._TemplateScope

    @TemplateScope.setter
    def TemplateScope(self, TemplateScope):
        self._TemplateScope = TemplateScope


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        if params.get("TemplateScope") is not None:
            self._TemplateScope = []
            for item in params.get("TemplateScope"):
                obj = TemplateScope()
                obj._deserialize(item)
                self._TemplateScope.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityType(AbstractModel):
    """The security type setting item.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable the security type setting. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerCertInfo(AbstractModel):
    """HTTPS server certificate configuration

    """

    def __init__(self):
        r"""
        :param _CertId: ID of the server certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertId: str
        :param _Alias: Alias of the certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Alias: str
        :param _Type: Type of the certificate. Values:
u200c<li>`default`: Default certificate</li>
u200c<li>`upload`: Custom certificate</li>
u200c<li>`managed`: Tencent Cloud-managed certificate</li>
Note: This field may return·null, indicating that no valid values can be obtained.
        :type Type: str
        :param _ExpireTime: Time when the certificate expires.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param _DeployTime: Time when the certificate is deployed.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DeployTime: str
        :param _SignAlgo: Signature algorithm.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SignAlgo: str
        :param _CommonName: Domain name of the certificate.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CommonName: str
        """
        self._CertId = None
        self._Alias = None
        self._Type = None
        self._ExpireTime = None
        self._DeployTime = None
        self._SignAlgo = None
        self._CommonName = None

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def DeployTime(self):
        return self._DeployTime

    @DeployTime.setter
    def DeployTime(self, DeployTime):
        self._DeployTime = DeployTime

    @property
    def SignAlgo(self):
        return self._SignAlgo

    @SignAlgo.setter
    def SignAlgo(self, SignAlgo):
        self._SignAlgo = SignAlgo

    @property
    def CommonName(self):
        return self._CommonName

    @CommonName.setter
    def CommonName(self, CommonName):
        self._CommonName = CommonName


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._Alias = params.get("Alias")
        self._Type = params.get("Type")
        self._ExpireTime = params.get("ExpireTime")
        self._DeployTime = params.get("DeployTime")
        self._SignAlgo = params.get("SignAlgo")
        self._CommonName = params.get("CommonName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkipCondition(AbstractModel):
    """Exception rule conditions, used to filter requests by specific fields

    """

    def __init__(self):
        r"""
        :param _Type: The field type. Values:
<li>`header_fields`: HTTP request header</li>
<li>`cookie`: HTTP request cookie</li>
<li>`query_string`: Query string in the HTTP request URL</li>
<li>`uri`: HTTP request URI</li>
<li>`body_raw`: HTTP request body</li>
<li>`body_json`: JSON HTTP request body</li>
        :type Type: str
        :param _Selector: The specific field. Values:
<li>`args`: Query parameter in the URI, such as "?name1=jack&age=12"</li>
<li>`path`: Partial path in the URI, such as "/path/to/resource.jpg"</li>
<li>`full`: Full path in the URI, such as "example.com/path/to/resource.jpg?name1=jack&age=12"</li>
<li>`upload_filename`: File path segment</li>
<li>`keys`: All keys</li>
<li>`values`: Values of all keys</li>
<li>`key_value`: Key and its value</li>
        :type Selector: str
        :param _MatchFromType: The match method used to match the key. Values:
<li>`equal`: Exact match</li>
<li>`wildcard`: Wildcard match (only asterisks)</li>
        :type MatchFromType: str
        :param _MatchFrom: The value that matches the key.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type MatchFrom: list of str
        :param _MatchContentType: The match method used to match the content.
<li>`equal`: Exact match</li>
<li>`wildcard`: Wildcard match (only asterisks)</li>
        :type MatchContentType: str
        :param _MatchContent: The value that matches the content.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type MatchContent: list of str
        """
        self._Type = None
        self._Selector = None
        self._MatchFromType = None
        self._MatchFrom = None
        self._MatchContentType = None
        self._MatchContent = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Selector(self):
        return self._Selector

    @Selector.setter
    def Selector(self, Selector):
        self._Selector = Selector

    @property
    def MatchFromType(self):
        return self._MatchFromType

    @MatchFromType.setter
    def MatchFromType(self, MatchFromType):
        self._MatchFromType = MatchFromType

    @property
    def MatchFrom(self):
        return self._MatchFrom

    @MatchFrom.setter
    def MatchFrom(self, MatchFrom):
        self._MatchFrom = MatchFrom

    @property
    def MatchContentType(self):
        return self._MatchContentType

    @MatchContentType.setter
    def MatchContentType(self, MatchContentType):
        self._MatchContentType = MatchContentType

    @property
    def MatchContent(self):
        return self._MatchContent

    @MatchContent.setter
    def MatchContent(self, MatchContent):
        self._MatchContent = MatchContent


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Selector = params.get("Selector")
        self._MatchFromType = params.get("MatchFromType")
        self._MatchFrom = params.get("MatchFrom")
        self._MatchContentType = params.get("MatchContentType")
        self._MatchContent = params.get("MatchContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowPostConfig(AbstractModel):
    """Slow attack defense configuration.

    """

    def __init__(self):
        r"""
        :param _Switch: Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param _FirstPartConfig: Detect slow attacks by the transfer period of the first 8 KB of requests
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FirstPartConfig: :class:`tencentcloud.teo.v20220901.models.FirstPartConfig`
        :param _SlowRateConfig: Detect slow attacks by the data rate of the main body (excluding the first 8 KB) of requests
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SlowRateConfig: :class:`tencentcloud.teo.v20220901.models.SlowRateConfig`
        :param _Action: The action to taken when a slow attack is detected. Values:
<li>`monitor`: Observe</li>
<li>`drop`: Block the request</li>
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Action: str
        :param _RuleId: ID of the rule
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuleId: int
        """
        self._Switch = None
        self._FirstPartConfig = None
        self._SlowRateConfig = None
        self._Action = None
        self._RuleId = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def FirstPartConfig(self):
        return self._FirstPartConfig

    @FirstPartConfig.setter
    def FirstPartConfig(self, FirstPartConfig):
        self._FirstPartConfig = FirstPartConfig

    @property
    def SlowRateConfig(self):
        return self._SlowRateConfig

    @SlowRateConfig.setter
    def SlowRateConfig(self, SlowRateConfig):
        self._SlowRateConfig = SlowRateConfig

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("FirstPartConfig") is not None:
            self._FirstPartConfig = FirstPartConfig()
            self._FirstPartConfig._deserialize(params.get("FirstPartConfig"))
        if params.get("SlowRateConfig") is not None:
            self._SlowRateConfig = SlowRateConfig()
            self._SlowRateConfig._deserialize(params.get("SlowRateConfig"))
        self._Action = params.get("Action")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowRateConfig(AbstractModel):
    """The configuration to detect slow attacks

    """

    def __init__(self):
        r"""
        :param _Switch: Switch. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param _Interval: The sampling interval in seconds. In this way, the first 8 KB of the request is ignored. The rest of data is separated in to multiple parts according to this interval for slow attack measurement.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Interval: int
        :param _Threshold: The transfer rate threshold in bps. When the transfer rate of a sample is lower than the threshold, it’s considered a slow attack and handled according to the specified `Action`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Threshold: int
        """
        self._Switch = None
        self._Interval = None
        self._Threshold = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Threshold(self):
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Interval = params.get("Interval")
        self._Threshold = params.get("Threshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartRouting(AbstractModel):
    """Smart acceleration configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable smart acceleration. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StandardDebug(AbstractModel):
    """Standard debugging

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable standard debugging. Values:
<li>`on`: Enable</li>
<li>`off`: Disable </li>
        :type Switch: str
        :param _AllowClientIPList: The client IP to allow. It can be an IPv4/IPv6 address or a CIDR block. If not specified, it means to allow any client IP
        :type AllowClientIPList: list of str
        :param _ExpireTime: The time when the standard debugging setting expires. If it is exceeded, this feature becomes invalid.
        :type ExpireTime: str
        """
        self._Switch = None
        self._AllowClientIPList = None
        self._ExpireTime = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def AllowClientIPList(self):
        return self._AllowClientIPList

    @AllowClientIPList.setter
    def AllowClientIPList(self, AllowClientIPList):
        self._AllowClientIPList = AllowClientIPList

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._AllowClientIPList = params.get("AllowClientIPList")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubRule(AbstractModel):
    """Nested rule settings

    """

    def __init__(self):
        r"""
        :param _Conditions: The condition that determines if a feature should run.
Note: If any condition in the array is met, the feature will run.
        :type Conditions: list of RuleAndConditions
        :param _Actions: The feature to be executed.
        :type Actions: list of Action
        """
        self._Conditions = None
        self._Actions = None

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def Actions(self):
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions


    def _deserialize(self, params):
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = RuleAndConditions()
                obj._deserialize(item)
                self._Conditions.append(obj)
        if params.get("Actions") is not None:
            self._Actions = []
            for item in params.get("Actions"):
                obj = Action()
                obj._deserialize(item)
                self._Actions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubRuleItem(AbstractModel):
    """Rule engine nested rule

    """

    def __init__(self):
        r"""
        :param _Rules: Nested rule settings
        :type Rules: list of SubRule
        :param _Tags: Tag of the rule.
        :type Tags: list of str
        """
        self._Rules = None
        self._Tags = None

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = SubRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Sv(AbstractModel):
    """Pricing query parameter

    """

    def __init__(self):
        r"""
        :param _Key: The parameter key.
        :type Key: str
        :param _Value: The parameter value.
        :type Value: str
        :param _Pack: Quota for a resource. Values:
<li>`zone`: Quota for sites</li>
<li>`custom-rule`: Quota for custom rules</li>
<li>`rate-limiting-rule`: Quota for rate limiting rules</li>
<li>`l4-proxy-instance`: Quota for L4 proxy instances </li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Pack: str
        :param _InstanceId: ID of the L4 proxy instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _ProtectionSpecs: The protection specification.
Values: <li> `cm_30G`: 30 Gbps base protection bandwidth in **Chinese mainland** service area</li><li> `cm_60G`: 60 Gbps base protection bandwidth in **Chinese mainland** service area</li><li> `cm_100G`: 100 Gbps base protection bandwidth in **Chinese mainland** service area</li><li> `anycast_300G`: 300 Gbps Anycast-based protection in **Global (MLC)** service area</li><li> `anycast_unlimited`: Unlimited Anycast-based protection bandwidth in **Global (MLC)** service area</li><li> `cm_30G_anycast_300G`: 30 Gbps base protection bandwidth in **Chinese mainland** service area and 300 Gbps Anycast-based protection bandwidth in **Global (MLC)** service area</li><li> `cm_30G_anycast_unlimited`: 30 Gbps base protection bandwidth in **Chinese mainland** service area and unlimited Anycast-based protection bandwidth in **Global (MLC)** service area</li><li> cm_60G_anycast_300G`: 60 Gbps base protection bandwidth in **Chinese mainland** service area and 300 Gbps Anycast-based protection bandwidth in **Global (MLC)** service area</li><li> cm_60G_anycast_unlimited`: 60 Gbps base protection bandwidth in **Chinese mainland** service area and unlimited Anycast-based protection bandwidth in **Global (MLC)** service area</li><li> `cm_100G_anycast_300G`: 100 Gbps base protection bandwidth in **Chinese mainland** service area and 300 Gbps Anycast-based protection bandwidth in **Global (MLC)** service area</li><li> cm_100G_anycast_unlimited`: 100 Gbps base protection bandwidth in **Chinese mainland** service area and unlimited Anycast-based protection bandwidth in **Global (MLC)** service area </li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProtectionSpecs: str
        """
        self._Key = None
        self._Value = None
        self._Pack = None
        self._InstanceId = None
        self._ProtectionSpecs = None

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

    @property
    def Pack(self):
        return self._Pack

    @Pack.setter
    def Pack(self, Pack):
        self._Pack = Pack

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProtectionSpecs(self):
        return self._ProtectionSpecs

    @ProtectionSpecs.setter
    def ProtectionSpecs(self, ProtectionSpecs):
        self._ProtectionSpecs = ProtectionSpecs


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Pack = params.get("Pack")
        self._InstanceId = params.get("InstanceId")
        self._ProtectionSpecs = params.get("ProtectionSpecs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchConfig(AbstractModel):
    """Web security configuration switch

    """

    def __init__(self):
        r"""
        :param _WebSwitch: Whether to enable web protection. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>It does not affect DDoS and bot configuration.
        :type WebSwitch: str
        """
        self._WebSwitch = None

    @property
    def WebSwitch(self):
        return self._WebSwitch

    @WebSwitch.setter
    def WebSwitch(self, WebSwitch):
        self._WebSwitch = WebSwitch


    def _deserialize(self, params):
        self._WebSwitch = params.get("WebSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Tag configuration

    """

    def __init__(self):
        r"""
        :param _TagKey: The tag key.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagKey: str
        :param _TagValue: The tag value.
Note: This field may return null, indicating that no valid values can be obtained.
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
        


class Task(AbstractModel):
    """Content management task result

    """

    def __init__(self):
        r"""
        :param _JobId: ID of the task.
        :type JobId: str
        :param _Target: Resource.
        :type Target: str
        :param _Type: Type of the task.
        :type Type: str
        :param _Method: Node cache purge method, with values:
<li>invalidate: Marks as expired. A back-to-origin validation is triggered upon user request, sending an HTTP conditional request with If-None-Match and If-Modified-Since headers. If the origin server responds with 200, the node will fetch new resources from the origin and update the cache; if the origin server responds with 304, the cache will not be updated;</li>
<li>delete: Directly deletes the node's cache, triggering a resource fetch from the origin upon user request.</li>
Note: This field may return null, which indicates a failure to obtain a valid value.
        :type Method: str
        :param _Status: Status. Valid values:
<li>processing: Processing;</li>
<li>success: Succeeded;</li>
<li>failed: Failed;</li>
<li>timeout: Timed out. </li>
        :type Status: str
        :param _CreateTime: Creation time of the task.
        :type CreateTime: str
        :param _UpdateTime: Completion time of the task.
        :type UpdateTime: str
        """
        self._JobId = None
        self._Target = None
        self._Type = None
        self._Method = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Target(self):
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

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
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._Target = params.get("Target")
        self._Type = params.get("Type")
        self._Method = params.get("Method")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateConfig(AbstractModel):
    """Security template settings

    """

    def __init__(self):
        r"""
        :param _TemplateId: The template ID.
        :type TemplateId: str
        :param _TemplateName: The template name.
        :type TemplateName: str
        """
        self._TemplateId = None
        self._TemplateName = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateScope(AbstractModel):
    """Domain names bound with the template.

    """

    def __init__(self):
        r"""
        :param _ZoneId: ID of the site.
Note: This field may return·null, indicating that no valid values can be obtained.
        :type ZoneId: str
        :param _EntityStatus: List of instance statuses
Note: This field may return·null, indicating that no valid values can be obtained.
        :type EntityStatus: list of EntityStatus
        """
        self._ZoneId = None
        self._EntityStatus = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def EntityStatus(self):
        return self._EntityStatus

    @EntityStatus.setter
    def EntityStatus(self, EntityStatus):
        self._EntityStatus = EntityStatus


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("EntityStatus") is not None:
            self._EntityStatus = []
            for item in params.get("EntityStatus"):
                obj = EntityStatus()
                obj._deserialize(item)
                self._EntityStatus.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimingDataItem(AbstractModel):
    """Data items of the statistical curve

    """

    def __init__(self):
        r"""
        :param _Timestamp: Time point for returning data, in the format of Unix timestamp in seconds.
        :type Timestamp: int
        :param _Value: The value.
        :type Value: int
        """
        self._Timestamp = None
        self._Value = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimingDataRecord(AbstractModel):
    """The time-series data

    """

    def __init__(self):
        r"""
        :param _TypeKey: The query dimension value.
        :type TypeKey: str
        :param _TypeValue: Detailed time series data
        :type TypeValue: list of TimingTypeValue
        """
        self._TypeKey = None
        self._TypeValue = None

    @property
    def TypeKey(self):
        return self._TypeKey

    @TypeKey.setter
    def TypeKey(self, TypeKey):
        self._TypeKey = TypeKey

    @property
    def TypeValue(self):
        return self._TypeValue

    @TypeValue.setter
    def TypeValue(self, TypeValue):
        self._TypeValue = TypeValue


    def _deserialize(self, params):
        self._TypeKey = params.get("TypeKey")
        if params.get("TypeValue") is not None:
            self._TypeValue = []
            for item in params.get("TypeValue"):
                obj = TimingTypeValue()
                obj._deserialize(item)
                self._TypeValue.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimingTypeValue(AbstractModel):
    """Detailed data of time series type

    """

    def __init__(self):
        r"""
        :param _Sum: Sum.
        :type Sum: int
        :param _Max: The maximum value.
        :type Max: int
        :param _Avg: The average value.
        :type Avg: int
        :param _MetricName: Metric name.
        :type MetricName: str
        :param _Detail: Details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Detail: list of TimingDataItem
        """
        self._Sum = None
        self._Max = None
        self._Avg = None
        self._MetricName = None
        self._Detail = None

    @property
    def Sum(self):
        return self._Sum

    @Sum.setter
    def Sum(self, Sum):
        self._Sum = Sum

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Avg(self):
        return self._Avg

    @Avg.setter
    def Avg(self, Avg):
        self._Avg = Avg

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail


    def _deserialize(self, params):
        self._Sum = params.get("Sum")
        self._Max = params.get("Max")
        self._Avg = params.get("Avg")
        self._MetricName = params.get("MetricName")
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = TimingDataItem()
                obj._deserialize(item)
                self._Detail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopDataRecord(AbstractModel):
    """The top-ranked data record

    """

    def __init__(self):
        r"""
        :param _TypeKey: The query dimension value.
        :type TypeKey: str
        :param _DetailData: Top data rankings
        :type DetailData: list of TopDetailData
        """
        self._TypeKey = None
        self._DetailData = None

    @property
    def TypeKey(self):
        return self._TypeKey

    @TypeKey.setter
    def TypeKey(self, TypeKey):
        self._TypeKey = TypeKey

    @property
    def DetailData(self):
        return self._DetailData

    @DetailData.setter
    def DetailData(self, DetailData):
        self._DetailData = DetailData


    def _deserialize(self, params):
        self._TypeKey = params.get("TypeKey")
        if params.get("DetailData") is not None:
            self._DetailData = []
            for item in params.get("DetailData"):
                obj = TopDetailData()
                obj._deserialize(item)
                self._DetailData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopDetailData(AbstractModel):
    """The top-ranked data details

    """

    def __init__(self):
        r"""
        :param _Key: The field name.
        :type Key: str
        :param _Value: The field value.
        :type Value: int
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
        


class TopEntry(AbstractModel):
    """The Top-ranked data

    """

    def __init__(self):
        r"""
        :param _Key: The query dimension value.
        :type Key: str
        :param _Value: The details.
        :type Value: list of TopEntryValue
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
        if params.get("Value") is not None:
            self._Value = []
            for item in params.get("Value"):
                obj = TopEntryValue()
                obj._deserialize(item)
                self._Value.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopEntryValue(AbstractModel):
    """The top-ranked data

    """

    def __init__(self):
        r"""
        :param _Name: The item name.
        :type Name: str
        :param _Count: The number of items.
        :type Count: int
        """
        self._Name = None
        self._Count = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradePlanRequest(AbstractModel):
    """UpgradePlan request structure.

    """

    def __init__(self):
        r"""
        :param _PlanId: Plan ID, formatted as edgeone-2unuvzjmmn2q.
        :type PlanId: str
        :param _PlanType: Target plan version for upgrade. Valid values: <li>basic: Basic Edition Plan;</li><li>standard: Standard Edition Plan. </li>
        :type PlanType: str
        :param _AutoUseVoucher: Whether to automatically use a voucher. Valid values: <li>true: Yes;</li><li>false: No. </li> If this field is not specified, the default value 'false' will be used.
        :type AutoUseVoucher: str
        """
        self._PlanId = None
        self._PlanType = None
        self._AutoUseVoucher = None

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def PlanType(self):
        return self._PlanType

    @PlanType.setter
    def PlanType(self, PlanType):
        self._PlanType = PlanType

    @property
    def AutoUseVoucher(self):
        return self._AutoUseVoucher

    @AutoUseVoucher.setter
    def AutoUseVoucher(self, AutoUseVoucher):
        self._AutoUseVoucher = AutoUseVoucher


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._PlanType = params.get("PlanType")
        self._AutoUseVoucher = params.get("AutoUseVoucher")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradePlanResponse(AbstractModel):
    """UpgradePlan response structure.

    """

    def __init__(self):
        r"""
        :param _DealName: Order number.
        :type DealName: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DealName = None
        self._RequestId = None

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class UpstreamHttp2(AbstractModel):
    """HTTP2 origin-pull configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable HTTP2 origin-pull. Valid values: 
<li>`on`: Enable;</li>
<li>`off`: Disable.</li>
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VanityNameServers(AbstractModel):
    """Custom name servers

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable custom name servers. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param _Servers: List of custom name servers
        :type Servers: list of str
        """
        self._Switch = None
        self._Servers = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Servers(self):
        return self._Servers

    @Servers.setter
    def Servers(self, Servers):
        self._Servers = Servers


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Servers = params.get("Servers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VanityNameServersIps(AbstractModel):
    """IP information of the custom name server

    """

    def __init__(self):
        r"""
        :param _Name: Custom name of the name server
        :type Name: str
        :param _IPv4: IPv4 address of the custom name server
        :type IPv4: str
        """
        self._Name = None
        self._IPv4 = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IPv4(self):
        return self._IPv4

    @IPv4.setter
    def IPv4(self, IPv4):
        self._IPv4 = IPv4


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._IPv4 = params.get("IPv4")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyOwnershipRequest(AbstractModel):
    """VerifyOwnership request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Site or acceleration domain name
        :type Domain: str
        """
        self._Domain = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyOwnershipResponse(AbstractModel):
    """VerifyOwnership response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Result of ownership verification
<li>`success`: Verification passed</li>
<li>`fail`: Verification failed</li>
        :type Status: str
        :param _Result: When the ownership verification result is `fail`, this field returns the reason of failure.
        :type Result: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._Result = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class Waf(AbstractModel):
    """N/A

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable WAF. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param _PolicyId: ID of the policy
        :type PolicyId: int
        """
        self._Switch = None
        self._PolicyId = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WafConfig(AbstractModel):
    """WAF configuration.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable WAF configuration. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>The configuration can be modified even when it is disabled.
        :type Switch: str
        :param _Level: The protection level. Values:
<li>`loose`: Loose</li>
<li>`normal`: Moderate</li>
<li>`strict`: Strict</li>
<li>`stricter`: Super strict</li>
<li>`custom`: Custom</li>
        :type Level: str
        :param _Mode: The WAF global mode. Values:
<li>`block`: Block globally</li>
<li>`observe`: Observe globally</li>
        :type Mode: str
        :param _WafRule: The settings of the managed rule. If it is null, the settings that were last configured will be used.
        :type WafRule: :class:`tencentcloud.teo.v20220901.models.WafRule`
        :param _AiRule: The setting of the AI rule engine. If it is null, the setting that was last configured will be used.
        :type AiRule: :class:`tencentcloud.teo.v20220901.models.AiRule`
        """
        self._Switch = None
        self._Level = None
        self._Mode = None
        self._WafRule = None
        self._AiRule = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def WafRule(self):
        return self._WafRule

    @WafRule.setter
    def WafRule(self, WafRule):
        self._WafRule = WafRule

    @property
    def AiRule(self):
        return self._AiRule

    @AiRule.setter
    def AiRule(self, AiRule):
        self._AiRule = AiRule


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Level = params.get("Level")
        self._Mode = params.get("Mode")
        if params.get("WafRule") is not None:
            self._WafRule = WafRule()
            self._WafRule._deserialize(params.get("WafRule"))
        if params.get("AiRule") is not None:
            self._AiRule = AiRule()
            self._AiRule._deserialize(params.get("AiRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WafRule(AbstractModel):
    """WAF rule

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable managed rules. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param _BlockRuleIDs: IDs of the rules to be disabled.
        :type BlockRuleIDs: list of int
        :param _ObserveRuleIDs: IDs of the rules to be executed in Observe mode.
        :type ObserveRuleIDs: list of int
        """
        self._Switch = None
        self._BlockRuleIDs = None
        self._ObserveRuleIDs = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def BlockRuleIDs(self):
        return self._BlockRuleIDs

    @BlockRuleIDs.setter
    def BlockRuleIDs(self, BlockRuleIDs):
        self._BlockRuleIDs = BlockRuleIDs

    @property
    def ObserveRuleIDs(self):
        return self._ObserveRuleIDs

    @ObserveRuleIDs.setter
    def ObserveRuleIDs(self, ObserveRuleIDs):
        self._ObserveRuleIDs = ObserveRuleIDs


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._BlockRuleIDs = params.get("BlockRuleIDs")
        self._ObserveRuleIDs = params.get("ObserveRuleIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebSocket(AbstractModel):
    """WebSocket configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable WebSocket connection timeout. Values:
<li>`on`: The field "Timeout" can be configured.</li>
<li>`off`: The field "Timeout" is fixed to 15 seconds.</li>
        :type Switch: str
        :param _Timeout: The timeout period in seconds. Maximum value: 120.
        :type Timeout: int
        """
        self._Switch = None
        self._Timeout = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Timeout(self):
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Timeout = params.get("Timeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Zone(AbstractModel):
    """Site information

    """

    def __init__(self):
        r"""
        :param _ZoneId: Site ID.
        :type ZoneId: str
        :param _ZoneName: The site name.
        :type ZoneName: str
        :param _OriginalNameServers: List of name servers used by the site
        :type OriginalNameServers: list of str
        :param _NameServers: The list of name servers assigned by Tencent Cloud.
        :type NameServers: list of str
        :param _Status: The site status. Values:
u200c<li>`active`: The name server is switched to EdgeOne.</li>
u200c<li>`pending`: The name server is not switched.</li>
u200c<li>`moved`: The name server is changed to other service providers.</li>
u200c<li>`deactivated`: The site is blocked.</li>
<li>`initializing`: The site is not bound with any plan. </li>
        :type Status: str
        :param _Type: Site access method. Valid values:
<li>full: NS access;</li>
<li>partial: CNAME access;</li>
<li>noDomainAccess: access with no domain name.</li>
        :type Type: str
        :param _Paused: Whether the site is disabled.
        :type Paused: bool
        :param _CnameSpeedUp: Whether CNAME acceleration is enabled. Values:
<li>`enabled`: Enabled</li>
<li>`disabled`: Disabled</li>
        :type CnameSpeedUp: str
        :param _CnameStatus: CNAME record access status. Values:
<li>`finished`: The site is verified.</li>
<li>`pending`: The site is being verified.</li>
        :type CnameStatus: str
        :param _Tags: The list of resource tags.
        :type Tags: list of Tag
        :param _Resources: The list of billable resources.
        :type Resources: list of Resource
        :param _CreatedOn: The creation time of the site.
        :type CreatedOn: str
        :param _ModifiedOn: The modification date of the site.
        :type ModifiedOn: str
        :param _Area: The site access region. Values:
<li>`global`: Global.</li>
<li>`mainland`: Chinese mainland.</li>
<li>`overseas`: Outside the Chinese mainland.</li>
        :type Area: str
        :param _VanityNameServers: The custom name server information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VanityNameServers: :class:`tencentcloud.teo.v20220901.models.VanityNameServers`
        :param _VanityNameServersIps: The custom name server IP information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VanityNameServersIps: list of VanityNameServersIps
        :param _ActiveStatus: Status of the proxy. Values:
<li>`active`: Enabled</li>
<li>`inactive`: Not activated</li>
<li>`paused`: Disabled</li>
        :type ActiveStatus: str
        :param _AliasZoneName: The site alias. It can be up to 20 characters consisting of digits, letters, hyphens (-) and underscores (_).
Note: This field may return null, indicating that no valid values can be obtained.
        :type AliasZoneName: str
        :param _IsFake: Whether it’s a fake site. Valid values: 
<li>`0`: Non-fake site;</li>
<li>`1`: Fake site.</li>
        :type IsFake: int
        :param _LockStatus: Lock status. Values: <li>`enable`: Normal. Modification is allowed.</li><li>`disable`: Locked. Modification is not allowed.</li><li>`plan_migrate`: Adjusting the plan. Modification is not allowed.</li> 
        :type LockStatus: str
        :param _OwnershipVerification: Ownership verification information
Note: This field may return·null, indicating that no valid values can be obtained.
        :type OwnershipVerification: :class:`tencentcloud.teo.v20220901.models.OwnershipVerification`
        """
        self._ZoneId = None
        self._ZoneName = None
        self._OriginalNameServers = None
        self._NameServers = None
        self._Status = None
        self._Type = None
        self._Paused = None
        self._CnameSpeedUp = None
        self._CnameStatus = None
        self._Tags = None
        self._Resources = None
        self._CreatedOn = None
        self._ModifiedOn = None
        self._Area = None
        self._VanityNameServers = None
        self._VanityNameServersIps = None
        self._ActiveStatus = None
        self._AliasZoneName = None
        self._IsFake = None
        self._LockStatus = None
        self._OwnershipVerification = None

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
    def OriginalNameServers(self):
        return self._OriginalNameServers

    @OriginalNameServers.setter
    def OriginalNameServers(self, OriginalNameServers):
        self._OriginalNameServers = OriginalNameServers

    @property
    def NameServers(self):
        return self._NameServers

    @NameServers.setter
    def NameServers(self, NameServers):
        self._NameServers = NameServers

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Paused(self):
        return self._Paused

    @Paused.setter
    def Paused(self, Paused):
        self._Paused = Paused

    @property
    def CnameSpeedUp(self):
        return self._CnameSpeedUp

    @CnameSpeedUp.setter
    def CnameSpeedUp(self, CnameSpeedUp):
        self._CnameSpeedUp = CnameSpeedUp

    @property
    def CnameStatus(self):
        return self._CnameStatus

    @CnameStatus.setter
    def CnameStatus(self, CnameStatus):
        self._CnameStatus = CnameStatus

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Resources(self):
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def CreatedOn(self):
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def ModifiedOn(self):
        return self._ModifiedOn

    @ModifiedOn.setter
    def ModifiedOn(self, ModifiedOn):
        self._ModifiedOn = ModifiedOn

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VanityNameServers(self):
        return self._VanityNameServers

    @VanityNameServers.setter
    def VanityNameServers(self, VanityNameServers):
        self._VanityNameServers = VanityNameServers

    @property
    def VanityNameServersIps(self):
        return self._VanityNameServersIps

    @VanityNameServersIps.setter
    def VanityNameServersIps(self, VanityNameServersIps):
        self._VanityNameServersIps = VanityNameServersIps

    @property
    def ActiveStatus(self):
        return self._ActiveStatus

    @ActiveStatus.setter
    def ActiveStatus(self, ActiveStatus):
        self._ActiveStatus = ActiveStatus

    @property
    def AliasZoneName(self):
        return self._AliasZoneName

    @AliasZoneName.setter
    def AliasZoneName(self, AliasZoneName):
        self._AliasZoneName = AliasZoneName

    @property
    def IsFake(self):
        return self._IsFake

    @IsFake.setter
    def IsFake(self, IsFake):
        self._IsFake = IsFake

    @property
    def LockStatus(self):
        return self._LockStatus

    @LockStatus.setter
    def LockStatus(self, LockStatus):
        self._LockStatus = LockStatus

    @property
    def OwnershipVerification(self):
        return self._OwnershipVerification

    @OwnershipVerification.setter
    def OwnershipVerification(self, OwnershipVerification):
        self._OwnershipVerification = OwnershipVerification


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._OriginalNameServers = params.get("OriginalNameServers")
        self._NameServers = params.get("NameServers")
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._Paused = params.get("Paused")
        self._CnameSpeedUp = params.get("CnameSpeedUp")
        self._CnameStatus = params.get("CnameStatus")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("Resources") is not None:
            self._Resources = []
            for item in params.get("Resources"):
                obj = Resource()
                obj._deserialize(item)
                self._Resources.append(obj)
        self._CreatedOn = params.get("CreatedOn")
        self._ModifiedOn = params.get("ModifiedOn")
        self._Area = params.get("Area")
        if params.get("VanityNameServers") is not None:
            self._VanityNameServers = VanityNameServers()
            self._VanityNameServers._deserialize(params.get("VanityNameServers"))
        if params.get("VanityNameServersIps") is not None:
            self._VanityNameServersIps = []
            for item in params.get("VanityNameServersIps"):
                obj = VanityNameServersIps()
                obj._deserialize(item)
                self._VanityNameServersIps.append(obj)
        self._ActiveStatus = params.get("ActiveStatus")
        self._AliasZoneName = params.get("AliasZoneName")
        self._IsFake = params.get("IsFake")
        self._LockStatus = params.get("LockStatus")
        if params.get("OwnershipVerification") is not None:
            self._OwnershipVerification = OwnershipVerification()
            self._OwnershipVerification._deserialize(params.get("OwnershipVerification"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneSetting(AbstractModel):
    """The site configuration.

    """

    def __init__(self):
        r"""
        :param _ZoneName: Name of the site
        :type ZoneName: str
        :param _Area: Site acceleration region. Values:
<li>`mainland`: Acceleration in the Chinese mainland.</li>
<li>`overseas`: Acceleration outside the Chinese mainland.</li>
        :type Area: str
        :param _CacheKey: Node cache key configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type CacheKey: :class:`tencentcloud.teo.v20220901.models.CacheKey`
        :param _Quic: The QUIC access configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Quic: :class:`tencentcloud.teo.v20220901.models.Quic`
        :param _PostMaxSize: The POST transport configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PostMaxSize: :class:`tencentcloud.teo.v20220901.models.PostMaxSize`
        :param _Compression: Smart compression configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Compression: :class:`tencentcloud.teo.v20220901.models.Compression`
        :param _UpstreamHttp2: HTTP2 origin-pull configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpstreamHttp2: :class:`tencentcloud.teo.v20220901.models.UpstreamHttp2`
        :param _ForceRedirect: Force HTTPS redirect configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type ForceRedirect: :class:`tencentcloud.teo.v20220901.models.ForceRedirect`
        :param _CacheConfig: Cache expiration time configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type CacheConfig: :class:`tencentcloud.teo.v20220901.models.CacheConfig`
        :param _Origin: Origin server configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Origin: :class:`tencentcloud.teo.v20220901.models.Origin`
        :param _SmartRouting: Smart acceleration configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type SmartRouting: :class:`tencentcloud.teo.v20220901.models.SmartRouting`
        :param _MaxAge: Browser cache configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxAge: :class:`tencentcloud.teo.v20220901.models.MaxAge`
        :param _OfflineCache: The offline cache configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OfflineCache: :class:`tencentcloud.teo.v20220901.models.OfflineCache`
        :param _WebSocket: WebSocket configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type WebSocket: :class:`tencentcloud.teo.v20220901.models.WebSocket`
        :param _ClientIpHeader: Origin-pull client IP header configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClientIpHeader: :class:`tencentcloud.teo.v20220901.models.ClientIpHeader`
        :param _CachePrefresh: Cache prefresh configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type CachePrefresh: :class:`tencentcloud.teo.v20220901.models.CachePrefresh`
        :param _Ipv6: IPv6 access configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type Ipv6: :class:`tencentcloud.teo.v20220901.models.Ipv6`
        :param _Https: HTTPS acceleration configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type Https: :class:`tencentcloud.teo.v20220901.models.Https`
        :param _ClientIpCountry: Whether to carry the location information of the client IP during origin-pull.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ClientIpCountry: :class:`tencentcloud.teo.v20220901.models.ClientIpCountry`
        :param _Grpc: Configuration of gRPC support
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Grpc: :class:`tencentcloud.teo.v20220901.models.Grpc`
        :param _ImageOptimize: Image optimization configuration. 
Note: This field may return `null`, indicating that no valid value was found.
        :type ImageOptimize: :class:`tencentcloud.teo.v20220901.models.ImageOptimize`
        :param _AccelerateMainland: Cross-MLC-border acceleration. 
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AccelerateMainland: :class:`tencentcloud.teo.v20220901.models.AccelerateMainland`
        :param _StandardDebug: Standard debugging configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type StandardDebug: :class:`tencentcloud.teo.v20220901.models.StandardDebug`
        """
        self._ZoneName = None
        self._Area = None
        self._CacheKey = None
        self._Quic = None
        self._PostMaxSize = None
        self._Compression = None
        self._UpstreamHttp2 = None
        self._ForceRedirect = None
        self._CacheConfig = None
        self._Origin = None
        self._SmartRouting = None
        self._MaxAge = None
        self._OfflineCache = None
        self._WebSocket = None
        self._ClientIpHeader = None
        self._CachePrefresh = None
        self._Ipv6 = None
        self._Https = None
        self._ClientIpCountry = None
        self._Grpc = None
        self._ImageOptimize = None
        self._AccelerateMainland = None
        self._StandardDebug = None

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def CacheKey(self):
        return self._CacheKey

    @CacheKey.setter
    def CacheKey(self, CacheKey):
        self._CacheKey = CacheKey

    @property
    def Quic(self):
        return self._Quic

    @Quic.setter
    def Quic(self, Quic):
        self._Quic = Quic

    @property
    def PostMaxSize(self):
        return self._PostMaxSize

    @PostMaxSize.setter
    def PostMaxSize(self, PostMaxSize):
        self._PostMaxSize = PostMaxSize

    @property
    def Compression(self):
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression

    @property
    def UpstreamHttp2(self):
        return self._UpstreamHttp2

    @UpstreamHttp2.setter
    def UpstreamHttp2(self, UpstreamHttp2):
        self._UpstreamHttp2 = UpstreamHttp2

    @property
    def ForceRedirect(self):
        return self._ForceRedirect

    @ForceRedirect.setter
    def ForceRedirect(self, ForceRedirect):
        self._ForceRedirect = ForceRedirect

    @property
    def CacheConfig(self):
        return self._CacheConfig

    @CacheConfig.setter
    def CacheConfig(self, CacheConfig):
        self._CacheConfig = CacheConfig

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def SmartRouting(self):
        return self._SmartRouting

    @SmartRouting.setter
    def SmartRouting(self, SmartRouting):
        self._SmartRouting = SmartRouting

    @property
    def MaxAge(self):
        return self._MaxAge

    @MaxAge.setter
    def MaxAge(self, MaxAge):
        self._MaxAge = MaxAge

    @property
    def OfflineCache(self):
        return self._OfflineCache

    @OfflineCache.setter
    def OfflineCache(self, OfflineCache):
        self._OfflineCache = OfflineCache

    @property
    def WebSocket(self):
        return self._WebSocket

    @WebSocket.setter
    def WebSocket(self, WebSocket):
        self._WebSocket = WebSocket

    @property
    def ClientIpHeader(self):
        return self._ClientIpHeader

    @ClientIpHeader.setter
    def ClientIpHeader(self, ClientIpHeader):
        self._ClientIpHeader = ClientIpHeader

    @property
    def CachePrefresh(self):
        return self._CachePrefresh

    @CachePrefresh.setter
    def CachePrefresh(self, CachePrefresh):
        self._CachePrefresh = CachePrefresh

    @property
    def Ipv6(self):
        return self._Ipv6

    @Ipv6.setter
    def Ipv6(self, Ipv6):
        self._Ipv6 = Ipv6

    @property
    def Https(self):
        return self._Https

    @Https.setter
    def Https(self, Https):
        self._Https = Https

    @property
    def ClientIpCountry(self):
        return self._ClientIpCountry

    @ClientIpCountry.setter
    def ClientIpCountry(self, ClientIpCountry):
        self._ClientIpCountry = ClientIpCountry

    @property
    def Grpc(self):
        return self._Grpc

    @Grpc.setter
    def Grpc(self, Grpc):
        self._Grpc = Grpc

    @property
    def ImageOptimize(self):
        return self._ImageOptimize

    @ImageOptimize.setter
    def ImageOptimize(self, ImageOptimize):
        self._ImageOptimize = ImageOptimize

    @property
    def AccelerateMainland(self):
        return self._AccelerateMainland

    @AccelerateMainland.setter
    def AccelerateMainland(self, AccelerateMainland):
        self._AccelerateMainland = AccelerateMainland

    @property
    def StandardDebug(self):
        return self._StandardDebug

    @StandardDebug.setter
    def StandardDebug(self, StandardDebug):
        self._StandardDebug = StandardDebug


    def _deserialize(self, params):
        self._ZoneName = params.get("ZoneName")
        self._Area = params.get("Area")
        if params.get("CacheKey") is not None:
            self._CacheKey = CacheKey()
            self._CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Quic") is not None:
            self._Quic = Quic()
            self._Quic._deserialize(params.get("Quic"))
        if params.get("PostMaxSize") is not None:
            self._PostMaxSize = PostMaxSize()
            self._PostMaxSize._deserialize(params.get("PostMaxSize"))
        if params.get("Compression") is not None:
            self._Compression = Compression()
            self._Compression._deserialize(params.get("Compression"))
        if params.get("UpstreamHttp2") is not None:
            self._UpstreamHttp2 = UpstreamHttp2()
            self._UpstreamHttp2._deserialize(params.get("UpstreamHttp2"))
        if params.get("ForceRedirect") is not None:
            self._ForceRedirect = ForceRedirect()
            self._ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("CacheConfig") is not None:
            self._CacheConfig = CacheConfig()
            self._CacheConfig._deserialize(params.get("CacheConfig"))
        if params.get("Origin") is not None:
            self._Origin = Origin()
            self._Origin._deserialize(params.get("Origin"))
        if params.get("SmartRouting") is not None:
            self._SmartRouting = SmartRouting()
            self._SmartRouting._deserialize(params.get("SmartRouting"))
        if params.get("MaxAge") is not None:
            self._MaxAge = MaxAge()
            self._MaxAge._deserialize(params.get("MaxAge"))
        if params.get("OfflineCache") is not None:
            self._OfflineCache = OfflineCache()
            self._OfflineCache._deserialize(params.get("OfflineCache"))
        if params.get("WebSocket") is not None:
            self._WebSocket = WebSocket()
            self._WebSocket._deserialize(params.get("WebSocket"))
        if params.get("ClientIpHeader") is not None:
            self._ClientIpHeader = ClientIpHeader()
            self._ClientIpHeader._deserialize(params.get("ClientIpHeader"))
        if params.get("CachePrefresh") is not None:
            self._CachePrefresh = CachePrefresh()
            self._CachePrefresh._deserialize(params.get("CachePrefresh"))
        if params.get("Ipv6") is not None:
            self._Ipv6 = Ipv6()
            self._Ipv6._deserialize(params.get("Ipv6"))
        if params.get("Https") is not None:
            self._Https = Https()
            self._Https._deserialize(params.get("Https"))
        if params.get("ClientIpCountry") is not None:
            self._ClientIpCountry = ClientIpCountry()
            self._ClientIpCountry._deserialize(params.get("ClientIpCountry"))
        if params.get("Grpc") is not None:
            self._Grpc = Grpc()
            self._Grpc._deserialize(params.get("Grpc"))
        if params.get("ImageOptimize") is not None:
            self._ImageOptimize = ImageOptimize()
            self._ImageOptimize._deserialize(params.get("ImageOptimize"))
        if params.get("AccelerateMainland") is not None:
            self._AccelerateMainland = AccelerateMainland()
            self._AccelerateMainland._deserialize(params.get("AccelerateMainland"))
        if params.get("StandardDebug") is not None:
            self._StandardDebug = StandardDebug()
            self._StandardDebug._deserialize(params.get("StandardDebug"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        