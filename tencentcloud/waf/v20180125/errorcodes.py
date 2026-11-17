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

# The current instance has not purchased the API security package.
AUTHFAILURE_ERRCODENOPURCHASED = 'AuthFailure.ErrCodeNoPurchased'

# DryRun operation means the request will be successful, but the DryRun parameter is passed.
DRYRUNOPERATION = 'DryRunOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# CKafka internal error.
FAILEDOPERATION_CKAFKAINTERNALERROR = 'FailedOperation.CKafkaInternalError'

# Failed to call the CLS API.
FAILEDOPERATION_CLSDBOPERATIONFAILED = 'FailedOperation.CLSDBOperationFailed'

# CLS internal error.
FAILEDOPERATION_CLSINTERNALERROR = 'FailedOperation.CLSInternalError'

# Failed to operate the MongoDB database.
FAILEDOPERATION_MONGOOPERATIONFAILED = 'FailedOperation.MongoOperationFailed'

# Failed to operate the MySQL database.
FAILEDOPERATION_MYSQLDBOPERATIONFAILED = 'FailedOperation.MysqlDBOperationFailed'

# Failed to operate the Redis database.
FAILEDOPERATION_REDISOPERATIONFAILED = 'FailedOperation.RedisOperationFailed'

# The number of additions to the blocklist/allowlist exceeds the limit.
FAILEDOPERATION_THENUMBEROFADDEDBLACKANDWHITELISTEXCEEDSTHEUPPERLIMIT = 'FailedOperation.TheNumberOfAddedBlackAndWhiteListExceedsTheUpperLimit'

# Reached the maximum number of one-time deletions.
FAILEDOPERATION_THENUMBEROFONETIMEDELETIONSREACHEDTHEUPPERLIMIT = 'FailedOperation.TheNumberOfOneTimeDeletionsReachedTheUpperLimit'

# Internal error.
INTERNALERROR = 'InternalError'

# Asynchronous call failed.
INTERNALERROR_ASYNCHRONOUSCALLFAILED = 'InternalError.AsynchronousCallFailed'

# DBErr
INTERNALERROR_DBERR = 'InternalError.DBErr'

# InternalError.Unknown
INTERNALERROR_UNKNOWN = 'InternalError.Unknown'

# An internal error exists. Please contact us.
INTERNALERROR_UNKNOWNERR = 'InternalError.UnknownErr'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# Certificate information parameter error
INVALIDPARAMETER_CERTIFICATIONPARAMETERERR = 'InvalidParameter.CertificationParameterErr'

# The number of domain names reached the upper limit.
INVALIDPARAMETER_DOMAINEXCEEDSLIMITERR = 'InvalidParameter.DomainExceedsLimitErr'

# The domain name is not registered.
INVALIDPARAMETER_DOMAINNOTRECORD = 'InvalidParameter.DomainNotRecord'

# Invalid certificate content.
INVALIDPARAMETER_INVALIDCERTIFICATE = 'InvalidParameter.InvalidCertificate'

# Content is empty.
INVALIDPARAMETER_LLMCONTENTEMPTY = 'InvalidParameter.LLMContentEmpty'

# Internal service error.
INVALIDPARAMETER_LLMINTERNALERROR = 'InvalidParameter.LLMInternalError'

# Invalid Type.
INVALIDPARAMETER_LLMINVALIDTYPE = 'InvalidParameter.LLMInvalidType'

# No rules are configured for the serviceid during large model invocation.
INVALIDPARAMETER_LLMNORULES = 'InvalidParameter.LLMNoRules'

# Failed to parse the request body.
INVALIDPARAMETER_LLMPARSEFAILED = 'InvalidParameter.LLMParseFailed'

# RequestId is empty.
INVALIDPARAMETER_LLMREQUESTIDEMPTY = 'InvalidParameter.LLMRequestIdEmpty'

# ServiceId is empty.
INVALIDPARAMETER_LLMSERVICEIDEMPTY = 'InvalidParameter.LLMServiceIdEmpty'

# The large model service switch is not enabled.
INVALIDPARAMETER_LLMSWITCHOFF = 'InvalidParameter.LLMSwitchOff'

# Logical error: Logical errors in SQL search statements can also lead to mistakes, such as using incorrect operators, wrong conditions, etc.
INVALIDPARAMETER_LOGICERR = 'InvalidParameter.LogicErr'

# Port information parameter error
INVALIDPARAMETER_PORTPARAMETERERR = 'InvalidParameter.PortParameterErr'

# Protective domain parameter error
INVALIDPARAMETER_PROTECTIONDOMAINPARAMETERERR = 'InvalidParameter.ProtectionDomainParameterErr'

# Failed to query certificate by ID.
INVALIDPARAMETER_QUERYCERTBYSSLIDFAILED = 'InvalidParameter.QueryCertBySSLIDFailed'

# Syntax error: Logical expression syntax analysis failed.
INVALIDPARAMETER_QUERYSTRINGSYNTAXERR = 'InvalidParameter.QueryStringSyntaxErr'

# Syntax error: SQL search statements must follow specific syntax rules. Failure to do so, such as missing keywords, spelling errors, missing semicolons, etc., will cause SQL statements to not execute.
INVALIDPARAMETER_SQLSYNTAXERR = 'InvalidParameter.SQLSyntaxErr'

# The API Key has been disabled.
INVALIDPARAMETER_SKILLSCANAPIKEYDISABLED = 'InvalidParameter.SkillScanApiKeyDisabled'

# Failed to create the scan task due to an internal service error.
INVALIDPARAMETER_SKILLSCANCREATESCANFAILED = 'InvalidParameter.SkillScanCreateScanFailed'

# FileData is not a valid Base64-encoded string.
INVALIDPARAMETER_SKILLSCANINVALIDBASE64 = 'InvalidParameter.SkillScanInvalidBase64'

# The file is not a valid ZIP archive.
INVALIDPARAMETER_SKILLSCANINVALIDFILEFORMAT = 'InvalidParameter.SkillScanInvalidFileFormat'

# Parameter validation failed, such as an invalid content_hash format or missing required fields.
INVALIDPARAMETER_SKILLSCANINVALIDPARAM = 'InvalidParameter.SkillScanInvalidParam'

# Invalid request format, such as an incorrect Content-Type or JSON parsing failure.
INVALIDPARAMETER_SKILLSCANINVALIDREQUEST = 'InvalidParameter.SkillScanInvalidRequest'

# No uploaded file detected.
INVALIDPARAMETER_SKILLSCANNOFILES = 'InvalidParameter.SkillScanNoFiles'

# Failed to query due to an internal service error.
INVALIDPARAMETER_SKILLSCANQUERYFAILED = 'InvalidParameter.SkillScanQueryFailed'

# Request frequency limit exceeded.
INVALIDPARAMETER_SKILLSCANRATELIMITEXCEEDED = 'InvalidParameter.SkillScanRateLimitExceeded'

# ServiceId is empty.
INVALIDPARAMETER_SKILLSCANSERVICEIDEMPTY = 'InvalidParameter.SkillScanServiceIdEmpty'

# The protection switch is not enabled.
INVALIDPARAMETER_SKILLSCANSWITCHOFF = 'InvalidParameter.SkillScanSwitchOff'

# Failed to trigger the detection task due to an internal service error.
INVALIDPARAMETER_SKILLSCANTRIGGERFAILED = 'InvalidParameter.SkillScanTriggerFailed'

# The API Key is missing or invalid.
INVALIDPARAMETER_SKILLSCANUNAUTHORIZED = 'InvalidParameter.SkillScanUnauthorized'

# The current instance version does not support enabling TLS by definition. Please upgrade to the Advanced Edition or above.
INVALIDPARAMETER_SUPPORTTLSCONFFAILED = 'InvalidParameter.SupportTLSConfFailed'

# TLS or encryption suite parameter error
INVALIDPARAMETER_TLSPARAMETERERR = 'InvalidParameter.TLSParameterErr'

# Data type error: The data types in SQL search statements must match those in the database, otherwise it will lead to errors. For example, comparing a string with an integer, incorrect date format, etc.
INVALIDPARAMETER_TYPEMISMATCH = 'InvalidParameter.TypeMismatch'

# Permission overstep parameter error
INVALIDPARAMETER_UNAUTHORIZEDOPERATIONPARAMETERERR = 'InvalidParameter.UnauthorizedOperationParameterErr'

# Origin information parameter error
INVALIDPARAMETER_UPSTREAMPARAMETERERR = 'InvalidParameter.UpstreamParameterErr'

# XFF reset parameter error
INVALIDPARAMETER_XFFRESETPARAMETERERR = 'InvalidParameter.XFFResetParameterErr'

# Invalid parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# InvalidRequest
INVALIDPARAMETERVALUE_INVALIDREQUEST = 'InvalidParameterValue.InvalidRequest'

# The quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# The number of content rules under the current domain has reached the upper limit.
LIMITEXCEEDED_CONTENTRULEERR = 'LimitExceeded.ContentRuleErr'

# The number of compute consumption rules under the current domain has reached the upper limit.
LIMITEXCEEDED_LIMITRULEERR = 'LimitExceeded.LimitRuleErr'

# SpecificationErr
LIMITEXCEEDED_SPECIFICATIONERR = 'LimitExceeded.SpecificationErr'

# Parameters are missing
MISSINGPARAMETER = 'MissingParameter'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# Too frequent requests
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# Resources are occupied.
RESOURCEINUSE = 'ResourceInUse'

# EmptyErr
RESOURCEINUSE_EMPTYERR = 'ResourceInUse.EmptyErr'

# Insufficient resources.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# Resources do not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# ResourceNotFound.NotFound
RESOURCENOTFOUND_NOTFOUND = 'ResourceNotFound.NotFound'

# Resources are unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# The IPv6 network is being allocated. Please wait patiently.
RESOURCEUNAVAILABLE_DOMAINIPV6INCONFIGERR = 'ResourceUnavailable.DomainIpv6InConfigErr'

# Resources are sold out.
RESOURCESSOLDOUT = 'ResourcesSoldOut'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Unknown parameter.
UNKNOWNPARAMETER = 'UnknownParameter'

# The operation is not supported.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# InvalidRequest
UNSUPPORTEDOPERATION_INVALIDREQUEST = 'UnsupportedOperation.InvalidRequest'
