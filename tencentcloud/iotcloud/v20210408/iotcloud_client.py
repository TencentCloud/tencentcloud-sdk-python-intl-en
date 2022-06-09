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
from tencentcloud.iotcloud.v20210408 import models


class IotcloudClient(AbstractClient):
    _apiVersion = '2021-04-08'
    _endpoint = 'iotcloud.tencentcloudapi.com'
    _service = 'iotcloud'


    def CreateDevice(self, request):
        """This API is used to create an IoT Hub device.

        :param request: Request instance for CreateDevice.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.CreateDeviceRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.CreateDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDevice", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDeviceResponse()
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


    def CreatePrivateCA(self, request):
        """This API is used to create a private CA certificate.

        :param request: Request instance for CreatePrivateCA.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.CreatePrivateCARequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.CreatePrivateCAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrivateCA", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePrivateCAResponse()
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


    def CreateProduct(self, request):
        """This API is used to create a new IoT communication product.

        :param request: Request instance for CreateProduct.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.CreateProductRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.CreateProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProduct", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProductResponse()
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


    def DeleteDevice(self, request):
        """This API is used to delete an IoT Hub device.

        :param request: Request instance for DeleteDevice.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DeleteDeviceRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DeleteDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDevice", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDeviceResponse()
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


    def DeletePrivateCA(self, request):
        """This API is used to delete a private CA certificate.

        :param request: Request instance for DeletePrivateCA.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DeletePrivateCARequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DeletePrivateCAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrivateCA", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePrivateCAResponse()
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


    def DeleteProduct(self, request):
        """This API is used to delete an IoT Hub product.

        :param request: Request instance for DeleteProduct.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DeleteProductRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DeleteProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProduct", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteProductResponse()
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


    def DescribeDevice(self, request):
        """This API is used to query device details.

        :param request: Request instance for DescribeDevice.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeDeviceRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDevice", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceResponse()
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


    def DescribeDevices(self, request):
        """This API is used to get the list of IoT Hub devices.

        :param request: Request instance for DescribeDevices.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeDevicesRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDevices", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDevicesResponse()
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


    def DescribePrivateCA(self, request):
        """This API is used to query private CA certificate details.

        :param request: Request instance for DescribePrivateCA.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribePrivateCARequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribePrivateCAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivateCA", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrivateCAResponse()
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


    def DescribePrivateCABindedProducts(self, request):
        """This API is used to query the products bound to a private CA certificate.

        :param request: Request instance for DescribePrivateCABindedProducts.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribePrivateCABindedProductsRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribePrivateCABindedProductsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivateCABindedProducts", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrivateCABindedProductsResponse()
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


    def DescribePrivateCAs(self, request):
        """This API is used to get the list of private CA certificates.

        :param request: Request instance for DescribePrivateCAs.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribePrivateCAsRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribePrivateCAsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivateCAs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrivateCAsResponse()
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


    def DescribeProduct(self, request):
        """This API is used to query product details.

        :param request: Request instance for DescribeProduct.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeProductRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProduct", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProductResponse()
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


    def DescribeProductCA(self, request):
        """This API is used to query the CA certificates bound to a product.

        :param request: Request instance for DescribeProductCA.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeProductCARequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeProductCAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProductCA", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProductCAResponse()
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


    def DescribeProducts(self, request):
        """This API is used to obtain the product list.

        :param request: Request instance for DescribeProducts.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.DescribeProductsRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.DescribeProductsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProducts", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProductsResponse()
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


    def SetProductsForbiddenStatus(self, request):
        """This API is used to enable or disable multiple products at a time.

        :param request: Request instance for SetProductsForbiddenStatus.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.SetProductsForbiddenStatusRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.SetProductsForbiddenStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetProductsForbiddenStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetProductsForbiddenStatusResponse()
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


    def UpdateDeviceLogLevel(self, request):
        """This API is used to set the device log level.

        :param request: Request instance for UpdateDeviceLogLevel.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.UpdateDeviceLogLevelRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.UpdateDeviceLogLevelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDeviceLogLevel", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateDeviceLogLevelResponse()
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


    def UpdateDevicesEnableState(self, request):
        """This API is used to enable or disable multiple devices.

        :param request: Request instance for UpdateDevicesEnableState.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.UpdateDevicesEnableStateRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.UpdateDevicesEnableStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDevicesEnableState", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateDevicesEnableStateResponse()
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


    def UpdatePrivateCA(self, request):
        """This API is used to update a private CA certificate.

        :param request: Request instance for UpdatePrivateCA.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.UpdatePrivateCARequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.UpdatePrivateCAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdatePrivateCA", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdatePrivateCAResponse()
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


    def UpdateProductDynamicRegister(self, request):
        """This API is used to update the configuration of product dynamic registration.

        :param request: Request instance for UpdateProductDynamicRegister.
        :type request: :class:`tencentcloud.iotcloud.v20210408.models.UpdateProductDynamicRegisterRequest`
        :rtype: :class:`tencentcloud.iotcloud.v20210408.models.UpdateProductDynamicRegisterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateProductDynamicRegister", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateProductDynamicRegisterResponse()
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