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

# 
FAILEDOPERATION_NOPERMISSIONTOUSETHEDATAENGINE = 'FailedOperation.NoPermissionToUseTheDataEngine'

# Unverified account.
FAILEDOPERATION_NOREALNAMEAUTHENTICATION = 'FailedOperation.NoRealNameAuthentication'

# Reached the allowed limit of engines.
FAILEDOPERATION_NUMBEREXCEEDLIMIT = 'FailedOperation.NumberExceedLimit'

# Failed to verify parameters.
FAILEDOPERATION_PARAMETERVALIDATIONFAILED = 'FailedOperation.ParameterValidationFailed'

# Refunding failed.
FAILEDOPERATION_REFUNDDEPOSITFAILED = 'FailedOperation.RefundDepositFailed'

# 
FAILEDOPERATION_SQLTASKPARSEFAILED = 'FailedOperation.SQLTaskParseFailed'

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

# 
INTERNALERROR_INTERNALSYSTEMEXCEPTION = 'InternalError.InternalSystemException'

# The parameter is incorrect.
INVALIDPARAMETER = 'InvalidParameter'

# 
INVALIDPARAMETER_BATCHSQLCUSTOMKEYNOTUNIQUE = 'InvalidParameter.BatchSQLCustomKeyNotUnique'

# 
INVALIDPARAMETER_DATAENGINECLUSTERTYPENOTMATCH = 'InvalidParameter.DataEngineClusterTypeNotMatch'

# 
INVALIDPARAMETER_DATAENGINEMODENOTMATCH = 'InvalidParameter.DataEngineModeNotMatch'

# 
INVALIDPARAMETER_DATAENGINEONLYSUPPORTSQL = 'InvalidParameter.DataEngineOnlySupportSQL'

# 
INVALIDPARAMETER_DATAENGINEONLYSUPPORTSPARKBATCH = 'InvalidParameter.DataEngineOnlySupportSparkBatch'

# 
INVALIDPARAMETER_DATAENGINESIZENOTMATCH = 'InvalidParameter.DataEngineSizeNotMatch'

# Duplicate engine name.
INVALIDPARAMETER_DUPLICATEDATAENGINENAME = 'InvalidParameter.DuplicateDataEngineName'

# 
INVALIDPARAMETER_FILTERSVALUESNUMBEROUTOFLIMIT = 'InvalidParameter.FiltersValuesNumberOutOfLimit'

# 
INVALIDPARAMETER_IMAGEENGINETYPENOTMATCH = 'InvalidParameter.ImageEngineTypeNotMatch'

# 
INVALIDPARAMETER_IMAGEISPUBLICNOTMATCH = 'InvalidParameter.ImageIsPublicNotMatch'

# 
INVALIDPARAMETER_IMAGEPARAMETERNOTFOUND = 'InvalidParameter.ImageParameterNotFound'

# 
INVALIDPARAMETER_IMAGEPARAMETERSUBMITMETHODNOTMATCH = 'InvalidParameter.ImageParameterSubmitMethodNotMatch'

# 
INVALIDPARAMETER_IMAGEPARAMETERTYPENOTMATCH = 'InvalidParameter.ImageParameterTypeNotMatch'

# 
INVALIDPARAMETER_IMAGESESSIONPARAMETERSFORMATNOTJSON = 'InvalidParameter.ImageSessionParametersFormatNotJson'

# 
INVALIDPARAMETER_IMAGESTATENOTMATCH = 'InvalidParameter.ImageStateNotMatch'

# 
INVALIDPARAMETER_IMAGEUSERRECORDSTYPENOTMATCH = 'InvalidParameter.ImageUserRecordsTypeNotMatch'

# 
INVALIDPARAMETER_INVALIDAPPFILEFORMAT = 'InvalidParameter.InvalidAppFileFormat'

# 
INVALIDPARAMETER_INVALIDCOLUMNNAMELENGTH = 'InvalidParameter.InvalidColumnNameLength'

# 
INVALIDPARAMETER_INVALIDCOLUMNNUMBER = 'InvalidParameter.InvalidColumnNumber'

# 
INVALIDPARAMETER_INVALIDCONFIGKEYNOTFOUND = 'InvalidParameter.InvalidConfigKeyNotFound'

# 
INVALIDPARAMETER_INVALIDCONFIGVALUELENGTHOUTLIMIT = 'InvalidParameter.InvalidConfigValueLengthOutLimit'

# 
INVALIDPARAMETER_INVALIDCONFIGVALUEREGEXPNOTMATCH = 'InvalidParameter.InvalidConfigValueRegexpNotMatch'

# 
INVALIDPARAMETER_INVALIDDATAENGINECIDRFORMAT = 'InvalidParameter.InvalidDataEngineCidrFormat'

# Invalid data engine mode.
INVALIDPARAMETER_INVALIDDATAENGINEMODE = 'InvalidParameter.InvalidDataEngineMode'

# The data engine name is invalid.
INVALIDPARAMETER_INVALIDDATAENGINENAME = 'InvalidParameter.InvalidDataEngineName'

# Invalid data engine spec.
INVALIDPARAMETER_INVALIDDATAENGINESPECS = 'InvalidParameter.InvalidDataEngineSpecs'

# 
INVALIDPARAMETER_INVALIDDATAENGINETIMESPAN = 'InvalidParameter.InvalidDataEngineTimeSpan'

# 
INVALIDPARAMETER_INVALIDDATAENGINETIMEUNIT = 'InvalidParameter.InvalidDataEngineTimeUnit'

# 
INVALIDPARAMETER_INVALIDDECIMALTYPE = 'InvalidParameter.InvalidDecimalType'

# 
INVALIDPARAMETER_INVALIDDRIVERSIZE = 'InvalidParameter.InvalidDriverSize'

# 
INVALIDPARAMETER_INVALIDDYNAMICALLOCATIONMAXEXECUTORS = 'InvalidParameter.InvalidDynamicAllocationMaxExecutors'

# Invalid engine type.
INVALIDPARAMETER_INVALIDENGINETYPE = 'InvalidParameter.InvalidEngineType'

# 
INVALIDPARAMETER_INVALIDEXECUTORSIZE = 'InvalidParameter.InvalidExecutorSize'

# The fault tolerance policy is invalid.
INVALIDPARAMETER_INVALIDFAILURETOLERANCE = 'InvalidParameter.InvalidFailureTolerance'

# 
INVALIDPARAMETER_INVALIDFILECOMPRESSIONFORMAT = 'InvalidParameter.InvalidFileCompressionFormat'

# 
INVALIDPARAMETER_INVALIDFILEPATHFORMAT = 'InvalidParameter.InvalidFilePathFormat'

# 
INVALIDPARAMETER_INVALIDFILTERLENGTH = 'InvalidParameter.InvalidFilterLength'

# Invalid maximum number of results.
INVALIDPARAMETER_INVALIDMAXRESULTS = 'InvalidParameter.InvalidMaxResults'

# Invalid billing mode.
INVALIDPARAMETER_INVALIDPAYMODE = 'InvalidParameter.InvalidPayMode'

# The CAM role arn is invalid.
INVALIDPARAMETER_INVALIDROLEARN = 'InvalidParameter.InvalidRoleArn'

# SQL parsing failed.
INVALIDPARAMETER_INVALIDSQL = 'InvalidParameter.InvalidSQL'

# 
INVALIDPARAMETER_INVALIDSQLCONFIGSQL = 'InvalidParameter.InvalidSQLConfigSQL'

# The number of SQL statements does not meet the specification.
INVALIDPARAMETER_INVALIDSQLNUM = 'InvalidParameter.InvalidSQLNum'

# 
INVALIDPARAMETER_INVALIDSQLTASKMAXRESULTS = 'InvalidParameter.InvalidSQLTaskMaxResults'

# 
INVALIDPARAMETER_INVALIDSESSIONKINDTYPE = 'InvalidParameter.InvalidSessionKindType'

# The `SparkAppParam` is invalid.
INVALIDPARAMETER_INVALIDSPARKAPPPARAM = 'InvalidParameter.InvalidSparkAppParam'

# 
INVALIDPARAMETER_INVALIDSPARKCONFIGFORMAT = 'InvalidParameter.InvalidSparkConfigFormat'

# 
INVALIDPARAMETER_INVALIDSTATEMENTKINDTYPE = 'InvalidParameter.InvalidStatementKindType'

# The storage location is incorrect.
INVALIDPARAMETER_INVALIDSTORELOCATION = 'InvalidParameter.InvalidStoreLocation'

# 
INVALIDPARAMETER_INVALIDTABLENAMELENGTH = 'InvalidParameter.InvalidTableNameLength'

# The `taskid` is invalid.
INVALIDPARAMETER_INVALIDTASKID = 'InvalidParameter.InvalidTaskId'

# The task type is invalid.
INVALIDPARAMETER_INVALIDTASKTYPE = 'InvalidParameter.InvalidTaskType'

# 
INVALIDPARAMETER_INVALIDTCRSPARKIMAGEFORMAT = 'InvalidParameter.InvalidTcrSparkImageFormat'

# 
INVALIDPARAMETER_INVALIDTIMEFORMAT = 'InvalidParameter.InvalidTimeFormat'

# 
INVALIDPARAMETER_INVALIDTIMEPARAMETER = 'InvalidParameter.InvalidTimeParameter'

# Invalid billing period.
INVALIDPARAMETER_INVALIDTIMESPAN = 'InvalidParameter.InvalidTimeSpan'

# Invalid unit of billing period.
INVALIDPARAMETER_INVALIDTIMEUNIT = 'InvalidParameter.InvalidTimeUnit'

# 
INVALIDPARAMETER_INVALIDWHITELISTKEY = 'InvalidParameter.InvalidWhiteListKey'

# 
INVALIDPARAMETER_MAXRESULTONLYSUPPORTHUNDRED = 'InvalidParameter.MaxResultOnlySupportHundred'

# 
INVALIDPARAMETER_NUMBEROFSQLEXCEEDSTHELIMIT = 'InvalidParameter.NumberOfSQLExceedsTheLimit'

# 
INVALIDPARAMETER_PARAMETERBASE64DECODEFAILED = 'InvalidParameter.ParameterBase64DecodeFailed'

# 
INVALIDPARAMETER_PARAMETERNOTFOUNDORBENONE = 'InvalidParameter.ParameterNotFoundOrBeNone'

# 
INVALIDPARAMETER_SQLBASE64DECODEFAIL = 'InvalidParameter.SQLBase64DecodeFail'

# 
INVALIDPARAMETER_SQLPARAMETERPREPROCESSINGFAILED = 'InvalidParameter.SQLParameterPreprocessingFailed'

# 
INVALIDPARAMETER_SQLTASKFILTERSKEYTYPENOTMATH = 'InvalidParameter.SQLTaskFiltersKeyTypeNotMath'

# 
INVALIDPARAMETER_SQLTASKNOTFOUND = 'InvalidParameter.SQLTaskNotFound'

# 
INVALIDPARAMETER_SQLTASKSORTBYTYPENOTMATCH = 'InvalidParameter.SQLTaskSortByTypeNotMatch'

# 
INVALIDPARAMETER_SPARKJOBFILTERSKEYTYPENOTMATH = 'InvalidParameter.SparkJobFiltersKeyTypeNotMath'

# 
INVALIDPARAMETER_SPARKJOBISINHERITTYPENOTMATCH = 'InvalidParameter.SparkJobIsInheritTypeNotMatch'

# 
INVALIDPARAMETER_SPARKJOBNOTFOUND = 'InvalidParameter.SparkJobNotFound'

# 
INVALIDPARAMETER_SPARKJOBNOTUNIQUE = 'InvalidParameter.SparkJobNotUnique'

# 
INVALIDPARAMETER_SPARKJOBONLYSUPPORTSPARKBATCHENGINE = 'InvalidParameter.SparkJobOnlySupportSparkBatchEngine'

# 
INVALIDPARAMETER_SPARKJOBROLEARNNOTFOUND = 'InvalidParameter.SparkJobRoleArnNotFound'

# 
INVALIDPARAMETER_SPARKJOBSORTBYTYPENOTMATCH = 'InvalidParameter.SparkJobSortByTypeNotMatch'

# The task has ended and cannot be canceled.
INVALIDPARAMETER_TASKALREADYFINISHED = 'InvalidParameter.TaskAlreadyFinished'

# 
INVALIDPARAMETER_TASKSTATETYPENOTMATH = 'InvalidParameter.TaskStateTypeNotMath'

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

# 
RESOURCEINSUFFICIENT_SPARKJOBINSUFFICIENTRESOURCES = 'ResourceInsufficient.SparkJobInsufficientResources'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# 
RESOURCENOTFOUND_BATCHSQLTASKNOTFOUND = 'ResourceNotFound.BatchSQLTaskNotFound'

# 
RESOURCENOTFOUND_BATCHSQLTASKNOTUNIQUE = 'ResourceNotFound.BatchSQLTaskNotUnique'

# 
RESOURCENOTFOUND_DATAENGINECONFIGINSTANCENOTFOUND = 'ResourceNotFound.DataEngineConfigInstanceNotFound'

# 
RESOURCENOTFOUND_DATAENGINECONFIGINSTANCENOTUNIQUE = 'ResourceNotFound.DataEngineConfigInstanceNotUnique'

# 
RESOURCENOTFOUND_DATAENGINENOTACTIVITY = 'ResourceNotFound.DataEngineNotActivity'

# 
RESOURCENOTFOUND_DATAENGINENOTFOUND = 'ResourceNotFound.DataEngineNotFound'

# 
RESOURCENOTFOUND_DATAENGINENOTRUNNING = 'ResourceNotFound.DataEngineNotRunning'

# 
RESOURCENOTFOUND_DATAENGINENOTUNIQUE = 'ResourceNotFound.DataEngineNotUnique'

# 
RESOURCENOTFOUND_DEFAULTDATAENGINENOTFOUND = 'ResourceNotFound.DefaultDataEngineNotFound'

# 
RESOURCENOTFOUND_IMAGESESSIONCONFIGNOTFOUND = 'ResourceNotFound.ImageSessionConfigNotFound'

# 
RESOURCENOTFOUND_IMAGESESSIONCONFIGNOTUNIQUE = 'ResourceNotFound.ImageSessionConfigNotUnique'

# 
RESOURCENOTFOUND_IMAGEVERSIONNOTFOUND = 'ResourceNotFound.ImageVersionNotFound'

# 
RESOURCENOTFOUND_IMAGEVERSIONNOTUNIQUE = 'ResourceNotFound.ImageVersionNotUnique'

# 
RESOURCENOTFOUND_RESOURCEUSAGEOUTOFLIMIT = 'ResourceNotFound.ResourceUsageOutOfLimit'

# The result path was not found.
RESOURCENOTFOUND_RESULTOUTPUTPATHNOTFOUND = 'ResourceNotFound.ResultOutputPathNotFound'

# 
RESOURCENOTFOUND_RESULTSAVEPATHNOTFOUND = 'ResourceNotFound.ResultSavePathNotFound'

# 
RESOURCENOTFOUND_ROLEARNRESOURCENOTFOUND = 'ResourceNotFound.RoleArnResourceNotFound'

# No resources are available to create a session currently. Please try again later or use a monthly subscription cluster.
RESOURCENOTFOUND_SESSIONINSUFFICIENTRESOURCES = 'ResourceNotFound.SessionInsufficientResources'

# The session does not exist.
RESOURCENOTFOUND_SESSIONNOTFOUND = 'ResourceNotFound.SessionNotFound'

# The session has expired.
RESOURCENOTFOUND_SESSIONSTATEDEAD = 'ResourceNotFound.SessionStateDead'

# 
RESOURCENOTFOUND_SHUFFLEDIRNOTFOUND = 'ResourceNotFound.ShuffleDirNotFound'

# 
RESOURCENOTFOUND_TASKALREADYFAILED = 'ResourceNotFound.TaskAlreadyFailed'

# 
RESOURCENOTFOUND_TASKALREADYFINISHED = 'ResourceNotFound.TaskAlreadyFinished'

# 
RESOURCENOTFOUND_WAREHOUSEDIRNOTFOUND = 'ResourceNotFound.WarehouseDirNotFound'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# The account balance is insufficient to run the SQL task.
RESOURCEUNAVAILABLE_BALANCEINSUFFICIENT = 'ResourceUnavailable.BalanceInsufficient'

# 
RESOURCEUNAVAILABLE_WHITELISTFUNCTION = 'ResourceUnavailable.WhiteListFunction'

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

# 
UNSUPPORTEDOPERATION_UNSUPPORTEDFILETYPE = 'UnsupportedOperation.UnsupportedFileType'
