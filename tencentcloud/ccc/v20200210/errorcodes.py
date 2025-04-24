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


# 
FAILEDOPERATION_AICONCURRENTNOPACKAGE = 'FailedOperation.AIConcurrentNoPackage'

# 
FAILEDOPERATION_AICONCURRENTOVERFREQUENCY = 'FailedOperation.AIConcurrentOverFrequency'

# Outbound call failure.
FAILEDOPERATION_CALLOUTFAILED = 'FailedOperation.CallOutFailed'

# High-risk users, do not call
FAILEDOPERATION_CALLEEISBLACKUSER = 'FailedOperation.CalleeIsBlackUser'

# Limited outbound called number.
FAILEDOPERATION_CALLEEISLIMITED = 'FailedOperation.CalleeIsLimited'

# Caller ID exceeds the outbound call limit.
FAILEDOPERATION_CALLEROVERFREQUENCY = 'FailedOperation.CallerOverFrequency'

# The number is in a restricted calling zone.
FAILEDOPERATION_CALLOUTRULEBLINDAREA = 'FailedOperation.CalloutRuleBlindArea'

# Exceeded call limit for the callee within a set time.
FAILEDOPERATION_CALLOUTRULEMAXCALLCOUNTCALLEEINTERVALTIME = 'FailedOperation.CalloutRuleMaxCallCountCalleeIntervalTime'

# Exceeded daily call limit for the callee.
FAILEDOPERATION_CALLOUTRULEMAXCALLCOUNTCALLEEPERDAYAPPID = 'FailedOperation.CalloutRuleMaxCallCountCalleePerDayAppID'

# Calls are not allowed at this time.
FAILEDOPERATION_CALLOUTRULENOTWORKTIME = 'FailedOperation.CalloutRuleNotWorkTime'

# The current number status cannot be modified.
FAILEDOPERATION_CURSTATENOTALLOWMODIFY = 'FailedOperation.CurStateNotAllowModify'

# Duplicate account.
FAILEDOPERATION_DUPLICATEDACCOUNT = 'FailedOperation.DuplicatedAccount'

# No available outbound call numbers.
FAILEDOPERATION_NOCALLOUTNUMBER = 'FailedOperation.NoCallOutNumber'

# Insufficient permissions.
FAILEDOPERATION_PERMISSIONDENIED = 'FailedOperation.PermissionDenied'

# Agent is busy.
FAILEDOPERATION_SEATSTATUSBUSY = 'FailedOperation.SeatStatusBusy'

# Number of uploaded files exceeds the limit.
FAILEDOPERATION_UPLOADFILEOVERFLOW = 'FailedOperation.UploadFileOverflow'

# An internal error occurs.
INTERNALERROR = 'InternalError'

# Internal database access failure.
INTERNALERROR_DBERROR = 'InternalError.DBError'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# Duplicate address.
INVALIDPARAMETER_DUPLICATEADDRESS = 'InvalidParameter.DuplicateAddress'

# Duplicate number.
INVALIDPARAMETER_DUPLICATEPHONENUMBER = 'InvalidParameter.DuplicatePhoneNumber'

# Duplicate sip account.
INVALIDPARAMETER_DUPLICATESIPACCOUNT = 'InvalidParameter.DuplicateSipAccount'

# Illegal address.
INVALIDPARAMETER_ILLEGALADDRESS = 'InvalidParameter.IllegalAddress'

# Illegal number.
INVALIDPARAMETER_ILLEGALPHONENUMBER = 'InvalidParameter.IllegalPhoneNumber'

# The instance does not exist.
INVALIDPARAMETER_INSTANCENOTEXIST = 'InvalidParameter.InstanceNotExist'

# Invalid address.
INVALIDPARAMETER_INVALIDADDRESS = 'InvalidParameter.InvalidAddress'

# Invalid ip information.
INVALIDPARAMETER_INVALIDIP = 'InvalidParameter.InvalidIP'

# Invalid number.
INVALIDPARAMETER_INVALIDPHONENUMBER = 'InvalidParameter.InvalidPhoneNumber'

# Invalid port information.
INVALIDPARAMETER_INVALIDPORT = 'InvalidParameter.InvalidPort'

# Illegal password. (the length should be no less than 8 digits and must contain upper and lower case letters and numbers.).
INVALIDPARAMETER_SIPACCOUNTPASSWORDFORMAT = 'InvalidParameter.SipAccountPasswordFormat'

# Illegal username (only can contain a-z,a-z, and number).
INVALIDPARAMETER_SIPACCOUNTUSERFORMAT = 'InvalidParameter.SipAccountUserFormat'

# The sip channel is still in use.
INVALIDPARAMETER_SIPTRUNKINUSED = 'InvalidParameter.SipTrunkInUsed'

# SIP channel information not found.
INVALIDPARAMETER_SIPTRUNKNOTFOUND = 'InvalidParameter.SipTrunkNotFound'

# Invalid Parameter
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Account does not exist.
INVALIDPARAMETERVALUE_ACCOUNTNOTEXIST = 'InvalidParameterValue.AccountNotExist'

# The approval form no. does not exist.
INVALIDPARAMETERVALUE_APPLYIDNOTEXIST = 'InvalidParameterValue.ApplyIDNotExist'

# Error in the status of the review form.
INVALIDPARAMETERVALUE_ERRORAPPLYSTATUS = 'InvalidParameterValue.ErrorApplyStatus'

# 
INVALIDPARAMETERVALUE_EXPERIENCEACCOUNT = 'InvalidParameterValue.ExperienceAccount'

# The SDKAppID does not exist.
INVALIDPARAMETERVALUE_INSTANCENOTEXIST = 'InvalidParameterValue.InstanceNotExist'

# Invalid number status.
INVALIDPARAMETERVALUE_PHONENUMINVALID = 'InvalidParameterValue.PhoneNumInvalid'

# The number has been bound to another account.
INVALIDPARAMETERVALUE_PHONENUMISBOUNDOTHERACCOUNT = 'InvalidParameterValue.PhoneNumIsBoundOtherAccount'

# Skill group error.
INVALIDPARAMETERVALUE_SKILLGROUPERROR = 'InvalidParameterValue.SkillGroupError'

# Skill group already exists.
INVALIDPARAMETERVALUE_SKILLGROUPEXIST = 'InvalidParameterValue.SkillGroupExist'

# The pending review form has exceeded the limit and cannot be submitted for the time being.
INVALIDPARAMETERVALUE_WAITINGAPPROVALOVERFLOW = 'InvalidParameterValue.WaitingApprovalOverflow'

# Exceeded quota limit.
LIMITEXCEEDED = 'LimitExceeded'

# Your call package is used up.
LIMITEXCEEDED_BASEPACKAGEEXPIRED = 'LimitExceeded.BasePackageExpired'

# Exceeded quantity limit.
LIMITEXCEEDED_OUTOFCOUNTLIMIT = 'LimitExceeded.OutOfCountLimit'

# Missing required parameters.
MISSINGPARAMETER = 'MissingParameter'

# Not in the allowlist.
OPERATIONDENIED_NOTINWHITELIST = 'OperationDenied.NotInWhiteList'

# The account has been disabled.
OPERATIONDENIED_UINDISABLED = 'OperationDenied.UinDisabled'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# Unknown parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
