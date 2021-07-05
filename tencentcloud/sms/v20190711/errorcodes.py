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


# The SMS message contains sensitive words. Please contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1) for assistance.
FAILEDOPERATION_CONTAINSENSITIVEWORD = 'FailedOperation.ContainSensitiveWord'

# Failed to parse the request packet. Generally, this is because that the API specification was not followed. Please see [Detailed Explanation of Request Body Parsing Error 1004](https://intl.cloud.tencent.com/document/product/382/9558?from_cn_redirect=1#.E8.BF.94.E5.9B.9E1014.E9.94.99.E8.AF.AF.E5.A6.82.E4.BD.95.E5.A4.84.E7.90.86.EF.BC.9F).
FAILEDOPERATION_FAILRESOLVEPACKET = 'FailedOperation.FailResolvePacket'

# The package balance is insufficient. Please [purchase a package](https://buy.cloud.tencent.com/sms).
FAILEDOPERATION_INSUFFICIENTBALANCEINSMSPACKAGE = 'FailedOperation.InsufficientBalanceInSmsPackage'

# Failed to parse the request packet.
FAILEDOPERATION_JSONPARSEFAIL = 'FailedOperation.JsonParseFail'

# Marketing SMS messages can only be sent between 8:00 and 22:00 in order not to disturb recipients.
FAILEDOPERATION_MARKETINGSENDTIMECONSTRAINT = 'FailedOperation.MarketingSendTimeConstraint'

# You cannot apply for a template before you apply for a signature. Please create a signature first as instructed in [Creating Signatures](https://intl.cloud.tencent.com/document/product/382/37794?from_cn_redirect=1#.E5.88.9B.E5.BB.BA.E7.AD.BE.E5.90.8D).
FAILEDOPERATION_MISSINGSIGNATURE = 'FailedOperation.MissingSignature'

# This signature ID has not been submitted for approval or does not exist, so it cannot be modified. Please check whether the `SignId` is entered correctly.
FAILEDOPERATION_MISSINGSIGNATURETOMODIFY = 'FailedOperation.MissingSignatureToModify'

# This template ID has not been submitted for approval or does not exist, so it cannot be modified. Please check whether the `TemplateId` is entered correctly.
FAILEDOPERATION_MISSINGTEMPLATETOMODIFY = 'FailedOperation.MissingTemplateToModify'

# Individual users cannot use the APIs related to signatures and templates. You can change your account identity type to enterprise as instructed [here](https://intl.cloud.tencent.com/document/product/378/34075?from_cn_redirect=1). The change will take effect in about one hour.
FAILEDOPERATION_NOTENTERPRISECERTIFICATION = 'FailedOperation.NotEnterpriseCertification'

# Other error. Generally, this is because that the carried parameter is non-compliant. For more information, please see the API description. If necessary, please contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) for assistance.
FAILEDOPERATION_OTHERERROR = 'FailedOperation.OtherError'

# The mobile number is in the blocklist. Generally, this is because that the recipient has unsubscribed or the carrier's blocklist was hit. You can contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) for assistance.
FAILEDOPERATION_PHONENUMBERINBLACKLIST = 'FailedOperation.PhoneNumberInBlacklist'

# The mobile number is in the blocklist. Usually, this is because that the user unsubscribed or the carrier's blocklist was hit. You can contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) for assistance.
FAILEDOPERATION_PHONENUMBERONBLACKLIST = 'FailedOperation.PhoneNumberOnBlacklist'

# The signature is in incorrect format or has not been approved. A signature can only contain 2-12 letters and digits. If the signature format is correct, please check whether it has been approved.
FAILEDOPERATION_SIGNATUREINCORRECTORUNAPPROVED = 'FailedOperation.SignatureIncorrectOrUnapproved'

# This template has been approved and cannot be modified again.
FAILEDOPERATION_TEMPLATEALREADYPASSEDCHECK = 'FailedOperation.TemplateAlreadyPassedCheck'

# The template content has not been approved or does not match the content of the approved template. Please see [Detailed Explanation of Error 1014](https://intl.cloud.tencent.com/document/product/382/9558?from_cn_redirect=1#.E8.BF.94.E5.9B.9E1014.E9.94.99.E8.AF.AF.E5.A6.82.E4.BD.95.E5.A4.84.E7.90.86.EF.BC.9F).
FAILEDOPERATION_TEMPLATEINCORRECTORUNAPPROVED = 'FailedOperation.TemplateIncorrectOrUnapproved'

# Other error. Please contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) and provide the failed mobile number for assistance.
INTERNALERROR_OTHERERROR = 'InternalError.OtherError'

# The request was initiated in an exceptional time. Generally, this is because that the difference between your server time and Tencent Cloud server time exceeds 10 minutes. Please check whether the server time and the time field in the API are correct.
INTERNALERROR_REQUESTTIMEEXCEPTION = 'InternalError.RequestTimeException'

# This RESTful API does not exist. Please check the RESTful API description.
INTERNALERROR_RESTAPIINTERFACENOTEXIST = 'InternalError.RestApiInterfaceNotExist'

# 
INTERNALERROR_SENDANDRECVFAIL = 'InternalError.SendAndRecvFail'

# The request packet in the backend packet does not have a `Sig` field or the `Sig` field is empty.
INTERNALERROR_SIGFIELDMISSING = 'InternalError.SigFieldMissing'

# `Sig` check on backend failed.
INTERNALERROR_SIGVERIFICATIONFAIL = 'InternalError.SigVerificationFail'

# The request to deliver an SMS message timed out. Please see [Detailed Explanation of Error 60008](https://intl.cloud.tencent.com/document/product/382/9558?from_cn_redirect=1#.E8.BF.94.E5.9B.9E60008.E9.94.99.E8.AF.AF.E5.A6.82.E4.BD.95.E5.A4.84.E7.90.86.EF.BC.9F).
INTERNALERROR_TIMEOUT = 'InternalError.Timeout'

# Unknown error.
INTERNALERROR_UNKNOWNERROR = 'InternalError.UnknownError'

# Invalid parameter.
INVALIDPARAMETER = 'InvalidParameter'

# The account does not match the application ID.
INVALIDPARAMETER_APPIDANDBIZID = 'InvalidParameter.AppidAndBizId'

# Incorrect `International` or `SmsType` parameter. If necessary, please contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) for assistance.
INVALIDPARAMETER_INVALIDPARAMETERS = 'InvalidParameter.InvalidParameters'

# The content of the requested SMS message is too long. For message length calculation rule, please see [Mainland China SMS Length Calculation Rule](https://intl.cloud.tencent.com/document/product/382/18058?from_cn_redirect=1).
INVALIDPARAMETERVALUE_CONTENTLENGTHLIMIT = 'InvalidParameterValue.ContentLengthLimit'

# The format of the uploaded transcoded image is incorrect. Please see the description of this field in the API description. If necessary, please contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) for assistance.
INVALIDPARAMETERVALUE_IMAGEINVALID = 'InvalidParameterValue.ImageInvalid'

# The format of the mobile number is incorrect. Please see [Detailed Explanation of Error 1016](https://intl.cloud.tencent.com/document/product/382/9558?from_cn_redirect=1#.E8.BF.94.E5.9B.9E1016.E9.94.99.E8.AF.AF.E5.A6.82.E4.BD.95.E5.A4.84.E7.90.86.EF.BC.9F).
INVALIDPARAMETERVALUE_INCORRECTPHONENUMBER = 'InvalidParameterValue.IncorrectPhoneNumber'

# `DocumentType` field check failed. Please see the description of this field in the API description. If necessary, please contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) for assistance.
INVALIDPARAMETERVALUE_INVALIDDOCUMENTTYPE = 'InvalidParameterValue.InvalidDocumentType'

# `International` field check failed. Please see the description of this field in the API description. If necessary, please contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) for assistance.
INVALIDPARAMETERVALUE_INVALIDINTERNATIONAL = 'InvalidParameterValue.InvalidInternational'

# Invalid start time or end time. The reason may be that the requested SendDateTime is later than EndDateTime.
INVALIDPARAMETERVALUE_INVALIDSTARTTIME = 'InvalidParameterValue.InvalidStartTime'

# `UsedMethod` field check failed. Please see the description of this field in the API description. If necessary, please contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) for assistance.
INVALIDPARAMETERVALUE_INVALIDUSEDMETHOD = 'InvalidParameterValue.InvalidUsedMethod'

# Unable to identify the signature. Generally, this is because that the signature has not been approved. Please check whether the signature has been approved. For more information, please see [Signature Review](https://intl.cloud.tencent.com/document/product/382/37745?from_cn_redirect=1#.E6.AD.A5.E9.AA.A43.EF.BC.9A.E7.AD.89.E5.BE.85.E5.AE.A1.E6.A0.B8).
INVALIDPARAMETERVALUE_MISSINGSIGNATURELIST = 'InvalidParameterValue.MissingSignatureList'

# URLs are not allowed in template variables.
INVALIDPARAMETERVALUE_PROHIBITEDUSEURLINTEMPLATEPARAMETER = 'InvalidParameterValue.ProhibitedUseUrlInTemplateParameter'

# The `SdkAppid` does not exist.
INVALIDPARAMETERVALUE_SDKAPPIDNOTEXIST = 'InvalidParameterValue.SdkAppidNotExist'

# This signature has been approved and cannot be modified again.
INVALIDPARAMETERVALUE_SIGNALREADYPASSEDCHECK = 'InvalidParameterValue.SignAlreadyPassedCheck'

# The parameter format of the verification code template is incorrect. For a verification code template, only 0-6 digits can be passed in as the template variable.
INVALIDPARAMETERVALUE_TEMPLATEPARAMETERFORMATERROR = 'InvalidParameterValue.TemplateParameterFormatError'

# There are more than 12 characters in a single template variable. There is no upper limit of variable characters for enterprise users. You can change your account identity type to enterprise as instructed [here](https://intl.cloud.tencent.com/document/product/378/34075?from_cn_redirect=1). The limit change will take effect in about one hour.
INVALIDPARAMETERVALUE_TEMPLATEPARAMETERLENGTHLIMIT = 'InvalidParameterValue.TemplateParameterLengthLimit'

# The number of SMS messages delivered on the current day exceeds the set upper limit. You can adjust the SMS frequency limit policy in the console.
LIMITEXCEEDED_APPDAILYLIMIT = 'LimitExceeded.AppDailyLimit'

# The number of SMS messages delivered on the current day exceeds the set upper limit (for global SMS). If you want to adjust the limit, please contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1) for assistance.
LIMITEXCEEDED_DAILYLIMIT = 'LimitExceeded.DailyLimit'

# The SMS delivery hit the frequency limit policy. You can adjust the policy in the console. If you have other requirements, please contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) for assistance.
LIMITEXCEEDED_DELIVERYFREQUENCYLIMIT = 'LimitExceeded.DeliveryFrequencyLimit'

# There are more than 200 mobile numbers submitted in a single call of the SMS delivery API. Please follow the requirements in [API Description](https://intl.cloud.tencent.com/document/product/382/38778?from_cn_redirect=1).
LIMITEXCEEDED_PHONENUMBERCOUNTLIMIT = 'LimitExceeded.PhoneNumberCountLimit'

# The number of SMS messages delivered to a single mobile number on the current day exceeds the set upper limit. You can adjust the SMS frequency limit policy in the console.
LIMITEXCEEDED_PHONENUMBERDAILYLIMIT = 'LimitExceeded.PhoneNumberDailyLimit'

# The number of SMS messages delivered to a single mobile number within 1 hour exceeds the set upper limit. You can adjust the SMS frequency limit policy in the console.
LIMITEXCEEDED_PHONENUMBERONEHOURLIMIT = 'LimitExceeded.PhoneNumberOneHourLimit'

# The number of identical SMS messages delivered to a single mobile number exceeds the set upper limit. You can adjust the SMS frequency limit policy in the console.
LIMITEXCEEDED_PHONENUMBERSAMECONTENTDAILYLIMIT = 'LimitExceeded.PhoneNumberSameContentDailyLimit'

# The number of SMS messages delivered to a single mobile number within 30 seconds exceeds the set upper limit. You can adjust the SMS frequency limit policy in the console
LIMITEXCEEDED_PHONENUMBERTHIRTYSECONDLIMIT = 'LimitExceeded.PhoneNumberThirtySecondLimit'

# Missing parameter.
MISSINGPARAMETER = 'MissingParameter'

# The list of mobile numbers passed in is empty. Please check whether numbers are present in your parameters.
MISSINGPARAMETER_EMPTYPHONENUMBERSET = 'MissingParameter.EmptyPhoneNumberSet'

# Individual users do not have permission to send marketing SMS messages. Please see [here](https://intl.cloud.tencent.com/document/product/382/13444?from_cn_redirect=1).
UNAUTHORIZEDOPERATION_INDIVIDUALUSERMARKETINGSMSPERMISSIONDENY = 'UnauthorizedOperation.IndividualUserMarketingSmsPermissionDeny'

# The requesting IP is not in the whitelist. You have configured verification of request source IP, but the current requesting IP is not in the configured whitelist. If necessary, please contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) for assistance.
UNAUTHORIZEDOPERATION_REQUESTIPNOTINWHITELIST = 'UnauthorizedOperation.RequestIpNotInWhitelist'

# You do not have permission to make the request. Please contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) for assistance.
UNAUTHORIZEDOPERATION_REQUESTPERMISSIONDENY = 'UnauthorizedOperation.RequestPermissionDeny'

# This `sdkappid` is forbidden to provide services. If necessary, please contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) for assistance.
UNAUTHORIZEDOPERATION_SDKAPPIDISDISABLED = 'UnauthorizedOperation.SdkAppidIsDisabled'

# The service has been suspended due to arrears. You can log in to Tencent Cloud to top up your account.
UNAUTHORIZEDOPERATION_SERIVCESUSPENDDUETOARREARS = 'UnauthorizedOperation.SerivceSuspendDueToArrears'

# `SmsSdkAppid` check failed.
UNAUTHORIZEDOPERATION_SMSSDKAPPIDVERIFYFAIL = 'UnauthorizedOperation.SmsSdkAppidVerifyFail'

# This request is not supported.
UNSUPPORTEDOPERATION_ = 'UnsupportedOperation.'

# The bulk SMS request contains both Mainland China and global mobile numbers.
UNSUPPORTEDOPERATION_CONTAINDOMESTICANDINTERNATIONALPHONENUMBER = 'UnsupportedOperation.ContainDomesticAndInternationalPhoneNumber'

# SMS delivery to this region is not supported.
UNSUPPORTEDOPERATION_UNSUPORTEDREGION = 'UnsupportedOperation.UnsuportedRegion'
