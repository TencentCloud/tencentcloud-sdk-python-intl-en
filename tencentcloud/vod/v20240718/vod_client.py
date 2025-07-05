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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.vod.v20240718 import models


class VodClient(AbstractClient):
    _apiVersion = '2024-07-18'
    _endpoint = 'vod.intl.tencentcloudapi.com'
    _service = 'vod'


    def CreateIncrementalMigrationStrategy(self, request):
        """Create an incremental migration strategy for the storage of the professional application.

        :param request: Request instance for CreateIncrementalMigrationStrategy.
        :type request: :class:`tencentcloud.vod.v20240718.models.CreateIncrementalMigrationStrategyRequest`
        :rtype: :class:`tencentcloud.vod.v20240718.models.CreateIncrementalMigrationStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIncrementalMigrationStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIncrementalMigrationStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStorage(self, request):
        """This API is used to create storage for professional applications.

        Note:
        - This API is exclusively for professional applications.
        - When a customer creates a VOD professional application, the system automatically enables storage in certain regions by default. If the customer needs to enable storage in other regions, they can do so using this API.
        - All storage regions and the regions where storage have already been enabled can be queried using the [DescribeStorageRegions](https://cloud.tencent.com/document/product/266/72480) API.

        :param request: Request instance for CreateStorage.
        :type request: :class:`tencentcloud.vod.v20240718.models.CreateStorageRequest`
        :rtype: :class:`tencentcloud.vod.v20240718.models.CreateStorageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStorage", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStorageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStorageCredentials(self, request):
        """The API is used to generate access credentials for VOD professional applications, such as generating credentials for client uploads.

        :param request: Request instance for CreateStorageCredentials.
        :type request: :class:`tencentcloud.vod.v20240718.models.CreateStorageCredentialsRequest`
        :rtype: :class:`tencentcloud.vod.v20240718.models.CreateStorageCredentialsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStorageCredentials", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStorageCredentialsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIncrementalMigrationStrategy(self, request):
        """Delete the incremental migration strategy.

        :param request: Request instance for DeleteIncrementalMigrationStrategy.
        :type request: :class:`tencentcloud.vod.v20240718.models.DeleteIncrementalMigrationStrategyRequest`
        :rtype: :class:`tencentcloud.vod.v20240718.models.DeleteIncrementalMigrationStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIncrementalMigrationStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIncrementalMigrationStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIncrementalMigrationStrategyInfos(self, request):
        """Describe the information of the incremental migration strategy.

        :param request: Request instance for DescribeIncrementalMigrationStrategyInfos.
        :type request: :class:`tencentcloud.vod.v20240718.models.DescribeIncrementalMigrationStrategyInfosRequest`
        :rtype: :class:`tencentcloud.vod.v20240718.models.DescribeIncrementalMigrationStrategyInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIncrementalMigrationStrategyInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIncrementalMigrationStrategyInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStorage(self, request):
        """This API is used to query bucket information in the professional application, and it also supports paginated queries.
        Note:
        - This API is exclusively for use in the professional application.

        :param request: Request instance for DescribeStorage.
        :type request: :class:`tencentcloud.vod.v20240718.models.DescribeStorageRequest`
        :rtype: :class:`tencentcloud.vod.v20240718.models.DescribeStorageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStorage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStorageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIncrementalMigrationStrategy(self, request):
        """Modify the information of incremental migration strategy.

        :param request: Request instance for ModifyIncrementalMigrationStrategy.
        :type request: :class:`tencentcloud.vod.v20240718.models.ModifyIncrementalMigrationStrategyRequest`
        :rtype: :class:`tencentcloud.vod.v20240718.models.ModifyIncrementalMigrationStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIncrementalMigrationStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIncrementalMigrationStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))