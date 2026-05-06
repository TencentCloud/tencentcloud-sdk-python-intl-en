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

# Unauthorized operation error.
AUTHFAILURE_UNAUTHORIZEDOPERATION = 'AuthFailure.UnauthorizedOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Call CLS service failure
FAILEDOPERATION_CLS = 'FailedOperation.Cls'

# Operation failed.
FAILEDOPERATION_FAILEDOPERATION = 'FailedOperation.FailedOperation'

# Operation failed. Internal error.
FAILEDOPERATION_INTERNALERROR = 'FailedOperation.InternalError'

# The maximum number of instance purchases is exceeded.
FAILEDOPERATION_RESOURCE = 'FailedOperation.Resource'

# Failed to get temporary key
FAILEDOPERATION_ROLE = 'FailedOperation.Role'

# Failed to call the VPC service
FAILEDOPERATION_VPC = 'FailedOperation.Vpc'

# Internal error.
INTERNALERROR = 'InternalError'

# Insufficient permissions.
INTERNALERROR_CAMNOAUTH = 'InternalError.CamNoAuth'

# Create an internal error.
INTERNALERROR_CREATEERROR = 'InternalError.CreateError'

# Decoding error.
INTERNALERROR_DECODEERROR = 'InternalError.DecodeError'

# Status code error.
INTERNALERROR_HTTPSTATUSCODEERROR = 'InternalError.HttpStatusCodeError'

# Internal service call exception.
INTERNALERROR_IOERROR = 'InternalError.IOError'

# Internal service error.
INTERNALERROR_INTERNALERROR = 'InternalError.InternalError'

# Operation failed.
INTERNALERROR_OPERATIONFAILED = 'InternalError.OperationFailed'

# Query internal error.
INTERNALERROR_QUERYERROR = 'InternalError.QueryError'

# Unknown error.
INTERNALERROR_UNKNOWNERROR = 'InternalError.UnknownError'

# Refresh internal error.
INTERNALERROR_UPDATEERROR = 'InternalError.UpdateError'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# Parameter value error.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The operation is not supported for old instances.
INVALIDPARAMETERVALUE_ACTION = 'InvalidParameterValue.Action'

# Request format incorrect.
INVALIDPARAMETERVALUE_BADREQUESTFORMAT = 'InvalidParameterValue.BadRequestFormat'

# Invalid request parameter caused creation failure.
INVALIDPARAMETERVALUE_CREATEERROR = 'InvalidParameterValue.CreateError'

# The description information is invalid.
INVALIDPARAMETERVALUE_DESCRIPTION = 'InvalidParameterValue.Description'

# Gateway ID invalid
INVALIDPARAMETERVALUE_GATEWAYID = 'InvalidParameterValue.GatewayId'

# Invalid parameter value.
INVALIDPARAMETERVALUE_INVALIDPARAMETERVALUE = 'InvalidParameterValue.InvalidParameterValue'

# Invalid name.
INVALIDPARAMETERVALUE_NAME = 'InvalidParameterValue.Name'

# Invalid request parameter caused operation failure.
INVALIDPARAMETERVALUE_OPERATIONFAILED = 'InvalidParameterValue.OperationFailed'

# Invalid request parameter. Query failed.
INVALIDPARAMETERVALUE_QUERYERROR = 'InvalidParameterValue.QueryError'

# Invalid Region.
INVALIDPARAMETERVALUE_REGION = 'InvalidParameterValue.Region'

# The resource already exists.
INVALIDPARAMETERVALUE_RESOURCEALREADYEXIST = 'InvalidParameterValue.ResourceAlreadyExist'

# Gateway specification parameter content error
INVALIDPARAMETERVALUE_SPECIFICATION = 'InvalidParameterValue.Specification'

# Gateway type parameter content error
INVALIDPARAMETERVALUE_TYPE = 'InvalidParameterValue.Type'

# Invalid request parameter caused update failure.
INVALIDPARAMETERVALUE_UPDATEERROR = 'InvalidParameterValue.UpdateError'

# The quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# The total certificate domain names of the gateway exceed the limit.
LIMITEXCEEDED_LBDOMAINS = 'LimitExceeded.LBDomains'

# The parameter exceeds the limit.
LIMITEXCEEDED_LIMITEXCEEDED = 'LimitExceeded.LimitExceeded'

# Parameters are missing.
MISSINGPARAMETER = 'MissingParameter'

# Missing parameter caused creation failure.
MISSINGPARAMETER_CREATEERROR = 'MissingParameter.CreateError'

# Missing required parameters.
MISSINGPARAMETER_MISSPARAMETER = 'MissingParameter.MissParameter'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# Operation not allowed.
OPERATIONDENIED_OPERATIONDENIED = 'OperationDenied.OperationDenied'

# Service source and service relationship.
RESOURCEINUSE_GATEWAYSERVICESOURCEEXISTSERVICE = 'ResourceInUse.GatewayServiceSourceExistService'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The resource does not exist. Operation is not allowed.
RESOURCENOTFOUND_FORBIDDEN = 'ResourceNotFound.Forbidden'

# The instance does not exist.
RESOURCENOTFOUND_INSTANCENOTFOUND = 'ResourceNotFound.InstanceNotFound'

# The resource does not exist.
RESOURCENOTFOUND_RESOURCENOTFOUND = 'ResourceNotFound.ResourceNotFound'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Authentication fail.
UNAUTHORIZEDOPERATION_CAMNOAUTH = 'UnauthorizedOperation.CamNoAuth'

# The sub-account lacks passRole permission.
UNAUTHORIZEDOPERATION_CAMPASSROLENOTEXIST = 'UnauthorizedOperation.CamPassRoleNotExist'

# CLS product is not activated.
UNAUTHORIZEDOPERATION_CLSNOTACTIVATED = 'UnauthorizedOperation.ClsNotActivated'

# Unauthorized Uin
UNAUTHORIZEDOPERATION_UIN = 'UnauthorizedOperation.Uin'

# Unauthorized operation.
UNAUTHORIZEDOPERATION_UNAUTHORIZEDOPERATION = 'UnauthorizedOperation.UnauthorizedOperation'

# The operation is not supported.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
