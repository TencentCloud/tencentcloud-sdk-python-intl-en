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

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Failed to add the security group information of an instance.
FAILEDOPERATION_ADDINSTANCEINFOFAILED = 'FailedOperation.AddInstanceInfoFailed'

# Failed to apply for VIP
FAILEDOPERATION_APPLYVIPFAILED = 'FailedOperation.ApplyVipFailed'

# Failed to associate the security group.
FAILEDOPERATION_ASSOCIATESECURITYGROUPSFAILED = 'FailedOperation.AssociateSecurityGroupsFailed'

# Authentication failed.
FAILEDOPERATION_AUTHNOSTRATEGY = 'FailedOperation.AuthNoStrategy'

# Failed to clear the security group information of an instance.
FAILEDOPERATION_CLEARINSTANCEINFOFAILED = 'FailedOperation.ClearInstanceInfoFailed'

# An error occurred while copying account permissions.
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

# Failed to query the security group details
FAILEDOPERATION_GETSECURITYGROUPDETAILFAILED = 'FailedOperation.GetSecurityGroupDetailFailed'

# Refund is not supported for the instance
FAILEDOPERATION_INSTANCECANNOTRETURN = 'FailedOperation.InstanceCanNotReturn'

# Instance refund failed
FAILEDOPERATION_INSTANCERETURNFAILED = 'FailedOperation.InstanceReturnFailed'

# Failed to modify account permissions.
FAILEDOPERATION_MODIFYRIGHTFAILED = 'FailedOperation.ModifyRightFailed'

# Failed to isolate the instance
FAILEDOPERATION_OSSISOLATEINSTANCEFAILED = 'FailedOperation.OssIsolateInstanceFailed'

# Failed to request the backend API.
FAILEDOPERATION_OSSOPERATIONFAILED = 'FailedOperation.OssOperationFailed'

# Failed to make order payment.
FAILEDOPERATION_PAYFAILED = 'FailedOperation.PayFailed'

# Failed to reset the account password.
FAILEDOPERATION_RESETPASSWORDFAILED = 'FailedOperation.ResetPasswordFailed'

# Failed to update the security group
FAILEDOPERATION_SGCHANGEVIP = 'FailedOperation.SGChangeVip'

# Failed to set a rule.
FAILEDOPERATION_SETRULELOCATIONFAILED = 'FailedOperation.SetRuleLocationFailed'

# Failed to publish security group rules
FAILEDOPERATION_SETSVCLOCATIONFAILED = 'FailedOperation.SetSvcLocationFailed'

# Either tag key/value verification or tag API authentication failed.
FAILEDOPERATION_TAGDRYRUNERROR = 'FailedOperation.TagDryRunError'

# Failed to update the security group information of an instance.
FAILEDOPERATION_UPDATEINSTANCEINFOFAILED = 'FailedOperation.UpdateInstanceInfoFailed'

# Unauthenticated user
FAILEDOPERATION_USERNOTAUTHED = 'FailedOperation.UserNotAuthed'

# VIP can’t be the same.
FAILEDOPERATION_VIPNOTCHANGE = 'FailedOperation.VipNotChange'

# Failed to add service to VPC
FAILEDOPERATION_VPCADDSERVICEFAILED = 'FailedOperation.VpcAddServiceFailed'

# Abnormal public network status
FAILEDOPERATION_WANSTATUSABNORMAL = 'FailedOperation.WanStatusAbnormal'

# Internal error.
INTERNALERROR = 'InternalError'

# CAM authentication request failed.
INTERNALERROR_CAMAUTHFAILED = 'InternalError.CamAuthFailed'

# Failed to verify the VIP status
INTERNALERROR_CHECKVIPSTATUSFAILED = 'InternalError.CheckVipStatusFailed'

# Invalid COS address configuration.
INTERNALERROR_COSCONFIGURATION = 'InternalError.CosConfiguration'

# Backup file signature failed.
INTERNALERROR_COSSIGNURL = 'InternalError.CosSignUrl'

# Failed to create a task.
INTERNALERROR_CREATEFLOWFAILED = 'InternalError.CreateFlowFailed'

# No database data has changed.
INTERNALERROR_DBROWSAFFECTEDERROR = 'InternalError.DBRowsAffectedError'

# Failed to query the database.
INTERNALERROR_DBOPERATIONFAILED = 'InternalError.DbOperationFailed'

# Failed to query the information of a dedicated cluster.
INTERNALERROR_FENCEERROR = 'InternalError.FenceError'

# Failed to get the database encryption key
INTERNALERROR_GETCIPHERTEXTFAILED = 'InternalError.GetCipherTextFailed'

# Failed to get database instance parameters.
INTERNALERROR_GETDBCONFIGFAILED = 'InternalError.GetDbConfigFailed'

# Failed to get the database list.
INTERNALERROR_GETDBLISTFAILED = 'InternalError.GetDbListFailed'

# Failed to get the database object.
INTERNALERROR_GETDBOBJECTFAILED = 'InternalError.GetDbObjectFailed'

# Failed to get the instance details.
INTERNALERROR_GETINSTANCEDETAILFAILED = 'InternalError.GetInstanceDetailFailed'

# Failed to get the backend instance information.
INTERNALERROR_GETINSTANCEINFOFAILED = 'InternalError.GetInstanceInfoFailed'

# Failed to get the current account permissions.
INTERNALERROR_GETRIGHTFAILED = 'InternalError.GetRightFailed'

# Failed to query security group details.
INTERNALERROR_GETSECURITYGROUPDETAILFAILED = 'InternalError.GetSecurityGroupDetailFailed'

# Failed to get the error log.
INTERNALERROR_GETSLOWLOGFAILED = 'InternalError.GetSlowLogFailed'

# Failed to query the VPC subnet information.
INTERNALERROR_GETSUBNETFAILED = 'InternalError.GetSubnetFailed'

# Failed to get the table structure.
INTERNALERROR_GETTABLEINFOFAILED = 'InternalError.GetTableInfoFailed'

# Failed to get the account list.
INTERNALERROR_GETUSERLISTFAILED = 'InternalError.GetUserListFailed'

# Failed to get the number of security groups
INTERNALERROR_GETUSERSGCOUNTFAILED = 'InternalError.GetUserSGCountFailed'

# Failed to query the security group quota of the user.
INTERNALERROR_GETUSGQUOTAERROR = 'InternalError.GetUsgQuotaError'

# Failed to query the VPC information.
INTERNALERROR_GETVPCFAILED = 'InternalError.GetVpcFailed'

# Failed to read the backup file.
INTERNALERROR_HDFSERROR = 'InternalError.HDFSError'

# Missing internal configuration.
INTERNALERROR_INNERCONFIGURATIONMISSING = 'InternalError.InnerConfigurationMissing'

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

# An error occurred when querying an instance.
INTERNALERROR_LISTINSTANCESERROR = 'InternalError.ListInstancesError'

# Failed to get the slow log.
INTERNALERROR_LOGDBFAILED = 'InternalError.LogDBFailed'

# Database operation failed.
INTERNALERROR_OPERATEDATABASEFAILED = 'InternalError.OperateDatabaseFailed'

# An error occurred when reading data from the database.
INTERNALERROR_QUERYDATABASEFAILED = 'InternalError.QueryDatabaseFailed'

# Failed to query the order information.
INTERNALERROR_QUERYORDERFAILED = 'InternalError.QueryOrderFailed'

# Failed to query the price
INTERNALERROR_QUERYPRICEFAILED = 'InternalError.QueryPriceFailed'

# An error occurred when reading data from the database.
INTERNALERROR_READDATABASEFAILED = 'InternalError.ReadDatabaseFailed'

# Route not found.
INTERNALERROR_ROUTENOTFOUND = 'InternalError.RouteNotFound'

# The security group policy of the resource failed to take effect.
INTERNALERROR_SETSVCLOCATIONFAILED = 'InternalError.SetSvcLocationFailed'

# Failed to update the database.
INTERNALERROR_UPDATEDATABASEFAILED = 'InternalError.UpdateDatabaseFailed'

# VPC operation failed
INTERNALERROR_VPCOPERATIONFAILED = 'InternalError.VpcOperationFailed'

# Public network operation failed.
INTERNALERROR_WANSERVICEFAILED = 'InternalError.WanServiceFailed'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# API not found
INVALIDPARAMETER_ACTIONNOTFOUND = 'InvalidParameter.ActionNotFound'

# The password contains invalid characters.
INVALIDPARAMETER_CHARACTERERROR = 'InvalidParameter.CharacterError'

# Verification of input parameters failed.
INVALIDPARAMETER_CHECKPARAMNOTPASS = 'InvalidParameter.CheckParamNotPass'

# The order ID to be queried is not specified.
INVALIDPARAMETER_DEALNAMENOTGIVEN = 'InvalidParameter.DealNameNotGiven'

# An error occurred while verifying parameter validity.
INVALIDPARAMETER_GENERICPARAMETERERROR = 'InvalidParameter.GenericParameterError'

# Invalid parameters
INVALIDPARAMETER_ILLEGALPARAMETERERROR = 'InvalidParameter.IllegalParameterError'

# The time parameter is incorrect.
INVALIDPARAMETER_ILLEGALTIME = 'InvalidParameter.IllegalTime'

# Failed to find the requested instance.
INVALIDPARAMETER_INSTANCENOTFOUND = 'InvalidParameter.InstanceNotFound'

# You have no permission to manipulate this API or resource.
INVALIDPARAMETER_PERMISSIONDENIED = 'InvalidParameter.PermissionDenied'

# Security group validity test failed.
INVALIDPARAMETER_SGCHECKFAIL = 'InvalidParameter.SGCheckFail'

# The instance shard does not exist.
INVALIDPARAMETER_SHARDRESOURCEIDNOTFOUND = 'InvalidParameter.ShardResourceIdNotFound'

# No purchasable specifications found
INVALIDPARAMETER_SPECNOTFOUND = 'InvalidParameter.SpecNotFound'

# The specified VPC subnet was not found.
INVALIDPARAMETER_SUBNETNOTFOUND = 'InvalidParameter.SubnetNotFound'

# The SNAT subnet doesn’t support applying for IPs.
INVALIDPARAMETER_SUBNETUNAVAILABLE = 'InvalidParameter.SubnetUnavailable'

# VIP is not in the subnet.
INVALIDPARAMETER_VIPNOTINSUBNET = 'InvalidParameter.VipNotInSubnet'

# VIP is in use.
INVALIDPARAMETER_VIPUSED = 'InvalidParameter.VipUsed'

# The specified VPC subnet was not found.
INVALIDPARAMETER_VPCNOTFOUND = 'InvalidParameter.VpcNotFound'

# Vport is in use.
INVALIDPARAMETER_VPORTUSED = 'InvalidParameter.VportUsed'

# The account to be created already exists.
INVALIDPARAMETERVALUE_ACCOUNTALREADYEXISTS = 'InvalidParameterValue.AccountAlreadyExists'

# The instance does not support this sync mode.
INVALIDPARAMETERVALUE_BADSYNCMODE = 'InvalidParameterValue.BadSyncMode'

# The specified permission could not be granted to this account.
INVALIDPARAMETERVALUE_BADUSERRIGHT = 'InvalidParameterValue.BadUserRight'

# Invalid account type.
INVALIDPARAMETERVALUE_BADUSERTYPE = 'InvalidParameterValue.BadUserType'

# The number of products exceeds the upper limit.
INVALIDPARAMETERVALUE_ILLEGALCOUNT = 'InvalidParameterValue.IllegalCount'

# The dedicated cluster to which the database instance belongs was not found.
INVALIDPARAMETERVALUE_ILLEGALEXCLUSTERID = 'InvalidParameterValue.IllegalExclusterID'

# The number of products exceeds the upper limit.
INVALIDPARAMETERVALUE_ILLEGALQUANTITY = 'InvalidParameterValue.IllegalQuantity'

# Incorrect permission parameters
INVALIDPARAMETERVALUE_ILLEGALRIGHTPARAM = 'InvalidParameterValue.IllegalRightParam'

# Information of the specified AZ was not found.
INVALIDPARAMETERVALUE_ILLEGALZONE = 'InvalidParameterValue.IllegalZone'

# Parameter verification error.
INVALIDPARAMETERVALUE_INVALIDPARAMETERVALUEERROR = 'InvalidParameterValue.InvalidParameterValueError'

# The specification information of the database instance was not found.
INVALIDPARAMETERVALUE_SPECIDILLEGAL = 'InvalidParameterValue.SpecIdIllegal'

# Operations by a system user are not allowed.
INVALIDPARAMETERVALUE_SUPERUSERFORBIDDEN = 'InvalidParameterValue.SuperUserForbidden'

# Resources are insufficient.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The specified account does not exist.
RESOURCENOTFOUND_ACCOUNTDOESNOTEXIST = 'ResourceNotFound.AccountDoesNotExist'

# The instance does not exist.
RESOURCENOTFOUND_INSTANCENOTFOUND = 'ResourceNotFound.InstanceNotFound'

# The specified database instance was not found.
RESOURCENOTFOUND_NOINSTANCEFOUND = 'ResourceNotFound.NoInstanceFound'

# Failed to find the configuration of the product associated with the security group.
RESOURCENOTFOUND_PRODUCTCONFIGNOTEXISTEDERROR = 'ResourceNotFound.ProductConfigNotExistedError'

# The sync task has been deleted.
RESOURCENOTFOUND_SYNCTASKDELETED = 'ResourceNotFound.SyncTaskDeleted'

# Unable to initialize the instance due to incorrect status.
RESOURCEUNAVAILABLE_BADINSTANCESTATUS = 'ResourceUnavailable.BadInstanceStatus'

# An error occurred while calling COS APIs.
RESOURCEUNAVAILABLE_COSAPIFAILED = 'ResourceUnavailable.CosApiFailed'

# The database instance has been deleted.
RESOURCEUNAVAILABLE_INSTANCEALREADYDELETED = 'ResourceUnavailable.InstanceAlreadyDeleted'

# The database instance has been locked. Operations are not allowed.
RESOURCEUNAVAILABLE_INSTANCEHASBEENLOCKED = 'ResourceUnavailable.InstanceHasBeenLocked'

# Incorrect database instance status. Operations are not allowed.
RESOURCEUNAVAILABLE_INSTANCESTATUSABNORMAL = 'ResourceUnavailable.InstanceStatusAbnormal'

# Failed to verify the security group
RESOURCEUNAVAILABLE_SGCHECKFAIL = 'ResourceUnavailable.SGCheckFail'

# You have no permission to manipulate this API or resource.
UNAUTHORIZEDOPERATION_PERMISSIONDENIED = 'UnauthorizedOperation.PermissionDenied'

# This database version is not supported.
UNSUPPORTEDOPERATION_DBVERSIONNOTSUPPORTED = 'UnsupportedOperation.DbVersionNotSupported'

# The operation is not supported.
UNSUPPORTEDOPERATION_INVALIDOPERATION = 'UnsupportedOperation.InvalidOperation'

# The proxy program is too old. Please contact customer service for upgrade and try again.
UNSUPPORTEDOPERATION_OLDPROXYVERSION = 'UnsupportedOperation.OldProxyVersion'
