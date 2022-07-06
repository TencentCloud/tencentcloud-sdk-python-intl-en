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


# DryRun operation. A request will not be successful if the `DryRun` parameter is passed in.
DRYRUNOPERATION = 'DryRunOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Failed to manipulate the AI API.
FAILEDOPERATION_AITRANSCODEOPTIONFAIL = 'FailedOperation.AiTranscodeOptionFail'

# Failed to change the task status.
FAILEDOPERATION_ALTERTASKSTATE = 'FailedOperation.AlterTaskState'

# Failed to call the third-party service.
FAILEDOPERATION_CALLOTHERSVRERROR = 'FailedOperation.CallOtherSvrError'

# Failed to call the internal service.
FAILEDOPERATION_CALLOTHERSVRFAILED = 'FailedOperation.CallOtherSvrFailed'

# The canceled stream mix session does not exist.
FAILEDOPERATION_CANCELSESSIONNOTEXIST = 'FailedOperation.CancelSessionNotExist'

# The template is in use.
FAILEDOPERATION_CONFINUSED = 'FailedOperation.ConfInUsed'

# The domain name cannot be deleted because it incurred traffic in the last 2 days and is in locked state.
FAILEDOPERATION_DELETEDOMAININLOCKEDTIME = 'FailedOperation.DeleteDomainInLockedTime'

# Failed to configure the domain rule.
FAILEDOPERATION_DOMAINGSLBFAIL = 'FailedOperation.DomainGslbFail'

# Unable to get the watermark URL.
FAILEDOPERATION_GETPICTUREURLERROR = 'FailedOperation.GetPictureUrlError'

# Failed to get the input stream length and width.
FAILEDOPERATION_GETSTREAMRESOLUTIONERROR = 'FailedOperation.GetStreamResolutionError'

# No live stream.
FAILEDOPERATION_HASNOTLIVINGSTREAM = 'FailedOperation.HasNotLivingStream'

# The number of domain names exceeded the upper limit (100).
FAILEDOPERATION_HOSTOUTLIMIT = 'FailedOperation.HostOutLimit'

# An exception occurred while manipulating the VOD API.
FAILEDOPERATION_INVOKEVIDEOAPIFAIL = 'FailedOperation.InvokeVideoApiFail'

# The billing platform returned an error of insufficient balance.
FAILEDOPERATION_JIFEINOENOUGHFUND = 'FailedOperation.JiFeiNoEnoughFund'

# No records found.
FAILEDOPERATION_NOTFOUND = 'FailedOperation.NotFound'

# Failed to start stream mix.
FAILEDOPERATION_PROCESSMIXERROR = 'FailedOperation.ProcessMixError'

# Failed to query the upload information.
FAILEDOPERATION_QUERYUPLOADINFOFAILED = 'FailedOperation.QueryUploadInfoFailed'

# The rule already exists.
FAILEDOPERATION_RULEALREADYEXIST = 'FailedOperation.RuleAlreadyExist'

# The user has no valid traffic package.
FAILEDOPERATION_SDKNOPACKAGE = 'FailedOperation.SdkNoPackage'

# The stream does not exist.
FAILEDOPERATION_STREAMNOTEXIST = 'FailedOperation.StreamNotExist'

# Failed to unbind the tag. Try unbinding it manually.
FAILEDOPERATION_TAGUNBINDERROR = 'FailedOperation.TagUnbindError'

# Internal error.
INTERNALERROR = 'InternalError'

# For the transcoding template adding API.
INTERNALERROR_ARGSNOTMATCH = 'InternalError.ArgsNotMatch'

# Error calling internal service.
INTERNALERROR_CALLOTHERSVRERROR = 'InternalError.CallOtherSvrError'

# Chinese domain names are not supported currently. Please check the domain name format.
INTERNALERROR_CHINESECHARACTERDETECTED = 'InternalError.ChineseCharacterDetected'

# The template is in use.
INTERNALERROR_CONFINUSED = 'InternalError.ConfInUsed'

# The template does not exist.
INTERNALERROR_CONFNOTFOUND = 'InternalError.ConfNotFound'

# The number of templates exceeded the limit.
INTERNALERROR_CONFOUTLIMIT = 'InternalError.ConfOutLimit'

# The configuration does not exist.
INTERNALERROR_CONFIGNOTEXIST = 'InternalError.ConfigNotExist'

# Database connection error.
INTERNALERROR_CONNECTDBERROR = 'InternalError.ConnectDbError'

# The certificate is in use.
INTERNALERROR_CRTDATEINUSING = 'InternalError.CrtDateInUsing'

# The certificate does not exist.
INTERNALERROR_CRTDATENOTFOUND = 'InternalError.CrtDateNotFound'

# The certificate is invalid.
INTERNALERROR_CRTDATENOTLEGAL = 'InternalError.CrtDateNotLegal'

# The certificate has expired.
INTERNALERROR_CRTDATEOVERDUE = 'InternalError.CrtDateOverdue'

# There is no related domain name.
INTERNALERROR_CRTDOMAINNOTFOUND = 'InternalError.CrtDomainNotFound'

# The certificate key does not match.
INTERNALERROR_CRTKEYNOTMATCH = 'InternalError.CrtKeyNotMatch'

# DB execution error.
INTERNALERROR_DBERROR = 'InternalError.DBError'

# The domain name is already connected elsewhere. Please check whether the entered domain name is correct, and if yes, you can add it again after successful ownership verification.
INTERNALERROR_DOMAINALREADYEXIST = 'InternalError.DomainAlreadyExist'

# The domain name format is incorrect. Please enter a valid one.
INTERNALERROR_DOMAINFORMATERROR = 'InternalError.DomainFormatError'

# Failed to add the GSLB rule.
INTERNALERROR_DOMAINGSLBFAIL = 'InternalError.DomainGslbFail'

# The domain name is already connected elsewhere. Please check whether the entered domain name is correct, and if yes, you can add it again after successful ownership verification.
INTERNALERROR_DOMAINISFAMOUS = 'InternalError.DomainIsFamous'

# Your domain name is unavailable. Please enter a correct domain name.
INTERNALERROR_DOMAINISLIMITED = 'InternalError.DomainIsLimited'

# The domain name has no ICP filing.
INTERNALERROR_DOMAINNORECORD = 'InternalError.DomainNoRecord'

# The domain name does not exist.
INTERNALERROR_DOMAINNOTEXIST = 'InternalError.DomainNotExist'

# The domain name length exceeds the limit.
INTERNALERROR_DOMAINTOOLONG = 'InternalError.DomainTooLong'

# Error getting user account.
INTERNALERROR_GETBIZIDERROR = 'InternalError.GetBizidError'

# Error getting the configuration.
INTERNALERROR_GETCONFIGERROR = 'InternalError.GetConfigError'

# Failed to get the stream information.
INTERNALERROR_GETSTREAMINFOERROR = 'InternalError.GetStreamInfoError'

# Error getting the live stream source information.
INTERNALERROR_GETUPSTREAMINFOERROR = 'InternalError.GetUpstreamInfoError'

# An error occurred while getting the watermark.
INTERNALERROR_GETWATERMARKERROR = 'InternalError.GetWatermarkError'

# No live stream.
INTERNALERROR_HASNOTLIVINGSTREAM = 'InternalError.HasNotLivingStream'

# Parameter check failed.
INTERNALERROR_INVALIDINPUT = 'InternalError.InvalidInput'

# Invalid request.
INTERNALERROR_INVALIDREQUEST = 'InternalError.InvalidRequest'

# Account information error.
INTERNALERROR_INVALIDUSER = 'InternalError.InvalidUser'

# The billing platform returned other errors.
INTERNALERROR_JIFEIOTHERERROR = 'InternalError.JiFeiOtherError'

# Internal network error.
INTERNALERROR_NETWORKERROR = 'InternalError.NetworkError'

# The record does not exist.
INTERNALERROR_NOTFOUND = 'InternalError.NotFound'

# No permission to operate.
INTERNALERROR_NOTPERMMITOPERAT = 'InternalError.NotPermmitOperat'

# The playback domain name does not exist.
INTERNALERROR_PLAYDOMAINNORECORD = 'InternalError.PlayDomainNoRecord'

# The transcoding template name already exists.
INTERNALERROR_PROCESSORALREADYEXIST = 'InternalError.ProcessorAlreadyExist'

# The push domain name does not exist.
INTERNALERROR_PUSHDOMAINNORECORD = 'InternalError.PushDomainNoRecord'

# Failed to query the playback information by ISP and district.
INTERNALERROR_QUERYPROISPPLAYINFOERROR = 'InternalError.QueryProIspPlayInfoError'

# Failed to query the upload information.
INTERNALERROR_QUERYUPLOADINFOFAILED = 'InternalError.QueryUploadInfoFailed'

# The rule has already been configured.
INTERNALERROR_RULEALREADYEXIST = 'InternalError.RuleAlreadyExist'

# The rule is in use.
INTERNALERROR_RULEINUSING = 'InternalError.RuleInUsing'

# The rule does not exist.
INTERNALERROR_RULENOTFOUND = 'InternalError.RuleNotFound'

# The rule exceeds the limit.
INTERNALERROR_RULEOUTLIMIT = 'InternalError.RuleOutLimit'

# Exceptional stream status.
INTERNALERROR_STREAMSTATUSERROR = 'InternalError.StreamStatusError'

# Internal system error.
INTERNALERROR_SYSTEMERROR = 'InternalError.SystemError'

# Failed to update data.
INTERNALERROR_UPDATEDATAERROR = 'InternalError.UpdateDataError'

# Failed to add the watermark.
INTERNALERROR_WATERMARKADDERROR = 'InternalError.WatermarkAddError'

# An internal error occurred while modifying the watermark.
INTERNALERROR_WATERMARKEDITERROR = 'InternalError.WatermarkEditError'

# The watermark does not exist.
INTERNALERROR_WATERMARKNOTEXIST = 'InternalError.WatermarkNotExist'

# Invalid parameter.
INVALIDPARAMETER = 'InvalidParameter'

# Incorrect template name.
INVALIDPARAMETER_ARGSNOTMATCH = 'InvalidParameter.ArgsNotMatch'

# Incorrect custom COS filename.
INVALIDPARAMETER_COSCUSTOMFILENAMEERROR = 'InvalidParameter.COSCustomFileNameError'

# The canceled session does not exist.
INVALIDPARAMETER_CANCELSESSIONNOTEXIST = 'InvalidParameter.CancelSessionNotExist'

# Incorrect Tencent Cloud-hosted certificate ID.
INVALIDPARAMETER_CLOUDCRTIDERROR = 'InvalidParameter.CloudCrtIdError'

# The gifted Tencent Cloud domain name has expired.
INVALIDPARAMETER_CLOUDDOMAINISSTOP = 'InvalidParameter.CloudDomainIsStop'

# The certificate is in use.
INVALIDPARAMETER_CRTDATEINUSING = 'InvalidParameter.CrtDateInUsing'

# The certificate is invalid.
INVALIDPARAMETER_CRTDATENOTLEGAL = 'InvalidParameter.CrtDateNotLegal'

# The certificate has expired.
INVALIDPARAMETER_CRTDATEOVERDUE = 'InvalidParameter.CrtDateOverdue'

# The certificate key does not match.
INVALIDPARAMETER_CRTKEYNOTMATCH = 'InvalidParameter.CrtKeyNotMatch'

# The certificate content or private key was not provided.
INVALIDPARAMETER_CRTORKEYNOTEXIST = 'InvalidParameter.CrtOrKeyNotExist'

# The domain name already exists.
INVALIDPARAMETER_DOMAINALREADYEXIST = 'InvalidParameter.DomainAlreadyExist'

# The domain name format is incorrect. Please enter a valid one.
INVALIDPARAMETER_DOMAINFORMATERROR = 'InvalidParameter.DomainFormatError'

# This domain name is on the blocklist.
INVALIDPARAMETER_DOMAINHITBLACKLIST = 'InvalidParameter.DomainHitBlackList'

# A blocklisted domain name is used.
INVALIDPARAMETER_DOMAINISFAMOUS = 'InvalidParameter.DomainIsFamous'

# The domain name is restricted. Please submit a ticket for application to remove the restrictions.
INVALIDPARAMETER_DOMAINISLIMITED = 'InvalidParameter.DomainIsLimited'

# The domain name exceeds the length limit.
INVALIDPARAMETER_DOMAINTOOLONG = 'InvalidParameter.DomainTooLong'

# The number of inputs exceeds the limit.
INVALIDPARAMETER_INPUTNUMLIMITEXCEEDED = 'InvalidParameter.InputNumLimitExceeded'

# Invalid background length and width.
INVALIDPARAMETER_INVALIDBACKGROUDRESOLUTION = 'InvalidParameter.InvalidBackgroudResolution'

# Invalid output bitrate.
INVALIDPARAMETER_INVALIDBITRATE = 'InvalidParameter.InvalidBitrate'

# Invalid callback URL.
INVALIDPARAMETER_INVALIDCALLBACKURL = 'InvalidParameter.InvalidCallbackUrl'

# The cropped area overflows the original image.
INVALIDPARAMETER_INVALIDCROPPARAM = 'InvalidParameter.InvalidCropParam'

# Invalid layer parameter.
INVALIDPARAMETER_INVALIDLAYERPARAM = 'InvalidParameter.InvalidLayerParam'

# The output stream ID is already used.
INVALIDPARAMETER_INVALIDOUTPUTSTREAMID = 'InvalidParameter.InvalidOutputStreamID'

# Invalid output type. Please check whether `OutputPram-StreamId` and `OutputType` match.
INVALIDPARAMETER_INVALIDOUTPUTTYPE = 'InvalidParameter.InvalidOutputType'

# The watermark ID was not set.
INVALIDPARAMETER_INVALIDPICTUREID = 'InvalidParameter.InvalidPictureID'

# Invalid corner radius of the rounded rectangle.
INVALIDPARAMETER_INVALIDROUNDRECTRADIUS = 'InvalidParameter.InvalidRoundRectRadius'

# Invalid source URL.
INVALIDPARAMETER_INVALIDSOURCEURL = 'InvalidParameter.InvalidSourceUrl'

# The time period of the task exceeded the limit.
INVALIDPARAMETER_INVALIDTASKTIME = 'InvalidParameter.InvalidTaskTime'

# Invalid destination URL.
INVALIDPARAMETER_INVALIDTOURL = 'InvalidParameter.InvalidToUrl'

# Incorrect `VodFileName`.
INVALIDPARAMETER_INVALIDVODFILENAME = 'InvalidParameter.InvalidVodFileName'

# 
INVALIDPARAMETER_INVALIDWATERMARK = 'InvalidParameter.InvalidWatermark'

# It is not allowed to add a Mini Program domain name deleted in the same month.
INVALIDPARAMETER_MPHOSTDELETE = 'InvalidParameter.MpHostDelete'

# The WeChat Mini Program plug-in is unauthorized.
INVALIDPARAMETER_MPPLUGINNOUSE = 'InvalidParameter.MpPluginNoUse'

# Other errors.
INVALIDPARAMETER_OTHERERROR = 'InvalidParameter.OtherError'

# The output stream of the same session has changed.
INVALIDPARAMETER_SESSIONOUTPUTSTREAMCHANGED = 'InvalidParameter.SessionOutputStreamChanged'

# The task does not exist.
INVALIDPARAMETER_TASKNOTEXIST = 'InvalidParameter.TaskNotExist'

# The number of tasks reached the limit.
INVALIDPARAMETER_TASKNUMMORETHANLIMIT = 'InvalidParameter.TaskNumMoreThanLimit'

# The template does not match the number of input streams.
INVALIDPARAMETER_TEMPLATENOTMATCHINPUTNUM = 'InvalidParameter.TemplateNotMatchInputNum'

# No permission to access the external URL.
INVALIDPARAMETER_TOURLNOPERMISSION = 'InvalidParameter.ToUrlNoPermission'

# Failed to resolve the domain name.
INVALIDPARAMETER_URLNOTSAFE = 'InvalidParameter.UrlNotSafe'

# Invalid parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Quota exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# The current number of concurrent tasks exceeds the limit.
LIMITEXCEEDED_MAXIMUMRUNNINGTASK = 'LimitExceeded.MaximumRunningTask'

# The number of tasks created on the day exceeds the limit.
LIMITEXCEEDED_MAXIMUMTASK = 'LimitExceeded.MaximumTask'

# Parameter missing.
MISSINGPARAMETER = 'MissingParameter'

# The resource is occupied.
RESOURCEINUSE = 'ResourceInUse'

# Insufficient resources.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The resource is not found.
RESOURCENOTFOUND = 'ResourceNotFound'

# The channel does not exist.
RESOURCENOTFOUND_CHANNELNOTEXIST = 'ResourceNotFound.ChannelNotExist'

# The certificate does not exist.
RESOURCENOTFOUND_CRTDATENOTFOUND = 'ResourceNotFound.CrtDateNotFound'

# No certificate was found.
RESOURCENOTFOUND_CRTDOMAINNOTFOUND = 'ResourceNotFound.CrtDomainNotFound'

# The domain name has no ICP filing.
RESOURCENOTFOUND_DOMAINNORECORD = 'ResourceNotFound.DomainNoRecord'

# The domain name does not exist or is not matched.
RESOURCENOTFOUND_DOMAINNOTEXIST = 'ResourceNotFound.DomainNotExist'

# 
RESOURCENOTFOUND_FORBIDSERVICE = 'ResourceNotFound.ForbidService'

# 
RESOURCENOTFOUND_FREEZESERVICE = 'ResourceNotFound.FreezeService'

# This API is not supported for the user.
RESOURCENOTFOUND_INVALIDUSER = 'ResourceNotFound.InvalidUser'

# The playback domain name does not exist.
RESOURCENOTFOUND_PLAYDOMAINNORECORD = 'ResourceNotFound.PlayDomainNoRecord'

# The push domain name does not exist.
RESOURCENOTFOUND_PUSHDOMAINNORECORD = 'ResourceNotFound.PushDomainNoRecord'

# The service has been suspended due to account arrears. Please top up it to a positive balance to activate the service first.
RESOURCENOTFOUND_STOPSERVICE = 'ResourceNotFound.StopService'

# The `TaskId` does not exist.
RESOURCENOTFOUND_TASKID = 'ResourceNotFound.TaskId'

# 
RESOURCENOTFOUND_USERDISABLESERVICE = 'ResourceNotFound.UserDisableService'

# The LVB service has not been activated.
RESOURCENOTFOUND_USERNOTEXIST = 'ResourceNotFound.UserNotExist'

# The user does not exist.
RESOURCENOTFOUND_USERNOTFOUNT = 'ResourceNotFound.UserNotFount'

# The watermark does not exist.
RESOURCENOTFOUND_WATERMARKNOTEXIST = 'ResourceNotFound.WatermarkNotExist'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# The VOD service has not been activated.
RESOURCEUNAVAILABLE_INVALIDVODSTATUS = 'ResourceUnavailable.InvalidVodStatus'

# The stream does not exist.
RESOURCEUNAVAILABLE_STREAMNOTEXIST = 'ResourceUnavailable.StreamNotExist'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Unknown parameter.
UNKNOWNPARAMETER = 'UnknownParameter'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# Not a LVB code/new console mode
UNSUPPORTEDOPERATION_NOTLVBCODEMODE = 'UnsupportedOperation.NotLVBCodeMode'
