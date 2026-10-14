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
from tencentcloud.es.v20180416 import models


class EsClient(AbstractClient):
    _apiVersion = '2018-04-16'
    _endpoint = 'es.intl.tencentcloudapi.com'
    _service = 'es'


    def CreateAutoBackUpStrategy(self, request):
        r"""This API is used to create an auto backup snapshot policy.

        :param request: Request instance for CreateAutoBackUpStrategy.
        :type request: :class:`tencentcloud.es.v20180416.models.CreateAutoBackUpStrategyRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.CreateAutoBackUpStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAutoBackUpStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAutoBackUpStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIndex(self, request):
        r"""Create an index

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
        r"""Create an ES cluster instance with the specified specification.

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


    def DeleteAutoBackUpStrategy(self, request):
        r"""This API is used to delete an auto backup snapshot policy.

        :param request: Request instance for DeleteAutoBackUpStrategy.
        :type request: :class:`tencentcloud.es.v20180416.models.DeleteAutoBackUpStrategyRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DeleteAutoBackUpStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAutoBackUpStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAutoBackUpStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIndex(self, request):
        r"""Delete an index

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
        r"""Terminate cluster instances

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


    def DescribeAutoBackUpStrategy(self, request):
        r"""This API is used to obtain an auto backup snapshot policy.

        :param request: Request instance for DescribeAutoBackUpStrategy.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeAutoBackUpStrategyRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeAutoBackUpStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoBackUpStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoBackUpStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIndexList(self, request):
        r"""This API is used to obtain the index list.

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
        r"""This API is used to retrieve index metadata.

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
        r"""Query the logs of eligible ES clusters in that region for the user.

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
        r"""Query the operation records of an instance under specified conditions.

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
        r"""Query all instances meeting conditions for the user in that region

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
        r"""Query view data of a cluster, including cluster-level, node, and Kibana dimensions.

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
        r"""Get the node type that receives client requests.

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


    def ModifyAutoBackUpCommonInfo(self, request):
        r"""This API is used to modify the common information of an auto backup snapshot policy.

        :param request: Request instance for ModifyAutoBackUpCommonInfo.
        :type request: :class:`tencentcloud.es.v20180416.models.ModifyAutoBackUpCommonInfoRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.ModifyAutoBackUpCommonInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAutoBackUpCommonInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAutoBackUpCommonInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAutoBackUpStrategy(self, request):
        r"""This API is used to modify an auto backup snapshot policy.

        :param request: Request instance for ModifyAutoBackUpStrategy.
        :type request: :class:`tencentcloud.es.v20180416.models.ModifyAutoBackUpStrategyRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.ModifyAutoBackUpStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAutoBackUpStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAutoBackUpStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartInstance(self, request):
        r"""Restart ES cluster instances for system version update.

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
        r"""Restart Kibana

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
        r"""Used to restart cluster nodes.

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
        r"""Update the ES cluster dictionary

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
        r"""Updates an index

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
        r"""Perform operations on the cluster, such as node specification change, instance name modification, configuration modification, password resetting, and Kibana blocklist/allowlist addition. InstanceId is a required parameter, while ForceRestart is optional. The remaining parameter combinations and their meanings are as follows:
        - InstanceName: Modify the instance name (only used to identify the instance)
        -NodeInfoList: Modify node configuration (horizontally scale nodes, vertically scale nodes, add primary nodes, add cold nodes, etc.)
        -EsConfig: modify cluster configuration
        -Password: Modify the password of the default user elastic
        -EsAcl: Modify an ACL
        -CosBackUp: Set cluster COS auto backup information
        Only one of the above parameters can be passed. Passing more or fewer will cause request failure.

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
        r"""Update the plug-in list

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
        r"""This API is used to update the node type that receives client requests.

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
        r"""Upgrades the edition of an ES cluster

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
        r"""Upgrade ES commercial features

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