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


# CAM signature/authentication error
AUTHFAILURE = 'AuthFailure'

# Unauthorized operation.
AUTHFAILURE_UNAUTHORIZEDOPERATION = 'AuthFailure.UnAuthorizedOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# An error occurred with the cluster resource quota limit.
FAILEDOPERATION_CLUSTERRESOURCELIMITERROR = 'FailedOperation.ClusterResourceLimitError'

# Failed to query the number of disks of the node
FAILEDOPERATION_DISKCOUNTPARAMERROR = 'FailedOperation.DiskCountParamError'

# Incorrect cluster status
FAILEDOPERATION_ERRORCLUSTERSTATE = 'FailedOperation.ErrorClusterState'

# No replicas for indexes in the cluster.
FAILEDOPERATION_ERRORCLUSTERSTATENOREPLICATION = 'FailedOperation.ErrorClusterStateNoReplication'

# The cluster is unhealthy.
FAILEDOPERATION_ERRORCLUSTERSTATEUNHEALTH = 'FailedOperation.ErrorClusterStateUnhealth'

# No credit card or PayPal account is linked to the current account. Unable to make a payment.
FAILEDOPERATION_NOPAYMENT = 'FailedOperation.NoPayment'

# Unverified user.
FAILEDOPERATION_NOTAUTHENTICATED = 'FailedOperation.NotAuthenticated'

# Request timeout.
FAILEDOPERATION_REQUESTTIMEOUT = 'FailedOperation.RequestTimeOut'

# Cannot increase the number of disks during rolling restart of scaled-out compute resources.
FAILEDOPERATION_UNSUPPORTRESETNODETYPEANDSCALEOUTDISK = 'FailedOperation.UnsupportResetNodeTypeAndScaleoutDisk'

# The disk capacity can’t be modified during rolling restart of scaled-in compute resources.
FAILEDOPERATION_UNSUPPORTRESETSCALEDOWNANDMODIFYDISK = 'FailedOperation.UnsupportResetScaledownAndModifyDisk'

# Cannot adjust the node configuration and disk capacity reversely.
FAILEDOPERATION_UNSUPPORTREVERSEREGULATIONNODETYPEANDDISK = 'FailedOperation.UnsupportReverseRegulationNodeTypeAndDisk'

# Internal error.
INTERNALERROR = 'InternalError'

# Invalid parameter.
INVALIDPARAMETER = 'InvalidParameter'

# AppId value does not match the expected value.
INVALIDPARAMETER_INVALIDAPPID = 'InvalidParameter.InvalidAppId'

# The instance version EsVersion value does not match the expected value.
INVALIDPARAMETER_INVALIDESVERSION = 'InvalidParameter.InvalidEsVersion'

# The value of the created index metadata JSON field IndexMetaJson does not match the expected value.
INVALIDPARAMETER_INVALIDINDEXMETAJSON = 'InvalidParameter.InvalidIndexMetaJson'

# The IndexName value does not match the expected value.
INVALIDPARAMETER_INVALIDINDEXNAME = 'InvalidParameter.InvalidIndexName'

# The IndexType value does not match the expected value.
INVALIDPARAMETER_INVALIDINDEXTYPE = 'InvalidParameter.InvalidIndexType'

# Invalid InstanceId, no corresponding resource found.
INVALIDPARAMETER_INVALIDINSTANCEID = 'InvalidParameter.InvalidInstanceId'

# The page size Limit value does not match the expected value.
INVALIDPARAMETER_INVALIDLIMIT = 'InvalidParameter.InvalidLimit'

# The LogType value does not match the expected value.
INVALIDPARAMETER_INVALIDLOGTYPE = 'InvalidParameter.InvalidLogType'

# The Offset value does not match the expected value.
INVALIDPARAMETER_INVALIDOFFSET = 'InvalidParameter.InvalidOffset'

# The sort field OrderByKey value does not match the expected value.
INVALIDPARAMETER_INVALIDORDERBYKEY = 'InvalidParameter.InvalidOrderByKey'

# Invalid lucene syntax
INVALIDPARAMETER_INVALIDQUERYSTRING = 'InvalidParameter.InvalidQueryString'

# The Region value does not match the expected value.
INVALIDPARAMETER_INVALIDREGION = 'InvalidParameter.InvalidRegion'

# The value or format of time-related parameters does not match the expected.
INVALIDPARAMETER_INVALIDTIMEPARAM = 'InvalidParameter.InvalidTimeParam'

# Incorrect parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Missing parameter.
MISSINGPARAMETER = 'MissingParameter'

# The number of requests exceeds the frequency limit.
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# Resource is in use.
RESOURCEINUSE = 'ResourceInUse'

# Insufficient resource.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# Insufficient account balance.
RESOURCEINSUFFICIENT_BALANCE = 'ResourceInsufficient.Balance'

# Dedicated master node resources in the hidden availability zone are insufficient.
RESOURCEINSUFFICIENT_HIDDENZONE = 'ResourceInsufficient.HiddenZone'

# Insufficient number of remaining subnet IPs.
RESOURCEINSUFFICIENT_SUBNET = 'ResourceInsufficient.Subnet'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# Failed to obtain cluster resources.
RESOURCENOTFOUND_CLUSTERINFONOTFOUND = 'ResourceNotFound.ClusterInfoNotFound'

# Failed to obtain database resources.
RESOURCENOTFOUND_DBINFONOTFOUND = 'ResourceNotFound.DBInfoNotFound'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Unknown parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
