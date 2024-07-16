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
from tencentcloud.cdwdoris.v20211228 import models


class CdwdorisClient(AbstractClient):
    _apiVersion = '2021-12-28'
    _endpoint = 'cdwdoris.tencentcloudapi.com'
    _service = 'cdwdoris'


    def CreateInstanceNew(self, request):
        """This API is used to create clusters.

        :param request: Request instance for CreateInstanceNew.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.CreateInstanceNewRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.CreateInstanceNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstanceNew", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstanceNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterConfigs(self, request):
        """This API is used to get the contents of the latest configuration files (config.xml, metrika.xml, and user.xml) of the cluster and display them to the user.

        :param request: Request instance for DescribeClusterConfigs.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeClusterConfigsRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeClusterConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabaseAuditDownload(self, request):
        """This API is used to download database audit logs.

        :param request: Request instance for DescribeDatabaseAuditDownload.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeDatabaseAuditDownloadRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeDatabaseAuditDownloadResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabaseAuditDownload", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabaseAuditDownloadResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabaseAuditRecords(self, request):
        """This API is used to get database audit records.

        :param request: Request instance for DescribeDatabaseAuditRecords.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeDatabaseAuditRecordsRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeDatabaseAuditRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabaseAuditRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabaseAuditRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstance(self, request):
        """This API is used to query the specific information of a cluster based on the cluster ID.

        :param request: Request instance for DescribeInstance.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceNodes(self, request):
        """This API is used to get the list of cluster node information.

        :param request: Request instance for DescribeInstanceNodes.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceNodesRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceNodesInfo(self, request):
        """This API is used to get the BE/FE node roles.

        :param request: Request instance for DescribeInstanceNodesInfo.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceNodesInfoRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceNodesInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceNodesInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceNodesInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceState(self, request):
        """This API is used to display cluster status, process progress, etc. in the cluster details page.

        :param request: Request instance for DescribeInstanceState.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceStateRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceState", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        """This API is used to get the list of clusters.

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstancesResponse`

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


    def DescribeSlowQueryRecords(self, request):
        """This API is used to get the slow log list.

        :param request: Request instance for DescribeSlowQueryRecords.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeSlowQueryRecordsRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeSlowQueryRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowQueryRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowQueryRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowQueryRecordsDownload(self, request):
        """This API is used to download slow log files.

        :param request: Request instance for DescribeSlowQueryRecordsDownload.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeSlowQueryRecordsDownloadRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeSlowQueryRecordsDownloadResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowQueryRecordsDownload", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowQueryRecordsDownloadResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyInstance(self, request):
        """This API is used to terminate clusters.

        :param request: Request instance for DestroyInstance.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DestroyInstanceRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DestroyInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstance(self, request):
        """This API is used to modify the cluster's name.

        :param request: Request instance for ModifyInstance.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyInstanceRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResizeDisk(self, request):
        """This API is used to expand cloud disks.

        :param request: Request instance for ResizeDisk.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ResizeDiskRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ResizeDiskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResizeDisk", params, headers=headers)
            response = json.loads(body)
            model = models.ResizeDiskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartClusterForNode(self, request):
        """This API is used to indicate the rolling restart of the clusters.

        :param request: Request instance for RestartClusterForNode.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.RestartClusterForNodeRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.RestartClusterForNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartClusterForNode", params, headers=headers)
            response = json.loads(body)
            model = models.RestartClusterForNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScaleOutInstance(self, request):
        """This API is used to horizontally scale out nodes.

        :param request: Request instance for ScaleOutInstance.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ScaleOutInstanceRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ScaleOutInstanceResponse`

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


    def ScaleUpInstance(self, request):
        """This API is used to scale up/down computing resources.

        :param request: Request instance for ScaleUpInstance.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ScaleUpInstanceRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ScaleUpInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScaleUpInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ScaleUpInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))