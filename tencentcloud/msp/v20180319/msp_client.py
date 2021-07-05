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
from tencentcloud.msp.v20180319 import models


class MspClient(AbstractClient):
    _apiVersion = '2018-03-19'
    _endpoint = 'msp.tencentcloudapi.com'
    _service = 'msp'


    def DeregisterMigrationTask(self, request):
        """This API is used to cancel the registered migration tasks.

        :param request: Request instance for DeregisterMigrationTask.
        :type request: :class:`tencentcloud.msp.v20180319.models.DeregisterMigrationTaskRequest`
        :rtype: :class:`tencentcloud.msp.v20180319.models.DeregisterMigrationTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeregisterMigrationTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeregisterMigrationTaskResponse()
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


    def DescribeMigrationTask(self, request):
        """This API is used to obtain the specified migration task details.

        :param request: Request instance for DescribeMigrationTask.
        :type request: :class:`tencentcloud.msp.v20180319.models.DescribeMigrationTaskRequest`
        :rtype: :class:`tencentcloud.msp.v20180319.models.DescribeMigrationTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMigrationTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMigrationTaskResponse()
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


    def ListMigrationProject(self, request):
        """This API is used to obtain the list of migration project names.

        :param request: Request instance for ListMigrationProject.
        :type request: :class:`tencentcloud.msp.v20180319.models.ListMigrationProjectRequest`
        :rtype: :class:`tencentcloud.msp.v20180319.models.ListMigrationProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListMigrationProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListMigrationProjectResponse()
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


    def ListMigrationTask(self, request):
        """This API is used to obtain migration task list.

        :param request: Request instance for ListMigrationTask.
        :type request: :class:`tencentcloud.msp.v20180319.models.ListMigrationTaskRequest`
        :rtype: :class:`tencentcloud.msp.v20180319.models.ListMigrationTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListMigrationTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListMigrationTaskResponse()
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


    def ModifyMigrationTaskBelongToProject(self, request):
        """This API is used to modify the project of a migration task.

        :param request: Request instance for ModifyMigrationTaskBelongToProject.
        :type request: :class:`tencentcloud.msp.v20180319.models.ModifyMigrationTaskBelongToProjectRequest`
        :rtype: :class:`tencentcloud.msp.v20180319.models.ModifyMigrationTaskBelongToProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMigrationTaskBelongToProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMigrationTaskBelongToProjectResponse()
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


    def ModifyMigrationTaskStatus(self, request):
        """This API is used to update the migration task status.

        :param request: Request instance for ModifyMigrationTaskStatus.
        :type request: :class:`tencentcloud.msp.v20180319.models.ModifyMigrationTaskStatusRequest`
        :rtype: :class:`tencentcloud.msp.v20180319.models.ModifyMigrationTaskStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMigrationTaskStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMigrationTaskStatusResponse()
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


    def RegisterMigrationTask(self, request):
        """This API is used to register a migration task.

        :param request: Request instance for RegisterMigrationTask.
        :type request: :class:`tencentcloud.msp.v20180319.models.RegisterMigrationTaskRequest`
        :rtype: :class:`tencentcloud.msp.v20180319.models.RegisterMigrationTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RegisterMigrationTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RegisterMigrationTaskResponse()
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