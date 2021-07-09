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


# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# An error occurred while manipulating the access key.
FAILEDOPERATION_ACCESSKEY = 'FailedOperation.Accesskey'

# The number of user policies has exceeded the limit.
FAILEDOPERATION_POLICYFULL = 'FailedOperation.PolicyFull'

# The policy name specified by the `PolicyName` field already exists.
FAILEDOPERATION_POLICYNAMEINUSE = 'FailedOperation.PolicyNameInUse'

# The policy version is already the default policy version.
FAILEDOPERATION_POLICYVERSIONALREADYDEFAULT = 'FailedOperation.PolicyVersionAlreadyDefault'

# The number of policy versions has reached the upper limit.
FAILEDOPERATION_POLICYVERSIONFULL = 'FailedOperation.PolicyVersionFull'

# No mobile number is bound to the account
FAILEDOPERATION_USERNOTBINDPHONE = 'FailedOperation.UserNotBindPhone'

# No WeChat Account is bound to the account
FAILEDOPERATION_USERNOTBINDWECHAT = 'FailedOperation.UserNotBindWechat'

# User does not have permission.
FAILEDOPERATION_USERUNBINDNOPERMISSION = 'FailedOperation.UserUnbindNoPermission'

# Internal error.
INTERNALERROR_SYSTEMERROR = 'InternalError.SystemError'

# Incorrect parameter.
INVALIDPARAMETER = 'InvalidParameter'

# `Action` field of policy document invalid.
INVALIDPARAMETER_ACTIONERROR = 'InvalidParameter.ActionError'

# The action in the policy syntax does not exist.
INVALIDPARAMETER_ACTIONMISS = 'InvalidParameter.ActionMiss'

# The action in the policy syntax does not exist.
INVALIDPARAMETER_ACTIONNOTEXIST = 'InvalidParameter.ActionNotExist'

# The action service in the policy syntax does not exist.
INVALIDPARAMETER_ACTIONSERVICENOTEXIST = 'InvalidParameter.ActionServiceNotExist'

# Limit on number of authorization object associated policies in the `principal` field reached.
INVALIDPARAMETER_ATTACHMENTFULL = 'InvalidParameter.AttachmentFull'

# The condition content in the policy syntax is incorrect.
INVALIDPARAMETER_CONDITIONCONTENTERROR = 'InvalidParameter.ConditionContentError'

# `condition` field of policy document invalid.
INVALIDPARAMETER_CONDITIONERROR = 'InvalidParameter.ConditionError'

# The condition operator in the policy syntax is incorrect.
INVALIDPARAMETER_CONDITIONTYPEERROR = 'InvalidParameter.ConditionTypeError'

# The task does not exist.
INVALIDPARAMETER_DELETIONTASKNOTEXIST = 'InvalidParameter.DeletionTaskNotExist'

# The input parameter `description` cannot exceed 300 bytes in length.
INVALIDPARAMETER_DESCRIPTIONLENGTHOVERLIMIT = 'InvalidParameter.DescriptionLengthOverlimit'

# `Effect` field of policy document invalid.
INVALIDPARAMETER_EFFECTERROR = 'InvalidParameter.EffectError'

# `EntityFilter` field invalid.
INVALIDPARAMETER_ENTITYFILTERERROR = 'InvalidParameter.EntityFilterError'

# Limit on number of user groups reached.
INVALIDPARAMETER_GROUPFULL = 'InvalidParameter.GroupFull'

# `GroupId` field invalid.
INVALIDPARAMETER_GROUPIDERROR = 'InvalidParameter.GroupIdError'

# User Group name repeated.
INVALIDPARAMETER_GROUPNAMEINUSE = 'InvalidParameter.GroupNameInUse'

# User Group does not exist.
INVALIDPARAMETER_GROUPNOTEXIST = 'InvalidParameter.GroupNotExist'

# Limit on number of sub-users in the user group reached.
INVALIDPARAMETER_GROUPUSERFULL = 'InvalidParameter.GroupUserFull'

# Identity provider name already in use.
INVALIDPARAMETER_IDENTITYNAMEINUSE = 'InvalidParameter.IdentityNameInUse'

# `Keyword` field invalid.
INVALIDPARAMETER_KEYWORDERROR = 'InvalidParameter.KeywordError'

# Multi-factor Token verification failed.
INVALIDPARAMETER_MFATOKENERROR = 'InvalidParameter.MFATokenError'

# CAM does not support the resource type specified in the policy document.
INVALIDPARAMETER_NOTSUPPORTPRODUCT = 'InvalidParameter.NotSupportProduct'

# There were too many entities in one operation.
INVALIDPARAMETER_OPERATEENTITIESOVERLIMIT = 'InvalidParameter.OperateEntitiesOverLimit'

# Invalid input parameter.
INVALIDPARAMETER_PARAMERROR = 'InvalidParameter.ParamError'

# Password incompatible with user safety settings.
INVALIDPARAMETER_PASSWORDVIOLATEDRULES = 'InvalidParameter.PasswordViolatedRules'

# `PolicyDocument` field invalid.
INVALIDPARAMETER_POLICYDOCUMENTERROR = 'InvalidParameter.PolicyDocumentError'

# `PolicyDocument` field exceeds length restriction.
INVALIDPARAMETER_POLICYDOCUMENTLENGTHOVERLIMIT = 'InvalidParameter.PolicyDocumentLengthOverLimit'

# Input parameter `PolicyId` invalid.
INVALIDPARAMETER_POLICYIDERROR = 'InvalidParameter.PolicyIdError'

# Policy ID does not exist.
INVALIDPARAMETER_POLICYIDNOTEXIST = 'InvalidParameter.PolicyIdNotExist'

# `PolicyName` field invalid.
INVALIDPARAMETER_POLICYNAMEERROR = 'InvalidParameter.PolicyNameError'

# The policy version does not exist.
INVALIDPARAMETER_POLICYVERSIONNOTEXISTS = 'InvalidParameter.PolicyVersionNotExists'

# `principal` field of policy document invalid.
INVALIDPARAMETER_PRINCIPALERROR = 'InvalidParameter.PrincipalError'

# Cross-site access is not supported for this role entity.
INVALIDPARAMETER_PRINCIPALQCSCROSSERROR = 'InvalidParameter.PrincipalQcsCrossError'

# Incorrect `PrincipalQcsc`.
INVALIDPARAMETER_PRINCIPALQCSERROR = 'InvalidParameter.PrincipalQcsError'

# `PrincipalQcs` does not exist.
INVALIDPARAMETER_PRINCIPALQCSNOTEXIST = 'InvalidParameter.PrincipalQcsNotExist'

# `PrincipalService` does not exist.
INVALIDPARAMETER_PRINCIPALSERVICENOTEXIST = 'InvalidParameter.PrincipalServiceNotExist'

# The resource context in the policy syntax is incorrect.
INVALIDPARAMETER_RESOURCECONTENTERROR = 'InvalidParameter.ResourceContentError'

# `Resource` field of policy document invalid.
INVALIDPARAMETER_RESOURCEERROR = 'InvalidParameter.ResourceError'

# The resource project in the policy syntax is incorrect.
INVALIDPARAMETER_RESOURCEPROJECTERROR = 'InvalidParameter.ResourceProjectError'

# Incorrect resource `QCS`.
INVALIDPARAMETER_RESOURCEQCSERROR = 'InvalidParameter.ResourceQcsError'

# The resource region in the policy syntax is incorrect.
INVALIDPARAMETER_RESOURCEREGIONERROR = 'InvalidParameter.ResourceRegionError'

# The resource service in the policy syntax does not exist.
INVALIDPARAMETER_RESOURCESERVICENOTEXIST = 'InvalidParameter.ResourceServiceNotExist'

# The resource root account in the policy syntax is incorrect.
INVALIDPARAMETER_RESOURCEUINERROR = 'InvalidParameter.ResourceUinError'

# Limit on number of roles reached.
INVALIDPARAMETER_ROLEFULL = 'InvalidParameter.RoleFull'

# Role name invalid.
INVALIDPARAMETER_ROLENAMEERROR = 'InvalidParameter.RoleNameError'

# A role with the same name already exists.
INVALIDPARAMETER_ROLENAMEINUSE = 'InvalidParameter.RoleNameInUse'

# Role does not exist.
INVALIDPARAMETER_ROLENOTEXIST = 'InvalidParameter.RoleNotExist'

# `Scope` field invalid.
INVALIDPARAMETER_SCOPEERROR = 'InvalidParameter.ScopeError'

# Service policies cannot be used for permission boundaries.
INVALIDPARAMETER_SERVICELINKEDPOLICYCANTINPERMISSIONBOUNDARY = 'InvalidParameter.ServiceLinkedPolicyCantInPermissionBoundary'

# Permission boundaries cannot be used for service roles.
INVALIDPARAMETER_SERVICELINKEDROLECANTUSEPERMISSIONBOUNDARY = 'InvalidParameter.ServiceLinkedRoleCantUsePermissionBoundary'

# `ServiceType` field invalid.
INVALIDPARAMETER_SERVICETYPEERROR = 'InvalidParameter.ServiceTypeError'

# `Statement` field of policy document invalid.
INVALIDPARAMETER_STATEMENTERROR = 'InvalidParameter.StatementError'

# Limit on number of sub-accounts reached.
INVALIDPARAMETER_SUBUSERFULL = 'InvalidParameter.SubUserFull'

# Sub-user name repeated.
INVALIDPARAMETER_SUBUSERNAMEINUSE = 'InvalidParameter.SubUserNameInUse'

# `Uin` field invalid.
INVALIDPARAMETER_UINERROR = 'InvalidParameter.UinError'

# Limit on number of user groups joined by a sub-user reached.
INVALIDPARAMETER_USERGROUPFULL = 'InvalidParameter.UserGroupFull'

# Invalid username.
INVALIDPARAMETER_USERNAMEILLEGAL = 'InvalidParameter.UserNameIllegal'

# User object does not exist
INVALIDPARAMETER_USERNOTEXIST = 'InvalidParameter.UserNotExist'

# `Version` field of policy document invalid.
INVALIDPARAMETER_VERSIONERROR = 'InvalidParameter.VersionError'

# Identity provider metadata document error.
INVALIDPARAMETERVALUE_METADATAERROR = 'InvalidParameterValue.MetadataError'

# Identity provider name error.
INVALIDPARAMETERVALUE_NAMEERROR = 'InvalidParameterValue.NameError'

# Limit on number of identity providers reached. 
LIMITEXCEEDED_IDENTITYFULL = 'LimitExceeded.IdentityFull'

# Each account can have up to two `AccessKey`.
OPERATIONDENIED_ACCESSKEYOVERLIMIT = 'OperationDenied.AccessKeyOverLimit'

# There are undeleted API keys.
OPERATIONDENIED_HAVEKEYS = 'OperationDenied.HaveKeys'

# The sub-user is not allowed to use the root account key.
OPERATIONDENIED_SUBUIN = 'OperationDenied.SubUin'

# The access key does not match the account.
OPERATIONDENIED_UINNOTMATCH = 'OperationDenied.UinNotMatch'

# The frequency limit of creating sub-users has been reached.
REQUESTLIMITEXCEEDED_CREATEUSER = 'RequestLimitExceeded.CreateUser'

# User group does not exist.
RESOURCENOTFOUND_GROUPNOTEXIST = 'ResourceNotFound.GroupNotExist'

# Identity provider does not exist.
RESOURCENOTFOUND_IDENTITYNOTEXIST = 'ResourceNotFound.IdentityNotExist'

# Resource does not exist.
RESOURCENOTFOUND_NOTFOUND = 'ResourceNotFound.NotFound'

# Resources specified by `PolicyId` does not exist.
RESOURCENOTFOUND_POLICYIDNOTFOUND = 'ResourceNotFound.PolicyIdNotFound'

# User does not exist.
RESOURCENOTFOUND_USERNOTEXIST = 'ResourceNotFound.UserNotExist'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# User do not have the authorization to delete API keys.
UNAUTHORIZEDOPERATION_DELETEAPIKEY = 'UnauthorizedOperation.DeleteApiKey'
