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

# Failed to access the CVM.
FAILEDOPERATION_CVMERROR = 'FailedOperation.CVMError'

# Failed to access the Lighthouse instance.
FAILEDOPERATION_LIGHTHOUSEERROR = 'FailedOperation.LighthouseError'

# Internal error.
INTERNALERROR = 'InternalError'

# Invalid parameter.
INVALIDPARAMETER = 'InvalidParameter'

# Conflicting parameters.
INVALIDPARAMETER_CONFLICTPARAMETER = 'InvalidParameter.ConflictParameter'

# Invalid username.
INVALIDPARAMETER_INVALIDUSERNAME = 'InvalidParameter.InvalidUsername'

# Invalid parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# TAT Agent does not support this command type.
INVALIDPARAMETERVALUE_AGENTUNSUPPORTEDCOMMANDTYPE = 'InvalidParameterValue.AgentUnsupportedCommandType'

# Invalid command content.
INVALIDPARAMETERVALUE_COMMANDCONTENTINVALID = 'InvalidParameterValue.CommandContentInvalid'

# Duplicate command name.
INVALIDPARAMETERVALUE_COMMANDNAMEDUPLICATED = 'InvalidParameterValue.CommandNameDuplicated'

# Inconsistent instance type.
INVALIDPARAMETERVALUE_INCONSISTENTINSTANCE = 'InvalidParameterValue.InconsistentInstance'

# The instance with this ID has no such execution activity.
INVALIDPARAMETERVALUE_INSTANCEISNOTRELATEDTOINVOCATION = 'InvalidParameterValue.InstanceIsNotRelatedToInvocation'

# Invalid CommandId.
INVALIDPARAMETERVALUE_INVALIDCOMMANDID = 'InvalidParameterValue.InvalidCommandId'

# Invalid command name.
INVALIDPARAMETERVALUE_INVALIDCOMMANDNAME = 'InvalidParameterValue.InvalidCommandName'

# Invalid command.
INVALIDPARAMETERVALUE_INVALIDCONTENT = 'InvalidParameterValue.InvalidContent'

# Invalid crontab expression.
INVALIDPARAMETERVALUE_INVALIDCRONEXPRESSION = 'InvalidParameterValue.InvalidCronExpression'

# Invalid filter.
INVALIDPARAMETERVALUE_INVALIDFILTER = 'InvalidParameterValue.InvalidFilter'

# Invalid instance ID.
INVALIDPARAMETERVALUE_INVALIDINSTANCEID = 'InvalidParameterValue.InvalidInstanceId'

# Invalid execution activity ID.
INVALIDPARAMETERVALUE_INVALIDINVOCATIONID = 'InvalidParameterValue.InvalidInvocationId'

# Invalid execution task ID.
INVALIDPARAMETERVALUE_INVALIDINVOCATIONTASKID = 'InvalidParameterValue.InvalidInvocationTaskId'

# Invalid InvokerId.
INVALIDPARAMETERVALUE_INVALIDINVOKERID = 'InvalidParameterValue.InvalidInvokerId'

# Invalid OutputCOSBucketUrl.
INVALIDPARAMETERVALUE_INVALIDOUTPUTCOSBUCKETURL = 'InvalidParameterValue.InvalidOutputCOSBucketUrl'

# Invalid OutputCOSKeyPrefix.
INVALIDPARAMETERVALUE_INVALIDOUTPUTCOSKEYPREFIX = 'InvalidParameterValue.InvalidOutputCOSKeyPrefix'

# Invalid command execution path.
INVALIDPARAMETERVALUE_INVALIDWORKINGDIRECTORY = 'InvalidParameterValue.InvalidWorkingDirectory'

# The custom parameter feature is enabled, but custom parameters are missing.
INVALIDPARAMETERVALUE_LACKOFPARAMETERINFO = 'InvalidParameterValue.LackOfParameterInfo'

# Parameters not provided.
INVALIDPARAMETERVALUE_LACKOFPARAMETERS = 'InvalidParameterValue.LackOfParameters'

# Parameter limit exceeded.
INVALIDPARAMETERVALUE_LIMITEXCEEDED = 'InvalidParameterValue.LimitExceeded'

# The custom parameter feature is not enabled.
INVALIDPARAMETERVALUE_PARAMETERDISABLED = 'InvalidParameterValue.ParameterDisabled'

# The parameter is not a valid JSON string.
INVALIDPARAMETERVALUE_PARAMETERINVALIDJSONFORMAT = 'InvalidParameterValue.ParameterInvalidJsonFormat'

# The parameter key contains invalid characters.
INVALIDPARAMETERVALUE_PARAMETERKEYCONTAINSINVALIDCHAR = 'InvalidParameterValue.ParameterKeyContainsInvalidChar'

# Duplicate parameter keys.
INVALIDPARAMETERVALUE_PARAMETERKEYDUPLICATED = 'InvalidParameterValue.ParameterKeyDuplicated'

# The parameter key is too long.
INVALIDPARAMETERVALUE_PARAMETERKEYLENEXCEEDED = 'InvalidParameterValue.ParameterKeyLenExceeded'

# Too many parameters.
INVALIDPARAMETERVALUE_PARAMETERNUMBEREXCEEDED = 'InvalidParameterValue.ParameterNumberExceeded'

# The parameter value is not a string.
INVALIDPARAMETERVALUE_PARAMETERVALUENOTSTRING = 'InvalidParameterValue.ParameterValueNotString'

# The parameter value is not in the valid range.
INVALIDPARAMETERVALUE_RANGE = 'InvalidParameterValue.Range'

# The custom parameter feature is not enabled.
INVALIDPARAMETERVALUE_SUPPORTPARAMETERSONLYIFENABLEPARAMETER = 'InvalidParameterValue.SupportParametersOnlyIfEnableParameter'

# Length limit exceeded.
INVALIDPARAMETERVALUE_TOOLONG = 'InvalidParameterValue.TooLong'

# Reached the quota limit.
LIMITEXCEEDED = 'LimitExceeded'

# Missing parameter.
MISSINGPARAMETER = 'MissingParameter'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The command does not exist.
RESOURCENOTFOUND_COMMANDNOTFOUND = 'ResourceNotFound.CommandNotFound'

# The instance does not exist.
RESOURCENOTFOUND_INSTANCENOTFOUND = 'ResourceNotFound.InstanceNotFound'

# No execution activity found.
RESOURCENOTFOUND_INVOCATIONNOTFOUND = 'ResourceNotFound.InvocationNotFound'

# TAT Agent is not installed.
RESOURCEUNAVAILABLE_AGENTNOTINSTALLED = 'ResourceUnavailable.AgentNotInstalled'

# TAT Agent is offline.
RESOURCEUNAVAILABLE_AGENTSTATUSNOTONLINE = 'ResourceUnavailable.AgentStatusNotOnline'

# The command is being executed.
RESOURCEUNAVAILABLE_COMMANDINEXECUTING = 'ResourceUnavailable.CommandInExecuting'

# The command has been bound to an invoker.
RESOURCEUNAVAILABLE_COMMANDININVOKER = 'ResourceUnavailable.CommandInInvoker'

# The instance is not running.
RESOURCEUNAVAILABLE_INSTANCESTATENOTRUNNING = 'ResourceUnavailable.InstanceStateNotRunning'

# CAM authentication failed.
UNAUTHORIZEDOPERATION_CAMAUTHFAILED = 'UnauthorizedOperation.CamAuthFailed'

# Invalid token.
UNAUTHORIZEDOPERATION_INVALIDTOKEN = 'UnauthorizedOperation.InvalidToken'

# The Multi-factor authentication (MFA) code expired.
UNAUTHORIZEDOPERATION_MFAEXPIRED = 'UnauthorizedOperation.MFAExpired'

# Multi-factor authentication (MFA) does not exist.
UNAUTHORIZEDOPERATION_MFANOTFOUND = 'UnauthorizedOperation.MFANotFound'

# Unknown parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'
