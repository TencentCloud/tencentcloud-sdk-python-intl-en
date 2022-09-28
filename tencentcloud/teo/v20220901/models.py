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


class AccelerateType(AbstractModel):
    """Acceleration type

    """

    def __init__(self):
        r"""
        :param Switch: Acceleration switch. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Action(AbstractModel):
    """Rule engine feature operation. A feature can be of only one of the following three types, so each item in the `RuleAction` array can be of only one of the following types. You can call the [DescribeRulesSetting](https://tcloud4api.woa.com/document/product/1657/79433?!preview&!document=1) API to view more requirements for entering feature items.

    """

    def __init__(self):
        r"""
        :param NormalAction: Common feature operation. Features of this type include:
<li>`AccessUrlRedirect`: Access URL rewrite.</li>
<li>`UpstreamUrlRedirect`: Origin-pull URL rewrite.</li>
<li>`QUIC`: QUIC.</li>
<li>`WebSocket`: WebSocket.</li>
<li>`VideoSeek`: Video dragging.</li>
<li>`Authentication`: Token authentication.</li>
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
<li>`Hsts`.</li>
<li>`ClientIpHeader`.</li>
<li>`TlsVersion`.</li>
<li>`OcspStapling`.</li>
<li>`Http2`: HTTP/2 access.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type NormalAction: :class:`tencentcloud.teo.v20220901.models.NormalAction`
        :param RewriteAction: Feature operation with a request/response header. Features of this type include:
<li>`RequestHeader`: HTTP request header modification.</li>
<li>`ResponseHeader`: HTTP response header modification.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type RewriteAction: :class:`tencentcloud.teo.v20220901.models.RewriteAction`
        :param CodeAction: Feature operation with a status code. Features of this type include:
<li>`ErrorPage`: Custom error page.</li>
<li>`StatusCodeCache`: Status code cache TTL.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type CodeAction: :class:`tencentcloud.teo.v20220901.models.CodeAction`
        """
        self.NormalAction = None
        self.RewriteAction = None
        self.CodeAction = None


    def _deserialize(self, params):
        if params.get("NormalAction") is not None:
            self.NormalAction = NormalAction()
            self.NormalAction._deserialize(params.get("NormalAction"))
        if params.get("RewriteAction") is not None:
            self.RewriteAction = RewriteAction()
            self.RewriteAction._deserialize(params.get("RewriteAction"))
        if params.get("CodeAction") is not None:
            self.CodeAction = CodeAction()
            self.CodeAction._deserialize(params.get("CodeAction"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedFilter(AbstractModel):
    """Key-value pair filters for conditional filtering queries and fuzzy queries, such as filtering ID, name, and status.
    If there are multiple filters, they’re combined with `AND`.
    Values of the same Filter are combined with `OR`.

    """

    def __init__(self):
        r"""
        :param Name: The name of the field to filter.
        :type Name: str
        :param Values: Values of the filtered field.
        :type Values: list of str
        :param Fuzzy: Whether to enable fuzzy query.
        :type Fuzzy: bool
        """
        self.Name = None
        self.Values = None
        self.Fuzzy = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        self.Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AscriptionInfo(AbstractModel):
    """The site ownership information

    """

    def __init__(self):
        r"""
        :param Subdomain: 
        :type Subdomain: str
        :param RecordType: The record type.
        :type RecordType: str
        :param RecordValue: The record value.
        :type RecordValue: str
        """
        self.Subdomain = None
        self.RecordType = None
        self.RecordValue = None


    def _deserialize(self, params):
        self.Subdomain = params.get("Subdomain")
        self.RecordType = params.get("RecordType")
        self.RecordValue = params.get("RecordValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillingDataFilter(AbstractModel):
    """A parameter that filters DNS data

    """

    def __init__(self):
        r"""
        :param Type: Parameter name. Valid values:
`zone`: Site name
`host`: Domain name
`proxy`: L4 proxy
`plan`: Plan type
        :type Type: str
        :param Value: Parameter value
        :type Value: str
        """
        self.Type = None
        self.Value = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotLog(AbstractModel):
    """Bot attack log

    """

    def __init__(self):
        r"""
        :param AttackTime: The attack time recorded in seconds using UNIX timestamp.
        :type AttackTime: int
        :param AttackIp: The attacker IP.
        :type AttackIp: str
        :param Domain: The attacked domain name.
        :type Domain: str
        :param RequestUri: The URI.
        :type RequestUri: str
        :param AttackType: Attack type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackType: str
        :param RequestMethod: Request method.
        :type RequestMethod: str
        :param AttackContent: The attack content.
        :type AttackContent: str
        :param RiskLevel: The attack level.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RiskLevel: str
        :param RuleId: The rule ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleId: int
        :param SipCountryCode: The country code of the attacker IP, which is defined in ISO-3166 alpha-2. For the list of country codes, see [ISO-3166](https://git.woa.com/edgeone/iso-3166/blob/master/all/all.json).
        :type SipCountryCode: str
        :param EventId: The attack event ID.
        :type EventId: str
        :param DisposalMethod: The processing method.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DisposalMethod: str
        :param HttpLog: The HTTP log.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HttpLog: str
        :param Ua: The user agent.
        :type Ua: str
        :param DetectionMethod: The detection method.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DetectionMethod: str
        :param Confidence: The credibility level.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Confidence: str
        :param Maliciousness: Maliciousness
Note: This field may return null, indicating that no valid values can be obtained.
        :type Maliciousness: str
        :param RuleDetailList: The security rule information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleDetailList: list of SecRuleRelatedInfo
        :param Label: The bot tag.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Label: str
        """
        self.AttackTime = None
        self.AttackIp = None
        self.Domain = None
        self.RequestUri = None
        self.AttackType = None
        self.RequestMethod = None
        self.AttackContent = None
        self.RiskLevel = None
        self.RuleId = None
        self.SipCountryCode = None
        self.EventId = None
        self.DisposalMethod = None
        self.HttpLog = None
        self.Ua = None
        self.DetectionMethod = None
        self.Confidence = None
        self.Maliciousness = None
        self.RuleDetailList = None
        self.Label = None


    def _deserialize(self, params):
        self.AttackTime = params.get("AttackTime")
        self.AttackIp = params.get("AttackIp")
        self.Domain = params.get("Domain")
        self.RequestUri = params.get("RequestUri")
        self.AttackType = params.get("AttackType")
        self.RequestMethod = params.get("RequestMethod")
        self.AttackContent = params.get("AttackContent")
        self.RiskLevel = params.get("RiskLevel")
        self.RuleId = params.get("RuleId")
        self.SipCountryCode = params.get("SipCountryCode")
        self.EventId = params.get("EventId")
        self.DisposalMethod = params.get("DisposalMethod")
        self.HttpLog = params.get("HttpLog")
        self.Ua = params.get("Ua")
        self.DetectionMethod = params.get("DetectionMethod")
        self.Confidence = params.get("Confidence")
        self.Maliciousness = params.get("Maliciousness")
        if params.get("RuleDetailList") is not None:
            self.RuleDetailList = []
            for item in params.get("RuleDetailList"):
                obj = SecRuleRelatedInfo()
                obj._deserialize(item)
                self.RuleDetailList.append(obj)
        self.Label = params.get("Label")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CC(AbstractModel):
    """CC configuration item.

    """

    def __init__(self):
        r"""
        :param Switch: WAF switch. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param PolicyId: ID of the policy
        :type PolicyId: int
        """
        self.Switch = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCInterceptEvent(AbstractModel):
    """CC block event

    """

    def __init__(self):
        r"""
        :param ClientIp: The client IP.
        :type ClientIp: str
        :param InterceptNum: The requests per minute that are blocked.
        :type InterceptNum: int
        :param InterceptTime: Block time in seconds.
        :type InterceptTime: int
        """
        self.ClientIp = None
        self.InterceptNum = None
        self.InterceptTime = None


    def _deserialize(self, params):
        self.ClientIp = params.get("ClientIp")
        self.InterceptNum = params.get("InterceptNum")
        self.InterceptTime = params.get("InterceptTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Cache(AbstractModel):
    """Cache time settings

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable cache configuration. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param CacheTime: Cache expiration time setting.
Unit: second. The maximum value is 365 days.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CacheTime: int
        :param IgnoreCacheControl: Whether to enable force cache. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IgnoreCacheControl: str
        """
        self.Switch = None
        self.CacheTime = None
        self.IgnoreCacheControl = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.CacheTime = params.get("CacheTime")
        self.IgnoreCacheControl = params.get("IgnoreCacheControl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfig(AbstractModel):
    """Cache rule configuration.

    """

    def __init__(self):
        r"""
        :param Cache: Cache configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type Cache: :class:`tencentcloud.teo.v20220901.models.Cache`
        :param NoCache: No-cache configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type NoCache: :class:`tencentcloud.teo.v20220901.models.NoCache`
        :param FollowOrigin: Follows the origin server configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type FollowOrigin: :class:`tencentcloud.teo.v20220901.models.FollowOrigin`
        """
        self.Cache = None
        self.NoCache = None
        self.FollowOrigin = None


    def _deserialize(self, params):
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("NoCache") is not None:
            self.NoCache = NoCache()
            self.NoCache._deserialize(params.get("NoCache"))
        if params.get("FollowOrigin") is not None:
            self.FollowOrigin = FollowOrigin()
            self.FollowOrigin._deserialize(params.get("FollowOrigin"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheKey(AbstractModel):
    """The cache key configuration.

    """

    def __init__(self):
        r"""
        :param FullUrlCache: Whether to enable full-path cache. Values:
<li>`on`: Enable full-path cache (i.e., disable Ignore Query String).</li>
<li>`off`: Disable full-path cache (i.e., enable Ignore Query String).</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type FullUrlCache: str
        :param IgnoreCase: Whether to ignore case in the cache key. Values:
<li>`on`: Ignore</li>
<li>`off`: Not ignore</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IgnoreCase: str
        :param QueryString: Request parameter contained in `CacheKey`
Note: This field may return null, indicating that no valid values can be obtained.
        :type QueryString: :class:`tencentcloud.teo.v20220901.models.QueryString`
        """
        self.FullUrlCache = None
        self.IgnoreCase = None
        self.QueryString = None


    def _deserialize(self, params):
        self.FullUrlCache = params.get("FullUrlCache")
        self.IgnoreCase = params.get("IgnoreCase")
        if params.get("QueryString") is not None:
            self.QueryString = QueryString()
            self.QueryString._deserialize(params.get("QueryString"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CachePrefresh(AbstractModel):
    """Cache prefresh

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable cache prefresh. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param Percent: The cache prefresh percentage. Values: 1-99
Note: This field may return null, indicating that no valid values can be obtained.
        :type Percent: int
        """
        self.Switch = None
        self.Percent = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Percent = params.get("Percent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCertificateRequest(AbstractModel):
    """CheckCertificate request structure.

    """

    def __init__(self):
        r"""
        :param Certificate: Content of the certificate.
        :type Certificate: str
        :param PrivateKey: Content of the private key.
        :type PrivateKey: str
        """
        self.Certificate = None
        self.PrivateKey = None


    def _deserialize(self, params):
        self.Certificate = params.get("Certificate")
        self.PrivateKey = params.get("PrivateKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCertificateResponse(AbstractModel):
    """CheckCertificate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ClientIpCountry(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param Switch: 
        :type Switch: str
        :param HeaderName: 
        :type HeaderName: str
        """
        self.Switch = None
        self.HeaderName = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.HeaderName = params.get("HeaderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClientIpHeader(AbstractModel):
    """The client IP header configuration

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable the configuration. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param HeaderName: The name of the HTTP header that contains the client IP, which is used for forwarding.
If this field is not specified, the default value `X-Forwarded-IP` will be used.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HeaderName: str
        """
        self.Switch = None
        self.HeaderName = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.HeaderName = params.get("HeaderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClientRule(AbstractModel):
    """The client rule information

    """

    def __init__(self):
        r"""
        :param ClientIp: The client IP.
        :type ClientIp: str
        :param RuleType: The rule type.
        :type RuleType: str
        :param RuleId: The rule ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleId: int
        :param Description: The rule description.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param IpStatus: The blocking status. Values:
<li>`block`: Block;</li>
<li>`allow`: Allow.</li>
        :type IpStatus: str
        :param BlockTime: The blocking time recorded in UNIX timestamp.
        :type BlockTime: int
        :param Id: The data entry ID.
        :type Id: str
        """
        self.ClientIp = None
        self.RuleType = None
        self.RuleId = None
        self.Description = None
        self.IpStatus = None
        self.BlockTime = None
        self.Id = None


    def _deserialize(self, params):
        self.ClientIp = params.get("ClientIp")
        self.RuleType = params.get("RuleType")
        self.RuleId = params.get("RuleId")
        self.Description = params.get("Description")
        self.IpStatus = params.get("IpStatus")
        self.BlockTime = params.get("BlockTime")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClsLogTopicInfo(AbstractModel):
    """The log topic information

    """

    def __init__(self):
        r"""
        :param TaskName: Name of the task.
        :type TaskName: str
        :param ZoneName: Name of the site.
        :type ZoneName: str
        :param LogSetId: ID of the logset.
        :type LogSetId: str
        :param TopicId: ID of the log topic.
        :type TopicId: str
        :param EntityType: Type of the task.
        :type EntityType: str
        :param Period: Retention period of the log topic.
        :type Period: int
        :param Enabled: Whether the log topic is enabled.
        :type Enabled: bool
        :param Deleted: Whether the log topic is deleted.
        :type Deleted: str
        :param CreateTime: Creation time.
        :type CreateTime: str
        :param Target: Target location. Values:
<li>`cls`: Ship logs to CLS;</li>
<li>`custom_enpoint`: Ship logs to a custom address.</li>
        :type Target: str
        :param LogSetRegion: Region of the logset.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogSetRegion: str
        :param ZoneId: ID of the site.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneId: str
        :param Area: Acceleration region. Values:
<li>`mainland`: Chinese mainland;</li>
<li>`overseas`: Global (outside the Chinese mainland).</li>
        :type Area: str
        :param LogSetType: 
        :type LogSetType: str
        """
        self.TaskName = None
        self.ZoneName = None
        self.LogSetId = None
        self.TopicId = None
        self.EntityType = None
        self.Period = None
        self.Enabled = None
        self.Deleted = None
        self.CreateTime = None
        self.Target = None
        self.LogSetRegion = None
        self.ZoneId = None
        self.Area = None
        self.LogSetType = None


    def _deserialize(self, params):
        self.TaskName = params.get("TaskName")
        self.ZoneName = params.get("ZoneName")
        self.LogSetId = params.get("LogSetId")
        self.TopicId = params.get("TopicId")
        self.EntityType = params.get("EntityType")
        self.Period = params.get("Period")
        self.Enabled = params.get("Enabled")
        self.Deleted = params.get("Deleted")
        self.CreateTime = params.get("CreateTime")
        self.Target = params.get("Target")
        self.LogSetRegion = params.get("LogSetRegion")
        self.ZoneId = params.get("ZoneId")
        self.Area = params.get("Area")
        self.LogSetType = params.get("LogSetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeAction(AbstractModel):
    """Rule engine action with a status code

    """

    def __init__(self):
        r"""
        :param Action: Feature name. You can call the [DescribeRulesSetting](https://tcloud4api.woa.com/document/product/1657/79433?!preview&!document=1) API to view the requirements for entering the feature name.
        :type Action: str
        :param Parameters: Operation parameter.
        :type Parameters: list of RuleCodeActionParams
        """
        self.Action = None
        self.Parameters = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        if params.get("Parameters") is not None:
            self.Parameters = []
            for item in params.get("Parameters"):
                obj = RuleCodeActionParams()
                obj._deserialize(item)
                self.Parameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Compression(AbstractModel):
    """Smart compression configuration.

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable smart compression. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param Algorithms: Compression algorithm. Values:
<li>`brotli`: Brotli algorithm</li>
<li>`gzip`: Gzip algorithm</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Algorithms: list of str
        """
        self.Switch = None
        self.Algorithms = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Algorithms = params.get("Algorithms")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCredentialRequest(AbstractModel):
    """CreateCredential request structure.

    """


class CreateCredentialResponse(AbstractModel):
    """CreateCredential response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDnsRecordRequest(AbstractModel):
    """CreateDnsRecord request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID of the DNS record.
        :type ZoneId: str
        :param Type: The DNS record type. Values:
<li>`A`: Point a domain name to an IPv4 address, such as 8.8.8.8.</li>
<li>`AAAA`: Point a domain name to an IPv6 address.</li>
<li>`MX`: It is used for email servers. The record value and priority parameters are provided by email service providers. If there are multiple MX records, the lower the priority value, the higher the priority.</li>
<li>`CNAME`: Point a domain name to another domain name that can be resolved to an IP address.</li>
<li>`TXT`: Identify and describe a domain name. It is usually used for domain verification and as SPF records (for anti-spam).</li>
<li>`NS`: If you need to authorize a subdomain name to another DNS service provider for DNS resolution, you need to add an NS record. You cannot add an NS record for a root domain name.</li>
<li>`CAA`: Specify CAs to issue certificates for sites.</li>
<li>`SRV`: Identify a service used by a server. It is commonly used in Microsoft directory management.</li>
        :type Type: str
        :param Name: The DNS record name.
        :type Name: str
        :param Content: The DNS record content.
        :type Content: str
        :param Mode: The proxy mode. Values:
<li>`dns_only`: Only DNS</li>
<li>`proxied`: Proxied</li>
        :type Mode: str
        :param TTL: TTL (in seconds). The smaller the value, the faster the record changes take effect. Default value: 300
        :type TTL: int
        :param Priority: Specifies a value in the range 1–50 when you make changes to the MX records. A smaller value indicates higher priority. Note that the default value 0 will be used if this field is not specified.
        :type Priority: int
        """
        self.ZoneId = None
        self.Type = None
        self.Name = None
        self.Content = None
        self.Mode = None
        self.TTL = None
        self.Priority = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        self.Mode = params.get("Mode")
        self.TTL = params.get("TTL")
        self.Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDnsRecordResponse(AbstractModel):
    """CreateDnsRecord response structure.

    """

    def __init__(self):
        r"""
        :param DnsRecordId: The DNS record ID.
        :type DnsRecordId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DnsRecordId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DnsRecordId = params.get("DnsRecordId")
        self.RequestId = params.get("RequestId")


class CreateLogSetRequest(AbstractModel):
    """CreateLogSet request structure.

    """

    def __init__(self):
        r"""
        :param LogSetName: Name of the logset.
        :type LogSetName: str
        :param LogSetRegion: Region of the logset.
        :type LogSetRegion: str
        """
        self.LogSetName = None
        self.LogSetRegion = None


    def _deserialize(self, params):
        self.LogSetName = params.get("LogSetName")
        self.LogSetRegion = params.get("LogSetRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLogSetResponse(AbstractModel):
    """CreateLogSet response structure.

    """

    def __init__(self):
        r"""
        :param LogSetId: ID of the logset created.
        :type LogSetId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LogSetId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogSetId = params.get("LogSetId")
        self.RequestId = params.get("RequestId")


class CreateLogTopicTaskRequest(AbstractModel):
    """CreateLogTopicTask request structure.

    """

    def __init__(self):
        r"""
        :param LogSetId: ID of the logset.
        :type LogSetId: str
        :param LogSetRegion: Region of the logset.
        :type LogSetRegion: str
        :param TopicName: Topic name of the logset.
        :type TopicName: str
        :param TaskName: Name of the shipping task.
        :type TaskName: str
        :param ZoneId: ID of the site.
        :type ZoneId: str
        :param ZoneName: Name of the site.
        :type ZoneName: str
        :param EntityType: Type of the shipping entity. Values:
<li>`domain`: L7 acceleration logs;</li>
<li>`application`: L4 acceleration logs;</li>
<li>`web-rateLiming`: Rate limiting logs;</li>
<li>`web-attack`: Web security logs;</li>
<li>`web-rule`: Custom rule logs;</li>
<li>`web-bot`: Bot management logs.</li>
        :type EntityType: str
        :param Period: Retention period of the log topic. Value range: 1–366 (in days).
        :type Period: int
        :param EntityList: List of shipping entities.
        :type EntityList: list of str
        :param Area: Acceleration region. Values:
<li>`mainland`: Chinese mainland.</li>
<li>`overseas`: Global (outside the Chinese mainland).</li> If this field is not specified, the acceleration region will be determined based on the user’s region.
        :type Area: str
        """
        self.LogSetId = None
        self.LogSetRegion = None
        self.TopicName = None
        self.TaskName = None
        self.ZoneId = None
        self.ZoneName = None
        self.EntityType = None
        self.Period = None
        self.EntityList = None
        self.Area = None


    def _deserialize(self, params):
        self.LogSetId = params.get("LogSetId")
        self.LogSetRegion = params.get("LogSetRegion")
        self.TopicName = params.get("TopicName")
        self.TaskName = params.get("TaskName")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.EntityType = params.get("EntityType")
        self.Period = params.get("Period")
        self.EntityList = params.get("EntityList")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLogTopicTaskResponse(AbstractModel):
    """CreateLogTopicTask response structure.

    """

    def __init__(self):
        r"""
        :param TopicId: ID of the log topic created.
        :type TopicId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TopicId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.RequestId = params.get("RequestId")


class CreatePlanForZoneRequest(AbstractModel):
    """CreatePlanForZone request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site.
        :type ZoneId: str
        :param PlanType: Plan options available for purchase. Values:
<li>`sta`: Standard plan for global areas except Chinese mainland;</li>
<li>`sta_with_bot`: Standard plan for global areas except Chinese mainland, with extra bot management;</li>
<li>`sta_cm`: Standard plan for Chinese mainland;</li>
<li>`sta_cm_with_bot`: Standard plan for Chinese mainland, with extra bot management;</li>
<li>`ent`: Enterprise plan for global areas except Chinese mainland;</li>
<li>`ent_with_bot`: Enterprise plan for global areas except Chinese mainland, with extra bot management;</li>
<li>`ent_cm`: Enterprise plan for Chinese mainland;</li>
<li>`ent_cm_with_bot`: Enterprise plan for Chinese mainland, with extra bot management.</li>To get the available plan options for your account, view the output from <a href="https://tcloud4api.woa.com/document/product/1657/80124?!preview&!document=1">DescribeAvailablePlans</a>.
        :type PlanType: str
        """
        self.ZoneId = None
        self.PlanType = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.PlanType = params.get("PlanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePlanForZoneResponse(AbstractModel):
    """CreatePlanForZone response structure.

    """

    def __init__(self):
        r"""
        :param ResourceNames: List of purchased resources.
        :type ResourceNames: list of str
        :param DealNames: List or order numbers.
        :type DealNames: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ResourceNames = None
        self.DealNames = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResourceNames = params.get("ResourceNames")
        self.DealNames = params.get("DealNames")
        self.RequestId = params.get("RequestId")


class CreatePrefetchTaskRequest(AbstractModel):
    """CreatePrefetchTask request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site.
        :type ZoneId: str
        :param Targets: List of resources to be pre-warmed, for example:
http://www.example.com/example.txt
        :type Targets: list of str
        :param EncodeUrl: Whether to encode a URL according to RFC3986. Enable this field when the URL contains non-ASCII characters.
        :type EncodeUrl: bool
        :param Headers: HTTP header information
        :type Headers: list of Header
        """
        self.ZoneId = None
        self.Targets = None
        self.EncodeUrl = None
        self.Headers = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Targets = params.get("Targets")
        self.EncodeUrl = params.get("EncodeUrl")
        if params.get("Headers") is not None:
            self.Headers = []
            for item in params.get("Headers"):
                obj = Header()
                obj._deserialize(item)
                self.Headers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrefetchTaskResponse(AbstractModel):
    """CreatePrefetchTask response structure.

    """

    def __init__(self):
        r"""
        :param JobId: ID of the task.
        :type JobId: str
        :param FailedList: List of failed tasks.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FailedList: list of FailReason
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.JobId = None
        self.FailedList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        if params.get("FailedList") is not None:
            self.FailedList = []
            for item in params.get("FailedList"):
                obj = FailReason()
                obj._deserialize(item)
                self.FailedList.append(obj)
        self.RequestId = params.get("RequestId")


class CreatePurgeTaskRequest(AbstractModel):
    """CreatePurgeTask request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site.
        :type ZoneId: str
        :param Type: Purging mode. Values:
<li>`purge_url`: Purge URLs;</li>
<li>`purge_prefix`: Purge prefixes;</li>
<li>`purge_host`: Purge hostnames;</li>
<li>`purge_all`: Purge all caches.</li>
        :type Type: str
        :param Targets: Target resource to be purged, which depends on the `Type` field.
1. When `Type = purge_host`:
Hostnames are purged, such as www.example.com and foo.bar.example.com.
2. When `Type = purge_prefix`:
Prefixes are purged, such as http://www.example.com/example.
3. When `Type = purge_url`:
URLs are purged, such as https://www.example.com/example.jpg.
4. When `Type = purge_all`: All types of resources are purged.
`Targets` is not a required field.
        :type Targets: list of str
        :param EncodeUrl: Specifies whether to transcode non-ASCII URLs according to RFC3986.
Note that if it’s enabled, the purging is based on the converted URLs.
        :type EncodeUrl: bool
        """
        self.ZoneId = None
        self.Type = None
        self.Targets = None
        self.EncodeUrl = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Type = params.get("Type")
        self.Targets = params.get("Targets")
        self.EncodeUrl = params.get("EncodeUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePurgeTaskResponse(AbstractModel):
    """CreatePurgeTask response structure.

    """

    def __init__(self):
        r"""
        :param JobId: ID of the task.
        :type JobId: str
        :param FailedList: List of failed tasks and reasons.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FailedList: list of FailReason
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.JobId = None
        self.FailedList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        if params.get("FailedList") is not None:
            self.FailedList = []
            for item in params.get("FailedList"):
                obj = FailReason()
                obj._deserialize(item)
                self.FailedList.append(obj)
        self.RequestId = params.get("RequestId")


class CreateReplayTaskRequest(AbstractModel):
    """CreateReplayTask request structure.

    """

    def __init__(self):
        r"""
        :param Ids: List of replay task IDs.
        :type Ids: list of str
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReplayTaskResponse(AbstractModel):
    """CreateReplayTask response structure.

    """

    def __init__(self):
        r"""
        :param JobId: ID of the task.
        :type JobId: str
        :param FailedList: List of failed tasks and reasons.
        :type FailedList: list of FailReason
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.JobId = None
        self.FailedList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        if params.get("FailedList") is not None:
            self.FailedList = []
            for item in params.get("FailedList"):
                obj = FailReason()
                obj._deserialize(item)
                self.FailedList.append(obj)
        self.RequestId = params.get("RequestId")


class CreateRuleRequest(AbstractModel):
    """CreateRule request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param RuleName: The rule name (1 to 255 characters)
        :type RuleName: str
        :param Status: Rule status. Values:
<li>`enable`: Enabled</li>
<li>`disable`: Disabled</li>
        :type Status: str
        :param Rules: The rule content.
        :type Rules: list of Rule
        """
        self.ZoneId = None
        self.RuleName = None
        self.Status = None
        self.Rules = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.RuleName = params.get("RuleName")
        self.Status = params.get("Status")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = Rule()
                obj._deserialize(item)
                self.Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRuleResponse(AbstractModel):
    """CreateRule response structure.

    """

    def __init__(self):
        r"""
        :param RuleId: Rule ID
        :type RuleId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class CreateZoneRequest(AbstractModel):
    """CreateZone request structure.

    """

    def __init__(self):
        r"""
        :param ZoneName: The site name.
        :type ZoneName: str
        :param Type: The access mode. Values:
<li>`full`: Access through a name server.</li>
<li>`partial`: Access through a CNAME record.</li>This field will be set to the default value `full` if not specified.
        :type Type: str
        :param JumpStart: Whether to skip scanning the existing DNS records of the site. Default value: false.
        :type JumpStart: bool
        :param Tags: The resource tag.
        :type Tags: list of Tag
        """
        self.ZoneName = None
        self.Type = None
        self.JumpStart = None
        self.Tags = None


    def _deserialize(self, params):
        self.ZoneName = params.get("ZoneName")
        self.Type = params.get("Type")
        self.JumpStart = params.get("JumpStart")
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
        


class CreateZoneResponse(AbstractModel):
    """CreateZone response structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ZoneId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.RequestId = params.get("RequestId")


class DDoS(AbstractModel):
    """DDoS mitigation configuration

    """

    def __init__(self):
        r"""
        :param Switch: Switch. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSAttackEvent(AbstractModel):
    """The DDoS attacker information

    """

    def __init__(self):
        r"""
        :param EventId: The event ID.
        :type EventId: str
        :param AttackType: The attack type.
        :type AttackType: str
        :param AttackStatus: The attack status.
        :type AttackStatus: int
        :param AttackMaxBandWidth: The maximum attack bandwidth.
        :type AttackMaxBandWidth: int
        :param AttackPacketMaxRate: The peak attack packet rate.
        :type AttackPacketMaxRate: int
        :param AttackStartTime: The attack start time recorded in seconds.
        :type AttackStartTime: int
        :param AttackEndTime: The attack end time recorded in seconds.
        :type AttackEndTime: int
        :param PolicyId: The DDoS policy ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PolicyId: int
        :param ZoneId: ID of the site.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneId: str
        """
        self.EventId = None
        self.AttackType = None
        self.AttackStatus = None
        self.AttackMaxBandWidth = None
        self.AttackPacketMaxRate = None
        self.AttackStartTime = None
        self.AttackEndTime = None
        self.PolicyId = None
        self.ZoneId = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.AttackType = params.get("AttackType")
        self.AttackStatus = params.get("AttackStatus")
        self.AttackMaxBandWidth = params.get("AttackMaxBandWidth")
        self.AttackPacketMaxRate = params.get("AttackPacketMaxRate")
        self.AttackStartTime = params.get("AttackStartTime")
        self.AttackEndTime = params.get("AttackEndTime")
        self.PolicyId = params.get("PolicyId")
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSAttackEventDetailData(AbstractModel):
    """The details of a DDoS attack event

    """

    def __init__(self):
        r"""
        :param AttackStatus: The attack status. Values:
<li>`1`: The attack is being observed;</li>
<li>`2`: The attack started;</li>
<li>`3`: The attack ended.</li>
        :type AttackStatus: int
        :param AttackType: The attack type.
        :type AttackType: str
        :param EndTime: The end time.
        :type EndTime: int
        :param StartTime: The start time.
        :type StartTime: int
        :param MaxBandWidth: The maximum bandwidth.
        :type MaxBandWidth: int
        :param PacketMaxRate: The maximum packet rate.
        :type PacketMaxRate: int
        :param EventId: The event ID.
        :type EventId: str
        :param PolicyId: The DDoS policy ID.
        :type PolicyId: int
        """
        self.AttackStatus = None
        self.AttackType = None
        self.EndTime = None
        self.StartTime = None
        self.MaxBandWidth = None
        self.PacketMaxRate = None
        self.EventId = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.AttackStatus = params.get("AttackStatus")
        self.AttackType = params.get("AttackType")
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        self.MaxBandWidth = params.get("MaxBandWidth")
        self.PacketMaxRate = params.get("PacketMaxRate")
        self.EventId = params.get("EventId")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSAttackSourceEvent(AbstractModel):
    """The DDoS attacker information

    """

    def __init__(self):
        r"""
        :param AttackSourceIp: The attacker IP.
        :type AttackSourceIp: str
        :param AttackRegion: The country or region.
        :type AttackRegion: str
        :param AttackFlow: The accumulative attack traffic.
        :type AttackFlow: int
        :param AttackPacketNum: The accumulative attack packets.
        :type AttackPacketNum: int
        """
        self.AttackSourceIp = None
        self.AttackRegion = None
        self.AttackFlow = None
        self.AttackPacketNum = None


    def _deserialize(self, params):
        self.AttackSourceIp = params.get("AttackSourceIp")
        self.AttackRegion = params.get("AttackRegion")
        self.AttackFlow = params.get("AttackFlow")
        self.AttackPacketNum = params.get("AttackPacketNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSBlockData(AbstractModel):
    """The blocking time of a DDoS attack

    """

    def __init__(self):
        r"""
        :param StartTime: The start time recorded in UNIX timestamp.
        :type StartTime: int
        :param EndTime: The start time recorded in UNIX timestamp.
        :type EndTime: int
        """
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSMajorAttackEvent(AbstractModel):
    """The large DDoS attack event

    """

    def __init__(self):
        r"""
        :param PolicyId: The DDoS policy ID.
        :type PolicyId: int
        :param AttackMaxBandWidth: The maximum attack bandwidth.
        :type AttackMaxBandWidth: int
        :param AttackTime: The attack time recorded in seconds using UNIX timestamp.
        :type AttackTime: int
        """
        self.PolicyId = None
        self.AttackMaxBandWidth = None
        self.AttackTime = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.AttackMaxBandWidth = params.get("AttackMaxBandWidth")
        self.AttackTime = params.get("AttackTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DefaultServerCertInfo(AbstractModel):
    """HTTPS server certificate configuration

    """

    def __init__(self):
        r"""
        :param CertId: ID of the server certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertId: str
        :param Alias: Alias of the certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Alias: str
        :param Type: Type of the certificate. Values:
<li>`default`: Default certificate;</li>
<li>`upload`: Custom certificate;</li>
<li>`managed`: Tencent Cloud-managed certificate.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param ExpireTime: Time when the certificate expires.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param EffectiveTime: Time when the certificate takes effect.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EffectiveTime: str
        :param CommonName: Common name of the certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CommonName: str
        :param SubjectAltName: Domain names added to the SAN certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubjectAltName: list of str
        :param Status: Deployment status. Values:
<li>`processing`: Deployment in progress;</li>
<li>`deployed`: Deployed.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param Message: Failure description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param SignAlgo: 
        :type SignAlgo: str
        """
        self.CertId = None
        self.Alias = None
        self.Type = None
        self.ExpireTime = None
        self.EffectiveTime = None
        self.CommonName = None
        self.SubjectAltName = None
        self.Status = None
        self.Message = None
        self.SignAlgo = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.Alias = params.get("Alias")
        self.Type = params.get("Type")
        self.ExpireTime = params.get("ExpireTime")
        self.EffectiveTime = params.get("EffectiveTime")
        self.CommonName = params.get("CommonName")
        self.SubjectAltName = params.get("SubjectAltName")
        self.Status = params.get("Status")
        self.Message = params.get("Message")
        self.SignAlgo = params.get("SignAlgo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDnsRecordsRequest(AbstractModel):
    """DeleteDnsRecords request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID of the DNS record to be deleted.
        :type ZoneId: str
        :param DnsRecordIds: The ID of the DNS record to be deleted.
        :type DnsRecordIds: list of str
        """
        self.ZoneId = None
        self.DnsRecordIds = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.DnsRecordIds = params.get("DnsRecordIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDnsRecordsResponse(AbstractModel):
    """DeleteDnsRecords response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLogTopicTaskRequest(AbstractModel):
    """DeleteLogTopicTask request structure.

    """

    def __init__(self):
        r"""
        :param TopicId: ID of the shipping task to be deleted.
        :type TopicId: str
        :param LogSetRegion: Region of the logset.
        :type LogSetRegion: str
        """
        self.TopicId = None
        self.LogSetRegion = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.LogSetRegion = params.get("LogSetRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLogTopicTaskResponse(AbstractModel):
    """DeleteLogTopicTask response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRulesRequest(AbstractModel):
    """DeleteRules request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param RuleIds: IDs of the rules to be deleted.
        :type RuleIds: list of str
        """
        self.ZoneId = None
        self.RuleIds = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.RuleIds = params.get("RuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRulesResponse(AbstractModel):
    """DeleteRules response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteZoneRequest(AbstractModel):
    """DeleteZone request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        """
        self.ZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteZoneResponse(AbstractModel):
    """DeleteZone response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAddableEntityListRequest(AbstractModel):
    """DescribeAddableEntityList request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site.
        :type ZoneId: str
        :param EntityType: Type of the shipping entity. Values:
<li>`domain`: L7 acceleration logs;</li>
<li>`application`: L4 acceleration logs;</li>
<li>`web-rateLiming`: Rate limiting logs;</li>
<li>`web-attack`: Web security logs;</li>
<li>`web-rule`: Custom rule logs;</li>
<li>`web-bot`: Bot management logs.</li>
        :type EntityType: str
        """
        self.ZoneId = None
        self.EntityType = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.EntityType = params.get("EntityType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAddableEntityListResponse(AbstractModel):
    """DescribeAddableEntityList response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param EntityList: List of available shipping entities.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EntityList: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.EntityList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.EntityList = params.get("EntityList")
        self.RequestId = params.get("RequestId")


class DescribeAvailablePlansRequest(AbstractModel):
    """DescribeAvailablePlans request structure.

    """


class DescribeAvailablePlansResponse(AbstractModel):
    """DescribeAvailablePlans response structure.

    """

    def __init__(self):
        r"""
        :param PlanInfo: Plans available for the current user
Note: This field may return null, indicating that no valid values can be obtained.
        :type PlanInfo: list of PlanInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PlanInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlanInfo") is not None:
            self.PlanInfo = []
            for item in params.get("PlanInfo"):
                obj = PlanInfo()
                obj._deserialize(item)
                self.PlanInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBillingDataRequest(AbstractModel):
    """DescribeBillingData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time.
        :type StartTime: str
        :param EndTime: End time.
        :type EndTime: str
        :param Interval: Time granularity. Values:
<ul>
<li>`min`: One minute</li>
<li>`5min`: Five minutes</li>
<li>`hour`: One hour</li>
<li>`day`: One day</li>
</ul>
        :type Interval: str
        :param MetricName: Metric item. Values:
<ul>
<li>`acc_flux`: Content acceleration traffic;</li>
<li>`quic_request`: QUIC requests;</li>
<li>`sec_flux`: Security traffic;</li>
<li>`sec_request_clean`: Clean security requests.</li>
</ul>
        :type MetricName: str
        :param Filters: Filter item. Values:
<ul>
<li>`zone`: Site;</li>
<li>`plan`: Service plan;</li>
<li>`service`: L4 or L7;</li>
<li>`tagKey`: Tag key;</li>
<li>`tagValue`: Tag value.</li>
</ul>
        :type Filters: list of BillingDataFilter
        """
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.MetricName = None
        self.Filters = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Interval = params.get("Interval")
        self.MetricName = params.get("MetricName")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = BillingDataFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillingDataResponse(AbstractModel):
    """DescribeBillingData response structure.

    """

    def __init__(self):
        r"""
        :param Data: Data of the sampling point
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of DnsData
        :param Interval: Time granularity of sampling
Note: This field may return null, indicating that no valid values can be obtained.
        :type Interval: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.Interval = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DnsData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Interval = params.get("Interval")
        self.RequestId = params.get("RequestId")


class DescribeBotClientIpListRequest(AbstractModel):
    """DescribeBotClientIpList request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param QueryCondition: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`action`: The action;</li>
        :type QueryCondition: list of QueryCondition
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland).</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ZoneIds = None
        self.Domains = None
        self.Interval = None
        self.QueryCondition = None
        self.Limit = None
        self.Offset = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Interval = params.get("Interval")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBotClientIpListResponse(AbstractModel):
    """DescribeBotClientIpList response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of client IP data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of SecClientIp
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecClientIp()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeBotDataRequest(AbstractModel):
    """DescribeBotData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricNames: List of statistical metric. Values:
<li>`bot_interceptNum`: Blocked bot requests;</li>
<li>`bot_noneRequestNum`: Uncategorized bot requests;</li>
<li>`bot_maliciousRequestNum`: Malicious bot requests;</li>
<li>`bot_suspectedRequestNum`: Suspected bot requests;</li>
<li>`bot_friendlyRequestNum`: Friendly bot requests;</li>
<li>`bot_normalRequestNum`: Normal bot requests.</li>
        :type MetricNames: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param ZoneIds: Specifies sites by ID. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param QueryCondition: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`action`: The action;</li>
        :type QueryCondition: list of QueryCondition
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.Domains = None
        self.ZoneIds = None
        self.Interval = None
        self.QueryCondition = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.Domains = params.get("Domains")
        self.ZoneIds = params.get("ZoneIds")
        self.Interval = params.get("Interval")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBotDataResponse(AbstractModel):
    """DescribeBotData response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of bot attack data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of SecEntry
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeBotHitRuleDetailRequest(AbstractModel):
    """DescribeBotHitRuleDetail request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param QueryCondition: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`action`: The action;</li>
        :type QueryCondition: list of QueryCondition
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ZoneIds = None
        self.Domains = None
        self.Interval = None
        self.QueryCondition = None
        self.Limit = None
        self.Offset = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Interval = params.get("Interval")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBotHitRuleDetailResponse(AbstractModel):
    """DescribeBotHitRuleDetail response structure.

    """

    def __init__(self):
        r"""
        :param Data: The hit rule information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of SecHitRuleInfo
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecHitRuleInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeBotLogRequest(AbstractModel):
    """DescribeBotLog request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        :param QueryCondition: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`action`: The action;</li>
<li>`sipCountryCode`: The country code of the attacker IP;</li>
<li>`attackIp`: Attacker IP;</li>
<li>`ruleId`: Rule ID;</li>
<li>`eventId`: The event ID;</li>
<li>`ua`: User agent;</li>
<li>`requestMethod`: Request method;</li>
<li>`uri`: Uniform resource identifier.</li>
        :type QueryCondition: list of QueryCondition
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ZoneIds = None
        self.Domains = None
        self.Limit = None
        self.Offset = None
        self.QueryCondition = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBotLogResponse(AbstractModel):
    """DescribeBotLog response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of bot attack data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of BotLog
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = BotLog()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeBotTopDataRequest(AbstractModel):
    """DescribeBotTopData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricName: List of statistical metric. Values:
<li>`bot_requestNum_labelType`: Top-ranked tag types by bot requests.</li>
<li>`bot_requestNum_url`: Top-ranked URLs by bot requests.</li>
<li>`bot_cipRequestNum_region`: Top-ranked client IPs by bot requests.</li>
        :type MetricName: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param Limit: Queries the top rows of data. Maximum value: 1000. Top 10 rows of data will be queried if this field is not specified.
        :type Limit: int
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param QueryCondition: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`action`: The action;</li>
        :type QueryCondition: list of QueryCondition
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.ZoneIds = None
        self.Domains = None
        self.Limit = None
        self.Interval = None
        self.QueryCondition = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Limit = params.get("Limit")
        self.Interval = params.get("Interval")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBotTopDataResponse(AbstractModel):
    """DescribeBotTopData response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of top-ranked bot attack data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TopEntry
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TopEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeClientRuleListRequest(AbstractModel):
    """DescribeClientRuleList request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The ID of the site to be queried.
        :type ZoneId: str
        :param Domain: The subdomain name to be queried.
        :type Domain: str
        :param RuleType: Rule type. Values:
<li>`acl`: Custom rules;</li>
<li>`rate`: Rate limiting rules.</li>All rules will be queried if this field is not specified.
        :type RuleType: str
        :param RuleId: The rule ID.
        :type RuleId: int
        :param SourceClientIp: The client IP.
        :type SourceClientIp: str
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.ZoneId = None
        self.Domain = None
        self.RuleType = None
        self.RuleId = None
        self.SourceClientIp = None
        self.Limit = None
        self.Offset = None
        self.Area = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Domain = params.get("Domain")
        self.RuleType = params.get("RuleType")
        self.RuleId = params.get("RuleId")
        self.SourceClientIp = params.get("SourceClientIp")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClientRuleListResponse(AbstractModel):
    """DescribeClientRuleList response structure.

    """

    def __init__(self):
        r"""
        :param Data: The blocked client information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of ClientRule
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ClientRule()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeContentQuotaRequest(AbstractModel):
    """DescribeContentQuota request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site.
        :type ZoneId: str
        """
        self.ZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeContentQuotaResponse(AbstractModel):
    """DescribeContentQuota response structure.

    """

    def __init__(self):
        r"""
        :param PurgeQuota: Purging quotas.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PurgeQuota: list of Quota
        :param PrefetchQuota: Pre-warming quotas.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PrefetchQuota: list of Quota
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PurgeQuota = None
        self.PrefetchQuota = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PurgeQuota") is not None:
            self.PurgeQuota = []
            for item in params.get("PurgeQuota"):
                obj = Quota()
                obj._deserialize(item)
                self.PurgeQuota.append(obj)
        if params.get("PrefetchQuota") is not None:
            self.PrefetchQuota = []
            for item in params.get("PrefetchQuota"):
                obj = Quota()
                obj._deserialize(item)
                self.PrefetchQuota.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSAttackDataRequest(AbstractModel):
    """DescribeDDoSAttackData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricNames: List of statistical metric. Values:
<li>`ddos_attackMaxBandwidth`: Peak attack bandwidth;</li>
<li>`ddos_attackMaxPackageRate`: Peak attack packet rate;</li>
<li>`ddos_attackBandwidth`: Attack bandwidth;</li>
<li>`ddos_attackPackageRate`: Attack packet rate.</li>
        :type MetricNames: list of str
        :param Port: The port number.
        :type Port: int
        :param AttackType: The attack type. Values:
<li>`flood`: Flood;</li>
<li>`icmpFlood`: ICMP flood;</li>
<li>`all`: All attack types.</li>This field will be set to the default value `all` if not specified.
        :type AttackType: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param PolicyIds: The list of DDoS policy IDs to be specified. All policies will be selected if this field is not specified.
        :type PolicyIds: list of int
        :param ProtocolType: The protocol type. Values:
<li>`tcp`: TCP protocol;</li>
<li>`udp`: UDP protocol;</li>
<li>`all`: All protocol types.</li>This field will be set to the default value `all` if not specified.
        :type ProtocolType: str
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.Port = None
        self.AttackType = None
        self.ZoneIds = None
        self.PolicyIds = None
        self.ProtocolType = None
        self.Interval = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.Port = params.get("Port")
        self.AttackType = params.get("AttackType")
        self.ZoneIds = params.get("ZoneIds")
        self.PolicyIds = params.get("PolicyIds")
        self.ProtocolType = params.get("ProtocolType")
        self.Interval = params.get("Interval")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAttackDataResponse(AbstractModel):
    """DescribeDDoSAttackData response structure.

    """

    def __init__(self):
        r"""
        :param Data: List of DDoS attack data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of SecEntry
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDDoSAttackEventDetailRequest(AbstractModel):
    """DescribeDDoSAttackEventDetail request structure.

    """

    def __init__(self):
        r"""
        :param EventId: The event ID to be queried.
        :type EventId: str
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.EventId = None
        self.Area = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAttackEventDetailResponse(AbstractModel):
    """DescribeDDoSAttackEventDetail response structure.

    """

    def __init__(self):
        r"""
        :param Data: The details of a DDoS attack event.
        :type Data: :class:`tencentcloud.teo.v20220901.models.DDoSAttackEventDetailData`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DDoSAttackEventDetailData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeDDoSAttackEventRequest(AbstractModel):
    """DescribeDDoSAttackEvent request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param ProtocolType: The protocol type. Values:
<li>`tcp`: TCP protocol;</li>
<li>`udp`: UDP protocol;</li>
<li>`all`: All protocol types.</li>This field will be set to the default value `all` if not specified.
        :type ProtocolType: str
        :param PolicyIds: The list of DDoS policy IDs to be specified. All policies will be selected if this field is not specified.
        :type PolicyIds: list of int
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        :param ShowDetail: Whether to display the details.
        :type ShowDetail: bool
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ProtocolType = None
        self.PolicyIds = None
        self.ZoneIds = None
        self.Limit = None
        self.Offset = None
        self.ShowDetail = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ProtocolType = params.get("ProtocolType")
        self.PolicyIds = params.get("PolicyIds")
        self.ZoneIds = params.get("ZoneIds")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.ShowDetail = params.get("ShowDetail")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAttackEventResponse(AbstractModel):
    """DescribeDDoSAttackEvent response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of DDoS attack data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of DDoSAttackEvent
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DDoSAttackEvent()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDDoSAttackSourceEventRequest(AbstractModel):
    """DescribeDDoSAttackSourceEvent request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param ProtocolType: The protocol type. Values:
<li>`tcp`: TCP protocol;</li>
<li>`udp`: UDP protocol;</li>
<li>`all`: All protocol types.</li>This field will be set to the default value `all` if not specified.
        :type ProtocolType: str
        :param PolicyIds: The list of DDoS policy IDs to be specified. All policies will be selected if this field is not specified.
        :type PolicyIds: list of int
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ProtocolType = None
        self.PolicyIds = None
        self.ZoneIds = None
        self.Limit = None
        self.Offset = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ProtocolType = params.get("ProtocolType")
        self.PolicyIds = params.get("PolicyIds")
        self.ZoneIds = params.get("ZoneIds")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAttackSourceEventResponse(AbstractModel):
    """DescribeDDoSAttackSourceEvent response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of DDoS attacker data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of DDoSAttackSourceEvent
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DDoSAttackSourceEvent()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDDoSAttackTopDataRequest(AbstractModel):
    """DescribeDDoSAttackTopData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricName: The statistical metric. Values:
<li>`ddos_attackFlux_protocol`: Top-ranked protocols by DDoS attack traffic.</li>
<li>`ddos_attackPackageNum_protocol`: Top-ranked protocols by DDoS attack packets.</li>
<li>`ddos_attackNum_attackType`: Top-ranked attack types by DDoS attacks.</li>
<li>`ddos_attackNum_sregion`: Top-ranked attack source regions by DDoS attacks.</li>
<li>`ddos_attackFlux_sip`: Top-ranked attacker IPs by DDoS attack traffic.</li>
<li>`ddos_attackFlux_sregion`: Top-ranked attack source regions by DDoS attack traffic.</li>
        :type MetricName: str
        :param ZoneIds: List of site IDs to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param PolicyIds: The list of DDoS policy IDs to be specified. All policies will be selected if this field is not specified.
        :type PolicyIds: list of int
        :param AttackType: The attack type. Values:
<li>`flood`: Flood;</li>
<li>`icmpFlood`: ICMP flood;</li>
<li>`all`: All attack types.</li>This field will be set to the default value `all` if not specified.
        :type AttackType: str
        :param ProtocolType: The protocol type. Values:
<li>`tcp`: TCP protocol;</li>
<li>`udp`: UDP protocol;</li>
<li>`all`: All protocol types.</li>This field will be set to the default value `all` if not specified.
        :type ProtocolType: str
        :param Port: The port number.
        :type Port: int
        :param Limit: Queries the top n rows of data. Top 10 rows of data will be queried if this field is not specified.
        :type Limit: int
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.ZoneIds = None
        self.PolicyIds = None
        self.AttackType = None
        self.ProtocolType = None
        self.Port = None
        self.Limit = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.ZoneIds = params.get("ZoneIds")
        self.PolicyIds = params.get("PolicyIds")
        self.AttackType = params.get("AttackType")
        self.ProtocolType = params.get("ProtocolType")
        self.Port = params.get("Port")
        self.Limit = params.get("Limit")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAttackTopDataResponse(AbstractModel):
    """DescribeDDoSAttackTopData response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of top-ranked DDoS attack data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TopEntry
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TopEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDDoSBlockListRequest(AbstractModel):
    """DescribeDDoSBlockList request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time of the attack event.
        :type StartTime: str
        :param EventIds: The list of attack events.
        :type EventIds: list of str
        :param ZoneIds: Specifies sites by ID. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param PolicyIds: The list of policy IDs to be specified. All policies will be selected if this field is not specified.
        :type PolicyIds: list of int
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EventIds = None
        self.ZoneIds = None
        self.PolicyIds = None
        self.Limit = None
        self.Offset = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EventIds = params.get("EventIds")
        self.ZoneIds = params.get("ZoneIds")
        self.PolicyIds = params.get("PolicyIds")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSBlockListResponse(AbstractModel):
    """DescribeDDoSBlockList response structure.

    """

    def __init__(self):
        r"""
        :param Data: The blocking time of a DDoS attack.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of DDoSBlockData
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DDoSBlockData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDDoSMajorAttackEventRequest(AbstractModel):
    """DescribeDDoSMajorAttackEvent request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param ZoneIds: Specifies sites by ID. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param PolicyIds: The list of DDoS policy IDs to be specified. All policies will be selected if this field is not specified.
        :type PolicyIds: list of int
        :param ProtocolType: The protocol type. Values:
<li>`tcp`: TCP protocol;</li>
<li>`udp`: UDP protocol;</li>
<li>`all`: All protocol types.</li>This field will be set to the default value `all` if not specified.
        :type ProtocolType: str
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ZoneIds = None
        self.PolicyIds = None
        self.ProtocolType = None
        self.Limit = None
        self.Offset = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ZoneIds = params.get("ZoneIds")
        self.PolicyIds = params.get("PolicyIds")
        self.ProtocolType = params.get("ProtocolType")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSMajorAttackEventResponse(AbstractModel):
    """DescribeDDoSMajorAttackEvent response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of large DDoS attack data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of DDoSMajorAttackEvent
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DDoSMajorAttackEvent()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDefaultCertificatesRequest(AbstractModel):
    """DescribeDefaultCertificates request structure.

    """

    def __init__(self):
        r"""
        :param Filters: Filter criteria. Each filter criteria can have up to 5 entries.
<li>`zone-id`: <br>Filter by <strong>site ID</strong>. Format: zone-xxx
        :type Filters: list of Filter
        :param Offset: Offset for paginated queries. Default value: `0`
        :type Offset: int
        :param Limit: Limit on paginated queries. Default value: `20`. Maximum value: `100`.
        :type Limit: int
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDefaultCertificatesResponse(AbstractModel):
    """DescribeDefaultCertificates response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of certificates
        :type TotalCount: int
        :param DefaultServerCertInfo: List of default certificates
        :type DefaultServerCertInfo: list of DefaultServerCertInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.DefaultServerCertInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DefaultServerCertInfo") is not None:
            self.DefaultServerCertInfo = []
            for item in params.get("DefaultServerCertInfo"):
                obj = DefaultServerCertInfo()
                obj._deserialize(item)
                self.DefaultServerCertInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDnsDataRequest(AbstractModel):
    """DescribeDnsData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param Filters: Filter criteria. Each filter criteria can have up to 20 entries.
<li>`zone`:<br>   Filter by <strong>site name</strong>, such as tencent.com (up to one entry)<br>   Type: String<br>   Required: No
<li>`host`:<br>   Filter by <strong>domain name</strong>, such as test.tencent.com (up to one entry)<br>   Type: String<br>   Required: No
<li>`type`:<br>   Filter by <strong>DNS record type</strong><br>   Type: String<br>   Required: No<br>   Values:<br>   `A`: A record<br>   `AAAA`: AAAA record<br>   `CNAME`: CNAME record<br>   `MX`: MX record<br>   `TXT`: TXT record<br>   `NS`: NS record<br>   `SRV`: SRV record<br>   `CAA`: CAA record
<li>`code`:<br>   Filter by <strong>DNS status code</strong><br>   Type: String<br>   Required: No<br>   Values:<br>   `NoError`: Success<br>   `NXDomain`: Not found the request domain<br>   `NotImp`: Not supported request type<br>   `Refused`: The domain name server refuses to execute the request for policy reasons
<li>`area`:<br>   Filter by <strong>DNS region</strong><br>   Type: String<br>   Required: No<br>   Values:<br>   `Asia`<br>   `Europe`<br>   `Africa`<br>   `Oceania`<br>   `Americas`
        :type Filters: list of Filter
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>This field will be set to the default value `min` if not specified.
        :type Interval: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Filters = None
        self.Interval = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDnsDataResponse(AbstractModel):
    """DescribeDnsData response structure.

    """

    def __init__(self):
        r"""
        :param Data: DNS statistics.
        :type Data: list of DnsData
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DnsData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDnsRecordsRequest(AbstractModel):
    """DescribeDnsRecords request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID of the DNS record. All sites’ DNS records will be returned if this field is not specified.
        :type ZoneId: str
        :param Filters: Filter criteria. Each filter criteria can have up to 20 entries.
<li>`record-id`:<br>   Filter by <strong>DNS record ID</strong>, such as record-1a8df68z<br>   Type: String<br>Required: No
<li>`record-name`:<br>   Filter by <strong>DNS record name</strong><br>   Type: String<br>Required: No
<li>`record-type`:<br>   Filter by <strong>DNS record type</strong><br>   Type: String<br>Required: No<br>   Values:<br>   `A`: Point a domain name to an IPv4 address, such as 8.8.8.8.<br>   `AAAA`: Point a domain name to an IPv6 address.<br>   `CNAME`: Point a domain name to another domain name that can be resolved to an IP address.<br>   `TXT`: Identify and describe a domain name. It is usually used for domain verification and as SPF records (for anti-spam).<br>   `NS`: If you need to authorize a subdomain name to another DNS service provider for DNS resolution, you need to add an NS record. You cannot add an NS record for a root domain name.<br>   `CAA`: Specify CAs to issue certificates for sites.<br>   `SRV`: Identify a service used by a server. It is commonly used in Microsoft directory management.<br>  `MX`: Specify the mail server for receiving emails.
<li>`mode`:<br>   Filter by <strong>proxy mode</strong><br>   Type: String<br>Required: No<br>   Values:<br>   `dns_only`: Only DNS<br>   `proxied`: Proxied
<li>`ttl`:<br>   Filter by <strong>TTL</strong><br>   Type: String<br>Required: No
        :type Filters: list of AdvancedFilter
        :param Direction: The sorting order. Values:
<li>`ASC`: Ascending order</li>
<li>`desc`: Descending order</li> Default value: asc
        :type Direction: str
        :param Match: The match mode. Values:
<li>`all`: Return all records that match the specified filter.</li>
<li>`any`: Return any record that matches the specified filter.</li>Default value: all.
        :type Match: str
        :param Limit: The paginated query limit. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0
        :type Offset: int
        :param Order: The sorting criteria. Values:
<li>`content`: DNS record content.</li>
<li>`created_on`: Creation time of the DNS record.</li>
<li>`mode`: Proxy mode.</li>
<li>`record-name`: DNS record name.</li>
<li>`ttl`: DNS TTL.</li>
<li>`record-type`: DNS record type.</li>If this field is not specified, the DNS records are sorted based on `record-type` and `recrod-name`.
        :type Order: str
        """
        self.ZoneId = None
        self.Filters = None
        self.Direction = None
        self.Match = None
        self.Limit = None
        self.Offset = None
        self.Order = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Direction = params.get("Direction")
        self.Match = params.get("Match")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDnsRecordsResponse(AbstractModel):
    """DescribeDnsRecords response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of DNS records.
        :type TotalCount: int
        :param DnsRecords: List of DNS records
        :type DnsRecords: list of DnsRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.DnsRecords = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DnsRecords") is not None:
            self.DnsRecords = []
            for item in params.get("DnsRecords"):
                obj = DnsRecord()
                obj._deserialize(item)
                self.DnsRecords.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDnssecRequest(AbstractModel):
    """DescribeDnssec request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        """
        self.ZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDnssecResponse(AbstractModel):
    """DescribeDnssec response structure.

    """

    def __init__(self):
        r"""
        :param Status: The DNSSEC status. Values:
<li>`enabled`: Enabled</li>
<li>`disabled`: Disabled</li>
        :type Status: str
        :param DnssecInfo: The DNSSEC information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DnssecInfo: :class:`tencentcloud.teo.v20220901.models.DnssecInfo`
        :param ModifiedOn: The update time of the site information.
        :type ModifiedOn: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.DnssecInfo = None
        self.ModifiedOn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        if params.get("DnssecInfo") is not None:
            self.DnssecInfo = DnssecInfo()
            self.DnssecInfo._deserialize(params.get("DnssecInfo"))
        self.ModifiedOn = params.get("ModifiedOn")
        self.RequestId = params.get("RequestId")


class DescribeHostsSettingRequest(AbstractModel):
    """DescribeHostsSetting request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param Offset: Offset for paginated queries. Default value: 0. Minimum value: 0.
        :type Offset: int
        :param Limit: Limit on paginated queries. Default value: 100. Maximum value: 1000.
        :type Limit: int
        :param Filters: Filter criteria. Each filter criteria can have up to 20 entries.
<li>`host`:<br>   Filter by <strong>domain name </strong><br>   Type: String<br>   Required: No
        :type Filters: list of Filter
        """
        self.ZoneId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostsSettingResponse(AbstractModel):
    """DescribeHostsSetting response structure.

    """

    def __init__(self):
        r"""
        :param DetailHosts: List of domain names.
        :type DetailHosts: list of DetailHost
        :param TotalNumber: Number of domain names
        :type TotalNumber: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DetailHosts = None
        self.TotalNumber = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DetailHosts") is not None:
            self.DetailHosts = []
            for item in params.get("DetailHosts"):
                obj = DetailHost()
                obj._deserialize(item)
                self.DetailHosts.append(obj)
        self.TotalNumber = params.get("TotalNumber")
        self.RequestId = params.get("RequestId")


class DescribeIdentificationsRequest(AbstractModel):
    """DescribeIdentifications request structure.

    """

    def __init__(self):
        r"""
        :param Filters: Filter criteria. Each filter criteria can have up to 20 entries.
<li>`zone-name`: <br>Filter by <strong>site name</strong><br>   Type: String<br>   Required: No
        :type Filters: list of Filter
        :param Offset: The page offset. Default value: 0
        :type Offset: int
        :param Limit: The paginated query limit. Default value: 20. Maximum value: 1000.
        :type Limit: int
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIdentificationsResponse(AbstractModel):
    """DescribeIdentifications response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of eligible sites.
        :type TotalCount: int
        :param Identifications: The site verification information.
        :type Identifications: list of Identification
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Identifications = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Identifications") is not None:
            self.Identifications = []
            for item in params.get("Identifications"):
                obj = Identification()
                obj._deserialize(item)
                self.Identifications.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLogSetsRequest(AbstractModel):
    """DescribeLogSets request structure.

    """

    def __init__(self):
        r"""
        :param LogSetRegion: Region of the logset.
        :type LogSetRegion: str
        :param LogSetId: ID of the logset.
        :type LogSetId: str
        :param LogSetName: Name of the logset.
        :type LogSetName: str
        """
        self.LogSetRegion = None
        self.LogSetId = None
        self.LogSetName = None


    def _deserialize(self, params):
        self.LogSetRegion = params.get("LogSetRegion")
        self.LogSetId = params.get("LogSetId")
        self.LogSetName = params.get("LogSetName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogSetsResponse(AbstractModel):
    """DescribeLogSets response structure.

    """

    def __init__(self):
        r"""
        :param LogSetList: List of logsets.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogSetList: list of LogSetInfo
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LogSetList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LogSetList") is not None:
            self.LogSetList = []
            for item in params.get("LogSetList"):
                obj = LogSetInfo()
                obj._deserialize(item)
                self.LogSetList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeLogTopicTaskDetailRequest(AbstractModel):
    """DescribeLogTopicTaskDetail request structure.

    """

    def __init__(self):
        r"""
        :param TopicId: ID of the shipping task.
        :type TopicId: str
        :param ZoneId: ID of the site.
        :type ZoneId: str
        """
        self.TopicId = None
        self.ZoneId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogTopicTaskDetailResponse(AbstractModel):
    """DescribeLogTopicTaskDetail response structure.

    """

    def __init__(self):
        r"""
        :param LogTopicDetailInfo: The shipping task details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogTopicDetailInfo: :class:`tencentcloud.teo.v20220901.models.LogTopicDetailInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LogTopicDetailInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LogTopicDetailInfo") is not None:
            self.LogTopicDetailInfo = LogTopicDetailInfo()
            self.LogTopicDetailInfo._deserialize(params.get("LogTopicDetailInfo"))
        self.RequestId = params.get("RequestId")


class DescribeLogTopicTasksRequest(AbstractModel):
    """DescribeLogTopicTasks request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site.
        :type ZoneId: str
        :param Limit: Limit on paginated queries. Default value: `20`. Maximum value: `1000`.
        :type Limit: int
        :param Offset: Page offset. Default value: 0.
        :type Offset: int
        """
        self.ZoneId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogTopicTasksResponse(AbstractModel):
    """DescribeLogTopicTasks response structure.

    """

    def __init__(self):
        r"""
        :param TopicList: List of shipping tasks.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TopicList: list of ClsLogTopicInfo
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TopicList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TopicList") is not None:
            self.TopicList = []
            for item in params.get("TopicList"):
                obj = ClsLogTopicInfo()
                obj._deserialize(item)
                self.TopicList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeOverviewL7DataRequest(AbstractModel):
    """DescribeOverviewL7Data request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricNames: The query metric. Values:
<li>`l7Flow_outFlux`: Access traffic;</li>
<li>`l7Flow_request`: Access requests;</li>
<li>`l7Flow_outBandwidth`: Access bandwidth.</li>
<li>`l7Flow_hit_outFlux`: Cache hit traffic.</li>
        :type MetricNames: list of str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param Protocol: The protocol type. Values:
<li>`http`: HTTP protocol;</li>
<li>`https`: HTTPS protocol;</li>
<li>`http2`: HTTP2 protocol;</li>
<li>`all`: All protocol types.</li>This field will be set to the default value `all` if not specified.
        :type Protocol: str
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        :param Filters: Filter criteria. Each filter criteria can have up to 20 entries.
<li>`tagKey`:<br>   Filter by <strong>tag key</strong><br>   Type: String<br>   Required: No</li>
<li>`tagValue`<br>  Filter by <strong>tag value</strong><br>   Type: String<br>   Required: No</li>
        :type Filters: list of QueryCondition
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.Domains = None
        self.Protocol = None
        self.Interval = None
        self.Area = None
        self.Filters = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Protocol = params.get("Protocol")
        self.Interval = params.get("Interval")
        self.Area = params.get("Area")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOverviewL7DataResponse(AbstractModel):
    """DescribeOverviewL7Data response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param Data: The list of L7 traffic summary statistics recorded over time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TimingDataRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TimingDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePrefetchTasksRequest(AbstractModel):
    """DescribePrefetchTasks request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time of the query.
        :type StartTime: str
        :param EndTime: End time of the query.
        :type EndTime: str
        :param Offset: Offset for paginated queries. Default value: `0`.
        :type Offset: int
        :param Limit: Limit on paginated queries. Default value: `20`. Maximum value: `1000`.
        :type Limit: int
        :param Filters: Filter criteria. Each filter criteria can have up to 20 entries.
<li>`zone-id`:<br>   Filter by the <strong>site ID</strong>, such as zone-1379afjk91u32h (up to one entry)<br>   Type: String<br>   Required: No<br>   Fuzzy query: Not supported<li>`job-id`:<br>   Filter by <strong>task ID</strong>, such as 1379afjk91u32h (up to one entry)<br>   Type: String<br>   Required: No<br>   Fuzzy query: Not supported<li>`target`:<br>   Filter by <strong>target resource</strong>, such as http://www.qq.com/1.txt (up to one entry)<br>   Type: String<br>   Required: No<br>   Fuzzy query: Not supported<li>`domains`:<br>   Filter by <strong>domain name</strong>, such as www.qq.com<br>   Type: String<br>   Required: No<br>   Fuzzy query: Not supported<li>`statuses`:<br>   Filter by <strong>task status</strong><br>   Required: No<br>   Fuzzy query: Not supported<br>   Values:<br>   `processing`: The task is in progress.<br>   `success`: The task succeeded.<br>   `failed`: The task failed.<br>   `timeout`: The task timed out.
        :type Filters: list of AdvancedFilter
        """
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrefetchTasksResponse(AbstractModel):
    """DescribePrefetchTasks response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total entries that match the specified query condition.
        :type TotalCount: int
        :param Tasks: List of tasks returned.
        :type Tasks: list of Task
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePurgeTasksRequest(AbstractModel):
    """DescribePurgeTasks request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site.
        :type ZoneId: str
        :param StartTime: Start time of the query.
        :type StartTime: str
        :param EndTime: End time of the query.
        :type EndTime: str
        :param Offset: Offset for paginated queries. Default value: `0`.
        :type Offset: int
        :param Limit: Limit on paginated queries. Default value: `20`. Maximum value: `1000`.
        :type Limit: int
        :param Filters: Filter criteria. Each filter criteria can have up to 20 entries.
<li>`job-id`:<br> Filter by the <strong>Task ID</strong>, such as 1379afjk91u32h. Only one ID can be specified.<br>Type: String<br>   Required: No<br>   Fuzzy query: Not supported<li>`target`:<br>   Filter by the <strong>resource address</strong>, such as http://www.qq.com/1.txt. Only one entry allowed.<br>   Type: String<br>   Required: No<br>   Fuzzy query: Not supported<li>`domains`:<br>   Filter by the <strong>domain name</strong>, such as www.qq.com<br>   Type: String<br>   Required: No<br>   Fuzzy query: Not supported<li>`statuses`:<br>   Filter by the <strong>task status</strong><br>   Required: No<br>   Fuzzy query: Not supported<br>   Values:<br>   `processing`: Tasks in progress<br>   `success`: Succeeded tasks<br>   `failed`: Failed tasks<br>   `timeout`: Timed-out tasks<li>`type`:<br>   Filter by the <strong>purging mode</strong>. Only one value allowed.<br>   Type: String<br>   Required: No<br>   Fuzzy query: Not supported<br>   Values:<br>   `purge_url`: Purge URLs.<br>   `purge_prefix`: Purge prefixes.<br>   `purge_all`: Purge all caches.<br>   `purge_host`: Purge hostnames.
        :type Filters: list of AdvancedFilter
        """
        self.ZoneId = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePurgeTasksResponse(AbstractModel):
    """DescribePurgeTasks response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total entries that match the specified query condition.
        :type TotalCount: int
        :param Tasks: List of tasks returned.
        :type Tasks: list of Task
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRulesRequest(AbstractModel):
    """DescribeRules request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param Filters: Filter criteria. Each filter criteria can have up to 20 entries.
<li>`rule-id`:<br>   Filter by the <strong>rule ID</strong><br>   Type: string<br>   Required: No
        :type Filters: list of Filter
        """
        self.ZoneId = None
        self.Filters = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRulesResponse(AbstractModel):
    """DescribeRules response structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param RuleItems: List of rules. Rules are sorted in order of execution.
        :type RuleItems: list of RuleItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ZoneId = None
        self.RuleItems = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("RuleItems") is not None:
            self.RuleItems = []
            for item in params.get("RuleItems"):
                obj = RuleItem()
                obj._deserialize(item)
                self.RuleItems.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRulesSettingRequest(AbstractModel):
    """DescribeRulesSetting request structure.

    """


class DescribeRulesSettingResponse(AbstractModel):
    """DescribeRulesSetting response structure.

    """

    def __init__(self):
        r"""
        :param Actions: List of the settings of the rule engine that can be used for request match and their detailed recommended configuration information.
        :type Actions: list of RulesSettingAction
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Actions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Actions") is not None:
            self.Actions = []
            for item in params.get("Actions"):
                obj = RulesSettingAction()
                obj._deserialize(item)
                self.Actions.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSingleL7AnalysisDataRequest(AbstractModel):
    """DescribeSingleL7AnalysisData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricNames: The query metric. Values:
<li>`l7Flow_singleIpRequest`: Number of requests from a single IP.</li>
        :type MetricNames: list of str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Filters: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`country`: Country/Region;</li>
<li>`domain`: Domain name;</li>
<li>`protocol`: Protocol type;</li>
<li>`tagKey`: Tag key;</li>
<li>`tagValue`: Tag value.</li>
        :type Filters: list of QueryCondition
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.Filters = None
        self.Interval = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Interval = params.get("Interval")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSingleL7AnalysisDataResponse(AbstractModel):
    """DescribeSingleL7AnalysisData response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param Data: The list of L7 dimensional data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of SingleDataRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SingleDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTimingL4DataRequest(AbstractModel):
    """DescribeTimingL4Data request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricNames: Metric to query. Values:
<li>`l4Flow_connections`: Access connections;</li>
<li>`l4Flow_flux`: Access traffic;</li>
<li>`l4Flow_inFlux`: Inbound traffic;</li>
<li>`l4Flow_outFlux`: Outbound traffic;</li>
<li>`l4Flow_outPkt`: Outbound packets.</li>
        :type MetricNames: list of str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param ProxyIds: List of L4 proxy IDs. All L4 proxies will be selected if this field is not specified.
        :type ProxyIds: list of str
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param Filters: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`ruleId`: Filter by rule ID;</li>
<li>`proxyId`: Filter by connection ID.</li>
        :type Filters: list of QueryCondition
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.ProxyIds = None
        self.Interval = None
        self.Filters = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        self.ProxyIds = params.get("ProxyIds")
        self.Interval = params.get("Interval")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimingL4DataResponse(AbstractModel):
    """DescribeTimingL4Data response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param Data: The list of L4 traffic data recorded over time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TimingDataRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TimingDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTimingL7AnalysisDataRequest(AbstractModel):
    """DescribeTimingL7AnalysisData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricNames: The list of metrics. Values:
<li>`l7Flow_outFlux`: Access traffic;</li>
<li>`l7Flow_request`: Access requests;</li>
<li>`l7Flow_outBandwidth`: Access bandwidth.</li>
        :type MetricNames: list of str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param Filters: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`country`: Country/Region;</li>
<li>`domain`: Domain name;</li>
<li>`protocol`: Protocol type;</li>
<li>`resourceType`: Resource type;</li>
<li>`statusCode`: Status code;</li>
<li>`browserType`: Browser type;</li>
<li>`deviceType`: Device type;</li>
<li>`operatingSystemType`: OS type;</li>
<li>`tlsVersion`: TLS version;</li>
<li>`url`: URL address;</li>
<li>`referer`: Refer header;</li>
<li>`ipVersion`: IP version;</li>
<li>`tagKey`: Tag key;</li>
<li>`tagValue`: Tag value.</li>
        :type Filters: list of QueryCondition
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.Interval = None
        self.Filters = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        self.Interval = params.get("Interval")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimingL7AnalysisDataResponse(AbstractModel):
    """DescribeTimingL7AnalysisData response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of L7 traffic data recorded over time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TimingDataRecord
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TimingDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTimingL7CacheDataRequest(AbstractModel):
    """DescribeTimingL7CacheData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricNames: The query metric. Values:
<li>`l7Cache_outFlux`: Response traffic.</li>
<li>`l7Cache_request`: Response requests.</li>
<li>`l7Cache_outBandwidth`: Response bandwidth.</li>
        :type MetricNames: list of str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Filters: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`cacheType`: Cache type;</li>
<li>`domain`: Host/domain name;</li>
<li>`resourceType`: Resource type;</li>
<li>`url`: URL address;</li>
<li>`tagKey`: Tag key;</li>
<li>`tagValue`: Tag value.</li>
        :type Filters: list of QueryCondition
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.Filters = None
        self.Interval = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Interval = params.get("Interval")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimingL7CacheDataResponse(AbstractModel):
    """DescribeTimingL7CacheData response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of cached L7 time-series data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TimingDataRecord
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TimingDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTopL7AnalysisDataRequest(AbstractModel):
    """DescribeTopL7AnalysisData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricName: The query metric. Values:
<li>`l7Flow_outFlux_country`: Country the request came from;</li>
<li>`l7Flow_outFlux_statusCode`: Status code of the request;</li>
<li>`l7Flow_outFlux_domain`: Domain name of the request;</li>
<li>`l7Flow_outFlux_url`: URL of the request;</li>
<li>`l7Flow_outFlux_resourceType`: Resource type;</li>
<li>`l7Flow_outFlux_sip`: Client IP;</li>
<li>`l7Flow_outFlux_referers`: Refer header;</li>
<li>`l7Flow_outFlux_ua_device`: Device type;</li>
<li>`l7Flow_outFlux_ua_browser`: Browser type;</li>
<li>`l7Flow_outFlux_us_os`: OS type;</li>
        :type MetricName: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Limit: Queries the top n rows of data. Maximum value: 1000. Top 10 rows of data will be queried if this field is not specified.
        :type Limit: int
        :param Filters: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`country`: Country/Region;</li>
<li>`domain`: Domain name;</li>
<li>`protocol`: Protocol type;</li>
<li>`resourceType`: Resource type;</li>
<li>`statusCode`: Status code;</li>
<li>`browserType`: Browser type;</li>
<li>`deviceType`: Device type;</li>
<li>`operatingSystemType`: OS type;</li>
<li>`tlsVersion`: TLS version;</li>
<li>`url`: URL address;</li>
<li>`referer`: Refer header;</li>
<li>`ipVersion`: IP version;</li>
<li>`tagKey`: Tag key;</li>
<li>`tagValue`: Tag value.</li>
        :type Filters: list of QueryCondition
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.ZoneIds = None
        self.Limit = None
        self.Filters = None
        self.Interval = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.ZoneIds = params.get("ZoneIds")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Interval = params.get("Interval")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopL7AnalysisDataResponse(AbstractModel):
    """DescribeTopL7AnalysisData response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of top-ranked L7 traffic data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TopDataRecord
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TopDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTopL7CacheDataRequest(AbstractModel):
    """DescribeTopL7CacheData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricName: The query metric. Values:
<li>`l7Cache_outFlux_domain`: Host/Domain name;</li>
<li>`l7Cache_outFlux_url`: URL address;</li>
<li>`l7Cache_outFlux_resourceType`: Resource type;</li>
<li>`l7Cache_outFlux_statusCode`: Status code.</li>
        :type MetricName: str
        :param ZoneIds: Specifies sites by ID. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Limit: Queries the top rows of data. Top 10 rows of data will be queried if this field is not specified.
        :type Limit: int
        :param Filters: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`cacheType`: Cache type;</li>
<li>`domain`: Host/domain name;</li>
<li>`resourceType`: Resource type;</li>
<li>`url`: URL address;</li>
<li>`tagKey`: Tag key;</li>
<li>`tagValue`: Tag value.</li>
        :type Filters: list of QueryCondition
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minutes;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.ZoneIds = None
        self.Limit = None
        self.Filters = None
        self.Interval = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.ZoneIds = params.get("ZoneIds")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Interval = params.get("Interval")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopL7CacheDataResponse(AbstractModel):
    """DescribeTopL7CacheData response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of cached L7 top-ranked traffic data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TopDataRecord
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TopDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWebManagedRulesDataRequest(AbstractModel):
    """DescribeWebManagedRulesData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricNames: List of statistical metric. Values:
<li>`waf_interceptNum`: Requests blocked by WAF.</li>
        :type MetricNames: list of str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param QueryCondition: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`action`: The action;</li>
        :type QueryCondition: list of QueryCondition
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.Domains = None
        self.QueryCondition = None
        self.Interval = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Interval = params.get("Interval")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebManagedRulesDataResponse(AbstractModel):
    """DescribeWebManagedRulesData response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of WAF attack data recorded over time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of SecEntry
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWebManagedRulesHitRuleDetailRequest(AbstractModel):
    """DescribeWebManagedRulesHitRuleDetail request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param QueryCondition: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`action`: The action;</li>
        :type QueryCondition: list of QueryCondition
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ZoneIds = None
        self.Domains = None
        self.Interval = None
        self.QueryCondition = None
        self.Limit = None
        self.Offset = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Interval = params.get("Interval")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebManagedRulesHitRuleDetailResponse(AbstractModel):
    """DescribeWebManagedRulesHitRuleDetail response structure.

    """

    def __init__(self):
        r"""
        :param Data: The hit rule information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of SecHitRuleInfo
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecHitRuleInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWebManagedRulesLogRequest(AbstractModel):
    """DescribeWebManagedRulesLog request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        :param QueryCondition: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`attackType`: Attack type;</li>
<li>`riskLevel`: Risk level;</li>
<li>`action`: Action;</li>
<li>`ruleId`: Rule ID;</li>
<li>`sipCountryCode`: Country code of the attacker IP;</li>
<li>`attackIp`: Attacker IP;</li>
<li>`oriDomain`: Attacked subdomain name;</li>
<li>`eventId`: Event ID;</li>
<li>`ua`: User agent;</li>
<li>`requestMethod`: Request method;</li>
<li>`uri`: Uniform resource identifier.</li>
        :type QueryCondition: list of QueryCondition
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ZoneIds = None
        self.Domains = None
        self.Limit = None
        self.Offset = None
        self.QueryCondition = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebManagedRulesLogResponse(AbstractModel):
    """DescribeWebManagedRulesLog response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of web log data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of WebLogs
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = WebLogs()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWebProtectionAttackEventsRequest(AbstractModel):
    """DescribeWebProtectionAttackEvents request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        """
        self.StartTime = None
        self.EndTime = None
        self.ZoneIds = None
        self.Domains = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebProtectionAttackEventsResponse(AbstractModel):
    """DescribeWebProtectionAttackEvents response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of CC attack events.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of CCInterceptEvent
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = CCInterceptEvent()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWebProtectionClientIpListRequest(AbstractModel):
    """DescribeWebProtectionClientIpList request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param QueryCondition: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`action`: The action;</li>
        :type QueryCondition: list of QueryCondition
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ZoneIds = None
        self.Domains = None
        self.Interval = None
        self.QueryCondition = None
        self.Limit = None
        self.Offset = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Interval = params.get("Interval")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebProtectionClientIpListResponse(AbstractModel):
    """DescribeWebProtectionClientIpList response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of CC attacker IPs.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of SecClientIp
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecClientIp()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWebProtectionDataRequest(AbstractModel):
    """DescribeWebProtectionData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricNames: Metrics to query. Values:
<li>`ccRate_interceptNum`: Requests restricted by the rate limiting rules;</li>
<li>`ccAcl_interceptNum`: Requests restricted by the custom rules.</li>
        :type MetricNames: list of str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param QueryCondition: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`action`: The action;</li>
        :type QueryCondition: list of QueryCondition
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.Domains = None
        self.Interval = None
        self.QueryCondition = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Interval = params.get("Interval")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebProtectionDataResponse(AbstractModel):
    """DescribeWebProtectionData response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of CC protection data recorded over time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of SecEntry
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWebProtectionHitRuleDetailRequest(AbstractModel):
    """DescribeWebProtectionHitRuleDetail request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param EntityType: The rule type. Values:
<li>`rate`: Rate limiting rules;</li>
<li>`acl`: Custom rules.</li>
        :type EntityType: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param QueryCondition: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`action`: The action;</li>
        :type QueryCondition: list of QueryCondition
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.EntityType = None
        self.ZoneIds = None
        self.Domains = None
        self.QueryCondition = None
        self.Limit = None
        self.Offset = None
        self.Interval = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.EntityType = params.get("EntityType")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Interval = params.get("Interval")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebProtectionHitRuleDetailResponse(AbstractModel):
    """DescribeWebProtectionHitRuleDetail response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of hit CC protection rules.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of SecHitRuleInfo
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecHitRuleInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWebProtectionTopDataRequest(AbstractModel):
    """DescribeWebProtectionTopData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param MetricName: List of statistical metric. Values:
<li>`ccRate_requestNum_url`: Top-ranked URLs by rate limiting requests.</li>
<li>`ccRate_cipRequestNum_region`: Top-ranked client IPs by rate limiting requests.</li>
<li>`ccAcl_requestNum_url`: Top-ranked URLs by custom rule requests.</li>
<li>`ccAcl_requestNum_cip`: Top-ranked client IPs by custom rule execution requests.</li>
<li>`ccAcl_cipRequestNum_region`: Top-ranked clients by custom rule execution requests.</li>
        :type MetricName: str
        :param Interval: The query time granularity. Values:
<li>`min`: 1 minute;</li>
<li>`5min`: 5 minute;</li>
<li>`hour`: 1 hour;</li>
<li>`day`: 1 day.</li>If this field is not specified, the granularity will be determined based on the interval between the start time and end time as follows: 1-minute granularity applies for a 1-hour interval, 5-minute granularity for a 2-day interval, 1-hour granularity for a 7-day interval, and 1-day granularity for an interval of over 7 days.
        :type Interval: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param Limit: Queries the top n rows of data. Top 10 rows of data will be queried if this field is not specified.
        :type Limit: int
        :param QueryCondition: The key of the parameter QueryCondition, which is used to specify a filter. Values:
<li>`action`: The action;</li>
        :type QueryCondition: list of QueryCondition
        :param Area: Data storage region. Values:
<li>`overseas`: Global (outside the Chinese mainland);</li>
<li>`mainland`: Chinese mainland.</li>If this field is not specified, the data storage region will be determined based on the user’s location.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.Interval = None
        self.ZoneIds = None
        self.Domains = None
        self.Limit = None
        self.QueryCondition = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.Interval = params.get("Interval")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Limit = params.get("Limit")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebProtectionTopDataResponse(AbstractModel):
    """DescribeWebProtectionTopData response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of top-ranked CC protection data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of TopEntry
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TopEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeZoneSettingRequest(AbstractModel):
    """DescribeZoneSetting request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        """
        self.ZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneSettingResponse(AbstractModel):
    """DescribeZoneSetting response structure.

    """

    def __init__(self):
        r"""
        :param ZoneSetting: The site configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneSetting: :class:`tencentcloud.teo.v20220901.models.ZoneSetting`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ZoneSetting = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ZoneSetting") is not None:
            self.ZoneSetting = ZoneSetting()
            self.ZoneSetting._deserialize(params.get("ZoneSetting"))
        self.RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones request structure.

    """

    def __init__(self):
        r"""
        :param Offset: The page offset. Default value: 0
        :type Offset: int
        :param Limit: The paginated query limit. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Filters: Filter criteria. Each filter criteria can have up to 20 entries.
<li>`zone-name`:<br>   Filter by <strong>site name</strong><br>   Type: String<br>   Required: No<li>`zone-id`:<br>   Filter by <strong>site ID</strong>, such as zone-xxx<br>   Type: String<br>   Required: No<li>`status`:<br>   Filter by <strong>site status</strong><br>   Type: String<br>   Required: No<li>`tag-key`:<br>   Filter by <strong>tag key</strong><br>   Type: String<br>   Required: No<li>`tag-value`:<br>   Filter by <strong>tag value</strong><br>   Type: String<br>   Required: No<li>`Fuzzy`:<br>   Filter by <strong>values in fuzzy query</strong> (only `zone-name` allowed). Values limit: 1<br>   Type: Boolean<br>   Required: No<br>   Default value: false
        :type Filters: list of AdvancedFilter
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZonesResponse(AbstractModel):
    """DescribeZones response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of eligible sites.
        :type TotalCount: int
        :param Zones: Details of sites
        :type Zones: list of Zone
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Zones = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Zones") is not None:
            self.Zones = []
            for item in params.get("Zones"):
                obj = Zone()
                obj._deserialize(item)
                self.Zones.append(obj)
        self.RequestId = params.get("RequestId")


class DetailHost(AbstractModel):
    """Domain name configuration information

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param Status: The acceleration status. Values:
<li>`process`: In progress</li>
<li>`online`: Enabled</li>
<li>`offline`: Disabled</li>
        :type Status: str
        :param Host: The domain name.
        :type Host: str
        :param ZoneName: Name of the site
        :type ZoneName: str
        :param Cname: The assigned CNAME
        :type Cname: str
        :param Id: The resource ID.
        :type Id: str
        :param InstanceId: The instance ID.
        :type InstanceId: str
        :param Lock: The lock status.
        :type Lock: int
        :param Mode: The domain name status.
        :type Mode: int
        :param Area: The acceleration area of the domain name. Values:
<li>`global`: Global.</li>
<li>`mainland`: Chinese mainland.</li>
<li>`overseas`: Outside the Chinese mainland.</li>
        :type Area: str
        :param AccelerateType: The acceleration type configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccelerateType: :class:`tencentcloud.teo.v20220901.models.AccelerateType`
        :param Https: The HTTPS configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Https: :class:`tencentcloud.teo.v20220901.models.Https`
        :param CacheConfig: The cache configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CacheConfig: :class:`tencentcloud.teo.v20220901.models.CacheConfig`
        :param Origin: The origin configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Origin: :class:`tencentcloud.teo.v20220901.models.Origin`
        :param SecurityType: The security type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SecurityType: :class:`tencentcloud.teo.v20220901.models.SecurityType`
        :param CacheKey: The cache key configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CacheKey: :class:`tencentcloud.teo.v20220901.models.CacheKey`
        :param Compression: The smart compression configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Compression: :class:`tencentcloud.teo.v20220901.models.Compression`
        :param Waf: The WAF protection configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Waf: :class:`tencentcloud.teo.v20220901.models.Waf`
        :param CC: The CC protection configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CC: :class:`tencentcloud.teo.v20220901.models.CC`
        :param DDoS: DDoS mitigation configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type DDoS: :class:`tencentcloud.teo.v20220901.models.DDoS`
        :param SmartRouting: The smart routing configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SmartRouting: :class:`tencentcloud.teo.v20220901.models.SmartRouting`
        :param Ipv6: The IPv6 access configuration item.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Ipv6: :class:`tencentcloud.teo.v20220901.models.Ipv6`
        :param ClientIpCountry: 
        :type ClientIpCountry: :class:`tencentcloud.teo.v20220901.models.ClientIpCountry`
        """
        self.ZoneId = None
        self.Status = None
        self.Host = None
        self.ZoneName = None
        self.Cname = None
        self.Id = None
        self.InstanceId = None
        self.Lock = None
        self.Mode = None
        self.Area = None
        self.AccelerateType = None
        self.Https = None
        self.CacheConfig = None
        self.Origin = None
        self.SecurityType = None
        self.CacheKey = None
        self.Compression = None
        self.Waf = None
        self.CC = None
        self.DDoS = None
        self.SmartRouting = None
        self.Ipv6 = None
        self.ClientIpCountry = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Status = params.get("Status")
        self.Host = params.get("Host")
        self.ZoneName = params.get("ZoneName")
        self.Cname = params.get("Cname")
        self.Id = params.get("Id")
        self.InstanceId = params.get("InstanceId")
        self.Lock = params.get("Lock")
        self.Mode = params.get("Mode")
        self.Area = params.get("Area")
        if params.get("AccelerateType") is not None:
            self.AccelerateType = AccelerateType()
            self.AccelerateType._deserialize(params.get("AccelerateType"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("CacheConfig") is not None:
            self.CacheConfig = CacheConfig()
            self.CacheConfig._deserialize(params.get("CacheConfig"))
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        if params.get("SecurityType") is not None:
            self.SecurityType = SecurityType()
            self.SecurityType._deserialize(params.get("SecurityType"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("Waf") is not None:
            self.Waf = Waf()
            self.Waf._deserialize(params.get("Waf"))
        if params.get("CC") is not None:
            self.CC = CC()
            self.CC._deserialize(params.get("CC"))
        if params.get("DDoS") is not None:
            self.DDoS = DDoS()
            self.DDoS._deserialize(params.get("DDoS"))
        if params.get("SmartRouting") is not None:
            self.SmartRouting = SmartRouting()
            self.SmartRouting._deserialize(params.get("SmartRouting"))
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6()
            self.Ipv6._deserialize(params.get("Ipv6"))
        if params.get("ClientIpCountry") is not None:
            self.ClientIpCountry = ClientIpCountry()
            self.ClientIpCountry._deserialize(params.get("ClientIpCountry"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DnsData(AbstractModel):
    """DNS data points

    """

    def __init__(self):
        r"""
        :param Time: The time.
        :type Time: str
        :param Value: The value.
        :type Value: int
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DnsRecord(AbstractModel):
    """DNS record

    """

    def __init__(self):
        r"""
        :param DnsRecordId: The record ID.
        :type DnsRecordId: str
        :param DnsRecordType: The DNS record type. Values:
<li>`A`: Point a domain name to an IPv4 address, such as 8.8.8.8.</li>
<li>`AAAA`: Point a domain name to an IPv6 address.</li>
<li>`MX`: It is used for email servers. The record value and priority parameters are provided by email service providers. If there are multiple MX records, the lower the priority value, the higher the priority.</li>
<li>`CNAME`: Point a domain name to another domain name that can be resolved to an IP address.</li>
<li>`TXT`: Identify and describe a domain name. It is usually used for domain verification and as SPF records (for anti-spam).</li>
<li>`NS`: If you need to authorize a subdomain name to another DNS service provider for DNS resolution, you need to add an NS record. You cannot add an NS record for a root domain name.</li>
<li>`CAA`: Specify CAs to issue certificates for sites.</li>
<li>`SRV`: Identify a service used by a server. It is commonly used in Microsoft directory management.</li>
        :type DnsRecordType: str
        :param DnsRecordName: The record name.
        :type DnsRecordName: str
        :param Content: The record value.
        :type Content: str
        :param Mode: The proxy mode. Values:
<li>`dns_only`: Only DNS</li>
<li>`proxied`: Proxied</li>
        :type Mode: str
        :param TTL: TTL (in seconds). The smaller the value, the faster the record changes take effect.
        :type TTL: int
        :param Priority: The MX record priority. The smaller the value, the higher the priority.
        :type Priority: int
        :param CreatedOn: The creation time.
        :type CreatedOn: str
        :param ModifiedOn: The modification time.
        :type ModifiedOn: str
        :param Locked: The lock status of the domain name.
        :type Locked: bool
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param ZoneName: The site name.
        :type ZoneName: str
        :param Status: The DNS record status. Values:
<li>`active`: Activated</li>
<li>`pending`: Deactivated</li>
        :type Status: str
        :param Cname: The CNAME address.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Cname: str
        :param DomainStatus: The service used by the domain name. Values:
<li>`lb`: Load balancing</li>
<li>`security`: Security protection</li>
<li>`l4`: L4 proxy</li>
        :type DomainStatus: list of str
        """
        self.DnsRecordId = None
        self.DnsRecordType = None
        self.DnsRecordName = None
        self.Content = None
        self.Mode = None
        self.TTL = None
        self.Priority = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.Locked = None
        self.ZoneId = None
        self.ZoneName = None
        self.Status = None
        self.Cname = None
        self.DomainStatus = None


    def _deserialize(self, params):
        self.DnsRecordId = params.get("DnsRecordId")
        self.DnsRecordType = params.get("DnsRecordType")
        self.DnsRecordName = params.get("DnsRecordName")
        self.Content = params.get("Content")
        self.Mode = params.get("Mode")
        self.TTL = params.get("TTL")
        self.Priority = params.get("Priority")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        self.Locked = params.get("Locked")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.Status = params.get("Status")
        self.Cname = params.get("Cname")
        self.DomainStatus = params.get("DomainStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DnssecInfo(AbstractModel):
    """DNSSEC information

    """

    def __init__(self):
        r"""
        :param Flags: Flag
        :type Flags: int
        :param Algorithm: Encryption algorithm
        :type Algorithm: str
        :param KeyType: Encryption type
        :type KeyType: str
        :param DigestType: Digest type
        :type DigestType: str
        :param DigestAlgorithm: Digest algorithm
        :type DigestAlgorithm: str
        :param Digest: Digest message
        :type Digest: str
        :param DS: DS record value
        :type DS: str
        :param KeyTag: Key tag
        :type KeyTag: int
        :param PublicKey: Public key
        :type PublicKey: str
        """
        self.Flags = None
        self.Algorithm = None
        self.KeyType = None
        self.DigestType = None
        self.DigestAlgorithm = None
        self.Digest = None
        self.DS = None
        self.KeyTag = None
        self.PublicKey = None


    def _deserialize(self, params):
        self.Flags = params.get("Flags")
        self.Algorithm = params.get("Algorithm")
        self.KeyType = params.get("KeyType")
        self.DigestType = params.get("DigestType")
        self.DigestAlgorithm = params.get("DigestAlgorithm")
        self.Digest = params.get("Digest")
        self.DS = params.get("DS")
        self.KeyTag = params.get("KeyTag")
        self.PublicKey = params.get("PublicKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadL4LogsRequest(AbstractModel):
    """DownloadL4Logs request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param ProxyIds: List of L4 proxy IDs.
        :type ProxyIds: list of str
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        """
        self.StartTime = None
        self.EndTime = None
        self.ZoneIds = None
        self.ProxyIds = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ZoneIds = params.get("ZoneIds")
        self.ProxyIds = params.get("ProxyIds")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadL4LogsResponse(AbstractModel):
    """DownloadL4Logs response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of L4 log data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of L4OfflineLog
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = L4OfflineLog()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DownloadL7LogsRequest(AbstractModel):
    """DownloadL7Logs request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time.
        :type StartTime: str
        :param EndTime: The end time.
        :type EndTime: str
        :param ZoneIds: List of sites to be queried. All sites will be selected if this field is not specified.
        :type ZoneIds: list of str
        :param Domains: List of subdomain names to be queried. All subdomain names will be selected if this field is not specified.
        :type Domains: list of str
        :param Limit: Limit on paginated queries. Default value: 20. Maximum value: 1000.
        :type Limit: int
        :param Offset: The page offset. Default value: 0.
        :type Offset: int
        """
        self.StartTime = None
        self.EndTime = None
        self.ZoneIds = None
        self.Domains = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadL7LogsResponse(AbstractModel):
    """DownloadL7Logs response structure.

    """

    def __init__(self):
        r"""
        :param Data: The list of L7 log data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of L7OfflineLog
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = L7OfflineLog()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class FailReason(AbstractModel):
    """Failure reason

    """

    def __init__(self):
        r"""
        :param Reason: Failure reason.
        :type Reason: str
        :param Targets: List of resources failed to be processed.
        :type Targets: list of str
        """
        self.Reason = None
        self.Targets = None


    def _deserialize(self, params):
        self.Reason = params.get("Reason")
        self.Targets = params.get("Targets")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileAscriptionInfo(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param IdentifyPath: 
        :type IdentifyPath: str
        :param IdentifyContent: 
        :type IdentifyContent: str
        """
        self.IdentifyPath = None
        self.IdentifyContent = None


    def _deserialize(self, params):
        self.IdentifyPath = params.get("IdentifyPath")
        self.IdentifyContent = params.get("IdentifyContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Key-value pair filters for conditional filtering queries, such as filtering ID, name, and status.
    If there are multiple filters, they’re combined with `AND`.
    Values of the same Filter are combined with `OR`.

    """

    def __init__(self):
        r"""
        :param Name: The name of the field to filter.
        :type Name: str
        :param Values: Value of the filtered field.
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FollowOrigin(AbstractModel):
    """The origin cache configuration

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable the configuration of following the origin server. Valid values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForceRedirect(AbstractModel):
    """Force HTTPS redirect configuration

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable force HTTPS redirect. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param RedirectStatusCode: Redirect status code. Values:
<li>`301`: 301 redirect</li>
<li>`302`: 302 redirect</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type RedirectStatusCode: int
        """
        self.Switch = None
        self.RedirectStatusCode = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.RedirectStatusCode = params.get("RedirectStatusCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Header(AbstractModel):
    """HTTP header, used as input for the CreatePrefetchTask API

    """

    def __init__(self):
        r"""
        :param Name: HTTP header name
        :type Name: str
        :param Value: HTTP header value
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Hsts(AbstractModel):
    """HSTS configuration

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable the configuration. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param MaxAge: The MaxAge value in seconds. Maximum value: `86400` (one day)
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxAge: int
        :param IncludeSubDomains: Whether to contain subdomain names. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type IncludeSubDomains: str
        :param Preload: Whether to enable preloading. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Preload: str
        """
        self.Switch = None
        self.MaxAge = None
        self.IncludeSubDomains = None
        self.Preload = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.MaxAge = params.get("MaxAge")
        self.IncludeSubDomains = params.get("IncludeSubDomains")
        self.Preload = params.get("Preload")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Https(AbstractModel):
    """Domain name HTTPS acceleration configuration. This is disabled by default.

    """

    def __init__(self):
        r"""
        :param Http2: Whether to enable HTTP2. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Http2: str
        :param OcspStapling: Whether to enable OCSP. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type OcspStapling: str
        :param TlsVersion: TLS version. Values:
<li>`TLSv1`: TLSv1 version</li>
<li>`TLSV1.1`: TLSv1.1 version</li>
<li>`TLSV1.2`: TLSv1.2 version</li>
<li>`TLSv1.3`: TLSv1.3 version</li>Only consecutive versions can be enabled at the same time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TlsVersion: list of str
        :param Hsts: HSTS Configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type Hsts: :class:`tencentcloud.teo.v20220901.models.Hsts`
        :param CertInfo: The certificate configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertInfo: list of ServerCertInfo
        """
        self.Http2 = None
        self.OcspStapling = None
        self.TlsVersion = None
        self.Hsts = None
        self.CertInfo = None


    def _deserialize(self, params):
        self.Http2 = params.get("Http2")
        self.OcspStapling = params.get("OcspStapling")
        self.TlsVersion = params.get("TlsVersion")
        if params.get("Hsts") is not None:
            self.Hsts = Hsts()
            self.Hsts._deserialize(params.get("Hsts"))
        if params.get("CertInfo") is not None:
            self.CertInfo = []
            for item in params.get("CertInfo"):
                obj = ServerCertInfo()
                obj._deserialize(item)
                self.CertInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Identification(AbstractModel):
    """The site verification information

    """

    def __init__(self):
        r"""
        :param ZoneName: The site name.
        :type ZoneName: str
        :param Status: The verification status. Values:
<li>`pending`: The verification is ongoing.</li>
<li>`finished`: The verification completed.</li>
        :type Status: str
        :param Ascription: The site ownership information.
        :type Ascription: :class:`tencentcloud.teo.v20220901.models.AscriptionInfo`
        :param OriginalNameServers: The NS record of the domain name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginalNameServers: list of str
        :param FileAscription: 
        :type FileAscription: :class:`tencentcloud.teo.v20220901.models.FileAscriptionInfo`
        """
        self.ZoneName = None
        self.Status = None
        self.Ascription = None
        self.OriginalNameServers = None
        self.FileAscription = None


    def _deserialize(self, params):
        self.ZoneName = params.get("ZoneName")
        self.Status = params.get("Status")
        if params.get("Ascription") is not None:
            self.Ascription = AscriptionInfo()
            self.Ascription._deserialize(params.get("Ascription"))
        self.OriginalNameServers = params.get("OriginalNameServers")
        if params.get("FileAscription") is not None:
            self.FileAscription = FileAscriptionInfo()
            self.FileAscription._deserialize(params.get("FileAscription"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdentifyZoneRequest(AbstractModel):
    """IdentifyZone request structure.

    """

    def __init__(self):
        r"""
        :param ZoneName: The site name.
        :type ZoneName: str
        """
        self.ZoneName = None


    def _deserialize(self, params):
        self.ZoneName = params.get("ZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdentifyZoneResponse(AbstractModel):
    """IdentifyZone response structure.

    """

    def __init__(self):
        r"""
        :param Ascription: The site ownership information.
        :type Ascription: :class:`tencentcloud.teo.v20220901.models.AscriptionInfo`
        :param FileAscription: 
        :type FileAscription: :class:`tencentcloud.teo.v20220901.models.FileAscriptionInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Ascription = None
        self.FileAscription = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Ascription") is not None:
            self.Ascription = AscriptionInfo()
            self.Ascription._deserialize(params.get("Ascription"))
        if params.get("FileAscription") is not None:
            self.FileAscription = FileAscriptionInfo()
            self.FileAscription._deserialize(params.get("FileAscription"))
        self.RequestId = params.get("RequestId")


class Ipv6(AbstractModel):
    """IPv6 access configuration

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable IPv6 access. Values:
<li>`on`: Enable IPv6 access.</li>
<li>`off`: Disable IPv6 access.</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4OfflineLog(AbstractModel):
    """The L7 log details

    """

    def __init__(self):
        r"""
        :param LogTime: The start time of the log packaging.
        :type LogTime: int
        :param ProxyId: The L4 proxy ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProxyId: str
        :param Size: The log size, in bytes.
        :type Size: int
        :param Url: The download address.
        :type Url: str
        :param LogPacketName: The log package name.
        :type LogPacketName: str
        :param Area: The acceleration region. Values:
<li>`mainland`: Chinese mainland;</li>
<li>`overseas`: Global (outside the Chinese mainland);</li>
        :type Area: str
        """
        self.LogTime = None
        self.ProxyId = None
        self.Size = None
        self.Url = None
        self.LogPacketName = None
        self.Area = None


    def _deserialize(self, params):
        self.LogTime = params.get("LogTime")
        self.ProxyId = params.get("ProxyId")
        self.Size = params.get("Size")
        self.Url = params.get("Url")
        self.LogPacketName = params.get("LogPacketName")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7OfflineLog(AbstractModel):
    """Layer-7 offline log details

    """

    def __init__(self):
        r"""
        :param LogTime: Start time of the log packaging
        :type LogTime: int
        :param Domain: The subdomain name.
        :type Domain: str
        :param Size: Log size, in bytes.
        :type Size: int
        :param Url: Download address
        :type Url: str
        :param LogPacketName: Log package name
        :type LogPacketName: str
        :param Area: Acceleration region. Values:
<li>`mainland`: Chinese mainland;</li>
<li>`overseas`: Global (outside the Chinese mainland);</li>
        :type Area: str
        """
        self.LogTime = None
        self.Domain = None
        self.Size = None
        self.Url = None
        self.LogPacketName = None
        self.Area = None


    def _deserialize(self, params):
        self.LogTime = params.get("LogTime")
        self.Domain = params.get("Domain")
        self.Size = params.get("Size")
        self.Url = params.get("Url")
        self.LogPacketName = params.get("LogPacketName")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogSetInfo(AbstractModel):
    """Logset information

    """

    def __init__(self):
        r"""
        :param LogSetRegion: Region of the logset.
        :type LogSetRegion: str
        :param LogSetName: Name of the logset.
        :type LogSetName: str
        :param LogSetId: ID of the logset.
        :type LogSetId: str
        :param Deleted: Whether the logset is deleted. Values:
<li>`no`: The logset is not deleted;</li>
<li>`yes`: The logset is deleted.</li>
        :type Deleted: str
        """
        self.LogSetRegion = None
        self.LogSetName = None
        self.LogSetId = None
        self.Deleted = None


    def _deserialize(self, params):
        self.LogSetRegion = params.get("LogSetRegion")
        self.LogSetName = params.get("LogSetName")
        self.LogSetId = params.get("LogSetId")
        self.Deleted = params.get("Deleted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogTopicDetailInfo(AbstractModel):
    """Details of the shipping task

    """

    def __init__(self):
        r"""
        :param TaskName: Name of the shipping task.
        :type TaskName: str
        :param LogSetRegion: Region of the logset.
        :type LogSetRegion: str
        :param EntityType: Type of the shipping task.
        :type EntityType: str
        :param EntityList: List of tasks.
        :type EntityList: list of str
        :param LogSetId: ID of the logset.
        :type LogSetId: str
        :param LogSetName: Name of the logset.
        :type LogSetName: str
        :param TopicId: Topic ID of the shipping task.
        :type TopicId: str
        :param TopicName: Topic name of the shipping task.
        :type TopicName: str
        :param Period: Retention period of the shipping task topic. Unit: day.
        :type Period: int
        :param Enabled: Whether the shipping task is enabled.
        :type Enabled: bool
        :param CreateTime: Creation time in the format of YYYY-mm-dd HH:MM:SS.
        :type CreateTime: str
        :param Area: Acceleration region. Values:
<li>`mainland`: Chinese mainland;</li>
<li>`overseas`: Global (outside the Chinese mainland).</li>
        :type Area: str
        :param ZoneId: ID of the site.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneId: str
        :param ZoneName: Name of the site.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneName: str
        :param Deleted: Whether the shipping task is deleted. Values:
<li>`yes`: The shipping task is deleted;</li>
<li>`no`: The shipping task is not deleted.</li>
        :type Deleted: str
        """
        self.TaskName = None
        self.LogSetRegion = None
        self.EntityType = None
        self.EntityList = None
        self.LogSetId = None
        self.LogSetName = None
        self.TopicId = None
        self.TopicName = None
        self.Period = None
        self.Enabled = None
        self.CreateTime = None
        self.Area = None
        self.ZoneId = None
        self.ZoneName = None
        self.Deleted = None


    def _deserialize(self, params):
        self.TaskName = params.get("TaskName")
        self.LogSetRegion = params.get("LogSetRegion")
        self.EntityType = params.get("EntityType")
        self.EntityList = params.get("EntityList")
        self.LogSetId = params.get("LogSetId")
        self.LogSetName = params.get("LogSetName")
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.Period = params.get("Period")
        self.Enabled = params.get("Enabled")
        self.CreateTime = params.get("CreateTime")
        self.Area = params.get("Area")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.Deleted = params.get("Deleted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaxAge(AbstractModel):
    """Browser cache rule configuration, which is used to set the default value of `MaxAge` and is disabled by default.

    """

    def __init__(self):
        r"""
        :param FollowOrigin: Whether to follow the origin server. Values:
<li>`on`: Follow the origin server and ignore the field MaxAgeTime;</li>
<li>`off`: Do not follow the origin server and apply the field MaxAgeTime.</li>
        :type FollowOrigin: str
        :param MaxAgeTime: Specifies the maximum amount of time (in seconds). The maximum value is 365 days.
Note: The value `0` means not to cache.
        :type MaxAgeTime: int
        """
        self.FollowOrigin = None
        self.MaxAgeTime = None


    def _deserialize(self, params):
        self.FollowOrigin = params.get("FollowOrigin")
        self.MaxAgeTime = params.get("MaxAgeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDefaultCertificateRequest(AbstractModel):
    """ModifyDefaultCertificate request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site.
        :type ZoneId: str
        :param CertId: ID of the certificate.
        :type CertId: str
        :param Status: Status of the certificate. Values:
<li>`deployed`: The certificate is deployed;</li>
<li>`disabled`: The certificate is disabled.</li>When a deployment fails, you can try again.
        :type Status: str
        """
        self.ZoneId = None
        self.CertId = None
        self.Status = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.CertId = params.get("CertId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDefaultCertificateResponse(AbstractModel):
    """ModifyDefaultCertificate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDnsRecordRequest(AbstractModel):
    """ModifyDnsRecord request structure.

    """

    def __init__(self):
        r"""
        :param DnsRecordId: The record ID.
        :type DnsRecordId: str
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param DnsRecordType: The DNS record type. Values:
<li>`A`: Point a domain name to an IPv4 address, such as 8.8.8.8.</li>
<li>`AAAA`: Point a domain name to an IPv6 address.</li>
<li>`MX`: It is used for email servers. The record value and priority parameters are provided by email service providers. If there are multiple MX records, the lower the priority value, the higher the priority.</li>
<li>`CNAME`: Point a domain name to another domain name that can be resolved to an IP address.</li>
<li>`TXT`: Identify and describe a domain name. It is usually used for domain verification and as SPF records (for anti-spam).</li>
<li>`NS`: If you need to authorize a subdomain name to another DNS service provider for DNS resolution, you need to add an NS record. You cannot add an NS record for a root domain name.</li>
<li>`CAA`: Specify CAs to issue certificates for sites.</li>
<li>`SRV`: Identify a service used by a server. It is commonly used in Microsoft directory management.</li>
        :type DnsRecordType: str
        :param DnsRecordName: The record name, which consists of the host record and site name. Note that the original configuration will be used if this field is not specified.
        :type DnsRecordName: str
        :param Content: The record content. Note that the original configuration will be used if this field is not specified.
        :type Content: str
        :param TTL: TTL (in seconds). The smaller the value, the faster the record changes take effect. Default value: 300. Note that the original configuration will be used if this field is not specified.
        :type TTL: int
        :param Priority: Specifies a value in the range 1–50 when you make changes to the MX records. A smaller value indicates higher priority. Note that the default value 0 will be used if this field is not specified.
        :type Priority: int
        :param Mode: The proxy mode. Values:
<li>`dns_only`: Only DNS</li>
<li>`proxied`: Proxied</li></li>The original configuration will apply if this field is not specified.
        :type Mode: str
        """
        self.DnsRecordId = None
        self.ZoneId = None
        self.DnsRecordType = None
        self.DnsRecordName = None
        self.Content = None
        self.TTL = None
        self.Priority = None
        self.Mode = None


    def _deserialize(self, params):
        self.DnsRecordId = params.get("DnsRecordId")
        self.ZoneId = params.get("ZoneId")
        self.DnsRecordType = params.get("DnsRecordType")
        self.DnsRecordName = params.get("DnsRecordName")
        self.Content = params.get("Content")
        self.TTL = params.get("TTL")
        self.Priority = params.get("Priority")
        self.Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDnsRecordResponse(AbstractModel):
    """ModifyDnsRecord response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDnssecRequest(AbstractModel):
    """ModifyDnssec request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param Status: The DNSSEC status. Values:
<li>`enabled`: Enabled</li>
<li>`disabled`: Disabled</li>
        :type Status: str
        """
        self.ZoneId = None
        self.Status = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDnssecResponse(AbstractModel):
    """ModifyDnssec response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyHostsCertificateRequest(AbstractModel):
    """ModifyHostsCertificate request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site.
        :type ZoneId: str
        :param Hosts: List of domain names that the certificate will be attached to.
        :type Hosts: list of str
        :param ServerCertInfo: Certificate information. Note that only `CertId` is required. If it is not specified, the default certificate will be used.
        :type ServerCertInfo: list of ServerCertInfo
        """
        self.ZoneId = None
        self.Hosts = None
        self.ServerCertInfo = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Hosts = params.get("Hosts")
        if params.get("ServerCertInfo") is not None:
            self.ServerCertInfo = []
            for item in params.get("ServerCertInfo"):
                obj = ServerCertInfo()
                obj._deserialize(item)
                self.ServerCertInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHostsCertificateResponse(AbstractModel):
    """ModifyHostsCertificate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLogTopicTaskRequest(AbstractModel):
    """ModifyLogTopicTask request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site.
        :type ZoneId: str
        :param LogSetRegion: Region of the logset.
        :type LogSetRegion: str
        :param LogSetId: ID of the logset.
        :type LogSetId: str
        :param TopicId: ID of the log topic.
        :type TopicId: str
        :param EntityType: Type of the shipping entity. Values:
<li>`domain`: L7 acceleration logs;</li>
<li>`application`: L4 acceleration logs;</li>
<li>`web-rateLiming`: Rate limiting logs;</li>
<li>`web-attack`: Web security logs;</li>
<li>`web-rule`: Custom rule logs;</li>
<li>`web-bot`: Bot management logs.</li>
        :type EntityType: str
        :param TaskName: Name of the shipping task.
        :type TaskName: str
        :param TopicName: The new topic name. If you do not specify this field, no changes will be made.
        :type TopicName: str
        :param LogSetName: The new logset name.
        :type LogSetName: str
        :param Period: The retention period of the updated logset.
        :type Period: int
        :param DropEntityList: List of shipping entities to be deleted.
        :type DropEntityList: list of str
        :param AddedEntityList: List of shipping entities to be added.
        :type AddedEntityList: list of str
        """
        self.ZoneId = None
        self.LogSetRegion = None
        self.LogSetId = None
        self.TopicId = None
        self.EntityType = None
        self.TaskName = None
        self.TopicName = None
        self.LogSetName = None
        self.Period = None
        self.DropEntityList = None
        self.AddedEntityList = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.LogSetRegion = params.get("LogSetRegion")
        self.LogSetId = params.get("LogSetId")
        self.TopicId = params.get("TopicId")
        self.EntityType = params.get("EntityType")
        self.TaskName = params.get("TaskName")
        self.TopicName = params.get("TopicName")
        self.LogSetName = params.get("LogSetName")
        self.Period = params.get("Period")
        self.DropEntityList = params.get("DropEntityList")
        self.AddedEntityList = params.get("AddedEntityList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLogTopicTaskResponse(AbstractModel):
    """ModifyLogTopicTask response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRulePriorityRequest(AbstractModel):
    """ModifyRulePriority request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param RuleIds: Order of rule IDs. If there are multiple rules, they will be executed in order from top to bottom.
        :type RuleIds: list of str
        """
        self.ZoneId = None
        self.RuleIds = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.RuleIds = params.get("RuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRulePriorityResponse(AbstractModel):
    """ModifyRulePriority response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRuleRequest(AbstractModel):
    """ModifyRule request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param RuleName: The rule name. It is a string that can contain 1–255 characters.
        :type RuleName: str
        :param Rules: The rule content.
        :type Rules: list of Rule
        :param RuleId: The rule ID.
        :type RuleId: str
        :param Status: Rule status. Values:
<li>`enable`: Enabled</li>
<li>`disable`: Disabled</li>
        :type Status: str
        """
        self.ZoneId = None
        self.RuleName = None
        self.Rules = None
        self.RuleId = None
        self.Status = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.RuleName = params.get("RuleName")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = Rule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RuleId = params.get("RuleId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRuleResponse(AbstractModel):
    """ModifyRule response structure.

    """

    def __init__(self):
        r"""
        :param RuleId: Rule ID
        :type RuleId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class ModifyZoneCnameSpeedUpRequest(AbstractModel):
    """ModifyZoneCnameSpeedUp request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param Status: The CNAME acceleration status. Values:
<li>`enabled`: Enabled</li>
<li>`disabled`: Disabled</li>
        :type Status: str
        """
        self.ZoneId = None
        self.Status = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneCnameSpeedUpResponse(AbstractModel):
    """ModifyZoneCnameSpeedUp response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyZoneRequest(AbstractModel):
    """ModifyZone request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param Type: The site access method. Values:
<li>`full`: Access through a name server.</li>
<li>`partial`: Access through a CNAME record.</li>The original configuration will apply if this field is not specified.
        :type Type: str
        :param VanityNameServers: The custom name servers. If this field is not specified, the default name servers will be used.
        :type VanityNameServers: :class:`tencentcloud.teo.v20220901.models.VanityNameServers`
        """
        self.ZoneId = None
        self.Type = None
        self.VanityNameServers = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Type = params.get("Type")
        if params.get("VanityNameServers") is not None:
            self.VanityNameServers = VanityNameServers()
            self.VanityNameServers._deserialize(params.get("VanityNameServers"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneResponse(AbstractModel):
    """ModifyZone response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyZoneSettingRequest(AbstractModel):
    """ModifyZoneSetting request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID to be modified.
        :type ZoneId: str
        :param CacheConfig: Cache expiration time configuration
The original configuration will apply if this field is not specified.
        :type CacheConfig: :class:`tencentcloud.teo.v20220901.models.CacheConfig`
        :param CacheKey: The node cache key configuration.
The original configuration will apply if this field is not specified.
        :type CacheKey: :class:`tencentcloud.teo.v20220901.models.CacheKey`
        :param MaxAge: The browser cache configuration.
The original configuration will apply if this field is not specified.
        :type MaxAge: :class:`tencentcloud.teo.v20220901.models.MaxAge`
        :param OfflineCache: The offline cache configuration.
The original configuration will apply if this field is not specified.
        :type OfflineCache: :class:`tencentcloud.teo.v20220901.models.OfflineCache`
        :param Quic: The QUIC access configuration.
The original configuration will apply if this field is not specified.
        :type Quic: :class:`tencentcloud.teo.v20220901.models.Quic`
        :param PostMaxSize: The POST transport configuration.
The original configuration will apply if this field is not specified.
        :type PostMaxSize: :class:`tencentcloud.teo.v20220901.models.PostMaxSize`
        :param Compression: The smart compression configuration.
The original configuration will apply if this field is not specified.
        :type Compression: :class:`tencentcloud.teo.v20220901.models.Compression`
        :param UpstreamHttp2: The HTTP2 origin-pull configuration.
The original configuration will apply if this field is not specified.
        :type UpstreamHttp2: :class:`tencentcloud.teo.v20220901.models.UpstreamHttp2`
        :param ForceRedirect: The force HTTPS redirect configuration.
The original configuration will apply if this field is not specified.
        :type ForceRedirect: :class:`tencentcloud.teo.v20220901.models.ForceRedirect`
        :param Https: The HTTPS acceleration configuration.
The original configuration will apply if this field is not specified.
        :type Https: :class:`tencentcloud.teo.v20220901.models.Https`
        :param Origin: The origin server configuration.
The original configuration will apply if this field is not specified.
        :type Origin: :class:`tencentcloud.teo.v20220901.models.Origin`
        :param SmartRouting: The smart acceleration configuration.
The original configuration will apply if this field is not specified.
        :type SmartRouting: :class:`tencentcloud.teo.v20220901.models.SmartRouting`
        :param WebSocket: The WebSocket configuration.
The original configuration will apply if this field is not specified.
        :type WebSocket: :class:`tencentcloud.teo.v20220901.models.WebSocket`
        :param ClientIpHeader: The origin-pull client IP header configuration.
The original configuration will apply if this field is not specified.
        :type ClientIpHeader: :class:`tencentcloud.teo.v20220901.models.ClientIpHeader`
        :param CachePrefresh: The cache prefresh configuration.
The original configuration will apply if this field is not specified.
        :type CachePrefresh: :class:`tencentcloud.teo.v20220901.models.CachePrefresh`
        :param Ipv6: The IPv6 access configuration.
The original configuration will apply if this field is not specified.
        :type Ipv6: :class:`tencentcloud.teo.v20220901.models.Ipv6`
        :param ClientIpCountry: 
        :type ClientIpCountry: :class:`tencentcloud.teo.v20220901.models.ClientIpCountry`
        """
        self.ZoneId = None
        self.CacheConfig = None
        self.CacheKey = None
        self.MaxAge = None
        self.OfflineCache = None
        self.Quic = None
        self.PostMaxSize = None
        self.Compression = None
        self.UpstreamHttp2 = None
        self.ForceRedirect = None
        self.Https = None
        self.Origin = None
        self.SmartRouting = None
        self.WebSocket = None
        self.ClientIpHeader = None
        self.CachePrefresh = None
        self.Ipv6 = None
        self.ClientIpCountry = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("CacheConfig") is not None:
            self.CacheConfig = CacheConfig()
            self.CacheConfig._deserialize(params.get("CacheConfig"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        if params.get("OfflineCache") is not None:
            self.OfflineCache = OfflineCache()
            self.OfflineCache._deserialize(params.get("OfflineCache"))
        if params.get("Quic") is not None:
            self.Quic = Quic()
            self.Quic._deserialize(params.get("Quic"))
        if params.get("PostMaxSize") is not None:
            self.PostMaxSize = PostMaxSize()
            self.PostMaxSize._deserialize(params.get("PostMaxSize"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("UpstreamHttp2") is not None:
            self.UpstreamHttp2 = UpstreamHttp2()
            self.UpstreamHttp2._deserialize(params.get("UpstreamHttp2"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        if params.get("SmartRouting") is not None:
            self.SmartRouting = SmartRouting()
            self.SmartRouting._deserialize(params.get("SmartRouting"))
        if params.get("WebSocket") is not None:
            self.WebSocket = WebSocket()
            self.WebSocket._deserialize(params.get("WebSocket"))
        if params.get("ClientIpHeader") is not None:
            self.ClientIpHeader = ClientIpHeader()
            self.ClientIpHeader._deserialize(params.get("ClientIpHeader"))
        if params.get("CachePrefresh") is not None:
            self.CachePrefresh = CachePrefresh()
            self.CachePrefresh._deserialize(params.get("CachePrefresh"))
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6()
            self.Ipv6._deserialize(params.get("Ipv6"))
        if params.get("ClientIpCountry") is not None:
            self.ClientIpCountry = ClientIpCountry()
            self.ClientIpCountry._deserialize(params.get("ClientIpCountry"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneSettingResponse(AbstractModel):
    """ModifyZoneSetting response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyZoneStatusRequest(AbstractModel):
    """ModifyZoneStatus request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param Paused: The site status. Values:
<li>`false`: Disabled</li>
<li>`true`: Enabled</li>
        :type Paused: bool
        """
        self.ZoneId = None
        self.Paused = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Paused = params.get("Paused")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneStatusResponse(AbstractModel):
    """ModifyZoneStatus response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NoCache(AbstractModel):
    """No-cache configuration

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable no-cache configuration. Valid values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NormalAction(AbstractModel):
    """Common action of the rule engine

    """

    def __init__(self):
        r"""
        :param Action: Feature name. You can call the [DescribeRulesSetting](https://tcloud4api.woa.com/document/product/1657/79433?!preview&!document=1) API to view the requirements for entering the feature name.
        :type Action: str
        :param Parameters: Parameter
        :type Parameters: list of RuleNormalActionParams
        """
        self.Action = None
        self.Parameters = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        if params.get("Parameters") is not None:
            self.Parameters = []
            for item in params.get("Parameters"):
                obj = RuleNormalActionParams()
                obj._deserialize(item)
                self.Parameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineCache(AbstractModel):
    """Offline cache feature status switch.

    """

    def __init__(self):
        r"""
        :param Switch: Whether offline cache is enabled. Valid values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Origin(AbstractModel):
    """The origin server configuration.

    """

    def __init__(self):
        r"""
        :param Origins: Primary origin server list
Note: This field may return null, indicating that no valid values can be obtained.
        :type Origins: list of str
        :param BackupOrigins: The list of backup origin servers.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupOrigins: list of str
        :param OriginPullProtocol: Origin-pull protocol configuration. Values:
<li>`http`: Force HTTP for origin-pull.</li>
<li>`follow`: Follow protocol.</li>
<li>`https`: Force HTTPS for origin-pull. This only supports port 443 on the origin server.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type OriginPullProtocol: str
        :param CosPrivateAccess: When OriginType is COS, you can specify if access to private buckets is allowed.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CosPrivateAccess: str
        """
        self.Origins = None
        self.BackupOrigins = None
        self.OriginPullProtocol = None
        self.CosPrivateAccess = None


    def _deserialize(self, params):
        self.Origins = params.get("Origins")
        self.BackupOrigins = params.get("BackupOrigins")
        self.OriginPullProtocol = params.get("OriginPullProtocol")
        self.CosPrivateAccess = params.get("CosPrivateAccess")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlanInfo(AbstractModel):
    """EdgeOne plan information

    """

    def __init__(self):
        r"""
        :param Currency: Settlement currency. Values:
<li>`CNY`: Settled by Chinese RMB;</li>
<li>`USD`: Settled by US dollars.</li>
        :type Currency: str
        :param Flux: Traffic quota of the plan. It includes the traffic for security acceleration, content acceleration and smart acceleration. Unit: byte.
        :type Flux: int
        :param Frequency: Settlement cycle. Values:
<li>`y`: Settled by year;</li>
<li>`m`: Settled by month;</li>
<li>`h`: Settled by hour;</li>
<li>`M`: Settled by minute;</li>
<li>`s`: Settled by second.</li>
        :type Frequency: str
        :param PlanType: Plan option. Values:
<li>`sta`: Standard plan that supports content delivery network outside Chinese mainland;</li>
<li>`sta_with_bot`: Standard plan that supports content delivery network outside Chinese mainland and bot management;</li>
<li>`sta_cm`: Standard plan that supports content delivery network inside Chinese mainland;</li>
<li>`sta_cm_with_bot`: Standard plan that supports content delivery network inside Chinese mainland and bot management;</li>
<li>`ent`: Enterprise plan that supports content delivery network outside Chinese mainland;</li>
<li>`ent_with_bot`: Enterprise plan that supports content delivery network outside Chinese mainland and bot management;</li>
<li>`ent_cm`: Enterprise plan that supports content delivery network inside Chinese mainland;</li>
<li>`ent_cm_with_bot`: Enterprise plan that supports content delivery network inside Chinese mainland and bot management.</li>
        :type PlanType: str
        :param Price: Plan price (in CNY fen/US cent). The price unit depends on the settlement currency.
        :type Price: float
        :param Request: Quota on security acceleration requests
        :type Request: int
        :param SiteNumber: Number of sites to be bound to the plan
        :type SiteNumber: int
        :param Area: Acceleration region. Values:
<li>`mainland`: Chinese mainland;</li>
<li>`overseas`: Global (Chinese mainland not included).</li>
        :type Area: str
        """
        self.Currency = None
        self.Flux = None
        self.Frequency = None
        self.PlanType = None
        self.Price = None
        self.Request = None
        self.SiteNumber = None
        self.Area = None


    def _deserialize(self, params):
        self.Currency = params.get("Currency")
        self.Flux = params.get("Flux")
        self.Frequency = params.get("Frequency")
        self.PlanType = params.get("PlanType")
        self.Price = params.get("Price")
        self.Request = params.get("Request")
        self.SiteNumber = params.get("SiteNumber")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PostMaxSize(AbstractModel):
    """Maximum size of the file uploaded for streaming via a POST request

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable POST upload limit (default limit: 32 MB). Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param MaxSize: Maximum size. Value range: 1-500 MB.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxSize: int
        """
        self.Switch = None
        self.MaxSize = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCondition(AbstractModel):
    """The query condition

    """

    def __init__(self):
        r"""
        :param Key: The key of QueryCondition.
        :type Key: str
        :param Operator: The conditional operator. Values:
<li>`equals`: Equal to;</li>
<li>`notEquals`: Not equal to;</li>
<li>`include`: Contain;</li>
<li>`notInclude`: Not contain;</li>
<li>`startWith`: Start with;</li>
<li>`notStartWith`: Not start with;</li>
<li>`endWith`: End with;</li>
<li>`notEndWith`: Not end with.</li>
        :type Operator: str
        :param Value: The value of QueryCondition.
        :type Value: list of str
        """
        self.Key = None
        self.Operator = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Operator = params.get("Operator")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryString(AbstractModel):
    """Request parameter contained in `CacheKey`

    """

    def __init__(self):
        r"""
        :param Switch: Whether to use `QueryString` as part of `CacheKey`. Values:
<li>`on`: Yes</li>
<li>`off`: No</li>
        :type Switch: str
        :param Action: Specifies how to use query strings in the cache key. Values:
<li>`includeCustom`: `Include partial query strings.</li>
<li>`excludeCustom`: Exclude partial query strings.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Action: str
        :param Value: Array of query strings used/excluded
Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: list of str
        """
        self.Switch = None
        self.Action = None
        self.Value = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Action = params.get("Action")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Quic(AbstractModel):
    """QUIC configuration item

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable QUIC. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Quota(AbstractModel):
    """Purging/Pre-warming available usage and quota

    """

    def __init__(self):
        r"""
        :param Batch: 
        :type Batch: int
        :param Daily: Daily submission quota limit.
        :type Daily: int
        :param DailyAvailable: Remaining daily submission quota.
        :type DailyAvailable: int
        :param Type: Quota type. Values:
<li>`purge_prefix`: Purge prefixes;</li>
<li>`purge_url`: Purge URLs;</li>
<li>`purge_host`: Purge hostnames;</li>
<li>`purge_all`: Purge all caches.</li>
        :type Type: str
        """
        self.Batch = None
        self.Daily = None
        self.DailyAvailable = None
        self.Type = None


    def _deserialize(self, params):
        self.Batch = params.get("Batch")
        self.Daily = params.get("Daily")
        self.DailyAvailable = params.get("DailyAvailable")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReclaimZoneRequest(AbstractModel):
    """ReclaimZone request structure.

    """

    def __init__(self):
        r"""
        :param ZoneName: The site name.
        :type ZoneName: str
        """
        self.ZoneName = None


    def _deserialize(self, params):
        self.ZoneName = params.get("ZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReclaimZoneResponse(AbstractModel):
    """ReclaimZone response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Resource(AbstractModel):
    """Billable resource

    """

    def __init__(self):
        r"""
        :param Id: The resource ID.
        :type Id: str
        :param PayMode: Billing mode
`0`: Pay-as-you-go
        :type PayMode: int
        :param CreateTime: The creation time.
        :type CreateTime: str
        :param EnableTime: The effective time.
        :type EnableTime: str
        :param ExpireTime: The expiration time.
        :type ExpireTime: str
        :param Status: The plan status. Values:
<li>`normal`: Normal</li>
<li>`isolated`: Isolated</li>
<li>`destroyed`: Terminated</li>
        :type Status: str
        :param Sv: Pricing query parameter
        :type Sv: list of Sv
        :param AutoRenewFlag: Whether to enable auto-renewal. Values:
<li>`0`: Default status.</li>
<li>`1`: Enable auto-renewal.</li>
<li>`2`: Disable auto-renewal.</li>
        :type AutoRenewFlag: int
        :param PlanId: ID of the resource associated with the plan.
        :type PlanId: str
        :param Area: The region. Values:
<li>`mainland`: Chinese mainland.</li>
<li>`overseas`: Outside the Chinese mainland.</li>
        :type Area: str
        """
        self.Id = None
        self.PayMode = None
        self.CreateTime = None
        self.EnableTime = None
        self.ExpireTime = None
        self.Status = None
        self.Sv = None
        self.AutoRenewFlag = None
        self.PlanId = None
        self.Area = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.PayMode = params.get("PayMode")
        self.CreateTime = params.get("CreateTime")
        self.EnableTime = params.get("EnableTime")
        self.ExpireTime = params.get("ExpireTime")
        self.Status = params.get("Status")
        if params.get("Sv") is not None:
            self.Sv = []
            for item in params.get("Sv"):
                obj = Sv()
                obj._deserialize(item)
                self.Sv.append(obj)
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.PlanId = params.get("PlanId")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RewriteAction(AbstractModel):
    """Rule engine action for the HTTP request/response header

    """

    def __init__(self):
        r"""
        :param Action: Feature name. You can call the [DescribeRulesSetting](https://tcloud4api.woa.com/document/product/1657/79433?!preview&!document=1) API to view the requirements for entering the feature name.
        :type Action: str
        :param Parameters: Parameter
        :type Parameters: list of RuleRewriteActionParams
        """
        self.Action = None
        self.Parameters = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        if params.get("Parameters") is not None:
            self.Parameters = []
            for item in params.get("Parameters"):
                obj = RuleRewriteActionParams()
                obj._deserialize(item)
                self.Parameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Rule(AbstractModel):
    """Rule item of the rule engine. The items in the `Conditions` array are in `OR` relationship, and the items in the inner `Conditions` list are in `AND` relationship.

    """

    def __init__(self):
        r"""
        :param Conditions: Feature execution conditions.
Note: If any condition in the array is met, the feature will run.
        :type Conditions: list of RuleAndConditions
        :param Actions: Feature to be executed.
        :type Actions: list of Action
        """
        self.Conditions = None
        self.Actions = None


    def _deserialize(self, params):
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = RuleAndConditions()
                obj._deserialize(item)
                self.Conditions.append(obj)
        if params.get("Actions") is not None:
            self.Actions = []
            for item in params.get("Actions"):
                obj = Action()
                obj._deserialize(item)
                self.Actions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleAndConditions(AbstractModel):
    """List of rule engine conditions in `AND` relationship

    """

    def __init__(self):
        r"""
        :param Conditions: Rule engine condition. This condition will be considered met if all items in the array are met.
        :type Conditions: list of RuleCondition
        """
        self.Conditions = None


    def _deserialize(self, params):
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = RuleCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleChoicePropertiesItem(AbstractModel):
    """Detailed settings of the rule engine that can be used for request match, which are optional parameter configuration items.

    """

    def __init__(self):
        r"""
        :param Name: The parameter name.
        :type Name: str
        :param Type: The parameter value type.
<li>CHOICE: The parameter value can be selected only from `Values`.</li>
<li>TOGGLE: The parameter value is of switch type and can be selected from `ChoicesValue`.</li>
<li>CUSTOM_NUM: The parameter value is a custom integer.</li>
<li>CUSTOM_STRING: The parameter value is a custom string.</li>
        :type Type: str
        :param ChoicesValue: Valid parameter values.
Note: If `Type` is `CUSTOM_NUM` or `CUSTOM_STRING`, this parameter will be an empty array.
        :type ChoicesValue: list of str
        :param Min: Minimum value. If both `Min` and `Max` are set to `0`, this parameter does not take effect.
        :type Min: int
        :param Max: Maximum value. If both `Min` and `Max` are set to `0`, this parameter does not take effect.
        :type Max: int
        :param IsMultiple: Whether multiple values can be selected or entered.
        :type IsMultiple: bool
        :param IsAllowEmpty: Whether the parameter can be left empty.
        :type IsAllowEmpty: bool
        :param ExtraParameter: Special parameter.
<li>NULL: Select `NormalAction` for `RuleAction`. </li>
<li>If the member parameter `Id` is `Action`, select `RewirteAction` for `RuleAction`.</li>
<li>If the member parameter `Id` is `StatusCode`, select `CodeAction` for `RuleAction`.</li>
        :type ExtraParameter: :class:`tencentcloud.teo.v20220901.models.RuleExtraParameter`
        """
        self.Name = None
        self.Type = None
        self.ChoicesValue = None
        self.Min = None
        self.Max = None
        self.IsMultiple = None
        self.IsAllowEmpty = None
        self.ExtraParameter = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.ChoicesValue = params.get("ChoicesValue")
        self.Min = params.get("Min")
        self.Max = params.get("Max")
        self.IsMultiple = params.get("IsMultiple")
        self.IsAllowEmpty = params.get("IsAllowEmpty")
        if params.get("ExtraParameter") is not None:
            self.ExtraParameter = RuleExtraParameter()
            self.ExtraParameter._deserialize(params.get("ExtraParameter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleCodeActionParams(AbstractModel):
    """Parameters of the action with the `StatusCode` field as the rule engine condition

    """

    def __init__(self):
        r"""
        :param StatusCode: The status code.
        :type StatusCode: int
        :param Name: The parameter name. You can call the [DescribeRulesSetting](https://tcloud4api.woa.com/document/product/1657/79433?!preview&!document=1) API to view the requirements for entering the parameter name.
        :type Name: str
        :param Values: The parameter value.
        :type Values: list of str
        """
        self.StatusCode = None
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.StatusCode = params.get("StatusCode")
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleCondition(AbstractModel):
    """Rule engine condition parameters

    """

    def __init__(self):
        r"""
        :param Operator: Operator. Valid values:
<li>equal: Equal to.</li>
<li>notequal: Not equal to.</li>
        :type Operator: str
        :param Target: Match type. Valid values:
<li>`host`: All</li>
<li>`filename`: File name</li>
<li>`extension`: File extension</li>
<li>`host`: HOST: .</li>
<li>`full_url`: The full URL of the current site. It must contain the HTTP protocol, host, and path.</li>
<li>`url`: The URL path of the current site.</li>
        :type Target: str
        :param Values: Parameter values of the match type. Each match type has the following valid values:
<li>`Target=extension`:  The extension of the file, such as `jpg` and `txt`.</li>
<li>`Target=filename`: The file name without the extension.</li>
<li>`Target=host`: Values can be `all` 
or a host, such as `www.maxx55.com`.</li>
<li>`Target=url`: A URL request path under the current site, such as `/example`.</li>
<li>`Target=full_url`: A complete URL request under the current site. It must contain the protocol, host, and path, such as `https://www.maxx55.cn/example`.</li>
        :type Values: list of str
        """
        self.Operator = None
        self.Target = None
        self.Values = None


    def _deserialize(self, params):
        self.Operator = params.get("Operator")
        self.Target = params.get("Target")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleExtraParameter(AbstractModel):
    """Rule engine parameter details and special parameter types.

    """

    def __init__(self):
        r"""
        :param Id: Parameter name. Valid values:
<li>`Action`: Required parameter for HTTP header modification when `RewirteAction` is selected for `RuleAction`.</li>
<li>`StatusCode`: Required parameter for the status code feature when `CodeAction` is selected for `RuleAction`.</li>
        :type Id: str
        :param Type: Parameter value type.
<li>`CHOICE`: The parameter value can be selected only from `Values`.</li>
<li>`CUSTOM_NUM`: The parameter value is a custom integer.</li>
<li>`CUSTOM_STRING`: The parameter value is a custom string.</li>
        :type Type: str
        :param Choices: Valid values.
Note: If the value of `Id` is `StatusCode`, values in the array are all integer values. When entering a parameter value, enter the integer value of the string.
        :type Choices: list of str
        """
        self.Id = None
        self.Type = None
        self.Choices = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Choices = params.get("Choices")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleItem(AbstractModel):
    """Rule details of the rule engine

    """

    def __init__(self):
        r"""
        :param RuleId: The rule ID.
        :type RuleId: str
        :param RuleName: The rule name. It is a string that can contain 1–255 characters.
        :type RuleName: str
        :param Status: Rule status. Values:
<li>`enable`: Enabled</li>
<li>`disable`: Disabled</li>
        :type Status: str
        :param Rules: The rule content.
        :type Rules: list of Rule
        :param RulePriority: The rule priority. The greater the value, the higher the priority. The minimum value is `1`.
        :type RulePriority: int
        """
        self.RuleId = None
        self.RuleName = None
        self.Status = None
        self.Rules = None
        self.RulePriority = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RuleName = params.get("RuleName")
        self.Status = params.get("Status")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = Rule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RulePriority = params.get("RulePriority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleNormalActionParams(AbstractModel):
    """Common action parameter of a rule engine condition

    """

    def __init__(self):
        r"""
        :param Name: Parameter name. You can call the [DescribeRulesSetting](https://tcloud4api.woa.com/document/product/1657/79433?!preview&!document=1) API to view the requirements for entering the parameter name.
        :type Name: str
        :param Values: The parameter value.
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleRewriteActionParams(AbstractModel):
    """Parameter of the action for the HTTP request/response header of a rule engine condition.

    """

    def __init__(self):
        r"""
        :param Action: Feature parameter name. You can call the [DescribeRulesSetting](https://tcloud4api.woa.com/document/product/1657/79433?!preview&!document=1) API to view the requirements for entering the parameter name, which has three values:
<li>add: Add the HTTP header.</li>
<li>set: Rewrite the HTTP header.</li>
<li>del: Delete the HTTP header.</li>
        :type Action: str
        :param Name: Parameter name
        :type Name: str
        :param Values: Parameter value
        :type Values: list of str
        """
        self.Action = None
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RulesProperties(AbstractModel):
    """Detailed settings of the rule engine that can be used for request match.

    """

    def __init__(self):
        r"""
        :param Name: Parameter name.
        :type Name: str
        :param Min: Minimum value. If both `Min` and `Max` are set to `0`, this parameter does not take effect.
        :type Min: int
        :param ChoicesValue: Valid parameter values.
Note: If `Type` is `CUSTOM_NUM` or `CUSTOM_STRING`, this parameter will be an empty array.
        :type ChoicesValue: list of str
        :param Type: Parameter value type.
<li>`CHOICE`: The parameter value can be selected only from `ChoicesValue`.</li>
<li>`TOGGLE`: The parameter value is of switch type and can be selected from `ChoicesValue`.</li>
<li>`OBJECT`: The parameter value is of object type, and `ChoiceProperties` indicates the attributes associated with the object type.</li>
<li>`CUSTOM_NUM`: Custom integer</li>
<li>`CUSTOM_STRING`: Custom string.</li>Note: If `OBJECT` is selected, refer to [Example 2. Create a rule with parameters of OBJECT type](https://tcloud4api.woa.com/document/product/1657/79382?!preview&!document=1).
        :type Type: str
        :param Max: Maximum value. If both `Min` and `Max` are set to `0`, this parameter does not take effect.
        :type Max: int
        :param IsMultiple: Whether multiple values can be selected or entered.
        :type IsMultiple: bool
        :param IsAllowEmpty: Whether the parameter can be left empty.
        :type IsAllowEmpty: bool
        :param ChoiceProperties: Associated configuration parameters of this parameter, which are required for API call.
Note: This parameter will be an empty array if no special parameters are added as optional parameters.
        :type ChoiceProperties: list of RuleChoicePropertiesItem
        :param ExtraParameter: <li>NULL: No special parameters when `NormalAction` is selected for `RuleAction`.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExtraParameter: :class:`tencentcloud.teo.v20220901.models.RuleExtraParameter`
        """
        self.Name = None
        self.Min = None
        self.ChoicesValue = None
        self.Type = None
        self.Max = None
        self.IsMultiple = None
        self.IsAllowEmpty = None
        self.ChoiceProperties = None
        self.ExtraParameter = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Min = params.get("Min")
        self.ChoicesValue = params.get("ChoicesValue")
        self.Type = params.get("Type")
        self.Max = params.get("Max")
        self.IsMultiple = params.get("IsMultiple")
        self.IsAllowEmpty = params.get("IsAllowEmpty")
        if params.get("ChoiceProperties") is not None:
            self.ChoiceProperties = []
            for item in params.get("ChoiceProperties"):
                obj = RuleChoicePropertiesItem()
                obj._deserialize(item)
                self.ChoiceProperties.append(obj)
        if params.get("ExtraParameter") is not None:
            self.ExtraParameter = RuleExtraParameter()
            self.ExtraParameter._deserialize(params.get("ExtraParameter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RulesSettingAction(AbstractModel):
    """List of the settings of the rule engine that can be used for request match and their detailed information.

    """

    def __init__(self):
        r"""
        :param Action: Feature name. Valid values:
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
        :param Properties: Parameter information
        :type Properties: list of RulesProperties
        """
        self.Action = None
        self.Properties = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        if params.get("Properties") is not None:
            self.Properties = []
            for item in params.get("Properties"):
                obj = RulesProperties()
                obj._deserialize(item)
                self.Properties.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecClientIp(AbstractModel):
    """Client IP information

    """

    def __init__(self):
        r"""
        :param ClientIp: IP of the client.
        :type ClientIp: str
        :param RequestMaxQps: Maximum QPS.
        :type RequestMaxQps: int
        :param RequestNum: Number of requests.
        :type RequestNum: int
        """
        self.ClientIp = None
        self.RequestMaxQps = None
        self.RequestNum = None


    def _deserialize(self, params):
        self.ClientIp = params.get("ClientIp")
        self.RequestMaxQps = params.get("RequestMaxQps")
        self.RequestNum = params.get("RequestNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecEntry(AbstractModel):
    """Returned value of security data entry

    """

    def __init__(self):
        r"""
        :param Key: The query dimension value.
        :type Key: str
        :param Value: The details.
        :type Value: list of SecEntryValue
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        if params.get("Value") is not None:
            self.Value = []
            for item in params.get("Value"):
                obj = SecEntryValue()
                obj._deserialize(item)
                self.Value.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecEntryValue(AbstractModel):
    """The security data queried by metric

    """

    def __init__(self):
        r"""
        :param Metric: The metric name.
        :type Metric: str
        :param Detail: The time-series data details.
        :type Detail: list of TimingDataItem
        :param Max: The maximum value.
        :type Max: int
        :param Avg: The average value.
        :type Avg: float
        :param Sum: Sum
        :type Sum: float
        """
        self.Metric = None
        self.Detail = None
        self.Max = None
        self.Avg = None
        self.Sum = None


    def _deserialize(self, params):
        self.Metric = params.get("Metric")
        if params.get("Detail") is not None:
            self.Detail = []
            for item in params.get("Detail"):
                obj = TimingDataItem()
                obj._deserialize(item)
                self.Detail.append(obj)
        self.Max = params.get("Max")
        self.Avg = params.get("Avg")
        self.Sum = params.get("Sum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecHitRuleInfo(AbstractModel):
    """The hit rule information

    """

    def __init__(self):
        r"""
        :param RuleId: The rule ID.
        :type RuleId: int
        :param RuleTypeName: The rule type.
        :type RuleTypeName: str
        :param Action: Action. Values:
<li>`trans`: Allow;</li>
<li>`alg`: Algorithm challenge;</li>
<li>`drop`: Discard;</li>
<li>`ban`: Block the source IP;</li>
<li>`redirect`: Redirect;</li>
<li>`page`: Return to the specified page;</li>
<li>`monitor`: Observe.</li>
        :type Action: str
        :param HitTime: The hit time recorded in seconds using UNIX timestamp.
        :type HitTime: int
        :param RequestNum: The number of requests.
        :type RequestNum: int
        :param Description: The rule description.
        :type Description: str
        :param Domain: The subdomain name.
        :type Domain: str
        """
        self.RuleId = None
        self.RuleTypeName = None
        self.Action = None
        self.HitTime = None
        self.RequestNum = None
        self.Description = None
        self.Domain = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RuleTypeName = params.get("RuleTypeName")
        self.Action = params.get("Action")
        self.HitTime = params.get("HitTime")
        self.RequestNum = params.get("RequestNum")
        self.Description = params.get("Description")
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecRuleRelatedInfo(AbstractModel):
    """CC/WAF/Bot security rule information

    """

    def __init__(self):
        r"""
        :param RuleId: The rule ID.
        :type RuleId: int
        :param Action: Action. Values:
<li>`trans`: Allow;</li>
<li>`alg`: Algorithm challenge;</li>
<li>`drop`: Discard;</li>
<li>`ban`: Block the source IP;</li>
<li>`redirect`: Redirect;</li>
<li>`page`: Return to the specified page;</li>
<li>`monitor`: Observe.</li>
        :type Action: str
        :param RiskLevel: Risk level (only found in WAF logs). Values:
<li>`high risk`: High risk;</li>
<li>`middle risk`: Middle risk;</li>
<li>`low risk`: Low risk;</li>
<li>`unkonw`: Unknown.</li>
        :type RiskLevel: str
        :param RuleLevel: Rule level. Values:
<li>`normal`: Moderate.</li>
        :type RuleLevel: str
        :param Description: Rule description.
        :type Description: str
        :param RuleTypeName: The rule type.
        :type RuleTypeName: str
        """
        self.RuleId = None
        self.Action = None
        self.RiskLevel = None
        self.RuleLevel = None
        self.Description = None
        self.RuleTypeName = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.Action = params.get("Action")
        self.RiskLevel = params.get("RiskLevel")
        self.RuleLevel = params.get("RuleLevel")
        self.Description = params.get("Description")
        self.RuleTypeName = params.get("RuleTypeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityType(AbstractModel):
    """The security type setting item.

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable the security type setting. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerCertInfo(AbstractModel):
    """HTTPS server certificate configuration

    """

    def __init__(self):
        r"""
        :param CertId: ID of the server certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CertId: str
        :param Alias: Alias of the certificate.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Alias: str
        :param Type: Type of the certificate. Values:
<li>`default`: Default certificate;</lil>
<li>`upload`: Custom certificate;</li>
<li>`managed`: Tencent Cloud-managed certificate.</li>
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param ExpireTime: Time when the certificate expires.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param DeployTime: Time when the certificate is deployed.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DeployTime: str
        :param SignAlgo: Signature algorithm.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SignAlgo: str
        """
        self.CertId = None
        self.Alias = None
        self.Type = None
        self.ExpireTime = None
        self.DeployTime = None
        self.SignAlgo = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.Alias = params.get("Alias")
        self.Type = params.get("Type")
        self.ExpireTime = params.get("ExpireTime")
        self.DeployTime = params.get("DeployTime")
        self.SignAlgo = params.get("SignAlgo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SingleDataRecord(AbstractModel):
    """The dimensional data record

    """

    def __init__(self):
        r"""
        :param TypeKey: The query dimension value.
        :type TypeKey: str
        :param TypeValue: Value of the metric under the query dimension.
        :type TypeValue: list of SingleTypeValue
        """
        self.TypeKey = None
        self.TypeValue = None


    def _deserialize(self, params):
        self.TypeKey = params.get("TypeKey")
        if params.get("TypeValue") is not None:
            self.TypeValue = []
            for item in params.get("TypeValue"):
                obj = SingleTypeValue()
                obj._deserialize(item)
                self.TypeValue.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SingleTypeValue(AbstractModel):
    """The dimensional data

    """

    def __init__(self):
        r"""
        :param MetricName: The metric name.
        :type MetricName: str
        :param DetailData: The metric value.
        :type DetailData: int
        """
        self.MetricName = None
        self.DetailData = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        self.DetailData = params.get("DetailData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartRouting(AbstractModel):
    """Smart acceleration configuration

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable smart acceleration. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Sv(AbstractModel):
    """Pricing query parameter

    """

    def __init__(self):
        r"""
        :param Key: The parameter key.
        :type Key: str
        :param Value: The parameter value.
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
        


class SwitchLogTopicTaskRequest(AbstractModel):
    """SwitchLogTopicTask request structure.

    """

    def __init__(self):
        r"""
        :param TopicId: Topic ID of the shipping task.
        :type TopicId: str
        :param IsOpen: Whether to enable the shipping task. Values:
<li>`true`: Enable the shipping task;</li>
<li>`false`: Disable the shipping task.</li>
        :type IsOpen: bool
        """
        self.TopicId = None
        self.IsOpen = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.IsOpen = params.get("IsOpen")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchLogTopicTaskResponse(AbstractModel):
    """SwitchLogTopicTask response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """Tag configuration

    """

    def __init__(self):
        r"""
        :param TagKey: The tag key.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagKey: str
        :param TagValue: The tag value.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Task(AbstractModel):
    """Content management task result

    """

    def __init__(self):
        r"""
        :param JobId: ID of the task.
        :type JobId: str
        :param Status: Status of the task.
        :type Status: str
        :param Target: Resource.
        :type Target: str
        :param Type: Type of the task.
        :type Type: str
        :param CreateTime: Creation time of the task.
        :type CreateTime: str
        :param UpdateTime: Completion time of the task.
        :type UpdateTime: str
        """
        self.JobId = None
        self.Status = None
        self.Target = None
        self.Type = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.Status = params.get("Status")
        self.Target = params.get("Target")
        self.Type = params.get("Type")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimingDataItem(AbstractModel):
    """Data items of the statistical curve

    """

    def __init__(self):
        r"""
        :param Timestamp: The query time recorded in seconds using UNIX timestamp.
        :type Timestamp: int
        :param Value: The value.
        :type Value: int
        """
        self.Timestamp = None
        self.Value = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimingDataRecord(AbstractModel):
    """The time-series data

    """

    def __init__(self):
        r"""
        :param TypeKey: The query dimension value.
        :type TypeKey: str
        :param TypeValue: Detailed time series data
        :type TypeValue: list of TimingTypeValue
        """
        self.TypeKey = None
        self.TypeValue = None


    def _deserialize(self, params):
        self.TypeKey = params.get("TypeKey")
        if params.get("TypeValue") is not None:
            self.TypeValue = []
            for item in params.get("TypeValue"):
                obj = TimingTypeValue()
                obj._deserialize(item)
                self.TypeValue.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimingTypeValue(AbstractModel):
    """Detailed data of time series type

    """

    def __init__(self):
        r"""
        :param Sum: Sum.
        :type Sum: int
        :param Max: The maximum value.
        :type Max: int
        :param Avg: The average value.
        :type Avg: int
        :param MetricName: Metric name.
        :type MetricName: str
        :param Detail: Details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Detail: list of TimingDataItem
        """
        self.Sum = None
        self.Max = None
        self.Avg = None
        self.MetricName = None
        self.Detail = None


    def _deserialize(self, params):
        self.Sum = params.get("Sum")
        self.Max = params.get("Max")
        self.Avg = params.get("Avg")
        self.MetricName = params.get("MetricName")
        if params.get("Detail") is not None:
            self.Detail = []
            for item in params.get("Detail"):
                obj = TimingDataItem()
                obj._deserialize(item)
                self.Detail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopDataRecord(AbstractModel):
    """The top-ranked data record

    """

    def __init__(self):
        r"""
        :param TypeKey: The query dimension value.
        :type TypeKey: str
        :param DetailData: Top data rankings
        :type DetailData: list of TopDetailData
        """
        self.TypeKey = None
        self.DetailData = None


    def _deserialize(self, params):
        self.TypeKey = params.get("TypeKey")
        if params.get("DetailData") is not None:
            self.DetailData = []
            for item in params.get("DetailData"):
                obj = TopDetailData()
                obj._deserialize(item)
                self.DetailData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopDetailData(AbstractModel):
    """The top-ranked data details

    """

    def __init__(self):
        r"""
        :param Key: The field name.
        :type Key: str
        :param Value: The field value.
        :type Value: int
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
        


class TopEntry(AbstractModel):
    """The Top-ranked data

    """

    def __init__(self):
        r"""
        :param Key: The query dimension value.
        :type Key: str
        :param Value: The details.
        :type Value: list of TopEntryValue
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        if params.get("Value") is not None:
            self.Value = []
            for item in params.get("Value"):
                obj = TopEntryValue()
                obj._deserialize(item)
                self.Value.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopEntryValue(AbstractModel):
    """The top-ranked data

    """

    def __init__(self):
        r"""
        :param Name: The item name.
        :type Name: str
        :param Count: The number of items.
        :type Count: int
        """
        self.Name = None
        self.Count = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpstreamHttp2(AbstractModel):
    """HTTP2 origin-pull configuration

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable HTTP2 origin-pull. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VanityNameServers(AbstractModel):
    """Custom name servers

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable custom name servers. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param Servers: List of custom name servers
        :type Servers: list of str
        """
        self.Switch = None
        self.Servers = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Servers = params.get("Servers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VanityNameServersIps(AbstractModel):
    """IP information of the custom name server

    """

    def __init__(self):
        r"""
        :param Name: Custom name of the name server
        :type Name: str
        :param IPv4: IPv4 address of the custom name server
        :type IPv4: str
        """
        self.Name = None
        self.IPv4 = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.IPv4 = params.get("IPv4")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Waf(AbstractModel):
    """N/A

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable WAF. Values:
<li>`on`: Enable</li>
<li>`off`: Disable</li>
        :type Switch: str
        :param PolicyId: ID of the policy
        :type PolicyId: int
        """
        self.Switch = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebLogs(AbstractModel):
    """Web attack log

    """

    def __init__(self):
        r"""
        :param EventId: The attack event ID.
        :type EventId: str
        :param AttackIp: The attacker IP.
        :type AttackIp: str
        :param Domain: The attacked subdomain name.
        :type Domain: str
        :param HttpLog: The HTTP log content.
        :type HttpLog: str
        :param SipCountryCode: The country code of the attacker IP, which is defined in ISO-3166 alpha-2. For the list of country codes, see [ISO-3166](https://git.woa.com/edgeone/iso-3166/blob/master/all/all.json).
        :type SipCountryCode: str
        :param AttackTime: The attack time recorded in seconds using UNIX timestamp.
        :type AttackTime: int
        :param RequestUri: The request address.
        :type RequestUri: str
        :param AttackContent: The attack content.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AttackContent: str
        :param RuleDetailList: The security rule information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleDetailList: list of SecRuleRelatedInfo
        :param ReqMethod: The request type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReqMethod: str
        """
        self.EventId = None
        self.AttackIp = None
        self.Domain = None
        self.HttpLog = None
        self.SipCountryCode = None
        self.AttackTime = None
        self.RequestUri = None
        self.AttackContent = None
        self.RuleDetailList = None
        self.ReqMethod = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.AttackIp = params.get("AttackIp")
        self.Domain = params.get("Domain")
        self.HttpLog = params.get("HttpLog")
        self.SipCountryCode = params.get("SipCountryCode")
        self.AttackTime = params.get("AttackTime")
        self.RequestUri = params.get("RequestUri")
        self.AttackContent = params.get("AttackContent")
        if params.get("RuleDetailList") is not None:
            self.RuleDetailList = []
            for item in params.get("RuleDetailList"):
                obj = SecRuleRelatedInfo()
                obj._deserialize(item)
                self.RuleDetailList.append(obj)
        self.ReqMethod = params.get("ReqMethod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebSocket(AbstractModel):
    """WebSocket configuration

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable WebSocket connection timeout. Values:
<li>`on`: The field "Timeout" can be configured.</li>
<li>`off`: The field "Timeout" is fixed to 15 seconds.</li>
        :type Switch: str
        :param Timeout: The timeout period in seconds. Maximum value: 120.
        :type Timeout: int
        """
        self.Switch = None
        self.Timeout = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Timeout = params.get("Timeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Zone(AbstractModel):
    """Site information

    """

    def __init__(self):
        r"""
        :param ZoneId: The site ID.
        :type ZoneId: str
        :param ZoneName: The site name.
        :type ZoneName: str
        :param OriginalNameServers: List of name servers used by the site
        :type OriginalNameServers: list of str
        :param NameServers: The list of name servers assigned by Tencent Cloud.
        :type NameServers: list of str
        :param Status: The site status. Values:
<li>`active`: The name server is switched.</li>
<li>`pending`: The name server is not switched.</li>
<li>`moved`: The name server is moved.</li>
<li>`deactivated`: The site is blocked.</li>
        :type Status: str
        :param Type: The site access method. Values:
<li>`full`: Access through a name server.</li>
<li>`partial`: Access through a CNAME record.</li>
        :type Type: str
        :param Paused: Whether the site is disabled.
        :type Paused: bool
        :param CnameSpeedUp: Whether CNAME flattening is enabled. Valid values:
<li>`enabled`: Enabled.</li>
<li>`disabled`: Disabled.</li>
        :type CnameSpeedUp: str
        :param CnameStatus: CNAME record access status. Values:
<li>`finished`: The site is verified.</li>
<li>`pending`: The site is being verified.</li>
        :type CnameStatus: str
        :param Tags: The list of resource tags.
        :type Tags: list of Tag
        :param Resources: The list of billable resources.
        :type Resources: list of Resource
        :param CreatedOn: The creation time of the site.
        :type CreatedOn: str
        :param ModifiedOn: The modification date of the site.
        :type ModifiedOn: str
        :param Area: The site access region. Values:
<li>`global`: Global.</li>
<li>`mainland`: Chinese mainland.</li>
<li>`overseas`: Outside the Chinese mainland.</li>
        :type Area: str
        :param VanityNameServers: The custom name server information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VanityNameServers: :class:`tencentcloud.teo.v20220901.models.VanityNameServers`
        :param VanityNameServersIps: The custom name server IP information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VanityNameServersIps: list of VanityNameServersIps
        """
        self.ZoneId = None
        self.ZoneName = None
        self.OriginalNameServers = None
        self.NameServers = None
        self.Status = None
        self.Type = None
        self.Paused = None
        self.CnameSpeedUp = None
        self.CnameStatus = None
        self.Tags = None
        self.Resources = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.Area = None
        self.VanityNameServers = None
        self.VanityNameServersIps = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.OriginalNameServers = params.get("OriginalNameServers")
        self.NameServers = params.get("NameServers")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.Paused = params.get("Paused")
        self.CnameSpeedUp = params.get("CnameSpeedUp")
        self.CnameStatus = params.get("CnameStatus")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("Resources") is not None:
            self.Resources = []
            for item in params.get("Resources"):
                obj = Resource()
                obj._deserialize(item)
                self.Resources.append(obj)
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        self.Area = params.get("Area")
        if params.get("VanityNameServers") is not None:
            self.VanityNameServers = VanityNameServers()
            self.VanityNameServers._deserialize(params.get("VanityNameServers"))
        if params.get("VanityNameServersIps") is not None:
            self.VanityNameServersIps = []
            for item in params.get("VanityNameServersIps"):
                obj = VanityNameServersIps()
                obj._deserialize(item)
                self.VanityNameServersIps.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneSetting(AbstractModel):
    """The site configuration.

    """

    def __init__(self):
        r"""
        :param ZoneName: Name of the site
        :type ZoneName: str
        :param Area: Site acceleration region. Values:
<li>`mainland`: Acceleration in the Chinese mainland.</li>
<li>`overseas`: Acceleration outside the Chinese mainland.</li>
        :type Area: str
        :param CacheKey: Node cache key configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type CacheKey: :class:`tencentcloud.teo.v20220901.models.CacheKey`
        :param Quic: The QUIC access configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Quic: :class:`tencentcloud.teo.v20220901.models.Quic`
        :param PostMaxSize: The POST transport configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PostMaxSize: :class:`tencentcloud.teo.v20220901.models.PostMaxSize`
        :param Compression: Smart compression configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Compression: :class:`tencentcloud.teo.v20220901.models.Compression`
        :param UpstreamHttp2: HTTP2 origin-pull configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpstreamHttp2: :class:`tencentcloud.teo.v20220901.models.UpstreamHttp2`
        :param ForceRedirect: Force HTTPS redirect configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type ForceRedirect: :class:`tencentcloud.teo.v20220901.models.ForceRedirect`
        :param CacheConfig: Cache expiration time configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type CacheConfig: :class:`tencentcloud.teo.v20220901.models.CacheConfig`
        :param Origin: Origin server configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Origin: :class:`tencentcloud.teo.v20220901.models.Origin`
        :param SmartRouting: Smart acceleration configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type SmartRouting: :class:`tencentcloud.teo.v20220901.models.SmartRouting`
        :param MaxAge: Browser cache configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxAge: :class:`tencentcloud.teo.v20220901.models.MaxAge`
        :param OfflineCache: The offline cache configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OfflineCache: :class:`tencentcloud.teo.v20220901.models.OfflineCache`
        :param WebSocket: WebSocket configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type WebSocket: :class:`tencentcloud.teo.v20220901.models.WebSocket`
        :param ClientIpHeader: Origin-pull client IP header configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClientIpHeader: :class:`tencentcloud.teo.v20220901.models.ClientIpHeader`
        :param CachePrefresh: Cache prefresh configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type CachePrefresh: :class:`tencentcloud.teo.v20220901.models.CachePrefresh`
        :param Ipv6: IPv6 access configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type Ipv6: :class:`tencentcloud.teo.v20220901.models.Ipv6`
        :param Https: HTTPS acceleration configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type Https: :class:`tencentcloud.teo.v20220901.models.Https`
        :param ClientIpCountry: 
        :type ClientIpCountry: :class:`tencentcloud.teo.v20220901.models.ClientIpCountry`
        """
        self.ZoneName = None
        self.Area = None
        self.CacheKey = None
        self.Quic = None
        self.PostMaxSize = None
        self.Compression = None
        self.UpstreamHttp2 = None
        self.ForceRedirect = None
        self.CacheConfig = None
        self.Origin = None
        self.SmartRouting = None
        self.MaxAge = None
        self.OfflineCache = None
        self.WebSocket = None
        self.ClientIpHeader = None
        self.CachePrefresh = None
        self.Ipv6 = None
        self.Https = None
        self.ClientIpCountry = None


    def _deserialize(self, params):
        self.ZoneName = params.get("ZoneName")
        self.Area = params.get("Area")
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Quic") is not None:
            self.Quic = Quic()
            self.Quic._deserialize(params.get("Quic"))
        if params.get("PostMaxSize") is not None:
            self.PostMaxSize = PostMaxSize()
            self.PostMaxSize._deserialize(params.get("PostMaxSize"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("UpstreamHttp2") is not None:
            self.UpstreamHttp2 = UpstreamHttp2()
            self.UpstreamHttp2._deserialize(params.get("UpstreamHttp2"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("CacheConfig") is not None:
            self.CacheConfig = CacheConfig()
            self.CacheConfig._deserialize(params.get("CacheConfig"))
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        if params.get("SmartRouting") is not None:
            self.SmartRouting = SmartRouting()
            self.SmartRouting._deserialize(params.get("SmartRouting"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        if params.get("OfflineCache") is not None:
            self.OfflineCache = OfflineCache()
            self.OfflineCache._deserialize(params.get("OfflineCache"))
        if params.get("WebSocket") is not None:
            self.WebSocket = WebSocket()
            self.WebSocket._deserialize(params.get("WebSocket"))
        if params.get("ClientIpHeader") is not None:
            self.ClientIpHeader = ClientIpHeader()
            self.ClientIpHeader._deserialize(params.get("ClientIpHeader"))
        if params.get("CachePrefresh") is not None:
            self.CachePrefresh = CachePrefresh()
            self.CachePrefresh._deserialize(params.get("CachePrefresh"))
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6()
            self.Ipv6._deserialize(params.get("Ipv6"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("ClientIpCountry") is not None:
            self.ClientIpCountry = ClientIpCountry()
            self.ClientIpCountry._deserialize(params.get("ClientIpCountry"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        