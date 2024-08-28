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

# Authentication for the current user failed.
AUTHFAILURE_UNAUTHORIZEDOPERATION = 'AuthFailure.UnauthorizedOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Failed to invoke the API service.
FAILEDOPERATION_APISERVERFAIL = 'FailedOperation.APIServerFail'

# The client is offline.
FAILEDOPERATION_AGENTOFFLINE = 'FailedOperation.AgentOffline'

# Failed to export the file.
FAILEDOPERATION_EXPORT = 'FailedOperation.Export'

# Insufficient available licenses, missing 1 license. Purchase a new license.
FAILEDOPERATION_LICENSEEXCEEDED = 'FailedOperation.LicenseExceeded'

# Uninstall the host.
FAILEDOPERATION_MACHINEDELETE = 'FailedOperation.MachineDelete'

# No Pro Edition host.
FAILEDOPERATION_NOPROFESSIONHOST = 'FailedOperation.NoProfessionHost'

# Isolation of multiple hosts partially or completely failed.
FAILEDOPERATION_PARTSEPARATE = 'FailedOperation.PartSeparate'

# Failed to respond to the Trojan.
FAILEDOPERATION_RECOVER = 'FailedOperation.Recover'

# Failed to double-check the vulnerability.
FAILEDOPERATION_RESCANVUL = 'FailedOperation.RescanVul'

# Isolation of a single host failed.
FAILEDOPERATION_SINGLESEPARATE = 'FailedOperation.SingleSeparate'

# The maximum number for baseline policy creation is exceeded.
FAILEDOPERATION_TOOMANYSTRATEGY = 'FailedOperation.TooManyStrategy'

# Internal error
INTERNALERROR = 'InternalError'

# Failed to manipulate the data.
INTERNALERROR_MAINDBFAIL = 'InternalError.MainDBFail'

# Incorrect parameter.
INVALIDPARAMETER = 'InvalidParameter'

# Incorrect time range format.
INVALIDPARAMETER_DATERANGE = 'InvalidParameter.DateRange'

# Invalid request.
INVALIDPARAMETER_ILLEGALREQUEST = 'InvalidParameter.IllegalRequest'

# Incorrect parameter format.
INVALIDPARAMETER_INVALIDFORMAT = 'InvalidParameter.InvalidFormat'

# The IP format is invalid.
INVALIDPARAMETER_IPNOVALID = 'InvalidParameter.IpNoValid'

# Missing parameter.
INVALIDPARAMETER_MISSINGPARAMETER = 'InvalidParameter.MissingParameter'

# The name already exists.
INVALIDPARAMETER_NAMEHASREPETITION = 'InvalidParameter.NameHasRepetition'

# Incorrect parameter parsing.
INVALIDPARAMETER_PARSINGERROR = 'InvalidParameter.ParsingError'

# Invalid port format.
INVALIDPARAMETER_PORTNOVALID = 'InvalidParameter.PortNoValid'

# The regular expression parameter format is incorrect.
INVALIDPARAMETER_REGEXRULEERROR = 'InvalidParameter.RegexRuleError'

# Process name/target IP/target port cannot be left blank simultaneously.
INVALIDPARAMETER_REVERSHELLKEYFIELDALLEMPTY = 'InvalidParameter.ReverShellKeyFieldAllEmpty'

# Rule-based API with duplicate hosts.
INVALIDPARAMETER_RULEHOSTDUPLICATEERR = 'InvalidParameter.RuleHostDuplicateErr'

# Rule-based API with incorrect host IPs.
INVALIDPARAMETER_RULEHOSTIPERR = 'InvalidParameter.RuleHostipErr'

# Invalid parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The tag name cannot exceed 15 characters.
INVALIDPARAMETERVALUE_TAGNAMELENGTHLIMIT = 'InvalidParameterValue.TagNameLengthLimit'

# The quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# The maximum number for batch addition is exceeded.
LIMITEXCEEDED_AREAQUOTA = 'LimitExceeded.AreaQuota'

# Missing parameter error.
MISSINGPARAMETER = 'MissingParameter'

# The operation was denied.
OPERATIONDENIED = 'OperationDenied'

# The resource is occupied.
RESOURCEINUSE = 'ResourceInUse'

# Insufficient resources.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The scanning machine does not exist.
RESOURCENOTFOUND_MACHINENOTFOUND = 'ResourceNotFound.MachineNotFound'

# The resource is not available.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Unknow parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'

# The operation is not supported.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
