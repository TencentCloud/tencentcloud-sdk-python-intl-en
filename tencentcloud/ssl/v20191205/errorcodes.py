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

# This operation can be performed only when the record status is Complete.
FAILEDOPERATION_CERTIFICATEDEPLOYDETAILROLLBACKSTATUSINVALID = 'FailedOperation.CertificateDeployDetailRollbackStatusInvalid'

# There is a running certificate deployment task. Please try again after the deployment is complete.
FAILEDOPERATION_CERTIFICATEDEPLOYHASPENDINGRECORD = 'FailedOperation.CertificateDeployHasPendingRecord'

# There is no instance for the selected cloud resource. Updating failed. Please try again after checking it.
FAILEDOPERATION_CERTIFICATEDEPLOYINSTANCEEMPTY = 'FailedOperation.CertificateDeployInstanceEmpty'

# The certificate deployment record does not exist.
FAILEDOPERATION_CERTIFICATEDEPLOYNOTEXIST = 'FailedOperation.CertificateDeployNotExist'

# This operation can be performed only when the record status is Failed.
FAILEDOPERATION_CERTIFICATEDEPLOYRETRYSTATUSINVALID = 'FailedOperation.CertificateDeployRetryStatusInvalid'

# A rollback can be performed only when there is a record indicating successful deployment.
FAILEDOPERATION_CERTIFICATEDEPLOYROLLBACKSTATUSINVALID = 'FailedOperation.CertificateDeployRollbackStatusInvalid'

# The certificate is suspected to be an SM2 certificate and does not comply with the selected certificate standard. Please check whether the selected certificate standard and the content of the certificate are correct.
FAILEDOPERATION_CERTIFICATEENCRYPTINVALID = 'FailedOperation.CertificateEncryptInvalid'

# The certificate already exists.
FAILEDOPERATION_CERTIFICATEEXISTS = 'FailedOperation.CertificateExists'

# The current certificate is not allowed to use the one-click update function.
FAILEDOPERATION_CERTIFICATEHOSTDEPLOYCANNOTALLOW = 'FailedOperation.CertificateHostDeployCanNotAllow'

# Unable to use the deployment feature because the login account is an internal account with too many instance resources. Please contact us to handle it.
FAILEDOPERATION_CERTIFICATEHOSTRESOURCEINNERINTERRUPT = 'FailedOperation.CertificateHostResourceInnerInterrupt'

# There are too many instances under the current account. Loading cannot be performed properly. Please switch the loading mode. After switching, click "Refresh List" and wait for a period of time. Then, all the instances can be loaded.
FAILEDOPERATION_CERTIFICATEHOSTRESOURCEINSTANCEHUGELIMIT = 'FailedOperation.CertificateHostResourceInstanceHugeLimit'

# The cloud resource type is invalid.
FAILEDOPERATION_CERTIFICATEHOSTRESOURCETYPEINVALID = 'FailedOperation.CertificateHostResourceTypeInvalid'

# The certificate is invalid.
FAILEDOPERATION_CERTIFICATEINVALID = 'FailedOperation.CertificateInvalid'

# The certificate and the private key do not match.
FAILEDOPERATION_CERTIFICATEMISMATCH = 'FailedOperation.CertificateMismatch'

# The certificate is not available. Please check and try again.
FAILEDOPERATION_CERTIFICATENOTAVAILABLE = 'FailedOperation.CertificateNotAvailable'

# The certificate is not allowed to be deployed under the instance list.
FAILEDOPERATION_CERTIFICATENOTDEPLOYINSTANCE = 'FailedOperation.CertificateNotDeployInstance'

# The certificate does not exist.
FAILEDOPERATION_CERTIFICATENOTFOUND = 'FailedOperation.CertificateNotFound'

# The certificate does not exist, or the review cannot be canceled.
FAILEDOPERATION_CERTIFICATENOTFOUNDORCANTCANCEL = 'FailedOperation.CertificateNotFoundOrCantCancel'

# You cannot re-submit a review application for a certificate in this status.
FAILEDOPERATION_CERTIFICATESTATUSNOTALLOWRESUBMIT = 'FailedOperation.CertificateStatusNotAllowResubmit'

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

# The benefit package does not exist.
FAILEDOPERATION_PACKAGENOTFOUND = 'FailedOperation.PackageNotFound'

# The role does not exist. Please authorize the role first.
FAILEDOPERATION_ROLENOTFOUNDAUTHORIZATION = 'FailedOperation.RoleNotFoundAuthorization'

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

# u200cYou cannot re-submit a review application for a certificate in this status.
INVALIDPARAMETER_CERTIFICATESTATUSNOTALLOWRESUBMIT = 'InvalidParameter.CertificateStatusNotAllowResubmit'

# Incorrect CSR ID.
INVALIDPARAMETER_INVALIDCSRID = 'InvalidParameter.InvalidCSRId'

# There is no matching private key.
INVALIDPARAMETER_MISSMATCHPRIVATEKEY = 'InvalidParameter.MissMatchPrivateKey'

# The list of benefit point IDs is invalid.
INVALIDPARAMETER_PACKAGEIDSINVALID = 'InvalidParameter.PackageIdsInvalid'

# The algorithm is invalid.
INVALIDPARAMETER_RENEWALGORITHMINVALID = 'InvalidParameter.RenewAlgorithmInvalid'

# The parameter is incorrect.
INVALIDPARAMETER_WITHDETAILREASON = 'InvalidParameter.WithDetailReason'

# Invalid parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The API rate limit is reached.
LIMITEXCEEDED_RATELIMITEXCEEDED = 'LimitExceeded.RateLimitExceeded'

# Missing parameter.
MISSINGPARAMETER = 'MissingParameter'

# The manager of the company does not exist.
RESOURCENOTFOUND_MANAGER = 'ResourceNotFound.Manager'
