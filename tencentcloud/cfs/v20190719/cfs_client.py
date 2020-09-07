# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.cfs.v20190719 import models


class CfsClient(AbstractClient):
    _apiVersion = '2019-07-19'
    _endpoint = 'cfs.tencentcloudapi.com'


    def CreateCfsFileSystem(self, request):
        """This API is used to create a file system.

        :param request: Request instance for CreateCfsFileSystem.
        :type request: :class:`tencentcloud.cfs.v20190719.models.CreateCfsFileSystemRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.CreateCfsFileSystemResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCfsFileSystem", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCfsFileSystemResponse()
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


    def CreateCfsPGroup(self, request):
        """This API is used to create a permission group.

        :param request: Request instance for CreateCfsPGroup.
        :type request: :class:`tencentcloud.cfs.v20190719.models.CreateCfsPGroupRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.CreateCfsPGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCfsPGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCfsPGroupResponse()
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


    def CreateCfsRule(self, request):
        """This API is used to create a permission group rule.

        :param request: Request instance for CreateCfsRule.
        :type request: :class:`tencentcloud.cfs.v20190719.models.CreateCfsRuleRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.CreateCfsRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCfsRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCfsRuleResponse()
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


    def DeleteCfsFileSystem(self, request):
        """This API is used to delete a file system.

        :param request: Request instance for DeleteCfsFileSystem.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsFileSystemRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsFileSystemResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCfsFileSystem", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCfsFileSystemResponse()
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


    def DeleteCfsPGroup(self, request):
        """This API is used to delete a permission group.

        :param request: Request instance for DeleteCfsPGroup.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsPGroupRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsPGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCfsPGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCfsPGroupResponse()
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


    def DeleteCfsRule(self, request):
        """This API is used to delete a permission group rule.

        :param request: Request instance for DeleteCfsRule.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsRuleRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCfsRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCfsRuleResponse()
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


    def DeleteMountTarget(self, request):
        """This API is used to delete a mount target.

        :param request: Request instance for DeleteMountTarget.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DeleteMountTargetRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DeleteMountTargetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMountTarget", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMountTargetResponse()
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


    def DescribeAvailableZoneInfo(self, request):
        """This API is used to query the availability of a region.

        :param request: Request instance for DescribeAvailableZoneInfo.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeAvailableZoneInfoRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeAvailableZoneInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAvailableZoneInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAvailableZoneInfoResponse()
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


    def DescribeCfsFileSystemClients(self, request):
        """This API is used to query clients on which this file system is mounted. To do so, the client needs to have the CFS monitoring plugin installed.

        :param request: Request instance for DescribeCfsFileSystemClients.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsFileSystemClientsRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsFileSystemClientsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCfsFileSystemClients", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCfsFileSystemClientsResponse()
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


    def DescribeCfsFileSystems(self, request):
        """This API is used to query file systems.

        :param request: Request instance for DescribeCfsFileSystems.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsFileSystemsRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsFileSystemsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCfsFileSystems", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCfsFileSystemsResponse()
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


    def DescribeCfsPGroups(self, request):
        """This API is used to query the list of permission groups.

        :param request: Request instance for DescribeCfsPGroups.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsPGroupsRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsPGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCfsPGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCfsPGroupsResponse()
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


    def DescribeCfsRules(self, request):
        """This API is used to query the list of permission group rules.

        :param request: Request instance for DescribeCfsRules.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsRulesRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCfsRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCfsRulesResponse()
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


    def DescribeCfsServiceStatus(self, request):
        """This API is used to query the status of the CFS service.

        :param request: Request instance for DescribeCfsServiceStatus.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsServiceStatusRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsServiceStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCfsServiceStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCfsServiceStatusResponse()
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


    def DescribeMountTargets(self, request):
        """This API is used to query the mount targets of a file system.

        :param request: Request instance for DescribeMountTargets.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeMountTargetsRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeMountTargetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMountTargets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMountTargetsResponse()
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


    def SignUpCfsService(self, request):
        """This API is used to activate the CFS service.

        :param request: Request instance for SignUpCfsService.
        :type request: :class:`tencentcloud.cfs.v20190719.models.SignUpCfsServiceRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.SignUpCfsServiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SignUpCfsService", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SignUpCfsServiceResponse()
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


    def UpdateCfsFileSystemName(self, request):
        """This API is used to update a file system name.

        :param request: Request instance for UpdateCfsFileSystemName.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsFileSystemNameRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsFileSystemNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateCfsFileSystemName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateCfsFileSystemNameResponse()
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


    def UpdateCfsFileSystemPGroup(self, request):
        """This API is used to update the permission group used by a file system.

        :param request: Request instance for UpdateCfsFileSystemPGroup.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsFileSystemPGroupRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsFileSystemPGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateCfsFileSystemPGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateCfsFileSystemPGroupResponse()
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


    def UpdateCfsFileSystemSizeLimit(self, request):
        """This API is used to update the capacity limit of a file system.

        :param request: Request instance for UpdateCfsFileSystemSizeLimit.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsFileSystemSizeLimitRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsFileSystemSizeLimitResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateCfsFileSystemSizeLimit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateCfsFileSystemSizeLimitResponse()
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


    def UpdateCfsPGroup(self, request):
        """This API is used to update the information of a permission group.

        :param request: Request instance for UpdateCfsPGroup.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsPGroupRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsPGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateCfsPGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateCfsPGroupResponse()
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


    def UpdateCfsRule(self, request):
        """This API is used to update a permission rule.

        :param request: Request instance for UpdateCfsRule.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsRuleRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateCfsRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateCfsRuleResponse()
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