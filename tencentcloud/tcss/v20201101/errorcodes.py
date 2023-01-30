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


# A CAM signature/authentication error occurred.
AUTHFAILURE = 'AuthFailure'

# The operation failed.
FAILEDOPERATION = 'FailedOperation'

# The agent is offline.
FAILEDOPERATION_AGENTOFFLINE = 'FailedOperation.AgentOffline'

# Licenses are insufficient.
FAILEDOPERATION_AUTHORIZEDNOTENOUGH = 'FailedOperation.AuthorizedNotEnough'

# The response data value is incorrect.
FAILEDOPERATION_DATAVALUENOTCORRECT = 'FailedOperation.DataValueNotCorrect'

# The scan is in progress or there is no scan permission. We recommend you perform the scan after authorization.
FAILEDOPERATION_ERRALREADYSCANNING = 'FailedOperation.ErrAlreadyScanning'

# The rule is not found.
FAILEDOPERATION_ERRRULENOTFIND = 'FailedOperation.ErrRuleNotFind'

# The notification policy change failed.
FAILEDOPERATION_NOTIFYPOLICYCHANGEFAILED = 'FailedOperation.NotifyPolicyChangeFailed'

# Too many sub-rules were configured.
FAILEDOPERATION_RULECONFIGTOOMANY = 'FailedOperation.RuleConfigTooMany'

# The rule information already exists.
FAILEDOPERATION_RULEINFOREPEAT = 'FailedOperation.RuleInfoRepeat'

# The rule name already exists.
FAILEDOPERATION_RULENAMEREPEAT = 'FailedOperation.RuleNameRepeat'

# The rule is not found.
FAILEDOPERATION_RULENOTFIND = 'FailedOperation.RuleNotFind'

# Too many images were selected.
FAILEDOPERATION_RULESELECTIMAGEOUTRANGE = 'FailedOperation.RuleSelectImageOutRange'

# An internal error occurred.
INTERNALERROR = 'InternalError'

# The user is unauthorized.
INTERNALERROR_ERRROLENOTEXIST = 'InternalError.ErrRoleNotExist'

# The database operation failed.
INTERNALERROR_MAINDBFAIL = 'InternalError.MainDBFail'

# The parameter is incorrect.
INVALIDPARAMETER = 'InvalidParameter'

# The IP format is invalid.
INVALIDPARAMETER_ERRIPNOVALID = 'InvalidParameter.ErrIpNoValid'

# The parameter format is incorrect.
INVALIDPARAMETER_INVALIDFORMAT = 'InvalidParameter.InvalidFormat'

# The required parameter is missing.
INVALIDPARAMETER_MISSINGPARAMETER = 'InvalidParameter.MissingParameter'

# A parameter parsing error occurred.
INVALIDPARAMETER_PARSINGERROR = 'InvalidParameter.ParsingError'

# The port format is invalid.
INVALIDPARAMETER_PORTNOVALID = 'InvalidParameter.PortNoValid'

# The process name, target IP, and target port cannot be empty at the same time.
INVALIDPARAMETER_REVERSHELLKEYFIELDALLEMPTY = 'InvalidParameter.ReverShellKeyFieldAllEmpty'

# The current rule parameter is invalid.
INVALIDPARAMETER_RULEINFOINVALID = 'InvalidParameter.RuleInfoInValid'

# The parameter value is incorrect.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The current data was not found.
INVALIDPARAMETERVALUE_DATANOTFOUND = 'InvalidParameterValue.DataNotFound'

# The data range is incorrect.
INVALIDPARAMETERVALUE_DATARANGE = 'InvalidParameterValue.DataRange'

# The parameter length is limited.
INVALIDPARAMETERVALUE_LENGTHLIMIT = 'InvalidParameterValue.LengthLimit'

# The quota limit has been reached.
LIMITEXCEEDED = 'LimitExceeded'

# The parameter is missing.
MISSINGPARAMETER = 'MissingParameter'

# The operation was denied.
OPERATIONDENIED = 'OperationDenied'

# The number of requests exceeds the frequency limit.
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# The resource is in use.
RESOURCEINUSE = 'ResourceInUse'

# Resources are insufficient.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# The operation is unauthorized.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# The parameter is unknown.
UNKNOWNPARAMETER = 'UnknownParameter'
