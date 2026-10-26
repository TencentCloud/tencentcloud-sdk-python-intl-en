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


# Contains a channel ID that you do not have permission to operate.
AUTHFAILURE_CONTAINUNAUTHORIZEDCHANNELID = 'AuthFailure.ContainUnauthorizedChannelId'

# No access permission for the organization
AUTHFAILURE_ORGANIZATIONUNAUTHORIZED = 'AuthFailure.OrganizationUnauthorized'

# Operation failed
FAILEDOPERATION = 'FailedOperation'

# Contains an associated channel ID. Do not associate it again.
FAILEDOPERATION_CHANNELALREADYASSIGNED = 'FailedOperation.ChannelAlreadyAssigned'

# Contains unassociated channel IDs. Unable to disassociate.
FAILEDOPERATION_CHANNELNOTASSIGNED = 'FailedOperation.ChannelNotAssigned'

# Database error.
FAILEDOPERATION_DATABASEERROR = 'FailedOperation.DatabaseError'

# timeout for the device
FAILEDOPERATION_DEVICERESPONSETIMEOUT = 'FailedOperation.DeviceResponseTimeOut'

# timeout for the device response
FAILEDOPERATION_DEVICERESULTTIMEOUT = 'FailedOperation.DeviceResultTimeOut'

# No such sub-user
FAILEDOPERATION_NOTHAVESUBUSER = 'FailedOperation.NotHaveSubUser'

# Request timeout.
FAILEDOPERATION_REQUESTTIMEOUT = 'FailedOperation.RequestTimeout'

# AI scenario template is associated with a plan and cannot be deleted.
FAILEDOPERATION_TEMPLATEINUSE = 'FailedOperation.TemplateInUse'

# Internal server error.
INTERNALERROR_SERVERINTERNALERROR = 'InternalError.ServerInternalError'

# Invalid input parameter
INVALIDPARAMETER = 'InvalidParameter'

# Illegal download URL
INVALIDPARAMETER_DOWNLOADURLERROR = 'InvalidParameter.DownloadUrlError'

# Download URL expired
INVALIDPARAMETER_DOWNLOADURLHASEXPIRED = 'InvalidParameter.DownloadUrlHasExpired'

# Invalid operation type.
INVALIDPARAMETER_INVALIDACTION = 'InvalidParameter.InvalidAction'

# Invalid message body format
INVALIDPARAMETER_INVALIDBODYFORMAT = 'InvalidParameter.InvalidBodyFormat'

# Invalid channel parameters
INVALIDPARAMETER_INVALIDCHANNELS = 'InvalidParameter.InvalidChannels'

# Invalid lifecycle parameter
INVALIDPARAMETER_INVALIDLIFERULEPARAM = 'InvalidParameter.InvalidLifeRuleParam'

# Invalid organization parameter
INVALIDPARAMETER_INVALIDORGANIZATIONPARAM = 'InvalidParameter.InvalidOrganizationParam'

# Invalid input parameter
INVALIDPARAMETER_INVALIDPARAMETER = 'InvalidParameter.InvalidParameter'

# Incorrect parameter format or missing required parameters
INVALIDPARAMETER_INVALIDPARAMETERFORMAT = 'InvalidParameter.InvalidParameterFormat'

# Invalid time segment
INVALIDPARAMETER_INVALIDTIMESECTION = 'InvalidParameter.InvalidTimeSection'

# Required request header parameter cannot be empty
INVALIDPARAMETER_REQUIREDHEADERPARAMETEREMPTY = 'InvalidParameter.RequiredHeaderParameterEmpty'

# TaskId not found
INVALIDPARAMETER_TASKIDNOTEXIST = 'InvalidParameter.TaskIdNotExist'

# Invalid parameter value
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Existence of a setting failing to satisfy (Cloud Upload Time Period = previous day's recording time period/cloud upload playback speed). Please check and confirm.
INVALIDPARAMETERVALUE_BAKTIMENOTENOUGH = 'InvalidParameterValue.BakTimeNotEnough'

# Number of channels exceeds the limit range.
INVALIDPARAMETERVALUE_CHANNELSEXCEEDSRANGE = 'InvalidParameterValue.ChannelsExceedsRange'

# Contains an invalid ChannelId.
INVALIDPARAMETERVALUE_CONTAININVALIDCHANNELID = 'InvalidParameterValue.ContainInvalidChannelId'

# Contains an invalid device ID
INVALIDPARAMETERVALUE_CONTAININVALIDDEVICEID = 'InvalidParameterValue.ContainInvalidDeviceId'

# Contains an invalid image ID
INVALIDPARAMETERVALUE_CONTAININVALIDIMAGEID = 'InvalidParameterValue.ContainInvalidImageId'

# Contains an invalid screenshot time range
INVALIDPARAMETERVALUE_CONTAININVALIDSNAPSHOTTIME = 'InvalidParameterValue.ContainInvalidSnapshotTime'

# Contains an invalid Token.
INVALIDPARAMETERVALUE_CONTAININVALIDTOKEN = 'InvalidParameterValue.ContainInvalidToken'

# Contains a non-existing channel ID
INVALIDPARAMETERVALUE_CONTAINNONEXISTENTCHANNELID = 'InvalidParameterValue.ContainNonexistentChannelId'

# Period exceeds the limit (1-7)
INVALIDPARAMETERVALUE_DATAOUTOFRANGE = 'InvalidParameterValue.DataOutOfRange'

# Device ID and channel ID do not match
INVALIDPARAMETERVALUE_DEVICEMISMATCHCHANNEL = 'InvalidParameterValue.DeviceMismatchChannel'

# Channel ID cannot be empty.
INVALIDPARAMETERVALUE_EMPTYCHANNELID = 'InvalidParameterValue.EmptyChannelId'

# ChannelIds cannot be empty. At least 1 channel ID is required.
INVALIDPARAMETERVALUE_EMPTYCHANNELIDS = 'InvalidParameterValue.EmptyChannelIds'

# Device ID cannot be empty.
INVALIDPARAMETERVALUE_EMPTYDEVICEID = 'InvalidParameterValue.EmptyDeviceId'

# Name cannot be empty
INVALIDPARAMETERVALUE_EMPTYNAME = 'InvalidParameterValue.EmptyName'

# Organization ID cannot be empty.
INVALIDPARAMETERVALUE_EMPTYORGANIZATIONID = 'InvalidParameterValue.EmptyOrganizationId'

# Associated template cannot be empty.
INVALIDPARAMETERVALUE_EMPTYTEMPLATEID = 'InvalidParameterValue.EmptyTemplateId'

# End time cannot be empty.
INVALIDPARAMETERVALUE_ENDTIMEZERO = 'InvalidParameterValue.EndTimeZero'

# Channel ID contains illegal characters
INVALIDPARAMETERVALUE_ILLEGALCHANNELID = 'InvalidParameterValue.IllegalChannelId'

# Description contains non-compliant characters (only Chinese, English, digits, _, and - are supported)
INVALIDPARAMETERVALUE_ILLEGALDESCRIBE = 'InvalidParameterValue.IllegalDescribe'

# Device ID contains illegal characters
INVALIDPARAMETERVALUE_ILLEGALDEVICEID = 'InvalidParameterValue.IllegalDeviceId'

# Name contains non-compliant characters (only Chinese, English, digits, _, and - are supported)
INVALIDPARAMETERVALUE_ILLEGALNAME = 'InvalidParameterValue.IllegalName'

# Organization ID contains illegal characters
INVALIDPARAMETERVALUE_ILLEGALORGANIZATIONID = 'InvalidParameterValue.IllegalOrganizationId'

# Stream type contains invalid characters (only English, digits, _, and - are supported)
INVALIDPARAMETERVALUE_ILLEGALSTREAMTYPE = 'InvalidParameterValue.IllegalStreamType'

# InvalidParameterValue.ImageVLPlanIDNotExisted
INVALIDPARAMETERVALUE_IMAGEVLPLANIDNOTEXISTED = 'InvalidParameterValue.ImageVLPlanIDNotExisted'

# InvalidParameterValue.ImageVLPlanNameContainIllegalCharacter
INVALIDPARAMETERVALUE_IMAGEVLPLANNAMECONTAINILLEGALCHARACTER = 'InvalidParameterValue.ImageVLPlanNameContainIllegalCharacter'

# InvalidParameterValue.InvalidAIModel
INVALIDPARAMETERVALUE_INVALIDAIMODEL = 'InvalidParameterValue.InvalidAIModel'

# Invalid device access protocol.
INVALIDPARAMETERVALUE_INVALIDACCESSPROTOCOL = 'InvalidParameterValue.InvalidAccessProtocol'

# Invalid start time
INVALIDPARAMETERVALUE_INVALIDBEGINTIME = 'InvalidParameterValue.InvalidBeginTime'

# Invalid callback Token.
INVALIDPARAMETERVALUE_INVALIDCALLBACKTOKEN = 'InvalidParameterValue.InvalidCallbackToken'

# Invalid callback URL
INVALIDPARAMETERVALUE_INVALIDCALLBACKURL = 'InvalidParameterValue.InvalidCallbackUrl'

# Invalid screenshot type filter value. Only realtime/low is supported.
INVALIDPARAMETERVALUE_INVALIDCAPTURETYPE = 'InvalidParameterValue.InvalidCaptureType'

# Invalid channel ID
INVALIDPARAMETERVALUE_INVALIDCHANNELID = 'InvalidParameterValue.InvalidChannelId'

# Contains an invalid channel ID or device ID
INVALIDPARAMETERVALUE_INVALIDCHANNELIDORDEVICEID = 'InvalidParameterValue.InvalidChannelIdOrDeviceId'

# Channel name is empty or incorrect.
INVALIDPARAMETERVALUE_INVALIDCHANNELNAME = 'InvalidParameterValue.InvalidChannelName'

# Invalid cluster ID. The length or content does not conform to rules.
INVALIDPARAMETERVALUE_INVALIDCLUSTERID = 'InvalidParameterValue.InvalidClusterId'

# Invalid command
INVALIDPARAMETERVALUE_INVALIDCMD = 'InvalidParameterValue.InvalidCmd'

# Invalid configuration ID
INVALIDPARAMETERVALUE_INVALIDCONFIGID = 'InvalidParameterValue.InvalidConfigId'

# Invalid description.
INVALIDPARAMETERVALUE_INVALIDDESCRIBE = 'InvalidParameterValue.InvalidDescribe'

# Incorrect description.
INVALIDPARAMETERVALUE_INVALIDDESCRIPTION = 'InvalidParameterValue.InvalidDescription'

# Invalid device ID
INVALIDPARAMETERVALUE_INVALIDDEVICEID = 'InvalidParameterValue.InvalidDeviceId'

# Device name is empty or incorrect.
INVALIDPARAMETERVALUE_INVALIDDEVICENAME = 'InvalidParameterValue.InvalidDeviceName'

# The device password must be greater than 1 character and less than 64 characters in length.
INVALIDPARAMETERVALUE_INVALIDDEVICEPASSWORDLENGTH = 'InvalidParameterValue.InvalidDevicePasswordLength'

# Invalid device status
INVALIDPARAMETERVALUE_INVALIDDEVICESTATUS = 'InvalidParameterValue.InvalidDeviceStatus'

# Invalid device type
INVALIDPARAMETERVALUE_INVALIDDEVICETYPE = 'InvalidParameterValue.InvalidDeviceType'

# Invalid domain type parameter
INVALIDPARAMETERVALUE_INVALIDDOMAINTYPE = 'InvalidParameterValue.InvalidDomainType'

# Invalid enable parameter
INVALIDPARAMETERVALUE_INVALIDENALBEVALUE = 'InvalidParameterValue.InvalidEnalbeValue'

# Invalid end time
INVALIDPARAMETERVALUE_INVALIDENDTIME = 'InvalidParameterValue.InvalidEndTime'

# Invalid replica validity period. Valid values: 1-365 days
INVALIDPARAMETERVALUE_INVALIDEXPIRATION = 'InvalidParameterValue.InvalidExpiration'

# Cold storage must be at least 60 days, and the total days of hot and cold storage cannot exceed 3650 days.
INVALIDPARAMETERVALUE_INVALIDEXPIRATIONRANGE = 'InvalidParameterValue.InvalidExpirationRange'

# Invalid expiration time. It must be more than 0 and less than 60.
INVALIDPARAMETERVALUE_INVALIDEXPIRE = 'InvalidParameterValue.InvalidExpire'

# Invalid file storage days
INVALIDPARAMETERVALUE_INVALIDFILEEXPIRES = 'InvalidParameterValue.InvalidFileExpires'

# Invalid file format
INVALIDPARAMETERVALUE_INVALIDFILETYPE = 'InvalidParameterValue.InvalidFileType'

# Invalid gateway access protocol.
INVALIDPARAMETERVALUE_INVALIDGATEWAYPROTOCOLTYPE = 'InvalidParameterValue.InvalidGatewayProtocolType'

# The value range of the infrequent frame capturing frequency is [30, 36000] seconds.
INVALIDPARAMETERVALUE_INVALIDIMAGECONFIGINTERVALFORLOWFREQ = 'InvalidParameterValue.InvalidImageConfigIntervalForLowFreq'

# The value range of the real-time frame capturing frequency is [5, 180] seconds.
INVALIDPARAMETERVALUE_INVALIDIMAGECONFIGINTERVALFORREALTIME = 'InvalidParameterValue.InvalidImageConfigIntervalForRealtime'

# Invalid screenshot type
INVALIDPARAMETERVALUE_INVALIDIMAGECONFIGTYPE = 'InvalidParameterValue.InvalidImageConfigType'

# InvalidParameterValue.InvalidImageVLPlanDescribe
INVALIDPARAMETERVALUE_INVALIDIMAGEVLPLANDESCRIBE = 'InvalidParameterValue.InvalidImageVLPlanDescribe'

# InvalidParameterValue.InvalidImageVLPlanID
INVALIDPARAMETERVALUE_INVALIDIMAGEVLPLANID = 'InvalidParameterValue.InvalidImageVLPlanID'

# InvalidParameterValue.InvalidImageVLPlanName
INVALIDPARAMETERVALUE_INVALIDIMAGEVLPLANNAME = 'InvalidParameterValue.InvalidImageVLPlanName'

# Invalid Ipv4 addresses.
INVALIDPARAMETERVALUE_INVALIDIPV4 = 'InvalidParameterValue.InvalidIpv4'

# Invalid keyword
INVALIDPARAMETERVALUE_INVALIDKEYWORD = 'InvalidParameterValue.InvalidKeyword'

# Invalid media type
INVALIDPARAMETERVALUE_INVALIDMEDIATYPE = 'InvalidParameterValue.InvalidMediaType'

# Name is empty or incorrect.
INVALIDPARAMETERVALUE_INVALIDNAME = 'InvalidParameterValue.InvalidName'

# Organization name is empty or incorrect.
INVALIDPARAMETERVALUE_INVALIDORGNAME = 'InvalidParameterValue.InvalidOrgName'

# Invalid organization ID
INVALIDPARAMETERVALUE_INVALIDORGANIZATIONID = 'InvalidParameterValue.InvalidOrganizationId'

# Invalid PageNumber
INVALIDPARAMETERVALUE_INVALIDPAGENUMBER = 'InvalidParameterValue.InvalidPageNumber'

# Invalid page parameter value
INVALIDPARAMETERVALUE_INVALIDPAGEPARAMETER = 'InvalidParameterValue.InvalidPageParameter'

# Invalid PageSize
INVALIDPARAMETERVALUE_INVALIDPAGESIZE = 'InvalidParameterValue.InvalidPageSize'

# Invalid plan ID
INVALIDPARAMETERVALUE_INVALIDPLANID = 'InvalidParameterValue.InvalidPlanId'

# Invalid prompt
INVALIDPARAMETERVALUE_INVALIDPROMPT = 'InvalidParameterValue.InvalidPrompt'

# Invalid pull authentication switch value
INVALIDPARAMETERVALUE_INVALIDPULLSTATE = 'InvalidParameterValue.InvalidPullState'

# Invalid push authentication switch value
INVALIDPARAMETERVALUE_INVALIDPUSHSTATE = 'InvalidParameterValue.InvalidPushState'

# Invalid RTMP push AppName
INVALIDPARAMETERVALUE_INVALIDRTMPAPPNAME = 'InvalidParameterValue.InvalidRTMPAppName'

# Invalid RTMP push StreamName
INVALIDPARAMETERVALUE_INVALIDRTMPSTREAMNAME = 'InvalidParameterValue.InvalidRTMPStreamName'

# Invalid video recording supplement parameter
INVALIDPARAMETERVALUE_INVALIDREPAIRMODE = 'InvalidParameterValue.InvalidRepairMode'

# Invalid retrieval mode
INVALIDPARAMETERVALUE_INVALIDRETRIEVALMODE = 'InvalidParameterValue.InvalidRetrievalMode'

# Invalid retrieval task ID.
INVALIDPARAMETERVALUE_INVALIDRETRIEVETASKID = 'InvalidParameterValue.InvalidRetrieveTaskId'

# Invalid secret key value. The length or content does not conform to rules.
INVALIDPARAMETERVALUE_INVALIDSECRET = 'InvalidParameterValue.InvalidSecret'

# Invalid start or end time
INVALIDPARAMETERVALUE_INVALIDSTARTTIMEORENDTIME = 'InvalidParameterValue.InvalidStartTimeOrEndTime'

# Invalid status
INVALIDPARAMETERVALUE_INVALIDSTATUS = 'InvalidParameterValue.InvalidStatus'

# Invalid stream type
INVALIDPARAMETERVALUE_INVALIDSTREAMTYPE = 'InvalidParameterValue.InvalidStreamType'

# Invalid template ID
INVALIDPARAMETERVALUE_INVALIDTEMPLATEID = 'InvalidParameterValue.InvalidTemplateId'

# Time format error.
INVALIDPARAMETERVALUE_INVALIDTIMEFORMAT = 'InvalidParameterValue.InvalidTimeFormat'

# Invalid time segment value
INVALIDPARAMETERVALUE_INVALIDTIMESECTIONVALUE = 'InvalidParameterValue.InvalidTimeSectionValue'

# InvalidParameterValue.InvalidTimes
INVALIDPARAMETERVALUE_INVALIDTIMES = 'InvalidParameterValue.InvalidTimes'

# Hot storage must be at least 1 day and at most 3650 days.
INVALIDPARAMETERVALUE_INVALIDTRANSITIONRANGE = 'InvalidParameterValue.InvalidTransitionRange'

# Invalid user parameter
INVALIDPARAMETERVALUE_INVALIDUSERPARAM = 'InvalidParameterValue.InvalidUserParam'

# Invalid username. The length or content does not conform to rules.
INVALIDPARAMETERVALUE_INVALIDUSERNAME = 'InvalidParameterValue.InvalidUsername'

# InvalidParameterValue.InvalidVLPlanResultID
INVALIDPARAMETERVALUE_INVALIDVLPLANRESULTID = 'InvalidParameterValue.InvalidVLPlanResultID'

# InvalidParameterValue.InvalidVLPlanResultIds
INVALIDPARAMETERVALUE_INVALIDVLPLANRESULTIDS = 'InvalidParameterValue.InvalidVLPlanResultIds'

# Enable video recording supplementary hot storage for at least 3 days.
INVALIDPARAMETERVALUE_LIMITREPAIRTRANSITION = 'InvalidParameterValue.LimitRepairTransition'

# InvalidParameterValue.MissingImageConfig
INVALIDPARAMETERVALUE_MISSINGIMAGECONFIG = 'InvalidParameterValue.MissingImageConfig'

# InvalidParameterValue.MissingTimes
INVALIDPARAMETERVALUE_MISSINGTIMES = 'InvalidParameterValue.MissingTimes'

# Time cannot span across days.
INVALIDPARAMETERVALUE_NONSAMEDAY = 'InvalidParameterValue.NonSameDay'

# Organization name must be unique
INVALIDPARAMETERVALUE_ORGNAMEREPEAT = 'InvalidParameterValue.OrgNameRepeat'

# The number of organizations cannot be greater than 1,000.
INVALIDPARAMETERVALUE_ORGANIZATIONCOUNTEXCEEDSRANGE = 'InvalidParameterValue.OrganizationCountExceedsRange'

# Organization ID does not exist.
INVALIDPARAMETERVALUE_ORGANIZATIONIDNOTEXISTED = 'InvalidParameterValue.OrganizationIDNotExisted'

# OrganizationIds does not allow input when Cmd=2 (unbind).
INVALIDPARAMETERVALUE_ORGANIZATIONIDSNOTALLOWEDFORUNASSIGN = 'InvalidParameterValue.OrganizationIdsNotAllowedForUnAssign'

# Time range exceeds the limit
INVALIDPARAMETERVALUE_OUTOFTIMERANGE = 'InvalidParameterValue.OutOfTimeRange'

# Page size exceeds the limit
INVALIDPARAMETERVALUE_PAGESIZEEXCEEDLIMIT = 'InvalidParameterValue.PageSizeExceedLimit'

# Add up to 5,000 channels at a time
INVALIDPARAMETERVALUE_PLANCHANNELSEXCEEDSRANGE = 'InvalidParameterValue.PlanChannelsExceedsRange'

# Plan name must be unique
INVALIDPARAMETERVALUE_PLANNAMEREPEAT = 'InvalidParameterValue.PlanNameRepeat'

# Custom RTMP push AppName and StreamName cannot be duplicated
INVALIDPARAMETERVALUE_RTMPPUSHSTREAMPARAMREPEAT = 'InvalidParameterValue.RTMPPushStreamParamRepeat'

# Add up to 32 device channels to a retrieval task.
INVALIDPARAMETERVALUE_RETRIEVETASKCHANNELSEXCEEDSRANGE = 'InvalidParameterValue.RetrieveTaskChannelsExceedsRange'

# Start time cannot be greater than end time.
INVALIDPARAMETERVALUE_STARTOVERENDTIME = 'InvalidParameterValue.StartOverEndTime'

# Start time cannot be greater than the current time.
INVALIDPARAMETERVALUE_STARTOVERNOWTIME = 'InvalidParameterValue.StartOverNowTime'

# Start time cannot be greater than or equal to end time.
INVALIDPARAMETERVALUE_STARTTIMEGREATERTHANOREQUALENDTIME = 'InvalidParameterValue.StartTimeGreaterThanOrEqualEndTime'

# Start time cannot be empty.
INVALIDPARAMETERVALUE_STARTTIMEZERO = 'InvalidParameterValue.StartTimeZero'

# Unsupported task type
INVALIDPARAMETERVALUE_TASKTYPENOTSUPPORTED = 'InvalidParameterValue.TaskTypeNotSupported'

# Visual understanding analysis template ID does not exist
INVALIDPARAMETERVALUE_TEMPLATEIDNOTEXISTED = 'InvalidParameterValue.TemplateIDNotExisted'

# Time interval cannot be less than 10 minutes.
INVALIDPARAMETERVALUE_TIMELESSTHANTENMINUTES = 'InvalidParameterValue.TimeLessThanTenMinutes'

# Description field too long
INVALIDPARAMETERVALUE_TOOLONGDESCRIBE = 'InvalidParameterValue.TooLongDescribe'

# Name is too long
INVALIDPARAMETERVALUE_TOOLONGNAME = 'InvalidParameterValue.TooLongName'

# Stream type too long.
INVALIDPARAMETERVALUE_TOOLONGSTREAMTYPE = 'InvalidParameterValue.TooLongStreamType'

# Number of ChannelIds exceeds the limit.
INVALIDPARAMETERVALUE_TOOMANYCHANNELIDS = 'InvalidParameterValue.TooManyChannelIds'

# Unsupported operation command.
INVALIDPARAMETERVALUE_UNSUPPORTOPERATECMD = 'InvalidParameterValue.UnSupportOperateCMD'

# Playback speed not supported
INVALIDPARAMETERVALUE_UNSUPPORTSCALE = 'InvalidParameterValue.UnSupportScale'

# Unsupported access type
INVALIDPARAMETERVALUE_UNSUPPORTEDACCESSTYPE = 'InvalidParameterValue.UnSupportedAccessType'

# Unsupported gimbal control command.
INVALIDPARAMETERVALUE_UNSUPPORTEDPTZCMD = 'InvalidParameterValue.UnSupportedPTZCMD'

# Unsupported preset position control command.
INVALIDPARAMETERVALUE_UNSUPPORTEDPRESETCMD = 'InvalidParameterValue.UnSupportedPresetCMD'

# Unsupported playback speed parameter
INVALIDPARAMETERVALUE_UNSUPPORTEDSCALEPARAM = 'InvalidParameterValue.UnSupportedScaleParam'

# Unsupported file storage expiry time
INVALIDPARAMETERVALUE_UNSUPPORTEDFILEEXPIRETIME = 'InvalidParameterValue.UnsupportedFileExpireTime'

# Unsupported image download url expiration time
INVALIDPARAMETERVALUE_UNSUPPORTEDIMAGEURLEXPIRETIME = 'InvalidParameterValue.UnsupportedImageUrlExpireTime'

# Unsupported frame capturing frequency configuration
INVALIDPARAMETERVALUE_UNSUPPORTEDINTERVAL = 'InvalidParameterValue.UnsupportedInterval'

# Unsupported frame count configuration
INVALIDPARAMETERVALUE_UNSUPPORTEDSNAPSHOTTOTAL = 'InvalidParameterValue.UnsupportedSnapshotTotal'

# Unsupported screenshot type
INVALIDPARAMETERVALUE_UNSUPPORTEDSNAPSHOTTYPE = 'InvalidParameterValue.UnsupportedSnapshotType'

# Unsupported sorting rule.
INVALIDPARAMETERVALUE_UNSUPPORTEDSORTRULE = 'InvalidParameterValue.UnsupportedSortRule'

# Unsupported stream protocol
INVALIDPARAMETERVALUE_UNSUPPORTEDSTREAMPROTOCOL = 'InvalidParameterValue.UnsupportedStreamProtocol'

# InvalidParameterValue.VLPlanResultIDNotExisted
INVALIDPARAMETERVALUE_VLPLANRESULTIDNOTEXISTED = 'InvalidParameterValue.VLPlanResultIDNotExisted'

# InvalidParameterValue.VLPlanResultIdsExceedLimit
INVALIDPARAMETERVALUE_VLPLANRESULTIDSEXCEEDLIMIT = 'InvalidParameterValue.VLPlanResultIdsExceedLimit'

# The number of channels added to the configuration in a single bulk operation exceeds the limit.
LIMITEXCEEDED_BATCHADDCHANNELNUMEXCEEDED = 'LimitExceeded.BatchAddChannelNumExceeded'

# Number of channels exceeds the limit.
LIMITEXCEEDED_CHANNELNUMEXCEEDED = 'LimitExceeded.ChannelNumExceeded'

# The number of queried devices cannot exceed 200.
LIMITEXCEEDED_DEICEIDQUANTITYEXCEEDEDLIMIT = 'LimitExceeded.DeiceIdQuantityExceededLimit'

# The number of queried national standard devices cannot exceed 500.
LIMITEXCEEDED_GBDEVICENUMEXCEEDED = 'LimitExceeded.GBDeviceNumExceeded'

# Image ID quantity exceeds the limit.
LIMITEXCEEDED_IMAGEIDSLICEEXCEEDLIMIT = 'LimitExceeded.ImageIdSliceExceedLimit'

# The creatable screenshot configuration quantity exceeds the limit.
LIMITEXCEEDED_SNAPSHOTCONFIGNUMEXCEEDED = 'LimitExceeded.SnapshotConfigNumExceeded'

# The creatable screenshot template quantity exceeds the limit.
LIMITEXCEEDED_SNAPSHOTTEMPLATENUMEXCEEDED = 'LimitExceeded.SnapshotTemplateNumExceeded'

# Number of time periods exceeds the limit
LIMITEXCEEDED_TIMELINESLICEEXCEEDLIMIT = 'LimitExceeded.TimelineSliceExceedLimit'

# Time segment not found
MISSINGPARAMETER_EMPTYTIMESECTION = 'MissingParameter.EmptyTimeSection'

# Lack of lifecycle parameters
MISSINGPARAMETER_MISSINGLIFERULEPARAM = 'MissingParameter.MissingLifeRuleParam'

# Lack of required parameters
MISSINGPARAMETER_MISSINGMUSTPARAMETER = 'MissingParameter.MissingMustParameter'

# Lack of retrieval task parameter
MISSINGPARAMETER_MISSINGRETRIEVETASKPARAM = 'MissingParameter.MissingRetrieveTaskParam'

# No update information.
MISSINGPARAMETER_MISSINGUPDATEDINFO = 'MissingParameter.MissingUpdatedInfo'

# Lack of user information
MISSINGPARAMETER_MISSINGUSERINFO = 'MissingParameter.MissingUserInfo'

# Bandwidth limitation
OPERATIONDENIED_BANDWIDTHLIMITZERO = 'OperationDenied.BandwidthLimitZero'

# Concurrent download limit exceeded
OPERATIONDENIED_CONCURRENTDOWNLOADSOVERLIMIT = 'OperationDenied.ConcurrentDownloadsOverLimit'

# Configuration is changing. Please try again later.
OPERATIONDENIED_CONFIGCHANGING = 'OperationDenied.ConfigChanging'

# Number of connections limited
OPERATIONDENIED_CONNECTSLIMITZERO = 'OperationDenied.ConnectsLimitZero'

# Failed to add the organization tree. The maximum depth of the organization tree is exceeded.
OPERATIONDENIED_EXCEEDEDMAXIMUMDEPTH = 'OperationDenied.ExceededMaximumDepth'

# Duplicate channel ID detected
OPERATIONDENIED_INPUTDUPLICATECHANNELID = 'OperationDenied.InputDuplicateChannelId'

# The feature requires allowlist configuration. To use it, you need to apply.
OPERATIONDENIED_NOWHITELIST = 'OperationDenied.NoWhitelist'

# Playback authentication is not enabled
OPERATIONDENIED_PLAYAUTHNOTENABLED = 'OperationDenied.PlayAuthNotEnabled'

# Resource unreachable. The resource is not within this region.
REGIONERROR_RESOURCEUNREACHABLE = 'RegionError.ResourceUnreachable'

# Existent channel with duplicate addition
RESOURCEINUSE_CHANNELREPEATADD = 'ResourceInUse.ChannelRepeatAdd'

# Cannot be modified during scheduled deletion.
RESOURCEINUSE_PLANDELETING = 'ResourceInUse.PlanDeleting'

# This template is associated with a plan and cannot be deleted.
RESOURCEINUSE_PLANLINKTEMPLATE = 'ResourceInUse.PlanLinkTemplate'

# Plan name must be unique
RESOURCEINUSE_PLANNAMEREPEAT = 'ResourceInUse.PlanNameRepeat'

# Retrieval task is in progress and cannot be deleted.
RESOURCEINUSE_RETRIEVETASKEXECUTING = 'ResourceInUse.RetrieveTaskExecuting'

# Retrieval task names cannot be duplicated.
RESOURCEINUSE_RETRIEVETASKNAMEREPEAT = 'ResourceInUse.RetrieveTaskNameRepeat'

# Template is currently in use and cannot be deleted.
RESOURCEINUSE_TEMPLATEISUSED = 'ResourceInUse.TemplateIsUsed'

# Template name must be unique.
RESOURCEINUSE_TEMPLATENAMEREPEAT = 'ResourceInUse.TemplateNameRepeat'

# Resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# Unable to access unauthorized devices
RESOURCENOTFOUND_ACCESSUNAUTHORIZED = 'ResourceNotFound.AccessUnauthorized'

# Channel not found
RESOURCENOTFOUND_CHANNELNOTEXIST = 'ResourceNotFound.ChannelNotExist'

# Device does not exist
RESOURCENOTFOUND_DEVICENOTEXIST = 'ResourceNotFound.DeviceNotExist'

# No available service nodes were found.
RESOURCENOTFOUND_NOTFOUNDCLUSTER = 'ResourceNotFound.NotFoundCluster'

# Organization ID does not exist.
RESOURCENOTFOUND_ORGANIZATIONIDNOTEXIST = 'ResourceNotFound.OrganizationIdNotExist'

# Plan not found
RESOURCENOTFOUND_PLANNOTEXIST = 'ResourceNotFound.PlanNotExist'

# The retrieval task does not exist.
RESOURCENOTFOUND_RETRIEVETASKNOTEXIST = 'ResourceNotFound.RetrieveTaskNotExist'

# Screenshot configuration not found
RESOURCENOTFOUND_SNAPSHOTCONFIGNOTEXIST = 'ResourceNotFound.SnapshotConfigNotExist'

# The template does not exist.
RESOURCENOTFOUND_TEMPLATENOTEXIST = 'ResourceNotFound.TemplateNotExist'

# Video recording not found.
RESOURCENOTFOUND_VIDEONOTFOUND = 'ResourceNotFound.VideoNotFound'

# Channel offline
RESOURCEUNAVAILABLE_CHANNELOFFLINE = 'ResourceUnavailable.ChannelOffline'

# Device disabled
RESOURCEUNAVAILABLE_DEVDISABLE = 'ResourceUnavailable.DevDisable'

# Device not registered.
RESOURCEUNAVAILABLE_DEVNOREGISTER = 'ResourceUnavailable.DevNoRegister'

# Device offline
RESOURCEUNAVAILABLE_DEVOFFLINE = 'ResourceUnavailable.DevOffline'

# Video recording archived
RESOURCEUNAVAILABLE_VIDEOARCHIVED = 'ResourceUnavailable.VideoArchived'

# Image domain name not found
UNSUPPORTEDOPERATION_IMAGEDOMAINNOTEXIST = 'UnsupportedOperation.ImageDomainNotExist'

# Devices added by the root account or other sub-accounts still exist in the organization. You cannot view or delete the organization.
UNSUPPORTEDOPERATION_ORGLINKDEV = 'UnsupportedOperation.OrgLinkDev'

# Deletion is not allowed when an organization has affiliated organizations.
UNSUPPORTEDOPERATION_ORGLINKORG = 'UnsupportedOperation.OrgLinkOrg'

# RTMP streaming domain not found
UNSUPPORTEDOPERATION_PUSHDOMAINNOTEXIST = 'UnsupportedOperation.PushDomainNotExist'

# StreamType and Resolution parameters are not supported to be delivered simultaneously.
UNSUPPORTEDOPERATION_STREAMTYPEORRESOLUTION = 'UnsupportedOperation.StreamTypeOrResolution'

# Intranet services are not enabled in this region.
UNSUPPORTEDOPERATION_UNOPENEDINTRANETSERVICESINREGION = 'UnsupportedOperation.UnopenedIntranetServicesInRegion'
