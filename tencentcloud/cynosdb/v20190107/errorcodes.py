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


# Failed to get permissions. Please try again later. If the problem persists, please contact customer service.
FAILEDOPERATION_CAMCHECKRESOURCEERROR = 'FailedOperation.CamCheckResourceError'

# Authentication failed. Please try again later. If the problem persists, please contact customer service.
FAILEDOPERATION_CAMSIGANDAUTHERROR = 'FailedOperation.CamSigAndAuthError'

# Failed to create the order and make a payment.
FAILEDOPERATION_CREATEORDER = 'FailedOperation.CreateOrder'

# Failed to access the database. Please try again later. If the problem persists, please contact customer service.
FAILEDOPERATION_DATABASEACCESSERROR = 'FailedOperation.DatabaseAccessError'

# Failed to create a task ({{1}}). Please try again later. If the problem persists, please contact customer service.
FAILEDOPERATION_FLOWCREATEERROR = 'FailedOperation.FlowCreateError'

# Failed to query the backup policy. Please try again later. If the problem persists, please contact customer service.
FAILEDOPERATION_GETBACKUPSTRATEGYERROR = 'FailedOperation.GetBackupStrategyError'

# Insufficient account balance.
FAILEDOPERATION_INSUFFICIENTBALANCE = 'FailedOperation.InsufficientBalance'

# Operation failed ({{1}}). Please try again later. If the problem persists, please contact customer service.
FAILEDOPERATION_OPERATIONFAILEDERROR = 'FailedOperation.OperationFailedError'

# Failed to create the order and make a payment. Please try again later. If the problem persists, please contact customer service.
FAILEDOPERATION_TRADECREATEORDERERROR = 'FailedOperation.TradeCreateOrderError'

# Internal error.
INTERNALERROR = 'InternalError'

# Failed to query the database.
INTERNALERROR_DBOPERATIONFAILED = 'InternalError.DbOperationFailed'

# Failed to get the security group information.
INTERNALERROR_GETSECURITYGROUPDETAILFAILED = 'InternalError.GetSecurityGroupDetailFailed'

# Failed to get the subnet.
INTERNALERROR_GETSUBNETFAILED = 'InternalError.GetSubnetFailed'

# Failed to get the VPC.
INTERNALERROR_GETVPCFAILED = 'InternalError.GetVpcFailed'

# Failed to query instances by security group.
INTERNALERROR_LISTINSTANCEFAILED = 'InternalError.ListInstanceFailed'

# Unsupported operation.
INTERNALERROR_OPERATIONNOTSUPPORT = 'InternalError.OperationNotSupport'

# Failed to query the database.
INTERNALERROR_QUERYDATABASEFAILED = 'InternalError.QueryDatabaseFailed'

# Internal system error.
INTERNALERROR_SYSTEMERROR = 'InternalError.SystemError'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# The current instance cannot be isolated.
INVALIDPARAMETER_ISOLATENOTALLOWED = 'InvalidParameter.IsolateNotAllowed'

# No cluster found.
INVALIDPARAMETERVALUE_CLUSTERNOTFOUND = 'InvalidParameterValue.ClusterNotFound'

# Unsupported instance type.
INVALIDPARAMETERVALUE_DBTYPENOTFOUND = 'InvalidParameterValue.DBTypeNotFound'

# No order ID found.
INVALIDPARAMETERVALUE_DEALNAMENOTFOUND = 'InvalidParameterValue.DealNameNotFound'

# The instance name contains invalid characters.
INVALIDPARAMETERVALUE_ILLEGALINSTANCENAME = 'InvalidParameterValue.IllegalInstanceName'

# Invalid sort by field.
INVALIDPARAMETERVALUE_ILLEGALORDERBY = 'InvalidParameterValue.IllegalOrderBy'

# The password does not meet the requirement.
INVALIDPARAMETERVALUE_ILLEGALPASSWORD = 'InvalidParameterValue.IllegalPassword'

# The instance does not exist.
INVALIDPARAMETERVALUE_INSTANCENOTFOUND = 'InvalidParameterValue.InstanceNotFound'

# Invalid instance version.
INVALIDPARAMETERVALUE_INVALIDDBVERSION = 'InvalidParameterValue.InvalidDBVersion'

# Invalid parameter value.
INVALIDPARAMETERVALUE_INVALIDPARAMETERVALUEERROR = 'InvalidParameterValue.InvalidParameterValueError'

# Invalid region ({{1}}).
INVALIDPARAMETERVALUE_INVALIDREGIONIDERROR = 'InvalidParameterValue.InvalidRegionIdError'

# Invalid instance specification.
INVALIDPARAMETERVALUE_INVALIDSPEC = 'InvalidParameterValue.InvalidSpec'

# Invalid availability zone ({{1}}).
INVALIDPARAMETERVALUE_INVALIDZONEIDERROR = 'InvalidParameterValue.InvalidZoneIdError'

# The parameters (`{{1}}` and `{{2}}`) cannot be set at the same time.
INVALIDPARAMETERVALUE_PARAMBOTHSETERROR = 'InvalidParameterValue.ParamBothSetError'

# Incorrect parameter.
INVALIDPARAMETERVALUE_PARAMERROR = 'InvalidParameterValue.ParamError'

# The selected region and AZ are unavailable.
INVALIDPARAMETERVALUE_REGIONZONEUNAVAILABLE = 'InvalidParameterValue.RegionZoneUnavailable'

# No related storage pool found.
INVALIDPARAMETERVALUE_STORAGEPOOLNOTFOUND = 'InvalidParameterValue.StoragePoolNotFound'

# The selected subnet could not be found.
INVALIDPARAMETERVALUE_SUBNETNOTFOUND = 'InvalidParameterValue.SubnetNotFound'

# The selected VPC could not be found.
INVALIDPARAMETERVALUE_VPCNOTFOUND = 'InvalidParameterValue.VpcNotFound'

# The number of instances exceeds the limit.
LIMITEXCEEDED_USERINSTANCELIMIT = 'LimitExceeded.UserInstanceLimit'

# This operation is not allowed for the current cluster. Reason: {{1}}.
OPERATIONDENIED_CLUSTEROPNOTALLOWEDERROR = 'OperationDenied.ClusterOpNotAllowedError'

# For the cluster ({{1}}) in this status, the operation is not allowed.
OPERATIONDENIED_CLUSTERSTATUSDENIEDERROR = 'OperationDenied.ClusterStatusDeniedError'

# Insufficient account balance.
OPERATIONDENIED_INSUFFICIENTBALANCEERROR = 'OperationDenied.InsufficientBalanceError'

# For the serverless instance in this status ({{1}}), the operation is not allowed.
OPERATIONDENIED_SERVERLESSINSTANCESTATUSDENIED = 'OperationDenied.ServerlessInstanceStatusDenied'

# You need to verify your identity to make a purchase.
OPERATIONDENIED_USERNOTAUTHENTICATEDERROR = 'OperationDenied.UserNotAuthenticatedError'

# The cluster ({{1}}) does not exist.
RESOURCENOTFOUND_CLUSTERNOTFOUNDERROR = 'ResourceNotFound.ClusterNotFoundError'

# The instance ({{1}}) does not exist.
RESOURCENOTFOUND_INSTANCENOTFOUNDERROR = 'ResourceNotFound.InstanceNotFoundError'

# Failed to lock the instance, so the operation cannot be performed temporarily.
RESOURCEUNAVAILABLE_INSTANCELOCKFAIL = 'ResourceUnavailable.InstanceLockFail'

# The instance is exceptional, so the operation cannot be performed temporarily.
RESOURCEUNAVAILABLE_INSTANCESTATUSABNORMAL = 'ResourceUnavailable.InstanceStatusAbnormal'

# Users who haven't completed identity verification cannot make purchases.
UNAUTHORIZEDOPERATION_NOTREALNAMEACCOUNT = 'UnauthorizedOperation.NotRealNameAccount'

# CAM authentication failed.
UNAUTHORIZEDOPERATION_PERMISSIONDENIED = 'UnauthorizedOperation.PermissionDenied'
