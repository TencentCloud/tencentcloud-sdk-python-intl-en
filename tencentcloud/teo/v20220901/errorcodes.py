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


# CAM signature/authentication error.
AUTHFAILURE = 'AuthFailure'

# DryRun operation, which means the DryRun parameter is passed in yet the request will still be successful.
DRYRUNOPERATION = 'DryRunOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# The certificate does not exist.
FAILEDOPERATION_CERTIFICATENOTFOUND = 'FailedOperation.CertificateNotFound'

# The site status is invalid.
FAILEDOPERATION_INVALIDZONESTATUS = 'FailedOperation.InvalidZoneStatus'

# Internal error.
INTERNALERROR = 'InternalError'

# Server error.
INTERNALERROR_BACKENDERROR = 'InternalError.BackendError'

# The configuration is locked. Please unlock and try again.
INTERNALERROR_CONFIGLOCKED = 'InternalError.ConfigLocked'

# Database error.
INTERNALERROR_DBERROR = 'InternalError.DBError'

# Failed to get configuration
INTERNALERROR_DOMAINCONFIG = 'InternalError.DomainConfig'

# Failed to generate an upload link.
INTERNALERROR_FAILEDTOGENERATEURL = 'InternalError.FailedToGenerateUrl'

# Failed to get the role.
INTERNALERROR_GETROLEERROR = 'InternalError.GetRoleError'

# An unknown error occurred in the backend server.
INTERNALERROR_PROXYSERVER = 'InternalError.ProxyServer'

# Server error.
INTERNALERROR_QUOTASYSTEM = 'InternalError.QuotaSystem'

# The backend routing address is incorrect.
INTERNALERROR_ROUTEERROR = 'InternalError.RouteError'

# Internal system error.
INTERNALERROR_SYSTEMERROR = 'InternalError.SystemError'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# Too many attempts. Please try again later.
INVALIDPARAMETER_ACTIONINPROGRESS = 'InvalidParameter.ActionInProgress'

# The query string has too many values.
INVALIDPARAMETER_CACHEKEYQUERYSTRINGTOOMANYVALUE = 'InvalidParameter.CacheKeyQueryStringTooManyValue'

# HTTPS certificate chain error.
INVALIDPARAMETER_CERTCHAINERROR = 'InvalidParameter.CertChainError'

# Certificate error.
INVALIDPARAMETER_CERTCHECKERROR = 'InvalidParameter.CertCheckError'

# Certificate error.
INVALIDPARAMETER_CERTCOMPLETEERROR = 'InvalidParameter.CertCompleteError'

# Certificate error.
INVALIDPARAMETER_CERTFORMATERROR = 'InvalidParameter.CertFormatError'

# The HTTPS certificate has expired.
INVALIDPARAMETER_CERTISEXPIRED = 'InvalidParameter.CertIsExpired'

# Certificate error.
INVALIDPARAMETER_CERTNOCN = 'InvalidParameter.CertNoCn'

# Invalid HTTPS certificate.
INVALIDPARAMETER_CERTNOINFO = 'InvalidParameter.CertNoInfo'

# Mismatch between the HTTPS certificate and the domain name.
INVALIDPARAMETER_CERTNOTMATCHDOMAIN = 'InvalidParameter.CertNotMatchDomain'

# Mismatch between the HTTPS certificate and the key.
INVALIDPARAMETER_CERTNOTMATCHKEY = 'InvalidParameter.CertNotMatchKey'

# Certificate error.
INVALIDPARAMETER_CERTNOTPEM = 'InvalidParameter.CertNotPem'

# Internal error.
INVALIDPARAMETER_CERTSYSTEMERROR = 'InvalidParameter.CertSystemError'

# The HTTPS certificate is about to expire.
INVALIDPARAMETER_CERTTOEXPIRE = 'InvalidParameter.CertToExpire'

# Certificate error.
INVALIDPARAMETER_CERTTOOSHORTKEYSIZE = 'InvalidParameter.CertTooShortKeySize'

# Certificate error.
INVALIDPARAMETER_CERTUNSUPPORTEDTYPE = 'InvalidParameter.CertUnsupportedType'

# 
INVALIDPARAMETER_CLIENTIPCOUNTRYCONFLICTSWITHIPV6 = 'InvalidParameter.ClientIpCountryConflictsWithIpv6'

# Unable to apply for a wildcard certificate under CNAME mode.
INVALIDPARAMETER_CNAMEWILDHOSTNOTALLOWAPPLYCERTIFICATE = 'InvalidParameter.CnameWildHostNotAllowApplyCertificate'

# 
INVALIDPARAMETER_CONFLICTHOSTORIGIN = 'InvalidParameter.ConflictHostOrigin'

# The domain name does not exist or is not belong to this account.
INVALIDPARAMETER_DOMAINNOTFOUND = 'InvalidParameter.DomainNotFound'

# Traffic scheduling is already enabled for the current domain name.
INVALIDPARAMETER_DOMAINONTRAFFICSCHEDULING = 'InvalidParameter.DomainOnTrafficScheduling'

# The current conditions do not support the requested operation.
INVALIDPARAMETER_ERRACTIONUNSUPPORTTARGET = 'InvalidParameter.ErrActionUnsupportTarget'

# Invalid operation.
INVALIDPARAMETER_ERRINVALIDACTION = 'InvalidParameter.ErrInvalidAction'

# Invalid operation: Invalid parameter.
INVALIDPARAMETER_ERRINVALIDACTIONPARAM = 'InvalidParameter.ErrInvalidActionParam'

# Invalid parameter "action".
INVALIDPARAMETER_ERRINVALIDACTIONPARAMACTION = 'InvalidParameter.ErrInvalidActionParamAction'

# Invalid value type for the parameter "action".
INVALIDPARAMETER_ERRINVALIDACTIONPARAMBADVALUETYPE = 'InvalidParameter.ErrInvalidActionParamBadValueType'

# Invalid parameter: Duplicate parameter names.
INVALIDPARAMETER_ERRINVALIDACTIONPARAMDUPLICATENAME = 'InvalidParameter.ErrInvalidActionParamDuplicateName'

# Invalid value type for the parameter "action".
INVALIDPARAMETER_ERRINVALIDACTIONPARAMNAME = 'InvalidParameter.ErrInvalidActionParamName'

# Invalid parameter: The parameter has too many values.
INVALIDPARAMETER_ERRINVALIDACTIONPARAMTOOMANYVALUES = 'InvalidParameter.ErrInvalidActionParamTooManyValues'

# Invalid action type.
INVALIDPARAMETER_ERRINVALIDACTIONTYPE = 'InvalidParameter.ErrInvalidActionType'

# Invalid condition: The letter case is ignored.
INVALIDPARAMETER_ERRINVALIDCONDITIONIGNORECASE = 'InvalidParameter.ErrInvalidConditionIgnoreCase'

# Invalid condition: Invalid parameter name.
INVALIDPARAMETER_ERRINVALIDCONDITIONNAMEBADNAME = 'InvalidParameter.ErrInvalidConditionNameBadName'

# Invalid condition: The match type is not supported by this parameter.
INVALIDPARAMETER_ERRINVALIDCONDITIONNAMETARGETNOTSUPPORTNAME = 'InvalidParameter.ErrInvalidConditionNameTargetNotSupportName'

# Invalid condition: Invalid regular expression for the parameter value.
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUEBADREGULAR = 'InvalidParameter.ErrInvalidConditionValueBadRegular'

# Invalid parameter value "url".
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUEBADURL = 'InvalidParameter.ErrInvalidConditionValueBadUrl'

# Invalid condition: The parameter value is invalid.
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUEBADVALUE = 'InvalidParameter.ErrInvalidConditionValueBadValue'

# Invalid parameter value: File extension is not allowed.
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUEBADVALUECONTAINFILENAMEEXTENSION = 'InvalidParameter.ErrInvalidConditionValueBadValueContainFileNameExtension'

# Invalid condition: The parameter value exceeds the limit.
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUETOOLONGVALUE = 'InvalidParameter.ErrInvalidConditionValueTooLongValue'

# The condition has too many regular expressions.
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUETOOMANYREGULAR = 'InvalidParameter.ErrInvalidConditionValueTooManyRegular'

# 
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUETOOMANYVALUES = 'InvalidParameter.ErrInvalidConditionValueTooManyValues'

# Invalid condition: Too many wildcards in the parameter.
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUETOOMANYWILDCARD = 'InvalidParameter.ErrInvalidConditionValueTooManyWildcard'

# Invalid condition: The parameter value is 0.
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUEZEROLENGTH = 'InvalidParameter.ErrInvalidConditionValueZeroLength'

# To enable gRPC support, HTTP/2 support must be enabled as well.
INVALIDPARAMETER_GRPCREQUIREHTTP2 = 'InvalidParameter.GrpcRequireHttp2'

# The domain name does not exist.
INVALIDPARAMETER_HOSTNOTFOUND = 'InvalidParameter.HostNotFound'

# CNAME is not switched or the origin is not routed to the EdgeOne server.
INVALIDPARAMETER_HOSTSTATUSNOTALLOWAPPLYCERTIFICATE = 'InvalidParameter.HostStatusNotAllowApplyCertificate'

# Parameter error.
INVALIDPARAMETER_INVALIDACCELERATETYPE = 'InvalidParameter.InvalidAccelerateType'

# Invalid token authentication.
INVALIDPARAMETER_INVALIDAUTHENTICATION = 'InvalidParameter.InvalidAuthentication'

# Invalid key for token authentication.
INVALIDPARAMETER_INVALIDAUTHENTICATIONTYPESECRETKEY = 'InvalidParameter.InvalidAuthenticationTypeSecretKey'

# Invalid token authentication parameter.
INVALIDPARAMETER_INVALIDAUTHENTICATIONTYPESIGNPARAM = 'InvalidParameter.InvalidAuthenticationTypeSignParam'

# Invalid secondary origin domain.
INVALIDPARAMETER_INVALIDBACKUPSERVERNAME = 'InvalidParameter.InvalidBackupServerName'

# Invalid node cache.
INVALIDPARAMETER_INVALIDCACHECONFIGCACHE = 'InvalidParameter.InvalidCacheConfigCache'

# Invalid node cache. The origin behavior is followed.
INVALIDPARAMETER_INVALIDCACHECONFIGFOLLOWORIGIN = 'InvalidParameter.InvalidCacheConfigFollowOrigin'

# Invalid cache key.
INVALIDPARAMETER_INVALIDCACHEKEY = 'InvalidParameter.InvalidCacheKey'

# Cases are ignored in the cache key.
INVALIDPARAMETER_INVALIDCACHEKEYIGNORECASE = 'InvalidParameter.InvalidCacheKeyIgnoreCase'

# Invalid query string.
INVALIDPARAMETER_INVALIDCACHEKEYQUERYSTRINGVALUE = 'InvalidParameter.InvalidCacheKeyQueryStringValue'

# Invalid cache key scheme.
INVALIDPARAMETER_INVALIDCACHEKEYSCHEME = 'InvalidParameter.InvalidCacheKeyScheme'

# Invalid node cache.
INVALIDPARAMETER_INVALIDCACHEONLYONSWITCH = 'InvalidParameter.InvalidCacheOnlyOnSwitch'

# Invalid node cache validity.
INVALIDPARAMETER_INVALIDCACHETIME = 'InvalidParameter.InvalidCacheTime'

# Incorrect certificate information.
INVALIDPARAMETER_INVALIDCERTINFO = 'InvalidParameter.InvalidCertInfo'

# Invalid client IP request header.
INVALIDPARAMETER_INVALIDCLIENTIPHEADERNAME = 'InvalidParameter.InvalidClientIpHeaderName'

# Invalid origin for region-specific origin-pull.
INVALIDPARAMETER_INVALIDCLIENTIPORIGIN = 'InvalidParameter.InvalidClientIpOrigin'

# Invalid smart acceleration.
INVALIDPARAMETER_INVALIDDYNAMICROUTINE = 'InvalidParameter.InvalidDynamicRoutine'

# The package does not support Smart Acceleration.
INVALIDPARAMETER_INVALIDDYNAMICROUTINEBILLING = 'InvalidParameter.InvalidDynamicRoutineBilling'

# 
INVALIDPARAMETER_INVALIDERRORPAGE = 'InvalidParameter.InvalidErrorPage'

# Invalid custom error page.
INVALIDPARAMETER_INVALIDERRORPAGEREDIRECTURL = 'InvalidParameter.InvalidErrorPageRedirectUrl'

# Invalid parameter "https".
INVALIDPARAMETER_INVALIDHTTPS = 'InvalidParameter.InvalidHttps'

# 
INVALIDPARAMETER_INVALIDHTTPSCERTINFO = 'InvalidParameter.InvalidHttpsCertInfo'

# The cipher suite does not match the TLS version.
INVALIDPARAMETER_INVALIDHTTPSCIPHERSUITEANDTLSVERSION = 'InvalidParameter.InvalidHttpsCipherSuiteAndTlsVersion'

# Invalid HTTPS HSTS.
INVALIDPARAMETER_INVALIDHTTPSHSTSMAXAGE = 'InvalidParameter.InvalidHttpsHstsMaxAge'

# Invalid HTTPS TLS version.
INVALIDPARAMETER_INVALIDHTTPSTLSVERSION = 'InvalidParameter.InvalidHttpsTlsVersion'

# Invalid IPv6 settings.
INVALIDPARAMETER_INVALIDIPV6SWITCH = 'InvalidParameter.InvalidIpv6Switch'

# Invalid origin server.
INVALIDPARAMETER_INVALIDORIGIN = 'InvalidParameter.InvalidOrigin'

# Invalid parameter.
INVALIDPARAMETER_INVALIDPARAMETER = 'InvalidParameter.InvalidParameter'

# The speciThe plan does not support limiting the max upload size.
INVALIDPARAMETER_INVALIDPOSTMAXSIZEBILLING = 'InvalidParameter.InvalidPostMaxSizeBilling'

# Invalid POST request size.
INVALIDPARAMETER_INVALIDPOSTSIZEVALUE = 'InvalidParameter.InvalidPostSizeValue'

# The plan does not support QUIC.
INVALIDPARAMETER_INVALIDQUICBILLING = 'InvalidParameter.InvalidQuicBilling'

# Invalid Range GETs.
INVALIDPARAMETER_INVALIDRANGEORIGINPULL = 'InvalidParameter.InvalidRangeOriginPull'

# Invalid request header.
INVALIDPARAMETER_INVALIDREQUESTHEADERNAME = 'InvalidParameter.InvalidRequestHeaderName'

# Invalid request header x-forwarded-for.
INVALIDPARAMETER_INVALIDREQUESTHEADERNAMEXFF = 'InvalidParameter.InvalidRequestHeaderNameXff'

# Invalid request header.
INVALIDPARAMETER_INVALIDREQUESTHEADERVALUE = 'InvalidParameter.InvalidRequestHeaderValue'

# You have not purchased a plan yet.
INVALIDPARAMETER_INVALIDRESOURCEIDBILLING = 'InvalidParameter.InvalidResourceIdBilling'

# Invalid response header.
INVALIDPARAMETER_INVALIDRESPONSEHEADERNAME = 'InvalidParameter.InvalidResponseHeaderName'

# Invalid response header.
INVALIDPARAMETER_INVALIDRESPONSEHEADERVALUE = 'InvalidParameter.InvalidResponseHeaderValue'

# Invalid rule engine settings.
INVALIDPARAMETER_INVALIDRULEENGINE = 'InvalidParameter.InvalidRuleEngine'

# Invalid rule engine operation.
INVALIDPARAMETER_INVALIDRULEENGINEACTION = 'InvalidParameter.InvalidRuleEngineAction'

# The rule does not exist.
INVALIDPARAMETER_INVALIDRULEENGINENOTFOUND = 'InvalidParameter.InvalidRuleEngineNotFound'

# Invalid rule engine condition.
INVALIDPARAMETER_INVALIDRULEENGINETARGET = 'InvalidParameter.InvalidRuleEngineTarget'

# Invalid file extension in the rule engine condition.
INVALIDPARAMETER_INVALIDRULEENGINETARGETSEXTENSION = 'InvalidParameter.InvalidRuleEngineTargetsExtension'

# Invalid URL in the rule engine condition.
INVALIDPARAMETER_INVALIDRULEENGINETARGETSURL = 'InvalidParameter.InvalidRuleEngineTargetsUrl'

# Invalid origin domain.
INVALIDPARAMETER_INVALIDSERVERNAME = 'InvalidParameter.InvalidServerName'

# Origin-pull request configuration error: Invalid query string.
INVALIDPARAMETER_INVALIDUPSTREAMREQUESTQUERYSTRINGVALUE = 'InvalidParameter.InvalidUpstreamRequestQueryStringValue'

# Invalid target host in the URL rewriting rule.
INVALIDPARAMETER_INVALIDURLREDIRECTHOST = 'InvalidParameter.InvalidUrlRedirectHost'

# The target URL for URL rewrite is invalid.
INVALIDPARAMETER_INVALIDURLREDIRECTURL = 'InvalidParameter.InvalidUrlRedirectUrl'

# Invalid WebSocket.
INVALIDPARAMETER_INVALIDWEBSOCKETTIMEOUT = 'InvalidParameter.InvalidWebSocketTimeout'

# Invalid cache key.
INVALIDPARAMETER_KEYRULESINVALIDQUERYSTRINGVALUE = 'InvalidParameter.KeyRulesInvalidQueryStringValue'

# Maximum parameter length exceeded.
INVALIDPARAMETER_LENGTHEXCEEDSLIMIT = 'InvalidParameter.LengthExceedsLimit'

# The origin address cannot be a private IP address.
INVALIDPARAMETER_ORIGINISINNERIP = 'InvalidParameter.OriginIsInnerIp'

# The origin group ID is required.
INVALIDPARAMETER_ORIGINORIGINGROUPIDISREQUIRED = 'InvalidParameter.OriginOriginGroupIdIsRequired'

# Parameter error: Invalid “End time”. The interval between the start and end time cannot exceed 7 days.
INVALIDPARAMETER_PARAMETERERROR = 'InvalidParameter.ParameterError'

# The plan doesn’t exist.
INVALIDPARAMETER_PLANNOTFOUND = 'InvalidParameter.PlanNotFound'

# Maximum upload size exceeded.
INVALIDPARAMETER_POSTMAXSIZELIMITEXCEEDED = 'InvalidParameter.PostMaxSizeLimitExceeded'

# Invalid parameter.
INVALIDPARAMETER_SECURITY = 'InvalidParameter.Security'

# Configuration parameter error.
INVALIDPARAMETER_SETTINGINVALIDPARAM = 'InvalidParameter.SettingInvalidParam'

# Resource error
INVALIDPARAMETER_TARGET = 'InvalidParameter.Target'

# Failed to create the task
INVALIDPARAMETER_TASKNOTGENERATED = 'InvalidParameter.TaskNotGenerated'

# Internal error.
INVALIDPARAMETER_TASKSYSTEMERROR = 'InvalidParameter.TaskSystemError'

# Invalid file upload link.
INVALIDPARAMETER_UPLOADURL = 'InvalidParameter.UploadUrl'

# The site is already bound.
INVALIDPARAMETER_ZONEHASBEENBOUND = 'InvalidParameter.ZoneHasBeenBound'

# The site does not exist.
INVALIDPARAMETER_ZONENOTFOUND = 'InvalidParameter.ZoneNotFound'

# Invalid parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# It conflicts with existing records.
INVALIDPARAMETERVALUE_CONFLICTRECORD = 'InvalidParameterValue.ConflictRecord'

# DNS records conflict with DNSSEC.
INVALIDPARAMETERVALUE_CONFLICTWITHDNSSEC = 'InvalidParameterValue.ConflictWithDNSSEC'

# The host record cannot be the same as the record value.
INVALIDPARAMETERVALUE_CONTENTSAMEASNAME = 'InvalidParameterValue.ContentSameAsName'

# The specified domain name does not match the site. 
INVALIDPARAMETERVALUE_DOMAINNOTMATCHZONE = 'InvalidParameterValue.DomainNotMatchZone'

# Incorrect DNS record.
INVALIDPARAMETERVALUE_INVALIDDNSCONTENT = 'InvalidParameterValue.InvalidDNSContent'

# Incorrect DNS record name.
INVALIDPARAMETERVALUE_INVALIDDNSNAME = 'InvalidParameterValue.InvalidDNSName'

# Invalid domain name. Please check the status.
INVALIDPARAMETERVALUE_INVALIDDOMAINSTATUS = 'InvalidParameterValue.InvalidDomainStatus'

# The site alias already exists. 
INVALIDPARAMETERVALUE_ZONESAMEASNAME = 'InvalidParameterValue.ZoneSameAsName'

# The quota limit has been reached.
LIMITEXCEEDED = 'LimitExceeded'

# Reached the upper limit of resource number
LIMITEXCEEDED_BATCHQUOTA = 'LimitExceeded.BatchQuota'

# Reached the daily upper limit of resource number
LIMITEXCEEDED_DAILYQUOTA = 'LimitExceeded.DailyQuota'

# Query time limit exceeded.
LIMITEXCEEDED_QUERYTIMELIMITEXCEEDED = 'LimitExceeded.QueryTimeLimitExceeded'

# Reached the API rate limit.
LIMITEXCEEDED_RATELIMITEXCEEDED = 'LimitExceeded.RateLimitExceeded'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# 
OPERATIONDENIED_ACCELERATEMAINLANDDISABLE = 'OperationDenied.AccelerateMainlandDisable'

# Switch failed: There are domain names in the shared CNAME group.
OPERATIONDENIED_DOMAININSHARECNAMEGROUP = 'OperationDenied.DomainInShareCnameGroup'

# Unable to use the domain name when it’s blocked.
OPERATIONDENIED_DOMAINISBLOCKED = 'OperationDenied.DomainIsBlocked'

# The domain name doesn't have an ICP filing number.
OPERATIONDENIED_DOMAINNOICP = 'OperationDenied.DomainNoICP'

# Operation failed: The L4 proxy is blocked.
OPERATIONDENIED_L4PROXYINBANNEDSTATUS = 'OperationDenied.L4ProxyInBannedStatus'

# Unable to operate the L4 instance when it’s not running
OPERATIONDENIED_L4STATUSNOTINONLINE = 'OperationDenied.L4StatusNotInOnline'

# The current intermediate IP is of the latest version. 
OPERATIONDENIED_LATESTVERSIONNOW = 'OperationDenied.LatestVersionNow'

# Unable to switch to NS for multiple sites using CNAME.
OPERATIONDENIED_MULTIPLECNAMEZONE = 'OperationDenied.MultipleCnameZone'

# Domain traffic scheduling is not supported in NS access mode.
OPERATIONDENIED_NSNOTALLOWTRAFFICSTRATEGY = 'OperationDenied.NSNotAllowTrafficStrategy'

# The DNS record cannot be added.
OPERATIONDENIED_RECORDISFORBIDDEN = 'OperationDenied.RecordIsForbidden'

# This operation conflicts with concurrent operations. Try again later.
OPERATIONDENIED_RESOURCELOCKEDTEMPORARY = 'OperationDenied.ResourceLockedTemporary'

# The resource is occupied.
RESOURCEINUSE = 'ResourceInUse'

# Resources occupied by the alias domain names under this account.
RESOURCEINUSE_ALIASDOMAIN = 'ResourceInUse.AliasDomain'

# The alias domain name already exists.
RESOURCEINUSE_ALIASNAME = 'ResourceInUse.AliasName'

# Resources occupied by this account via CNAME.
RESOURCEINUSE_CNAME = 'ResourceInUse.Cname'

# DNS resources occupied.
RESOURCEINUSE_DNS = 'ResourceInUse.Dns'

# The domain name is being resolved. If you need to enable acceleration, please go to DNS Records.
RESOURCEINUSE_DNSRECORD = 'ResourceInUse.DnsRecord'

# Duplicate alias domain names.
RESOURCEINUSE_DUPLICATENAME = 'ResourceInUse.DuplicateName'

# Resources occupied by the wildcard domain name.
RESOURCEINUSE_GENERICHOST = 'ResourceInUse.GenericHost'

# Resources occupied by the subdomain names under this account.
RESOURCEINUSE_HOST = 'ResourceInUse.Host'

# Resources occupied by this account via NS.
RESOURCEINUSE_NS = 'ResourceInUse.NS'

# The resource has been connected to EdgeOne by another user.
RESOURCEINUSE_OTHERS = 'ResourceInUse.Others'

# Resources occupied by the alias domain names under other accounts.
RESOURCEINUSE_OTHERSALIASDOMAIN = 'ResourceInUse.OthersAliasDomain'

# Resources occupied by other accounts via CNAME.
RESOURCEINUSE_OTHERSCNAME = 'ResourceInUse.OthersCname'

# Resources occupied by the subdomain names under other accounts.
RESOURCEINUSE_OTHERSHOST = 'ResourceInUse.OthersHost'

# Resources occupied by other accounts via NS.
RESOURCEINUSE_OTHERSNS = 'ResourceInUse.OthersNS'

# Resources occupied by this account and others via CNAME.
RESOURCEINUSE_SELFANDOTHERSCNAME = 'ResourceInUse.SelfAndOthersCname'

# The alias domain name is already added.
RESOURCEINUSE_ZONE = 'ResourceInUse.Zone'

# Insufficient resource.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The resource doesn’t exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# 
RESOURCENOTFOUND_POSTMAXSIZEQUOTANOTFOUND = 'ResourceNotFound.PostMaxSizeQuotaNotFound'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# The certificate does not exist or is not authorized.
RESOURCEUNAVAILABLE_CERTNOTFOUND = 'ResourceUnavailable.CertNotFound'

# The domain name is already connected to EdgeOne by another account. Please retrieve it first in order to add it.
RESOURCEUNAVAILABLE_DOMAINALREADYEXISTS = 'ResourceUnavailable.DomainAlreadyExists'

# The requested accelerated domain name doesn’t exist. 
RESOURCEUNAVAILABLE_DOMAINNOTFOUND = 'ResourceUnavailable.DomainNotFound'

# The domain name does not exist or not use a proxy.
RESOURCEUNAVAILABLE_HOSTNOTFOUND = 'ResourceUnavailable.HostNotFound'

# No proxied sites found
RESOURCEUNAVAILABLE_PROXYZONENOTFOUND = 'ResourceUnavailable.ProxyZoneNotFound'

# The site does not exist or is not belong to this account.
RESOURCEUNAVAILABLE_ZONENOTFOUND = 'ResourceUnavailable.ZoneNotFound'

# 
RESOURCESSOLDOUT_L7LACKOFRESOURCES = 'ResourcesSoldOut.L7LackOfResources'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# CAM is not authorized.
UNAUTHORIZEDOPERATION_CAMUNAUTHORIZED = 'UnauthorizedOperation.CamUnauthorized'

# Authentication error.
UNAUTHORIZEDOPERATION_DOMAINEMPTY = 'UnauthorizedOperation.DomainEmpty'

# The sub-account is not authorized for the operation. Please get permissions first.
UNAUTHORIZEDOPERATION_NOPERMISSION = 'UnauthorizedOperation.NoPermission'

# An unknown error occurred in the backend server.
UNAUTHORIZEDOPERATION_UNKNOWN = 'UnauthorizedOperation.Unknown'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# 
UNSUPPORTEDOPERATION_TARGETNAMEORIGINTYPECOS = 'UnsupportedOperation.TargetNameOriginTypeCos'
