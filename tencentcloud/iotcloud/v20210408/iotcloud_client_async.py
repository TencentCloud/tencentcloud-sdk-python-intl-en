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
from tencentcloud.iotcloud.v20210408 import models
from typing import Dict


class IotcloudClient(AbstractClient):
    _apiVersion = '2021-04-08'
    _endpoint = 'iotcloud.intl.tencentcloudapi.com'
    _service = 'iotcloud'

    async def CreateDevice(
            self,
            request: models.CreateDeviceRequest,
            opts: Dict = None,
    ) -> models.CreateDeviceResponse:
        """
        This API is used to create an IoT Hub device.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrivateCA(
            self,
            request: models.CreatePrivateCARequest,
            opts: Dict = None,
    ) -> models.CreatePrivateCAResponse:
        """
        This API is used to create a private CA certificate.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrivateCA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrivateCAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProduct(
            self,
            request: models.CreateProductRequest,
            opts: Dict = None,
    ) -> models.CreateProductResponse:
        """
        This API is used to create a new IoT communication product.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDevice(
            self,
            request: models.DeleteDeviceRequest,
            opts: Dict = None,
    ) -> models.DeleteDeviceResponse:
        """
        This API is used to delete an IoT Hub device.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDeviceShadow(
            self,
            request: models.DeleteDeviceShadowRequest,
            opts: Dict = None,
    ) -> models.DeleteDeviceShadowResponse:
        """
        This API is used to delete a device shadow.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDeviceShadow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDeviceShadowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrivateCA(
            self,
            request: models.DeletePrivateCARequest,
            opts: Dict = None,
    ) -> models.DeletePrivateCAResponse:
        """
        This API is used to delete a private CA certificate.
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrivateCA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrivateCAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProduct(
            self,
            request: models.DeleteProductRequest,
            opts: Dict = None,
    ) -> models.DeleteProductResponse:
        """
        This API is used to delete an IoT Hub product.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDevice(
            self,
            request: models.DescribeDeviceRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceResponse:
        """
        This API is used to query device details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDevices(
            self,
            request: models.DescribeDevicesRequest,
            opts: Dict = None,
    ) -> models.DescribeDevicesResponse:
        """
        This API is used to get the list of IoT Hub devices.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDevices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDevicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivateCA(
            self,
            request: models.DescribePrivateCARequest,
            opts: Dict = None,
    ) -> models.DescribePrivateCAResponse:
        """
        This API is used to query private CA certificate details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivateCA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivateCAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivateCABindedProducts(
            self,
            request: models.DescribePrivateCABindedProductsRequest,
            opts: Dict = None,
    ) -> models.DescribePrivateCABindedProductsResponse:
        """
        This API is used to query the products bound to a private CA certificate.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivateCABindedProducts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivateCABindedProductsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivateCAs(
            self,
            request: models.DescribePrivateCAsRequest,
            opts: Dict = None,
    ) -> models.DescribePrivateCAsResponse:
        """
        This API is used to get the list of private CA certificates.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivateCAs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivateCAsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProduct(
            self,
            request: models.DescribeProductRequest,
            opts: Dict = None,
    ) -> models.DescribeProductResponse:
        """
        This API is used to query product details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProductCA(
            self,
            request: models.DescribeProductCARequest,
            opts: Dict = None,
    ) -> models.DescribeProductCAResponse:
        """
        This API is used to query the CA certificates bound to a product.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProductCA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductCAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProducts(
            self,
            request: models.DescribeProductsRequest,
            opts: Dict = None,
    ) -> models.DescribeProductsResponse:
        """
        This API is used to obtain the product list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProducts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetProductsForbiddenStatus(
            self,
            request: models.SetProductsForbiddenStatusRequest,
            opts: Dict = None,
    ) -> models.SetProductsForbiddenStatusResponse:
        """
        This API is used to enable or disable multiple products at a time.
        """
        
        kwargs = {}
        kwargs["action"] = "SetProductsForbiddenStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetProductsForbiddenStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDeviceLogLevel(
            self,
            request: models.UpdateDeviceLogLevelRequest,
            opts: Dict = None,
    ) -> models.UpdateDeviceLogLevelResponse:
        """
        This API is used to set the device log level.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDeviceLogLevel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDeviceLogLevelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDevicesEnableState(
            self,
            request: models.UpdateDevicesEnableStateRequest,
            opts: Dict = None,
    ) -> models.UpdateDevicesEnableStateResponse:
        """
        This API is used to enable or disable multiple devices.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDevicesEnableState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDevicesEnableStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdatePrivateCA(
            self,
            request: models.UpdatePrivateCARequest,
            opts: Dict = None,
    ) -> models.UpdatePrivateCAResponse:
        """
        This API is used to update a private CA certificate.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdatePrivateCA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdatePrivateCAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateProductDynamicRegister(
            self,
            request: models.UpdateProductDynamicRegisterRequest,
            opts: Dict = None,
    ) -> models.UpdateProductDynamicRegisterResponse:
        """
        This API is used to update the configuration of product dynamic registration.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateProductDynamicRegister"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateProductDynamicRegisterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)