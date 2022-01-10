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


# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Internal error.
INTERNALERROR = 'InternalError'

# Failed to obtain the user authentication information
INTERNALERROR_ACCOUNTCOMMON = 'InternalError.AccountCommon'

# Account not verified.
INTERNALERROR_ACCOUNTUSERNOTAUTHENTICATED = 'InternalError.AccountUserNotAuthenticated'

# Error creating scaling group resource.
INTERNALERROR_ASCOMMON = 'InternalError.AsCommon'

# You do not have permissions.
INTERNALERROR_CAMNOAUTH = 'InternalError.CamNoAuth'

# CIDR conflicts with the CIDR of another cluster.
INTERNALERROR_CIDRCONFLICTWITHOTHERCLUSTER = 'InternalError.CidrConflictWithOtherCluster'

# CIDR conflicts with another route.
INTERNALERROR_CIDRCONFLICTWITHOTHERROUTE = 'InternalError.CidrConflictWithOtherRoute'

# CIDR conflicts with VPC.
INTERNALERROR_CIDRCONFLICTWITHVPCCIDR = 'InternalError.CidrConflictWithVpcCidr'

# CIDR conflicts with global route.
INTERNALERROR_CIDRCONFLICTWITHVPCGLOBALROUTE = 'InternalError.CidrConflictWithVpcGlobalRoute'

# Invalid CIDR.
INTERNALERROR_CIDRINVALI = 'InternalError.CidrInvali'

# Invalid CIDR mask.
INTERNALERROR_CIDRMASKSIZEOUTOFRANGE = 'InternalError.CidrMaskSizeOutOfRange'

# Cluster not found.
INTERNALERROR_CLUSTERNOTFOUND = 'InternalError.ClusterNotFound'

# Cluster status error.
INTERNALERROR_CLUSTERSTATE = 'InternalError.ClusterState'

# The version of the cluster node is outdated.
INTERNALERROR_CLUSTERUPGRADENODEVERSION = 'InternalError.ClusterUpgradeNodeVersion'

# Internal HTTP client error
INTERNALERROR_COMPONENTCLIENTHTTP = 'InternalError.ComponentClientHttp'

# Error while requesting (HTTP) other Tencent Cloud services
INTERNALERROR_COMPONENTCLINETHTTP = 'InternalError.ComponentClinetHttp'

# Failed to create cluster.
INTERNALERROR_CREATEMASTERFAILED = 'InternalError.CreateMasterFailed'

# Error in node creation.
INTERNALERROR_CVMCOMMON = 'InternalError.CvmCommon'

# CVM does not exist.
INTERNALERROR_CVMNOTFOUND = 'InternalError.CvmNotFound'

# Some of the CVMs cannot be found
INTERNALERROR_CVMNUMBERNOTMATCH = 'InternalError.CvmNumberNotMatch'

# DB error.
INTERNALERROR_DB = 'InternalError.Db'

# Database error.
INTERNALERROR_DBAFFECTIVEDROWS = 'InternalError.DbAffectivedRows'

# Record not found.
INTERNALERROR_DBRECORDNOTFOUND = 'InternalError.DbRecordNotFound'

# Failed to obtain total number of current security groups.
INTERNALERROR_DFWGETUSGCOUNT = 'InternalError.DfwGetUSGCount'

# Failed to obtain security group quota.
INTERNALERROR_DFWGETUSGQUOTA = 'InternalError.DfwGetUSGQuota'

# Empty clusters are not supported.
INTERNALERROR_EMPTYCLUSTERNOTSUPPORT = 'InternalError.EmptyClusterNotSupport'

# Image not found.
INTERNALERROR_IMAGEIDNOTFOUND = 'InternalError.ImageIdNotFound'

# Failed to initialize Master.
INTERNALERROR_INITMASTERFAILED = 'InternalError.InitMasterFailed'

# Invalid CIDR.
INTERNALERROR_INVALIDPRIVATENETWORKCIDR = 'InternalError.InvalidPrivateNetworkCidr'

# Failed to connect to the user’s Kubernetes cluster.
INTERNALERROR_KUBECLIENTCONNECTION = 'InternalError.KubeClientConnection'

# Kubernetes API error.
INTERNALERROR_KUBECOMMON = 'InternalError.KubeCommon'

# Failed to create the kubernetes client.
INTERNALERROR_KUBERNETESCLIENTBUILDERROR = 'InternalError.KubernetesClientBuildError'

# Failed to create the kubernetes resource.
INTERNALERROR_KUBERNETESCREATEOPERATIONERROR = 'InternalError.KubernetesCreateOperationError'

# Failed to delete the kubernetes resource.
INTERNALERROR_KUBERNETESDELETEOPERATIONERROR = 'InternalError.KubernetesDeleteOperationError'

# Failed to obtain the kubernetes resources
INTERNALERROR_KUBERNETESGETOPERATIONERROR = 'InternalError.KubernetesGetOperationError'

# Unknown Kubernetes error
INTERNALERROR_KUBERNETESINTERNAL = 'InternalError.KubernetesInternal'

# An error occurs while calling the underlying CLB
INTERNALERROR_LBCOMMON = 'InternalError.LbCommon'

# Image OS not supported.
INTERNALERROR_OSNOTSUPPORT = 'InternalError.OsNotSupport'

# Parameter error.
INTERNALERROR_PARAM = 'InternalError.Param'

# Pod not found
INTERNALERROR_PODNOTFOUND = 'InternalError.PodNotFound'

# Cluster does not support the current operation.
INTERNALERROR_PUBLICCLUSTEROPNOTSUPPORT = 'InternalError.PublicClusterOpNotSupport'

# Quota limit exceeded.
INTERNALERROR_QUOTAMAXCLSLIMIT = 'InternalError.QuotaMaxClsLimit'

# Quota limit exceeded.
INTERNALERROR_QUOTAMAXNODLIMIT = 'InternalError.QuotaMaxNodLimit'

# Quota limit exceeded.
INTERNALERROR_QUOTAMAXRTLIMIT = 'InternalError.QuotaMaxRtLimit'

# Insufficient security group quota.
INTERNALERROR_QUOTAUSGLIMIT = 'InternalError.QuotaUSGLimit'

# Resource already exists.
INTERNALERROR_RESOURCEEXISTALREADY = 'InternalError.ResourceExistAlready'

# Route table is not empty.
INTERNALERROR_ROUTETABLENOTEMPTY = 'InternalError.RouteTableNotEmpty'

# Route table does not exist.
INTERNALERROR_ROUTETABLENOTFOUND = 'InternalError.RouteTableNotFound'

# Failed to create the task.
INTERNALERROR_TASKCREATEFAILED = 'InternalError.TaskCreateFailed'

# The task in the current state does not support this operation.
INTERNALERROR_TASKLIFESTATEERROR = 'InternalError.TaskLifeStateError'

# No task found
INTERNALERROR_TASKNOTFOUND = 'InternalError.TaskNotFound'

# Internal error.
INTERNALERROR_UNEXCEPTEDINTERNAL = 'InternalError.UnexceptedInternal'

# Unknown internal error.
INTERNALERROR_UNEXPECTEDINTERNAL = 'InternalError.UnexpectedInternal'

# Unknown VPC error
INTERNALERROR_VPCUNEXPECTEDERROR = 'InternalError.VPCUnexpectedError'

# VPC error
INTERNALERROR_VPCCOMMON = 'InternalError.VpcCommon'

# Peering connection does not exist
INTERNALERROR_VPCPEERNOTFOUND = 'InternalError.VpcPeerNotFound'

# VPC record not found
INTERNALERROR_VPCRECODRNOTFOUND = 'InternalError.VpcRecodrNotFound'

# Unknown allowlist error
INTERNALERROR_WHITELISTUNEXPECTEDERROR = 'InternalError.WhitelistUnexpectedError'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# Auto scaling group creation parameter error.
INVALIDPARAMETER_ASCOMMONERROR = 'InvalidParameter.AsCommonError'

# Invalid CIDR block mask (valid range: 10 to 24).
INVALIDPARAMETER_CIDRMASKSIZEOUTOFRANGE = 'InvalidParameter.CIDRMaskSizeOutOfRange'

# The CIDR block conflicts with the CIDR blocks of other clusters.
INVALIDPARAMETER_CIDRCONFLICTWITHOTHERCLUSTER = 'InvalidParameter.CidrConflictWithOtherCluster'

# The route to create conflicts with existing routes.
INVALIDPARAMETER_CIDRCONFLICTWITHOTHERROUTE = 'InvalidParameter.CidrConflictWithOtherRoute'

# The CIDR block conflicts with the VPC’s CIDR block.
INVALIDPARAMETER_CIDRCONFLICTWITHVPCCIDR = 'InvalidParameter.CidrConflictWithVpcCidr'

# The created route conflicts with the existing global route under the VPC.
INVALIDPARAMETER_CIDRCONFLICTWITHVPCGLOBALROUTE = 'InvalidParameter.CidrConflictWithVpcGlobalRoute'

# Parameter error. The CIDR block does not meet the specification.
INVALIDPARAMETER_CIDRINVALID = 'InvalidParameter.CidrInvalid'

# The CIDR block is not in the route table.
INVALIDPARAMETER_CIDROUTOFROUTETABLE = 'InvalidParameter.CidrOutOfRouteTable'

# The cluster ID does not exist.
INVALIDPARAMETER_CLUSTERNOTFOUND = 'InvalidParameter.ClusterNotFound'

# Next hop address is already associated with a CIDR block.
INVALIDPARAMETER_GATEWAYALREADYASSOCIATEDCIDR = 'InvalidParameter.GatewayAlreadyAssociatedCidr'

# Invalid private CIDR block.
INVALIDPARAMETER_INVALIDPRIVATENETWORKCIDR = 'InvalidParameter.InvalidPrivateNetworkCIDR'

# Invalid parameter.
INVALIDPARAMETER_PARAM = 'InvalidParameter.Param'

# The PROM instance does not exist.
INVALIDPARAMETER_PROMINSTANCENOTFOUND = 'InvalidParameter.PromInstanceNotFound'

# Route table is not empty.
INVALIDPARAMETER_ROUTETABLENOTEMPTY = 'InvalidParameter.RouteTableNotEmpty'

# Quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# Missing parameter.
MISSINGPARAMETER = 'MissingParameter'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# The cluster is under deletion protection and cannot be deleted.
OPERATIONDENIED_CLUSTERINDELETIONPROTECTION = 'OperationDenied.ClusterInDeletionProtection'

# The resource is occupied.
RESOURCEINUSE = 'ResourceInUse'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The scaling group does not exist.
RESOURCENOTFOUND_ASASGNOTEXIST = 'ResourceNotFound.AsAsgNotExist'

# The cluster does not exist.
RESOURCENOTFOUND_CLUSTERNOTFOUND = 'ResourceNotFound.ClusterNotFound'

# The specified resource is not found in the Kubernetes cluster.
RESOURCENOTFOUND_KUBERESOURCENOTFOUND = 'ResourceNotFound.KubeResourceNotFound'

# The kubernetes resource does not exist.
RESOURCENOTFOUND_KUBERNETESRESOURCENOTFOUND = 'ResourceNotFound.KubernetesResourceNotFound'

# Resource is unavailable
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# The cluster’s status does support this operation.
RESOURCEUNAVAILABLE_CLUSTERSTATE = 'ResourceUnavailable.ClusterState'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# The API has no CAM permissions.
UNAUTHORIZEDOPERATION_CAMNOAUTH = 'UnauthorizedOperation.CamNoAuth'

# Unknown parameter.
UNKNOWNPARAMETER = 'UnknownParameter'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# Failed to enable CA because AS is disabled.
UNSUPPORTEDOPERATION_CAENABLEFAILED = 'UnsupportedOperation.CaEnableFailed'

# The user is not in the allowlist.
UNSUPPORTEDOPERATION_NOTINWHITELIST = 'UnsupportedOperation.NotInWhitelist'
