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

# The deletion of the data engine failed.
FAILEDOPERATION_DELETEDATAENGINEFAILED = 'FailedOperation.DeleteDataEngineFailed'

# Failed to deliver the goods.
FAILEDOPERATION_DELIVERGOODSFAILED = 'FailedOperation.DeliverGoodsFailed'

# Duplicate tag keys.
FAILEDOPERATION_DUPLICATETAGKEY = 'FailedOperation.DuplicateTagKey'

# Deduction failed.
FAILEDOPERATION_FEEDEDUCTIONFAILED = 'FailedOperation.FeeDeductionFailed'

# Obtaining the authentication policy failed.
FAILEDOPERATION_GETPOLICYFAILED = 'FailedOperation.GetPolicyFailed'

# Failed to get product information.
FAILEDOPERATION_GETPRODUCTINFORMATIONFAILED = 'FailedOperation.GetProductInformationFailed'

# Obtaining user information failed. Please try again or submit a ticket to contact us.
FAILEDOPERATION_GETUSERINFOFAILED = 'FailedOperation.GetUserInfoFailed'

# Obtaining working group information failed.
FAILEDOPERATION_GETWORKGROUPINFOFAILED = 'FailedOperation.GetWorkGroupInfoFailed'

# Authorization failed.
FAILEDOPERATION_GRANTPOLICYFAILED = 'FailedOperation.GrantPolicyFailed'

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

# The user does not have permission to specify the engine.
FAILEDOPERATION_NOPERMISSIONTOUSETHEDATAENGINE = 'FailedOperation.NoPermissionToUseTheDataEngine'

# Unverified account.
FAILEDOPERATION_NOREALNAMEAUTHENTICATION = 'FailedOperation.NoRealNameAuthentication'

# Reached the allowed limit of engines.
FAILEDOPERATION_NUMBEREXCEEDLIMIT = 'FailedOperation.NumberExceedLimit'

# Failed to verify parameters.
FAILEDOPERATION_PARAMETERVALIDATIONFAILED = 'FailedOperation.ParameterValidationFailed'

# Refunding failed.
FAILEDOPERATION_REFUNDDEPOSITFAILED = 'FailedOperation.RefundDepositFailed'

# Canceling authorization failed.
FAILEDOPERATION_REVOKEPOLICYFAILED = 'FailedOperation.RevokePolicyFailed'

# Syntax parsing failed. Please verify and try again.
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

# The business system is abnormal. Please try again or submit a ticket to contact us.
INTERNALERROR_INTERNALSYSTEMEXCEPTION = 'InternalError.InternalSystemException'

# The parameter is incorrect.
INVALIDPARAMETER = 'InvalidParameter'

# The custom primary key of the specified interactive SQL task is not unique.
INVALIDPARAMETER_BATCHSQLCUSTOMKEYNOTUNIQUE = 'InvalidParameter.BatchSQLCustomKeyNotUnique'

# The specified cluster resource type does not match. Currently, only spark_cu (corresponding to Spark cluster) and presto_cu (corresponding to Presto cluster) are supported.
INVALIDPARAMETER_DATAENGINECLUSTERTYPENOTMATCH = 'InvalidParameter.DataEngineClusterTypeNotMatch'

# The specified cluster parameter already exists
INVALIDPARAMETER_DATAENGINECONFIGPAIRSDUPLICATE = 'InvalidParameter.DataEngineConfigPairsDuplicate'

# The parameter ExecType passing to the specified cluster is invalid. Currently, only SQL or BATCH is supported.
INVALIDPARAMETER_DATAENGINEEXECTYPENOTMATCH = 'InvalidParameter.DataEngineExecTypeNotMatch'

# The specified cluster image operation does not match. Currently, only InitImage/UpgradeImage/SwitchImage/RollbackImage/ModifyResource is supported.
INVALIDPARAMETER_DATAENGINEIMAGEOPERATENOTMATCH = 'InvalidParameter.DataEngineImageOperateNotMatch'

# The specified cluster billing mode does not match. Currently, it only supports 1: pay-as-you-go and 2: annual and monthly subscriptions.
INVALIDPARAMETER_DATAENGINEMODENOTMATCH = 'InvalidParameter.DataEngineModeNotMatch'

# The current task only supports SQL engine operation.
INVALIDPARAMETER_DATAENGINEONLYSUPPORTSQL = 'InvalidParameter.DataEngineOnlySupportSQL'

# The current task only supports the Spark batch job processing engine.
INVALIDPARAMETER_DATAENGINEONLYSUPPORTSPARKBATCH = 'InvalidParameter.DataEngineOnlySupportSparkBatch'

# The specified cluster payment type does not match. Currently, it only supports 0: postpaid and 1: prepaid.
INVALIDPARAMETER_DATAENGINEPAYMODETYPENOTMATCH = 'InvalidParameter.DataEnginePayModeTypeNotMatch'

# The specified cluster specifications are not compliant.
INVALIDPARAMETER_DATAENGINESIZENOTMATCH = 'InvalidParameter.DataEngineSizeNotMatch'

# The specified cluster type does not match. Currently, only spark/presto is supported.
INVALIDPARAMETER_DATAENGINETYPENOTMATCH = 'InvalidParameter.DataEngineTypeNotMatch'

# Duplicate engine name.
INVALIDPARAMETER_DUPLICATEDATAENGINENAME = 'InvalidParameter.DuplicateDataEngineName'

# The working group name is duplicated.
INVALIDPARAMETER_DUPLICATEGROUPNAME = 'InvalidParameter.DuplicateGroupName'

# The username is duplicated.
INVALIDPARAMETER_DUPLICATEUSERNAME = 'InvalidParameter.DuplicateUserName'

# The number of specified Filter.Values parameters exceeds the limit. Currently, it should be less than or equal to 50.
INVALIDPARAMETER_FILTERSVALUESNUMBEROUTOFLIMIT = 'InvalidParameter.FiltersValuesNumberOutOfLimit'

# The specified cluster image Cluster parameter format is not JSON.
INVALIDPARAMETER_IMAGECLUSTERPARAMETERSFORMATNOTJSON = 'InvalidParameter.ImageClusterParametersFormatNotJson'

# The specified engine type does not match. Currently, only SparkSQL, PrestoSQL, and SparkBatch are supported.
INVALIDPARAMETER_IMAGEENGINETYPENOTMATCH = 'InvalidParameter.ImageEngineTypeNotMatch'

# The specified isPublic does not match. Currently, it only supports 1: public and 2: private.
INVALIDPARAMETER_IMAGEISPUBLICNOTMATCH = 'InvalidParameter.ImageIsPublicNotMatch'

# The specified cluster image parameter does not exist.
INVALIDPARAMETER_IMAGEPARAMETERNOTFOUND = 'InvalidParameter.ImageParameterNotFound'

# The specified cluster image ParameterSubmitMethod does not match. Currently, only User and BackGround are supported.
INVALIDPARAMETER_IMAGEPARAMETERSUBMITMETHODNOTMATCH = 'InvalidParameter.ImageParameterSubmitMethodNotMatch'

# The specified cluster image ParameterType does not match. Currently, it only supports 1: session; 2: common; 3: cluster.
INVALIDPARAMETER_IMAGEPARAMETERTYPENOTMATCH = 'InvalidParameter.ImageParameterTypeNotMatch'

# The specified cluster image Session parameter format is not JSON.
INVALIDPARAMETER_IMAGESESSIONPARAMETERSFORMATNOTJSON = 'InvalidParameter.ImageSessionParametersFormatNotJson'

# The specified state does not match. Currently, it only supports 1: initializing, 2: online, 3: offline.
INVALIDPARAMETER_IMAGESTATENOTMATCH = 'InvalidParameter.ImageStateNotMatch'

# The specified cluster image UserRecords does not match. Currently, it only supports: 1: parentVersion; 2: childVersion; 3: pySpark.
INVALIDPARAMETER_IMAGEUSERRECORDSTYPENOTMATCH = 'InvalidParameter.ImageUserRecordsTypeNotMatch'

# Instances are in other processes.
INVALIDPARAMETER_INSTANCEINPROCESS = 'InvalidParameter.InstanceInProcess'

# The access policy is invalid.
INVALIDPARAMETER_INVALIDACCESSPOLICY = 'InvalidParameter.InvalidAccessPolicy'

# The specified Spark task package file format does not match. Currently, only .jar or .py is supported.
INVALIDPARAMETER_INVALIDAPPFILEFORMAT = 'InvalidParameter.InvalidAppFileFormat'

# The field name is set incorrectly. The field name must be less than or equal to 128 bytes.
INVALIDPARAMETER_INVALIDCOLUMNNAMELENGTH = 'InvalidParameter.InvalidColumnNameLength'

# The number of fields is set incorrectly. The number of fields must be less than or equal to 4096.
INVALIDPARAMETER_INVALIDCOLUMNNUMBER = 'InvalidParameter.InvalidColumnNumber'

# The specified task parameter Key value does not exist.
INVALIDPARAMETER_INVALIDCONFIGKEYNOTFOUND = 'InvalidParameter.InvalidConfigKeyNotFound'

# The length of the specified task parameter Value exceeds the limit.
INVALIDPARAMETER_INVALIDCONFIGVALUELENGTHOUTLIMIT = 'InvalidParameter.InvalidConfigValueLengthOutLimit'

# The specified task parameter Value does not conform to the rules.
INVALIDPARAMETER_INVALIDCONFIGVALUEREGEXPNOTMATCH = 'InvalidParameter.InvalidConfigValueRegexpNotMatch'

# The specified cluster CIDR format does not match, and the reference style is 192.0.2.1/24.
INVALIDPARAMETER_INVALIDDATAENGINECIDRFORMAT = 'InvalidParameter.InvalidDataEngineCidrFormat'

# The specified cluster parameters are invalid. Please verify and try again.
INVALIDPARAMETER_INVALIDDATAENGINECONFIGPAIRS = 'InvalidParameter.InvalidDataEngineConfigPairs'

# The engine description information is invalid.
INVALIDPARAMETER_INVALIDDATAENGINEDESCRIPTION = 'InvalidParameter.InvalidDataEngineDescription'

# Invalid data engine mode.
INVALIDPARAMETER_INVALIDDATAENGINEMODE = 'InvalidParameter.InvalidDataEngineMode'

# The data engine name is invalid.
INVALIDPARAMETER_INVALIDDATAENGINENAME = 'InvalidParameter.InvalidDataEngineName'

# Invalid data engine spec.
INVALIDPARAMETER_INVALIDDATAENGINESPECS = 'InvalidParameter.InvalidDataEngineSpecs'

# The usage duration of the specified cluster resource: Postpaid: Fill in 3,600 as a fixed figure; prepaid: Fill in a figure equal to or bigger than 1 which means purchasing resources for one month. The maximum figure is no more than 120. The default is 3,600.
INVALIDPARAMETER_INVALIDDATAENGINETIMESPAN = 'InvalidParameter.InvalidDataEngineTimeSpan'

# The unit of the usage duration of the specified cluster resource does not match; postpaid: h; prepaid: m. The default is h.
INVALIDPARAMETER_INVALIDDATAENGINETIMEUNIT = 'InvalidParameter.InvalidDataEngineTimeUnit'

# The DecimalType setting is invalid. Precision must be greater than or equal to Scale, and Precision must be less than 38.
INVALIDPARAMETER_INVALIDDECIMALTYPE = 'InvalidParameter.InvalidDecimalType'

# The default data engine parameters are invalid.
INVALIDPARAMETER_INVALIDDEFAULTDATAENGINE = 'InvalidParameter.InvalidDefaultDataEngine'

# The description information is invalid.
INVALIDPARAMETER_INVALIDDESCRIPTION = 'InvalidParameter.InvalidDescription'

# The current DriverSize specification only supports small/medium/large/xlarge/m.small/m.medium/m.large/m.xlarge.
INVALIDPARAMETER_INVALIDDRIVERSIZE = 'InvalidParameter.InvalidDriverSize'

# The specified dynamic number of executors must be the current maximum value.
INVALIDPARAMETER_INVALIDDYNAMICALLOCATIONMAXEXECUTORS = 'InvalidParameter.InvalidDynamicAllocationMaxExecutors'

# The engine execution type is invalid.
INVALIDPARAMETER_INVALIDENGINEEXECTYPE = 'InvalidParameter.InvalidEngineExecType'

# The engine type is invalid.
INVALIDPARAMETER_INVALIDENGINETYPE = 'InvalidParameter.InvalidEngineType'

# The current ExecutorSize specification only supports small/medium/large/xlarge/m.small/m.medium/m.large/m.xlarge.
INVALIDPARAMETER_INVALIDEXECUTORSIZE = 'InvalidParameter.InvalidExecutorSize'

# The task fault tolerance type is wrong. Currently, only Proceed/Terminate is supported.
INVALIDPARAMETER_INVALIDFAILURETOLERANCE = 'InvalidParameter.InvalidFailureTolerance'

# The specified file compression format is not compliant. Currently, only .tar.gz/.tar/.tgz is supported.
INVALIDPARAMETER_INVALIDFILECOMPRESSIONFORMAT = 'InvalidParameter.InvalidFileCompressionFormat'

# The specified file path format is not compliant. Currently, only cosn:// or lakefs:// is supported.
INVALIDPARAMETER_INVALIDFILEPATHFORMAT = 'InvalidParameter.InvalidFilePathFormat'

# The filter condition is not supported.
INVALIDPARAMETER_INVALIDFILTERKEY = 'InvalidParameter.InvalidFilterKey'

# The number of filter conditions is invalid. When filter conditions are specified, the number of filter conditions should be greater than or equal to 1 and less than or equal to 5.
INVALIDPARAMETER_INVALIDFILTERLENGTH = 'InvalidParameter.InvalidFilterLength'

# The working group ID is invalid.
INVALIDPARAMETER_INVALIDGROUPID = 'InvalidParameter.InvalidGroupId'

# The requested message type is invalid.
INVALIDPARAMETER_INVALIDINFOTYPE = 'InvalidParameter.InvalidInfoType'

# Invalid maximum number of results.
INVALIDPARAMETER_INVALIDMAXRESULTS = 'InvalidParameter.InvalidMaxResults'

# The minimum number of clusters is invalid.
INVALIDPARAMETER_INVALIDMINCLUSTERS = 'InvalidParameter.InvalidMinClusters'

# The Offset value is invalid.
INVALIDPARAMETER_INVALIDOFFSET = 'InvalidParameter.InvalidOffset'

# Invalid billing mode.
INVALIDPARAMETER_INVALIDPAYMODE = 'InvalidParameter.InvalidPayMode'

# The CAM role arn is invalid.
INVALIDPARAMETER_INVALIDROLEARN = 'InvalidParameter.InvalidRoleArn'

# SQL parsing failed.
INVALIDPARAMETER_INVALIDSQL = 'InvalidParameter.InvalidSQL'

# Parameter verification failed. Please adjust the parameters or submit a ticket to contact us.
INVALIDPARAMETER_INVALIDSQLCONFIGSQL = 'InvalidParameter.InvalidSQLConfigSQL'

# The number of executed SQL statements is incorrect. The number of SQL statements must be greater than or equal to 1 and less than or equal to 50.
INVALIDPARAMETER_INVALIDSQLNUM = 'InvalidParameter.InvalidSQLNum'

# The number of SQL task results obtained at a time must be greater than 0 and less than 1,000.
INVALIDPARAMETER_INVALIDSQLTASKMAXRESULTS = 'InvalidParameter.InvalidSQLTaskMaxResults'

# Currently, types supported by Session only include spark/pyspark/sparkr/sql.
INVALIDPARAMETER_INVALIDSESSIONKINDTYPE = 'InvalidParameter.InvalidSessionKindType'

# The sorting type is not supported.
INVALIDPARAMETER_INVALIDSORTBYTYPE = 'InvalidParameter.InvalidSortByType'

# Invalid Sorting
INVALIDPARAMETER_INVALIDSORTING = 'InvalidParameter.InvalidSorting'

# The `SparkAppParam` is invalid.
INVALIDPARAMETER_INVALIDSPARKAPPPARAM = 'InvalidParameter.InvalidSparkAppParam'

# The specified Spark job configuration format is abnormal. Please see spark.network.timeout=120s.
INVALIDPARAMETER_INVALIDSPARKCONFIGFORMAT = 'InvalidParameter.InvalidSparkConfigFormat'

# Currently, Statement only supports the type of sql.
INVALIDPARAMETER_INVALIDSTATEMENTKINDTYPE = 'InvalidParameter.InvalidStatementKindType'

# The storage location is incorrect.
INVALIDPARAMETER_INVALIDSTORELOCATION = 'InvalidParameter.InvalidStoreLocation'

# The table name is set incorrectly. The length of the table name must be less than or equal to 128 bytes.
INVALIDPARAMETER_INVALIDTABLENAMELENGTH = 'InvalidParameter.InvalidTableNameLength'

# The `taskid` is invalid.
INVALIDPARAMETER_INVALIDTASKID = 'InvalidParameter.InvalidTaskId'

# The TaskType is incorrect. The Spark engine task type is SparkSQLTask, and the Presto engine task type is SQLTask.
INVALIDPARAMETER_INVALIDTASKTYPE = 'InvalidParameter.InvalidTaskType'

# The specified TCR Spark image format does not match. The example for reference is my-image/ndf/python/latest.
INVALIDPARAMETER_INVALIDTCRSPARKIMAGEFORMAT = 'InvalidParameter.InvalidTcrSparkImageFormat'

# The specified time format is not compliant. Currently, only YYYY-mm-dd HH:MM:SS is supported.
INVALIDPARAMETER_INVALIDTIMEFORMAT = 'InvalidParameter.InvalidTimeFormat'

# The date parameters are abnormal. For example, the end time is earlier than the start time.
INVALIDPARAMETER_INVALIDTIMEPARAMETER = 'InvalidParameter.InvalidTimeParameter'

# Invalid billing period.
INVALIDPARAMETER_INVALIDTIMESPAN = 'InvalidParameter.InvalidTimeSpan'

# Invalid unit of billing period.
INVALIDPARAMETER_INVALIDTIMEUNIT = 'InvalidParameter.InvalidTimeUnit'

# The username is invalid.
INVALIDPARAMETER_INVALIDUSERALIAS = 'InvalidParameter.InvalidUserAlias'

# The username is invalid.
INVALIDPARAMETER_INVALIDUSERNAME = 'InvalidParameter.InvalidUserName'

# The user type is invalid.
INVALIDPARAMETER_INVALIDUSERTYPE = 'InvalidParameter.InvalidUserType'

# There is an error in getting an allowlist. Please try again or submit a ticket to contact us.
INVALIDPARAMETER_INVALIDWHITELISTKEY = 'InvalidParameter.InvalidWhiteListKey'

# The working group name is invalid.
INVALIDPARAMETER_INVALIDWORKGROUPNAME = 'InvalidParameter.InvalidWorkGroupName'

# Job not found.
INVALIDPARAMETER_JOBNOTFOUND = 'InvalidParameter.JobNotFound'

# You are currently only allowed to view 100 results. If you need to make an adjustment, please contact us.
INVALIDPARAMETER_MAXRESULTONLYSUPPORTHUNDRED = 'InvalidParameter.MaxResultOnlySupportHundred'

# The number of SQL statements submitted is limited to 1~50.
INVALIDPARAMETER_NUMBEROFSQLEXCEEDSTHELIMIT = 'InvalidParameter.NumberOfSQLExceedsTheLimit'

# Base64 parsing of the specified parameter failed.
INVALIDPARAMETER_PARAMETERBASE64DECODEFAILED = 'InvalidParameter.ParameterBase64DecodeFailed'

# The parameter is not found or empty.
INVALIDPARAMETER_PARAMETERNOTFOUNDORBENONE = 'InvalidParameter.ParameterNotFoundOrBeNone'

# Base64 parsing of the SQL script failed.
INVALIDPARAMETER_SQLBASE64DECODEFAIL = 'InvalidParameter.SQLBase64DecodeFail'

# SQL parameter preprocessing failed.
INVALIDPARAMETER_SQLPARAMETERPREPROCESSINGFAILED = 'InvalidParameter.SQLParameterPreprocessingFailed'

# The specified Filter.Key does not match. Currently, only task-id/task-sql-keyword/task-kind/task-operator/batch-id/session-id/task-state is supported.
INVALIDPARAMETER_SQLTASKFILTERSKEYTYPENOTMATH = 'InvalidParameter.SQLTaskFiltersKeyTypeNotMath'

# The specified SQL task does not exist.
INVALIDPARAMETER_SQLTASKNOTFOUND = 'InvalidParameter.SQLTaskNotFound'

# The SortBy type specified in the SQL task does not match. Currently, only create-time/data-amount/used-time/resource-usage is supported.
INVALIDPARAMETER_SQLTASKSORTBYTYPENOTMATCH = 'InvalidParameter.SQLTaskSortByTypeNotMatch'

# The specified Spark task Filter.Key does not match. Currently, only spark-app-type/user-name/spark-job-name/spark-job-id/key-word is supported.
INVALIDPARAMETER_SPARKJOBFILTERSKEYTYPENOTMATH = 'InvalidParameter.SparkJobFiltersKeyTypeNotMath'

# The specified Spark task IsInherit type does not match. Currently, it only supports: 0: Inherit; 1: Do not inherit.
INVALIDPARAMETER_SPARKJOBISINHERITTYPENOTMATCH = 'InvalidParameter.SparkJobIsInheritTypeNotMatch'

# The specified Spark task does not exist.
INVALIDPARAMETER_SPARKJOBNOTFOUND = 'InvalidParameter.SparkJobNotFound'

# The specified Spark task already exists.
INVALIDPARAMETER_SPARKJOBNOTUNIQUE = 'InvalidParameter.SparkJobNotUnique'

# Spark tasks can only be run using the Spark job engine.
INVALIDPARAMETER_SPARKJOBONLYSUPPORTSPARKBATCHENGINE = 'InvalidParameter.SparkJobOnlySupportSparkBatchEngine'

# The specified Spark task RoleArn does not exist.
INVALIDPARAMETER_SPARKJOBROLEARNNOTFOUND = 'InvalidParameter.SparkJobRoleArnNotFound'

# The specified Spark task sorting type does not match. Currently, only create-time/update-time/user-name/data-engine-name is supported.
INVALIDPARAMETER_SPARKJOBSORTBYTYPENOTMATCH = 'InvalidParameter.SparkJobSortByTypeNotMatch'

# The task has ended and cannot be canceled.
INVALIDPARAMETER_TASKALREADYFINISHED = 'InvalidParameter.TaskAlreadyFinished'

# The task does not exist.
INVALIDPARAMETER_TASKNOTFOUND = 'InvalidParameter.TaskNotFound'

# The specified task status does not match. Currently, it only supports 0: initializing, 1: running, 2: successful, 3: writing data, 4: queuing, -1: failed, and -3: deleted.
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

# The resource is occupied.
RESOURCEINUSE = 'ResourceInUse'

# Some SQL tasks have not yet been completed.
RESOURCEINUSE_UNFINISHEDSQLS = 'ResourceInUse.UnfinishedSQLs'

# The specified spark job resources are insufficient. Please adjust the driver/executor specifications.
RESOURCEINSUFFICIENT_SPARKJOBINSUFFICIENTRESOURCES = 'ResourceInsufficient.SparkJobInsufficientResources'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The specified interactive SQL task does not exist.
RESOURCENOTFOUND_BATCHSQLTASKNOTFOUND = 'ResourceNotFound.BatchSQLTaskNotFound'

# The specified interactive SQL task is not unique.
RESOURCENOTFOUND_BATCHSQLTASKNOTUNIQUE = 'ResourceNotFound.BatchSQLTaskNotUnique'

# The specified cluster configuration instance does not exist.
RESOURCENOTFOUND_DATAENGINECONFIGINSTANCENOTFOUND = 'ResourceNotFound.DataEngineConfigInstanceNotFound'

# The specified cluster configuration instance already exists.
RESOURCENOTFOUND_DATAENGINECONFIGINSTANCENOTUNIQUE = 'ResourceNotFound.DataEngineConfigInstanceNotUnique'

# The specified cluster is not running.
RESOURCENOTFOUND_DATAENGINENOTACTIVITY = 'ResourceNotFound.DataEngineNotActivity'

# The specified engine does not exist.
RESOURCENOTFOUND_DATAENGINENOTFOUND = 'ResourceNotFound.DataEngineNotFound'

# The specified cluster is not a multi-version type and does not support this operation.
RESOURCENOTFOUND_DATAENGINENOTMULTIVERSION = 'ResourceNotFound.DataEngineNotMultiVersion'

# The specified engine is not running.
RESOURCENOTFOUND_DATAENGINENOTRUNNING = 'ResourceNotFound.DataEngineNotRunning'

# The specified engine already exists.
RESOURCENOTFOUND_DATAENGINENOTUNIQUE = 'ResourceNotFound.DataEngineNotUnique'

# The specified cluster is not a Spark batch job type and does not support this operation.
RESOURCENOTFOUND_DATAENGINETYPEONLYSUPPORTBATCH = 'ResourceNotFound.DataEngineTypeOnlySupportBatch'

# The data source connection does not exist. Please try again or submit a ticket to contact us.
RESOURCENOTFOUND_DATASOURCENOTFOUND = 'ResourceNotFound.DatasourceNotFound'

# No default engine can be found.
RESOURCENOTFOUND_DEFAULTDATAENGINENOTFOUND = 'ResourceNotFound.DefaultDataEngineNotFound'

# The specified cluster image Session configuration does not exist.
RESOURCENOTFOUND_IMAGESESSIONCONFIGNOTFOUND = 'ResourceNotFound.ImageSessionConfigNotFound'

# The specified cluster image Session configuration already exists.
RESOURCENOTFOUND_IMAGESESSIONCONFIGNOTUNIQUE = 'ResourceNotFound.ImageSessionConfigNotUnique'

# The specified cluster image is not activated.
RESOURCENOTFOUND_IMAGEVERSIONNOTACTIVITY = 'ResourceNotFound.ImageVersionNotActivity'

# The specified cluster image version does not exist.
RESOURCENOTFOUND_IMAGEVERSIONNOTFOUND = 'ResourceNotFound.ImageVersionNotFound'

# The specified cluster image version already exists.
RESOURCENOTFOUND_IMAGEVERSIONNOTUNIQUE = 'ResourceNotFound.ImageVersionNotUnique'

# The specified task resources exceed the limit of the remaining resources of the cluster. Please try again after adjustment.
RESOURCENOTFOUND_RESOURCEUSAGEOUTOFLIMIT = 'ResourceNotFound.ResourceUsageOutOfLimit'

# The result path was not found.
RESOURCENOTFOUND_RESULTOUTPUTPATHNOTFOUND = 'ResourceNotFound.ResultOutputPathNotFound'

# Obtaining the result storage path failed. Please go to the Console -> Data Exploration page for settings.
RESOURCENOTFOUND_RESULTSAVEPATHNOTFOUND = 'ResourceNotFound.ResultSavePathNotFound'

# The specified RoleArn does not exist.
RESOURCENOTFOUND_ROLEARNRESOURCENOTFOUND = 'ResourceNotFound.RoleArnResourceNotFound'

# There are currently no resources to create a session. Please try again later or use an annual or monthly subscription cluster.
RESOURCENOTFOUND_SESSIONINSUFFICIENTRESOURCES = 'ResourceNotFound.SessionInsufficientResources'

# The session does not exist.
RESOURCENOTFOUND_SESSIONNOTFOUND = 'ResourceNotFound.SessionNotFound'

# The session has expired.
RESOURCENOTFOUND_SESSIONSTATEDEAD = 'ResourceNotFound.SessionStateDead'

# The Spark Shuffle storage path cannot be found. Please go to the Console -> Data Exploration page -> Storage Configuration to set it.
RESOURCENOTFOUND_SHUFFLEDIRNOTFOUND = 'ResourceNotFound.ShuffleDirNotFound'

# The task has failed.
RESOURCENOTFOUND_TASKALREADYFAILED = 'ResourceNotFound.TaskAlreadyFailed'

# The task has been completed.
RESOURCENOTFOUND_TASKALREADYFINISHED = 'ResourceNotFound.TaskAlreadyFinished'

# The Warehouse storage path cannot be found. Please go to the Console->Data Exploration page->Storage Configuration to set it.
RESOURCENOTFOUND_WAREHOUSEDIRNOTFOUND = 'ResourceNotFound.WarehouseDirNotFound'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# The account balance is insufficient to run the SQL task.
RESOURCEUNAVAILABLE_BALANCEINSUFFICIENT = 'ResourceUnavailable.BalanceInsufficient'

# Currently, the allowlist function is available. Please contact us to activate it.
RESOURCEUNAVAILABLE_WHITELISTFUNCTION = 'ResourceUnavailable.WhiteListFunction'

# The resource is sold out.
RESOURCESSOLDOUT = 'ResourcesSoldOut'

# There is no permission authorization policy.
RESOURCESSOLDOUT_UNAUTHORIZEDGRANTPOLICY = 'ResourcesSoldOut.UnauthorizedGrantPolicy'

# There is no permission to operate.
RESOURCESSOLDOUT_UNAUTHORIZEDOPERATION = 'ResourcesSoldOut.UnauthorizedOperation'

# There is no permission to reclaim permissions.
RESOURCESSOLDOUT_UNAUTHORIZEDREVOKEPOLICY = 'ResourcesSoldOut.UnauthorizedRevokePolicy'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Sub-users are not administrators and cannot add users to working groups.
UNAUTHORIZEDOPERATION_ADDUSERSTOWORKGROUP = 'UnauthorizedOperation.AddUsersToWorkgroup'

# Sub-users are not administrators and cannot bind working groups to users.
UNAUTHORIZEDOPERATION_BINDWORKGROUPSTOUSER = 'UnauthorizedOperation.BindWorkgroupsToUser'

# Sub-users are not administrators and cannot create working groups.
UNAUTHORIZEDOPERATION_CREATEWORKGROUP = 'UnauthorizedOperation.CreateWorkgroup'

# Sub-users cannot delete a computing engine.
UNAUTHORIZEDOPERATION_DELETECOMPUTINGENGINE = 'UnauthorizedOperation.DeleteComputingEngine'

# Sub-users are not administrators and cannot delete users.
UNAUTHORIZEDOPERATION_DELETEUSER = 'UnauthorizedOperation.DeleteUser'

# Sub-users are not administrators and cannot unbind users from working groups.
UNAUTHORIZEDOPERATION_DELETEUSERSFROMWORKGROUP = 'UnauthorizedOperation.DeleteUsersFromWorkgroup'

# Sub-users are not administrators and cannot delete working groups.
UNAUTHORIZEDOPERATION_DELETEWORKGROUP = 'UnauthorizedOperation.DeleteWorkgroup'

# Sub-users do not have the authority to grant specific permissions.
UNAUTHORIZEDOPERATION_GRANTPOLICY = 'UnauthorizedOperation.GrantPolicy'

# Sub-users cannot modify engine configuration.
UNAUTHORIZEDOPERATION_MODIFYCOMPUTINGENGINE = 'UnauthorizedOperation.ModifyComputingEngine'

# Sub-users are not administrators and cannot modify user information.
UNAUTHORIZEDOPERATION_MODIFYUSERINFO = 'UnauthorizedOperation.ModifyUserInfo'

# Sub-users are not administrators and cannot modify user types.
UNAUTHORIZEDOPERATION_MODIFYUSERTYPE = 'UnauthorizedOperation.ModifyUserType'

# Sub-users are not administrators and cannot modify working group information.
UNAUTHORIZEDOPERATION_MODIFYWORKGROUPINFO = 'UnauthorizedOperation.ModifyWorkgroupInfo'

# Sub-users do not have the permission to view engine monitoring.
UNAUTHORIZEDOPERATION_MONITORCOMPUTINGENGINE = 'UnauthorizedOperation.MonitorComputingEngine'

# No permission to pay.
UNAUTHORIZEDOPERATION_NOPAYMENTAUTHORITY = 'UnauthorizedOperation.NoPaymentAuthority'

# Unauthorized engine operation by a sub-user.
UNAUTHORIZEDOPERATION_OPERATECOMPUTINGENGINE = 'UnauthorizedOperation.OperateComputingEngine'

# Prohibited operation admin
UNAUTHORIZEDOPERATION_PROHIBITEDOPERATIONADMIN = 'UnauthorizedOperation.ProhibitedOperationAdmin'

# Sub-users have no authority to renew the computing engine.
UNAUTHORIZEDOPERATION_RENEWCOMPUTINGENGINE = 'UnauthorizedOperation.RenewComputingEngine'

# Sub-users do not have the authority to revoke specific permissions.
UNAUTHORIZEDOPERATION_REVOKEPOLICY = 'UnauthorizedOperation.RevokePolicy'

# Sub-users are not administrators and cannot unbind working groups and users.
UNAUTHORIZEDOPERATION_UNBINDWORKGROUPSFROMUSER = 'UnauthorizedOperation.UnbindWorkgroupsFromUser'

# The sub-user does not have permission to use the compute engine.
UNAUTHORIZEDOPERATION_USECOMPUTINGENGINE = 'UnauthorizedOperation.UseComputingEngine'

# The sub-user does not exist.
UNAUTHORIZEDOPERATION_USERNOTEXIST = 'UnauthorizedOperation.UserNotExist'

# Unknown parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# The root account cannot be modified.
UNSUPPORTEDOPERATION_MODIFYOWNERUNSUPPORTED = 'UnsupportedOperation.ModifyOwnerUnsupported'

# The current file format is not supported. Currently, it only supports json/csv/avro/orc/parquet.
UNSUPPORTEDOPERATION_UNSUPPORTEDFILETYPE = 'UnsupportedOperation.UnsupportedFileType'
