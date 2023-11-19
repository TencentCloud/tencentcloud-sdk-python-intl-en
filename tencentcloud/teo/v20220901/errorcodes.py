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


# DryRun operation, which means the DryRun parameter is passed in yet the request will still be successful.
DRYRUNOPERATION = 'DryRunOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Failed to publish: The certificate has expired. 
FAILEDOPERATION_CERTIFICATEHASEXPIRED = 'FailedOperation.CertificateHasExpired'

# The certificate does not exist.
FAILEDOPERATION_CERTIFICATENOTFOUND = 'FailedOperation.CertificateNotFound'

# Insufficient account balance
FAILEDOPERATION_INSUFFICIENTACCOUNTBALANCE = 'FailedOperation.InsufficientAccountBalance'

# The site status is invalid.
FAILEDOPERATION_INVALIDZONESTATUS = 'FailedOperation.InvalidZoneStatus'

# Operation failed.
FAILEDOPERATION_MODIFYFAILED = 'FailedOperation.ModifyFailed'

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

# Unknown error.
INTERNALERROR_UNKNOWERROR = 'InternalError.UnknowError'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# The regex is not in the standard RE2 format.
INVALIDPARAMETER_ACCESSREDIRECTREGEXERROR = 'InvalidParameter.AccessRedirectRegexError'

# Too many attempts. Please try again later.
INVALIDPARAMETER_ACTIONINPROGRESS = 'InvalidParameter.ActionInProgress'

# Cu200dhinese SM certificates are not supported for alias domain names.
INVALIDPARAMETER_ALIASDOMAINNOTSUPPORTSMCERT = 'InvalidParameter.AliasDomainNotSupportSMCert'

# Invalid query string.
INVALIDPARAMETER_CACHEKEYQUERYSTRINGREQUIRESFULLURLCACHEOFF = 'InvalidParameter.CacheKeyQueryStringRequiresFullUrlCacheOff'

# The query string has too many values.
INVALIDPARAMETER_CACHEKEYQUERYSTRINGTOOMANYVALUE = 'InvalidParameter.CacheKeyQueryStringTooManyValue'

# Mismatch between the HTTPS certificate and the domain name.
INVALIDPARAMETER_CERTNOTMATCHDOMAIN = 'InvalidParameter.CertNotMatchDomain'

# Internal error.
INVALIDPARAMETER_CERTSYSTEMERROR = 'InvalidParameter.CertSystemError'

# The HTTPS certificate is about to expire.
INVALIDPARAMETER_CERTTOEXPIRE = 'InvalidParameter.CertToExpire'

# Certificate error.
INVALIDPARAMETER_CERTTOOSHORTKEYSIZE = 'InvalidParameter.CertTooShortKeySize'

# IPv6 access conflicts with client IP geographical location.
INVALIDPARAMETER_CLIENTIPCOUNTRYCONFLICTSWITHIPV6 = 'InvalidParameter.ClientIpCountryConflictsWithIpv6'

# Unable to apply for a wildcard certificate under CNAME mode.
INVALIDPARAMETER_CNAMEWILDHOSTNOTALLOWAPPLYCERTIFICATE = 'InvalidParameter.CnameWildHostNotAllowApplyCertificate'

# The origin cannot be the same as the domain name.
INVALIDPARAMETER_CONFLICTHOSTORIGIN = 'InvalidParameter.ConflictHostOrigin'

# The domain name does not exist or is not belong to this account.
INVALIDPARAMETER_DOMAINNOTFOUND = 'InvalidParameter.DomainNotFound'

# Traffic scheduling is already enabled for the current domain name.
INVALIDPARAMETER_DOMAINONTRAFFICSCHEDULING = 'InvalidParameter.DomainOnTrafficScheduling'

# The current conditions do not support the requested operation.
INVALIDPARAMETER_ERRACTIONUNSUPPORTTARGET = 'InvalidParameter.ErrActionUnsupportTarget'

# Invalid operation.
INVALIDPARAMETER_ERRINVALIDACTION = 'InvalidParameter.ErrInvalidAction'

# Invalid operation: Duplicate operation configuration.
INVALIDPARAMETER_ERRINVALIDACTIONDUPLICATEACTION = 'InvalidParameter.ErrInvalidActionDuplicateAction'

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

# Invalid action.
INVALIDPARAMETER_ERRINVALIDACTIONPARAMVALUE = 'InvalidParameter.ErrInvalidActionParamValue'

# Invalid action type.
INVALIDPARAMETER_ERRINVALIDACTIONTYPE = 'InvalidParameter.ErrInvalidActionType'

# Invalid conditions.
INVALIDPARAMETER_ERRINVALIDCONDITION = 'InvalidParameter.ErrInvalidCondition'

# You can only configure one host matching type when modifying the origin.
INVALIDPARAMETER_ERRINVALIDCONDITIONHOSTTOOMANYWHENMODIFYORIGINACTIONCONFIGURED = 'InvalidParameter.ErrInvalidConditionHostTooManyWhenModifyOriginActionConfigured'

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

# Invalid condition: The parameter value exceeds the limit.
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUETOOMANYVALUES = 'InvalidParameter.ErrInvalidConditionValueTooManyValues'

# Invalid condition: Too many wildcards in the parameter.
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUETOOMANYWILDCARD = 'InvalidParameter.ErrInvalidConditionValueTooManyWildcard'

# Invalid condition: The parameter value is 0.
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUEZEROLENGTH = 'InvalidParameter.ErrInvalidConditionValueZeroLength'

# ELSE is not supported for origin server modification.
INVALIDPARAMETER_ERRINVALIDELSEWHENMODIFYORIGINACTIONCONFIGURED = 'InvalidParameter.ErrInvalidElseWhenModifyOriginActionConfigured'

# 
INVALIDPARAMETER_ERRNILCONDITION = 'InvalidParameter.ErrNilCondition'

# To enable gRPC support, HTTP/2 support must be enabled as well.
INVALIDPARAMETER_GRPCREQUIREHTTP2 = 'InvalidParameter.GrpcRequireHttp2'

# Host header error
INVALIDPARAMETER_HOSTHEADERINVALID = 'InvalidParameter.HostHeaderInvalid'

# The domain name does not exist.
INVALIDPARAMETER_HOSTNOTFOUND = 'InvalidParameter.HostNotFound'

# CNAME is not switched or the origin is not routed to the EdgeOne server.
INVALIDPARAMETER_HOSTSTATUSNOTALLOWAPPLYCERTIFICATE = 'InvalidParameter.HostStatusNotAllowApplyCertificate'

# Parameter error.
INVALIDPARAMETER_INVALIDACCELERATETYPE = 'InvalidParameter.InvalidAccelerateType'

# Invalid token authentication.
INVALIDPARAMETER_INVALIDAUTHENTICATION = 'InvalidParameter.InvalidAuthentication'

# 
INVALIDPARAMETER_INVALIDAUTHENTICATIONTYPEEXPIRETIME = 'InvalidParameter.InvalidAuthenticationTypeExpireTime'

# Invalid key for token authentication.
INVALIDPARAMETER_INVALIDAUTHENTICATIONTYPESECRETKEY = 'InvalidParameter.InvalidAuthenticationTypeSecretKey'

# Invalid token authentication parameter.
INVALIDPARAMETER_INVALIDAUTHENTICATIONTYPESIGNPARAM = 'InvalidParameter.InvalidAuthenticationTypeSignParam'

# Invalid authentication token format.
INVALIDPARAMETER_INVALIDAUTHENTICATIONTYPETIMEFORMAT = 'InvalidParameter.InvalidAuthenticationTypeTimeFormat'

# Invalid authentication token parameter.
INVALIDPARAMETER_INVALIDAUTHENTICATIONTYPETIMEPARAM = 'InvalidParameter.InvalidAuthenticationTypeTimeParam'

# Invalid third-party object storage.
INVALIDPARAMETER_INVALIDAWSPRIVATEACCESS = 'InvalidParameter.InvalidAwsPrivateAccess'

# Invalid region. Please fill in a correct region of the third-party object storage service.
INVALIDPARAMETER_INVALIDAWSREGION = 'InvalidParameter.InvalidAwsRegion'

# Invalid third-party object storage.
INVALIDPARAMETER_INVALIDAWSSECRETKEY = 'InvalidParameter.InvalidAwsSecretKey'

# Invalid secondary origin domain.
INVALIDPARAMETER_INVALIDBACKUPSERVERNAME = 'InvalidParameter.InvalidBackupServerName'

# Invalid node cache.
INVALIDPARAMETER_INVALIDCACHECONFIGCACHE = 'InvalidParameter.InvalidCacheConfigCache'

# Invalid node cache. The origin behavior is followed.
INVALIDPARAMETER_INVALIDCACHECONFIGFOLLOWORIGIN = 'InvalidParameter.InvalidCacheConfigFollowOrigin'

# Invalid cache key.
INVALIDPARAMETER_INVALIDCACHEKEY = 'InvalidParameter.InvalidCacheKey'

# Invalid cache key cookie.
INVALIDPARAMETER_INVALIDCACHEKEYCOOKIE = 'InvalidParameter.InvalidCacheKeyCookie'

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

# Invalid origin-pull configuration. When `OriginType` is `COS` or `AWS_S3`, the origin address must be an object storage domain name.
INVALIDPARAMETER_INVALIDCOSDOMAIN = 'InvalidParameter.InvalidCosDomain'

# Invalid smart acceleration.
INVALIDPARAMETER_INVALIDDYNAMICROUTINE = 'InvalidParameter.InvalidDynamicRoutine'

# The package does not support Smart Acceleration.
INVALIDPARAMETER_INVALIDDYNAMICROUTINEBILLING = 'InvalidParameter.InvalidDynamicRoutineBilling'

# Invalid custom error page.
INVALIDPARAMETER_INVALIDERRORPAGE = 'InvalidParameter.InvalidErrorPage'

# Invalid custom error page.
INVALIDPARAMETER_INVALIDERRORPAGEREDIRECTURL = 'InvalidParameter.InvalidErrorPageRedirectUrl'

# Invalid forced HTTPS direction settings
INVALIDPARAMETER_INVALIDFORCEREDIRECTTYPE = 'InvalidParameter.InvalidForceRedirectType'

# Invalid parameter "https".
INVALIDPARAMETER_INVALIDHTTPS = 'InvalidParameter.InvalidHttps'

# Invalid HTTPS certificate.
INVALIDPARAMETER_INVALIDHTTPSCERTINFO = 'InvalidParameter.InvalidHttpsCertInfo'

# The cipher suite does not match the TLS version.
INVALIDPARAMETER_INVALIDHTTPSCIPHERSUITEANDTLSVERSION = 'InvalidParameter.InvalidHttpsCipherSuiteAndTlsVersion'

# Invalid HTTPS HSTS.
INVALIDPARAMETER_INVALIDHTTPSHSTSMAXAGE = 'InvalidParameter.InvalidHttpsHstsMaxAge'

# Invalid HTTPS TLS version.
INVALIDPARAMETER_INVALIDHTTPSTLSVERSION = 'InvalidParameter.InvalidHttpsTlsVersion'

# Invalid IPv6 settings.
INVALIDPARAMETER_INVALIDIPV6SWITCH = 'InvalidParameter.InvalidIpv6Switch'

# Invalid browser cache.
INVALIDPARAMETER_INVALIDMAXAGETIME = 'InvalidParameter.InvalidMaxAgeTime'

# Invalid origin server.
INVALIDPARAMETER_INVALIDORIGIN = 'InvalidParameter.InvalidOrigin'

# The origin cannot be a private IP or loopback address.
INVALIDPARAMETER_INVALIDORIGINIP = 'InvalidParameter.InvalidOriginIp'

# Invalid parameter.
INVALIDPARAMETER_INVALIDPARAMETER = 'InvalidParameter.InvalidParameter'

# The speciThe plan does not support limiting the max upload size.
INVALIDPARAMETER_INVALIDPOSTMAXSIZEBILLING = 'InvalidParameter.InvalidPostMaxSizeBilling'

# Invalid POST request size.
INVALIDPARAMETER_INVALIDPOSTSIZEVALUE = 'InvalidParameter.InvalidPostSizeValue'

# AccessKeyId and SecretAccessKey u200dare required to access the third-party object storage.
INVALIDPARAMETER_INVALIDPRIVATEACCESSPARAMS = 'InvalidParameter.InvalidPrivateAccessParams'

# The value of `PrivateAccess` should be `on` or `off`.
INVALIDPARAMETER_INVALIDPRIVATEACCESSSWITCH = 'InvalidParameter.InvalidPrivateAccessSwitch'

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

# Invalid client IP or CIDR block.
INVALIDPARAMETER_INVALIDSTANDARDDEBUGCLIENTIP = 'InvalidParameter.InvalidStandardDebugClientIp'

# The expiration time is exceeded.
INVALIDPARAMETER_INVALIDSTANDARDDEBUGEXPIRETIMELIMIT = 'InvalidParameter.InvalidStandardDebugExpireTimeLimit'

# Origin-pull request configuration error: Invalid query string.
INVALIDPARAMETER_INVALIDUPSTREAMREQUESTQUERYSTRINGVALUE = 'InvalidParameter.InvalidUpstreamRequestQueryStringValue'

# Invalid URL rewrite.
INVALIDPARAMETER_INVALIDURLREDIRECT = 'InvalidParameter.InvalidUrlRedirect'

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

# Smart routing is not supported.
INVALIDPARAMETER_MULTIPLYLAYERNOTSUPPORTSMARTROUTING = 'InvalidParameter.MultiplyLayerNotSupportSmartRouting'

# Unsupported preset variables exist.
INVALIDPARAMETER_NOTSUPPORTTHISPRESET = 'InvalidParameter.NotSupportThisPreset'

# The domain name is configured to forward requests to the origin directly. iSmart Acceleration must be enabled.
INVALIDPARAMETER_OCDIRECTORIGINREQUIRESSMARTROUTING = 'InvalidParameter.OCDirectOriginRequiresSmartRouting'

# The origin address cannot be a private IP address.
INVALIDPARAMETER_ORIGINISINNERIP = 'InvalidParameter.OriginIsInnerIp'

# The origin group name already exists.
INVALIDPARAMETER_ORIGINNAMEEXISTS = 'InvalidParameter.OriginNameExists'

# The origin group ID is required.
INVALIDPARAMETER_ORIGINORIGINGROUPIDISREQUIRED = 'InvalidParameter.OriginOriginGroupIdIsRequired'

# Incorrect origin server format. 
INVALIDPARAMETER_ORIGINRECORDFORMATERROR = 'InvalidParameter.OriginRecordFormatError'

# Parameter error: Invalid “End time”. The interval between the start and end time cannot exceed 7 days.
INVALIDPARAMETER_PARAMETERERROR = 'InvalidParameter.ParameterError'

# The plan doesn’t exist.
INVALIDPARAMETER_PLANNOTFOUND = 'InvalidParameter.PlanNotFound'

# Maximum upload size exceeded.
INVALIDPARAMETER_POSTMAXSIZELIMITEXCEEDED = 'InvalidParameter.PostMaxSizeLimitExceeded'

# The instance name already exists.
INVALIDPARAMETER_PROXYNAMEDUPLICATING = 'InvalidParameter.ProxyNameDuplicating'

# 
INVALIDPARAMETER_RULEORIGINFORMATERROR = 'InvalidParameter.RuleOriginFormatError'

# The origin of the rule does not support multiple domain names.
INVALIDPARAMETER_RULEORIGINMULTIDOMAIN = 'InvalidParameter.RuleOriginMultiDomain'

# The origin port of the rule must be an integer.
INVALIDPARAMETER_RULEORIGINPORTINTEGER = 'InvalidParameter.RuleOriginPortInteger'

# Invalid origin in the rule.
INVALIDPARAMETER_RULEORIGINVALUEERROR = 'InvalidParameter.RuleOriginValueError'

# The rule port already exists.
INVALIDPARAMETER_RULEPORTDUPLICATING = 'InvalidParameter.RulePortDuplicating'

# 
INVALIDPARAMETER_RULEPORTGROUP = 'InvalidParameter.RulePortGroup'

# 
INVALIDPARAMETER_RULEPORTINTEGER = 'InvalidParameter.RulePortInteger'

# Invalid parameter.
INVALIDPARAMETER_SECURITY = 'InvalidParameter.Security'

# Configuration parameter error.
INVALIDPARAMETER_SETTINGINVALIDPARAM = 'InvalidParameter.SettingInvalidParam'

# Shield Space is not bound with an origin. 
INVALIDPARAMETER_SPACENOTBINDORIGIN = 'InvalidParameter.SpaceNotBindOrigin'

# Resource error
INVALIDPARAMETER_TARGET = 'InvalidParameter.Target'

# Failed to create the task
INVALIDPARAMETER_TASKNOTGENERATED = 'InvalidParameter.TaskNotGenerated'

# Internal error.
INVALIDPARAMETER_TASKSYSTEMERROR = 'InvalidParameter.TaskSystemError'

# Too many filter values.
INVALIDPARAMETER_TOOMANYFILTERVALUES = 'InvalidParameter.TooManyFilterValues'

# Invalid file upload link.
INVALIDPARAMETER_UPLOADURL = 'InvalidParameter.UploadUrl'

# The site is already bound.
INVALIDPARAMETER_ZONEHASBEENBOUND = 'InvalidParameter.ZoneHasBeenBound'

# The site is being upgraded. Changing is not supported. Please try again later.
INVALIDPARAMETER_ZONEISGRAYPUBLISHING = 'InvalidParameter.ZoneIsGrayPublishing'

# To switch a site from connecting without a domain name to connecting via the CNAME, the site name is required.
INVALIDPARAMETER_ZONENAMEISREQUIRED = 'InvalidParameter.ZoneNameIsRequired'

# The site does not exist.
INVALIDPARAMETER_ZONENOTFOUND = 'InvalidParameter.ZoneNotFound'

# Invalid parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# It conflicts with existing records.
INVALIDPARAMETERVALUE_CONFLICTRECORD = 'InvalidParameterValue.ConflictRecord'

# DNS records conflict with DNSSEC.
INVALIDPARAMETERVALUE_CONFLICTWITHDNSSEC = 'InvalidParameterValue.ConflictWithDNSSEC'

# This DNS record conflicts with NS records.
INVALIDPARAMETERVALUE_CONFLICTWITHNSRECORD = 'InvalidParameterValue.ConflictWithNSRecord'

# The host record cannot be the same as the record value.
INVALIDPARAMETERVALUE_CONTENTSAMEASNAME = 'InvalidParameterValue.ContentSameAsName'

# The specified domain name does not match the site. 
INVALIDPARAMETERVALUE_DOMAINNOTMATCHZONE = 'InvalidParameterValue.DomainNotMatchZone'

# Invalid alias domain suffix. This domain is for internal usage and cannot be used as the alias domain.
INVALIDPARAMETERVALUE_INVALIDALIASNAMESUFFIX = 'InvalidParameterValue.InvalidAliasNameSuffix'

# Incorrect DNS record.
INVALIDPARAMETERVALUE_INVALIDDNSCONTENT = 'InvalidParameterValue.InvalidDNSContent'

# Incorrect DNS record name.
INVALIDPARAMETERVALUE_INVALIDDNSNAME = 'InvalidParameterValue.InvalidDNSName'

# Invalid accelerated domain name. It can contain [0-9], [A-Z], [a-z] and [-]. It cannot start or end with "-". 
INVALIDPARAMETERVALUE_INVALIDDOMAINNAME = 'InvalidParameterValue.InvalidDomainName'

# Invalid domain name. Please check the status.
INVALIDPARAMETERVALUE_INVALIDDOMAINSTATUS = 'InvalidParameterValue.InvalidDomainStatus'

# Incorrect DNS proxy
INVALIDPARAMETERVALUE_INVALIDPROXYORIGIN = 'InvalidParameterValue.InvalidProxyOrigin'

# Wildcard domain CNAMEs are not supported.
INVALIDPARAMETERVALUE_NOTALLOWEDWILDCARDSHAREDCNAME = 'InvalidParameterValue.NotAllowedWildcardSharedCNAME'

# The specified origin group does not exist.
INVALIDPARAMETERVALUE_ORIGINGROUPNOTEXISTS = 'InvalidParameterValue.OriginGroupNotExists'

# Enter a valid shared CNAME prefix of up to 50 characters.
INVALIDPARAMETERVALUE_SHAREDCNAMEPREFIXNOTMATCH = 'InvalidParameterValue.SharedCNAMEPrefixNotMatch'

# The site alias already exists. 
INVALIDPARAMETERVALUE_ZONESAMEASNAME = 'InvalidParameterValue.ZoneSameAsName'

# The quota limit has been reached.
LIMITEXCEEDED = 'LimitExceeded'

# Reached the upper limit of resource number
LIMITEXCEEDED_BATCHQUOTA = 'LimitExceeded.BatchQuota'

# Reached the daily upper limit of resource number
LIMITEXCEEDED_DAILYQUOTA = 'LimitExceeded.DailyQuota'

# Not supported by the plan.
LIMITEXCEEDED_PACKNOTALLOW = 'LimitExceeded.PackNotAllow'

# Query time limit exceeded.
LIMITEXCEEDED_QUERYTIMELIMITEXCEEDED = 'LimitExceeded.QueryTimeLimitExceeded'

# Reached the API rate limit.
LIMITEXCEEDED_RATELIMITEXCEEDED = 'LimitExceeded.RateLimitExceeded'

# Limit exceeded
LIMITEXCEEDED_SECURITY = 'LimitExceeded.Security'

# Reached the upper limit of sites of the plan
LIMITEXCEEDED_ZONEBINDPLAN = 'LimitExceeded.ZoneBindPlan'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# Cross-MLC-border acceleration is in beta. To join the beta, submit a ticket.
OPERATIONDENIED_ACCELERATEMAINLANDDISABLE = 'OperationDenied.AccelerateMainlandDisable'

# Cross-MLC-border acceleration and IPv6 cannot be configured at the same time.
OPERATIONDENIED_ACCELERATEMAINLANDIPV6CONFLICT = 'OperationDenied.AccelerateMainlandIpv6Conflict'

# An L7 DNS service referencing the origin group is being deployed. Please edit later.
OPERATIONDENIED_ACCELERATIONDOMAINSTATUSNOTINONLINE = 'OperationDenied.AccelerationDomainStatusNotInOnline'

# The configuration is locked. Please unlock and try again.
OPERATIONDENIED_CONFIGLOCKED = 'OperationDenied.ConfigLocked'

# The EdgeOne service of the site is being disabled. Please try again later.
OPERATIONDENIED_DISABLEZONENOTCOMPLETED = 'OperationDenied.DisableZoneNotCompleted'

# Switch failed: There are domain names in the shared CNAME group.
OPERATIONDENIED_DOMAININSHARECNAMEGROUP = 'OperationDenied.DomainInShareCnameGroup'

# Unable to use the domain name when it’s blocked.
OPERATIONDENIED_DOMAINISBLOCKED = 'OperationDenied.DomainIsBlocked'

# The domain name doesn't have an ICP filing number.
OPERATIONDENIED_DOMAINNOICP = 'OperationDenied.DomainNoICP'

# Unable to modify the service area: There are domain names under the site.
OPERATIONDENIED_DOMAINNUMBERISNOTZERO = 'OperationDenied.DomainNumberIsNotZero'

# The EdgeOne service of the site is disabled. Please enable it and try again.
OPERATIONDENIED_ERRZONEISALREADYPAUSED = 'OperationDenied.ErrZoneIsAlreadyPaused'

# The security service must be enabled when you enable the DDoS Protection.
OPERATIONDENIED_INVALIDADVANCEDDEFENSESECURITYTYPE = 'OperationDenied.InvalidAdvancedDefenseSecurityType'

# The acceleration regions of the site must be in the Chinese mainland when you enable the DDoS Protection.
OPERATIONDENIED_INVALIDADVANCEDDEFENSEZONEAREA = 'OperationDenied.InvalidAdvancedDefenseZoneArea'

# Operation failed: The L4 proxy is blocked.
OPERATIONDENIED_L4PROXYINBANNEDSTATUS = 'OperationDenied.L4ProxyInBannedStatus'

# The EdgeOne service cannot be disabled for the site: A L4 proxy instance is being deployed.
OPERATIONDENIED_L4PROXYINPROGRESSSTATUS = 'OperationDenied.L4ProxyInProgressStatus'

# Unable to disable the site: There are L4 proxy instances disabled.
OPERATIONDENIED_L4PROXYINSTOPPINGSTATUS = 'OperationDenied.L4ProxyInStoppingStatus'

# Unable to operate the L4 instance when it’s not running
OPERATIONDENIED_L4STATUSNOTINONLINE = 'OperationDenied.L4StatusNotInOnline'

# The EdgeOne service cannot be disabled for the site: An accelerated domain name is being deployed.
OPERATIONDENIED_L7HOSTINPROCESSSTATUS = 'OperationDenied.L7HostInProcessStatus'

# The site status does not support operations on load balancers.
OPERATIONDENIED_LOADBALANCINGZONEISNOTACTIVE = 'OperationDenied.LoadBalancingZoneIsNotActive'

# Unable to switch to NS for multiple sites using CNAME.
OPERATIONDENIED_MULTIPLECNAMEZONE = 'OperationDenied.MultipleCnameZone'

# Domain traffic scheduling is not supported in NS access mode.
OPERATIONDENIED_NSNOTALLOWTRAFFICSTRATEGY = 'OperationDenied.NSNotAllowTrafficStrategy'

# You can only switch a site connected without a domain name to connecting via the CNAME
OPERATIONDENIED_NODOMAINACCESSZONEONLYALLOWMODIFIEDTOCNAME = 'OperationDenied.NoDomainAccessZoneOnlyAllowModifiedToCNAME'

# You can only switch a site connected without a domain name to connecting via the CNAME. Other operations are not allowed.
OPERATIONDENIED_NODOMAINACCESSZONEONLYSUPPORTMODIFYTYPE = 'OperationDenied.NoDomainAccessZoneOnlySupportModifyType'

# Failed to delete: The acceleration domain name is in use. 
OPERATIONDENIED_ORIGINGROUPACCELERATIONDOMAINUSED = 'OperationDenied.OriginGroupAccelerationDomainUsed'

# The specified plan does not support changing the service area of the site.
OPERATIONDENIED_PLANNOTSUPPORTMODIFYZONEAREA = 'OperationDenied.PlanNotSupportModifyZoneArea'

# This site is using Anycast IP scheduling mode and does not support Cross-MLC-border acceleration. 
OPERATIONDENIED_PLATTYPEIPACCELERATEMAINLANDNOTSUPPORT = 'OperationDenied.PlatTypeIPAccelerateMainlandNotSupport'

# The DNS record cannot be added.
OPERATIONDENIED_RECORDISFORBIDDEN = 'OperationDenied.RecordIsForbidden'

# This operation conflicts with concurrent operations. Try again later.
OPERATIONDENIED_RESOURCELOCKEDTEMPORARY = 'OperationDenied.ResourceLockedTemporary'

# The domain name is bound with a shared CNAME and cannot be changed to "Cross-MLC-border acceleration". Please unbind the domain name from the shared CNAME first.
OPERATIONDENIED_SHAREDCNAMEUNSUPPORTEDACCELERATEMAINLAND = 'OperationDenied.SharedCNAMEUnsupportedAccelerateMainland'

# The domain name is bound with a shared CNAME and cannot be changed to "IPv6 access". Please unbind the domain name from the shared CNAME first.
OPERATIONDENIED_SHAREDCNAMEUNSUPPORTEDIPV6 = 'OperationDenied.SharedCNAMEUnsupportedIPv6'

# There is a test version in use. Please release the test version to the live environment, or roll back the test version and try again.
OPERATIONDENIED_VERSIONCONTROLISGRAYING = 'OperationDenied.VersionControlIsGraying'

# The shared CNAME has been bound to another site. Please unbind first.
OPERATIONDENIED_ZONEISBINDINGSHAREDCNAME = 'OperationDenied.ZoneIsBindingSharedCNAME'

# Error found in the associated custom error page. Please unbind it first.
OPERATIONDENIED_ZONEISREFERENCECUSTOMERRORPAGE = 'OperationDenied.ZoneIsReferenceCustomErrorPage'

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

# Unable to delete the shared CNAME: It is bound to an acceleration domain name. Please remove the binding first.
RESOURCEINUSE_SHAREDCNAME = 'ResourceInUse.SharedCNAME'

# The alias domain name is already added.
RESOURCEINUSE_ZONE = 'ResourceInUse.Zone'

# Insufficient resource.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The resource doesn’t exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# Maximum upload size is not configured.
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

# The shared CNAME is used by others.
RESOURCEUNAVAILABLE_SHAREDCNAMEALREADYEXISTS = 'ResourceUnavailable.SharedCNAMEAlreadyExists'

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

# The origin type of the target domain cannot be COS for an alias domain.
UNSUPPORTEDOPERATION_TARGETNAMEORIGINTYPECOS = 'UnsupportedOperation.TargetNameOriginTypeCos'
