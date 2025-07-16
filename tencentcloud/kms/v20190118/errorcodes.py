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


# CAM signature/authentication error
AUTHFAILURE = 'AuthFailure'

# Unauthorized operation.
AUTHFAILURE_UNAUTHORIZEDOPERATION = 'AuthFailure.UnauthorizedOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# The CMK is being used by a Tencent Cloud product.
FAILEDOPERATION_CMKUSEDBYCLOUDPRODUCT = 'FailedOperation.CmkUsedByCloudProduct'

# Decryption failed.
FAILEDOPERATION_DECRYPTERROR = 'FailedOperation.DecryptError'

# Encryption failed.
FAILEDOPERATION_ENCRYPTIONERROR = 'FailedOperation.EncryptionError'

# Tagging error.
FAILEDOPERATION_TAGGINGERROR = 'FailedOperation.TaggingError'

# Internal error.
INTERNALERROR = 'InternalError'

# Invalid parameter.
INVALIDPARAMETER = 'InvalidParameter'

# Decryption of `EncryptedKeyMaterial` failed.
INVALIDPARAMETER_DECRYPTMATERIALERROR = 'InvalidParameter.DecryptMaterialError'

# The schedule deletion time parameter is invalid.
INVALIDPARAMETER_INVALIDPENDINGWINDOWINDAYS = 'InvalidParameter.InvalidPendingWindowInDays'

# Incorrect parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The alias already exists.
INVALIDPARAMETERVALUE_ALIASALREADYEXISTS = 'InvalidParameterValue.AliasAlreadyExists'

# The data key name already exists.
INVALIDPARAMETERVALUE_DATAKEYNAMEALREADYEXISTS = 'InvalidParameterValue.DataKeyNameAlreadyExists'

# Duplicate data key ID exists.
INVALIDPARAMETERVALUE_DUPLICATEDDATAKEYID = 'InvalidParameterValue.DuplicatedDataKeyId'

# Duplicate `KeyId`.
INVALIDPARAMETERVALUE_DUPLICATEDKEYID = 'InvalidParameterValue.DuplicatedKeyId'

# Incorrect alias format
INVALIDPARAMETERVALUE_INVALIDALIAS = 'InvalidParameterValue.InvalidAlias'

# Incorrect ciphertext format
INVALIDPARAMETERVALUE_INVALIDCIPHERTEXT = 'InvalidParameterValue.InvalidCiphertext'

# Invalid data key ID.
INVALIDPARAMETERVALUE_INVALIDDATAKEYID = 'InvalidParameterValue.InvalidDataKeyId'

# Invalid data key name.
INVALIDPARAMETERVALUE_INVALIDDATAKEYNAME = 'InvalidParameterValue.InvalidDataKeyName'

# Invalid HSM cluster ID.
INVALIDPARAMETERVALUE_INVALIDHSMCLUSTERID = 'InvalidParameterValue.InvalidHsmClusterId'

# The imported data key is valid.
INVALIDPARAMETERVALUE_INVALIDIMPORTKEYMATERIAL = 'InvalidParameterValue.InvalidImportKeyMaterial'

# Invalid `KeyId`.
INVALIDPARAMETERVALUE_INVALIDKEYID = 'InvalidParameterValue.InvalidKeyId'

# Incorrect `KeyUsage` parameter.
INVALIDPARAMETERVALUE_INVALIDKEYUSAGE = 'InvalidParameterValue.InvalidKeyUsage'

# Invalid `Plaintext`.
INVALIDPARAMETERVALUE_INVALIDPLAINTEXT = 'InvalidParameterValue.InvalidPlaintext'

# Incorrect `Type` parameter.
INVALIDPARAMETERVALUE_INVALIDTYPE = 'InvalidParameterValue.InvalidType'

# The key material is different from the one previously imported.
INVALIDPARAMETERVALUE_MATERIALNOTMATCH = 'InvalidParameterValue.MaterialNotMatch'

# Duplicate tag key.
INVALIDPARAMETERVALUE_TAGKEYSDUPLICATED = 'InvalidParameterValue.TagKeysDuplicated'

# The tag key or tag value does not exist.
INVALIDPARAMETERVALUE_TAGSNOTEXISTED = 'InvalidParameterValue.TagsNotExisted'

# The number of CMKs has reached the upper limit.
LIMITEXCEEDED_CMKLIMITEXCEEDED = 'LimitExceeded.CmkLimitExceeded'

# DataKey exceeds the upper limit.
LIMITEXCEEDED_DATAKEYLIMITEXCEEDED = 'LimitExceeded.DataKeyLimitExceeded'

# The number of device fingerprints exceeded the limit.
LIMITEXCEEDED_FINGERPRINTSLIMITEXCEEDED = 'LimitExceeded.FingerprintsLimitExceeded'

# The number of created keys exceeded the limit.
LIMITEXCEEDED_KEYLIMITEXCEEDED = 'LimitExceeded.KeyLimitExceeded'

# Missing parameters. Please check and try again.
MISSINGPARAMETER = 'MissingParameter'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The CMK is not bound with the Tencent Cloud resource
RESOURCEUNAVAILABLE_CLOUDRESOURCEBINDINGNOTFOUND = 'ResourceUnavailable.CloudResourceBindingNotFound'

# The CMK has been archived.
RESOURCEUNAVAILABLE_CMKARCHIVED = 'ResourceUnavailable.CmkArchived'

# The CMK has been disabled.
RESOURCEUNAVAILABLE_CMKDISABLED = 'ResourceUnavailable.CmkDisabled'

# The CMK does not exist.
RESOURCEUNAVAILABLE_CMKNOTFOUND = 'ResourceUnavailable.CmkNotFound'

# As the CMK is not scheduled for deletion, you cannot cancel the schedule deletion.
RESOURCEUNAVAILABLE_CMKNOTPENDINGDELETE = 'ResourceUnavailable.CmkNotPendingDelete'

# An enabled CMK cannot be scheduled for deletion.
RESOURCEUNAVAILABLE_CMKSHOULDBEDISABLED = 'ResourceUnavailable.CmkShouldBeDisabled'

# This operation cannot be performed under the current CMK status.
RESOURCEUNAVAILABLE_CMKSTATENOTSUPPORT = 'ResourceUnavailable.CmkStateNotSupport'

# The data key is disabled.
RESOURCEUNAVAILABLE_DATAKEYDISABLED = 'ResourceUnavailable.DataKeyDisabled'

# The data key does not exist.
RESOURCEUNAVAILABLE_DATAKEYNOTFOUND = 'ResourceUnavailable.DataKeyNotFound'

# The data key is not in scheduled deletion status and cannot execute cancel scheduled deletion.
RESOURCEUNAVAILABLE_DATAKEYNOTPENDINGDELETE = 'ResourceUnavailable.DataKeyNotPendingDelete'

# The data key is scheduled for deletion.
RESOURCEUNAVAILABLE_DATAKEYPENDINGDELETE = 'ResourceUnavailable.DataKeyPendingDelete'

# Data operation is not supported for the data key status.
RESOURCEUNAVAILABLE_DATAKEYSTATENOTSUPPORT = 'ResourceUnavailable.DataKeyStateNotSupport'

# The key has been disabled.
RESOURCEUNAVAILABLE_KEYDISABLED = 'ResourceUnavailable.KeyDisabled'

# The key is not available as it’s pending deleted.
RESOURCEUNAVAILABLE_KEYPENDINGDELETE = 'ResourceUnavailable.KeyPendingDelete'

# The white-box key service has not been activated.
RESOURCEUNAVAILABLE_NOTPURCHASED = 'ResourceUnavailable.NotPurchased'

# Token has expired.
RESOURCEUNAVAILABLE_TOKENEXPIRED = 'ResourceUnavailable.TokenExpired'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# External CMKs cannot be rotated.
UNSUPPORTEDOPERATION_EXTERNALCMKCANNOTROTATE = 'UnsupportedOperation.ExternalCmkCanNotRotate'

# Incorrect CMK type. Only `External` CMKs are supported.
UNSUPPORTEDOPERATION_NOTEXTERNALCMK = 'UnsupportedOperation.NotExternalCmk'

# You can only update the CMKs created by you.
UNSUPPORTEDOPERATION_NOTUSERCREATEDCMK = 'UnsupportedOperation.NotUserCreatedCmk'

# The service is temporarily unavailable.
UNSUPPORTEDOPERATION_SERVICETEMPORARYUNAVAILABLE = 'UnsupportedOperation.ServiceTemporaryUnavailable'

# The encryption method is not supported in the current region.
UNSUPPORTEDOPERATION_UNSUPPORTEDKEYUSAGEINCURRENTREGION = 'UnsupportedOperation.UnsupportedKeyUsageInCurrentRegion'
