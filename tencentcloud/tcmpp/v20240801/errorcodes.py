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

# The application name already exists.
FAILEDOPERATION_APPLICATIONNAMEALREADYEXISTED = 'FailedOperation.ApplicationNameAlreadyExisted'

# The number of applications exceeds the limit.
FAILEDOPERATION_APPLICATIONNUMBEREXCEEDLIMIT = 'FailedOperation.ApplicationNumberExceedLimit'

# The domain name is already in the blocklist.
FAILEDOPERATION_EXISTBLACKDOMAIN = 'FailedOperation.ExistBlackDomain'

# There is an ongoing approval request for this mini program.
FAILEDOPERATION_EXISTMNPAPPROVALRECORD = 'FailedOperation.ExistMNPApprovalRecord'

# Failed to add: The domain name URL already exists. 
FAILEDOPERATION_EXISTREPEATDOMAINURL = 'FailedOperation.ExistRepeatDomainUrl'

# The sensitive API already exists.
FAILEDOPERATION_EXISTSENSITIVEAPI = 'FailedOperation.ExistSensitiveAPI'

# The domain name is already in the allowlist.
FAILEDOPERATION_EXISTWHITEDOMAIN = 'FailedOperation.ExistWhiteDomain'

# Failed to download the mini program file
FAILEDOPERATION_FILEDOWNLOADFAILED = 'FailedOperation.FileDownloadFailed'

# Failed to obtain the operation resource.
FAILEDOPERATION_GETOPERATERESOURCEFAILED = 'FailedOperation.GetOperateResourceFailed'

# Invalid team information
FAILEDOPERATION_INVALIDREQUESTENTERPRISEINFO = 'FailedOperation.InvalidRequestEnterpriseInfo'

# User login authentication failed.
FAILEDOPERATION_LOGINAUTHFAILED = 'FailedOperation.LoginAuthFailed'

# The number of mini programs exceeds the limit.
FAILEDOPERATION_MNPNUMBEREXCEEDLIMIT = 'FailedOperation.MNPNumberExceedLimit'

# The mini program does not have an online version.
FAILEDOPERATION_MNPONLINEVERSIONNOTEXIST = 'FailedOperation.MNPOnlineVersionNotExist'

# The number of released mini programs exceeds the limit.
FAILEDOPERATION_MNPRELEASENUMBEREXCEEDLIMIT = 'FailedOperation.MNPReleaseNumberExceedLimit'

# The mini program-associated application team has not created any mini programs.
FAILEDOPERATION_MNPTEAMASSOCIATEDAPPLICATIONTEAMNOTCREATEAPPLICATION = 'FailedOperation.MNPTeamAssociatedApplicationTeamNotCreateApplication'

# The mini program team is not associated with an application team.
FAILEDOPERATION_MNPTEAMNOTASSOCIATEDAPPLICATIONTEAM = 'FailedOperation.MNPTeamNotAssociatedApplicationTeam'

# This mini program version has already been released.
FAILEDOPERATION_MNPVERSIONRELEASED = 'FailedOperation.MNPVersionReleased'

# Failed to parse the mini program icon.
FAILEDOPERATION_MINIPROGRAMICONANALYSISFAILED = 'FailedOperation.MiniProgramIconAnalysisFailed'

# Unauthorized operation
FAILEDOPERATION_NOACCESSPERMISSION = 'FailedOperation.NoAccessPermission'

# Only approved mini program versions can be released.
FAILEDOPERATION_ONLYRELEASEPLATFORMAPPROVEDMNPVERSION = 'FailedOperation.OnlyReleasePlatformApprovedMNPVersion'

# The current team does not have the permission to create applications.
FAILEDOPERATION_OPERATIONSTEAMNOAPPLICATIONPERMISSION = 'FailedOperation.OperationsTeamNoApplicationPermission'

# The current operation team does not have permission to create a mini program.
FAILEDOPERATION_OPERATIONSTEAMNOMINIPROGRAMPERMISSION = 'FailedOperation.OperationsTeamNoMiniProgramPermission'

# The TCMPP plan under the current account has expired.
FAILEDOPERATION_PACKAGEALREADYEXPIRED = 'FailedOperation.PackageAlreadyExpired'

# The record does not exist.
FAILEDOPERATION_RECORDNOTFOUND = 'FailedOperation.RecordNotFound'

# The version of the mini program to be released must be later than the online version.
FAILEDOPERATION_RELEASEMNPVERSIONNEEDGREATERTHANONLINEVERSION = 'FailedOperation.ReleaseMNPVersionNeedGreaterThanOnlineVersion'

# Failed to parse request parameters.
FAILEDOPERATION_REQUESTPARAMANALYSISFAILED = 'FailedOperation.RequestParamAnalysisFailed'

# The preview version already exists.
FAILEDOPERATION_SHOWCASEVERSIONALREADYEXIST = 'FailedOperation.ShowcaseVersionAlreadyExist'

# System error.
FAILEDOPERATION_SYSTEMERROR = 'FailedOperation.SystemError'

# You do not have permissions to manage the admin account.
FAILEDOPERATION_UNABLEOPERATEADMINACCOUNT = 'FailedOperation.UnableOperateAdminAccount'

# Internal error
INTERNALERROR = 'InternalError'

# Incorrect parameter.
INVALIDPARAMETER = 'InvalidParameter'

# Invalid parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The application package name is not specified.
INVALIDPARAMETERVALUE_APPPACKAGENAMENOTCONFIG = 'InvalidParameterValue.AppPackageNameNotConfig'

# Invalid value type or a required parameter is missing.
INVALIDPARAMETERVALUE_EXISTMISMATCHPARAMETERTYPE = 'InvalidParameterValue.ExistMismatchParameterType'

# The team name already exists.
INVALIDPARAMETERVALUE_EXISTTEAMNAME = 'InvalidParameterValue.ExistTeamName'

# The account already exists.
INVALIDPARAMETERVALUE_EXISTUSERACCOUNT = 'InvalidParameterValue.ExistUserAccount'

# Invalid account type
INVALIDPARAMETERVALUE_INVALIDACCOUNTTYPE = 'InvalidParameterValue.InvalidAccountType'

# Incorrect application package name format
INVALIDPARAMETERVALUE_INVALIDAPPPACKAGENAMELAYOUT = 'InvalidParameterValue.InvalidAppPackageNameLayout'

# Application ID is not specified or the ID does not exist.
INVALIDPARAMETERVALUE_INVALIDAPPLICATIONID = 'InvalidParameterValue.InvalidApplicationId'

# The application introduction is empty or exceeds 500 characters.
INVALIDPARAMETERVALUE_INVALIDAPPLICATIONINTRO = 'InvalidParameterValue.InvalidApplicationIntro'

# Invalid format or length of the application name
INVALIDPARAMETERVALUE_INVALIDAPPLICATIONNAME = 'InvalidParameterValue.InvalidApplicationName'

# The application remark is empty or exceeds 1,000 characters.
INVALIDPARAMETERVALUE_INVALIDAPPLICATIONREMARK = 'InvalidParameterValue.InvalidApplicationRemark'

# Invalid request operation
INVALIDPARAMETERVALUE_INVALIDAPPLYACTION = 'InvalidParameterValue.InvalidApplyAction'

# Invalid approval ID
INVALIDPARAMETERVALUE_INVALIDAPPROVALNO = 'InvalidParameterValue.InvalidApprovalNo'

# The length of approval notes exceeds the limit.
INVALIDPARAMETERVALUE_INVALIDAPPROVALNOTE = 'InvalidParameterValue.InvalidApprovalNote'

# Invalid file type of the mini program icon
INVALIDPARAMETERVALUE_INVALIDMNPICON = 'InvalidParameterValue.InvalidMNPIcon'

# Invalid mini program ID
INVALIDPARAMETERVALUE_INVALIDMNPID = 'InvalidParameterValue.InvalidMNPId'

# The mini program introduction is empty or too long.
INVALIDPARAMETERVALUE_INVALIDMNPINTRO = 'InvalidParameterValue.InvalidMNPIntro'

# Invalid format or length of the mini program name
INVALIDPARAMETERVALUE_INVALIDMNPNAME = 'InvalidParameterValue.InvalidMNPName'

# Invalid mini program type
INVALIDPARAMETERVALUE_INVALIDMNPTYPE = 'InvalidParameterValue.InvalidMNPType'

# Invalid mini program version number
INVALIDPARAMETERVALUE_INVALIDMNPVERSION = 'InvalidParameterValue.InvalidMNPVersion'

# The mini program version ID is empty or the version does not exist.
INVALIDPARAMETERVALUE_INVALIDMNPVERSIONID = 'InvalidParameterValue.InvalidMNPVersionId'

# The mini program version introduction is empty or is too long.
INVALIDPARAMETERVALUE_INVALIDMNPVERSIONINTRO = 'InvalidParameterValue.InvalidMNPVersionIntro'

# Invalid task ID
INVALIDPARAMETERVALUE_INVALIDMNPVERSIONTASKID = 'InvalidParameterValue.InvalidMNPVersionTaskId'

# Invalid mini program ID.
INVALIDPARAMETERVALUE_INVALIDMINIAPPID = 'InvalidParameterValue.InvalidMiniAppId'

# Invalid platform ID
INVALIDPARAMETERVALUE_INVALIDPLATFORMID = 'InvalidParameterValue.InvalidPlatformId'

# Invalid role ID
INVALIDPARAMETERVALUE_INVALIDROLEID = 'InvalidParameterValue.InvalidRoleId'

# Invalid team ID
INVALIDPARAMETERVALUE_INVALIDTEAMID = 'InvalidParameterValue.InvalidTeamId'

# Invalid user
INVALIDPARAMETERVALUE_INVALIDUSERID = 'InvalidParameterValue.InvalidUserId'

# Invalid username format or length
INVALIDPARAMETERVALUE_INVALIDUSERNAME = 'InvalidParameterValue.InvalidUserName'

# Invalid value of the approval request status of the mini program.
INVALIDPARAMETERVALUE_MNPAPPROVALSTATUSERROR = 'InvalidParameterValue.MNPApprovalStatusError'

# The mini program package size exceeds the limit.
INVALIDPARAMETERVALUE_MNPFILESIZEXCEEDLIMIT = 'InvalidParameterValue.MNPFileSizExceedLimit'

# The number of mini program categories exceeds the limit.
INVALIDPARAMETERVALUE_MNPTYPENUMBEREXCEEDLIMIT = 'InvalidParameterValue.MNPTypeNumberExceedLimit'

# The mini program version has not been approved.
INVALIDPARAMETERVALUE_MNPVERSIONISNOTPLATFORMPHASE = 'InvalidParameterValue.MNPVersionIsNotPlatformPhase'

# The mini program name already exists.
INVALIDPARAMETERVALUE_MINIPROGRAMNAMEALREADYEXIST = 'InvalidParameterValue.MiniProgramNameAlreadyExist'

# The application in the approval request does not match the application associated with the mini program. 
INVALIDPARAMETERVALUE_PROCESSAPPLICATIONANDAPPROVALAPPLICATIONMISMATCH = 'InvalidParameterValue.ProcessApplicationAndApprovalApplicationMismatch'

# The approval details are required.
INVALIDPARAMETERVALUE_PROCESSAPPROVALITEMISEMPTY = 'InvalidParameterValue.ProcessApprovalItemIsEmpty'

# Invalid value of the mini program approval status
INVALIDPARAMETERVALUE_PROCESSMNPAPPROVALSTATUSERROR = 'InvalidParameterValue.ProcessMNPApprovalStatusError'

# The length of the query parameter exceeds 64 characters.
INVALIDPARAMETERVALUE_QUERYPARAMETERLENGTHEXCEEDLIMIT = 'InvalidParameterValue.QueryParameterLengthExceedLimit'

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

# There are no TCMPP plans under this account.
RESOURCENOTFOUND_NOTFOUNDPURCHASEDPACKAGE = 'ResourceNotFound.NotFoundPurchasedPackage'

# The resource is not available.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Unknow parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'

# The operation is not supported.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
