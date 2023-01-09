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

# The domain name does not exist or is not belong to this account.
INVALIDPARAMETER_DOMAINNOTFOUND = 'InvalidParameter.DomainNotFound'

# The current conditions do not support the requested operation.
INVALIDPARAMETER_ERRACTIONUNSUPPORTTARGET = 'InvalidParameter.ErrActionUnsupportTarget'

# Invalid operation.
INVALIDPARAMETER_ERRINVALIDACTION = 'InvalidParameter.ErrInvalidAction'

# Invalid operation: Invalid parameter.
INVALIDPARAMETER_ERRINVALIDACTIONPARAM = 'InvalidParameter.ErrInvalidActionParam'

# 
INVALIDPARAMETER_ERRINVALIDACTIONPARAMBADVALUETYPE = 'InvalidParameter.ErrInvalidActionParamBadValueType'

# Invalid parameter: Duplicate parameter names.
INVALIDPARAMETER_ERRINVALIDACTIONPARAMDUPLICATENAME = 'InvalidParameter.ErrInvalidActionParamDuplicateName'

# Invalid parameter: The parameter has too many values.
INVALIDPARAMETER_ERRINVALIDACTIONPARAMTOOMANYVALUES = 'InvalidParameter.ErrInvalidActionParamTooManyValues'

# Invalid action type.
INVALIDPARAMETER_ERRINVALIDACTIONTYPE = 'InvalidParameter.ErrInvalidActionType'

# Invalid condition: The letter case is ignored.
INVALIDPARAMETER_ERRINVALIDCONDITIONIGNORECASE = 'InvalidParameter.ErrInvalidConditionIgnoreCase'

# Invalid condition: The match type is not supported by this parameter.
INVALIDPARAMETER_ERRINVALIDCONDITIONNAMETARGETNOTSUPPORTNAME = 'InvalidParameter.ErrInvalidConditionNameTargetNotSupportName'

# 
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUEBADREGULAR = 'InvalidParameter.ErrInvalidConditionValueBadRegular'

# Invalid condition: The parameter value is invalid.
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUEBADVALUE = 'InvalidParameter.ErrInvalidConditionValueBadValue'

# Invalid parameter value: File extension is not allowed.
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUEBADVALUECONTAINFILENAMEEXTENSION = 'InvalidParameter.ErrInvalidConditionValueBadValueContainFileNameExtension'

# Invalid condition: The parameter value exceeds the limit.
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUETOOLONGVALUE = 'InvalidParameter.ErrInvalidConditionValueTooLongValue'

# 
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUETOOMANYWILDCARD = 'InvalidParameter.ErrInvalidConditionValueTooManyWildcard'

# Invalid condition: The parameter value is 0.
INVALIDPARAMETER_ERRINVALIDCONDITIONVALUEZEROLENGTH = 'InvalidParameter.ErrInvalidConditionValueZeroLength'

# To enable gRPC support, HTTP/2 support must be enabled as well.
INVALIDPARAMETER_GRPCREQUIREHTTP2 = 'InvalidParameter.GrpcRequireHttp2'

# The domain name does not exist.
INVALIDPARAMETER_HOSTNOTFOUND = 'InvalidParameter.HostNotFound'

# 
INVALIDPARAMETER_HOSTSTATUSNOTALLOWAPPLYCERTIFICATE = 'InvalidParameter.HostStatusNotAllowApplyCertificate'

# Invalid token authentication.
INVALIDPARAMETER_INVALIDAUTHENTICATION = 'InvalidParameter.InvalidAuthentication'

# Invalid token authentication parameter.
INVALIDPARAMETER_INVALIDAUTHENTICATIONTYPESIGNPARAM = 'InvalidParameter.InvalidAuthenticationTypeSignParam'

# 
INVALIDPARAMETER_INVALIDCACHECONFIGFOLLOWORIGIN = 'InvalidParameter.InvalidCacheConfigFollowOrigin'

# Invalid cache key.
INVALIDPARAMETER_INVALIDCACHEKEY = 'InvalidParameter.InvalidCacheKey'

# Invalid query string.
INVALIDPARAMETER_INVALIDCACHEKEYQUERYSTRINGVALUE = 'InvalidParameter.InvalidCacheKeyQueryStringValue'

# Invalid node cache.
INVALIDPARAMETER_INVALIDCACHEONLYONSWITCH = 'InvalidParameter.InvalidCacheOnlyOnSwitch'

# 
INVALIDPARAMETER_INVALIDCACHETIME = 'InvalidParameter.InvalidCacheTime'

# Incorrect certificate information.
INVALIDPARAMETER_INVALIDCERTINFO = 'InvalidParameter.InvalidCertInfo'

# Invalid client IP request header.
INVALIDPARAMETER_INVALIDCLIENTIPHEADERNAME = 'InvalidParameter.InvalidClientIpHeaderName'

# Invalid smart acceleration.
INVALIDPARAMETER_INVALIDDYNAMICROUTINE = 'InvalidParameter.InvalidDynamicRoutine'

# 
INVALIDPARAMETER_INVALIDDYNAMICROUTINEBILLING = 'InvalidParameter.InvalidDynamicRoutineBilling'

# Invalid custom error page.
INVALIDPARAMETER_INVALIDERRORPAGEREDIRECTURL = 'InvalidParameter.InvalidErrorPageRedirectUrl'

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

# Invalid request header.
INVALIDPARAMETER_INVALIDREQUESTHEADERNAME = 'InvalidParameter.InvalidRequestHeaderName'

# You have not purchased a plan yet.
INVALIDPARAMETER_INVALIDRESOURCEIDBILLING = 'InvalidParameter.InvalidResourceIdBilling'

# Invalid response header.
INVALIDPARAMETER_INVALIDRESPONSEHEADERNAME = 'InvalidParameter.InvalidResponseHeaderName'

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

# Parameter error.
INVALIDPARAMETER_PARAMETERERROR = 'InvalidParameter.ParameterError'

# The plan doesn’t exist.
INVALIDPARAMETER_PLANNOTFOUND = 'InvalidParameter.PlanNotFound'

# Invalid parameter.
INVALIDPARAMETER_SECURITY = 'InvalidParameter.Security'

# Configuration parameter error.
INVALIDPARAMETER_SETTINGINVALIDPARAM = 'InvalidParameter.SettingInvalidParam'

# Resource error
INVALIDPARAMETER_TARGET = 'InvalidParameter.Target'

# Failed to create the task
INVALIDPARAMETER_TASKNOTGENERATED = 'InvalidParameter.TaskNotGenerated'

# 
INVALIDPARAMETER_TASKSYSTEMERROR = 'InvalidParameter.TaskSystemError'

# Invalid file upload link.
INVALIDPARAMETER_UPLOADURL = 'InvalidParameter.UploadUrl'

# The site is already bound.
INVALIDPARAMETER_ZONEHASBEENBOUND = 'InvalidParameter.ZoneHasBeenBound'

# The site does not exist.
INVALIDPARAMETER_ZONENOTFOUND = 'InvalidParameter.ZoneNotFound'

# Invalid parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Invalid domain name. Please check the status.
INVALIDPARAMETERVALUE_INVALIDDOMAINSTATUS = 'InvalidParameterValue.InvalidDomainStatus'

# The quota limit has been reached.
LIMITEXCEEDED = 'LimitExceeded'

# Reached the upper limit of resource number
LIMITEXCEEDED_BATCHQUOTA = 'LimitExceeded.BatchQuota'

# Reached the daily upper limit of resource number
LIMITEXCEEDED_DAILYQUOTA = 'LimitExceeded.DailyQuota'

# Reached the API rate limit.
LIMITEXCEEDED_RATELIMITEXCEEDED = 'LimitExceeded.RateLimitExceeded'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# Unable to use the domain name when it’s blocked.
OPERATIONDENIED_DOMAINISBLOCKED = 'OperationDenied.DomainIsBlocked'

# The domain name doesn't have an ICP filing number.
OPERATIONDENIED_DOMAINNOICP = 'OperationDenied.DomainNoICP'

# Operation failed: The L4 proxy is blocked.
OPERATIONDENIED_L4PROXYINBANNEDSTATUS = 'OperationDenied.L4ProxyInBannedStatus'

# Unable to operate the L4 instance when it’s not running
OPERATIONDENIED_L4STATUSNOTINONLINE = 'OperationDenied.L4StatusNotInOnline'

# Unable to switch to NS for multiple sites using CNAME.
OPERATIONDENIED_MULTIPLECNAMEZONE = 'OperationDenied.MultipleCnameZone'

# Domain traffic scheduling is not supported in NS access mode.
OPERATIONDENIED_NSNOTALLOWTRAFFICSTRATEGY = 'OperationDenied.NSNotAllowTrafficStrategy'

# The resource is occupied.
RESOURCEINUSE = 'ResourceInUse'

# Resources occupied by the alias domain names under this account.
RESOURCEINUSE_ALIASDOMAIN = 'ResourceInUse.AliasDomain'

# Resources occupied by this account via CNAME.
RESOURCEINUSE_CNAME = 'ResourceInUse.Cname'

# DNS resources occupied.
RESOURCEINUSE_DNS = 'ResourceInUse.Dns'

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

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# The certificate does not exist or is not authorized.
RESOURCEUNAVAILABLE_CERTNOTFOUND = 'ResourceUnavailable.CertNotFound'

# The domain name does not exist or not use a proxy.
RESOURCEUNAVAILABLE_HOSTNOTFOUND = 'ResourceUnavailable.HostNotFound'

# No proxied sites found
RESOURCEUNAVAILABLE_PROXYZONENOTFOUND = 'ResourceUnavailable.ProxyZoneNotFound'

# The site does not exist or is not belong to this account.
RESOURCEUNAVAILABLE_ZONENOTFOUND = 'ResourceUnavailable.ZoneNotFound'

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
