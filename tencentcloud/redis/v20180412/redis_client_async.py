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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.redis.v20180412 import models
from typing import Dict


class RedisClient(AbstractClient):
    _apiVersion = '2018-04-12'
    _endpoint = 'redis.intl.tencentcloudapi.com'
    _service = 'redis'

    async def AddReplicationInstance(
            self,
            request: models.AddReplicationInstanceRequest,
            opts: Dict = None,
    ) -> models.AddReplicationInstanceResponse:
        """
        This API is used to add an instance member to the global replication group.
        """
        
        kwargs = {}
        kwargs["action"] = "AddReplicationInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddReplicationInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AllocateWanAddress(
            self,
            request: models.AllocateWanAddressRequest,
            opts: Dict = None,
    ) -> models.AllocateWanAddressResponse:
        """
        This API is used to enable public network access for instances.
        """
        
        kwargs = {}
        kwargs["action"] = "AllocateWanAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AllocateWanAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApplyParamsTemplate(
            self,
            request: models.ApplyParamsTemplateRequest,
            opts: Dict = None,
    ) -> models.ApplyParamsTemplateResponse:
        """
        This API is used to apply parameter templates to instances.
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyParamsTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyParamsTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateSecurityGroups(
            self,
            request: models.AssociateSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.AssociateSecurityGroupsResponse:
        """
        This API is used to bind a security group to one or more database instances. When you create an instance without configuring a security group, it is recommended to bind a security group through this API.
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ChangeInstanceRole(
            self,
            request: models.ChangeInstanceRoleRequest,
            opts: Dict = None,
    ) -> models.ChangeInstanceRoleResponse:
        """
        This API is used to change the role of an instance in a replication group.
        """
        
        kwargs = {}
        kwargs["action"] = "ChangeInstanceRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChangeInstanceRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ChangeMasterInstance(
            self,
            request: models.ChangeMasterInstanceRequest,
            opts: Dict = None,
    ) -> models.ChangeMasterInstanceResponse:
        """
        This API is used to set a read-only instance in a replication group as a master instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ChangeMasterInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChangeMasterInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ChangeReplicaToMaster(
            self,
            request: models.ChangeReplicaToMasterRequest,
            opts: Dict = None,
    ) -> models.ChangeReplicaToMasterResponse:
        """
        This API is used to promote a replica node group to a master node group or a replica node to a master node for an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ChangeReplicaToMaster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChangeReplicaToMasterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CleanUpInstance(
            self,
            request: models.CleanUpInstanceRequest,
            opts: Dict = None,
    ) -> models.CleanUpInstanceResponse:
        """
        This API is used to immediately terminate instances in the recycle bin.
        """
        
        kwargs = {}
        kwargs["action"] = "CleanUpInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CleanUpInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ClearInstance(
            self,
            request: models.ClearInstanceRequest,
            opts: Dict = None,
    ) -> models.ClearInstanceResponse:
        """
        This API is used to clear instance data.
        """
        
        kwargs = {}
        kwargs["action"] = "ClearInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ClearInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloneInstances(
            self,
            request: models.CloneInstancesRequest,
            opts: Dict = None,
    ) -> models.CloneInstancesResponse:
        """
        This API is used to clone a complete new instance based on the current instance backup file.
        """
        
        kwargs = {}
        kwargs["action"] = "CloneInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloneInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseSSL(
            self,
            request: models.CloseSSLRequest,
            opts: Dict = None,
    ) -> models.CloseSSLResponse:
        """
        This API is used to disable SSL encryption and authentication.
        """
        
        kwargs = {}
        kwargs["action"] = "CloseSSL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseSSLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstanceAccount(
            self,
            request: models.CreateInstanceAccountRequest,
            opts: Dict = None,
    ) -> models.CreateInstanceAccountResponse:
        """
        This API is used to customize the account for accessing instances.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstanceAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstances(
            self,
            request: models.CreateInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateInstancesResponse:
        """
        This API is used to create an TencentDB or Redis instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateParamTemplate(
            self,
            request: models.CreateParamTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateParamTemplateResponse:
        """
        This API is used to create a parameter template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateParamTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateParamTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateReplicationGroup(
            self,
            request: models.CreateReplicationGroupRequest,
            opts: Dict = None,
    ) -> models.CreateReplicationGroupResponse:
        """
        This API is used to create a replication group.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReplicationGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReplicationGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteInstanceAccount(
            self,
            request: models.DeleteInstanceAccountRequest,
            opts: Dict = None,
    ) -> models.DeleteInstanceAccountResponse:
        """
        This API is used to delete instance sub-accounts.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInstanceAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInstanceAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteParamTemplate(
            self,
            request: models.DeleteParamTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteParamTemplateResponse:
        """
        This API is used to delete a parameter template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteParamTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteParamTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReplicationInstance(
            self,
            request: models.DeleteReplicationInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteReplicationInstanceResponse:
        """
        This API is used to remove a replication group member. Note: This API is being deprecated. Use [RemoveReplicationInstance](https://intl.cloud.tencent.com/document/product/239/90099?from_cn_redirect=1) instead.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReplicationInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReplicationInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoBackupConfig(
            self,
            request: models.DescribeAutoBackupConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoBackupConfigResponse:
        """
        This API is used to get the configuration rules for an automatic backup.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoBackupConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoBackupConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupDetail(
            self,
            request: models.DescribeBackupDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupDetailResponse:
        """
        This API is used to query the backup details of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupDownloadRestriction(
            self,
            request: models.DescribeBackupDownloadRestrictionRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupDownloadRestrictionResponse:
        """
        This API is used to query the download address for a database backup file in the current region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupDownloadRestriction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupDownloadRestrictionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupUrl(
            self,
            request: models.DescribeBackupUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupUrlResponse:
        """
        This API is used to query the download address of a backup RDB file.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBandwidthRange(
            self,
            request: models.DescribeBandwidthRangeRequest,
            opts: Dict = None,
    ) -> models.DescribeBandwidthRangeResponse:
        """
        This API is used to query the information of instance bandwidth.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBandwidthRange"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBandwidthRangeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCommonDBInstances(
            self,
            request: models.DescribeCommonDBInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeCommonDBInstancesResponse:
        """
        This API is used to query the list of Redis instances. It is now deprecated.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCommonDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCommonDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSecurityGroups(
            self,
            request: models.DescribeDBSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSecurityGroupsResponse:
        """
        This API is used to query the security group details of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGlobalReplicationArea(
            self,
            request: models.DescribeGlobalReplicationAreaRequest,
            opts: Dict = None,
    ) -> models.DescribeGlobalReplicationAreaResponse:
        """
        This API is used to query the information on regions supported for global replication.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGlobalReplicationArea"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGlobalReplicationAreaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceAccount(
            self,
            request: models.DescribeInstanceAccountRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceAccountResponse:
        """
        This API is used to view instance account information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceBackups(
            self,
            request: models.DescribeInstanceBackupsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceBackupsResponse:
        """
        This API is used to query the backup list of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceBackups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceBackupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceDTSInfo(
            self,
            request: models.DescribeInstanceDTSInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceDTSInfoResponse:
        """
        This API is used to query instance DTS information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceDTSInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceDTSInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceDealDetail(
            self,
            request: models.DescribeInstanceDealDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceDealDetailResponse:
        """
        This API is used to query the order information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceDealDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceDealDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceEvents(
            self,
            request: models.DescribeInstanceEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceEventsResponse:
        """
        This API is used to query the event information on a TecentDB for Redis instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceLogDelivery(
            self,
            request: models.DescribeInstanceLogDeliveryRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceLogDeliveryResponse:
        """
        This API is used to query the instance log shipping configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceLogDelivery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceLogDeliveryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceMonitorBigKey(
            self,
            request: models.DescribeInstanceMonitorBigKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceMonitorBigKeyResponse:
        """
        The API for querying big keys of a TencentDB for Redis instance was disused on October 31, 2022. For more information, see [API for Querying Instance Big Key Will Be Disused](https://intl.cloud.tencent.com/document/product/239/81005?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceMonitorBigKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceMonitorBigKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceMonitorBigKeySizeDist(
            self,
            request: models.DescribeInstanceMonitorBigKeySizeDistRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceMonitorBigKeySizeDistResponse:
        """
        The API for querying big keys of a TencentDB for Redis instance was disused on October 31, 2022. For more information, see [API for Querying Instance Big Key Will Be Disused](https://intl.cloud.tencent.com/document/product/239/81005?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceMonitorBigKeySizeDist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceMonitorBigKeySizeDistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceMonitorBigKeyTypeDist(
            self,
            request: models.DescribeInstanceMonitorBigKeyTypeDistRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceMonitorBigKeyTypeDistResponse:
        """
        The API for querying big keys of a TencentDB for Redis instance was disused on October 31, 2022. For more information, see [API for Querying Instance Big Key Will Be Disused](https://intl.cloud.tencent.com/document/product/239/81005?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceMonitorBigKeyTypeDist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceMonitorBigKeyTypeDistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceMonitorHotKey(
            self,
            request: models.DescribeInstanceMonitorHotKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceMonitorHotKeyResponse:
        """
        This API is used to query instance hot keys.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceMonitorHotKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceMonitorHotKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceMonitorSIP(
            self,
            request: models.DescribeInstanceMonitorSIPRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceMonitorSIPResponse:
        """
        This API is no longer used. Please use the TencentDB for DBbrain API [DescribeProxyProcessStatistics](https://intl.cloud.tencent.com/document/product/1130/84544?from_cn_redirect=1) to obtain the instance access source.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceMonitorSIP"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceMonitorSIPResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceMonitorTookDist(
            self,
            request: models.DescribeInstanceMonitorTookDistRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceMonitorTookDistResponse:
        """
        This API is used to query the time distribution of instance access.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceMonitorTookDist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceMonitorTookDistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceMonitorTopNCmd(
            self,
            request: models.DescribeInstanceMonitorTopNCmdRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceMonitorTopNCmdResponse:
        """
        This API is used to query instance access commands.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceMonitorTopNCmd"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceMonitorTopNCmdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceMonitorTopNCmdTook(
            self,
            request: models.DescribeInstanceMonitorTopNCmdTookRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceMonitorTopNCmdTookResponse:
        """
        This API is used to query the instance CPU time.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceMonitorTopNCmdTook"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceMonitorTopNCmdTookResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceNodeInfo(
            self,
            request: models.DescribeInstanceNodeInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceNodeInfoResponse:
        """
        This API is used to query the information of an instance node.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceNodeInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceNodeInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceParamRecords(
            self,
            request: models.DescribeInstanceParamRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceParamRecordsResponse:
        """
        This API is used to query the parameter modification record list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceParamRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceParamRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceParams(
            self,
            request: models.DescribeInstanceParamsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceParamsResponse:
        """
        This API is used to query the parameter list of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceParams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceParamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceSecurityGroup(
            self,
            request: models.DescribeInstanceSecurityGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceSecurityGroupResponse:
        """
        This API is used to query the security group information of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceSecurityGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceSecurityGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceShards(
            self,
            request: models.DescribeInstanceShardsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceShardsResponse:
        """
        This API is used to get the shard information of the instance on cluster architecture.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceShards"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceShardsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceSpecBandwidth(
            self,
            request: models.DescribeInstanceSpecBandwidthRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceSpecBandwidthResponse:
        """
        This API is used to query or calculate bandwidth specifications.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceSpecBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceSpecBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceSupportFeature(
            self,
            request: models.DescribeInstanceSupportFeatureRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceSupportFeatureResponse:
        """
        This API (DescribeInstanceSupportFeature) is used to query the supported features of the instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceSupportFeature"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceSupportFeatureResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceZoneInfo(
            self,
            request: models.DescribeInstanceZoneInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceZoneInfoResponse:
        """
        This API is used to query the details of a Redis node.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceZoneInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceZoneInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        This API is used to query the list of Redis instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMaintenanceWindow(
            self,
            request: models.DescribeMaintenanceWindowRequest,
            opts: Dict = None,
    ) -> models.DescribeMaintenanceWindowResponse:
        """
        This API is used to query the instance maintenance window. Instances that require the version or architecture upgrade will undergo time switching during the maintenance window.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMaintenanceWindow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMaintenanceWindowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeParamTemplateInfo(
            self,
            request: models.DescribeParamTemplateInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeParamTemplateInfoResponse:
        """
        This API is used to query the details of a parameter template.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeParamTemplateInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeParamTemplateInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeParamTemplates(
            self,
            request: models.DescribeParamTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeParamTemplatesResponse:
        """
        This API is used to query the parameter template list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeParamTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeParamTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProductInfo(
            self,
            request: models.DescribeProductInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeProductInfoResponse:
        """
        This API is used to query purchasable TencentDB for Redis specifications in all regions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProductInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjectSecurityGroup(
            self,
            request: models.DescribeProjectSecurityGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectSecurityGroupResponse:
        """
        This API is used to query project security group information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjectSecurityGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectSecurityGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjectSecurityGroups(
            self,
            request: models.DescribeProjectSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectSecurityGroupsResponse:
        """
        This API is used to query the security group details of a project.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjectSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxySlowLog(
            self,
            request: models.DescribeProxySlowLogRequest,
            opts: Dict = None,
    ) -> models.DescribeProxySlowLogResponse:
        """
        This API is used to query the slow queries of the proxy.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxySlowLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxySlowLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRedisClusterOverview(
            self,
            request: models.DescribeRedisClusterOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeRedisClusterOverviewResponse:
        """
        This API is used to query the overview information of a dedicated Redis cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRedisClusterOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRedisClusterOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRedisClusters(
            self,
            request: models.DescribeRedisClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeRedisClustersResponse:
        """
        This API is used to query the list of dedicated Redis clusters.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRedisClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRedisClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReplicationGroup(
            self,
            request: models.DescribeReplicationGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeReplicationGroupResponse:
        """
        This API is used to query a replication group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReplicationGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReplicationGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReplicationGroupInstance(
            self,
            request: models.DescribeReplicationGroupInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeReplicationGroupInstanceResponse:
        """
        This API is used to query replication group information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReplicationGroupInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReplicationGroupInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSSLStatus(
            self,
            request: models.DescribeSSLStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeSSLStatusResponse:
        """
        This API is used to query the SSL authentication information of an instance, such as enablement status, configuration status, and certificate address.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSSLStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSSLStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecondLevelBackupInfo(
            self,
            request: models.DescribeSecondLevelBackupInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSecondLevelBackupInfoResponse:
        """
        This API is used to query second-level backup information for the instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecondLevelBackupInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecondLevelBackupInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowLog(
            self,
            request: models.DescribeSlowLogRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowLogResponse:
        """
        This API is used to query the records of slow query.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskInfo(
            self,
            request: models.DescribeTaskInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskInfoResponse:
        """
        This API is used to get the execution of a specified task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskList(
            self,
            request: models.DescribeTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskListResponse:
        """
        This API is used to query the task list data for the last 30 days.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTendisSlowLog(
            self,
            request: models.DescribeTendisSlowLogRequest,
            opts: Dict = None,
    ) -> models.DescribeTendisSlowLogResponse:
        """
        This API is used to query the slow query logs of a Tendis instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTendisSlowLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTendisSlowLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyPostpaidInstance(
            self,
            request: models.DestroyPostpaidInstanceRequest,
            opts: Dict = None,
    ) -> models.DestroyPostpaidInstanceResponse:
        """
        This API is used to terminate pay-as-you-go instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyPostpaidInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyPostpaidInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyPrepaidInstance(
            self,
            request: models.DestroyPrepaidInstanceRequest,
            opts: Dict = None,
    ) -> models.DestroyPrepaidInstanceResponse:
        """
        This API is used to return Redis instances with monthly subscription.
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyPrepaidInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyPrepaidInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableReplicaReadonly(
            self,
            request: models.DisableReplicaReadonlyRequest,
            opts: Dict = None,
    ) -> models.DisableReplicaReadonlyResponse:
        """
        This API is used to disable read/write separation.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableReplicaReadonly"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableReplicaReadonlyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateSecurityGroups(
            self,
            request: models.DisassociateSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DisassociateSecurityGroupsResponse:
        """
        This API is used to unbind security groups from instances in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableReplicaReadonly(
            self,
            request: models.EnableReplicaReadonlyRequest,
            opts: Dict = None,
    ) -> models.EnableReplicaReadonlyResponse:
        """
        This API is used to enable read/write separation.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableReplicaReadonly"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableReplicaReadonlyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceCreateInstance(
            self,
            request: models.InquiryPriceCreateInstanceRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceCreateInstanceResponse:
        """
        This API is used to query the price of new instances.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceCreateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceCreateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceUpgradeInstance(
            self,
            request: models.InquiryPriceUpgradeInstanceRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceUpgradeInstanceResponse:
        """
        This API is used to query the price for instance scale-out.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceUpgradeInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceUpgradeInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def KillMasterGroup(
            self,
            request: models.KillMasterGroupRequest,
            opts: Dict = None,
    ) -> models.KillMasterGroupResponse:
        """
        This API is used to simulate a fault.
        """
        
        kwargs = {}
        kwargs["action"] = "KillMasterGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.KillMasterGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ManualBackupInstance(
            self,
            request: models.ManualBackupInstanceRequest,
            opts: Dict = None,
    ) -> models.ManualBackupInstanceResponse:
        """
        This API is used to manually back up a Redis instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ManualBackupInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ManualBackupInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModfiyInstancePassword(
            self,
            request: models.ModfiyInstancePasswordRequest,
            opts: Dict = None,
    ) -> models.ModfiyInstancePasswordResponse:
        """
        This API is used to change the instance access password. Due to a spelling error in the original API name, it has been corrected to [ModifyInstancePassword](https://intl.cloud.tencent.com/document/product/239/111555?from_cn_redirect=1). It is recommended to use the corrected API.
        """
        
        kwargs = {}
        kwargs["action"] = "ModfiyInstancePassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModfiyInstancePasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAutoBackupConfig(
            self,
            request: models.ModifyAutoBackupConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyAutoBackupConfigResponse:
        """
        This API is used to set the configuration for an automatic backup.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAutoBackupConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAutoBackupConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBackupDownloadRestriction(
            self,
            request: models.ModifyBackupDownloadRestrictionRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupDownloadRestrictionResponse:
        """
        This API is used to modify the network information and address for downloading a backup file.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupDownloadRestriction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupDownloadRestrictionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConnectionConfig(
            self,
            request: models.ModifyConnectionConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyConnectionConfigResponse:
        """
        This API is used to modify the connection configuration of an instance, including the bandwidth and maximum number of connections.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConnectionConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConnectionConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceSecurityGroups(
            self,
            request: models.ModifyDBInstanceSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceSecurityGroupsResponse:
        """
        This API is used to modify the original security group list of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstance(
            self,
            request: models.ModifyInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceResponse:
        """
        This API is used to modify instance information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceAccount(
            self,
            request: models.ModifyInstanceAccountRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceAccountResponse:
        """
        This API is used to modify an instance account.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceAvailabilityZones(
            self,
            request: models.ModifyInstanceAvailabilityZonesRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceAvailabilityZonesResponse:
        """
        This API is used to change the availability zone of the instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceAvailabilityZones"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceAvailabilityZonesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceBackupMode(
            self,
            request: models.ModifyInstanceBackupModeRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceBackupModeResponse:
        """
        This API is used to modify the backup mode of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceBackupMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceBackupModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceEvent(
            self,
            request: models.ModifyInstanceEventRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceEventResponse:
        """
        This API is used to modify the operations event execution schedule of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceLogDelivery(
            self,
            request: models.ModifyInstanceLogDeliveryRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceLogDeliveryResponse:
        """
        This API is used to enable or disable the shipping of instance logs to CLS.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceLogDelivery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceLogDeliveryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceParams(
            self,
            request: models.ModifyInstanceParamsRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceParamsResponse:
        """
        This API is used to modify the parameter configuration of a Redis instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceParams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceParamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstancePassword(
            self,
            request: models.ModifyInstancePasswordRequest,
            opts: Dict = None,
    ) -> models.ModifyInstancePasswordResponse:
        """
        This API is used to change the instance access password.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstancePassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstancePasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceReadOnly(
            self,
            request: models.ModifyInstanceReadOnlyRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceReadOnlyResponse:
        """
        This API is used to set the instance input mode.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceReadOnly"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceReadOnlyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMaintenanceWindow(
            self,
            request: models.ModifyMaintenanceWindowRequest,
            opts: Dict = None,
    ) -> models.ModifyMaintenanceWindowResponse:
        """
        This API is used to modify the time of instance maintenance window. Instances that require the version or architecture upgrade will undergo time switching during the maintenance window. Note: If the version or architecture upgrade has been initiated for an instance, its maintenance window cannot be modified.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMaintenanceWindow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMaintenanceWindowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNetworkConfig(
            self,
            request: models.ModifyNetworkConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyNetworkConfigResponse:
        """
        This API is used to modify the network configuration of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNetworkConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNetworkConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyParamTemplate(
            self,
            request: models.ModifyParamTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyParamTemplateResponse:
        """
        This API is used to modify the parameter template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyParamTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyParamTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyReplicationGroup(
            self,
            request: models.ModifyReplicationGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyReplicationGroupResponse:
        """
        This API is used to modify replication group information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyReplicationGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyReplicationGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenSSL(
            self,
            request: models.OpenSSLRequest,
            opts: Dict = None,
    ) -> models.OpenSSLResponse:
        """
        This API is used to enable SSL encryption and authentication.
        """
        
        kwargs = {}
        kwargs["action"] = "OpenSSL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenSSLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseWanAddress(
            self,
            request: models.ReleaseWanAddressRequest,
            opts: Dict = None,
    ) -> models.ReleaseWanAddressResponse:
        """
        This API is used to disable public network access.
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseWanAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseWanAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveReplicationGroup(
            self,
            request: models.RemoveReplicationGroupRequest,
            opts: Dict = None,
    ) -> models.RemoveReplicationGroupResponse:
        """
        This API is used to delete a replication group.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveReplicationGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveReplicationGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveReplicationInstance(
            self,
            request: models.RemoveReplicationInstanceRequest,
            opts: Dict = None,
    ) -> models.RemoveReplicationInstanceResponse:
        """
        This API is used to remove instances from a replication group.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveReplicationInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveReplicationInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewInstance(
            self,
            request: models.RenewInstanceRequest,
            opts: Dict = None,
    ) -> models.RenewInstanceResponse:
        """
        This API is used to renew an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "RenewInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetPassword(
            self,
            request: models.ResetPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetPasswordResponse:
        """
        This API is used to reset the instance access password.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestoreInstance(
            self,
            request: models.RestoreInstanceRequest,
            opts: Dict = None,
    ) -> models.RestoreInstanceResponse:
        """
        This API is used to restore an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "RestoreInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestoreInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartupInstance(
            self,
            request: models.StartupInstanceRequest,
            opts: Dict = None,
    ) -> models.StartupInstanceResponse:
        """
        This API is used to deisolate instances.
        """
        
        kwargs = {}
        kwargs["action"] = "StartupInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartupInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchAccessNewInstance(
            self,
            request: models.SwitchAccessNewInstanceRequest,
            opts: Dict = None,
    ) -> models.SwitchAccessNewInstanceResponse:
        """
        This API is used to immediately switch instances that are in the time window pending switch operation. Users can manually initiate this operation.
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchAccessNewInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchAccessNewInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchInstanceVip(
            self,
            request: models.SwitchInstanceVipRequest,
            opts: Dict = None,
    ) -> models.SwitchInstanceVipResponse:
        """
        This API is used to swap the VIPs of instances for disaster recovery in DTS-based cross-AZ disaster recovery scenarios. After the swapping, the target instance becomes writable, the VIPs of the source and target instances are swapped, and the DTS synchronization task between the source and target instances is disconnected.
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchInstanceVip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchInstanceVipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchProxy(
            self,
            request: models.SwitchProxyRequest,
            opts: Dict = None,
    ) -> models.SwitchProxyResponse:
        """
        This API is used to simulate the fault of a Proxy node.
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeInstance(
            self,
            request: models.UpgradeInstanceRequest,
            opts: Dict = None,
    ) -> models.UpgradeInstanceResponse:
        """
        This API is used to change the configuration specifications of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeInstanceVersion(
            self,
            request: models.UpgradeInstanceVersionRequest,
            opts: Dict = None,
    ) -> models.UpgradeInstanceVersionResponse:
        """
        This API is used to upgrade the current instance to a later version or upgrade the current standard architecture to a cluster architecture.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeInstanceVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeInstanceVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeProxyVersion(
            self,
            request: models.UpgradeProxyVersionRequest,
            opts: Dict = None,
    ) -> models.UpgradeProxyVersionResponse:
        """
        This API is used to upgrade the instance Proxy version.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeProxyVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeProxyVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeSmallVersion(
            self,
            request: models.UpgradeSmallVersionRequest,
            opts: Dict = None,
    ) -> models.UpgradeSmallVersionResponse:
        """
        This API is used to upgrade the minor version of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeSmallVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeSmallVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeVersionToMultiAvailabilityZones(
            self,
            request: models.UpgradeVersionToMultiAvailabilityZonesRequest,
            opts: Dict = None,
    ) -> models.UpgradeVersionToMultiAvailabilityZonesResponse:
        """
        This API is used to upgrade an instance to support multiple AZs.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeVersionToMultiAvailabilityZones"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeVersionToMultiAvailabilityZonesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)