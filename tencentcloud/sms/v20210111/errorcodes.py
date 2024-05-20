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


# The SMS message contains sensitive words. You can contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) for assistance.
FAILEDOPERATION_CONTAINSENSITIVEWORD = 'FailedOperation.ContainSensitiveWord'

# Failed to parse the request packet. Usually, this is because that the API specification was not followed. Please see [Detailed Explanation of Request Body Parsing Error 1004](https://intl.cloud.tencent.com/document/product/382/9558?from_cn_redirect=1#.E8.BF.94.E5.9B.9E1004.E9.94.99.E8.AF.AF.E5.A6.82.E4.BD.95.E5.A4.84.E7.90.86.EF.BC.9F).
FAILEDOPERATION_FAILRESOLVEPACKET = 'FailedOperation.FailResolvePacket'

# Individual users cannot apply for sending marketing SMS messages.
FAILEDOPERATION_FORBIDADDMARKETINGTEMPLATES = 'FailedOperation.ForbidAddMarketingTemplates'

# The package balance is insufficient. Please [purchase an SMS package](https://buy.cloud.tencent.com/sms).
FAILEDOPERATION_INSUFFICIENTBALANCEINSMSPACKAGE = 'FailedOperation.InsufficientBalanceInSmsPackage'

# Failed to parse the request body.
FAILEDOPERATION_JSONPARSEFAIL = 'FailedOperation.JsonParseFail'

# Marketing SMS messages can only be sent between 8:00 and 22:00 in order not to disturb recipients.
FAILEDOPERATION_MARKETINGSENDTIMECONSTRAINT = 'FailedOperation.MarketingSendTimeConstraint'

# You cannot apply for a template before you apply for a signature. Please create a signature first as instructed in [Creating Signature](https://www.tencentcloud.com/document/product/382/35460).
FAILEDOPERATION_MISSINGSIGNATURE = 'FailedOperation.MissingSignature'

# Unable to identify the signature. Please check whether the signature has been approved. For more information, see the signature approval section in [Getting Started](https://www.tencentcloud.com/jp/document/product/382/35452).
FAILEDOPERATION_MISSINGSIGNATURELIST = 'FailedOperation.MissingSignatureList'

# This signature ID has not been submitted for approval or does not exist, so it cannot be modified. Please check whether the `SignId` is entered correctly.
FAILEDOPERATION_MISSINGSIGNATURETOMODIFY = 'FailedOperation.MissingSignatureToModify'

# Unable to identify the template. Please check whether the template has been approved. For more information, see the template approval section in [Getting Started](https://www.tencentcloud.com/document/product/382/35452).
FAILEDOPERATION_MISSINGTEMPLATELIST = 'FailedOperation.MissingTemplateList'

# This template ID has not been submitted for approval or does not exist, so it cannot be modified. Please check whether the `TemplateId` is entered correctly.
FAILEDOPERATION_MISSINGTEMPLATETOMODIFY = 'FailedOperation.MissingTemplateToModify'

# Individual users cannot use the APIs related to signatures and templates. You can change your account identity type to enterprise as instructed [here](https://www.tencentcloud.com/zh/document/product/378/37276). The change will take effect in about one hour.
FAILEDOPERATION_NOTENTERPRISECERTIFICATION = 'FailedOperation.NotEnterpriseCertification'

# Other error. Usually, this is because that the carried parameter is non-compliant. For more information, see the API description. If necessary, you can contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) for assistance.
FAILEDOPERATION_OTHERERROR = 'FailedOperation.OtherError'

# Unknown error. If necessary, you can contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) for assistance.
FAILEDOPERATION_PARAMETERSOTHERERROR = 'FailedOperation.ParametersOtherError'

# The mobile number is in the opt-out list. This may be because the recipient has unsubscribed from your service or the mobile number is in the carrier’s opt-out list. To solve this problem, contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81).
FAILEDOPERATION_PHONENUMBERINBLACKLIST = 'FailedOperation.PhoneNumberInBlacklist'

# Failed to parse the mobile number. Please check whether it meets the E.164 standard.
FAILEDOPERATION_PHONENUMBERPARSEFAIL = 'FailedOperation.PhoneNumberParseFail'

# Non-Root accounts cannot use the template list pull feature. You can use the TencentCloud API key of your root account to call the API.
FAILEDOPERATION_PROHIBITSUBACCOUNTUSE = 'FailedOperation.ProhibitSubAccountUse'

# The signature ID does not exist.
FAILEDOPERATION_SIGNIDNOTEXIST = 'FailedOperation.SignIdNotExist'

# The number of signatures has reached the maximum value.
FAILEDOPERATION_SIGNNUMBERLIMIT = 'FailedOperation.SignNumberLimit'

# The signature is not approved or in an incorrect format. (1) Log in to the [SMS console](https://console.cloud.tencent.com/smsv2) and check whether the signature has been approved; (2) Check whether the signature is in compliance with the format specification, that is, it can contain 2–12 letters and digits. If you have any questions, contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) for assistance.
FAILEDOPERATION_SIGNATUREINCORRECTORUNAPPROVED = 'FailedOperation.SignatureIncorrectOrUnapproved'

# This template has been approved and cannot be modified again.
FAILEDOPERATION_TEMPLATEALREADYPASSEDCHECK = 'FailedOperation.TemplateAlreadyPassedCheck'

# The template ID does not exist.
FAILEDOPERATION_TEMPLATEIDNOTEXIST = 'FailedOperation.TemplateIdNotExist'

# The template has not been approved or its content does not match that of the approved template. (1) Please log in to the [SMS console](https://console.cloud.tencent.com/smsv2) to check whether the template has been reviewed and approved. (2) Please click [here](https://intl.cloud.tencent.com/document/product/382/9558?from_cn_redirect=1#.E8.BF.94.E5.9B.9E1014.E9.94.99.E8.AF.AF.E5.A6.82.E4.BD.95.E5.A4.84.E7.90.86.EF.BC.9F) to check whether the template format is correct. If you have any questions, contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81).
FAILEDOPERATION_TEMPLATEINCORRECTORUNAPPROVED = 'FailedOperation.TemplateIncorrectOrUnapproved'

# The number of templates has reached the maximum value.
FAILEDOPERATION_TEMPLATENUMBERLIMIT = 'FailedOperation.TemplateNumberLimit'

# The request content does not match that of the approved template. Please check whether the number of parameters in the request is consistent with that in the approved template. If you have any questions, contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81).
FAILEDOPERATION_TEMPLATEPARAMSETNOTMATCHAPPROVEDTEMPLATE = 'FailedOperation.TemplateParamSetNotMatchApprovedTemplate'

# The template has not been approved or does not exist. Please log in to the [SMS console](https://console.cloud.tencent.com/smsv2) to check whether the template has been reviewed and approved. If you have any questions, contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81).
FAILEDOPERATION_TEMPLATEUNAPPROVEDORNOTEXIST = 'FailedOperation.TemplateUnapprovedOrNotExist'

# Failed to parse the user parameter. You can contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) for assistance.
INTERNALERROR_JSONPARSEFAIL = 'InternalError.JsonParseFail'

# Other error. You can contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) and provide the failed mobile number for assistance.
INTERNALERROR_OTHERERROR = 'InternalError.OtherError'

# Failed to parse the carrier’s response packet. Please contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) for assistance.
INTERNALERROR_PARSEBACKENDRESPONSEFAIL = 'InternalError.ParseBackendResponseFail'

# The request was initiated in an exceptional time. Usually, this is because that the difference between your server time and Tencent Cloud server time exceeds 10 minutes. Please check whether the server time and the time field in the API are correct.
INTERNALERROR_REQUESTTIMEEXCEPTION = 'InternalError.RequestTimeException'

# This RESTful API does not exist. Please check the RESTful API description.
INTERNALERROR_RESTAPIINTERFACENOTEXIST = 'InternalError.RestApiInterfaceNotExist'

# The API timed out or SMS packet sending/receiving timed out. You need to check whether your network jitters or contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) for assistance.
INTERNALERROR_SENDANDRECVFAIL = 'InternalError.SendAndRecvFail'

# The request body in the backend body does not have a `Sig` field or the `Sig` field is empty.
INTERNALERROR_SIGFIELDMISSING = 'InternalError.SigFieldMissing'

# Backend check of `Sig` failed.
INTERNALERROR_SIGVERIFICATIONFAIL = 'InternalError.SigVerificationFail'

# The request to deliver an SMS message timed out. Please see [Detailed Explanation of Error 60008](https://intl.cloud.tencent.com/document/product/382/9558?from_cn_redirect=1#.E8.BF.94.E5.9B.9E60008.E9.94.99.E8.AF.AF.E5.A6.82.E4.BD.95.E5.A4.84.E7.90.86.EF.BC.9F).
INTERNALERROR_TIMEOUT = 'InternalError.Timeout'

# Unknown error.
INTERNALERROR_UNKNOWNERROR = 'InternalError.UnknownError'

# A parameter error occurred.
INVALIDPARAMETER = 'InvalidParameter'

# The account does not match the application ID.
INVALIDPARAMETER_APPIDANDBIZID = 'InvalidParameter.AppidAndBizId'

# There are sensitive words.
INVALIDPARAMETER_DIRTYWORDFOUND = 'InvalidParameter.DirtyWordFound'

# Invalid parameter. If you have any questions, contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81).
INVALIDPARAMETER_INVALIDPARAMETERS = 'InvalidParameter.InvalidParameters'

# `BeginTime` parameter check failed.
INVALIDPARAMETERVALUE_BEGINTIMEVERIFYFAIL = 'InvalidParameterValue.BeginTimeVerifyFail'

# The content of the requested SMS message is too long. For message length calculation rule, please see [SMS Length Calculation Rule](https://www.tencentcloud.com/document/product/382/18052#sms-length-calculation-rule).
INVALIDPARAMETERVALUE_CONTENTLENGTHLIMIT = 'InvalidParameterValue.ContentLengthLimit'

# `EndTime` parameter check failed.
INVALIDPARAMETERVALUE_ENDTIMEVERIFYFAIL = 'InvalidParameterValue.EndTimeVerifyFail'

# The format of the uploaded transcoded image is incorrect. See the description of this field in the API description. If necessary, you can contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) for assistance.
INVALIDPARAMETERVALUE_IMAGEINVALID = 'InvalidParameterValue.ImageInvalid'

# Incorrect mobile number format
INVALIDPARAMETERVALUE_INCORRECTPHONENUMBER = 'InvalidParameterValue.IncorrectPhoneNumber'

# `DocumentType` field check failed. See the description of this field in the API description. If necessary, you can contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) for assistance.
INVALIDPARAMETERVALUE_INVALIDDOCUMENTTYPE = 'InvalidParameterValue.InvalidDocumentType'

# `International` field check failed. See the description of this field in the API description. If necessary, you can contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) for assistance.
INVALIDPARAMETERVALUE_INVALIDINTERNATIONAL = 'InvalidParameterValue.InvalidInternational'

# `SignPurpose` field check failed. See the description of this field in the API description. If necessary, you can contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) for assistance.
INVALIDPARAMETERVALUE_INVALIDSIGNPURPOSE = 'InvalidParameterValue.InvalidSignPurpose'

# Invalid start time or end time. The reason may be that the requested `SendDateTime` is later than `EndDateTime`.
INVALIDPARAMETERVALUE_INVALIDSTARTTIME = 'InvalidParameterValue.InvalidStartTime'

# The template format is incorrect. For more information, please see [Body Template Review Standards](https://intl.cloud.tencent.com/document/product/382/39023?from_cn_redirect=1).
INVALIDPARAMETERVALUE_INVALIDTEMPLATEFORMAT = 'InvalidParameterValue.InvalidTemplateFormat'

# `UsedMethod` field check failed. See the description of this field in the API description. If necessary, you can contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) for assistance.
INVALIDPARAMETERVALUE_INVALIDUSEDMETHOD = 'InvalidParameterValue.InvalidUsedMethod'

# `Limit` parameter check failed.
INVALIDPARAMETERVALUE_LIMITVERIFYFAIL = 'InvalidParameterValue.LimitVerifyFail'

# Marketing messages must include an unsubscribe method.
INVALIDPARAMETERVALUE_MARKETINGTEMPLATEWITHOUTUNSUBSCRIBE = 'InvalidParameterValue.MarketingTemplateWithoutUnsubscribe'

# `Offset` parameter check failed.
INVALIDPARAMETERVALUE_OFFSETVERIFYFAIL = 'InvalidParameterValue.OffsetVerifyFail'

# URLs are not allowed in template variables.
INVALIDPARAMETERVALUE_PROHIBITEDUSEURLINTEMPLATEPARAMETER = 'InvalidParameterValue.ProhibitedUseUrlInTemplateParameter'

# The `SdkAppId` does not exist.
INVALIDPARAMETERVALUE_SDKAPPIDNOTEXIST = 'InvalidParameterValue.SdkAppIdNotExist'

# This signature has been approved and cannot be modified again.
INVALIDPARAMETERVALUE_SIGNALREADYPASSEDCHECK = 'InvalidParameterValue.SignAlreadyPassedCheck'

# The same signature pending review already exists.
INVALIDPARAMETERVALUE_SIGNEXISTANDUNAPPROVED = 'InvalidParameterValue.SignExistAndUnapproved'

# Too much signature content
INVALIDPARAMETERVALUE_SIGNNAMELENGTHTOOLONG = 'InvalidParameterValue.SignNameLengthTooLong'

# The parameter format of the verification code template is incorrect. For a verification code template, only 0–6 digits can be passed in as the template variable.
INVALIDPARAMETERVALUE_TEMPLATEPARAMETERFORMATERROR = 'InvalidParameterValue.TemplateParameterFormatError'

# There are more than 12 characters in a single template variable. There is no upper limit of variable characters for enterprise users. You can change your account identity type to enterprise as instructed [here](https://www.tencentcloud.com/zh/document/product/378/37276). The limit change will take effect in about one hour.
INVALIDPARAMETERVALUE_TEMPLATEPARAMETERLENGTHLIMIT = 'InvalidParameterValue.TemplateParameterLengthLimit'

# The template content contains sensitive words. For more information, please see [Body Template Review Standards](https://intl.cloud.tencent.com/document/product/382/39023?from_cn_redirect=1).
INVALIDPARAMETERVALUE_TEMPLATEWITHDIRTYWORDS = 'InvalidParameterValue.TemplateWithDirtyWords'

# The number of Global SMS messages sent to the specified country/region per day has exceeded the preset limit. You can adjust the message sending limit in **Application Management** > **Basic Configuration** in the SMS console.
LIMITEXCEEDED_APPCOUNTRYORREGIONDAILYLIMIT = 'LimitExceeded.AppCountryOrRegionDailyLimit'

# The Global SMS message failed to be sent because the recipient country/region is not included in the specified country/region list. You can adjust the country/region list in **Application Management** > **Basic Configuration** in the SMS console.
LIMITEXCEEDED_APPCOUNTRYORREGIONINBLACKLIST = 'LimitExceeded.AppCountryOrRegionInBlacklist'

# The number of SMS messages delivered on the current day exceeds the set upper limit. You can adjust the SMS delivery rate limit policy in the console.
LIMITEXCEEDED_APPDAILYLIMIT = 'LimitExceeded.AppDailyLimit'

# The number of Global SMS messages sent per day has exceeded the preset limit. You can adjust the message sending threshold in **Application Management** > **Basic Configuration** in the SMS console.
LIMITEXCEEDED_APPGLOBALDAILYLIMIT = 'LimitExceeded.AppGlobalDailyLimit'

# The number of Chinese Mainland SMS messages sent per day has exceeded the preset limit. You can adjust the message sending threshold in **Application Management** > **Basic Configuration** in the SMS console.
LIMITEXCEEDED_APPMAINLANDCHINADAILYLIMIT = 'LimitExceeded.AppMainlandChinaDailyLimit'

# The number of SMS messages delivered on the current day exceeds the set upper limit (for Global SMS). If you want to adjust the limit, you can contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1) for assistance.
LIMITEXCEEDED_DAILYLIMIT = 'LimitExceeded.DailyLimit'

# The SMS delivery hits the delivery rate limit policy. You can adjust the policy in the console. If you have other requirements, you can contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) for assistance.
LIMITEXCEEDED_DELIVERYFREQUENCYLIMIT = 'LimitExceeded.DeliveryFrequencyLimit'

# The number of mobile numbers you query at a time exceeds 200. Please refer to the input parameter `PhoneNumberSet`.
LIMITEXCEEDED_PHONENUMBERCOUNTLIMIT = 'LimitExceeded.PhoneNumberCountLimit'

# The number of SMS messages delivered to a single mobile number on the current day exceeds the set upper limit. You can adjust the SMS delivery rate limit policy in the console.
LIMITEXCEEDED_PHONENUMBERDAILYLIMIT = 'LimitExceeded.PhoneNumberDailyLimit'

# The number of SMS messages delivered to a single mobile number within 1 hour exceeds the set upper limit. You can adjust the SMS delivery rate limit policy in the console.
LIMITEXCEEDED_PHONENUMBERONEHOURLIMIT = 'LimitExceeded.PhoneNumberOneHourLimit'

# The number of identical SMS messages delivered to a single mobile number exceeds the set upper limit. You can adjust the SMS delivery rate limit policy in the console.
LIMITEXCEEDED_PHONENUMBERSAMECONTENTDAILYLIMIT = 'LimitExceeded.PhoneNumberSameContentDailyLimit'

# The number of SMS messages delivered to a single mobile number within 30 seconds exceeds the set upper limit. You can adjust the SMS delivery rate limit policy in the console
LIMITEXCEEDED_PHONENUMBERTHIRTYSECONDLIMIT = 'LimitExceeded.PhoneNumberThirtySecondLimit'

# Missing parameters. Please check and try again.
MISSINGPARAMETER = 'MissingParameter'

# The list of mobile numbers passed in is empty. Please check whether numbers are present in your parameters.
MISSINGPARAMETER_EMPTYPHONENUMBERSET = 'MissingParameter.EmptyPhoneNumberSet'

# Individual users do not have permission to send marketing SMS messages. Please see [Differences in Rights](https://intl.cloud.tencent.com/document/product/382/13444?from_cn_redirect=1).
UNAUTHORIZEDOPERATION_INDIVIDUALUSERMARKETINGSMSPERMISSIONDENY = 'UnauthorizedOperation.IndividualUserMarketingSmsPermissionDeny'

# The requesting IP is not in the allowlist. You have configured the verification of request source IP, but the current requesting IP is not in the configured allowlist. If necessary, you can contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81).
UNAUTHORIZEDOPERATION_REQUESTIPNOTINWHITELIST = 'UnauthorizedOperation.RequestIpNotInWhitelist'

# The request does not have permission. You can contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81).
UNAUTHORIZEDOPERATION_REQUESTPERMISSIONDENY = 'UnauthorizedOperation.RequestPermissionDeny'

# This `SdkAppId` is forbidden to provide services. If necessary, you can contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81).
UNAUTHORIZEDOPERATION_SDKAPPIDISDISABLED = 'UnauthorizedOperation.SdkAppIdIsDisabled'

# If the service is suspended due to outstanding fees, you can log in to Tencent Cloud to recharge and clear the debt on your own.
UNAUTHORIZEDOPERATION_SERVICESUSPENDDUETOARREARS = 'UnauthorizedOperation.ServiceSuspendDueToArrears'

# Failed to verify `SmsSdkAppId`. Please check whether [SmsSdkAppId](https://console.cloud.tencent.com/smsv2/app-manage) is under the account associated with the [TencentCloud API key](https://console.cloud.tencent.com/cam/capi).
UNAUTHORIZEDOPERATION_SMSSDKAPPIDVERIFYFAIL = 'UnauthorizedOperation.SmsSdkAppIdVerifyFail'

# The request is not supported.
UNSUPPORTEDOPERATION_ = 'UnsupportedOperation.'

# A Chinese Mainland SMS template cannot be used to sent messages to global numbers. Please use a Global SMS template instead.
UNSUPPORTEDOPERATION_CHINESEMAINLANDTEMPLATETOGLOBALPHONE = 'UnsupportedOperation.ChineseMainlandTemplateToGlobalPhone'

# The group message request contains both Chinese mainland numbers and international numbers. Please check: (1) whether the message is sent to international numbers with a Chinese mainland signature or template; (2) whether the message is sent to Chinese mainland numbers with an international signature or template.
UNSUPPORTEDOPERATION_CONTAINDOMESTICANDINTERNATIONALPHONENUMBER = 'UnsupportedOperation.ContainDomesticAndInternationalPhoneNumber'

# A Global SMS template cannot be used to sent messages to Chinese mainland numbers. Please use a Chinese Mainland SMS template instead.
UNSUPPORTEDOPERATION_GLOBALTEMPLATETOCHINESEMAINLANDPHONE = 'UnsupportedOperation.GlobalTemplateToChineseMainlandPhone'

# 
UNSUPPORTEDOPERATION_UNSUPPORTEDREGION = 'UnsupportedOperation.UnsupportedRegion'
