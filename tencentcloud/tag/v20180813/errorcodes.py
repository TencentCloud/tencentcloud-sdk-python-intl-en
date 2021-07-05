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


# CAM authentication failed.
AUTHFAILURE_UNAUTHORIZEDOPERATION = 'AuthFailure.UnauthorizedOperation'

# The `appId` of resources in one single request must be the same.
FAILEDOPERATION_RESOURCEAPPIDNOTSAME = 'FailedOperation.ResourceAppIdNotSame'

# Tags associated with resources cannot be deleted.
FAILEDOPERATION_TAGATTACHEDRESOURCE = 'FailedOperation.TagAttachedResource'

# Incorrect parameter.
INVALIDPARAMETER = 'InvalidParameter'

# System reserved tag keys `qcloud`, `tencent` and `project` cannot be created.
INVALIDPARAMETER_RESERVEDTAGKEY = 'InvalidParameter.ReservedTagKey'

# `Tag` parameter error.
INVALIDPARAMETER_TAG = 'InvalidParameter.Tag'

# `DeleteTags` cannot contain the elements in `ReplaceTags` or `AddTags`.
INVALIDPARAMETERVALUE_DELETETAGSPARAMERROR = 'InvalidParameterValue.DeleteTagsParamError'

# Offset error.
INVALIDPARAMETERVALUE_OFFSETINVALID = 'InvalidParameterValue.OffsetInvalid'

# Region error.
INVALIDPARAMETERVALUE_REGIONINVALID = 'InvalidParameterValue.RegionInvalid'

# System reserved tag keys `qcloud`, `tencent` and `project` cannot be created.
INVALIDPARAMETERVALUE_RESERVEDTAGKEY = 'InvalidParameterValue.ReservedTagKey'

# Resource description error.
INVALIDPARAMETERVALUE_RESOURCEDESCRIPTIONERROR = 'InvalidParameterValue.ResourceDescriptionError'

# Resource ID error.
INVALIDPARAMETERVALUE_RESOURCEIDINVALID = 'InvalidParameterValue.ResourceIdInvalid'

# Resource prefix error.
INVALIDPARAMETERVALUE_RESOURCEPREFIXINVALID = 'InvalidParameterValue.ResourcePrefixInvalid'

# Service type error.
INVALIDPARAMETERVALUE_SERVICETYPEINVALID = 'InvalidParameterValue.ServiceTypeInvalid'

# `TagFilters` parameter error
INVALIDPARAMETERVALUE_TAGFILTERS = 'InvalidParameterValue.TagFilters'

# Tag filtering arrays reached the upper limit 6 when querying resources by tag.
INVALIDPARAMETERVALUE_TAGFILTERSLENGTHEXCEEDED = 'InvalidParameterValue.TagFiltersLengthExceeded'

# Tag key contains illegal characters.
INVALIDPARAMETERVALUE_TAGKEYCHARACTERILLEGAL = 'InvalidParameterValue.TagKeyCharacterIllegal'

# Tag key cannot be empty.
INVALIDPARAMETERVALUE_TAGKEYEMPTY = 'InvalidParameterValue.TagKeyEmpty'

# Tag key length exceeds limit.
INVALIDPARAMETERVALUE_TAGKEYLENGTHEXCEEDED = 'InvalidParameterValue.TagKeyLengthExceeded'

# Tag value contains illegal characters.
INVALIDPARAMETERVALUE_TAGVALUECHARACTERILLEGAL = 'InvalidParameterValue.TagValueCharacterIllegal'

# Tag value length exceeds limit.
INVALIDPARAMETERVALUE_TAGVALUELENGTHEXCEEDED = 'InvalidParameterValue.TagValueLengthExceeded'

# `Uin` parameter is invalid.
INVALIDPARAMETERVALUE_UININVALID = 'InvalidParameterValue.UinInvalid'

# The number of tags associated with the resource exceeds the limit.
LIMITEXCEEDED_RESOURCEATTACHEDTAGS = 'LimitExceeded.ResourceAttachedTags'

# The number of resources requested at a time reaches the upper limit.
LIMITEXCEEDED_RESOURCENUMPERREQUEST = 'LimitExceeded.ResourceNumPerRequest'

# The number of created tag keys reaches the limit of 1,000.
LIMITEXCEEDED_TAGKEY = 'LimitExceeded.TagKey'

# Each tag key can have up to 1,000 values.
LIMITEXCEEDED_TAGVALUE = 'LimitExceeded.TagValue'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# Tag already exists.
RESOURCEINUSE_TAGDUPLICATE = 'ResourceInUse.TagDuplicate'

# The corresponding tag key has already been associated with the resource.
RESOURCEINUSE_TAGKEYATTACHED = 'ResourceInUse.TagKeyAttached'

# The tag key associated with the resource doesn’t exist.
RESOURCENOTFOUND_ATTACHEDTAGKEYNOTFOUND = 'ResourceNotFound.AttachedTagKeyNotFound'

# Tag does not exist.
RESOURCENOTFOUND_TAGNONEXIST = 'ResourceNotFound.TagNonExist'
