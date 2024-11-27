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

# The session being deleted is in use.
FAILEDOPERATION_SESSIONINUSED = 'FailedOperation.SessionInUsed'

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

# The quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

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
