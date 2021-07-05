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


# Error with CAM signature/authentication.
AUTHFAILURE = 'AuthFailure'

# The request is not authorized. For more information on the authentication, see the CAM documentation.
AUTHFAILURE_UNAUTHORIZEDOPERATION = 'AuthFailure.UnauthorizedOperation'

# DryRun Operation. It means that the request would have succeeded, but the DryRun parameter was used.
DRYRUNOPERATION = 'DryRunOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Failed to delete the filter rule.
FAILEDOPERATION_ALERTFILTERRULEDELETEFAILED = 'FailedOperation.AlertFilterRuleDeleteFailed'

# Failed to create the alarm policy.
FAILEDOPERATION_ALERTPOLICYCREATEFAILED = 'FailedOperation.AlertPolicyCreateFailed'

# Failed to delete the alarm policy.
FAILEDOPERATION_ALERTPOLICYDELETEFAILED = 'FailedOperation.AlertPolicyDeleteFailed'

# Failed to query the alarm policy.
FAILEDOPERATION_ALERTPOLICYDESCRIBEFAILED = 'FailedOperation.AlertPolicyDescribeFailed'

# Failed to modify the alarm policy.
FAILEDOPERATION_ALERTPOLICYMODIFYFAILED = 'FailedOperation.AlertPolicyModifyFailed'

# Failed to delete the trigger condition.
FAILEDOPERATION_ALERTTRIGGERRULEDELETEFAILED = 'FailedOperation.AlertTriggerRuleDeleteFailed'

# The data table field doesn't exist.
FAILEDOPERATION_DATACOLUMNNOTFOUND = 'FailedOperation.DataColumnNotFound'

# Failed to query the data.
FAILEDOPERATION_DATAQUERYFAILED = 'FailedOperation.DataQueryFailed'

# The data table doesn't exist.
FAILEDOPERATION_DATATABLENOTFOUND = 'FailedOperation.DataTableNotFound'

# Failed to query the database.
FAILEDOPERATION_DBQUERYFAILED = 'FailedOperation.DbQueryFailed'

# Failed to create the database record.
FAILEDOPERATION_DBRECORDCREATEFAILED = 'FailedOperation.DbRecordCreateFailed'

# Failed to delete the database record.
FAILEDOPERATION_DBRECORDDELETEFAILED = 'FailedOperation.DbRecordDeleteFailed'

# Failed to update the database record.
FAILEDOPERATION_DBRECORDUPDATEFAILED = 'FailedOperation.DbRecordUpdateFailed'

# Failed to start the database transaction.
FAILEDOPERATION_DBTRANSACTIONBEGINFAILED = 'FailedOperation.DbTransactionBeginFailed'

# Failed to submit the database transaction.
FAILEDOPERATION_DBTRANSACTIONCOMMITFAILED = 'FailedOperation.DbTransactionCommitFailed'

# Failed to query the service in the request dimension.
FAILEDOPERATION_DIMQUERYREQUESTFAILED = 'FailedOperation.DimQueryRequestFailed'

# The dividend is zero.
FAILEDOPERATION_DIVISIONBYZERO = 'FailedOperation.DivisionByZero'

# Failed to query analysis data.
FAILEDOPERATION_DRUIDQUERYFAILED = 'FailedOperation.DruidQueryFailed'

# The druid table does not exist.
FAILEDOPERATION_DRUIDTABLENOTFOUND = 'FailedOperation.DruidTableNotFound'

# The name already exists.
FAILEDOPERATION_DUPLICATENAME = 'FailedOperation.DuplicateName'

# The service is not enabled and can be used only after being enabled.
FAILEDOPERATION_SERVICENOTENABLED = 'FailedOperation.ServiceNotEnabled'

# Internal error.
INTERNALERROR = 'InternalError'

# Error with the callback.
INTERNALERROR_CALLBACKFAIL = 'InternalError.CallbackFail'

# Error with another dependent API.
INTERNALERROR_DEPENDSAPI = 'InternalError.DependsApi'

# Error with the dependent db.
INTERNALERROR_DEPENDSDB = 'InternalError.DependsDb'

# Error with the dependent mq.
INTERNALERROR_DEPENDSMQ = 'InternalError.DependsMq'

# Execution timed out.
INTERNALERROR_EXETIMEOUT = 'InternalError.ExeTimeout'

# System error.
INTERNALERROR_SYSTEM = 'InternalError.System'

# An error occurred while parsing the task result.
INTERNALERROR_TASKRESULTFORMAT = 'InternalError.TaskResultFormat'

# Invalid parameter.
INVALIDPARAMETER = 'InvalidParameter'

# The task has already been submitted.
INVALIDPARAMETER_DUPTASK = 'InvalidParameter.DupTask'

# Invalid parameter.
INVALIDPARAMETER_INVALIDPARAMETER = 'InvalidParameter.InvalidParameter'

# Invalid parameter.
INVALIDPARAMETER_INVALIDPARAMETERPARAM = 'InvalidParameter.InvalidParameterParam'

# The platform configuration is missing.
INVALIDPARAMETER_MISSAKSK = 'InvalidParameter.MissAKSK'

# Incorrect parameter.
INVALIDPARAMETER_PARAMERROR = 'InvalidParameter.ParamError'

# Error with the platform configuration.
INVALIDPARAMETER_SECRETIDORSECRETKEYERROR = 'InvalidParameter.SecretIdOrSecretKeyError'

# This product doesn't support scan.
INVALIDPARAMETER_UNSUPPORTEDPRODUCT = 'InvalidParameter.UnsupportedProduct'

# The parameter value is incorrect.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The dashboard name already exists.
INVALIDPARAMETERVALUE_DASHBOARDNAMEEXISTS = 'InvalidParameterValue.DashboardNameExists'

# The version does not match.
INVALIDPARAMETERVALUE_VERSIONMISMATCH = 'InvalidParameterValue.VersionMismatch'

# Quota limit is reached.
LIMITEXCEEDED = 'LimitExceeded'

# Quota limit on metrics is reached. Requests containing unregistered metrics are prohibited.
LIMITEXCEEDED_METRICQUOTAEXCEEDED = 'LimitExceeded.MetricQuotaExceeded'

# Missing parameter.
MISSINGPARAMETER = 'MissingParameter'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# The number of requests exceeds the frequency limit.
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# The resource is in use.
RESOURCEINUSE = 'ResourceInUse'

# Insufficient resources.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The resource is not found.
RESOURCENOTFOUND = 'ResourceNotFound'

# The task does not exist.
RESOURCENOTFOUND_NOTEXISTTASK = 'ResourceNotFound.NotExistTask'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# The resources have been sold out.
RESOURCESSOLDOUT = 'ResourcesSoldOut'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Unknown parameter.
UNKNOWNPARAMETER = 'UnknownParameter'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
