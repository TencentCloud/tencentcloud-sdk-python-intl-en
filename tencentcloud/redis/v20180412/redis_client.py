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
from tencentcloud.redis.v20180412 import models


class RedisClient(AbstractClient):
    _apiVersion = '2018-04-12'
    _endpoint = 'redis.tencentcloudapi.com'


    def CleanUpInstance(self, request):
        """This API is used to deactivate an instance in the recycle bin immediately.

        :param request: Request instance for CleanUpInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.CleanUpInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.CleanUpInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CleanUpInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CleanUpInstanceResponse()
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


    def ClearInstance(self, request):
        """This API is used to clear the data of a Redis instance.

        :param request: Request instance for ClearInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.ClearInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ClearInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ClearInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ClearInstanceResponse()
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


    def CreateInstanceAccount(self, request):
        """This API is used to create an instance sub-account.

        :param request: Request instance for CreateInstanceAccount.
        :type request: :class:`tencentcloud.redis.v20180412.models.CreateInstanceAccountRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.CreateInstanceAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateInstanceAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateInstanceAccountResponse()
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


    def CreateInstances(self, request):
        """This API is used to create a Redis instance.

        :param request: Request instance for CreateInstances.
        :type request: :class:`tencentcloud.redis.v20180412.models.CreateInstancesRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.CreateInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateInstancesResponse()
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


    def DeleteInstanceAccount(self, request):
        """This API is used to delete an instance sub-account.

        :param request: Request instance for DeleteInstanceAccount.
        :type request: :class:`tencentcloud.redis.v20180412.models.DeleteInstanceAccountRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DeleteInstanceAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteInstanceAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteInstanceAccountResponse()
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


    def DescribeAutoBackupConfig(self, request):
        """This API is used to get the backup configuration.

        :param request: Request instance for DescribeAutoBackupConfig.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeAutoBackupConfigRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeAutoBackupConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAutoBackupConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAutoBackupConfigResponse()
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


    def DescribeBackupUrl(self, request):
        """This API is used to query the download address of a backup RDB (it is during beta test and can be used only after you apply for the eligibility).

        :param request: Request instance for DescribeBackupUrl.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeBackupUrlRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeBackupUrlResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBackupUrl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBackupUrlResponse()
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


    def DescribeInstanceAccount(self, request):
        """This API is used to view instance sub-account information.

        :param request: Request instance for DescribeInstanceAccount.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceAccountRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceAccountResponse()
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


    def DescribeInstanceBackups(self, request):
        """This API is used to query the list of Redis instance backups.

        :param request: Request instance for DescribeInstanceBackups.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceBackupsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceBackupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceBackups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceBackupsResponse()
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


    def DescribeInstanceDealDetail(self, request):
        """This API is used to query the order information.

        :param request: Request instance for DescribeInstanceDealDetail.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceDealDetailRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceDealDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceDealDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceDealDetailResponse()
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


    def DescribeInstanceMonitorBigKey(self, request):
        """This API is used to query the big key of an instance.

        :param request: Request instance for DescribeInstanceMonitorBigKey.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorBigKeyRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorBigKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceMonitorBigKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceMonitorBigKeyResponse()
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


    def DescribeInstanceMonitorBigKeySizeDist(self, request):
        """This API is used to query the big key size distribution of an instance.

        :param request: Request instance for DescribeInstanceMonitorBigKeySizeDist.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorBigKeySizeDistRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorBigKeySizeDistResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceMonitorBigKeySizeDist", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceMonitorBigKeySizeDistResponse()
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


    def DescribeInstanceMonitorBigKeyTypeDist(self, request):
        """This API is used to query the big key type distribution of an instance

        :param request: Request instance for DescribeInstanceMonitorBigKeyTypeDist.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorBigKeyTypeDistRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorBigKeyTypeDistResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceMonitorBigKeyTypeDist", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceMonitorBigKeyTypeDistResponse()
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


    def DescribeInstanceMonitorHotKey(self, request):
        """This API is used to query the hot key of an instance.

        :param request: Request instance for DescribeInstanceMonitorHotKey.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorHotKeyRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorHotKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceMonitorHotKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceMonitorHotKeyResponse()
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


    def DescribeInstanceMonitorSIP(self, request):
        """This API is used to query the access source information of an instance.

        :param request: Request instance for DescribeInstanceMonitorSIP.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorSIPRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorSIPResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceMonitorSIP", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceMonitorSIPResponse()
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


    def DescribeInstanceMonitorTookDist(self, request):
        """This API is used to query the distribution of instance access duration.

        :param request: Request instance for DescribeInstanceMonitorTookDist.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorTookDistRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorTookDistResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceMonitorTookDist", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceMonitorTookDistResponse()
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


    def DescribeInstanceMonitorTopNCmd(self, request):
        """This API is used to query an instance access command.

        :param request: Request instance for DescribeInstanceMonitorTopNCmd.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorTopNCmdRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorTopNCmdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceMonitorTopNCmd", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceMonitorTopNCmdResponse()
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


    def DescribeInstanceMonitorTopNCmdTook(self, request):
        """This API is used to query the instance CPU time.

        :param request: Request instance for DescribeInstanceMonitorTopNCmdTook.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorTopNCmdTookRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorTopNCmdTookResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceMonitorTopNCmdTook", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceMonitorTopNCmdTookResponse()
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


    def DescribeInstanceParamRecords(self, request):
        """This API is used to query the list of parameter modifications.

        :param request: Request instance for DescribeInstanceParamRecords.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceParamRecordsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceParamRecordsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceParamRecords", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceParamRecordsResponse()
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


    def DescribeInstanceParams(self, request):
        """This API is used to query the list of instance parameters.

        :param request: Request instance for DescribeInstanceParams.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceParamsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceParamsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceParams", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceParamsResponse()
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


    def DescribeInstanceSecurityGroup(self, request):
        """This API is used to query the security group information of an instance.

        :param request: Request instance for DescribeInstanceSecurityGroup.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceSecurityGroupRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceSecurityGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceSecurityGroupResponse()
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


    def DescribeInstanceShards(self, request):
        """This API is used to get the information of cluster edition instance shards.

        :param request: Request instance for DescribeInstanceShards.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceShardsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceShardsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceShards", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceShardsResponse()
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


    def DescribeInstances(self, request):
        """This API is used to query the list of Redis instances.

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstancesResponse()
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


    def DescribeProductInfo(self, request):
        """This API is used to query the purchasable capacity specifications of Redis instances in the specified AZ and instance type. If you are not in the whitelist for the AZ or instance type, you cannot view the details of the capacity specifications. To apply for the eligibility, please submit a ticket.

        :param request: Request instance for DescribeProductInfo.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeProductInfoRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeProductInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProductInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProductInfoResponse()
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


    def DescribeProjectSecurityGroup(self, request):
        """This API is used to query the security group information of a project.

        :param request: Request instance for DescribeProjectSecurityGroup.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeProjectSecurityGroupRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeProjectSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProjectSecurityGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProjectSecurityGroupResponse()
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


    def DescribeSlowLog(self, request):
        """This API is used to query the slow log.

        :param request: Request instance for DescribeSlowLog.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeSlowLogRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeSlowLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSlowLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSlowLogResponse()
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


    def DescribeTaskInfo(self, request):
        """This API is used to query a task result.

        :param request: Request instance for DescribeTaskInfo.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeTaskInfoRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeTaskInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskInfoResponse()
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


    def DescribeTaskList(self, request):
        """This API is used to query the list of tasks.

        :param request: Request instance for DescribeTaskList.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeTaskListRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeTaskListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskListResponse()
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


    def DestroyPostpaidInstance(self, request):
        """This API is used to terminate a pay-as-you-go instance.

        :param request: Request instance for DestroyPostpaidInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.DestroyPostpaidInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DestroyPostpaidInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DestroyPostpaidInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DestroyPostpaidInstanceResponse()
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


    def DestroyPrepaidInstance(self, request):
        """This API is used to return a monthly subscribed instance.

        :param request: Request instance for DestroyPrepaidInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.DestroyPrepaidInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DestroyPrepaidInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DestroyPrepaidInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DestroyPrepaidInstanceResponse()
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


    def DisableReplicaReadonly(self, request):
        """This API is used to disable read/write separation.

        :param request: Request instance for DisableReplicaReadonly.
        :type request: :class:`tencentcloud.redis.v20180412.models.DisableReplicaReadonlyRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DisableReplicaReadonlyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableReplicaReadonly", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableReplicaReadonlyResponse()
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


    def EnableReplicaReadonly(self, request):
        """This API is used to enable read/write separation.

        :param request: Request instance for EnableReplicaReadonly.
        :type request: :class:`tencentcloud.redis.v20180412.models.EnableReplicaReadonlyRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.EnableReplicaReadonlyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableReplicaReadonly", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableReplicaReadonlyResponse()
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


    def ManualBackupInstance(self, request):
        """This API is used to manually back up a Redis instance.

        :param request: Request instance for ManualBackupInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.ManualBackupInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ManualBackupInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ManualBackupInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ManualBackupInstanceResponse()
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


    def ModfiyInstancePassword(self, request):
        """This API is used to change the Redis password.

        :param request: Request instance for ModfiyInstancePassword.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModfiyInstancePasswordRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModfiyInstancePasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModfiyInstancePassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModfiyInstancePasswordResponse()
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


    def ModifyAutoBackupConfig(self, request):
        """This API is used to set an auto-backup schedule.

        :param request: Request instance for ModifyAutoBackupConfig.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyAutoBackupConfigRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyAutoBackupConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAutoBackupConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAutoBackupConfigResponse()
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


    def ModifyInstance(self, request):
        """This API is used to modify instance information.

        :param request: Request instance for ModifyInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstanceResponse()
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


    def ModifyInstanceAccount(self, request):
        """This API is used to modify an instance sub-account.

        :param request: Request instance for ModifyInstanceAccount.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyInstanceAccountRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyInstanceAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstanceAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstanceAccountResponse()
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


    def ModifyInstanceParams(self, request):
        """This API is used to modify instance parameters.

        :param request: Request instance for ModifyInstanceParams.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyInstanceParamsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyInstanceParamsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstanceParams", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstanceParamsResponse()
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


    def ModifyNetworkConfig(self, request):
        """This API is used to modify the network configuration of an instance.

        :param request: Request instance for ModifyNetworkConfig.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyNetworkConfigRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyNetworkConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNetworkConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNetworkConfigResponse()
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


    def RenewInstance(self, request):
        """This API is used to renew an instance.

        :param request: Request instance for RenewInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.RenewInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.RenewInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewInstanceResponse()
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


    def ResetPassword(self, request):
        """This API is used to reset a password.

        :param request: Request instance for ResetPassword.
        :type request: :class:`tencentcloud.redis.v20180412.models.ResetPasswordRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ResetPasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetPassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetPasswordResponse()
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


    def RestoreInstance(self, request):
        """This API is used to restore a Redis instance.

        :param request: Request instance for RestoreInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.RestoreInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.RestoreInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RestoreInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RestoreInstanceResponse()
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


    def StartupInstance(self, request):
        """This API is used to deisolate an instance.

        :param request: Request instance for StartupInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.StartupInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.StartupInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartupInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartupInstanceResponse()
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


    def UpgradeInstance(self, request):
        """This API is used to upgrade an instance.

        :param request: Request instance for UpgradeInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.UpgradeInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.UpgradeInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeInstanceResponse()
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