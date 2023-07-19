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
from tencentcloud.es.v20180416 import models


class EsClient(AbstractClient):
    _apiVersion = '2018-04-16'
    _endpoint = 'es.tencentcloudapi.com'
    _service = 'es'


    def CreateIndex(self, request):
        """This API is used to create indices.

        :param request: Request instance for CreateIndex.
        :type request: :class:`tencentcloud.es.v20180416.models.CreateIndexRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.CreateIndexResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIndex", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIndexResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstance(self, request):
        """This API is used to create an ES cluster instance with the specified specification.

        :param request: Request instance for CreateInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.CreateInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.CreateInstanceResponse`

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


    def DeleteIndex(self, request):
        """This API is used to delete indices.

        :param request: Request instance for DeleteIndex.
        :type request: :class:`tencentcloud.es.v20180416.models.DeleteIndexRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DeleteIndexResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIndex", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIndexResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteInstance(self, request):
        """This API is used to terminate a cluster instance.

        :param request: Request instance for DeleteInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.DeleteInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DeleteInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIndexList(self, request):
        """This API is used to obtain the index list.

        :param request: Request instance for DescribeIndexList.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeIndexListRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeIndexListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIndexList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIndexListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIndexMeta(self, request):
        """This API is used to obtain index metadata.

        :param request: Request instance for DescribeIndexMeta.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeIndexMetaRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeIndexMetaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIndexMeta", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIndexMetaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceLogs(self, request):
        """This API is used to query the eligible ES cluster logs in the current region.

        :param request: Request instance for DescribeInstanceLogs.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeInstanceLogsRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeInstanceLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceOperations(self, request):
        """This API is used to query the operation history of an instance by specified criteria.

        :param request: Request instance for DescribeInstanceOperations.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeInstanceOperationsRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeInstanceOperationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceOperations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceOperationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        """This API is used to query all eligible instances in the current region under the current account.

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeInstancesResponse`

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


    def DescribeViews(self, request):
        """This API is used to query view data from three dimensions: cluster, node, and Kibana.

        :param request: Request instance for DescribeViews.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeViewsRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeViewsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeViews", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeViewsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRequestTargetNodeTypes(self, request):
        """This API is used to get the node types used to receive client requests.

        :param request: Request instance for GetRequestTargetNodeTypes.
        :type request: :class:`tencentcloud.es.v20180416.models.GetRequestTargetNodeTypesRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.GetRequestTargetNodeTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRequestTargetNodeTypes", params, headers=headers)
            response = json.loads(body)
            model = models.GetRequestTargetNodeTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartInstance(self, request):
        """This API is used to restart an ES cluster instance (for operations such as system update).

        :param request: Request instance for RestartInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.RestartInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.RestartInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RestartInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartKibana(self, request):
        """This API is used to restart Kibana.

        :param request: Request instance for RestartKibana.
        :type request: :class:`tencentcloud.es.v20180416.models.RestartKibanaRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.RestartKibanaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartKibana", params, headers=headers)
            response = json.loads(body)
            model = models.RestartKibanaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartNodes(self, request):
        """This API is used to restart cluster nodes.

        :param request: Request instance for RestartNodes.
        :type request: :class:`tencentcloud.es.v20180416.models.RestartNodesRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.RestartNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartNodes", params, headers=headers)
            response = json.loads(body)
            model = models.RestartNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateDictionaries(self, request):
        """This API is used to update ES cluster dictionaries.

        :param request: Request instance for UpdateDictionaries.
        :type request: :class:`tencentcloud.es.v20180416.models.UpdateDictionariesRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpdateDictionariesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDictionaries", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDictionariesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateIndex(self, request):
        """This API is used to update indices.

        :param request: Request instance for UpdateIndex.
        :type request: :class:`tencentcloud.es.v20180416.models.UpdateIndexRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpdateIndexResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateIndex", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateIndexResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateInstance(self, request):
        """This API is used for operations such as modifying node specification, renaming an instance, modifying configuration, resetting password, and setting Kibana blocklist/allowlist. `InstanceId` is required, while `ForceRestart` is optional. Other parameters or parameter combinations and their meanings are as follows:
        - InstanceName: renames an instance (only for instance identification)
        - NodeInfoList: modifies node configuration (horizontally scaling nodes, vertically scaling nodes, adding primary nodes, adding cold nodes, etc.)
        - EsConfig: modifies cluster configuration
        - Password: changes the password of the default user "elastic"
        - EsAcl: modifies the ACL
        - CosBackUp: sets auto-backup to COS for a cluster
        Only one of the parameters or parameter combinations above can be passed in at a time, while passing fewer or more ones will cause the request to fail.

        :param request: Request instance for UpdateInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.UpdateInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpdateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdatePlugins(self, request):
        """This API is used to change the list of plugins.

        :param request: Request instance for UpdatePlugins.
        :type request: :class:`tencentcloud.es.v20180416.models.UpdatePluginsRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpdatePluginsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdatePlugins", params, headers=headers)
            response = json.loads(body)
            model = models.UpdatePluginsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateRequestTargetNodeTypes(self, request):
        """This API is used to update the node types used to receive client requests.

        :param request: Request instance for UpdateRequestTargetNodeTypes.
        :type request: :class:`tencentcloud.es.v20180416.models.UpdateRequestTargetNodeTypesRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpdateRequestTargetNodeTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRequestTargetNodeTypes", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRequestTargetNodeTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeInstance(self, request):
        """This API is used to upgrade ES cluster version

        :param request: Request instance for UpgradeInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.UpgradeInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpgradeInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeLicense(self, request):
        """This API is used to upgrade ES X-Pack.

        :param request: Request instance for UpgradeLicense.
        :type request: :class:`tencentcloud.es.v20180416.models.UpgradeLicenseRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpgradeLicenseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeLicense", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeLicenseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))