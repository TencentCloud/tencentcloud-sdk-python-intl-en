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


# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Failed to create the API gateway trigger.
FAILEDOPERATION_APIGATEWAY = 'FailedOperation.ApiGateway'

# Failed to create the trigger.
FAILEDOPERATION_APIGW = 'FailedOperation.Apigw'

# This operation is not supported by the current async event status. Please try again later.
FAILEDOPERATION_ASYNCEVENTSTATUS = 'FailedOperation.AsyncEventStatus'

# Login information verification failed and token verification failed.
FAILEDOPERATION_AUTHFAILURE = 'FailedOperation.AuthFailure'

# Failed to query the role information.
FAILEDOPERATION_CALLROLEFAILED = 'FailedOperation.CallRoleFailed'

# CopyAsyncRun parameter error
FAILEDOPERATION_COPYASYNCRUN = 'FailedOperation.CopyAsyncRun'

# Failed to replicate the function.
FAILEDOPERATION_COPYFAILED = 'FailedOperation.CopyFailed'

# Replication to this region is not supported.
FAILEDOPERATION_COPYFUNCTION = 'FailedOperation.CopyFunction'

# Failed to operate on the COS resources.
FAILEDOPERATION_COS = 'FailedOperation.Cos'

# Failed to create the alias.
FAILEDOPERATION_CREATEALIAS = 'FailedOperation.CreateAlias'

# Failed to create the namespace.
FAILEDOPERATION_CREATENAMESPACE = 'FailedOperation.CreateNamespace'

# This operation is not supported in the current function state.
FAILEDOPERATION_CREATETRIGGER = 'FailedOperation.CreateTrigger'

# This operation cannot be performed in the current debugging status.
FAILEDOPERATION_DEBUGMODESTATUS = 'FailedOperation.DebugModeStatus'

# Failed to delete the alias.
FAILEDOPERATION_DELETEALIAS = 'FailedOperation.DeleteAlias'

# This operation cannot be performed in the current function status. Please try again when the function is in normal status.
FAILEDOPERATION_DELETEFUNCTION = 'FailedOperation.DeleteFunction'

# Failed to delete the layer version.
FAILEDOPERATION_DELETELAYERVERSION = 'FailedOperation.DeleteLayerVersion'

# The default namespace cannot be deleted.
FAILEDOPERATION_DELETENAMESPACE = 'FailedOperation.DeleteNamespace'

# Failed to delete the trigger.
FAILEDOPERATION_DELETETRIGGER = 'FailedOperation.DeleteTrigger'

# You cannot update code in the current function state. Please try again when the state is normal.
FAILEDOPERATION_FUNCTIONNAMESTATUSERROR = 'FailedOperation.FunctionNameStatusError'

# Operation failed. The function is deploying.
FAILEDOPERATION_FUNCTIONSTATUSERROR = 'FailedOperation.FunctionStatusError'

# This operation cannot be performed in the current function version status. Please try again when the version is in normal status.
FAILEDOPERATION_FUNCTIONVERSIONSTATUSNOTACTIVE = 'FailedOperation.FunctionVersionStatusNotActive'

# Failed to get the alias information.
FAILEDOPERATION_GETALIAS = 'FailedOperation.GetAlias'

# Failed to get the function code address.
FAILEDOPERATION_GETFUNCTIONADDRESS = 'FailedOperation.GetFunctionAddress'

# The current account or namespace is in arrears. Please try again when it becomes available.
FAILEDOPERATION_INSUFFICIENTBALANCE = 'FailedOperation.InsufficientBalance'

# Failed to invoke the function.
FAILEDOPERATION_INVOKEFUNCTION = 'FailedOperation.InvokeFunction'

# Operation conflict.
FAILEDOPERATION_OPERATIONCONFLICT = 'FailedOperation.OperationConflict'

# Failed to create the scheduled provisioned concurrency scaling action
FAILEDOPERATION_PROVISIONCREATETIMER = 'FailedOperation.ProvisionCreateTimer'

# Failed to delete the scheduled provisioned concurrency scaling action
FAILEDOPERATION_PROVISIONDELETETIMER = 'FailedOperation.ProvisionDeleteTimer'

# Running out of available provisioned concurrency quota
FAILEDOPERATION_PROVISIONEDEXCEEDAVAILABLE = 'FailedOperation.ProvisionedExceedAvailable'

# The provisioned concurrency exceeds the limit.
FAILEDOPERATION_PROVISIONEDEXCEEDRESERVED = 'FailedOperation.ProvisionedExceedReserved'

# The function version already has a provisioned concurrency setting task in progress. Please try again later.
FAILEDOPERATION_PROVISIONEDINPROGRESS = 'FailedOperation.ProvisionedInProgress'

# Failed to publish the layer version.
FAILEDOPERATION_PUBLISHLAYERVERSION = 'FailedOperation.PublishLayerVersion'

# You cannot publish a version in the current function state. Please try again when the state is normal.
FAILEDOPERATION_PUBLISHVERSION = 'FailedOperation.PublishVersion'

# The value of ReservedExceedTotal exceeds the limit.
FAILEDOPERATION_RESERVEDEXCEEDTOTAL = 'FailedOperation.ReservedExceedTotal'

# The function already has a reserved concurrency setting task in progress. Please try again later.
FAILEDOPERATION_RESERVEDINPROGRESS = 'FailedOperation.ReservedInProgress'

# ServiceClosed. Please check and try again.
FAILEDOPERATION_SERVICECLOSED = 'FailedOperation.ServiceClosed'

# This topic does not exsit.
FAILEDOPERATION_TOPICNOTEXIST = 'FailedOperation.TopicNotExist'

# The user already has a concurrency quota setting task in progress. Please try again later.
FAILEDOPERATION_TOTALCONCURRENCYMEMORYINPROGRESS = 'FailedOperation.TotalConcurrencyMemoryInProgress'

# The specified service has not been activated. Please submit a ticket for activation.
FAILEDOPERATION_UNOPENEDSERVICE = 'FailedOperation.UnOpenedService'

# Failed to update the alias.
FAILEDOPERATION_UPDATEALIAS = 'FailedOperation.UpdateAlias'

# You cannot update code in the current function state. Please try again when the state is normal.
FAILEDOPERATION_UPDATEFUNCTIONCODE = 'FailedOperation.UpdateFunctionCode'

# Internal error.
INTERNALERROR = 'InternalError'

# Internal errors occurred during the creation of the apigw trigger.
INTERNALERROR_APIGATEWAY = 'InternalError.ApiGateway'

# ckafka API failure.
INTERNALERROR_CKAFKA = 'InternalError.Ckafka'

# Failed to delete the cmq trigger.
INTERNALERROR_CMQ = 'InternalError.Cmq'

# Failed to update the trigger.
INTERNALERROR_COS = 'InternalError.Cos'

# ES error.
INTERNALERROR_ES = 'InternalError.ES'

# Internal service error
INTERNALERROR_EXCEPTION = 'InternalError.Exception'

# Internal system error.
INTERNALERROR_SYSTEM = 'InternalError.System'

# The value of `FunctionName` does not conform to the specification. Please fix it and try again. For more information, please visit https://tencentcs.com/5jXKFnBW.
INVALIDPARAMETER_FUNCTIONNAME = 'InvalidParameter.FunctionName'

# Function creation parameter error.
INVALIDPARAMETER_PARAMERROR = 'InvalidParameter.ParamError'

# Invalid request parameter.
INVALIDPARAMETER_PAYLOAD = 'InvalidParameter.Payload'

# 
INVALIDPARAMETER_REQUESTTOOLARGE = 'InvalidParameter.RequestTooLarge'

# RoleCheck parameter error
INVALIDPARAMETER_ROLECHECK = 'InvalidParameter.RoleCheck'

# Incorrect `RoutingConfig` parameter.
INVALIDPARAMETER_ROUTINGCONFIG = 'InvalidParameter.RoutingConfig'

# Incorrect parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Incorrect `AdditionalVersionWeights` parameter.
INVALIDPARAMETERVALUE_ADDITIONALVERSIONWEIGHTS = 'InvalidParameterValue.AdditionalVersionWeights'

# The default alias cannot be deleted. Please check and try again.
INVALIDPARAMETERVALUE_ALIAS = 'InvalidParameterValue.Alias'

# ApiGateway parameter error.
INVALIDPARAMETERVALUE_APIGATEWAY = 'InvalidParameterValue.ApiGateway'

# The value of Args is incorrect.
INVALIDPARAMETERVALUE_ARGS = 'InvalidParameterValue.Args'

# The parameter for async retry configuration of the function is invalid.
INVALIDPARAMETERVALUE_ASYNCTRIGGERCONFIG = 'InvalidParameterValue.AsyncTriggerConfig'

# Cdn error.
INVALIDPARAMETERVALUE_CDN = 'InvalidParameterValue.Cdn'

# Ckafka error.
INVALIDPARAMETERVALUE_CKAFKA = 'InvalidParameterValue.Ckafka'

# Function running parameter error
INVALIDPARAMETERVALUE_CLIENTCONTEXT = 'InvalidParameterValue.ClientContext'

# Cmq error.
INVALIDPARAMETERVALUE_CMQ = 'InvalidParameterValue.Cmq'

# Code error.
INVALIDPARAMETERVALUE_CODE = 'InvalidParameterValue.Code'

# CodeSecret error.
INVALIDPARAMETERVALUE_CODESECRET = 'InvalidParameterValue.CodeSecret'

# CodeSource error.
INVALIDPARAMETERVALUE_CODESOURCE = 'InvalidParameterValue.CodeSource'

# The value of Command[Entrypoint] is incorrect.
INVALIDPARAMETERVALUE_COMMAND = 'InvalidParameterValue.Command'

# Incorrect `CompatibleRuntimes` parameter.
INVALIDPARAMETERVALUE_COMPATIBLERUNTIMES = 'InvalidParameterValue.CompatibleRuntimes'

# Incorrect `Content` parameter.
INVALIDPARAMETERVALUE_CONTENT = 'InvalidParameterValue.Content'

# Cos error.
INVALIDPARAMETERVALUE_COS = 'InvalidParameterValue.Cos'

# Invalid CosBucketName.
INVALIDPARAMETERVALUE_COSBUCKETNAME = 'InvalidParameterValue.CosBucketName'

# The value of CosBucketRegion is invalid. Please modify and try again. See: https://tencentcs.com/5jXKFnBW
INVALIDPARAMETERVALUE_COSBUCKETREGION = 'InvalidParameterValue.CosBucketRegion'

# Invalid CosObjectName.
INVALIDPARAMETERVALUE_COSOBJECTNAME = 'InvalidParameterValue.CosObjectName'

# CustomArgument exceeds the length limit.
INVALIDPARAMETERVALUE_CUSTOMARGUMENT = 'InvalidParameterValue.CustomArgument'

# DateTime error.
INVALIDPARAMETERVALUE_DATETIME = 'InvalidParameterValue.DateTime'

# Failed to create the default namespace.
INVALIDPARAMETERVALUE_DEFAULTNAMESPACE = 'InvalidParameterValue.DefaultNamespace'

# The code parameter of the function template corresponding with the DemoID is error.
INVALIDPARAMETERVALUE_DEMO = 'InvalidParameterValue.Demo'

# The DemoId does not exist.
INVALIDPARAMETERVALUE_DEMOID = 'InvalidParameterValue.DemoId'

# Description error.
INVALIDPARAMETERVALUE_DESCRIPTION = 'InvalidParameterValue.Description'

# The configuration of the environment variable DNS[OS_NAMESERVER] is incorrect.
INVALIDPARAMETERVALUE_DNSINFO = 'InvalidParameterValue.DnsInfo'

# The value of `Enable` does not conform to the specification. Please fix it and try again. For more information, please visit https://tencentcs.com/5jXKFnBW.
INVALIDPARAMETERVALUE_ENABLE = 'InvalidParameterValue.Enable'

# Environment error.
INVALIDPARAMETERVALUE_ENVIRONMENT = 'InvalidParameterValue.Environment'

# Filters parameter error.
INVALIDPARAMETERVALUE_FILTERS = 'InvalidParameterValue.Filters'

# The value of `FunctionName` is incorrect. See https://tencentcs.com/5jXKFnBW
INVALIDPARAMETERVALUE_FUNCTION = 'InvalidParameterValue.Function'

# The function does not exist.
INVALIDPARAMETERVALUE_FUNCTIONNAME = 'InvalidParameterValue.FunctionName'

# Request ID error
INVALIDPARAMETERVALUE_FUNCTIONREQUESTID = 'InvalidParameterValue.FunctionRequestId'

# FunctionType error
INVALIDPARAMETERVALUE_FUNCTIONTYPE = 'InvalidParameterValue.FunctionType'

# The format of GitBranch is incorrect. 
INVALIDPARAMETERVALUE_GITBRANCH = 'InvalidParameterValue.GitBranch'

# The format of GitDirectory is incorrect.
INVALIDPARAMETERVALUE_GITDIRECTORY = 'InvalidParameterValue.GitDirectory'

# The format of GitPassword is incorrect.
INVALIDPARAMETERVALUE_GITPASSWORD = 'InvalidParameterValue.GitPassword'

# The format of GitUrl is incorrect.
INVALIDPARAMETERVALUE_GITURL = 'InvalidParameterValue.GitUrl'

# The format of GitUserName is incorrect.
INVALIDPARAMETERVALUE_GITUSERNAME = 'InvalidParameterValue.GitUserName'

# Handler error.
INVALIDPARAMETERVALUE_HANDLER = 'InvalidParameterValue.Handler'

# ImageType error
INVALIDPARAMETERVALUE_IMAGETYPE = 'InvalidParameterValue.ImageType'

# The input of imageUri is incorrect.
INVALIDPARAMETERVALUE_IMAGEURI = 'InvalidParameterValue.ImageUri'

# Invalid InlineZipFile.
INVALIDPARAMETERVALUE_INLINEZIPFILE = 'InvalidParameterValue.InlineZipFile'

# The `InvokeType` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_INVOKETYPE = 'InvalidParameterValue.InvokeType'

# Incorrect `LayerName` parameter.
INVALIDPARAMETERVALUE_LAYERNAME = 'InvalidParameterValue.LayerName'

# Limit error.
INVALIDPARAMETERVALUE_LIMIT = 'InvalidParameterValue.Limit'

# The parameter exceeds the length limit.
INVALIDPARAMETERVALUE_LIMITEXCEEDED = 'InvalidParameterValue.LimitExceeded'

# MinCapacity parameter input error.
INVALIDPARAMETERVALUE_MINCAPACITY = 'InvalidParameterValue.MinCapacity'

# Incorrect `Name` parameter.
INVALIDPARAMETERVALUE_NAME = 'InvalidParameterValue.Name'

# Namespace error.
INVALIDPARAMETERVALUE_NAMESPACE = 'InvalidParameterValue.Namespace'

# Incorrect Namespace. A namespace contains up to 30 characters of letters, digits, hyphens (-), and underscores (_).
INVALIDPARAMETERVALUE_NAMESPACEINVALID = 'InvalidParameterValue.NamespaceInvalid'

# Invalid offset.
INVALIDPARAMETERVALUE_OFFSET = 'InvalidParameterValue.Offset'

# Order error.
INVALIDPARAMETERVALUE_ORDER = 'InvalidParameterValue.Order'

# The value of `OrderBy` does not conform to the specification. Please fix it and try again. For more information, please visit https://tencentcs.com/5jXKFnBW.
INVALIDPARAMETERVALUE_ORDERBY = 'InvalidParameterValue.OrderBy'

# The input parameter is not in the standard JSON format.
INVALIDPARAMETERVALUE_PARAM = 'InvalidParameterValue.Param'

# Cron expression of the scheduled action already exists
INVALIDPARAMETERVALUE_PROVISIONTRIGGERCRONCONFIGDUPLICATE = 'InvalidParameterValue.ProvisionTriggerCronConfigDuplicate'

# TriggerName input parameter error
INVALIDPARAMETERVALUE_PROVISIONTRIGGERNAME = 'InvalidParameterValue.ProvisionTriggerName'

# TriggerName already exists
INVALIDPARAMETERVALUE_PROVISIONTRIGGERNAMEDUPLICATE = 'InvalidParameterValue.ProvisionTriggerNameDuplicate'

# ProvisionType input parameter error
INVALIDPARAMETERVALUE_PROVISIONTYPE = 'InvalidParameterValue.ProvisionType'

# Unsupported function version.
INVALIDPARAMETERVALUE_QUALIFIER = 'InvalidParameterValue.Qualifier'

# Version parameter error
INVALIDPARAMETERVALUE_QUERYVERSION = 'InvalidParameterValue.QueryVersion'

# The value Enterprise Edition image ID [RegistryId] is incorrect.
INVALIDPARAMETERVALUE_REGISTRYID = 'InvalidParameterValue.RegistryId'

# Invalid RetCode
INVALIDPARAMETERVALUE_RETCODE = 'InvalidParameterValue.RetCode'

# The value of `RoutingConfig` does not conform to the specification. Please fix it and try again. For more information, please visit https://tencentcs.com/5jXKFnBW.
INVALIDPARAMETERVALUE_ROUTINGCONFIG = 'InvalidParameterValue.RoutingConfig'

# Runtime error.
INVALIDPARAMETERVALUE_RUNTIME = 'InvalidParameterValue.Runtime'

# The searchkey is not `Keyword`, `Tag`, or `Runtime`.
INVALIDPARAMETERVALUE_SEARCHKEY = 'InvalidParameterValue.SearchKey'

# SecretInfo error
INVALIDPARAMETERVALUE_SECRETINFO = 'InvalidParameterValue.SecretInfo'

# Invalid ServiceName.
INVALIDPARAMETERVALUE_SERVICENAME = 'InvalidParameterValue.ServiceName'

# The value of `Stamp` does not meet the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_STAMP = 'InvalidParameterValue.Stamp'

# The start time is incorrect.
INVALIDPARAMETERVALUE_STARTTIME = 'InvalidParameterValue.StartTime'

# You need to specify both the start time and the end time.
INVALIDPARAMETERVALUE_STARTTIMEORENDTIME = 'InvalidParameterValue.StartTimeOrEndTime'

# The `Status` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_STATUS = 'InvalidParameterValue.Status'

# Invalid TempCosObjectName.
INVALIDPARAMETERVALUE_TEMPCOSOBJECTNAME = 'InvalidParameterValue.TempCosObjectName'

# TrackingTarget parameter error
INVALIDPARAMETERVALUE_TRACKINGTARGET = 'InvalidParameterValue.TrackingTarget'

# TriggerCronConfig input parameter error
INVALIDPARAMETERVALUE_TRIGGERCRONCONFIG = 'InvalidParameterValue.TriggerCronConfig'

# The interval of triggering specified in TriggerCronConfig is smaller than the specified value.
INVALIDPARAMETERVALUE_TRIGGERCRONCONFIGTIMEINTERVAL = 'InvalidParameterValue.TriggerCronConfigTimeInterval'

# TriggerDesc error.
INVALIDPARAMETERVALUE_TRIGGERDESC = 'InvalidParameterValue.TriggerDesc'

# TriggerName error.
INVALIDPARAMETERVALUE_TRIGGERNAME = 'InvalidParameterValue.TriggerName'

# TriggerProvisionedConcurrencyNum input parameter error
INVALIDPARAMETERVALUE_TRIGGERPROVISIONEDCONCURRENCYNUM = 'InvalidParameterValue.TriggerProvisionedConcurrencyNum'

# Type error.
INVALIDPARAMETERVALUE_TYPE = 'InvalidParameterValue.Type'

# A non-standard zip file was detected. Please recompress and try again.
INVALIDPARAMETERVALUE_ZIPFILE = 'InvalidParameterValue.ZipFile'

# Failed to Base64-decode the compressed file: `Incorrect padding`. Please fix it and try again.
INVALIDPARAMETERVALUE_ZIPFILEBASE64BINASCIIERROR = 'InvalidParameterValue.ZipFileBase64BinasciiError'

# The number of aliases exceeds the upper limit.
LIMITEXCEEDED_ALIAS = 'LimitExceeded.Alias'

# The Cdn usage exceeds the upper limit.
LIMITEXCEEDED_CDN = 'LimitExceeded.Cdn'

# If the number of functions exceeds the upper limit, you can apply for an increase by [submitting a ticket](https://intl.cloud.tencent.com/act/event/Online_service?from=scf%7Cindex?from_cn_redirect=1).
LIMITEXCEEDED_FUNCTION = 'LimitExceeded.Function'

# The number of functions under the same topic exceeds the upper limit.
LIMITEXCEEDED_FUNCTIONONTOPIC = 'LimitExceeded.FunctionOnTopic'

# The value of `FunctionProvisionedConcurrencyMemory` has reached the upper limit. You can submit a ticket to increase it at https://mc.tencent.com/dI7DzbBV.
LIMITEXCEEDED_FUNCTIONPROVISIONEDCONCURRENCYMEMORY = 'LimitExceeded.FunctionProvisionedConcurrencyMemory'

# The function's reserved concurrency memory has exceeded the limit.
LIMITEXCEEDED_FUNCTIONRESERVEDCONCURRENCYMEMORY = 'LimitExceeded.FunctionReservedConcurrencyMemory'

# The value of `FunctionTotalProvisionedConcurrencyMemory` has reached the upper limit. You can submit a ticket to increase it at https://mc.tencent.com/dI7DzbBV.
LIMITEXCEEDED_FUNCTIONTOTALPROVISIONEDCONCURRENCYMEMORY = 'LimitExceeded.FunctionTotalProvisionedConcurrencyMemory'

# The total amount of provisioned concurrency of the function has exceeded the limit.
LIMITEXCEEDED_FUNCTIONTOTALPROVISIONEDCONCURRENCYNUM = 'LimitExceeded.FunctionTotalProvisionedConcurrencyNum'

# The number of layer versions exceeds the upper limit.
LIMITEXCEEDED_LAYERVERSIONS = 'LimitExceeded.LayerVersions'

# 
LIMITEXCEEDED_LAYERS = 'LimitExceeded.Layers'

# Reached the upper limit of dynamic scaling.
LIMITEXCEEDED_MAXCAPACITY = 'LimitExceeded.MaxCapacity'

# The memory exceeds the upper limit.
LIMITEXCEEDED_MEMORY = 'LimitExceeded.Memory'

# The message retention period in the async retry configuration of the function exceeds the limit.
LIMITEXCEEDED_MSGTTL = 'LimitExceeded.MsgTTL'

# If the number of namespaces exceeds the upper limit, you can apply for an increase by [submitting a ticket](https://intl.cloud.tencent.com/act/event/Online_service?from=scf%7Cindex?from_cn_redirect=1).
LIMITEXCEEDED_NAMESPACE = 'LimitExceeded.Namespace'

# Offset exceeds the upper limit.
LIMITEXCEEDED_OFFSET = 'LimitExceeded.Offset'

# The number of provisioned concurrency specified for the scheduled action is too large.
LIMITEXCEEDED_PROVISIONTRIGGERACTION = 'LimitExceeded.ProvisionTriggerAction'

# The interval of triggering is too short.
LIMITEXCEEDED_PROVISIONTRIGGERINTERVAL = 'LimitExceeded.ProvisionTriggerInterval'

# Reached the upper limit of quota
LIMITEXCEEDED_QUOTA = 'LimitExceeded.Quota'

# The number of retry attempts in the async retry configuration of the function exceeds the limit.
LIMITEXCEEDED_RETRYNUM = 'LimitExceeded.RetryNum'

# Timeout exceeds the upper limit.
LIMITEXCEEDED_TIMEOUT = 'LimitExceeded.Timeout'

# The account concurrency memory has exceeded the limit.
LIMITEXCEEDED_TOTALCONCURRENCYMEMORY = 'LimitExceeded.TotalConcurrencyMemory'

# If the number of triggers exceeds the upper limit, you can apply for an increase by [submitting a ticket](https://intl.cloud.tencent.com/act/event/Online_service?from=scf%7Cindex?from_cn_redirect=1).
LIMITEXCEEDED_TRIGGER = 'LimitExceeded.Trigger'

# The value of `UserTotalConcurrencyMemory` has reached the upper limit. You can submit a ticket to increase it at https://tencentcs.com/7Fixwt63.
LIMITEXCEEDED_USERTOTALCONCURRENCYMEMORY = 'LimitExceeded.UserTotalConcurrencyMemory'

# Missing parameter.
MISSINGPARAMETER = 'MissingParameter'

# The resource is in use.
RESOURCEINUSE = 'ResourceInUse'

# The alias is in use.
RESOURCEINUSE_ALIAS = 'ResourceInUse.Alias'

# Cdn is in use.
RESOURCEINUSE_CDN = 'ResourceInUse.Cdn'

# Cmq is in use.
RESOURCEINUSE_CMQ = 'ResourceInUse.Cmq'

# Cos is in use.
RESOURCEINUSE_COS = 'ResourceInUse.Cos'

# This FunctionName already exists.
RESOURCEINUSE_FUNCTIONNAME = 'ResourceInUse.FunctionName'

# The layer version is in use.
RESOURCEINUSE_LAYERVERSION = 'ResourceInUse.LayerVersion'

# This Namespace already exists.
RESOURCEINUSE_NAMESPACE = 'ResourceInUse.Namespace'

# This TriggerName already exists.
RESOURCEINUSE_TRIGGER = 'ResourceInUse.Trigger'

# This TriggerName already exists.
RESOURCEINUSE_TRIGGERNAME = 'ResourceInUse.TriggerName'

# Insufficient COS resources.
RESOURCEINSUFFICIENT_COS = 'ResourceInsufficient.COS'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The alias does not exist.
RESOURCENOTFOUND_ALIAS = 'ResourceNotFound.Alias'

# The specified `AsyncEvent` was not found. Please create it and try again.
RESOURCENOTFOUND_ASYNCEVENT = 'ResourceNotFound.AsyncEvent'

# Cdn does not exist.
RESOURCENOTFOUND_CDN = 'ResourceNotFound.Cdn'

# Ckafka does not exist.
RESOURCENOTFOUND_CKAFKA = 'ResourceNotFound.Ckafka'

# Cmq does not exist.
RESOURCENOTFOUND_CMQ = 'ResourceNotFound.Cmq'

# Cos does not exist.
RESOURCENOTFOUND_COS = 'ResourceNotFound.Cos'

# The function does not exist.
RESOURCENOTFOUND_FUNCTION = 'ResourceNotFound.Function'

# The function does not exist.
RESOURCENOTFOUND_FUNCTIONNAME = 'ResourceNotFound.FunctionName'

# The function version does not exist.
RESOURCENOTFOUND_FUNCTIONVERSION = 'ResourceNotFound.FunctionVersion'

# Failed to find the specified `ImageConfig`. Please create it first.
RESOURCENOTFOUND_IMAGECONFIG = 'ResourceNotFound.ImageConfig'

# The layer does not exist.
RESOURCENOTFOUND_LAYER = 'ResourceNotFound.Layer'

# The layer version does not exist.
RESOURCENOTFOUND_LAYERVERSION = 'ResourceNotFound.LayerVersion'

# Namespace does not exist.
RESOURCENOTFOUND_NAMESPACE = 'ResourceNotFound.Namespace'

# The version does not exist.
RESOURCENOTFOUND_QUALIFIER = 'ResourceNotFound.Qualifier'

# The role does not exist.
RESOURCENOTFOUND_ROLECHECK = 'ResourceNotFound.RoleCheck'

# Timer does not exist.
RESOURCENOTFOUND_TIMER = 'ResourceNotFound.Timer'

# The concurrency memory quota resource was not found.
RESOURCENOTFOUND_TOTALCONCURRENCYMEMORY = 'ResourceNotFound.TotalConcurrencyMemory'

# The trigger does not exist.
RESOURCENOTFOUND_TRIGGER = 'ResourceNotFound.Trigger'

# The version does not exist.
RESOURCENOTFOUND_VERSION = 'ResourceNotFound.Version'

# Your balance is insufficient. Please top up first.
RESOURCEUNAVAILABLE_INSUFFICIENTBALANCE = 'ResourceUnavailable.InsufficientBalance'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# CAM authentication failed.
UNAUTHORIZEDOPERATION_CAM = 'UnauthorizedOperation.CAM'

# You do not have permissions to access the code.
UNAUTHORIZEDOPERATION_CODESECRET = 'UnauthorizedOperation.CodeSecret'

# You do not have permissions.
UNAUTHORIZEDOPERATION_CREATETRIGGER = 'UnauthorizedOperation.CreateTrigger'

# Unauthorized operation.
UNAUTHORIZEDOPERATION_DELETEFUNCTION = 'UnauthorizedOperation.DeleteFunction'

# You do not have permissions.
UNAUTHORIZEDOPERATION_DELETETRIGGER = 'UnauthorizedOperation.DeleteTrigger'

# This API is not called from the console.
UNAUTHORIZEDOPERATION_NOTMC = 'UnauthorizedOperation.NotMC'

# Region error.
UNAUTHORIZEDOPERATION_REGION = 'UnauthorizedOperation.Region'

# The `Appid` of TempCos is not consistent with the APPID of the request account.
UNAUTHORIZEDOPERATION_TEMPCOSAPPID = 'UnauthorizedOperation.TempCosAppid'

# Operation failed.
UNAUTHORIZEDOPERATION_UPDATEFUNCTIONCODE = 'UnauthorizedOperation.UpdateFunctionCode'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# The resource is bound to an alias, and the current operation cannot be performed. Please unbind the alias and try again.
UNSUPPORTEDOPERATION_ALIASBIND = 'UnsupportedOperation.AliasBind'

# Cdn is not supported.
UNSUPPORTEDOPERATION_CDN = 'UnsupportedOperation.Cdn'

# Cos operation is not supported.
UNSUPPORTEDOPERATION_COS = 'UnsupportedOperation.Cos'

# The specified EipFixed does not exist.
UNSUPPORTEDOPERATION_EIPFIXED = 'UnsupportedOperation.EipFixed'

# This region is not supported.
UNSUPPORTEDOPERATION_REGION = 'UnsupportedOperation.Region'

# Trigger operation is not supported.
UNSUPPORTEDOPERATION_TRIGGER = 'UnsupportedOperation.Trigger'

# The specified configuration is not supported. Please modify and try again.
UNSUPPORTEDOPERATION_UPDATEFUNCTIONEVENTINVOKECONFIG = 'UnsupportedOperation.UpdateFunctionEventInvokeConfig'

# The specified VpcConfig does not exist.
UNSUPPORTEDOPERATION_VPCCONFIG = 'UnsupportedOperation.VpcConfig'
