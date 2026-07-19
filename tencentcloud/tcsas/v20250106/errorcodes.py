# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# FailedOperation.AppAlreadyBindAudit
FAILEDOPERATION_APPALREADYBINDAUDIT = 'FailedOperation.AppAlreadyBindAudit'

# FailedOperation.AppAlreadyBindMiniProgram
FAILEDOPERATION_APPALREADYBINDMINIPROGRAM = 'FailedOperation.AppAlreadyBindMiniProgram'

# FailedOperation.ApplicationNameAlreadyExisted
FAILEDOPERATION_APPLICATIONNAMEALREADYEXISTED = 'FailedOperation.ApplicationNameAlreadyExisted'

# FailedOperation.ApplicationNumberExceedLimit
FAILEDOPERATION_APPLICATIONNUMBEREXCEEDLIMIT = 'FailedOperation.ApplicationNumberExceedLimit'

# The approval request has already been processed. Please do not repeat this operation.
FAILEDOPERATION_APPROVALALREADYPROCESSED = 'FailedOperation.ApprovalAlreadyProcessed'

# The approval request does not belong to the current superapp.
FAILEDOPERATION_APPROVALNOTBELONGTOAPPLICATION = 'FailedOperation.ApprovalNotBelongToApplication'

# FailedOperation.ExistMNPApprovalRecord
FAILEDOPERATION_EXISTMNPAPPROVALRECORD = 'FailedOperation.ExistMNPApprovalRecord'

# A merchant binding request already exists.
FAILEDOPERATION_EXISTMERCHANTBINDAPPLY = 'FailedOperation.ExistMerchantBindApply'

# The merchant is already bound.
FAILEDOPERATION_EXISTMERCHANTBINDRELATION = 'FailedOperation.ExistMerchantBindRelation'

# A payment activation approval request is already pending. Please do not resubmit.
FAILEDOPERATION_EXISTPAYMENTOPENAPPLY = 'FailedOperation.ExistPaymentOpenApply'

# FailedOperation.ExistRepeatDomainUrl
FAILEDOPERATION_EXISTREPEATDOMAINURL = 'FailedOperation.ExistRepeatDomainUrl'

# FailedOperation.ExistSensitiveAPI
FAILEDOPERATION_EXISTSENSITIVEAPI = 'FailedOperation.ExistSensitiveAPI'

# FailedOperation.FileDownloadFailed
FAILEDOPERATION_FILEDOWNLOADFAILED = 'FailedOperation.FileDownloadFailed'

# FailedOperation.GetOperateResourceFailed
FAILEDOPERATION_GETOPERATERESOURCEFAILED = 'FailedOperation.GetOperateResourceFailed'

# FailedOperation.LoginAuthFailed
FAILEDOPERATION_LOGINAUTHFAILED = 'FailedOperation.LoginAuthFailed'

# FailedOperation.MNPNumberExceedLimit
FAILEDOPERATION_MNPNUMBEREXCEEDLIMIT = 'FailedOperation.MNPNumberExceedLimit'

# FailedOperation.MNPOnlineVersionNotExist
FAILEDOPERATION_MNPONLINEVERSIONNOTEXIST = 'FailedOperation.MNPOnlineVersionNotExist'

# The payment capability of this mini program is already activated.
FAILEDOPERATION_MNPPAYMENTALREADYENABLED = 'FailedOperation.MNPPaymentAlreadyEnabled'

# FailedOperation.MNPReleaseNumberExceedLimit
FAILEDOPERATION_MNPRELEASENUMBEREXCEEDLIMIT = 'FailedOperation.MNPReleaseNumberExceedLimit'

# FailedOperation.MNPTeamAssociatedApplicationTeamNotCreateApplication
FAILEDOPERATION_MNPTEAMASSOCIATEDAPPLICATIONTEAMNOTCREATEAPPLICATION = 'FailedOperation.MNPTeamAssociatedApplicationTeamNotCreateApplication'

# FailedOperation.MNPTeamNotAssociatedApplicationTeam
FAILEDOPERATION_MNPTEAMNOTASSOCIATEDAPPLICATIONTEAM = 'FailedOperation.MNPTeamNotAssociatedApplicationTeam'

# FailedOperation.MNPVersionReleased
FAILEDOPERATION_MNPVERSIONRELEASED = 'FailedOperation.MNPVersionReleased'

# The superapp payment configuration is disabled.
FAILEDOPERATION_MERCHANTPAYMENTFUNCTIONCLOSED = 'FailedOperation.MerchantPaymentFunctionClosed'

# FailedOperation.MiniProgramIconAnalysisFailed
FAILEDOPERATION_MINIPROGRAMICONANALYSISFAILED = 'FailedOperation.MiniProgramIconAnalysisFailed'

# FailedOperation.NoAccessPermission
FAILEDOPERATION_NOACCESSPERMISSION = 'FailedOperation.NoAccessPermission'

# FailedOperation.OnlyReleasePlatformApprovedMNPVersion
FAILEDOPERATION_ONLYRELEASEPLATFORMAPPROVEDMNPVERSION = 'FailedOperation.OnlyReleasePlatformApprovedMNPVersion'

# FailedOperation.OperationsTeamNoMiniProgramPermission
FAILEDOPERATION_OPERATIONSTEAMNOMINIPROGRAMPERMISSION = 'FailedOperation.OperationsTeamNoMiniProgramPermission'

# FailedOperation.PackageAlreadyExpired
FAILEDOPERATION_PACKAGEALREADYEXPIRED = 'FailedOperation.PackageAlreadyExpired'

# Invalid superapp ID or parameter ID.
FAILEDOPERATION_PAYMENTRECORDNOTBELONGTOAPPLICATION = 'FailedOperation.PaymentRecordNotBelongToApplication'

# Payment binding not found.
FAILEDOPERATION_PAYMENTRECORDNOTFOUND = 'FailedOperation.PaymentRecordNotFound'

# Payment version verification failed.
FAILEDOPERATION_PAYMENTVERSIONCHECKERROR = 'FailedOperation.PaymentVersionCheckError'

# Number of production superapp package name configurations exceeds the limit.
FAILEDOPERATION_PRODAPPLICATIONCONFIGEXCEEDLIMIT = 'FailedOperation.ProdApplicationConfigExceedLimit'

# FailedOperation.RecordNotFound
FAILEDOPERATION_RECORDNOTFOUND = 'FailedOperation.RecordNotFound'

# FailedOperation.ReleaseMNPVersionNeedGreaterThanOnlineVersion
FAILEDOPERATION_RELEASEMNPVERSIONNEEDGREATERTHANONLINEVERSION = 'FailedOperation.ReleaseMNPVersionNeedGreaterThanOnlineVersion'

# FailedOperation.RequestParamAnalysisFailed
FAILEDOPERATION_REQUESTPARAMANALYSISFAILED = 'FailedOperation.RequestParamAnalysisFailed'

# FailedOperation.ShowcaseVersionAlreadyExist
FAILEDOPERATION_SHOWCASEVERSIONALREADYEXIST = 'FailedOperation.ShowcaseVersionAlreadyExist'

# FailedOperation.SystemError
FAILEDOPERATION_SYSTEMERROR = 'FailedOperation.SystemError'

# Number of non-production superapp package names exceeds the limit.
FAILEDOPERATION_TESTAPPLICATIONCONFIGEXCEEDLIMIT = 'FailedOperation.TestApplicationConfigExceedLimit'

# FailedOperation.UnableOperateAdminAccount
FAILEDOPERATION_UNABLEOPERATEADMINACCOUNT = 'FailedOperation.UnableOperateAdminAccount'

# FailedOperation.UserNotFound
FAILEDOPERATION_USERNOTFOUND = 'FailedOperation.UserNotFound'

# Internal error.
INTERNALERROR = 'InternalError'

# Incorrect parameter.
INVALIDPARAMETER = 'InvalidParameter'

# Duplicate superapp package names exist.
INVALIDPARAMETER_INVALIDEXISTSAMEAPPKEY = 'InvalidParameter.InvalidExistSameAppKey'

# Invalid parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Age rating exceeds the superapp limit.
INVALIDPARAMETERVALUE_AGERATINGEXCEEDSUPPERAPPLIMIT = 'InvalidParameterValue.AgeRatingExceedSupperAppLimit'

# Superapp package name length exceeds the limit.
INVALIDPARAMETERVALUE_APPKEYLENGTHEXCEEDLIMIT = 'InvalidParameterValue.AppKeyLengthExceedLimit'

# InvalidParameterValue.AppPackageNameNotConfig
INVALIDPARAMETERVALUE_APPPACKAGENAMENOTCONFIG = 'InvalidParameterValue.AppPackageNameNotConfig'

# Superapp URL length exceeds the limit.
INVALIDPARAMETERVALUE_APPURLLENGTHEXCEEDLIMIT = 'InvalidParameterValue.AppURLLengthExceedLimit'

# Approval note cannot be empty.
INVALIDPARAMETERVALUE_APPROVALNOTEREQUIRED = 'InvalidParameterValue.ApprovalNoteRequired'

# Duplicate age rating.
INVALIDPARAMETERVALUE_DUPLICATEAGERATINGSTANDARD = 'InvalidParameterValue.DuplicateAgeRatingStandard'

# InvalidParameterValue.ExistMismatchParameterType
INVALIDPARAMETERVALUE_EXISTMISMATCHPARAMETERTYPE = 'InvalidParameterValue.ExistMismatchParameterType'

# InvalidParameterValue.ExistTeamName
INVALIDPARAMETERVALUE_EXISTTEAMNAME = 'InvalidParameterValue.ExistTeamName'

# InvalidParameterValue.ExistUserAccount
INVALIDPARAMETERVALUE_EXISTUSERACCOUNT = 'InvalidParameterValue.ExistUserAccount'

# InvalidParameterValue.InvalidAccountType
INVALIDPARAMETERVALUE_INVALIDACCOUNTTYPE = 'InvalidParameterValue.InvalidAccountType'

# Invalid age rating parameters.
INVALIDPARAMETERVALUE_INVALIDAGERATINGSTANDARD = 'InvalidParameterValue.InvalidAgeRatingStandard'

# InvalidParameterValue.InvalidAppPackageNameLayout
INVALIDPARAMETERVALUE_INVALIDAPPPACKAGENAMELAYOUT = 'InvalidParameterValue.InvalidAppPackageNameLayout'

# Invalid superapp type.
INVALIDPARAMETERVALUE_INVALIDAPPTYPE = 'InvalidParameterValue.InvalidAppType'

# InvalidParameterValue.InvalidApplicationId
INVALIDPARAMETERVALUE_INVALIDAPPLICATIONID = 'InvalidParameterValue.InvalidApplicationId'

# InvalidParameterValue.InvalidApplicationIntro
INVALIDPARAMETERVALUE_INVALIDAPPLICATIONINTRO = 'InvalidParameterValue.InvalidApplicationIntro'

# InvalidParameterValue.InvalidApplicationName
INVALIDPARAMETERVALUE_INVALIDAPPLICATIONNAME = 'InvalidParameterValue.InvalidApplicationName'

# InvalidParameterValue.InvalidApplicationRemark
INVALIDPARAMETERVALUE_INVALIDAPPLICATIONREMARK = 'InvalidParameterValue.InvalidApplicationRemark'

# InvalidParameterValue.InvalidApplyAction
INVALIDPARAMETERVALUE_INVALIDAPPLYACTION = 'InvalidParameterValue.InvalidApplyAction'

# InvalidParameterValue.InvalidApprovalNo
INVALIDPARAMETERVALUE_INVALIDAPPROVALNO = 'InvalidParameterValue.InvalidApprovalNo'

# InvalidParameterValue.InvalidApprovalNote
INVALIDPARAMETERVALUE_INVALIDAPPROVALNOTE = 'InvalidParameterValue.InvalidApprovalNote'

# Invalid approval type.
INVALIDPARAMETERVALUE_INVALIDAPPROVALTYPE = 'InvalidParameterValue.InvalidApprovalType'

# Invalid multi-language language code.
INVALIDPARAMETERVALUE_INVALIDMNPI18NLANG = 'InvalidParameterValue.InvalidMNPI18NLang'

# InvalidParameterValue.InvalidMNPIcon
INVALIDPARAMETERVALUE_INVALIDMNPICON = 'InvalidParameterValue.InvalidMNPIcon'

# InvalidParameterValue.InvalidMNPId
INVALIDPARAMETERVALUE_INVALIDMNPID = 'InvalidParameterValue.InvalidMNPId'

# InvalidParameterValue.InvalidMNPIntro
INVALIDPARAMETERVALUE_INVALIDMNPINTRO = 'InvalidParameterValue.InvalidMNPIntro'

# InvalidParameterValue.InvalidMNPName
INVALIDPARAMETERVALUE_INVALIDMNPNAME = 'InvalidParameterValue.InvalidMNPName'

# InvalidParameterValue.InvalidMNPType
INVALIDPARAMETERVALUE_INVALIDMNPTYPE = 'InvalidParameterValue.InvalidMNPType'

# InvalidParameterValue.InvalidMNPVersion
INVALIDPARAMETERVALUE_INVALIDMNPVERSION = 'InvalidParameterValue.InvalidMNPVersion'

# InvalidParameterValue.InvalidMNPVersionId
INVALIDPARAMETERVALUE_INVALIDMNPVERSIONID = 'InvalidParameterValue.InvalidMNPVersionId'

# InvalidParameterValue.InvalidMNPVersionIntro
INVALIDPARAMETERVALUE_INVALIDMNPVERSIONINTRO = 'InvalidParameterValue.InvalidMNPVersionIntro'

# InvalidParameterValue.InvalidMNPVersionTaskId
INVALIDPARAMETERVALUE_INVALIDMNPVERSIONTASKID = 'InvalidParameterValue.InvalidMNPVersionTaskId'

# Invalid merchant ID.
INVALIDPARAMETERVALUE_INVALIDMERCHANTID = 'InvalidParameterValue.InvalidMerchantId'

# Invalid merchant name.
INVALIDPARAMETERVALUE_INVALIDMERCHANTNAME = 'InvalidParameterValue.InvalidMerchantName'

# InvalidParameterValue.InvalidMiniAppId
INVALIDPARAMETERVALUE_INVALIDMINIAPPID = 'InvalidParameterValue.InvalidMiniAppId'

# InvalidParameterValue.InvalidPlatformId
INVALIDPARAMETERVALUE_INVALIDPLATFORMID = 'InvalidParameterValue.InvalidPlatformId'

# InvalidParameterValue.InvalidRoleId
INVALIDPARAMETERVALUE_INVALIDROLEID = 'InvalidParameterValue.InvalidRoleId'

# InvalidParameterValue.InvalidTeamId
INVALIDPARAMETERVALUE_INVALIDTEAMID = 'InvalidParameterValue.InvalidTeamId'

# InvalidParameterValue.InvalidUserId
INVALIDPARAMETERVALUE_INVALIDUSERID = 'InvalidParameterValue.InvalidUserId'

# InvalidParameterValue.InvalidUserName
INVALIDPARAMETERVALUE_INVALIDUSERNAME = 'InvalidParameterValue.InvalidUserName'

# InvalidParameterValue.MNPApprovalStatusError
INVALIDPARAMETERVALUE_MNPAPPROVALSTATUSERROR = 'InvalidParameterValue.MNPApprovalStatusError'

# InvalidParameterValue.MNPFileSizExceedLimit
INVALIDPARAMETERVALUE_MNPFILESIZEXCEEDLIMIT = 'InvalidParameterValue.MNPFileSizExceedLimit'

# InvalidParameterValue.MNPTypeNumberExceedLimit
INVALIDPARAMETERVALUE_MNPTYPENUMBEREXCEEDLIMIT = 'InvalidParameterValue.MNPTypeNumberExceedLimit'

# InvalidParameterValue.MNPVersionIsNotPlatformPhase
INVALIDPARAMETERVALUE_MNPVERSIONISNOTPLATFORMPHASE = 'InvalidParameterValue.MNPVersionIsNotPlatformPhase'

# InvalidParameterValue.MiniProgramNameAlreadyExist
INVALIDPARAMETERVALUE_MINIPROGRAMNAMEALREADYEXIST = 'InvalidParameterValue.MiniProgramNameAlreadyExist'

# Approval note is required.
INVALIDPARAMETERVALUE_PAYMENTRECORDNOTFOUND = 'InvalidParameterValue.PaymentRecordNotFound'

# InvalidParameterValue.ProcessApplicationAndApprovalApplicationMismatch
INVALIDPARAMETERVALUE_PROCESSAPPLICATIONANDAPPROVALAPPLICATIONMISMATCH = 'InvalidParameterValue.ProcessApplicationAndApprovalApplicationMismatch'

# InvalidParameterValue.ProcessApprovalItemIsEmpty
INVALIDPARAMETERVALUE_PROCESSAPPROVALITEMISEMPTY = 'InvalidParameterValue.ProcessApprovalItemIsEmpty'

# InvalidParameterValue.ProcessMNPApprovalStatusError
INVALIDPARAMETERVALUE_PROCESSMNPAPPROVALSTATUSERROR = 'InvalidParameterValue.ProcessMNPApprovalStatusError'

# InvalidParameterValue.QueryParameterLengthExceedLimit
INVALIDPARAMETERVALUE_QUERYPARAMETERLENGTHEXCEEDLIMIT = 'InvalidParameterValue.QueryParameterLengthExceedLimit'

# Missing required parameters.
MISSINGPARAMETER = 'MissingParameter'

# MissingParameter.LoginInfoNotFound
MISSINGPARAMETER_LOGININFONOTFOUND = 'MissingParameter.LoginInfoNotFound'

# ResourceNotFound.NotFoundPurchasedPackage
RESOURCENOTFOUND_NOTFOUNDPURCHASEDPACKAGE = 'ResourceNotFound.NotFoundPurchasedPackage'

# Unknow parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'
