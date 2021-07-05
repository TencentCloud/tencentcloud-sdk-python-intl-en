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


# CAM signature/authentication error
AUTHFAILURE = 'AuthFailure'

# The DryRun operation means that the request will be successful, but an extra DryRun parameter is passed.
DRYRUNOPERATION = 'DryRunOperation'

# Operation failed
FAILEDOPERATION = 'FailedOperation'

# Failed to enable the logging feature. Please submit a ticket.
FAILEDOPERATION_CLSFAILEDOPERATION = 'FailedOperation.CLSFailedOperation'

# Frequency limit. The interval between the player's repeated request for matchmaking shall not be less than 100 ms.
FAILEDOPERATION_FREQUENCYSAMEPLAYERLIMITED = 'FailedOperation.FrequencySamePlayerLimited'

# The number of the created matches exceeds the limit.
FAILEDOPERATION_LIMITMATCHCOUNT = 'FailedOperation.LimitMatchCount'

# The number of the created rules exceeds the limit.
FAILEDOPERATION_LIMITRULECOUNT = 'FailedOperation.LimitRuleCount'

# System error. If you cannot solve the problem, please submit a ticket.
FAILEDOPERATION_SERVICEUNAVAILABLE = 'FailedOperation.ServiceUnavailable'

# The tagging operation failed
FAILEDOPERATION_TAGSOPEARTIONFAILED = 'FailedOperation.TagsOpeartionFailed'

# Internal error
INTERNALERROR = 'InternalError'

# The API does not exist.
INVALIDACTION = 'InvalidAction'

# Parameter error
INVALIDPARAMETER = 'InvalidParameter'

# Invalid parameter value
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# A GameServerSession is in progress. Start another session until this one is completed.
INVALIDPARAMETERVALUE_GAMESERVERSESSIONREPEATED = 'InvalidParameterValue.GameServerSessionRepeated'

# Incorrect rule script
INVALIDPARAMETERVALUE_INVALIDRULESCRIPT = 'InvalidParameterValue.InvalidRuleScript'

# MatchCode does not exist.
INVALIDPARAMETERVALUE_MATCHCODENOTFOUND = 'InvalidParameterValue.MatchCodeNotFound'

# The length of field value exceeds the limit.
INVALIDPARAMETERVALUE_MATCHFEILDVALUELIMIT = 'InvalidParameterValue.MatchFeildValueLimit'

# Field contains invalid characters.
INVALIDPARAMETERVALUE_MATCHINVALIDCHARACTERS = 'InvalidParameterValue.MatchInvalidCharacters'

# The matchmaking does not exist.
INVALIDPARAMETERVALUE_MATCHNOTFOUND = 'InvalidParameterValue.MatchNotFound'

# The number of players exceeds the limit.
INVALIDPARAMETERVALUE_MATCHPLAYERSLIMIT = 'InvalidParameterValue.MatchPlayersLimit'

# The player ID already exists.
INVALIDPARAMETERVALUE_MATCHPLAYERSREPEATED = 'InvalidParameterValue.MatchPlayersRepeated'

# The matchmaking cannot be canceled under the current status.
INVALIDPARAMETERVALUE_MATCHSTATUSNOTPERMITCANCEL = 'InvalidParameterValue.MatchStatusNotPermitCancel'

# The MatchTicket ID does not exist.
INVALIDPARAMETERVALUE_MATCHTICKETIDNOTFOUND = 'InvalidParameterValue.MatchTicketIdNotFound'

# The MatchTicket ID already exists.
INVALIDPARAMETERVALUE_MATCHTICKETIDREPEATED = 'InvalidParameterValue.MatchTicketIdRepeated'

# The length of MatchTicket list exceeds the limit.
INVALIDPARAMETERVALUE_MATCHTICKETLIMIT = 'InvalidParameterValue.MatchTicketLimit'

# There is a match associated with the rule.
INVALIDPARAMETERVALUE_RULEMATCHEXISTENT = 'InvalidParameterValue.RuleMatchExistent'

# The rule name already exists.
INVALIDPARAMETERVALUE_RULENAMEDUPLICATED = 'InvalidParameterValue.RuleNameDuplicated'

# The rule does not exist.
INVALIDPARAMETERVALUE_RULENOTFOUND = 'InvalidParameterValue.RuleNotFound'

# No permission for this tag
INVALIDPARAMETERVALUE_TAGSLIMITPERMISSION = 'InvalidParameterValue.TagsLimitPermission'

# The CompatibleSpan of the token exceeds the limit.
INVALIDPARAMETERVALUE_TOKENCOMPATIBLESPANINVALID = 'InvalidParameterValue.TokenCompatibleSpanInvalid'

# The token length exceeds the limit.
INVALIDPARAMETERVALUE_TOKENLIMIT = 'InvalidParameterValue.TokenLimit'

# The value exceeds the range.
INVALIDPARAMETERVALUE_VALUERANGELIMIT = 'InvalidParameterValue.ValueRangeLimit'

# Quota limit exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# The token update frequency exceeds the limit.
LIMITEXCEEDED_TOKENUPDATEEXCEED = 'LimitExceeded.TokenUpdateExceed'

# The parameter is missing.
MISSINGPARAMETER = 'MissingParameter'

# API version does not exist.
NOSUCHVERSION = 'NoSuchVersion'

# Operation denied
OPERATIONDENIED = 'OperationDenied'

# The number of requests exceeds the frequency limit.
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# Occupied resource
RESOURCEINUSE = 'ResourceInUse'

# Insufficient resources
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# Resource not found
RESOURCENOTFOUND = 'ResourceNotFound'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# The CLS service has not been activated.
RESOURCEUNAVAILABLE_CLSSERVICENOTACTIVATED = 'ResourceUnavailable.CLSServiceNotActivated'

# The resources have been sold out.
RESOURCESSOLDOUT = 'ResourcesSoldOut'

# The operation is unauthorized.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# It is required to grant the GPM role permissions.
UNAUTHORIZEDOPERATION_CAMUNAUTHORIZEDOPERATION = 'UnauthorizedOperation.CAMUnauthorizedOperation'

# API permission authorization is needed.
UNAUTHORIZEDOPERATION_UNAUTHORIZEDACTION = 'UnauthorizedOperation.UnauthorizedAction'

# The current account has not verified its identity. Please complete identity verification before using the service.
UNAUTHORIZEDOPERATION_USERUNAUTH = 'UnauthorizedOperation.UserUnAuth'

# Unknown parameter error
UNKNOWNPARAMETER = 'UnknownParameter'

# Unsupported operation
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# The API does not support the region passed in.
UNSUPPORTEDREGION = 'UnsupportedRegion'
