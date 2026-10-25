# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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


# DryRun operation means the request will be successful, but the DryRun parameter is passed.
DRYRUNOPERATION = 'DryRunOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# The edge HTTPS certificate has expired. Issuing expired certificates is currently not supported.
FAILEDOPERATION_CERTIFICATEHASEXPIRED = 'FailedOperation.CertificateHasExpired'

# The edge HTTPS certificate does not exist.
FAILEDOPERATION_CERTIFICATENOTFOUND = 'FailedOperation.CertificateNotFound'

# Syntax error in the Condition expression in the configuration file.
FAILEDOPERATION_CONFIGCONDITIONSYNTAXERROR = 'FailedOperation.ConfigConditionSyntaxError'

# Unrecognized Condition match type.
FAILEDOPERATION_CONFIGCONDITIONUNKNOWNTARGET = 'FailedOperation.ConfigConditionUnknownTarget'

# The Condition expression value in the configuration file cannot be empty.
FAILEDOPERATION_CONFIGCONDITIONVALUEEMPTYERROR = 'FailedOperation.ConfigConditionValueEmptyError'

# Duplicate keywords are not allowed in the configuration file.
FAILEDOPERATION_CONFIGDUPLICATEKEYERROR = 'FailedOperation.ConfigDuplicateKeyError'

# The config file contains a field with a type mismatch.
FAILEDOPERATION_CONFIGFIELDTYPEERROR = 'FailedOperation.ConfigFieldTypeError'

# Syntax error in the configuration file.
FAILEDOPERATION_CONFIGFORMATERROR = 'FailedOperation.ConfigFormatError'

# Version management configuration file JSON format error.
FAILEDOPERATION_CONFIGJSONFORMATERROR = 'FailedOperation.ConfigJSONFormatError'

# Configuration file content format error. Unable to resolve.
FAILEDOPERATION_CONFIGMALFORMEDCONTENT = 'FailedOperation.ConfigMalformedContent'

# Configuration file parameter validation error.
FAILEDOPERATION_CONFIGPARAMVALIDATEERRORS = 'FailedOperation.ConfigParamValidateErrors'

# Time format parsing error.
FAILEDOPERATION_CONFIGTIMEPARSINGERROR = 'FailedOperation.ConfigTimeParsingError'

# Unrecognized field in the configuration file: spelling error or the level where the field is located is incorrect.
FAILEDOPERATION_CONFIGUNKNOWNFIELD = 'FailedOperation.ConfigUnknownField'

# Unsupported configuration item Action
FAILEDOPERATION_CONFIGUNSUPPORTEDACTION = 'FailedOperation.ConfigUnsupportedAction'

# Configuration file version not supported currently.
FAILEDOPERATION_CONFIGUNSUPPORTEDFORMATVERSION = 'FailedOperation.ConfigUnsupportedFormatVersion'

# Failed to create the log set. Check if the log set name already exists.
FAILEDOPERATION_CREATECLSLOGSETFAILED = 'FailedOperation.CreateClsLogSetFailed'

# Failed to create the log topic task. Check whether the log topic name or task name already exists.
FAILEDOPERATION_CREATECLSLOGTOPICTASKFAILED = 'FailedOperation.CreateClsLogTopicTaskFailed'

# Authentication failed while creating a custom push task. Check whether the push address is correct.
FAILEDOPERATION_CREATELOGTOPICTASKAUTHFAILURE = 'FailedOperation.CreateLogTopicTaskAuthFailure'

# Failed to create the preheated origin-pull rate limiting configuration. Try again later or submit a ticket.
FAILEDOPERATION_CREATEPREFETCHORIGINLIMITFAILED = 'FailedOperation.CreatePrefetchOriginLimitFailed'

# The edge client certificate has expired. It is not supported to issue expired certificates for the time being.
FAILEDOPERATION_EDGECLIENTCERTIFICATEHASEXPIRED = 'FailedOperation.EdgeClientCertificateHasExpired'

# Failed to call DNSPod. Please try again later. If the problem persists, submit a ticket.
FAILEDOPERATION_FAILEDTOCALLDNSPOD = 'FailedOperation.FailedToCallDNSPod'

# Another task is being deployed. Please try again later.
FAILEDOPERATION_FUNCTIONDEPLOYING = 'FailedOperation.FunctionDeploying'

# The account balance is insufficient.
FAILEDOPERATION_INSUFFICIENTACCOUNTBALANCE = 'FailedOperation.InsufficientAccountBalance'

# Site status incorrect.
FAILEDOPERATION_INVALIDZONESTATUS = 'FailedOperation.InvalidZoneStatus'

# The content lacks the required configuration block.
FAILEDOPERATION_MISSINGCONFIGCHUNK = 'FailedOperation.MissingConfigChunk'

# Operation failed.
FAILEDOPERATION_MODIFYFAILED = 'FailedOperation.ModifyFailed'

# Exceeded the quantity limit. Unable to create more. Delete unnecessary configurations or submit a request to elevate the quantity limit.
FAILEDOPERATION_PREFETCHORIGINLIMITCOUNTEXCEEDED = 'FailedOperation.PrefetchOriginLimitCountExceeded'

# The corresponding preheated origin-pull rate limiting configuration was not found. Please confirm whether the configuration exists and try again.
FAILEDOPERATION_PREFETCHORIGINLIMITNOTFOUND = 'FailedOperation.PrefetchOriginLimitNotFound'

# The product will already be discontinued. Operation denied.
FAILEDOPERATION_PRODUCTDISCONTINUED = 'FailedOperation.ProductDiscontinued'

# No. Enable this product and try again.
FAILEDOPERATION_PRODUCTNOTACTIVATED = 'FailedOperation.ProductNotActivated'

# Real-time log authentication fail
FAILEDOPERATION_REALTIMELOGAUTHFAILURE = 'FailedOperation.RealtimeLogAuthFailure'

# Currently, creation of real-time log push tasks for EdgeOne log analytics is not supported.
FAILEDOPERATION_REALTIMELOGLOGANALYSISNOTSUPPORT = 'FailedOperation.RealtimeLogLogAnalysisNotSupport'

# The real-time log push task does not exist.
FAILEDOPERATION_REALTIMELOGNOTFOUND = 'FailedOperation.RealtimeLogNotFound'

# Function rule operations conflict under this site.
FAILEDOPERATION_RULEOPERATIONCONFLICT = 'FailedOperation.RuleOperationConflict'

# The number of templates under this site exceeds the maximum quantity limit.
FAILEDOPERATION_TEMPLATEOVERLIMIT = 'FailedOperation.TemplateOverLimit'

# Unknown configuration group type.
FAILEDOPERATION_UNKNOWNCONFIGGROUPTYPE = 'FailedOperation.UnknownConfigGroupType'

# The client certificate for the origin-pull mutual authentication has expired. It is not supported to issue expired certificates.
FAILEDOPERATION_UPSTREAMCLIENTCERTIFICATEHASEXPIRED = 'FailedOperation.UpstreamClientCertificateHasExpired'

# The origin CA certificate has expired. Issuing expired certificates is currently not supported.
FAILEDOPERATION_UPSTREAMVERIFYCUSTOMCACERTIFICATEHASEXPIRED = 'FailedOperation.UpstreamVerifyCustomCACertificateHasExpired'

# Internal error.
INTERNALERROR = 'InternalError'

# Error in background processing.
INTERNALERROR_BACKENDERROR = 'InternalError.BackendError'

# The configuration has been locked. Unlock it and retry.
INTERNALERROR_CONFIGLOCKED = 'InternalError.ConfigLocked'

# Database error.
INTERNALERROR_DBERROR = 'InternalError.DBError'

# Failed to get configuration.
INTERNALERROR_DOMAINCONFIG = 'InternalError.DomainConfig'

# Failed to generate the upload URL.
INTERNALERROR_FAILEDTOGENERATEURL = 'InternalError.FailedToGenerateUrl'

# Failed to obtain role.
INTERNALERROR_GETROLEERROR = 'InternalError.GetRoleError'

# Unknown error occurs on the real server.
INTERNALERROR_PROXYSERVER = 'InternalError.ProxyServer'

# Quota system processing failure.
INTERNALERROR_QUOTASYSTEM = 'InternalError.QuotaSystem'

# Backend service routing address error.
INTERNALERROR_ROUTEERROR = 'InternalError.RouteError'

# Internal error. System error.
INTERNALERROR_SYSTEMERROR = 'InternalError.SystemError'

# Unknown error.
INTERNALERROR_UNKNOWERROR = 'InternalError.UnknowError'

# Invalid Filter
INVALIDFILTER = 'InvalidFilter'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# Regular expression is in non-standard RE2 format.
INVALIDPARAMETER_ACCESSREDIRECTREGEXERROR = 'InvalidParameter.AccessRedirectRegexError'

# Operations are too frequent. Please try again later.
INVALIDPARAMETER_ACTIONINPROGRESS = 'InvalidParameter.ActionInProgress'

# The current domain name does not support enabling advanced origin optimization and network optimization in the Chinese mainland (international acceleration) simultaneously.
INVALIDPARAMETER_ADVANCEDORIGINROUTINGNOTSUPPORTACCELERATEMAINLAND = 'InvalidParameter.AdvancedOriginRoutingNotSupportAccelerateMainland'

# The source IP whitelist package for the current domain name does not support advanced origin optimization.
INVALIDPARAMETER_ADVANCEDORIGINROUTINGNOTSUPPORTCURRENTPLANORIGINWHITELIST = 'InvalidParameter.AdvancedOriginRoutingNotSupportCurrentPlanOriginWhitelist'

# The current domain name does not support enabling advanced origin optimization and multi-layer architecture simultaneously.
INVALIDPARAMETER_ADVANCEDORIGINROUTINGNOTSUPPORTMULTIPLYLAYER = 'InvalidParameter.AdvancedOriginRoutingNotSupportMultiplyLayer'

# The current domain name does not support enabling advanced origin optimization and OC switching simultaneously.
INVALIDPARAMETER_ADVANCEDORIGINROUTINGNOTSUPPORTOCDIRECTORIGIN = 'InvalidParameter.AdvancedOriginRoutingNotSupportOCDirectOrigin'

# Unsupported to enable advanced origin optimization and racing platform simultaneously.
INVALIDPARAMETER_ADVANCEDORIGINROUTINGNOTSUPPORTRACINGPLATFORM = 'InvalidParameter.AdvancedOriginRoutingNotSupportRacingPlatform'

# Alias domain names do not support configuring a keyless certificate.
INVALIDPARAMETER_ALIASDOMAINNOTSUPPORTKEYLESS = 'InvalidParameter.AliasDomainNotSupportKeyless'

# Alias domain names do not support configuring an SM certificate.
INVALIDPARAMETER_ALIASDOMAINNOTSUPPORTSMCERT = 'InvalidParameter.AliasDomainNotSupportSMCert'

# The function content has a syntax error.
INVALIDPARAMETER_BADCONTENT = 'InvalidParameter.BadContent'

# The function name does not meet specifications.
INVALIDPARAMETER_BADFUNCTIONNAME = 'InvalidParameter.BadFunctionName'

# Invalid namespace name.
INVALIDPARAMETER_BADNAMESPACENAME = 'InvalidParameter.BadNamespaceName'

# Bind variable not found.
INVALIDPARAMETER_BINDINGNOTFOUND = 'InvalidParameter.BindingNotFound'

# Invalid query string.
INVALIDPARAMETER_CACHEKEYQUERYSTRINGREQUIRESFULLURLCACHEOFF = 'InvalidParameter.CacheKeyQueryStringRequiresFullUrlCacheOff'

# Query string rule exceeds the limit.
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

# IPv6 access conflicts with the Client IP Geolocation feature.
INVALIDPARAMETER_CLIENTIPCOUNTRYCONFLICTSWITHIPV6 = 'InvalidParameter.ClientIpCountryConflictsWithIpv6'

# A wildcard domain name certificate cannot be applied for in CNAME mode.
INVALIDPARAMETER_CNAMEWILDHOSTNOTALLOWAPPLYCERTIFICATE = 'InvalidParameter.CnameWildHostNotAllowApplyCertificate'

# Invalid compression algorithm.
INVALIDPARAMETER_COMPRESSIONINVALIDALGORITHMS = 'InvalidParameter.CompressionInvalidAlgorithms'

# The origin server cannot be the same as the domain name.
INVALIDPARAMETER_CONFLICTHOSTORIGIN = 'InvalidParameter.ConflictHostOrigin'

# The function content exceeds the size limit.
INVALIDPARAMETER_CONTENTEXCEEDSLIMIT = 'InvalidParameter.ContentExceedsLimit'

# Domain Acceleration Region: the preheated origin-pull rate limiting region configuration is not supported. Adjust it and resubmit.
INVALIDPARAMETER_DOMAINAREANOTSUPPORTPREFETCHORIGINLIMITAREA = 'InvalidParameter.DomainAreaNotSupportPrefetchOriginLimitArea'

# The domain name does not exist or does not belong to this account.
INVALIDPARAMETER_DOMAINNOTFOUND = 'InvalidParameter.DomainNotFound'

# Traffic scheduling is enabled for the current domain.
INVALIDPARAMETER_DOMAINONTRAFFICSCHEDULING = 'InvalidParameter.DomainOnTrafficScheduling'

# Bind variable name already exists.
INVALIDPARAMETER_DUPLICATEBINDINGNAME = 'InvalidParameter.DuplicateBindingName'

# Duplicate rules.
INVALIDPARAMETER_DUPLICATERULE = 'InvalidParameter.DuplicateRule'

# Invalid edge client certificate configuration.
INVALIDPARAMETER_EDGECLIENTCERTCHECKERROR = 'InvalidParameter.EdgeClientCertCheckError'

# The operation does not support conditions.
INVALIDPARAMETER_ERRACTIONUNSUPPORTTARGET = 'InvalidParameter.ErrActionUnsupportTarget'

# Unauthorized operation.
INVALIDPARAMETER_ERRINVALIDACTION = 'InvalidParameter.ErrInvalidAction'

# Unauthorized operations - duplicate operation configuration.
INVALIDPARAMETER_ERRINVALIDACTIONDUPLICATEACTION = 'InvalidParameter.ErrInvalidActionDuplicateAction'

# Invalid rule engine operation. The origin server IP does not support private IP addresses or loopback addresses.
INVALIDPARAMETER_ERRINVALIDACTIONORIGINPRIVATEADDRESS = 'InvalidParameter.ErrInvalidActionOriginPrivateAddress'

# Unauthorized operations - Illegal parameters.
INVALIDPARAMETER_ERRINVALIDACTIONPARAM = 'InvalidParameter.ErrInvalidActionParam'

# Unauthorized operations - Illegal parameters - Invalid action.
INVALIDPARAMETER_ERRINVALIDACTIONPARAMACTION = 'InvalidParameter.ErrInvalidActionParamAction'

# Unauthorized operations - Illegal parameters - Invalid parameter value type.
INVALIDPARAMETER_ERRINVALIDACTIONPARAMBADVALUETYPE = 'InvalidParameter.ErrInvalidActionParamBadValueType'

# Unauthorized operations - illegal parameters - duplicate parameter name.
INVALIDPARAMETER_ERRINVALIDACTIONPARAMDUPLICATENAME = 'InvalidParameter.ErrInvalidActionParamDuplicateName'

# Unauthorized operations - illegal parameters - invalid parameter value type.
INVALIDPARAMETER_ERRINVALIDACTIONPARAMNAME = 'InvalidParameter.ErrInvalidActionParamName'

# Illegal operation - Illegal parameter - Number of parameter values exceeds the limit.
INVALIDPARAMETER_ERRINVALIDACTIONPARAMTOOMANYVALUES = 'InvalidParameter.ErrInvalidActionParamTooManyValues'

# Unauthorized operations - Illegal parameters - Invalid parameter value.
INVALIDPARAMETER_ERRINVALIDACTIONPARAMVALUE = 'InvalidParameter.ErrInvalidActionParamValue'

# Unauthorized operation - illegal type.
INVALIDPARAMETER_ERRINVALIDACTIONTYPE = 'InvalidParameter.ErrInvalidActionType'

# Invalid condition.
INVALIDPARAMETER_ERRINVALIDCONDITION = 'InvalidParameter.ErrInvalidCondition'

# Operation of modifying the origin server cannot only configure host match type.
INVALIDPARAMETER_ERRINVALIDCONDITIONCANNOTONLYCONTAINHOSTWHENMODIFYORIGINACTIONCONFIGURED = 'InvalidParameter.ErrInvalidConditionCannotOnlyContainHostWhenModifyOriginActionConfigured'

# The operation of modifying the origin server only supports configuring one host match type.
INVALIDPARAMETER_ERRINVALIDCONDITIONHOSTTOOMANYWHENMODIFYORIGINACTIONCONFIGURED = 'InvalidParameter.ErrInvalidConditionHostTooManyWhenModifyOriginActionConfigured'

# Invalid condition - illegal ignore case.
INVALIDPARAMETER_ERRINVALIDCONDITIONIGNORECASE = 'InvalidParameter.ErrInvalidConditionIgnoreCase'

# Invalid condition - Illegal parameter name - Invalid parameter name.
INVALIDPARAMETER_ERRINVALIDCONDITIONNAMEBADNAME = 'InvalidParameter.ErrInvalidConditionNameBadName'

# Invalid condition - Invalid parameter name - The match type does not support the parameter name.
INVALIDPARAMETER_ERRINVALIDCONDITIONNAMETARGETNOTSUPPORTNAME = 'InvalidParameter.ErrInvalidConditionNameTargetNotSupportName'

# Invalid condition - Illegal parameter value - Invalid regular expression.
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUEBADREGULAR = 'InvalidParameter.ErrInvalidConditionValueBadRegular'

# Invalid condition - Illegal parameter value - Invalid url.
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUEBADURL = 'InvalidParameter.ErrInvalidConditionValueBadUrl'

# Invalid condition - Illegal parameter value - Invalid parameter value.
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUEBADVALUE = 'InvalidParameter.ErrInvalidConditionValueBadValue'

# Invalid condition - illegal parameter value - invalid parameter value - file name should not include a file suffix.
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUEBADVALUECONTAINFILENAMEEXTENSION = 'InvalidParameter.ErrInvalidConditionValueBadValueContainFileNameExtension'

# Invalid condition - illegal parameter value - parameter value length exceeds the limit.
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUETOOLONGVALUE = 'InvalidParameter.ErrInvalidConditionValueTooLongValue'

# Invalid condition - illegal parameter value - the number of regular expressions exceeds the limit.
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUETOOMANYREGULAR = 'InvalidParameter.ErrInvalidConditionValueTooManyRegular'

# Invalid condition - illegal parameter value - the number of parameter values exceeds the limit.
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUETOOMANYVALUES = 'InvalidParameter.ErrInvalidConditionValueTooManyValues'

# Invalid condition - illegal parameter value - the number of wildcards exceeds the limit.
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUETOOMANYWILDCARD = 'InvalidParameter.ErrInvalidConditionValueTooManyWildcard'

# Invalid condition - Illegal parameter value - Number of parameter values is 0.
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUEZEROLENGTH = 'InvalidParameter.ErrInvalidConditionValueZeroLength'

# The operation of modifying the origin server does not support ELSE.
INVALIDPARAMETER_ERRINVALIDELSEWHENMODIFYORIGINACTIONCONFIGURED = 'InvalidParameter.ErrInvalidElseWhenModifyOriginActionConfigured'

# Condition is empty.
INVALIDPARAMETER_ERRNILCONDITION = 'InvalidParameter.ErrNilCondition'

# The binding name already exists. To overwrite, please use bind-override.
INVALIDPARAMETER_FUNCTIONBINDVARIABLENAMECONFLICT = 'InvalidParameter.FunctionBindVariableNameConflict'

# The function name conflicts with that of another function under this account.
INVALIDPARAMETER_FUNCTIONNAMECONFLICT = 'InvalidParameter.FunctionNameConflict'

# The number of GroupBy parameters exceeds the limit.
INVALIDPARAMETER_GROUPBYLIMITEXCEEDED = 'InvalidParameter.GroupByLimitExceeded'

# Enabling Grpc protocol support requires enabling HTTP/2 protocol support simultaneously.
INVALIDPARAMETER_GRPCREQUIREHTTP2 = 'InvalidParameter.GrpcRequireHttp2'

# Origin-pull Host error.
INVALIDPARAMETER_HOSTHEADERINVALID = 'InvalidParameter.HostHeaderInvalid'

# The domain name does not exist.
INVALIDPARAMETER_HOSTNOTFOUND = 'InvalidParameter.HostNotFound'

# CNAME not switched or origin not routed to the EO server.
INVALIDPARAMETER_HOSTSTATUSNOTALLOWAPPLYCERTIFICATE = 'InvalidParameter.HostStatusNotAllowApplyCertificate'

# Parameter error.
INVALIDPARAMETER_INVALIDACCELERATETYPE = 'InvalidParameter.InvalidAccelerateType'

# The set match condition does not support advanced origin optimization. Delete the configuration.
INVALIDPARAMETER_INVALIDADVANCEDORIGINROUTINGUNSUPPORTED = 'InvalidParameter.InvalidAdvancedOriginRoutingUnsupported'

# Invalid token authentication.
INVALIDPARAMETER_INVALIDAUTHENTICATION = 'InvalidParameter.InvalidAuthentication'

# Invalid token authentication expiration time.
INVALIDPARAMETER_INVALIDAUTHENTICATIONTYPEEXPIRETIME = 'InvalidParameter.InvalidAuthenticationTypeExpireTime'

# Invalid token authentication key.
INVALIDPARAMETER_INVALIDAUTHENTICATIONTYPESECRETKEY = 'InvalidParameter.InvalidAuthenticationTypeSecretKey'

# Invalid token authentication parameter.
INVALIDPARAMETER_INVALIDAUTHENTICATIONTYPESIGNPARAM = 'InvalidParameter.InvalidAuthenticationTypeSignParam'

# Invalid token authentication time format.
INVALIDPARAMETER_INVALIDAUTHENTICATIONTYPETIMEFORMAT = 'InvalidParameter.InvalidAuthenticationTypeTimeFormat'

# Invalid token authentication time parameter.
INVALIDPARAMETER_INVALIDAUTHENTICATIONTYPETIMEPARAM = 'InvalidParameter.InvalidAuthenticationTypeTimeParam'

# The format of automatically used vouchers is incorrect. Enter the correct format.
INVALIDPARAMETER_INVALIDAUTOUSEVOUCHER = 'InvalidParameter.InvalidAutoUseVoucher'

# Invalid third-party object storage.
INVALIDPARAMETER_INVALIDAWSPRIVATEACCESS = 'InvalidParameter.InvalidAwsPrivateAccess'

# Fill in the region correctly as a private network access parameter for third-party object storage.
INVALIDPARAMETER_INVALIDAWSREGION = 'InvalidParameter.InvalidAwsRegion'

# Invalid third-party object storage.
INVALIDPARAMETER_INVALIDAWSSECRETKEY = 'InvalidParameter.InvalidAwsSecretKey'

# Invalid backup origin-pull Host.
INVALIDPARAMETER_INVALIDBACKUPSERVERNAME = 'InvalidParameter.InvalidBackupServerName'

# Invalid node cache.
INVALIDPARAMETER_INVALIDCACHECONFIGCACHE = 'InvalidParameter.InvalidCacheConfigCache'

# Invalid node cache. Follow the origin site behavior.
INVALIDPARAMETER_INVALIDCACHECONFIGFOLLOWORIGIN = 'InvalidParameter.InvalidCacheConfigFollowOrigin'

# Invalid cache key.
INVALIDPARAMETER_INVALIDCACHEKEY = 'InvalidParameter.InvalidCacheKey'

# Invalid custom Cache Key Cookie.
INVALIDPARAMETER_INVALIDCACHEKEYCOOKIE = 'InvalidParameter.InvalidCacheKeyCookie'

# Invalid cache key. Ignore case.
INVALIDPARAMETER_INVALIDCACHEKEYIGNORECASE = 'InvalidParameter.InvalidCacheKeyIgnoreCase'

# Invalid query string.
INVALIDPARAMETER_INVALIDCACHEKEYQUERYSTRINGACTION = 'InvalidParameter.InvalidCacheKeyQueryStringAction'

# Invalid query string.
INVALIDPARAMETER_INVALIDCACHEKEYQUERYSTRINGVALUE = 'InvalidParameter.InvalidCacheKeyQueryStringValue'

# Invalid custom Cache Key Scheme.
INVALIDPARAMETER_INVALIDCACHEKEYSCHEME = 'InvalidParameter.InvalidCacheKeyScheme'

# Invalid node cache.
INVALIDPARAMETER_INVALIDCACHEONLYONSWITCH = 'InvalidParameter.InvalidCacheOnlyOnSwitch'

# Invalid node cache time.
INVALIDPARAMETER_INVALIDCACHETIME = 'InvalidParameter.InvalidCacheTime'

# Invalid edge HTTPS certificate information.
INVALIDPARAMETER_INVALIDCERTINFO = 'InvalidParameter.InvalidCertInfo'

# Invalid client IP location configuration. HeaderName consists of 1-100 letters or digits and cannot start or end with "-".
INVALIDPARAMETER_INVALIDCLIENTIPCOUNTRYHEADERNAME = 'InvalidParameter.InvalidClientIpCountryHeaderName'

# Invalid client IP request header.
INVALIDPARAMETER_INVALIDCLIENTIPHEADERNAME = 'InvalidParameter.InvalidClientIpHeaderName'

# Invalid origin server for subregional origin-pull.
INVALIDPARAMETER_INVALIDCLIENTIPORIGIN = 'InvalidParameter.InvalidClientIpOrigin'

# Invalid condition.
INVALIDPARAMETER_INVALIDCONDITIONS = 'InvalidParameter.InvalidConditions'

# Invalid origin-pull configuration. When the origin server type is COS, the origin server address must be a COS domain name.
INVALIDPARAMETER_INVALIDCOSDOMAIN = 'InvalidParameter.InvalidCosDomain'

# Invalid domain name. Check input parameters for non-existent domain names.
INVALIDPARAMETER_INVALIDDOMAINS = 'InvalidParameter.InvalidDomains'

# Invalid smart acceleration.
INVALIDPARAMETER_INVALIDDYNAMICROUTINE = 'InvalidParameter.InvalidDynamicRoutine'

# The package does not support intelligent acceleration configuration.
INVALIDPARAMETER_INVALIDDYNAMICROUTINEBILLING = 'InvalidParameter.InvalidDynamicRoutineBilling'

# Invalid custom error page.
INVALIDPARAMETER_INVALIDERRORPAGE = 'InvalidParameter.InvalidErrorPage'

# Invalid custom error page.
INVALIDPARAMETER_INVALIDERRORPAGEREDIRECTURL = 'InvalidParameter.InvalidErrorPageRedirectUrl'

# Invalid filter field.
INVALIDPARAMETER_INVALIDFILTERNAME = 'InvalidParameter.InvalidFilterName'

# Invalid forced HTTPS redirect.
INVALIDPARAMETER_INVALIDFORCEREDIRECTTYPE = 'InvalidParameter.InvalidForceRedirectType'

# Invalid HTTPS.
INVALIDPARAMETER_INVALIDHTTPS = 'InvalidParameter.InvalidHttps'

# Invalid edge HTTPS certificate configuration. The certificate content is invalid.
INVALIDPARAMETER_INVALIDHTTPSCERTINFO = 'InvalidParameter.InvalidHttpsCertInfo'

# Encryption suite and TLS version mismatch.
INVALIDPARAMETER_INVALIDHTTPSCIPHERSUITEANDTLSVERSION = 'InvalidParameter.InvalidHttpsCipherSuiteAndTlsVersion'

# Invalid HTTPS HSTS.
INVALIDPARAMETER_INVALIDHTTPSHSTSMAXAGE = 'InvalidParameter.InvalidHttpsHstsMaxAge'

# Invalid HTTPS TLS version.
INVALIDPARAMETER_INVALIDHTTPSTLSVERSION = 'InvalidParameter.InvalidHttpsTlsVersion'

# Invalid interval. The value should be [min 5min hour day].
INVALIDPARAMETER_INVALIDINTERVAL = 'InvalidParameter.InvalidInterval'

# Invalid Ipv6 switch configuration.
INVALIDPARAMETER_INVALIDIPV6SWITCH = 'InvalidParameter.InvalidIpv6Switch'

# Invalid log analysis match condition. Query statement parsing failed.
INVALIDPARAMETER_INVALIDLOGANALYSISCONDITION = 'InvalidParameter.InvalidLogAnalysisCondition'

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

# Invalid query dimension.
INVALIDPARAMETER_INVALIDMETRIC = 'InvalidParameter.InvalidMetric'

# Invalid operation type.
INVALIDPARAMETER_INVALIDOPERATION = 'InvalidParameter.InvalidOperation'

# Invalid origin server.
INVALIDPARAMETER_INVALIDORIGIN = 'InvalidParameter.InvalidOrigin'

# Origin server group type error.
INVALIDPARAMETER_INVALIDORIGINGROUPTYPE = 'InvalidParameter.InvalidOriginGroupType'

# Private IP addresses or loopback addresses are not supported as the origin server address.
INVALIDPARAMETER_INVALIDORIGINIP = 'InvalidParameter.InvalidOriginIp'

# Origin server type error.
INVALIDPARAMETER_INVALIDORIGINTYPE = 'InvalidParameter.InvalidOriginType'

# Origin server error or does not exist.
INVALIDPARAMETER_INVALIDORIGINVALUE = 'InvalidParameter.InvalidOriginValue'

# Parameter error.
INVALIDPARAMETER_INVALIDPARAMETER = 'InvalidParameter.InvalidParameter'

# The plan cycle format is incorrect. Enter the correct format.
INVALIDPARAMETER_INVALIDPERIOD = 'InvalidParameter.InvalidPeriod'

# The plan type format is incorrect. Enter the correct format.
INVALIDPARAMETER_INVALIDPLANTYPE = 'InvalidParameter.InvalidPlanType'

# Maximum upload size is not supported for packages.
INVALIDPARAMETER_INVALIDPOSTMAXSIZEBILLING = 'InvalidParameter.InvalidPostMaxSizeBilling'

# Invalid maximum upload size.
INVALIDPARAMETER_INVALIDPOSTSIZEVALUE = 'InvalidParameter.InvalidPostSizeValue'

# Fill in AccessKeyId and SecretAccessKey as private network access parameters for third-party object storage.
INVALIDPARAMETER_INVALIDPRIVATEACCESSPARAMS = 'InvalidParameter.InvalidPrivateAccessParams'

# Specify the PrivateAccess parameter value as on/off.
INVALIDPARAMETER_INVALIDPRIVATEACCESSSWITCH = 'InvalidParameter.InvalidPrivateAccessSwitch'

# Invalid Layer 4 proxy. Check whether a non-existing proxy is passed in the input parameters.
INVALIDPARAMETER_INVALIDPROXIES = 'InvalidParameter.InvalidProxies'

# The package does not support Quic configuration.
INVALIDPARAMETER_INVALIDQUICBILLING = 'InvalidParameter.InvalidQuicBilling'

# The quota quantity format is incorrect. Enter the correct format.
INVALIDPARAMETER_INVALIDQUOTANUMBER = 'InvalidParameter.InvalidQuotaNumber'

# The quota type format is incorrect. Enter the correct quota type format.
INVALIDPARAMETER_INVALIDQUOTATYPE = 'InvalidParameter.InvalidQuotaType'

# Invalid range-based origin pull.
INVALIDPARAMETER_INVALIDRANGEORIGINPULL = 'InvalidParameter.InvalidRangeOriginPull'

# The auto-renewal flag format is incorrect. Enter the correct format.
INVALIDPARAMETER_INVALIDRENEWFLAG = 'InvalidParameter.InvalidRenewFlag'

# Invalid request header.
INVALIDPARAMETER_INVALIDREQUESTHEADERNAME = 'InvalidParameter.InvalidRequestHeaderName'

# Invalid x-forwarded-for request header configuration
INVALIDPARAMETER_INVALIDREQUESTHEADERNAMEXFF = 'InvalidParameter.InvalidRequestHeaderNameXff'

# Invalid request header.
INVALIDPARAMETER_INVALIDREQUESTHEADERVALUE = 'InvalidParameter.InvalidRequestHeaderValue'

# No package bundle.
INVALIDPARAMETER_INVALIDRESOURCEIDBILLING = 'InvalidParameter.InvalidResourceIdBilling'

# Invalid response header.
INVALIDPARAMETER_INVALIDRESPONSEHEADERNAME = 'InvalidParameter.InvalidResponseHeaderName'

# Invalid response header.
INVALIDPARAMETER_INVALIDRESPONSEHEADERVALUE = 'InvalidParameter.InvalidResponseHeaderValue'

# Invalid rule engine configuration.
INVALIDPARAMETER_INVALIDRULEENGINE = 'InvalidParameter.InvalidRuleEngine'

# Invalid rule engine operation.
INVALIDPARAMETER_INVALIDRULEENGINEACTION = 'InvalidParameter.InvalidRuleEngineAction'

# Rule does not exist.
INVALIDPARAMETER_INVALIDRULEENGINENOTFOUND = 'InvalidParameter.InvalidRuleEngineNotFound'

# Invalid rule engine condition.
INVALIDPARAMETER_INVALIDRULEENGINETARGET = 'InvalidParameter.InvalidRuleEngineTarget'

# Invalid rule engine file suffix condition.
INVALIDPARAMETER_INVALIDRULEENGINETARGETSEXTENSION = 'InvalidParameter.InvalidRuleEngineTargetsExtension'

# Invalid rule engine URL condition.
INVALIDPARAMETER_INVALIDRULEENGINETARGETSURL = 'InvalidParameter.InvalidRuleEngineTargetsUrl'

# Rule protocol error. (TCP/UDP).
INVALIDPARAMETER_INVALIDRULEPROTO = 'InvalidParameter.InvalidRuleProto'

# Invalid origin-pull Host.
INVALIDPARAMETER_INVALIDSERVERNAME = 'InvalidParameter.InvalidServerName'

# The set match condition does not support EdgeOne Shield operations. Delete the configuration.
INVALIDPARAMETER_INVALIDSHIELDUNSUPPORTED = 'InvalidParameter.InvalidShieldUnsupported'

# The sorting field is invalid.
INVALIDPARAMETER_INVALIDSORTBY = 'InvalidParameter.InvalidSortBy'

# Invalid sorting order.
INVALIDPARAMETER_INVALIDSORTORDER = 'InvalidParameter.InvalidSortOrder'

# The edgeone debug configuration is invalid.
INVALIDPARAMETER_INVALIDSTANDARDDEBUG = 'InvalidParameter.InvalidStandardDebug'

# Invalid client ip or ip range.
INVALIDPARAMETER_INVALIDSTANDARDDEBUGCLIENTIP = 'InvalidParameter.InvalidStandardDebugClientIp'

# AllowClientIPList parameter required. Supports IPv4 and IPv6 CIDR blocks. 0.0.0.0/0 indicates permission for all IPv4 client-side debugging, and ::/0 indicates permission for all IPv6 client-side debugging.
INVALIDPARAMETER_INVALIDSTANDARDDEBUGEMPTYLIST = 'InvalidParameter.InvalidStandardDebugEmptyList'

# The valid period exceeds the limit.
INVALIDPARAMETER_INVALIDSTANDARDDEBUGEXPIRETIMELIMIT = 'InvalidParameter.InvalidStandardDebugExpireTimeLimit'

# Invalid origin-pull request parameter setting - invalid query string value.
INVALIDPARAMETER_INVALIDUPSTREAMREQUESTQUERYSTRINGVALUE = 'InvalidParameter.InvalidUpstreamRequestQueryStringValue'

# Invalid URL rewrite.
INVALIDPARAMETER_INVALIDURLREDIRECT = 'InvalidParameter.InvalidUrlRedirect'

# The target HOST for URL rewrite is invalid.
INVALIDPARAMETER_INVALIDURLREDIRECTHOST = 'InvalidParameter.InvalidUrlRedirectHost'

# Invalid target URL for URL rewrite.
INVALIDPARAMETER_INVALIDURLREDIRECTURL = 'InvalidParameter.InvalidUrlRedirectUrl'

# Invalid WebSocket.
INVALIDPARAMETER_INVALIDWEBSOCKETTIMEOUT = 'InvalidParameter.InvalidWebSocketTimeout'

# Invalid cache key.
INVALIDPARAMETER_KEYRULESINVALIDQUERYSTRINGVALUE = 'InvalidParameter.KeyRulesInvalidQueryStringValue'

# The number of keys in the request exceeds the limit.
INVALIDPARAMETER_KEYSTOOMANY = 'InvalidParameter.KeysTooMany'

# The parameter length exceeds the limit.
INVALIDPARAMETER_LENGTHEXCEEDSLIMIT = 'InvalidParameter.LengthExceedsLimit'

# Load balancing instance Id is required in the operation of modifying the origin server.
INVALIDPARAMETER_LOADBALANCEINSTANCEIDISREQUIRED = 'InvalidParameter.LoadBalanceInstanceIdIsRequired'

# The Layer-4 proxy service referencing a LoadBalancer is being deployed. Please edit later.
INVALIDPARAMETER_LOADBALANCERBINDL4NOTINSTABLESTATUS = 'InvalidParameter.LoadBalancerBindL4NotInStableStatus'

# The Layer-7 domain name service referencing a LoadBalancer is being deployed. Please edit later.
INVALIDPARAMETER_LOADBALANCERBINDL7NOTINSTABLESTATUS = 'InvalidParameter.LoadBalancerBindL7NotInStableStatus'

# The origin server group bound to the load balancer is invalid.
INVALIDPARAMETER_LOADBALANCERBINDORIGINGROUPINVALID = 'InvalidParameter.LoadBalancerBindOriginGroupInvalid'

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

# Smart routing unsupported
INVALIDPARAMETER_MULTIPLYLAYERNOTSUPPORTSMARTROUTING = 'InvalidParameter.MultiplyLayerNotSupportSmartRouting'

# Namespace is currently in use and cannot be deleted.
INVALIDPARAMETER_NAMESPACEINUSE = 'InvalidParameter.NamespaceInUse'

# The operation configuration contains unsupported preset variables.
INVALIDPARAMETER_NOTSUPPORTTHISPRESET = 'InvalidParameter.NotSupportThisPreset'

# The domain name is in a direct origin architecture, so smart acceleration must remain enabled.
INVALIDPARAMETER_OCDIRECTORIGINREQUIRESSMARTROUTING = 'InvalidParameter.OCDirectOriginRequiresSmartRouting'

# The type of the origin server group does not match the LoadBalancer type.
INVALIDPARAMETER_ORIGINGROUPTYPECANNOTMATCHLBTYPE = 'InvalidParameter.OriginGroupTypeCanNotMatchLBType'

# The origin server uses a private IP.
INVALIDPARAMETER_ORIGINISINNERIP = 'InvalidParameter.OriginIsInnerIp'

# Layer-4 proxy prohibits mixing IPs and domain names.
INVALIDPARAMETER_ORIGINL4RECORDIPV4MIXDOMAIN = 'InvalidParameter.OriginL4RecordIPV4MixDomain'

# Layer 4 proxy prohibits multi-domain name origin server.
INVALIDPARAMETER_ORIGINL4RECORDMULTIDOMAIN = 'InvalidParameter.OriginL4RecordMultiDomain'

# Origin server group name already exists.
INVALIDPARAMETER_ORIGINNAMEEXISTS = 'InvalidParameter.OriginNameExists'

# Origin server group Id is required in the operation of modifying the origin server.
INVALIDPARAMETER_ORIGINORIGINGROUPIDISREQUIRED = 'InvalidParameter.OriginOriginGroupIdIsRequired'

# Return protocol is required when modifying the origin server.
INVALIDPARAMETER_ORIGINPULLPROTOCOLISREQUIRED = 'InvalidParameter.OriginPullProtocolIsRequired'

# Origin server format error.
INVALIDPARAMETER_ORIGINRECORDFORMATERROR = 'InvalidParameter.OriginRecordFormatError'

# Weight value range: 0-100.
INVALIDPARAMETER_ORIGINRECORDWEIGHTVALUE = 'InvalidParameter.OriginRecordWeightValue'

# Invalid key format.
INVALIDPARAMETER_ORIGINTHIRDPARTYPARAMFORMATERROR = 'InvalidParameter.OriginThirdPartyParamFormatError'

# Parameter error: invalid "end time", not in the allowed query range: [start time, start + 7 days]
INVALIDPARAMETER_PARAMETERERROR = 'InvalidParameter.ParameterError'

# The package does not exist.
INVALIDPARAMETER_PLANNOTFOUND = 'InvalidParameter.PlanNotFound'

# Maximum upload size exceeds limit
INVALIDPARAMETER_POSTMAXSIZELIMITEXCEEDED = 'InvalidParameter.PostMaxSizeLimitExceeded'

# The preheated origin-pull rate limiting region parameter is invalid. Adjust the region and resubmit.
INVALIDPARAMETER_PREFETCHORIGINLIMITAREAINVALID = 'InvalidParameter.PrefetchOriginLimitAreaInvalid'

# The preheated origin-pull rate limiting bandwidth value is too large. Adjust it and resubmit.
INVALIDPARAMETER_PREFETCHORIGINLIMITBANDWIDTHTOOLARGE = 'InvalidParameter.PrefetchOriginLimitBandwidthTooLarge'

# The preheated origin-pull rate limiting bandwidth value is too low. Adjust it and resubmit.
INVALIDPARAMETER_PREFETCHORIGINLIMITBANDWIDTHTOOSMALL = 'InvalidParameter.PrefetchOriginLimitBandwidthTooSmall'

# The preheated origin-pull rate limiting control switch parameter is invalid. Adjust the region and resubmit.
INVALIDPARAMETER_PREFETCHORIGINLIMITENABLEDINVALID = 'InvalidParameter.PrefetchOriginLimitEnabledInvalid'

# Instance name duplicated.
INVALIDPARAMETER_PROXYNAMEDUPLICATING = 'InvalidParameter.ProxyNameDuplicating'

# Instance name can contain 1-50 characters. Allowed characters are a-z, 0-9, and -. Hyphens cannot be registered alone or used continuously, and cannot be placed at the beginning or the end.
INVALIDPARAMETER_PROXYNAMENOTMATCHED = 'InvalidParameter.ProxyNameNotMatched'

# Instance push has been created.
INVALIDPARAMETER_REALTIMELOGENTITYALREADYCREATED = 'InvalidParameter.RealtimeLogEntityAlreadyCreated'

# Log push region is invalid
INVALIDPARAMETER_REALTIMELOGINVALIDDELIVERYAREA = 'InvalidParameter.RealtimeLogInvalidDeliveryArea'

# Invalid log push type
INVALIDPARAMETER_REALTIMELOGINVALIDLOGTYPE = 'InvalidParameter.RealtimeLogInvalidLogType'

# Real-time log delivery type is invalid
INVALIDPARAMETER_REALTIMELOGINVALIDTASKTYPE = 'InvalidParameter.RealtimeLogInvalidTaskType'

# Real-time log push task data exceeds the limit.
INVALIDPARAMETER_REALTIMELOGNUMSEXCEEDLIMIT = 'InvalidParameter.RealtimeLogNumsExceedLimit'

# Namespace remark information is too long.
INVALIDPARAMETER_REMARKTOOLONG = 'InvalidParameter.RemarkTooLong'

# Invalid response header.
INVALIDPARAMETER_RESPONSEHEADERCACHECONTROLNOTALLOWDELETE = 'InvalidParameter.ResponseHeaderCacheControlNotAllowDelete'

# Rule origin server information format error.
INVALIDPARAMETER_RULEORIGINFORMATERROR = 'InvalidParameter.RuleOriginFormatError'

# The rule source does not support multiple domains.
INVALIDPARAMETER_RULEORIGINMULTIDOMAIN = 'InvalidParameter.RuleOriginMultiDomain'

# Rule origin server port must be an integer.
INVALIDPARAMETER_RULEORIGINPORTINTEGER = 'InvalidParameter.RuleOriginPortInteger'

# Rule origin site error.
INVALIDPARAMETER_RULEORIGINVALUEERROR = 'InvalidParameter.RuleOriginValueError'

# Rule port duplication.
INVALIDPARAMETER_RULEPORTDUPLICATING = 'InvalidParameter.RulePortDuplicating'

# Rule port range error.
INVALIDPARAMETER_RULEPORTGROUP = 'InvalidParameter.RulePortGroup'

# Rule port must be an integer.
INVALIDPARAMETER_RULEPORTINTEGER = 'InvalidParameter.RulePortInteger'

# Parameter error.
INVALIDPARAMETER_SECURITY = 'InvalidParameter.Security'

# Configuration item parameter error.
INVALIDPARAMETER_SETTINGINVALIDPARAM = 'InvalidParameter.SettingInvalidParam'

# The current domain name does not support enabling EdgeOne Shield and cache pre-refresh simultaneously.
INVALIDPARAMETER_SHIELDNOTSUPPORTHOSTCACHEPREFRESH = 'InvalidParameter.ShieldNotSupportHostCachePrefresh'

# The current domain name does not support enabling EdgeOne Shield and origin protection simultaneously.
INVALIDPARAMETER_SHIELDNOTSUPPORTHOSTORIGINWHITELIST = 'InvalidParameter.ShieldNotSupportHostOriginWhitelist'

# The current domain name does not support enabling EdgeOne Shield and smart acceleration simultaneously.
INVALIDPARAMETER_SHIELDNOTSUPPORTHOSTSMARTROUTING = 'InvalidParameter.ShieldNotSupportHostSmartRouting'

# The current site does not support enabling EdgeOne Shield and cache pre-refresh simultaneously.
INVALIDPARAMETER_SHIELDNOTSUPPORTZONECACHEPREFRESH = 'InvalidParameter.ShieldNotSupportZoneCachePrefresh'

# The current site does not support enabling EdgeOne Shield and smart acceleration simultaneously.
INVALIDPARAMETER_SHIELDNOTSUPPORTZONESMARTROUTING = 'InvalidParameter.ShieldNotSupportZoneSmartRouting'

# EdgeOne Shield space not found.
INVALIDPARAMETER_SHIELDSPACENOTFOUND = 'InvalidParameter.ShieldSpaceNotFound'

# EdgeOne Shield space parameter required.
INVALIDPARAMETER_SHIELDSPACEREQUIREDERROR = 'InvalidParameter.ShieldSpaceRequiredError'

# EdgeOne Shield space status must be online.
INVALIDPARAMETER_SHIELDSPACESTATUSMUSTONLINE = 'InvalidParameter.ShieldSpaceStatusMustOnline'

# Some bound origin server groups do not exist.
INVALIDPARAMETER_SOMEORIGINGROUPNOTEXIST = 'InvalidParameter.SomeOriginGroupNotExist'

# Shield Space is not bound to an origin server. Please bind an origin server first and try again.
INVALIDPARAMETER_SPACENOTBINDORIGIN = 'InvalidParameter.SpaceNotBindOrigin'

# The status code in the status code cache is invalid.
INVALIDPARAMETER_STATUSCODECACHEINVALIDSTATUSCODE = 'InvalidParameter.StatusCodeCacheInvalidStatusCode'

# The resource has an error.
INVALIDPARAMETER_TARGET = 'InvalidParameter.Target'

# Task unable to generate.
INVALIDPARAMETER_TASKNOTGENERATED = 'InvalidParameter.TaskNotGenerated'

# Internal error.
INVALIDPARAMETER_TASKSYSTEMERROR = 'InvalidParameter.TaskSystemError'

# The HTTPS TLS version is not continuous.
INVALIDPARAMETER_TLSVERSIONNOTINSEQUENCE = 'InvalidParameter.TlsVersionNotInSequence'

# Too many filter values.
INVALIDPARAMETER_TOOMANYFILTERVALUES = 'InvalidParameter.TooManyFilterValues'

# Too many filter items.
INVALIDPARAMETER_TOOMANYFILTERS = 'InvalidParameter.TooManyFilters'

# The file upload link has an issue.
INVALIDPARAMETER_UPLOADURL = 'InvalidParameter.UploadUrl'

# Invalid origin-pull client certificate configuration.
INVALIDPARAMETER_UPSTREAMCLIENTCERTCHECKERROR = 'InvalidParameter.UpstreamClientCertCheckError'

# Invalid origin certificate verification configuration.
INVALIDPARAMETER_UPSTREAMVERIFYCERTCHECKERROR = 'InvalidParameter.UpstreamVerifyCertCheckError'

# Invalid origin certificate verification configuration. The certificate content is empty.
INVALIDPARAMETER_UPSTREAMVERIFYCUSTOMCACERTNOINFO = 'InvalidParameter.UpstreamVerifyCustomCACertNoInfo'

# Site working mode not updated
INVALIDPARAMETER_WORKMODEISSAME = 'InvalidParameter.WorkModeIsSame'

# Site acceleration region: preheating origin-pull rate limiting is not supported for this regional configuration. Adjust it and resubmit.
INVALIDPARAMETER_ZONEAREANOTSUPPORTPREFETCHORIGINLIMITAREA = 'InvalidParameter.ZoneAreaNotSupportPrefetchOriginLimitArea'

# Site has been bound.
INVALIDPARAMETER_ZONEHASBEENBOUND = 'InvalidParameter.ZoneHasBeenBound'

# Zone not bound to package.
INVALIDPARAMETER_ZONEHASNOTBEENBOUNDTOPLAN = 'InvalidParameter.ZoneHasNotBeenBoundToPlan'

# Site is upgrading. Changes are not currently supported. Try again later.
INVALIDPARAMETER_ZONEISGRAYPUBLISHING = 'InvalidParameter.ZoneIsGrayPublishing'

# The site name is required when switching a domainless access site to the CNAME access type.
INVALIDPARAMETER_ZONENAMEISREQUIRED = 'InvalidParameter.ZoneNameIsRequired'

# The site does not exist.
INVALIDPARAMETER_ZONENOTFOUND = 'InvalidParameter.ZoneNotFound'

# Parameter value error.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The site domain name is disabled.
INVALIDPARAMETERVALUE_ACCESSBLACKLIST = 'InvalidParameterValue.AccessBlacklist'

# Alias domain names do not support the configuration of edge mutual authentication for the time being.
INVALIDPARAMETERVALUE_ALIASDOMAINNOTSUPPORTEDGEMTLS = 'InvalidParameterValue.AliasDomainNotSupportEdgeMTLS'

# Alias domain names do not support the configuration of origin-pull mutual authentication for the time being.
INVALIDPARAMETERVALUE_ALIASDOMAINNOTSUPPORTUPSTREAMMTLS = 'InvalidParameterValue.AliasDomainNotSupportUpstreamMTLS'

# Alias domain names do not support the configuration of origin certificate verification for the time being.
INVALIDPARAMETERVALUE_ALIASDOMAINNOTSUPPORTUPSTREAMVERIFY = 'InvalidParameterValue.AliasDomainNotSupportUpstreamVerify'

# The client certificate in the edge mutual authentication configuration must be a CA certificate.
INVALIDPARAMETERVALUE_CERTIFICATEVERIFYCLIENTMUSTCA = 'InvalidParameterValue.CertificateVerifyClientMustCa'

# Edge mutual authentication configuration requires at least one certificate.
INVALIDPARAMETERVALUE_CERTIFICATEVERIFYCLIENTNEEDCERT = 'InvalidParameterValue.CertificateVerifyClientNeedCert'

# Currently, only RSA or ECC algorithm certificates are supported for the origin-pull mutual authentication, and the SCA SM2 algorithm certificates are not supported.
INVALIDPARAMETERVALUE_CERTIFICATEVERIFYUPSTREAMCLIENTMUSTRSAORECC = 'InvalidParameterValue.CertificateVerifyUpstreamClientMustRSAorECC'

# The certificate type for the origin-pull mutual authentication is incorrect and cannot be configured as a CA certificate.
INVALIDPARAMETERVALUE_CERTIFICATEVERIFYUPSTREAMCLIENTMUSTSVR = 'InvalidParameterValue.CertificateVerifyUpstreamClientMustSVR'

# Origin-pull mutual authentication configuration requires at least one certificate.
INVALIDPARAMETERVALUE_CERTIFICATEVERIFYUPSTREAMCLIENTNEEDCERT = 'InvalidParameterValue.CertificateVerifyUpstreamClientNeedCert'

# The certificate type for origin certificate verification is incorrect. Only CA certificates are supported.
INVALIDPARAMETERVALUE_CERTIFICATEVERIFYUPSTREAMVERIFYCUSTOMCAMUSTCA = 'InvalidParameterValue.CertificateVerifyUpstreamVerifyCustomCAMustCA'

# Currently, only RSA or ECC algorithm certificates are supported for origin certificate verification, and SCA SM2 algorithm certificates are not supported.
INVALIDPARAMETERVALUE_CERTIFICATEVERIFYUPSTREAMVERIFYCUSTOMCAMUSTRSAORECC = 'InvalidParameterValue.CertificateVerifyUpstreamVerifyCustomCAMustRSAorECC'

# Origin certificate verification configuration requires at least one certificate.
INVALIDPARAMETERVALUE_CERTIFICATEVERIFYUPSTREAMVERIFYCUSTOMCANEEDCERT = 'InvalidParameterValue.CertificateVerifyUpstreamVerifyCustomCANeedCert'

# A maximum of 20 client CA certificates can be configured in the edge mutual authentication configuration.
INVALIDPARAMETERVALUE_CLIENTCERTINFOQUOTALIMIT = 'InvalidParameterValue.ClientCertInfoQuotaLimit'

# Conflicts with an added record.
INVALIDPARAMETERVALUE_CONFLICTRECORD = 'InvalidParameterValue.ConflictRecord'

# The DNS record conflicts with the DNSSEC feature.
INVALIDPARAMETERVALUE_CONFLICTWITHDNSSEC = 'InvalidParameterValue.ConflictWithDNSSEC'

# The DNS record conflicts with acceleration domain name record.
INVALIDPARAMETERVALUE_CONFLICTWITHDOMAIN = 'InvalidParameterValue.ConflictWithDomain'

# The DNS record conflicts with the NS record.
INVALIDPARAMETERVALUE_CONFLICTWITHNSRECORD = 'InvalidParameterValue.ConflictWithNSRecord'

# Host record and record value cannot have the same value.
INVALIDPARAMETERVALUE_CONTENTSAMEASNAME = 'InvalidParameterValue.ContentSameAsName'

# The page content does not match the Content-Type.
INVALIDPARAMETERVALUE_CONTENTTYPENOTMATCH = 'InvalidParameterValue.ContentTypeNotMatch'

# The domain name in the input parameters does not match the site parameter. Correct it and try again.
INVALIDPARAMETERVALUE_DOMAINNOTMATCHZONE = 'InvalidParameterValue.DomainNotMatchZone'

# When specifying the DimensionName parameter, the Filters field must contain filter criteria corresponding to DimensionName.
INVALIDPARAMETERVALUE_FILTERSMUSTINCLUDEDIMENSIONNAME = 'InvalidParameterValue.FiltersMustIncludeDimensionName'

# Format mismatch.
INVALIDPARAMETERVALUE_FORMATMISMATCH = 'InvalidParameterValue.FormatMismatch'

# Configuration parameter format mismatch.
INVALIDPARAMETERVALUE_GENERALMISMATCH = 'InvalidParameterValue.GeneralMismatch'

# Contains invalid value.
INVALIDPARAMETERVALUE_INCLUDEINVALIDVALUE = 'InvalidParameterValue.IncludeInvalidValue'

# Invalid inference service name format.
INVALIDPARAMETERVALUE_INFERENCESERVICENAME = 'InvalidParameterValue.InferenceServiceName'

# Duplicated inference service name.
INVALIDPARAMETERVALUE_INFERENCESERVICENAMEDUPLICATE = 'InvalidParameterValue.InferenceServiceNameDuplicate'

# Alias domain name is invalid. It can only contain digits, letters, and hyphens, and cannot begin or end with a hyphen.
INVALIDPARAMETERVALUE_INVALIDALIASDOMAINNAME = 'InvalidParameterValue.InvalidAliasDomainName'

# Invalid alias domain suffix (that domain name is for internal usage and not supported as an alias domain name).
INVALIDPARAMETERVALUE_INVALIDALIASNAMESUFFIX = 'InvalidParameterValue.InvalidAliasNameSuffix'

# DNS record content error.
INVALIDPARAMETERVALUE_INVALIDDNSCONTENT = 'InvalidParameterValue.InvalidDNSContent'

# DNS record name error.
INVALIDPARAMETERVALUE_INVALIDDNSNAME = 'InvalidParameterValue.InvalidDNSName'

# Invalid acceleration domain name. It can contain digits, letters (a-z and A-Z), and hyphens, but hyphens are not allowed at the beginning or end.
INVALIDPARAMETERVALUE_INVALIDDOMAINNAME = 'InvalidParameterValue.InvalidDomainName'

# Accelerated domain name status does not meet requirements.
INVALIDPARAMETERVALUE_INVALIDDOMAINSTATUS = 'InvalidParameterValue.InvalidDomainStatus'

# Invalid keyless server ID.
INVALIDPARAMETERVALUE_INVALIDKEYLESSSERVERID = 'InvalidParameterValue.InvalidKeylessServerId'

# DNS proxy domain name origin site error.
INVALIDPARAMETERVALUE_INVALIDPROXYORIGIN = 'InvalidParameterValue.InvalidProxyOrigin'

# A source station fault migration configuration item is configured under an unsupported match condition. Delete the configuration.
INVALIDPARAMETERVALUE_INVALIDSITEFAILOVERUNSUPPORTED = 'InvalidParameterValue.InvalidSiteFailoverUnsupported'

# Tag value contains invalid characters.
INVALIDPARAMETERVALUE_INVALIDTAGVALUE = 'InvalidParameterValue.InvalidTagValue'

# Missing required configuration parameters.
INVALIDPARAMETERVALUE_MISSINGNECESSARYPARAM = 'InvalidParameterValue.MissingNecessaryParam'

# No support for accessing wildcard domain CNAME
INVALIDPARAMETERVALUE_NOTALLOWEDWILDCARDSHAREDCNAME = 'InvalidParameterValue.NotAllowedWildcardSharedCNAME'

# The value is not within the required collection.
INVALIDPARAMETERVALUE_NOTINENUMERATION = 'InvalidParameterValue.NotInEnumeration'

# The value is not within the specified range.
INVALIDPARAMETERVALUE_NOTWITHINRANGE = 'InvalidParameterValue.NotWithinRange'

# OC switching does not support enabling origin certificate verification.
INVALIDPARAMETERVALUE_OCDIRECTORIGINDOMAINNOTSUPPORTUPSTREAMVERIFY = 'InvalidParameterValue.OCDirectOriginDomainNotSupportUpstreamVerify'

# The specified origin server group does not exist.
INVALIDPARAMETERVALUE_ORIGINGROUPNOTEXISTS = 'InvalidParameterValue.OriginGroupNotExists'

# Ownership verification failed. Please complete site ownership verification first.
INVALIDPARAMETERVALUE_OWNERSHIPVERIFICATIONNOTPASSED = 'InvalidParameterValue.OwnershipVerificationNotPassed'

# The page name already exists.
INVALIDPARAMETERVALUE_PAGENAMEALREADYEXIST = 'InvalidParameterValue.PageNameAlreadyExist'

# Does not match the specified regular expression.
INVALIDPARAMETERVALUE_REGEXMISMATCH = 'InvalidParameterValue.RegExMismatch'

# Edge mTLS is enabled. When the client uses an RSA or ECC algorithm certificate, the same algorithm certificate should also be configured in the edge HTTPS certificate.
INVALIDPARAMETERVALUE_SERVERCERTINFONEEDCONTAINRSAORECC = 'InvalidParameterValue.ServerCertInfoNeedContainRSAorECC'

# Edge mTLS is enabled. When the client uses a national encryption CA certificate, the national encryption certificate should also be configured in the edge HTTPS certificate.
INVALIDPARAMETERVALUE_SERVERCERTINFONEEDCONTAINSM2 = 'InvalidParameterValue.ServerCertInfoNeedContainSM2'

# Enter a valid shared CNAME prefix. It supports up to 50 characters.
INVALIDPARAMETERVALUE_SHAREDCNAMEPREFIXNOTMATCH = 'InvalidParameterValue.SharedCNAMEPrefixNotMatch'

# Enabling origin server failover and origin-pull rate limiting simultaneously is not supported.
INVALIDPARAMETERVALUE_SITEFAILOVERNOTSUPPORTHOSTORIGINPULLRATELIMIT = 'InvalidParameterValue.SiteFailoverNotSupportHostOriginPullRateLimit'

# Origin server failover does not support VOD origin servers.
INVALIDPARAMETERVALUE_SITEFAILOVERNOTSUPPORTHOSTORIGINTYPEVOD = 'InvalidParameterValue.SiteFailoverNotSupportHostOriginTypeVod'

# Enabling origin server failover and origin-pull mutual authentication/origin certificate verification simultaneously is not supported.
INVALIDPARAMETERVALUE_SITEFAILOVERNOTSUPPORTHOSTUPSTREAMVERIFY = 'InvalidParameterValue.SiteFailoverNotSupportHostUpstreamVerify'

# The input template contains a template that is not of the custom template type.
INVALIDPARAMETERVALUE_TEMPLATENOTCUSTOM = 'InvalidParameterValue.TemplateNotCustom'

# The template contains a non-existing template. Please check whether the template id is correct.
INVALIDPARAMETERVALUE_TEMPLATENOTFOUND = 'InvalidParameterValue.TemplateNotFound'

# The current domain suffix is not supported for access. If you need to use it, contact us.
INVALIDPARAMETERVALUE_TOPLEVELDOMAINNOTSUPPORT = 'InvalidParameterValue.TopLevelDomainNotSupport'

# Custom pages in the trial plan cannot be referenced.
INVALIDPARAMETERVALUE_TRIALPLANRESPONSEPAGE = 'InvalidParameterValue.TrialPlanResponsePage'

# Configuration item error.
INVALIDPARAMETERVALUE_UNRECOGNIZABLEVALUE = 'InvalidParameterValue.UnrecognizableValue'

# One client certificate is allowed at most in the origin-pull mutual authentication configuration.
INVALIDPARAMETERVALUE_UPSTREAMCLIENTCERTINFOQUOTALIMIT = 'InvalidParameterValue.UpstreamClientCertInfoQuotaLimit'

# A maximum of 1 CA certificate can be configured for origin certificate verification.
INVALIDPARAMETERVALUE_UPSTREAMVERIFYCUSTOMCACERTINFOQUOTALIMIT = 'InvalidParameterValue.UpstreamVerifyCustomCACertInfoQuotaLimit'

# Zone name format is incorrect. Please input a correctly formed domain name.
INVALIDPARAMETERVALUE_ZONENAMEINVALID = 'InvalidParameterValue.ZoneNameInvalid'

# punycode access is not supported.
INVALIDPARAMETERVALUE_ZONENAMENOTSUPPORTPUNYCODE = 'InvalidParameterValue.ZoneNameNotSupportPunyCode'

# Zone does not support subdomain access. Use second-level domains for zone access.
INVALIDPARAMETERVALUE_ZONENAMENOTSUPPORTSUBDOMAIN = 'InvalidParameterValue.ZoneNameNotSupportSubDomain'

# No corresponding site. Please ensure the site information is filled correctly.
INVALIDPARAMETERVALUE_ZONENOTFOUND = 'InvalidParameterValue.ZoneNotFound'

# Site disabled. Check the current site status.
INVALIDPARAMETERVALUE_ZONEPAUSED = 'InvalidParameterValue.ZonePaused'

# The identical site identifier is occupied. Please enter again.
INVALIDPARAMETERVALUE_ZONESAMEASNAME = 'InvalidParameterValue.ZoneSameAsName'

# The quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# Resource count in this submission exceeds the upper limit.
LIMITEXCEEDED_BATCHQUOTA = 'LimitExceeded.BatchQuota'

# The number of regular expression type fields in real-time log custom fields exceeds the limit.
LIMITEXCEEDED_CUSTOMLOGFIELDREGEXLIMITEXCEEDED = 'LimitExceeded.CustomLogFieldRegexLimitExceeded'

# Resource count submitted on the day exceeds the upper limit.
LIMITEXCEEDED_DAILYQUOTA = 'LimitExceeded.DailyQuota'

# The number of functions has reached the limit.
LIMITEXCEEDED_FUNCTIONLIMITEXCEEDED = 'LimitExceeded.FunctionLimitExceeded'

# The number of inference services has exceeded the limit.
LIMITEXCEEDED_INFERENCESERVICE = 'LimitExceeded.InferenceService'

# The number of LoadBalancers exceeds the limit.
LIMITEXCEEDED_LOADBALANCINGCOUNTLIMITEXCEEDED = 'LimitExceeded.LoadBalancingCountLimitExceeded'

# The number of KV namespaces under the site has reached the cap
LIMITEXCEEDED_NAMESPACELIMITEXCEEDED = 'LimitExceeded.NamespaceLimitExceeded'

# Billing package unsupported.
LIMITEXCEEDED_PACKNOTALLOW = 'LimitExceeded.PackNotAllow'

# Number of imported rules exceeds limit.
LIMITEXCEEDED_PROXYRULESLIMITEXCEEDED = 'LimitExceeded.ProxyRulesLimitExceeded'

# Query time range exceeds the limit.
LIMITEXCEEDED_QUERYTIMELIMITEXCEEDED = 'LimitExceeded.QueryTimeLimitExceeded'

# The request frequency reaches the limit per unit time.
LIMITEXCEEDED_RATELIMITEXCEEDED = 'LimitExceeded.RateLimitExceeded'

# The number of rules has reached the limit.
LIMITEXCEEDED_RULELIMITEXCEEDED = 'LimitExceeded.RuleLimitExceeded'

# Exceeded the functional limitation.
LIMITEXCEEDED_SECURITY = 'LimitExceeded.Security'

# The time series data items queried this time exceed the limit.
LIMITEXCEEDED_TIMINGDATAITEMLIMITEXCEEDED = 'LimitExceeded.TimingDataItemLimitExceeded'

# User instance quantity limitation.
LIMITEXCEEDED_USERQUOTALIMITED = 'LimitExceeded.UserQuotaLimited'

# The number of sites that can be bound to the package exceeds the quota.
LIMITEXCEEDED_ZONEBINDPLAN = 'LimitExceeded.ZoneBindPlan'

# Parameters are missing.
MISSINGPARAMETER = 'MissingParameter'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# Feature in beta test. Contact sales to enable "network optimization in the Chinese mainland (international acceleration)".
OPERATIONDENIED_ACCELERATEMAINLANDDISABLE = 'OperationDenied.AccelerateMainlandDisable'

# Acceleration on the Chinese mainland conflicts with IPv6. They cannot be configured at the same time.
OPERATIONDENIED_ACCELERATEMAINLANDIPV6CONFLICT = 'OperationDenied.AccelerateMainlandIpv6Conflict'

# A domain name feature under the current site conflicts with network optimization in the Chinese mainland and cannot be configured simultaneously.
OPERATIONDENIED_ACCELERATEMAINLANDMULTIPLYLAYERCONFLICT = 'OperationDenied.AccelerateMainlandMultiplyLayerConflict'

# The Layer-7 domain name service referencing an origin group is being deployed. Please re-edit later.
OPERATIONDENIED_ACCELERATIONDOMAINSTATUSNOTINONLINE = 'OperationDenied.AccelerationDomainStatusNotInOnline'

# The current domain name does not support enabling advanced origin optimization and cross-border direct connect simultaneously.
OPERATIONDENIED_ADVANCEDORIGINROUTINGCONFLICTWITHDCIOVERSEALAN = 'OperationDenied.AdvancedOriginRoutingConflictWithDciOverseaLan'

# This operation does not support alias domain names.
OPERATIONDENIED_ALIASDOMAINNOTSUPPORT = 'OperationDenied.AliasDomainNotSupport'

# Currently, only the keyless certificate mode allows the private key of the certificate to be empty.
OPERATIONDENIED_CERTIFICATEPRIVATEKEYISEMPTY = 'OperationDenied.CertificatePrivateKeyIsEmpty'

# The current compliance status is banning.
OPERATIONDENIED_COMPLIANCEFORBIDDEN = 'OperationDenied.ComplianceForbidden'

# The configuration has been locked. Unlock it and retry.
OPERATIONDENIED_CONFIGLOCKED = 'OperationDenied.ConfigLocked'

# The TEO_QCSLinkedRoleInDnspodAccessEO role is not authorized. Please authorize it and try again.
OPERATIONDENIED_DNSPODUNAUTHORIZEDROLEOPERATION = 'OperationDenied.DNSPodUnauthorizedRoleOperation'

# Site deletion pre-check failed.
OPERATIONDENIED_DELETEZONEPRECHECKFAILED = 'OperationDenied.DeleteZonePreCheckFailed'

# Site disabling not complete. Try again later.
OPERATIONDENIED_DISABLEZONENOTCOMPLETED = 'OperationDenied.DisableZoneNotCompleted'

# A domain name is in the shared cname group and the access type cannot be switched.
OPERATIONDENIED_DOMAININSHARECNAMEGROUP = 'OperationDenied.DomainInShareCnameGroup'

# Domain banned. Unable to operate temporarily.
OPERATIONDENIED_DOMAINISBLOCKED = 'OperationDenied.DomainIsBlocked'

# The domain name must be in the site associated with the IP SSL shared CNAME and in the IP SSL shared CNAME.
OPERATIONDENIED_DOMAINMUSTINIPSSLSHAREDCNAMEZONEANDINSHAREDCNAME = 'OperationDenied.DomainMustInIPSSLSharedCNAMEZoneAndInSharedCNAME'

# The domain name has not obtained an ICP Filing.
OPERATIONDENIED_DOMAINNOICP = 'OperationDenied.DomainNoICP'

# The service area is not allowed to be modified when a domain name exists under the site.
OPERATIONDENIED_DOMAINNUMBERISNOTZERO = 'OperationDenied.DomainNumberIsNotZero'

# A domain name on the site is not in a steady state. Steady states include "online" and "offline".
OPERATIONDENIED_DOMAINSTATUSUNSTABLE = 'OperationDenied.DomainStatusUnstable'

# The Enterprise Edition Plan does not support auto-renewal.
OPERATIONDENIED_ENTERPRISEPLANAUTORENEWUNSUPPORTED = 'OperationDenied.EnterprisePlanAutoRenewUnsupported'

# The Enterprise Edition Plan does not support renewal.
OPERATIONDENIED_ENTERPRISEPLANRENEWUNSUPPORTED = 'OperationDenied.EnterprisePlanRenewUnsupported'

# The Enterprise Edition Plan does not support upgrades.
OPERATIONDENIED_ENTERPRISEPLANUPGRADEUNSUPPORTED = 'OperationDenied.EnterprisePlanUpgradeUnsupported'

# Site environment not ready.
OPERATIONDENIED_ENVNOTREADY = 'OperationDenied.EnvNotReady'

# Site disabled. Turn it on and try again.
OPERATIONDENIED_ERRZONEISALREADYPAUSED = 'OperationDenied.ErrZoneIsAlreadyPaused'

# The edge HTTPS certificate of the domain name to be changed is inconsistent. Please confirm that the domain name certificates are consistent and retry.
OPERATIONDENIED_HOSTSCERTIFICATEINCONSISTENCY = 'OperationDenied.HostsCertificateInconsistency'

# The edge mutual authentication certificates for the domain name to be changed are inconsistent. Please confirm that the domain name certificates are consistent and try again.
OPERATIONDENIED_HOSTSCLIENTCERTIFICATEINCONSISTENCY = 'OperationDenied.HostsClientCertificateInconsistency'

# The keyless server of the domain name to be changed is inconsistent. Please confirm that the keyless server is consistent before retrying.
OPERATIONDENIED_HOSTSKEYLESSSERVERINCONSISTENCY = 'OperationDenied.HostsKeylessServerInconsistency'

# The origin-pull mutual authentication certificates for the domain name to be changed are inconsistent. Please confirm that the domain name certificates are consistent and try again.
OPERATIONDENIED_HOSTSUPSTREAMCERTIFICATEINCONSISTENCY = 'OperationDenied.HostsUpstreamCertificateInconsistency'

# The origin certificate verification configuration of the domain name to be changed is inconsistent. Please confirm that the domain name configuration is consistent and try again.
OPERATIONDENIED_HOSTSUPSTREAMCERTIFICATEVERIFYINCONSISTENCY = 'OperationDenied.HostsUpstreamCertificateVerifyInconsistency'

# IP SSL is bound to other domains. No operations allowed.
OPERATIONDENIED_IPSSLALREADYBOUNDANOTHERDOMAIN = 'OperationDenied.IPSSLAlreadyBoundAnotherDomain'

# To enable Anti-DDoS, security must be enabled.
OPERATIONDENIED_INVALIDADVANCEDDEFENSESECURITYTYPE = 'OperationDenied.InvalidAdvancedDefenseSecurityType'

# To enable Anti-DDoS, the site acceleration region must be Chinese mainland.
OPERATIONDENIED_INVALIDADVANCEDDEFENSEZONEAREA = 'OperationDenied.InvalidAdvancedDefenseZoneArea'

# The package does not support advanced origin-pull optimization configuration.
OPERATIONDENIED_INVALIDADVANCEDORIGINROUTINGBILLING = 'OperationDenied.InvalidAdvancedOriginRoutingBilling'

# Exclusive DDoS protection conflicts with IPv6. They cannot be configured at the same time.
OPERATIONDENIED_IPV6ADVANCEDCONFLICT = 'OperationDenied.Ipv6AdvancedConflict'

# The IPv6 feature and static IP cannot be enabled at the same time.
OPERATIONDENIED_IPV6STATICIPCONFLICT = 'OperationDenied.Ipv6StaticIpConflict'

# The domain name to be changed has a different certificate or keyless server. Please confirm that the edge HTTPS certificate or keyless server is consistent before retrying.
OPERATIONDENIED_KEYLESSCERTSWITCHTOFREECERTCONFLICT = 'OperationDenied.KeylessCertSwitchToFreeCertConflict'

# The keyless certificate mode requires the private key of the certificate to be empty.
OPERATIONDENIED_KEYLESSMODECERTIFICATEPRIVATEKEYNEEDEMPTY = 'OperationDenied.KeylessModeCertificatePrivateKeyNeedEmpty'

# Layer 4 instance resources are selling out quickly and are currently out of stock. We are urgently restocking. It is not possible to add new Layer 4 proxies right now. Please wait patiently.
OPERATIONDENIED_L4LACKOFRESOURCES = 'OperationDenied.L4LackOfResources'

# Layer 4 port resources are in high demand and sold out. We are urgently restocking. It is not possible to add new Layer 4 proxies or add rules. Please wait patiently.
OPERATIONDENIED_L4PORTLACKOFRESOURCES = 'OperationDenied.L4PortLackOfResources'

# The Layer 4 proxy resource is blocked, so operations are not allowed.
OPERATIONDENIED_L4PROXYINBANNEDSTATUS = 'OperationDenied.L4ProxyInBannedStatus'

# The Layer 4 channel is closed, so no rules are allowed to be added.
OPERATIONDENIED_L4PROXYINOFFLINESTATUS = 'OperationDenied.L4ProxyInOfflineStatus'

# Instance in deployment. Unable to operate.
OPERATIONDENIED_L4PROXYINPROCESSSTATUS = 'OperationDenied.L4ProxyInProcessStatus'

# A Layer 4 proxy instance is in deployment, so the site cannot be deactivated.
OPERATIONDENIED_L4PROXYINPROGRESSSTATUS = 'OperationDenied.L4ProxyInProgressStatus'

# A Layer 4 proxy instance is being disabled, so the site cannot be deactivated now.
OPERATIONDENIED_L4PROXYINSTOPPINGSTATUS = 'OperationDenied.L4ProxyInStoppingStatus'

# The bound L4 instance is not in the running state. Operation not allowed.
OPERATIONDENIED_L4STATUSNOTINONLINE = 'OperationDenied.L4StatusNotInOnline'

# An acceleration domain name is in deploying status. Deactivating the site is not currently supported.
OPERATIONDENIED_L7HOSTINPROCESSSTATUS = 'OperationDenied.L7HostInProcessStatus'

# The domain name associated with the last IP SSL operation has not completed launch yet. Wait for launch completion before proceeding.
OPERATIONDENIED_LASTIPSSLOPERATIONNOTCOMPLETE = 'OperationDenied.LastIPSSLOperationNotComplete'

# The origin-pull allowlist is already the latest version. No update required.
OPERATIONDENIED_LATESTVERSIONNOW = 'OperationDenied.LatestVersionNow'

# The bound load balancer is not in the running state. Operation not allowed.
OPERATIONDENIED_LOADBALANCESTATUSNOTINONLINE = 'OperationDenied.LoadBalanceStatusNotInOnline'

# Operation not supported for load balancing in this site status.
OPERATIONDENIED_LOADBALANCINGZONEISNOTACTIVE = 'OperationDenied.LoadBalancingZoneIsNotActive'

# IPv6 cannot be enabled for non-overseas exclusive protection.
OPERATIONDENIED_MSGIPV6ADVANCEDCONFLICT = 'OperationDenied.MsgIpv6AdvancedConflict'

# Multiple Cname sites already exist. Switching to NS is not allowed.
OPERATIONDENIED_MULTIPLECNAMEZONE = 'OperationDenied.MultipleCnameZone'

# Traffic scheduling by domain is not supported in NS access mode.
OPERATIONDENIED_NSNOTALLOWTRAFFICSTRATEGY = 'OperationDenied.NSNotAllowTrafficStrategy'

# Sites without domain access can only be switched to the CNAME access type.
OPERATIONDENIED_NODOMAINACCESSZONEONLYALLOWMODIFIEDTOCNAME = 'OperationDenied.NoDomainAccessZoneOnlyAllowModifiedToCNAME'

# Domainless access sites support modification of only the acceleration region and identical site identifier.
OPERATIONDENIED_NODOMAINACCESSZONEONLYSUPPORTMODIFYAREAANDALIASZONENAME = 'OperationDenied.NoDomainAccessZoneOnlySupportModifyAreaAndAliasZoneName'

# Sites without domain access do not support any modification actions other than switching to the CNAME access type.
OPERATIONDENIED_NODOMAINACCESSZONEONLYSUPPORTMODIFYTYPE = 'OperationDenied.NoDomainAccessZoneOnlySupportModifyType'

# A domain name under the current site is associated with an exclusive accelerated IP. To disable network optimization in the Chinese mainland, unbind the exclusive IP first and try again.
OPERATIONDENIED_NOTALLOWCLOSEACCELERATEMAINLANDWHENDOMAINBOUNDEXCLUSIVEIP = 'OperationDenied.NotAllowCloseAccelerateMainlandWhenDomainBoundExclusiveIP'

# The advanced origin optimization feature is currently only available to allowlist users.
OPERATIONDENIED_NOTINADVANCEDORIGINROUTINGWHITELIST = 'OperationDenied.NotInAdvancedOriginRoutingWhiteList'

# Currently, the keyless certificate feature is available only to users in the allowlist.
OPERATIONDENIED_NOTINKEYLESSWHITELIST = 'OperationDenied.NotInKeylessWhiteList'

# Not in the preheated origin-pull rate limiting configuration allowlist. Submit a ticket.
OPERATIONDENIED_NOTINPREFETCHORIGINLIMITWHITELIST = 'OperationDenied.NotInPrefetchOriginLimitWhiteList'

# EdgeOne Shield is currently only available to allowlist users.
OPERATIONDENIED_NOTINSHIELDSPACEWHITELIST = 'OperationDenied.NotInShieldSpaceWhiteList'

# The current origin server failure failover feature is only available to allowlist users.
OPERATIONDENIED_NOTINSITEFAILOVERWHITELIST = 'OperationDenied.NotInSiteFailoverWhiteList'

# The current origin-pull mutual authentication feature is only available to allowlist users.
OPERATIONDENIED_NOTINUPSTREAMMTLSWHITELIST = 'OperationDenied.NotInUpstreamMTLSWhiteList'

# The user is not in the allowlist for version management.
OPERATIONDENIED_NOTINVERSIONCONTROLWHITELIST = 'OperationDenied.NotInVersionControlWhiteList'

# Acceleration domain name is in use and cannot be deleted.
OPERATIONDENIED_ORIGINGROUPACCELERATIONDOMAINUSED = 'OperationDenied.OriginGroupAccelerationDomainUsed'

# Layer 4 proxy in use. It cannot be deleted.
OPERATIONDENIED_ORIGINGROUPL4USED = 'OperationDenied.OriginGroupL4Used'

# Load balancing is active and cannot be deleted.
OPERATIONDENIED_ORIGINGROUPLBUSED = 'OperationDenied.OriginGroupLBUsed'

# Rule engine in use and cannot be deleted.
OPERATIONDENIED_ORIGINGROUPRULEENGINEUSED = 'OperationDenied.OriginGroupRuleEngineUsed'

# The current root account does not have permission to use the origin-pull data query interface. Contact after-sales service.
OPERATIONDENIED_ORIGINPULLDATANOTSUPPORTED = 'OperationDenied.OriginPullDataNotSupported'

# Ownership verification failed. Please complete site ownership verification first.
OPERATIONDENIED_OWNERSHIPVERIFICATIONNOTPASSED = 'OperationDenied.OwnershipVerificationNotPassed'

# A plan downgrade is not supported.
OPERATIONDENIED_PLANDOWNGRADENOTALLOWED = 'OperationDenied.PlanDowngradeNotAllowed'

# The plan has expired.
OPERATIONDENIED_PLANHASBEENEXPIRED = 'OperationDenied.PlanHasBeenExpired'

# The plan has been isolated.
OPERATIONDENIED_PLANHASBEENISOLATED = 'OperationDenied.PlanHasBeenIsolated'

# This plan does not support the purchase of additional plan quotas.
OPERATIONDENIED_PLANINCREASEPLANQUOTAUNSUPPORTED = 'OperationDenied.PlanIncreasePlanQuotaUnsupported'

# The plan does not support changing the service area of a site.
OPERATIONDENIED_PLANNOTSUPPORTMODIFYZONEAREA = 'OperationDenied.PlanNotSupportModifyZoneArea'

# The enterprise package of the site configuration does not support the version control feature.
OPERATIONDENIED_PLANTYPEISWRONG = 'OperationDenied.PlanTypeIsWrong'

# The Anycast IP scheduling mode does not support enabling acceleration in the Chinese mainland.
OPERATIONDENIED_PLATTYPEIPACCELERATEMAINLANDNOTSUPPORT = 'OperationDenied.PlatTypeIPAccelerateMainlandNotSupport'

# To create an Enterprise Edition Plan, contact the business personnel.
OPERATIONDENIED_PLEASECONTACTBUSINESSPERSONNEL = 'OperationDenied.PleaseContactBusinessPersonnel'

# DNS record is not allowed to be added.
OPERATIONDENIED_RECORDISFORBIDDEN = 'OperationDenied.RecordIsForbidden'

# Billing resources are in operation. Try again later.
OPERATIONDENIED_RESOURCEHASBEENLOCKED = 'OperationDenied.ResourceHasBeenLocked'

# Currently there are parallel request operations that repel each other. Please try again later.
OPERATIONDENIED_RESOURCELOCKEDTEMPORARY = 'OperationDenied.ResourceLockedTemporary'

# Advanced protection resources are sold out due to high demand. We are urgently restocking. Advanced protection cannot be enabled now. Please wait patiently.
OPERATIONDENIED_SECURITYLACKOFRESOURCES = 'OperationDenied.SecurityLackOfResources'

# Domains bound to a shared CNAME are not allowed to update network optimization in the Chinese mainland (international acceleration) access. If you need to update it separately, unbind the domain from the shared CNAME first.
OPERATIONDENIED_SHAREDCNAMEUNSUPPORTEDACCELERATEMAINLAND = 'OperationDenied.SharedCNAMEUnsupportedAccelerateMainland'

# Domains bound to a shared CNAME are not allowed to update IPv6 access. If you need to update it separately, unbind the domain from the shared CNAME first.
OPERATIONDENIED_SHAREDCNAMEUNSUPPORTEDIPV6 = 'OperationDenied.SharedCNAMEUnsupportedIPv6'

# The static IP cannot be enabled for this instance's region.
OPERATIONDENIED_STATICIPAREACONFLICT = 'OperationDenied.StaticIpAreaConflict'

# The current domain is integrated with both CDN and EdgeOne. No operation can be performed at this time.
OPERATIONDENIED_SWITCHAREACDNPLATFORMREUSE = 'OperationDenied.SwitchAreaCdnPlatformReuse'

# Origin protection configuration is being deployed. Switch the acceleration region after deployment.
OPERATIONDENIED_SWITCHAREAORIGINPROTECTIONDEPLOYING = 'OperationDenied.SwitchAreaOriginProtectionDeploying'

# Disabling the origin-pull mutual authentication is not supported now. To disable it, please change the edge HTTPS certificate configuration to 'none'.
OPERATIONDENIED_UNSUPPORTTOCLOSEUPSTREAMMTLS = 'OperationDenied.UnSupportToCloseUpstreamMTLS'

# Plan not supported.
OPERATIONDENIED_UNSUPPORTEDPLAN = 'OperationDenied.UnsupportedPlan'

# Please first update the IP allowlist.
OPERATIONDENIED_UPDATEIPWHITELISTFIRST = 'OperationDenied.UpdateIPWhitelistFirst'

# To enable the origin-pull mutual authentication, please configure the edge HTTPS certificate first.
OPERATIONDENIED_USEUPSTREAMMTLSNEEDOPENHTTPS = 'OperationDenied.UseUpstreamMTLSNeedOpenHttps'

# A test version is in use. Release the test version to production or roll it back and try again.
OPERATIONDENIED_VERSIONCONTROLISGRAYING = 'OperationDenied.VersionControlIsGraying'

# Version management mode is applied. Operation not allowed.
OPERATIONDENIED_VERSIONCONTROLLOCKED = 'OperationDenied.VersionControlLocked'

# For sites in NS mode, please first switch the NS before toggling version management.
OPERATIONDENIED_VERSIONCONTROLNEEDNSSWITCHED = 'OperationDenied.VersionControlNeedNSSwitched'

# The site working mode is NOT_IN version management mode.
OPERATIONDENIED_WORKMODENOTINVERSIONCONTROL = 'OperationDenied.WorkModeNotInVersionControl'

# When modifying the acceleration region, if a domain name already exists under the site, you do not have permission to simultaneously adjust other information.
OPERATIONDENIED_ZONEHASHOSTSMODIFYCONFLICT = 'OperationDenied.ZoneHasHostsModifyConflict'

# The shared CNAME is bound to another site. Unbind it first before deleting the site.
OPERATIONDENIED_ZONEISBINDINGSHAREDCNAME = 'OperationDenied.ZoneIsBindingSharedCNAME'

# The site has a custom error page reference. Unbind it first.
OPERATIONDENIED_ZONEISREFERENCECUSTOMERRORPAGE = 'OperationDenied.ZoneIsReferenceCustomErrorPage'

# Zone not activated.
OPERATIONDENIED_ZONENOTACTIVE = 'OperationDenied.ZoneNotActive'

# The resource is occupied.
RESOURCEINUSE = 'ResourceInUse'

# Resource is occupied by the alias domain name of this account.
RESOURCEINUSE_ALIASDOMAIN = 'ResourceInUse.AliasDomain'

# The same alias domain name already exists and does not support duplicate addition.
RESOURCEINUSE_ALIASNAME = 'ResourceInUse.AliasName'

# That domain name already exists as an acceleration domain name. Repeated access is not supported.
RESOURCEINUSE_ALREADYEXISTSASANACCELERATIONDOMAIN = 'ResourceInUse.AlreadyExistsAsAnAccelerationDomain'

# The resource is occupied by a Cname integration from this account.
RESOURCEINUSE_CNAME = 'ResourceInUse.Cname'

# Dns resources are occupied.
RESOURCEINUSE_DNS = 'ResourceInUse.Dns'

# That domain name is being parsed. If you need to enable acceleration, please go to the DNS record page to enable acceleration.
RESOURCEINUSE_DNSRECORD = 'ResourceInUse.DnsRecord'

# The same alias domain name already exists.
RESOURCEINUSE_DUPLICATENAME = 'ResourceInUse.DuplicateName'

# Resource is occupied by a wildcard domain name.
RESOURCEINUSE_GENERICHOST = 'ResourceInUse.GenericHost'

# Resource is occupied by a subdomain of this account.
RESOURCEINUSE_HOST = 'ResourceInUse.Host'

# The resource is occupied by an NS access from this account.
RESOURCEINUSE_NS = 'ResourceInUse.NS'

# Resource is connected by another user.
RESOURCEINUSE_OTHERS = 'ResourceInUse.Others'

# Resource is occupied by the alias domain name of another account.
RESOURCEINUSE_OTHERSALIASDOMAIN = 'ResourceInUse.OthersAliasDomain'

# The resource is occupied by a Cname integration from another account.
RESOURCEINUSE_OTHERSCNAME = 'ResourceInUse.OthersCname'

# Resource is occupied by a subdomain of another account.
RESOURCEINUSE_OTHERSHOST = 'ResourceInUse.OthersHost'

# The resource is occupied by an NS access from another account.
RESOURCEINUSE_OTHERSNS = 'ResourceInUse.OthersNS'

# The preheated origin-pull rate limiting configuration already exists and cannot be recreated. Please check whether the corresponding configuration has been created.
RESOURCEINUSE_PREFETCHORIGINLIMITALREADYEXISTS = 'ResourceInUse.PrefetchOriginLimitAlreadyExists'

# The resource is occupied by simultaneous Cname integrations from this account and another account.
RESOURCEINUSE_SELFANDOTHERSCNAME = 'ResourceInUse.SelfAndOthersCname'

# This shared CNAME is bound to an acceleration domain name and deletion protection is enabled. If you need to delete it, please first unbind the corresponding domain.
RESOURCEINUSE_SHAREDCNAME = 'ResourceInUse.SharedCNAME'

# Alias domain name has been connected to the site.
RESOURCEINUSE_ZONE = 'ResourceInUse.Zone'

# Insufficient resources.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The domain name is not properly accessed via DNSPod. Please try again after DNSPod access.
RESOURCENOTFOUND_DNSPODDOMAINNOTINACCOUNT = 'ResourceNotFound.DNSPodDomainNotInAccount'

# The reasoning service does not exist.
RESOURCENOTFOUND_INFERENCESERVICE = 'ResourceNotFound.InferenceService'

# Maximum upload size limit unconfigured
RESOURCENOTFOUND_POSTMAXSIZEQUOTANOTFOUND = 'ResourceNotFound.PostMaxSizeQuotaNotFound'

# The configuration group version does not exist. Check and retry.
RESOURCENOTFOUND_VERSIONNOTFOUND = 'ResourceNotFound.VersionNotFound'

# The site does not exist.
RESOURCENOTFOUND_ZONENOTFOUND = 'ResourceNotFound.ZoneNotFound'

# Resources are unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# The cert does not exist or is unauthorized.
RESOURCEUNAVAILABLE_CERTNOTFOUND = 'ResourceUnavailable.CertNotFound'

# The current domain is connected to EdgeOne. To connect it to the current account, retrieve the domain name.
RESOURCEUNAVAILABLE_DOMAINALREADYEXISTS = 'ResourceUnavailable.DomainAlreadyExists'

# The requested acceleration domain name does not exist. Correct it and try again.
RESOURCEUNAVAILABLE_DOMAINNOTFOUND = 'ResourceUnavailable.DomainNotFound'

# The function does not exist or does not belong to the account.
RESOURCEUNAVAILABLE_FUNCTIONNOTFOUND = 'ResourceUnavailable.FunctionNotFound'

# Domain name not found or proxy not enabled.
RESOURCEUNAVAILABLE_HOSTNOTFOUND = 'ResourceUnavailable.HostNotFound'

# KV namespace does not exist.
RESOURCEUNAVAILABLE_NAMESPACENOTFOUND = 'ResourceUnavailable.NamespaceNotFound'

# The rule does not exist or does not belong to the account.
RESOURCEUNAVAILABLE_RULENOTFOUND = 'ResourceUnavailable.RuleNotFound'

# The shared CNAME is occupied. Please enter another one.
RESOURCEUNAVAILABLE_SHAREDCNAMEALREADYEXISTS = 'ResourceUnavailable.SharedCNAMEAlreadyExists'

# The site does not exist or does not belong to this account.
RESOURCEUNAVAILABLE_ZONENOTFOUND = 'ResourceUnavailable.ZoneNotFound'

# Resources are sold out due to high demand. We are urgently restocking. New domain names cannot be added now. Please wait patiently.
RESOURCESSOLDOUT_L7LACKOFRESOURCES = 'ResourcesSoldOut.L7LackOfResources'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Unauthorized Cam operation.
UNAUTHORIZEDOPERATION_CAMUNAUTHORIZED = 'UnauthorizedOperation.CamUnauthorized'

# Authentication error occurred.
UNAUTHORIZEDOPERATION_DOMAINEMPTY = 'UnauthorizedOperation.DomainEmpty'

# The subaccount has insufficient permissions. Grant the required permissions and proceed with the operation.
UNAUTHORIZEDOPERATION_NOPERMISSION = 'UnauthorizedOperation.NoPermission'

# Unknown error occurs on the real server.
UNAUTHORIZEDOPERATION_UNKNOWN = 'UnauthorizedOperation.Unknown'

# The operation is not supported.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# Alias domain names do not support object storage as the origin server type of the target domain.
UNSUPPORTEDOPERATION_TARGETNAMEORIGINTYPECOS = 'UnsupportedOperation.TargetNameOriginTypeCos'
