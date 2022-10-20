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

# Failed to create the logset: The logset name already exists.
FAILEDOPERATION_CREATECLSLOGSETFAILED = 'FailedOperation.CreateClsLogSetFailed'

# Failed to create the log topic: The topic/task name already exists.
FAILEDOPERATION_CREATECLSLOGTOPICTASKFAILED = 'FailedOperation.CreateClsLogTopicTaskFailed'

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

# System error.
INTERNALERROR_SYSTEMERROR = 'InternalError.SystemError'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# 
INVALIDPARAMETER_ACTIONINPROGRESS = 'InvalidParameter.ActionInProgress'

# The domain name does not exist or is not belong to this account.
INVALIDPARAMETER_DOMAINNOTFOUND = 'InvalidParameter.DomainNotFound'

# 
INVALIDPARAMETER_HOSTNOTFOUND = 'InvalidParameter.HostNotFound'

# 
INVALIDPARAMETER_INVALIDAUTHENTICATIONTYPESIGNPARAM = 'InvalidParameter.InvalidAuthenticationTypeSignParam'

# Invalid node cache.
INVALIDPARAMETER_INVALIDCACHEONLYONSWITCH = 'InvalidParameter.InvalidCacheOnlyOnSwitch'

# Incorrect certificate information.
INVALIDPARAMETER_INVALIDCERTINFO = 'InvalidParameter.InvalidCertInfo'

# Invalid client IP request header.
INVALIDPARAMETER_INVALIDCLIENTIPHEADERNAME = 'InvalidParameter.InvalidClientIpHeaderName'

# 
INVALIDPARAMETER_INVALIDDYNAMICROUTINE = 'InvalidParameter.InvalidDynamicRoutine'

# 
INVALIDPARAMETER_INVALIDERRORPAGEREDIRECTURL = 'InvalidParameter.InvalidErrorPageRedirectUrl'

# Invalid origin server.
INVALIDPARAMETER_INVALIDORIGIN = 'InvalidParameter.InvalidOrigin'

# 
INVALIDPARAMETER_INVALIDPARAMETER = 'InvalidParameter.InvalidParameter'

# The speciThe plan does not support limiting the max upload size.
INVALIDPARAMETER_INVALIDPOSTMAXSIZEBILLING = 'InvalidParameter.InvalidPostMaxSizeBilling'

# Invalid request header.
INVALIDPARAMETER_INVALIDREQUESTHEADERNAME = 'InvalidParameter.InvalidRequestHeaderName'

# You have not purchased a plan yet.
INVALIDPARAMETER_INVALIDRESOURCEIDBILLING = 'InvalidParameter.InvalidResourceIdBilling'

# 
INVALIDPARAMETER_INVALIDRULEENGINEACTION = 'InvalidParameter.InvalidRuleEngineAction'

# 
INVALIDPARAMETER_INVALIDRULEENGINENOTFOUND = 'InvalidParameter.InvalidRuleEngineNotFound'

# 
INVALIDPARAMETER_INVALIDRULEENGINETARGET = 'InvalidParameter.InvalidRuleEngineTarget'

# 
INVALIDPARAMETER_INVALIDRULEENGINETARGETSEXTENSION = 'InvalidParameter.InvalidRuleEngineTargetsExtension'

# 
INVALIDPARAMETER_INVALIDRULEENGINETARGETSURL = 'InvalidParameter.InvalidRuleEngineTargetsUrl'

# 
INVALIDPARAMETER_INVALIDURLREDIRECTHOST = 'InvalidParameter.InvalidUrlRedirectHost'

# The target URL for URL rewrite is invalid.
INVALIDPARAMETER_INVALIDURLREDIRECTURL = 'InvalidParameter.InvalidUrlRedirectUrl'

# Invalid WebSocket.
INVALIDPARAMETER_INVALIDWEBSOCKETTIMEOUT = 'InvalidParameter.InvalidWebSocketTimeout'

# Parameter error.
INVALIDPARAMETER_PARAMETERERROR = 'InvalidParameter.ParameterError'

# Invalid parameter.
INVALIDPARAMETER_SECURITY = 'InvalidParameter.Security'

# Incorrect domain name configuration.
INVALIDPARAMETER_SETTINGINVALIDPARAM = 'InvalidParameter.SettingInvalidParam'

# Resource error
INVALIDPARAMETER_TARGET = 'InvalidParameter.Target'

# Failed to create the task
INVALIDPARAMETER_TASKNOTGENERATED = 'InvalidParameter.TaskNotGenerated'

# Invalid file upload link.
INVALIDPARAMETER_UPLOADURL = 'InvalidParameter.UploadUrl'

# The site does not exist.
INVALIDPARAMETER_ZONENOTFOUND = 'InvalidParameter.ZoneNotFound'

# It conflicts with existing records.
INVALIDPARAMETERVALUE_CONFLICTRECORD = 'InvalidParameterValue.ConflictRecord'

# DNS records conflict with DNSSEC.
INVALIDPARAMETERVALUE_CONFLICTWITHDNSSEC = 'InvalidParameterValue.ConflictWithDNSSEC'

# This DNS record conflicts with CLB records.
INVALIDPARAMETERVALUE_CONFLICTWITHLBRECORD = 'InvalidParameterValue.ConflictWithLBRecord'

# This DNS record conflicts with NS records.
INVALIDPARAMETERVALUE_CONFLICTWITHNSRECORD = 'InvalidParameterValue.ConflictWithNSRecord'

# Incorrect DNS record
INVALIDPARAMETERVALUE_INVALIDDNSCONTENT = 'InvalidParameterValue.InvalidDNSContent'

# Incorrect DNS CNAME
INVALIDPARAMETERVALUE_INVALIDDNSNAME = 'InvalidParameterValue.InvalidDNSName'

# Incorrect DNS proxied domain name.
INVALIDPARAMETERVALUE_INVALIDPROXYNAME = 'InvalidParameterValue.InvalidProxyName'

# Incorrect DNS proxy
INVALIDPARAMETERVALUE_INVALIDPROXYORIGIN = 'InvalidParameterValue.InvalidProxyOrigin'

# This record already exists.
INVALIDPARAMETERVALUE_RECORDALREADYEXISTS = 'InvalidParameterValue.RecordAlreadyExists'

# This record cannot be added.
INVALIDPARAMETERVALUE_RECORDNOTALLOWED = 'InvalidParameterValue.RecordNotAllowed'

# The quota limit has been reached.
LIMITEXCEEDED = 'LimitExceeded'

# Reached the upper limit of resource number
LIMITEXCEEDED_BATCHQUOTA = 'LimitExceeded.BatchQuota'

# Reached the daily upper limit of resource number
LIMITEXCEEDED_DAILYQUOTA = 'LimitExceeded.DailyQuota'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# 
OPERATIONDENIED_DOMAINISBLOCKED = 'OperationDenied.DomainIsBlocked'

# The domain name doesn't have an ICP filing number.
OPERATIONDENIED_DOMAINNOICP = 'OperationDenied.DomainNoICP'

# Operation failed: The L4 proxy is blocked.
OPERATIONDENIED_L4PROXYINBANNEDSTATUS = 'OperationDenied.L4ProxyInBannedStatus'

# 
OPERATIONDENIED_MULTIPLECNAMEZONE = 'OperationDenied.MultipleCnameZone'

# The resource is occupied.
RESOURCEINUSE = 'ResourceInUse'

# 
RESOURCEINUSE_ALIASDOMAIN = 'ResourceInUse.AliasDomain'

# 
RESOURCEINUSE_CNAME = 'ResourceInUse.Cname'

# 
RESOURCEINUSE_DNS = 'ResourceInUse.Dns'

# 
RESOURCEINUSE_HOST = 'ResourceInUse.Host'

# 
RESOURCEINUSE_NS = 'ResourceInUse.NS'

# The resource has been connected to EdgeOne by another user.
RESOURCEINUSE_OTHERS = 'ResourceInUse.Others'

# 
RESOURCEINUSE_OTHERSALIASDOMAIN = 'ResourceInUse.OthersAliasDomain'

# 
RESOURCEINUSE_OTHERSCNAME = 'ResourceInUse.OthersCname'

# 
RESOURCEINUSE_OTHERSHOST = 'ResourceInUse.OthersHost'

# 
RESOURCEINUSE_OTHERSNS = 'ResourceInUse.OthersNS'

# 
RESOURCEINUSE_SELFANDOTHERSCNAME = 'ResourceInUse.SelfAndOthersCname'

# Insufficient resource.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The resource doesn’t exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# No domain names available.
RESOURCEUNAVAILABLE_AVAILABLEDOMAINNOTFOUND = 'ResourceUnavailable.AvailableDomainNotFound'

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

# Unknown parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
