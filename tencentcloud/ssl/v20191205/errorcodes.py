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


# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# You do not have permission to perform this operation.
FAILEDOPERATION_AUTHERROR = 'FailedOperation.AuthError'

# Failed to cancel the order.
FAILEDOPERATION_CANCELORDERFAILED = 'FailedOperation.CancelOrderFailed'

# Failed to delete the certificate because it has been issued.
FAILEDOPERATION_CANNOTBEDELETEDISSUED = 'FailedOperation.CannotBeDeletedIssued'

# Free certificates cannot be deleted within 1 hour after being applied for.
FAILEDOPERATION_CANNOTBEDELETEDWITHINHOUR = 'FailedOperation.CannotBeDeletedWithinHour'

# Failed to get order information. Try again later.
FAILEDOPERATION_CANNOTGETORDER = 'FailedOperation.CannotGetOrder'

# The certificate already exists.
FAILEDOPERATION_CERTIFICATEEXISTS = 'FailedOperation.CertificateExists'

# The certificate is invalid.
FAILEDOPERATION_CERTIFICATEINVALID = 'FailedOperation.CertificateInvalid'

# The certificate and the private key do not match.
FAILEDOPERATION_CERTIFICATEMISMATCH = 'FailedOperation.CertificateMismatch'

# The certificate does not exist.
FAILEDOPERATION_CERTIFICATENOTFOUND = 'FailedOperation.CertificateNotFound'

# The number of free certificates exceeds the maximum value.
FAILEDOPERATION_EXCEEDSFREELIMIT = 'FailedOperation.ExceedsFreeLimit'

# The certificate status is incorrect.
FAILEDOPERATION_INVALIDCERTIFICATESTATUSCODE = 'FailedOperation.InvalidCertificateStatusCode'

# Incorrect parameters.
FAILEDOPERATION_INVALIDPARAM = 'FailedOperation.InvalidParam'

# The CA system is busy. Try again later.
FAILEDOPERATION_NETWORKERROR = 'FailedOperation.NetworkError'

# You do not have the permission to operate on this project.
FAILEDOPERATION_NOPROJECTPERMISSION = 'FailedOperation.NoProjectPermission'

# You have not completed the identity verification.
FAILEDOPERATION_NOREALNAMEAUTH = 'FailedOperation.NoRealNameAuth'

# This order has already been replaced.
FAILEDOPERATION_ORDERALREADYREPLACED = 'FailedOperation.OrderAlreadyReplaced'

# Failed to reissue a certificate.
FAILEDOPERATION_ORDERREPLACEFAILED = 'FailedOperation.OrderReplaceFailed'

# Internal error.
INTERNALERROR = 'InternalError'
