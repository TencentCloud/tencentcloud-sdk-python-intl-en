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

# DryRun operation, which means the DryRun parameter is passed in yet the request will still be successful.
DRYRUNOPERATION = 'DryRunOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# FailedOperation.InvalidContext
FAILEDOPERATION_INVALIDCONTEXT = 'FailedOperation.InvalidContext'

# FailedOperation.QueryError
FAILEDOPERATION_QUERYERROR = 'FailedOperation.QueryError'

# FailedOperation.ResponseTooLarge
FAILEDOPERATION_RESPONSETOOLARGE = 'FailedOperation.ResponseTooLarge'

# FailedOperation.SearchTimeout
FAILEDOPERATION_SEARCHTIMEOUT = 'FailedOperation.SearchTimeout'

# FailedOperation.SyntaxError
FAILEDOPERATION_SYNTAXERROR = 'FailedOperation.SyntaxError'

# FailedOperation.Timeout
FAILEDOPERATION_TIMEOUT = 'FailedOperation.Timeout'

# FailedOperation.TopicIsolated
FAILEDOPERATION_TOPICISOLATED = 'FailedOperation.TopicIsolated'

# Internal error.
INTERNALERROR = 'InternalError'

# InternalError.SearchError
INTERNALERROR_SEARCHERROR = 'InternalError.SearchError'

# InternalError.SearchFailed
INTERNALERROR_SEARCHFAILED = 'InternalError.SearchFailed'

# InternalError.ServerBusy
INTERNALERROR_SERVERBUSY = 'InternalError.ServerBusy'

# Invalid parameter.
INVALIDPARAMETER = 'InvalidParameter'

# Invalid parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The quota limit has been reached.
LIMITEXCEEDED = 'LimitExceeded'

# LimitExceeded.LogSearch
LIMITEXCEEDED_LOGSEARCH = 'LimitExceeded.LogSearch'

# LimitExceeded.SearchResources
LIMITEXCEEDED_SEARCHRESOURCES = 'LimitExceeded.SearchResources'

# LimitExceeded.SearchResultTooLarge
LIMITEXCEEDED_SEARCHRESULTTOOLARGE = 'LimitExceeded.SearchResultTooLarge'

# Missing parameter.
MISSINGPARAMETER = 'MissingParameter'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# OperationDenied.AccountDestroy
OPERATIONDENIED_ACCOUNTDESTROY = 'OperationDenied.AccountDestroy'

# OperationDenied.AccountIsolate
OPERATIONDENIED_ACCOUNTISOLATE = 'OperationDenied.AccountIsolate'

# OperationDenied.AccountNotExists
OPERATIONDENIED_ACCOUNTNOTEXISTS = 'OperationDenied.AccountNotExists'

# OperationDenied.NewSyntaxNotSupported
OPERATIONDENIED_NEWSYNTAXNOTSUPPORTED = 'OperationDenied.NewSyntaxNotSupported'

# OperationDenied.OperationNotSupportInSearchLow
OPERATIONDENIED_OPERATIONNOTSUPPORTINSEARCHLOW = 'OperationDenied.OperationNotSupportInSearchLow'

# The number of requests exceeds the frequency limit.
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# The resource is occupied.
RESOURCEINUSE = 'ResourceInUse'

# Insufficient resource.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# ResourceNotFound.TopicNotExist
RESOURCENOTFOUND_TOPICNOTEXIST = 'ResourceNotFound.TopicNotExist'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# The resources have been sold out.
RESOURCESSOLDOUT = 'ResourcesSoldOut'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Unknown parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
