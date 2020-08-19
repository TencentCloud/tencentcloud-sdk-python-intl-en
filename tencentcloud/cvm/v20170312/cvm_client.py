# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.cvm.v20170312 import models


class CvmClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'cvm.tencentcloudapi.com'


    def AllocateHosts(self, request):
        """This API is used to create CDH instances with specified configuration.
        * When HostChargeType is PREPAID, the HostChargePrepaid parameter must be specified.

        :param request: Request instance for AllocateHosts.
        :type request: :class:`tencentcloud.cvm.v20170312.models.AllocateHostsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.AllocateHostsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AllocateHosts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AllocateHostsResponse()
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


    def AssociateInstancesKeyPairs(self, request):
        """This API is used to associate key pairs with instances.

        * If the public key of a key pair is written to the `SSH` configuration of the instance, users will be able to log in to the instance with the private key of the key pair.
        * If the instance is already associated with a key, the old key will become invalid.
        If you currently use a password to log in, you will no longer be able to do so after you associate the instance with a key.
        * Batch operations are supported. The maximum number of instances in each request is 100. If any instance in the request cannot be associated with a key, you will get an error code.

        :param request: Request instance for AssociateInstancesKeyPairs.
        :type request: :class:`tencentcloud.cvm.v20170312.models.AssociateInstancesKeyPairsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.AssociateInstancesKeyPairsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssociateInstancesKeyPairs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateInstancesKeyPairsResponse()
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


    def AssociateSecurityGroups(self, request):
        """This API is used to associate security groups with specified instances.

        :param request: Request instance for AssociateSecurityGroups.
        :type request: :class:`tencentcloud.cvm.v20170312.models.AssociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.AssociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssociateSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateSecurityGroupsResponse()
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


    def CreateDisasterRecoverGroup(self, request):
        """This API is used to create a [spread placement group](https://intl.cloud.tencent.com/document/product/213/15486?from_cn_redirect=1). After you create one, you can specify it for an instance when you [create the instance](https://intl.cloud.tencent.com/document/api/213/15730?from_cn_redirect=1),

        :param request: Request instance for CreateDisasterRecoverGroup.
        :type request: :class:`tencentcloud.cvm.v20170312.models.CreateDisasterRecoverGroupRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.CreateDisasterRecoverGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDisasterRecoverGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDisasterRecoverGroupResponse()
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


    def CreateImage(self, request):
        """This API is used to create a new image with the system disk of an instance. The image can be used to create new instances.

        :param request: Request instance for CreateImage.
        :type request: :class:`tencentcloud.cvm.v20170312.models.CreateImageRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.CreateImageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateImage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateImageResponse()
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


    def CreateKeyPair(self, request):
        """This API is used to create an `OpenSSH RSA` key pair, which you can use to log in to a `Linux` instance.

        * You only need to specify a name, and the system will automatically create a key pair and return its `ID` and the public and private keys.
        * The name of the key pair must be unique.
        * You can save the private key to a file and use it as an authentication method for `SSH`.
        * Tencent Cloud does not save users' private keys. Be sure to save it yourself.

        :param request: Request instance for CreateKeyPair.
        :type request: :class:`tencentcloud.cvm.v20170312.models.CreateKeyPairRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.CreateKeyPairResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateKeyPair", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateKeyPairResponse()
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


    def DeleteDisasterRecoverGroups(self, request):
        """This API is used to delete a [spread placement group](https://intl.cloud.tencent.com/document/product/213/15486?from_cn_redirect=1). Only empty placement groups can be deleted. To delete a non-empty group, you need to terminate all the CVM instances in it first. Otherwise, the deletion will fail.

        :param request: Request instance for DeleteDisasterRecoverGroups.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DeleteDisasterRecoverGroupsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DeleteDisasterRecoverGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDisasterRecoverGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDisasterRecoverGroupsResponse()
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


    def DeleteImages(self, request):
        """This API is used to delete images.

        * If the [ImageState](https://intl.cloud.tencent.com/document/api/213/9452?from_cn_redirect=1#image_state) of an image is `Creating` or `In Use`, it cannot be deleted. Use [DescribeImages](https://intl.cloud.tencent.com/document/api/213/9418?from_cn_redirect=1) to query the image state.
        * You can only create up to 10 custom images in each region. If you have used up the quota, you can delete images to create new ones.
        * A shared image cannot be deleted.

        :param request: Request instance for DeleteImages.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DeleteImagesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DeleteImagesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteImages", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteImagesResponse()
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


    def DeleteKeyPairs(self, request):
        """This API is used to delete the key pairs hosted in Tencent Cloud.

        * You can delete multiple key pairs at the same time.
        * A key pair used by an instance or image cannot be deleted. Therefore, you need to verify whether all the key pairs have been deleted successfully.

        :param request: Request instance for DeleteKeyPairs.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DeleteKeyPairsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DeleteKeyPairsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteKeyPairs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteKeyPairsResponse()
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


    def DescribeDisasterRecoverGroupQuota(self, request):
        """This API is used to query the quota of [spread placement groups](https://intl.cloud.tencent.com/document/product/213/15486?from_cn_redirect=1).

        :param request: Request instance for DescribeDisasterRecoverGroupQuota.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeDisasterRecoverGroupQuotaRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeDisasterRecoverGroupQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDisasterRecoverGroupQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDisasterRecoverGroupQuotaResponse()
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


    def DescribeDisasterRecoverGroups(self, request):
        """This API is used to query the information on [spread placement groups](https://intl.cloud.tencent.com/document/product/213/15486?from_cn_redirect=1).

        :param request: Request instance for DescribeDisasterRecoverGroups.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeDisasterRecoverGroupsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeDisasterRecoverGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDisasterRecoverGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDisasterRecoverGroupsResponse()
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


    def DescribeHosts(self, request):
        """This API is used to query the details of CDH instances.

        :param request: Request instance for DescribeHosts.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeHostsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeHostsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeHosts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeHostsResponse()
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


    def DescribeImageQuota(self, request):
        """This API is used to query the image quota of an user account.

        :param request: Request instance for DescribeImageQuota.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeImageQuotaRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeImageQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImageQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageQuotaResponse()
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


    def DescribeImageSharePermission(self, request):
        """This API is used to query image sharing information.

        :param request: Request instance for DescribeImageSharePermission.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeImageSharePermissionRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeImageSharePermissionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImageSharePermission", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageSharePermissionResponse()
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


    def DescribeImages(self, request):
        """This API is used to view the list of images.

        * You specify the image ID or set filters to query the details of certain images.
        * You can specify `Offset` and `Limit` to select a certain part of the results. By default, the information on the first 20 matching results is returned.

        :param request: Request instance for DescribeImages.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeImagesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeImagesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImages", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImagesResponse()
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


    def DescribeImportImageOs(self, request):
        """This API is used to query the list of supported operating systems of imported images.

        :param request: Request instance for DescribeImportImageOs.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeImportImageOsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeImportImageOsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImportImageOs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImportImageOsResponse()
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


    def DescribeInstanceFamilyConfigs(self, request):
        """This API is used to query a list of model families available to the current user in the current region.

        :param request: Request instance for DescribeInstanceFamilyConfigs.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeInstanceFamilyConfigsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeInstanceFamilyConfigsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceFamilyConfigs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceFamilyConfigsResponse()
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


    def DescribeInstanceTypeConfigs(self, request):
        """This API is used to query the model configuration of an instance.

        * You can filter the query results with `zone` or `instance-family`. For more information on filtering conditions, see [`Filter`](https://intl.cloud.tencent.com/document/api/213/15753?from_cn_redirect=1#Filter).
        * If no parameter is defined, the model configuration of all the instances in the specified region will be returned.

        :param request: Request instance for DescribeInstanceTypeConfigs.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeInstanceTypeConfigsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeInstanceTypeConfigsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceTypeConfigs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceTypeConfigsResponse()
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


    def DescribeInstanceVncUrl(self, request):
        """This API is used to query the Virtual Network Console (VNC) URL of an instance for its login to the VNC.

        * It does not support `STOPPED` CVMs.
        * A VNC URL is only valid for 15 seconds. If you do not access the URL within 15 seconds, it will become invalid and you have to query a URL again.
        * Once the VNC URL is accessed, it will become invalid and you have to query a URL again if needed.
        * If the connection is interrupted, you can make up to 30 reconnection attempts per minute.
        * After getting the value `InstanceVncUrl`, you need to append `InstanceVncUrl=xxxx` to the end of the link <https://img.qcloud.com/qcloud/app/active_vnc/index.html?>.

          - `InstanceVncUrl`: its value will be returned after the API is successfully called.

            The final URL is in the following format:

        ```
        https://img.qcloud.com/qcloud/app/active_vnc/index.html?InstanceVncUrl=wss%3A%2F%2Fbjvnc.qcloud.com%3A26789%2Fvnc%3Fs%3DaHpjWnRVMFNhYmxKdDM5MjRHNlVTSVQwajNUSW0wb2tBbmFtREFCTmFrcy8vUUNPMG0wSHZNOUUxRm5PMmUzWmFDcWlOdDJIbUJxSTZDL0RXcHZxYnZZMmRkWWZWcEZia2lyb09XMzdKNmM9
        ```

        :param request: Request instance for DescribeInstanceVncUrl.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeInstanceVncUrlRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeInstanceVncUrlResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceVncUrl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceVncUrlResponse()
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


    def DescribeInstances(self, request):
        """This API is used to query the details of instances.

        * You can filter the query results with the instance `ID`, name, or billing method. See `Filter` for more information.
        * If no parameter is defined, a certain number of instances under the current account will be returned. The number is specified by `Limit` and is 20 by default.

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstancesResponse()
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


    def DescribeInstancesOperationLimit(self, request):
        """This API is used to query limitations on operations on an instance.

        * Currently you can use this API to query the maximum number of times you can modify the configuration of an instance.

        :param request: Request instance for DescribeInstancesOperationLimit.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeInstancesOperationLimitRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeInstancesOperationLimitResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstancesOperationLimit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstancesOperationLimitResponse()
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


    def DescribeInstancesStatus(self, request):
        """This API is used to query the status of instances.

        * You can query the status of an instance with its `ID`.
        * If no parameter is defined, the status of a certain number of instances under the current account will be returned. The number is specified by `Limit` and is 20 by default.

        :param request: Request instance for DescribeInstancesStatus.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeInstancesStatusRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeInstancesStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstancesStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstancesStatusResponse()
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


    def DescribeInternetChargeTypeConfigs(self, request):
        """This API is used to query the network billing methods.

        :param request: Request instance for DescribeInternetChargeTypeConfigs.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeInternetChargeTypeConfigsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeInternetChargeTypeConfigsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInternetChargeTypeConfigs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInternetChargeTypeConfigsResponse()
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


    def DescribeKeyPairs(self, request):
        """This API is used to query key pairs.

        * A key pair is a pair of keys generated by an algorithm in which the public key is available to the public and the private key is available only to the user. You can use this API to query the public key but not the private key.

        :param request: Request instance for DescribeKeyPairs.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeKeyPairsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeKeyPairsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeKeyPairs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeKeyPairsResponse()
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


    def DescribeRegions(self, request):
        """This API is used to query regions.

        :param request: Request instance for DescribeRegions.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRegions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRegionsResponse()
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


    def DescribeReservedInstances(self, request):
        """This API is used to list reserved instances the user has purchased.

        :param request: Request instance for DescribeReservedInstances.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeReservedInstancesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeReservedInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeReservedInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReservedInstancesResponse()
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


    def DescribeReservedInstancesOfferings(self, request):
        """This API is used to describe Reserved Instance offerings that are available for purchase.

        :param request: Request instance for DescribeReservedInstancesOfferings.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeReservedInstancesOfferingsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeReservedInstancesOfferingsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeReservedInstancesOfferings", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReservedInstancesOfferingsResponse()
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


    def DescribeZoneInstanceConfigInfos(self, request):
        """This API is used to query the configurations of models in an availability zone.

        :param request: Request instance for DescribeZoneInstanceConfigInfos.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeZoneInstanceConfigInfosRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeZoneInstanceConfigInfosResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeZoneInstanceConfigInfos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZoneInstanceConfigInfosResponse()
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


    def DescribeZones(self, request):
        """This API is used to query availability zones.

        :param request: Request instance for DescribeZones.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeZonesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeZones", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZonesResponse()
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


    def DisassociateInstancesKeyPairs(self, request):
        """This API is used to unbind one or more key pairs from one or more instances.

        * It only supports [`STOPPED`](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#InstanceStatus) Linux instances.
        * After a key pair is disassociated from an instance, you can log in to the instance with password.
        * If you did not set a password for the instance, you will not be able to log in via SSH after the unbinding. In this case, you can call [ResetInstancesPassword](https://intl.cloud.tencent.com/document/api/213/15736?from_cn_redirect=1) to set a login password.
        * Batch operations are supported. The maximum number of instances in each request is 100. If instances not available for the operation are selected, you will get an error code.

        :param request: Request instance for DisassociateInstancesKeyPairs.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DisassociateInstancesKeyPairsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DisassociateInstancesKeyPairsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisassociateInstancesKeyPairs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateInstancesKeyPairsResponse()
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


    def DisassociateSecurityGroups(self, request):
        """This API is used to disassociate security groups from instances.

        :param request: Request instance for DisassociateSecurityGroups.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DisassociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DisassociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisassociateSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateSecurityGroupsResponse()
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


    def ImportImage(self, request):
        """This API is used to import images. Imported images can be used to create instances.

        :param request: Request instance for ImportImage.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ImportImageRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ImportImageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImportImage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImportImageResponse()
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


    def ImportKeyPair(self, request):
        """This API is used to import key pairs.

        * You can use this API to import key pairs to a user account, but the key pairs will not be automatically associated with any instance. You may use [AssociasteInstancesKeyPair](https://intl.cloud.tencent.com/document/api/213/9404?from_cn_redirect=1) to associate key pairs with instances.
        * You need to specify the names of the key pairs and the content of the public keys.
        * If you only have private keys, you can convert them to public keys with the `SSL` tool before importing them.

        :param request: Request instance for ImportKeyPair.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ImportKeyPairRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ImportKeyPairResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImportKeyPair", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImportKeyPairResponse()
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


    def InquiryPriceResetInstance(self, request):
        """This API is used to query the price for reinstalling an instance.

        * If you have specified the `ImageId` parameter, the price query is performed with the specified image. Otherwise, the image used by the current instance is used.
        * You can only query the price for reinstallation caused by switching between Linux and Windows OS. And the [system disk type](https://intl.cloud.tencent.com/document/api/213/15753?from_cn_redirect=1#SystemDisk) of the instance must be `CLOUD_BASIC`, `CLOUD_PREMIUM`, or `CLOUD_SSD`.
        * Currently, this API only supports instances in Mainland China regions.

        :param request: Request instance for InquiryPriceResetInstance.
        :type request: :class:`tencentcloud.cvm.v20170312.models.InquiryPriceResetInstanceRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.InquiryPriceResetInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceResetInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceResetInstanceResponse()
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


    def InquiryPriceResetInstancesInternetMaxBandwidth(self, request):
        """This API is used to query the price for upgrading the public bandwidth cap of an instance.

        * The allowed bandwidth cap varies for different models. For details, see [Purchasing Network Bandwidth](https://intl.cloud.tencent.com/document/product/213/509?from_cn_redirect=1).
        * For bandwidth billed by the `TRAFFIC_POSTPAID_BY_HOUR` method, changing the bandwidth cap through this API takes effect in real time. You can increase or reduce bandwidth within applicable limits.

        :param request: Request instance for InquiryPriceResetInstancesInternetMaxBandwidth.
        :type request: :class:`tencentcloud.cvm.v20170312.models.InquiryPriceResetInstancesInternetMaxBandwidthRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.InquiryPriceResetInstancesInternetMaxBandwidthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceResetInstancesInternetMaxBandwidth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceResetInstancesInternetMaxBandwidthResponse()
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


    def InquiryPriceResetInstancesType(self, request):
        """This API is used to query the price for adjusting the instance model.

        * Currently, you can only use this API to query the prices of instances whose [system disk type](https://intl.cloud.tencent.com/document/api/213/9452?from_cn_redirect=1#block_device) is `CLOUD_BASIC`, `CLOUD_PREMIUM`, or `CLOUD_SSD`.
        * Currently, you cannot use this API to query the prices of [CDH](https://intl.cloud.tencent.com/document/product/416?from_cn_redirect=1) instances.

        :param request: Request instance for InquiryPriceResetInstancesType.
        :type request: :class:`tencentcloud.cvm.v20170312.models.InquiryPriceResetInstancesTypeRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.InquiryPriceResetInstancesTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceResetInstancesType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceResetInstancesTypeResponse()
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


    def InquiryPriceResizeInstanceDisks(self, request):
        """This API is used to query the price for expanding data disks of an instance.

        * Currently, you can only use this API to query the price of non-elastic data disks whose [disk type](https://intl.cloud.tencent.com/document/api/213/9452?from_cn_redirect=1#block_device) is `CLOUD_BASIC`, `CLOUD_PREMIUM`, or `CLOUD_SSD`. You can use [`DescribeDisks`](https://intl.cloud.tencent.com/document/api/362/16315?from_cn_redirect=1) to check whether a disk is elastic. If the `Portable` field in the response is `false`, it means that the disk is non-elastic.
        * Currently, you cannot use this API to query the price for [CDH](https://intl.cloud.tencent.com/document/product/416?from_cn_redirect=1) instances. *Also, you can only query the price of expanding one data disk at a time.

        :param request: Request instance for InquiryPriceResizeInstanceDisks.
        :type request: :class:`tencentcloud.cvm.v20170312.models.InquiryPriceResizeInstanceDisksRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.InquiryPriceResizeInstanceDisksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceResizeInstanceDisks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceResizeInstanceDisksResponse()
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


    def InquiryPriceRunInstances(self, request):
        """This API is used to query the price of creating instances. You can only use this API for instances whose configuration is within the purchase limit. For more information, see [RunInstances](https://intl.cloud.tencent.com/document/api/213/15730?from_cn_redirect=1).

        :param request: Request instance for InquiryPriceRunInstances.
        :type request: :class:`tencentcloud.cvm.v20170312.models.InquiryPriceRunInstancesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.InquiryPriceRunInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceRunInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceRunInstancesResponse()
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


    def ModifyDisasterRecoverGroupAttribute(self, request):
        """This API is used to modify the attributes of [spread placement groups](https://intl.cloud.tencent.com/document/product/213/15486?from_cn_redirect=1).

        :param request: Request instance for ModifyDisasterRecoverGroupAttribute.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ModifyDisasterRecoverGroupAttributeRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ModifyDisasterRecoverGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDisasterRecoverGroupAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDisasterRecoverGroupAttributeResponse()
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


    def ModifyHostsAttribute(self, request):
        """This API is used to modify the attributes of a CDH instance, such as instance name and renewal flag. One of the two parameters, HostName and RenewFlag, must be set, but you cannot set both of them at the same time.

        :param request: Request instance for ModifyHostsAttribute.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ModifyHostsAttributeRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ModifyHostsAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyHostsAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyHostsAttributeResponse()
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


    def ModifyImageAttribute(self, request):
        """This API is used to modify image attributes.

        * Attributes of shared images cannot be modified.

        :param request: Request instance for ModifyImageAttribute.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ModifyImageAttributeRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ModifyImageAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyImageAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyImageAttributeResponse()
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


    def ModifyImageSharePermission(self, request):
        """This API is used to modify image sharing information.

        * The accounts with which an image is shared can use the shared image to create instances.
        * Each custom image can be shared with up to 50 accounts.
        * You can use a shared image to create instances, but you cannot change its name and description.
        * If an image is shared with another account, the shared image will be in the same region as the original image.

        :param request: Request instance for ModifyImageSharePermission.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ModifyImageSharePermissionRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ModifyImageSharePermissionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyImageSharePermission", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyImageSharePermissionResponse()
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


    def ModifyInstancesAttribute(self, request):
        """This API is used to modify the attributes of an instance. Currently you can only use the API to modify the name and the associated security groups of the instance.

        * Instance names are used only for users' convenience. Tencent Cloud does not use the name for ticket submission or instance management.
        * Batch operations are supported. The maximum number of instances in each request is 100.
        * When you change the security groups associated with an instance, the original security groups will be disassociated.

        :param request: Request instance for ModifyInstancesAttribute.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ModifyInstancesAttributeRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ModifyInstancesAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstancesAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstancesAttributeResponse()
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


    def ModifyInstancesProject(self, request):
        """This API is used to change the project to which an instance belongs.

        * Project is a virtual concept. You can create multiple projects under one account, manage different resources in each project, and assign different instances to different projects. You may use the [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) API to query instances and use the project ID to filter results.
        * You cannot modify the project of an instance that is bound to a load balancer. You need to firstly unbind the load balancer from the instance by using the [`DeregisterInstancesFromLoadBalancer`](https://intl.cloud.tencent.com/document/api/214/1258?from_cn_redirect=1) API.
        [^_^]: # (If you modify the project of an instance, security groups associated with the instance will be automatically disassociated. You can use the [`ModifyInstancesAttribute`](https://intl.cloud.tencent.com/document/api/213/15739?from_cn_redirect=1) API to associate the instance with the security groups again.
        * Batch operations are supported. You can operate up to 100 instances in each request.
        * You can call the [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5) API and find the result of the operation in the response parameter `LatestOperationState`. If the value is `SUCCESS`, the operation is successful.

        :param request: Request instance for ModifyInstancesProject.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ModifyInstancesProjectRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ModifyInstancesProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstancesProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstancesProjectResponse()
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


    def ModifyInstancesVpcAttribute(self, request):
        """This API is used to modify the VPC attributes of an instance, such as the VPC IP address.
        * By default, the instances will shut down when you perform this operation and restart upon completion.
        * If the specified VPC ID and subnet ID (the subnet must be in the same availability zone as the instance) are different from the VPC where the specified instance resides, the instance will be migrated to a subnet of the specified VPC. Before performing this operation, make sure that the specified instance is not bound with an [ENI](https://intl.cloud.tencent.com/document/product/576?from_cn_redirect=1) or [CLB](https://intl.cloud.tencent.com/document/product/214?from_cn_redirect=1).

        :param request: Request instance for ModifyInstancesVpcAttribute.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ModifyInstancesVpcAttributeRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ModifyInstancesVpcAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstancesVpcAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstancesVpcAttributeResponse()
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


    def ModifyKeyPairAttribute(self, request):
        """This API is used to modify the attributes of key pairs.

        * This API modifies the name and description of the key pair identified by the key pair ID.
        * The name of the key pair must be unique.
        * Key pair ID is the unique identifier of a key pair and cannot be modified.

        :param request: Request instance for ModifyKeyPairAttribute.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ModifyKeyPairAttributeRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ModifyKeyPairAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyKeyPairAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyKeyPairAttributeResponse()
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


    def PurchaseReservedInstancesOffering(self, request):
        """This API is used to purchase one or more specific Reserved Instances.

        :param request: Request instance for PurchaseReservedInstancesOffering.
        :type request: :class:`tencentcloud.cvm.v20170312.models.PurchaseReservedInstancesOfferingRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.PurchaseReservedInstancesOfferingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PurchaseReservedInstancesOffering", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PurchaseReservedInstancesOfferingResponse()
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


    def RebootInstances(self, request):
        """This API is used to restart instances.

        * You can only perform this operation on instances whose status is `RUNNING`.
        * If the API is called successfully, the instance status will become `REBOOTING`. After the instance is restarted, its status will become `RUNNING` again.
        * Forced restart is supported. A forced restart is similar to switching off the power of a physical computer and starting it again. It may cause data loss or file system corruption. Be sure to only force start a CVM when it cannot be restarted normally.
        * Batch operations are supported. The maximum number of instances in each request is 100.

        :param request: Request instance for RebootInstances.
        :type request: :class:`tencentcloud.cvm.v20170312.models.RebootInstancesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.RebootInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RebootInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RebootInstancesResponse()
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


    def ResetInstance(self, request):
        """This API is used to reinstall the operating system of the specified instance.

        * If you specify an `ImageId`, the specified image is used. Otherwise, the image used by the current instance is used.
        * The system disk will be formatted and reset. Therefore, make sure that no important files are stored on the system disk.
        * If the operating system switches between `Linux` and `Windows`, the system disk `ID` of the instance will change, and the snapshots that are associated with the system disk can no longer be used to roll back and restore data.
        * If no password is specified, you will get a random password via internal message.
        * You can only use this API to switch the operating system between `Linux` and `Windows` for instances whose [system disk type](https://intl.cloud.tencent.com/document/api/213/9452?from_cn_redirect=1#SystemDisk) is `CLOUD_BASIC`, `CLOUD_PREMIUM`, or `CLOUD_SSD`.
        * Currently, this API only supports instances in Mainland China regions.

        :param request: Request instance for ResetInstance.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ResetInstanceRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ResetInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetInstanceResponse()
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


    def ResetInstancesInternetMaxBandwidth(self, request):
        """This API is used to change the public bandwidth cap of an instance.

        * The allowed bandwidth cap varies for different models. For details, see [Purchasing Network Bandwidth](https://intl.cloud.tencent.com/document/product/213/509?from_cn_redirect=1).
        * For bandwidth billed by the `TRAFFIC_POSTPAID_BY_HOUR` method, changing the bandwidth cap through this API takes effect in real time. Users can increase or reduce bandwidth within applicable limits.

        :param request: Request instance for ResetInstancesInternetMaxBandwidth.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ResetInstancesInternetMaxBandwidthRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ResetInstancesInternetMaxBandwidthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetInstancesInternetMaxBandwidth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetInstancesInternetMaxBandwidthResponse()
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


    def ResetInstancesPassword(self, request):
        """This API is used to reset the password of the operating system instances to a user-specified password.

        * To modify the password of the administrator account: the name of the administrator account varies with the operating system. In Windows, it is `Administrator`; in Ubuntu, it is `ubuntu`; in Linux, it is `root`.
        * To reset the password of a running instance, you need to set the parameter `ForceStop` to `True` for a forced shutdown. If not, only passwords of stopped instances can be reset.
        * Batch operations are supported. You can reset the passwords of up to 100 instances to the same value once.
        * You can call the [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5) API and find the result of the operation in the response parameter `LatestOperationState`. If the value is `SUCCESS`, the operation is successful.

        :param request: Request instance for ResetInstancesPassword.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ResetInstancesPasswordRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ResetInstancesPasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetInstancesPassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetInstancesPasswordResponse()
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


    def ResetInstancesType(self, request):
        """This API is used to change the model of an instance.
        * You can only use this API to change the models of instances whose [system disk type](https://intl.cloud.tencent.com/document/api/213/9452?from_cn_redirect=1#block_device) is `CLOUD_BASIC`, `CLOUD_PREMIUM`, or `CLOUD_SSD`.
        * Currently, you cannot use this API to change the models of [CDH](https://intl.cloud.tencent.com/document/product/416?from_cn_redirect=1) instances.

        :param request: Request instance for ResetInstancesType.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ResetInstancesTypeRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ResetInstancesTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetInstancesType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetInstancesTypeResponse()
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


    def ResizeInstanceDisks(self, request):
        """This API (ResizeInstanceDisks) is used to expand the data disks of an instance.

        * Currently, you can only use the API to expand non-elastic data disks whose [disk type](https://intl.cloud.tencent.com/document/api/213/9452?from_cn_redirect=1#block_device) is `CLOUD_BASIC`, `CLOUD_PREMIUM`, or `CLOUD_SSD`. You can use [`DescribeDisks`](https://intl.cloud.tencent.com/document/api/362/16315?from_cn_redirect=1) to check whether a disk is elastic. If the `Portable` field in the response is `false`, it means that the disk is non-elastic.
        * Currently, this API does not support [CDH](https://intl.cloud.tencent.com/document/product/416?from_cn_redirect=1) instances.
        * Currently, only one data disk can be expanded at a time.

        :param request: Request instance for ResizeInstanceDisks.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ResizeInstanceDisksRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ResizeInstanceDisksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResizeInstanceDisks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResizeInstanceDisksResponse()
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


    def RunInstances(self, request):
        """This API is used to create one or more instances with a specified configuration.

        * After an instance is created successfully, it will start up automatically, and the [instance state](https://intl.cloud.tencent.com/document/api/213/9452?from_cn_redirect=1#instance_state) will become "Running".
        * If you create a pay-as-you-go instance billed on an hourly basis, an amount equivalent to the hourly rate will be frozen before the creation. Make sure your account balance is sufficient before calling this API.
        * The number of instances you can purchase through this API is subject to the [CVM instance purchase limit](https://intl.cloud.tencent.com/document/product/213/2664?from_cn_redirect=1). Both the instances created through this API and the console will be counted toward the quota.
        * This API is an async API. An instance `ID` list will be returned after you successfully make a creation request. However, it does not mean the creation has been completed. The state of the instance will be `Creating` during the creation. You can use [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) to query the status of the instance. If the status changes from `Creating` to `Running`, it means that the instance has been created successfully.

        :param request: Request instance for RunInstances.
        :type request: :class:`tencentcloud.cvm.v20170312.models.RunInstancesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.RunInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RunInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RunInstancesResponse()
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


    def StartInstances(self, request):
        """This API is used to start instances.

        * You can only perform this operation on instances whose status is `STOPPED`.
        * The instance status will become `STARTING` when the API is called successfully and `RUNNING` when the instance is successfully started.
        * Batch operations are supported. The maximum number of instances in each request is 100.

        :param request: Request instance for StartInstances.
        :type request: :class:`tencentcloud.cvm.v20170312.models.StartInstancesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.StartInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartInstancesResponse()
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


    def StopInstances(self, request):
        """This API is used to shut down instances.

        * You can only perform this operation on instances whose status is `RUNNING`.
        * The instance status will become `STOPPING` when the API is called successfully and `STOPPED` when the instance is successfully shut down.
        * Forced shutdown is supported. A forced shutdown is similar to switching off the power of a physical computer. It may cause data loss or file system corruption. Be sure to only force shut down a CVM when it cannot be sht down normally.
        * Batch operations are supported. The maximum number of instances in each request is 100.

        :param request: Request instance for StopInstances.
        :type request: :class:`tencentcloud.cvm.v20170312.models.StopInstancesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.StopInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopInstancesResponse()
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


    def SyncImages(self, request):
        """This API is used to sync a custom image to other regions.

        * Each API call syncs a single image.
        * This API supports syncing an image to multiple regions.
        * Each account can have up to 10 custom images in each region.

        :param request: Request instance for SyncImages.
        :type request: :class:`tencentcloud.cvm.v20170312.models.SyncImagesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.SyncImagesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SyncImages", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SyncImagesResponse()
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


    def TerminateInstances(self, request):
        """This API is used to return instances.

        * Use this API to return instances that are no longer required.
        * Pay-as-you-go instances can be returned directly through this API.
        * When this API is called for the first time, the instance will be moved to the recycle bin. When this API is called for the second time, the instance will be terminated and cannot be recovered.
        * Batch operations are supported. The allowed maximum number of instances in each request is 100.

        :param request: Request instance for TerminateInstances.
        :type request: :class:`tencentcloud.cvm.v20170312.models.TerminateInstancesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.TerminateInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TerminateInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateInstancesResponse()
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