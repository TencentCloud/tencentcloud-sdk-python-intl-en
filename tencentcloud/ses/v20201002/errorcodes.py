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


# CAM token authentication failure.
AUTHFAILURE_UNAUTHORIZEDOPERATION = 'AuthFailure.UnauthorizedOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# The attachments are too large. Make sure they do not exceed the size limit for a single attachment and the overall limit for all attachments.
FAILEDOPERATION_ATTACHCONTENTTOOLARGE = 'FailedOperation.AttachContentToolarge'

# The email address is in the blocklist.
FAILEDOPERATION_EMAILADDRINBLACKLIST = 'FailedOperation.EmailAddrInBlacklist'

# The email is too large. Remove some content.
FAILEDOPERATION_EMAILCONTENTTOOLARGE = 'FailedOperation.EmailContentToolarge'

# The number of emails exceeds the daily sending limit.
FAILEDOPERATION_EXCEEDSENDLIMIT = 'FailedOperation.ExceedSendLimit'

# The number of templates exceeds the upper limit.
FAILEDOPERATION_EXCEEDTEMPLATELIMIT = 'FailedOperation.ExceedTemplateLimit'

# You have sent too many emails to the same address in a short period.
FAILEDOPERATION_FREQUENCYLIMIT = 'FailedOperation.FrequencyLimit'

# The email has been blocked temporarily due to high rejection rate.
FAILEDOPERATION_HIGHREJECTIONRATE = 'FailedOperation.HighRejectionRate'

# Mail contains non-compliant link.
FAILEDOPERATION_ILLEGALURL = 'FailedOperation.IllegalURL'

# Incorrect email address.
FAILEDOPERATION_INCORRECTEMAIL = 'FailedOperation.IncorrectEmail'

# Incorrect sender format. Follow the sample in this document.
FAILEDOPERATION_INCORRECTSENDER = 'FailedOperation.IncorrectSender'

# Insufficient balance or account in arrears.
FAILEDOPERATION_INSUFFICIENTBALANCE = 'FailedOperation.InsufficientBalance'

# Insufficient emails in plans.
FAILEDOPERATION_INSUFFICIENTQUOTA = 'FailedOperation.InsufficientQuota'

# Unsupported attachment name. please check whether the attachment name contains special characters. for details, see the appendix attachment description (https://www.tencentcloud.comom/document/product/1288/51951?from_cn_redirect=1).
FAILEDOPERATION_INVALIDATTACHNAME = 'FailedOperation.InvalidAttachName'

# Reached the query limit (100).
FAILEDOPERATION_INVALIDLIMIT = 'FailedOperation.InvalidLimit'

# Invalid template ID or unavailable template.
FAILEDOPERATION_INVALIDTEMPLATEID = 'FailedOperation.InvalidTemplateID'

# Missing email content (`TemplateData` and `Simple` cannot be both empty).
FAILEDOPERATION_MISSINGEMAILCONTENT = 'FailedOperation.MissingEmailContent'

# No permission to send an email with attachments.
FAILEDOPERATION_NOATTACHPERMISSION = 'FailedOperation.NoAttachPermission'

# Unable to send because the sender is not verified.
FAILEDOPERATION_NOTAUTHENTICATEDSENDER = 'FailedOperation.NotAuthenticatedSender'

# You cannot query email records for this date. Only data within 90 days can be queried.
FAILEDOPERATION_NOTSUPPORTDATE = 'FailedOperation.NotSupportDate'

# Incorrect protocol. Make sure the protocol is correct.
FAILEDOPERATION_PROTOCOLCHECKERR = 'FailedOperation.ProtocolCheckErr'

# The recipient has unsubscribed.
FAILEDOPERATION_RECEIVERHASUNSUBSCRIBED = 'FailedOperation.ReceiverHasUnsubscribed'

# The message was rejected by the recipient.
FAILEDOPERATION_REJECTEDBYRECIPIENTS = 'FailedOperation.RejectedByRecipients'

# Email sending error. Please submit a ticket to us for troubleshooting.
FAILEDOPERATION_SENDEMAILERR = 'FailedOperation.SendEmailErr'

# The request has not taken effect. Try again.
FAILEDOPERATION_SERVICENOTAVAILABLE = 'FailedOperation.ServiceNotAvailable'

# The template size is too large. Reduce the size.
FAILEDOPERATION_TEMPLATECONTENTTOOLARGE = 'FailedOperation.TemplateContentToolarge'

# The email push platform will suspend sending emails to the service provider for 10 minutes due to the corresponding recipient service provider's limit. it will be automatically released after 10 minutes.
FAILEDOPERATION_TEMPORARYBLOCKED = 'FailedOperation.TemporaryBlocked'

# Too many attachments. A single email supports up to 10 attachments.
FAILEDOPERATION_TOOMANYATTACHMENTS = 'FailedOperation.TooManyAttachments'

# Too many recipients. Set a maximum of 50 recipients at a time.
FAILEDOPERATION_TOOMANYRECIPIENTS = 'FailedOperation.TooManyRecipients'

# Forbid users with low delivery rate to include URL webpage links in email content.
FAILEDOPERATION_URLFORBIDDEN = 'FailedOperation.URLForbidden'

# Unsupported email type.
FAILEDOPERATION_UNSUPPORTMAILTYPE = 'FailedOperation.UnsupportMailType'

# You can only send emails by using a template.
FAILEDOPERATION_WITHOUTPERMISSION = 'FailedOperation.WithOutPermission'

# The format of the `TemplateData` field is incorrect. Make sure it is in JSON format.
FAILEDOPERATION_WRONGCONTENTJSON = 'FailedOperation.WrongContentJson'

# Internal error.
INTERNALERROR = 'InternalError'

# Incorrect parameter.
INVALIDPARAMETER = 'InvalidParameter'

# Invalid parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Incorrect attachment content. Make sure the base64 content is correct.
INVALIDPARAMETERVALUE_ATTACHCONTENTISWRONG = 'InvalidParameterValue.AttachContentIsWrong'

# The start time cannot be earlier than the current time.
INVALIDPARAMETERVALUE_BEGINTIMEBEFORENOW = 'InvalidParameterValue.BeginTimeBeforeNow'

# This sender domain has been created by another Tencent Cloud account.
INVALIDPARAMETERVALUE_CREATEDBYOTHER = 'InvalidParameterValue.CreatedByOther'

# The recipient or sender address is empty. Please check.
INVALIDPARAMETERVALUE_EMAILADDRESSISNULL = 'InvalidParameterValue.EmailAddressIsNULL'

# Incorrect email content. Make sure TEXT/HTML base64 is correct.
INVALIDPARAMETERVALUE_EMAILCONTENTISWRONG = 'InvalidParameterValue.EmailContentIsWrong'

# Invalid email address. Make sure the address format is correct.
INVALIDPARAMETERVALUE_ILLEGALEMAILADDRESS = 'InvalidParameterValue.IllegalEmailAddress'

# The sender alias is incorrect.
INVALIDPARAMETERVALUE_ILLEGALSENDERNAME = 'InvalidParameterValue.IllegalSenderName'

# The template parameter attached to the recipient address cannot contain html tags.
INVALIDPARAMETERVALUE_INVALIDTEMPLATEDATA = 'InvalidParameterValue.InValidTemplateData'

# Invalid domain value.
INVALIDPARAMETERVALUE_INVALIDEMAILIDENTITY = 'InvalidParameterValue.InvalidEmailIdentity'

# The password can contain 10-20 characters and must contain at least 2 unique digits, lowercase letters, and uppercase letters.
INVALIDPARAMETERVALUE_INVALIDSMTPPASSWORD = 'InvalidParameterValue.InvalidSmtpPassWord'

# You don’t have the sender address. Check if it exists.
INVALIDPARAMETERVALUE_NOSUCHSENDER = 'InvalidParameterValue.NoSuchSender'

# This sender domain does not exist. Create it first.
INVALIDPARAMETERVALUE_NOTEXISTDOMAIN = 'InvalidParameterValue.NotExistDomain'

# Invalid recipient group description. The description cannot contain special characters and must contain 1 to 300 characters.
INVALIDPARAMETERVALUE_RECEIVERDESCILLEGAL = 'InvalidParameterValue.ReceiverDescIllegal'

# The recipient address is incorrect.
INVALIDPARAMETERVALUE_RECEIVEREMAILINVALID = 'InvalidParameterValue.ReceiverEmailInvalid'

# Invalid recipient group name. Check the name and its size.
INVALIDPARAMETERVALUE_RECEIVERNAMEILLEGAL = 'InvalidParameterValue.ReceiverNameIllegal'

# This sender domain already exists. Do not create it again.
INVALIDPARAMETERVALUE_REPEATCREATION = 'InvalidParameterValue.RepeatCreation'

# This email address already exists. Do not create it again.
INVALIDPARAMETERVALUE_REPEATEMAILADDRESS = 'InvalidParameterValue.RepeatEmailAddress'

# Duplicate recipient group name.
INVALIDPARAMETERVALUE_REPEATRECEIVERNAME = 'InvalidParameterValue.RepeatReceiverName'

# The email subject must contain 1 to 100 characters.
INVALIDPARAMETERVALUE_SUBJECTLENGTHERROR = 'InvalidParameterValue.SubjectLengthError'

# The template resource is empty.
INVALIDPARAMETERVALUE_TEMPLATECONTENTISNULL = 'InvalidParameterValue.TemplateContentIsNULL'

# Incorrect template content. Make sure the Base64 content is correct.
INVALIDPARAMETERVALUE_TEMPLATECONTENTISWRONG = 'InvalidParameterValue.TemplateContentIsWrong'

# Template parameters must be in JSON format.
INVALIDPARAMETERVALUE_TEMPLATEDATAERROR = 'InvalidParameterValue.TemplateDataError'

# The name of a template parameter variable is not the same as the original name.
INVALIDPARAMETERVALUE_TEMPLATEDATAINCONSISTENT = 'InvalidParameterValue.TemplateDataInconsistent'

# The template parameter (entire JSON structure) attached to a single recipient address exceeds the length limit of 800 bytes.
INVALIDPARAMETERVALUE_TEMPLATEDATALENLIMIT = 'InvalidParameterValue.TemplateDataLenLimit'

# Invalid template name. Make sure the characters and length of the template name are valid.
INVALIDPARAMETERVALUE_TEMPLATENAMEILLEGAL = 'InvalidParameterValue.TemplateNameIllegal'

# The template name cannot be empty.
INVALIDPARAMETERVALUE_TEMPLATENAMEISNULL = 'InvalidParameterValue.TemplateNameIsNULL'

# The template does not exist. Please create a template.
INVALIDPARAMETERVALUE_TEMPLATENOTEXIST = 'InvalidParameterValue.TemplateNotExist'

# Template variables do not match recipient list parameters.
INVALIDPARAMETERVALUE_TEMPLATENOTMATCHDATA = 'InvalidParameterValue.TemplateNotMatchData'

# Incorrect search date. Make sure the date and its format are valid.
INVALIDPARAMETERVALUE_WRONGDATE = 'InvalidParameterValue.WrongDate'

# The quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# The number of recipient groups exceeded the limit.
LIMITEXCEEDED_EXCEEDRECEIVERLIMIT = 'LimitExceeded.ExceedReceiverLimit'

# The number of recipient addresses in the recipient group exceeds the limit.
LIMITEXCEEDED_RECEIVERDETAILCOUNTLIMIT = 'LimitExceeded.ReceiverDetailCountLimit'

# The number of recipient addresses requested exceeds the limit.
LIMITEXCEEDED_RECEIVERDETAILREQUESTLIMIT = 'LimitExceeded.ReceiverDetailRequestLimit'

# Missing parameter.
MISSINGPARAMETER = 'MissingParameter'

# For a recurring sending task, you must select the start time and recurrence.
MISSINGPARAMETER_CYCLEPARAMNECESSARY = 'MissingParameter.CycleParamNecessary'

# The recipient email address is required.
MISSINGPARAMETER_EMAILSNECESSARY = 'MissingParameter.EmailsNecessary'

# The recipient group ID is required.
MISSINGPARAMETER_RECEIVERIDNECESSARY = 'MissingParameter.ReceiverIdNecessary'

# Sender address, recipient group, and email template are required.
MISSINGPARAMETER_SENDPARAMNECESSARY = 'MissingParameter.SendParamNecessary'

# For a scheduled sending task, you must select the start time.
MISSINGPARAMETER_TIMEDPARAMNECESSARY = 'MissingParameter.TimedParamNecessary'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# Domain verification failed. Check whether the domain has passed verification.
OPERATIONDENIED_DOMAINNOTVERIFIED = 'OperationDenied.DomainNotVerified'

# The number of sender domains exceeds the upper limit.
OPERATIONDENIED_EXCEEDDOMAINLIMIT = 'OperationDenied.ExceedDomainLimit'

# The number of sender addresses exceeds the upper limit.
OPERATIONDENIED_EXCEEDSENDERLIMIT = 'OperationDenied.ExceedSenderLimit'

# Domain name cannot be deleted.
OPERATIONDENIED_NOTALLOWDELETE = 'OperationDenied.NotAllowDelete'

# The recipient group is being uploaded. Try again later.
OPERATIONDENIED_RECEIVERISOPERATING = 'OperationDenied.ReceiverIsOperating'

# The recipient group does not exist.
OPERATIONDENIED_RECEIVERNOTEXIST = 'OperationDenied.ReceiverNotExist'

# The recipient group is empty or hasn’t been completely uploaded.
OPERATIONDENIED_RECEIVERSTATUSERROR = 'OperationDenied.ReceiverStatusError'

# The password cannot be the same as the last set password.
OPERATIONDENIED_REPEATPASSWORD = 'OperationDenied.RepeatPassWord'

# The sender address does not exist or hasn’t been approved.
OPERATIONDENIED_SENDADDRESSSTATUSERROR = 'OperationDenied.SendAddressStatusError'

# The email template does not exist or hasn’t been approved.
OPERATIONDENIED_TEMPLATESTATUSERROR = 'OperationDenied.TemplateStatusError'

# The number of requests exceeds the frequency limit.
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# Insufficient resources.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# Unknown parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
