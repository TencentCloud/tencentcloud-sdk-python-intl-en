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

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Failed to create the delivery target. Please check the function status.
FAILEDOPERATION_CREATETRIGGER = 'FailedOperation.CreateTrigger'

# Failed to delete the connector. Please check the resource status.
FAILEDOPERATION_DELETECONNECTION = 'FailedOperation.DeleteConnection'

# 
FAILEDOPERATION_ERRORFILTER = 'FailedOperation.ErrorFilter'

# ServiceError: operation failed. Please check the resource information.
FAILEDOPERATION_SERVICEERROR = 'FailedOperation.ServiceError'

# Internal error.
INTERNALERROR = 'InternalError'

# An error occurred while processing the service. Please try again later. If the problem persists, please contact the smart customer service or submit a ticket.
INTERNALERROR_OSSEXCEPTION = 'InternalError.OssException'

# An error occurred while processing the service. Please try again later. If the problem persists, please contact the smart customer service or submit a ticket.
INTERNALERROR_SYSTEM = 'InternalError.System'

# Incorrect parameter.
INVALIDPARAMETER = 'InvalidParameter'

# `Payload` does not conform to the specification. Please fix it and try again.
INVALIDPARAMETER_PAYLOAD = 'InvalidParameter.Payload'

# The `AMPParams` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_AMPPARAMS = 'InvalidParameterValue.AMPParams'

# The `BatchEventCount` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_BATCHEVENTCOUNT = 'InvalidParameterValue.BatchEventCount'

# The `BatchTimeout` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_BATCHTIMEOUT = 'InvalidParameterValue.BatchTimeout'

# The `CallbackType` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_CALLBACKTYPE = 'InvalidParameterValue.CallbackType'

# The `CallbackWeComURL` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_CALLBACKWECOMURL = 'InvalidParameterValue.CallbackWeComURL'

# The `ConnectionDescription` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_CONNECTIONDESCRIPTION = 'InvalidParameterValue.ConnectionDescription'

# The `ConnectionId` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_CONNECTIONID = 'InvalidParameterValue.ConnectionId'

# The `ConnectionName` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_CONNECTIONNAME = 'InvalidParameterValue.ConnectionName'

# The `Description` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_DESCRIPTION = 'InvalidParameterValue.Description'

# The `EventBusId` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_EVENTBUSID = 'InvalidParameterValue.EventBusId'

# The `EventBusName` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_EVENTBUSNAME = 'InvalidParameterValue.EventBusName'

# The `EventPattern` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_EVENTPATTERN = 'InvalidParameterValue.EventPattern'

# The `Filters` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_FILTERS = 'InvalidParameterValue.Filters'

# The `InvalidApiRequestConfig` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_INVALIDAPIREQUESTCONFIG = 'InvalidParameterValue.InvalidApiRequestConfig'

# The `Limit` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_LIMIT = 'InvalidParameterValue.Limit'

# The `NoticeReceiverChannel` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_NOTICERECEIVERCHANNEL = 'InvalidParameterValue.NoticeReceiverChannel'

# The `NoticeReceiverTimeWindow` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_NOTICERECEIVERTIMEWINDOW = 'InvalidParameterValue.NoticeReceiverTimeWindow'

# The `NoticeReceiverUserIds` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_NOTICERECEIVERUSERIDS = 'InvalidParameterValue.NoticeReceiverUserIds'

# The `NoticeReceiverUserType` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_NOTICERECEIVERUSERTYPE = 'InvalidParameterValue.NoticeReceiverUserType'

# The `Offset` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_OFFSET = 'InvalidParameterValue.Offset'

# The `Order` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_ORDER = 'InvalidParameterValue.Order'

# The `OrderBy` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_ORDERBY = 'InvalidParameterValue.OrderBy'

# The `Qualifier` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_QUALIFIER = 'InvalidParameterValue.Qualifier'

# The `RuleId` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_RULEID = 'InvalidParameterValue.RuleId'

# The `RuleName` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_RULENAME = 'InvalidParameterValue.RuleName'

# The `TargetDescription` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_TARGETDESCRIPTION = 'InvalidParameterValue.TargetDescription'

# The `TargetId` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_TARGETID = 'InvalidParameterValue.TargetId'

# The `Type` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_TYPE = 'InvalidParameterValue.Type'

# The `Connection` quantity has reached the upper limit. You can submit a ticket to increase it.
LIMITEXCEEDED_CONNECTION = 'LimitExceeded.Connection'

# The `EventBus` quantity has reached the upper limit. You can submit a ticket to increase it.
LIMITEXCEEDED_EVENTBUS = 'LimitExceeded.EventBus'

# The `Logset` quantity has reached the upper limit. You can submit a ticket to increase it.
LIMITEXCEEDED_LOGSET = 'LimitExceeded.Logset'

# The `RouteOverLimit` quantity has reached the upper limit. You can submit a ticket to increase it.
LIMITEXCEEDED_ROUTEOVERLIMIT = 'LimitExceeded.RouteOverLimit'

# The `Rule` quantity has reached the upper limit. You can submit a ticket to increase it.
LIMITEXCEEDED_RULE = 'LimitExceeded.Rule'

# The `Target` quantity has reached the upper limit. You can submit a ticket to increase it.
LIMITEXCEEDED_TARGET = 'LimitExceeded.Target'

# Failed to create the delivery target, as the number of function triggers has reached the limit. You can submit a ticket to increase it.
LIMITEXCEEDED_TRIGGER = 'LimitExceeded.Trigger'

# Failed to create the delivery target, as it was detected that the current account did not exist. Please check your account status.
OPERATIONDENIED_ACCOUNTNOTEXISTS = 'OperationDenied.AccountNotExists'

# 
OPERATIONDENIED_DEFAULTCLSRESOURCEUNSUPPORTED = 'OperationDenied.DefaultCLSResourceUnsupported'

# The operation failed, as the resource could not be modified or deleted.
OPERATIONDENIED_RESOURCEIMMUTABLE = 'OperationDenied.ResourceImmutable'

# The default Tencent Cloud service event bus cannot be created repeatedly in the same region.
RESOURCEINUSE_DEFAULTEVENTBUS = 'ResourceInUse.DefaultEventBus'

# There are rules or connectors under the event bus, so it cannot be deleted. Please delete all rules and connectors and try again.
RESOURCEINUSE_EVENTBUS = 'ResourceInUse.EventBus'

# There are targets under the rule, so it cannot be deleted. Please delete all targets and try again.
RESOURCEINUSE_RULE = 'ResourceInUse.Rule'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The specified `Connection` was not found. Please create it and try again.
RESOURCENOTFOUND_CONNECTION = 'ResourceNotFound.Connection'

# The specified event bus was not found. Please create it and try again.
RESOURCENOTFOUND_EVENTBUS = 'ResourceNotFound.EventBus'

# The specified `Function` was not found. Please create it and try again.
RESOURCENOTFOUND_FUNCTION = 'ResourceNotFound.Function'

# Failed to delete the connector, as the specified API was not found.
RESOURCENOTFOUND_INVALIDAPI = 'ResourceNotFound.InvalidApi'

# The connector operation failed, as the specified API Gateway service was not found.
RESOURCENOTFOUND_INVALIDSERVICE = 'ResourceNotFound.InvalidService'

# Failed to create the delivery target, as the specified namespace was not found. Please create it and try again.
RESOURCENOTFOUND_NAMESPACE = 'ResourceNotFound.Namespace'

# The specified service role was not found. Please create it and try again.
RESOURCENOTFOUND_ROLE = 'ResourceNotFound.Role'

# The specified `Rule` was not found. Please create it and try again.
RESOURCENOTFOUND_RULE = 'ResourceNotFound.Rule'

# The specified `Target` was not found. Please create it and try again.
RESOURCENOTFOUND_TARGET = 'ResourceNotFound.Target'

# Failed to create the delivery target, as the specified service version was not found. Please create it and try again.
RESOURCENOTFOUND_VERSION = 'ResourceNotFound.Version'

# Failed to create the connector, as the current resource was unavailable.
RESOURCEUNAVAILABLE_CONNECTION = 'ResourceUnavailable.Connection'

# Failed to create the delivery target, as the current resource was unavailable.
RESOURCEUNAVAILABLE_TARGET = 'ResourceUnavailable.Target'

# The current account does not have permissions to use EB. Please log in to the CAM console for authorization.
UNAUTHORIZEDOPERATION_CAM = 'UnauthorizedOperation.CAM'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# The connector operation failed, as the API did not support the current operation.
UNSUPPORTEDOPERATION_INVALIDACTION = 'UnsupportedOperation.InvalidAction'

# Failed to create the connector, as the current backend service type was not supported.
UNSUPPORTEDOPERATION_INVALIDENDPOINTTYPE = 'UnsupportedOperation.InvalidEndpointType'
