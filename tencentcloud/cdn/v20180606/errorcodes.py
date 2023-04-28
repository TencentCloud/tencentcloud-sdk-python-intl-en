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


# Authentication error. Please check and try again.
AUTHFAILURE_INVALIDAUTHORIZATION = 'AuthFailure.InvalidAuthorization'

# Failed to update the domain name configuration. Please submit a ticket for troubleshooting.
FAILEDOPERATION_CDNCONFIGERROR = 'FailedOperation.CdnConfigError'

# Authentication system internal error.
INTERNALERROR_CAMSYSTEMERROR = 'InternalError.CamSystemError'

# Failed to update the domain name configuration.
INTERNALERROR_CDNCONFIGERROR = 'InternalError.CdnConfigError'

# Internal data error. Please submit a ticket for troubleshooting.
INTERNALERROR_CDNDBERROR = 'InternalError.CdnDbError'

# Internal error. Please try again or contact the customer service for assistance.
INTERNALERROR_CDNQUERYPARAMERROR = 'InternalError.CdnQueryParamError'

# Internal error. Please try again or contact the customer service for assistance.
INTERNALERROR_CDNQUERYSYSTEMERROR = 'InternalError.CdnQuerySystemError'

# System error. Please submit a ticket for troubleshooting.
INTERNALERROR_CDNSYSTEMERROR = 'InternalError.CdnSystemError'

# CLS internal error.
INTERNALERROR_CLSINTERNALERROR = 'InternalError.ClsInternalError'

# Billing data query internal error. Please submit a ticket for troubleshooting.
INTERNALERROR_COSTDATASYSTEMERROR = 'InternalError.CostDataSystemError'

# Error with the data query. Please submit a ticket for troubleshooting.
INTERNALERROR_DATASYSTEMERROR = 'InternalError.DataSystemError'

# Service internal error. Please submit a ticket for troubleshooting.
INTERNALERROR_ERROR = 'InternalError.Error'

# Service internal error. Please submit a ticket for troubleshooting.
INTERNALERROR_INVALIDERRORCODE = 'InternalError.InvalidErrorCode'

# Internal service error. Please submit a ticket for troubleshooting.
INTERNALERROR_PROXYSERVER = 'InternalError.ProxyServer'

# Internal service error. Please submit a ticket for troubleshooting.
INTERNALERROR_ROUTEERROR = 'InternalError.RouteError'

# The SCDN service is not activated. Please purchase or renew an SCDN packet and try again.
INTERNALERROR_SCDNUSERNOPACKAGE = 'InternalError.ScdnUserNoPackage'

# Your SCDN service is suspended. Please purchase a new SCDN packet.
INTERNALERROR_SCDNUSERSUSPEND = 'InternalError.ScdnUserSuspend'

# Tag internal error. Please submit a ticket for troubleshooting.
INTERNALERROR_TAGSYSTEMERROR = 'InternalError.TagSystemError'

# The access port 443 must be enabled for HTTPS configuration.
INVALIDPARAMETER_ACCESSPORTOPENEDHTTPS = 'InvalidParameter.AccessPortOpenedHttps'

# Please delete the rate limiting configuration before you switch the acceleration region.
INVALIDPARAMETER_BANDLIMITREQUIREDMAINLAND = 'InvalidParameter.BandLimitRequiredMainland'

# Tencent Cloud COS and third-party object storage origins only support "Return 404". Please modify and try again.
INVALIDPARAMETER_BANDWIDTHALERTCOUNTERMEASURECONFLICTORIGINTYPE = 'InvalidParameter.BandwidthAlertCounterMeasureConflictOriginType'

# Invalid domain name status.
INVALIDPARAMETER_CDNSTATUSINVALIDDOMAIN = 'InvalidParameter.CDNStatusInvalidDomain'

# Inconsistent resource AppID.
INVALIDPARAMETER_CAMRESOURCEBELONGTODIFFERENTUSER = 'InvalidParameter.CamResourceBelongToDifferentUser'

# Incorrect six-segment resource parameter.
INVALIDPARAMETER_CAMRESOURCESIXSTAGEERROR = 'InvalidParameter.CamResourceSixStageError'

# The domain name has already been associated with this tag.
INVALIDPARAMETER_CAMTAGKEYALREADYATTACHED = 'InvalidParameter.CamTagKeyAlreadyAttached'

# Invalid characters in the tag key.
INVALIDPARAMETER_CAMTAGKEYILLEGAL = 'InvalidParameter.CamTagKeyIllegal'

# The tag key does not exist.
INVALIDPARAMETER_CAMTAGKEYNOTEXIST = 'InvalidParameter.CamTagKeyNotExist'

# Invalid characters in the tag value.
INVALIDPARAMETER_CAMTAGVALUEILLEGAL = 'InvalidParameter.CamTagValueIllegal'

# The certificate information is invalid or does not exist. Please check and try again.
INVALIDPARAMETER_CDNCERTINFONOTFOUND = 'InvalidParameter.CdnCertInfoNotFound'

# Invalid certificate. Please check and try again.
INVALIDPARAMETER_CDNCERTNOCERTINFO = 'InvalidParameter.CdnCertNoCertInfo'

# Invalid HTTPS certificate.
INVALIDPARAMETER_CDNCERTNOTPEM = 'InvalidParameter.CdnCertNotPem'

# A duplicate topic is found.
INVALIDPARAMETER_CDNCLSDUPLICATETOPIC = 'InvalidParameter.CdnClsDuplicateTopic'

# Invalid topic name.
INVALIDPARAMETER_CDNCLSTOPICNAMEINVALID = 'InvalidParameter.CdnClsTopicNameInvalid'

# The CLS topic does not exist.
INVALIDPARAMETER_CDNCLSTOPICNOTEXIST = 'InvalidParameter.CdnClsTopicNotExist'

# Invalid cache configuration. Please check and try again.
INVALIDPARAMETER_CDNCONFIGINVALIDCACHE = 'InvalidParameter.CdnConfigInvalidCache'

# Invalid domain name. Please make sure the domain name is valid.
INVALIDPARAMETER_CDNCONFIGINVALIDHOST = 'InvalidParameter.CdnConfigInvalidHost'

# Invalid tag configuration.
INVALIDPARAMETER_CDNCONFIGINVALIDTAG = 'InvalidParameter.CdnConfigInvalidTag'

# Failed to add the domain name. Please make sure to specify a tag for the domain name.
INVALIDPARAMETER_CDNCONFIGTAGREQUIRED = 'InvalidParameter.CdnConfigTagRequired'

# The domain name is configured with special configurations, please submit a ticket.
INVALIDPARAMETER_CDNHOSTHASSPECIALCONFIG = 'InvalidParameter.CdnHostHasSpecialConfig'

# This domain name belongs to another account. You are not allowed o connect it to CDN.
INVALIDPARAMETER_CDNHOSTINTERNALHOST = 'InvalidParameter.CdnHostInternalHost'

# Incorrect intermediate server configuration.
INVALIDPARAMETER_CDNHOSTINVALIDMIDDLECONFIG = 'InvalidParameter.CdnHostInvalidMiddleConfig'

# Invalid domain name format. Please check and try again.
INVALIDPARAMETER_CDNHOSTINVALIDPARAM = 'InvalidParameter.CdnHostInvalidParam'

# Invalid domain name status.
INVALIDPARAMETER_CDNHOSTINVALIDSTATUS = 'InvalidParameter.CdnHostInvalidStatus'

# It is a COS origin domain name. Please go to the COS console to enable "Default CDN Acceleration Domain".
INVALIDPARAMETER_CDNHOSTISCOSDEFAULTACCESS = 'InvalidParameter.CdnHostIsCosDefaultAccess'

# The domain name is too long.
INVALIDPARAMETER_CDNHOSTTOOLONGHOST = 'InvalidParameter.CdnHostTooLongHost'

# Internal API error. Please submit a ticket for troubleshooting.
INVALIDPARAMETER_CDNINTERFACEERROR = 'InvalidParameter.CdnInterfaceError'

# Parameter error: Interval. Please check and try again.
INVALIDPARAMETER_CDNINVALIDPARAMINTERVAL = 'InvalidParameter.CdnInvalidParamInterval'

# Parameter error: Metric. Please check and try again.
INVALIDPARAMETER_CDNINVALIDPARAMMETRIC = 'InvalidParameter.CdnInvalidParamMetric'

# Invalid field: ServiceType. Please check and try again.
INVALIDPARAMETER_CDNINVALIDPARAMSERVICETYPE = 'InvalidParameter.CdnInvalidParamServiceType'

# The configuration is not supported.
INVALIDPARAMETER_CDNKEYRULESEXCLUDECUSTOMREQUIRESFULLLEGO = 'InvalidParameter.CdnKeyRulesExcludeCustomRequiresFullLego'

# Invalid field: QueryString. Please check and try again.
INVALIDPARAMETER_CDNKEYRULESINVALIDQUERYSTRINGVALUE = 'InvalidParameter.CdnKeyRulesInvalidQueryStringValue'

# Parameter error. Please see the sample parameters in the documentation.
INVALIDPARAMETER_CDNPARAMERROR = 'InvalidParameter.CdnParamError'

# Cache purge does not support wildcard domain names.
INVALIDPARAMETER_CDNPURGEWILDCARDNOTALLOWED = 'InvalidParameter.CdnPurgeWildcardNotAllowed'

# Prefetch does not support wildcard domain names.
INVALIDPARAMETER_CDNPUSHWILDCARDNOTALLOWED = 'InvalidParameter.CdnPushWildcardNotAllowed'

# Invalid date. Please see the sample date in the documentation.
INVALIDPARAMETER_CDNSTATINVALIDDATE = 'InvalidParameter.CdnStatInvalidDate'

# Invalid statistical dimension. Please see the sample statistical analysis in the documentation.
INVALIDPARAMETER_CDNSTATINVALIDFILTER = 'InvalidParameter.CdnStatInvalidFilter'

# Invalid statistical type. Please see the sample statistical analysis in the documentation.
INVALIDPARAMETER_CDNSTATINVALIDMETRIC = 'InvalidParameter.CdnStatInvalidMetric'

# Incorrect project ID. Please check and try again.
INVALIDPARAMETER_CDNSTATINVALIDPROJECTID = 'InvalidParameter.CdnStatInvalidProjectId'

# The number of queried domain names reached the limit.
INVALIDPARAMETER_CDNSTATTOOMANYDOMAINS = 'InvalidParameter.CdnStatTooManyDomains'

# The URL exceeds the length limit.
INVALIDPARAMETER_CDNURLEXCEEDLENGTH = 'InvalidParameter.CdnUrlExceedLength'

# Index conflict.
INVALIDPARAMETER_CLSINDEXCONFLICT = 'InvalidParameter.ClsIndexConflict'

# The index rule is empty.
INVALIDPARAMETER_CLSINDEXRULEEMPTY = 'InvalidParameter.ClsIndexRuleEmpty'

# Invalid content.
INVALIDPARAMETER_CLSINVALIDCONTENT = 'InvalidParameter.ClsInvalidContent'

# Invalid `Content-Type`.
INVALIDPARAMETER_CLSINVALIDCONTENTTYPE = 'InvalidParameter.ClsInvalidContentType'

# Parameter error. Please check and try again.
INVALIDPARAMETER_CLSINVALIDPARAM = 'InvalidParameter.ClsInvalidParam'

# Logset conflict.
INVALIDPARAMETER_CLSLOGSETCONFLICT = 'InvalidParameter.ClsLogsetConflict'

# The logset is empty.
INVALIDPARAMETER_CLSLOGSETEMPTY = 'InvalidParameter.ClsLogsetEmpty'

# The logset is not empty.
INVALIDPARAMETER_CLSLOGSETNOTEMPTY = 'InvalidParameter.ClsLogsetNotEmpty'

# No authorization information.
INVALIDPARAMETER_CLSMISSINGAUTHORIZATION = 'InvalidParameter.ClsMissingAuthorization'

# Lost content.
INVALIDPARAMETER_CLSMISSINGCONTENT = 'InvalidParameter.ClsMissingContent'

# Syntax error.
INVALIDPARAMETER_CLSSYNTAXERROR = 'InvalidParameter.ClsSyntaxError'

# The topic has been closed.
INVALIDPARAMETER_CLSTOPICCLOSED = 'InvalidParameter.ClsTopicClosed'

# Topic conflict.
INVALIDPARAMETER_CLSTOPICCONFLICT = 'InvalidParameter.ClsTopicConflict'

# API internal error. Please try again or contact the customer service for assistance.
INVALIDPARAMETER_ECDNINTERFACEERROR = 'InvalidParameter.EcdnInterfaceError'

# The maximum number of regex sub-patterns is exceeded.
INVALIDPARAMETER_PATHREGEXTOOMANYSUBPATTERN = 'InvalidParameter.PathRegexTooManySubPattern'

# This platform does not support remote authentication.
INVALIDPARAMETER_REMOTEAUTHINVALIDPLATFORM = 'InvalidParameter.RemoteAuthInvalidPlatform'

# This platform does not support remote access to an authentication address via the HTTPS protocol.
INVALIDPARAMETER_REMOTEAUTHINVALIDPROTOCOL = 'InvalidParameter.RemoteAuthInvalidProtocol'

# Unable to recreate: the task has expired.
INVALIDPARAMETER_SCDNLOGTASKEXPIRED = 'InvalidParameter.ScdnLogTaskExpired'

# The task does not exist or was not failed.
INVALIDPARAMETER_SCDNLOGTASKNOTFOUNDORNOTFAIL = 'InvalidParameter.ScdnLogTaskNotFoundOrNotFail'

# Incorrect time range
INVALIDPARAMETER_SCDNLOGTASKTIMERANGEINVALID = 'InvalidParameter.ScdnLogTaskTimeRangeInvalid'

# The number of resource arrays exceeds the upper limit.
LIMITEXCEEDED_CAMRESOURCEARRAYTOOLONG = 'LimitExceeded.CamResourceArrayTooLong'

# The number of tag keys exceeds the upper limit. Each resource can have up to 50 tag keys.
LIMITEXCEEDED_CAMRESOURCETOOMANYTAGKEY = 'LimitExceeded.CamResourceTooManyTagKey'

# The tag key length exceeds the upper limit.
LIMITEXCEEDED_CAMTAGKEYTOOLONG = 'LimitExceeded.CamTagKeyTooLong'

# The number of tag values exceeds the upper limit. Each tag key can have up to 1,000 tag values.
LIMITEXCEEDED_CAMTAGKEYTOOMANYTAGVALUE = 'LimitExceeded.CamTagKeyTooManyTagValue'

# The number of bound tags exceeds the limit.
LIMITEXCEEDED_CAMTAGQUOTAEXCEEDLIMIT = 'LimitExceeded.CamTagQuotaExceedLimit'

# The number of keys exceeds the upper limit. Each user can have up to 1,000 different keys.
LIMITEXCEEDED_CAMUSERTOOMANYTAGKEY = 'LimitExceeded.CamUserTooManyTagKey'

# Too frequent queries on IP ownership.
LIMITEXCEEDED_CDNCALLINGQUERYIPTOOOFTEN = 'LimitExceeded.CdnCallingQueryIpTooOften'

# This account has created too many topics.
LIMITEXCEEDED_CDNCLSTOOMANYTOPICS = 'LimitExceeded.CdnClsTooManyTopics'

# The number of cache validity configuration rules exceeds the limit.
LIMITEXCEEDED_CDNCONFIGTOOMANYCACHERULES = 'LimitExceeded.CdnConfigTooManyCacheRules'

# Domain name operations are too frequent.
LIMITEXCEEDED_CDNHOSTOPTOOOFTEN = 'LimitExceeded.CdnHostOpTooOften'

# The number of directories to be purged exceeds the limit.
LIMITEXCEEDED_CDNPURGEPATHEXCEEDBATCHLIMIT = 'LimitExceeded.CdnPurgePathExceedBatchLimit'

# The number of directories to be purged exceeds the daily limit.
LIMITEXCEEDED_CDNPURGEPATHEXCEEDDAYLIMIT = 'LimitExceeded.CdnPurgePathExceedDayLimit'

# The number of URLs to be purged exceeds the limit.
LIMITEXCEEDED_CDNPURGEURLEXCEEDBATCHLIMIT = 'LimitExceeded.CdnPurgeUrlExceedBatchLimit'

# The number of URLs to be purged exceeds the daily limit.
LIMITEXCEEDED_CDNPURGEURLEXCEEDDAYLIMIT = 'LimitExceeded.CdnPurgeUrlExceedDayLimit'

# The number of URLs to be prefetched at a time exceeds the limit.
LIMITEXCEEDED_CDNPUSHEXCEEDBATCHLIMIT = 'LimitExceeded.CdnPushExceedBatchLimit'

# The number of URLs to be prefetched exceeds the daily limit.
LIMITEXCEEDED_CDNPUSHEXCEEDDAYLIMIT = 'LimitExceeded.CdnPushExceedDayLimit'

# The number of IPs to be queried exceeds the limit.
LIMITEXCEEDED_CDNQUERYIPBATCHTOOMANY = 'LimitExceeded.CdnQueryIpBatchTooMany'

# The number of domain names under the account has reached the upper limit. Please submit a ticket for assistance.
LIMITEXCEEDED_CDNUSERTOOMANYHOSTS = 'LimitExceeded.CdnUserTooManyHosts'

# The log size exceeds the limit.
LIMITEXCEEDED_CLSLOGSIZEEXCEED = 'LimitExceeded.ClsLogSizeExceed'

# The number of logsets exceeds the limit.
LIMITEXCEEDED_CLSLOGSETEXCEED = 'LimitExceeded.ClsLogsetExceed'

# The number of topics exceeds the limit.
LIMITEXCEEDED_CLSTOPICEXCEED = 'LimitExceeded.ClsTopicExceed'

# Daily task quota exceeded
LIMITEXCEEDED_SCDNLOGTASKEXCEEDDAYLIMIT = 'LimitExceeded.ScdnLogTaskExceedDayLimit'

# The domain name conflicts with an existing domain name in the system.
RESOURCEINUSE_CDNCONFLICTHOSTEXISTS = 'ResourceInUse.CdnConflictHostExists'

# Domain name already exists.
RESOURCEINUSE_CDNHOSTEXISTS = 'ResourceInUse.CdnHostExists'

# CDN resources are being operated.
RESOURCEINUSE_CDNOPINPROGRESS = 'ResourceInUse.CdnOpInProgress'

# The tag key does not exist.
RESOURCENOTFOUND_CAMTAGKEYNOTEXIST = 'ResourceNotFound.CamTagKeyNotExist'

# Unable to find the domain name. Please make sure the domain name is correct.
RESOURCENOTFOUND_CDNHOSTNOTEXISTS = 'ResourceNotFound.CdnHostNotExists'

# The project does not exist. Please check and try again.
RESOURCENOTFOUND_CDNPROJECTNOTEXISTS = 'ResourceNotFound.CdnProjectNotExists'

# The CDN service has not been activated. Please activate it first before using this API.
RESOURCENOTFOUND_CDNUSERNOTEXISTS = 'ResourceNotFound.CdnUserNotExists'

# The number of domain names under the account has reached the upper limit. Please submit a ticket for assistance.
RESOURCENOTFOUND_CDNUSERTOOMANYHOSTS = 'ResourceNotFound.CdnUserTooManyHosts'

# The index does not exist.
RESOURCENOTFOUND_CLSINDEXNOTEXIST = 'ResourceNotFound.ClsIndexNotExist'

# The logset does not exist.
RESOURCENOTFOUND_CLSLOGSETNOTEXIST = 'ResourceNotFound.ClsLogsetNotExist'

# The topic does not exist.
RESOURCENOTFOUND_CLSTOPICNOTEXIST = 'ResourceNotFound.ClsTopicNotExist'

# The domain name does not exist. Please check and try again.
RESOURCENOTFOUND_ECDNDOMAINNOTEXISTS = 'ResourceNotFound.EcdnDomainNotExists'

# The domain name has been connected to the Mainland China service region. If you need to switch the service region to "Global", please verify its ownership for domain name retrieval.
RESOURCEUNAVAILABLE_CDNHOSTBELONGSTOOTHERSINMAINLAND = 'ResourceUnavailable.CdnHostBelongsToOthersInMainland'

# The domain name has been connected to the service region outside Mainland China. If you need to switch the service region to "Global", please verify its ownership for domain name retrieval.
RESOURCEUNAVAILABLE_CDNHOSTBELONGSTOOTHERSINOVERSEAS = 'ResourceUnavailable.CdnHostBelongsToOthersInOverseas'

# The DSA feature is enabled for the domain name.
RESOURCEUNAVAILABLE_CDNHOSTEXISTSINDSA = 'ResourceUnavailable.CdnHostExistsInDsa'

# The domain name has been connected in the TCB console.
RESOURCEUNAVAILABLE_CDNHOSTEXISTSINTCB = 'ResourceUnavailable.CdnHostExistsInTcb'

# The domain name is locked.
RESOURCEUNAVAILABLE_CDNHOSTISLOCKED = 'ResourceUnavailable.CdnHostIsLocked'

# The domain name is not compliant and cannot be connected.
RESOURCEUNAVAILABLE_CDNHOSTISMALICIOUS = 'ResourceUnavailable.CdnHostIsMalicious'

# Domain name is still in use.
RESOURCEUNAVAILABLE_CDNHOSTISNOTOFFLINE = 'ResourceUnavailable.CdnHostIsNotOffline'

# The domain name has been deactivated. Prefetch requests cannot be submitted.
RESOURCEUNAVAILABLE_CDNHOSTISNOTONLINE = 'ResourceUnavailable.CdnHostIsNotOnline'

# ICP filing is required for the domain name and the synchronization takes 2 hours. If it is already filed, please try later.
RESOURCEUNAVAILABLE_CDNHOSTNOICP = 'ResourceUnavailable.CdnHostNoIcp'

# The domain name has been connected to VOD. To access CDN, please delete it from VOD first.
RESOURCEUNAVAILABLE_HOSTEXISTINVOD = 'ResourceUnavailable.HostExistInVod'

# The SCDN service is not activated. Please purchase or renew an SCDN packet and try again.
RESOURCEUNAVAILABLE_SCDNUSERNOPACKAGE = 'ResourceUnavailable.ScdnUserNoPackage'

# The sub-account is unauthorized to query full data.
UNAUTHORIZEDOPERATION_CDNACCOUNTUNAUTHORIZED = 'UnauthorizedOperation.CdnAccountUnauthorized'

# No CAM policy is configured for the sub-account.
UNAUTHORIZEDOPERATION_CDNCAMUNAUTHORIZED = 'UnauthorizedOperation.CdnCamUnauthorized'

# This account is not authorized to activate CLS.
UNAUTHORIZEDOPERATION_CDNCLSNOTREGISTERED = 'UnauthorizedOperation.CdnClsNotRegistered'

# The domain name has not been verified.
UNAUTHORIZEDOPERATION_CDNDOMAINRECORDNOTVERIFIED = 'UnauthorizedOperation.CdnDomainRecordNotVerified'

# The domain name already exists in the system. Please submit a ticket.
UNAUTHORIZEDOPERATION_CDNHOSTEXISTSININTERNAL = 'UnauthorizedOperation.CdnHostExistsInInternal'

# The domain name is not compliant and cannot be connected.
UNAUTHORIZEDOPERATION_CDNHOSTINICPBLACKLIST = 'UnauthorizedOperation.CdnHostInIcpBlacklist'

# This domain name belongs to another account, and you do not have permission to connect it.
UNAUTHORIZEDOPERATION_CDNHOSTISOWNEDBYOTHER = 'UnauthorizedOperation.CdnHostIsOwnedByOther'

# The domain name has been connected by another account. For more information, please submit a ticket.
UNAUTHORIZEDOPERATION_CDNHOSTISUSEDBYOTHER = 'UnauthorizedOperation.CdnHostIsUsedByOther'

# The sub-account has no access to the CDN-accelerated domain name.
UNAUTHORIZEDOPERATION_CDNHOSTUNAUTHORIZED = 'UnauthorizedOperation.CdnHostUnauthorized'

# The project is not authorized for the sub-account.
UNAUTHORIZEDOPERATION_CDNPROJECTUNAUTHORIZED = 'UnauthorizedOperation.CdnProjectUnauthorized'

# The sub-account has no access to the tag.
UNAUTHORIZEDOPERATION_CDNTAGUNAUTHORIZED = 'UnauthorizedOperation.CdnTagUnauthorized'

# Fail to authenticate the CDN user.
UNAUTHORIZEDOPERATION_CDNUSERAUTHFAIL = 'UnauthorizedOperation.CdnUserAuthFail'

# The CDN user is pending authentication.
UNAUTHORIZEDOPERATION_CDNUSERAUTHWAIT = 'UnauthorizedOperation.CdnUserAuthWait'

# Service internal error. Please submit a ticket for troubleshooting.
UNAUTHORIZEDOPERATION_CDNUSERINVALIDCREDENTIAL = 'UnauthorizedOperation.CdnUserInvalidCredential'

# The account has been isolated due to arrears. Please pay the bill and try again.
UNAUTHORIZEDOPERATION_CDNUSERISISOLATED = 'UnauthorizedOperation.CdnUserIsIsolated'

# The CDN service has been suspended. Please restart it and try again.
UNAUTHORIZEDOPERATION_CDNUSERISSUSPENDED = 'UnauthorizedOperation.CdnUserIsSuspended'

# You are not in the beta whitelist and thus have no permission to use this function.
UNAUTHORIZEDOPERATION_CDNUSERNOWHITELIST = 'UnauthorizedOperation.CdnUserNoWhitelist'

# Invalid authorization.
UNAUTHORIZEDOPERATION_CLSINVALIDAUTHORIZATION = 'UnauthorizedOperation.ClsInvalidAuthorization'

# You have not activated CLS service. Please activate it in the CLS console first.
UNAUTHORIZEDOPERATION_CLSSERVICENOTACTIVATED = 'UnauthorizedOperation.ClsServiceNotActivated'

# Authorization failed.
UNAUTHORIZEDOPERATION_CLSUNAUTHORIZED = 'UnauthorizedOperation.ClsUnauthorized'

# Service internal error. Please submit a ticket for troubleshooting.
UNAUTHORIZEDOPERATION_CSRFERROR = 'UnauthorizedOperation.CsrfError'

# Please go to the CDN console for operation.
UNAUTHORIZEDOPERATION_ECDNMIGRATEDCDN = 'UnauthorizedOperation.EcdnMigratedCdn'

# This operation is not supported currently. Please submit a ticket for assistance.
UNAUTHORIZEDOPERATION_OPNOAUTH = 'UnauthorizedOperation.OpNoAuth'

# Too many calling attempts.
UNAUTHORIZEDOPERATION_OPERATIONTOOOFTEN = 'UnauthorizedOperation.OperationTooOften'

# The operation is not allowed.
UNSUPPORTEDOPERATION_CLSNOTALLOWED = 'UnsupportedOperation.ClsNotAllowed'

# This operation is not supported currently. Please submit a ticket for assistance.
UNSUPPORTEDOPERATION_OPNOAUTH = 'UnsupportedOperation.OpNoAuth'
