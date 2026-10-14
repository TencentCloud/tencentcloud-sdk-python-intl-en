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


# CAM signature/authentication error.
AUTHFAILURE = 'AuthFailure'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Failed to call the <apiName> API of the <serviceName> service: <message>.
FAILEDOPERATION_CALLTHIRDPARTAPIERROR = 'FailedOperation.CallThirdPartApiError'

# Failed to create workflow
FAILEDOPERATION_CREATEWORKFLOWFAILED = 'FailedOperation.CreateWorkflowFailed'

# This data source Connection is already associated with an analytical catalog. Each Connection can only create one analytical catalog in the same workspace.
FAILEDOPERATION_DUPLICATEANACATALOG = 'FailedOperation.DuplicateAnaCatalog'

# Existent active workflow is running and cannot operate.
FAILEDOPERATION_EXISTWORKFLOWEXECUTIONS = 'FailedOperation.ExistWorkflowExecutions'

# Number of tags has reached the upper limit.
FAILEDOPERATION_LABELCOUNTLIMIT = 'FailedOperation.LabelCountLimit'

# No operation required for the workflow running
FAILEDOPERATION_NOWORKFLOWEXECUTIONNEEDOPERATE = 'FailedOperation.NoWorkflowExecutionNeedOperate'

# Failed to rerun the workflow
FAILEDOPERATION_RERUNWORKFLOWFAIL = 'FailedOperation.RerunWorkflowFail'

# Failed to run workflow
FAILEDOPERATION_RUNWORKFLOWFAIL = 'FailedOperation.RunWorkflowFail'

# The execution ID returned by running the workflow is empty.
FAILEDOPERATION_RUNWORKFLOWFAILEXECUTIONIDEMPTY = 'FailedOperation.RunWorkflowFailExecutionIdEmpty'

# Internal service error.
FAILEDOPERATION_SERVICEERROR = 'FailedOperation.ServiceError'

# Tencent Cloud SDK request error
FAILEDOPERATION_TENCENTCLOUDSDKERROR = 'FailedOperation.TencentCloudSDKError'

# Failed to update workflow
FAILEDOPERATION_UPDATEWORKFLOWFAILED = 'FailedOperation.UpdateWorkflowFailed'

# This workflow is content deployed through a bundle package. Do not edit this workflow.
FAILEDOPERATION_WORKFLOWBUNDLENOPERMISSION = 'FailedOperation.WorkflowBundleNoPermission'

# Workflow number exceeds the upper limit of 10000.
FAILEDOPERATION_WORKFLOWCOUNTLIMIT = 'FailedOperation.WorkflowCountLimit'

# Failed to obtain the distributed lock for the workflow name.
FAILEDOPERATION_WORKFLOWCREATELOCKACQUIREFAILED = 'FailedOperation.WorkflowCreateLockAcquireFailed'

# Workflow run deleted
FAILEDOPERATION_WORKFLOWEXECUTIONHASBEDELETE = 'FailedOperation.WorkflowExecutionHasBeDelete'

# No operation permissions.
FAILEDOPERATION_WORKFLOWNOPERMISSION = 'FailedOperation.WorkflowNoPermission'

# Internal error.
INTERNALERROR = 'InternalError'

# Business logic error.
INTERNALERROR_BIZEXCEPTION = 'InternalError.BizException'

# Operation failed
INTERNALERROR_FAILEDOPERATION = 'InternalError.FailedOperation'

# API is busy, try again later.
INTERNALERROR_INTERFACECALLERROR = 'InternalError.InterfaceCallError'

# Invalid parameters.
INTERNALERROR_INVALIDPARAMETER = 'InternalError.InvalidParameter'

# InternalError.PermissionDenied
INTERNALERROR_PERMISSIONDENIED = 'InternalError.PermissionDenied'

# InternalError.ResourceNotFound
INTERNALERROR_RESOURCENOTFOUND = 'InternalError.ResourceNotFound'

# Unknown error.
INTERNALERROR_UNKNOWNERROR = 'InternalError.UnknownError'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# Incorrect parameter.
INVALIDPARAMETER_INVALIDPARAMETER = 'InvalidParameter.InvalidParameter'

# Invalid parameter.
INVALIDPARAMETER_INVALIDPARAMSERROR = 'InvalidParameter.InvalidParamsError'

# JWT authentication fail
INVALIDPARAMETER_JWTAUTHFAILURE = 'InvalidParameter.JWTAuthFailure'

# Parameter value error.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Duplicate tasks exist in the same workflow.
INVALIDPARAMETERVALUE_DUPLICATETASKNAMEERROR = 'InvalidParameterValue.DuplicateTaskNameError'

# Parameter error.
INVALIDPARAMETERVALUE_INVALIDPARAMETER = 'InvalidParameterValue.InvalidParameter'

# Invalid filter field Key value in the workflow list.
INVALIDPARAMETERVALUE_LISTWORKFLOWFILTERPARAMERROR = 'InvalidParameterValue.ListWorkflowFilterParamError'

# The number of LoopDataArray elements exceeds the upper limit.
INVALIDPARAMETERVALUE_LOOPDATAARRAYELEMENTCOUNTLIMIT = 'InvalidParameterValue.LoopDataArrayElementCountLimit'

# The LoopDataArray value is not a JSON array literal or a {{var}} placeholder expression.
INVALIDPARAMETERVALUE_LOOPDATAARRAYJSONINVALID = 'InvalidParameterValue.LoopDataArrayJsonInvalid'

# The LoopDataArray value was successfully parsed, but the top-level node is not a JSON array.
INVALIDPARAMETERVALUE_LOOPDATAARRAYNOTJSONARRAY = 'InvalidParameterValue.LoopDataArrayNotJsonArray'

# The LoopDataArray value is not a JSON array literal or a {{var}} placeholder expression.
INVALIDPARAMETERVALUE_LOOPDATAARRAYNOTJSONARRAYLITERAL = 'InvalidParameterValue.LoopDataArrayNotJsonArrayLiteral'

# The LoopDataArray field in the FOR_EACH task is empty or contains only whitespace.
INVALIDPARAMETERVALUE_LOOPDATAARRAYVALUEBLANK = 'InvalidParameterValue.LoopDataArrayValueBlank'

# The string length of the LoopDataArray field in the FOR_EACH task exceeds the upper limit.
INVALIDPARAMETERVALUE_LOOPDATAARRAYVALUELENGTHLIMIT = 'InvalidParameterValue.LoopDataArrayValueLengthLimit'

# The LoopDataArray variable expression fails to satisfy the placeholder syntax (curly brackets must be paired and not nested).
INVALIDPARAMETERVALUE_LOOPDATAARRAYVARIABLEEXPRESSIONINVALID = 'InvalidParameterValue.LoopDataArrayVariableExpressionInvalid'

# Parameter <parameter> cannot be empty.
INVALIDPARAMETERVALUE_PARAMBLANKERROR = 'InvalidParameterValue.ParamBlankError'

# Parameter <parameter> does not meet requirements: <message>
INVALIDPARAMETERVALUE_PARAMILLEGALERROR = 'InvalidParameterValue.ParamIllegalError'

# Parameter <parameter> cannot be null.
INVALIDPARAMETERVALUE_PARAMNULLERROR = 'InvalidParameterValue.ParamNullError'

# Referenced object does not exist or has been deleted
INVALIDPARAMETERVALUE_TASKHOOKVALIDATIONFAILED = 'InvalidParameterValue.TaskHookValidationFailed'

# Task name contains invalid characters
INVALIDPARAMETERVALUE_TASKNAMECONTAINSILLEGALCHARACTERSERROR = 'InvalidParameterValue.TaskNameContainsIllegalCharactersError'

# Task name exceeds the maximum number of characters (128).
INVALIDPARAMETERVALUE_TASKNAMEEXCEEDSLIMITERROR = 'InvalidParameterValue.TaskNameExceedsLimitError'

# Remove the resource group configuration of this task type
INVALIDPARAMETERVALUE_TASKTYPENOTSUPPORTRESOURCEGROUP = 'InvalidParameterValue.TaskTypeNotSupportResourceGroup'

# Task type attribute value is required in input parameters, but it is not transmitted.
INVALIDPARAMETERVALUE_TASKTYPEPROPERTYKEYVALUEREQUESTREQUIREDERROR = 'InvalidParameterValue.TaskTypePropertyKeyValueRequestRequiredError'

# End time cannot be earlier than start time.
INVALIDPARAMETERVALUE_WORKFLOWENDTIMELESSSTARTTIME = 'InvalidParameterValue.WorkflowEndTimeLessStartTime'

# Workflow name already exists.
INVALIDPARAMETERVALUE_WORKFLOWNAMEEXISTS = 'InvalidParameterValue.WorkflowNameExists'

# Invalid workflow name.
INVALIDPARAMETERVALUE_WORKFLOWNAMEINVALID = 'InvalidParameterValue.WorkflowNameInvalid'

# Query time range exceeds the 60-day limit.
INVALIDPARAMETERVALUE_WORKFLOWQUERYENDTIMEANDSTARTTIMEEXCEED = 'InvalidParameterValue.WorkflowQueryEndTimeAndStartTimeExceed'

# Workflow schedule start time cannot be later than end time.
INVALIDPARAMETERVALUE_WORKFLOWSTARTTIMEAFTERENDTIMEERROR = 'InvalidParameterValue.WorkflowStartTimeAfterEndTimeError'

# Please check the advanced configuration of the workflow trigger and fix the illegal JSON content.
INVALIDPARAMETERVALUE_WORKFLOWTRIGGERADVANCEDCONFIGERROR = 'InvalidParameterValue.WorkflowTriggerAdvancedConfigError'

# The maximum number of custom roles has been reached.
LIMITEXCEEDED_CUSTOMROLEQUOTA = 'LimitExceeded.CustomRoleQuota'

# The number of Setats Catalogs in the current tenant has reached the cap (max 5)
LIMITEXCEEDED_SETATSCATALOGLIMITEXCEEDED = 'LimitExceeded.SetatsCatalogLimitExceeded'

# Number of user group members exceeds the workspace space limit.
LIMITEXCEEDED_WORKSPACEGROUPMEMBERQUOTA = 'LimitExceeded.WorkspaceGroupMemberQuota'

# Maximum number of workspace user groups reached.
LIMITEXCEEDED_WORKSPACEGROUPQUOTA = 'LimitExceeded.WorkspaceGroupQuota'

# Maximum number of workspace users reached.
LIMITEXCEEDED_WORKSPACEUSERQUOTA = 'LimitExceeded.WorkspaceUserQuota'

# Parameters are missing.
MISSINGPARAMETER = 'MissingParameter'

# Missing required parameters
MISSINGPARAMETER_MISSINGPARAMETER = 'MissingParameter.MissingParameter'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# Region error
REGIONERROR = 'RegionError'

# Data catalog already exists
RESOURCEINUSE_CATALOGALREADYEXISTS = 'ResourceInUse.CatalogAlreadyExists'

# Schema already exists
RESOURCEINUSE_SCHEMAALREADYEXISTS = 'ResourceInUse.SchemaAlreadyExists'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The specified Catalog does not exist.
RESOURCENOTFOUND_CATALOGNOTFOUND = 'ResourceNotFound.CatalogNotFound'

# Resource does not exist or has been deleted
RESOURCENOTFOUND_ONEFLOWRESOURCENOEXISTERROR = 'ResourceNotFound.OneFlowResourceNoExistError'

# The specified Schema does not exist.
RESOURCENOTFOUND_SCHEMANOTFOUND = 'ResourceNotFound.SchemaNotFound'

# The run does not exist.
RESOURCENOTFOUND_TASKEXECUTIONNOTEXIST = 'ResourceNotFound.TaskExecutionNotExist'

# Workflow run does not exist.
RESOURCENOTFOUND_WORKFLOWEXECUTIONNOTEXIST = 'ResourceNotFound.WorkflowExecutionNotExist'

# Workflow does not exist.
RESOURCENOTFOUND_WORKFLOWNOTEXIST = 'ResourceNotFound.WorkflowNotExist'

# Workflow not found according to the input workflow ID
RESOURCENOTFOUND_WORKFLOWNOTFOUND = 'ResourceNotFound.WorkflowNotFound'

# The task in the workflow does not exist.
RESOURCENOTFOUND_WORKFLOWTASKNOTEXIST = 'ResourceNotFound.WorkflowTaskNotExist'

# Workflow scheduling configuration not found.
RESOURCENOTFOUND_WORKFLOWTRIGGERNOTFOUND = 'ResourceNotFound.WorkflowTriggerNotFound'

# Unknown parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'

# Workflow run has reached the final state and cannot be terminated.
UNSUPPORTEDOPERATION_WORKFLOWEXECUTIONHASREACHEDFINALSTATECANNOTBESTOPPED = 'UnsupportedOperation.WorkflowExecutionHasReachedFinalStateCannotBeStopped'
