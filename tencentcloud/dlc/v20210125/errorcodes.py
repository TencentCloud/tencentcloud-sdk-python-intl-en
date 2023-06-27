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

# The operation failed.
FAILEDOPERATION = 'FailedOperation'

# Order status exception.
FAILEDOPERATION_ABNORMALORDERSTATUS = 'FailedOperation.AbnormalOrderStatus'

# Another data source is being created.
FAILEDOPERATION_ANOTHERCREATEPROCESSRUNNING = 'FailedOperation.AnotherCreateProcessRunning'

# Another operation is in progress. Please try again later.
FAILEDOPERATION_ANOTHERPROCESSRUNNING = 'FailedOperation.AnotherProcessRunning'

# Another request is being processed. Try again later.
FAILEDOPERATION_ANOTHERREQUESTPROCESSING = 'FailedOperation.AnotherRequestProcessing'

# Insufficient account balance.
FAILEDOPERATION_BALANCENOTENOUGH = 'FailedOperation.BalanceNotEnough'

# Billing system exception.
FAILEDOPERATION_BILLINGSYSTEMERROR = 'FailedOperation.BillingSystemError'

# The number of tags set reached the limit.
FAILEDOPERATION_BINDTOOMANYTAGS = 'FailedOperation.BindTooManyTags'

# Failed to create the engine.
FAILEDOPERATION_CREATEDATAENGINEFAILED = 'FailedOperation.CreateDataEngineFailed'

# Failed to deliver the goods.
FAILEDOPERATION_DELIVERGOODSFAILED = 'FailedOperation.DeliverGoodsFailed'

# Duplicate tag keys.
FAILEDOPERATION_DUPLICATETAGKEY = 'FailedOperation.DuplicateTagKey'

# Deduction failed.
FAILEDOPERATION_FEEDEDUCTIONFAILED = 'FailedOperation.FeeDeductionFailed'

# Failed to get product information.
FAILEDOPERATION_GETPRODUCTINFORMATIONFAILED = 'FailedOperation.GetProductInformationFailed'

# The HTTP client request failed.
FAILEDOPERATION_HTTPCLIENTDOREQUESTFAILED = 'FailedOperation.HttpClientDoRequestFailed'

# Invalid resources.
FAILEDOPERATION_ILLEGALRESOURCE = 'FailedOperation.IllegalResource'

# Invalid characters in the tag key.
FAILEDOPERATION_ILLEGALTAGKEY = 'FailedOperation.IllegalTagKey'

# Invalid characters in the tag value.
FAILEDOPERATION_ILLEGALTAGVALUE = 'FailedOperation.IllegalTagValue'

# Price query failed.
FAILEDOPERATION_INQUIREPRICEFAILED = 'FailedOperation.InquirePriceFailed'

# Failed to scale up/down the instance.
FAILEDOPERATION_MODIFYINSTANCEFAILED = 'FailedOperation.ModifyInstanceFailed'

# No permission.
FAILEDOPERATION_NOPERMISSION = 'FailedOperation.NoPermission'

# Unverified account.
FAILEDOPERATION_NOREALNAMEAUTHENTICATION = 'FailedOperation.NoRealNameAuthentication'

# Reached the allowed limit of engines.
FAILEDOPERATION_NUMBEREXCEEDLIMIT = 'FailedOperation.NumberExceedLimit'

# Failed to verify parameters.
FAILEDOPERATION_PARAMETERVALIDATIONFAILED = 'FailedOperation.ParameterValidationFailed'

# Refunding failed.
FAILEDOPERATION_REFUNDDEPOSITFAILED = 'FailedOperation.RefundDepositFailed'

# A tag key of the same name has been set for the resource.
FAILEDOPERATION_TAGALREADYATTACHED = 'FailedOperation.TagAlreadyAttached'

# The tag key exceeded the length limit.
FAILEDOPERATION_TAGKEYTOOLONG = 'FailedOperation.TagKeyTooLong'

# The tag does not exist.
FAILEDOPERATION_TAGNOTEXIST = 'FailedOperation.TagNotExist'

# The tag value exceeded the length limit.
FAILEDOPERATION_TAGVALUETOOLONG = 'FailedOperation.TagValueTooLong'

# The number of resources reached the limit.
FAILEDOPERATION_TOOMANYRESOURCES = 'FailedOperation.TooManyResources'

# The number of tags reached the limit.
FAILEDOPERATION_TOOMANYTAGS = 'FailedOperation.TooManyTags'

# An internal error occurred.
INTERNALERROR = 'InternalError'

# A database error occurred.
INTERNALERROR_DBERROR = 'InternalError.DBError'

# The parameter is incorrect.
INVALIDPARAMETER = 'InvalidParameter'

# Duplicate engine name.
INVALIDPARAMETER_DUPLICATEDATAENGINENAME = 'InvalidParameter.DuplicateDataEngineName'

# Invalid data engine mode.
INVALIDPARAMETER_INVALIDDATAENGINEMODE = 'InvalidParameter.InvalidDataEngineMode'

# The data engine name is invalid.
INVALIDPARAMETER_INVALIDDATAENGINENAME = 'InvalidParameter.InvalidDataEngineName'

# Invalid data engine spec.
INVALIDPARAMETER_INVALIDDATAENGINESPECS = 'InvalidParameter.InvalidDataEngineSpecs'

# Invalid engine type.
INVALIDPARAMETER_INVALIDENGINETYPE = 'InvalidParameter.InvalidEngineType'

# The fault tolerance policy is invalid.
INVALIDPARAMETER_INVALIDFAILURETOLERANCE = 'InvalidParameter.InvalidFailureTolerance'

# Invalid maximum number of results.
INVALIDPARAMETER_INVALIDMAXRESULTS = 'InvalidParameter.InvalidMaxResults'

# Invalid billing mode.
INVALIDPARAMETER_INVALIDPAYMODE = 'InvalidParameter.InvalidPayMode'

# The CAM role arn is invalid.
INVALIDPARAMETER_INVALIDROLEARN = 'InvalidParameter.InvalidRoleArn'

# SQL parsing failed.
INVALIDPARAMETER_INVALIDSQL = 'InvalidParameter.InvalidSQL'

# The number of SQL statements does not meet the specification.
INVALIDPARAMETER_INVALIDSQLNUM = 'InvalidParameter.InvalidSQLNum'

# The `SparkAppParam` is invalid.
INVALIDPARAMETER_INVALIDSPARKAPPPARAM = 'InvalidParameter.InvalidSparkAppParam'

# The storage location is incorrect.
INVALIDPARAMETER_INVALIDSTORELOCATION = 'InvalidParameter.InvalidStoreLocation'

# The `taskid` is invalid.
INVALIDPARAMETER_INVALIDTASKID = 'InvalidParameter.InvalidTaskId'

# The task type is invalid.
INVALIDPARAMETER_INVALIDTASKTYPE = 'InvalidParameter.InvalidTaskType'

# Invalid billing period.
INVALIDPARAMETER_INVALIDTIMESPAN = 'InvalidParameter.InvalidTimeSpan'

# Invalid unit of billing period.
INVALIDPARAMETER_INVALIDTIMEUNIT = 'InvalidParameter.InvalidTimeUnit'

# The task has ended and cannot be canceled.
INVALIDPARAMETER_TASKALREADYFINISHED = 'InvalidParameter.TaskAlreadyFinished'

# Invalid VPC CIDR format.
INVALIDPARAMETER_VPCCIDRFORMATERROR = 'InvalidParameter.VpcCidrFormatError'

# The parameter value is incorrect.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The quota limit is reached.
LIMITEXCEEDED = 'LimitExceeded'

# Missing parameters.
MISSINGPARAMETER = 'MissingParameter'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# No resources are available to create a session currently. Please try again later or use a monthly subscription cluster.
RESOURCENOTFOUND_RESOURCENOTFOUNDCODE_SESSIONINSUFFICIENTRESOURCES = 'ResourceNotFound.ResourceNotFoundCode_SessionInsufficientResources'

# The result path was not found.
RESOURCENOTFOUND_RESULTOUTPUTPATHNOTFOUND = 'ResourceNotFound.ResultOutputPathNotFound'

# The session does not exist.
RESOURCENOTFOUND_SESSIONNOTFOUND = 'ResourceNotFound.SessionNotFound'

# The session has expired.
RESOURCENOTFOUND_SESSIONSTATEDEAD = 'ResourceNotFound.SessionStateDead'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# The account balance is insufficient to run the SQL task.
RESOURCEUNAVAILABLE_BALANCEINSUFFICIENT = 'ResourceUnavailable.BalanceInsufficient'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# No permission to pay.
UNAUTHORIZEDOPERATION_NOPAYMENTAUTHORITY = 'UnauthorizedOperation.NoPaymentAuthority'

# Unauthorized engine operation by a sub-user.
UNAUTHORIZEDOPERATION_OPERATECOMPUTINGENGINE = 'UnauthorizedOperation.OperateComputingEngine'

# The sub-user does not have permission to use the compute engine.
UNAUTHORIZEDOPERATION_USECOMPUTINGENGINE = 'UnauthorizedOperation.UseComputingEngine'

# Unknown parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
