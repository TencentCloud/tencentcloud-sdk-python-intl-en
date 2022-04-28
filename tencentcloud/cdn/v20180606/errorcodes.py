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

# Failed to update the domain name configuration. Please try again or contact customer service.
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

# Internal error. Please try again or contact the customer service for assistance.
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

# Internal error. Please try again or contact the customer service for assistance.
INTERNALERROR_TAGSYSTEMERROR = 'InternalError.TagSystemError'

# Invalid domain name status.
INVALIDPARAMETER_CDNSTATUSINVALIDDOMAIN = 'InvalidParameter.CDNStatusInvalidDomain'

# Incorrect intermediate server configuration.
INVALIDPARAMETER_CDNHOSTINVALIDMIDDLECONFIG = 'InvalidParameter.CdnHostInvalidMiddleConfig'

# Invalid domain name format. Please check and try again.
INVALIDPARAMETER_CDNHOSTINVALIDPARAM = 'InvalidParameter.CdnHostInvalidParam'

# Invalid domain name status.
INVALIDPARAMETER_CDNHOSTINVALIDSTATUS = 'InvalidParameter.CdnHostInvalidStatus'

# Internal API error. Please submit a ticket for troubleshooting.
INVALIDPARAMETER_CDNINTERFACEERROR = 'InvalidParameter.CdnInterfaceError'

# The parameter “Metric” is wrong. Please check and try again.
INVALIDPARAMETER_CDNINVALIDPARAMMETRIC = 'InvalidParameter.CdnInvalidParamMetric'

# Parameter error. Please see the sample parameters in the documentation.
INVALIDPARAMETER_CDNPARAMERROR = 'InvalidParameter.CdnParamError'

# Cache purge does not support wildcard domain names.
INVALIDPARAMETER_CDNPURGEWILDCARDNOTALLOWED = 'InvalidParameter.CdnPurgeWildcardNotAllowed'

# Prefetch does not support wildcard domain names.
INVALIDPARAMETER_CDNPUSHWILDCARDNOTALLOWED = 'InvalidParameter.CdnPushWildcardNotAllowed'

# Invalid date. Please see the sample date in the documentation.
INVALIDPARAMETER_CDNSTATINVALIDDATE = 'InvalidParameter.CdnStatInvalidDate'

# Invalid statistical type. Please see the sample statistical analysis in the documentation.
INVALIDPARAMETER_CDNSTATINVALIDMETRIC = 'InvalidParameter.CdnStatInvalidMetric'

# Incorrect project ID. Please check and try again.
INVALIDPARAMETER_CDNSTATINVALIDPROJECTID = 'InvalidParameter.CdnStatInvalidProjectId'

# The number of queried domain names reached the limit.
INVALIDPARAMETER_CDNSTATTOOMANYDOMAINS = 'InvalidParameter.CdnStatTooManyDomains'

# The URL exceeds the length limit.
INVALIDPARAMETER_CDNURLEXCEEDLENGTH = 'InvalidParameter.CdnUrlExceedLength'

# API internal error. Please try again or contact the customer service for assistance.
INVALIDPARAMETER_ECDNINTERFACEERROR = 'InvalidParameter.EcdnInterfaceError'

# Unable to recreate: the task has expired.
INVALIDPARAMETER_SCDNLOGTASKEXPIRED = 'InvalidParameter.ScdnLogTaskExpired'

# The task does not exist or was not failed.
INVALIDPARAMETER_SCDNLOGTASKNOTFOUNDORNOTFAIL = 'InvalidParameter.ScdnLogTaskNotFoundOrNotFail'

# Incorrect time range
INVALIDPARAMETER_SCDNLOGTASKTIMERANGEINVALID = 'InvalidParameter.ScdnLogTaskTimeRangeInvalid'

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

# Daily task quota exceeded
LIMITEXCEEDED_SCDNLOGTASKEXCEEDDAYLIMIT = 'LimitExceeded.ScdnLogTaskExceedDayLimit'

# CDN resources are being operated.
RESOURCEINUSE_CDNOPINPROGRESS = 'ResourceInUse.CdnOpInProgress'

# This domain name does not exist under the account. Please check and try again.
RESOURCENOTFOUND_CDNHOSTNOTEXISTS = 'ResourceNotFound.CdnHostNotExists'

# The project does not exist. Please check and try again.
RESOURCENOTFOUND_CDNPROJECTNOTEXISTS = 'ResourceNotFound.CdnProjectNotExists'

# The CDN service has not been activated. Please activate it first before using this API.
RESOURCENOTFOUND_CDNUSERNOTEXISTS = 'ResourceNotFound.CdnUserNotExists'

# The number of accessed domain names reached the limit.
RESOURCENOTFOUND_CDNUSERTOOMANYHOSTS = 'ResourceNotFound.CdnUserTooManyHosts'

# The domain name is locked.
RESOURCEUNAVAILABLE_CDNHOSTISLOCKED = 'ResourceUnavailable.CdnHostIsLocked'

# The domain name has been deactivated. Prefetch requests cannot be submitted.
RESOURCEUNAVAILABLE_CDNHOSTISNOTONLINE = 'ResourceUnavailable.CdnHostIsNotOnline'

# The sub-account is unauthorized to query full data.
UNAUTHORIZEDOPERATION_CDNACCOUNTUNAUTHORIZED = 'UnauthorizedOperation.CdnAccountUnauthorized'

# No CAM policy is configured for the sub-account.
UNAUTHORIZEDOPERATION_CDNCAMUNAUTHORIZED = 'UnauthorizedOperation.CdnCamUnauthorized'

# The sub-account has no access to the CDN-accelerated domain name.
UNAUTHORIZEDOPERATION_CDNHOSTUNAUTHORIZED = 'UnauthorizedOperation.CdnHostUnauthorized'

# The sub-account has no access to the project.
UNAUTHORIZEDOPERATION_CDNPROJECTUNAUTHORIZED = 'UnauthorizedOperation.CdnProjectUnauthorized'

# The sub-account has no access to the tag.
UNAUTHORIZEDOPERATION_CDNTAGUNAUTHORIZED = 'UnauthorizedOperation.CdnTagUnauthorized'

# Fail to authenticate the CDN user.
UNAUTHORIZEDOPERATION_CDNUSERAUTHFAIL = 'UnauthorizedOperation.CdnUserAuthFail'

# The CDN user is pending authentication.
UNAUTHORIZEDOPERATION_CDNUSERAUTHWAIT = 'UnauthorizedOperation.CdnUserAuthWait'

# The CDN service has been suspended. Please restart it and try again.
UNAUTHORIZEDOPERATION_CDNUSERISSUSPENDED = 'UnauthorizedOperation.CdnUserIsSuspended'

# You are not in the beta whitelist and thus have no permission to use this function.
UNAUTHORIZEDOPERATION_CDNUSERNOWHITELIST = 'UnauthorizedOperation.CdnUserNoWhitelist'

# Service internal error. Please submit a ticket for troubleshooting.
UNAUTHORIZEDOPERATION_CSRFERROR = 'UnauthorizedOperation.CsrfError'

# Please go to the CDN console for operation.
UNAUTHORIZEDOPERATION_ECDNMIGRATEDCDN = 'UnauthorizedOperation.EcdnMigratedCdn'

# This operation is not supported currently. Please submit a ticket for assistance.
UNAUTHORIZEDOPERATION_OPNOAUTH = 'UnauthorizedOperation.OpNoAuth'

# Too many calling attempts.
UNAUTHORIZEDOPERATION_OPERATIONTOOOFTEN = 'UnauthorizedOperation.OperationTooOften'
