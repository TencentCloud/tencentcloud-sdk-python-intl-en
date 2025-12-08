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


# Internal error.
INTERNALERROR = 'InternalError'

# Media library resource deletion failed.
INTERNALERROR_MODIFYRESOURCESTATUSFAIL = 'InternalError.ModifyResourceStatusFail'

# Post-Payment activation failed.
INTERNALERROR_POSTPAIDFAIL = 'InternalError.PostpaidFail'

# Error occurs when sending sms verification code.
INTERNALERROR_SENDSMS = 'InternalError.SendSms'

# Parameter value error.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The bucket name is invalid.
INVALIDPARAMETERVALUE_BUCKETNAMEINVALID = 'InvalidParameterValue.BucketNameInvalid'

# The bucket name does not belong to the current root account.
INVALIDPARAMETERVALUE_BUCKETNAMENOTBELONGYOU = 'InvalidParameterValue.BucketNameNotBelongYou'

# The bucket does not exist or is not in the specified region.
INVALIDPARAMETERVALUE_BUCKETNOTFOUND = 'InvalidParameterValue.BucketNotFound'

# The service no longer supports selected buckets.
INVALIDPARAMETERVALUE_BUCKETNOTSUPPORT = 'InvalidParameterValue.BucketNotSupport'

# Bucket location is invalid.
INVALIDPARAMETERVALUE_BUCKETREGIONINVALID = 'InvalidParameterValue.BucketRegionInvalid'

# The specified storage class is invalid.
INVALIDPARAMETERVALUE_COSSTORAGECLASS = 'InvalidParameterValue.CosStorageClass'

# The specified bucket does not have intelligent tiering storage enabled. activate the intelligent tiering storage feature for the bucket first.
INVALIDPARAMETERVALUE_COSSTORAGECLASSINTELLIGENTTIERING = 'InvalidParameterValue.CosStorageClassIntelligentTiering'

# The specified country code is invalid.
INVALIDPARAMETERVALUE_COUNTRYCODE = 'InvalidParameterValue.CountryCode'

# The number of parameter values or characters exceeds the limit.
INVALIDPARAMETERVALUE_LIMITEXCEEDED = 'InvalidParameterValue.LimitExceeded'

# The specified phone number is the same as the current one.
INVALIDPARAMETERVALUE_NOTMODIFIED = 'InvalidParameterValue.NotModified'

# The specified phone number is not the super administrator of the enterprise.
INVALIDPARAMETERVALUE_NOTSUPERADMIN = 'InvalidParameterValue.NotSuperAdmin'

# The specified phone number is invalid.
INVALIDPARAMETERVALUE_PHONENUMBER = 'InvalidParameterValue.PhoneNumber'

# The number of users has been reached. please first upgrade the product spec.
LIMITEXCEEDED_USERLIMIT = 'LimitExceeded.UserLimit'

# The sms verification code sent to the designated mobile number has reached the rate limit.
REQUESTLIMITEXCEEDED_SENDSMS = 'RequestLimitExceeded.SendSms'

# A tenant space in the multi-tenant media library is in use.
RESOURCEINUSE_MULTISPACE = 'ResourceInUse.MultiSpace'

# The media library does not exist or does not belong to the current account.
RESOURCENOTFOUND_LIBRARY = 'ResourceNotFound.Library'

# The official cloud disk instance does not exist or does not belong to the current account.
RESOURCENOTFOUND_OFFICIALINSTANCE = 'ResourceNotFound.OfficialInstance'

# cam:PassRole permission is not granted.
UNAUTHORIZEDOPERATION_PASSROLE = 'UnauthorizedOperation.PassRole'

# SMH service-related role is not granted.
UNAUTHORIZEDOPERATION_SERVICELINKEDROLE = 'UnauthorizedOperation.ServiceLinkedRole'

# Incorrect or expired sms verification code.
UNAUTHORIZEDOPERATION_SMSCODE = 'UnauthorizedOperation.SmsCode'

# SMS verification code verification count exceeded. please resend the sms verification code.
UNAUTHORIZEDOPERATION_SMSCODEEXCEEDED = 'UnauthorizedOperation.SmsCodeExceeded'

# Insufficient account balance.
UNSUPPORTEDOPERATION_BALANCELESS = 'UnsupportedOperation.BalanceLess'

# The specified purpose is unsupported.
UNSUPPORTEDOPERATION_PURPOSE = 'UnsupportedOperation.Purpose'
