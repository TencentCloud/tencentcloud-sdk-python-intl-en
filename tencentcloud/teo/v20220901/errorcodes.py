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

# The edge HTTPS certificate has expired. Issuing expired certificates is currently not supported.
FAILEDOPERATION_CERTIFICATEHASEXPIRED = 'FailedOperation.CertificateHasExpired'

# The edge HTTPS certificate does not exist.
FAILEDOPERATION_CERTIFICATENOTFOUND = 'FailedOperation.CertificateNotFound'

# Syntax error in the condition expression of the configuration file.
FAILEDOPERATION_CONFIGCONDITIONSYNTAXERROR = 'FailedOperation.ConfigConditionSyntaxError'

# Unrecognized condition matching type.
FAILEDOPERATION_CONFIGCONDITIONUNKNOWNTARGET = 'FailedOperation.ConfigConditionUnknownTarget'

# The value field of the condition expression cannot be empty in the configuration file.
FAILEDOPERATION_CONFIGCONDITIONVALUEEMPTYERROR = 'FailedOperation.ConfigConditionValueEmptyError'

# The configuration file contains fields with inconsistent data types.
FAILEDOPERATION_CONFIGFIELDTYPEERROR = 'FailedOperation.ConfigFieldTypeError'

# Syntax error in the configuration file.
FAILEDOPERATION_CONFIGFORMATERROR = 'FailedOperation.ConfigFormatError'

# Incorrect format of the configuration file. Parsing failed.
FAILEDOPERATION_CONFIGMALFORMEDCONTENT = 'FailedOperation.ConfigMalformedContent'

# Parameter verification error in the configuration file.
FAILEDOPERATION_CONFIGPARAMVALIDATEERRORS = 'FailedOperation.ConfigParamValidateErrors'

# The specified field in the configuration file is not recognized, indicating a possible spelling error or incorrect placement within the file structure.
FAILEDOPERATION_CONFIGUNKNOWNFIELD = 'FailedOperation.ConfigUnknownField'

# The current configuration file version is not supported.
FAILEDOPERATION_CONFIGUNSUPPORTEDFORMATVERSION = 'FailedOperation.ConfigUnsupportedFormatVersion'

# Failed to create the log set. Check whether the log set name already exists.
FAILEDOPERATION_CREATECLSLOGSETFAILED = 'FailedOperation.CreateClsLogSetFailed'

# Failed to create the log topic task. Check whether the log topic name or task name already exists.
FAILEDOPERATION_CREATECLSLOGTOPICTASKFAILED = 'FailedOperation.CreateClsLogTopicTaskFailed'

# Authentication failed while creating a custom push task. Check whether the push address is correct.
FAILEDOPERATION_CREATELOGTOPICTASKAUTHFAILURE = 'FailedOperation.CreateLogTopicTaskAuthFailure'

# The edge client certificate has expired. It is not supported to issue expired certificates for the time being.
FAILEDOPERATION_EDGECLIENTCERTIFICATEHASEXPIRED = 'FailedOperation.EdgeClientCertificateHasExpired'

# Failed to call dnspod. please try again later. if the issue persists, please contact the intelligent customer service or submit a ticket.
FAILEDOPERATION_FAILEDTOCALLDNSPOD = 'FailedOperation.FailedToCallDNSPod'

# Another task is being deployed. Please try again later.
FAILEDOPERATION_FUNCTIONDEPLOYING = 'FailedOperation.FunctionDeploying'

# The account balance is insufficient.
FAILEDOPERATION_INSUFFICIENTACCOUNTBALANCE = 'FailedOperation.InsufficientAccountBalance'

# The site status is invalid.
FAILEDOPERATION_INVALIDZONESTATUS = 'FailedOperation.InvalidZoneStatus'

# The content is missing a mandatory configuration block.
FAILEDOPERATION_MISSINGCONFIGCHUNK = 'FailedOperation.MissingConfigChunk'

# Operation failed.
FAILEDOPERATION_MODIFYFAILED = 'FailedOperation.ModifyFailed'

# The real-time log authentication failed.
FAILEDOPERATION_REALTIMELOGAUTHFAILURE = 'FailedOperation.RealtimeLogAuthFailure'

# The real-time log push task does not exist.
FAILEDOPERATION_REALTIMELOGNOTFOUND = 'FailedOperation.RealtimeLogNotFound'

# Function rule operations conflict under this site.
FAILEDOPERATION_RULEOPERATIONCONFLICT = 'FailedOperation.RuleOperationConflict'

# Unknown configuration group type.
FAILEDOPERATION_UNKNOWNCONFIGGROUPTYPE = 'FailedOperation.UnknownConfigGroupType'

# The client certificate for the origin-pull mutual authentication has expired. It is not supported to issue expired certificates.
FAILEDOPERATION_UPSTREAMCLIENTCERTIFICATEHASEXPIRED = 'FailedOperation.UpstreamClientCertificateHasExpired'

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

# Alias domain names do not support configuring a keyless certificate.
INVALIDPARAMETER_ALIASDOMAINNOTSUPPORTKEYLESS = 'InvalidParameter.AliasDomainNotSupportKeyless'

# Chinese SM certificates are not supported for alias domain names.
INVALIDPARAMETER_ALIASDOMAINNOTSUPPORTSMCERT = 'InvalidParameter.AliasDomainNotSupportSMCert'

# The function content has a syntax error.
INVALIDPARAMETER_BADCONTENT = 'InvalidParameter.BadContent'

# The function name does not meet specifications.
INVALIDPARAMETER_BADFUNCTIONNAME = 'InvalidParameter.BadFunctionName'

# Invalid query string.
INVALIDPARAMETER_CACHEKEYQUERYSTRINGREQUIRESFULLURLCACHEOFF = 'InvalidParameter.CacheKeyQueryStringRequiresFullUrlCacheOff'

# The query string has too many values.
INVALIDPARAMETER_CACHEKEYQUERYSTRINGTOOMANYVALUE = 'InvalidParameter.CacheKeyQueryStringTooManyValue'

# Invalid edge HTTPS certificate configuration. The certificate does not match the domain name.
INVALIDPARAMETER_CERTNOTMATCHDOMAIN = 'InvalidParameter.CertNotMatchDomain'

# Internal error.
INVALIDPARAMETER_CERTSYSTEMERROR = 'InvalidParameter.CertSystemError'

# The edge HTTPS certificate is about to expire.
INVALIDPARAMETER_CERTTOEXPIRE = 'InvalidParameter.CertToExpire'

# Invalid edge HTTPS certificate configuration. The key length does not meet the minimum requirement RSA>=2048, DSA>=2048, DH>=2048, and EC>=225.
INVALIDPARAMETER_CERTTOOSHORTKEYSIZE = 'InvalidParameter.CertTooShortKeySize'

# The domain name to be changed is not bound to a certificate or keyless server. Please bind it first and then proceed.
INVALIDPARAMETER_CERTIFICATECONFLICTWITHKEYLESSSERVER = 'InvalidParameter.CertificateConflictWithKeylessServer'

# IPv6 access conflicts with client IP geographical location.
INVALIDPARAMETER_CLIENTIPCOUNTRYCONFLICTSWITHIPV6 = 'InvalidParameter.ClientIpCountryConflictsWithIpv6'

# Unable to apply for a wildcard certificate under CNAME mode.
INVALIDPARAMETER_CNAMEWILDHOSTNOTALLOWAPPLYCERTIFICATE = 'InvalidParameter.CnameWildHostNotAllowApplyCertificate'

# Invalid compression algorithm.
INVALIDPARAMETER_COMPRESSIONINVALIDALGORITHMS = 'InvalidParameter.CompressionInvalidAlgorithms'

# The origin cannot be the same as the domain name.
INVALIDPARAMETER_CONFLICTHOSTORIGIN = 'InvalidParameter.ConflictHostOrigin'

# The function content exceeds the size limit.
INVALIDPARAMETER_CONTENTEXCEEDSLIMIT = 'InvalidParameter.ContentExceedsLimit'

# The domain name does not exist or is not belong to this account.
INVALIDPARAMETER_DOMAINNOTFOUND = 'InvalidParameter.DomainNotFound'

# Traffic scheduling is already enabled for the current domain name.
INVALIDPARAMETER_DOMAINONTRAFFICSCHEDULING = 'InvalidParameter.DomainOnTrafficScheduling'

# Duplicate rules.
INVALIDPARAMETER_DUPLICATERULE = 'InvalidParameter.DuplicateRule'

# Invalid edge client certificate configuration.
INVALIDPARAMETER_EDGECLIENTCERTCHECKERROR = 'InvalidParameter.EdgeClientCertCheckError'

# The current conditions do not support the requested operation.
INVALIDPARAMETER_ERRACTIONUNSUPPORTTARGET = 'InvalidParameter.ErrActionUnsupportTarget'

# Invalid operation.
INVALIDPARAMETER_ERRINVALIDACTION = 'InvalidParameter.ErrInvalidAction'

# Invalid operation: Duplicate operation configuration.
INVALIDPARAMETER_ERRINVALIDACTIONDUPLICATEACTION = 'InvalidParameter.ErrInvalidActionDuplicateAction'

# Invalid rule engine operation. The origin server IP cannot be a private network IP or loopback address.
INVALIDPARAMETER_ERRINVALIDACTIONORIGINPRIVATEADDRESS = 'InvalidParameter.ErrInvalidActionOriginPrivateAddress'

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

# The operations of modifying the origin server cannot be only to configure host matching type.
INVALIDPARAMETER_ERRINVALIDCONDITIONCANNOTONLYCONTAINHOSTWHENMODIFYORIGINACTIONCONFIGURED = 'InvalidParameter.ErrInvalidConditionCannotOnlyContainHostWhenModifyOriginActionConfigured'

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

# Empty condition.
INVALIDPARAMETER_ERRNILCONDITION = 'InvalidParameter.ErrNilCondition'

# The function name conflicts with that of another function under this account.
INVALIDPARAMETER_FUNCTIONNAMECONFLICT = 'InvalidParameter.FunctionNameConflict'

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

# Invalid token authentication expiration time.
INVALIDPARAMETER_INVALIDAUTHENTICATIONTYPEEXPIRETIME = 'InvalidParameter.InvalidAuthenticationTypeExpireTime'

# Invalid key for token authentication.
INVALIDPARAMETER_INVALIDAUTHENTICATIONTYPESECRETKEY = 'InvalidParameter.InvalidAuthenticationTypeSecretKey'

# Invalid token authentication parameter.
INVALIDPARAMETER_INVALIDAUTHENTICATIONTYPESIGNPARAM = 'InvalidParameter.InvalidAuthenticationTypeSignParam'

# Invalid authentication token format.
INVALIDPARAMETER_INVALIDAUTHENTICATIONTYPETIMEFORMAT = 'InvalidParameter.InvalidAuthenticationTypeTimeFormat'

# Invalid authentication token parameter.
INVALIDPARAMETER_INVALIDAUTHENTICATIONTYPETIMEPARAM = 'InvalidParameter.InvalidAuthenticationTypeTimeParam'

# The format of automatically used vouchers is incorrect. Enter the correct format.
INVALIDPARAMETER_INVALIDAUTOUSEVOUCHER = 'InvalidParameter.InvalidAutoUseVoucher'

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
INVALIDPARAMETER_INVALIDCACHEKEYQUERYSTRINGACTION = 'InvalidParameter.InvalidCacheKeyQueryStringAction'

# Invalid query string.
INVALIDPARAMETER_INVALIDCACHEKEYQUERYSTRINGVALUE = 'InvalidParameter.InvalidCacheKeyQueryStringValue'

# Invalid cache key scheme.
INVALIDPARAMETER_INVALIDCACHEKEYSCHEME = 'InvalidParameter.InvalidCacheKeyScheme'

# Invalid node cache.
INVALIDPARAMETER_INVALIDCACHEONLYONSWITCH = 'InvalidParameter.InvalidCacheOnlyOnSwitch'

# Invalid node cache validity.
INVALIDPARAMETER_INVALIDCACHETIME = 'InvalidParameter.InvalidCacheTime'

# Invalid edge HTTPS certificate information.
INVALIDPARAMETER_INVALIDCERTINFO = 'InvalidParameter.InvalidCertInfo'

# Invalid client IP location configuration. HeaderName consists of 1-100 alphanumeric characters and cannot start or end with hyphens (-).
INVALIDPARAMETER_INVALIDCLIENTIPCOUNTRYHEADERNAME = 'InvalidParameter.InvalidClientIpCountryHeaderName'

# Invalid client IP request header.
INVALIDPARAMETER_INVALIDCLIENTIPHEADERNAME = 'InvalidParameter.InvalidClientIpHeaderName'

# Invalid origin for region-specific origin-pull.
INVALIDPARAMETER_INVALIDCLIENTIPORIGIN = 'InvalidParameter.InvalidClientIpOrigin'

# Invalid conditions.
INVALIDPARAMETER_INVALIDCONDITIONS = 'InvalidParameter.InvalidConditions'

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

# Invalid filter field.
INVALIDPARAMETER_INVALIDFILTERNAME = 'InvalidParameter.InvalidFilterName'

# Invalid forced HTTPS direction settings
INVALIDPARAMETER_INVALIDFORCEREDIRECTTYPE = 'InvalidParameter.InvalidForceRedirectType'

# Invalid parameter "https".
INVALIDPARAMETER_INVALIDHTTPS = 'InvalidParameter.InvalidHttps'

# Invalid edge HTTPS certificate configuration. The certificate content is invalid.
INVALIDPARAMETER_INVALIDHTTPSCERTINFO = 'InvalidParameter.InvalidHttpsCertInfo'

# The cipher suite does not match the TLS version.
INVALIDPARAMETER_INVALIDHTTPSCIPHERSUITEANDTLSVERSION = 'InvalidParameter.InvalidHttpsCipherSuiteAndTlsVersion'

# Invalid HTTPS HSTS.
INVALIDPARAMETER_INVALIDHTTPSHSTSMAXAGE = 'InvalidParameter.InvalidHttpsHstsMaxAge'

# Invalid HTTPS TLS version.
INVALIDPARAMETER_INVALIDHTTPSTLSVERSION = 'InvalidParameter.InvalidHttpsTlsVersion'

# Invalid interval. The value should be either [min 5min hour day].
INVALIDPARAMETER_INVALIDINTERVAL = 'InvalidParameter.InvalidInterval'

# Invalid IPv6 settings.
INVALIDPARAMETER_INVALIDIPV6SWITCH = 'InvalidParameter.InvalidIpv6Switch'

# The field separator in the log output format is incorrect.
INVALIDPARAMETER_INVALIDLOGFORMATFIELDDELIMITER = 'InvalidParameter.InvalidLogFormatFieldDelimiter'

# The log output format type is incorrect.
INVALIDPARAMETER_INVALIDLOGFORMATFORMATTYPE = 'InvalidParameter.InvalidLogFormatFormatType'

# The log record separator in the log output format is incorrect.
INVALIDPARAMETER_INVALIDLOGFORMATRECORDDELIMITER = 'InvalidParameter.InvalidLogFormatRecordDelimiter'

# Invalid browser cache.
INVALIDPARAMETER_INVALIDMAXAGEFOLLOWORIGIN = 'InvalidParameter.InvalidMaxAgeFollowOrigin'

# Invalid browser cache.
INVALIDPARAMETER_INVALIDMAXAGETIME = 'InvalidParameter.InvalidMaxAgeTime'

# The query dimension is invalid.
INVALIDPARAMETER_INVALIDMETRIC = 'InvalidParameter.InvalidMetric'

# Invalid origin server.
INVALIDPARAMETER_INVALIDORIGIN = 'InvalidParameter.InvalidOrigin'

# The origin server group type is incorrect.
INVALIDPARAMETER_INVALIDORIGINGROUPTYPE = 'InvalidParameter.InvalidOriginGroupType'

# The origin cannot be a private IP or loopback address.
INVALIDPARAMETER_INVALIDORIGINIP = 'InvalidParameter.InvalidOriginIp'

# Incorrect origin server type.
INVALIDPARAMETER_INVALIDORIGINTYPE = 'InvalidParameter.InvalidOriginType'

# The origin server is incorrect or inexistent.
INVALIDPARAMETER_INVALIDORIGINVALUE = 'InvalidParameter.InvalidOriginValue'

# Invalid parameter.
INVALIDPARAMETER_INVALIDPARAMETER = 'InvalidParameter.InvalidParameter'

# The plan cycle format is incorrect. Enter the correct format.
INVALIDPARAMETER_INVALIDPERIOD = 'InvalidParameter.InvalidPeriod'

# The plan type format is incorrect. Enter the correct format.
INVALIDPARAMETER_INVALIDPLANTYPE = 'InvalidParameter.InvalidPlanType'

# The speciThe plan does not support limiting the max upload size.
INVALIDPARAMETER_INVALIDPOSTMAXSIZEBILLING = 'InvalidParameter.InvalidPostMaxSizeBilling'

# Invalid POST request size.
INVALIDPARAMETER_INVALIDPOSTSIZEVALUE = 'InvalidParameter.InvalidPostSizeValue'

# AccessKeyId and SecretAccessKey are required to access the third-party object storage.
INVALIDPARAMETER_INVALIDPRIVATEACCESSPARAMS = 'InvalidParameter.InvalidPrivateAccessParams'

# The value of `PrivateAccess` should be `on` or `off`.
INVALIDPARAMETER_INVALIDPRIVATEACCESSSWITCH = 'InvalidParameter.InvalidPrivateAccessSwitch'

# The plan does not support QUIC.
INVALIDPARAMETER_INVALIDQUICBILLING = 'InvalidParameter.InvalidQuicBilling'

# The quota quantity format is incorrect. Enter the correct format.
INVALIDPARAMETER_INVALIDQUOTANUMBER = 'InvalidParameter.InvalidQuotaNumber'

# The quota type format is incorrect. Enter the correct quota type format.
INVALIDPARAMETER_INVALIDQUOTATYPE = 'InvalidParameter.InvalidQuotaType'

# Invalid Range GETs.
INVALIDPARAMETER_INVALIDRANGEORIGINPULL = 'InvalidParameter.InvalidRangeOriginPull'

# The auto-renewal flag format is incorrect. Enter the correct format.
INVALIDPARAMETER_INVALIDRENEWFLAG = 'InvalidParameter.InvalidRenewFlag'

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

# The rule engine configuration is invalid.
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

# Incorrect protocol of the rules. (TCP/UDP).
INVALIDPARAMETER_INVALIDRULEPROTO = 'InvalidParameter.InvalidRuleProto'

# Invalid origin domain.
INVALIDPARAMETER_INVALIDSERVERNAME = 'InvalidParameter.InvalidServerName'

# Invalid debug configuration for EdgeOne.
INVALIDPARAMETER_INVALIDSTANDARDDEBUG = 'InvalidParameter.InvalidStandardDebug'

# Invalid client IP or CIDR block.
INVALIDPARAMETER_INVALIDSTANDARDDEBUGCLIENTIP = 'InvalidParameter.InvalidStandardDebugClientIp'

# The AllowClientIPList parameter is mandatory. The IPv4 and IPv6 network segments are supported. 0.0.0.0/0 indicates that all IPv4 clients can be debugged, and ::/0 indicates that all IPv6 clients can be debugged.
INVALIDPARAMETER_INVALIDSTANDARDDEBUGEMPTYLIST = 'InvalidParameter.InvalidStandardDebugEmptyList'

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

# The Cloud Load Balancer instance ID is required in the operation of modifying the origin server.
INVALIDPARAMETER_LOADBALANCEINSTANCEIDISREQUIRED = 'InvalidParameter.LoadBalanceInstanceIdIsRequired'

# The Layer-4 proxy service referencing a LoadBalancer is being deployed. Please edit later.
INVALIDPARAMETER_LOADBALANCERBINDL4NOTINSTABLESTATUS = 'InvalidParameter.LoadBalancerBindL4NotInStableStatus'

# The Layer-7 domain name service referencing a LoadBalancer is being deployed. Please edit later.
INVALIDPARAMETER_LOADBALANCERBINDL7NOTINSTABLESTATUS = 'InvalidParameter.LoadBalancerBindL7NotInStableStatus'

# The LoadBalancer names under the same site should be unique.
INVALIDPARAMETER_LOADBALANCERNAMEREPEATED = 'InvalidParameter.LoadBalancerNameRepeated'

# The LoadBalancer is referenced by the layer-4 instance and cannot be deleted.
INVALIDPARAMETER_LOADBALANCERUSEDINL4PROXY = 'InvalidParameter.LoadBalancerUsedInL4Proxy'

# The LoadBalancer is referenced by the layer-7 domain name and cannot be deleted.
INVALIDPARAMETER_LOADBALANCERUSEDINL7DOMAIN = 'InvalidParameter.LoadBalancerUsedInL7Domain'

# The LoadBalancer is referenced by the rule engine and cannot be deleted.
INVALIDPARAMETER_LOADBALANCERUSEDINRULEENGINE = 'InvalidParameter.LoadBalancerUsedInRuleEngine'

# Modification parameters are missing.
INVALIDPARAMETER_MODIFYPARAMETERSMISSING = 'InvalidParameter.ModifyParametersMissing'

# Smart routing is not supported.
INVALIDPARAMETER_MULTIPLYLAYERNOTSUPPORTSMARTROUTING = 'InvalidParameter.MultiplyLayerNotSupportSmartRouting'

# Unsupported preset variables exist.
INVALIDPARAMETER_NOTSUPPORTTHISPRESET = 'InvalidParameter.NotSupportThisPreset'

# The domain name is configured to forward requests to the origin directly. iSmart Acceleration must be enabled.
INVALIDPARAMETER_OCDIRECTORIGINREQUIRESSMARTROUTING = 'InvalidParameter.OCDirectOriginRequiresSmartRouting'

# The type of the origin server group does not match the LoadBalancer type.
INVALIDPARAMETER_ORIGINGROUPTYPECANNOTMATCHLBTYPE = 'InvalidParameter.OriginGroupTypeCanNotMatchLBType'

# The origin address cannot be a private IP address.
INVALIDPARAMETER_ORIGINISINNERIP = 'InvalidParameter.OriginIsInnerIp'

# The layer-4 proxy strictly prohibits mixing IPs and domain names.
INVALIDPARAMETER_ORIGINL4RECORDIPV4MIXDOMAIN = 'InvalidParameter.OriginL4RecordIPV4MixDomain'

# Usage of multi-domain origin server is forbidden for layer-4 proxy.
INVALIDPARAMETER_ORIGINL4RECORDMULTIDOMAIN = 'InvalidParameter.OriginL4RecordMultiDomain'

# The origin group name already exists.
INVALIDPARAMETER_ORIGINNAMEEXISTS = 'InvalidParameter.OriginNameExists'

# The origin group ID is required.
INVALIDPARAMETER_ORIGINORIGINGROUPIDISREQUIRED = 'InvalidParameter.OriginOriginGroupIdIsRequired'

# The return protocol is required in the operation of modifying the origin server.
INVALIDPARAMETER_ORIGINPULLPROTOCOLISREQUIRED = 'InvalidParameter.OriginPullProtocolIsRequired'

# Incorrect origin server format. 
INVALIDPARAMETER_ORIGINRECORDFORMATERROR = 'InvalidParameter.OriginRecordFormatError'

# Weight value range: 0-100.
INVALIDPARAMETER_ORIGINRECORDWEIGHTVALUE = 'InvalidParameter.OriginRecordWeightValue'

# The key format is incorrect.
INVALIDPARAMETER_ORIGINTHIRDPARTYPARAMFORMATERROR = 'InvalidParameter.OriginThirdPartyParamFormatError'

# Parameter error: Invalid “End time”. The interval between the start and end time cannot exceed 7 days.
INVALIDPARAMETER_PARAMETERERROR = 'InvalidParameter.ParameterError'

# The plan doesn’t exist.
INVALIDPARAMETER_PLANNOTFOUND = 'InvalidParameter.PlanNotFound'

# Maximum upload size exceeded.
INVALIDPARAMETER_POSTMAXSIZELIMITEXCEEDED = 'InvalidParameter.PostMaxSizeLimitExceeded'

# The instance name already exists.
INVALIDPARAMETER_PROXYNAMEDUPLICATING = 'InvalidParameter.ProxyNameDuplicating'

# Instance name can contain 1 to 50 characters. The allowed characters are a to z, 0 to 9, and -. - cannot be registered alone or used continuously and cannot be placed at the beginning or the end.
INVALIDPARAMETER_PROXYNAMENOTMATCHED = 'InvalidParameter.ProxyNameNotMatched'

# The push instance has been created.
INVALIDPARAMETER_REALTIMELOGENTITYALREADYCREATED = 'InvalidParameter.RealtimeLogEntityAlreadyCreated'

# The log push region is invalid.
INVALIDPARAMETER_REALTIMELOGINVALIDDELIVERYAREA = 'InvalidParameter.RealtimeLogInvalidDeliveryArea'

# The log push type is invalid.
INVALIDPARAMETER_REALTIMELOGINVALIDLOGTYPE = 'InvalidParameter.RealtimeLogInvalidLogType'

# The real-time log delivery type is invalid.
INVALIDPARAMETER_REALTIMELOGINVALIDTASKTYPE = 'InvalidParameter.RealtimeLogInvalidTaskType'

# The real-time log push task data exceeded the limit.
INVALIDPARAMETER_REALTIMELOGNUMSEXCEEDLIMIT = 'InvalidParameter.RealtimeLogNumsExceedLimit'

# Invalid response header.
INVALIDPARAMETER_RESPONSEHEADERCACHECONTROLNOTALLOWDELETE = 'InvalidParameter.ResponseHeaderCacheControlNotAllowDelete'

# Incorrect origin server information format of the rules.
INVALIDPARAMETER_RULEORIGINFORMATERROR = 'InvalidParameter.RuleOriginFormatError'

# The origin of the rule does not support multiple domain names.
INVALIDPARAMETER_RULEORIGINMULTIDOMAIN = 'InvalidParameter.RuleOriginMultiDomain'

# The origin port of the rule must be an integer.
INVALIDPARAMETER_RULEORIGINPORTINTEGER = 'InvalidParameter.RuleOriginPortInteger'

# Invalid origin in the rule.
INVALIDPARAMETER_RULEORIGINVALUEERROR = 'InvalidParameter.RuleOriginValueError'

# The rule port already exists.
INVALIDPARAMETER_RULEPORTDUPLICATING = 'InvalidParameter.RulePortDuplicating'

# Incorrect port number segment of the rules.
INVALIDPARAMETER_RULEPORTGROUP = 'InvalidParameter.RulePortGroup'

# The port number of the rules must be an integer.
INVALIDPARAMETER_RULEPORTINTEGER = 'InvalidParameter.RulePortInteger'

# Invalid parameter.
INVALIDPARAMETER_SECURITY = 'InvalidParameter.Security'

# Configuration parameter error.
INVALIDPARAMETER_SETTINGINVALIDPARAM = 'InvalidParameter.SettingInvalidParam'

# Some bound origin server groups do not exist.
INVALIDPARAMETER_SOMEORIGINGROUPNOTEXIST = 'InvalidParameter.SomeOriginGroupNotExist'

# Shield Space is not bound with an origin. 
INVALIDPARAMETER_SPACENOTBINDORIGIN = 'InvalidParameter.SpaceNotBindOrigin'

# Invalid status code in cache.
INVALIDPARAMETER_STATUSCODECACHEINVALIDSTATUSCODE = 'InvalidParameter.StatusCodeCacheInvalidStatusCode'

# Resource error
INVALIDPARAMETER_TARGET = 'InvalidParameter.Target'

# Failed to create the task
INVALIDPARAMETER_TASKNOTGENERATED = 'InvalidParameter.TaskNotGenerated'

# Internal error.
INVALIDPARAMETER_TASKSYSTEMERROR = 'InvalidParameter.TaskSystemError'

# TLS version is not continuous for HTTPS.
INVALIDPARAMETER_TLSVERSIONNOTINSEQUENCE = 'InvalidParameter.TlsVersionNotInSequence'

# Too many filter values.
INVALIDPARAMETER_TOOMANYFILTERVALUES = 'InvalidParameter.TooManyFilterValues'

# Too many filter items.
INVALIDPARAMETER_TOOMANYFILTERS = 'InvalidParameter.TooManyFilters'

# Invalid file upload link.
INVALIDPARAMETER_UPLOADURL = 'InvalidParameter.UploadUrl'

# Invalid origin-pull client certificate configuration.
INVALIDPARAMETER_UPSTREAMCLIENTCERTCHECKERROR = 'InvalidParameter.UpstreamClientCertCheckError'

# The site is already bound.
INVALIDPARAMETER_ZONEHASBEENBOUND = 'InvalidParameter.ZoneHasBeenBound'

# The zone is not bound to a package.
INVALIDPARAMETER_ZONEHASNOTBEENBOUNDTOPLAN = 'InvalidParameter.ZoneHasNotBeenBoundToPlan'

# The site is being upgraded. Changing is not supported. Please try again later.
INVALIDPARAMETER_ZONEISGRAYPUBLISHING = 'InvalidParameter.ZoneIsGrayPublishing'

# To switch a site from connecting without a domain name to connecting via the CNAME, the site name is required.
INVALIDPARAMETER_ZONENAMEISREQUIRED = 'InvalidParameter.ZoneNameIsRequired'

# The site does not exist.
INVALIDPARAMETER_ZONENOTFOUND = 'InvalidParameter.ZoneNotFound'

# Invalid parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The domain name for this zone has been banned.
INVALIDPARAMETERVALUE_ACCESSBLACKLIST = 'InvalidParameterValue.AccessBlacklist'

# Alias domain names do not support the configuration of edge mutual authentication for the time being.
INVALIDPARAMETERVALUE_ALIASDOMAINNOTSUPPORTEDGEMTLS = 'InvalidParameterValue.AliasDomainNotSupportEdgeMTLS'

# Alias domain names do not support the configuration of origin-pull mutual authentication for the time being.
INVALIDPARAMETERVALUE_ALIASDOMAINNOTSUPPORTUPSTREAMMTLS = 'InvalidParameterValue.AliasDomainNotSupportUpstreamMTLS'

# 
INVALIDPARAMETERVALUE_CERTIFICATEVERIFYCLIENTMUSTCA = 'InvalidParameterValue.CertificateVerifyClientMustCa'

# 
INVALIDPARAMETERVALUE_CERTIFICATEVERIFYCLIENTNEEDCERT = 'InvalidParameterValue.CertificateVerifyClientNeedCert'

# Currently, only RSA or ECC algorithm certificates are supported for the origin-pull mutual authentication, and the SCA SM2 algorithm certificates are not supported.
INVALIDPARAMETERVALUE_CERTIFICATEVERIFYUPSTREAMCLIENTMUSTRSAORECC = 'InvalidParameterValue.CertificateVerifyUpstreamClientMustRSAorECC'

# The certificate type for the origin-pull mutual authentication is incorrect and cannot be configured as a CA certificate.
INVALIDPARAMETERVALUE_CERTIFICATEVERIFYUPSTREAMCLIENTMUSTSVR = 'InvalidParameterValue.CertificateVerifyUpstreamClientMustSVR'

# Origin-pull mutual authentication configuration requires at least one certificate.
INVALIDPARAMETERVALUE_CERTIFICATEVERIFYUPSTREAMCLIENTNEEDCERT = 'InvalidParameterValue.CertificateVerifyUpstreamClientNeedCert'

# 
INVALIDPARAMETERVALUE_CLIENTCERTINFOQUOTALIMIT = 'InvalidParameterValue.ClientCertInfoQuotaLimit'

# It conflicts with existing records.
INVALIDPARAMETERVALUE_CONFLICTRECORD = 'InvalidParameterValue.ConflictRecord'

# DNS records conflict with DNSSEC.
INVALIDPARAMETERVALUE_CONFLICTWITHDNSSEC = 'InvalidParameterValue.ConflictWithDNSSEC'

# The DNS record conflicts with acceleration domain name record.
INVALIDPARAMETERVALUE_CONFLICTWITHDOMAIN = 'InvalidParameterValue.ConflictWithDomain'

# This DNS record conflicts with NS records.
INVALIDPARAMETERVALUE_CONFLICTWITHNSRECORD = 'InvalidParameterValue.ConflictWithNSRecord'

# The host record cannot be the same as the record value.
INVALIDPARAMETERVALUE_CONTENTSAMEASNAME = 'InvalidParameterValue.ContentSameAsName'

# The page content does not match the Content-Type.
INVALIDPARAMETERVALUE_CONTENTTYPENOTMATCH = 'InvalidParameterValue.ContentTypeNotMatch'

# The specified domain name does not match the site. 
INVALIDPARAMETERVALUE_DOMAINNOTMATCHZONE = 'InvalidParameterValue.DomainNotMatchZone'

# Format mismatch.
INVALIDPARAMETERVALUE_FORMATMISMATCH = 'InvalidParameterValue.FormatMismatch'

# Configuration parameter format mismatch.
INVALIDPARAMETERVALUE_GENERALMISMATCH = 'InvalidParameterValue.GeneralMismatch'

# Contains invalid value.
INVALIDPARAMETERVALUE_INCLUDEINVALIDVALUE = 'InvalidParameterValue.IncludeInvalidValue'

# The alias domain name is invalid. It must contain numerics, English characters, and hyphens, but hyphen is not allowed at the beginning or the end.
INVALIDPARAMETERVALUE_INVALIDALIASDOMAINNAME = 'InvalidParameterValue.InvalidAliasDomainName'

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

# Invalid keyless server ID.
INVALIDPARAMETERVALUE_INVALIDKEYLESSSERVERID = 'InvalidParameterValue.InvalidKeylessServerId'

# Incorrect DNS proxy
INVALIDPARAMETERVALUE_INVALIDPROXYORIGIN = 'InvalidParameterValue.InvalidProxyOrigin'

# The tag value contains invalid characters.
INVALIDPARAMETERVALUE_INVALIDTAGVALUE = 'InvalidParameterValue.InvalidTagValue'

# Missing required configuration parameters.
INVALIDPARAMETERVALUE_MISSINGNECESSARYPARAM = 'InvalidParameterValue.MissingNecessaryParam'

# Wildcard domain CNAMEs are not supported.
INVALIDPARAMETERVALUE_NOTALLOWEDWILDCARDSHAREDCNAME = 'InvalidParameterValue.NotAllowedWildcardSharedCNAME'

# The value is not within the required collection.
INVALIDPARAMETERVALUE_NOTINENUMERATION = 'InvalidParameterValue.NotInEnumeration'

# The value is not within the specified range.
INVALIDPARAMETERVALUE_NOTWITHINRANGE = 'InvalidParameterValue.NotWithinRange'

# The specified origin group does not exist.
INVALIDPARAMETERVALUE_ORIGINGROUPNOTEXISTS = 'InvalidParameterValue.OriginGroupNotExists'

# The page name already exists.
INVALIDPARAMETERVALUE_PAGENAMEALREADYEXIST = 'InvalidParameterValue.PageNameAlreadyExist'

# Does not match the specified regular expression.
INVALIDPARAMETERVALUE_REGEXMISMATCH = 'InvalidParameterValue.RegExMismatch'

# Edge mTLS is enabled. When the client uses an RSA or ECC algorithm certificate, the same algorithm certificate should also be configured in the edge HTTPS certificate.
INVALIDPARAMETERVALUE_SERVERCERTINFONEEDCONTAINRSAORECC = 'InvalidParameterValue.ServerCertInfoNeedContainRSAorECC'

# Edge mTLS is enabled. When the client uses a national encryption CA certificate, the national encryption certificate should also be configured in the edge HTTPS certificate.
INVALIDPARAMETERVALUE_SERVERCERTINFONEEDCONTAINSM2 = 'InvalidParameterValue.ServerCertInfoNeedContainSM2'

# Enter a valid shared CNAME prefix of up to 50 characters.
INVALIDPARAMETERVALUE_SHAREDCNAMEPREFIXNOTMATCH = 'InvalidParameterValue.SharedCNAMEPrefixNotMatch'

# The current domain suffix is not supported for access. Please contact us if you need to use it.
INVALIDPARAMETERVALUE_TOPLEVELDOMAINNOTSUPPORT = 'InvalidParameterValue.TopLevelDomainNotSupport'

# Referencing is not allowed on the custom page of the trial plan.
INVALIDPARAMETERVALUE_TRIALPLANRESPONSEPAGE = 'InvalidParameterValue.TrialPlanResponsePage'

# Configuration item error.
INVALIDPARAMETERVALUE_UNRECOGNIZABLEVALUE = 'InvalidParameterValue.UnrecognizableValue'

# One client certificate is allowed at most in the origin-pull mutual authentication configuration.
INVALIDPARAMETERVALUE_UPSTREAMCLIENTCERTINFOQUOTALIMIT = 'InvalidParameterValue.UpstreamClientCertInfoQuotaLimit'

# The zone name format is incorrect. Please input a correctly formed domain name.
INVALIDPARAMETERVALUE_ZONENAMEINVALID = 'InvalidParameterValue.ZoneNameInvalid'

# Punycode access is not supported at present.
INVALIDPARAMETERVALUE_ZONENAMENOTSUPPORTPUNYCODE = 'InvalidParameterValue.ZoneNameNotSupportPunyCode'

# The zone does not support subdomain access. Please use second-level domains for zone access.
INVALIDPARAMETERVALUE_ZONENAMENOTSUPPORTSUBDOMAIN = 'InvalidParameterValue.ZoneNameNotSupportSubDomain'

# The site alias already exists. 
INVALIDPARAMETERVALUE_ZONESAMEASNAME = 'InvalidParameterValue.ZoneSameAsName'

# The quota limit has been reached.
LIMITEXCEEDED = 'LimitExceeded'

# Reached the upper limit of resource number
LIMITEXCEEDED_BATCHQUOTA = 'LimitExceeded.BatchQuota'

# The number of regular expression type fields in real-time log custom fields exceeds the limit.
LIMITEXCEEDED_CUSTOMLOGFIELDREGEXLIMITEXCEEDED = 'LimitExceeded.CustomLogFieldRegexLimitExceeded'

# Reached the daily upper limit of resource number
LIMITEXCEEDED_DAILYQUOTA = 'LimitExceeded.DailyQuota'

# The number of functions has reached the limit.
LIMITEXCEEDED_FUNCTIONLIMITEXCEEDED = 'LimitExceeded.FunctionLimitExceeded'

# The number of LoadBalancers exceeds the limit.
LIMITEXCEEDED_LOADBALANCINGCOUNTLIMITEXCEEDED = 'LimitExceeded.LoadBalancingCountLimitExceeded'

# Not supported by the plan.
LIMITEXCEEDED_PACKNOTALLOW = 'LimitExceeded.PackNotAllow'

# The number of rules imported has exceeded the limit.
LIMITEXCEEDED_PROXYRULESLIMITEXCEEDED = 'LimitExceeded.ProxyRulesLimitExceeded'

# Query time limit exceeded.
LIMITEXCEEDED_QUERYTIMELIMITEXCEEDED = 'LimitExceeded.QueryTimeLimitExceeded'

# Reached the API rate limit.
LIMITEXCEEDED_RATELIMITEXCEEDED = 'LimitExceeded.RateLimitExceeded'

# The number of rules has reached the limit.
LIMITEXCEEDED_RULELIMITEXCEEDED = 'LimitExceeded.RuleLimitExceeded'

# Limit exceeded
LIMITEXCEEDED_SECURITY = 'LimitExceeded.Security'

# User instance quantity limitation.
LIMITEXCEEDED_USERQUOTALIMITED = 'LimitExceeded.UserQuotaLimited'

# Reached the upper limit of sites of the plan
LIMITEXCEEDED_ZONEBINDPLAN = 'LimitExceeded.ZoneBindPlan'

# Missing parameters.
MISSINGPARAMETER = 'MissingParameter'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# Cross-MLC-border acceleration is in beta. To join the beta, submit a ticket.
OPERATIONDENIED_ACCELERATEMAINLANDDISABLE = 'OperationDenied.AccelerateMainlandDisable'

# Cross-MLC-border acceleration and IPv6 cannot be configured at the same time.
OPERATIONDENIED_ACCELERATEMAINLANDIPV6CONFLICT = 'OperationDenied.AccelerateMainlandIpv6Conflict'

# The existing domain feature under the current site conflicts with the Chinese mainland network optimization, and cannot be configured at the same time.
OPERATIONDENIED_ACCELERATEMAINLANDMULTIPLYLAYERCONFLICT = 'OperationDenied.AccelerateMainlandMultiplyLayerConflict'

# An L7 DNS service referencing the origin group is being deployed. Please edit later.
OPERATIONDENIED_ACCELERATIONDOMAINSTATUSNOTINONLINE = 'OperationDenied.AccelerationDomainStatusNotInOnline'

# Currently, only the keyless certificate mode allows the private key of the certificate to be empty.
OPERATIONDENIED_CERTIFICATEPRIVATEKEYISEMPTY = 'OperationDenied.CertificatePrivateKeyIsEmpty'

# The current compliance status is banning.
OPERATIONDENIED_COMPLIANCEFORBIDDEN = 'OperationDenied.ComplianceForbidden'

# The configuration is locked. Please unlock and try again.
OPERATIONDENIED_CONFIGLOCKED = 'OperationDenied.ConfigLocked'

# The TEO_QCSLinkedRoleInDnspodAccessEO role is not authorized. Please authorize it and try again.
OPERATIONDENIED_DNSPODUNAUTHORIZEDROLEOPERATION = 'OperationDenied.DNSPodUnauthorizedRoleOperation'

# The pre-check failed during site deletion.
OPERATIONDENIED_DELETEZONEPRECHECKFAILED = 'OperationDenied.DeleteZonePreCheckFailed'

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

# Some domain names on the site are currently experiencing instability. The stable states for domain names are "online" and "offline".
OPERATIONDENIED_DOMAINSTATUSUNSTABLE = 'OperationDenied.DomainStatusUnstable'

# The Enterprise Edition Plan does not support auto-renewal.
OPERATIONDENIED_ENTERPRISEPLANAUTORENEWUNSUPPORTED = 'OperationDenied.EnterprisePlanAutoRenewUnsupported'

# The Enterprise Edition Plan does not support renewal.
OPERATIONDENIED_ENTERPRISEPLANRENEWUNSUPPORTED = 'OperationDenied.EnterprisePlanRenewUnsupported'

# The Enterprise Edition Plan does not support upgrades.
OPERATIONDENIED_ENTERPRISEPLANUPGRADEUNSUPPORTED = 'OperationDenied.EnterprisePlanUpgradeUnsupported'

# The site environment is not ready.
OPERATIONDENIED_ENVNOTREADY = 'OperationDenied.EnvNotReady'

# The EdgeOne service of the site is disabled. Please enable it and try again.
OPERATIONDENIED_ERRZONEISALREADYPAUSED = 'OperationDenied.ErrZoneIsAlreadyPaused'

# The edge mutual authentication certificates for the domain name to be changed are inconsistent. Please confirm that the domain name certificates are consistent and try again.
OPERATIONDENIED_HOSTSCLIENTCERTIFICATEINCONSISTENCY = 'OperationDenied.HostsClientCertificateInconsistency'

# The keyless server of the domain name to be changed is inconsistent. Please confirm that the keyless server is consistent before retrying.
OPERATIONDENIED_HOSTSKEYLESSSERVERINCONSISTENCY = 'OperationDenied.HostsKeylessServerInconsistency'

# The origin-pull mutual authentication certificates for the domain name to be changed are inconsistent. Please confirm that the domain name certificates are consistent and try again.
OPERATIONDENIED_HOSTSUPSTREAMCERTIFICATEINCONSISTENCY = 'OperationDenied.HostsUpstreamCertificateInconsistency'

# The security service must be enabled when you enable the DDoS Protection.
OPERATIONDENIED_INVALIDADVANCEDDEFENSESECURITYTYPE = 'OperationDenied.InvalidAdvancedDefenseSecurityType'

# The acceleration regions of the site must be in the Chinese mainland when you enable the DDoS Protection.
OPERATIONDENIED_INVALIDADVANCEDDEFENSEZONEAREA = 'OperationDenied.InvalidAdvancedDefenseZoneArea'

# Exclusive DDoS protection conflicts with IPv6. They cannot be configured at the same time.
OPERATIONDENIED_IPV6ADVANCEDCONFLICT = 'OperationDenied.Ipv6AdvancedConflict'

# The IPv6 feature and static IP cannot be enabled at the same time.
OPERATIONDENIED_IPV6STATICIPCONFLICT = 'OperationDenied.Ipv6StaticIpConflict'

# The domain name to be changed has a different certificate or keyless server. Please confirm that the edge HTTPS certificate or keyless server is consistent before retrying.
OPERATIONDENIED_KEYLESSCERTSWITCHTOFREECERTCONFLICT = 'OperationDenied.KeylessCertSwitchToFreeCertConflict'

# The keyless certificate mode requires the private key of the certificate to be empty.
OPERATIONDENIED_KEYLESSMODECERTIFICATEPRIVATEKEYNEEDEMPTY = 'OperationDenied.KeylessModeCertificatePrivateKeyNeedEmpty'

# The layer-4 instance resource sales are skyrocketing and now the resources are sold out. Replenishing is in progress. Currently, new layer-4 proxies cannot be added. Please wait.
OPERATIONDENIED_L4LACKOFRESOURCES = 'OperationDenied.L4LackOfResources'

# The sale of Layer 4 port resources is booming and they have been sold out. We are urgently restocking. At present, it is not possible to add new Layer 4 proxies or rules, and we kindly ask for your patience.
OPERATIONDENIED_L4PORTLACKOFRESOURCES = 'OperationDenied.L4PortLackOfResources'

# Operation failed: The L4 proxy is blocked.
OPERATIONDENIED_L4PROXYINBANNEDSTATUS = 'OperationDenied.L4ProxyInBannedStatus'

# The Layer 4 channel is closed and rule addition is disallowed.
OPERATIONDENIED_L4PROXYINOFFLINESTATUS = 'OperationDenied.L4ProxyInOfflineStatus'

# The instance is currently in deployment and cannot be operated.
OPERATIONDENIED_L4PROXYINPROCESSSTATUS = 'OperationDenied.L4ProxyInProcessStatus'

# The EdgeOne service cannot be disabled for the site: A L4 proxy instance is being deployed.
OPERATIONDENIED_L4PROXYINPROGRESSSTATUS = 'OperationDenied.L4ProxyInProgressStatus'

# Unable to disable the site: There are L4 proxy instances disabled.
OPERATIONDENIED_L4PROXYINSTOPPINGSTATUS = 'OperationDenied.L4ProxyInStoppingStatus'

# Unable to operate the L4 instance when it’s not running
OPERATIONDENIED_L4STATUSNOTINONLINE = 'OperationDenied.L4StatusNotInOnline'

# The EdgeOne service cannot be disabled for the site: An accelerated domain name is being deployed.
OPERATIONDENIED_L7HOSTINPROCESSSTATUS = 'OperationDenied.L7HostInProcessStatus'

# The affiliated Cloud Load Balancer is not in a running state. Operation is forbidden.
OPERATIONDENIED_LOADBALANCESTATUSNOTINONLINE = 'OperationDenied.LoadBalanceStatusNotInOnline'

# The site status does not support operations on load balancers.
OPERATIONDENIED_LOADBALANCINGZONEISNOTACTIVE = 'OperationDenied.LoadBalancingZoneIsNotActive'

# IPv6 cannot be enabled for non-overseas exclusive protection.
OPERATIONDENIED_MSGIPV6ADVANCEDCONFLICT = 'OperationDenied.MsgIpv6AdvancedConflict'

# Unable to switch to NS for multiple sites using CNAME.
OPERATIONDENIED_MULTIPLECNAMEZONE = 'OperationDenied.MultipleCnameZone'

# Domain traffic scheduling is not supported in NS access mode.
OPERATIONDENIED_NSNOTALLOWTRAFFICSTRATEGY = 'OperationDenied.NSNotAllowTrafficStrategy'

# You can only switch a site connected without a domain name to connecting via the CNAME
OPERATIONDENIED_NODOMAINACCESSZONEONLYALLOWMODIFIEDTOCNAME = 'OperationDenied.NoDomainAccessZoneOnlyAllowModifiedToCNAME'

# You can only switch a site connected without a domain name to connecting via the CNAME. Other operations are not allowed.
OPERATIONDENIED_NODOMAINACCESSZONEONLYSUPPORTMODIFYTYPE = 'OperationDenied.NoDomainAccessZoneOnlySupportModifyType'

# Currently, the keyless certificate feature is available only to users in the allowlist.
OPERATIONDENIED_NOTINKEYLESSWHITELIST = 'OperationDenied.NotInKeylessWhiteList'

# The current origin-pull mutual authentication feature is only available to allowlist users.
OPERATIONDENIED_NOTINUPSTREAMMTLSWHITELIST = 'OperationDenied.NotInUpstreamMTLSWhiteList'

# The current user is not included in the whitelist for version management.
OPERATIONDENIED_NOTINVERSIONCONTROLWHITELIST = 'OperationDenied.NotInVersionControlWhiteList'

# Failed to delete: The acceleration domain name is in use. 
OPERATIONDENIED_ORIGINGROUPACCELERATIONDOMAINUSED = 'OperationDenied.OriginGroupAccelerationDomainUsed'

# The Layer 4 proxy is in use and cannot be deleted.
OPERATIONDENIED_ORIGINGROUPL4USED = 'OperationDenied.OriginGroupL4Used'

# The Cloud Load Balancer is in use and cannot be deleted.
OPERATIONDENIED_ORIGINGROUPLBUSED = 'OperationDenied.OriginGroupLBUsed'

# The rule engine is in use and cannot be deleted.
OPERATIONDENIED_ORIGINGROUPRULEENGINEUSED = 'OperationDenied.OriginGroupRuleEngineUsed'

# Ownership verification failed. Please complete the site ownership verification first.
OPERATIONDENIED_OWNERSHIPVERIFICATIONNOTPASSED = 'OperationDenied.OwnershipVerificationNotPassed'

# A plan downgrade is not supported.
OPERATIONDENIED_PLANDOWNGRADENOTALLOWED = 'OperationDenied.PlanDowngradeNotAllowed'

# The plan has expired.
OPERATIONDENIED_PLANHASBEENEXPIRED = 'OperationDenied.PlanHasBeenExpired'

# The plan has been isolated.
OPERATIONDENIED_PLANHASBEENISOLATED = 'OperationDenied.PlanHasBeenIsolated'

# This plan does not support the purchase of additional plan quotas.
OPERATIONDENIED_PLANINCREASEPLANQUOTAUNSUPPORTED = 'OperationDenied.PlanIncreasePlanQuotaUnsupported'

# The specified plan does not support changing the service area of the site.
OPERATIONDENIED_PLANNOTSUPPORTMODIFYZONEAREA = 'OperationDenied.PlanNotSupportModifyZoneArea'

# This site is using Anycast IP scheduling mode and does not support Cross-MLC-border acceleration. 
OPERATIONDENIED_PLATTYPEIPACCELERATEMAINLANDNOTSUPPORT = 'OperationDenied.PlatTypeIPAccelerateMainlandNotSupport'

# To create an Enterprise Edition Plan, contact the business personnel.
OPERATIONDENIED_PLEASECONTACTBUSINESSPERSONNEL = 'OperationDenied.PleaseContactBusinessPersonnel'

# The DNS record cannot be added.
OPERATIONDENIED_RECORDISFORBIDDEN = 'OperationDenied.RecordIsForbidden'

# Billing resources are in operation. Try again later.
OPERATIONDENIED_RESOURCEHASBEENLOCKED = 'OperationDenied.ResourceHasBeenLocked'

# This operation conflicts with concurrent operations. Try again later.
OPERATIONDENIED_RESOURCELOCKEDTEMPORARY = 'OperationDenied.ResourceLockedTemporary'

# The domain name is bound with a shared CNAME and cannot be changed to "Cross-MLC-border acceleration". Please unbind the domain name from the shared CNAME first.
OPERATIONDENIED_SHAREDCNAMEUNSUPPORTEDACCELERATEMAINLAND = 'OperationDenied.SharedCNAMEUnsupportedAccelerateMainland'

# The domain name is bound with a shared CNAME and cannot be changed to "IPv6 access". Please unbind the domain name from the shared CNAME first.
OPERATIONDENIED_SHAREDCNAMEUNSUPPORTEDIPV6 = 'OperationDenied.SharedCNAMEUnsupportedIPv6'

# The static IP cannot be enabled for this instance's region.
OPERATIONDENIED_STATICIPAREACONFLICT = 'OperationDenied.StaticIpAreaConflict'

# Disabling the origin-pull mutual authentication is not supported now. To disable it, please change the edge HTTPS certificate configuration to 'none'.
OPERATIONDENIED_UNSUPPORTTOCLOSEUPSTREAMMTLS = 'OperationDenied.UnSupportToCloseUpstreamMTLS'

# To enable the origin-pull mutual authentication, please configure the edge HTTPS certificate first.
OPERATIONDENIED_USEUPSTREAMMTLSNEEDOPENHTTPS = 'OperationDenied.UseUpstreamMTLSNeedOpenHttps'

# There is a test version in use. Please release the test version to the live environment, or roll back the test version and try again.
OPERATIONDENIED_VERSIONCONTROLISGRAYING = 'OperationDenied.VersionControlIsGraying'

# The operation is not allowed because the version management mode is applied.
OPERATIONDENIED_VERSIONCONTROLLOCKED = 'OperationDenied.VersionControlLocked'

# The specified site working mode is not applicable to the version management mode.
OPERATIONDENIED_WORKMODENOTINVERSIONCONTROL = 'OperationDenied.WorkModeNotInVersionControl'

# The shared CNAME has been bound to another site. Please unbind first.
OPERATIONDENIED_ZONEISBINDINGSHAREDCNAME = 'OperationDenied.ZoneIsBindingSharedCNAME'

# Error found in the associated custom error page. Please unbind it first.
OPERATIONDENIED_ZONEISREFERENCECUSTOMERRORPAGE = 'OperationDenied.ZoneIsReferenceCustomErrorPage'

# The zone is disabled.
OPERATIONDENIED_ZONENOTACTIVE = 'OperationDenied.ZoneNotActive'

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

# The domain name is not properly accessed via DNSPod. Please try again after DNSPod access.
RESOURCENOTFOUND_DNSPODDOMAINNOTINACCOUNT = 'ResourceNotFound.DNSPodDomainNotInAccount'

# Maximum upload size is not configured.
RESOURCENOTFOUND_POSTMAXSIZEQUOTANOTFOUND = 'ResourceNotFound.PostMaxSizeQuotaNotFound'

# The configuration group version does not exist. Please check and try again.
RESOURCENOTFOUND_VERSIONNOTFOUND = 'ResourceNotFound.VersionNotFound'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# The certificate does not exist or is not authorized.
RESOURCEUNAVAILABLE_CERTNOTFOUND = 'ResourceUnavailable.CertNotFound'

# The domain name is already connected to EdgeOne by another account. Please retrieve it first in order to add it.
RESOURCEUNAVAILABLE_DOMAINALREADYEXISTS = 'ResourceUnavailable.DomainAlreadyExists'

# The requested accelerated domain name doesn’t exist. 
RESOURCEUNAVAILABLE_DOMAINNOTFOUND = 'ResourceUnavailable.DomainNotFound'

# The function does not exist or does not belong to this account.
RESOURCEUNAVAILABLE_FUNCTIONNOTFOUND = 'ResourceUnavailable.FunctionNotFound'

# The domain name does not exist or not use a proxy.
RESOURCEUNAVAILABLE_HOSTNOTFOUND = 'ResourceUnavailable.HostNotFound'

# The rule does not exist or does not belong to the account.
RESOURCEUNAVAILABLE_RULENOTFOUND = 'ResourceUnavailable.RuleNotFound'

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
