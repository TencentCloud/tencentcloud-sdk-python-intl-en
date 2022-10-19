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


# A CAM signature/authentication error occurred.
AUTHFAILURE = 'AuthFailure'

# `DryRun` Operation. It means that the request would have succeeded, but the `DryRun` parameter was used.
DRYRUNOPERATION = 'DryRunOperation'

# The operation failed.
FAILEDOPERATION = 'FailedOperation'

# The secondary account has already been merged and cannot be merged again.
FAILEDOPERATION_ACCOUNTALREADYBELINKED = 'FailedOperation.AccountAlreadyBeLinked'

# The user attribute format is abnormal.
FAILEDOPERATION_ATTRIBUTEFORMATERROR = 'FailedOperation.AttributeFormatError'

# There are already two valid tasks. Wait for one of them to complete and try again.
FAILEDOPERATION_DATAFLOWTOOMANYREQUESTS = 'FailedOperation.DataFlowTooManyRequests'

# The email address has already been bound to a user.
FAILEDOPERATION_EMAILALREADYEXISTS = 'FailedOperation.EmailAlreadyExists'

# The email address cannot be empty.
FAILEDOPERATION_EMAILISNULL = 'FailedOperation.EmailIsNull'

# The user is empty during user import.
FAILEDOPERATION_IMPORTUSERISEMPTY = 'FailedOperation.ImportUserIsEmpty'

# indexedAttribute can contain up to 512 characters.
FAILEDOPERATION_INDEXEDATTRIBUTETOOLONG = 'FailedOperation.IndexedAttributeTooLong'

# The tenant is invalid.
FAILEDOPERATION_INVALIDTENANT = 'FailedOperation.InvalidTenant'

# The status enumerated value is wrong. See the API documentation.
FAILEDOPERATION_INVALIDUSERSTATUSENUM = 'FailedOperation.InvalidUserStatusEnum'

# The user pool is invalid.
FAILEDOPERATION_INVALIDUSERSTORE = 'FailedOperation.InvalidUserStore'

# The password cannot be empty.
FAILEDOPERATION_PASSWORDISNULL = 'FailedOperation.PasswordIsNull'

# The mobile number has already been bound to a user.
FAILEDOPERATION_PHONENUMBERALREADYEXISTS = 'FailedOperation.PhoneNumberAlreadyExists'

# The mobile number cannot be empty.
FAILEDOPERATION_PHONENUMBERISNULL = 'FailedOperation.PhoneNumberIsNull'

# The primary user does not exist.
FAILEDOPERATION_PRIMARYUSERNOTFOUND = 'FailedOperation.PrimaryUserNotFound'

# The query condition must contain at least one of the followings: userName, phoneNumber, email, userGroup, alipayUserId, wechatOpenId,wechatUnionId, qqOpenId, qqUnionId,lastModifiedDate, indexedAttribute1, indexedAttribute2,indexedAttribute3, indexedAttribute4, indexedAttribute5.
FAILEDOPERATION_QUERYUSERSPARAMETERMUSTINWHITELIST = 'FailedOperation.QueryUsersParameterMustInWhitelist'

# The conditions can not duplicate.
FAILEDOPERATION_QUERYUSERSPARAMETERREPEAT = 'FailedOperation.QueryUsersParameterRepeat'

# The `PropertyKey` of `Sort` must include one of the followings: id, userName, phoneNumber, email, userGroup, alipayUserId, wechatOpenId,wechatUnionId, qqOpenId, qqUnionId,lastModifiedDate, indexedAttribute1, indexedAttribute2,indexedAttribute3, indexedAttribute4, indexedAttribute5.
FAILEDOPERATION_QUERYUSERSSORTPARAMETERMUSTINWHITELIST = 'FailedOperation.QueryUsersSortParameterMustInWhitelist'

# The quota is exceeded. Contact customer service.
FAILEDOPERATION_QUOTALIMITEXCEEDED = 'FailedOperation.QuotaLimitExceeded'

# The secondary user does not exist.
FAILEDOPERATION_SECONDARYUSERNOTFOUND = 'FailedOperation.SecondaryUserNotFound'

# The user group does not exist.
FAILEDOPERATION_USERGROUPNOTFOUND = 'FailedOperation.UserGroupNotFound'

# The user account is frozen.
FAILEDOPERATION_USERISFREEZE = 'FailedOperation.UserIsFreeze'

# The user name already exists.
FAILEDOPERATION_USERNAMEALREADYEXISTS = 'FailedOperation.UserNameAlreadyExists'

# The username cannot be empty.
FAILEDOPERATION_USERNAMEISNULL = 'FailedOperation.UserNameIsNull'

# The user does not exist.
FAILEDOPERATION_USERNOTFOUND = 'FailedOperation.UserNotFound'

# The updated status is required.
FAILEDOPERATION_USERSTATUSREQUIRED = 'FailedOperation.UserStatusRequired'

# An internal error occurred.
INTERNALERROR = 'InternalError'

# An unknown error occurred.
INTERNALERROR_UNKNOWNERROR = 'InternalError.UnknownError'

# The parameter is incorrect.
INVALIDPARAMETER = 'InvalidParameter'

# The request parameter is invalid.
INVALIDPARAMETER_PARAMETERILLEGAL = 'InvalidParameter.ParameterIllegal'

# The parameter value is incorrect.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# The parameter is missing.
MISSINGPARAMETER = 'MissingParameter'

# The operation was denied.
OPERATIONDENIED = 'OperationDenied'

# The number of requests exceeds the frequency limit.
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# Too many requests. Try again later.
REQUESTLIMITEXCEEDED_FREQUENTREQUEST = 'RequestLimitExceeded.FrequentRequest'

# Repeated request. Try again later.
REQUESTLIMITEXCEEDED_REPEATREQUEST = 'RequestLimitExceeded.RepeatRequest'

# The resource is in use.
RESOURCEINUSE = 'ResourceInUse'

# The resource is insufficient.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# The resources have been sold out.
RESOURCESSOLDOUT = 'ResourcesSoldOut'

# The operation is unauthorized.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# The service is not activated.
UNAUTHORIZEDOPERATION_TENANTNOTACTIVATED = 'UnauthorizedOperation.TenantNotActivated'

# The parameter is unknown.
UNKNOWNPARAMETER = 'UnknownParameter'

# The operation is not supported.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
