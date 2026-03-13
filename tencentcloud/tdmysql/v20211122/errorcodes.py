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

# CAM authentication error.
AUTHFAILURE_CAMAUTHERROR = 'AuthFailure.CamAuthError'

# CAM authentication request parameter check failed.
AUTHFAILURE_CHECKCAMAUTHERROR = 'AuthFailure.CheckCamAuthError'

# CAM authentication failure.
AUTHFAILURE_UNAUTHORIZEDOPERATION = 'AuthFailure.UnauthorizedOperation'

# FailedOperation.AddInstanceInfoFailed
FAILEDOPERATION_ADDINSTANCEINFOFAILED = 'FailedOperation.AddInstanceInfoFailed'

# FailedOperation.AuthNoStrategy
FAILEDOPERATION_AUTHNOSTRATEGY = 'FailedOperation.AuthNoStrategy'

# FailedOperation.ClearInstanceInfoFailed
FAILEDOPERATION_CLEARINSTANCEINFOFAILED = 'FailedOperation.ClearInstanceInfoFailed'

# Failed to create the task.
FAILEDOPERATION_CREATEFLOWERROR = 'FailedOperation.CreateFlowError'

# Query instance data failed.
FAILEDOPERATION_DBQUERYINSTANCEERROR = 'FailedOperation.DBQueryInstanceError'

# Failed to update the new instance name.
FAILEDOPERATION_DBUPDATEINSTANCEERROR = 'FailedOperation.DBUpdateInstanceError'

# FailedOperation.DisassociateSecurityGroupsFailed
FAILEDOPERATION_DISASSOCIATESECURITYGROUPSFAILED = 'FailedOperation.DisassociateSecurityGroupsFailed'

# FailedOperation.GetSecurityGroupDetailFailed
FAILEDOPERATION_GETSECURITYGROUPDETAILFAILED = 'FailedOperation.GetSecurityGroupDetailFailed'

# Instance isolation failed.
FAILEDOPERATION_ISOLATEINSTANCEERROR = 'FailedOperation.IsolateInstanceError'

# Failed to lock the instance.
FAILEDOPERATION_LOCKINSTANCEERROR = 'FailedOperation.LockInstanceError'

# Modify backup policy failed.
FAILEDOPERATION_MODIFYBACKUPPOLICYERR = 'FailedOperation.ModifyBackupPolicyErr'

# Modify backup policy failed.
FAILEDOPERATION_MODIFYPOLICYERR = 'FailedOperation.ModifyPolicyErr'

# Oss query parameter error.
FAILEDOPERATION_OSSGETVARIABLESERROR = 'FailedOperation.OssGetVariablesError'

# oss parameter modification error.
FAILEDOPERATION_OSSMODIFYVARIABLESERROR = 'FailedOperation.OssModifyVariablesError'

# Database query error.
FAILEDOPERATION_QUERYDBERROR = 'FailedOperation.QueryDBError'

# FailedOperation.SetRuleLocationFailed
FAILEDOPERATION_SETRULELOCATIONFAILED = 'FailedOperation.SetRuleLocationFailed'

# FailedOperation.UpdateInstanceInfoFailed
FAILEDOPERATION_UPDATEINSTANCEINFOFAILED = 'FailedOperation.UpdateInstanceInfoFailed'

# Database access error.
INTERNALERROR_DATABASEACCESSERROR = 'InternalError.DatabaseAccessError'

# Query database object failed.
INTERNALERROR_DESCRIBEDBOBJECTSERROR = 'InternalError.DescribeDBObjectsError'

# InternalError.GetSecurityGroupDetailFailed
INTERNALERROR_GETSECURITYGROUPDETAILFAILED = 'InternalError.GetSecurityGroupDetailFailed'

# InternalError.InstanceOperatePermissionError
INTERNALERROR_INSTANCEOPERATEPERMISSIONERROR = 'InternalError.InstanceOperatePermissionError'

# InternalError.InstanceSGOverLimitError
INTERNALERROR_INSTANCESGOVERLIMITERROR = 'InternalError.InstanceSGOverLimitError'

# InternalError.ListInstanceRespResourceCountNotMatchError
INTERNALERROR_LISTINSTANCERESPRESOURCECOUNTNOTMATCHERROR = 'InternalError.ListInstanceRespResourceCountNotMatchError'

# InternalError.ListInstancesError
INTERNALERROR_LISTINSTANCESERROR = 'InternalError.ListInstancesError'

# InternalError.QueryDatabaseFailed
INTERNALERROR_QUERYDATABASEFAILED = 'InternalError.QueryDatabaseFailed'

# InternalError.ReadDatabaseFailed
INTERNALERROR_READDATABASEFAILED = 'InternalError.ReadDatabaseFailed'

# InternalError.RouteNotFound
INTERNALERROR_ROUTENOTFOUND = 'InternalError.RouteNotFound'

# Route not found. whether parameter passing is incorrect.
INTERNALERROR_ROUTERNOTFOUND = 'InternalError.RouterNotFound'

# InternalError.SetSvcLocationFailed
INTERNALERROR_SETSVCLOCATIONFAILED = 'InternalError.SetSvcLocationFailed'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# Invalid backup policy parameters.
INVALIDPARAMETER_ILLEGALBACKUPPOLICYPARAMSERR = 'InvalidParameter.IllegalBackupPolicyParamsErr'

# InvalidParameter.IllegalParameterError
INVALIDPARAMETER_ILLEGALPARAMETERERROR = 'InvalidParameter.IllegalParameterError'

# Parameter validation error.
INVALIDPARAMETER_INPUTILLEGAL = 'InvalidParameter.InputIllegal'

# InvalidParameter.InstanceNotFound
INVALIDPARAMETER_INSTANCENOTFOUND = 'InvalidParameter.InstanceNotFound'

# Parameter verification failed.
INVALIDPARAMETER_INVALIDPARAMETERERROR = 'InvalidParameter.InvalidParameterError'

# InvalidParameter.PermissionDenied
INVALIDPARAMETER_PERMISSIONDENIED = 'InvalidParameter.PermissionDenied'

# Parameter value error.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Parameter value is invalid or out of range.
INVALIDPARAMETERVALUE_BIZINVALIDPARAMETERVALUEERROR = 'InvalidParameterValue.BizInvalidParameterValueError'

# Instance version validation error.
INVALIDPARAMETERVALUE_CHECKINSTANCEVERSIONERROR = 'InvalidParameterValue.CheckInstanceVersionError'

# Name verification failed.
INVALIDPARAMETERVALUE_CHECKNAMEERROR = 'InvalidParameterValue.CheckNameError'

# Instance specification validation error.
INVALIDPARAMETERVALUE_CHECKSPECERROR = 'InvalidParameterValue.CheckSpecError'

# Parameter error
INVALIDPARAMETERVALUE_INVALIDPARAMETERVALUEERROR = 'InvalidParameterValue.InvalidParameterValueError'

# Missing parameter error.
MISSINGPARAMETER_MISSINGPARAMETERERROR = 'MissingParameter.MissingParameterError'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# The count of backup tasks created exceeds the threshold.
OPERATIONDENIED_CREATEBACKUPTASKTHRESHOLDERR = 'OperationDenied.CreateBackupTaskThresholdErr'

# The running backup task cannot be deleted.
OPERATIONDENIED_DELETERUNNINGBACKUPTASKERR = 'OperationDenied.DeleteRunningBackupTaskErr'

# Incorrect instance status
OPERATIONDENIED_INSTANCESTATUSERROR = 'OperationDenied.InstanceStatusError'

# The quota for performing manual backup on a single instance per day.
OPERATIONDENIED_MANUALBACKUPQUOTAPERDAYEXCEEDEDERR = 'OperationDenied.ManualBackupQuotaPerDayExceededErr'

# The number of backups exceeds the quota. backups cannot be created again.
OPERATIONDENIED_MANUALBACKUPSETQUOTAEXCEEDEDERR = 'OperationDenied.ManualBackupSetQuotaExceededErr'

# Instance resource not found.
RESOURCENOTFOUND_BIZRESOURCENOTFOUNDERROR = 'ResourceNotFound.BizResourceNotFoundError'

# ResourceNotFound.InstanceNotFound
RESOURCENOTFOUND_INSTANCENOTFOUND = 'ResourceNotFound.InstanceNotFound'

# ResourceNotFound.ProductConfigNotExistedError
RESOURCENOTFOUND_PRODUCTCONFIGNOTEXISTEDERROR = 'ResourceNotFound.ProductConfigNotExistedError'

# ResourceUnavailable.InstanceStatusAbnormal
RESOURCEUNAVAILABLE_INSTANCESTATUSABNORMAL = 'ResourceUnavailable.InstanceStatusAbnormal'

# ResourceUnavailable.SGCheckFail
RESOURCEUNAVAILABLE_SGCHECKFAIL = 'ResourceUnavailable.SGCheckFail'

# UnauthorizedOperation.PermissionDenied
UNAUTHORIZEDOPERATION_PERMISSIONDENIED = 'UnauthorizedOperation.PermissionDenied'
