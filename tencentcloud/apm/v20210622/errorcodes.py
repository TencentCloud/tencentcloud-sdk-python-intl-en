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

# CAM authentication fails.
AUTHFAILURE_ACCESSCAMFAIL = 'AuthFailure.AccessCAMFail'

# AuthFailure.UnauthorizedOperation
AUTHFAILURE_UNAUTHORIZEDOPERATION = 'AuthFailure.UnauthorizedOperation'

# CAM authentication parsing failed.
AUTHFAILURE_UNMARSHALRESPONSE = 'AuthFailure.UnmarshalResponse'

# DryRun operation means the request will be successful, but the dryrun parameter is passed.
DRYRUNOPERATION = 'DryRunOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Tag access failed.
FAILEDOPERATION_ACCESSTAGFAIL = 'FailedOperation.AccessTagFail'

# The token information does not exist.
FAILEDOPERATION_APMCREDENTIALNOTEXIST = 'FailedOperation.ApmCredentialNotExist'

# The appid does not match the business system information.
FAILEDOPERATION_APPIDNOTMATCHINSTANCEINFO = 'FailedOperation.AppIdNotMatchInstanceInfo'

# Modification to the API is not allowed when the allowlist is not hit and the business system id is the official demo business system id.
FAILEDOPERATION_DEMOINSTANCENOTALLOWMODIFIED = 'FailedOperation.DemoInstanceNotAllowModified'

# Do not enter duplicate application names.
FAILEDOPERATION_DUPLICATESERVICE = 'FailedOperation.DuplicateService'

# Do not enter duplicate Tag names.
FAILEDOPERATION_DUPLICATETAGFIELD = 'FailedOperation.DuplicateTagField'

# Modification of this business system is not allowed.
FAILEDOPERATION_INSTANCECANNOTMODIFY = 'FailedOperation.InstanceCannotModify'

# Destruction of the business system is not allowed.
FAILEDOPERATION_INSTANCECANNOTTERMINATE = 'FailedOperation.InstanceCannotTerminate'

# Business system id is empty.
FAILEDOPERATION_INSTANCEIDISEMPTY = 'FailedOperation.InstanceIdIsEmpty'

# The apm business system does not exist.
FAILEDOPERATION_INSTANCENOTFOUND = 'FailedOperation.InstanceNotFound'

# Invalid business system id.
FAILEDOPERATION_INVALIDINSTANCEID = 'FailedOperation.InvalidInstanceID'

# Invalid input parameter.
FAILEDOPERATION_INVALIDPARAM = 'FailedOperation.InvalidParam'

# Invalid regular expression.
FAILEDOPERATION_INVALIDREGEX = 'FailedOperation.InvalidRegex'

# Invalid request.
FAILEDOPERATION_INVALIDREQUEST = 'FailedOperation.InvalidRequest'

# Business system and application name do not match.
FAILEDOPERATION_INVALIDSERVICENAME = 'FailedOperation.InvalidServiceName'

# Invalid key specified in the tag.
FAILEDOPERATION_INVALIDTAGFIELD = 'FailedOperation.InvalidTagField'

# Invalid token.
FAILEDOPERATION_INVALIDTOKEN = 'FailedOperation.InvalidToken'

# The metric data query lacks filter parameters in the query criteria.
FAILEDOPERATION_METRICFILTERSLACKPARAMS = 'FailedOperation.MetricFiltersLackParams'

# Non-Private vpc.
FAILEDOPERATION_NOTINNERVPC = 'FailedOperation.NotInnerVPC'

# Query time range not supported.
FAILEDOPERATION_QUERYTIMEINTERVALISNOTSUPPORTED = 'FailedOperation.QueryTimeIntervalIsNotSupported'

# This region is not supported.
FAILEDOPERATION_REGIONNOTSUPPORT = 'FailedOperation.RegionNotSupport'

# Failed to send the query request.
FAILEDOPERATION_SENDREQUEST = 'FailedOperation.SendRequest'

# The number of applications exceeds 10.
FAILEDOPERATION_SERVICELISTEXCEEDINGLIMITNUMBER = 'FailedOperation.ServiceListExceedingLimitNumber'

# Application list is empty.
FAILEDOPERATION_SERVICELISTNULL = 'FailedOperation.ServiceListNull'

# The view name does not exist or is invalid.
FAILEDOPERATION_VIEWNAMENOTEXISTORILLEGAL = 'FailedOperation.ViewNameNotExistOrIllegal'

# Internal error.
INTERNALERROR = 'InternalError'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# The field in filters does not exist or is invalid.
INVALIDPARAMETER_FILTERSFIELDSNOTEXISTORILLEGAL = 'InvalidParameter.FiltersFieldsNotExistOrIllegal'

# The field in groupby does not exist or is invalid.
INVALIDPARAMETER_GROUPBYFIELDSNOTEXISTORILLEGAL = 'InvalidParameter.GroupByFieldsNotExistOrIllegal'

# The service.name field must exist in filters, otherwise an error will occur.
INVALIDPARAMETER_METRICFILTERSLACKPARAMS = 'InvalidParameter.MetricFiltersLackParams'

# The field in metrics does not exist or is invalid.
INVALIDPARAMETER_METRICSFIELDNOTEXISTORILLEGAL = 'InvalidParameter.MetricsFieldNotExistOrIllegal'

# Metrics cannot be empty.
INVALIDPARAMETER_METRICSFIELDSNOTALLOWEMPTY = 'InvalidParameter.MetricsFieldsNotAllowEmpty'

# Period should not be empty, and can be 0 or 60.
INVALIDPARAMETER_PERIODISILLEGAL = 'InvalidParameter.PeriodIsIllegal'

# Query time not supported. up to 30 days of recent data can be queried.
INVALIDPARAMETER_QUERYTIMEINTERVALISNOTSUPPORTED = 'InvalidParameter.QueryTimeIntervalIsNotSupported'

# The view name does not exist or is invalid.
INVALIDPARAMETER_VIEWNAMENOTEXISTORILLEGAL = 'InvalidParameter.ViewNameNotExistOrIllegal'
