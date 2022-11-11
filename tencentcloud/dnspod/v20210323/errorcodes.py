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

# The operation failed.
FAILEDOPERATION = 'FailedOperation'

# The domain is already in your list. There is no need to add it again.
FAILEDOPERATION_DOMAINEXISTS = 'FailedOperation.DomainExists'

# This domain is a key protected resource in DNSPod. To prevent the service from being affected by maloperations, you cannot delete it. If you are sure you need to delete it, please contact your sales rep for technical support.
FAILEDOPERATION_DOMAINISKEYDOMAIN = 'FailedOperation.DomainIsKeyDomain'

# You cannot perform this operation on a locked domain.
FAILEDOPERATION_DOMAINISLOCKED = 'FailedOperation.DomainIsLocked'

# You cannot perform this operation on a banned domain.
FAILEDOPERATION_DOMAINISSPAM = 'FailedOperation.DomainIsSpam'

# You cannot perform this operation on a VIP domain.
FAILEDOPERATION_DOMAINISVIP = 'FailedOperation.DomainIsVip'

# This domain has been added by another account and can be reclaimed in the domain list.
FAILEDOPERATION_DOMAINOWNEDBYOTHERUSER = 'FailedOperation.DomainOwnedByOtherUser'

# The request was rejected due to an unusual login location of your account.
FAILEDOPERATION_LOGINAREANOTALLOWED = 'FailedOperation.LoginAreaNotAllowed'

# Login failed. Check whether the account and password are correct.
FAILEDOPERATION_LOGINFAILED = 'FailedOperation.LoginFailed'

# You are not the domain owner.
FAILEDOPERATION_NOTDOMAINOWNER = 'FailedOperation.NotDomainOwner'

# Your account identity has not been verified. Complete identity verification first before performing this operation.
FAILEDOPERATION_NOTREALNAMEDUSER = 'FailedOperation.NotRealNamedUser'

# The operation has no response. Try again later.
FAILEDOPERATION_UNKNOWERROR = 'FailedOperation.UnknowError'

# Internal error.
INTERNALERROR = 'InternalError'

# Invalid parameter.
INVALIDPARAMETER = 'InvalidParameter'

# Your account is banned by the system. Please contact us if you have any questions.
INVALIDPARAMETER_ACCOUNTISBANNED = 'InvalidParameter.AccountIsBanned'

# Custom error message.
INVALIDPARAMETER_CUSTOMMESSAGE = 'InvalidParameter.CustomMessage'

# DNSSEC has been enabled for this domain. You cannot add an @CNAME, URL, or framed URL record.
INVALIDPARAMETER_DNSSECADDCNAMEERROR = 'InvalidParameter.DnssecAddCnameError'

# The domain number is incorrect.
INVALIDPARAMETER_DOMAINIDINVALID = 'InvalidParameter.DomainIdInvalid'

# You cannot perform operations on a domain currently active or invalid.
INVALIDPARAMETER_DOMAININEFFECTORINVALIDATED = 'InvalidParameter.DomainInEffectOrInvalidated'

# The domain is incorrect. Enter a top-level domain such as dnspod.cn.
INVALIDPARAMETER_DOMAININVALID = 'InvalidParameter.DomainInvalid'

# This domain is an alias of another domain.
INVALIDPARAMETER_DOMAINISALIASER = 'InvalidParameter.DomainIsAliaser'

# You cannot change the DNS record of a domain currently active or invalid.
INVALIDPARAMETER_DOMAINNOTALLOWEDMODIFYRECORDS = 'InvalidParameter.DomainNotAllowedModifyRecords'

# The domain does not have an ICP filing, so you cannot add a URL record for it.
INVALIDPARAMETER_DOMAINNOTBEIAN = 'InvalidParameter.DomainNotBeian'

# The domain has not been registered and cannot be added.
INVALIDPARAMETER_DOMAINNOTREGED = 'InvalidParameter.DomainNotReged'

# The record already exists and does not need to be added again.
INVALIDPARAMETER_DOMAINRECORDEXIST = 'InvalidParameter.DomainRecordExist'

# Sorry, the email address of your account has not been verified.
INVALIDPARAMETER_EMAILNOTVERIFIED = 'InvalidParameter.EmailNotVerified'

# The weight is invalid. Enter an integer between 0 and 100.
INVALIDPARAMETER_INVALIDWEIGHT = 'InvalidParameter.InvalidWeight'

# The token ID is incorrect.
INVALIDPARAMETER_LOGINTOKENIDERROR = 'InvalidParameter.LoginTokenIdError'

# The token passed in does not exist.
INVALIDPARAMETER_LOGINTOKENNOTEXISTS = 'InvalidParameter.LoginTokenNotExists'

# Failed to verify the token.
INVALIDPARAMETER_LOGINTOKENVALIDATEFAILED = 'InvalidParameter.LoginTokenValidateFailed'

# Sorry, the mobile number of your account has not been verified.
INVALIDPARAMETER_MOBILENOTVERIFIED = 'InvalidParameter.MobileNotVerified'

# The MX priority is incorrect.
INVALIDPARAMETER_MXINVALID = 'InvalidParameter.MxInvalid'

# Operation failed. Please try again later.
INVALIDPARAMETER_OPERATEFAILED = 'InvalidParameter.OperateFailed'

# Parameter format error.
INVALIDPARAMETER_PARAMINVALID = 'InvalidParameter.ParamInvalid'

# The record number is incorrect.
INVALIDPARAMETER_RECORDIDINVALID = 'InvalidParameter.RecordIdInvalid'

# The record split zone is incorrect.
INVALIDPARAMETER_RECORDLINEINVALID = 'InvalidParameter.RecordLineInvalid'

# The record type is incorrect.
INVALIDPARAMETER_RECORDTYPEINVALID = 'InvalidParameter.RecordTypeInvalid'

# The record value is incorrect.
INVALIDPARAMETER_RECORDVALUEINVALID = 'InvalidParameter.RecordValueInvalid'

# The DNS record value is too long.
INVALIDPARAMETER_RECORDVALUELENGTHINVALID = 'InvalidParameter.RecordValueLengthInvalid'

# The remarks are too long (max 200 characters).
INVALIDPARAMETER_REMARKTOOLONG = 'InvalidParameter.RemarkTooLong'

# Your IP is invalid, so the request was rejected.
INVALIDPARAMETER_REQUESTIPLIMITED = 'InvalidParameter.RequestIpLimited'

# The search results contain more than 500 entries. Add one or more keywords.
INVALIDPARAMETER_RESULTMORETHAN500 = 'InvalidParameter.ResultMoreThan500'

# The subdomain is incorrect.
INVALIDPARAMETER_SUBDOMAININVALID = 'InvalidParameter.SubdomainInvalid'

# The domain is invalid.
INVALIDPARAMETER_TOOLSDOMAININVALID = 'InvalidParameter.ToolsDomainInvalid'

# Your account identity has not been verified. Complete identity verification first before performing this operation.
INVALIDPARAMETER_UNREALNAMEUSER = 'InvalidParameter.UnrealNameUser'

# Sorry, the URL failed to be added/enabled because its content did not comply with the DNSPod Terms of Service. Please contact technical support for assistance.
INVALIDPARAMETER_URLVALUEILLEGAL = 'InvalidParameter.UrlValueIllegal'

# The user does not exist.
INVALIDPARAMETER_USERNOTEXISTS = 'InvalidParameter.UserNotExists'

# The current domain is incorrect. Return to the previous step and try again.
INVALIDPARAMETERVALUE_DOMAINNOTEXISTS = 'InvalidParameterValue.DomainNotExists'

# Error in number of entries per page.
INVALIDPARAMETERVALUE_LIMITINVALID = 'InvalidParameterValue.LimitInvalid'

# The user number is incorrect.
INVALIDPARAMETERVALUE_USERIDINVALID = 'InvalidParameterValue.UserIdInvalid'

# The number of AAAA records exceeds the limit.
LIMITEXCEEDED_AAAACOUNTLIMIT = 'LimitExceeded.AAAACountLimit'

# The @NS record can be set to the default split zone only.
LIMITEXCEEDED_ATNSRECORDLIMIT = 'LimitExceeded.AtNsRecordLimit'

# Your account has been banned by the system due to excessive failed login attempts.
LIMITEXCEEDED_FAILEDLOGINLIMITEXCEEDED = 'LimitExceeded.FailedLoginLimitExceeded'

# The DNS plan used by this domain does not support framed URL forwarding, or the number of framed URL forward records exceeds the limit. To use this feature, please purchase more records.
LIMITEXCEEDED_HIDDENURLEXCEEDED = 'LimitExceeded.HiddenUrlExceeded'

# The number of NS records exceeds the limit.
LIMITEXCEEDED_NSCOUNTLIMIT = 'LimitExceeded.NsCountLimit'

# The TTL value of the record exceeds the limit.
LIMITEXCEEDED_RECORDTTLLIMIT = 'LimitExceeded.RecordTtlLimit'

# The number of SRV records exceeds the limit.
LIMITEXCEEDED_SRVCOUNTLIMIT = 'LimitExceeded.SrvCountLimit'

# The number of subdomain levels exceeds the limit.
LIMITEXCEEDED_SUBDOMAINLEVELLIMIT = 'LimitExceeded.SubdomainLevelLimit'

# The number of round-robin DNS records of the subdomain exceeds the limit.
LIMITEXCEEDED_SUBDOMAINROLLLIMIT = 'LimitExceeded.SubdomainRollLimit'

# The number of wildcard levels exceeds the limit.
LIMITEXCEEDED_SUBDOMAINWCARDLIMIT = 'LimitExceeded.SubdomainWcardLimit'

# The number of URL forward records of this domain exceeds the limit. To continue using this feature, please purchase more records.
LIMITEXCEEDED_URLCOUNTLIMIT = 'LimitExceeded.UrlCountLimit'

# Only the domain owner can perform this operation.
OPERATIONDENIED_DOMAINOWNERALLOWEDONLY = 'OperationDenied.DomainOwnerAllowedOnly'

# Sorry, you cannot add a blocked IP.
OPERATIONDENIED_IPINBLACKLISTNOTALLOWED = 'OperationDenied.IPInBlacklistNotAllowed'

# You have no permission to perform operations on the current domain. Return to the domain list.
OPERATIONDENIED_NOPERMISSIONTOOPERATEDOMAIN = 'OperationDenied.NoPermissionToOperateDomain'

# You are not an admin.
OPERATIONDENIED_NOTADMIN = 'OperationDenied.NotAdmin'

# Your are not a proxy user.
OPERATIONDENIED_NOTAGENT = 'OperationDenied.NotAgent'

# The user is not under your account.
OPERATIONDENIED_NOTMANAGEDUSER = 'OperationDenied.NotManagedUser'

# The number of requests exceeds the frequency limit.
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# The number of API requests exceeds the limit.
REQUESTLIMITEXCEEDED_REQUESTLIMITEXCEEDED = 'RequestLimitExceeded.RequestLimitExceeded'

# Empty record list.
RESOURCENOTFOUND_NODATAOFRECORD = 'ResourceNotFound.NoDataOfRecord'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'
