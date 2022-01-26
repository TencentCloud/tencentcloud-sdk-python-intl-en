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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.ssm.v20190923 import models


class SsmClient(AbstractClient):
    _apiVersion = '2019-09-23'
    _endpoint = 'ssm.tencentcloudapi.com'
    _service = 'ssm'


    def CreateProductSecret(self, request):
        """This API is used to create a Tencent Cloud service credential.

        :param request: Request instance for CreateProductSecret.
        :type request: :class:`tencentcloud.ssm.v20190923.models.CreateProductSecretRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.CreateProductSecretResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateProductSecret", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProductSecretResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSSHKeyPairSecret(self, request):
        """This API is used to create a secret that hosts SSH keys.

        :param request: Request instance for CreateSSHKeyPairSecret.
        :type request: :class:`tencentcloud.ssm.v20190923.models.CreateSSHKeyPairSecretRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.CreateSSHKeyPairSecretResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSSHKeyPairSecret", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSSHKeyPairSecretResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSecret(self, request):
        """This API is used to create a KMS-encrypted Secret. You can create and store up to 1,000 Secrets in each region.

        :param request: Request instance for CreateSecret.
        :type request: :class:`tencentcloud.ssm.v20190923.models.CreateSecretRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.CreateSecretResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSecret", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSecretResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSecret(self, request):
        """This API is used to delete a Secret. You can set whether to delete the Secret immediately or on schedule using the `RecoveryWindowInDays` parameter. For a Secret to be deleted on schedule, its status will be `PendingDelete` before the scheduled deletion time. You can use `RestoreSecret` to restore a deleted Secret during this time. A deleted Secret will not be restorable after the scheduled deletion time. A Secret can only be deleted after being disabled using `DisableSecret`.

        :param request: Request instance for DeleteSecret.
        :type request: :class:`tencentcloud.ssm.v20190923.models.DeleteSecretRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.DeleteSecretResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSecret", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSecretResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSecretVersion(self, request):
        """This API is used to directly delete a single credential version under the specified credential. The deletion takes effect immediately, and the credential version in all status can be deleted.
        This API is only applicable to user-defined credentials but not Tencent Cloud service credentials.

        :param request: Request instance for DeleteSecretVersion.
        :type request: :class:`tencentcloud.ssm.v20190923.models.DeleteSecretVersionRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.DeleteSecretVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSecretVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSecretVersionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAsyncRequestInfo(self, request):
        """This API is used to query the execution result of an async task.

        :param request: Request instance for DescribeAsyncRequestInfo.
        :type request: :class:`tencentcloud.ssm.v20190923.models.DescribeAsyncRequestInfoRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.DescribeAsyncRequestInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAsyncRequestInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAsyncRequestInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRotationDetail(self, request):
        """This API is used to query the details of a credential rotation policy.
        This API is only applicable to Tencent Cloud service credentials.

        :param request: Request instance for DescribeRotationDetail.
        :type request: :class:`tencentcloud.ssm.v20190923.models.DescribeRotationDetailRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.DescribeRotationDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRotationDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRotationDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRotationHistory(self, request):
        """This API is used to query the historical versions of a rotated credential.
        This API is only applicable to Tencent Cloud service credentials.

        :param request: Request instance for DescribeRotationHistory.
        :type request: :class:`tencentcloud.ssm.v20190923.models.DescribeRotationHistoryRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.DescribeRotationHistoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRotationHistory", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRotationHistoryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecret(self, request):
        """This API is used to obtain the detailed attribute information of a Secret.

        :param request: Request instance for DescribeSecret.
        :type request: :class:`tencentcloud.ssm.v20190923.models.DescribeSecretRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.DescribeSecretResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecret", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecretResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSupportedProducts(self, request):
        """This API is used to query the list of supported Tencent Cloud services.

        :param request: Request instance for DescribeSupportedProducts.
        :type request: :class:`tencentcloud.ssm.v20190923.models.DescribeSupportedProductsRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.DescribeSupportedProductsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSupportedProducts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSupportedProductsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisableSecret(self, request):
        """This API is used to disable a Secret and will change its status to `Disabled`. The plaintext of a disabled Secret cannot be obtained through APIs.

        :param request: Request instance for DisableSecret.
        :type request: :class:`tencentcloud.ssm.v20190923.models.DisableSecretRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.DisableSecretResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableSecret", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableSecretResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnableSecret(self, request):
        """This API is used to enable a Secret and will change its status to `Enabled`. You can call the `GetSecretValue` API to obtain the plaintext of this Secret. Secrets in `PendingDelete` status can only be enabled after being restored by using `RestoreSecret`.

        :param request: Request instance for EnableSecret.
        :type request: :class:`tencentcloud.ssm.v20190923.models.EnableSecretRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.EnableSecretResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableSecret", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableSecretResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetRegions(self, request):
        """This API is used to obtain the list of regions displayed on Console.

        :param request: Request instance for GetRegions.
        :type request: :class:`tencentcloud.ssm.v20190923.models.GetRegionsRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.GetRegionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetRegions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetRegionsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetSSHKeyPairValue(self, request):
        """This API is used to obtain the plaintext value of the SSH key secret.

        :param request: Request instance for GetSSHKeyPairValue.
        :type request: :class:`tencentcloud.ssm.v20190923.models.GetSSHKeyPairValueRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.GetSSHKeyPairValueResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetSSHKeyPairValue", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetSSHKeyPairValueResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetSecretValue(self, request):
        """For user-defined credentials, this API is used to get the plaintext information of a credential by specifying the credential name and version.
        For Tencent Cloud service credentials such as MySQL credentials, this API is used to get the plaintext information of a previously rotated credential by specifying the credential name and historical version number. If you want to get the plaintext of the credential version currently in use, you need to specify the version number as `SSM_Current`.

        :param request: Request instance for GetSecretValue.
        :type request: :class:`tencentcloud.ssm.v20190923.models.GetSecretValueRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.GetSecretValueResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetSecretValue", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetSecretValueResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetServiceStatus(self, request):
        """This API is used to obtain the SecretsManager service status of a user.

        :param request: Request instance for GetServiceStatus.
        :type request: :class:`tencentcloud.ssm.v20190923.models.GetServiceStatusRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.GetServiceStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetServiceStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetServiceStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListSecretVersionIds(self, request):
        """This API is used to obtain list of versions of a Secret.

        :param request: Request instance for ListSecretVersionIds.
        :type request: :class:`tencentcloud.ssm.v20190923.models.ListSecretVersionIdsRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.ListSecretVersionIdsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListSecretVersionIds", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListSecretVersionIdsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListSecrets(self, request):
        """This API is used to obtain the detailed information list of all Secrets. You can specify the filter fields and sorting order as needed.

        :param request: Request instance for ListSecrets.
        :type request: :class:`tencentcloud.ssm.v20190923.models.ListSecretsRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.ListSecretsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListSecrets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListSecretsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PutSecretValue(self, request):
        """This API adds the new version of the credential content under the specified credential. One credential can have up to 10 versions. New versions can be added to credentials only in `Enabled` or `Disabled` status.
        This API is only applicable to user-defined credentials but not Tencent Cloud service credentials.

        :param request: Request instance for PutSecretValue.
        :type request: :class:`tencentcloud.ssm.v20190923.models.PutSecretValueRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.PutSecretValueResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PutSecretValue", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PutSecretValueResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RestoreSecret(self, request):
        """This API is used to restore a `PendingDelete` Secret, canceling its scheduled deletion. The restored Secret will be in `Disabled` status. You can call the `EnableSecret` API to enable this Secret again.

        :param request: Request instance for RestoreSecret.
        :type request: :class:`tencentcloud.ssm.v20190923.models.RestoreSecretRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.RestoreSecretResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RestoreSecret", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RestoreSecretResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RotateProductSecret(self, request):
        """This API is used to rotate secrets for Tencent Cloud services or Tencent Cloud API key pairs.
        Note that only the secrets with the "Enabled" status can be rotated.

        :param request: Request instance for RotateProductSecret.
        :type request: :class:`tencentcloud.ssm.v20190923.models.RotateProductSecretRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.RotateProductSecretResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RotateProductSecret", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RotateProductSecretResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateDescription(self, request):
        """This API is used to update the description of a Secret. This API can only update Secrets in `Enabled` or `Disabled` status.

        :param request: Request instance for UpdateDescription.
        :type request: :class:`tencentcloud.ssm.v20190923.models.UpdateDescriptionRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.UpdateDescriptionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateDescription", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateDescriptionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateRotationStatus(self, request):
        """This API is used to set a Tencent Cloud service credential rotation policy, including the following parameters:
        Specifies whether to enable rotation
        Rotation frequency
        Rotation start time

        :param request: Request instance for UpdateRotationStatus.
        :type request: :class:`tencentcloud.ssm.v20190923.models.UpdateRotationStatusRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.UpdateRotationStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateRotationStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateRotationStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateSecret(self, request):
        """This API is used to update the credential content of the specified credential name and version number. Calling this API will encrypt the content of the new credential and overwrite the old content. Only credentials in `Enabled` or `Disabled` status can be updated.
        This API is only applicable to user-defined credentials but not Tencent Cloud service credentials.

        :param request: Request instance for UpdateSecret.
        :type request: :class:`tencentcloud.ssm.v20190923.models.UpdateSecretRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.UpdateSecretResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateSecret", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateSecretResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)