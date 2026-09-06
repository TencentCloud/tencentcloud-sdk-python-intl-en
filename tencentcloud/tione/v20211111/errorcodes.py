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

# Cloud Access Management (CAM) system exception.
AUTHFAILURE_CAMEXCEPTION = 'AuthFailure.CamException'

# Unauthorized operation.
AUTHFAILURE_UNAUTHORIZEDOPERATION = 'AuthFailure.UnauthorizedOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Failed to access the API Gateway. Please try again.
FAILEDOPERATION_APIGATEWAYQUERYFAILED = 'FailedOperation.ApiGatewayQueryFailed'

# Failed to access the billing module.
FAILEDOPERATION_BILLINGQUERYFAILED = 'FailedOperation.BillingQueryFailed'

# Cluster access failed.
FAILEDOPERATION_CLUSTERQUERYFAILED = 'FailedOperation.ClusterQueryFailed'

# Duplicated name.
FAILEDOPERATION_DUPLICATENAME = 'FailedOperation.DuplicateName'

# The training task name already exists. Change the name.
FAILEDOPERATION_DUPLICATENAMETASKISCREATING = 'FailedOperation.DuplicateNameTaskIsCreating'

# Database execution error.
FAILEDOPERATION_EXECDATABASEFAIL = 'FailedOperation.ExecDatabaseFail'

# Tag operation failed.
FAILEDOPERATION_EXECTAGFAIL = 'FailedOperation.ExecTagFail'

# Failed to freeze due to insufficient balance.
FAILEDOPERATION_FREEZEBILLFAILED = 'FailedOperation.FreezeBillFailed'

# No permissions.
FAILEDOPERATION_NOPERMISSION = 'FailedOperation.NoPermission'

# The operation is not allowed.
FAILEDOPERATION_NOTALLOW = 'FailedOperation.NotAllow'

# Database query error.
FAILEDOPERATION_QUERYDATABASEFAIL = 'FailedOperation.QueryDatabaseFail'

# Failed to query billable item details.
FAILEDOPERATION_QUERYRESOURCESPECFAILED = 'FailedOperation.QueryResourceSpecFailed'

# Failed to query the tag service.
FAILEDOPERATION_QUERYTAGFAIL = 'FailedOperation.QueryTagFail'

# Failed to access the key service. Please try again.
FAILEDOPERATION_STSQUERYFAILED = 'FailedOperation.StsQueryFailed'

# Unknown instance specifications.
FAILEDOPERATION_UNKNOWNINSTANCETYPE = 'FailedOperation.UnknownInstanceType'

# Data parsing failed.
FAILEDOPERATION_UNMARSHALDATA = 'FailedOperation.UnmarshalData'

# Internal error.
INTERNALERROR = 'InternalError'

# Failed to bind the tag.
INTERNALERROR_BINDINGTAGSFAILED = 'InternalError.BindingTagsFailed'

# The file system does not exist.
INTERNALERROR_CFSNOTFOUND = 'InternalError.CFSNotFound'

# Failed to validate the permissions of the file system path.
INTERNALERROR_CHECKFSPATHACCESSIBILITYFAILED = 'InternalError.CheckFSPathAccessibilityFailed'

# Failed to create the long-term access credential for the TCR image repository.
INTERNALERROR_CREATETCRINSTANCETOKENFAILED = 'InternalError.CreateTcrInstanceTokenFailed'

# Failed to query the file system information.
INTERNALERROR_GETCFSFILESYSTEMSFAILED = 'InternalError.GetCFSFileSystemsFailed'

# Failed to query the file system mount information.
INTERNALERROR_GETCFSMOUNTINFOFAILED = 'InternalError.GetCFSMountInfoFailed'

# Failed to retrieve the HDFS storage information.
INTERNALERROR_QUERYHDFSINFOFAILED = 'InternalError.QueryHDFSInfoFailed'

# Failed to query prepaid resource group details.
INTERNALERROR_QUERYRESOURCEGROUPFAILED = 'InternalError.QueryResourceGroupFailed'

# Failed to query the resource package specification.
INTERNALERROR_QUERYRESOURCESPECFAILED = 'InternalError.QueryResourceSpecFailed'

# Failed to query the subnet information.
INTERNALERROR_QUERYSUBNETINFOFAILED = 'InternalError.QuerySubnetInfoFailed'

# Failed to query VPC information.
INTERNALERROR_QUERYVPCINFOFAILED = 'InternalError.QueryVPCInfoFailed'

# Failed to validate task parameters.
INTERNALERROR_VALIDATECREATETASKFAILED = 'InternalError.ValidateCreateTaskFailed'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# Parameter value error.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The platform's built-in CFS code is selected for the task, but the /opt/ml/output/data output path is incorrect. Unable to submit the task.
INVALIDPARAMETERVALUE_AIMARKETOUTPUTCONFIGEMPTY = 'InvalidParameterValue.AIMarketOutputConfigEmpty'

# The version ID of the AI market public algorithm does not exist.
INVALIDPARAMETERVALUE_AIMARKETPUBLICALGOVERSIONNOTEXIST = 'InvalidParameterValue.AIMarketPublicAlgoVersionNotExist'

# Invalid auto-restart count.
INVALIDPARAMETERVALUE_BACKOFFLIMITILLEGAL = 'InvalidParameterValue.BackOffLimitIllegal'

# Auto-restart is not supported for this task.
INVALIDPARAMETERVALUE_BACKOFFLIMITNOTSUPPORT = 'InvalidParameterValue.BackOffLimitNotSupport'

# Invalid name.
INVALIDPARAMETERVALUE_BADNAME = 'InvalidParameterValue.BadName'

# The COS path does not exist.
INVALIDPARAMETERVALUE_COSPATHNOTEXIST = 'InvalidParameterValue.CosPathNotExist'

# The number of data sets has exceeded the limit.
INVALIDPARAMETERVALUE_DATASETNUMLIMITEXCEEDED = 'InvalidParameterValue.DatasetNumLimitExceeded'

# Instance name conflict. Change the name and try again.
INVALIDPARAMETERVALUE_DUPLICATENAME = 'InvalidParameterValue.DuplicateName'

# Access to the file system path is restricted.
INVALIDPARAMETERVALUE_FSPATHINACCESSIBLE = 'InvalidParameterValue.FSPathInaccessible'

# Unsupported training framework version. Read the documentation to view the frameworks and versions supported by TI-ONE.
INVALIDPARAMETERVALUE_FRAMEWORKVERSIONNOTSUPPORT = 'InvalidParameterValue.FrameworkVersionNotSupport'

# Failed to retrieve the mount IP address for CFS.
INVALIDPARAMETERVALUE_GETCFSMOUNTIPFAILED = 'InvalidParameterValue.GetCFSMountIPFailed'

# Failed to retrieve the GooseFS instance.
INVALIDPARAMETERVALUE_GETGOOSEFSFAILED = 'InvalidParameterValue.GetGooseFSFailed'

# The selected GooseFS instance does not exist.
INVALIDPARAMETERVALUE_GOOSEFSNOTEXIST = 'InvalidParameterValue.GooseFSNotExist'

# Invalid image address.
INVALIDPARAMETERVALUE_IMAGEILLEGAL = 'InvalidParameterValue.ImageIllegal'

# The training task image does not exist.
INVALIDPARAMETERVALUE_IMAGENOTFOUND = 'InvalidParameterValue.ImageNotFound'

# The operation is not allowed.
INVALIDPARAMETERVALUE_NOTALLOW = 'InvalidParameterValue.NotAllow'

# The parameter length has exceeded the limit.
INVALIDPARAMETERVALUE_PARAMLENGTHEXCEEDLIMIT = 'InvalidParameterValue.ParamLengthExceedLimit'

# Invalid local disk path.
INVALIDPARAMETERVALUE_PATHILLEGAL = 'InvalidParameterValue.PathIllegal'

# Failed to query the VPC information.
INVALIDPARAMETERVALUE_QUERYVPCINFOFAILED = 'InvalidParameterValue.QueryVPCInfoFailed'

# Invalid RDMA configuration.
INVALIDPARAMETERVALUE_RDMACONFIGILLEGAL = 'InvalidParameterValue.RDMAConfigIllegal'

# Invalid resource configuration.
INVALIDPARAMETERVALUE_RESOURCECONFIGILLEGAL = 'InvalidParameterValue.ResourceConfigIllegal'

# Failed to create a fine-tuning task. Configure the resources according to the template recommendations.
INVALIDPARAMETERVALUE_TAIJIRESOURCECONFIGILLEGAL = 'InvalidParameterValue.TAIJIResourceConfigIllegal'

# Bare metal resource groups do not support input data configuration.
INVALIDPARAMETERVALUE_UNSUPPORTEDDATACONFIG = 'InvalidParameterValue.UnsupportedDataConfig'

# Error of missing parameters.
MISSINGPARAMETER = 'MissingParameter'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# Insufficient balance. Failed to create or update.
OPERATIONDENIED_BALANCEINSUFFICIENT = 'OperationDenied.BalanceInsufficient'

# Billing platform error.
OPERATIONDENIED_BILLINGEXCEPTION = 'OperationDenied.BillingException'

# Pay-as-you-go resources are sold out.
OPERATIONDENIED_BILLINGSTATUSRESOURCEINSUFFICIENT = 'OperationDenied.BillingStatusResourceInsufficient'

# Invalid IP address.
OPERATIONDENIED_IPILLEGAL = 'OperationDenied.IpIllegal'

# Insufficient balance in the Miying resource package. Top up first.
OPERATIONDENIED_MIYINGBALANCEINSUFFICIENT = 'OperationDenied.MIYINGBalanceInsufficient'

# Invalid IP address range.
OPERATIONDENIED_NETWORKCIDRILLEGAL = 'OperationDenied.NetworkCidrIllegal'

# The operation is not allowed.
OPERATIONDENIED_NOTALLOW = 'OperationDenied.NotAllow'

# Insufficient remaining quota in the prepaid resource group.
OPERATIONDENIED_RESOURCEGROUPINSUFFICIENT = 'OperationDenied.ResourceGroupInsufficient'

# Invalid subnet.
OPERATIONDENIED_SUBNETILLEGAL = 'OperationDenied.SubnetIllegal'

# Insufficient resources in the Taiji application group to meet training requirements.
OPERATIONDENIED_TAIJIAPPLICATIONGROUPINSUFFICIENT = 'OperationDenied.TAIJIApplicationGroupInsufficient'

# Insufficient free quota for the allowlist.
OPERATIONDENIED_WHITELISTQUOTAEXCEED = 'OperationDenied.WhitelistQuotaExceed'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The file system does not exist.
RESOURCENOTFOUND_CFSNOTFOUND = 'ResourceNotFound.CfsNotFound'

# The VPC does not exist.
RESOURCENOTFOUND_VPCNOTFOUND = 'ResourceNotFound.VPCNotFound'

# Unknown parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'
