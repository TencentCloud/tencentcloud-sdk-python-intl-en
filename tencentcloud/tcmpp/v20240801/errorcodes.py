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

# DryRun operation, indicating that the request will be successful, but with an additional DryRun parameter.
DRYRUNOPERATION = 'DryRunOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Failed to delete: the application is bound with an ongoing approval ticket.
FAILEDOPERATION_APPALREADYBINDAUDIT = 'FailedOperation.AppAlreadyBindAudit'

# Failed to delete: This app is bound to a mini program.
FAILEDOPERATION_APPALREADYBINDMINIPROGRAM = 'FailedOperation.AppAlreadyBindMiniProgram'

# The domain name is already in the blocklist.
FAILEDOPERATION_EXISTBLACKDOMAIN = 'FailedOperation.ExistBlackDomain'

# The team name already exists.
FAILEDOPERATION_EXISTENTERPRISENAME = 'FailedOperation.ExistEnterpriseName'

# Failed to add: The domain name URL already exists. 
FAILEDOPERATION_EXISTREPEATDOMAINURL = 'FailedOperation.ExistRepeatDomainUrl'

# The sensitive API already exists.
FAILEDOPERATION_EXISTSENSITIVEAPI = 'FailedOperation.ExistSensitiveAPI'

# The domain name is already in the allowlist.
FAILEDOPERATION_EXISTWHITEDOMAIN = 'FailedOperation.ExistWhiteDomain'

# Failed to obtain the operation resource.
FAILEDOPERATION_GETOPERATERESOURCEFAILED = 'FailedOperation.GetOperateResourceFailed'

# Invalid team information
FAILEDOPERATION_INVALIDREQUESTENTERPRISEINFO = 'FailedOperation.InvalidRequestEnterpriseInfo'

# User login authentication failed.
FAILEDOPERATION_LOGINAUTHFAILED = 'FailedOperation.LoginAuthFailed'

# Failed to parse the mini program icon.
FAILEDOPERATION_MINIPROGRAMICONANALYSISFAILED = 'FailedOperation.MiniProgramIconAnalysisFailed'

# Unauthorized operation
FAILEDOPERATION_NOACCESSPERMISSION = 'FailedOperation.NoAccessPermission'

# The current team does not have the permission to create applications.
FAILEDOPERATION_OPERATIONSTEAMNOAPPLICATIONPERMISSION = 'FailedOperation.OperationsTeamNoApplicationPermission'

# The current operation team does not have permission to create a mini program.
FAILEDOPERATION_OPERATIONSTEAMNOMINIPROGRAMPERMISSION = 'FailedOperation.OperationsTeamNoMiniProgramPermission'

# The record does not exist.
FAILEDOPERATION_RECORDNOTFOUND = 'FailedOperation.RecordNotFound'

# Failed to parse request parameters.
FAILEDOPERATION_REQUESTPARAMANALYSISFAILED = 'FailedOperation.RequestParamAnalysisFailed'

# The preview version already exists.
FAILEDOPERATION_SHOWCASEVERSIONALREADYEXIST = 'FailedOperation.ShowcaseVersionAlreadyExist'

# System error.
FAILEDOPERATION_SYSTEMERROR = 'FailedOperation.SystemError'

# Internal error
INTERNALERROR = 'InternalError'

# Incorrect parameter.
INVALIDPARAMETER = 'InvalidParameter'

# Invalid parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The application name already exists.
INVALIDPARAMETERVALUE_APPNAMEALREADYEXIST = 'InvalidParameterValue.AppNameAlreadyExist'

# The account already exists.
INVALIDPARAMETERVALUE_EXISTUSERACCOUNT = 'InvalidParameterValue.ExistUserAccount'

# Invalid mini program ID.
INVALIDPARAMETERVALUE_INVALIDMINIAPPID = 'InvalidParameterValue.InvalidMiniAppId'

# Invalid team ID
INVALIDPARAMETERVALUE_INVALIDTEAMID = 'InvalidParameterValue.InvalidTeamId'

# Invalid user
INVALIDPARAMETERVALUE_INVALIDUSERID = 'InvalidParameterValue.InvalidUserId'

# The mini program name already exists.
INVALIDPARAMETERVALUE_MINIPROGRAMNAMEALREADYEXIST = 'InvalidParameterValue.MiniProgramNameAlreadyExist'

# Invalid team type
INVALIDPARAMETERVALUE_TEAMTYPEMISMATCH = 'InvalidParameterValue.TeamTypeMismatch'

# The user is not in the specified team.
INVALIDPARAMETERVALUE_USERTEAMRELATIONNOTEXIST = 'InvalidParameterValue.UserTeamRelationNotExist'

# Missing required parameters.
MISSINGPARAMETER = 'MissingParameter'

# No valid login information found.
MISSINGPARAMETER_LOGININFONOTFOUND = 'MissingParameter.LoginInfoNotFound'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# Too frequent requests
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# The resource is occupied.
RESOURCEINUSE = 'ResourceInUse'

# Insufficient resources.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The resource is not available.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Unknow parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'

# The operation is not supported.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
