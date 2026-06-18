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

# Whitelist authentication error occurred.
AUTHFAILURE_UINWHITELISTCHECKERROR = 'AuthFailure.UinWhiteListCheckError'

# CAM authentication failure.
AUTHFAILURE_UNAUTHORIZEDOPERATION = 'AuthFailure.UnauthorizedOperation'

# Failed to bind the tag.
DRYRUNOPERATION_ADDTAGDRYRUNERROR = 'DryRunOperation.AddTagDryrunError'

# FailedOperation.AddInstanceInfoFailed
FAILEDOPERATION_ADDINSTANCEINFOFAILED = 'FailedOperation.AddInstanceInfoFailed'

# FailedOperation.ApplyVipFailed
FAILEDOPERATION_APPLYVIPFAILED = 'FailedOperation.ApplyVipFailed'

# FailedOperation.AuthNoStrategy
FAILEDOPERATION_AUTHNOSTRATEGY = 'FailedOperation.AuthNoStrategy'

# The current instance version does not support this API.
FAILEDOPERATION_CHECKSUPPORTACTIONERROR = 'FailedOperation.CheckSupportActionError'

# FailedOperation.ClearInstanceInfoFailed
FAILEDOPERATION_CLEARINSTANCEINFOFAILED = 'FailedOperation.ClearInstanceInfoFailed'

# Failed to create the task.
FAILEDOPERATION_CREATEFLOWERROR = 'FailedOperation.CreateFlowError'

# Failed to add instance data.
FAILEDOPERATION_DBCREATEINSTANCEERROR = 'FailedOperation.DBCreateInstanceError'

# Query instance data failed.
FAILEDOPERATION_DBQUERYINSTANCEERROR = 'FailedOperation.DBQueryInstanceError'

# Query user permission error.
FAILEDOPERATION_DBQUERYPRIVILEGESERROR = 'FailedOperation.DBQueryPrivilegesError'

# Failed to query instance data bound to tags.
FAILEDOPERATION_DBQUERYTAGERROR = 'FailedOperation.DBQueryTagError'

# Query user data failed.
FAILEDOPERATION_DBQUERYUSERERROR = 'FailedOperation.DBQueryUserError'

# Query Available Sale Zones failed.
FAILEDOPERATION_DBQUERYZONEERROR = 'FailedOperation.DBQueryZoneError'

# Failed to update the new instance name.
FAILEDOPERATION_DBUPDATEINSTANCEERROR = 'FailedOperation.DBUpdateInstanceError'

# Failed to update user data.
FAILEDOPERATION_DBUPDATEUSERERROR = 'FailedOperation.DBUpdateUserError'

# Failed to update and maintain window configuration
FAILEDOPERATION_DBUPSERTMAINTENANCEWINDOWERROR = 'FailedOperation.DBUpsertMaintenanceWindowError'

# The number of DBs has exceeded the limit.
FAILEDOPERATION_DBCOUNTLIMITERROR = 'FailedOperation.DbCountLimitError'

# Querying full backup list error.
FAILEDOPERATION_DESCRIBEFULLBACKUPLISTERROR = 'FailedOperation.DescribeFullBackupListError'

# FailedOperation.DisassociateSecurityGroupsFailed
FAILEDOPERATION_DISASSOCIATESECURITYGROUPSFAILED = 'FailedOperation.DisassociateSecurityGroupsFailed'

# Instance scale-out failed.
FAILEDOPERATION_EXPANDINSTANCEERROR = 'FailedOperation.ExpandInstanceError'

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

# Query user failed.
FAILEDOPERATION_QUERYUSERERROR = 'FailedOperation.QueryUserError'

# FailedOperation.SetRuleLocationFailed
FAILEDOPERATION_SETRULELOCATIONFAILED = 'FailedOperation.SetRuleLocationFailed'

# The number of tables has exceeded the limit.
FAILEDOPERATION_TABLECOUNTLIMITERROR = 'FailedOperation.TableCountLimitError'

# FailedOperation.UpdateInstanceInfoFailed
FAILEDOPERATION_UPDATEINSTANCEINFOFAILED = 'FailedOperation.UpdateInstanceInfoFailed'

# Update permission error.
FAILEDOPERATION_UPDATEPRIVILEGESERROR = 'FailedOperation.UpdatePrivilegesError'

# FailedOperation.WanStatusAbnormal
FAILEDOPERATION_WANSTATUSABNORMAL = 'FailedOperation.WanStatusAbnormal'

# InternalError.CheckVipStatusFailed
INTERNALERROR_CHECKVIPSTATUSFAILED = 'InternalError.CheckVipStatusFailed'

# Database access error.
INTERNALERROR_DATABASEACCESSERROR = 'InternalError.DatabaseAccessError'

# InternalError.DbOperationFailed
INTERNALERROR_DBOPERATIONFAILED = 'InternalError.DbOperationFailed'

# Query database object failed.
INTERNALERROR_DESCRIBEDBOBJECTSERROR = 'InternalError.DescribeDBObjectsError'

# InternalError.GetSecurityGroupDetailFailed
INTERNALERROR_GETSECURITYGROUPDETAILFAILED = 'InternalError.GetSecurityGroupDetailFailed'

# InternalError.GetSubnetFailed
INTERNALERROR_GETSUBNETFAILED = 'InternalError.GetSubnetFailed'

# InternalError.GetVpcFailed
INTERNALERROR_GETVPCFAILED = 'InternalError.GetVpcFailed'

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

# InternalError.VpcOperationFailed
INTERNALERROR_VPCOPERATIONFAILED = 'InternalError.VpcOperationFailed'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# Parameter error in creating an instance.
INVALIDPARAMETER_CREATEINSTANCEPARAMERROR = 'InvalidParameter.CreateInstanceParamError'

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

# InvalidParameter.SubnetUnavailable
INVALIDPARAMETER_SUBNETUNAVAILABLE = 'InvalidParameter.SubnetUnavailable'

# InvalidParameter.VipNotInSubnet
INVALIDPARAMETER_VIPNOTINSUBNET = 'InvalidParameter.VipNotInSubnet'

# InvalidParameter.VipUsed
INVALIDPARAMETER_VIPUSED = 'InvalidParameter.VipUsed'

# Parameter value error.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Parameter value is invalid or out of range.
INVALIDPARAMETERVALUE_BIZINVALIDPARAMETERVALUEERROR = 'InvalidParameterValue.BizInvalidParameterValueError'

# Query disk size error.
INVALIDPARAMETERVALUE_CHECKCLONEINSTANCEDISKERROR = 'InvalidParameterValue.CheckCloneInstanceDiskError'

# Disk size validation error.
INVALIDPARAMETERVALUE_CHECKDISKERROR = 'InvalidParameterValue.CheckDiskError'

# host verification failed.
INVALIDPARAMETERVALUE_CHECKHOSTERROR = 'InvalidParameterValue.CheckHostError'

# Instance version validation error.
INVALIDPARAMETERVALUE_CHECKINSTANCEVERSIONERROR = 'InvalidParameterValue.CheckInstanceVersionError'

# Name verification failed.
INVALIDPARAMETERVALUE_CHECKNAMEERROR = 'InvalidParameterValue.CheckNameError'

# Password verification failed.
INVALIDPARAMETERVALUE_CHECKPASSWDERROR = 'InvalidParameterValue.CheckPasswdError'

# Instance specification validation error.
INVALIDPARAMETERVALUE_CHECKSPECERROR = 'InvalidParameterValue.CheckSpecError'

# VPC validation error.
INVALIDPARAMETERVALUE_CHECKVPCERROR = 'InvalidParameterValue.CheckVpcError'

# Filter parameter error in the instance.
INVALIDPARAMETERVALUE_INSTANCEFILTERKEYERROR = 'InvalidParameterValue.InstanceFilterKeyError'

# Parameter error
INVALIDPARAMETERVALUE_INVALIDPARAMETERVALUEERROR = 'InvalidParameterValue.InvalidParameterValueError'

# Parameter verification failure for maintenance window
INVALIDPARAMETERVALUE_MAINTENANCEWINDOWPARAMERROR = 'InvalidParameterValue.MaintenanceWindowParamError'

# The number of instance replicas created does not meet specifications.
INVALIDPARAMETERVALUE_NODEREPLICASINVALIDERROR = 'InvalidParameterValue.NodeReplicasInvalidError'

# Vport range error.
INVALIDPARAMETERVALUE_VPORTRANGEERROR = 'InvalidParameterValue.VportRangeError'

# The number of bound tags exceeds the limit.
LIMITEXCEEDED_ADDTAGCOUNTERROR = 'LimitExceeded.AddTagCountError'

# The number of batch create instances exceeds the limit.
LIMITEXCEEDED_OUTOFINSTANCECNTLIMITERROR = 'LimitExceeded.OutOfInstanceCntLimitError'

# The count of pull instances exceeds the limit.
LIMITEXCEEDED_OUTOFINSTANCECOUNTLIMITERROR = 'LimitExceeded.OutOfInstanceCountLimitError'

# The specification exceeds the limit.
LIMITEXCEEDED_OUTOFLIMITERROR = 'LimitExceeded.OutOfLimitError'

# The number of replicas exceeds the limit.
LIMITEXCEEDED_OUTOFNODEREPLICASLIMITERROR = 'LimitExceeded.OutOfNodeReplicasLimitError'

# The specification exceeds the limit.
LIMITEXCEEDED_OUTOFSPECLIMITERROR = 'LimitExceeded.OutOfSpecLimitError'

# Missing parameter error.
MISSINGPARAMETER_MISSINGPARAMETERERROR = 'MissingParameter.MissingParameterError'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# Instance specification scale-in is not currently supported.
OPERATIONDENIED_CHECKDECREASESPECERROR = 'OperationDenied.CheckDecreaseSpecError'

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

# Reset super user password failed.
OPERATIONDENIED_RESETUSERPASSWORDERROR = 'OperationDenied.ResetUserPasswordError'

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

# Error retrieving maximum node count.
UNSUPPORTEDOPERATION_GETMAXNODENUMERROR = 'UnsupportedOperation.GetMaxNodeNumError'
