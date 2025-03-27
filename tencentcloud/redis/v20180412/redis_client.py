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
from tencentcloud.redis.v20180412 import models


class RedisClient(AbstractClient):
    _apiVersion = '2018-04-12'
    _endpoint = 'redis.intl.tencentcloudapi.com'
    _service = 'redis'


    def AddReplicationInstance(self, request):
        """This API is used to add an instance member to the global replication group.

        :param request: Request instance for AddReplicationInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.AddReplicationInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.AddReplicationInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddReplicationInstance", params, headers=headers)
            response = json.loads(body)
            model = models.AddReplicationInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AllocateWanAddress(self, request):
        """This API is used to enable public network access for instances.

        :param request: Request instance for AllocateWanAddress.
        :type request: :class:`tencentcloud.redis.v20180412.models.AllocateWanAddressRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.AllocateWanAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AllocateWanAddress", params, headers=headers)
            response = json.loads(body)
            model = models.AllocateWanAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ApplyParamsTemplate(self, request):
        """This API is used to apply parameter templates to instances.

        :param request: Request instance for ApplyParamsTemplate.
        :type request: :class:`tencentcloud.redis.v20180412.models.ApplyParamsTemplateRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ApplyParamsTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyParamsTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyParamsTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateSecurityGroups(self, request):
        """This API is used to bind a security group to one or more database instances. When you create an instance without configuring a security group, it is recommended to bind a security group through this API.

        :param request: Request instance for AssociateSecurityGroups.
        :type request: :class:`tencentcloud.redis.v20180412.models.AssociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.AssociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChangeInstanceRole(self, request):
        """This API is used to change the role of an instance in a replication group.

        :param request: Request instance for ChangeInstanceRole.
        :type request: :class:`tencentcloud.redis.v20180412.models.ChangeInstanceRoleRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ChangeInstanceRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChangeInstanceRole", params, headers=headers)
            response = json.loads(body)
            model = models.ChangeInstanceRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChangeMasterInstance(self, request):
        """This API is used to set a read-only instance in a replication group as a master instance.

        :param request: Request instance for ChangeMasterInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.ChangeMasterInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ChangeMasterInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChangeMasterInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ChangeMasterInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChangeReplicaToMaster(self, request):
        """This API is used to promote a replica node group to a master node group or a replica node to a master node for an instance.

        :param request: Request instance for ChangeReplicaToMaster.
        :type request: :class:`tencentcloud.redis.v20180412.models.ChangeReplicaToMasterRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ChangeReplicaToMasterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChangeReplicaToMaster", params, headers=headers)
            response = json.loads(body)
            model = models.ChangeReplicaToMasterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CleanUpInstance(self, request):
        """This API is used to immediately terminate instances in the recycle bin.

        :param request: Request instance for CleanUpInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.CleanUpInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.CleanUpInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CleanUpInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CleanUpInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ClearInstance(self, request):
        """This API is used to clear instance data.

        :param request: Request instance for ClearInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.ClearInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ClearInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ClearInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ClearInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloneInstances(self, request):
        """This API is used to clone a complete new instance based on the current instance backup file.

        :param request: Request instance for CloneInstances.
        :type request: :class:`tencentcloud.redis.v20180412.models.CloneInstancesRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.CloneInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloneInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CloneInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseSSL(self, request):
        """This API is used to disable SSL encryption and authentication.

        :param request: Request instance for CloseSSL.
        :type request: :class:`tencentcloud.redis.v20180412.models.CloseSSLRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.CloseSSLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseSSL", params, headers=headers)
            response = json.loads(body)
            model = models.CloseSSLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstanceAccount(self, request):
        """This API is used to customize the account for accessing instances.

        :param request: Request instance for CreateInstanceAccount.
        :type request: :class:`tencentcloud.redis.v20180412.models.CreateInstanceAccountRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.CreateInstanceAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstanceAccount", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstanceAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstances(self, request):
        """This API is used to create an TencentDB or Redis instance.

        :param request: Request instance for CreateInstances.
        :type request: :class:`tencentcloud.redis.v20180412.models.CreateInstancesRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.CreateInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateParamTemplate(self, request):
        """This API is used to create a parameter template.

        :param request: Request instance for CreateParamTemplate.
        :type request: :class:`tencentcloud.redis.v20180412.models.CreateParamTemplateRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.CreateParamTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateParamTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateParamTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateReplicationGroup(self, request):
        """This API is used to create a replication group.

        :param request: Request instance for CreateReplicationGroup.
        :type request: :class:`tencentcloud.redis.v20180412.models.CreateReplicationGroupRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.CreateReplicationGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReplicationGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReplicationGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteInstanceAccount(self, request):
        """This API is used to delete instance sub-accounts.

        :param request: Request instance for DeleteInstanceAccount.
        :type request: :class:`tencentcloud.redis.v20180412.models.DeleteInstanceAccountRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DeleteInstanceAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteInstanceAccount", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteInstanceAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteParamTemplate(self, request):
        """This API is used to delete a parameter template.

        :param request: Request instance for DeleteParamTemplate.
        :type request: :class:`tencentcloud.redis.v20180412.models.DeleteParamTemplateRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DeleteParamTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteParamTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteParamTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteReplicationInstance(self, request):
        """This API is used to remove a replication group member. Note: This API is being deprecated. Use [RemoveReplicationInstance](https://intl.cloud.tencent.com/document/product/239/90099?from_cn_redirect=1) instead.

        :param request: Request instance for DeleteReplicationInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.DeleteReplicationInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DeleteReplicationInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReplicationInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteReplicationInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoBackupConfig(self, request):
        """This API is used to get the configuration rules for an automatic backup.

        :param request: Request instance for DescribeAutoBackupConfig.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeAutoBackupConfigRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeAutoBackupConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoBackupConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoBackupConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupDetail(self, request):
        """This API is used to query the backup details of an instance.

        :param request: Request instance for DescribeBackupDetail.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeBackupDetailRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeBackupDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupDownloadRestriction(self, request):
        """This API is used to query the download address for a database backup file in the current region.

        :param request: Request instance for DescribeBackupDownloadRestriction.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeBackupDownloadRestrictionRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeBackupDownloadRestrictionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupDownloadRestriction", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupDownloadRestrictionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupUrl(self, request):
        """This API is used to query the download address of a backup RDB file.

        :param request: Request instance for DescribeBackupUrl.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeBackupUrlRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeBackupUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBandwidthRange(self, request):
        """This API is used to query the information of instance bandwidth.

        :param request: Request instance for DescribeBandwidthRange.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeBandwidthRangeRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeBandwidthRangeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBandwidthRange", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBandwidthRangeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCommonDBInstances(self, request):
        """This API is used to query the list of Redis instances. It is now deprecated.

        :param request: Request instance for DescribeCommonDBInstances.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeCommonDBInstancesRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeCommonDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCommonDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCommonDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBSecurityGroups(self, request):
        """This API is used to query the security group details of an instance.

        :param request: Request instance for DescribeDBSecurityGroups.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeDBSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeDBSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGlobalReplicationArea(self, request):
        """This API is used to query the supported regions for global replication.

        :param request: Request instance for DescribeGlobalReplicationArea.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeGlobalReplicationAreaRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeGlobalReplicationAreaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGlobalReplicationArea", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGlobalReplicationAreaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceAccount(self, request):
        """This API is used to query the information of an instance sub-account.

        :param request: Request instance for DescribeInstanceAccount.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceAccountRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceAccount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceBackups(self, request):
        """This API is used to query the backup list of an instance.

        :param request: Request instance for DescribeInstanceBackups.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceBackupsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceBackupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceBackups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceBackupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceDTSInfo(self, request):
        """This API is used to query instance DTS information.

        :param request: Request instance for DescribeInstanceDTSInfo.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceDTSInfoRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceDTSInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceDTSInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceDTSInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceDealDetail(self, request):
        """This API is used to query the order information.

        :param request: Request instance for DescribeInstanceDealDetail.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceDealDetailRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceDealDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceDealDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceDealDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceEvents(self, request):
        """This API is used to query the event information on a TecentDB for Redis instance.

        :param request: Request instance for DescribeInstanceEvents.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceEventsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceLogDelivery(self, request):
        """This API is used to query the instance log shipping configuration.

        :param request: Request instance for DescribeInstanceLogDelivery.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceLogDeliveryRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceLogDeliveryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceLogDelivery", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceLogDeliveryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceMonitorBigKey(self, request):
        """The API for querying big keys of a TencentDB for Redis instance was disused on October 31, 2022. For more information, see [API for Querying Instance Big Key Will Be Disused](https://intl.cloud.tencent.com/document/product/239/81005?from_cn_redirect=1).

        :param request: Request instance for DescribeInstanceMonitorBigKey.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorBigKeyRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorBigKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceMonitorBigKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceMonitorBigKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceMonitorBigKeySizeDist(self, request):
        """The API for querying big keys of a TencentDB for Redis instance was disused on October 31, 2022. For more information, see [API for Querying Instance Big Key Will Be Disused](https://intl.cloud.tencent.com/document/product/239/81005?from_cn_redirect=1).

        :param request: Request instance for DescribeInstanceMonitorBigKeySizeDist.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorBigKeySizeDistRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorBigKeySizeDistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceMonitorBigKeySizeDist", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceMonitorBigKeySizeDistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceMonitorBigKeyTypeDist(self, request):
        """The API for querying big keys of a TencentDB for Redis instance was disused on October 31, 2022. For more information, see [API for Querying Instance Big Key Will Be Disused](https://intl.cloud.tencent.com/document/product/239/81005?from_cn_redirect=1).

        :param request: Request instance for DescribeInstanceMonitorBigKeyTypeDist.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorBigKeyTypeDistRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorBigKeyTypeDistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceMonitorBigKeyTypeDist", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceMonitorBigKeyTypeDistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceMonitorHotKey(self, request):
        """This API is used to query instance hot keys.

        :param request: Request instance for DescribeInstanceMonitorHotKey.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorHotKeyRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorHotKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceMonitorHotKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceMonitorHotKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceMonitorSIP(self, request):
        """This API is used to query the access source information of an instance.

        :param request: Request instance for DescribeInstanceMonitorSIP.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorSIPRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorSIPResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceMonitorSIP", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceMonitorSIPResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceMonitorTookDist(self, request):
        """This API is used to query the time distribution of instance access.

        :param request: Request instance for DescribeInstanceMonitorTookDist.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorTookDistRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorTookDistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceMonitorTookDist", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceMonitorTookDistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceMonitorTopNCmd(self, request):
        """This API is used to query an instance access command.

        :param request: Request instance for DescribeInstanceMonitorTopNCmd.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorTopNCmdRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorTopNCmdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceMonitorTopNCmd", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceMonitorTopNCmdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceMonitorTopNCmdTook(self, request):
        """This API is used to query the instance CPU time.

        :param request: Request instance for DescribeInstanceMonitorTopNCmdTook.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorTopNCmdTookRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorTopNCmdTookResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceMonitorTopNCmdTook", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceMonitorTopNCmdTookResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceNodeInfo(self, request):
        """This API is used to query the information of an instance node.

        :param request: Request instance for DescribeInstanceNodeInfo.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceNodeInfoRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceNodeInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceNodeInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceNodeInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceParamRecords(self, request):
        """This API is used to query the list of parameter modifications.

        :param request: Request instance for DescribeInstanceParamRecords.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceParamRecordsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceParamRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceParamRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceParamRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceParams(self, request):
        """This API is used to query the parameter list of an instance.

        :param request: Request instance for DescribeInstanceParams.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceParamsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceParamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceParams", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceParamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceSecurityGroup(self, request):
        """This API is used to query the security group information of an instance.

        :param request: Request instance for DescribeInstanceSecurityGroup.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceSecurityGroupRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceSecurityGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceSecurityGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceShards(self, request):
        """This API is used to get the shard information of the instance on cluster architecture.

        :param request: Request instance for DescribeInstanceShards.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceShardsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceShardsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceShards", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceShardsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceSpecBandwidth(self, request):
        """This API is used to query or calculate bandwidth specifications.

        :param request: Request instance for DescribeInstanceSpecBandwidth.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceSpecBandwidthRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceSpecBandwidthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceSpecBandwidth", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceSpecBandwidthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceSupportFeature(self, request):
        """This API (DescribeInstanceSupportFeature) is used to query the supported features of the instance.

        :param request: Request instance for DescribeInstanceSupportFeature.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceSupportFeatureRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceSupportFeatureResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceSupportFeature", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceSupportFeatureResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceZoneInfo(self, request):
        """This API is used to query the details of a Redis node.

        :param request: Request instance for DescribeInstanceZoneInfo.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceZoneInfoRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceZoneInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceZoneInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceZoneInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        """This API is used to query the list of Redis instances.

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstancesResponse`

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


    def DescribeMaintenanceWindow(self, request):
        """This API is used to query the instance maintenance window. Instances that require the version or architecture upgrade will undergo time switching during the maintenance window.

        :param request: Request instance for DescribeMaintenanceWindow.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeMaintenanceWindowRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeMaintenanceWindowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMaintenanceWindow", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMaintenanceWindowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeParamTemplateInfo(self, request):
        """This API is used to query the details of a parameter template.

        :param request: Request instance for DescribeParamTemplateInfo.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeParamTemplateInfoRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeParamTemplateInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeParamTemplateInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeParamTemplateInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeParamTemplates(self, request):
        """This API is used to query the list of parameter templates.

        :param request: Request instance for DescribeParamTemplates.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeParamTemplatesRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeParamTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeParamTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeParamTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProductInfo(self, request):
        """This API is used to query purchasable TencentDB for Redis specifications in all regions.

        :param request: Request instance for DescribeProductInfo.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeProductInfoRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeProductInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProductInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProductInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjectSecurityGroup(self, request):
        """This API is used to query project security group information.

        :param request: Request instance for DescribeProjectSecurityGroup.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeProjectSecurityGroupRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeProjectSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjectSecurityGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectSecurityGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjectSecurityGroups(self, request):
        """This API is used to query the security group details of a project.

        :param request: Request instance for DescribeProjectSecurityGroups.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeProjectSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeProjectSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjectSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProxySlowLog(self, request):
        """This API is used to query the slow queries of the proxy.

        :param request: Request instance for DescribeProxySlowLog.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeProxySlowLogRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeProxySlowLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProxySlowLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProxySlowLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRedisClusterOverview(self, request):
        """This API is used to query the overview information of a dedicated Redis cluster.

        :param request: Request instance for DescribeRedisClusterOverview.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeRedisClusterOverviewRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeRedisClusterOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRedisClusterOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRedisClusterOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRedisClusters(self, request):
        """This API is used to query the list of dedicated Redis clusters.

        :param request: Request instance for DescribeRedisClusters.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeRedisClustersRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeRedisClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRedisClusters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRedisClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReplicationGroup(self, request):
        """This API is used to query a replication group.

        :param request: Request instance for DescribeReplicationGroup.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeReplicationGroupRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeReplicationGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReplicationGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReplicationGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReplicationGroupInstance(self, request):
        """This API is used to query replication group information.

        :param request: Request instance for DescribeReplicationGroupInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeReplicationGroupInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeReplicationGroupInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReplicationGroupInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReplicationGroupInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSSLStatus(self, request):
        """This API is used to query the SSL authentication information of an instance, such as enablement status, configuration status, and certificate address.

        :param request: Request instance for DescribeSSLStatus.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeSSLStatusRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeSSLStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSSLStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSSLStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowLog(self, request):
        """This API is used to query the records of slow query.

        :param request: Request instance for DescribeSlowLog.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeSlowLogRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeSlowLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskInfo(self, request):
        """This API is used to get the execution of a specified task.

        :param request: Request instance for DescribeTaskInfo.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeTaskInfoRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeTaskInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskList(self, request):
        """This API is used to query the task list data for the last 30 days.

        :param request: Request instance for DescribeTaskList.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeTaskListRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTendisSlowLog(self, request):
        """This API is used to query the slow query logs of a Tendis instance.

        :param request: Request instance for DescribeTendisSlowLog.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeTendisSlowLogRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeTendisSlowLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTendisSlowLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTendisSlowLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyPostpaidInstance(self, request):
        """This API is used to terminate pay-as-you-go instances.

        :param request: Request instance for DestroyPostpaidInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.DestroyPostpaidInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DestroyPostpaidInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyPostpaidInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyPostpaidInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyPrepaidInstance(self, request):
        """This API is used to return Redis instances with monthly subscription.

        :param request: Request instance for DestroyPrepaidInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.DestroyPrepaidInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DestroyPrepaidInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyPrepaidInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyPrepaidInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableReplicaReadonly(self, request):
        """This API is used to disable read/write separation.

        :param request: Request instance for DisableReplicaReadonly.
        :type request: :class:`tencentcloud.redis.v20180412.models.DisableReplicaReadonlyRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DisableReplicaReadonlyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableReplicaReadonly", params, headers=headers)
            response = json.loads(body)
            model = models.DisableReplicaReadonlyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateSecurityGroups(self, request):
        """This API is used to unbind security groups from instances in batches.

        :param request: Request instance for DisassociateSecurityGroups.
        :type request: :class:`tencentcloud.redis.v20180412.models.DisassociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DisassociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableReplicaReadonly(self, request):
        """This API is used to enable read/write separation.

        :param request: Request instance for EnableReplicaReadonly.
        :type request: :class:`tencentcloud.redis.v20180412.models.EnableReplicaReadonlyRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.EnableReplicaReadonlyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableReplicaReadonly", params, headers=headers)
            response = json.loads(body)
            model = models.EnableReplicaReadonlyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceCreateInstance(self, request):
        """This API is used to query the price of new instances.

        :param request: Request instance for InquiryPriceCreateInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.InquiryPriceCreateInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.InquiryPriceCreateInstanceResponse`

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


    def InquiryPriceUpgradeInstance(self, request):
        """This API is used to query the price for instance scale-out.

        :param request: Request instance for InquiryPriceUpgradeInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.InquiryPriceUpgradeInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.InquiryPriceUpgradeInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceUpgradeInstance", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceUpgradeInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def KillMasterGroup(self, request):
        """This API is used to simulate a fault.

        :param request: Request instance for KillMasterGroup.
        :type request: :class:`tencentcloud.redis.v20180412.models.KillMasterGroupRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.KillMasterGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KillMasterGroup", params, headers=headers)
            response = json.loads(body)
            model = models.KillMasterGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ManualBackupInstance(self, request):
        """This API is used to manually back up a Redis instance.

        :param request: Request instance for ManualBackupInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.ManualBackupInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ManualBackupInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ManualBackupInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ManualBackupInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModfiyInstancePassword(self, request):
        """This API is used to change the instance access password. Due to a spelling error in the original API name, it has been corrected to [ModifyInstancePassword](https://intl.cloud.tencent.com/document/product/239/111555?from_cn_redirect=1). It is recommended to use the corrected API.

        :param request: Request instance for ModfiyInstancePassword.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModfiyInstancePasswordRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModfiyInstancePasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModfiyInstancePassword", params, headers=headers)
            response = json.loads(body)
            model = models.ModfiyInstancePasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAutoBackupConfig(self, request):
        """This API is used to set the configuration for an automatic backup.

        :param request: Request instance for ModifyAutoBackupConfig.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyAutoBackupConfigRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyAutoBackupConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAutoBackupConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAutoBackupConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBackupDownloadRestriction(self, request):
        """This API is used to modify the network information and address for downloading a backup file.

        :param request: Request instance for ModifyBackupDownloadRestriction.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyBackupDownloadRestrictionRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyBackupDownloadRestrictionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBackupDownloadRestriction", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBackupDownloadRestrictionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyConnectionConfig(self, request):
        """This API is used to modify the connection configuration of an instance, including the bandwidth and maximum number of connections.

        :param request: Request instance for ModifyConnectionConfig.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyConnectionConfigRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyConnectionConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyConnectionConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyConnectionConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceSecurityGroups(self, request):
        """This API is used to modify the original security group list of an instance.

        :param request: Request instance for ModifyDBInstanceSecurityGroups.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyDBInstanceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyDBInstanceSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstance(self, request):
        """This API is used to modify instance information.

        :param request: Request instance for ModifyInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyInstanceResponse`

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


    def ModifyInstanceAccount(self, request):
        """This API is used to modify the instance sub-account.

        :param request: Request instance for ModifyInstanceAccount.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyInstanceAccountRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyInstanceAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceAccount", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceAvailabilityZones(self, request):
        """This API is used to change the availability zone of the instance.

        :param request: Request instance for ModifyInstanceAvailabilityZones.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyInstanceAvailabilityZonesRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyInstanceAvailabilityZonesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceAvailabilityZones", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceAvailabilityZonesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceEvent(self, request):
        """This API is used to modify the operations event execution schedule of an instance.

        :param request: Request instance for ModifyInstanceEvent.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyInstanceEventRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyInstanceEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceEvent", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceLogDelivery(self, request):
        """This API is used to enable or disable the shipping of instance logs to CLS.

        :param request: Request instance for ModifyInstanceLogDelivery.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyInstanceLogDeliveryRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyInstanceLogDeliveryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceLogDelivery", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceLogDeliveryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceParams(self, request):
        """This API is used to modify the parameter configuration of a Redis instance.

        :param request: Request instance for ModifyInstanceParams.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyInstanceParamsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyInstanceParamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceParams", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceParamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstancePassword(self, request):
        """This API is used to change the instance access password.

        :param request: Request instance for ModifyInstancePassword.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyInstancePasswordRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyInstancePasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstancePassword", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstancePasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceReadOnly(self, request):
        """This API is used to set the instance input mode.

        :param request: Request instance for ModifyInstanceReadOnly.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyInstanceReadOnlyRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyInstanceReadOnlyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceReadOnly", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceReadOnlyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMaintenanceWindow(self, request):
        """This API is used to modify the time of instance maintenance window. Instances that require the version or architecture upgrade will undergo time switching during the maintenance window. Note: If the version or architecture upgrade has been initiated for an instance, its maintenance window cannot be modified.

        :param request: Request instance for ModifyMaintenanceWindow.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyMaintenanceWindowRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyMaintenanceWindowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMaintenanceWindow", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMaintenanceWindowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNetworkConfig(self, request):
        """This API is used to modify the network configuration of an instance.

        :param request: Request instance for ModifyNetworkConfig.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyNetworkConfigRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyNetworkConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNetworkConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNetworkConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyParamTemplate(self, request):
        """This API is used to modify the parameter template.

        :param request: Request instance for ModifyParamTemplate.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyParamTemplateRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyParamTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyParamTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyParamTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyReplicationGroup(self, request):
        """This API is used to modify replication group information.

        :param request: Request instance for ModifyReplicationGroup.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyReplicationGroupRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyReplicationGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyReplicationGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyReplicationGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenSSL(self, request):
        """This API is used to enable SSL encryption and authentication.

        :param request: Request instance for OpenSSL.
        :type request: :class:`tencentcloud.redis.v20180412.models.OpenSSLRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.OpenSSLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenSSL", params, headers=headers)
            response = json.loads(body)
            model = models.OpenSSLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReleaseWanAddress(self, request):
        """This API is used to disable public network access.

        :param request: Request instance for ReleaseWanAddress.
        :type request: :class:`tencentcloud.redis.v20180412.models.ReleaseWanAddressRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ReleaseWanAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseWanAddress", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseWanAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveReplicationInstance(self, request):
        """This API is used to remove instances from a replication group.

        :param request: Request instance for RemoveReplicationInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.RemoveReplicationInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.RemoveReplicationInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveReplicationInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveReplicationInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewInstance(self, request):
        """This API is used to renew an instance.

        :param request: Request instance for RenewInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.RenewInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.RenewInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RenewInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetPassword(self, request):
        """This API is used to reset the instance access password.

        :param request: Request instance for ResetPassword.
        :type request: :class:`tencentcloud.redis.v20180412.models.ResetPasswordRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ResetPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestoreInstance(self, request):
        """This API is used to restore a Redis instance.

        :param request: Request instance for RestoreInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.RestoreInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.RestoreInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestoreInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RestoreInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartupInstance(self, request):
        """This API is used to deisolate instances.

        :param request: Request instance for StartupInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.StartupInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.StartupInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartupInstance", params, headers=headers)
            response = json.loads(body)
            model = models.StartupInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchAccessNewInstance(self, request):
        """This API is used to immediately switch instances that are in the time window pending switch operation. Users can manually initiate this operation.

        :param request: Request instance for SwitchAccessNewInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.SwitchAccessNewInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.SwitchAccessNewInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchAccessNewInstance", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchAccessNewInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchInstanceVip(self, request):
        """This API is used to swap the VIPs of instances for disaster recovery in DTS-based cross-AZ disaster recovery scenarios. After the swapping, the target instance becomes writable, the VIPs of the source and target instances are swapped, and the DTS synchronization task between the source and target instances is disconnected.

        :param request: Request instance for SwitchInstanceVip.
        :type request: :class:`tencentcloud.redis.v20180412.models.SwitchInstanceVipRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.SwitchInstanceVipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchInstanceVip", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchInstanceVipResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchProxy(self, request):
        """This API is used to simulate the fault of a Proxy node.

        :param request: Request instance for SwitchProxy.
        :type request: :class:`tencentcloud.redis.v20180412.models.SwitchProxyRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.SwitchProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchProxy", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeInstance(self, request):
        """This API is used to change the configuration specifications of an instance.

        :param request: Request instance for UpgradeInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.UpgradeInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.UpgradeInstanceResponse`

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


    def UpgradeInstanceVersion(self, request):
        """This API is used to upgrade the current instance to a later version or upgrade the current standard architecture to a cluster architecture.

        :param request: Request instance for UpgradeInstanceVersion.
        :type request: :class:`tencentcloud.redis.v20180412.models.UpgradeInstanceVersionRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.UpgradeInstanceVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeInstanceVersion", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeInstanceVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeProxyVersion(self, request):
        """This API is used to upgrade the instance Proxy version.

        :param request: Request instance for UpgradeProxyVersion.
        :type request: :class:`tencentcloud.redis.v20180412.models.UpgradeProxyVersionRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.UpgradeProxyVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeProxyVersion", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeProxyVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeSmallVersion(self, request):
        """This API is used to upgrade the minor version of an instance.

        :param request: Request instance for UpgradeSmallVersion.
        :type request: :class:`tencentcloud.redis.v20180412.models.UpgradeSmallVersionRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.UpgradeSmallVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeSmallVersion", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeSmallVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeVersionToMultiAvailabilityZones(self, request):
        """This API is used to upgrade an instance to support multiple AZs.

        :param request: Request instance for UpgradeVersionToMultiAvailabilityZones.
        :type request: :class:`tencentcloud.redis.v20180412.models.UpgradeVersionToMultiAvailabilityZonesRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.UpgradeVersionToMultiAvailabilityZonesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeVersionToMultiAvailabilityZones", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeVersionToMultiAvailabilityZonesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))