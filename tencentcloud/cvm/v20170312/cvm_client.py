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
from tencentcloud.cvm.v20170312 import models


class CvmClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'cvm.tencentcloudapi.com'
    _service = 'cvm'


    def AllocateHosts(self, request):
        """This API is used to create CDH instances with specified configuration.
        * When HostChargeType is PREPAID, the HostChargePrepaid parameter must be specified.

        :param request: Request instance for AllocateHosts.
        :type request: :class:`tencentcloud.cvm.v20170312.models.AllocateHostsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.AllocateHostsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AllocateHosts", params, headers=headers)
            response = json.loads(body)
            model = models.AllocateHostsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("AssociateInstancesKeyPairs", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateInstancesKeyPairsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateSecurityGroups(self, request):
        """This API is used to associate security groups with specified instances.

        :param request: Request instance for AssociateSecurityGroups.
        :type request: :class:`tencentcloud.cvm.v20170312.models.AssociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.AssociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ConfigureChcAssistVpc(self, request):
        """This API is used to configure the out-of-band network and deployment network of a CHC host.

        :param request: Request instance for ConfigureChcAssistVpc.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ConfigureChcAssistVpcRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ConfigureChcAssistVpcResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ConfigureChcAssistVpc", params, headers=headers)
            response = json.loads(body)
            model = models.ConfigureChcAssistVpcResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ConfigureChcDeployVpc(self, request):
        """This API is used to configure the deployment network of a CHC host.

        :param request: Request instance for ConfigureChcDeployVpc.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ConfigureChcDeployVpcRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ConfigureChcDeployVpcResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ConfigureChcDeployVpc", params, headers=headers)
            response = json.loads(body)
            model = models.ConfigureChcDeployVpcResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDisasterRecoverGroup(self, request):
        """This API is used to create a [spread placement group](https://intl.cloud.tencent.com/document/product/213/15486?from_cn_redirect=1). After you create one, you can specify it for an instance when you [create the instance](https://intl.cloud.tencent.com/document/api/213/15730?from_cn_redirect=1),

        :param request: Request instance for CreateDisasterRecoverGroup.
        :type request: :class:`tencentcloud.cvm.v20170312.models.CreateDisasterRecoverGroupRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.CreateDisasterRecoverGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDisasterRecoverGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDisasterRecoverGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImage(self, request):
        """This API is used to create a new image with the system disk of an instance. The image can be used to create new instances.

        :param request: Request instance for CreateImage.
        :type request: :class:`tencentcloud.cvm.v20170312.models.CreateImageRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.CreateImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImage", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("CreateKeyPair", params, headers=headers)
            response = json.loads(body)
            model = models.CreateKeyPairResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLaunchTemplateVersion(self, request):
        """This API is used to create an instance launch template based on the specified template ID and the corresponding template version number. The default version number will be used when no template version numbers are specified. Each instance launch template can have up to 30 version numbers.

        :param request: Request instance for CreateLaunchTemplateVersion.
        :type request: :class:`tencentcloud.cvm.v20170312.models.CreateLaunchTemplateVersionRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.CreateLaunchTemplateVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLaunchTemplateVersion", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLaunchTemplateVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDisasterRecoverGroups(self, request):
        """This API is used to delete a [spread placement group](https://intl.cloud.tencent.com/document/product/213/15486?from_cn_redirect=1). Only empty placement groups can be deleted. To delete a non-empty group, you need to terminate all the CVM instances in it first. Otherwise, the deletion will fail.

        :param request: Request instance for DeleteDisasterRecoverGroups.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DeleteDisasterRecoverGroupsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DeleteDisasterRecoverGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDisasterRecoverGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDisasterRecoverGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImages(self, request):
        """This API is used to delete one or more images.

        * If the [ImageState](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#Image) of an image is `CREATING` or `USING`, the image cannot be deleted. Call the [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1) API to query the image status.
        * Up to 10 custom images are allowed in each region. If you have run out of the quota, delete unused images to create new ones.
        * A shared image cannot be deleted.

        :param request: Request instance for DeleteImages.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DeleteImagesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DeleteImagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImages", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("DeleteKeyPairs", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteKeyPairsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLaunchTemplate(self, request):
        """This API is used to delete an instance launch template.

        :param request: Request instance for DeleteLaunchTemplate.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DeleteLaunchTemplateRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DeleteLaunchTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLaunchTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLaunchTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLaunchTemplateVersions(self, request):
        """This API is used to delete one or more instance launch template versions.

        :param request: Request instance for DeleteLaunchTemplateVersions.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DeleteLaunchTemplateVersionsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DeleteLaunchTemplateVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLaunchTemplateVersions", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLaunchTemplateVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeChcDeniedActions(self, request):
        """This API is used to query the actions not allowed for the specified CHC instances.

        :param request: Request instance for DescribeChcDeniedActions.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeChcDeniedActionsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeChcDeniedActionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeChcDeniedActions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeChcDeniedActionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeChcHosts(self, request):
        """This API is used to query the details of one or more CHC host.

        * You can filter the query results with the instance ID, name or device type. See `Filter` for more information.
        * If no parameter is defined, a certain number of instances under the current account will be returned. The number is specified by `Limit` and is `20` by default.

        :param request: Request instance for DescribeChcHosts.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeChcHostsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeChcHostsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeChcHosts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeChcHostsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDisasterRecoverGroupQuota(self, request):
        """This API is used to query the quota of [spread placement groups](https://intl.cloud.tencent.com/document/product/213/15486?from_cn_redirect=1).

        :param request: Request instance for DescribeDisasterRecoverGroupQuota.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeDisasterRecoverGroupQuotaRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeDisasterRecoverGroupQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDisasterRecoverGroupQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDisasterRecoverGroupQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDisasterRecoverGroups(self, request):
        """This API is used to query the information on [spread placement groups](https://intl.cloud.tencent.com/document/product/213/15486?from_cn_redirect=1).

        :param request: Request instance for DescribeDisasterRecoverGroups.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeDisasterRecoverGroupsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeDisasterRecoverGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDisasterRecoverGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDisasterRecoverGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHosts(self, request):
        """This API is used to query the details of CDH instances.

        :param request: Request instance for DescribeHosts.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeHostsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeHostsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHosts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageQuota(self, request):
        """This API is used to query the image quota of an user account.

        :param request: Request instance for DescribeImageQuota.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeImageQuotaRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeImageQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageSharePermission(self, request):
        """This API is used to query image sharing information.

        :param request: Request instance for DescribeImageSharePermission.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeImageSharePermissionRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeImageSharePermissionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageSharePermission", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageSharePermissionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("DescribeImages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImportImageOs(self, request):
        """This API is used to query the list of supported operating systems of imported images.

        :param request: Request instance for DescribeImportImageOs.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeImportImageOsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeImportImageOsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImportImageOs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImportImageOsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceFamilyConfigs(self, request):
        """This API is used to query a list of model families available to the current user in the current region.

        :param request: Request instance for DescribeInstanceFamilyConfigs.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeInstanceFamilyConfigsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeInstanceFamilyConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceFamilyConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceFamilyConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("DescribeInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstancesOperationLimit(self, request):
        """This API is used to query limitations on operations on an instance.

        * Currently you can use this API to query the maximum number of times you can modify the configuration of an instance.

        :param request: Request instance for DescribeInstancesOperationLimit.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeInstancesOperationLimitRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeInstancesOperationLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancesOperationLimit", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesOperationLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("DescribeInstancesStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInternetChargeTypeConfigs(self, request):
        """This API is used to query the network billing methods.

        :param request: Request instance for DescribeInternetChargeTypeConfigs.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeInternetChargeTypeConfigsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeInternetChargeTypeConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInternetChargeTypeConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInternetChargeTypeConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKeyPairs(self, request):
        """This API is used to query key pairs.

        * A key pair is a pair of keys generated by an algorithm in which the public key is available to the public and the private key is available only to the user. You can use this API to query the public key but not the private key.

        :param request: Request instance for DescribeKeyPairs.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeKeyPairsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeKeyPairsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKeyPairs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKeyPairsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLaunchTemplateVersions(self, request):
        """This API is used to query the information of instance launch template versions.

        :param request: Request instance for DescribeLaunchTemplateVersions.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeLaunchTemplateVersionsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeLaunchTemplateVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLaunchTemplateVersions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLaunchTemplateVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLaunchTemplates(self, request):
        """This API is used to query one or more instance launch templates.

        :param request: Request instance for DescribeLaunchTemplates.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeLaunchTemplatesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeLaunchTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLaunchTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLaunchTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegions(self, request):
        """This API is suspended. To query the information of regions, use [DescribeZones](https://intl.cloud.tencent.com/document/product/1596/77930?from_cn_redirect=1).

        :param request: Request instance for DescribeRegions.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReservedInstancesConfigInfos(self, request):
        """This API is used to describe reserved instance (RI) offerings. Currently, RIs are only offered to beta users.

        :param request: Request instance for DescribeReservedInstancesConfigInfos.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeReservedInstancesConfigInfosRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeReservedInstancesConfigInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReservedInstancesConfigInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReservedInstancesConfigInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReservedInstancesOfferings(self, request):
        """This API is used to describe Reserved Instance offerings that are available for purchase.

        :param request: Request instance for DescribeReservedInstancesOfferings.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeReservedInstancesOfferingsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeReservedInstancesOfferingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReservedInstancesOfferings", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReservedInstancesOfferingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZoneInstanceConfigInfos(self, request):
        """This API is used to query the configurations of models in an availability zone.

        :param request: Request instance for DescribeZoneInstanceConfigInfos.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeZoneInstanceConfigInfosRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeZoneInstanceConfigInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZoneInstanceConfigInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZoneInstanceConfigInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZones(self, request):
        """This API is used to query availability zones.

        :param request: Request instance for DescribeZones.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeZonesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZones", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZonesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("DisassociateInstancesKeyPairs", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateInstancesKeyPairsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateSecurityGroups(self, request):
        """This API is used to disassociate security groups from instances.

        :param request: Request instance for DisassociateSecurityGroups.
        :type request: :class:`tencentcloud.cvm.v20170312.models.DisassociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DisassociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportImages(self, request):
        """This API is used to export custom images to the specified COS bucket.

        :param request: Request instance for ExportImages.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ExportImagesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ExportImagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportImages", params, headers=headers)
            response = json.loads(body)
            model = models.ExportImagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportImage(self, request):
        """The API is used to import an image. The image imported can be used to create instances. Currently, this API can import images in formats like RAW, VHD, QCOW2, and VMDK.

        :param request: Request instance for ImportImage.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ImportImageRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ImportImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportImage", params, headers=headers)
            response = json.loads(body)
            model = models.ImportImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportKeyPair(self, request):
        """This API is used to import key pairs.

        * You can use this API to import key pairs to a user account, but the key pairs will not be automatically associated with any instance. You may use [AssociasteInstancesKeyPair](https://intl.cloud.tencent.com/document/api/213/15698?from_cn_redirect=1) to associate key pairs with instances.
        * You need to specify the names of the key pairs and the content of the public keys.
        * If you only have private keys, you can convert them to public keys with the `SSL` tool before importing them.

        :param request: Request instance for ImportKeyPair.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ImportKeyPairRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ImportKeyPairResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportKeyPair", params, headers=headers)
            response = json.loads(body)
            model = models.ImportKeyPairResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePricePurchaseReservedInstancesOffering(self, request):
        """This API is used to query the price of reserved instances. It only supports querying purchasable reserved instance offerings. Currently, RIs are only offered to beta users.

        :param request: Request instance for InquirePricePurchaseReservedInstancesOffering.
        :type request: :class:`tencentcloud.cvm.v20170312.models.InquirePricePurchaseReservedInstancesOfferingRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.InquirePricePurchaseReservedInstancesOfferingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePricePurchaseReservedInstancesOffering", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePricePurchaseReservedInstancesOfferingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("InquiryPriceResetInstance", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceResetInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("InquiryPriceResetInstancesInternetMaxBandwidth", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceResetInstancesInternetMaxBandwidthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("InquiryPriceResetInstancesType", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceResetInstancesTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("InquiryPriceResizeInstanceDisks", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceResizeInstanceDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceRunInstances(self, request):
        """This API is used to query the price of creating instances. You can only use this API for instances whose configuration is within the purchase limit. For more information, see [RunInstances](https://intl.cloud.tencent.com/document/api/213/15730?from_cn_redirect=1).

        :param request: Request instance for InquiryPriceRunInstances.
        :type request: :class:`tencentcloud.cvm.v20170312.models.InquiryPriceRunInstancesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.InquiryPriceRunInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceRunInstances", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceRunInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyChcAttribute(self, request):
        """This API is used to modify the CHC host attributes.

        :param request: Request instance for ModifyChcAttribute.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ModifyChcAttributeRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ModifyChcAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyChcAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyChcAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDisasterRecoverGroupAttribute(self, request):
        """This API is used to modify the attributes of [spread placement groups](https://intl.cloud.tencent.com/document/product/213/15486?from_cn_redirect=1).

        :param request: Request instance for ModifyDisasterRecoverGroupAttribute.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ModifyDisasterRecoverGroupAttributeRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ModifyDisasterRecoverGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDisasterRecoverGroupAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDisasterRecoverGroupAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHostsAttribute(self, request):
        """This API is used to modify the attributes of a CDH instance, such as instance name and renewal flag. One of the two parameters, HostName and RenewFlag, must be set, but you cannot set both of them at the same time.

        :param request: Request instance for ModifyHostsAttribute.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ModifyHostsAttributeRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ModifyHostsAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHostsAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHostsAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyImageAttribute(self, request):
        """This API is used to modify image attributes.

        * Attributes of shared images cannot be modified.

        :param request: Request instance for ModifyImageAttribute.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ModifyImageAttributeRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ModifyImageAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyImageAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyImageAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("ModifyImageSharePermission", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyImageSharePermissionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstancesAttribute(self, request):
        """The API is used to modify the attributes of an instance. Only the name and the associated security groups can be modified for now.

        * An attribute must be specified in the request.
        * "Instance name" is a custom name for easier management. Tencent Cloud does not use the name for online support or instance management.
        * Batch operations are supported. Each request can modify up to 100 instances.
        * When you modify the security groups associated with an instance is modified, the original security groups are disassociated.
        * You can use the API [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5) to query the instance operation result. If the 'LatestOperationState' in the response is **SUCCESS**, the operation is successful.

        :param request: Request instance for ModifyInstancesAttribute.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ModifyInstancesAttributeRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ModifyInstancesAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstancesAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstancesAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstancesProject(self, request):
        """This API is used to change the project to which an instance is assigned.

        * Project is a virtual concept. You can create multiple projects under one account, manage different resources in each project, and assign different instances to different projects. You may use the [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) API to query instances and use the project ID to filter the results.
        * You cannot modify the project of an instance that is bound to a load balancer. You need to unbind the load balancer from the instance by using the [DeregisterInstancesFromLoadBalancer](https://intl.cloud.tencent.com/document/api/214/1258?from_cn_redirect=1) API before using this API.
        * Batch operations are supported. Up to 100 instances per request is allowed.
        * You can use the API [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5) to query the operation result. If the `LatestOperationState` in the response is `SUCCESS`, the operation is successful.

        :param request: Request instance for ModifyInstancesProject.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ModifyInstancesProjectRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ModifyInstancesProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstancesProject", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstancesProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstancesVpcAttribute(self, request):
        """This API is used to modify the VPC attributes of an instance, such as the VPC IP address.
        * This action will shut down the instance, and restart it after the modification is completed.
        * To migrate an instance to another VPC/subnet, specify the new VPC and subnet directly. Make sure that the instance to migrate is not bound to an [ENI](https://intl.cloud.tencent.com/document/product/576?from_cn_redirect=1) or [CLB](https://intl.cloud.tencent.com/document/product/214?from_cn_redirect=1) instances.
        * You can use the API [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5) to query the operation result. If the `LatestOperationState` in the response is `SUCCESS`, the operation is successful.

        :param request: Request instance for ModifyInstancesVpcAttribute.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ModifyInstancesVpcAttributeRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ModifyInstancesVpcAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstancesVpcAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstancesVpcAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("ModifyKeyPairAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyKeyPairAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLaunchTemplateDefaultVersion(self, request):
        """This API is used to modify the default version of the instance launch template.

        :param request: Request instance for ModifyLaunchTemplateDefaultVersion.
        :type request: :class:`tencentcloud.cvm.v20170312.models.ModifyLaunchTemplateDefaultVersionRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ModifyLaunchTemplateDefaultVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLaunchTemplateDefaultVersion", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLaunchTemplateDefaultVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PurchaseReservedInstancesOffering(self, request):
        """This API is used to purchase one or more specific Reserved Instances.

        :param request: Request instance for PurchaseReservedInstancesOffering.
        :type request: :class:`tencentcloud.cvm.v20170312.models.PurchaseReservedInstancesOfferingRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.PurchaseReservedInstancesOfferingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PurchaseReservedInstancesOffering", params, headers=headers)
            response = json.loads(body)
            model = models.PurchaseReservedInstancesOfferingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("RebootInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RebootInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveChcAssistVpc(self, request):
        """This API is used to remove the out-of-band network and deployment network of a CHC host.

        :param request: Request instance for RemoveChcAssistVpc.
        :type request: :class:`tencentcloud.cvm.v20170312.models.RemoveChcAssistVpcRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.RemoveChcAssistVpcResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveChcAssistVpc", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveChcAssistVpcResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveChcDeployVpc(self, request):
        """This API is used to remove the deployment network of a CHC host.

        :param request: Request instance for RemoveChcDeployVpc.
        :type request: :class:`tencentcloud.cvm.v20170312.models.RemoveChcDeployVpcRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.RemoveChcDeployVpcResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveChcDeployVpc", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveChcDeployVpcResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("ResetInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ResetInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("ResetInstancesInternetMaxBandwidth", params, headers=headers)
            response = json.loads(body)
            model = models.ResetInstancesInternetMaxBandwidthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("ResetInstancesPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetInstancesPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("ResetInstancesType", params, headers=headers)
            response = json.loads(body)
            model = models.ResetInstancesTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("ResizeInstanceDisks", params, headers=headers)
            response = json.loads(body)
            model = models.ResizeInstanceDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunInstances(self, request):
        """This API is used to create one or more instances with a specified configuration.

        * After an instance is created successfully, it will start up automatically, and the [instance status](https://intl.cloud.tencent.com/document/api/213/9452?from_cn_redirect=1#instance_state) will become "Running".
        * If you create a pay-as-you-go instance billed on an hourly basis, an amount equivalent to the hourly rate will be frozen. Make sure your account balance is sufficient before calling this API.
        * The number of instances you can purchase through this API is subject to the [Quota for CVM Instances](https://intl.cloud.tencent.com/document/product/213/2664?from_cn_redirect=1). Instances created through this API and in the CVM console are counted toward the quota.
        * This API is an async API. An instance ID list is returned after the creation request is sent. However, it does not mean the creation has been completed. The status of the instance will be `Creating` during the creation. You can use [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) to query the status of the instance. If the status changes from `Creating` to `Running`, it means that the instance has been created successfully.

        :param request: Request instance for RunInstances.
        :type request: :class:`tencentcloud.cvm.v20170312.models.RunInstancesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.RunInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RunInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("StartInstances", params, headers=headers)
            response = json.loads(body)
            model = models.StartInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("StopInstances", params, headers=headers)
            response = json.loads(body)
            model = models.StopInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("SyncImages", params, headers=headers)
            response = json.loads(body)
            model = models.SyncImagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            headers = request.headers
            body = self.call("TerminateInstances", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))