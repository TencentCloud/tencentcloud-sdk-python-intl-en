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


# Request timeout at the engine layer. try again later.
FAILEDOPERATION_ENGINEREQUESTTIMEOUT = 'FailedOperation.EngineRequestTimeout'

# Internal error at the engine layer. try again later.
FAILEDOPERATION_ENGINESERVERERROR = 'FailedOperation.EngineServerError'

# Request exceeds the limit at the engine layer. try again later.
FAILEDOPERATION_ENGINESERVERLIMITEXCEEDED = 'FailedOperation.EngineServerLimitExceeded'

# The remaining free resource package quota is exhausted. purchase a resource pack or enable post-payment.
FAILEDOPERATION_FREERESOURCEPACKEXHAUSTED = 'FailedOperation.FreeResourcePackExhausted'

# The remaining resource package quota is exhausted. purchase a resource pack or enable post-payment.
FAILEDOPERATION_RESOURCEPACKEXHAUSTED = 'FailedOperation.ResourcePackExhausted'

# The service is not activated. go to the console to apply for a trial.
FAILEDOPERATION_SERVICENOTACTIVATED = 'FailedOperation.ServiceNotActivated'

# User proactively stopped services.
FAILEDOPERATION_SERVICESTOP = 'FailedOperation.ServiceStop'

# Service suspended due to overdue payments.
FAILEDOPERATION_SERVICESTOPARREARS = 'FailedOperation.ServiceStopArrears'

# Internal error.
INTERNALERROR = 'InternalError'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# Parameter value error.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Model does not exist.
INVALIDPARAMETERVALUE_MODEL = 'InvalidParameterValue.Model'

# The quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'
