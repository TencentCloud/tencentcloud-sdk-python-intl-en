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


# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# 
FAILEDOPERATION_ACCOUNTINSUFFICIENT = 'FailedOperation.AccountInsufficient'

# Failed to create the API gateway trigger.
FAILEDOPERATION_APIGATEWAY = 'FailedOperation.ApiGateway'

# Failed to create the trigger.
FAILEDOPERATION_APIGW = 'FailedOperation.Apigw'

# Failed to obtain Apm InstanceId
FAILEDOPERATION_APMCONFIGINSTANCEID = 'FailedOperation.ApmConfigInstanceId'

# This operation is not supported by the current async event status. Please try again later.
FAILEDOPERATION_ASYNCEVENTSTATUS = 'FailedOperation.AsyncEventStatus'

# Login information verification failed and token verification failed.
FAILEDOPERATION_AUTHFAILURE = 'FailedOperation.AuthFailure'

# 
FAILEDOPERATION_BINDPLUGIN = 'FailedOperation.BindPlugin'

# 
FAILEDOPERATION_CALLNETDEPLOYFAILED = 'FailedOperation.CallNetDeployFailed'

# Failed to query the role information.
FAILEDOPERATION_CALLROLEFAILED = 'FailedOperation.CallRoleFailed'

# 
FAILEDOPERATION_CLSSERVICEUNREGISTERED = 'FailedOperation.ClsServiceUnregistered'

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

# Execution timeout period cannot be updated in debug mode.
FAILEDOPERATION_DEBUGMODEUPDATETIMEOUTFAIL = 'FailedOperation.DebugModeUpdateTimeOutFail'

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

# 
FAILEDOPERATION_INSTANCENOTFOUND = 'FailedOperation.InstanceNotFound'

# The current account or namespace is in arrears. Please try again when it becomes available.
FAILEDOPERATION_INSUFFICIENTBALANCE = 'FailedOperation.InsufficientBalance'

# 
FAILEDOPERATION_INSUFFICIENTRESOURCES = 'FailedOperation.InsufficientResources'

# Failed to invoke the function.
FAILEDOPERATION_INVOKEFUNCTION = 'FailedOperation.InvokeFunction'

# 
FAILEDOPERATION_MIXNODECONFIG = 'FailedOperation.MixNodeConfig'

# Failed to activate the service.
FAILEDOPERATION_OPENSERVICE = 'FailedOperation.OpenService'

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

# The role does not exist.
FAILEDOPERATION_QCSROLENOTFOUND = 'FailedOperation.QcsRoleNotFound'

# Query failed.
FAILEDOPERATION_QUERYERROR = 'FailedOperation.QueryError'

# The value of ReservedExceedTotal exceeds the limit.
FAILEDOPERATION_RESERVEDEXCEEDTOTAL = 'FailedOperation.ReservedExceedTotal'

# The function already has a reserved concurrency setting task in progress. Please try again later.
FAILEDOPERATION_RESERVEDINPROGRESS = 'FailedOperation.ReservedInProgress'

# ServiceClosed. Please check and try again.
FAILEDOPERATION_SERVICECLOSED = 'FailedOperation.ServiceClosed'

# 
FAILEDOPERATION_SESSIONNAME = 'FailedOperation.SessionName'

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

# The `UpdateFunctionConfiguration` operation failed.
FAILEDOPERATION_UPDATEFUNCTIONCONFIGURATION = 'FailedOperation.UpdateFunctionConfiguration'

# Failed to update the status
FAILEDOPERATION_UPDATESTATUS = 'FailedOperation.UpdateStatus'

# The new status is the same as the previous one.
FAILEDOPERATION_UPDATETRIGGERSTATUS = 'FailedOperation.UpdateTriggerStatus'

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

# Internal service error.
INTERNALERROR_SYSTEMERROR = 'InternalError.SystemError'

# Log parameter error
INVALIDPARAMETER_CLS = 'InvalidParameter.Cls'

# The value of `FunctionName` does not conform to the specification. Please fix it and try again. For more information, please visit https://tencentcs.com/5jXKFnBW.
INVALIDPARAMETER_FUNCTIONNAME = 'InvalidParameter.FunctionName'

# 
INVALIDPARAMETER_GOOSEFSREQUIRED = 'InvalidParameter.GooseFsRequired'

# Function creation parameter error.
INVALIDPARAMETER_PARAMERROR = 'InvalidParameter.ParamError'

# Invalid request parameter.
INVALIDPARAMETER_PAYLOAD = 'InvalidParameter.Payload'

# Request size 
INVALIDPARAMETER_REQUESTTOOLARGE = 'InvalidParameter.RequestTooLarge'

# RoleCheck parameter error
INVALIDPARAMETER_ROLECHECK = 'InvalidParameter.RoleCheck'

# Incorrect `RoutingConfig` parameter.
INVALIDPARAMETER_ROUTINGCONFIG = 'InvalidParameter.RoutingConfig'

# Incorrect parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Invalid `Action` value. For more information, go to https://tencentcs.com/5jXKFnBW.
INVALIDPARAMETERVALUE_ACTION = 'InvalidParameterValue.Action'

# Incorrect `AdditionalVersionWeights` parameter.
INVALIDPARAMETERVALUE_ADDITIONALVERSIONWEIGHTS = 'InvalidParameterValue.AdditionalVersionWeights'

# The default alias cannot be deleted. Please check and try again.
INVALIDPARAMETERVALUE_ALIAS = 'InvalidParameterValue.Alias'

# ApiGateway parameter error.
INVALIDPARAMETERVALUE_APIGATEWAY = 'InvalidParameterValue.ApiGateway'

# ApmConfig input error
INVALIDPARAMETERVALUE_APMCONFIG = 'InvalidParameterValue.ApmConfig'

# ApmConfigInstanceId input error
INVALIDPARAMETERVALUE_APMCONFIGINSTANCEID = 'InvalidParameterValue.ApmConfigInstanceId'

# ApmConfigRegion input error
INVALIDPARAMETERVALUE_APMCONFIGREGION = 'InvalidParameterValue.ApmConfigRegion'

# The value of Args is incorrect.
INVALIDPARAMETERVALUE_ARGS = 'InvalidParameterValue.Args'

# The parameter for async retry configuration of the function is invalid.
INVALIDPARAMETERVALUE_ASYNCTRIGGERCONFIG = 'InvalidParameterValue.AsyncTriggerConfig'

# Cdn error.
INVALIDPARAMETERVALUE_CDN = 'InvalidParameterValue.Cdn'

# 
INVALIDPARAMETERVALUE_CFSID = 'InvalidParameterValue.CfsId'

# 
INVALIDPARAMETERVALUE_CFSLOCALMOUNTDIR = 'InvalidParameterValue.CfsLocalMountDir'

# 
INVALIDPARAMETERVALUE_CFSMOUNTINSID = 'InvalidParameterValue.CfsMountInsId'

# The `cfs` configuration item already exists.
INVALIDPARAMETERVALUE_CFSPARAMETERDUPLICATE = 'InvalidParameterValue.CfsParameterDuplicate'

# The value of `cfs` configuration item does not meet the specification.
INVALIDPARAMETERVALUE_CFSPARAMETERERROR = 'InvalidParameterValue.CfsParameterError'

# 
INVALIDPARAMETERVALUE_CFSREGION = 'InvalidParameterValue.CfsRegion'

# 
INVALIDPARAMETERVALUE_CFSREMOTEMOUNTDIR = 'InvalidParameterValue.CfsRemoteMountDir'

# 
INVALIDPARAMETERVALUE_CFSTYPE = 'InvalidParameterValue.CfsType'

# 
INVALIDPARAMETERVALUE_CFSUSERGROUPID = 'InvalidParameterValue.CfsUserGroupId'

# 
INVALIDPARAMETERVALUE_CFSUSERID = 'InvalidParameterValue.CfsUserId'

# Ckafka error.
INVALIDPARAMETERVALUE_CKAFKA = 'InvalidParameterValue.Ckafka'

# Function running parameter error
INVALIDPARAMETERVALUE_CLIENTCONTEXT = 'InvalidParameterValue.ClientContext'

# Cls error.
INVALIDPARAMETERVALUE_CLS = 'InvalidParameterValue.Cls'

# To modify CLS configuration, Role parameter is required. Please check and try again.
INVALIDPARAMETERVALUE_CLSROLE = 'InvalidParameterValue.ClsRole'

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

# 
INVALIDPARAMETERVALUE_COSFSBUCKETMOUNTDIR = 'InvalidParameterValue.CosFsBucketMountDir'

# 
INVALIDPARAMETERVALUE_COSFSBUCKETNAME = 'InvalidParameterValue.CosFsBucketName'

# 
INVALIDPARAMETERVALUE_COSFSLOCALMOUNTDIR = 'InvalidParameterValue.CosFsLocalMountDir'

# 
INVALIDPARAMETERVALUE_COSFSREGION = 'InvalidParameterValue.CosFsRegion'

# 
INVALIDPARAMETERVALUE_COSFSSTRUCTION = 'InvalidParameterValue.CosFsStruction'

# 
INVALIDPARAMETERVALUE_COSFSTYPE = 'InvalidParameterValue.CosFsType'

# COS notification rule conflict
INVALIDPARAMETERVALUE_COSNOTIFYRULECONFLICT = 'InvalidParameterValue.CosNotifyRuleConflict'

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

# 
INVALIDPARAMETERVALUE_DISKSIZE = 'InvalidParameterValue.DiskSize'

# The configuration of the environment variable DNS[OS_NAMESERVER] is incorrect.
INVALIDPARAMETERVALUE_DNSINFO = 'InvalidParameterValue.DnsInfo'

# 
INVALIDPARAMETERVALUE_DYNAMICENABLED = 'InvalidParameterValue.DynamicEnabled'

# EipConfig parameter error.
INVALIDPARAMETERVALUE_EIPCONFIG = 'InvalidParameterValue.EipConfig'

# The value of `Enable` does not conform to the specification. Please fix it and try again. For more information, please visit https://tencentcs.com/5jXKFnBW.
INVALIDPARAMETERVALUE_ENABLE = 'InvalidParameterValue.Enable'

# Environment error.
INVALIDPARAMETERVALUE_ENVIRONMENT = 'InvalidParameterValue.Environment'

# The size of the environment variable exceeds the limit. Please keep it within 4 KB.
INVALIDPARAMETERVALUE_ENVIRONMENTEXCEEDEDLIMIT = 'InvalidParameterValue.EnvironmentExceededLimit'

# You cannot modify the function's system environment variables or runtime environment variables.
INVALIDPARAMETERVALUE_ENVIRONMENTSYSTEMPROTECT = 'InvalidParameterValue.EnvironmentSystemProtect'

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

# 
INVALIDPARAMETERVALUE_GOOSEFSCLUSTER = 'InvalidParameterValue.GooseFsCluster'

# 
INVALIDPARAMETERVALUE_GOOSEFSCLUSTERGOOSEFSSITEPROPERTIESBASE64DECODEERR = 'InvalidParameterValue.GooseFsClusterGooseFsSitePropertiesBase64DecodeErr'

# 
INVALIDPARAMETERVALUE_GOOSEFSCLUSTERGOOSEFSSITEPROPERTIESFORMATERR = 'InvalidParameterValue.GooseFsClusterGooseFsSitePropertiesFormatErr'

# 
INVALIDPARAMETERVALUE_GOOSEFSENDPOINT = 'InvalidParameterValue.GooseFsEndpoint'

# 
INVALIDPARAMETERVALUE_GOOSEFSFUSEJVMCONFIG = 'InvalidParameterValue.GooseFsFuseJVMConfig'

# 
INVALIDPARAMETERVALUE_GOOSEFSLOCALMOUNTDIR = 'InvalidParameterValue.GooseFsLocalMountDir'

# 
INVALIDPARAMETERVALUE_GOOSEFSNAMESPACE = 'InvalidParameterValue.GooseFsNamespace'

# 
INVALIDPARAMETERVALUE_GOOSEFSREMOTEMOUNTPATH = 'InvalidParameterValue.GooseFsRemoteMountPath'

# 
INVALIDPARAMETERVALUE_GOOSEFSSTRUCTIONERROR = 'InvalidParameterValue.GooseFsStructionError'

# 
INVALIDPARAMETERVALUE_GOOSEFSTYPE = 'InvalidParameterValue.GooseFsType'

# Handler error.
INVALIDPARAMETERVALUE_HANDLER = 'InvalidParameterValue.Handler'

# IdleTimeOut input parameter error
INVALIDPARAMETERVALUE_IDLETIMEOUT = 'InvalidParameterValue.IdleTimeOut'

# ImageType error
INVALIDPARAMETERVALUE_IMAGETYPE = 'InvalidParameterValue.ImageType'

# The input of imageUri is incorrect.
INVALIDPARAMETERVALUE_IMAGEURI = 'InvalidParameterValue.ImageUri'

# Invalid InlineZipFile.
INVALIDPARAMETERVALUE_INLINEZIPFILE = 'InvalidParameterValue.InlineZipFile'

# 
INVALIDPARAMETERVALUE_INSTANCECONCURRENCYCONFIG = 'InvalidParameterValue.InstanceConcurrencyConfig'

# The `InvokeType` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_INVOKETYPE = 'InvalidParameterValue.InvokeType'

# The value of L5Enable is invalid. Please modify and try again.
INVALIDPARAMETERVALUE_L5ENABLE = 'InvalidParameterValue.L5Enable'

# Incorrect `LayerName` parameter.
INVALIDPARAMETERVALUE_LAYERNAME = 'InvalidParameterValue.LayerName'

# Layers parameter error.
INVALIDPARAMETERVALUE_LAYERS = 'InvalidParameterValue.Layers'

# Limit error.
INVALIDPARAMETERVALUE_LIMIT = 'InvalidParameterValue.Limit'

# The parameter exceeds the length limit.
INVALIDPARAMETERVALUE_LIMITEXCEEDED = 'InvalidParameterValue.LimitExceeded'

# 
INVALIDPARAMETERVALUE_LOGFORMAT = 'InvalidParameterValue.LogFormat'

# 
INVALIDPARAMETERVALUE_MAXCONCURRENCY = 'InvalidParameterValue.MaxConcurrency'

# The value of `Memory` does not conform to the specification. Please fix it and try again. For more information, please visit https://tencentcs.com/5jXKFnBW.
INVALIDPARAMETERVALUE_MEMORY = 'InvalidParameterValue.Memory'

# MemorySize error.
INVALIDPARAMETERVALUE_MEMORYSIZE = 'InvalidParameterValue.MemorySize'

# MinCapacity parameter input error.
INVALIDPARAMETERVALUE_MINCAPACITY = 'InvalidParameterValue.MinCapacity'

# 
INVALIDPARAMETERVALUE_MOUNTOPTION = 'InvalidParameterValue.MountOption'

# Incorrect `Name` parameter.
INVALIDPARAMETERVALUE_NAME = 'InvalidParameterValue.Name'

# Namespace error.
INVALIDPARAMETERVALUE_NAMESPACE = 'InvalidParameterValue.Namespace'

# Incorrect Namespace. A namespace contains up to 30 characters of letters, digits, hyphens (-), and underscores (_).
INVALIDPARAMETERVALUE_NAMESPACEINVALID = 'InvalidParameterValue.NamespaceInvalid'

# NodeSpec parameter error
INVALIDPARAMETERVALUE_NODESPEC = 'InvalidParameterValue.NodeSpec'

# NodeType parameter error
INVALIDPARAMETERVALUE_NODETYPE = 'InvalidParameterValue.NodeType'

# Invalid offset.
INVALIDPARAMETERVALUE_OFFSET = 'InvalidParameterValue.Offset'

# Order error.
INVALIDPARAMETERVALUE_ORDER = 'InvalidParameterValue.Order'

# The value of `OrderBy` does not conform to the specification. Please fix it and try again. For more information, please visit https://tencentcs.com/5jXKFnBW.
INVALIDPARAMETERVALUE_ORDERBY = 'InvalidParameterValue.OrderBy'

# The input parameter is not in the standard JSON format.
INVALIDPARAMETERVALUE_PARAM = 'InvalidParameterValue.Param'

# 
INVALIDPARAMETERVALUE_PERMISSION = 'InvalidParameterValue.Permission'

# 
INVALIDPARAMETERVALUE_PLUGINCONFIG = 'InvalidParameterValue.PluginConfig'

# 
INVALIDPARAMETERVALUE_PORT = 'InvalidParameterValue.Port'

# Cron expression of the scheduled action already exists
INVALIDPARAMETERVALUE_PROVISIONTRIGGERCRONCONFIGDUPLICATE = 'InvalidParameterValue.ProvisionTriggerCronConfigDuplicate'

# TriggerName input parameter error
INVALIDPARAMETERVALUE_PROVISIONTRIGGERNAME = 'InvalidParameterValue.ProvisionTriggerName'

# TriggerName already exists
INVALIDPARAMETERVALUE_PROVISIONTRIGGERNAMEDUPLICATE = 'InvalidParameterValue.ProvisionTriggerNameDuplicate'

# ProvisionType input parameter error
INVALIDPARAMETERVALUE_PROVISIONTYPE = 'InvalidParameterValue.ProvisionType'

# The `PublicNetConfig` parameter is invalid.
INVALIDPARAMETERVALUE_PUBLICNETCONFIG = 'InvalidParameterValue.PublicNetConfig'

# Unsupported function version.
INVALIDPARAMETERVALUE_QUALIFIER = 'InvalidParameterValue.Qualifier'

# Version parameter error
INVALIDPARAMETERVALUE_QUERYVERSION = 'InvalidParameterValue.QueryVersion'

# 
INVALIDPARAMETERVALUE_READINESSPROBE = 'InvalidParameterValue.ReadinessProbe'

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

# The system environment variable is invalid.
INVALIDPARAMETERVALUE_SYSTEMENVIRONMENT = 'InvalidParameterValue.SystemEnvironment'

# Invalid TempCosObjectName.
INVALIDPARAMETERVALUE_TEMPCOSOBJECTNAME = 'InvalidParameterValue.TempCosObjectName'

# The value of `TraceEnable` is invalid. Please modify and try again.
INVALIDPARAMETERVALUE_TRACEENABLE = 'InvalidParameterValue.TraceEnable'

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

# 
INVALIDPARAMETERVALUE_VPC = 'InvalidParameterValue.Vpc'

# WebSocketsParams input parameter error
INVALIDPARAMETERVALUE_WEBSOCKETSPARAMS = 'InvalidParameterValue.WebSocketsParams'

# A non-standard zip file was detected. Please recompress and try again.
INVALIDPARAMETERVALUE_ZIPFILE = 'InvalidParameterValue.ZipFile'

# Failed to Base64-decode the compressed file: `Incorrect padding`. Please fix it and try again.
INVALIDPARAMETERVALUE_ZIPFILEBASE64BINASCIIERROR = 'InvalidParameterValue.ZipFileBase64BinasciiError'

# The number of aliases exceeds the upper limit.
LIMITEXCEEDED_ALIAS = 'LimitExceeded.Alias'

# The Cdn usage exceeds the upper limit.
LIMITEXCEEDED_CDN = 'LimitExceeded.Cdn'

# Reached the upper limit of function versions enabling image acceleration
LIMITEXCEEDED_CONTAINERIMAGEACCELERATE = 'LimitExceeded.ContainerImageAccelerate'

# Reached the upper limit of function versions enabling image acceleration
LIMITEXCEEDED_CONTAINERIMAGEACCELERATEQUOTA = 'LimitExceeded.ContainerImageAccelerateQuota'

# The EIP resource exceeded the limit.
LIMITEXCEEDED_EIP = 'LimitExceeded.Eip'

# 
LIMITEXCEEDED_FS = 'LimitExceeded.Fs'

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

# The value of `InitTimeout` has reached the upper limit. You can submit a ticket to increase it at https://tencentcs.com/7Fixwt63.
LIMITEXCEEDED_INITTIMEOUT = 'LimitExceeded.InitTimeout'

# 
LIMITEXCEEDED_INTRAIP = 'LimitExceeded.IntraIp'

# The number of layer versions exceeds the upper limit.
LIMITEXCEEDED_LAYERVERSIONS = 'LimitExceeded.LayerVersions'

# The number of layers exceeds the maximum limit.
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

# 
LIMITEXCEEDED_PRIVILEGECONTAINER = 'LimitExceeded.PrivilegeContainer'

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

# This account has been isolated.
OPERATIONDENIED_ACCOUNTISOLATE = 'OperationDenied.AccountIsolate'

# Account does not exist.
OPERATIONDENIED_ACCOUNTNOTEXISTS = 'OperationDenied.AccountNotExists'

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

# The tag key does not exist.
RESOURCENOTFOUND_ATTACHEDTAGKEYNOTFOUND = 'ResourceNotFound.AttachedTagKeyNotFound'

# Cdn does not exist.
RESOURCENOTFOUND_CDN = 'ResourceNotFound.Cdn'

# Unable to find the specified mount point under the specified CFS
RESOURCENOTFOUND_CFSMOUNTINSNOTMATCH = 'ResourceNotFound.CfsMountInsNotMatch'

# 
RESOURCENOTFOUND_CFSPROTOCOLERROR = 'ResourceNotFound.CfsProtocolError'

# CFS not available
RESOURCENOTFOUND_CFSSTATUSERROR = 'ResourceNotFound.CfsStatusError'

# VPCs of the CFS instance and the SCF function are different.
RESOURCENOTFOUND_CFSVPCNOTMATCH = 'ResourceNotFound.CfsVpcNotMatch'

# Ckafka does not exist.
RESOURCENOTFOUND_CKAFKA = 'ResourceNotFound.Ckafka'

# Cmq does not exist.
RESOURCENOTFOUND_CMQ = 'ResourceNotFound.Cmq'

# Cos does not exist.
RESOURCENOTFOUND_COS = 'ResourceNotFound.Cos'

# 
RESOURCENOTFOUND_COSOBJECT = 'ResourceNotFound.CosObject'

# The function does not exist.
RESOURCENOTFOUND_FUNCTION = 'ResourceNotFound.Function'

# The function does not exist.
RESOURCENOTFOUND_FUNCTIONNAME = 'ResourceNotFound.FunctionName'

# The function version does not exist.
RESOURCENOTFOUND_FUNCTIONVERSION = 'ResourceNotFound.FunctionVersion'

# An error occurred while getting the CFS mount target information.
RESOURCENOTFOUND_GETCFSMOUNTINSERROR = 'ResourceNotFound.GetCfsMountInsError'

# An error occurred while getting the CFS information.
RESOURCENOTFOUND_GETCFSNOTMATCH = 'ResourceNotFound.GetCfsNotMatch'

# 
RESOURCENOTFOUND_GOOSEFSCLUSTERENDPOINT = 'ResourceNotFound.GooseFsClusterEndpoint'

# 
RESOURCENOTFOUND_GOOSEFSCLUSTERID = 'ResourceNotFound.GooseFsClusterId'

# 
RESOURCENOTFOUND_GOOSEFSCLUSTERNAMESPACE = 'ResourceNotFound.GooseFsClusterNamespace'

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
RESOURCENOTFOUND_ROLE = 'ResourceNotFound.Role'

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

# The VPC or subnet does not exist.
RESOURCENOTFOUND_VPC = 'ResourceNotFound.Vpc'

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

# Not authorized to access your COS resources.
UNAUTHORIZEDOPERATION_ROLE = 'UnauthorizedOperation.Role'

# The `Appid` of TempCos is not consistent with the APPID of the request account.
UNAUTHORIZEDOPERATION_TEMPCOSAPPID = 'UnauthorizedOperation.TempCosAppid'

# Operation failed.
UNAUTHORIZEDOPERATION_UPDATEFUNCTIONCODE = 'UnauthorizedOperation.UpdateFunctionCode'

# You are not authorized for the operation.
UNAUTHORIZEDOPERATION_UPDATETRIGGERSTATUS = 'UnauthorizedOperation.UpdateTriggerStatus'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# The resource is bound to an alias, and the current operation cannot be performed. Please unbind the alias and try again.
UNSUPPORTEDOPERATION_ALIASBIND = 'UnsupportedOperation.AliasBind'

# Cdn is not supported.
UNSUPPORTEDOPERATION_CDN = 'UnsupportedOperation.Cdn'

# The function cannot be copied.
UNSUPPORTEDOPERATION_COPYFUNCTION = 'UnsupportedOperation.CopyFunction'

# Cos operation is not supported.
UNSUPPORTEDOPERATION_COS = 'UnsupportedOperation.Cos'

# 
UNSUPPORTEDOPERATION_DISKSIZE = 'UnsupportedOperation.DiskSize'

# The specified EipFixed does not exist.
UNSUPPORTEDOPERATION_EIPFIXED = 'UnsupportedOperation.EipFixed'

# Unsupported region.
UNSUPPORTEDOPERATION_NOTSUPPORTREGION = 'UnsupportedOperation.NotSupportRegion'

# Cannot release the version in the current state.
UNSUPPORTEDOPERATION_PUBLISHVERSION = 'UnsupportedOperation.PublishVersion'

# This region is not supported.
UNSUPPORTEDOPERATION_REGION = 'UnsupportedOperation.Region'

# Trigger operation is not supported.
UNSUPPORTEDOPERATION_TRIGGER = 'UnsupportedOperation.Trigger'

# The specified configuration is not supported. Please modify and try again.
UNSUPPORTEDOPERATION_UPDATEFUNCTIONEVENTINVOKECONFIG = 'UnsupportedOperation.UpdateFunctionEventInvokeConfig'

# The specified VpcConfig does not exist.
UNSUPPORTEDOPERATION_VPCCONFIG = 'UnsupportedOperation.VpcConfig'
