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


# A CAM signature/authentication error occurred.
AUTHFAILURE = 'AuthFailure'

# The operation is unauthorized.
AUTHFAILURE_UNAUTHORIZEDOPERATION = 'AuthFailure.UnauthorizedOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# You do not have permission to perform this operation.
FAILEDOPERATION_AUTHERROR = 'FailedOperation.AuthError'

# A CAM authentication error occurred.
FAILEDOPERATION_CAMAUTHORIZEDFAIL = 'FailedOperation.CAMAuthorizedFail'

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

# The confirmation letter file cannot exceed 1.4 MB.
FAILEDOPERATION_CONFIRMLETTERTOOLARGE = 'FailedOperation.ConfirmLetterTooLarge'

# The confirmation letter file cannot be smaller than 1 KB.
FAILEDOPERATION_CONFIRMLETTERTOOSMALL = 'FailedOperation.ConfirmLetterTooSmall'

# The certificate is associated with a Tencent Cloud resource and cannot be deleted.
FAILEDOPERATION_DELETERESOURCEFAILED = 'FailedOperation.DeleteResourceFailed'

# The number of free certificates exceeds the maximum value.
FAILEDOPERATION_EXCEEDSFREELIMIT = 'FailedOperation.ExceedsFreeLimit'

# Certificate source error.
FAILEDOPERATION_INVALIDCERTIFICATESOURCE = 'FailedOperation.InvalidCertificateSource'

# The certificate status is incorrect.
FAILEDOPERATION_INVALIDCERTIFICATESTATUSCODE = 'FailedOperation.InvalidCertificateStatusCode'

# The format of the confirmation letter file is invalid (JPG, JPEG, PNG, and PDF are supported).
FAILEDOPERATION_INVALIDCONFIRMLETTERFORMAT = 'FailedOperation.InvalidConfirmLetterFormat'

# The format of the confirmation letter file is invalid (JPG, PDF, and GIF are supported).
FAILEDOPERATION_INVALIDCONFIRMLETTERFORMATWOSIGN = 'FailedOperation.InvalidConfirmLetterFormatWosign'

# Incorrect parameters.
FAILEDOPERATION_INVALIDPARAM = 'FailedOperation.InvalidParam'

# The number of free certificates applied for under the primary domain name (%s) has reached the upper limit of %s. Please purchase a paid certificate.
FAILEDOPERATION_MAINDOMAINCERTIFICATECOUNTLIMIT = 'FailedOperation.MainDomainCertificateCountLimit'

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

# The remaining benefit points are insufficient.
FAILEDOPERATION_PACKAGECOUNTLIMIT = 'FailedOperation.PackageCountLimit'

# The benefit package has expired.
FAILEDOPERATION_PACKAGEEXPIRED = 'FailedOperation.PackageExpired'

# A system error occurred.
FAILEDOPERATION_SYSTEMERROR = 'FailedOperation.SystemError'

# Internal error.
INTERNALERROR = 'InternalError'

# The backend service response is empty.
INTERNALERROR_BACKENDRESPONSEEMPTY = 'InternalError.BackendResponseEmpty'

# An error occurred with the backend service response.
INTERNALERROR_BACKENDRESPONSEERROR = 'InternalError.BackendResponseError'

# The parameter is incorrect.
INVALIDPARAMETER = 'InvalidParameter'

# The list of benefit point IDs is invalid.
INVALIDPARAMETER_PACKAGEIDSINVALID = 'InvalidParameter.PackageIdsInvalid'

# The parameter is incorrect.
INVALIDPARAMETER_WITHDETAILREASON = 'InvalidParameter.WithDetailReason'

# Invalid parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The API rate limit is reached.
LIMITEXCEEDED_RATELIMITEXCEEDED = 'LimitExceeded.RateLimitExceeded'

# Missing parameter.
MISSINGPARAMETER = 'MissingParameter'
