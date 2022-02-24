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


# Failed to update the domain name configuration. Please try again or contact customer service for assistance.
FAILEDOPERATION_ECDNCONFIGERROR = 'FailedOperation.EcdnConfigError'

# Internal configuration service error. Please try again later or contact the customer service for assistance.
INTERNALERROR_ECDNCONFIGERROR = 'InternalError.EcdnConfigError'

# Internal data error. Please submit a ticket for troubleshooting.
INTERNALERROR_ECDNDBERROR = 'InternalError.EcdnDbError'

# System error. Please submit a ticket for troubleshooting.
INTERNALERROR_ECDNSYSTEMERROR = 'InternalError.EcdnSystemError'

# Backend service error. Please try again later.
INTERNALERROR_PROXYSERVER = 'InternalError.ProxyServer'

# The tag key does not exist.
INVALIDPARAMETER_ECDNCAMTAGKEYNOTEXIST = 'InvalidParameter.EcdnCamTagKeyNotExist'

# Unable to resolve the certificate information.
INVALIDPARAMETER_ECDNCERTNOCERTINFO = 'InvalidParameter.EcdnCertNoCertInfo'

# The cache configuration is invalid.
INVALIDPARAMETER_ECDNCONFIGINVALIDCACHE = 'InvalidParameter.EcdnConfigInvalidCache'

# Invalid domain name status.
INVALIDPARAMETER_ECDNDOMAININVALIDSTATUS = 'InvalidParameter.EcdnDomainInvalidStatus'

# Internal API error. Please submit a ticket for troubleshooting.
INVALIDPARAMETER_ECDNINTERFACEERROR = 'InvalidParameter.EcdnInterfaceError'

# Invalid `Area` parameter. Please see the sample parameters in the documentation.
INVALIDPARAMETER_ECDNINVALIDPARAMAREA = 'InvalidParameter.EcdnInvalidParamArea'

# Invalid statistical granularity. Please see the sample statistical analysis in the documentation.
INVALIDPARAMETER_ECDNINVALIDPARAMINTERVAL = 'InvalidParameter.EcdnInvalidParamInterval'

# Parameter error. Please see the sample parameters in the documentation.
INVALIDPARAMETER_ECDNPARAMERROR = 'InvalidParameter.EcdnParamError'

# Wildcard domain names are not supported for purging.
INVALIDPARAMETER_ECDNPURGEWILDCARDNOTALLOWED = 'InvalidParameter.EcdnPurgeWildcardNotAllowed'

# This domain name binds too many tag keys.
INVALIDPARAMETER_ECDNRESOURCEMANYTAGKEY = 'InvalidParameter.EcdnResourceManyTagKey'

# Invalid date. Please see the sample date in the documentation.
INVALIDPARAMETER_ECDNSTATINVALIDDATE = 'InvalidParameter.EcdnStatInvalidDate'

# Invalid statistical type. Please see the sample statistical analysis in the documentation.
INVALIDPARAMETER_ECDNSTATINVALIDMETRIC = 'InvalidParameter.EcdnStatInvalidMetric'

# Invalid tag key.
INVALIDPARAMETER_ECDNTAGKEYINVALID = 'InvalidParameter.EcdnTagKeyInvalid'

# The tag key does not exist.
INVALIDPARAMETER_ECDNTAGKEYNOTEXIST = 'InvalidParameter.EcdnTagKeyNotExist'

# The tag key has too many values.
INVALIDPARAMETER_ECDNTAGKEYTOOMANYVALUE = 'InvalidParameter.EcdnTagKeyTooManyValue'

# Invalid tag value.
INVALIDPARAMETER_ECDNTAGVALUEINVALID = 'InvalidParameter.EcdnTagValueInvalid'

# The URL length exceeds the limit.
INVALIDPARAMETER_ECDNURLEXCEEDLENGTH = 'InvalidParameter.EcdnUrlExceedLength'

# This user has too many tag keys.
INVALIDPARAMETER_ECDNUSERTOOMANYTAGKEY = 'InvalidParameter.EcdnUserTooManyTagKey'

# Parameter error
INVALIDPARAMETER_PARAMERROR = 'InvalidParameter.ParamError'

# Domain name operations are too frequent.
LIMITEXCEEDED_ECDNDOMAINOPTOOOFTEN = 'LimitExceeded.EcdnDomainOpTooOften'

# The number of directories to be purged exceeded the limit on one request.
LIMITEXCEEDED_ECDNPURGEPATHEXCEEDBATCHLIMIT = 'LimitExceeded.EcdnPurgePathExceedBatchLimit'

# The number of directories to be purged exceeded the daily limit.
LIMITEXCEEDED_ECDNPURGEPATHEXCEEDDAYLIMIT = 'LimitExceeded.EcdnPurgePathExceedDayLimit'

# The number of URLs to be purged exceeded the limit on one request.
LIMITEXCEEDED_ECDNPURGEURLEXCEEDBATCHLIMIT = 'LimitExceeded.EcdnPurgeUrlExceedBatchLimit'

# The number of URLs to be purged exceeded the daily quota.
LIMITEXCEEDED_ECDNPURGEURLEXCEEDDAYLIMIT = 'LimitExceeded.EcdnPurgeUrlExceedDayLimit'

# The number of connected domain names reached the upper limit.
LIMITEXCEEDED_ECDNUSERTOOMANYDOMAINS = 'LimitExceeded.EcdnUserTooManyDomains'

# This domain name already exists.
RESOURCEINUSE_ECDNDOMAINEXISTS = 'ResourceInUse.EcdnDomainExists'

# The ECDN resource is being manipulated.
RESOURCEINUSE_ECDNOPINPROGRESS = 'ResourceInUse.EcdnOpInProgress'

# This domain name does not exist under the account. Please check and try again.
RESOURCENOTFOUND_ECDNDOMAINNOTEXISTS = 'ResourceNotFound.EcdnDomainNotExists'

# This domain name does not exist under the account. Please check and try again.
RESOURCENOTFOUND_ECDNHOSTNOTEXISTS = 'ResourceNotFound.EcdnHostNotExists'

# The project does not exist.
RESOURCENOTFOUND_ECDNPROJECTNOTEXISTS = 'ResourceNotFound.EcdnProjectNotExists'

# The ECDN service has not been activated. Please activate it first before using this API.
RESOURCENOTFOUND_ECDNUSERNOTEXISTS = 'ResourceNotFound.EcdnUserNotExists'

# The domain name has been locked. Please submit a ticket.
RESOURCEUNAVAILABLE_ECDNDOMAINISLOCKED = 'ResourceUnavailable.EcdnDomainIsLocked'

# Failed to deactivate the domain name. Please check and try again.
RESOURCEUNAVAILABLE_ECDNDOMAINISNOTOFFLINE = 'ResourceUnavailable.EcdnDomainIsNotOffline'

# The domain name has been deactivated. Please check and try again.
RESOURCEUNAVAILABLE_ECDNDOMAINISNOTONLINE = 'ResourceUnavailable.EcdnDomainIsNotOnline'

# The sub-account is unauthorized to query full data.
UNAUTHORIZEDOPERATION_CDNACCOUNTUNAUTHORIZED = 'UnauthorizedOperation.CdnAccountUnauthorized'

# No CAM policy is configured for the sub-account.
UNAUTHORIZEDOPERATION_CDNCAMUNAUTHORIZED = 'UnauthorizedOperation.CdnCamUnauthorized'

# The acceleration domain name is not authorized for the ECDN sub-account.
UNAUTHORIZEDOPERATION_CDNDOMAINUNAUTHORIZED = 'UnauthorizedOperation.CdnDomainUnauthorized'

# The acceleration domain name is not authorized for the ECDN sub-account.
UNAUTHORIZEDOPERATION_CDNHOSTUNAUTHORIZED = 'UnauthorizedOperation.CdnHostUnauthorized'

# The sub-account does not have the permission to access the domain name. Please try again after authorization.
UNAUTHORIZEDOPERATION_CDNNODOMAINUNAUTHORIZED = 'UnauthorizedOperation.CdnNoDomainUnauthorized'

# The project is not authorized for the sub-account.
UNAUTHORIZEDOPERATION_CDNPROJECTUNAUTHORIZED = 'UnauthorizedOperation.CdnProjectUnauthorized'

# The acceleration domain name is not authorized for the ECDN sub-account.
UNAUTHORIZEDOPERATION_DOMAINNOPERMISSION = 'UnauthorizedOperation.DomainNoPermission'

# The acceleration domain name is not authorized for the ECDN sub-account.
UNAUTHORIZEDOPERATION_DOMAINSNOPERMISSION = 'UnauthorizedOperation.DomainsNoPermission'

# The sub-account is unauthorized to query full data.
UNAUTHORIZEDOPERATION_ECDNACCOUNTUNAUTHORIZED = 'UnauthorizedOperation.EcdnAccountUnauthorized'

# No CAM policy is configured for the sub-account.
UNAUTHORIZEDOPERATION_ECDNCAMUNAUTHORIZED = 'UnauthorizedOperation.EcdnCamUnauthorized'

# The domain name resolution is not verified.
UNAUTHORIZEDOPERATION_ECDNDOMAINRECORDNOTVERIFIED = 'UnauthorizedOperation.EcdnDomainRecordNotVerified'

# The acceleration domain name is not authorized for the ECDN sub-account.
UNAUTHORIZEDOPERATION_ECDNDOMAINUNAUTHORIZED = 'UnauthorizedOperation.EcdnDomainUnauthorized'

# This domain name belongs to another account. You are not allowed o connect it to ECDN.
UNAUTHORIZEDOPERATION_ECDNHOSTISOWNEDBYOTHER = 'UnauthorizedOperation.EcdnHostIsOwnedByOther'

# The acceleration domain name is not authorized for the ECDN sub-account.
UNAUTHORIZEDOPERATION_ECDNHOSTUNAUTHORIZED = 'UnauthorizedOperation.EcdnHostUnauthorized'

# Please go to the CDN console for operation.
UNAUTHORIZEDOPERATION_ECDNMIGRATEDCDN = 'UnauthorizedOperation.EcdnMigratedCdn'

# The sub-account does not have the permission to access the domain name. Please try again after authorization.
UNAUTHORIZEDOPERATION_ECDNNODOMAINUNAUTHORIZED = 'UnauthorizedOperation.EcdnNoDomainUnauthorized'

# The project is not authorized for the sub-account.
UNAUTHORIZEDOPERATION_ECDNPROJECTUNAUTHORIZED = 'UnauthorizedOperation.EcdnProjectUnauthorized'

# The acceleration service has been suspended. Please restart it and try again.
UNAUTHORIZEDOPERATION_ECDNUSERISSUSPENDED = 'UnauthorizedOperation.EcdnUserIsSuspended'

# You are not on the beta allowlist and thus have no permission to use this feature.
UNAUTHORIZEDOPERATION_ECDNUSERNOWHITELIST = 'UnauthorizedOperation.EcdnUserNoWhitelist'

# CAM is not authorized for the ECDN sub-account.
UNAUTHORIZEDOPERATION_NOPERMISSION = 'UnauthorizedOperation.NoPermission'

# The project is not authorized for the ECDN sub-account.
UNAUTHORIZEDOPERATION_PROJECTNOPERMISSION = 'UnauthorizedOperation.ProjectNoPermission'

# The project is not authorized for the ECDN sub-account.
UNAUTHORIZEDOPERATION_PROJECTSNOPERMISSION = 'UnauthorizedOperation.ProjectsNoPermission'

# Unknown error. Please try again later.
UNAUTHORIZEDOPERATION_UNKNOWN = 'UnauthorizedOperation.Unknown'
