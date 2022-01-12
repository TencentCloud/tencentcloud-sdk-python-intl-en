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
from tencentcloud.dts.v20180330 import models


class DtsClient(AbstractClient):
    _apiVersion = '2018-03-30'
    _endpoint = 'dts.tencentcloudapi.com'
    _service = 'dts'


    def ActivateSubscribe(self, request):
        """This API is used to configure a data subscription, which can be called only for subscription instances in unconfigured status.

        :param request: Request instance for ActivateSubscribe.
        :type request: :class:`tencentcloud.dts.v20180330.models.ActivateSubscribeRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.ActivateSubscribeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ActivateSubscribe", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ActivateSubscribeResponse()
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


    def CompleteMigrateJob(self, request):
        """This API (CompleteMigrateJob) is used to complete a data migration task.
        For tasks in incremental migration mode, you need to call this API before migration gets ready, so as to stop migrating incremental data.
        If the task status queried through the (DescribeMigrateJobs) API is ready (status=8), you can call this API to complete the migration task.

        :param request: Request instance for CompleteMigrateJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.CompleteMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.CompleteMigrateJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CompleteMigrateJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CompleteMigrateJobResponse()
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


    def CreateMigrateCheckJob(self, request):
        """This API is used to create a migration check task.
        Before migration, you should call this API to create a check. Migration will start only if the check succeeds. You can view the check result through the DescribeMigrateCheckJob API.
        After successful check, if the migration task needs to be modified, a new check task should be created and migration will begin only after the new check succeeds.

        :param request: Request instance for CreateMigrateCheckJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.CreateMigrateCheckJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.CreateMigrateCheckJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMigrateCheckJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMigrateCheckJobResponse()
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


    def CreateMigrateJob(self, request):
        """This API (CreateMigrateJob) is used to create a data migration task.

        For a finance zone linkage, please use the domain name dts.ap-shenzhen-fsi.tencentcloudapi.com.

        :param request: Request instance for CreateMigrateJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.CreateMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.CreateMigrateJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMigrateJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMigrateJobResponse()
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


    def CreateSubscribe(self, request):
        """This API is used to create a data subscription instance.

        :param request: Request instance for CreateSubscribe.
        :type request: :class:`tencentcloud.dts.v20180330.models.CreateSubscribeRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.CreateSubscribeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSubscribe", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSubscribeResponse()
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


    def DeleteMigrateJob(self, request):
        """This API (DeleteMigrationJob) is used to delete a data migration task. If the task status queried through the DescribeMigrateJobs API is checking (status=3), running (status=7), ready (status=8), canceling (status=11), or completing (status=12), the task cannot be deleted.

        :param request: Request instance for DeleteMigrateJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.DeleteMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DeleteMigrateJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMigrateJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMigrateJobResponse()
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
        """This API is used to query the execution result of a task.

        :param request: Request instance for DescribeAsyncRequestInfo.
        :type request: :class:`tencentcloud.dts.v20180330.models.DescribeAsyncRequestInfoRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DescribeAsyncRequestInfoResponse`

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


    def DescribeMigrateCheckJob(self, request):
        """This API is used to get the check result and query check status and progress after a check is created.
        If the check succeeds, you can call the StartMigrateJob API to start migration.
        If the check fails, the reason can be queried. Please modify the migration configuration or adjust relevant parameters of the source/target instances through the ModifyMigrateJob API based on the error message.

        :param request: Request instance for DescribeMigrateCheckJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.DescribeMigrateCheckJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DescribeMigrateCheckJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMigrateCheckJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMigrateCheckJobResponse()
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


    def DescribeMigrateJobs(self, request):
        """This API is used to query data migration tasks.
        For a finance zone linkage, please use the domain name https://dts.ap-shenzhen-fsi.tencentcloudapi.com.

        :param request: Request instance for DescribeMigrateJobs.
        :type request: :class:`tencentcloud.dts.v20180330.models.DescribeMigrateJobsRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DescribeMigrateJobsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMigrateJobs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMigrateJobsResponse()
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


    def DescribeRegionConf(self, request):
        """This API is used to query the purchasable subscription instance regions.

        :param request: Request instance for DescribeRegionConf.
        :type request: :class:`tencentcloud.dts.v20180330.models.DescribeRegionConfRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DescribeRegionConfResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRegionConf", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRegionConfResponse()
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


    def DescribeSubscribeConf(self, request):
        """This API is used to query the subscription instance configuration.

        :param request: Request instance for DescribeSubscribeConf.
        :type request: :class:`tencentcloud.dts.v20180330.models.DescribeSubscribeConfRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DescribeSubscribeConfResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSubscribeConf", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSubscribeConfResponse()
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


    def DescribeSubscribes(self, request):
        """This API is used to get the information list of data subscription instances. Pagination is enabled by default with 20 results returned each time.

        :param request: Request instance for DescribeSubscribes.
        :type request: :class:`tencentcloud.dts.v20180330.models.DescribeSubscribesRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DescribeSubscribesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSubscribes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSubscribesResponse()
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


    def IsolateSubscribe(self, request):
        """This API is used to isolate an hourly billed subscription instance. After this API is called, the instance will become unavailable and billing will stop for it.

        :param request: Request instance for IsolateSubscribe.
        :type request: :class:`tencentcloud.dts.v20180330.models.IsolateSubscribeRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.IsolateSubscribeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("IsolateSubscribe", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IsolateSubscribeResponse()
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


    def ModifyMigrateJob(self, request):
        """This API (ModifyMigrateJob) is used to modify a data migration task.
        If the status of a migration task is creating (status=1), check succeeded (status=4), check failed (status=5), or migration failed (status=10), this API can be called to modify the task, but the type of the source and target instances and the region of the target instance cannot be modified.

        For a finance zone linkage, please use the domain name dts.ap-shenzhen-fsi.tencentcloudapi.com.

        :param request: Request instance for ModifyMigrateJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.ModifyMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.ModifyMigrateJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMigrateJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMigrateJobResponse()
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


    def ModifySubscribeConsumeTime(self, request):
        """This API is used to modify the consumption time point of a data subscription channel.

        :param request: Request instance for ModifySubscribeConsumeTime.
        :type request: :class:`tencentcloud.dts.v20180330.models.ModifySubscribeConsumeTimeRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.ModifySubscribeConsumeTimeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySubscribeConsumeTime", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySubscribeConsumeTimeResponse()
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


    def ModifySubscribeName(self, request):
        """This API is used to rename a data subscription instance.

        :param request: Request instance for ModifySubscribeName.
        :type request: :class:`tencentcloud.dts.v20180330.models.ModifySubscribeNameRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.ModifySubscribeNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySubscribeName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySubscribeNameResponse()
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


    def ModifySubscribeObjects(self, request):
        """This API is used to modify the subscription rule of a data subscription channel.

        :param request: Request instance for ModifySubscribeObjects.
        :type request: :class:`tencentcloud.dts.v20180330.models.ModifySubscribeObjectsRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.ModifySubscribeObjectsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySubscribeObjects", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySubscribeObjectsResponse()
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


    def ModifySubscribeVipVport(self, request):
        """This API is used to modify the IP and port number of a data subscription instance.

        :param request: Request instance for ModifySubscribeVipVport.
        :type request: :class:`tencentcloud.dts.v20180330.models.ModifySubscribeVipVportRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.ModifySubscribeVipVportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySubscribeVipVport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySubscribeVipVportResponse()
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


    def OfflineIsolatedSubscribe(self, request):
        """This API is used to deactivate an isolated data subscription instance.

        :param request: Request instance for OfflineIsolatedSubscribe.
        :type request: :class:`tencentcloud.dts.v20180330.models.OfflineIsolatedSubscribeRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.OfflineIsolatedSubscribeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OfflineIsolatedSubscribe", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OfflineIsolatedSubscribeResponse()
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


    def ResetSubscribe(self, request):
        """This API is used to reset a data subscription instance. Once reset, an activated instance can be bound to other database instances through the `ActivateSubscribe` API.

        :param request: Request instance for ResetSubscribe.
        :type request: :class:`tencentcloud.dts.v20180330.models.ResetSubscribeRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.ResetSubscribeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetSubscribe", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetSubscribeResponse()
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


    def StartMigrateJob(self, request):
        """This API (StartMigrationJob) is used to start a migration task. After the API is called, non-scheduled migration tasks will start the migration immediately, while scheduled tasks will start the countdown.
        Before calling this API, be sure to use the CreateMigrateCheckJob API to check the data migration task, which can be started only if its status queried through the DescribeMigrateJobs API is check succeeded (status=4).

        :param request: Request instance for StartMigrateJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.StartMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.StartMigrateJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartMigrateJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartMigrateJobResponse()
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


    def StopMigrateJob(self, request):
        """This API (StopMigrateJob) is used to cancel a data migration task.
        During migration, this API can be used to cancel migration if the task status queried through the DescribeMigrateJobs API is running (status=7) or ready (status=8), and the migration task will fail.

        :param request: Request instance for StopMigrateJob.
        :type request: :class:`tencentcloud.dts.v20180330.models.StopMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.StopMigrateJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopMigrateJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopMigrateJobResponse()
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