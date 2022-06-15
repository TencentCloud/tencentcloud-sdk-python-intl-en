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


# CAM signature/authentication error
AUTHFAILURE = 'AuthFailure'

# Failed to add the security group information of an instance.
FAILEDOPERATION_ADDINSTANCEINFOFAILED = 'FailedOperation.AddInstanceInfoFailed'

# Failed to associate the security group.
FAILEDOPERATION_ASSOCIATESECURITYGROUPSFAILED = 'FailedOperation.AssociateSecurityGroupsFailed'

# Authentication failed.
FAILEDOPERATION_AUTHNOSTRATEGY = 'FailedOperation.AuthNoStrategy'

# Failed to clear the security group information of an instance.
FAILEDOPERATION_CLEARINSTANCEINFOFAILED = 'FailedOperation.ClearInstanceInfoFailed'

# Error copying account permissions.
FAILEDOPERATION_COPYRIGHTERROR = 'FailedOperation.CopyRightError'

# Failed to create the flow.
FAILEDOPERATION_CREATEFLOWFAILED = 'FailedOperation.CreateFlowFailed'

# Failed to create an order.
FAILEDOPERATION_CREATEORDERFAILED = 'FailedOperation.CreateOrderFailed'

# Failed to create the account.
FAILEDOPERATION_CREATEUSERFAILED = 'FailedOperation.CreateUserFailed'

# Failed to delete the account.
FAILEDOPERATION_DELETEUSERFAILED = 'FailedOperation.DeleteUserFailed'

# Failed to unassociate the security group.
FAILEDOPERATION_DISASSOCIATESECURITYGROUPSFAILED = 'FailedOperation.DisassociateSecurityGroupsFailed'

# Failed to modify account permissions.
FAILEDOPERATION_MODIFYRIGHTFAILED = 'FailedOperation.ModifyRightFailed'

# Failed to request the backend API.
FAILEDOPERATION_OSSOPERATIONFAILED = 'FailedOperation.OssOperationFailed'

# Failed to reset the account password.
FAILEDOPERATION_RESETPASSWORDFAILED = 'FailedOperation.ResetPasswordFailed'

# Failed to set a rule.
FAILEDOPERATION_SETRULELOCATIONFAILED = 'FailedOperation.SetRuleLocationFailed'

# Either tag key/value verification or tag API authentication failed.
FAILEDOPERATION_TAGDRYRUNERROR = 'FailedOperation.TagDryRunError'

# Failed to update the security group information of an instance.
FAILEDOPERATION_UPDATEINSTANCEINFOFAILED = 'FailedOperation.UpdateInstanceInfoFailed'

# Unverified user.
FAILEDOPERATION_USERNOTAUTHED = 'FailedOperation.UserNotAuthed'

# Internal error.
INTERNALERROR = 'InternalError'

# CAM authentication request failed.
INTERNALERROR_CAMAUTHFAILED = 'InternalError.CamAuthFailed'

# Invalid COS instance address configuration.
INTERNALERROR_COSCONFIGURATION = 'InternalError.CosConfiguration'

# Backup filename signature failed.
INTERNALERROR_COSSIGNURL = 'InternalError.CosSignUrl'

# No database data has changed.
INTERNALERROR_DBROWSAFFECTEDERROR = 'InternalError.DBRowsAffectedError'

# Failed to query the database.
INTERNALERROR_DBOPERATIONFAILED = 'InternalError.DbOperationFailed'

# Failed to query the information of a dedicated cluster.
INTERNALERROR_FENCEERROR = 'InternalError.FenceError'

# Failed to get database instance parameters.
INTERNALERROR_GETDBCONFIGFAILED = 'InternalError.GetDbConfigFailed'

# Failed to get database list.
INTERNALERROR_GETDBLISTFAILED = 'InternalError.GetDbListFailed'

# Failed to get the database objects.
INTERNALERROR_GETDBOBJECTFAILED = 'InternalError.GetDbObjectFailed'

# Failed to get the instance details.
INTERNALERROR_GETINSTANCEDETAILFAILED = 'InternalError.GetInstanceDetailFailed'

# Failed to get the instance information.
INTERNALERROR_GETINSTANCEINFOFAILED = 'InternalError.GetInstanceInfoFailed'

# Failed to get the current permissions of the account.
INTERNALERROR_GETRIGHTFAILED = 'InternalError.GetRightFailed'

# Failed to query security group details.
INTERNALERROR_GETSECURITYGROUPDETAILFAILED = 'InternalError.GetSecurityGroupDetailFailed'

# Failed to query slow query logs.
INTERNALERROR_GETSLOWLOGFAILED = 'InternalError.GetSlowLogFailed'

# Failed to query the VPC subnet information.
INTERNALERROR_GETSUBNETFAILED = 'InternalError.GetSubnetFailed'

# Failed to get the table information.
INTERNALERROR_GETTABLEINFOFAILED = 'InternalError.GetTableInfoFailed'

# Failed to get the list of accounts.
INTERNALERROR_GETUSERLISTFAILED = 'InternalError.GetUserListFailed'

# Failed to query the security group quota of the user.
INTERNALERROR_GETUSGQUOTAERROR = 'InternalError.GetUsgQuotaError'

# Failed to query the VPC information.
INTERNALERROR_GETVPCFAILED = 'InternalError.GetVpcFailed'

# Internal system error.
INTERNALERROR_INNERSYSTEMERROR = 'InternalError.InnerSystemError'

# Failed to insert data into the database.
INTERNALERROR_INSERTFAIL = 'InternalError.InsertFail'

# You have no permission to operate this instance.
INTERNALERROR_INSTANCEOPERATEPERMISSIONERROR = 'InternalError.InstanceOperatePermissionError'

# The maximum number of security groups with which a single instance can associate has been reached.
INTERNALERROR_INSTANCESGOVERLIMITERROR = 'InternalError.InstanceSGOverLimitError'

# The number of resources returned is inconsistent with the number specified in the request of querying instance information.
INTERNALERROR_LISTINSTANCERESPRESOURCECOUNTNOTMATCHERROR = 'InternalError.ListInstanceRespResourceCountNotMatchError'

# An error occurred when querying instance information.
INTERNALERROR_LISTINSTANCESERROR = 'InternalError.ListInstancesError'

# Database operation failed.
INTERNALERROR_OPERATEDATABASEFAILED = 'InternalError.OperateDatabaseFailed'

# An error occurred when reading data from the database.
INTERNALERROR_QUERYDATABASEFAILED = 'InternalError.QueryDatabaseFailed'

# Failed to query the order information.
INTERNALERROR_QUERYORDERFAILED = 'InternalError.QueryOrderFailed'

# An error occurred when reading data from the database.
INTERNALERROR_READDATABASEFAILED = 'InternalError.ReadDatabaseFailed'

# Route not found.
INTERNALERROR_ROUTENOTFOUND = 'InternalError.RouteNotFound'

# The security group policy of the resource failed to take effect.
INTERNALERROR_SETSVCLOCATIONFAILED = 'InternalError.SetSvcLocationFailed'

# Failed to update the database.
INTERNALERROR_UPDATEDATABASEFAILED = 'InternalError.UpdateDatabaseFailed'

# Public network operation failed.
INTERNALERROR_WANSERVICEFAILED = 'InternalError.WanServiceFailed'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# The password contains invalid characters.
INVALIDPARAMETER_CHARACTERERROR = 'InvalidParameter.CharacterError'

# Failed to verify input parameters.
INVALIDPARAMETER_CHECKPARAMNOTPASS = 'InvalidParameter.CheckParamNotPass'

# The order ID to be queried is not specified.
INVALIDPARAMETER_DEALNAMENOTGIVEN = 'InvalidParameter.DealNameNotGiven'

# The specified task information was not found.
INVALIDPARAMETER_FLOWNOTFOUND = 'InvalidParameter.FlowNotFound'

# An error occurred while verifying parameter validity.
INVALIDPARAMETER_GENERICPARAMETERERROR = 'InvalidParameter.GenericParameterError'

# Invalid parameters.
INVALIDPARAMETER_ILLEGALPARAMETERERROR = 'InvalidParameter.IllegalParameterError'

# Incorrect time parameter.
INVALIDPARAMETER_ILLEGALTIME = 'InvalidParameter.IllegalTime'

# Failed to find the requested instance.
INVALIDPARAMETER_INSTANCENOTFOUND = 'InvalidParameter.InstanceNotFound'

# You have no permission to manipulate this API or resource.
INVALIDPARAMETER_PERMISSIONDENIED = 'InvalidParameter.PermissionDenied'

# Security group validity test failed.
INVALIDPARAMETER_SGCHECKFAIL = 'InvalidParameter.SGCheckFail'

# The specified VPC subnet was not found.
INVALIDPARAMETER_SUBNETNOTFOUND = 'InvalidParameter.SubnetNotFound'

# The specified VPC was not found.
INVALIDPARAMETER_VPCNOTFOUND = 'InvalidParameter.VpcNotFound'

# Incorrect AZ information.
INVALIDPARAMETER_ZONEIDILLEGAL = 'InvalidParameter.ZoneIdIllegal'

# The account to be created already exists.
INVALIDPARAMETERVALUE_ACCOUNTALREADYEXISTS = 'InvalidParameterValue.AccountAlreadyExists'

# The instance does not support this sync mode.
INVALIDPARAMETERVALUE_BADSYNCMODE = 'InvalidParameterValue.BadSyncMode'

# The specified permission could not be granted to this account.
INVALIDPARAMETERVALUE_BADUSERRIGHT = 'InvalidParameterValue.BadUserRight'

# Invalid account type.
INVALIDPARAMETERVALUE_BADUSERTYPE = 'InvalidParameterValue.BadUserType'

# The dedicated cluster to which the database instance belongs was not found.
INVALIDPARAMETERVALUE_ILLEGALEXCLUSTERID = 'InvalidParameterValue.IllegalExclusterID'

# An error occurred while initializing database instance parameters.
INVALIDPARAMETERVALUE_ILLEGALINITPARAM = 'InvalidParameterValue.IllegalInitParam'

# Incorrect permission parameter
INVALIDPARAMETERVALUE_ILLEGALRIGHTPARAM = 'InvalidParameterValue.IllegalRightParam'

# The specified AZ was not found.
INVALIDPARAMETERVALUE_ILLEGALZONE = 'InvalidParameterValue.IllegalZone'

# The specification information of the database instance was not found.
INVALIDPARAMETERVALUE_SPECIDILLEGAL = 'InvalidParameterValue.SpecIdIllegal'

# Operations by a system user are not allowed.
INVALIDPARAMETERVALUE_SUPERUSERFORBIDDEN = 'InvalidParameterValue.SuperUserForbidden'

# The specified account does not exist.
RESOURCENOTFOUND_ACCOUNTDOESNOTEXIST = 'ResourceNotFound.AccountDoesNotExist'

# The instance doesn’t exist.
RESOURCENOTFOUND_INSTANCENOTFOUND = 'ResourceNotFound.InstanceNotFound'

# The specified database instance was not found.
RESOURCENOTFOUND_NOINSTANCEFOUND = 'ResourceNotFound.NoInstanceFound'

# Failed to find the configuration of the product associated with the security group.
RESOURCENOTFOUND_PRODUCTCONFIGNOTEXISTEDERROR = 'ResourceNotFound.ProductConfigNotExistedError'

# Incorrect instance status. Unable to initialize.
RESOURCEUNAVAILABLE_BADINSTANCESTATUS = 'ResourceUnavailable.BadInstanceStatus'

# An error occurred while calling COS APIs.
RESOURCEUNAVAILABLE_COSAPIFAILED = 'ResourceUnavailable.CosApiFailed'

# The database instance has been dropped.
RESOURCEUNAVAILABLE_INSTANCEALREADYDELETED = 'ResourceUnavailable.InstanceAlreadyDeleted'

# The database instance has been locked. Operations are not allowed.
RESOURCEUNAVAILABLE_INSTANCEHASBEENLOCKED = 'ResourceUnavailable.InstanceHasBeenLocked'

# Incorrect database instance status. Operations are not allowed.
RESOURCEUNAVAILABLE_INSTANCESTATUSABNORMAL = 'ResourceUnavailable.InstanceStatusAbnormal'

# You have no permission to manipulate this API or resource.
UNAUTHORIZEDOPERATION_PERMISSIONDENIED = 'UnauthorizedOperation.PermissionDenied'

# Unsupported operation.
UNSUPPORTEDOPERATION_INVALIDOPERATION = 'UnsupportedOperation.InvalidOperation'

# The proxy program is too old. Please contact customer service for upgrade and try again.
UNSUPPORTEDOPERATION_OLDPROXYVERSION = 'UnsupportedOperation.OldProxyVersion'
