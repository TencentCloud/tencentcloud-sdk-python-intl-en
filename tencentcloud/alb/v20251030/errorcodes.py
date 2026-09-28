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

# DryRun operation means the request will be successful, but the DryRun parameter is passed.
DRYRUNOPERATION = 'DryRunOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Resource already exists.
FAILEDOPERATION_RESOURCEALREADYEXISTS = 'FailedOperation.ResourceAlreadyExists'

# Rule priority already exists.
FAILEDOPERATION_RULEALREADYEXISTS = 'FailedOperation.RuleAlreadyExists'

# Internal error.
INTERNALERROR = 'InternalError'

# Invalid Filter
INVALIDFILTER = 'InvalidFilter'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# Invalid ClientToken format.
INVALIDPARAMETER_INVALIDCLIENTTOKEN = 'InvalidParameter.InvalidClientToken'

# Field format error.
INVALIDPARAMETER_INVALIDFIELDFORMAT = 'InvalidParameter.InvalidFieldFormat'

# Field type error.
INVALIDPARAMETER_INVALIDFIELDTYPE = 'InvalidParameter.InvalidFieldType'

# Field value is incorrect.
INVALIDPARAMETER_INVALIDFIELDVALUE = 'InvalidParameter.InvalidFieldValue'

# Quota check request is invalid.
INVALIDPARAMETER_INVALIDQUOTACHECKREQUEST = 'InvalidParameter.InvalidQuotaCheckRequest'

# Action parameter is missing.
INVALIDPARAMETER_MISSINGACTION = 'InvalidParameter.MissingAction'

# Please enter the required parameter.
INVALIDPARAMETER_MISSINGFIELD = 'InvalidParameter.MissingField'

# Parameter value error.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Business parameter inconsistency.
INVALIDPARAMETERVALUE_BUSINESSPARAMETERMISMATCH = 'InvalidParameterValue.BusinessParameterMismatch'

# The quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# The quota limit is exceeded.
LIMITEXCEEDED_QUOTA = 'LimitExceeded.Quota'

# Parameters are missing.
MISSINGPARAMETER = 'MissingParameter'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# Region error
REGIONERROR = 'RegionError'

# Number of requests exceeds the frequency limit.
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# The resource is occupied.
RESOURCEINUSE = 'ResourceInUse'

# A listener still exists under the instance, so it cannot be deleted.
RESOURCEINUSE_LOADBALANCERHASLISTENERS = 'ResourceInUse.LoadBalancerHasListeners'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# Cert not found.
RESOURCENOTFOUND_CERTIFICATE = 'ResourceNotFound.Certificate'

# Listener not found.
RESOURCENOTFOUND_LISTENER = 'ResourceNotFound.Listener'

# The CLB resource does not exist.
RESOURCENOTFOUND_LOADBALANCER = 'ResourceNotFound.LoadBalancer'

# Forwarding rule not found
RESOURCENOTFOUND_RULE = 'ResourceNotFound.Rule'

# Target group not found.
RESOURCENOTFOUND_TARGETGROUP = 'ResourceNotFound.TargetGroup'

# Resources are unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# The cert is in unavailable status (updating/deleting).
RESOURCEUNAVAILABLE_CERTIFICATE = 'ResourceUnavailable.Certificate'

# Listener is in unavailable status.
RESOURCEUNAVAILABLE_LISTENER = 'ResourceUnavailable.Listener'

# ALB status is unavailable.
RESOURCEUNAVAILABLE_LOADBALANCER = 'ResourceUnavailable.LoadBalancer'

# The previous task is not completed.
RESOURCEUNAVAILABLE_PREVIOUSTASKNOTCOMPLETED = 'ResourceUnavailable.PreviousTaskNotCompleted'

# Rule status unavailable.
RESOURCEUNAVAILABLE_RULE = 'ResourceUnavailable.Rule'

# Target group is in unavailable status
RESOURCEUNAVAILABLE_TARGETGROUP = 'ResourceUnavailable.TargetGroup'

# Resource status of the superior is blocked.
RESOURCEUNAVAILABLE_UPSTREAMSTATUSBLOCKED = 'ResourceUnavailable.UpstreamStatusBlocked'

# Resources are sold out.
RESOURCESSOLDOUT = 'ResourcesSoldOut'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Service role not authorized.
UNAUTHORIZEDOPERATION_SERVICEROLEUNAUTHORIZED = 'UnauthorizedOperation.ServiceRoleUnauthorized'

# Unknown parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'

# The operation is not supported.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# Listener cannot bind a bound cert.
UNSUPPORTEDOPERATION_CERTIFICATEALREADYBOUND = 'UnsupportedOperation.CertificateAlreadyBound'

# The listener is not allowed to unbind an unbound cert.
UNSUPPORTEDOPERATION_CERTIFICATENOTBOUND = 'UnsupportedOperation.CertificateNotBound'

# The listener is not allowed to unbind the default certificate.
UNSUPPORTEDOPERATION_DISASSOCIATEDEFAULTCERTIFICATE = 'UnsupportedOperation.DisassociateDefaultCertificate'

# Invalid state transition.
UNSUPPORTEDOPERATION_INVALIDSTATETRANSITION = 'UnsupportedOperation.InvalidStateTransition'

# Insufficient resources.
UNSUPPORTEDOPERATION_RESOURCESSOLDOUT = 'UnsupportedOperation.ResourcesSoldOut'

# Listener protocol and target group backend forwarding protocol mismatch
UNSUPPORTEDOPERATION_TARGETGROUPPROTOCOLMISMATCH = 'UnsupportedOperation.TargetGroupProtocolMismatch'

# Operation not supported for the CLB listener protocol.
UNSUPPORTEDOPERATION_UNSUPPORTEDPROTOCOL = 'UnsupportedOperation.UnsupportedProtocol'
