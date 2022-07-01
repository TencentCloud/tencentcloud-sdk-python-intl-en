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


class ApplicationProxy(AbstractModel):
    """Application proxy instance

    """

    def __init__(self):
        r"""
        :param ProxyId: Instance ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ProxyId: str
        :param ProxyName: Instance name
        :type ProxyName: str
        :param PlatType: Scheduling mode:
`ip`: Anycast IP
`domain`: CNAME
        :type PlatType: str
        :param SecurityType: `0`: Disable security protection; `1`: Enable security protection.
        :type SecurityType: int
        :param AccelerateType: `0`: Disable acceleration; `1`: Enable acceleration.
        :type AccelerateType: int
        :param ForwardClientIp: This field is moved to `Rule.ForwardClientIp`.
        :type ForwardClientIp: str
        :param SessionPersist: This field is moved to `Rule.SessionPersist`.
        :type SessionPersist: bool
        :param Rule: Rule list
        :type Rule: list of ApplicationProxyRule
        :param Status: Status:
`online`: Enable
`offline`: Disable
`progress`: Deploying
`stopping`: Disabling
`fail`: Deployment/Disabling failed
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Status: str
        :param ScheduleValue: Scheduling information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ScheduleValue: list of str
        :param UpdateTime: Update time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UpdateTime: str
        :param ZoneId: Site ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ZoneId: str
        :param ZoneName: Site name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ZoneName: str
        :param SessionPersistTime: Session persistence duration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SessionPersistTime: int
        :param ProxyType: Specifies how a layer-4 proxy is created.
`hostname`: Subdomain name
`instance`: Instance
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ProxyType: str
        :param HostId: ID of the layer-7 domain name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type HostId: str
        """
        self.ProxyId = None
        self.ProxyName = None
        self.PlatType = None
        self.SecurityType = None
        self.AccelerateType = None
        self.ForwardClientIp = None
        self.SessionPersist = None
        self.Rule = None
        self.Status = None
        self.ScheduleValue = None
        self.UpdateTime = None
        self.ZoneId = None
        self.ZoneName = None
        self.SessionPersistTime = None
        self.ProxyType = None
        self.HostId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.ProxyName = params.get("ProxyName")
        self.PlatType = params.get("PlatType")
        self.SecurityType = params.get("SecurityType")
        self.AccelerateType = params.get("AccelerateType")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        if params.get("Rule") is not None:
            self.Rule = []
            for item in params.get("Rule"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self.Rule.append(obj)
        self.Status = params.get("Status")
        self.ScheduleValue = params.get("ScheduleValue")
        self.UpdateTime = params.get("UpdateTime")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.SessionPersistTime = params.get("SessionPersistTime")
        self.ProxyType = params.get("ProxyType")
        self.HostId = params.get("HostId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationProxyRule(AbstractModel):
    """Application proxy rule

    """

    def __init__(self):
        r"""
        :param Proto: Protocol. Valid values: `TCP` and `UDP`.
        :type Proto: str
        :param Port: Port. Valid values:
`80`: Port 80
`81-90`: Port range 81-90
        :type Port: list of str
        :param OriginType: Origin server type. Valid values:
`custom`: Specified origins
`origins`: An origin group
`load_balancing`: A load balancer
        :type OriginType: str
        :param OriginValue: Origin server information.
When `OriginType=custom`, this field value indicates multiple origin servers in either of the following formats:
IP:Port
Domain name:Port
When `OriginType=origins`, it indicates the origin group ID.
 
        :type OriginValue: list of str
        :param RuleId: Rule ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuleId: str
        :param Status: Status:
`online`: Enable
`offline`: Disable
`progress`: Deploying
`stopping`: Disabling
`fail`: Deployment/Disabling failed
        :type Status: str
        :param ForwardClientIp: Passes the client IP. When `Proto=TCP`, valid values:
`TOA`: Pass the client IP via TOA
`PPV1`: Pass the client IP via Proxy Protocol V1
`PPV2`: Pass the client IP via Proxy Protocol V2
`OFF`: Do not pass the client IP.
When `Proto=UDP`, valid values:
`PPV2`: Pass the client IP via Proxy Protocol V2
`OFF`: Do not pass the client IP.
        :type ForwardClientIp: str
        :param SessionPersist: Specifies whether to enable session persistence
        :type SessionPersist: bool
        """
        self.Proto = None
        self.Port = None
        self.OriginType = None
        self.OriginValue = None
        self.RuleId = None
        self.Status = None
        self.ForwardClientIp = None
        self.SessionPersist = None


    def _deserialize(self, params):
        self.Proto = params.get("Proto")
        self.Port = params.get("Port")
        self.OriginType = params.get("OriginType")
        self.OriginValue = params.get("OriginValue")
        self.RuleId = params.get("RuleId")
        self.Status = params.get("Status")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfig(AbstractModel):
    """Cache rule configuration

    """

    def __init__(self):
        r"""
        :param Cache: Cache configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cache: :class:`tencentcloud.teo.v20220106.models.CacheConfigCache`
        :param NoCache: No-cache configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type NoCache: :class:`tencentcloud.teo.v20220106.models.CacheConfigNoCache`
        :param FollowOrigin: Follows the origin server configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FollowOrigin: :class:`tencentcloud.teo.v20220106.models.CacheConfigFollowOrigin`
        """
        self.Cache = None
        self.NoCache = None
        self.FollowOrigin = None


    def _deserialize(self, params):
        if params.get("Cache") is not None:
            self.Cache = CacheConfigCache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("NoCache") is not None:
            self.NoCache = CacheConfigNoCache()
            self.NoCache._deserialize(params.get("NoCache"))
        if params.get("FollowOrigin") is not None:
            self.FollowOrigin = CacheConfigFollowOrigin()
            self.FollowOrigin._deserialize(params.get("FollowOrigin"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfigCache(AbstractModel):
    """Cache time settings

    """

    def __init__(self):
        r"""
        :param Switch: Cache configuration switch
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Switch: str
        :param CacheTime: Cache expiration time settings
Unit: second. The maximum value is 365 days.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CacheTime: int
        :param IgnoreCacheControl: Specifies whether to enable force cache
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid value can be obtained.
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
        


class CacheConfigFollowOrigin(AbstractModel):
    """Follows the origin server configuration

    """

    def __init__(self):
        r"""
        :param Switch: Specifies whether to follow the origin server configuration
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid value can be obtained.
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
        


class CacheConfigNoCache(AbstractModel):
    """Do not cache the configuration

    """

    def __init__(self):
        r"""
        :param Switch: Whether to cache the configuration
`on`: Do not cache
`off`: Cache
Note: This field may return `null`, indicating that no valid values can be obtained.
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
        


class CacheKey(AbstractModel):
    """Cache key configuration

    """

    def __init__(self):
        r"""
        :param FullUrlCache: Specifies whether to enable full-path cache
`on`: Enable full-path cache (i.e., disable Ignore Query String)
`off`: Disable full-path cache (i.e., enable Ignore Query String)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FullUrlCache: str
        :param IgnoreCase: Specifies whether the cache key is case sensitive
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IgnoreCase: str
        :param QueryString: Request parameter contained in `CacheKey`
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type QueryString: :class:`tencentcloud.teo.v20220106.models.QueryString`
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
    """

    """

    def __init__(self):
        r"""
        :param Switch: 
        :type Switch: str
        :param Percent: 
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
        


class CertFilter(AbstractModel):
    """Query filter to search for certificates

    """

    def __init__(self):
        r"""
        :param Name: Filters by the field name. Values:
 - `host`: Domain name
 - `certId`: Certificate ID
 - `certAlias`: Certificate alias
 - `certType: default`: Default certificate; `upload`: External certificate; `managed`: Tencent Cloud certificate.
        :type Name: str
        :param Values: Filters by the field value
        :type Values: list of str
        :param Fuzzy: Specifies whether to enable fuzzy query, which only supports the `host` field.
If it is enabled, the length of `Value` must be 1.
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
        


class CertSort(AbstractModel):
    """Sorting conditions for query results.

    """

    def __init__(self):
        r"""
        :param Key: Fields that can be sorted. Values:
`createTime`: Domain name creation time
`certExpireTime`: Certificate expiration time
`certDeployTime`: Certificate deployment time
        :type Key: str
        :param Sequence: Sorting order. Valid values: `asc` and `desc` (default).
        :type Sequence: str
        """
        self.Key = None
        self.Sequence = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Sequence = params.get("Sequence")
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
        :param Certificate: Certificate
        :type Certificate: str
        :param PrivateKey: Private key
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


class ClientIp(AbstractModel):
    """Client IP header

    """

    def __init__(self):
        r"""
        :param Switch: Specifies whether to enable client IP header
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Switch: str
        :param HeaderName: Name of the origin-pull client IP request header
Note: This field may return `null`, indicating that no valid value can be obtained.
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
        


class CnameStatus(AbstractModel):
    """CNAME status

    """

    def __init__(self):
        r"""
        :param Name: Record name
        :type Name: str
        :param Cname: CNAME address
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cname: str
        :param Status: Status
`active`: Activated
`moved`: Not activated
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Status: str
        """
        self.Name = None
        self.Cname = None
        self.Status = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Cname = params.get("Cname")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Compression(AbstractModel):
    """Smart compression

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable Smart compression
`on`: Enable
`off`: Disable
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
        


class CreateApplicationProxyRequest(AbstractModel):
    """CreateApplicationProxy request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ZoneName: Site name
        :type ZoneName: str
        :param ProxyName: Layer-4 proxy name
        :type ProxyName: str
        :param PlatType: Scheduling mode. Values:
`ip`: Anycast IP
`domain`: CNAME
        :type PlatType: str
        :param SecurityType: `0`: Disable security protection; `1`: Enable security protection.
        :type SecurityType: int
        :param AccelerateType: `0`: Disable acceleration; `1`: Enable acceleration.
        :type AccelerateType: int
        :param ForwardClientIp: This field is moved to `Rule.ForwardClientIp`.
        :type ForwardClientIp: str
        :param SessionPersist: This field is moved to `Rule.SessionPersist`.
        :type SessionPersist: bool
        :param Rule: Rule details
        :type Rule: list of ApplicationProxyRule
        :param SessionPersistTime: Session persistence duration. Value range: 30-3600 (in seconds).
        :type SessionPersistTime: int
        :param ProxyType: Specifies how a layer-4 proxy is created.
`hostname`: Subdomain name
`instance`: Instance
        :type ProxyType: str
        """
        self.ZoneId = None
        self.ZoneName = None
        self.ProxyName = None
        self.PlatType = None
        self.SecurityType = None
        self.AccelerateType = None
        self.ForwardClientIp = None
        self.SessionPersist = None
        self.Rule = None
        self.SessionPersistTime = None
        self.ProxyType = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.ProxyName = params.get("ProxyName")
        self.PlatType = params.get("PlatType")
        self.SecurityType = params.get("SecurityType")
        self.AccelerateType = params.get("AccelerateType")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        if params.get("Rule") is not None:
            self.Rule = []
            for item in params.get("Rule"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self.Rule.append(obj)
        self.SessionPersistTime = params.get("SessionPersistTime")
        self.ProxyType = params.get("ProxyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationProxyResponse(AbstractModel):
    """CreateApplicationProxy response structure.

    """

    def __init__(self):
        r"""
        :param ProxyId: Layer-4 application proxy ID
        :type ProxyId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ProxyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.RequestId = params.get("RequestId")


class CreateApplicationProxyRuleRequest(AbstractModel):
    """CreateApplicationProxyRule request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ProxyId: Proxy ID
        :type ProxyId: str
        :param Proto: Protocol. Valid values: `TCP` and `UDP`.
        :type Proto: str
        :param Port: Port. Valid values:
`80`: Port 80
`81-90`: Port range 81-90
        :type Port: list of str
        :param OriginType: Origin server type. Valid values:
`custom`: Specified origins
`origins`: An origin group
`load_balancing`: A load balancer
        :type OriginType: str
        :param OriginValue: Origin server information.
When `OriginType=custom`, this field value indicates multiple origin servers in either of the following formats:
IP:Port
Domain name:Port
When `OriginType=origins`, it indicates the origin group ID.
 
        :type OriginValue: list of str
        :param ForwardClientIp: Passes the client IP. When `Proto=TCP`, valid values:
`TOA`: Pass the client IP via TOA
`PPV1`: Pass the client IP via Proxy Protocol V1
`PPV2`: Pass the client IP via Proxy Protocol V2
`OFF`: Do not pass the client IP.
When `Proto=UDP`, valid values:
`PPV2`: Pass the client IP via Proxy Protocol V2
`OFF`: Do not pass the client IP.
        :type ForwardClientIp: str
        :param SessionPersist: Specifies whether to enable session persistence 
        :type SessionPersist: bool
        """
        self.ZoneId = None
        self.ProxyId = None
        self.Proto = None
        self.Port = None
        self.OriginType = None
        self.OriginValue = None
        self.ForwardClientIp = None
        self.SessionPersist = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.Proto = params.get("Proto")
        self.Port = params.get("Port")
        self.OriginType = params.get("OriginType")
        self.OriginValue = params.get("OriginValue")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationProxyRuleResponse(AbstractModel):
    """CreateApplicationProxyRule response structure.

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


class CreateApplicationProxyRulesRequest(AbstractModel):
    """CreateApplicationProxyRules request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ProxyId: Proxy ID
        :type ProxyId: str
        :param Rule: Rule list
        :type Rule: list of ApplicationProxyRule
        """
        self.ZoneId = None
        self.ProxyId = None
        self.Rule = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        if params.get("Rule") is not None:
            self.Rule = []
            for item in params.get("Rule"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self.Rule.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationProxyRulesResponse(AbstractModel):
    """CreateApplicationProxyRules response structure.

    """

    def __init__(self):
        r"""
        :param RuleId: Array of rule IDs
        :type RuleId: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class CreateDnsRecordRequest(AbstractModel):
    """CreateDnsRecord request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param Type: Record type
        :type Type: str
        :param Name: Record name
        :type Name: str
        :param Content: Record content
        :type Content: str
        :param Mode: Proxy mode. Valid values: `dns_only`, `cdn_only`, and `secure_cdn`.
        :type Mode: str
        :param Ttl: 
        :type Ttl: int
        :param Priority: Priority
        :type Priority: int
        """
        self.ZoneId = None
        self.Type = None
        self.Name = None
        self.Content = None
        self.Mode = None
        self.Ttl = None
        self.Priority = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        self.Mode = params.get("Mode")
        self.Ttl = params.get("Ttl")
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
        :param Id: Record ID
        :type Id: str
        :param Type: Record type
        :type Type: str
        :param Name: Record name
        :type Name: str
        :param Content: Record content
        :type Content: str
        :param Ttl: 
        :type Ttl: int
        :param Priority: Priority
        :type Priority: int
        :param Mode: Proxy mode
        :type Mode: str
        :param Status: Resolution status. Valid values:
`active`: Activated
`pending`: Not activated
        :type Status: str
        :param Locked: Whether the DNS record is locked
        :type Locked: bool
        :param CreatedOn: Creation time
        :type CreatedOn: str
        :param ModifiedOn: Modification time
        :type ModifiedOn: str
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ZoneName: Site name
        :type ZoneName: str
        :param Cname: CNAME address
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cname: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.Type = None
        self.Name = None
        self.Content = None
        self.Ttl = None
        self.Priority = None
        self.Mode = None
        self.Status = None
        self.Locked = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.ZoneId = None
        self.ZoneName = None
        self.Cname = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        self.Ttl = params.get("Ttl")
        self.Priority = params.get("Priority")
        self.Mode = params.get("Mode")
        self.Status = params.get("Status")
        self.Locked = params.get("Locked")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.Cname = params.get("Cname")
        self.RequestId = params.get("RequestId")


class CreateLoadBalancingRequest(AbstractModel):
    """CreateLoadBalancing request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param Host: Subdomain name. You can use @ to represent the root domain.
        :type Host: str
        :param Type: Proxy mode. Valid values:
`dns_only`: Only DNS
`proxied`: Enable proxy
        :type Type: str
        :param OriginId: ID of the origin group used
        :type OriginId: list of str
        :param TTL: Indicates DNS TTL time when `Type=dns_only` 
        :type TTL: int
        """
        self.ZoneId = None
        self.Host = None
        self.Type = None
        self.OriginId = None
        self.TTL = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Host = params.get("Host")
        self.Type = params.get("Type")
        self.OriginId = params.get("OriginId")
        self.TTL = params.get("TTL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoadBalancingResponse(AbstractModel):
    """CreateLoadBalancing response structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LoadBalancingId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.RequestId = params.get("RequestId")


class CreatePrefetchTaskRequest(AbstractModel):
    """CreatePrefetchTask request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param Targets: List of resources to be pre-warmed, for example:
http://www.example.com/example.txt
        :type Targets: list of str
        :param EncodeUrl: Specifies whether to encode the URL
Note that if it’s enabled, the purging is based on the converted URLs.
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
        :param JobId: Task ID
        :type JobId: str
        :param FailedList: List of failed tasks
Note: This field may return `null`, indicating that no valid value can be obtained.
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
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param Type: Type of the purging task. Values:
- `purge_url`: Purge by the URL
- `purge_prefix`: Purge by the prefix
- `purge_host`: Purge by the Hostname
- `purge_all`: Purge all cached contents
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
        :param JobId: Task ID
        :type JobId: str
        :param FailedList: List of failed tasks and reasons
Note: This field may return `null`, indicating that no valid value can be obtained.
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


class CreateZoneRequest(AbstractModel):
    """CreateZone request structure.

    """

    def __init__(self):
        r"""
        :param Name: Site name
        :type Name: str
        :param Type: Access mode. Valid values:
- `full` (default): Access via NS
- `partial`: Access via CNAME
        :type Type: str
        :param JumpStart: Specifies whether to skip resolution record scanning
        :type JumpStart: bool
        """
        self.Name = None
        self.Type = None
        self.JumpStart = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.JumpStart = params.get("JumpStart")
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
        :param Id: Site ID
        :type Id: str
        :param Name: Site name
        :type Name: str
        :param Type: Specifies how the site is connected to EdgeOne.
        :type Type: str
        :param Status: Site status
- `pending`: The name server is not switched.
- `active`: The name server is switched to another assigned.
- `moved`: Move the NS out of Tencent Cloud
        :type Status: str
        :param OriginalNameServers: List of name servers
        :type OriginalNameServers: list of str
        :param NameServers: List of name servers assigned to users
        :type NameServers: list of str
        :param CreatedOn: Site creation date
        :type CreatedOn: str
        :param ModifiedOn: Site update time
        :type ModifiedOn: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.Type = None
        self.Status = None
        self.OriginalNameServers = None
        self.NameServers = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.OriginalNameServers = params.get("OriginalNameServers")
        self.NameServers = params.get("NameServers")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        self.RequestId = params.get("RequestId")


class DataItem(AbstractModel):
    """Data items in a DNS request curve

    """

    def __init__(self):
        r"""
        :param Time: Time
        :type Time: str
        :param Value: Value
Note: This field may return `null`, indicating that no valid value can be obtained.
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
        


class DefaultServerCertInfo(AbstractModel):
    """HTTPS server certificate configuration

    """

    def __init__(self):
        r"""
        :param CertId: Server certificate ID, which is the ID of the default certificate. If you choose to upload an external certificate for SSL certificate management, a certificate ID will be generated.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CertId: str
        :param Alias: Certificate alias
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Alias: str
        :param Type: Certificate type. Valid values:
`default`: Default certificate
`upload`: External certificate
`managed`: Tencent Cloud managed certificate
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Type: str
        :param ExpireTime: Time when the certificate expires
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ExpireTime: str
        :param EffectiveTime: Time when the certificate takes effect
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type EffectiveTime: str
        :param CommonName: Certificate common name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CommonName: str
        :param SubjectAltName: Domain names added to the SAN certificate
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SubjectAltName: list of str
        :param Status: Certificate status. Valid values:
`applying`: Application in progress
`failed`: Application failed
`processing`: Deploying certificate
`deployed`: Certificate deployed
`disabled`: Certificate disabled
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Status: str
        :param Message: Returns a message to display failure causes when `Status=failed`
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Message: str
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationProxyRequest(AbstractModel):
    """DeleteApplicationProxy request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ProxyId: Proxy ID
        :type ProxyId: str
        """
        self.ZoneId = None
        self.ProxyId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationProxyResponse(AbstractModel):
    """DeleteApplicationProxy response structure.

    """

    def __init__(self):
        r"""
        :param ProxyId: Proxy ID
        :type ProxyId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ProxyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.RequestId = params.get("RequestId")


class DeleteApplicationProxyRuleRequest(AbstractModel):
    """DeleteApplicationProxyRule request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ProxyId: Proxy ID
        :type ProxyId: str
        :param RuleId: Rule ID
        :type RuleId: str
        """
        self.ZoneId = None
        self.ProxyId = None
        self.RuleId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationProxyRuleResponse(AbstractModel):
    """DeleteApplicationProxyRule response structure.

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


class DeleteDnsRecordsRequest(AbstractModel):
    """DeleteDnsRecords request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param Ids: Record ID
        :type Ids: list of str
        """
        self.ZoneId = None
        self.Ids = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Ids = params.get("Ids")
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
        :param Ids: Record ID
        :type Ids: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Ids = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        self.RequestId = params.get("RequestId")


class DeleteLoadBalancingRequest(AbstractModel):
    """DeleteLoadBalancing request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        """
        self.ZoneId = None
        self.LoadBalancingId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.LoadBalancingId = params.get("LoadBalancingId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoadBalancingResponse(AbstractModel):
    """DeleteLoadBalancing response structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LoadBalancingId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.RequestId = params.get("RequestId")


class DeleteZoneRequest(AbstractModel):
    """DeleteZone request structure.

    """

    def __init__(self):
        r"""
        :param Id: Site ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
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
        :param Id: Site ID
        :type Id: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class DescribeApplicationProxyDetailRequest(AbstractModel):
    """DescribeApplicationProxyDetail request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ProxyId: Instance ID
        :type ProxyId: str
        """
        self.ZoneId = None
        self.ProxyId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationProxyDetailResponse(AbstractModel):
    """DescribeApplicationProxyDetail response structure.

    """

    def __init__(self):
        r"""
        :param ProxyId: Instance ID
        :type ProxyId: str
        :param ProxyName: Instance name
        :type ProxyName: str
        :param PlatType: Proxy mode. Valid values:
`ip`: Anycast IP
`domain`: CNAME
        :type PlatType: str
        :param SecurityType: `0`: Disable security protection; `1`: Enable security protection.
        :type SecurityType: int
        :param AccelerateType: `0`: Disable acceleration; `1`: Enable acceleration.
        :type AccelerateType: int
        :param ForwardClientIp: This field is moved to `Rule.ForwardClientIp`.
        :type ForwardClientIp: str
        :param SessionPersist: This field is moved to `Rule.SessionPersist`.
        :type SessionPersist: bool
        :param Rule: List of rules
        :type Rule: list of ApplicationProxyRule
        :param Status: Status. Valid values:
`online`: Enable
`offline`: Disable
`progress`: Deploying
        :type Status: str
        :param ScheduleValue: Scheduling information
        :type ScheduleValue: list of str
        :param UpdateTime: Update time
        :type UpdateTime: str
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ZoneName: Site name
        :type ZoneName: str
        :param SessionPersistTime: Session persistence time
        :type SessionPersistTime: int
        :param ProxyType: Specifies how a layer-4 proxy is created.
`hostname`: Subdomain name
`instance`: Instance
        :type ProxyType: str
        :param HostId: ID of the layer-7 domain name
        :type HostId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ProxyId = None
        self.ProxyName = None
        self.PlatType = None
        self.SecurityType = None
        self.AccelerateType = None
        self.ForwardClientIp = None
        self.SessionPersist = None
        self.Rule = None
        self.Status = None
        self.ScheduleValue = None
        self.UpdateTime = None
        self.ZoneId = None
        self.ZoneName = None
        self.SessionPersistTime = None
        self.ProxyType = None
        self.HostId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.ProxyName = params.get("ProxyName")
        self.PlatType = params.get("PlatType")
        self.SecurityType = params.get("SecurityType")
        self.AccelerateType = params.get("AccelerateType")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        if params.get("Rule") is not None:
            self.Rule = []
            for item in params.get("Rule"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self.Rule.append(obj)
        self.Status = params.get("Status")
        self.ScheduleValue = params.get("ScheduleValue")
        self.UpdateTime = params.get("UpdateTime")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.SessionPersistTime = params.get("SessionPersistTime")
        self.ProxyType = params.get("ProxyType")
        self.HostId = params.get("HostId")
        self.RequestId = params.get("RequestId")


class DescribeApplicationProxyRequest(AbstractModel):
    """DescribeApplicationProxy request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param Offset: Pagination parameter
        :type Offset: int
        :param Limit: Pagination parameter
        :type Limit: int
        """
        self.ZoneId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationProxyResponse(AbstractModel):
    """DescribeApplicationProxy response structure.

    """

    def __init__(self):
        r"""
        :param Data: List of data
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Data: list of ApplicationProxy
        :param TotalCount: Total number of records
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param Quota: Indicates the number of instances that can be created by the site when `ZoneId` is specified
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Quota: int
        :param IpCount: 
        :type IpCount: int
        :param DomainCount: 
        :type DomainCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.Quota = None
        self.IpCount = None
        self.DomainCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ApplicationProxy()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.Quota = params.get("Quota")
        self.IpCount = params.get("IpCount")
        self.DomainCount = params.get("DomainCount")
        self.RequestId = params.get("RequestId")


class DescribeCnameStatusRequest(AbstractModel):
    """DescribeCnameStatus request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param Names: List of domain names
        :type Names: list of str
        """
        self.ZoneId = None
        self.Names = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCnameStatusResponse(AbstractModel):
    """DescribeCnameStatus response structure.

    """

    def __init__(self):
        r"""
        :param Status: List of CNAME statuses
        :type Status: list of CnameStatus
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Status") is not None:
            self.Status = []
            for item in params.get("Status"):
                obj = CnameStatus()
                obj._deserialize(item)
                self.Status.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDefaultCertificatesRequest(AbstractModel):
    """DescribeDefaultCertificates request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
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
        


class DescribeDefaultCertificatesResponse(AbstractModel):
    """DescribeDefaultCertificates response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of certificates
        :type TotalCount: int
        :param CertInfo: List of default certificates
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CertInfo: list of DefaultServerCertInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.CertInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("CertInfo") is not None:
            self.CertInfo = []
            for item in params.get("CertInfo"):
                obj = DefaultServerCertInfo()
                obj._deserialize(item)
                self.CertInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDnsDataRequest(AbstractModel):
    """DescribeDnsData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param Filters: Filter parameters
        :type Filters: list of DnsDataFilter
        :param Interval: Time granularity. The default value is `min`. The server can adapt to the time granularity specified.
Valid values:
`min`: 1 minute
`5min`: 5 minutes
`hour`: 1 hour
`day`: 1 day
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
                obj = DnsDataFilter()
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
        :param Data: DNS request data
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Data: list of DataItem
        :param Interval: Interval
Note: This field may return `null`, indicating that no valid value can be obtained.
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
                obj = DataItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Interval = params.get("Interval")
        self.RequestId = params.get("RequestId")


class DescribeDnsRecordsRequest(AbstractModel):
    """DescribeDnsRecords request structure.

    """

    def __init__(self):
        r"""
        :param Filters: Query filter
        :type Filters: list of DnsRecordFilter
        :param Order: Sorts the order
        :type Order: str
        :param Direction: Valid values: `asc`, and `desc`.
        :type Direction: str
        :param Match: Valid values: `all`, and `any`.
        :type Match: str
        :param Limit: Limit on paginated queries. Default value: 100. Maximum value: 1000.
        :type Limit: int
        :param Offset: Offset for paginated queries. Default value: 0
        :type Offset: int
        :param ZoneId: Site ID
        :type ZoneId: str
        """
        self.Filters = None
        self.Order = None
        self.Direction = None
        self.Match = None
        self.Limit = None
        self.Offset = None
        self.ZoneId = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = DnsRecordFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.Direction = params.get("Direction")
        self.Match = params.get("Match")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.ZoneId = params.get("ZoneId")
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
        :param TotalCount: Used for paginated query by total count
        :type TotalCount: int
        :param Records: List of DNS records
        :type Records: list of DnsRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Records = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Records") is not None:
            self.Records = []
            for item in params.get("Records"):
                obj = DnsRecord()
                obj._deserialize(item)
                self.Records.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDnssecRequest(AbstractModel):
    """DescribeDnssec request structure.

    """

    def __init__(self):
        r"""
        :param Id: Site ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
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
        :param Id: Site ID
        :type Id: str
        :param Name: Site name
        :type Name: str
        :param Status: DNSSEC status. Valid values:
- `enabled`: Enabled
- `disabled`: Disabled
        :type Status: str
        :param Dnssec: 
        :type Dnssec: :class:`tencentcloud.teo.v20220106.models.DnssecInfo`
        :param ModifiedOn: Modification time
        :type ModifiedOn: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.Status = None
        self.Dnssec = None
        self.ModifiedOn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        if params.get("Dnssec") is not None:
            self.Dnssec = DnssecInfo()
            self.Dnssec._deserialize(params.get("Dnssec"))
        self.ModifiedOn = params.get("ModifiedOn")
        self.RequestId = params.get("RequestId")


class DescribeHostsCertificateRequest(AbstractModel):
    """DescribeHostsCertificate request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param Offset: Offset for paginated queries. Default value: 0
        :type Offset: int
        :param Limit: Limit on paginated queries. Default value: 100. Maximum value: 1000.
        :type Limit: int
        :param Filters: Query filter
        :type Filters: list of CertFilter
        :param Sort: Sorting order
        :type Sort: :class:`tencentcloud.teo.v20220106.models.CertSort`
        """
        self.ZoneId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.Sort = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = CertFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("Sort") is not None:
            self.Sort = CertSort()
            self.Sort._deserialize(params.get("Sort"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostsCertificateResponse(AbstractModel):
    """DescribeHostsCertificate response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Used for paginated query by total count
        :type TotalCount: int
        :param Hosts: List of certificate configurations for domain names
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Hosts: list of HostCertSetting
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Hosts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Hosts") is not None:
            self.Hosts = []
            for item in params.get("Hosts"):
                obj = HostCertSetting()
                obj._deserialize(item)
                self.Hosts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHostsSettingRequest(AbstractModel):
    """DescribeHostsSetting request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param Offset: Offset for paginated queries. Default value: 0
        :type Offset: int
        :param Limit: Limit on paginated queries. Default value: 100. Maximum value: 1000.
        :type Limit: int
        :param Hosts: Specifies a domain name for the query
        :type Hosts: list of str
        """
        self.ZoneId = None
        self.Offset = None
        self.Limit = None
        self.Hosts = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Hosts = params.get("Hosts")
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
        :param Hosts: List of domain names
        :type Hosts: list of DetailHost
        :param TotalNumber: Number of domain names
        :type TotalNumber: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Hosts = None
        self.TotalNumber = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Hosts") is not None:
            self.Hosts = []
            for item in params.get("Hosts"):
                obj = DetailHost()
                obj._deserialize(item)
                self.Hosts.append(obj)
        self.TotalNumber = params.get("TotalNumber")
        self.RequestId = params.get("RequestId")


class DescribeIdentificationRequest(AbstractModel):
    """DescribeIdentification request structure.

    """

    def __init__(self):
        r"""
        :param Name: Site name
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
        


class DescribeIdentificationResponse(AbstractModel):
    """DescribeIdentification response structure.

    """

    def __init__(self):
        r"""
        :param Name: Site name
        :type Name: str
        :param Status: Verification status. Valid values:
- `pending`: Verifying
- `finished`: The site is verified.
        :type Status: str
        :param Subdomain: 
        :type Subdomain: str
        :param RecordType: Record type
        :type RecordType: str
        :param RecordValue: Record value
        :type RecordValue: str
        :param OriginalNameServers: NS records of the domain name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OriginalNameServers: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Name = None
        self.Status = None
        self.Subdomain = None
        self.RecordType = None
        self.RecordValue = None
        self.OriginalNameServers = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.Subdomain = params.get("Subdomain")
        self.RecordType = params.get("RecordType")
        self.RecordValue = params.get("RecordValue")
        self.OriginalNameServers = params.get("OriginalNameServers")
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancingDetailRequest(AbstractModel):
    """DescribeLoadBalancingDetail request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        """
        self.ZoneId = None
        self.LoadBalancingId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.LoadBalancingId = params.get("LoadBalancingId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancingDetailResponse(AbstractModel):
    """DescribeLoadBalancingDetail response structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        :param ZoneId: Site ID
        :type ZoneId: str
        :param Host: Subdomain name. You can use @ to represent the root domain.
        :type Host: str
        :param Type: Proxy mode. Valid values:
`dns_only`: Only DNS
`proxied`: Enable proxy
        :type Type: str
        :param TTL: Indicates DNS TTL time when `Type=dns_only`
        :type TTL: int
        :param OriginId: ID of the origin group used
        :type OriginId: list of str
        :param Origin: Information of the origin server used
        :type Origin: list of OriginGroup
        :param UpdateTime: Update time
        :type UpdateTime: str
        :param Status: Status of the task
        :type Status: str
        :param Cname: Schedules domain names
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cname: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LoadBalancingId = None
        self.ZoneId = None
        self.Host = None
        self.Type = None
        self.TTL = None
        self.OriginId = None
        self.Origin = None
        self.UpdateTime = None
        self.Status = None
        self.Cname = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.ZoneId = params.get("ZoneId")
        self.Host = params.get("Host")
        self.Type = params.get("Type")
        self.TTL = params.get("TTL")
        self.OriginId = params.get("OriginId")
        if params.get("Origin") is not None:
            self.Origin = []
            for item in params.get("Origin"):
                obj = OriginGroup()
                obj._deserialize(item)
                self.Origin.append(obj)
        self.UpdateTime = params.get("UpdateTime")
        self.Status = params.get("Status")
        self.Cname = params.get("Cname")
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancingRequest(AbstractModel):
    """DescribeLoadBalancing request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param Offset: Pagination parameter
        :type Offset: int
        :param Limit: Pagination parameter
        :type Limit: int
        :param Host: Ignore query string parameter
        :type Host: str
        :param Fuzzy: Specifies whether the `Host` parameter supports fuzzy match
        :type Fuzzy: bool
        """
        self.ZoneId = None
        self.Offset = None
        self.Limit = None
        self.Host = None
        self.Fuzzy = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Host = params.get("Host")
        self.Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancingResponse(AbstractModel):
    """DescribeLoadBalancing response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of records
        :type TotalCount: int
        :param Data: CLB information
        :type Data: list of LoadBalancing
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
                obj = LoadBalancing()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePrefetchTasksRequest(AbstractModel):
    """DescribePrefetchTasks request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Task ID
        :type JobId: str
        :param StartTime: Start time of the query
        :type StartTime: str
        :param EndTime: End time of the query
        :type EndTime: str
        :param Offset: Offset of the query
        :type Offset: int
        :param Limit: Maximum number of results returned
        :type Limit: int
        :param Statuses: Statuses of tasks to be queried. Values:
`processing`, `success`, `failed`, `timeout` and `invalid`
        :type Statuses: list of str
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param Domains: List of domain names queried
        :type Domains: list of str
        :param Target: Resources queried
        :type Target: str
        """
        self.JobId = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.Statuses = None
        self.ZoneId = None
        self.Domains = None
        self.Target = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Statuses = params.get("Statuses")
        self.ZoneId = params.get("ZoneId")
        self.Domains = params.get("Domains")
        self.Target = params.get("Target")
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
        :param TotalCount: Total entries that match the specified query condition
        :type TotalCount: int
        :param Tasks: List of tasks returned
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
        :param JobId: Task ID
        :type JobId: str
        :param Type: Type of the purging task
        :type Type: str
        :param StartTime: Start time of the query
        :type StartTime: str
        :param EndTime: End time of the query
        :type EndTime: str
        :param Offset: Offset of the query
        :type Offset: int
        :param Limit: Maximum number of results returned
        :type Limit: int
        :param Statuses: Statuses of tasks to be queried. Values:
`processing`, `success`, `failed`, `timeout` and `invalid`
        :type Statuses: list of str
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param Domains: List of domain names queried
        :type Domains: list of str
        :param Target: Queries content
        :type Target: str
        """
        self.JobId = None
        self.Type = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.Statuses = None
        self.ZoneId = None
        self.Domains = None
        self.Target = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.Type = params.get("Type")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Statuses = params.get("Statuses")
        self.ZoneId = params.get("ZoneId")
        self.Domains = params.get("Domains")
        self.Target = params.get("Target")
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
        :param TotalCount: Total entries that match the specified query condition
        :type TotalCount: int
        :param Tasks: List of tasks returned
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


class DescribeZoneDetailsRequest(AbstractModel):
    """DescribeZoneDetails request structure.

    """

    def __init__(self):
        r"""
        :param Id: Site ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneDetailsResponse(AbstractModel):
    """DescribeZoneDetails response structure.

    """

    def __init__(self):
        r"""
        :param Id: Site ID
        :type Id: str
        :param Name: Site name
        :type Name: str
        :param OriginalNameServers: List of name servers used
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OriginalNameServers: list of str
        :param NameServers: List of name servers assigned to users by Tencent Cloud
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type NameServers: list of str
        :param Status: Site status
- `active`: The name server is switched.
- `pending`: The name server is not switched.
- `moved`: The name server is moved.
- `deactivated`: The name server is blocked.
        :type Status: str
        :param Type: Specifies how the site is connected to EdgeOne.
- `full`: The site is connected via name server.
- `partial`: The site is connected via CNAME.
        :type Type: str
        :param Paused: Indicates whether the site is disabled
        :type Paused: bool
        :param CreatedOn: Site creation date
        :type CreatedOn: str
        :param ModifiedOn: Site modification date
        :type ModifiedOn: str
        :param VanityNameServers: User-defined name server information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type VanityNameServers: :class:`tencentcloud.teo.v20220106.models.VanityNameServers`
        :param VanityNameServersIps: User-defined name server IP information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type VanityNameServersIps: list of VanityNameServersIps
        :param CnameSpeedUp: Specifies whether to enable CNAME acceleration
- `enabled`: Enable
- `disabled`: Disable
        :type CnameSpeedUp: str
        :param CnameStatus: Ownership verification status of the site when it accesses via CNAME.
- `finished`: The site is verified.
- `pending`: The site is waiting for verification.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CnameStatus: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.OriginalNameServers = None
        self.NameServers = None
        self.Status = None
        self.Type = None
        self.Paused = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.VanityNameServers = None
        self.VanityNameServersIps = None
        self.CnameSpeedUp = None
        self.CnameStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.OriginalNameServers = params.get("OriginalNameServers")
        self.NameServers = params.get("NameServers")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.Paused = params.get("Paused")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        if params.get("VanityNameServers") is not None:
            self.VanityNameServers = VanityNameServers()
            self.VanityNameServers._deserialize(params.get("VanityNameServers"))
        if params.get("VanityNameServersIps") is not None:
            self.VanityNameServersIps = []
            for item in params.get("VanityNameServersIps"):
                obj = VanityNameServersIps()
                obj._deserialize(item)
                self.VanityNameServersIps.append(obj)
        self.CnameSpeedUp = params.get("CnameSpeedUp")
        self.CnameStatus = params.get("CnameStatus")
        self.RequestId = params.get("RequestId")


class DescribeZoneSettingRequest(AbstractModel):
    """DescribeZoneSetting request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
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
        :param Cache: Cache expiration time configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cache: :class:`tencentcloud.teo.v20220106.models.CacheConfig`
        :param CacheKey: Node cache key configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CacheKey: :class:`tencentcloud.teo.v20220106.models.CacheKey`
        :param MaxAge: Browser cache configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type MaxAge: :class:`tencentcloud.teo.v20220106.models.MaxAge`
        :param OfflineCache: Offline cache
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OfflineCache: :class:`tencentcloud.teo.v20220106.models.OfflineCache`
        :param Quic: QUIC access
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Quic: :class:`tencentcloud.teo.v20220106.models.Quic`
        :param PostMaxSize: POST transport configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PostMaxSize: :class:`tencentcloud.teo.v20220106.models.PostMaxSize`
        :param Compression: Smart compression configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Compression: :class:`tencentcloud.teo.v20220106.models.Compression`
        :param UpstreamHttp2: HTTP2 origin-pull configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UpstreamHttp2: :class:`tencentcloud.teo.v20220106.models.UpstreamHttp2`
        :param ForceRedirect: Force HTTPS redirect configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ForceRedirect: :class:`tencentcloud.teo.v20220106.models.ForceRedirect`
        :param Https: HTTPS acceleration configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Https: :class:`tencentcloud.teo.v20220106.models.Https`
        :param Origin: Origin server configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Origin: :class:`tencentcloud.teo.v20220106.models.Origin`
        :param SmartRouting: Dynamic acceleration configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SmartRouting: :class:`tencentcloud.teo.v20220106.models.SmartRouting`
        :param ZoneId: Site ID
        :type ZoneId: str
        :param Zone: Domain name of the site
        :type Zone: str
        :param WebSocket: WebSocket configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type WebSocket: :class:`tencentcloud.teo.v20220106.models.WebSocket`
        :param ClientIpHeader: Origin-pull client IP header configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ClientIpHeader: :class:`tencentcloud.teo.v20220106.models.ClientIp`
        :param CachePrefresh: 
        :type CachePrefresh: :class:`tencentcloud.teo.v20220106.models.CachePrefresh`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Cache = None
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
        self.ZoneId = None
        self.Zone = None
        self.WebSocket = None
        self.ClientIpHeader = None
        self.CachePrefresh = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Cache") is not None:
            self.Cache = CacheConfig()
            self.Cache._deserialize(params.get("Cache"))
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
        self.ZoneId = params.get("ZoneId")
        self.Zone = params.get("Zone")
        if params.get("WebSocket") is not None:
            self.WebSocket = WebSocket()
            self.WebSocket._deserialize(params.get("WebSocket"))
        if params.get("ClientIpHeader") is not None:
            self.ClientIpHeader = ClientIp()
            self.ClientIpHeader._deserialize(params.get("ClientIpHeader"))
        if params.get("CachePrefresh") is not None:
            self.CachePrefresh = CachePrefresh()
            self.CachePrefresh._deserialize(params.get("CachePrefresh"))
        self.RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Pagination parameter, which specifies the offset.
        :type Offset: int
        :param Limit: Pagination parameter, which specifies the number of sites returned in each page.
        :type Limit: int
        :param Filters: Query condition filter, which supports complex type.
        :type Filters: list of ZoneFilter
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
                obj = ZoneFilter()
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
        :param TotalCount: Number of sites that match the specified conditions
        :type TotalCount: int
        :param Zones: Details of sites
Note: This field may return `null`, indicating that no valid value can be obtained.
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
        :param AppId: Tencent Cloud account ID
        :type AppId: int
        :param ZoneId: Site ID
        :type ZoneId: str
        :param Status: Acceleration service status
`process`: Deploying
`online`: Enabled
`offline`: Disabled
        :type Status: str
        :param Host: Domain name
        :type Host: str
        """
        self.AppId = None
        self.ZoneId = None
        self.Status = None
        self.Host = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.ZoneId = params.get("ZoneId")
        self.Status = params.get("Status")
        self.Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DnsDataFilter(AbstractModel):
    """Ignore query string parameters for DNS data

    """

    def __init__(self):
        r"""
        :param Name: Parameter name. Valid values:
`zone`: Site name
`host`: Domain name
`type`: DNS resolution type
`code`: DNS response code
`area`: Region of the resolution server
        :type Name: str
        :param Value: Parameter value
When `Name=area`, valid values:
`Asia`
`Europe`
`Africa`
`Oceania`
`Americas`

When `Name=code`, valid values:
`NoError`: Successful response.
`NXDomain`: Non-existent domain in the request. It is only valid when the response is from the authoritative name server.
`NotImp`: Request type not supported.
`Refused`: The name server refuses to perform the requested operation for policy reasons.
        :type Value: str
        :param Values: Parameter value
When `Name=area`, valid values:
`Asia`
`Europe`
`Africa`
`Oceania`
`Americas`

When `Name=code`, valid values:
`NoError`: Successful response.
`NXDomain`: Non-existent domain in the request. It is only valid when the response is from the authoritative name server.
`NotImp`: Request type not supported.
`Refused`: The name server refuses to perform the requested operation for policy reasons.
        :type Values: list of str
        """
        self.Name = None
        self.Value = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        self.Values = params.get("Values")
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
        :param Id: Record ID
        :type Id: str
        :param Type: Record type
        :type Type: str
        :param Name: Host record
        :type Name: str
        :param Content: Record value
        :type Content: str
        :param Mode: Proxy mode
        :type Mode: str
        :param Ttl: TTL value
        :type Ttl: int
        :param Priority: Priority
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Priority: int
        :param CreatedOn: Creation time
        :type CreatedOn: str
        :param ModifiedOn: Modification time
        :type ModifiedOn: str
        :param Locked: Domain name lock
        :type Locked: bool
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ZoneName: Site name
        :type ZoneName: str
        :param Status: Resolution status
`active`: Activated
`pending`: Not activated
        :type Status: str
        :param Cname: CNAME address
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cname: str
        :param DomainStatus: Specifies whether to enable load balancing, layer-4 proxy, or security protection for the domain name.
- `lb`: Load balancing.
- `security`: Security protection.
- `l4`: Layer-4 proxy.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DomainStatus: list of str
        """
        self.Id = None
        self.Type = None
        self.Name = None
        self.Content = None
        self.Mode = None
        self.Ttl = None
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
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        self.Mode = params.get("Mode")
        self.Ttl = params.get("Ttl")
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
        


class DnsRecordFilter(AbstractModel):
    """Query filter to search for DNS records

    """

    def __init__(self):
        r"""
        :param Name: Filters by the field name. Vaules:
- `name`: Site name.
- `status`: Site status.
        :type Name: str
        :param Values: Filters by the field value
        :type Values: list of str
        :param Fuzzy: Specifies whether to enable fuzzy query. It’s only available when the filter name is `name`. If it’s enabled, the length of `Values` must be 1.
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
        


class DownloadL7LogsRequest(AbstractModel):
    """DownloadL7Logs request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time. It must conform to the RFC3339 standard.
        :type StartTime: str
        :param EndTime: End time. It must conform to the RFC3339 standard.
        :type EndTime: str
        :param PageSize: Number of entries per page
        :type PageSize: int
        :param PageNo: Current page
        :type PageNo: int
        :param Zones: List of sites
        :type Zones: list of str
        :param Domains: List of domain names
        :type Domains: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.PageSize = None
        self.PageNo = None
        self.Zones = None
        self.Domains = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.Zones = params.get("Zones")
        self.Domains = params.get("Domains")
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
        :param Data: Layer-7 offline log data
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Data: list of L7OfflineLog
        :param PageSize: Page size
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PageSize: int
        :param PageNo: Page number
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PageNo: int
        :param Pages: Total number of pages
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Pages: int
        :param TotalSize: Total number of entries
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TotalSize: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.PageSize = None
        self.PageNo = None
        self.Pages = None
        self.TotalSize = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = L7OfflineLog()
                obj._deserialize(item)
                self.Data.append(obj)
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.Pages = params.get("Pages")
        self.TotalSize = params.get("TotalSize")
        self.RequestId = params.get("RequestId")


class FailReason(AbstractModel):
    """Failure reason

    """

    def __init__(self):
        r"""
        :param Reason: Failure reason
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
        


class ForceRedirect(AbstractModel):
    """Force HTTPS redirect configuration

    """

    def __init__(self):
        r"""
        :param Switch: Force redirect configuration switch
`on`: Enable
`off`: Disable
        :type Switch: str
        :param RedirectStatusCode: Redirection status code
301
302
Note: This field may return `null`, indicating that no valid value can be obtained.
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
        


class HostCertSetting(AbstractModel):
    """Certificate configurations for domain names

    """

    def __init__(self):
        r"""
        :param Host: Domain name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Host: str
        :param CertInfo: Server certificate configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CertInfo: list of ServerCertInfo
        """
        self.Host = None
        self.CertInfo = None


    def _deserialize(self, params):
        self.Host = params.get("Host")
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
        


class Hsts(AbstractModel):
    """HSTS configuration

    """

    def __init__(self):
        r"""
        :param Switch: Specifies whether to enable. Valid values: `on` and `off`.
        :type Switch: str
        :param MaxAge: `MaxAge` value.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type MaxAge: int
        :param IncludeSubDomains: Specifies whether to include subdomain names. Valid values: `on` and `off`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IncludeSubDomains: str
        :param Preload: Specifies whether to preload. Valid values: `on` and `off`.
Note: This field may return `null`, indicating that no valid value can be obtained.
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
        :param Http2: HTTP2 configuration switch
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Http2: str
        :param OcspStapling: OCSP configuration switch
`on`: Enable
`off`: Disable
It is disabled by default.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OcspStapling: str
        :param TlsVersion: TLS version settings. Valid values: `TLSv1`, `TLSV1.1`, `TLSV1.2`, and `TLSv1.3`. Only consecutive versions can be enabled at the same time.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TlsVersion: list of str
        :param Hsts: HSTS Configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Hsts: :class:`tencentcloud.teo.v20220106.models.Hsts`
        """
        self.Http2 = None
        self.OcspStapling = None
        self.TlsVersion = None
        self.Hsts = None


    def _deserialize(self, params):
        self.Http2 = params.get("Http2")
        self.OcspStapling = params.get("OcspStapling")
        self.TlsVersion = params.get("TlsVersion")
        if params.get("Hsts") is not None:
            self.Hsts = Hsts()
            self.Hsts._deserialize(params.get("Hsts"))
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
        :param Name: Site name
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
        


class IdentifyZoneResponse(AbstractModel):
    """IdentifyZone response structure.

    """

    def __init__(self):
        r"""
        :param Name: Site name
        :type Name: str
        :param Subdomain: 
        :type Subdomain: str
        :param RecordType: Record type
        :type RecordType: str
        :param RecordValue: Record value
        :type RecordValue: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Name = None
        self.Subdomain = None
        self.RecordType = None
        self.RecordValue = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Subdomain = params.get("Subdomain")
        self.RecordType = params.get("RecordType")
        self.RecordValue = params.get("RecordValue")
        self.RequestId = params.get("RequestId")


class ImportDnsRecordsRequest(AbstractModel):
    """ImportDnsRecords request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param File: File content
        :type File: str
        """
        self.ZoneId = None
        self.File = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.File = params.get("File")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportDnsRecordsResponse(AbstractModel):
    """ImportDnsRecords response structure.

    """

    def __init__(self):
        r"""
        :param Ids: Record ID
        :type Ids: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Ids = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        self.RequestId = params.get("RequestId")


class L7OfflineLog(AbstractModel):
    """Layer-7 offline log details

    """

    def __init__(self):
        r"""
        :param LogTime: Start time of the log packaging
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type LogTime: int
        :param Domain: Site name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Domain: str
        :param Size: Log size, in bytes
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Size: int
        :param Url: Download address
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Url: str
        :param LogPacketName: Log package name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type LogPacketName: str
        """
        self.LogTime = None
        self.Domain = None
        self.Size = None
        self.Url = None
        self.LogPacketName = None


    def _deserialize(self, params):
        self.LogTime = params.get("LogTime")
        self.Domain = params.get("Domain")
        self.Size = params.get("Size")
        self.Url = params.get("Url")
        self.LogPacketName = params.get("LogPacketName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancing(AbstractModel):
    """CLB information

    """

    def __init__(self):
        r"""
        :param LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        :param ZoneId: Site ID
        :type ZoneId: str
        :param Host: Subdomain name. You can use @ to represent the root domain.
        :type Host: str
        :param Type: Proxy mode. Valid values:
`dns_only`: Only DNS
`proxied`: Enable proxy
        :type Type: str
        :param TTL: Indicates DNS TTL time when `Type=dns_only`
        :type TTL: int
        :param OriginId: ID of the origin group used
        :type OriginId: list of str
        :param Origin: Information of the origin server used
        :type Origin: list of OriginGroup
        :param UpdateTime: Update time
        :type UpdateTime: str
        :param Status: Status
        :type Status: str
        :param Cname: Schedules domain names
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cname: str
        """
        self.LoadBalancingId = None
        self.ZoneId = None
        self.Host = None
        self.Type = None
        self.TTL = None
        self.OriginId = None
        self.Origin = None
        self.UpdateTime = None
        self.Status = None
        self.Cname = None


    def _deserialize(self, params):
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.ZoneId = params.get("ZoneId")
        self.Host = params.get("Host")
        self.Type = params.get("Type")
        self.TTL = params.get("TTL")
        self.OriginId = params.get("OriginId")
        if params.get("Origin") is not None:
            self.Origin = []
            for item in params.get("Origin"):
                obj = OriginGroup()
                obj._deserialize(item)
                self.Origin.append(obj)
        self.UpdateTime = params.get("UpdateTime")
        self.Status = params.get("Status")
        self.Cname = params.get("Cname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaxAge(AbstractModel):
    """Browser cache rule configuration.

    """

    def __init__(self):
        r"""
        :param MaxAgeTime: Specifies the max age of the cache (in seconds). The maximum value is 365 days.
Note: the value `0` means not to cache.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type MaxAgeTime: int
        :param FollowOrigin: Specifies whether to follow the max cache age of the origin server. Valid values: `on` and `off`. If it's on, `MaxAgeTime` is ignored.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FollowOrigin: str
        """
        self.MaxAgeTime = None
        self.FollowOrigin = None


    def _deserialize(self, params):
        self.MaxAgeTime = params.get("MaxAgeTime")
        self.FollowOrigin = params.get("FollowOrigin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyRequest(AbstractModel):
    """ModifyApplicationProxy request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ProxyId: Layer-4 proxy ID
        :type ProxyId: str
        :param ProxyName: Layer-4 proxy name
        :type ProxyName: str
        :param ForwardClientIp: This parameter is disused.
        :type ForwardClientIp: str
        :param SessionPersist: This parameter is disused.
        :type SessionPersist: bool
        :param SessionPersistTime: Session persistence time. Value range: 30-3600 (in seconds).
        :type SessionPersistTime: int
        :param ProxyType: Specifies how a layer-4 proxy is created.
`hostname`: Subdomain name
`instance`: Instance
        :type ProxyType: str
        """
        self.ZoneId = None
        self.ProxyId = None
        self.ProxyName = None
        self.ForwardClientIp = None
        self.SessionPersist = None
        self.SessionPersistTime = None
        self.ProxyType = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.ProxyName = params.get("ProxyName")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        self.SessionPersistTime = params.get("SessionPersistTime")
        self.ProxyType = params.get("ProxyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyResponse(AbstractModel):
    """ModifyApplicationProxy response structure.

    """

    def __init__(self):
        r"""
        :param ProxyId: Layer-4 proxy ID
        :type ProxyId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ProxyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.RequestId = params.get("RequestId")


class ModifyApplicationProxyRuleRequest(AbstractModel):
    """ModifyApplicationProxyRule request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ProxyId: Proxy ID
        :type ProxyId: str
        :param RuleId: Rule ID
        :type RuleId: str
        :param Proto: Protocol. Valid values: `TCP` and `UDP`.
        :type Proto: str
        :param Port: Port. Valid values:
`80`: Port 80
`81-90`: Port range 81-90
        :type Port: list of str
        :param OriginType: Origin server type. Valid values:
`custom`: Specified origins
`origins`: An origin group
`load_balancing`: A load balancer
        :type OriginType: str
        :param OriginValue: Origin server information.
When `OriginType=custom`, this field value indicates multiple origin servers in either of the following formats:
IP:Port
Domain name: Port
When `OriginType=origins`, it indicates the origin group ID.
 
        :type OriginValue: list of str
        :param ForwardClientIp: Passes the client IP. When `Proto=TCP`, valid values:
`TOA`: Pass the client IP via TOA.
`PPV1`: Pass the client IP via Proxy Protocol V1.
`PPV2`: Pass the client IP via Proxy Protocol V2.
`OFF`: Do not pass the client IP.
When `Proto=UDP`, valid values:
`PPV2`: Pass the client IP via Proxy Protocol V2.
`OFF`: Do not pass the client IP.
        :type ForwardClientIp: str
        :param SessionPersist: Specifies whether to enable session persistence
        :type SessionPersist: bool
        """
        self.ZoneId = None
        self.ProxyId = None
        self.RuleId = None
        self.Proto = None
        self.Port = None
        self.OriginType = None
        self.OriginValue = None
        self.ForwardClientIp = None
        self.SessionPersist = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.RuleId = params.get("RuleId")
        self.Proto = params.get("Proto")
        self.Port = params.get("Port")
        self.OriginType = params.get("OriginType")
        self.OriginValue = params.get("OriginValue")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyRuleResponse(AbstractModel):
    """ModifyApplicationProxyRule response structure.

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


class ModifyApplicationProxyRuleStatusRequest(AbstractModel):
    """ModifyApplicationProxyRuleStatus request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ProxyId: Layer-4 proxy ID
        :type ProxyId: str
        :param RuleId: Rule ID
        :type RuleId: str
        :param Status: Status
`offline`: Disabled
`online`: Enabled
        :type Status: str
        """
        self.ZoneId = None
        self.ProxyId = None
        self.RuleId = None
        self.Status = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.RuleId = params.get("RuleId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyRuleStatusResponse(AbstractModel):
    """ModifyApplicationProxyRuleStatus response structure.

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


class ModifyApplicationProxyStatusRequest(AbstractModel):
    """ModifyApplicationProxyStatus request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ProxyId: Layer-4 proxy ID
        :type ProxyId: str
        :param Status: Status
`offline`: Disabled
`online`: Enabled
        :type Status: str
        """
        self.ZoneId = None
        self.ProxyId = None
        self.Status = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyStatusResponse(AbstractModel):
    """ModifyApplicationProxyStatus response structure.

    """

    def __init__(self):
        r"""
        :param ProxyId: Layer-4 proxy ID
        :type ProxyId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ProxyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.RequestId = params.get("RequestId")


class ModifyDefaultCertificateRequest(AbstractModel):
    """ModifyDefaultCertificate request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param CertId: Certificate ID
        :type CertId: str
        :param Status: Certificate status
`deployed`: The certificate is deployed.
`disabled`: The certificate is disabled.
If the deployment fails, you can pass in `Status = deployed` again.
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
        :param Id: Record ID
        :type Id: str
        :param ZoneId: Site ID
        :type ZoneId: str
        :param Type: Record type
        :type Type: str
        :param Name: Record name
        :type Name: str
        :param Content: Record content
        :type Content: str
        :param Ttl: 
        :type Ttl: int
        :param Priority: Priority
        :type Priority: int
        :param Mode: Proxy mode
        :type Mode: str
        """
        self.Id = None
        self.ZoneId = None
        self.Type = None
        self.Name = None
        self.Content = None
        self.Ttl = None
        self.Priority = None
        self.Mode = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.ZoneId = params.get("ZoneId")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        self.Ttl = params.get("Ttl")
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
        :param Id: Record ID
        :type Id: str
        :param Type: Record type
        :type Type: str
        :param Name: Record name
        :type Name: str
        :param Content: Record content
        :type Content: str
        :param Ttl: 
        :type Ttl: int
        :param Priority: Priority
        :type Priority: int
        :param Mode: Proxy mode
        :type Mode: str
        :param Status: Resolution status
        :type Status: str
        :param Cname: CNAME address
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cname: str
        :param Locked: Whether the DNS record is locked
        :type Locked: bool
        :param CreatedOn: Creation time
        :type CreatedOn: str
        :param ModifiedOn: Modification time
        :type ModifiedOn: str
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ZoneName: Site name
        :type ZoneName: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.Type = None
        self.Name = None
        self.Content = None
        self.Ttl = None
        self.Priority = None
        self.Mode = None
        self.Status = None
        self.Cname = None
        self.Locked = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.ZoneId = None
        self.ZoneName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        self.Ttl = params.get("Ttl")
        self.Priority = params.get("Priority")
        self.Mode = params.get("Mode")
        self.Status = params.get("Status")
        self.Cname = params.get("Cname")
        self.Locked = params.get("Locked")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.RequestId = params.get("RequestId")


class ModifyDnssecRequest(AbstractModel):
    """ModifyDnssec request structure.

    """

    def __init__(self):
        r"""
        :param Id: Site ID
        :type Id: str
        :param Status: DNSSEC status
- `enabled`: Enabled
- `disabled`: Disabled
        :type Status: str
        """
        self.Id = None
        self.Status = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
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
        :param Id: Site ID
        :type Id: str
        :param Name: Site name
        :type Name: str
        :param Status: DNSSEC status.
- `enabled`: Enabled
- `disabled`: Disabled
        :type Status: str
        :param Dnssec: DNSSEC information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Dnssec: :class:`tencentcloud.teo.v20220106.models.DnssecInfo`
        :param ModifiedOn: Modification time
        :type ModifiedOn: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.Status = None
        self.Dnssec = None
        self.ModifiedOn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        if params.get("Dnssec") is not None:
            self.Dnssec = DnssecInfo()
            self.Dnssec._deserialize(params.get("Dnssec"))
        self.ModifiedOn = params.get("ModifiedOn")
        self.RequestId = params.get("RequestId")


class ModifyHostsCertificateRequest(AbstractModel):
    """ModifyHostsCertificate request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param Hosts: Domain name that the certificate will be attached to
        :type Hosts: list of str
        :param CertInfo: Certificate information. Note that only `CertId` is required. If it is not specified, the default certificate will be used.
        :type CertInfo: list of ServerCertInfo
        """
        self.ZoneId = None
        self.Hosts = None
        self.CertInfo = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Hosts = params.get("Hosts")
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


class ModifyLoadBalancingRequest(AbstractModel):
    """ModifyLoadBalancing request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        :param Type: Proxy mode.
`dns_only`: Only DNS
`proxied`: Enable proxy
        :type Type: str
        :param OriginId: ID of the origin group used
        :type OriginId: list of str
        :param TTL: Indicates DNS TTL time when `Type=dns_only`
        :type TTL: int
        """
        self.ZoneId = None
        self.LoadBalancingId = None
        self.Type = None
        self.OriginId = None
        self.TTL = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.Type = params.get("Type")
        self.OriginId = params.get("OriginId")
        self.TTL = params.get("TTL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancingResponse(AbstractModel):
    """ModifyLoadBalancing response structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LoadBalancingId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.RequestId = params.get("RequestId")


class ModifyLoadBalancingStatusRequest(AbstractModel):
    """ModifyLoadBalancingStatus request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
        :type ZoneId: str
        :param LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        :param Status: Status.
`online`: Enabled
`offline`: Disabled
        :type Status: str
        """
        self.ZoneId = None
        self.LoadBalancingId = None
        self.Status = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancingStatusResponse(AbstractModel):
    """ModifyLoadBalancingStatus response structure.

    """

    def __init__(self):
        r"""
        :param LoadBalancingId: CLB instance ID
        :type LoadBalancingId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LoadBalancingId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.RequestId = params.get("RequestId")


class ModifyZoneCnameSpeedUpRequest(AbstractModel):
    """ModifyZoneCnameSpeedUp request structure.

    """

    def __init__(self):
        r"""
        :param Id: Site ID
        :type Id: str
        :param Status: CNAME acceleration status.
- `enabled`: Enabled
- `disabled`: Disabled
        :type Status: str
        """
        self.Id = None
        self.Status = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
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
        :param Id: Site ID
        :type Id: str
        :param Name: Site name
        :type Name: str
        :param Status: CNAME acceleration status.
- `enabled`: Enabled
- `disabled`: Disabled
        :type Status: str
        :param ModifiedOn: Update time
        :type ModifiedOn: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.Status = None
        self.ModifiedOn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.ModifiedOn = params.get("ModifiedOn")
        self.RequestId = params.get("RequestId")


class ModifyZoneRequest(AbstractModel):
    """ModifyZone request structure.

    """

    def __init__(self):
        r"""
        :param Id: Site ID, which is used to identify the site.
        :type Id: str
        :param Type: Specifies how the site is connected to EdgeOne.
- `full`: Connect via the name server.
- `partial`: Connect via the CNAME.
        :type Type: str
        :param VanityNameServers: Custom site information
        :type VanityNameServers: :class:`tencentcloud.teo.v20220106.models.VanityNameServers`
        """
        self.Id = None
        self.Type = None
        self.VanityNameServers = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
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
        :param Id: Site ID
        :type Id: str
        :param Name: Site name
        :type Name: str
        :param OriginalNameServers: Name server used by the site
        :type OriginalNameServers: list of str
        :param Status: Site status.
- `pending`: The name server is not connected.
- `active`: The name server is connected.
- `moved`: The name server is moved.
        :type Status: str
        :param Type: Specifies how the site is connected to EdgeOne.
- `full`: Connect via the name server.
- `partial`: Connect via the CNAME.
        :type Type: str
        :param NameServers: List of name servers assigned by Tencent Cloud
        :type NameServers: list of str
        :param CreatedOn: Creation time
        :type CreatedOn: str
        :param ModifiedOn: Modification time
        :type ModifiedOn: str
        :param CnameStatus: CNAME access status.
- `finished`: Ownership of the site is verified.
- `pending`: Verifying the ownership of the site.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CnameStatus: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.OriginalNameServers = None
        self.Status = None
        self.Type = None
        self.NameServers = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.CnameStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.OriginalNameServers = params.get("OriginalNameServers")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.NameServers = params.get("NameServers")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        self.CnameStatus = params.get("CnameStatus")
        self.RequestId = params.get("RequestId")


class ModifyZoneSettingRequest(AbstractModel):
    """ModifyZoneSetting request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site to be modified
        :type ZoneId: str
        :param Cache: Cache expiration time
        :type Cache: :class:`tencentcloud.teo.v20220106.models.CacheConfig`
        :param CacheKey: Node cache key
        :type CacheKey: :class:`tencentcloud.teo.v20220106.models.CacheKey`
        :param MaxAge: Browser cache configuration
        :type MaxAge: :class:`tencentcloud.teo.v20220106.models.MaxAge`
        :param OfflineCache: Offline cache
        :type OfflineCache: :class:`tencentcloud.teo.v20220106.models.OfflineCache`
        :param Quic: QUIC access
        :type Quic: :class:`tencentcloud.teo.v20220106.models.Quic`
        :param PostMaxSize: Maximum size of files transferred over POST request
        :type PostMaxSize: :class:`tencentcloud.teo.v20220106.models.PostMaxSize`
        :param Compression: Smart compression configuration
        :type Compression: :class:`tencentcloud.teo.v20220106.models.Compression`
        :param UpstreamHttp2: HTTP2 origin-pull configuration
        :type UpstreamHttp2: :class:`tencentcloud.teo.v20220106.models.UpstreamHttp2`
        :param ForceRedirect: Force HTTPS redirect configuration
        :type ForceRedirect: :class:`tencentcloud.teo.v20220106.models.ForceRedirect`
        :param Https: HTTPS acceleration configuration
        :type Https: :class:`tencentcloud.teo.v20220106.models.Https`
        :param Origin: Origin server configuration
        :type Origin: :class:`tencentcloud.teo.v20220106.models.Origin`
        :param SmartRouting: Smart acceleration configuration
        :type SmartRouting: :class:`tencentcloud.teo.v20220106.models.SmartRouting`
        :param WebSocket: WebSocket configuration
        :type WebSocket: :class:`tencentcloud.teo.v20220106.models.WebSocket`
        :param ClientIpHeader: Origin-pull client IP header configuration
        :type ClientIpHeader: :class:`tencentcloud.teo.v20220106.models.ClientIp`
        :param CachePrefresh: 
        :type CachePrefresh: :class:`tencentcloud.teo.v20220106.models.CachePrefresh`
        """
        self.ZoneId = None
        self.Cache = None
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


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("Cache") is not None:
            self.Cache = CacheConfig()
            self.Cache._deserialize(params.get("Cache"))
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
            self.ClientIpHeader = ClientIp()
            self.ClientIpHeader._deserialize(params.get("ClientIpHeader"))
        if params.get("CachePrefresh") is not None:
            self.CachePrefresh = CachePrefresh()
            self.CachePrefresh._deserialize(params.get("CachePrefresh"))
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
        :param ZoneId: Site ID
        :type ZoneId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ZoneId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.RequestId = params.get("RequestId")


class ModifyZoneStatusRequest(AbstractModel):
    """ModifyZoneStatus request structure.

    """

    def __init__(self):
        r"""
        :param Id: Site ID
        :type Id: str
        :param Paused: Site status.
- `false`: Enable the site.
- `true`: Disable the site.
        :type Paused: bool
        """
        self.Id = None
        self.Paused = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
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
        :param Id: Site ID
        :type Id: str
        :param Name: Site name
        :type Name: str
        :param Paused: Site status.
- `false`: Enable the site.
- `true`: Disable the site.
        :type Paused: bool
        :param ModifiedOn: Update time
        :type ModifiedOn: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.Paused = None
        self.ModifiedOn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Paused = params.get("Paused")
        self.ModifiedOn = params.get("ModifiedOn")
        self.RequestId = params.get("RequestId")


class OfflineCache(AbstractModel):
    """Configuration of offline cache

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable offline cache. Valid values: `on` and `off`.
Note: This field may return `null`, indicating that no valid value can be obtained.
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
    """Origin server configuration

    """

    def __init__(self):
        r"""
        :param OriginPullProtocol: Origin-pull protocol.
`http`: Switch HTTPS requests to HTTP
`follow`: Follow the protocol of the request.
`https`: Switch HTTP requests to HTTPS. This only supports port 443 on the origin server.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OriginPullProtocol: str
        """
        self.OriginPullProtocol = None


    def _deserialize(self, params):
        self.OriginPullProtocol = params.get("OriginPullProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginCheckOriginStatus(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param Status: 
        :type Status: str
        :param Host: 
        :type Host: list of str
        """
        self.Status = None
        self.Host = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginGroup(AbstractModel):
    """Origin group information

    """

    def __init__(self):
        r"""
        :param OriginId: Origin group ID
        :type OriginId: str
        :param OriginName: Origin group name
        :type OriginName: str
        :param Type: Origin server type
        :type Type: str
        :param Record: Record
        :type Record: list of OriginRecord
        :param UpdateTime: Update time
        :type UpdateTime: str
        :param ZoneId: Site ID
        :type ZoneId: str
        :param ZoneName: Site name
        :type ZoneName: str
        :param OriginType: Origin server type
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OriginType: str
        :param ApplicationProxyUsed: Whether the origin group is used for layer-4 proxy
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ApplicationProxyUsed: bool
        :param LoadBalancingUsed: Whether the origin group is used for load balancing
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type LoadBalancingUsed: bool
        :param Status: 
        :type Status: :class:`tencentcloud.teo.v20220106.models.OriginCheckOriginStatus`
        :param LoadBalancingUsedType: 
        :type LoadBalancingUsedType: str
        """
        self.OriginId = None
        self.OriginName = None
        self.Type = None
        self.Record = None
        self.UpdateTime = None
        self.ZoneId = None
        self.ZoneName = None
        self.OriginType = None
        self.ApplicationProxyUsed = None
        self.LoadBalancingUsed = None
        self.Status = None
        self.LoadBalancingUsedType = None


    def _deserialize(self, params):
        self.OriginId = params.get("OriginId")
        self.OriginName = params.get("OriginName")
        self.Type = params.get("Type")
        if params.get("Record") is not None:
            self.Record = []
            for item in params.get("Record"):
                obj = OriginRecord()
                obj._deserialize(item)
                self.Record.append(obj)
        self.UpdateTime = params.get("UpdateTime")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.OriginType = params.get("OriginType")
        self.ApplicationProxyUsed = params.get("ApplicationProxyUsed")
        self.LoadBalancingUsed = params.get("LoadBalancingUsed")
        if params.get("Status") is not None:
            self.Status = OriginCheckOriginStatus()
            self.Status._deserialize(params.get("Status"))
        self.LoadBalancingUsedType = params.get("LoadBalancingUsedType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginRecord(AbstractModel):
    """Origin group record

    """

    def __init__(self):
        r"""
        :param Record: Record value
        :type Record: str
        :param Area: Region of the origin group. It’s available when the origin group `Type` is `area`. 
If it’s left empty, it means to use the default region.
        :type Area: list of str
        :param Weight: The weight of the origin group. It’s available when the `Type` is `weight`.
        :type Weight: int
        :param Port: Port
        :type Port: int
        :param RecordId: Record ID
        :type RecordId: str
        :param Private: Specifies whether to run private origin authentication.
It is valid only when `OriginType=third_part`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Private: bool
        :param PrivateParameter: Private origin parameter.
It is valid only when `Private=true`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PrivateParameter: list of OriginRecordPrivateParameter
        """
        self.Record = None
        self.Area = None
        self.Weight = None
        self.Port = None
        self.RecordId = None
        self.Private = None
        self.PrivateParameter = None


    def _deserialize(self, params):
        self.Record = params.get("Record")
        self.Area = params.get("Area")
        self.Weight = params.get("Weight")
        self.Port = params.get("Port")
        self.RecordId = params.get("RecordId")
        self.Private = params.get("Private")
        if params.get("PrivateParameter") is not None:
            self.PrivateParameter = []
            for item in params.get("PrivateParameter"):
                obj = OriginRecordPrivateParameter()
                obj._deserialize(item)
                self.PrivateParameter.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginRecordPrivateParameter(AbstractModel):
    """Private origin authentication parameter

    """

    def __init__(self):
        r"""
        :param Name: Name of the private origin authentication parameter.
`AccessKeyId`: Access key ID
`SecretAccessKey`: Secret access key
        :type Name: str
        :param Value: Value of the private origin authentication parameter
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
        


class PostMaxSize(AbstractModel):
    """Maximum size of the file uploaded for streaming via a POST request

    """

    def __init__(self):
        r"""
        :param Switch: Specifies whether to enable custom setting of the maximum file size. 
`off`: Disable. In this case, the max size defaults to 32 MB.
`on`: Enable. You can set a custom max size.
        :type Switch: str
        :param MaxSize: Maximum size. Value range: 1-500 MB.
Note: This field may return `null`, indicating that no valid value can be obtained.
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
        


class QueryString(AbstractModel):
    """Request parameter contained in `CacheKey`

    """

    def __init__(self):
        r"""
        :param Switch: Whether to use `QueryString` as part of `CacheKey`. Valid values: `on` and `off`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Switch: str
        :param Action: `includeCustom`: Include the specified query strings.
`excludeCustom`: Exclude the specified query strings.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Action: str
        :param Value: Array of query strings used/excluded
Note: This field may return `null`, indicating that no valid value can be obtained.
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
        :param Switch: Whether to enable QUIC
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
        


class ReclaimZoneRequest(AbstractModel):
    """ReclaimZone request structure.

    """

    def __init__(self):
        r"""
        :param Name: Site name
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
        


class ReclaimZoneResponse(AbstractModel):
    """ReclaimZone response structure.

    """

    def __init__(self):
        r"""
        :param Name: Site name
        :type Name: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Name = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.RequestId = params.get("RequestId")


class ScanDnsRecordsRequest(AbstractModel):
    """ScanDnsRecords request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Site ID
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
        


class ScanDnsRecordsResponse(AbstractModel):
    """ScanDnsRecords response structure.

    """

    def __init__(self):
        r"""
        :param Status: Scan status
- `doing`: Scanning
- `done`: Scanned
        :type Status: str
        :param RecordsAdded: Number of DNS records added after scanning
        :type RecordsAdded: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.RecordsAdded = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RecordsAdded = params.get("RecordsAdded")
        self.RequestId = params.get("RequestId")


class ServerCertInfo(AbstractModel):
    """HTTPS server certificate configuration

    """

    def __init__(self):
        r"""
        :param CertId: Server certificate ID, which is the ID of the default certificate. If you choose to upload an external certificate for SSL certificate management, a certificate ID will be generated.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CertId: str
        :param Alias: Alias of the certificate
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Alias: str
        :param Type: Certificate type.
`default`: Default certificate
`upload`: External certificate
`managed`: Tencent Cloud managed certificate
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Type: str
        :param ExpireTime: Time when the certificate expires
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ExpireTime: str
        :param DeployTime: Certificate deployment time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DeployTime: str
        :param Status: Certificate deployment status.
`processing`: Deploying
`deployed`: Deployed
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Status: str
        """
        self.CertId = None
        self.Alias = None
        self.Type = None
        self.ExpireTime = None
        self.DeployTime = None
        self.Status = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.Alias = params.get("Alias")
        self.Type = params.get("Type")
        self.ExpireTime = params.get("ExpireTime")
        self.DeployTime = params.get("DeployTime")
        self.Status = params.get("Status")
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
        :param Switch: Whether to enable smart acceleration
`on`: Enable
`off`: Disable
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
        


class Task(AbstractModel):
    """Content management task result

    """

    def __init__(self):
        r"""
        :param JobId: Task ID
        :type JobId: str
        :param Status: Status of the task
        :type Status: str
        :param Target: Resource
        :type Target: str
        :param Type: Task type
        :type Type: str
        :param CreateTime: Task creation time
        :type CreateTime: str
        :param UpdateTime: Task completion time
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
        


class UpstreamHttp2(AbstractModel):
    """HTTP2 origin-pull configuration

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable HTTP2 origin-pull
`on`: Enable
`off`: Disable
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
        :param Switch: Whether to enable the custom name server
`on`: Enable
`off`: Disable
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
    """IP of the custom name server

    """

    def __init__(self):
        r"""
        :param Name: Name of the custom name server
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
        


class WebSocket(AbstractModel):
    """WebSocket configuration.

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable custom WebSocket timeout setting. When it’s `off`: it means to keep the default WebSocket connection timeout period, which is 15 seconds. To change the timeout period, please set it to `on`.
        :type Switch: str
        :param Timeout: Sets timeout period in seconds. Maximum value: 120
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
        :param Id: Site ID
        :type Id: str
        :param Name: Site name
        :type Name: str
        :param OriginalNameServers: List of name servers used by the site
        :type OriginalNameServers: list of str
        :param NameServers: List of name servers assigned by Tencent Cloud
        :type NameServers: list of str
        :param Status: Site status
- `active`: The name server is switched.
- `pending`: The name server is not switched.
- `moved`: The name server is moved.
- `deactivated`: The name server is blocked.
        :type Status: str
        :param Type: How the site is connected to EdgeOne.
- `full`: The site is connected via name server.
- `partial`: The site is connected via CNAME.
        :type Type: str
        :param Paused: Indicates whether the site is disabled
        :type Paused: bool
        :param CreatedOn: Site creation date
        :type CreatedOn: str
        :param ModifiedOn: Site modification date
        :type ModifiedOn: str
        :param CnameStatus: Ownership verification status of the site when it is connected to EdgeOne via CNAME.
- `finished`: The site is verified.
- `pending`: Verifying the ownership of the site.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CnameStatus: str
        """
        self.Id = None
        self.Name = None
        self.OriginalNameServers = None
        self.NameServers = None
        self.Status = None
        self.Type = None
        self.Paused = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.CnameStatus = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.OriginalNameServers = params.get("OriginalNameServers")
        self.NameServers = params.get("NameServers")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.Paused = params.get("Paused")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        self.CnameStatus = params.get("CnameStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneFilter(AbstractModel):
    """Site query filter

    """

    def __init__(self):
        r"""
        :param Name: Filters by the field name. Vaules:
- `name`: Site name.
- `status`: Site status.
        :type Name: str
        :param Values: Filters by the field value
        :type Values: list of str
        :param Fuzzy: Specifies whether to enable fuzzy query. It’s only available when filter name is `name`. If it’s enabled, the length of `Values` must be 1.
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
        