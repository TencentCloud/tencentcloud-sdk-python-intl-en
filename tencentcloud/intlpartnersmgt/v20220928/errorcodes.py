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

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# The account type is not a corporate account.
FAILEDOPERATION_ACCOUNTTYPENOTCOMPANY = 'FailedOperation.AccountTypeNotCompany'

# The account balance is insufficient.
FAILEDOPERATION_BALANCEINSUFFICIENT = 'FailedOperation.BalanceInsufficient'

# The account is a group account and cannot be bound as a sub-customer.
FAILEDOPERATION_BINDORGANIZATIONACCOUNT = 'FailedOperation.BindOrganizationAccount'

# The sub-customer balance is less than zero.
FAILEDOPERATION_CLIENTBALANCEISLESSOREQUALZERO = 'FailedOperation.ClientBalanceIsLessOrEqualZero'

# The sub-customer has purchased an sp package.
FAILEDOPERATION_CLIENTBUYSP = 'FailedOperation.ClientBuySP'

# The sub-customer has created a shared unit.
FAILEDOPERATION_CLIENTCREATESHAREUNIT = 'FailedOperation.ClientCreateShareUnit'

# The sub-customer has joined a shared unit.
FAILEDOPERATION_CLIENTJOINSHAREUNIT = 'FailedOperation.ClientJoinShareUnit'

# The user has not applied to become a sub-customer.
FAILEDOPERATION_CLIENTNOTAPPLY = 'FailedOperation.ClientNotApply'

# 
FAILEDOPERATION_EXCEEDMAXBINDCOUNT = 'FailedOperation.ExceedMaxBindCount'

# The uin of the second-level reseller is invalid.
FAILEDOPERATION_INVALIDSUBAGENTUIN = 'FailedOperation.InvalidSubAgentUin'

# FailedOperation.MailIsRegistered
FAILEDOPERATION_MAILISREGISTERED = 'FailedOperation.MailIsRegistered'

# The number of registered accounts for the current mobile number has reached the maximum limit. Please change the phone number and try again.
FAILEDOPERATION_PHONEBINDUPPER = 'FailedOperation.PhoneBindUpper'

# Real-Name pending approval.
FAILEDOPERATION_REALNAMEINAPPROVAL = 'FailedOperation.RealNameInApproval'

# User has not completed enterprise identity verification.
FAILEDOPERATION_REALNAMENOTCOMPLETED = 'FailedOperation.RealNameNotCompleted'

# Identity audit was rejected.
FAILEDOPERATION_REALNAMEREJECT = 'FailedOperation.RealNameReject'

# Illegal real-name type.
FAILEDOPERATION_REALNAMETYPEILLEGAL = 'FailedOperation.RealNameTypeIllegal'

# Unsubmitted application for second-level reseller.
FAILEDOPERATION_RESELLERNOTAPPLY = 'FailedOperation.ResellerNotApply'

# The interval between sending invitation links is less than three minutes. Please try again later.
FAILEDOPERATION_SENDMAILLIMIT180 = 'FailedOperation.SendMailLimit180'

# Verification codes are sent too frequently. Please try again later.
FAILEDOPERATION_SENDVERIFYCODELIMIT = 'FailedOperation.SendVerifyCodeLimit'

# The interval for sending SMS verification codes should be greater than 60 seconds. Please try again later.
FAILEDOPERATION_SENDVERIFYCODELIMIT60 = 'FailedOperation.SendVerifyCodeLimit60'

# The primary industry id and secondary industry id do not match.
FAILEDOPERATION_TRADEINFOINCORRECT = 'FailedOperation.TradeInfoIncorrect'

# Tencent cloud ka account cannot become a sub-customer.
FAILEDOPERATION_UINALREADYKA = 'FailedOperation.UinAlreadyKA'

# The uin has already applied to become a reseller.
FAILEDOPERATION_UINAPPLIEDAGENT = 'FailedOperation.UinAppliedAgent'

# Invalid UIN
FAILEDOPERATION_UININVALID = 'FailedOperation.UinInvalid'

# UIN is not a reseller.
FAILEDOPERATION_UINNOTAGENT = 'FailedOperation.UinNotAgent'

# UIN is a non-reseller (master reseller, reseller, sub-reseller) account.
FAILEDOPERATION_UINNOTRESELLER = 'FailedOperation.UinNotReseller'

# Incorrect verification code.
FAILEDOPERATION_VERIFICATIONCODEILLEGAL = 'FailedOperation.VerificationCodeIllegal'

# Internal error.
INTERNALERROR = 'InternalError'

# Invalid parameter
INVALIDPARAMETER = 'InvalidParameter'

# InvalidParameter.AccountTypeContentIncorrect
INVALIDPARAMETER_ACCOUNTTYPECONTENTINCORRECT = 'InvalidParameter.AccountTypeContentIncorrect'

# InvalidParameter.AreaContentIncorrect
INVALIDPARAMETER_AREACONTENTINCORRECT = 'InvalidParameter.AreaContentIncorrect'

# InvalidParameter.AreaFormatIncorrect
INVALIDPARAMETER_AREAFORMATINCORRECT = 'InvalidParameter.AreaFormatIncorrect'

# InvalidParameter.ConfirmPasswordContentIncorrect
INVALIDPARAMETER_CONFIRMPASSWORDCONTENTINCORRECT = 'InvalidParameter.ConfirmPasswordContentIncorrect'

# InvalidParameter.CountryCodeContentIncorrect
INVALIDPARAMETER_COUNTRYCODECONTENTINCORRECT = 'InvalidParameter.CountryCodeContentIncorrect'

# InvalidParameter.CountryCodeFormatIncorrect
INVALIDPARAMETER_COUNTRYCODEFORMATINCORRECT = 'InvalidParameter.CountryCodeFormatIncorrect'

# InvalidParameter.MailFormatIncorrect
INVALIDPARAMETER_MAILFORMATINCORRECT = 'InvalidParameter.MailFormatIncorrect'

# Incorrect page parameter value.
INVALIDPARAMETER_PAGE = 'InvalidParameter.Page'

# InvalidParameter.PasswordContentIncorrect
INVALIDPARAMETER_PASSWORDCONTENTINCORRECT = 'InvalidParameter.PasswordContentIncorrect'

# InvalidParameter.PasswordFormatIncorrect
INVALIDPARAMETER_PASSWORDFORMATINCORRECT = 'InvalidParameter.PasswordFormatIncorrect'

# InvalidParameter.PhoneNumFormatIncorrect
INVALIDPARAMETER_PHONENUMFORMATINCORRECT = 'InvalidParameter.PhoneNumFormatIncorrect'

# Invalid parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# InvalidParameterValue.AccountTypeEmpty
INVALIDPARAMETERVALUE_ACCOUNTTYPEEMPTY = 'InvalidParameterValue.AccountTypeEmpty'

# InvalidParameterValue.AreaEmpty
INVALIDPARAMETERVALUE_AREAEMPTY = 'InvalidParameterValue.AreaEmpty'

# InvalidParameterValue.CountryCodeEmpty
INVALIDPARAMETERVALUE_COUNTRYCODEEMPTY = 'InvalidParameterValue.CountryCodeEmpty'

# The credit quota has exceeded the limit with the newly allocated quota.
INVALIDPARAMETERVALUE_CREDITAMOUNTOUTOFRANGE = 'InvalidParameterValue.CreditAmountOutOfRange'

# The dimension data entered is incorrect.
INVALIDPARAMETERVALUE_INVALIDDIMENSION = 'InvalidParameterValue.InvalidDimension'

# Incorrect month value
INVALIDPARAMETERVALUE_INVALIDMONTH = 'InvalidParameterValue.InvalidMonth'

# InvalidParameterValue.InvalidUin
INVALIDPARAMETERVALUE_INVALIDUIN = 'InvalidParameterValue.InvalidUin'

# InvalidParameterValue.MailEmpty
INVALIDPARAMETERVALUE_MAILEMPTY = 'InvalidParameterValue.MailEmpty'

# InvalidParameterValue.PasswordEmpty
INVALIDPARAMETERVALUE_PASSWORDEMPTY = 'InvalidParameterValue.PasswordEmpty'

# InvalidParameterValue.PhoneNumEmpty
INVALIDPARAMETERVALUE_PHONENUMEMPTY = 'InvalidParameterValue.PhoneNumEmpty'

# The primary industry id or secondary industry id is empty.
INVALIDPARAMETERVALUE_TRADEINFOEMPTY = 'InvalidParameterValue.TradeInfoEmpty'

# The user has already applied to become a sub - customer of another reseller.
INVALIDPARAMETERVALUE_UINALREADYAPPLIEDCLIENT = 'InvalidParameterValue.UinAlreadyAppliedClient'

# The user has become a sub-customer of another reseller.
INVALIDPARAMETERVALUE_UINALREADYCLIENT = 'InvalidParameterValue.UinAlreadyClient'

# The user has become a second - level reseller of another partner.
INVALIDPARAMETERVALUE_UINALREADYRESELLER = 'InvalidParameterValue.UinAlreadyReseller'

# The user is a sub-account.
INVALIDPARAMETERVALUE_UINISSUBACCOUNT = 'InvalidParameterValue.UinIsSubAccount'

# Invalid UinList. Array length value: 1-50.
INVALIDPARAMETERVALUE_UINLIST = 'InvalidParameterValue.UinList'

# The current region does not support creating a Tencent Cloud International account.
INVALIDPARAMETERVALUE_UNSUPPORTAREA = 'InvalidParameterValue.UnSupportArea'

# 
INVALIDPARAMETERVALUE_VOUCHERAMOUNTOUTOFRANGE = 'InvalidParameterValue.VoucherAmountOutOfRange'

# Missing parameter
MISSINGPARAMETER = 'MissingParameter'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# System busy. Please try again later.
OPERATIONDENIED_SERVICEBUSY = 'OperationDenied.ServiceBusy'

# Too many requests.
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# The current user is not a customer.
UNAUTHORIZEDOPERATION_NOTCUSTOMERUIN = 'UnauthorizedOperation.NotCustomerUin'

# The current user doesn’t have permission for the operation.
UNAUTHORIZEDOPERATION_UINNOAUTH = 'UnauthorizedOperation.UinNoAuth'

# Unknown parameter
UNKNOWNPARAMETER = 'UnknownParameter'
