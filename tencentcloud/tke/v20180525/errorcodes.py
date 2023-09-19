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

# Failed to obtain user authentication information.
FAILEDOPERATION_ACCOUNTCOMMON = 'FailedOperation.AccountCommon'

# The account is not verified.
FAILEDOPERATION_ACCOUNTUSERNOTAUTHENTICATED = 'FailedOperation.AccountUserNotAuthenticated'

# An error occurs while creating scaling group resources.
FAILEDOPERATION_ASCOMMON = 'FailedOperation.AsCommon'

# Not authorized to access this API
FAILEDOPERATION_CAMNOAUTH = 'FailedOperation.CamNoAuth'

# The cluster cannot be deleted.
FAILEDOPERATION_CLUSTERFORBIDDENTODELETE = 'FailedOperation.ClusterForbiddenToDelete'

# The cluster is not found.
FAILEDOPERATION_CLUSTERNOTFOUND = 'FailedOperation.ClusterNotFound'

# Cluster status error.
FAILEDOPERATION_CLUSTERSTATE = 'FailedOperation.ClusterState'

# The version of the cluster node is too old.
FAILEDOPERATION_CLUSTERUPGRADENODEVERSION = 'FailedOperation.ClusterUpgradeNodeVersion'

# Internal client error.
FAILEDOPERATION_COMPONENTCLIENTCOMMON = 'FailedOperation.ComponentClientCommon'

# Internal HTTP client error.
FAILEDOPERATION_COMPONENTCLIENTHTTP = 'FailedOperation.ComponentClientHttp'

# Internal HTTP decapsulation failed.
FAILEDOPERATION_COMPONENTCLIENTUNPACK = 'FailedOperation.ComponentClientUnpack'

# Failed to request (HTTP request) other Tencent Cloud services.
FAILEDOPERATION_COMPONENTCLINETHTTP = 'FailedOperation.ComponentClinetHttp'

# Failed to create the node due to a CVM error
FAILEDOPERATION_CVMCOMMON = 'FailedOperation.CvmCommon'

# Some of the specified CVMs are not found.
FAILEDOPERATION_CVMNUMBERNOTMATCH = 'FailedOperation.CvmNumberNotMatch'

# The CVM does not match the VPC ID.
FAILEDOPERATION_CVMVPCIDNOTMATCH = 'FailedOperation.CvmVpcidNotMatch'

# Database error.
FAILEDOPERATION_DB = 'FailedOperation.Db'

# Record not found.
FAILEDOPERATION_DBRECORDNOTFOUND = 'FailedOperation.DbRecordNotFound'

# Failed to obtain security group quota.
FAILEDOPERATION_DFWGETUSGQUOTA = 'FailedOperation.DfwGetUSGQuota'

# Failed to enable the VPC-CNI mode.
FAILEDOPERATION_ENABLEVPCCNIFAILED = 'FailedOperation.EnableVPCCNIFailed'

# Failed to connect to the customer Kubernetes cluster.
FAILEDOPERATION_KUBECLIENTCONNECTION = 'FailedOperation.KubeClientConnection'

# Kubernetes API error.
FAILEDOPERATION_KUBECOMMON = 'FailedOperation.KubeCommon'

# Failed to create the Kubernetes client.
FAILEDOPERATION_KUBERNETESCLIENTBUILDERROR = 'FailedOperation.KubernetesClientBuildError'

# An error occurs while creating the cluster client.
FAILEDOPERATION_KUBERNETESCREATEOPERATIONERROR = 'FailedOperation.KubernetesCreateOperationError'

# 
FAILEDOPERATION_KUBERNETESGETOPERATIONERROR = 'FailedOperation.KubernetesGetOperationError'

# Unknown Kubernetes error.
FAILEDOPERATION_KUBERNETESINTERNAL = 'FailedOperation.KubernetesInternal'

# Failed to obtain the kubernetes resource list.
FAILEDOPERATION_KUBERNETESLISTOPERATIONERROR = 'FailedOperation.KubernetesListOperationError'

# An unknown error occurs while calling the underlying CLB.
FAILEDOPERATION_LBCOMMON = 'FailedOperation.LbCommon'

# Network extension error.
FAILEDOPERATION_NETWORKSCALEERROR = 'FailedOperation.NetworkScaleError'

# The node has a secondary ENI.
FAILEDOPERATION_NODEEXISTSSECONDARYNETWORKINTERFACE = 'FailedOperation.NodeExistsSecondaryNetworkInterface'

# The image OS is not supported.
FAILEDOPERATION_OSNOTSUPPORT = 'FailedOperation.OsNotSupport'

# Invalid parameter.
FAILEDOPERATION_PARAM = 'FailedOperation.Param'

# GPE error.
FAILEDOPERATION_POLICYSERVERCOMMONERROR = 'FailedOperation.PolicyServerCommonError'

# Reached the quota limit.
FAILEDOPERATION_QUOTAMAXCLSLIMIT = 'FailedOperation.QuotaMaxClsLimit'

# Reached the quota limit.
FAILEDOPERATION_QUOTAMAXNODLIMIT = 'FailedOperation.QuotaMaxNodLimit'

# Insufficient security group quota.
FAILEDOPERATION_QUOTAUSGLIMIT = 'FailedOperation.QuotaUSGLimit'

# The sub-account does not have the required RBAC permissions.
FAILEDOPERATION_RBACFORBIDDEN = 'FailedOperation.RBACForbidden'

# Record not found.
FAILEDOPERATION_RECORDNOTFOUND = 'FailedOperation.RecordNotFound'

# A same task is in progress.
FAILEDOPERATION_TASKALREADYRUNNING = 'FailedOperation.TaskAlreadyRunning'

# This operation is not supported when the task is in the current status.
FAILEDOPERATION_TASKLIFESTATEERROR = 'FailedOperation.TaskLifeStateError'

# Query failed.
FAILEDOPERATION_TRADECOMMON = 'FailedOperation.TradeCommon'

# Unexpected error.
FAILEDOPERATION_UNEXPECTEDERROR = 'FailedOperation.UnexpectedError'

# Unknown VPC error.
FAILEDOPERATION_VPCUNEXPECTEDERROR = 'FailedOperation.VPCUnexpectedError'

# VPC error.
FAILEDOPERATION_VPCCOMMON = 'FailedOperation.VpcCommon'

# VPC record not found.
FAILEDOPERATION_VPCRECODRNOTFOUND = 'FailedOperation.VpcRecodrNotFound'

# Allowlist error.
FAILEDOPERATION_WHITELISTUNEXPECTEDERROR = 'FailedOperation.WhitelistUnexpectedError'

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

# Command execution timeout.
INTERNALERROR_CMDTIMEOUT = 'InternalError.CmdTimeout'

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

# Exceptional CVM status.
INTERNALERROR_CVMSTATUS = 'InternalError.CvmStatus'

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

# Failed to obtain the kubernetes resource list.
INTERNALERROR_KUBERNETESLISTOPERATIONERROR = 'InternalError.KubernetesListOperationError'

# Kubernetes Patch operation failed.
INTERNALERROR_KUBERNETESPATCHOPERATIONERROR = 'InternalError.KubernetesPatchOperationError'

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

# A same task is in progress.
INTERNALERROR_TASKALREADYRUNNING = 'InternalError.TaskAlreadyRunning'

# Failed to create the task.
INTERNALERROR_TASKCREATEFAILED = 'InternalError.TaskCreateFailed'

# The task in the current state does not support this operation.
INTERNALERROR_TASKLIFESTATEERROR = 'InternalError.TaskLifeStateError'

# No task found
INTERNALERROR_TASKNOTFOUND = 'InternalError.TaskNotFound'

# Query failed
INTERNALERROR_TRADECOMMON = 'InternalError.TradeCommon'

# Insufficient account balance.
INTERNALERROR_TRADEINSUFFICIENTBALANCE = 'InternalError.TradeInsufficientBalance'

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

# VstationError.
INTERNALERROR_VSTATIONERROR = 'InternalError.VstationError'

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

# Invalid CIDR block.
INVALIDPARAMETER_CIDRINVALI = 'InvalidParameter.CidrInvali'

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

# The iage OS is not supported.
INVALIDPARAMETER_OSNOTSUPPORT = 'InvalidParameter.OsNotSupport'

# Invalid parameter.
INVALIDPARAMETER_PARAM = 'InvalidParameter.Param'

# The PROM instance does not exist.
INVALIDPARAMETER_PROMINSTANCENOTFOUND = 'InvalidParameter.PromInstanceNotFound'

# Route table is not empty.
INVALIDPARAMETER_ROUTETABLENOTEMPTY = 'InvalidParameter.RouteTableNotEmpty'

# Invalid subnet.
INVALIDPARAMETER_SUBNETINVALIDERROR = 'InvalidParameter.SubnetInvalidError'

# The subnet does not exist.
INVALIDPARAMETER_SUBNETNOTEXIST = 'InvalidParameter.SubnetNotExist'

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

# A running Pod exists.
RESOURCEINUSE_EXISTRUNNINGPOD = 'ResourceInUse.ExistRunningPod'

# The resource already exists.
RESOURCEINUSE_RESOURCEEXISTALREADY = 'ResourceInUse.ResourceExistAlready'

# The subnet already exists.
RESOURCEINUSE_SUBNETALREADYEXIST = 'ResourceInUse.SubnetAlreadyExist'

# Insufficient CVM resources.
RESOURCEINSUFFICIENT_SPECIFIEDINSTANCETYPE = 'ResourceInsufficient.SpecifiedInstanceType'

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

# Abnormal cluster status.
RESOURCEUNAVAILABLE_CLUSTERINABNORMALSTAT = 'ResourceUnavailable.ClusterInAbnormalStat'

# The cluster’s status does support this operation.
RESOURCEUNAVAILABLE_CLUSTERSTATE = 'ResourceUnavailable.ClusterState'

# The node pool is in an abnormal status.
RESOURCEUNAVAILABLE_NODEPOOLSTATENOTNORMAL = 'ResourceUnavailable.NodePoolStateNotNormal'

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

# The VPC-CNI mode is not supported.
UNSUPPORTEDOPERATION_CLUSTERNOTSUITENABLEVPCCNI = 'UnsupportedOperation.ClusterNotSuitEnableVPCCNI'

# The user is not in the allowlist.
UNSUPPORTEDOPERATION_NOTINWHITELIST = 'UnsupportedOperation.NotInWhitelist'

# Virtual nodes cannot be installed.
UNSUPPORTEDOPERATION_NOTSUPPORTINSTALLVIRTUALKUBELET = 'UnsupportedOperation.NotSupportInstallVirtualKubelet'
