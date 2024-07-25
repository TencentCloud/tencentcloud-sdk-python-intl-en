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

# Duplicate table headers.
FAILEDOPERATION_DUPLICATETABLEHEADER = 'FailedOperation.DuplicateTableHeader'

# Empty table header.
FAILEDOPERATION_EMPTYTABLEHEADER = 'FailedOperation.EmptyTableHeader'

# Incorrect table header.
FAILEDOPERATION_INVALIDTABLEHEADER = 'FailedOperation.InvalidTableHeader'

# Incorrect number of table rows.
FAILEDOPERATION_INVALIDTABLELENGTH = 'FailedOperation.InvalidTableLength'

# Retry count exceeds the upper limit.
FAILEDOPERATION_RETRYLIMITEXCEEDED = 'FailedOperation.RetryLimitExceeded'

# Unsupported status.
FAILEDOPERATION_STATUSNOTSUPPORTED = 'FailedOperation.StatusNotSupported'

# Mismatch exists between table data and type.
FAILEDOPERATION_TABLEDATATYPEMISMATCH = 'FailedOperation.TableDataTypeMismatch'

# Version not released.
FAILEDOPERATION_VERSIONNOTRELEASED = 'FailedOperation.VersionNotReleased'

# Internal error.
INTERNALERROR = 'InternalError'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# Parameter value error.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Duplicated name.
INVALIDPARAMETERVALUE_DUPLICATENAME = 'InvalidParameterValue.DuplicateName'

# Entry file not specified.
INVALIDPARAMETERVALUE_ENTRYPOINTNOTSET = 'InvalidParameterValue.EntrypointNotSet'

# Environment not available.
INVALIDPARAMETERVALUE_ENVIRONMENTNOTAVAILABLE = 'InvalidParameterValue.EnvironmentNotAvailable'

# Base64 encoding error.
INVALIDPARAMETERVALUE_INVALIDBASE64ENCODE = 'InvalidParameterValue.InvalidBase64Encode'

# Incorrect COS path.
INVALIDPARAMETERVALUE_INVALIDCOSKEY = 'InvalidParameterValue.InvalidCosKey'

# Incorrect CSV file format.
INVALIDPARAMETERVALUE_INVALIDCSVFORMAT = 'InvalidParameterValue.InvalidCsvFormat'

# Incorrect description.
INVALIDPARAMETERVALUE_INVALIDDESCRIPTION = 'InvalidParameterValue.InvalidDescription'

# Incorrect input JSON format.
INVALIDPARAMETERVALUE_INVALIDINPUTJSONFORMAT = 'InvalidParameterValue.InvalidInputJsonFormat'

# Incorrect input placeholder.
INVALIDPARAMETERVALUE_INVALIDINPUTPLACEHOLDER = 'InvalidParameterValue.InvalidInputPlaceholder'

# Incorrect name.
INVALIDPARAMETERVALUE_INVALIDNAME = 'InvalidParameterValue.InvalidName'

# Incorrect running parameters.
INVALIDPARAMETERVALUE_INVALIDRUNOPTION = 'InvalidParameterValue.InvalidRunOption'

# Length mismatch exists between table data and type.
INVALIDPARAMETERVALUE_TABLEDATATYPELENGTHMISMATCH = 'InvalidParameterValue.TableDataTypeLengthMismatch'

# Unsupported table data type.
INVALIDPARAMETERVALUE_UNSUPPORTEDTABLEDATATYPE = 'InvalidParameterValue.UnsupportedTableDataType'

# Exceeded the quota limit.
LIMITEXCEEDED = 'LimitExceeded'

# Operation rejected.
OPERATIONDENIED = 'OperationDenied'

# Resources are occupied.
RESOURCEINUSE = 'ResourceInUse'

# Insufficient resources.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The application does not exist.
RESOURCENOTFOUND_APPLICATIONNOTEXIST = 'ResourceNotFound.ApplicationNotExist'

# The application version does not exist.
RESOURCENOTFOUND_APPLICATIONVERSIONNOTEXIST = 'ResourceNotFound.ApplicationVersionNotExist'

# The bucket does not exist.
RESOURCENOTFOUND_COSBUCKETNOTEXIST = 'ResourceNotFound.CosBucketNotExist'

# The storage object does not exist.
RESOURCENOTFOUND_COSOBJECTNOTEXIST = 'ResourceNotFound.CosObjectNotExist'

# The environment does not exist.
RESOURCENOTFOUND_ENVIRONMENTNOTEXIST = 'ResourceNotFound.EnvironmentNotExist'

# The project does not exist.
RESOURCENOTFOUND_PROJECTNOTEXIST = 'ResourceNotFound.ProjectNotExist'

# The run group does not exist.
RESOURCENOTFOUND_RUNGROUPNOTEXIST = 'ResourceNotFound.RunGroupNotExist'

# The run does not exist.
RESOURCENOTFOUND_RUNNOTEXIST = 'ResourceNotFound.RunNotExist'

# The table does not exist.
RESOURCENOTFOUND_TABLENOTEXIST = 'ResourceNotFound.TableNotExist'

# The table row does not exist.
RESOURCENOTFOUND_TABLEROWNOTEXIST = 'ResourceNotFound.TableRowNotExist'

# Resource not available.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
