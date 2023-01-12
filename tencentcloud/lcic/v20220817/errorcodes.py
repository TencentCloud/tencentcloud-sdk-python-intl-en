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


# Class status error. The class has already started.
FAILEDOPERATION_CLASSSTARTED = 'FailedOperation.ClassStarted'

# A class session cannot be longer than five hours.
FAILEDOPERATION_CLASSTOOLONG = 'FailedOperation.ClassTooLong'

# The user origin ID already exists.
FAILEDOPERATION_ORIGINIDEXISTS = 'FailedOperation.OriginIdExists'

# The class has not ended.
FAILEDOPERATION_ROOMNOTEND = 'FailedOperation.RoomNotEnd'

# Internal error.
INTERNALERROR = 'InternalError'

# Invalid parameter.
INVALIDPARAMETER = 'InvalidParameter'

# The end time cannot be earlier than the current time.
INVALIDPARAMETER_ENDTIME = 'InvalidParameter.EndTime'

# `SdkAppId` is incorrect.
INVALIDPARAMETER_SDKAPPID = 'InvalidParameter.SdkAppId'

# The start time cannot be earlier than the current time.
INVALIDPARAMETER_STARTTIME = 'InvalidParameter.StartTime'

# Insufficient resource.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# Insufficient storage space.
RESOURCEINSUFFICIENT_RECORD = 'ResourceInsufficient.Record'

# Failed to enter the class. Please check your resource usage in the console.
RESOURCEINSUFFICIENT_ROOM = 'ResourceInsufficient.Room'

# The file does not exist.
RESOURCENOTFOUND_DOCUMENT = 'ResourceNotFound.Document'

# The room does not exist.
RESOURCENOTFOUND_ROOM = 'ResourceNotFound.Room'

# The user does not exist.
RESOURCENOTFOUND_USER = 'ResourceNotFound.User'

# Getting room data. Please wait.
RESOURCEUNAVAILABLE_ROOMSTATISTICS = 'ResourceUnavailable.RoomStatistics'
