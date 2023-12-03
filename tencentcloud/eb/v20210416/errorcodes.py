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

# Failed to add the private link
FAILEDOPERATION_ADDPRIVATELINK = 'FailedOperation.AddPrivateLink'

# User authentication failed
FAILEDOPERATION_AUTHENTICATEUSERFAILED = 'FailedOperation.AuthenticateUserFailed'

# Failed to create the delivery target. Please check the function status.
FAILEDOPERATION_CREATETRIGGER = 'FailedOperation.CreateTrigger'

# Failed to delete the connector. Please check the resource status.
FAILEDOPERATION_DELETECONNECTION = 'FailedOperation.DeleteConnection'

# Failed to delete the private link
FAILEDOPERATION_DELETEPRIVATELINK = 'FailedOperation.DeletePrivateLink'

# Failed to delete the rule. Please make sure the resource exists, and the status is normal.
FAILEDOPERATION_DELETERULE = 'FailedOperation.DeleteRule'

# ES cluster internal error
FAILEDOPERATION_ESINTERNALERROR = 'FailedOperation.ESInternalError'

# ES cluster operation failure
FAILEDOPERATION_ESREQUESTFAILED = 'FailedOperation.ESRequestFailed'

# ES indexing template conflict
FAILEDOPERATION_ESTEMPLATECONFLICT = 'FailedOperation.ESTemplateConflict'

# The rule does not match with the event. Please modify and try again.
FAILEDOPERATION_ERRORFILTER = 'FailedOperation.ErrorFilter'

# Failed to register the CLS service.
FAILEDOPERATION_REGISTERCLSSERVICE = 'FailedOperation.RegisterCLSService'

# ServiceError: operation failed. Please check the resource information.
FAILEDOPERATION_SERVICEERROR = 'FailedOperation.ServiceError'

# Failed to bind the tag
FAILEDOPERATION_TAGRESOURCE = 'FailedOperation.TagResource'

# Failed to apply for more tag quota
FAILEDOPERATION_TAGRESOURCEALLOCATEQUOTAS = 'FailedOperation.TagResourceAllocateQuotas'

# Failed to unbind the tag
FAILEDOPERATION_UNTAGRESOURCE = 'FailedOperation.UnTagResource'

# Failed to update the connector. Please make sure the resource exists, and the status is normal.
FAILEDOPERATION_UPDATECONNECTION = 'FailedOperation.UpdateConnection'

# Failed to update the rule. Please make sure the resource exists, and the status is normal.
FAILEDOPERATION_UPDATERULE = 'FailedOperation.UpdateRule'

# Internal error.
INTERNALERROR = 'InternalError'

# An error occurred while processing the service. Please try again later. If the problem persists, please contact the smart customer service or submit a ticket.
INTERNALERROR_OSSEXCEPTION = 'InternalError.OssException'

# Service error. Please try again. If the problem persists, please submit a ticket.
INTERNALERROR_SYSTEM = 'InternalError.System'

# 
INTERNALERROR_UNKNOWNINTERNALERROR = 'InternalError.UnknownInternalError'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# APIGateway cannot be enabled or disabled. Please check and try again.
INVALIDPARAMETER_ENABLEAPIGATEWAY = 'InvalidParameter.EnableAPIGateway'

# `Payload` does not conform to the specification. Please fix it and try again.
INVALIDPARAMETER_PAYLOAD = 'InvalidParameter.Payload'

# The `AMPParams` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_AMPPARAMS = 'InvalidParameterValue.AMPParams'

# The `Action` value is invalid.
INVALIDPARAMETERVALUE_ACTION = 'InvalidParameterValue.Action'

# The `BatchEventCount` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_BATCHEVENTCOUNT = 'InvalidParameterValue.BatchEventCount'

# The `BatchTimeout` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_BATCHTIMEOUT = 'InvalidParameterValue.BatchTimeout'

# The CKafka parameter is invalid. Please check and try again. 
INVALIDPARAMETERVALUE_CKAFKATARGETPARAMS = 'InvalidParameterValue.CKafkaTargetParams'

# The `CallbackType` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_CALLBACKTYPE = 'InvalidParameterValue.CallbackType'

# The `CallbackWeComURL` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_CALLBACKWECOMURL = 'InvalidParameterValue.CallbackWeComURL'

# The `ConnectionDescription` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_CONNECTIONDESCRIPTION = 'InvalidParameterValue.ConnectionDescription'

# The `ConnectionId` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_CONNECTIONID = 'InvalidParameterValue.ConnectionId'

# The value of `ConnectionName` is invalid. Please check and try again.
INVALIDPARAMETERVALUE_CONNECTIONNAME = 'InvalidParameterValue.ConnectionName'

# The value of `AMPParams` is invalid. Please check and try again.
INVALIDPARAMETERVALUE_DTSPARAMS = 'InvalidParameterValue.DTSParams'

# The dead letter queue parameter is invalid. Please check and try again.
INVALIDPARAMETERVALUE_DEADLETTERCONFIG = 'InvalidParameterValue.DeadLetterConfig'

# The `Description` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_DESCRIPTION = 'InvalidParameterValue.Description'

# ES target parameter error
INVALIDPARAMETERVALUE_ELASTICSEARCHTARGETPARAMS = 'InvalidParameterValue.ElasticSearchTargetParams'

# The `EventBusId` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_EVENTBUSID = 'InvalidParameterValue.EventBusId'

# The value of `EventBusName` is invalid. Please check and try again.
INVALIDPARAMETERVALUE_EVENTBUSNAME = 'InvalidParameterValue.EventBusName'

# The `EventPattern` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_EVENTPATTERN = 'InvalidParameterValue.EventPattern'

# The linkage tracing parameter is invalid. Please check and try again.
INVALIDPARAMETERVALUE_EVENTTRACECONFIG = 'InvalidParameterValue.EventTraceConfig'

# The `Filters` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_FILTERS = 'InvalidParameterValue.Filters'

# The value of `InvalidApiRequestConfig` is invalid. Please check and try again.
INVALIDPARAMETERVALUE_INVALIDAPIREQUESTCONFIG = 'InvalidParameterValue.InvalidApiRequestConfig'

# Invalid event mode format. Please check and try again.
INVALIDPARAMETERVALUE_INVALIDFILTERRULE = 'InvalidParameterValue.InvalidFilterRule'

# Invalid matching rules. Please check and try again.
INVALIDPARAMETERVALUE_INVALIDPATTERN = 'InvalidParameterValue.InvalidPattern'

# The `Limit` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_LIMIT = 'InvalidParameterValue.Limit'

# The value of `LinkMode` is invalid. Please check and try again.
INVALIDPARAMETERVALUE_LINKMODE = 'InvalidParameterValue.LinkMode'

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

# Incorrect tag parameter
INVALIDPARAMETERVALUE_TAGS = 'InvalidParameterValue.Tags'

# The `TargetDescription` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_TARGETDESCRIPTION = 'InvalidParameterValue.TargetDescription'

# The `TargetId` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_TARGETID = 'InvalidParameterValue.TargetId'

# The data transformation parameter is invalid. Please check and try again.
INVALIDPARAMETERVALUE_TRANSFORMATIONID = 'InvalidParameterValue.TransformationID'

# Failed to create the data transformation task: The parameter is invalid. Please check and try again.
INVALIDPARAMETERVALUE_TRANSFORMATIONS = 'InvalidParameterValue.Transformations'

# The `Type` value does not conform to the specification. Please fix it and try again.
INVALIDPARAMETERVALUE_TYPE = 'InvalidParameterValue.Type'

# Reached the upper limit of cluster private links
LIMITEXCEEDED_CLUSTERPRIVATELINKEXCEEDED = 'LimitExceeded.ClusterPrivateLinkExceeded'

# The number of `Connection` reaches the upper limit. You can submit a ticket to increase it.
LIMITEXCEEDED_CONNECTION = 'LimitExceeded.Connection'

# The number of `EventBus` reaches the upper limit. You can submit a ticket to increase it.
LIMITEXCEEDED_EVENTBUS = 'LimitExceeded.EventBus'

# Failed to create the resource: Insufficient balance. Please check and try again.
LIMITEXCEEDED_INSUFFICIENTBALANCE = 'LimitExceeded.InsufficientBalance'

# The `Logset` quantity has reached the upper limit. You can submit a ticket to increase it.
LIMITEXCEEDED_LOGSET = 'LimitExceeded.Logset'

# The number of `RouteOverLimit` reaches the upper limit. Submit a ticket to increase it.
LIMITEXCEEDED_ROUTEOVERLIMIT = 'LimitExceeded.RouteOverLimit'

# The `Rule` quantity has reached the upper limit. You can submit a ticket to increase it.
LIMITEXCEEDED_RULE = 'LimitExceeded.Rule'

# The `Target` quantity has reached the upper limit. You can submit a ticket to increase it.
LIMITEXCEEDED_TARGET = 'LimitExceeded.Target'

# Failed to create the delivery target, as the number of function triggers has reached the limit. You can submit a ticket to increase it.
LIMITEXCEEDED_TRIGGER = 'LimitExceeded.Trigger'

# Reached the upper limit of private links for the user
LIMITEXCEEDED_USERPRIVATELINKEXCEEDED = 'LimitExceeded.UserPrivateLinkExceeded'

# Failed to create the delivery target, as it was detected that the current account did not exist. Please check your account status.
OPERATIONDENIED_ACCOUNTNOTEXISTS = 'OperationDenied.AccountNotExists'

# You cannot create a CLS event target based on the default EventBridge logset in the custom event bus.
OPERATIONDENIED_DEFAULTCLSRESOURCEUNSUPPORTED = 'OperationDenied.DefaultCLSResourceUnsupported'

# The current ES version is not supported.
OPERATIONDENIED_ESVERSIONUNSUPPORTED = 'OperationDenied.ESVersionUnsupported'

# Due to service upgrade, this resource is locked. It may last for about 3-5 minutes. Event pushing is not affected.
OPERATIONDENIED_EVENTBUSRESOURCEISLOCKED = 'OperationDenied.EventBusResourceIsLocked'

# The operation failed, as the resource could not be modified or deleted.
OPERATIONDENIED_RESOURCEIMMUTABLE = 'OperationDenied.ResourceImmutable'

# The current user account type does not support this operation. Please submit a ticket. 
OPERATIONDENIED_UNSUPPORTEDOPERATION = 'OperationDenied.UnsupportedOperation'

# The default Tencent Cloud service event bus cannot be created repeatedly in the same region.
RESOURCEINUSE_DEFAULTEVENTBUS = 'ResourceInUse.DefaultEventBus'

# Failed to delete the event bus. Please first delete all rules, connectors and archives of it. 
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

# The network resource association is not found.
RESOURCENOTFOUND_NETASSOCIATION = 'ResourceNotFound.NetAssociation'

# The privatelink is not found.
RESOURCENOTFOUND_PRIVATELINKRESOURCE = 'ResourceNotFound.PrivateLinkResource'

# The specified service role was not found. Please create it and try again.
RESOURCENOTFOUND_ROLE = 'ResourceNotFound.Role'

# The specified `Rule` was not found. Please create it and try again.
RESOURCENOTFOUND_RULE = 'ResourceNotFound.Rule'

# The specified tag is not found.
RESOURCENOTFOUND_TAG = 'ResourceNotFound.Tag'

# The specified `Target` was not found. Please create it and try again.
RESOURCENOTFOUND_TARGET = 'ResourceNotFound.Target'

# The specified task is not found. Please check and try again.
RESOURCENOTFOUND_TRANSFORMATION = 'ResourceNotFound.Transformation'

# Failed to create the delivery target, as the specified service version was not found. Please create it and try again.
RESOURCENOTFOUND_VERSION = 'ResourceNotFound.Version'

# Failed to create the connector: The current resource is unavailable.
RESOURCEUNAVAILABLE_CONNECTION = 'ResourceUnavailable.Connection'

# ES cluster status error
RESOURCEUNAVAILABLE_ESUNHEALTH = 'ResourceUnavailable.ESUnhealth'

# Failed to create the delivery target, as the current resource was unavailable.
RESOURCEUNAVAILABLE_TARGET = 'ResourceUnavailable.Target'

# The current account does not have permissions to use EB. Please log in to the CAM console for authorization.
UNAUTHORIZEDOPERATION_CAM = 'UnauthorizedOperation.CAM'

# Unsupported operation
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# The connector operation failed, as the API did not support the current operation.
UNSUPPORTEDOPERATION_INVALIDACTION = 'UnsupportedOperation.InvalidAction'

# Failed to create the connector: The current backend service type is not supported.
UNSUPPORTEDOPERATION_INVALIDENDPOINTTYPE = 'UnsupportedOperation.InvalidEndpointType'
