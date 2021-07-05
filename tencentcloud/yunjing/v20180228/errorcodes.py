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


# The agent is offline.
FAILEDOPERATION_AGENTOFFLINE = 'FailedOperation.AgentOffline'

# Failed to deactivate CWP Pro.
FAILEDOPERATION_CLOSEPROVERSION = 'FailedOperation.CloseProVersion'

# Failed to create a port acquisition task.
FAILEDOPERATION_CREATEOPENPORTTASK = 'FailedOperation.CreateOpenPortTask'

# Failed to create a real-time process acquisition task.
FAILEDOPERATION_CREATEPROCESSTASK = 'FailedOperation.CreateProcessTask'

# Failed to export.
FAILEDOPERATION_EXPORT = 'FailedOperation.Export'

# The server was uninstalled.
FAILEDOPERATION_MACHINEDELETE = 'FailedOperation.MachineDelete'

# The real-time port pulling task does not exist.
FAILEDOPERATION_OPENPORTTASKNOTFOUND = 'FailedOperation.OpenPortTaskNotFound'

# Failed to activate CWP Pro.
FAILEDOPERATION_OPENPROVERSION = 'FailedOperation.OpenProVersion'

# Failed to isolate all or part of servers.
FAILEDOPERATION_PARTSEPARATE = 'FailedOperation.PartSeparate'

# Unable to disable the prepaid Pro edition. Please disable it in Billing Center. 
FAILEDOPERATION_PREPAYMODE = 'FailedOperation.PrePayMode'

# The real-time process pulling task does not exist.
FAILEDOPERATION_PROCESSTASKNOTFOUND = 'FailedOperation.ProcessTaskNotFound'

# Failed to recover the trojan.
FAILEDOPERATION_RECOVER = 'FailedOperation.Recover'

# Failed to scan for vulnerabilities again.
FAILEDOPERATION_RESCANVUL = 'FailedOperation.RescanVul'

# The server already has a rescan task in progress.
FAILEDOPERATION_RESCANVULPROCESSINUSE = 'FailedOperation.RescanVulProcessInUse'

# Failed to isolate a single server.
FAILEDOPERATION_SINGLESEPARATE = 'FailedOperation.SingleSeparate'

# Internal error.
INTERNALERROR = 'InternalError'

# The time range format is incorrect.
INVALIDPARAMETER_DATERANGE = 'InvalidParameter.DateRange'

# Invalid request.
INVALIDPARAMETER_ILLEGALREQUEST = 'InvalidParameter.IllegalRequest'

# Incorrect parameter format.
INVALIDPARAMETER_INVALIDFORMAT = 'InvalidParameter.InvalidFormat'

# Missing parameter.
INVALIDPARAMETER_MISSINGPARAMETER = 'InvalidParameter.MissingParameter'

# Parameter parsing error.
INVALIDPARAMETER_PARSINGERROR = 'InvalidParameter.ParsingError'

# The tag name cannot contain more than 15 characters.
INVALIDPARAMETERVALUE_TAGNAMELENGTHLIMIT = 'InvalidParameterValue.TagNameLengthLimit'

# The maximum number of entries to be added in batches is exceeded.
LIMITEXCEEDED_AREAQUOTA = 'LimitExceeded.AreaQuota'

# Missing parameter.
MISSINGPARAMETER = 'MissingParameter'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'
