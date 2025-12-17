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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.cvm.v20170312 import models
from typing import Dict


class CvmClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'cvm.intl.tencentcloudapi.com'
    _service = 'cvm'

    async def AllocateHosts(
            self,
            request: models.AllocateHostsRequest,
            opts: Dict = None,
    ) -> models.AllocateHostsResponse:
        """
        This API is used to create CDH instances with specified configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "AllocateHosts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AllocateHostsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateInstancesKeyPairs(
            self,
            request: models.AssociateInstancesKeyPairsRequest,
            opts: Dict = None,
    ) -> models.AssociateInstancesKeyPairsResponse:
        """
        This API is used to associate key pairs with instances.

        * If the public key of a key pair is written to the `SSH` configuration of the instance, users will be able to log in to the instance with the private key of the key pair.
        * If the instance is already associated with a key, the old key will become invalid.
        If you currently use a password to log in, you will no longer be able to do so after you associate the instance with a key.
        * Batch operations are supported. The maximum number of instances in each request is 100. If any instance in the request cannot be associated with a key, you will get an error code.
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateInstancesKeyPairs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateInstancesKeyPairsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateSecurityGroups(
            self,
            request: models.AssociateSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.AssociateSecurityGroupsResponse:
        """
        This API is used to associate security groups with specified instances.
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ConfigureChcAssistVpc(
            self,
            request: models.ConfigureChcAssistVpcRequest,
            opts: Dict = None,
    ) -> models.ConfigureChcAssistVpcResponse:
        """
        This API is used to configure the out-of-band network and deployment network of a CHC host.
        """
        
        kwargs = {}
        kwargs["action"] = "ConfigureChcAssistVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ConfigureChcAssistVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ConfigureChcDeployVpc(
            self,
            request: models.ConfigureChcDeployVpcRequest,
            opts: Dict = None,
    ) -> models.ConfigureChcDeployVpcResponse:
        """
        This API is used to configure the deployment network of a CHC host.
        """
        
        kwargs = {}
        kwargs["action"] = "ConfigureChcDeployVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ConfigureChcDeployVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ConvertOperatingSystems(
            self,
            request: models.ConvertOperatingSystemsRequest,
            opts: Dict = None,
    ) -> models.ConvertOperatingSystemsResponse:
        """
        This API is used to switch the operating system of an instance with CentOS 7 or CentOS 8 as the source operating system.
        """
        
        kwargs = {}
        kwargs["action"] = "ConvertOperatingSystems"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ConvertOperatingSystemsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDisasterRecoverGroup(
            self,
            request: models.CreateDisasterRecoverGroupRequest,
            opts: Dict = None,
    ) -> models.CreateDisasterRecoverGroupResponse:
        """
        This API is used to create a [spread placement group](https://intl.cloud.tencent.com/document/product/213/15486?from_cn_redirect=1). After you create one, you can specify it for an instance when you [create the instance](https://intl.cloud.tencent.com/document/api/213/15730?from_cn_redirect=1),
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDisasterRecoverGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDisasterRecoverGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImage(
            self,
            request: models.CreateImageRequest,
            opts: Dict = None,
    ) -> models.CreateImageResponse:
        """
        This API is used to create a new image with the system disk of an instance. The image can be used to create new instances.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateKeyPair(
            self,
            request: models.CreateKeyPairRequest,
            opts: Dict = None,
    ) -> models.CreateKeyPairResponse:
        """
        This API is used to create an `OpenSSH RSA` key pair, which you can use to log in to a `Linux` instance.

        * You only need to specify a name, and the system will automatically create a key pair and return its `ID` and the public and private keys.
        * The name of the key pair must be unique.
        * You can save the private key to a file and use it as an authentication method for `SSH`.
        * Tencent Cloud does not save users' private keys. Be sure to save it yourself.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateKeyPair"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateKeyPairResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLaunchTemplate(
            self,
            request: models.CreateLaunchTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateLaunchTemplateResponse:
        """
        This interface (CreateLaunchTemplate) is used for instance launch template creation.

        An instance launch template is a configuration data and can be used to create instances. Its content includes configurations required to create instances, such as instance type, types and sizes of data disk and system disk, and security group and other information.

        This API is used to create an instance launch template. After the initial creation of the instance template, its template version is the default version 1. A new version can be created using CreateLaunchTemplateVersion (https://intl.cloud.tencent.com/document/product/213/66326?from_cn_redirect=1), and the version number will increment. By default, when specifying an instance launch template in RunInstances (https://intl.cloud.tencent.com/document/product/213/15730?from_cn_redirect=1), if the template version number is not specified, the default version will be used.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLaunchTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLaunchTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLaunchTemplateVersion(
            self,
            request: models.CreateLaunchTemplateVersionRequest,
            opts: Dict = None,
    ) -> models.CreateLaunchTemplateVersionResponse:
        """
        This API is used to create an instance launch template based on the specified template ID and the corresponding template version number. The default version number will be used when no template version numbers are specified. Each instance launch template can have up to 30 version numbers.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLaunchTemplateVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLaunchTemplateVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDisasterRecoverGroups(
            self,
            request: models.DeleteDisasterRecoverGroupsRequest,
            opts: Dict = None,
    ) -> models.DeleteDisasterRecoverGroupsResponse:
        """
        This API is used to delete a [spread placement group](https://intl.cloud.tencent.com/document/product/213/15486?from_cn_redirect=1). Only empty placement groups can be deleted. To delete a non-empty group, you need to terminate all the CVM instances in it first. Otherwise, the deletion will fail.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDisasterRecoverGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDisasterRecoverGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteImages(
            self,
            request: models.DeleteImagesRequest,
            opts: Dict = None,
    ) -> models.DeleteImagesResponse:
        """
        This API is used to delete one or more images.

        * If the [ImageState](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#Image) of an image is `CREATING` or `USING`, the image cannot be deleted. Call the [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1) API to query the image status.
        * Up to 10 custom images are allowed in each region. If you have run out of the quota, delete unused images to create new ones.
        * A shared image cannot be deleted.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteImages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteImagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteKeyPairs(
            self,
            request: models.DeleteKeyPairsRequest,
            opts: Dict = None,
    ) -> models.DeleteKeyPairsResponse:
        """
        This API is used to delete the key pairs hosted in Tencent Cloud.

        * You can delete multiple key pairs at the same time.
        * A key pair used by an instance or image cannot be deleted. Therefore, you need to verify whether all the key pairs have been deleted successfully.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteKeyPairs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteKeyPairsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLaunchTemplate(
            self,
            request: models.DeleteLaunchTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteLaunchTemplateResponse:
        """
        This API is used to delete an instance launch template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLaunchTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLaunchTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLaunchTemplateVersions(
            self,
            request: models.DeleteLaunchTemplateVersionsRequest,
            opts: Dict = None,
    ) -> models.DeleteLaunchTemplateVersionsResponse:
        """
        This API is used to delete one or more instance launch template versions.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLaunchTemplateVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLaunchTemplateVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeChcDeniedActions(
            self,
            request: models.DescribeChcDeniedActionsRequest,
            opts: Dict = None,
    ) -> models.DescribeChcDeniedActionsResponse:
        """
        This API is used to query the actions not allowed for the specified CHC instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeChcDeniedActions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeChcDeniedActionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeChcHosts(
            self,
            request: models.DescribeChcHostsRequest,
            opts: Dict = None,
    ) -> models.DescribeChcHostsResponse:
        """
        This API is used to query the details of one or more CHC host.

        * You can filter the query results with the instance ID, name or device type. See `Filter` for more information.
        * If no parameter is defined, a certain number of instances under the current account will be returned. The number is specified by `Limit` and is `20` by default.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeChcHosts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeChcHostsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDisasterRecoverGroupQuota(
            self,
            request: models.DescribeDisasterRecoverGroupQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeDisasterRecoverGroupQuotaResponse:
        """
        This API is used to query the quota of [spread placement groups](https://intl.cloud.tencent.com/document/product/213/15486?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDisasterRecoverGroupQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDisasterRecoverGroupQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDisasterRecoverGroups(
            self,
            request: models.DescribeDisasterRecoverGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDisasterRecoverGroupsResponse:
        """
        This API is used to query the information on [spread placement groups](https://intl.cloud.tencent.com/document/product/213/15486?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDisasterRecoverGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDisasterRecoverGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHosts(
            self,
            request: models.DescribeHostsRequest,
            opts: Dict = None,
    ) -> models.DescribeHostsResponse:
        """
        This API is used to query the details of CDH instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHosts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageFromFamily(
            self,
            request: models.DescribeImageFromFamilyRequest,
            opts: Dict = None,
    ) -> models.DescribeImageFromFamilyResponse:
        """
        This API is used to view information about available images within an image family.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageFromFamily"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageFromFamilyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageQuota(
            self,
            request: models.DescribeImageQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeImageQuotaResponse:
        """
        This API is used to query the image quota of an user account.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageSharePermission(
            self,
            request: models.DescribeImageSharePermissionRequest,
            opts: Dict = None,
    ) -> models.DescribeImageSharePermissionResponse:
        """
        This API is used to query image sharing information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageSharePermission"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageSharePermissionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImages(
            self,
            request: models.DescribeImagesRequest,
            opts: Dict = None,
    ) -> models.DescribeImagesResponse:
        """
        This API is used to view the list of images.

        * You specify the image ID or set filters to query the details of certain images.
        * You can specify `Offset` and `Limit` to select a certain part of the results. By default, the information on the first 20 matching results is returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImportImageOs(
            self,
            request: models.DescribeImportImageOsRequest,
            opts: Dict = None,
    ) -> models.DescribeImportImageOsResponse:
        """
        This API is used to query the list of supported operating systems of imported images.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImportImageOs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImportImageOsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceFamilyConfigs(
            self,
            request: models.DescribeInstanceFamilyConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceFamilyConfigsResponse:
        """
        This API is used to query a list of model families available to the current user in the current region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceFamilyConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceFamilyConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        This API is used to query the details of instances.

        * You can filter the query results with the instance `ID`, name, or billing method. See `Filter` for more information.
        * If no parameter is defined, a certain number of instances under the current account will be returned. The number is specified by `Limit` and is 20 by default.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstancesAttributes(
            self,
            request: models.DescribeInstancesAttributesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesAttributesResponse:
        """
        This API is used to obtain the attributes of specified instances. Currently, it supports querying the custom data UserData of instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancesAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstancesOperationLimit(
            self,
            request: models.DescribeInstancesOperationLimitRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesOperationLimitResponse:
        """
        This API is used to query limitations on operations on an instance.

        * Currently you can use this API to query the maximum number of times you can modify the configuration of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancesOperationLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesOperationLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstancesStatus(
            self,
            request: models.DescribeInstancesStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesStatusResponse:
        """
        This API is used to query the status of instances.

        * You can query the status of an instance with its `ID`.
        * If no parameter is defined, the status of a certain number of instances under the current account will be returned. The number is specified by `Limit` and is 20 by default.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancesStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInternetChargeTypeConfigs(
            self,
            request: models.DescribeInternetChargeTypeConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeInternetChargeTypeConfigsResponse:
        """
        This API is used to query the network billing methods.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInternetChargeTypeConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInternetChargeTypeConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKeyPairs(
            self,
            request: models.DescribeKeyPairsRequest,
            opts: Dict = None,
    ) -> models.DescribeKeyPairsResponse:
        """
        This API is used to query key pairs.

        * A key pair is a pair of keys generated by an algorithm in which the public key is available to the public and the private key is available only to the user. You can use this API to query the public key but not the private key.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKeyPairs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKeyPairsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLaunchTemplateVersions(
            self,
            request: models.DescribeLaunchTemplateVersionsRequest,
            opts: Dict = None,
    ) -> models.DescribeLaunchTemplateVersionsResponse:
        """
        This API is used to query the information of instance launch template versions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLaunchTemplateVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLaunchTemplateVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLaunchTemplates(
            self,
            request: models.DescribeLaunchTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeLaunchTemplatesResponse:
        """
        This API is used to query one or more instance launch templates.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLaunchTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLaunchTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegions(
            self,
            request: models.DescribeRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeRegionsResponse:
        """
        This API is suspended. To query the information of regions, use [DescribeZones](https://intl.cloud.tencent.com/document/product/1596/77930?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReservedInstances(
            self,
            request: models.DescribeReservedInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeReservedInstancesResponse:
        """
        This API is used to list the reserved instances purchased by the user.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReservedInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReservedInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReservedInstancesConfigInfos(
            self,
            request: models.DescribeReservedInstancesConfigInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeReservedInstancesConfigInfosResponse:
        """
        This API is used to describe reserved instance (RI) offerings.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReservedInstancesConfigInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReservedInstancesConfigInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReservedInstancesOfferings(
            self,
            request: models.DescribeReservedInstancesOfferingsRequest,
            opts: Dict = None,
    ) -> models.DescribeReservedInstancesOfferingsResponse:
        """
        This API is used to describe Reserved Instance offerings that are available for purchase.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReservedInstancesOfferings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReservedInstancesOfferingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZoneInstanceConfigInfos(
            self,
            request: models.DescribeZoneInstanceConfigInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeZoneInstanceConfigInfosResponse:
        """
        This API is used to query the configurations of models in an availability zone.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZoneInstanceConfigInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZoneInstanceConfigInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZones(
            self,
            request: models.DescribeZonesRequest,
            opts: Dict = None,
    ) -> models.DescribeZonesResponse:
        """
        This API is used to query availability zones.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZones"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZonesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateInstancesKeyPairs(
            self,
            request: models.DisassociateInstancesKeyPairsRequest,
            opts: Dict = None,
    ) -> models.DisassociateInstancesKeyPairsResponse:
        """
        This API is used to unbind one or more key pairs from one or more instances.

        * It only supports [`STOPPED`](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#InstanceStatus) Linux instances.
        * After a key pair is disassociated from an instance, you can log in to the instance with password.
        * If you did not set a password for the instance, you will not be able to log in via SSH after the unbinding. In this case, you can call [ResetInstancesPassword](https://intl.cloud.tencent.com/document/api/213/15736?from_cn_redirect=1) to set a login password.
        * Batch operations are supported. The maximum number of instances in each request is 100. If instances not available for the operation are selected, you will get an error code.
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateInstancesKeyPairs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateInstancesKeyPairsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateSecurityGroups(
            self,
            request: models.DisassociateSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DisassociateSecurityGroupsResponse:
        """
        This API is used to disassociate security groups from instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnterRescueMode(
            self,
            request: models.EnterRescueModeRequest,
            opts: Dict = None,
    ) -> models.EnterRescueModeResponse:
        """
        This API is used to enter the rescue mode.
        """
        
        kwargs = {}
        kwargs["action"] = "EnterRescueMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnterRescueModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExitRescueMode(
            self,
            request: models.ExitRescueModeRequest,
            opts: Dict = None,
    ) -> models.ExitRescueModeResponse:
        """
        This API is used to exit the rescue mode.
        """
        
        kwargs = {}
        kwargs["action"] = "ExitRescueMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExitRescueModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportImages(
            self,
            request: models.ExportImagesRequest,
            opts: Dict = None,
    ) -> models.ExportImagesResponse:
        """
        This API is used to export custom images to the specified COS bucket.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportImages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportImagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportImage(
            self,
            request: models.ImportImageRequest,
            opts: Dict = None,
    ) -> models.ImportImageResponse:
        """
        This API is used to import an image. The image imported can be used to create instances. Currently, this API supports RAW, VHD, QCOW2, and VMDK image formats.
        """
        
        kwargs = {}
        kwargs["action"] = "ImportImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportKeyPair(
            self,
            request: models.ImportKeyPairRequest,
            opts: Dict = None,
    ) -> models.ImportKeyPairResponse:
        """
        This API is used to import key pairs.

        * You can use this API to import key pairs to a user account, but the key pairs will not be automatically associated with any instance. You may use [AssociasteInstancesKeyPair](https://intl.cloud.tencent.com/document/api/213/15698?from_cn_redirect=1) to associate key pairs with instances.
        * You need to specify the names of the key pairs and the content of the public keys.
        * If you only have private keys, you can convert them to public keys with the `SSL` tool before importing them.
        """
        
        kwargs = {}
        kwargs["action"] = "ImportKeyPair"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportKeyPairResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePricePurchaseReservedInstancesOffering(
            self,
            request: models.InquirePricePurchaseReservedInstancesOfferingRequest,
            opts: Dict = None,
    ) -> models.InquirePricePurchaseReservedInstancesOfferingResponse:
        """
        This API is used to query the price of reserved instances. It only supports querying purchasable reserved instance offerings. Currently, RIs are only offered to beta users.
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePricePurchaseReservedInstancesOffering"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePricePurchaseReservedInstancesOfferingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceModifyInstancesChargeType(
            self,
            request: models.InquiryPriceModifyInstancesChargeTypeRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceModifyInstancesChargeTypeResponse:
        """
        This API is used to inquire about the price for switching billing modes of instance.


        This API is used to indicate that instances with no charge when shut down, instances of the model families Batch Computing BC1 and Batch Computing BS1, instances of scheduled termination, and spot instances do not support this operation.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceModifyInstancesChargeType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceModifyInstancesChargeTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceRenewInstances(
            self,
            request: models.InquiryPriceRenewInstancesRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceRenewInstancesResponse:
        """
        This API is used to inquire about the price for renewing a monthly subscription instance.

        This API is used to query the renewal price of monthly subscription instances.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceRenewInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceRenewInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceResetInstance(
            self,
            request: models.InquiryPriceResetInstanceRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceResetInstanceResponse:
        """
        This API is used to inquire about the price for reinstalling an instance.

        * If you have specified the parameter `ImageId`, inquire about the price for reinstallation by using the specified image. Otherwise, inquire about the price for reinstallation based on the image currently used by the instance.
        * Currently, only instances with a [system disk type](https://intl.cloud.tencent.com/document/api/213/15753?from_cn_redirect=1#SystemDisk) of `CLOUD_BSSD`, `CLOUD_PREMIUM`, or `CLOUD_SSD` are supported for inquiring about the price for reinstallation caused by switching between `Linux` and `Windows` operating systems through this API.
        * Currently, instances in regions outside the Chinese mainland are not supported for inquiring about the price for reinstallation caused by switching between `Linux` and `Windows` operating systems through this API.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceResetInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceResetInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceResetInstancesInternetMaxBandwidth(
            self,
            request: models.InquiryPriceResetInstancesInternetMaxBandwidthRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceResetInstancesInternetMaxBandwidthResponse:
        """
        This API is used to query the price for upgrading the public bandwidth cap of an instance.

        * The allowed bandwidth cap varies for different models. For details, see [Purchasing Network Bandwidth](https://intl.cloud.tencent.com/document/product/213/509?from_cn_redirect=1).
        * For bandwidth billed by the `TRAFFIC_POSTPAID_BY_HOUR` method, changing the bandwidth cap through this API takes effect in real time. You can increase or reduce bandwidth within applicable limits.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceResetInstancesInternetMaxBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceResetInstancesInternetMaxBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceResetInstancesType(
            self,
            request: models.InquiryPriceResetInstancesTypeRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceResetInstancesTypeResponse:
        """
        This API is used to query the price for adjusting the instance model.

        * Currently, you can only use this API to query the prices of instances whose [system disk type](https://intl.cloud.tencent.com/document/api/213/9452?from_cn_redirect=1#block_device) is `CLOUD_BASIC`, `CLOUD_PREMIUM`, or `CLOUD_SSD`.
        * Currently, you cannot use this API to query the prices of [CDH](https://intl.cloud.tencent.com/document/product/416?from_cn_redirect=1) instances.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceResetInstancesType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceResetInstancesTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceResizeInstanceDisks(
            self,
            request: models.InquiryPriceResizeInstanceDisksRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceResizeInstanceDisksResponse:
        """
        This API is used to query the price for expanding data disks of an instance.

        * Currently, you can only use this API to query the price of non-elastic data disks whose [disk type](https://intl.cloud.tencent.com/document/api/213/9452?from_cn_redirect=1#block_device) is `CLOUD_BASIC`, `CLOUD_PREMIUM`, or `CLOUD_SSD`. You can use [`DescribeDisks`](https://intl.cloud.tencent.com/document/api/362/16315?from_cn_redirect=1) to check whether a disk is elastic. If the `Portable` field in the response is `false`, it means that the disk is non-elastic.
        * Currently, you cannot use this API to query the price for [CDH](https://intl.cloud.tencent.com/document/product/416?from_cn_redirect=1) instances. *Also, you can only query the price of expanding one data disk at a time.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceResizeInstanceDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceResizeInstanceDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceRunInstances(
            self,
            request: models.InquiryPriceRunInstancesRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceRunInstancesResponse:
        """
        This API is used to query the price of creating instances. You can only use this API for instances whose configuration is within the purchase limit. For more information, see [RunInstances](https://intl.cloud.tencent.com/document/api/213/15730?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceRunInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceRunInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyChcAttribute(
            self,
            request: models.ModifyChcAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyChcAttributeResponse:
        """
        This API is used to modify the CHC host attributes.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyChcAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyChcAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDisasterRecoverGroupAttribute(
            self,
            request: models.ModifyDisasterRecoverGroupAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyDisasterRecoverGroupAttributeResponse:
        """
        This API is used to modify the attributes of [spread placement groups](https://intl.cloud.tencent.com/document/product/213/15486?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDisasterRecoverGroupAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDisasterRecoverGroupAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHostsAttribute(
            self,
            request: models.ModifyHostsAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyHostsAttributeResponse:
        """
        This API is used to modify the attributes of a CDH instance, such as instance name and renewal flag. One of the two parameters, HostName and RenewFlag, must be set, but you cannot set both of them at the same time.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHostsAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHostsAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyImageAttribute(
            self,
            request: models.ModifyImageAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyImageAttributeResponse:
        """
        This API is used to modify image attributes.

        * Attributes of shared images cannot be modified.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyImageAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyImageAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyImageSharePermission(
            self,
            request: models.ModifyImageSharePermissionRequest,
            opts: Dict = None,
    ) -> models.ModifyImageSharePermissionResponse:
        """
        This API is used to modify image sharing information.

        * The account with shared image access can use the image to create instances.
        * Each custom image can be shared with a maximum of 500 accounts.
        * Shared images cannot have their names or description changed. They can only be used to create instances.
        * Sharing is only supported within the same region as the recipient's account.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyImageSharePermission"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyImageSharePermissionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstancesAttribute(
            self,
            request: models.ModifyInstancesAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyInstancesAttributeResponse:
        """
        This API is used to modify instance attributes.

        This API is used to modify one attribute of the instance per request. The attribute must be specified.
        The instance name is only for user convenience in management. Tencent Cloud does not use this name as the basis for online support or to perform instance management operations.
        This API is used to support batch operations. The maximum of 100 batch instances per request is supported.
        This API is used to modify the security group association. The originally associated security group of the instance will be unbound.
        * You can query the result of the instance operation by calling the API [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5). If the latest operation status (LatestOperationState) of the instance is **SUCCESS**, the operation is successful.
        This API is used to modify the hostname. The instance restarts immediately after hostname modification, and the new hostname takes effect after restart.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstancesAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstancesAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstancesChargeType(
            self,
            request: models.ModifyInstancesChargeTypeRequest,
            opts: Dict = None,
    ) -> models.ModifyInstancesChargeTypeResponse:
        """
        This API is used to switch the billing mode of an instance.

        This API is used to perform operations that do not support instances with no charge when shut down, instances of the model families Batch Compute BC1 and Batch Compute BS1, or instances of scheduled termination.
        * You can query the result of the instance operation by calling the API [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5). If the latest operation status (LatestOperationState) of the instance is **SUCCESS**, the operation is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstancesChargeType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstancesChargeTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstancesDisasterRecoverGroup(
            self,
            request: models.ModifyInstancesDisasterRecoverGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyInstancesDisasterRecoverGroupResponse:
        """
        This API is used to adjust the placement group of an instance.
        * Currently only basic networks or Virtual Private Cloud (VPC) instances are supported.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstancesDisasterRecoverGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstancesDisasterRecoverGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstancesProject(
            self,
            request: models.ModifyInstancesProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyInstancesProjectResponse:
        """
        This API is used to change the project to which an instance is assigned.

        * Project is a virtual concept. You can create multiple projects under one account, manage different resources in each project, and assign different instances to different projects. You may use the [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) API to query instances and use the project ID to filter the results.
        * You cannot modify the project of an instance that is bound to a load balancer. You need to unbind the load balancer from the instance by using the [DeregisterInstancesFromLoadBalancer](https://intl.cloud.tencent.com/document/api/214/1258?from_cn_redirect=1) API before using this API.
        * Batch operations are supported. Up to 100 instances per request is allowed.
        * You can use the API [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5) to query the operation result. If the `LatestOperationState` in the response is `SUCCESS`, the operation is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstancesProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstancesProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstancesRenewFlag(
            self,
            request: models.ModifyInstancesRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifyInstancesRenewFlagResponse:
        """
        This API is used to modify the renewal flag of monthly subscription instances.

        * After an instance is marked as auto-renewal, it will be automatically renewed for one month each time it expires.
        * Batch operations are supported. The maximum number of instances for each request is 100.* You can query the result of the instance operation by calling the API [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5). If the latest operation status (LatestOperationState) of the instance is **SUCCESS**, the operation is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstancesRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstancesRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstancesVpcAttribute(
            self,
            request: models.ModifyInstancesVpcAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyInstancesVpcAttributeResponse:
        """
        This API is used to modify the VPC attributes of an instance, such as the VPC IP address.
        * This action will shut down the instance, and restart it after the modification is completed.
        * To migrate an instance to another VPC/subnet, specify the new VPC and subnet directly. Make sure that the instance to migrate is not bound to an [ENI](https://intl.cloud.tencent.com/document/product/576?from_cn_redirect=1) or [CLB](https://intl.cloud.tencent.com/document/product/214?from_cn_redirect=1) instances.
        * You can use the API [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5) to query the operation result. If the `LatestOperationState` in the response is `SUCCESS`, the operation is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstancesVpcAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstancesVpcAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyKeyPairAttribute(
            self,
            request: models.ModifyKeyPairAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyKeyPairAttributeResponse:
        """
        This API is used to modify attributes of a key pair.

        * Modify the name and description information of the key pair specified by the key pair ID.
        * The key pair name should not be the same as the name of an existing key pair.
        * The key pair ID is the unique identifier of a key pair and cannot be modified.

        * Either the key pair name or description information should be specified, and both can also be specified simultaneously.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyKeyPairAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyKeyPairAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLaunchTemplateDefaultVersion(
            self,
            request: models.ModifyLaunchTemplateDefaultVersionRequest,
            opts: Dict = None,
    ) -> models.ModifyLaunchTemplateDefaultVersionResponse:
        """
        This API is used to modify the default version of the instance launch template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLaunchTemplateDefaultVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLaunchTemplateDefaultVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PurchaseReservedInstancesOffering(
            self,
            request: models.PurchaseReservedInstancesOfferingRequest,
            opts: Dict = None,
    ) -> models.PurchaseReservedInstancesOfferingResponse:
        """
        This API is used to purchase one or more specific Reserved Instances.
        """
        
        kwargs = {}
        kwargs["action"] = "PurchaseReservedInstancesOffering"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PurchaseReservedInstancesOfferingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RebootInstances(
            self,
            request: models.RebootInstancesRequest,
            opts: Dict = None,
    ) -> models.RebootInstancesResponse:
        """
        This API is used to restart instances.

        * You can only perform this operation on instances whose status is `RUNNING`.
        * If the API is called successfully, the instance status will become `REBOOTING`. After the instance is restarted, its status will become `RUNNING` again.
        * Forced restart is supported. A forced restart is similar to switching off the power of a physical computer and starting it again. It may cause data loss or file system corruption. Be sure to only force start a CVM when it cannot be restarted normally.
        * Batch operations are supported. The maximum number of instances in each request is 100.
        """
        
        kwargs = {}
        kwargs["action"] = "RebootInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RebootInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveChcAssistVpc(
            self,
            request: models.RemoveChcAssistVpcRequest,
            opts: Dict = None,
    ) -> models.RemoveChcAssistVpcResponse:
        """
        This API is used to remove the out-of-band network and deployment network of a CHC host.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveChcAssistVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveChcAssistVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveChcDeployVpc(
            self,
            request: models.RemoveChcDeployVpcRequest,
            opts: Dict = None,
    ) -> models.RemoveChcDeployVpcResponse:
        """
        This API is used to remove the deployment network of a CHC host.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveChcDeployVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveChcDeployVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewInstances(
            self,
            request: models.RenewInstancesRequest,
            opts: Dict = None,
    ) -> models.RenewInstancesResponse:
        """
        This API is used to renew annual and monthly subscription instances.

        This API is used to operate on monthly subscription instances only.
        This API is used to ensure your account balance is sufficient for renewal. You can check the balance via the DescribeAccountBalance API (https://www.tencentcloud.comom/document/product/555/20253?from_cn_redirect=1).
        * You can query the result of the instance operation by calling the API [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5). If the latest operation status (LatestOperationState) of the instance is **SUCCESS**, the operation is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "RenewInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetInstance(
            self,
            request: models.ResetInstanceRequest,
            opts: Dict = None,
    ) -> models.ResetInstanceResponse:
        """
        This API (ResetInstance) is used to reinstall the operating system on a specified instance.



        * If you have specified the parameter `ImageId`, use the specified image for reinstallation. Otherwise, perform reinstallation based on the image currently used by the instance.
        * The system disk will be formatted and reset. Ensure that there are no important files in the system disk.
        * If you do not specify a password, a random password will be sent via Message Center.
        * Currently, only instances with a [system disk type](https://intl.cloud.tencent.com/document/api/213/9452?from_cn_redirect=1#SystemDisk) of `CLOUD_BASIC`, `CLOUD_PREMIUM`, `CLOUD_SSD`, or `CLOUD_BSSD` are supported for implementing operating system switching through this API.
        * You can query the result of the instance operation by calling the API [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5). If the latest operation status (LatestOperationState) of the instance is **SUCCESS**, the operation is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetInstancesInternetMaxBandwidth(
            self,
            request: models.ResetInstancesInternetMaxBandwidthRequest,
            opts: Dict = None,
    ) -> models.ResetInstancesInternetMaxBandwidthResponse:
        """
        This API is used to change the public bandwidth cap of an instance.

        * The allowed bandwidth cap varies for different models. For details, see [Purchasing Network Bandwidth](https://intl.cloud.tencent.com/document/product/213/509?from_cn_redirect=1).
        * For bandwidth billed by the `TRAFFIC_POSTPAID_BY_HOUR` method, changing the bandwidth cap through this API takes effect in real time. Users can increase or reduce bandwidth within applicable limits.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetInstancesInternetMaxBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetInstancesInternetMaxBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetInstancesPassword(
            self,
            request: models.ResetInstancesPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetInstancesPasswordResponse:
        """
        This API is used to reset the password of the operating system instances to a user-specified password.

        * To modify the password of the administrator account: the name of the administrator account varies with the operating system. In Windows, it is `Administrator`; in Ubuntu, it is `ubuntu`; in Linux, it is `root`.
        * To reset the password of a running instance, you need to set the parameter `ForceStop` to `True` for a forced shutdown. If not, only passwords of stopped instances can be reset.
        * Batch operations are supported. You can reset the passwords of up to 100 instances to the same value once.
        * You can call the [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1#.E7.A4.BA.E4.BE.8B3-.E6.9F.A5.E8.AF.A2.E5.AE.9E.E4.BE.8B.E7.9A.84.E6.9C.80.E6.96.B0.E6.93.8D.E4.BD.9C.E6.83.85.E5.86.B5) API and find the result of the operation in the response parameter `LatestOperationState`. If the value is `SUCCESS`, the operation is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetInstancesPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetInstancesPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetInstancesType(
            self,
            request: models.ResetInstancesTypeRequest,
            opts: Dict = None,
    ) -> models.ResetInstancesTypeResponse:
        """
        This API is used to change the model of an instance.
        * You can only use this API to change the models of instances whose [system disk type](https://intl.cloud.tencent.com/document/api/213/9452?from_cn_redirect=1#block_device) is `CLOUD_BASIC`, `CLOUD_PREMIUM`, or `CLOUD_SSD`.
        * Currently, you cannot use this API to change the models of [CDH](https://intl.cloud.tencent.com/document/product/416?from_cn_redirect=1) instances.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetInstancesType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetInstancesTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResizeInstanceDisks(
            self,
            request: models.ResizeInstanceDisksRequest,
            opts: Dict = None,
    ) -> models.ResizeInstanceDisksResponse:
        """
        This API (ResizeInstanceDisks) is used to expand the data disks of an instance.

        * Currently, you can only use the API to expand non-elastic data disks whose [disk type](https://intl.cloud.tencent.com/document/api/213/9452?from_cn_redirect=1#block_device) is `CLOUD_BASIC`, `CLOUD_PREMIUM`, or `CLOUD_SSD`. You can use [`DescribeDisks`](https://intl.cloud.tencent.com/document/api/362/16315?from_cn_redirect=1) to check whether a disk is elastic. If the `Portable` field in the response is `false`, it means that the disk is non-elastic.
        * Currently, this API does not support [CDH](https://intl.cloud.tencent.com/document/product/416?from_cn_redirect=1) instances.
        * Currently, only one data disk can be expanded at a time.
        """
        
        kwargs = {}
        kwargs["action"] = "ResizeInstanceDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResizeInstanceDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunInstances(
            self,
            request: models.RunInstancesRequest,
            opts: Dict = None,
    ) -> models.RunInstancesResponse:
        """
        This API is used to create one or more instances with a specified configuration.

        * After an instance is created successfully, it will start up automatically, and the [instance status](https://www.tencentcloud.com/document/product/213/15753?has_map=1#instancestatus) will become "Running".
        * If you create a pay-as-you-go instance billed on an hourly basis, an amount equivalent to the hourly rate will be frozen. Make sure your account balance is sufficient before calling this API.
        * The number of instances you can purchase through this API is subject to the [Quota for CVM Instances](https://intl.cloud.tencent.com/document/product/213/2664?from_cn_redirect=1). Instances created through this API and in the CVM console are counted toward the quota.
        * This API is an async API. An instance ID list is returned after the creation request is sent. However, it does not mean the creation has been completed. The status of the instance will be `Creating` during the creation. You can use [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) to query the status of the instance. If the status changes from `Creating` to `Running`, it means that the instance has been created successfully.
        """
        
        kwargs = {}
        kwargs["action"] = "RunInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartInstances(
            self,
            request: models.StartInstancesRequest,
            opts: Dict = None,
    ) -> models.StartInstancesResponse:
        """
        This API is used to start instances.

        * You can only perform this operation on instances whose status is `STOPPED`.
        * The instance status will become `STARTING` when the API is called successfully and `RUNNING` when the instance is successfully started.
        * Batch operations are supported. The maximum number of instances in each request is 100.
        """
        
        kwargs = {}
        kwargs["action"] = "StartInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopInstances(
            self,
            request: models.StopInstancesRequest,
            opts: Dict = None,
    ) -> models.StopInstancesResponse:
        """
        This API is used to shut down instances.

        * You can only perform this operation on instances whose status is `RUNNING`.
        * The instance status will become `STOPPING` when the API is called successfully and `STOPPED` when the instance is successfully shut down.
        * Forced shutdown is supported. A forced shutdown is similar to switching off the power of a physical computer. It may cause data loss or file system corruption. Be sure to only force shut down a CVM when it cannot be sht down normally.
        * Batch operations are supported. The maximum number of instances in each request is 100.
        """
        
        kwargs = {}
        kwargs["action"] = "StopInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncImages(
            self,
            request: models.SyncImagesRequest,
            opts: Dict = None,
    ) -> models.SyncImagesResponse:
        """
        This API is used to synchronize custom images to other regions.

        * This API only supports synchronizing one image per call.
        * This API supports multiple synchronization regions.
        * A single account can have a maximum of 500 custom images in each region.
        """
        
        kwargs = {}
        kwargs["action"] = "SyncImages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncImagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateInstances(
            self,
            request: models.TerminateInstancesRequest,
            opts: Dict = None,
    ) -> models.TerminateInstancesResponse:
        """
        This API is used to return instances.

        * Use this API to return instances that are no longer required.
        * Pay-as-you-go instances can be returned directly through this API.
        * Batch operations are supported. The allowed maximum number of instances in each request is 100.
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)