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


# CAM signature/authentication error.
AUTHFAILURE = 'AuthFailure'

# Captcha signature error.
AUTHFAILURE_CAPSIGERROR = 'AuthFailure.CapSigError'

# Request expired.
AUTHFAILURE_EXPIRED = 'AuthFailure.Expired'

# DryRun operation means the request will be successful, but the DryRun parameter is passed.
DRYRUNOPERATION = 'DryRunOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Internal error.
INTERNALERROR = 'InternalError'

# Business system logic error.
INTERNALERROR_BACKENDLOGICERROR = 'InternalError.BackendLogicError'

# Connection to the database timed out.
INTERNALERROR_CONNECTDBTIMEOUT = 'InternalError.ConnectDBTimeout'

# Sign backend error.
INTERNALERROR_SIGNBACKENDERROR = 'InternalError.SignBackendError'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# Captcha signature error.
INVALIDPARAMETER_CAPSIGERROR = 'InvalidParameter.CapSigError'

# Parameter error.
INVALIDPARAMETER_PARAMERROR = 'InvalidParameter.ParamError'

# URL error.
INVALIDPARAMETER_URLERROR = 'InvalidParameter.UrlError'

# Version error.
INVALIDPARAMETER_VERSIONERROR = 'InvalidParameter.VersionError'

# Parameter value error.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# BadBody。
INVALIDPARAMETERVALUE_BADBODY = 'InvalidParameterValue.BadBody'

# The request packet is too large.
INVALIDPARAMETERVALUE_BODYTOOLARGE = 'InvalidParameterValue.BodyTooLarge'

# Captcha mismatch.
INVALIDPARAMETERVALUE_CAPMISMATCH = 'InvalidParameterValue.CapMisMatch'

# HTTP method error.
INVALIDPARAMETERVALUE_HTTPMETHODERROR = 'InvalidParameterValue.HttpMethodError'

# Date value error.
INVALIDPARAMETERVALUE_INVALIDDATE = 'InvalidParameterValue.InvalidDate'

# Incorrect PageLimit value.
INVALIDPARAMETERVALUE_INVALIDLIMIT = 'InvalidParameterValue.InvalidLimit'

# PageNum value error.
INVALIDPARAMETERVALUE_INVALIDNUM = 'InvalidParameterValue.InvalidNum'

# SrvId value error.
INVALIDPARAMETERVALUE_INVALIDSRVID = 'InvalidParameterValue.InvalidSrvId'

# Stride value error.
INVALIDPARAMETERVALUE_INVALIDSTRIDE = 'InvalidParameterValue.InvalidStride'

# The quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# Quota exceeded.
LIMITEXCEEDED_FREQCNT = 'LimitExceeded.FreqCnt'

# Quota exceeded (user IP address).
LIMITEXCEEDED_IPFREQCNT = 'LimitExceeded.IpFreqCnt'

# Restricted keyword frequency control.
LIMITEXCEEDED_KEYFREQCNT = 'LimitExceeded.KeyFreqCnt'

# Replay attack.
LIMITEXCEEDED_REPLAYATTACK = 'LimitExceeded.ReplayAttack'

# Parameters are missing
MISSINGPARAMETER = 'MissingParameter'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# Too many and frequent requests.
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# The resource is occupied.
RESOURCEINUSE = 'ResourceInUse'

# Insufficient resources.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The API does not exist.
RESOURCENOTFOUND_INTERFACENOTFOUND = 'ResourceNotFound.InterfaceNotFound'

# Resources are unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# Service permission not activated.
RESOURCEUNAVAILABLE_PERMISSIONDENIED = 'ResourceUnavailable.PermissionDenied'

# Resources are sold out.
RESOURCESSOLDOUT = 'ResourcesSoldOut'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Authentication failed.
UNAUTHORIZEDOPERATION_AUTHFAILED = 'UnauthorizedOperation.AuthFailed'

# Unknown parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'

# The key does not exist.
UNKNOWNPARAMETER_SECRETIDNOTEXISTS = 'UnknownParameter.SecretIdNotExists'

# The operation is not supported.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
