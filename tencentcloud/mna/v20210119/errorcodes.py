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


# Transaction process exception
FAILEDOPERATION_TRANSACTIONEXCEPTION = 'FailedOperation.TransactionException'

# Internal error.
INTERNALERROR = 'InternalError'

# Request controller encounters an error.
INTERNALERROR_CONTROLREQUESTERROR = 'InternalError.ControlRequestError'

# cos Cloud Object Storage request error.
INTERNALERROR_COSREQUESTERROR = 'InternalError.CosRequestError'

# Device key already exists.
INTERNALERROR_DUPLICATEDATAKEY = 'InternalError.DuplicateDataKey'

# Device name already exists.
INTERNALERROR_DUPLICATEDEVICENAME = 'InternalError.DuplicateDeviceName'

# File read/write exception.
INTERNALERROR_FILEIOERROR = 'InternalError.FileIOError'

# Monitor data request error.
INTERNALERROR_MONITORDATAREQUESTERROR = 'InternalError.MonitorDataRequestError'

# Zhiyan traffic data request error.
INTERNALERROR_NETWORKINFOREQUESTERROR = 'InternalError.NetworkInfoRequestError'

# Preset key not created.
INTERNALERROR_UNDEFINEDENCRYPTEDKEY = 'InternalError.UndefinedEncryptedKey'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# Parameter value error.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Query end time is later than current system time
INVALIDPARAMETERVALUE_TIMEFUTURE = 'InvalidParameterValue.TimeFuture'

# Query time span exceeds 7 days
INVALIDPARAMETERVALUE_TIMESPANEXCEEDED = 'InvalidParameterValue.TimeSpanExceeded'

# Start time earlier than 30 days ago
INVALIDPARAMETERVALUE_TIMETOOEARLY = 'InvalidParameterValue.TimeTooEarly'

# The quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# The device does not exist or is currently unavailable.
OPERATIONDENIED_DEVICENOTFOUND = 'OperationDenied.DeviceNotFound'

# SN already exists
OPERATIONDENIED_DUPLICATESN = 'OperationDenied.DuplicateSN'

# Hardware corresponding to SN has been activated
OPERATIONDENIED_HARDWAREHASACTIVATED = 'OperationDenied.HardwareHasActivated'

# The hardware corresponding to the input SN does not exist.
OPERATIONDENIED_HARDWARENOTEXIST = 'OperationDenied.HardwareNotExist'

# Invalid request, might be replay attack or forged attack.
OPERATIONDENIED_ILLEGALREQUEST = 'OperationDenied.IllegalRequest'

# Insufficient balance
OPERATIONDENIED_INSUFFICIENTBALANCE = 'OperationDenied.InsufficientBalance'

# Interconnection rule CIDR overlap
OPERATIONDENIED_L3CIDROVERLAP = 'OperationDenied.L3CidrOverLap'

# Number of interconnection rules exceeds the maximum limit of 150
OPERATIONDENIED_L3CONNECTIONOVERSIZE = 'OperationDenied.L3ConnectionOverSize'

# The resource package has been modified or renewed
OPERATIONDENIED_MODIFIEDORRENEWED = 'OperationDenied.ModifiedOrRenewed'

# No Payment Permission
OPERATIONDENIED_NOTALLOWEDTOPAY = 'OperationDenied.NotAllowedToPay'

# Repeat purchase
OPERATIONDENIED_REPEATPURCHASE = 'OperationDenied.RepeatPurchase'

# Truncation is enabled
OPERATIONDENIED_TRUNCFLAGON = 'OperationDenied.TruncFlagOn'

# Not identity verified
OPERATIONDENIED_UNAUTHORIZEDUSER = 'OperationDenied.UnauthorizedUser'

# The current account is not yet registered as a manufacturer.
OPERATIONDENIED_VENDORNOTREGISTER = 'OperationDenied.VendorNotRegister'

# The resource is occupied.
RESOURCEINUSE = 'ResourceInUse'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# Resources are unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Service permission not verified
UNAUTHORIZEDOPERATION_NOPERMISSION = 'UnauthorizedOperation.NoPermission'

# Live stream service not activated
UNAUTHORIZEDOPERATION_UNOPENEDLIVESERVICE = 'UnauthorizedOperation.UnopenedLiveService'
