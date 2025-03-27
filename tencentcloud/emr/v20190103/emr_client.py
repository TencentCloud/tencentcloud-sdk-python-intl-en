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
from tencentcloud.emr.v20190103 import models


class EmrClient(AbstractClient):
    _apiVersion = '2019-01-03'
    _endpoint = 'emr.intl.tencentcloudapi.com'
    _service = 'emr'


    def AddUsersForUserManager(self, request):
        """This API is available for clusters with OpenLDAP components configured.
        This API is used to add user lists (user management).

        :param request: Request instance for AddUsersForUserManager.
        :type request: :class:`tencentcloud.emr.v20190103.models.AddUsersForUserManagerRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.AddUsersForUserManagerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddUsersForUserManager", params, headers=headers)
            response = json.loads(body)
            model = models.AddUsersForUserManagerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCluster(self, request):
        """This API is used to create an EMR cluster instance.

        :param request: Request instance for CreateCluster.
        :type request: :class:`tencentcloud.emr.v20190103.models.CreateClusterRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.CreateClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCluster", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstance(self, request):
        """This API is used to create an EMR cluster instance.

        :param request: Request instance for CreateInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.CreateInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.CreateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoScaleRecords(self, request):
        """This API is used to inquiry detailed records of cluster autoscaling.

        :param request: Request instance for DescribeAutoScaleRecords.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeAutoScaleRecordsRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeAutoScaleRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoScaleRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoScaleRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterNodes(self, request):
        """This API is used to query the information of nodes in a cluster.

        :param request: Request instance for DescribeClusterNodes.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeClusterNodesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeClusterNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEmrApplicationStatics(self, request):
        """This API is used to query the Yarn application statistics.

        :param request: Request instance for DescribeEmrApplicationStatics.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeEmrApplicationStaticsRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeEmrApplicationStaticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEmrApplicationStatics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEmrApplicationStaticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHiveQueries(self, request):
        """This API is used to inquiry Hive query data.

        :param request: Request instance for DescribeHiveQueries.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeHiveQueriesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeHiveQueriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHiveQueries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHiveQueriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        """This API is used to query the information of instances in a cluster.

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeInstancesResponse`

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


    def DescribeInstancesList(self, request):
        """This API is used to query the cluster list.

        :param request: Request instance for DescribeInstancesList.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeInstancesListRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeInstancesListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancesList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceSchedule(self, request):
        """This API is used to query the data of YARN Resource Scheduling.

        :param request: Request instance for DescribeResourceSchedule.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeResourceScheduleRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeResourceScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsersForUserManager(self, request):
        """This API is available for clusters with OpenLDAP components configured.
        This API is used to export users in batches. For a Kerberos cluster, set `NeedKeytabInfo` to `true` to obtain the download link of the Keytab file. If `SupportDownLoadKeyTab` is `true`, but `DownLoadKeyTabUrl` is null, the Keytab file is not ready yet (being generated) in the backend.

        :param request: Request instance for DescribeUsersForUserManager.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeUsersForUserManagerRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeUsersForUserManagerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsersForUserManager", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsersForUserManagerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceCreateInstance(self, request):
        """This API is used to query price of instance creation.

        :param request: Request instance for InquiryPriceCreateInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.InquiryPriceCreateInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquiryPriceCreateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceCreateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceCreateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceRenewInstance(self, request):
        """This API is used to query the price for renewal.

        :param request: Request instance for InquiryPriceRenewInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.InquiryPriceRenewInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquiryPriceRenewInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceRenewInstance", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceRenewInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceScaleOutInstance(self, request):
        """This API is used to query price of scale-out.

        :param request: Request instance for InquiryPriceScaleOutInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.InquiryPriceScaleOutInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquiryPriceScaleOutInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceScaleOutInstance", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceScaleOutInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceUpdateInstance(self, request):
        """This API is used to query price of scaling.

        :param request: Request instance for InquiryPriceUpdateInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.InquiryPriceUpdateInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquiryPriceUpdateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceUpdateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceUpdateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourceScheduleConfig(self, request):
        """This API is used to modify the resource configuration of YARN Resource Scheduling.

        :param request: Request instance for ModifyResourceScheduleConfig.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyResourceScheduleConfigRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyResourceScheduleConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourceScheduleConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourceScheduleConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourceScheduler(self, request):
        """This API is used to modify the YARN resource scheduler (the change will take effect after you click Apply).

        :param request: Request instance for ModifyResourceScheduler.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyResourceSchedulerRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyResourceSchedulerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourceScheduler", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourceSchedulerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourcesTags(self, request):
        """This API is used to forcibly modify tags.

        :param request: Request instance for ModifyResourcesTags.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyResourcesTagsRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyResourcesTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourcesTags", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourcesTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserManagerPwd(self, request):
        """This API is used to change user password (user management).

        :param request: Request instance for ModifyUserManagerPwd.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyUserManagerPwdRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyUserManagerPwdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserManagerPwd", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserManagerPwdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScaleOutCluster(self, request):
        """This API is used to scale out a cluster.

        :param request: Request instance for ScaleOutCluster.
        :type request: :class:`tencentcloud.emr.v20190103.models.ScaleOutClusterRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ScaleOutClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScaleOutCluster", params, headers=headers)
            response = json.loads(body)
            model = models.ScaleOutClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScaleOutInstance(self, request):
        """This API is used to scale out instances.

        :param request: Request instance for ScaleOutInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.ScaleOutInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ScaleOutInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScaleOutInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ScaleOutInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartStopServiceOrMonitor(self, request):
        """This API is used to start, stop, or restart services.

        :param request: Request instance for StartStopServiceOrMonitor.
        :type request: :class:`tencentcloud.emr.v20190103.models.StartStopServiceOrMonitorRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.StartStopServiceOrMonitorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartStopServiceOrMonitor", params, headers=headers)
            response = json.loads(body)
            model = models.StartStopServiceOrMonitorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateClusterNodes(self, request):
        """This API is used to terminate cluster nodes.

        :param request: Request instance for TerminateClusterNodes.
        :type request: :class:`tencentcloud.emr.v20190103.models.TerminateClusterNodesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.TerminateClusterNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateClusterNodes", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateClusterNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateInstance(self, request):
        """This API is used to terminate EMR instances. It is only supported in the official paid edition of EMR.

        :param request: Request instance for TerminateInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.TerminateInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.TerminateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateTasks(self, request):
        """This API is used to terminate a task node.

        :param request: Request instance for TerminateTasks.
        :type request: :class:`tencentcloud.emr.v20190103.models.TerminateTasksRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.TerminateTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateTasks", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))