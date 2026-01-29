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
from tencentcloud.csip.v20221121 import models
from typing import Dict


class CsipClient(AbstractClient):
    _apiVersion = '2022-11-21'
    _endpoint = 'csip.intl.tencentcloudapi.com'
    _service = 'csip'

    async def AddNewBindRoleUser(
            self,
            request: models.AddNewBindRoleUserRequest,
            opts: Dict = None,
    ) -> models.AddNewBindRoleUserResponse:
        """
        This API is used to add the CAM role of Cloud Security Center (CSC) to the current account. The name of the CAM role is "csip".
        """
        
        kwargs = {}
        kwargs["action"] = "AddNewBindRoleUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddNewBindRoleUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccessKeyCheckTask(
            self,
            request: models.CreateAccessKeyCheckTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAccessKeyCheckTaskResponse:
        """
        Detect AK async task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccessKeyCheckTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccessKeyCheckTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccessKeySyncTask(
            self,
            request: models.CreateAccessKeySyncTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAccessKeySyncTaskResponse:
        """
        Trigger an AK asset sync task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccessKeySyncTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccessKeySyncTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDomainAndIp(
            self,
            request: models.CreateDomainAndIpRequest,
            opts: Dict = None,
    ) -> models.CreateDomainAndIpResponse:
        """
        This API is used to create an asset with the specific domain/IP.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDomainAndIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDomainAndIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRiskCenterScanTask(
            self,
            request: models.CreateRiskCenterScanTaskRequest,
            opts: Dict = None,
    ) -> models.CreateRiskCenterScanTaskResponse:
        """
        This API is used to create a risk scan task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRiskCenterScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRiskCenterScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDomainAndIp(
            self,
            request: models.DeleteDomainAndIpRequest,
            opts: Dict = None,
    ) -> models.DeleteDomainAndIpResponse:
        """
        This API is used to delete assets.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDomainAndIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDomainAndIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRiskScanTask(
            self,
            request: models.DeleteRiskScanTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteRiskScanTaskResponse:
        """
        This API is used to delete a risk scan task.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRiskScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRiskScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAbnormalCallRecord(
            self,
            request: models.DescribeAbnormalCallRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeAbnormalCallRecordResponse:
        """
        Retrieve the call record list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAbnormalCallRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAbnormalCallRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessKeyAlarm(
            self,
            request: models.DescribeAccessKeyAlarmRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessKeyAlarmResponse:
        """
        List of alarm records for access keys.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessKeyAlarm"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessKeyAlarmResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessKeyAlarmDetail(
            self,
            request: models.DescribeAccessKeyAlarmDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessKeyAlarmDetailResponse:
        """
        Alarm Record Details for Access Key.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessKeyAlarmDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessKeyAlarmDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessKeyAsset(
            self,
            request: models.DescribeAccessKeyAssetRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessKeyAssetResponse:
        """
        Obtain user access key asset list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessKeyAsset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessKeyAssetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessKeyRisk(
            self,
            request: models.DescribeAccessKeyRiskRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessKeyRiskResponse:
        """
        Access key risk record list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessKeyRisk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessKeyRiskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessKeyRiskDetail(
            self,
            request: models.DescribeAccessKeyRiskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessKeyRiskDetailResponse:
        """
        Access Key Risk Record Details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessKeyRiskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessKeyRiskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessKeyUserDetail(
            self,
            request: models.DescribeAccessKeyUserDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessKeyUserDetailResponse:
        """
        Query the user's account details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessKeyUserDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessKeyUserDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessKeyUserList(
            self,
            request: models.DescribeAccessKeyUserListRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessKeyUserListResponse:
        """
        Query the account list of a user.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessKeyUserList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessKeyUserListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetProcessList(
            self,
            request: models.DescribeAssetProcessListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetProcessListResponse:
        """
        Query the process list of host nodes under the exposed path in cloud boundary analysis.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetProcessList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetProcessListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCFWAssetStatistics(
            self,
            request: models.DescribeCFWAssetStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeCFWAssetStatisticsResponse:
        """
        Cloud Defense Asset Center Statistics
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCFWAssetStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCFWAssetStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCSIPRiskStatistics(
            self,
            request: models.DescribeCSIPRiskStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeCSIPRiskStatisticsResponse:
        """
        Obtain risk center risk overview example.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCSIPRiskStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCSIPRiskStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCVMAssetInfo(
            self,
            request: models.DescribeCVMAssetInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeCVMAssetInfoResponse:
        """
        This API is used to query details of CVM assets.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCVMAssetInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCVMAssetInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCVMAssets(
            self,
            request: models.DescribeCVMAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeCVMAssetsResponse:
        """
        This API is used to query the list of CVM assets.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCVMAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCVMAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCallRecord(
            self,
            request: models.DescribeCallRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeCallRecordResponse:
        """
        Retrieve the call record list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCallRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCallRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterAssets(
            self,
            request: models.DescribeClusterAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterAssetsResponse:
        """
        This example shows you how to obtain the cluster list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterPodAssets(
            self,
            request: models.DescribeClusterPodAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterPodAssetsResponse:
        """
        This API is used to list cluster pods.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterPodAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterPodAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDbAssetInfo(
            self,
            request: models.DescribeDbAssetInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDbAssetInfoResponse:
        """
        This API is used to query details of a database asset.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDbAssetInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDbAssetInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDbAssets(
            self,
            request: models.DescribeDbAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeDbAssetsResponse:
        """
        This API is used to list database assets.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDbAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDbAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainAssets(
            self,
            request: models.DescribeDomainAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainAssetsResponse:
        """
        This API is used to list domain assets.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExposeAssetCategory(
            self,
            request: models.DescribeExposeAssetCategoryRequest,
            opts: Dict = None,
    ) -> models.DescribeExposeAssetCategoryResponse:
        """
        Cloud boundary analysis asset category.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExposeAssetCategory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExposeAssetCategoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExposePath(
            self,
            request: models.DescribeExposePathRequest,
            opts: Dict = None,
    ) -> models.DescribeExposePathResponse:
        """
        Query the node of the cloud boundary analysis path.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExposePath"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExposePathResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExposures(
            self,
            request: models.DescribeExposuresRequest,
            opts: Dict = None,
    ) -> models.DescribeExposuresResponse:
        """
        Cloud Boundary Analysis Asset List.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExposures"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExposuresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGatewayAssets(
            self,
            request: models.DescribeGatewayAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeGatewayAssetsResponse:
        """
        Obtain Gateway List
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGatewayAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGatewayAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHighBaseLineRiskList(
            self,
            request: models.DescribeHighBaseLineRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeHighBaseLineRiskListResponse:
        """
        Query the high-risk baseline risk list of host nodes under the exposed path in cloud boundary analysis.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHighBaseLineRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHighBaseLineRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListenerList(
            self,
            request: models.DescribeListenerListRequest,
            opts: Dict = None,
    ) -> models.DescribeListenerListResponse:
        """
        This API is used to query the list of TCP listeners.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListenerList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListenerListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNICAssets(
            self,
            request: models.DescribeNICAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeNICAssetsResponse:
        """
        Obtain Network Interface Card List
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNICAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNICAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganizationInfo(
            self,
            request: models.DescribeOrganizationInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationInfoResponse:
        """
        Check group account details
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganizationInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganizationInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganizationUserInfo(
            self,
            request: models.DescribeOrganizationUserInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationUserInfoResponse:
        """
        Query group account user list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganizationUserInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganizationUserInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOtherCloudAssets(
            self,
            request: models.DescribeOtherCloudAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeOtherCloudAssetsResponse:
        """
        Asset list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOtherCloudAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOtherCloudAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublicIpAssets(
            self,
            request: models.DescribePublicIpAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribePublicIpAssetsResponse:
        """
        This API is used to query the list of public IP assets.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublicIpAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublicIpAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRepositoryImageAssets(
            self,
            request: models.DescribeRepositoryImageAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeRepositoryImageAssetsResponse:
        """
        Repository Image List
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRepositoryImageAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRepositoryImageAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskCenterAssetViewCFGRiskList(
            self,
            request: models.DescribeRiskCenterAssetViewCFGRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskCenterAssetViewCFGRiskListResponse:
        """
        This API is used to query the list of configuration risks by assets.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskCenterAssetViewCFGRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskCenterAssetViewCFGRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskCenterAssetViewPortRiskList(
            self,
            request: models.DescribeRiskCenterAssetViewPortRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskCenterAssetViewPortRiskListResponse:
        """
        This API is used to query the list of port risks by assets.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskCenterAssetViewPortRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskCenterAssetViewPortRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskCenterAssetViewVULRiskList(
            self,
            request: models.DescribeRiskCenterAssetViewVULRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskCenterAssetViewVULRiskListResponse:
        """
        This API is used to query the list of vulnerabilities by assets.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskCenterAssetViewVULRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskCenterAssetViewVULRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskCenterAssetViewWeakPasswordRiskList(
            self,
            request: models.DescribeRiskCenterAssetViewWeakPasswordRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskCenterAssetViewWeakPasswordRiskListResponse:
        """
        This API is used to query the list of weak passwords by assets.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskCenterAssetViewWeakPasswordRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskCenterAssetViewWeakPasswordRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskCenterCFGViewCFGRiskList(
            self,
            request: models.DescribeRiskCenterCFGViewCFGRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskCenterCFGViewCFGRiskListResponse:
        """
        Obtain Configuration Risk List from Configuration's Perspective
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskCenterCFGViewCFGRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskCenterCFGViewCFGRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskCenterPortViewPortRiskList(
            self,
            request: models.DescribeRiskCenterPortViewPortRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskCenterPortViewPortRiskListResponse:
        """
        This API is used to query the list of port risks by ports.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskCenterPortViewPortRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskCenterPortViewPortRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskCenterServerRiskList(
            self,
            request: models.DescribeRiskCenterServerRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskCenterServerRiskListResponse:
        """
        This API is used to query the list of services in risk.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskCenterServerRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskCenterServerRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskCenterVULViewVULRiskList(
            self,
            request: models.DescribeRiskCenterVULViewVULRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskCenterVULViewVULRiskListResponse:
        """
        This API is used to query the list of vulnerabilities by vulnerabilities.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskCenterVULViewVULRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskCenterVULViewVULRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskCenterWebsiteRiskList(
            self,
            request: models.DescribeRiskCenterWebsiteRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskCenterWebsiteRiskListResponse:
        """
        This API is used to get the list of content risks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskCenterWebsiteRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskCenterWebsiteRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanReportList(
            self,
            request: models.DescribeScanReportListRequest,
            opts: Dict = None,
    ) -> models.DescribeScanReportListResponse:
        """
        This API is used to get the list of scan reports.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanReportList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanReportListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanStatistic(
            self,
            request: models.DescribeScanStatisticRequest,
            opts: Dict = None,
    ) -> models.DescribeScanStatisticResponse:
        """
        Query the statistical information of cloud boundary analysis scanning results.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanStatistic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanStatisticResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanTaskList(
            self,
            request: models.DescribeScanTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeScanTaskListResponse:
        """
        This API is used to get the list of scan tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSearchBugInfo(
            self,
            request: models.DescribeSearchBugInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSearchBugInfoResponse:
        """
        This API is used to query information of a vulnerability.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSearchBugInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSearchBugInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSourceIPAsset(
            self,
            request: models.DescribeSourceIPAssetRequest,
            opts: Dict = None,
    ) -> models.DescribeSourceIPAssetResponse:
        """
        This API is used to obtain user access key asset list (source IP perspective).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSourceIPAsset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSourceIPAssetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubUserInfo(
            self,
            request: models.DescribeSubUserInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSubUserInfoResponse:
        """
        Query the group's sub-account list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubUserInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubUserInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubnetAssets(
            self,
            request: models.DescribeSubnetAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeSubnetAssetsResponse:
        """
        This API is used to get the list of subnets.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubnetAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubnetAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskLogList(
            self,
            request: models.DescribeTaskLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskLogListResponse:
        """
        This API is used to get the list of scan task reports.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskLogURL(
            self,
            request: models.DescribeTaskLogURLRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskLogURLResponse:
        """
        This API is used to get the temp download link of a report.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskLogURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskLogURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserCallRecord(
            self,
            request: models.DescribeUserCallRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeUserCallRecordResponse:
        """
        Obtain account call record list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserCallRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserCallRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVULList(
            self,
            request: models.DescribeVULListRequest,
            opts: Dict = None,
    ) -> models.DescribeVULListResponse:
        """
        Security Center Risk Center - List of Vulnerabilities.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVULList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVULListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVULRiskAdvanceCFGList(
            self,
            request: models.DescribeVULRiskAdvanceCFGListRequest,
            opts: Dict = None,
    ) -> models.DescribeVULRiskAdvanceCFGListResponse:
        """
        This API is used to query the advanced configuration of vulnerability scan.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVULRiskAdvanceCFGList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVULRiskAdvanceCFGListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVULRiskDetail(
            self,
            request: models.DescribeVULRiskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeVULRiskDetailResponse:
        """
        Retrieve vulnerability details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVULRiskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVULRiskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcAssets(
            self,
            request: models.DescribeVpcAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcAssetsResponse:
        """
        This API is used to get the list of VPCs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulRiskList(
            self,
            request: models.DescribeVulRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulRiskListResponse:
        """
        Query the list of vulnerabilities of host nodes under the exposed path in cloud boundary analysis.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulViewVulRiskList(
            self,
            request: models.DescribeVulViewVulRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulViewVulRiskListResponse:
        """
        Obtain Vulnerability Risk List from Vulnerability's Perspective
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulViewVulRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulViewVulRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOrganizationAccountStatus(
            self,
            request: models.ModifyOrganizationAccountStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyOrganizationAccountStatusResponse:
        """
        Modify Group Account Status
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOrganizationAccountStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOrganizationAccountStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRiskCenterRiskStatus(
            self,
            request: models.ModifyRiskCenterRiskStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyRiskCenterRiskStatusResponse:
        """
        This API is used to modify the status of a risk.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRiskCenterRiskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRiskCenterRiskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRiskCenterScanTask(
            self,
            request: models.ModifyRiskCenterScanTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyRiskCenterScanTaskResponse:
        """
        Modify Risk Center Scan Task
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRiskCenterScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRiskCenterScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopRiskCenterTask(
            self,
            request: models.StopRiskCenterTaskRequest,
            opts: Dict = None,
    ) -> models.StopRiskCenterTaskResponse:
        """
        This API is used to stop a scan task.
        """
        
        kwargs = {}
        kwargs["action"] = "StopRiskCenterTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopRiskCenterTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAccessKeyAlarmStatus(
            self,
            request: models.UpdateAccessKeyAlarmStatusRequest,
            opts: Dict = None,
    ) -> models.UpdateAccessKeyAlarmStatusResponse:
        """
        Tag the risk or Alarm as processed/ignored.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAccessKeyAlarmStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAccessKeyAlarmStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAccessKeyRemark(
            self,
            request: models.UpdateAccessKeyRemarkRequest,
            opts: Dict = None,
    ) -> models.UpdateAccessKeyRemarkResponse:
        """
        Edit access key/Source IP remark.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAccessKeyRemark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAccessKeyRemarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)