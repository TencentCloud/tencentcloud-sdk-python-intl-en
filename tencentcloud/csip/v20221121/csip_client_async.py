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

    async def AccessAIAnalysisSMTP(
            self,
            request: models.AccessAIAnalysisSMTPRequest,
            opts: Dict = None,
    ) -> models.AccessAIAnalysisSMTPResponse:
        """
        This API is used to create or modify SMTP mailbox access requests.
        """
        
        kwargs = {}
        kwargs["action"] = "AccessAIAnalysisSMTP"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AccessAIAnalysisSMTPResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddDspmAssetManager(
            self,
            request: models.AddDspmAssetManagerRequest,
            opts: Dict = None,
    ) -> models.AddDspmAssetManagerResponse:
        """
        Add asset administrator
        """
        
        kwargs = {}
        kwargs["action"] = "AddDspmAssetManager"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddDspmAssetManagerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddImageRegistry(
            self,
            request: models.AddImageRegistryRequest,
            opts: Dict = None,
    ) -> models.AddImageRegistryResponse:
        """
        Add mirror repository information.
        """
        
        kwargs = {}
        kwargs["action"] = "AddImageRegistry"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddImageRegistryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddLoginWhiteLists(
            self,
            request: models.AddLoginWhiteListsRequest,
            opts: Dict = None,
    ) -> models.AddLoginWhiteListsResponse:
        """
        This API is used to add cross-region log-in allowlists in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "AddLoginWhiteLists"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddLoginWhiteListsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddNewBindRoleUser(
            self,
            request: models.AddNewBindRoleUserRequest,
            opts: Dict = None,
    ) -> models.AddNewBindRoleUserResponse:
        """
        CSIP Role Authorization Binding API
        """
        
        kwargs = {}
        kwargs["action"] = "AddNewBindRoleUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddNewBindRoleUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddVulWhitelist(
            self,
            request: models.AddVulWhitelistRequest,
            opts: Dict = None,
    ) -> models.AddVulWhitelistResponse:
        """
        Add a vulnerability allowlist
        """
        
        kwargs = {}
        kwargs["action"] = "AddVulWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddVulWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchModifyBaselinePolicy(
            self,
            request: models.BatchModifyBaselinePolicyRequest,
            opts: Dict = None,
    ) -> models.BatchModifyBaselinePolicyResponse:
        """
        Batch modify the "periodic scan configuration / automatic synchronization of newly-added detection items / detection item hit configuration / customized detection items" settings in the baseline policy. Only fields passed in the request are modified.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchModifyBaselinePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchModifyBaselinePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchModifyImageRegistryTimedScanTaskConfig(
            self,
            request: models.BatchModifyImageRegistryTimedScanTaskConfigRequest,
            opts: Dict = None,
    ) -> models.BatchModifyImageRegistryTimedScanTaskConfigResponse:
        """
        Batch modify the scheduled scan task configurations of image repositories.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchModifyImageRegistryTimedScanTaskConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchModifyImageRegistryTimedScanTaskConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchModifyImageSensitiveWhitelist(
            self,
            request: models.BatchModifyImageSensitiveWhitelistRequest,
            opts: Dict = None,
    ) -> models.BatchModifyImageSensitiveWhitelistResponse:
        """
        Batch Modify Sensitive Information Allowlist for Container Images
        """
        
        kwargs = {}
        kwargs["action"] = "BatchModifyImageSensitiveWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchModifyImageSensitiveWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchModifyImageVirusWhitelist(
            self,
            request: models.BatchModifyImageVirusWhitelistRequest,
            opts: Dict = None,
    ) -> models.BatchModifyImageVirusWhitelistResponse:
        """
        Batch modify the Trojan allowlist for images.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchModifyImageVirusWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchModifyImageVirusWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchModifyImageVulWhitelist(
            self,
            request: models.BatchModifyImageVulWhitelistRequest,
            opts: Dict = None,
    ) -> models.BatchModifyImageVulWhitelistResponse:
        """
        Batch Modify Vulnerability Allowlist for Container Images
        """
        
        kwargs = {}
        kwargs["action"] = "BatchModifyImageVulWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchModifyImageVulWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelEdrAlertIgnore(
            self,
            request: models.CancelEdrAlertIgnoreRequest,
            opts: Dict = None,
    ) -> models.CancelEdrAlertIgnoreResponse:
        """
        Cancel a permanently ignored EDR multi-behavior alarm. Remove the corresponding host and rule record from the AI-Link permanent ignore allowlist and restore the alarm status to PENDING.
        """
        
        kwargs = {}
        kwargs["action"] = "CancelEdrAlertIgnore"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelEdrAlertIgnoreResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckCWPExposePathPermission(
            self,
            request: models.CheckCWPExposePathPermissionRequest,
            opts: Dict = None,
    ) -> models.CheckCWPExposePathPermissionResponse:
        """
        Determine whether the current user is on the flagship edition for hosts.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckCWPExposePathPermission"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckCWPExposePathPermissionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckImageRegistryInstanceNameDuplicate(
            self,
            request: models.CheckImageRegistryInstanceNameDuplicateRequest,
            opts: Dict = None,
    ) -> models.CheckImageRegistryInstanceNameDuplicateResponse:
        """
        Check whether the image repository instance name is duplicate.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckImageRegistryInstanceNameDuplicate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckImageRegistryInstanceNameDuplicateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckIsUltimateVersion(
            self,
            request: models.CheckIsUltimateVersionRequest,
            opts: Dict = None,
    ) -> models.CheckIsUltimateVersionResponse:
        """
        Determine whether the current user is on the flagship edition.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckIsUltimateVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckIsUltimateVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckRisk(
            self,
            request: models.CheckRiskRequest,
            opts: Dict = None,
    ) -> models.CheckRiskResponse:
        """
        Risk verification example
        """
        
        kwargs = {}
        kwargs["action"] = "CheckRisk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckRiskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CopyBaselinePolicy(
            self,
            request: models.CopyBaselinePolicyRequest,
            opts: Dict = None,
    ) -> models.CopyBaselinePolicyResponse:
        """
        Replicate a custom baseline policy.
        """
        
        kwargs = {}
        kwargs["action"] = "CopyBaselinePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CopyBaselinePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAISchedule(
            self,
            request: models.CreateAIScheduleRequest,
            opts: Dict = None,
    ) -> models.CreateAIScheduleResponse:
        """
        Create an AI scheduled task.

        Create an AI scheduled task by entering the task name, prompt content, and trigger configuration. The AI scheduled task ID will be returned after successful creation.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAISchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAIScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccessKeyCheckTask(
            self,
            request: models.CreateAccessKeyCheckTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAccessKeyCheckTaskResponse:
        """
        Detect async tasks of AK
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
        
    async def CreateAllAssetsExportJob(
            self,
            request: models.CreateAllAssetsExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateAllAssetsExportJobResponse:
        """
        Creates a task to export all assets.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAllAssetsExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAllAssetsExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAssetComponentListExportJob(
            self,
            request: models.CreateAssetComponentListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateAssetComponentListExportJobResponse:
        """
        Creates a component list export task for image assets.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAssetComponentListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssetComponentListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAssetComponentRelatedImageListExportJob(
            self,
            request: models.CreateAssetComponentRelatedImageListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateAssetComponentRelatedImageListExportJobResponse:
        """
        Create a mirror repository component associated image list export task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAssetComponentRelatedImageListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssetComponentRelatedImageListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAssetFilterView(
            self,
            request: models.CreateAssetFilterViewRequest,
            opts: Dict = None,
    ) -> models.CreateAssetFilterViewResponse:
        """
        Create an asset search view.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAssetFilterView"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssetFilterViewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAssetProcessExportJob(
            self,
            request: models.CreateAssetProcessExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateAssetProcessExportJobResponse:
        """
        Create a host process list export task
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAssetProcessExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssetProcessExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAssetSyncTask(
            self,
            request: models.CreateAssetSyncTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAssetSyncTaskResponse:
        """
        This API is used to create an asset sync task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAssetSyncTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssetSyncTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAssetTag(
            self,
            request: models.CreateAssetTagRequest,
            opts: Dict = None,
    ) -> models.CreateAssetTagResponse:
        """
        Create an asset tag.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAssetTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssetTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAssetViewRisksExportJob(
            self,
            request: models.CreateAssetViewRisksExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateAssetViewRisksExportJobResponse:
        """
        Create a sample risk list export task from the asset perspective
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAssetViewRisksExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssetViewRisksExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBaselineAggregatedItemExportJob(
            self,
            request: models.CreateBaselineAggregatedItemExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateBaselineAggregatedItemExportJobResponse:
        """
        Create a baseline aggregation detection item export task. Use ExportType to select exporting statistics or risk details. You can limit the range by conditions such as policy and category. The task executes asynchronously in the backend. Once completed, you can download the result file from the export task list.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBaselineAggregatedItemExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBaselineAggregatedItemExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBaselineFixRecordExportJob(
            self,
            request: models.CreateBaselineFixRecordExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateBaselineFixRecordExportJobResponse:
        """
        This API is used to create a baseline fix record export task to export the records of fixed detection items, including detection item information, asset information, and repair time. The task executes asynchronously in the backend. Once completed, the result file can be downloaded from the export task list.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBaselineFixRecordExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBaselineFixRecordExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBaselineMainTaskExportJob(
            self,
            request: models.CreateBaselineMainTaskExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateBaselineMainTaskExportJobResponse:
        """
        Create a baseline main task export task to export detection items and subtask data under the specified main task. The task executes asynchronously in the backend. Once completed, the result file can be downloaded in the export task list.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBaselineMainTaskExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBaselineMainTaskExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCFGRiskPDFReportExportJob(
            self,
            request: models.CreateCFGRiskPDFReportExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateCFGRiskPDFReportExportJobResponse:
        """
        Example of creating an export task for a cloud resource configuration detection PDF report.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCFGRiskPDFReportExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCFGRiskPDFReportExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCFGRisksExportJob(
            self,
            request: models.CreateCFGRisksExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateCFGRisksExportJobResponse:
        """
        Example of creating an asset perspective risk list export task
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCFGRisksExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCFGRisksExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCSIPManualMalwareScan(
            self,
            request: models.CreateCSIPManualMalwareScanRequest,
            opts: Dict = None,
    ) -> models.CreateCSIPManualMalwareScanResponse:
        """
        This API is used to create a CSIP manual scan.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCSIPManualMalwareScan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCSIPManualMalwareScanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCheckViewRisksExportJob(
            self,
            request: models.CreateCheckViewRisksExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateCheckViewRisksExportJobResponse:
        """
        Create a sample risk list export task from the asset perspective
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCheckViewRisksExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCheckViewRisksExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudFunctionExportJob(
            self,
            request: models.CreateCloudFunctionExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateCloudFunctionExportJobResponse:
        """
        This API is used to create an SCF export task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudFunctionExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudFunctionExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterAssetSyncTask(
            self,
            request: models.CreateClusterAssetSyncTaskRequest,
            opts: Dict = None,
    ) -> models.CreateClusterAssetSyncTaskResponse:
        """
        This API is used to create a cluster asset sync task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterAssetSyncTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterAssetSyncTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterContainerListExportJob(
            self,
            request: models.CreateClusterContainerListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateClusterContainerListExportJobResponse:
        """
        Creates a cluster container list export task
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterContainerListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterContainerListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterListExportJob(
            self,
            request: models.CreateClusterListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateClusterListExportJobResponse:
        """
        Create a cluster list export task
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterNamespaceListExportJob(
            self,
            request: models.CreateClusterNamespaceListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateClusterNamespaceListExportJobResponse:
        """
        Creates a cluster namespace list export task. The export fields include namespace name, Labels, and creation time. Filter filtering is supported. Export is implemented through an async task. After JobId is returned, the frontend polls to query the export task status.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterNamespaceListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterNamespaceListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterNodeListExportJob(
            self,
            request: models.CreateClusterNodeListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateClusterNodeListExportJobResponse:
        """
        This API is used to create a cluster node list export task. The export fields include node ID, node name, public IP address, private IP address, node type, cores, client status, and running state. NodeType, ClientStatus, and RunStatus are internationalized. Filter filtering is supported, including ClientStatus memory filtering. Export is implemented through an async task. After JobId is returned, the frontend polls to query the export task status.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterNodeListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterNodeListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateComplianceRiskExportJob(
            self,
            request: models.CreateComplianceRiskExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateComplianceRiskExportJobResponse:
        """
        Example of creating a risk list export task from a compliance standard aggregation perspective
        """
        
        kwargs = {}
        kwargs["action"] = "CreateComplianceRiskExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateComplianceRiskExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDomainAndIp(
            self,
            request: models.CreateDomainAndIpRequest,
            opts: Dict = None,
    ) -> models.CreateDomainAndIpResponse:
        """
        Create Domain and IP Information
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDomainAndIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDomainAndIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmAccessExportJob(
            self,
            request: models.CreateDspmAccessExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateDspmAccessExportJobResponse:
        """
        Creates a Dspm access record export task
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmAccessExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmAccessExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmApplyOrder(
            self,
            request: models.CreateDspmApplyOrderRequest,
            opts: Dict = None,
    ) -> models.CreateDspmApplyOrderResponse:
        """
        This API is used to create a Dspm application.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmApplyOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmApplyOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmApproveHistoryExportJob(
            self,
            request: models.CreateDspmApproveHistoryExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateDspmApproveHistoryExportJobResponse:
        """
        Creates a Dspm approval history export task
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmApproveHistoryExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmApproveHistoryExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmAssetAccessTopologyExportJob(
            self,
            request: models.CreateDspmAssetAccessTopologyExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateDspmAssetAccessTopologyExportJobResponse:
        """
        This API is used to create a Dspm asset access topology export task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmAssetAccessTopologyExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmAssetAccessTopologyExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmAssetIdentifyInfoExportJob(
            self,
            request: models.CreateDspmAssetIdentifyInfoExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateDspmAssetIdentifyInfoExportJobResponse:
        """
        Create an asset list export task for Dspm.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmAssetIdentifyInfoExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmAssetIdentifyInfoExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmAssetsExportJob(
            self,
            request: models.CreateDspmAssetsExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateDspmAssetsExportJobResponse:
        """
        Creates a Dspm asset list export task
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmAssetsExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmAssetsExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmAuditFilterStrategy(
            self,
            request: models.CreateDspmAuditFilterStrategyRequest,
            opts: Dict = None,
    ) -> models.CreateDspmAuditFilterStrategyResponse:
        """
        This API is used to create a Dspm audit filter policy.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmAuditFilterStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmAuditFilterStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmExportTask(
            self,
            request: models.CreateDspmExportTaskRequest,
            opts: Dict = None,
    ) -> models.CreateDspmExportTaskResponse:
        """
        This API is used to create log export tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmExportTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmExportTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmIdentifyCategory(
            self,
            request: models.CreateDspmIdentifyCategoryRequest,
            opts: Dict = None,
    ) -> models.CreateDspmIdentifyCategoryResponse:
        """
        This API is used to create a dspm data identification category.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmIdentifyCategory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmIdentifyCategoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmIdentifyComplianceCategoryRelation(
            self,
            request: models.CreateDspmIdentifyComplianceCategoryRelationRequest,
            opts: Dict = None,
    ) -> models.CreateDspmIdentifyComplianceCategoryRelationResponse:
        """
        This API is used to create a dspm data identification template category association.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmIdentifyComplianceCategoryRelation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmIdentifyComplianceCategoryRelationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmIdentifyComplianceGroup(
            self,
            request: models.CreateDspmIdentifyComplianceGroupRequest,
            opts: Dict = None,
    ) -> models.CreateDspmIdentifyComplianceGroupResponse:
        """
        This API is used to create a dspm data identification template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmIdentifyComplianceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmIdentifyComplianceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmIdentifyComplianceGroupCopy(
            self,
            request: models.CreateDspmIdentifyComplianceGroupCopyRequest,
            opts: Dict = None,
    ) -> models.CreateDspmIdentifyComplianceGroupCopyResponse:
        """
        Replicate a dspm data identification template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmIdentifyComplianceGroupCopy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmIdentifyComplianceGroupCopyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmIdentifyComplianceRuleRelation(
            self,
            request: models.CreateDspmIdentifyComplianceRuleRelationRequest,
            opts: Dict = None,
    ) -> models.CreateDspmIdentifyComplianceRuleRelationResponse:
        """
        Creates a dspm data identification template data item association
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmIdentifyComplianceRuleRelation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmIdentifyComplianceRuleRelationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmIdentifyInfoListExportJob(
            self,
            request: models.CreateDspmIdentifyInfoListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateDspmIdentifyInfoListExportJobResponse:
        """
        This API is used to create a Dspm identity list export task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmIdentifyInfoListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmIdentifyInfoListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmIdentifyLevelGroup(
            self,
            request: models.CreateDspmIdentifyLevelGroupRequest,
            opts: Dict = None,
    ) -> models.CreateDspmIdentifyLevelGroupResponse:
        """
        Creating a dspm Data Identification and Classification Group
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmIdentifyLevelGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmIdentifyLevelGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmIdentifyRule(
            self,
            request: models.CreateDspmIdentifyRuleRequest,
            opts: Dict = None,
    ) -> models.CreateDspmIdentifyRuleResponse:
        """
        This API is used to create a dspm identification data item.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmIdentifyRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmIdentifyRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmPersonalIdentify(
            self,
            request: models.CreateDspmPersonalIdentifyRequest,
            opts: Dict = None,
    ) -> models.CreateDspmPersonalIdentifyResponse:
        """
        Create a Dspm personal identity id.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmPersonalIdentify"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmPersonalIdentifyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmResource(
            self,
            request: models.CreateDspmResourceRequest,
            opts: Dict = None,
    ) -> models.CreateDspmResourceResponse:
        """
        Create a Dspm instance
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmRiskExportJob(
            self,
            request: models.CreateDspmRiskExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateDspmRiskExportJobResponse:
        """
        Create a Dspm risk export task
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmRiskExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmRiskExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmRiskStrategy(
            self,
            request: models.CreateDspmRiskStrategyRequest,
            opts: Dict = None,
    ) -> models.CreateDspmRiskStrategyResponse:
        """
        This API is used to create a Dspm custom risk policy.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmRiskStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmRiskStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDspmWhitelistStrategy(
            self,
            request: models.CreateDspmWhitelistStrategyRequest,
            opts: Dict = None,
    ) -> models.CreateDspmWhitelistStrategyResponse:
        """
        Create a Dspm allowlist policy.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDspmWhitelistStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDspmWhitelistStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDynamicAssetsExportJob(
            self,
            request: models.CreateDynamicAssetsExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateDynamicAssetsExportJobResponse:
        """
        Creates a public network asset export task
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDynamicAssetsExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDynamicAssetsExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEDRManualScan(
            self,
            request: models.CreateEDRManualScanRequest,
            opts: Dict = None,
    ) -> models.CreateEDRManualScanResponse:
        """
        Triggered after you click start scanning. It supports multi-account and multiple asset types. When both hosts and container clusters are selected, it splits into two independent tasks (host + container).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEDRManualScan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEDRManualScanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEdrAlertExportJob(
            self,
            request: models.CreateEdrAlertExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateEdrAlertExportJobResponse:
        """
        This API is used to create an EDR alert export task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEdrAlertExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEdrAlertExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEdrLessAlertExportJob(
            self,
            request: models.CreateEdrLessAlertExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateEdrLessAlertExportJobResponse:
        """
        This API is used to create an EDR alert ordinary export task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEdrLessAlertExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEdrLessAlertExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateExposureAutoTagRule(
            self,
            request: models.CreateExposureAutoTagRuleRequest,
            opts: Dict = None,
    ) -> models.CreateExposureAutoTagRuleResponse:
        """
        Create rules for automatic cloud boundary tagging.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateExposureAutoTagRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateExposureAutoTagRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateExposuresExportJob(
            self,
            request: models.CreateExposuresExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateExposuresExportJobResponse:
        """
        Export Task for Exposed Assets
        """
        
        kwargs = {}
        kwargs["action"] = "CreateExposuresExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateExposuresExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHighBaseLineRisksExportJob(
            self,
            request: models.CreateHighBaseLineRisksExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateHighBaseLineRisksExportJobResponse:
        """
        This API is used to create a high-risk baseline risk export task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHighBaseLineRisksExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHighBaseLineRisksExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHostImageListExportJob(
            self,
            request: models.CreateHostImageListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateHostImageListExportJobResponse:
        """
        Create a local image list export task. The export fields include image ID, image name, mirror version, number of associated containers, number of associated hosts, creation time, account nickname, and risk fields such as scan status, vulnerability, Trojan, and sensitive information. Filtering is supported. Export is implemented through an async task. After JobId is returned, the frontend polls to query the export task status. In single account mode, the NickName field is automatically excluded.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHostImageListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHostImageListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHostVulExportJob(
            self,
            request: models.CreateHostVulExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateHostVulExportJobResponse:
        """
        This API is used to create a host vulnerability table export task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHostVulExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHostVulExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIaCAccessToken(
            self,
            request: models.CreateIaCAccessTokenRequest,
            opts: Dict = None,
    ) -> models.CreateIaCAccessTokenResponse:
        """
        Create an IaC detection integration Token.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIaCAccessToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIaCAccessTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIaCFileExportJob(
            self,
            request: models.CreateIaCFileExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateIaCFileExportJobResponse:
        """
        Creates an IaC detection file export task
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIaCFileExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIaCFileExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIaCFileReScanTask(
            self,
            request: models.CreateIaCFileReScanTaskRequest,
            opts: Dict = None,
    ) -> models.CreateIaCFileReScanTaskResponse:
        """
        This API is used to create an IaC detection file rescan task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIaCFileReScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIaCFileReScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImageAssetListExportJob(
            self,
            request: models.CreateImageAssetListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateImageAssetListExportJobResponse:
        """
        Create an image asset list export task
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImageAssetListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageAssetListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImageAssociatedContainerListExportJob(
            self,
            request: models.CreateImageAssociatedContainerListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateImageAssociatedContainerListExportJobResponse:
        """
        Create an image associated container asset export task
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImageAssociatedContainerListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageAssociatedContainerListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImageAssociatedHostListExportJob(
            self,
            request: models.CreateImageAssociatedHostListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateImageAssociatedHostListExportJobResponse:
        """
        Create image associated host asset list export task
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImageAssociatedHostListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageAssociatedHostListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImageComponentListExportJob(
            self,
            request: models.CreateImageComponentListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateImageComponentListExportJobResponse:
        """
        Create an image component list export task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImageComponentListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageComponentListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImageLayerVulListExportJob(
            self,
            request: models.CreateImageLayerVulListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateImageLayerVulListExportJobResponse:
        """
        Create Image Layer Vulnerability List Export Task
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImageLayerVulListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageLayerVulListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImageRegistryConnectivityTask(
            self,
            request: models.CreateImageRegistryConnectivityTaskRequest,
            opts: Dict = None,
    ) -> models.CreateImageRegistryConnectivityTaskResponse:
        """
        This API is used to create a mirror repository connectivity check task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImageRegistryConnectivityTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageRegistryConnectivityTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImageRegistryListExportJob(
            self,
            request: models.CreateImageRegistryListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateImageRegistryListExportJobResponse:
        """
        This API is used to create an image repository list export task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImageRegistryListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageRegistryListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImageRegistryScanTask(
            self,
            request: models.CreateImageRegistryScanTaskRequest,
            opts: Dict = None,
    ) -> models.CreateImageRegistryScanTaskResponse:
        """
        Creating an Image Scanning Task
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImageRegistryScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageRegistryScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImageRegistryTimedScanTaskConfig(
            self,
            request: models.CreateImageRegistryTimedScanTaskConfigRequest,
            opts: Dict = None,
    ) -> models.CreateImageRegistryTimedScanTaskConfigResponse:
        """
        Create an image scanning task configuration for an image repository
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImageRegistryTimedScanTaskConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageRegistryTimedScanTaskConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImageSensitiveInfoListExportJob(
            self,
            request: models.CreateImageSensitiveInfoListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateImageSensitiveInfoListExportJobResponse:
        """
        Create Image Sensitive Information List Export Task
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImageSensitiveInfoListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageSensitiveInfoListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImageSensitiveWhitelist(
            self,
            request: models.CreateImageSensitiveWhitelistRequest,
            opts: Dict = None,
    ) -> models.CreateImageSensitiveWhitelistResponse:
        """
        This API is used to create an allowlist for sensitive information in container images.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImageSensitiveWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageSensitiveWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImageVirusListExportJob(
            self,
            request: models.CreateImageVirusListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateImageVirusListExportJobResponse:
        """
        Create an image Trojan virus list export task
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImageVirusListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageVirusListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImageVirusWhitelist(
            self,
            request: models.CreateImageVirusWhitelistRequest,
            opts: Dict = None,
    ) -> models.CreateImageVirusWhitelistResponse:
        """
        This API is used to create an image Trojan allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImageVirusWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageVirusWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImageVulListExportJob(
            self,
            request: models.CreateImageVulListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateImageVulListExportJobResponse:
        """
        This API is used to create a task of exporting the image vulnerability list.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImageVulListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageVulListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImageVulSummaryListExportJob(
            self,
            request: models.CreateImageVulSummaryListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateImageVulSummaryListExportJobResponse:
        """
        Creates an export task for the vulnerability overview list of an image.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImageVulSummaryListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageVulSummaryListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImageVulWhitelist(
            self,
            request: models.CreateImageVulWhitelistRequest,
            opts: Dict = None,
    ) -> models.CreateImageVulWhitelistResponse:
        """
        This API is used to create a vulnerability allowlist for container images.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImageVulWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageVulWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePodContainerListExportJob(
            self,
            request: models.CreatePodContainerListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreatePodContainerListExportJobResponse:
        """
        This API is used to create a Pod associated container list export task. Export fields include container ID, container name, running state, node ID, node type, image ID, image name, and isolation status. Filtering is supported. Export is implemented through an async task. After JobId is returned, front-end polling is used to query the export task status.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePodContainerListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePodContainerListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePodServiceListExportJob(
            self,
            request: models.CreatePodServiceListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreatePodServiceListExportJobResponse:
        """
        Creates a Pod Association service list export task. The export fields include service name, type, Selector, namespace, and creation time. Filtering is supported. When PodUniqueID is input, the Pod Association matching logic of DescribeClusterServiceList is reused. Export is implemented through an async task, and after JobId is returned, the frontend polls to query the export task status.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePodServiceListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePodServiceListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePublicAssetsExportJob(
            self,
            request: models.CreatePublicAssetsExportJobRequest,
            opts: Dict = None,
    ) -> models.CreatePublicAssetsExportJobResponse:
        """
        This API is used to create a public network asset export task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePublicAssetsExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePublicAssetsExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRiskCenterScanTask(
            self,
            request: models.CreateRiskCenterScanTaskRequest,
            opts: Dict = None,
    ) -> models.CreateRiskCenterScanTaskResponse:
        """
        Create Risk Center Scan Task
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRiskCenterScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRiskCenterScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRiskDetailExportJob(
            self,
            request: models.CreateRiskDetailExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateRiskDetailExportJobResponse:
        """
        Sample code for creating a cloud resource configuration check risk details export task
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRiskDetailExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRiskDetailExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSandboxACLRule(
            self,
            request: models.CreateSandboxACLRuleRequest,
            opts: Dict = None,
    ) -> models.CreateSandboxACLRuleResponse:
        """
        This API is used to create an ACL user access control rule. You can refer to several system rules or define a custom rule. At least one of them must be provided.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSandboxACLRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSandboxACLRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSandboxDLPRule(
            self,
            request: models.CreateSandboxDLPRuleRequest,
            opts: Dict = None,
    ) -> models.CreateSandboxDLPRuleResponse:
        """
        Create a DLP user rule. You can reference several system rules (SystemRuleIDList) or define a custom rule (UserRuleContent, name + regular). At least one of both is required. UserRuleInfo is a newly-added optional structured input parameter. When it is passed together with UserRuleContent, UserRuleInfo takes precedence.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSandboxDLPRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSandboxDLPRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSandboxFileRule(
            self,
            request: models.CreateSandboxFileRuleRequest,
            opts: Dict = None,
    ) -> models.CreateSandboxFileRuleResponse:
        """
        Create command sandbox file access policy
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSandboxFileRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSandboxFileRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSandboxLLMAuditRule(
            self,
            request: models.CreateSandboxLLMAuditRuleRequest,
            opts: Dict = None,
    ) -> models.CreateSandboxLLMAuditRuleResponse:
        """
        This API is used to create an LLM audit user rule. It must refer to at least one system rule and does not support user customization of rule content.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSandboxLLMAuditRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSandboxLLMAuditRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateScanStatisticExportJob(
            self,
            request: models.CreateScanStatisticExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateScanStatisticExportJobResponse:
        """
        Exported task for exposed surface scanning results
        """
        
        kwargs = {}
        kwargs["action"] = "CreateScanStatisticExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateScanStatisticExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateScanTask(
            self,
            request: models.CreateScanTaskRequest,
            opts: Dict = None,
    ) -> models.CreateScanTaskResponse:
        """
        This API is used to create an immediate detection task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSkillScan(
            self,
            request: models.CreateSkillScanRequest,
            opts: Dict = None,
    ) -> models.CreateSkillScanResponse:
        """
        Upload a Skill ZIP file to trigger asynchronous security detection. After a successful upload, poll the DescribeSkillScanResult API using the returned ContentHash and EngineVersion to obtain the result. The upload API is idempotent. Re-uploading a file with the same Hash does not create a repetition task. Detection results are retained for 90 days. Re-upload for detection after the retention period expires.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSkillScan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSkillScanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulFixRetryTask(
            self,
            request: models.CreateVulFixRetryTaskRequest,
            opts: Dict = None,
    ) -> models.CreateVulFixRetryTaskResponse:
        """
        Retry the vulnerability repair task that failed to fix, and redispatch the repair instruction only for the hosts of the original task that failed to fix. Retry is allowed only when the task status is partially or totally failed to fix.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulFixRetryTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulFixRetryTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulFixTask(
            self,
            request: models.CreateVulFixTaskRequest,
            opts: Dict = None,
    ) -> models.CreateVulFixTaskResponse:
        """
        Users manually submit vulnerability repair tasks, specify the vulnerabilities and target hosts that need to be repaired, and the system creates fixing tasks and dispatches execution. It supports options such as specifying the repair timeout period and whether to create a snapshot. The FixItems array is used to precisely control which hosts each vulnerability or KB patch repairs.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulFixTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulFixTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulFixedExportJob(
            self,
            request: models.CreateVulFixedExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateVulFixedExportJobResponse:
        """
        Create an export task for the list of fixed vulnerabilities. It supports the same filter criteria as DescribeVulFixedList. The export is implemented via an asynchronous task. After a JobID is returned, the frontend polls to query the export task status. The export fields include vulnerability ID, vulnerability name, vulnerability level, VPR rating, vulnerability type, CVE ID, host name, instance ID, associated component & path, and repair time.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulFixedExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulFixedExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulReScan(
            self,
            request: models.CreateVulReScanRequest,
            opts: Dict = None,
    ) -> models.CreateVulReScanResponse:
        """
        This API is used to create a vulnerability rescan
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulReScan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulReScanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulRisksExportJob(
            self,
            request: models.CreateVulRisksExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateVulRisksExportJobResponse:
        """
        This API is used to create a vulnerability risk export task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulRisksExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulRisksExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulScanManual(
            self,
            request: models.CreateVulScanManualRequest,
            opts: Dict = None,
    ) -> models.CreateVulScanManualResponse:
        """
        This API is used to create a vulnerability scanning (one-click scan).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulScanManual"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulScanManualResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAIAnalysisSMTPAccess(
            self,
            request: models.DeleteAIAnalysisSMTPAccessRequest,
            opts: Dict = None,
    ) -> models.DeleteAIAnalysisSMTPAccessResponse:
        """
        Delete the SMTP mailbox access information of the AI assistant.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAIAnalysisSMTPAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAIAnalysisSMTPAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAISchedule(
            self,
            request: models.DeleteAIScheduleRequest,
            opts: Dict = None,
    ) -> models.DeleteAIScheduleResponse:
        """
        This API is used to delete AI scheduled tasks.

        This API is used to delete a scheduled task based on the specified AI scheduled task ID. Deletion is irreversible.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAISchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAIScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAssetFilterView(
            self,
            request: models.DeleteAssetFilterViewRequest,
            opts: Dict = None,
    ) -> models.DeleteAssetFilterViewResponse:
        """
        Delete the search view of a user-created specified asset
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAssetFilterView"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAssetFilterViewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAssetTag(
            self,
            request: models.DeleteAssetTagRequest,
            opts: Dict = None,
    ) -> models.DeleteAssetTagResponse:
        """
        Delete asset tag
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAssetTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAssetTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBaselineSelfDefinedPolicyList(
            self,
            request: models.DeleteBaselineSelfDefinedPolicyListRequest,
            opts: Dict = None,
    ) -> models.DeleteBaselineSelfDefinedPolicyListResponse:
        """
        Delete custom baseline policies in batches. Only support deletion of policies with PolicyType=SELF. After deletion, historical risk records are retained, but no new results are generated.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBaselineSelfDefinedPolicyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBaselineSelfDefinedPolicyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCSIPMalwareScanTask(
            self,
            request: models.DeleteCSIPMalwareScanTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteCSIPMalwareScanTaskResponse:
        """
        CSIP manual scan task delete API
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCSIPMalwareScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCSIPMalwareScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCluster(
            self,
            request: models.DeleteClusterRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterResponse:
        """
        Deleting a cluster
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDomainAndIp(
            self,
            request: models.DeleteDomainAndIpRequest,
            opts: Dict = None,
    ) -> models.DeleteDomainAndIpResponse:
        """
        Delete Domain and IP Request
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDomainAndIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDomainAndIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmApplyOrder(
            self,
            request: models.DeleteDspmApplyOrderRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmApplyOrderResponse:
        """
        Deletes a Dspm application form.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmApplyOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmApplyOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmAssetAccount(
            self,
            request: models.DeleteDspmAssetAccountRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmAssetAccountResponse:
        """
        Delete a Dspm asset account
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmAssetAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmAssetAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmAuditFilterStrategy(
            self,
            request: models.DeleteDspmAuditFilterStrategyRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmAuditFilterStrategyResponse:
        """
        Delete a Dspm audit filter policy
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmAuditFilterStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmAuditFilterStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmBackupLogList(
            self,
            request: models.DeleteDspmBackupLogListRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmBackupLogListResponse:
        """
        This API is used to delete the backup logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmBackupLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmBackupLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmCkafkaConfig(
            self,
            request: models.DeleteDspmCkafkaConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmCkafkaConfigResponse:
        """
        This API is used to cancel the log shipping configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmCkafkaConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmCkafkaConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmExportTask(
            self,
            request: models.DeleteDspmExportTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmExportTaskResponse:
        """
        This API is used to delete export tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmExportTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmExportTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmIdentifyCategory(
            self,
            request: models.DeleteDspmIdentifyCategoryRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmIdentifyCategoryResponse:
        """
        Delete dspm data identification category
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmIdentifyCategory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmIdentifyCategoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmIdentifyComplianceCategoryRelation(
            self,
            request: models.DeleteDspmIdentifyComplianceCategoryRelationRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmIdentifyComplianceCategoryRelationResponse:
        """
        Deletes classification association from a dspm identification template
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmIdentifyComplianceCategoryRelation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmIdentifyComplianceCategoryRelationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmIdentifyComplianceGroup(
            self,
            request: models.DeleteDspmIdentifyComplianceGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmIdentifyComplianceGroupResponse:
        """
        Delete dspm data identification template
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmIdentifyComplianceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmIdentifyComplianceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmIdentifyComplianceRuleRelation(
            self,
            request: models.DeleteDspmIdentifyComplianceRuleRelationRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmIdentifyComplianceRuleRelationResponse:
        """
        Delete dspm data identification template data item association
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmIdentifyComplianceRuleRelation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmIdentifyComplianceRuleRelationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmIdentifyLevelGroup(
            self,
            request: models.DeleteDspmIdentifyLevelGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmIdentifyLevelGroupResponse:
        """
        Delete a dspm data identification classification group
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmIdentifyLevelGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmIdentifyLevelGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmIdentifyRule(
            self,
            request: models.DeleteDspmIdentifyRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmIdentifyRuleResponse:
        """
        Delete dspm data identification data item
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmIdentifyRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmIdentifyRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmPersonalIdentify(
            self,
            request: models.DeleteDspmPersonalIdentifyRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmPersonalIdentifyResponse:
        """
        Delete a Dspm personal identity id.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmPersonalIdentify"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmPersonalIdentifyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmRestoreLogList(
            self,
            request: models.DeleteDspmRestoreLogListRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmRestoreLogListResponse:
        """
        Delete restore logs
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmRestoreLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmRestoreLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmRiskStrategy(
            self,
            request: models.DeleteDspmRiskStrategyRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmRiskStrategyResponse:
        """
        This API is used to delete a DSPM custom risk policy. It only supports deletion of custom policies with rule_source=custom. Built-in policies are non-deletable. Disable them by setting IsEnabled in ModifyDspmRiskStrategy.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmRiskStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmRiskStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmShareUserData(
            self,
            request: models.DeleteDspmShareUserDataRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmShareUserDataResponse:
        """
        Delete dspmg shared account data
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmShareUserData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmShareUserDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDspmWhitelistStrategy(
            self,
            request: models.DeleteDspmWhitelistStrategyRequest,
            opts: Dict = None,
    ) -> models.DeleteDspmWhitelistStrategyResponse:
        """
        Delete a Dspm allowlist policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDspmWhitelistStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDspmWhitelistStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEDRRules(
            self,
            request: models.DeleteEDRRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteEDRRulesResponse:
        """
        This API is used to delete EDR policies.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEDRRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEDRRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEDRScanTask(
            self,
            request: models.DeleteEDRScanTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteEDRScanTaskResponse:
        """
        This API is used to delete terminated scan tasks by physically deleting the primary and detailed tables. Only tasks in the final state can be deleted, and only the creator can perform the deletion.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEDRScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEDRScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEdrLogCollectPaths(
            self,
            request: models.DeleteEdrLogCollectPathsRequest,
            opts: Dict = None,
    ) -> models.DeleteEdrLogCollectPathsResponse:
        """
        Delete EDR log collection path configurations in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEdrLogCollectPaths"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEdrLogCollectPathsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteExposureAutoTagRule(
            self,
            request: models.DeleteExposureAutoTagRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteExposureAutoTagRuleResponse:
        """
        Delete rules for automatic cloud boundary tagging.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteExposureAutoTagRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteExposureAutoTagRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIaCAccessToken(
            self,
            request: models.DeleteIaCAccessTokenRequest,
            opts: Dict = None,
    ) -> models.DeleteIaCAccessTokenResponse:
        """
        Delete an IaC detection integration Token
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIaCAccessToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIaCAccessTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIaCFile(
            self,
            request: models.DeleteIaCFileRequest,
            opts: Dict = None,
    ) -> models.DeleteIaCFileResponse:
        """
        Delete an IaC detection file
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIaCFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIaCFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteImageRegistry(
            self,
            request: models.DeleteImageRegistryRequest,
            opts: Dict = None,
    ) -> models.DeleteImageRegistryResponse:
        """
        Delete image repository information.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteImageRegistry"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteImageRegistryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteImageRegistryScanTask(
            self,
            request: models.DeleteImageRegistryScanTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteImageRegistryScanTaskResponse:
        """
        Deletes an image repository scanning task.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteImageRegistryScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteImageRegistryScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteImageRegistryTimedScanTaskConfig(
            self,
            request: models.DeleteImageRegistryTimedScanTaskConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteImageRegistryTimedScanTaskConfigResponse:
        """
        Delete the scheduled scan task configuration of an image repository.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteImageRegistryTimedScanTaskConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteImageRegistryTimedScanTaskConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteImageSensitiveWhitelist(
            self,
            request: models.DeleteImageSensitiveWhitelistRequest,
            opts: Dict = None,
    ) -> models.DeleteImageSensitiveWhitelistResponse:
        """
        This API is used to delete an allowlist for sensitive information from a container image.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteImageSensitiveWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteImageSensitiveWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteImageVirusWhitelist(
            self,
            request: models.DeleteImageVirusWhitelistRequest,
            opts: Dict = None,
    ) -> models.DeleteImageVirusWhitelistResponse:
        """
        This API is used to delete the image Trojan allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteImageVirusWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteImageVirusWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteImageVulWhitelist(
            self,
            request: models.DeleteImageVulWhitelistRequest,
            opts: Dict = None,
    ) -> models.DeleteImageVulWhitelistResponse:
        """
        Deletes the vulnerability allowlist of a container image
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteImageVulWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteImageVulWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLoginWhiteList(
            self,
            request: models.DeleteLoginWhiteListRequest,
            opts: Dict = None,
    ) -> models.DeleteLoginWhiteListResponse:
        """
        This API is used to delete the cross-region log-in allowlist rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLoginWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLoginWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMachineClearHistory(
            self,
            request: models.DeleteMachineClearHistoryRequest,
            opts: Dict = None,
    ) -> models.DeleteMachineClearHistoryResponse:
        """
        This API is used to delete clearing records of a machine.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMachineClearHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMachineClearHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRiskScanTask(
            self,
            request: models.DeleteRiskScanTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteRiskScanTaskResponse:
        """
        Delete Risk Center Scan Task
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRiskScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRiskScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSandboxACLRule(
            self,
            request: models.DeleteSandboxACLRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteSandboxACLRuleResponse:
        """
        Delete ACL user rules in batches. After deletion, rules are no longer returned in list queries and no longer take effect on traffic. If any ID does not exist or belongs to another tenant, an error is returned overall.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSandboxACLRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSandboxACLRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSandboxDLPRule(
            self,
            request: models.DeleteSandboxDLPRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteSandboxDLPRuleResponse:
        """
        Batch delete DLP user rules. If any ID does not exist or belongs to another tenant, an error is returned for the entire request.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSandboxDLPRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSandboxDLPRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSandboxFileRule(
            self,
            request: models.DeleteSandboxFileRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteSandboxFileRuleResponse:
        """
        Create command sandbox file access policy
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSandboxFileRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSandboxFileRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSandboxLLMAuditRule(
            self,
            request: models.DeleteSandboxLLMAuditRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteSandboxLLMAuditRuleResponse:
        """
        Batch delete LLM audit user rules. If any ID does not exist or belongs to another tenant, an error is returned overall.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSandboxLLMAuditRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSandboxLLMAuditRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVulWhitelist(
            self,
            request: models.DeleteVulWhitelistRequest,
            opts: Dict = None,
    ) -> models.DeleteVulWhitelistResponse:
        """
        This API is used to delete a vulnerability allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVulWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVulWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWebhookPolicies(
            self,
            request: models.DeleteWebhookPoliciesRequest,
            opts: Dict = None,
    ) -> models.DeleteWebhookPoliciesResponse:
        """
        Delete notification policies in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWebhookPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWebhookPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWebhookReceivers(
            self,
            request: models.DeleteWebhookReceiversRequest,
            opts: Dict = None,
    ) -> models.DeleteWebhookReceiversResponse:
        """
        Delete receiving robots in batches. Before deletion, the reference relationships are automatically removed from all policies that refer to these robots.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWebhookReceivers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWebhookReceiversResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIAgentAssetList(
            self,
            request: models.DescribeAIAgentAssetListRequest,
            opts: Dict = None,
    ) -> models.DescribeAIAgentAssetListResponse:
        """
        Search for AI agent asset list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIAgentAssetList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIAgentAssetListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIAgentCredentialList(
            self,
            request: models.DescribeAIAgentCredentialListRequest,
            opts: Dict = None,
    ) -> models.DescribeAIAgentCredentialListResponse:
        """
        Retrieves the scan list of AIAgent asset credentials
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIAgentCredentialList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIAgentCredentialListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIAgentCredentialLocationList(
            self,
            request: models.DescribeAIAgentCredentialLocationListRequest,
            opts: Dict = None,
    ) -> models.DescribeAIAgentCredentialLocationListResponse:
        """
        This API is used to query the leaked location list of one credential by credential group row ID in pages. It is used with the DescribeAIAgentCredentialList interface in the split and unfold scenario to avoid performance issues caused by pulling hundreds of thousands of locations at once in data skew scenarios.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIAgentCredentialLocationList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIAgentCredentialLocationListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIAgentSkillList(
            self,
            request: models.DescribeAIAgentSkillListRequest,
            opts: Dict = None,
    ) -> models.DescribeAIAgentSkillListResponse:
        """
        Search the skill list of an AI Agent
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIAgentSkillList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIAgentSkillListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIAnalysisFileDownloadURL(
            self,
            request: models.DescribeAIAnalysisFileDownloadURLRequest,
            opts: Dict = None,
    ) -> models.DescribeAIAnalysisFileDownloadURLResponse:
        """
        Get the temporary download link of an AI analysis file.

        The original address of the input file. Returns a signed temporary download link with a validity period of 2 hours.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIAnalysisFileDownloadURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIAnalysisFileDownloadURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIAnalysisHistory(
            self,
            request: models.DescribeAIAnalysisHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeAIAnalysisHistoryResponse:
        """
        Retrieve historical analysis records of the cloud security AI assistant.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIAnalysisHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIAnalysisHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIAnalysisRecommendQuestions(
            self,
            request: models.DescribeAIAnalysisRecommendQuestionsRequest,
            opts: Dict = None,
    ) -> models.DescribeAIAnalysisRecommendQuestionsResponse:
        """
        Retrieve recommended questions for AI QA.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIAnalysisRecommendQuestions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIAnalysisRecommendQuestionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIAnalysisRobotInfo(
            self,
            request: models.DescribeAIAnalysisRobotInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAIAnalysisRobotInfoResponse:
        """
        This API is used to obtain basic information of the Cloud Security AI Assistant.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIAnalysisRobotInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIAnalysisRobotInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIAnalysisSMTP(
            self,
            request: models.DescribeAIAnalysisSMTPRequest,
            opts: Dict = None,
    ) -> models.DescribeAIAnalysisSMTPResponse:
        """
        Query SMTP mailbox access information of the AI assistant
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIAnalysisSMTP"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIAnalysisSMTPResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAILinkSetting(
            self,
            request: models.DescribeAILinkSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeAILinkSettingResponse:
        """
        Query the AI-Link engine configuration
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAILinkSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAILinkSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIScheduleList(
            self,
            request: models.DescribeAIScheduleListRequest,
            opts: Dict = None,
    ) -> models.DescribeAIScheduleListResponse:
        """
        Query the list of AI scheduled tasks.

        Supports paging query and status filtering, and returns the scheduled task list and total number of entries.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIScheduleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIScheduleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAISchedulePlanList(
            self,
            request: models.DescribeAISchedulePlanListRequest,
            opts: Dict = None,
    ) -> models.DescribeAISchedulePlanListResponse:
        """
        Queries AI scheduled task trigger plans.

        This API is used to query the future trigger plan list of a specified AI scheduled task within a given time window.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAISchedulePlanList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAISchedulePlanListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIScheduleStats(
            self,
            request: models.DescribeAIScheduleStatsRequest,
            opts: Dict = None,
    ) -> models.DescribeAIScheduleStatsResponse:
        """
        Queries AI scheduled task statistics information.

        Returns the total number of scheduled tasks and the number of running tasks for the current user.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIScheduleStats"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIScheduleStatsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIScheduleTaskDetail(
            self,
            request: models.DescribeAIScheduleTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAIScheduleTaskDetailResponse:
        """
        Queries the details of AI scheduled task executions.

        This API is used to query the detailed information of a specified task execution by task ID, including the execution status and results.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIScheduleTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIScheduleTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIScheduleTaskList(
            self,
            request: models.DescribeAIScheduleTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeAIScheduleTaskListResponse:
        """
        This API is used to query the scheduled AI task execution list.

        Queries the historical execution records of AI scheduled tasks. Supports pagination and filtering by scheduled task ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIScheduleTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIScheduleTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAKAnalysisDetail(
            self,
            request: models.DescribeAKAnalysisDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAKAnalysisDetailResponse:
        """
        Access key alarm record AI analysis result details
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAKAnalysisDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAKAnalysisDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAbTestUser(
            self,
            request: models.DescribeAbTestUserRequest,
            opts: Dict = None,
    ) -> models.DescribeAbTestUserResponse:
        """
        Determine whether the user is a grayscale user
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAbTestUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAbTestUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAbnormalCallRecord(
            self,
            request: models.DescribeAbnormalCallRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeAbnormalCallRecordResponse:
        """
        Get the call record list
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
        List of access key alarm records
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
        Access key alarm record details
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
        Retrieve the user access key asset list
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
        List of access key risk records
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
        Access key risk record details
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
        This API is used to query account details of a user.
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
        Query user account list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessKeyUserList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessKeyUserListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessKeyWhiteList(
            self,
            request: models.DescribeAccessKeyWhiteListRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessKeyWhiteListResponse:
        """
        Access key alarm record list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessKeyWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessKeyWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentConfigSetting(
            self,
            request: models.DescribeAgentConfigSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentConfigSettingResponse:
        """
        Query client configuration settings (configuration group). This is a standalone API split from DescribeAgentRunMode.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentConfigSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentConfigSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentRunMode(
            self,
            request: models.DescribeAgentRunModeRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentRunModeResponse:
        """
        Get the client running mode and runtime configuration information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentRunMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentRunModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentRunPolicy(
            self,
            request: models.DescribeAgentRunPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentRunPolicyResponse:
        """
        Query client running policies (policy groups). This is a standalone API split from DescribeAgentRunMode.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentRunPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentRunPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlertList(
            self,
            request: models.DescribeAlertListRequest,
            opts: Dict = None,
    ) -> models.DescribeAlertListResponse:
        """
        Alarm Center full alarm list API
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlertList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlertListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetComponentList(
            self,
            request: models.DescribeAssetComponentListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetComponentListResponse:
        """
        Query the component list in an asset.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetComponentList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetComponentListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetComponentRelatedImageList(
            self,
            request: models.DescribeAssetComponentRelatedImageListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetComponentRelatedImageListResponse:
        """
        Queries the list of associated images of image repository components.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetComponentRelatedImageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetComponentRelatedImageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetDetail(
            self,
            request: models.DescribeAssetDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetDetailResponse:
        """
        Asset detail information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetFilterViews(
            self,
            request: models.DescribeAssetFilterViewsRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetFilterViewsResponse:
        """
        Asset search view
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetFilterViews"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetFilterViewsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetInfo(
            self,
            request: models.DescribeAssetInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetInfoResponse:
        """
        Asset information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetLastSyncTime(
            self,
            request: models.DescribeAssetLastSyncTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetLastSyncTimeResponse:
        """
        Last Synchronization Time of Assets
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetLastSyncTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetLastSyncTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetOverview(
            self,
            request: models.DescribeAssetOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetOverviewResponse:
        """
        Asset Overview statistics
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetProcessList(
            self,
            request: models.DescribeAssetProcessListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetProcessListResponse:
        """
        This API is used to query the process list of host nodes on exposed paths in cloud boundary analysis.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetProcessList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetProcessListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetRiskDetail(
            self,
            request: models.DescribeAssetRiskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetRiskDetailResponse:
        """
        Asset risk details
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetRiskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetRiskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetRiskList(
            self,
            request: models.DescribeAssetRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetRiskListResponse:
        """
        Cloud resource configuration risk list from the asset perspective
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetSyncTaskStatus(
            self,
            request: models.DescribeAssetSyncTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetSyncTaskStatusResponse:
        """
        Asset sync task status
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetSyncTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetSyncTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetTagAttributes(
            self,
            request: models.DescribeAssetTagAttributesRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetTagAttributesResponse:
        """
        Retrieves asset tag attributes
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetTagAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetTagAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetTagTree(
            self,
            request: models.DescribeAssetTagTreeRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetTagTreeResponse:
        """
        Asset tag tree structured data
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetTagTree"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetTagTreeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetTags(
            self,
            request: models.DescribeAssetTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetTagsResponse:
        """
        All assets
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetTree(
            self,
            request: models.DescribeAssetTreeRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetTreeResponse:
        """
        Asset tree structure
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetTree"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetTreeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetViewVulRiskList(
            self,
            request: models.DescribeAssetViewVulRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetViewVulRiskListResponse:
        """
        Obtain Vulnerability Risk List from Asset's Perspective
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetViewVulRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetViewVulRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackendScanEngineRegionList(
            self,
            request: models.DescribeBackendScanEngineRegionListRequest,
            opts: Dict = None,
    ) -> models.DescribeBackendScanEngineRegionListResponse:
        """
        This API is used to query the region list of the backend scanning engine.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackendScanEngineRegionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackendScanEngineRegionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBanMode(
            self,
            request: models.DescribeBanModeRequest,
            opts: Dict = None,
    ) -> models.DescribeBanModeResponse:
        """
        This API is used to obtain the brute-force blocking mode.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBanMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBanModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBanStatus(
            self,
            request: models.DescribeBanStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeBanStatusResponse:
        """
        This API is used to obtain the block button status.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBanStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBanStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineAggregatedItemList(
            self,
            request: models.DescribeBaselineAggregatedItemListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineAggregatedItemListResponse:
        """
        This API is used to obtain the aggregated scan result list by detection item, for showing the number of passed and failed assets by detection item on the "Detection Item" Tab of the policy details page.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineAggregatedItemList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineAggregatedItemListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineAggregatedPolicyList(
            self,
            request: models.DescribeBaselineAggregatedPolicyListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineAggregatedPolicyListResponse:
        """
        This API is used to get the aggregation scan result list by baseline policy dimension, for the "Baseline Scan Policy" module on the overview page to display pass/fail status by policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineAggregatedPolicyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineAggregatedPolicyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineCalculatingStatisticsPolicyIDList(
            self,
            request: models.DescribeBaselineCalculatingStatisticsPolicyIDListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineCalculatingStatisticsPolicyIDListResponse:
        """
        Queries the list of Policy IDs currently at the "statistical calculation" status, used for frontend polling to judge whether the scan results statistics are ready.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineCalculatingStatisticsPolicyIDList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineCalculatingStatisticsPolicyIDListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineCategoryItemList(
            self,
            request: models.DescribeBaselineCategoryItemListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineCategoryItemListResponse:
        """
        This API is used to query the detection item list of a category.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineCategoryItemList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineCategoryItemListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineFixRecordList(
            self,
            request: models.DescribeBaselineFixRecordListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineFixRecordListResponse:
        """
        Get the historical record list of baseline risk corrections, used to show fixed detection items and corresponding assets on the "Correction Record" page.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineFixRecordList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineFixRecordListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineItemRiskList(
            self,
            request: models.DescribeBaselineItemRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineItemRiskListResponse:
        """
        This API is used to retrieve the risk record list of detection item dimensions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineItemRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineItemRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineMainTaskItemList(
            self,
            request: models.DescribeBaselineMainTaskItemListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineMainTaskItemListResponse:
        """
        Get the detection item list of built-in baseline classifications (parent category -> subcategory -> built-in detection item ID list) for selecting baseline detection items on the policy editing page.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineMainTaskItemList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineMainTaskItemListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineMainTaskList(
            self,
            request: models.DescribeBaselineMainTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineMainTaskListResponse:
        """
        Get the scan main task list for the Task Record page to show the history and results of one-click scan, period scanning, and disperse scan.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineMainTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineMainTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineOverview(
            self,
            request: models.DescribeBaselineOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineOverviewResponse:
        """
        Retrieve header data of the baseline overview page, including the total count of failed detection items, the number of fixes in the past one year, the last scan time, and whether period scanning is currently enabled.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselinePolicyCategoryList(
            self,
            request: models.DescribeBaselinePolicyCategoryListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselinePolicyCategoryListResponse:
        """
        This API is used to retrieve the built-in baseline classification tree (parent category → subcategory → built-in detection item ID list) for policy details display.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselinePolicyCategoryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselinePolicyCategoryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselinePolicyItemList(
            self,
            request: models.DescribeBaselinePolicyItemListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselinePolicyItemListResponse:
        """
        Get the Detection Item List configured in a policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselinePolicyItemList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselinePolicyItemListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselinePolicyList(
            self,
            request: models.DescribeBaselinePolicyListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselinePolicyListResponse:
        """
        This API is used to obtain the list of baseline policies for list page display of system and custom policies and their configuration status in scenarios such as cycle plan management.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselinePolicyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselinePolicyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselinePolicyNameExistAppidList(
            self,
            request: models.DescribeBaselinePolicyNameExistAppidListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselinePolicyNameExistAppidListResponse:
        """
        This API is used to obtain the list of existing users for a baseline policy name.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselinePolicyNameExistAppidList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselinePolicyNameExistAppidListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineSubTaskList(
            self,
            request: models.DescribeBaselineSubTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineSubTaskListResponse:
        """
        Get the scan subtask list to show the scan status and failure reason of each host or cluster in the "Asset dimension" section of the task details page.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineSubTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineSubTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineSyncConf(
            self,
            request: models.DescribeBaselineSyncConfRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineSyncConfResponse:
        """
        This API is used to get the baseline synchronization configuration of the current admin account. Only the Group Administrator can call this API. For ordinary member accounts, please use DescribeBaselineUserOtherConf.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineSyncConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineSyncConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineSystemCategoryList(
            self,
            request: models.DescribeBaselineSystemCategoryListRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineSystemCategoryListResponse:
        """
        Obtain the system built-in baseline classification tree (parent category → subcategory → built-in detection item ID list), used for selecting baseline detection items on the policy editing page.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineSystemCategoryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineSystemCategoryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineUserOtherConf(
            self,
            request: models.DescribeBaselineUserOtherConfRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineUserOtherConfResponse:
        """
        Retrieve user-level baseline configuration for the current account.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineUserOtherConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineUserOtherConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaselineUserWeakPasswordConf(
            self,
            request: models.DescribeBaselineUserWeakPasswordConfRequest,
            opts: Dict = None,
    ) -> models.DescribeBaselineUserWeakPasswordConfResponse:
        """
        This API is used to search for the custom dictionary of weak passwords for users under the current account.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaselineUserWeakPasswordConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaselineUserWeakPasswordConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBruteAttackRules(
            self,
            request: models.DescribeBruteAttackRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeBruteAttackRulesResponse:
        """
        This API is used to obtain brute force cracking rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBruteAttackRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBruteAttackRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCFGRiskReportStatistics(
            self,
            request: models.DescribeCFGRiskReportStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeCFGRiskReportStatisticsResponse:
        """
        Risk statistics for cloud resource configuration check reports
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCFGRiskReportStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCFGRiskReportStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCFGRiskStatistics(
            self,
            request: models.DescribeCFGRiskStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeCFGRiskStatisticsResponse:
        """
        Query the statistical information of scanning results.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCFGRiskStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCFGRiskStatisticsResponse
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
        
    async def DescribeCLSLogIndexV3(
            self,
            request: models.DescribeCLSLogIndexV3Request,
            opts: Dict = None,
    ) -> models.DescribeCLSLogIndexV3Response:
        """
        Get log index information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCLSLogIndexV3"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCLSLogIndexV3Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCLSLogListV3(
            self,
            request: models.DescribeCLSLogListV3Request,
            opts: Dict = None,
    ) -> models.DescribeCLSLogListV3Response:
        """
        Log analytics retrieval interface v3
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCLSLogListV3"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCLSLogListV3Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCSCPayInfo(
            self,
            request: models.DescribeCSCPayInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeCSCPayInfoResponse:
        """
        Query the consolidated billing information of the current account, including order status, payment mode, quotas, and other detailed information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCSCPayInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCSCPayInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCSIPLicenseBindSchedule(
            self,
            request: models.DescribeCSIPLicenseBindScheduleRequest,
            opts: Dict = None,
    ) -> models.DescribeCSIPLicenseBindScheduleResponse:
        """
        Query the progress of the async binding task returned by ModifyCSIPLicenseBinds.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCSIPLicenseBindSchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCSIPLicenseBindScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCSIPMalwareScanTaskDetail(
            self,
            request: models.DescribeCSIPMalwareScanTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCSIPMalwareScanTaskDetailResponse:
        """
        This API is used to get host details of a CSIP scan task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCSIPMalwareScanTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCSIPMalwareScanTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCSIPMalwareScanTaskProgress(
            self,
            request: models.DescribeCSIPMalwareScanTaskProgressRequest,
            opts: Dict = None,
    ) -> models.DescribeCSIPMalwareScanTaskProgressResponse:
        """
        This API is used to query the progress of CSIP manual scan.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCSIPMalwareScanTaskProgress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCSIPMalwareScanTaskProgressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCSIPRiskStatistics(
            self,
            request: models.DescribeCSIPRiskStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeCSIPRiskStatisticsResponse:
        """
        Obtain risk center risk overview sample code
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCSIPRiskStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCSIPRiskStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCSPMPayInfo(
            self,
            request: models.DescribeCSPMPayInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeCSPMPayInfoResponse:
        """
        This API is used to obtain purchased CSPM order information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCSPMPayInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCSPMPayInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCVMAssetInfo(
            self,
            request: models.DescribeCVMAssetInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeCVMAssetInfoResponse:
        """
        CVM Details
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
        Get cvm list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCVMAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCVMAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCWPExposePath(
            self,
            request: models.DescribeCWPExposePathRequest,
            opts: Dict = None,
    ) -> models.DescribeCWPExposePathResponse:
        """
        Queries cloud boundary analysis path nodes (dedicated for hosts)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCWPExposePath"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCWPExposePathResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCWPExposures(
            self,
            request: models.DescribeCWPExposuresRequest,
            opts: Dict = None,
    ) -> models.DescribeCWPExposuresResponse:
        """
        Cloud boundary analysis asset list (suitable for host assets)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCWPExposures"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCWPExposuresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCWPLicenseBindSchedule(
            self,
            request: models.DescribeCWPLicenseBindScheduleRequest,
            opts: Dict = None,
    ) -> models.DescribeCWPLicenseBindScheduleResponse:
        """
        This API is used to query the binding task progress of the authorization.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCWPLicenseBindSchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCWPLicenseBindScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCWPMachineDetail(
            self,
            request: models.DescribeCWPMachineDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCWPMachineDetailResponse:
        """
        Host details
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCWPMachineDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCWPMachineDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCWPMachineOsList(
            self,
            request: models.DescribeCWPMachineOsListRequest,
            opts: Dict = None,
    ) -> models.DescribeCWPMachineOsListResponse:
        """
        This API is used to query the machine operating system list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCWPMachineOsList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCWPMachineOsListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCWPMachines(
            self,
            request: models.DescribeCWPMachinesRequest,
            opts: Dict = None,
    ) -> models.DescribeCWPMachinesResponse:
        """
        Host list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCWPMachines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCWPMachinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCWPOrderList(
            self,
            request: models.DescribeCWPOrderListRequest,
            opts: Dict = None,
    ) -> models.DescribeCWPOrderListResponse:
        """
        Query the resource order list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCWPOrderList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCWPOrderListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCWPScanIpInfo(
            self,
            request: models.DescribeCWPScanIpInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeCWPScanIpInfoResponse:
        """
        Query Tencent Cloud scan IP information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCWPScanIpInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCWPScanIpInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCWPTaskDuration(
            self,
            request: models.DescribeCWPTaskDurationRequest,
            opts: Dict = None,
    ) -> models.DescribeCWPTaskDurationResponse:
        """
        Obtain Task Distribution Duration
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCWPTaskDuration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCWPTaskDurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCallRecord(
            self,
            request: models.DescribeCallRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeCallRecordResponse:
        """
        Query the call record list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCallRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCallRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCheckConnectivityHostList(
            self,
            request: models.DescribeCheckConnectivityHostListRequest,
            opts: Dict = None,
    ) -> models.DescribeCheckConnectivityHostListResponse:
        """
        Query the list of connectivity detection hosts
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCheckConnectivityHostList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCheckConnectivityHostListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCheckViewRisks(
            self,
            request: models.DescribeCheckViewRisksRequest,
            opts: Dict = None,
    ) -> models.DescribeCheckViewRisksResponse:
        """
        Cloud resource configuration risk list from the check perspective
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCheckViewRisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCheckViewRisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClbListenerList(
            self,
            request: models.DescribeClbListenerListRequest,
            opts: Dict = None,
    ) -> models.DescribeClbListenerListResponse:
        """
        Queries the listener list corresponding to a specified Tencent Cloud CLB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClbListenerList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClbListenerListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClbListenerRules(
            self,
            request: models.DescribeClbListenerRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeClbListenerRulesResponse:
        """
        Queries the list of Layer 7 forwarding rules corresponding to a specified CLB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClbListenerRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClbListenerRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClbTargets(
            self,
            request: models.DescribeClbTargetsRequest,
            opts: Dict = None,
    ) -> models.DescribeClbTargetsResponse:
        """
        Query the CLB backend service list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClbTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClbTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudAssets(
            self,
            request: models.DescribeCloudAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudAssetsResponse:
        """
        All assets
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudFunctionList(
            self,
            request: models.DescribeCloudFunctionListRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudFunctionListResponse:
        """
        Function list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudFunctionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudFunctionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterAssetList(
            self,
            request: models.DescribeClusterAssetListRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterAssetListResponse:
        """
        Queries the asset list of a container cluster
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterAssetList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterAssetListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterAssetSyncTaskStatus(
            self,
            request: models.DescribeClusterAssetSyncTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterAssetSyncTaskStatusResponse:
        """
        This API is used to query the synchronization task status of cluster assets.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterAssetSyncTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterAssetSyncTaskStatusResponse
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
        
    async def DescribeClusterContainerAppList(
            self,
            request: models.DescribeClusterContainerAppListRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterContainerAppListResponse:
        """
        This API is used to query the associated application list of a container. It retrieves associated application service information by container ID and supports pagination.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterContainerAppList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterContainerAppListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterContainerComponentList(
            self,
            request: models.DescribeClusterContainerComponentListRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterContainerComponentListResponse:
        """
        Query the list of components associated with a container. Get associated component information by container ID. Pagination is supported.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterContainerComponentList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterContainerComponentListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterContainerDetail(
            self,
            request: models.DescribeClusterContainerDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterContainerDetailResponse:
        """
        This API is used to query cluster container details. It retrieves basic container info, mirror information, mount information, network info, and associated node information by container ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterContainerDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterContainerDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterContainerList(
            self,
            request: models.DescribeClusterContainerListRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterContainerListResponse:
        """
        Query the container list of a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterContainerList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterContainerListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterContainerPortList(
            self,
            request: models.DescribeClusterContainerPortListRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterContainerPortListResponse:
        """
        Query the list of ports associated with a container. This API is used to obtain associated port information by container ID and supports pagination.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterContainerPortList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterContainerPortListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterContainerProcessList(
            self,
            request: models.DescribeClusterContainerProcessListRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterContainerProcessListResponse:
        """
        This API is used to query the associated process list of a container. It obtains associated process information by container ID, supports time sorting and pagination. Filter.By supports StartTime; Filter.Order supports ASC/DESC.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterContainerProcessList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterContainerProcessListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterContainerWebServiceList(
            self,
            request: models.DescribeClusterContainerWebServiceListRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterContainerWebServiceListResponse:
        """
        This API is used to query the associated Web Service List of a container. It retrieves associated web service information by container ID and supports pagination.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterContainerWebServiceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterContainerWebServiceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterDetail(
            self,
            request: models.DescribeClusterDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterDetailResponse:
        """
        Querying Cluster Details
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterInstallCommand(
            self,
            request: models.DescribeClusterInstallCommandRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterInstallCommandResponse:
        """
        Query the cluster installation command
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterInstallCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterInstallCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterNamespaceList(
            self,
            request: models.DescribeClusterNamespaceListRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterNamespaceListResponse:
        """
        Query the cluster namespace list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterNamespaceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterNamespaceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterNodeList(
            self,
            request: models.DescribeClusterNodeListRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterNodeListResponse:
        """
        Query the cluster node list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterNodeList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterNodeListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterPodAssets(
            self,
            request: models.DescribeClusterPodAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterPodAssetsResponse:
        """
        Cluster Pod List
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterPodAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterPodAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterPodDetail(
            self,
            request: models.DescribeClusterPodDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterPodDetailResponse:
        """
        This API is used to query Pod details in A cluster. It is A new Type A API for the container asset revision and serves as the main entrance to the Pod Asset Details Page. The input parameter is only UniqueID. The output parameters cover asset information, cluster, namespace, node, Workload, as well as the number of risk events and alarm events grouped by four risk levels.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterPodDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterPodDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterPodList(
            self,
            request: models.DescribeClusterPodListRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterPodListResponse:
        """
        Inquires the cluster pod list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterPodList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterPodListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterServiceList(
            self,
            request: models.DescribeClusterServiceListRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterServiceListResponse:
        """
        Query the cluster service list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterServiceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterServiceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterSummary(
            self,
            request: models.DescribeClusterSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterSummaryResponse:
        """
        Query cluster overview data
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterSuperNodeInfo(
            self,
            request: models.DescribeClusterSuperNodeInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterSuperNodeInfoResponse:
        """
        This API is used to query super node details in a cluster and return basic info (region, availability zone, last asset update time, node origin, subnet, and core count) and cluster information (cluster name, Cluster ID, cluster status, Kubernetes version, and Kubelet version).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterSuperNodeInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterSuperNodeInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComplianceOverview(
            self,
            request: models.DescribeComplianceOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeComplianceOverviewResponse:
        """
        Cloud resource configuration detection compliance overview
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComplianceOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComplianceOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComplianceRiskList(
            self,
            request: models.DescribeComplianceRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeComplianceRiskListResponse:
        """
        Cloud resource configuration risk list from the compliance standard aggregation perspective
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComplianceRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComplianceRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComplianceStandardTermTree(
            self,
            request: models.DescribeComplianceStandardTermTreeRequest,
            opts: Dict = None,
    ) -> models.DescribeComplianceStandardTermTreeResponse:
        """
        Cloud resource configuration inspection standard chapter clause tree
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComplianceStandardTermTree"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComplianceStandardTermTreeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComplianceStatistics(
            self,
            request: models.DescribeComplianceStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeComplianceStatisticsResponse:
        """
        Category statistics for cloud resource configuration detection specifications
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComplianceStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComplianceStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigCheckRules(
            self,
            request: models.DescribeConfigCheckRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigCheckRulesResponse:
        """
        Example of cloud resource configuration risk rule list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigCheckRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigCheckRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCspmShardConfig(
            self,
            request: models.DescribeCspmShardConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeCspmShardConfigResponse:
        """
        This API is used to query the CSPM auto quota shared configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCspmShardConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCspmShardConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomAssetTagCount(
            self,
            request: models.DescribeCustomAssetTagCountRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomAssetTagCountResponse:
        """
        number of user-customized tags
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomAssetTagCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomAssetTagCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomRiskRuleDetail(
            self,
            request: models.DescribeCustomRiskRuleDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomRiskRuleDetailResponse:
        """
        Example of a custom risk rule configuration detail list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomRiskRuleDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomRiskRuleDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomRiskRules(
            self,
            request: models.DescribeCustomRiskRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomRiskRulesResponse:
        """
        Lists the configuration of custom risk rules
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomRiskRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomRiskRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDbAssetInfo(
            self,
            request: models.DescribeDbAssetInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDbAssetInfoResponse:
        """
        DB Asset Details
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
        Database Asset List
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDbAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDbAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDefaultSecurityScoreRule(
            self,
            request: models.DescribeDefaultSecurityScoreRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeDefaultSecurityScoreRuleResponse:
        """
        Retrieve the built-in default security scoring rules for resetting custom rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDefaultSecurityScoreRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDefaultSecurityScoreRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainAssets(
            self,
            request: models.DescribeDomainAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainAssetsResponse:
        """
        Domain name list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAccessRecord(
            self,
            request: models.DescribeDspmAccessRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAccessRecordResponse:
        """
        Query Dspm access records
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAccessRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAccessRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAccessTopologyAccounts(
            self,
            request: models.DescribeDspmAccessTopologyAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAccessTopologyAccountsResponse:
        """
        Queries the Dspm access topology account list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAccessTopologyAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAccessTopologyAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAccessTopologyAssets(
            self,
            request: models.DescribeDspmAccessTopologyAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAccessTopologyAssetsResponse:
        """
        Query the Dspm access topology asset list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAccessTopologyAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAccessTopologyAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAccessTopologyIps(
            self,
            request: models.DescribeDspmAccessTopologyIpsRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAccessTopologyIpsResponse:
        """
        Query the Dspm access topology ip list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAccessTopologyIps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAccessTopologyIpsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmApplyHistory(
            self,
            request: models.DescribeDspmApplyHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmApplyHistoryResponse:
        """
        Queries Dspm application history
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmApplyHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmApplyHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmApplyOrderList(
            self,
            request: models.DescribeDspmApplyOrderListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmApplyOrderListResponse:
        """
        Queries the Dspm application form list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmApplyOrderList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmApplyOrderListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmApproveHistory(
            self,
            request: models.DescribeDspmApproveHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmApproveHistoryResponse:
        """
        Query Dspm approval history
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmApproveHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmApproveHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmApproveOrderList(
            self,
            request: models.DescribeDspmApproveOrderListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmApproveOrderListResponse:
        """
        Queries Dspm approval form list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmApproveOrderList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmApproveOrderListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetAccessTopology(
            self,
            request: models.DescribeDspmAssetAccessTopologyRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetAccessTopologyResponse:
        """
        Query the Dspm asset access topology
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetAccessTopology"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetAccessTopologyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetAccountIdentify(
            self,
            request: models.DescribeDspmAssetAccountIdentifyRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetAccountIdentifyResponse:
        """
        Query Dspm asset account identity information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetAccountIdentify"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetAccountIdentifyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetAccountPresetPrivileges(
            self,
            request: models.DescribeDspmAssetAccountPresetPrivilegesRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetAccountPresetPrivilegesResponse:
        """
        Querying preset privileged information of Dspm asset accounts
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetAccountPresetPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetAccountPresetPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetAccountRecycledPrivileges(
            self,
            request: models.DescribeDspmAssetAccountRecycledPrivilegesRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetAccountRecycledPrivilegesResponse:
        """
        Querying privileged information of Dspm asset accounts after recycling
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetAccountRecycledPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetAccountRecycledPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetAccounts(
            self,
            request: models.DescribeDspmAssetAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetAccountsResponse:
        """
        Query the Dspm asset account list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetDatabaseList(
            self,
            request: models.DescribeDspmAssetDatabaseListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetDatabaseListResponse:
        """
        This API is used to query asset database information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetDatabaseList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetDatabaseListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetDatabases(
            self,
            request: models.DescribeDspmAssetDatabasesRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetDatabasesResponse:
        """
        This API is used to query the list of Dspm asset databases.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetDatabases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetDatabasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetFieldList(
            self,
            request: models.DescribeDspmAssetFieldListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetFieldListResponse:
        """
        Queries the dspm asset field information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetFieldList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetFieldListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetFieldSamples(
            self,
            request: models.DescribeDspmAssetFieldSamplesRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetFieldSamplesResponse:
        """
        Query sample values of dspm asset fields
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetFieldSamples"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetFieldSamplesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetIdentifyInfoList(
            self,
            request: models.DescribeDspmAssetIdentifyInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetIdentifyInfoListResponse:
        """
        Queries the dspm asset data recognition information list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetIdentifyInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetIdentifyInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetIds(
            self,
            request: models.DescribeDspmAssetIdsRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetIdsResponse:
        """
        Queries the list of Dspm asset IDs
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetLoginCredential(
            self,
            request: models.DescribeDspmAssetLoginCredentialRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetLoginCredentialResponse:
        """
        Query Dspm asset login credentials
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetLoginCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetLoginCredentialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetSecurityAnalyseStatus(
            self,
            request: models.DescribeDspmAssetSecurityAnalyseStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetSecurityAnalyseStatusResponse:
        """
        Query the security analysis status of Dspm assets.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetSecurityAnalyseStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetSecurityAnalyseStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetSupportedPrivileges(
            self,
            request: models.DescribeDspmAssetSupportedPrivilegesRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetSupportedPrivilegesResponse:
        """
        Queries supported permissions for Dspm assets
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetSupportedPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetSupportedPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssetTableList(
            self,
            request: models.DescribeDspmAssetTableListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetTableListResponse:
        """
        This API is used to query asset table information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssetTableList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetTableListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAssets(
            self,
            request: models.DescribeDspmAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAssetsResponse:
        """
        Queries the Dspm asset list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmAuditFilterStrategy(
            self,
            request: models.DescribeDspmAuditFilterStrategyRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmAuditFilterStrategyResponse:
        """
        Query dspm audit filter policies
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmAuditFilterStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmAuditFilterStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmBackupLogList(
            self,
            request: models.DescribeDspmBackupLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmBackupLogListResponse:
        """
        This API is used to query the backup log list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmBackupLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmBackupLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmBackupSetting(
            self,
            request: models.DescribeDspmBackupSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmBackupSettingResponse:
        """
        This API is used to query the log backup configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmBackupSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmBackupSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmCkafkaRouteList(
            self,
            request: models.DescribeDspmCkafkaRouteListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmCkafkaRouteListResponse:
        """
        This API is used to query the routing information of the CKafka instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmCkafkaRouteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmCkafkaRouteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmCkafkaTopicList(
            self,
            request: models.DescribeDspmCkafkaTopicListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmCkafkaTopicListResponse:
        """
        This API is used to query the topic list of the instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmCkafkaTopicList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmCkafkaTopicListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmDictionaryList(
            self,
            request: models.DescribeDspmDictionaryListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmDictionaryListResponse:
        """
        Query the list of dspm dictionary information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmDictionaryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmDictionaryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmExportTask(
            self,
            request: models.DescribeDspmExportTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmExportTaskResponse:
        """
        This API is used to query export tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmExportTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmExportTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmIdentifyCategoryList(
            self,
            request: models.DescribeDspmIdentifyCategoryListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmIdentifyCategoryListResponse:
        """
        Querying the dspm data identification classification list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmIdentifyCategoryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmIdentifyCategoryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmIdentifyComplianceCategoryRuleList(
            self,
            request: models.DescribeDspmIdentifyComplianceCategoryRuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmIdentifyComplianceCategoryRuleListResponse:
        """
        This API is used to query the list of data items associated with dspm data recognition template classifications.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmIdentifyComplianceCategoryRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmIdentifyComplianceCategoryRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmIdentifyComplianceGroupDetail(
            self,
            request: models.DescribeDspmIdentifyComplianceGroupDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmIdentifyComplianceGroupDetailResponse:
        """
        Query dspm identification template details
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmIdentifyComplianceGroupDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmIdentifyComplianceGroupDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmIdentifyComplianceGroupList(
            self,
            request: models.DescribeDspmIdentifyComplianceGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmIdentifyComplianceGroupListResponse:
        """
        Queries the dspm data identification template list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmIdentifyComplianceGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmIdentifyComplianceGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmIdentifyDistributionStatistics(
            self,
            request: models.DescribeDspmIdentifyDistributionStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmIdentifyDistributionStatisticsResponse:
        """
        Querying dspm data identification distribution statistics
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmIdentifyDistributionStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmIdentifyDistributionStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmIdentifyIdList(
            self,
            request: models.DescribeDspmIdentifyIdListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmIdentifyIdListResponse:
        """
        Query the Dspm identity ID list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmIdentifyIdList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmIdentifyIdListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmIdentifyInfo(
            self,
            request: models.DescribeDspmIdentifyInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmIdentifyInfoResponse:
        """
        Queries the Dspm identity information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmIdentifyInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmIdentifyInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmIdentifyInfoList(
            self,
            request: models.DescribeDspmIdentifyInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmIdentifyInfoListResponse:
        """
        Query the Dspm identity information list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmIdentifyInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmIdentifyInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmIdentifyLevelGroupList(
            self,
            request: models.DescribeDspmIdentifyLevelGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmIdentifyLevelGroupListResponse:
        """
        Query the dspm data identification classification group list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmIdentifyLevelGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmIdentifyLevelGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmIdentifyRuleDetail(
            self,
            request: models.DescribeDspmIdentifyRuleDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmIdentifyRuleDetailResponse:
        """
        Queries the dspm data identification data item details
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmIdentifyRuleDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmIdentifyRuleDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmIdentifyRuleList(
            self,
            request: models.DescribeDspmIdentifyRuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmIdentifyRuleListResponse:
        """
        Query the list of dspm identification data items.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmIdentifyRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmIdentifyRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmIdentifyRuleTestResult(
            self,
            request: models.DescribeDspmIdentifyRuleTestResultRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmIdentifyRuleTestResultResponse:
        """
        This API is used to query verification results of dspm data identification data items.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmIdentifyRuleTestResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmIdentifyRuleTestResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmLogDeliveryType(
            self,
            request: models.DescribeDspmLogDeliveryTypeRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmLogDeliveryTypeResponse:
        """
        This API is used to query the log type for log shipping.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmLogDeliveryType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmLogDeliveryTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmLogList(
            self,
            request: models.DescribeDspmLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmLogListResponse:
        """
        This API is used to query the log list information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmLogTypeConfigList(
            self,
            request: models.DescribeDspmLogTypeConfigListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmLogTypeConfigListResponse:
        """
        This API is used to query the log shipping configuration of a tenant.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmLogTypeConfigList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmLogTypeConfigListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmPayInfo(
            self,
            request: models.DescribeDspmPayInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmPayInfoResponse:
        """
        Get purchased Dspm order information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmPayInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmPayInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmPersonApplyHistory(
            self,
            request: models.DescribeDspmPersonApplyHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmPersonApplyHistoryResponse:
        """
        Queries Dspm visitor application records.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmPersonApplyHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmPersonApplyHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmPersonalIdentifyList(
            self,
            request: models.DescribeDspmPersonalIdentifyListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmPersonalIdentifyListResponse:
        """
        Query the list of Dspm personal identification information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmPersonalIdentifyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmPersonalIdentifyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmResource(
            self,
            request: models.DescribeDspmResourceRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmResourceResponse:
        """
        Queries Dspm instances
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmRisk(
            self,
            request: models.DescribeDspmRiskRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmRiskResponse:
        """
        Queries Dspm risk records
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmRisk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmRiskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmRiskDetail(
            self,
            request: models.DescribeDspmRiskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmRiskDetailResponse:
        """
        Queries Dspm risk details
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmRiskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmRiskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmRiskStrategy(
            self,
            request: models.DescribeDspmRiskStrategyRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmRiskStrategyResponse:
        """
        Queries Dspm risk policies
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmRiskStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmRiskStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmRiskStrategyGroup(
            self,
            request: models.DescribeDspmRiskStrategyGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmRiskStrategyGroupResponse:
        """
        Query Dspm risk group policies
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmRiskStrategyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmRiskStrategyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmRiskTendency(
            self,
            request: models.DescribeDspmRiskTendencyRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmRiskTendencyResponse:
        """
        Query Dspm risk trends.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmRiskTendency"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmRiskTendencyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmSessionList(
            self,
            request: models.DescribeDspmSessionListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmSessionListResponse:
        """
        This API is used to query the audit session list information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmSessionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmSessionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmStatistics(
            self,
            request: models.DescribeDspmStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmStatisticsResponse:
        """
        Query Dspm statistical information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmSupportedAssetType(
            self,
            request: models.DescribeDspmSupportedAssetTypeRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmSupportedAssetTypeResponse:
        """
        Queries information on asset types supported by Dspm.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmSupportedAssetType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmSupportedAssetTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmSyncAssetsStatus(
            self,
            request: models.DescribeDspmSyncAssetsStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmSyncAssetsStatusResponse:
        """
        Query the Dspm asset status synchronization.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmSyncAssetsStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmSyncAssetsStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmSyncUsersStatus(
            self,
            request: models.DescribeDspmSyncUsersStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmSyncUsersStatusResponse:
        """
        Query the Dspm user synchronization status.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmSyncUsersStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmSyncUsersStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmUserCkafkaInstanceList(
            self,
            request: models.DescribeDspmUserCkafkaInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmUserCkafkaInstanceListResponse:
        """
        This API is used to query the tenant CKafka instance list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmUserCkafkaInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmUserCkafkaInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDspmWhitelistStrategy(
            self,
            request: models.DescribeDspmWhitelistStrategyRequest,
            opts: Dict = None,
    ) -> models.DescribeDspmWhitelistStrategyResponse:
        """
        Query the Dspm allowlist policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDspmWhitelistStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDspmWhitelistStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDynamicAssets(
            self,
            request: models.DescribeDynamicAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeDynamicAssetsResponse:
        """
        List of specified asset types
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDynamicAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDynamicAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEDRRuleList(
            self,
            request: models.DescribeEDRRuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeEDRRuleListResponse:
        """
        This API is used to obtain the list of EDR policies.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEDRRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEDRRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEDRScanRecordList(
            self,
            request: models.DescribeEDRScanRecordListRequest,
            opts: Dict = None,
    ) -> models.DescribeEDRScanRecordListResponse:
        """
        This API is used to query the scan task list. Filter.Filters supports Name: Keyword (blurry, OperatorType=9), ScanType (MANUAL/CYCLE), TaskType (HOST/CONTAINER), Status (WAIT/SCANNING/FINISHED/FAILED/CANCELED), AppId (account).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEDRScanRecordList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEDRScanRecordListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEDRScanTaskDetail(
            self,
            request: models.DescribeEDRScanTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeEDRScanTaskDetailResponse:
        """
        Query scan task details. Filter.Filters supports Name: Status (asset scan status, OperatorType=7 IN match, Value: WAIT/SCANNING/FINISHED/FAILED).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEDRScanTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEDRScanTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdrAlertCountForAsset(
            self,
            request: models.DescribeEdrAlertCountForAssetRequest,
            opts: Dict = None,
    ) -> models.DescribeEdrAlertCountForAssetResponse:
        """
        This API is used to obtain EDR alarm quantity statistics for the asset module. It queries the EDR alarm table based on the passed-in MemberId and InstanceIDs and returns the number of alarm records. If InstanceIDs is empty, summarized statistics are returned. Otherwise, statistics are returned by InstanceID granularity.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdrAlertCountForAsset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdrAlertCountForAssetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdrAlertCountForContainer(
            self,
            request: models.DescribeEdrAlertCountForContainerRequest,
            opts: Dict = None,
    ) -> models.DescribeEdrAlertCountForContainerResponse:
        """
        Alarm quantity statistics in the container scenario.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdrAlertCountForContainer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdrAlertCountForContainerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdrAlertInfo(
            self,
            request: models.DescribeEdrAlertInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeEdrAlertInfoResponse:
        """
        This API is used to obtain EDR alert details, including complete information such as alert content JSON, asset enrichment, and intelligence enrichment.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdrAlertInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdrAlertInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdrAlertList(
            self,
            request: models.DescribeEdrAlertListRequest,
            opts: Dict = None,
    ) -> models.DescribeEdrAlertListResponse:
        """
        Query the EDR alarm list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdrAlertList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdrAlertListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdrAlertMultiAttackStages(
            self,
            request: models.DescribeEdrAlertMultiAttackStagesRequest,
            opts: Dict = None,
    ) -> models.DescribeEdrAlertMultiAttackStagesResponse:
        """
        EDR alert multi-attack stage queries
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdrAlertMultiAttackStages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdrAlertMultiAttackStagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdrAlertSummary(
            self,
            request: models.DescribeEdrAlertSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeEdrAlertSummaryResponse:
        """
        Retrieves EDR alarm statistics
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdrAlertSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdrAlertSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdrAlertThreatTags(
            self,
            request: models.DescribeEdrAlertThreatTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeEdrAlertThreatTagsResponse:
        """
        This API is used to query EDR alarm tags in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdrAlertThreatTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdrAlertThreatTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdrExcludeNetworkSegments(
            self,
            request: models.DescribeEdrExcludeNetworkSegmentsRequest,
            opts: Dict = None,
    ) -> models.DescribeEdrExcludeNetworkSegmentsResponse:
        """
        This API is used to query the exclusion network segment configurations for EDR log collection. TCP logs from network segments in the exclusion list will not be collected. If no user configuration exists, the system-recommended default network segments will be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdrExcludeNetworkSegments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdrExcludeNetworkSegmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdrExportJobDownloadURL(
            self,
            request: models.DescribeEdrExportJobDownloadURLRequest,
            opts: Dict = None,
    ) -> models.DescribeEdrExportJobDownloadURLResponse:
        """
        Query the EDR export download link
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdrExportJobDownloadURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdrExportJobDownloadURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdrExportJobList(
            self,
            request: models.DescribeEdrExportJobListRequest,
            opts: Dict = None,
    ) -> models.DescribeEdrExportJobListResponse:
        """
        Export the EDR task list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdrExportJobList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdrExportJobListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdrLogCollectPaths(
            self,
            request: models.DescribeEdrLogCollectPathsRequest,
            opts: Dict = None,
    ) -> models.DescribeEdrLogCollectPathsResponse:
        """
        This API is used to query the collection path configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdrLogCollectPaths"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdrLogCollectPathsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExportJobDownloadURL(
            self,
            request: models.DescribeExportJobDownloadURLRequest,
            opts: Dict = None,
    ) -> models.DescribeExportJobDownloadURLResponse:
        """
        Result download URL of an export task
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExportJobDownloadURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExportJobDownloadURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExportJobManageList(
            self,
            request: models.DescribeExportJobManageListRequest,
            opts: Dict = None,
    ) -> models.DescribeExportJobManageListResponse:
        """
        Exports the task list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExportJobManageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExportJobManageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExposeAssetCategory(
            self,
            request: models.DescribeExposeAssetCategoryRequest,
            opts: Dict = None,
    ) -> models.DescribeExposeAssetCategoryResponse:
        """
        Cloud boundary analysis asset category
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
        Query the cloud boundary analysis path node
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExposePath"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExposePathResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExposeRiskStatistics(
            self,
            request: models.DescribeExposeRiskStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeExposeRiskStatisticsResponse:
        """
        Pending risks to be governed for cloud boundaries
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExposeRiskStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExposeRiskStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExposeRisks(
            self,
            request: models.DescribeExposeRisksRequest,
            opts: Dict = None,
    ) -> models.DescribeExposeRisksResponse:
        """
        List of pending risks in cloud boundaries
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExposeRisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExposeRisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExposeRules(
            self,
            request: models.DescribeExposeRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeExposeRulesResponse:
        """
        List of boundary rules
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExposeRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExposeRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExposureAutoTagAttribute(
            self,
            request: models.DescribeExposureAutoTagAttributeRequest,
            opts: Dict = None,
    ) -> models.DescribeExposureAutoTagAttributeResponse:
        """
        Rule attributes for automatic tagging at cloud boundaries
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExposureAutoTagAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExposureAutoTagAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExposureAutoTagRules(
            self,
            request: models.DescribeExposureAutoTagRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeExposureAutoTagRulesResponse:
        """
        Automatic tagging of cloud boundaries - rule list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExposureAutoTagRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExposureAutoTagRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExposureTrend(
            self,
            request: models.DescribeExposureTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeExposureTrendResponse:
        """
        Query Internet exposure cycle count trend statistics.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExposureTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExposureTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExposures(
            self,
            request: models.DescribeExposuresRequest,
            opts: Dict = None,
    ) -> models.DescribeExposuresResponse:
        """
        Cloud boundary analysis asset list
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
        Query the high-risk baseline risk list of host nodes under the cloud boundary analysis exposed path.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHighBaseLineRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHighBaseLineRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostKBRiskList(
            self,
            request: models.DescribeHostKBRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeHostKBRiskListResponse:
        """
        Search the host kb risk list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostKBRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostKBRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostVulItemVPRInfo(
            self,
            request: models.DescribeHostVulItemVPRInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeHostVulItemVPRInfoResponse:
        """
        This API is used to obtain host vulnerability VPR information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostVulItemVPRInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostVulItemVPRInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostVulOverview(
            self,
            request: models.DescribeHostVulOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeHostVulOverviewResponse:
        """
        This API is used to obtain the host vulnerability overview.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostVulOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostVulOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostVulRiskList(
            self,
            request: models.DescribeHostVulRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeHostVulRiskListResponse:
        """
        This API is used to retrieve the host vulnerability risk list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostVulRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostVulRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIaCFileList(
            self,
            request: models.DescribeIaCFileListRequest,
            opts: Dict = None,
    ) -> models.DescribeIaCFileListResponse:
        """
        Retrieve the IaC detection file list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIaCFileList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIaCFileListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIaCFileOverview(
            self,
            request: models.DescribeIaCFileOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeIaCFileOverviewResponse:
        """
        Obtain the IaC detection file overview.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIaCFileOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIaCFileOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIaCFileReport(
            self,
            request: models.DescribeIaCFileReportRequest,
            opts: Dict = None,
    ) -> models.DescribeIaCFileReportResponse:
        """
        Obtain the IaC detection file report.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIaCFileReport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIaCFileReportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIaCTokenList(
            self,
            request: models.DescribeIaCTokenListRequest,
            opts: Dict = None,
    ) -> models.DescribeIaCTokenListResponse:
        """
        This API is used to search the IaC detection integration Token list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIaCTokenList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIaCTokenListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageAssetDetail(
            self,
            request: models.DescribeImageAssetDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeImageAssetDetailResponse:
        """
        Queries image asset details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageAssetDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageAssetDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageAssetList(
            self,
            request: models.DescribeImageAssetListRequest,
            opts: Dict = None,
    ) -> models.DescribeImageAssetListResponse:
        """
        Query the image asset list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageAssetList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageAssetListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageAssociatedAssetCount(
            self,
            request: models.DescribeImageAssociatedAssetCountRequest,
            opts: Dict = None,
    ) -> models.DescribeImageAssociatedAssetCountResponse:
        """
        Query the number of related assets of an image.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageAssociatedAssetCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageAssociatedAssetCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageAssociatedContainerList(
            self,
            request: models.DescribeImageAssociatedContainerListRequest,
            opts: Dict = None,
    ) -> models.DescribeImageAssociatedContainerListResponse:
        """
        Queries the container assets associated with an image.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageAssociatedContainerList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageAssociatedContainerListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageAssociatedHostList(
            self,
            request: models.DescribeImageAssociatedHostListRequest,
            opts: Dict = None,
    ) -> models.DescribeImageAssociatedHostListResponse:
        """
        Query the asset list of hosts associated with the image.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageAssociatedHostList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageAssociatedHostListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageComponentList(
            self,
            request: models.DescribeImageComponentListRequest,
            opts: Dict = None,
    ) -> models.DescribeImageComponentListResponse:
        """
        Queries the image component list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageComponentList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageComponentListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageExportJobList(
            self,
            request: models.DescribeImageExportJobListRequest,
            opts: Dict = None,
    ) -> models.DescribeImageExportJobListResponse:
        """
        Queries the image repository export task list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageExportJobList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageExportJobListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageLayerList(
            self,
            request: models.DescribeImageLayerListRequest,
            opts: Dict = None,
    ) -> models.DescribeImageLayerListResponse:
        """
        Query the image layer information list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageLayerList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageLayerListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageLayerVulList(
            self,
            request: models.DescribeImageLayerVulListRequest,
            opts: Dict = None,
    ) -> models.DescribeImageLayerVulListResponse:
        """
        Queries the list of vulnerabilities in an image layer
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageLayerVulList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageLayerVulListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageRegistryAssetOverview(
            self,
            request: models.DescribeImageRegistryAssetOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeImageRegistryAssetOverviewResponse:
        """
        Query the repository asset overview of images
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageRegistryAssetOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageRegistryAssetOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageRegistryConnectivityTaskResult(
            self,
            request: models.DescribeImageRegistryConnectivityTaskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeImageRegistryConnectivityTaskResultResponse:
        """
        Query the connectivity check task result of an image repository.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageRegistryConnectivityTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageRegistryConnectivityTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageRegistryList(
            self,
            request: models.DescribeImageRegistryListRequest,
            opts: Dict = None,
    ) -> models.DescribeImageRegistryListResponse:
        """
        This API is used to query the image repository list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageRegistryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageRegistryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageRegistryNamespaceList(
            self,
            request: models.DescribeImageRegistryNamespaceListRequest,
            opts: Dict = None,
    ) -> models.DescribeImageRegistryNamespaceListResponse:
        """
        This API is used to query the mirror repository namespace list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageRegistryNamespaceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageRegistryNamespaceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageRegistryScanSubTaskList(
            self,
            request: models.DescribeImageRegistryScanSubTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeImageRegistryScanSubTaskListResponse:
        """
        Query subtask information of image repository scanning
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageRegistryScanSubTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageRegistryScanSubTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageRegistryScanTaskList(
            self,
            request: models.DescribeImageRegistryScanTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeImageRegistryScanTaskListResponse:
        """
        Query the image repository scan task list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageRegistryScanTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageRegistryScanTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageRegistryTimedScanTaskConfig(
            self,
            request: models.DescribeImageRegistryTimedScanTaskConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeImageRegistryTimedScanTaskConfigResponse:
        """
        View the scheduled scan task configuration of a mirror repository
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageRegistryTimedScanTaskConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageRegistryTimedScanTaskConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageRegistryTimedScanTaskPreview(
            self,
            request: models.DescribeImageRegistryTimedScanTaskPreviewRequest,
            opts: Dict = None,
    ) -> models.DescribeImageRegistryTimedScanTaskPreviewResponse:
        """
        Query the preview of a scheduled scan task in the mirror repository
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageRegistryTimedScanTaskPreview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageRegistryTimedScanTaskPreviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageSensitiveInfoList(
            self,
            request: models.DescribeImageSensitiveInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeImageSensitiveInfoListResponse:
        """
        Query the sensitive information list of an image
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageSensitiveInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageSensitiveInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageSensitiveWhitelist(
            self,
            request: models.DescribeImageSensitiveWhitelistRequest,
            opts: Dict = None,
    ) -> models.DescribeImageSensitiveWhitelistResponse:
        """
        Query the sensitive information allowlist for container images
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageSensitiveWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageSensitiveWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageVirusList(
            self,
            request: models.DescribeImageVirusListRequest,
            opts: Dict = None,
    ) -> models.DescribeImageVirusListResponse:
        """
        Queries the Trojan virus list of an image
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageVirusList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageVirusListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageVirusWhitelist(
            self,
            request: models.DescribeImageVirusWhitelistRequest,
            opts: Dict = None,
    ) -> models.DescribeImageVirusWhitelistResponse:
        """
        This API is used to query the Trojan allowlist of an image.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageVirusWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageVirusWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageVirusWhitelistDetail(
            self,
            request: models.DescribeImageVirusWhitelistDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeImageVirusWhitelistDetailResponse:
        """
        Queries the detailed information of the Trojan allowlist of an image.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageVirusWhitelistDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageVirusWhitelistDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageVulList(
            self,
            request: models.DescribeImageVulListRequest,
            opts: Dict = None,
    ) -> models.DescribeImageVulListResponse:
        """
        This API is used to query the image vulnerability list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageVulList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageVulListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageVulSummaryList(
            self,
            request: models.DescribeImageVulSummaryListRequest,
            opts: Dict = None,
    ) -> models.DescribeImageVulSummaryListResponse:
        """
        Queries the image vulnerability overview list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageVulSummaryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageVulSummaryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageVulWhitelist(
            self,
            request: models.DescribeImageVulWhitelistRequest,
            opts: Dict = None,
    ) -> models.DescribeImageVulWhitelistResponse:
        """
        This API is used to query the vulnerability allowlist of a container image.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageVulWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageVulWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKBDetail(
            self,
            request: models.DescribeKBDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeKBDetailResponse:
        """
        Query the details of a single Windows KB patch based on the user's input KB internal ID, and return the basic KB info, release time, whether restart is required, as well as the list of vulnerabilities associated with the KB.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKBDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKBDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKBUpdatableMachineList(
            self,
            request: models.DescribeKBUpdatableMachineListRequest,
            opts: Dict = None,
    ) -> models.DescribeKBUpdatableMachineListResponse:
        """
        Query the list of hosts that can update a specified KB patch. This API is used for Windows patch repair scenarios to query which hosts lack the patch and support auto-update before user-submitted KB patch update tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKBUpdatableMachineList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKBUpdatableMachineListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKeySandboxCredential(
            self,
            request: models.DescribeKeySandboxCredentialRequest,
            opts: Dict = None,
    ) -> models.DescribeKeySandboxCredentialResponse:
        """
        This API is used to query credential details and return credential metadata and masked credential data. The access type returns an Access array (original Key, masked Value), and the sts type returns an STS object (original System, masked SecretID and SecretKey).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKeySandboxCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKeySandboxCredentialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKeySandboxCredentialList(
            self,
            request: models.DescribeKeySandboxCredentialListRequest,
            opts: Dict = None,
    ) -> models.DescribeKeySandboxCredentialListResponse:
        """
        Query the voucher list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKeySandboxCredentialList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKeySandboxCredentialListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLastScanTaskInfo(
            self,
            request: models.DescribeLastScanTaskInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeLastScanTaskInfoResponse:
        """
        Get last check-now task info
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLastScanTaskInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLastScanTaskInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLicenseStatus(
            self,
            request: models.DescribeLicenseStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeLicenseStatusResponse:
        """
        Queries the overall status of all valid authorizations under the current account, returns total count, used, remaining, and expiry time grouped by billing item, and also returns the auto-purchase switch status and merged remaining unbind count. The output sequence is fixed as: flagship edition → pro edition → RASP → other.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLicenseStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLicenseStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLighthouseFirewallRules(
            self,
            request: models.DescribeLighthouseFirewallRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeLighthouseFirewallRulesResponse:
        """
        Query the firewall rules of a lightweight application server
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLighthouseFirewallRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLighthouseFirewallRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListenerList(
            self,
            request: models.DescribeListenerListRequest,
            opts: Dict = None,
    ) -> models.DescribeListenerListResponse:
        """
        Query CLB Listener List
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListenerList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListenerListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoginTypeGlobalConf(
            self,
            request: models.DescribeLoginTypeGlobalConfRequest,
            opts: Dict = None,
    ) -> models.DescribeLoginTypeGlobalConfResponse:
        """
        This API is used to obtain the global configuration for anti-uninstallation.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoginTypeGlobalConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoginTypeGlobalConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoginTypeHost(
            self,
            request: models.DescribeLoginTypeHostRequest,
            opts: Dict = None,
    ) -> models.DescribeLoginTypeHostResponse:
        """
        Get the host list for QR code log-in
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoginTypeHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoginTypeHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoginWhiteCombinedList(
            self,
            request: models.DescribeLoginWhiteCombinedListRequest,
            opts: Dict = None,
    ) -> models.DescribeLoginWhiteCombinedListResponse:
        """
        This API is used to obtain the list of cross-region log-in allowlists after merge.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoginWhiteCombinedList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoginWhiteCombinedListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoginWhiteHostList(
            self,
            request: models.DescribeLoginWhiteHostListRequest,
            opts: Dict = None,
    ) -> models.DescribeLoginWhiteHostListResponse:
        """
        This API is used to query the list of allowlisted machines after merge.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoginWhiteHostList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoginWhiteHostListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineClearHistory(
            self,
            request: models.DescribeMachineClearHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineClearHistoryResponse:
        """
        This API is used to query the clearing history records of a machine.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineClearHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineClearHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineGeneral(
            self,
            request: models.DescribeMachineGeneralRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineGeneralResponse:
        """
        This API is used to query the information of the host overview.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineGeneral"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineGeneralResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineLoginType(
            self,
            request: models.DescribeMachineLoginTypeRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineLoginTypeResponse:
        """
        This API is used to obtain the host login method.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineLoginType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineLoginTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMalwareTimingScanSetting(
            self,
            request: models.DescribeMalwareTimingScanSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeMalwareTimingScanSettingResponse:
        """
        This API is used to query the scheduled scan configuration for file scan and removal.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMalwareTimingScanSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMalwareTimingScanSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMandatoryVulSet(
            self,
            request: models.DescribeMandatoryVulSetRequest,
            opts: Dict = None,
    ) -> models.DescribeMandatoryVulSetResponse:
        """
        Show mandatory vulnerability intelligence for businesses.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMandatoryVulSet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMandatoryVulSetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModifyMachinesLoginTypeTasks(
            self,
            request: models.DescribeModifyMachinesLoginTypeTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeModifyMachinesLoginTypeTasksResponse:
        """
        This API is used to obtain a list of batch tasks for modification of host login methods.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModifyMachinesLoginTypeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModifyMachinesLoginTypeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMultiCloudAssetCount(
            self,
            request: models.DescribeMultiCloudAssetCountRequest,
            opts: Dict = None,
    ) -> models.DescribeMultiCloudAssetCountResponse:
        """
        Retrieve the total number of assets integrated across multiple clouds (Tencent Cloud, Alibaba Cloud, AWS, Huawei Cloud, Azure, etc.) and the details of asset counts for each cloud service provider.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMultiCloudAssetCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMultiCloudAssetCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNFSScanConf(
            self,
            request: models.DescribeNFSScanConfRequest,
            opts: Dict = None,
    ) -> models.DescribeNFSScanConfResponse:
        """
        This API is used to obtain the global configuration for NFS scanning.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNFSScanConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNFSScanConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNFSScanHost(
            self,
            request: models.DescribeNFSScanHostRequest,
            opts: Dict = None,
    ) -> models.DescribeNFSScanHostResponse:
        """
        This API is used to query the host list for QR code log-in.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNFSScanHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNFSScanHostResponse
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
        
    async def DescribeNatRules(
            self,
            request: models.DescribeNatRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeNatRulesResponse:
        """
        Query the nat policy corresponding to a Tencent Cloud nat gateway instance
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetAttackSetting(
            self,
            request: models.DescribeNetAttackSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeNetAttackSettingResponse:
        """
        Query the cyber attack detection switch and asset scope configuration
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetAttackSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetAttackSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNotifyAgentOfflineDuration(
            self,
            request: models.DescribeNotifyAgentOfflineDurationRequest,
            opts: Dict = None,
    ) -> models.DescribeNotifyAgentOfflineDurationResponse:
        """
        Query client offline duration
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNotifyAgentOfflineDuration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNotifyAgentOfflineDurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNotifyAssetConfig(
            self,
            request: models.DescribeNotifyAssetConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeNotifyAssetConfigResponse:
        """
        Get the notification asset scope configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNotifyAssetConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNotifyAssetConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNotifySetting(
            self,
            request: models.DescribeNotifySettingRequest,
            opts: Dict = None,
    ) -> models.DescribeNotifySettingResponse:
        """
        Get notification settings
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNotifySetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNotifySettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNotifySettingAk(
            self,
            request: models.DescribeNotifySettingAkRequest,
            opts: Dict = None,
    ) -> models.DescribeNotifySettingAkResponse:
        """
        Gets notification settings for risk governance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNotifySettingAk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNotifySettingAkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNotifySettingAlert(
            self,
            request: models.DescribeNotifySettingAlertRequest,
            opts: Dict = None,
    ) -> models.DescribeNotifySettingAlertResponse:
        """
        This API is used to obtain advanced configurations for alarm center notifications.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNotifySettingAlert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNotifySettingAlertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganizationInfo(
            self,
            request: models.DescribeOrganizationInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationInfoResponse:
        """
        Query Group Account Details
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
        Query Group Account User List
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
        Asset list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOtherCloudAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOtherCloudAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePodContainerList(
            self,
            request: models.DescribePodContainerListRequest,
            opts: Dict = None,
    ) -> models.DescribePodContainerListResponse:
        """
        Query the container list associated with a Pod
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePodContainerList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePodContainerListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePortDetectList(
            self,
            request: models.DescribePortDetectListRequest,
            opts: Dict = None,
    ) -> models.DescribePortDetectListResponse:
        """
        Port detection list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePortDetectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePortDetectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePortScanTaskCount(
            self,
            request: models.DescribePortScanTaskCountRequest,
            opts: Dict = None,
    ) -> models.DescribePortScanTaskCountResponse:
        """
        Query the number of port scanning tasks under the current account.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePortScanTaskCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePortScanTaskCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePreventUninstallGlobalConf(
            self,
            request: models.DescribePreventUninstallGlobalConfRequest,
            opts: Dict = None,
    ) -> models.DescribePreventUninstallGlobalConfResponse:
        """
        This API is used to obtain the global configuration for anti-uninstallation.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePreventUninstallGlobalConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePreventUninstallGlobalConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePreventUninstallHost(
            self,
            request: models.DescribePreventUninstallHostRequest,
            opts: Dict = None,
    ) -> models.DescribePreventUninstallHostResponse:
        """
        Retrieve the host list for uninstallation prevention.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePreventUninstallHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePreventUninstallHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProcessDaemonGlobalConf(
            self,
            request: models.DescribeProcessDaemonGlobalConfRequest,
            opts: Dict = None,
    ) -> models.DescribeProcessDaemonGlobalConfResponse:
        """
        Obtain the global configuration for process protection.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProcessDaemonGlobalConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProcessDaemonGlobalConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProcessDaemonHost(
            self,
            request: models.DescribeProcessDaemonHostRequest,
            opts: Dict = None,
    ) -> models.DescribeProcessDaemonHostResponse:
        """
        Get the process daemon host list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProcessDaemonHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProcessDaemonHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublicCloudAssets(
            self,
            request: models.DescribePublicCloudAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribePublicCloudAssetsResponse:
        """
        Public network asset
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublicCloudAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublicCloudAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublicIpAssets(
            self,
            request: models.DescribePublicIpAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribePublicIpAssetsResponse:
        """
        IP Public Network List
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublicIpAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublicIpAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRaspLicenseList(
            self,
            request: models.DescribeRaspLicenseListRequest,
            opts: Dict = None,
    ) -> models.DescribeRaspLicenseListResponse:
        """
        This API is used to query the authorization list for application protection.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRaspLicenseList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRaspLicenseListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegistryOverview(
            self,
            request: models.DescribeRegistryOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeRegistryOverviewResponse:
        """
        Query repository overview
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegistryOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegistryOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegistryRegionList(
            self,
            request: models.DescribeRegistryRegionListRequest,
            opts: Dict = None,
    ) -> models.DescribeRegistryRegionListResponse:
        """
        Queries the region list of an image repository.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegistryRegionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegistryRegionListResponse
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
        
    async def DescribeReverseShellSystemPolicyConfig(
            self,
            request: models.DescribeReverseShellSystemPolicyConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeReverseShellSystemPolicyConfigResponse:
        """
        This API is used to query the intranet alert and asset scope configuration for rebound Shell.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReverseShellSystemPolicyConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReverseShellSystemPolicyConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskCallRecord(
            self,
            request: models.DescribeRiskCallRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskCallRecordResponse:
        """
        This API is used to obtain the risk call record list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskCallRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskCallRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskCenterAssetViewCFGRiskList(
            self,
            request: models.DescribeRiskCenterAssetViewCFGRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskCenterAssetViewCFGRiskListResponse:
        """
        Obtain Configuration Risk List from Asset's Perspective
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
        Obtain Port Risk List from Asset's Perspective
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
        Obtain Vulnerability Risk List from Asset's Perspective
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
        Obtain Weak Password Risk List from Asset's Perspective
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
        Obtain Port Risk List from Port's Perspective
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskCenterPortViewPortRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskCenterPortViewPortRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskCenterRiskTrendAnalysis(
            self,
            request: models.DescribeRiskCenterRiskTrendAnalysisRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskCenterRiskTrendAnalysisResponse:
        """
        Sample code for obtaining risk trend analysis
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskCenterRiskTrendAnalysis"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskCenterRiskTrendAnalysisResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskCenterServerRiskList(
            self,
            request: models.DescribeRiskCenterServerRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskCenterServerRiskListResponse:
        """
        Obtain Risk Service List
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
        Obtain Vulnerability Risk List from Vulnerability's Perspective
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
        Obtain Content Risk List
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskCenterWebsiteRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskCenterWebsiteRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskDetailList(
            self,
            request: models.DescribeRiskDetailListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskDetailListResponse:
        """
        Sample risk detail list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskDetailList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskDetailListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskRuleDetail(
            self,
            request: models.DescribeRiskRuleDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskRuleDetailResponse:
        """
        Sample code for querying risk rule details
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskRuleDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskRuleDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskRules(
            self,
            request: models.DescribeRiskRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskRulesResponse:
        """
        Illustrative example of the advanced configuration risk rule list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskScanCronConfig(
            self,
            request: models.DescribeRiskScanCronConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskScanCronConfigResponse:
        """
        Get the periodic schedule for risk scans
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskScanCronConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskScanCronConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSCFAliasList(
            self,
            request: models.DescribeSCFAliasListRequest,
            opts: Dict = None,
    ) -> models.DescribeSCFAliasListResponse:
        """
        Queries the alias list of a specified SCF function.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSCFAliasList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSCFAliasListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSCFFunctionList(
            self,
            request: models.DescribeSCFFunctionListRequest,
            opts: Dict = None,
    ) -> models.DescribeSCFFunctionListResponse:
        """
        Query the list of SCF functions in the specified namespace. Only functions of the Event trigger type are returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSCFFunctionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSCFFunctionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSCFFunctionVersionList(
            self,
            request: models.DescribeSCFFunctionVersionListRequest,
            opts: Dict = None,
    ) -> models.DescribeSCFFunctionVersionListResponse:
        """
        Queries the version list of a specified SCF function.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSCFFunctionVersionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSCFFunctionVersionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSCFNamespaceList(
            self,
            request: models.DescribeSCFNamespaceListRequest,
            opts: Dict = None,
    ) -> models.DescribeSCFNamespaceListResponse:
        """
        Queries the namespace list of SCF in the designated region for the current user.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSCFNamespaceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSCFNamespaceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSandboxACLAlertList(
            self,
            request: models.DescribeSandboxACLAlertListRequest,
            opts: Dict = None,
    ) -> models.DescribeSandboxACLAlertListResponse:
        """
        This API is used to query the ACL access control alarm log list by paging. It supports precise filtering of a single alarm by Filter.Name=ID for the details page scenario.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSandboxACLAlertList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSandboxACLAlertListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSandboxACLRuleList(
            self,
            request: models.DescribeSandboxACLRuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeSandboxACLRuleListResponse:
        """
        This API is used to query the access control rule list for ACL users under the current tenant. Import Filter.Name=RuleID to query an individual rule precisely.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSandboxACLRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSandboxACLRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSandboxACLSystemRuleList(
            self,
            request: models.DescribeSandboxACLSystemRuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeSandboxACLSystemRuleListResponse:
        """
        Queries the traffic sandbox access control (ACL) system rule list. System rules are built into the CSIP platform and can be referenced by user rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSandboxACLSystemRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSandboxACLSystemRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSandboxDLPAlertList(
            self,
            request: models.DescribeSandboxDLPAlertListRequest,
            opts: Dict = None,
    ) -> models.DescribeSandboxDLPAlertListResponse:
        """
        Paging query for the DLP data leakage alert log list. Supports precise filtering of a single alert by Filter.Name=ID for the details page scenario.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSandboxDLPAlertList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSandboxDLPAlertListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSandboxDLPRuleList(
            self,
            request: models.DescribeSandboxDLPRuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeSandboxDLPRuleListResponse:
        """
        Query the DLP user rule list of the current tenant. Input Filter.Name=RuleID to query an individual rule for the details page scenario.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSandboxDLPRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSandboxDLPRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSandboxDLPSystemRuleList(
            self,
            request: models.DescribeSandboxDLPSystemRuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeSandboxDLPSystemRuleListResponse:
        """
        Queries the traffic sandbox data leakage protection (DLP) system rule list. System rules are built into the CSIP platform and can be referenced by user rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSandboxDLPSystemRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSandboxDLPSystemRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSandboxFileRuleList(
            self,
            request: models.DescribeSandboxFileRuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeSandboxFileRuleListResponse:
        """
        Query the command sandbox file rule list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSandboxFileRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSandboxFileRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSandboxLLMAuditAlertList(
            self,
            request: models.DescribeSandboxLLMAuditAlertListRequest,
            opts: Dict = None,
    ) -> models.DescribeSandboxLLMAuditAlertListResponse:
        """
        Paging query for the LLM audit alarm log list. Supports precise filtering of a single alarm by Filter.Name=ID for the details page scenario.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSandboxLLMAuditAlertList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSandboxLLMAuditAlertListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSandboxLLMAuditRuleList(
            self,
            request: models.DescribeSandboxLLMAuditRuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeSandboxLLMAuditRuleListResponse:
        """
        Queries the LLM audit user rule list for the current tenant. LLM audit rules do not support user-defined content and can only refer to system rule composites. Import Filter.Name=RuleID for exact querying of an individual rule (for details page scenarios).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSandboxLLMAuditRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSandboxLLMAuditRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSandboxLLMAuditSystemRuleList(
            self,
            request: models.DescribeSandboxLLMAuditSystemRuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeSandboxLLMAuditSystemRuleListResponse:
        """
        This API is used to query the rule list of the LLM audit system. System rules are built into the CSIP platform and originate from the LLM audit system rule base. They are split into two flat rule arrays by LLM reasoning protection and ToolCall protection and can be referenced by user rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSandboxLLMAuditSystemRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSandboxLLMAuditSystemRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanReportList(
            self,
            request: models.DescribeScanReportListRequest,
            opts: Dict = None,
    ) -> models.DescribeScanReportListResponse:
        """
        Obtain Scan Report List
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
        This API is used to query result statistics of cloud boundary analysis scans.
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
        Obtain Scan Task List
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanTaskRecordList(
            self,
            request: models.DescribeScanTaskRecordListRequest,
            opts: Dict = None,
    ) -> models.DescribeScanTaskRecordListResponse:
        """
        This API is used to query the scan task record list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanTaskRecordList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanTaskRecordListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScfCustomDomainEndpoints(
            self,
            request: models.DescribeScfCustomDomainEndpointsRequest,
            opts: Dict = None,
    ) -> models.DescribeScfCustomDomainEndpointsResponse:
        """
        Query the list of custom domain name endpoints for Tencent Cloud SCF
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScfCustomDomainEndpoints"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScfCustomDomainEndpointsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSearchBugInfo(
            self,
            request: models.DescribeSearchBugInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSearchBugInfoResponse:
        """
        Query vulnerability information in the three-dimensional protection center.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSearchBugInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSearchBugInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroupPolicy(
            self,
            request: models.DescribeSecurityGroupPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupPolicyResponse:
        """
        Query the security group rules correspond to the specified security group ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroupPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityRiskTrend(
            self,
            request: models.DescribeSecurityRiskTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityRiskTrendResponse:
        """
        This API is used to obtain security risk trends and return the daily number of risks grouped by dimension.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityRiskTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityRiskTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityScoreOverview(
            self,
            request: models.DescribeSecurityScoreOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityScoreOverviewResponse:
        """
        This API is used to obtain the security score overview and real-time compute point deductions in each dimension and sub-item.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityScoreOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityScoreOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityScoreRule(
            self,
            request: models.DescribeSecurityScoreRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityScoreRuleResponse:
        """
        Retrieve the security scoring rules for the current account. If no custom rules exist, return the built-in default.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityScoreRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityScoreRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSkillScanAlertDetail(
            self,
            request: models.DescribeSkillScanAlertDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeSkillScanAlertDetailResponse:
        """
        This API is used to query Skill security detection alarm details, including local alarm information and engine real-time detection data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSkillScanAlertDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSkillScanAlertDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSkillScanAlertList(
            self,
            request: models.DescribeSkillScanAlertListRequest,
            opts: Dict = None,
    ) -> models.DescribeSkillScanAlertListResponse:
        """
        Queries the Skill security detection alarm list with pagination, filtering, and sorting supported.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSkillScanAlertList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSkillScanAlertListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSkillScanPayInfo(
            self,
            request: models.DescribeSkillScanPayInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSkillScanPayInfoResponse:
        """
        This API is used to query Skill security detection billing information, including order status, total quota, consumed quota, expiration time, and payment mode. If no order exists, zero values are returned (only TimeNow and BetaEndTime). Trial orders are claimed through ModifyTrialStatus(Module=9), and official orders are created through the billing system.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSkillScanPayInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSkillScanPayInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSkillScanResult(
            self,
            request: models.DescribeSkillScanResultRequest,
            opts: Dict = None,
    ) -> models.DescribeSkillScanResultResponse:
        """
        Queries the security detection result of a skill. After calling CreateSkillScan successfully, use the returned ContentHash + EngineVersion to poll this API to obtain the result. We recommend polling for the first time 5 minutes after a successful upload. If detection is not completed, poll once every 1 minute afterward. The response uses the Status field to distinguish four statuses: detection completed (SUCCESS), detecting (SCANNING), no record (NOT_FOUND), and detection failed (FAILED). Note: Detection results are retained for 90 days. NOT_FOUND will be returned after they expire.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSkillScanResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSkillScanResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSourceIPAsset(
            self,
            request: models.DescribeSourceIPAssetRequest,
            opts: Dict = None,
    ) -> models.DescribeSourceIPAssetResponse:
        """
        Retrieve the user access key asset list from an IP perspective.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSourceIPAsset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSourceIPAssetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSourceIPDetail(
            self,
            request: models.DescribeSourceIPDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeSourceIPDetailResponse:
        """
        This API is used to query user access key asset list from source IP perspective.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSourceIPDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSourceIPDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubUserInfo(
            self,
            request: models.DescribeSubUserInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSubUserInfoResponse:
        """
        Query the sub-account list of a group
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
        Obtain Subnet List
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubnetAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubnetAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTCRInstanceList(
            self,
            request: models.DescribeTCRInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeTCRInstanceListResponse:
        """
        This API is used to obtain the TCR instance list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTCRInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTCRInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTagRuleAssets(
            self,
            request: models.DescribeTagRuleAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeTagRuleAssetsResponse:
        """
        Tagging policy enforcement asset list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTagRuleAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagRuleAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskLogList(
            self,
            request: models.DescribeTaskLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskLogListResponse:
        """
        Obtain Task Scan Report List
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
        Obtain the Temporary Link for Report Download
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskLogURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskLogURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskPredictCostQuota(
            self,
            request: models.DescribeTaskPredictCostQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskPredictCostQuotaResponse:
        """
        Obtain the pre-consumed quota for scans.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskPredictCostQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskPredictCostQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopAttackInfo(
            self,
            request: models.DescribeTopAttackInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeTopAttackInfoResponse:
        """
        Query TOP attack information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopAttackInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopAttackInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUebaBehaviorSummary(
            self,
            request: models.DescribeUebaBehaviorSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeUebaBehaviorSummaryResponse:
        """
        Queries the behavior overview of user behavior analysis.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUebaBehaviorSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUebaBehaviorSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUebaRule(
            self,
            request: models.DescribeUebaRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeUebaRuleResponse:
        """
        Query the list of user behavior analysis policies
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUebaRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUebaRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUebaUserSummary(
            self,
            request: models.DescribeUebaUserSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeUebaUserSummaryResponse:
        """
        This API is used to get the user overview of the user behavior analysis module.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUebaUserSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUebaUserSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserAKInfoList(
            self,
            request: models.DescribeUserAKInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeUserAKInfoListResponse:
        """
        Obtain AK information of the account
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserAKInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserAKInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserCSPMInfoList(
            self,
            request: models.DescribeUserCSPMInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeUserCSPMInfoListResponse:
        """
        This API is used to obtain CSPM information of an account.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserCSPMInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserCSPMInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserCallRecord(
            self,
            request: models.DescribeUserCallRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeUserCallRecordResponse:
        """
        This API is used to obtain the account call record list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserCallRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserCallRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserDspmInfoList(
            self,
            request: models.DescribeUserDspmInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeUserDspmInfoListResponse:
        """
        Get the dspm information list of an account
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserDspmInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserDspmInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserInfo(
            self,
            request: models.DescribeUserInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeUserInfoResponse:
        """
        CSPM quota information of a user
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVULList(
            self,
            request: models.DescribeVULListRequest,
            opts: Dict = None,
    ) -> models.DescribeVULListResponse:
        """
        Vulnerability list in the risk center of the new security center
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
        Query Vulnerability Risk Advanced Configuration
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
        Retrieve vulnerability details
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVULRiskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVULRiskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVdbAndPocInfo(
            self,
            request: models.DescribeVdbAndPocInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeVdbAndPocInfoResponse:
        """
        This API is used to obtain virus database and POC updates.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVdbAndPocInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVdbAndPocInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVoucherEligibility(
            self,
            request: models.DescribeVoucherEligibilityRequest,
            opts: Dict = None,
    ) -> models.DescribeVoucherEligibilityResponse:
        """
        Check whether the current user is eligible to claim vouchers for the designated promotion.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVoucherEligibility"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVoucherEligibilityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcAssets(
            self,
            request: models.DescribeVpcAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcAssetsResponse:
        """
        Obtain VPC List
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulComponentRelateHost(
            self,
            request: models.DescribeVulComponentRelateHostRequest,
            opts: Dict = None,
    ) -> models.DescribeVulComponentRelateHostResponse:
        """
        This API is used to query the associated server of a vulnerable component.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulComponentRelateHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulComponentRelateHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulFixTaskDetail(
            self,
            request: models.DescribeVulFixTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeVulFixTaskDetailResponse:
        """
        This API is used to query the details of a specified vulnerability repair task, including detailed data such as remediation status and snapshot status for each host, and supports pagination and filtering.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulFixTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulFixTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulFixTaskList(
            self,
            request: models.DescribeVulFixTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulFixTaskListResponse:
        """
        This API is used to query the vulnerability repair task record list with paging, support by conditional filtering such as remediation status and time range, and show summary information for each repair task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulFixTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulFixTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulFixableMachineList(
            self,
            request: models.DescribeVulFixableMachineListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulFixableMachineListResponse:
        """
        This API is used to query the host list where specified vulnerabilities can be repaired. Before a user submits a repair task, it is necessary to query which hosts support automatic fix, providing data support for users to select repair targets.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulFixableMachineList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulFixableMachineListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulFixedHostDetail(
            self,
            request: models.DescribeVulFixedHostDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeVulFixedHostDetailResponse:
        """
        This API is used to query the repair details of a certain fixed vulnerability on a specified host, including basic information about the vulnerability, repair host information, and a detailed list of associated components and paths (component name, version number hit, associated path, repair command).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulFixedHostDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulFixedHostDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulFixedList(
            self,
            request: models.DescribeVulFixedListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulFixedListResponse:
        """
        This API is used to query the list of repaired vulnerabilities, show vulnerability information with successful fixes and statistics on repair conditions, helping users understand the repair results.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulFixedList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulFixedListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulHostRelateComponent(
            self,
            request: models.DescribeVulHostRelateComponentRequest,
            opts: Dict = None,
    ) -> models.DescribeVulHostRelateComponentResponse:
        """
        This API is used to query host-associated vulnerability components.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulHostRelateComponent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulHostRelateComponentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulIgnoreRuleList(
            self,
            request: models.DescribeVulIgnoreRuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulIgnoreRuleListResponse:
        """
        This API is used to retrieve the vulnerability ignore list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulIgnoreRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulIgnoreRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulItemList(
            self,
            request: models.DescribeVulItemListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulItemListResponse:
        """
        This API is used to obtain vulnerability list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulItemList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulItemListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulLabelList(
            self,
            request: models.DescribeVulLabelListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulLabelListResponse:
        """
        Obtains the vulnerability tag list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulLabelList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulLabelListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulRiskList(
            self,
            request: models.DescribeVulRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulRiskListResponse:
        """
        Query the list of vulnerabilities on host nodes under the exposed path in cloud boundary analysis.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulRiskRelateComponent(
            self,
            request: models.DescribeVulRiskRelateComponentRequest,
            opts: Dict = None,
    ) -> models.DescribeVulRiskRelateComponentResponse:
        """
        Retrieve the associated component of a vulnerability
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulRiskRelateComponent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulRiskRelateComponentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulRiskRelateHost(
            self,
            request: models.DescribeVulRiskRelateHostRequest,
            opts: Dict = None,
    ) -> models.DescribeVulRiskRelateHostResponse:
        """
        Search for hosts associated with vulnerabilities or KBs
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulRiskRelateHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulRiskRelateHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulScanPeriodic(
            self,
            request: models.DescribeVulScanPeriodicRequest,
            opts: Dict = None,
    ) -> models.DescribeVulScanPeriodicResponse:
        """
        This API is used to obtain vulnerability scanning (period scanning).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulScanPeriodic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulScanPeriodicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulScanTaskDetail(
            self,
            request: models.DescribeVulScanTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeVulScanTaskDetailResponse:
        """
        This API is used to retrieve vulnerability scanning task detail
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulScanTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulScanTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulScanTaskList(
            self,
            request: models.DescribeVulScanTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulScanTaskListResponse:
        """
        This API is used to search vulnerability scanning task history
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulScanTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulScanTaskListResponse
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
        
    async def DescribeWebhookPolicyList(
            self,
            request: models.DescribeWebhookPolicyListRequest,
            opts: Dict = None,
    ) -> models.DescribeWebhookPolicyListResponse:
        """
        This API is used to query the notification policy list for the current tenant by page, corresponding to the table on the Notification Policy Configuration Tab in Notification Center - Robot Notification. The returned fields are simplified info required for row display. Use DescribeWebhookPolicy for complete configuration in editing scenarios. Each tenant can have up to 100 notification policies.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebhookPolicyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebhookPolicyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebhookReceiverList(
            self,
            request: models.DescribeWebhookReceiverListRequest,
            opts: Dict = None,
    ) -> models.DescribeWebhookReceiverListResponse:
        """
        This API is used to query the list of receiving robots for the current tenant by page, corresponding to the table on the Receive Bot Management Tab in Notification Center - Robot Notification. Each tenant can have up to 50 robots.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebhookReceiverList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebhookReceiverListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableAISchedule(
            self,
            request: models.DisableAIScheduleRequest,
            opts: Dict = None,
    ) -> models.DisableAIScheduleResponse:
        """
        Disable scheduled AI tasks.

        Set the status of the specified AI scheduled task to disabled. After it is disabled, the task will suspend automatic execution.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableAISchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableAIScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DownloadDspmExportLog(
            self,
            request: models.DownloadDspmExportLogRequest,
            opts: Dict = None,
    ) -> models.DownloadDspmExportLogResponse:
        """
        This API is used to download export logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DownloadDspmExportLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DownloadDspmExportLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableAISchedule(
            self,
            request: models.EnableAIScheduleRequest,
            opts: Dict = None,
    ) -> models.EnableAIScheduleResponse:
        """
        Enable AI scheduled tasks.

        Set the status of the specified AI scheduled task to enabled. After it is enabled, the task will automatically execute based on the trigger configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableAISchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableAIScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportCSIPMalwareScanTaskDetail(
            self,
            request: models.ExportCSIPMalwareScanTaskDetailRequest,
            opts: Dict = None,
    ) -> models.ExportCSIPMalwareScanTaskDetailResponse:
        """
        Exports host details of a CSIP scan task to Excel files. This API is used to query the download link through DescribeExportMachines after asynchronous generation.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportCSIPMalwareScanTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportCSIPMalwareScanTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportClientSettingHostList(
            self,
            request: models.ExportClientSettingHostListRequest,
            opts: Dict = None,
    ) -> models.ExportClientSettingHostListResponse:
        """
        Export the host list for client settings.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportClientSettingHostList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportClientSettingHostListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportEDRRules(
            self,
            request: models.ExportEDRRulesRequest,
            opts: Dict = None,
    ) -> models.ExportEDRRulesResponse:
        """
        This API is used to export the EDR policy list.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportEDRRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportEDRRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportTasks(
            self,
            request: models.ExportTasksRequest,
            opts: Dict = None,
    ) -> models.ExportTasksResponse:
        """
        This API is used to export log files with large data volumes asynchronously.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InstallClusterAgent(
            self,
            request: models.InstallClusterAgentRequest,
            opts: Dict = None,
    ) -> models.InstallClusterAgentResponse:
        """
        Install Agent for cluster container security (parallel container installation method).

        capi layer processing process:
        1. Query the DB cluster list by ClusterCaMD5List (only used for resolving the appid ownership of each cluster, not for existence/type verification)
        2. Group by appid and pass through to the access side ClusterInstall RPC

        Description (container asset revision 2026 H1): This API is a passthrough API. The capi layer does not verify the existence, data type, or format of ClusterCaMD5. ClusterCaMD5 values that miss in the DB are silently skipped with no error reported.
        """
        
        kwargs = {}
        kwargs["action"] = "InstallClusterAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InstallClusterAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InstallKeySandboxSkill(
            self,
            request: models.InstallKeySandboxSkillRequest,
            opts: Dict = None,
    ) -> models.InstallKeySandboxSkillResponse:
        """
        Install the key sandbox SKILL on specified machine instances. Batch operations are supported, allowing input of multiple instance IDs at once. After installation, the AI Agent on the target machine can access credentials through the key sandbox proxy without being exposed to plaintext keys. Duplicate invocations on installed instances will not trigger an error (idempotent) and are deemed successful.
        """
        
        kwargs = {}
        kwargs["action"] = "InstallKeySandboxSkill"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InstallKeySandboxSkillResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InstallSandboxPlugin(
            self,
            request: models.InstallSandboxPluginRequest,
            opts: Dict = None,
    ) -> models.InstallSandboxPluginResponse:
        """
        Trigger installation of the traffic sandbox plugin to AI Agent assets in a specified range. Use BelongAssetType to distinguish host or container dimensions, and use EffectScope to specify the installation target (INCLUDE = install only to specified assets, EXCLUDE = all assets minus specified assets). This API only triggers the action and does not wait for completion.
        """
        
        kwargs = {}
        kwargs["action"] = "InstallSandboxPlugin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InstallSandboxPluginResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAILinkSetting(
            self,
            request: models.ModifyAILinkSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyAILinkSettingResponse:
        """
        Modify the AI-Link engine configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAILinkSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAILinkSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAISchedule(
            self,
            request: models.ModifyAIScheduleRequest,
            opts: Dict = None,
    ) -> models.ModifyAIScheduleResponse:
        """
        Modify a scheduled AI task.

        Partial update is supported. Only the passed-in optional fields are updated. Whether the trigger list is fully replaced is controlled by the UpdateTriggers flag.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAISchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAIScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAgentConfigSetting(
            self,
            request: models.ModifyAgentConfigSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyAgentConfigSettingResponse:
        """
        This API is used to modify client log collection settings exclusive to CSIP. It allows you to set the log collection type and asset scope for which the settings take effect.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAgentConfigSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAgentConfigSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAgentRunMode(
            self,
            request: models.ModifyAgentRunModeRequest,
            opts: Dict = None,
    ) -> models.ModifyAgentRunModeResponse:
        """
        Set the client running mode and configuration
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAgentRunMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAgentRunModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAgentRunPolicy(
            self,
            request: models.ModifyAgentRunPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyAgentRunPolicyResponse:
        """
        Modify the client running policy group. This API is used to set custom policies and associate machine lists.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAgentRunPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAgentRunPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAssetCoreAttribute(
            self,
            request: models.ModifyAssetCoreAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyAssetCoreAttributeResponse:
        """
        Tag an asset as core or not.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAssetCoreAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAssetCoreAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAssetFilterView(
            self,
            request: models.ModifyAssetFilterViewRequest,
            opts: Dict = None,
    ) -> models.ModifyAssetFilterViewResponse:
        """
        Update the asset search view.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAssetFilterView"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAssetFilterViewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAssetTag(
            self,
            request: models.ModifyAssetTagRequest,
            opts: Dict = None,
    ) -> models.ModifyAssetTagResponse:
        """
        This API is used to edit asset tags.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAssetTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAssetTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAssetTags(
            self,
            request: models.ModifyAssetTagsRequest,
            opts: Dict = None,
    ) -> models.ModifyAssetTagsResponse:
        """
        Operate assets to edit tags.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAssetTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAssetTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAssetTagsByAssetInfo(
            self,
            request: models.ModifyAssetTagsByAssetInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyAssetTagsByAssetInfoResponse:
        """
        Operate assets and edit tags.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAssetTagsByAssetInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAssetTagsByAssetInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBanMode(
            self,
            request: models.ModifyBanModeRequest,
            opts: Dict = None,
    ) -> models.ModifyBanModeResponse:
        """
        This API is used to modify the brute-force blocking mode.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBanMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBanModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBaselinePolicy(
            self,
            request: models.ModifyBaselinePolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyBaselinePolicyResponse:
        """
        Create or edit a baseline policy. Policy.ID 0 means create, non-zero means edit. Name is required when creating or editing. CheckAssetType and Type must comply with the CheckAssetType and PolicyType enums.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBaselinePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBaselinePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBaselinePolicyEnable(
            self,
            request: models.ModifyBaselinePolicyEnableRequest,
            opts: Dict = None,
    ) -> models.ModifyBaselinePolicyEnableResponse:
        """
        Batch enable or disable baseline policies. Once disabled, a policy will no longer be included in scans and statistics.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBaselinePolicyEnable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBaselinePolicyEnableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBaselineSyncConf(
            self,
            request: models.ModifyBaselineSyncConfRequest,
            opts: Dict = None,
    ) -> models.ModifyBaselineSyncConfResponse:
        """
        This API is used to update the baseline synchronization configuration of the current account (admin). When AutoSync is true, TargetAppidList cannot be empty and its elements cannot be 0.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBaselineSyncConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBaselineSyncConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBaselineUserOtherConf(
            self,
            request: models.ModifyBaselineUserOtherConfRequest,
            opts: Dict = None,
    ) -> models.ModifyBaselineUserOtherConfResponse:
        """
        This API is used to update user-level baseline configurations for the current account, including sync permission, offline risk clearing, and Agent scan timeout.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBaselineUserOtherConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBaselineUserOtherConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBaselineUserWeakPasswordConf(
            self,
            request: models.ModifyBaselineUserWeakPasswordConfRequest,
            opts: Dict = None,
    ) -> models.ModifyBaselineUserWeakPasswordConfResponse:
        """
        Update the custom "user weak password" dictionary for the current account. The dictionary content is stored after server encryption. Input an empty string to clear it.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBaselineUserWeakPasswordConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBaselineUserWeakPasswordConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBruteAttackBanStatus(
            self,
            request: models.ModifyBruteAttackBanStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyBruteAttackBanStatusResponse:
        """
        This API is used to set the status of brute force attack blocking.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBruteAttackBanStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBruteAttackBanStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBruteAttackRules(
            self,
            request: models.ModifyBruteAttackRulesRequest,
            opts: Dict = None,
    ) -> models.ModifyBruteAttackRulesResponse:
        """
        This API is used to modify brute force cracking rules.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBruteAttackRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBruteAttackRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCSIPLicenseBinds(
            self,
            request: models.ModifyCSIPLicenseBindsRequest,
            opts: Dict = None,
    ) -> models.ModifyCSIPLicenseBindsResponse:
        """
        Bind host authorization or RASP authorization to a specified order. Execute asynchronously and return TaskId to query progress. Specify the authorized version by LicenseType.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCSIPLicenseBinds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCSIPLicenseBindsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCSIPLicenseUnBinds(
            self,
            request: models.ModifyCSIPLicenseUnBindsRequest,
            opts: Dict = None,
    ) -> models.ModifyCSIPLicenseUnBindsResponse:
        """
        Manually unbind host authorization. Execute synchronously and return results directly. Only unbind host authorization (category=0, including Pro and Ultimate editions). In single order mode, appid can locate the order without the need to pass ResourceId. For RASP unbinding, use ModifyCSIPRaspLicenseUnBinds.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCSIPLicenseUnBinds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCSIPLicenseUnBindsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCSIPRaspLicenseBinds(
            self,
            request: models.ModifyCSIPRaspLicenseBindsRequest,
            opts: Dict = None,
    ) -> models.ModifyCSIPRaspLicenseBindsResponse:
        """
        Bind RASP or Flagship Edition Authorization to a specified order. Execute asynchronously and return TaskId to query progress. LicenseType=rasp binds RASP, LicenseType=enterprise_hp binds flagship host authorization. AssetType is case-sensitive for host/container node/EKS.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCSIPRaspLicenseBinds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCSIPRaspLicenseBindsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCSIPRaspLicenseUnBinds(
            self,
            request: models.ModifyCSIPRaspLicenseUnBindsRequest,
            opts: Dict = None,
    ) -> models.ModifyCSIPRaspLicenseUnBindsResponse:
        """
        Manually unbind RASP authorization. Execute synchronously and return results directly. Only unbind RASP authorization (category=1), with no unbinding frequency limit. In single order mode, appid can locate the order without the need to pass ResourceId.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCSIPRaspLicenseUnBinds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCSIPRaspLicenseUnBindsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterDefendStatus(
            self,
            request: models.ModifyClusterDefendStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterDefendStatusResponse:
        """
        Modify the cluster protection status.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterDefendStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterDefendStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCosAuditBucketMonitorStatus(
            self,
            request: models.ModifyCosAuditBucketMonitorStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyCosAuditBucketMonitorStatusResponse:
        """
        Modify the bucket monitoring status.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCosAuditBucketMonitorStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCosAuditBucketMonitorStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCspmShardConfig(
            self,
            request: models.ModifyCspmShardConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyCspmShardConfigResponse:
        """
        Updates the CSPM automated quota manager shared switch.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCspmShardConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCspmShardConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmAccessRecord(
            self,
            request: models.ModifyDspmAccessRecordRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmAccessRecordResponse:
        """
        Modify Dspm access management information
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmAccessRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmAccessRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmApplyingIdentifyComplianceGroup(
            self,
            request: models.ModifyDspmApplyingIdentifyComplianceGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmApplyingIdentifyComplianceGroupResponse:
        """
        Modifies the data identification template of the current dspm application
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmApplyingIdentifyComplianceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmApplyingIdentifyComplianceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmApproveStatus(
            self,
            request: models.ModifyDspmApproveStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmApproveStatusResponse:
        """
        Modifies the Dspm approval form status.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmApproveStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmApproveStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmAssetAccount(
            self,
            request: models.ModifyDspmAssetAccountRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmAssetAccountResponse:
        """
        Modify Dspm asset account information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmAssetAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmAssetAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmAssetAccountPrivileges(
            self,
            request: models.ModifyDspmAssetAccountPrivilegesRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmAssetAccountPrivilegesResponse:
        """
        Modify Dspm asset account permissions
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmAssetAccountPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmAssetAccountPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmAssetDataScanTask(
            self,
            request: models.ModifyDspmAssetDataScanTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmAssetDataScanTaskResponse:
        """
        Modifies a Dspm Asset Data scan task
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmAssetDataScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmAssetDataScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmAssetDataScanTaskStatus(
            self,
            request: models.ModifyDspmAssetDataScanTaskStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmAssetDataScanTaskStatusResponse:
        """
        Modify the status of a Dspm Asset Data scan task
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmAssetDataScanTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmAssetDataScanTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmAssetLogDeliverySwitch(
            self,
            request: models.ModifyDspmAssetLogDeliverySwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmAssetLogDeliverySwitchResponse:
        """
        Modify the Dspm asset log delivery switch.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmAssetLogDeliverySwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmAssetLogDeliverySwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmAssetSecurityAnalysisSwitch(
            self,
            request: models.ModifyDspmAssetSecurityAnalysisSwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmAssetSecurityAnalysisSwitchResponse:
        """
        Modify the Dspm asset log delivery switch
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmAssetSecurityAnalysisSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmAssetSecurityAnalysisSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmAuditFilterStrategy(
            self,
            request: models.ModifyDspmAuditFilterStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmAuditFilterStrategyResponse:
        """
        Modify a Dspm audit filter policy
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmAuditFilterStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmAuditFilterStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmBackupSetting(
            self,
            request: models.ModifyDspmBackupSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmBackupSettingResponse:
        """
        This API is used to modify the log backup settings.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmBackupSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmBackupSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmCkafkaSave(
            self,
            request: models.ModifyDspmCkafkaSaveRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmCkafkaSaveResponse:
        """
        This API is used to save the tenant CKafka configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmCkafkaSave"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmCkafkaSaveResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmCkafkaStart(
            self,
            request: models.ModifyDspmCkafkaStartRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmCkafkaStartResponse:
        """
        This API is used to enable the log shipping.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmCkafkaStart"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmCkafkaStartResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmCkafkaStop(
            self,
            request: models.ModifyDspmCkafkaStopRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmCkafkaStopResponse:
        """
        This API is used to disable the log type shipping.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmCkafkaStop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmCkafkaStopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmIdentifyCategory(
            self,
            request: models.ModifyDspmIdentifyCategoryRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmIdentifyCategoryResponse:
        """
        Modifies dspm data identification categorization
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmIdentifyCategory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmIdentifyCategoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmIdentifyComplianceGroup(
            self,
            request: models.ModifyDspmIdentifyComplianceGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmIdentifyComplianceGroupResponse:
        """
        Modifies a dspm data identification template
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmIdentifyComplianceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmIdentifyComplianceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmIdentifyComplianceGroupStatus(
            self,
            request: models.ModifyDspmIdentifyComplianceGroupStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmIdentifyComplianceGroupStatusResponse:
        """
        Modifies the status of a dspm data identification template
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmIdentifyComplianceGroupStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmIdentifyComplianceGroupStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmIdentifyComplianceRuleLevelInfo(
            self,
            request: models.ModifyDspmIdentifyComplianceRuleLevelInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmIdentifyComplianceRuleLevelInfoResponse:
        """
        This API is used to modify association level information of dspm data identification template data items.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmIdentifyComplianceRuleLevelInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmIdentifyComplianceRuleLevelInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmIdentifyInfo(
            self,
            request: models.ModifyDspmIdentifyInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmIdentifyInfoResponse:
        """
        Modify Dspm identity information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmIdentifyInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmIdentifyInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmIdentifyLevelGroup(
            self,
            request: models.ModifyDspmIdentifyLevelGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmIdentifyLevelGroupResponse:
        """
        Modifies dspm data identification classification groups
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmIdentifyLevelGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmIdentifyLevelGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmIdentifyLevelItem(
            self,
            request: models.ModifyDspmIdentifyLevelItemRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmIdentifyLevelItemResponse:
        """
        Modify dspm data identification grading information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmIdentifyLevelItem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmIdentifyLevelItemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmIdentifyRule(
            self,
            request: models.ModifyDspmIdentifyRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmIdentifyRuleResponse:
        """
        Modify a dspm identification data item
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmIdentifyRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmIdentifyRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmIdentifyRuleStatus(
            self,
            request: models.ModifyDspmIdentifyRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmIdentifyRuleStatusResponse:
        """
        Modifies the status of a dspm identification data item
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmIdentifyRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmIdentifyRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmIpInfo(
            self,
            request: models.ModifyDspmIpInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmIpInfoResponse:
        """
        Modify DspmIp information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmIpInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmIpInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmLogDeliveryType(
            self,
            request: models.ModifyDspmLogDeliveryTypeRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmLogDeliveryTypeResponse:
        """
        This API is used to modify the log shipping configuration information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmLogDeliveryType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmLogDeliveryTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmPersonalIdentify(
            self,
            request: models.ModifyDspmPersonalIdentifyRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmPersonalIdentifyResponse:
        """
        Modifies the Dspm personal identity ID.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmPersonalIdentify"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmPersonalIdentifyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmRestoreLogTask(
            self,
            request: models.ModifyDspmRestoreLogTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmRestoreLogTaskResponse:
        """
        This API is used to restore the backup logs.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmRestoreLogTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmRestoreLogTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmRiskInfo(
            self,
            request: models.ModifyDspmRiskInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmRiskInfoResponse:
        """
        Modifies Dspm risk information
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmRiskInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmRiskInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmRiskStrategy(
            self,
            request: models.ModifyDspmRiskStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmRiskStrategyResponse:
        """
        Modifies Dspm risk policies
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmRiskStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmRiskStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDspmWhitelistStrategy(
            self,
            request: models.ModifyDspmWhitelistStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyDspmWhitelistStrategyResponse:
        """
        Modify the Dspm allowlist policy
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDspmWhitelistStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDspmWhitelistStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEDRRule(
            self,
            request: models.ModifyEDRRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyEDRRuleResponse:
        """
        This API is used to edit or create an EDR policy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEDRRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEDRRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEDRRuleStatus(
            self,
            request: models.ModifyEDRRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyEDRRuleStatusResponse:
        """
        This API is used to modify the switch status of EDR policies.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEDRRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEDRRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEDRRulesAction(
            self,
            request: models.ModifyEDRRulesActionRequest,
            opts: Dict = None,
    ) -> models.ModifyEDRRulesActionResponse:
        """
        Batch modify EDR policy actions.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEDRRulesAction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEDRRulesActionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEdrAlertIsolation(
            self,
            request: models.ModifyEdrAlertIsolationRequest,
            opts: Dict = None,
    ) -> models.ModifyEdrAlertIsolationResponse:
        """
        EDR alert quarantine and recovery
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEdrAlertIsolation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEdrAlertIsolationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEdrAlertPermanentIgnore(
            self,
            request: models.ModifyEdrAlertPermanentIgnoreRequest,
            opts: Dict = None,
    ) -> models.ModifyEdrAlertPermanentIgnoreResponse:
        """
        Permanently ignore EDR multi-behavior alarms. Add the host and rule corresponding to the alarm to the AI-Link permanent ignore allowlist. Subsequently, alarms of the same type will be automatically discarded.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEdrAlertPermanentIgnore"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEdrAlertPermanentIgnoreResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEdrAlertStatus(
            self,
            request: models.ModifyEdrAlertStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyEdrAlertStatusResponse:
        """
        Handle the status of an EDR alert
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEdrAlertStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEdrAlertStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEdrExcludeNetworkSegments(
            self,
            request: models.ModifyEdrExcludeNetworkSegmentsRequest,
            opts: Dict = None,
    ) -> models.ModifyEdrExcludeNetworkSegmentsResponse:
        """
        This API is used to modify the CIDR block exclusion settings for log collection. IPs, IP ranges, and CIDR formats are supported, with up to 100 entries.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEdrExcludeNetworkSegments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEdrExcludeNetworkSegmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEdrLogCollectPath(
            self,
            request: models.ModifyEdrLogCollectPathRequest,
            opts: Dict = None,
    ) -> models.ModifyEdrLogCollectPathResponse:
        """
        This API is used to modify path configurations for application log collection.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEdrLogCollectPath"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEdrLogCollectPathResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyExposureAutoTagRule(
            self,
            request: models.ModifyExposureAutoTagRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyExposureAutoTagRuleResponse:
        """
        Update automatic cloud boundary tagging rules
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyExposureAutoTagRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyExposureAutoTagRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyExposureAutoTagRuleStatus(
            self,
            request: models.ModifyExposureAutoTagRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyExposureAutoTagRuleStatusResponse:
        """
        Enable or disable automatic cloud boundary tagging rules.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyExposureAutoTagRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyExposureAutoTagRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyExposureTag(
            self,
            request: models.ModifyExposureTagRequest,
            opts: Dict = None,
    ) -> models.ModifyExposureTagResponse:
        """
        Update custom tags for cloud boundaries
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyExposureTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyExposureTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIaCTokenPeriod(
            self,
            request: models.ModifyIaCTokenPeriodRequest,
            opts: Dict = None,
    ) -> models.ModifyIaCTokenPeriodResponse:
        """
        Modify the storage cycle of IaC detection integration tokens.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIaCTokenPeriod"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIaCTokenPeriodResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyImageRegistry(
            self,
            request: models.ModifyImageRegistryRequest,
            opts: Dict = None,
    ) -> models.ModifyImageRegistryResponse:
        """
        Modify image repository information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyImageRegistry"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyImageRegistryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyImageRegistryTimedScanTaskConfig(
            self,
            request: models.ModifyImageRegistryTimedScanTaskConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyImageRegistryTimedScanTaskConfigResponse:
        """
        Modify the scheduled scan task configuration of an image repository
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyImageRegistryTimedScanTaskConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyImageRegistryTimedScanTaskConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyImageSensitiveWhitelist(
            self,
            request: models.ModifyImageSensitiveWhitelistRequest,
            opts: Dict = None,
    ) -> models.ModifyImageSensitiveWhitelistResponse:
        """
        Modifies the Sensitive Information Allowlist of a Container Image
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyImageSensitiveWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyImageSensitiveWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyImageVirusWhitelist(
            self,
            request: models.ModifyImageVirusWhitelistRequest,
            opts: Dict = None,
    ) -> models.ModifyImageVirusWhitelistResponse:
        """
        This API is used to query asset database information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyImageVirusWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyImageVirusWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyImageVulWhitelist(
            self,
            request: models.ModifyImageVulWhitelistRequest,
            opts: Dict = None,
    ) -> models.ModifyImageVulWhitelistResponse:
        """
        Modifies the vulnerability allowlist of a container image.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyImageVulWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyImageVulWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoginWhiteRecord(
            self,
            request: models.ModifyLoginWhiteRecordRequest,
            opts: Dict = None,
    ) -> models.ModifyLoginWhiteRecordResponse:
        """
        This API is used to update the log-in audit allowlist information. (The number of server lists needs to be less than 1,000.)
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoginWhiteRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoginWhiteRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMachineAutoClearConfig(
            self,
            request: models.ModifyMachineAutoClearConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyMachineAutoClearConfigResponse:
        """
        This API is used to modify the cleanup configuration of the machine.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMachineAutoClearConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMachineAutoClearConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMachineRemark(
            self,
            request: models.ModifyMachineRemarkRequest,
            opts: Dict = None,
    ) -> models.ModifyMachineRemarkResponse:
        """
        Modify the remark information of a host asset
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMachineRemark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMachineRemarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMachinesLoginType(
            self,
            request: models.ModifyMachinesLoginTypeRequest,
            opts: Dict = None,
    ) -> models.ModifyMachinesLoginTypeResponse:
        """
        This API is used to modify host login methods in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMachinesLoginType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMachinesLoginTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMalwareTimingScanSettings(
            self,
            request: models.ModifyMalwareTimingScanSettingsRequest,
            opts: Dict = None,
    ) -> models.ModifyMalwareTimingScanSettingsResponse:
        """
        Modify the scheduled scan configuration for malicious file scan, including scan cycle, detection mode, asset scope, engine selection, and quarantine configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMalwareTimingScanSettings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMalwareTimingScanSettingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNFSScanConf(
            self,
            request: models.ModifyNFSScanConfRequest,
            opts: Dict = None,
    ) -> models.ModifyNFSScanConfResponse:
        """
        This API is used to add or update the global configuration for NFS scanning.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNFSScanConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNFSScanConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNFSScanHost(
            self,
            request: models.ModifyNFSScanHostRequest,
            opts: Dict = None,
    ) -> models.ModifyNFSScanHostResponse:
        """
        This API is used to disable process guard.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNFSScanHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNFSScanHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNetAttackSetting(
            self,
            request: models.ModifyNetAttackSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyNetAttackSettingResponse:
        """
        Modify the network attack detection switch and asset scope configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNetAttackSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNetAttackSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNotifyAgentOfflineDuration(
            self,
            request: models.ModifyNotifyAgentOfflineDurationRequest,
            opts: Dict = None,
    ) -> models.ModifyNotifyAgentOfflineDurationResponse:
        """
        This API is used to modify client offline duration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNotifyAgentOfflineDuration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNotifyAgentOfflineDurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNotifyAssetConfig(
            self,
            request: models.ModifyNotifyAssetConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyNotifyAssetConfigResponse:
        """
        Modify the asset scope configuration for notifications
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNotifyAssetConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNotifyAssetConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNotifyMember(
            self,
            request: models.ModifyNotifyMemberRequest,
            opts: Dict = None,
    ) -> models.ModifyNotifyMemberResponse:
        """
        Modify the member account for notification.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNotifyMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNotifyMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNotifySetting(
            self,
            request: models.ModifyNotifySettingRequest,
            opts: Dict = None,
    ) -> models.ModifyNotifySettingResponse:
        """
        Modifies notification settings
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNotifySetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNotifySettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNotifySettingAk(
            self,
            request: models.ModifyNotifySettingAkRequest,
            opts: Dict = None,
    ) -> models.ModifyNotifySettingAkResponse:
        """
        Modify notification settings
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNotifySettingAk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNotifySettingAkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNotifySettingAlert(
            self,
            request: models.ModifyNotifySettingAlertRequest,
            opts: Dict = None,
    ) -> models.ModifyNotifySettingAlertResponse:
        """
        Modify alarm center notification advanced configuration
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNotifySettingAlert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNotifySettingAlertResponse
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
        
    async def ModifyPayConfig(
            self,
            request: models.ModifyPayConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyPayConfigResponse:
        """
        Modify the auto-scaling configuration (multi-module and expandable; only the CWP module is available in the current period).

        Auto-scaling is an external user-oriented concept equivalent to automatic purchase (auto_repurchase) at the underlying layer: when an account has new assets, the desired authorization is automatically purchased.

        Supplemental description:
        1. In the current period, only the HostConfig module is implemented for host security. Subsequent scalability allows named module fields for container security and AI-Agent security. Configuration fields of each module can be heterogeneous.
        2. Partial update semantics: An empty module object indicates that the module is not modified, and an empty field in the module indicates that this field is not modified;
        3. HostConfig.Switch linkage map: auto_repurchase_switch; auto_bind_switch is always on and not modified by this API.
        4. Auto renewal (renew_flag) is not modified by this API; to query the limit/amount, call DescribeLicenseStatus.
        5. The top auto scaling global switch state is aggregated by the frontend based on each module switch. The backend does not store or return the global switch.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPayConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPayConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProtectionSetting(
            self,
            request: models.ModifyProtectionSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyProtectionSettingResponse:
        """
        This API is used to configure protection settings for the major event protection package.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProtectionSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProtectionSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRaspLicenseBinds(
            self,
            request: models.ModifyRaspLicenseBindsRequest,
            opts: Dict = None,
    ) -> models.ModifyRaspLicenseBindsResponse:
        """
        Bind an important period guarantee protection authorization package.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRaspLicenseBinds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRaspLicenseBindsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyReverseShellSystemPolicyConfig(
            self,
            request: models.ModifyReverseShellSystemPolicyConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyReverseShellSystemPolicyConfigResponse:
        """
        This API is used to modify the intranet alert and asset scope configuration for rebound Shell.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyReverseShellSystemPolicyConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyReverseShellSystemPolicyConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRiskCenterRiskStatus(
            self,
            request: models.ModifyRiskCenterRiskStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyRiskCenterRiskStatusResponse:
        """
        Modify Risk Center Risk Status
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
        
    async def ModifyRiskScanCronConfig(
            self,
            request: models.ModifyRiskScanCronConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyRiskScanCronConfigResponse:
        """
        Update the periodic scanning plan
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRiskScanCronConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRiskScanCronConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySandboxACLRule(
            self,
            request: models.ModifySandboxACLRuleRequest,
            opts: Dict = None,
    ) -> models.ModifySandboxACLRuleResponse:
        """
        Modify an existing ACL user rule. Fields not passed retain their original values, and partial field update is supported.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySandboxACLRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySandboxACLRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySandboxACLRuleStatus(
            self,
            request: models.ModifySandboxACLRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifySandboxACLRuleStatusResponse:
        """
        Batch switch the enable/disable status of ACL user rules. If any rule does not exist, belongs to another tenant, or has been deleted, an error is returned for the entirety.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySandboxACLRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySandboxACLRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySandboxAlertStatus(
            self,
            request: models.ModifySandboxAlertStatusRequest,
            opts: Dict = None,
    ) -> models.ModifySandboxAlertStatusResponse:
        """
        Batch update traffic sandbox alarms (overwrite ACL, DLP, and LLM audit). Locate the alarm source by AlertType + BelongAssetType. Status supports HANDLED / IGNORE to modify status, as well as DELETE to delete. If any alarm ID does not exist or belongs to another tenant, an error is returned overall. Note: Whitelisting (PASS) is not handled by this interface. It is triggered by Create/Modify***Rule writing back through AlertID.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySandboxAlertStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySandboxAlertStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySandboxDLPRule(
            self,
            request: models.ModifySandboxDLPRuleRequest,
            opts: Dict = None,
    ) -> models.ModifySandboxDLPRuleResponse:
        """
        Modify an existing DLP user rule. Fields not passed retain their original values, and partial field update is supported. BelongAssetType cannot be modified.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySandboxDLPRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySandboxDLPRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySandboxDLPRuleStatus(
            self,
            request: models.ModifySandboxDLPRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifySandboxDLPRuleStatusResponse:
        """
        Batch switch the enable/disable status of DLP user rules. If any rule does not exist, belongs to another tenant, or has been deleted, an error is returned for the entirety.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySandboxDLPRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySandboxDLPRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySandboxFileRule(
            self,
            request: models.ModifySandboxFileRuleRequest,
            opts: Dict = None,
    ) -> models.ModifySandboxFileRuleResponse:
        """
        Modify command sandbox file access rule
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySandboxFileRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySandboxFileRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySandboxFileRuleStatus(
            self,
            request: models.ModifySandboxFileRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifySandboxFileRuleStatusResponse:
        """
        Batch enable or disable command sandbox file access rules.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySandboxFileRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySandboxFileRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySandboxLLMAuditRule(
            self,
            request: models.ModifySandboxLLMAuditRuleRequest,
            opts: Dict = None,
    ) -> models.ModifySandboxLLMAuditRuleResponse:
        """
        Modify an existing LLM audit user rule. Fields not passed retain their original values, and partial field update is supported.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySandboxLLMAuditRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySandboxLLMAuditRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySandboxLLMAuditRuleStatus(
            self,
            request: models.ModifySandboxLLMAuditRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifySandboxLLMAuditRuleStatusResponse:
        """
        Batch switch the enable or disable status of LLM audit user rules. If any rule does not exist, belongs to another tenant, or has been deleted, an error is returned overall.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySandboxLLMAuditRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySandboxLLMAuditRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityScoreRule(
            self,
            request: models.ModifySecurityScoreRuleRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityScoreRuleResponse:
        """
        Modify a security scoring rule. You need to pass in a complete rule set.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityScoreRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityScoreRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyShareUserAK(
            self,
            request: models.ModifyShareUserAKRequest,
            opts: Dict = None,
    ) -> models.ModifyShareUserAKResponse:
        """
        Edit the ak monitoring account.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyShareUserAK"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyShareUserAKResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyShareUserCSPM(
            self,
            request: models.ModifyShareUserCSPMRequest,
            opts: Dict = None,
    ) -> models.ModifyShareUserCSPMResponse:
        """
        Edit a CSPM shared account
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyShareUserCSPM"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyShareUserCSPMResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyShareUserDspm(
            self,
            request: models.ModifyShareUserDspmRequest,
            opts: Dict = None,
    ) -> models.ModifyShareUserDspmResponse:
        """
        Edit dspm monitored account
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyShareUserDspm"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyShareUserDspmResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySkillScanAlertStatus(
            self,
            request: models.ModifySkillScanAlertStatusRequest,
            opts: Dict = None,
    ) -> models.ModifySkillScanAlertStatusResponse:
        """
        Batch modify the processing status of Skill security detection alarms.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySkillScanAlertStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySkillScanAlertStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUebaRuleSwitch(
            self,
            request: models.ModifyUebaRuleSwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyUebaRuleSwitchResponse:
        """
        Update the switch of a custom policy
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUebaRuleSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUebaRuleSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVulScanPeriodic(
            self,
            request: models.ModifyVulScanPeriodicRequest,
            opts: Dict = None,
    ) -> models.ModifyVulScanPeriodicResponse:
        """
        This API is used to modify vulnerability scanning (period scanning).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVulScanPeriodic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVulScanPeriodicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVulWhitelistConfig(
            self,
            request: models.ModifyVulWhitelistConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyVulWhitelistConfigResponse:
        """
        This API is used to modify the vulnerability allowlist configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVulWhitelistConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVulWhitelistConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVulWhitelistSwitch(
            self,
            request: models.ModifyVulWhitelistSwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyVulWhitelistSwitchResponse:
        """
        This API is used to modify the vulnerability allowlist switch.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVulWhitelistSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVulWhitelistSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWebhookPolicy(
            self,
            request: models.ModifyWebhookPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyWebhookPolicyResponse:
        """
        Add or modify a notification policy. ID > 0 means modification; ID = 0 or not passed means adding new. When MemberAppIds is configured as empty, the policy only acts on current root account events; when not empty, it acts on the self account + listed member accounts at the same time.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWebhookPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWebhookPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWebhookPolicyStatus(
            self,
            request: models.ModifyWebhookPolicyStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyWebhookPolicyStatusResponse:
        """
        Switch the enable status of the notification policy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWebhookPolicyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWebhookPolicyStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWebhookReceiver(
            self,
            request: models.ModifyWebhookReceiverRequest,
            opts: Dict = None,
    ) -> models.ModifyWebhookReceiverResponse:
        """
        Add or modify a receiving robot. ID > 0 means modifying an existing record; ID = 0 or not passed means adding new. The robot type is determined by the Type field. When Type=WEBHOOK, WebhookAddr is required. When Type=SCF, SCFRegion/Namespace/FunctionName/FunctionVersion/Alias/MaxWaitSeconds are all required. Type is not allowed to be changed during modification.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWebhookReceiver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWebhookReceiverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OperateRisk(
            self,
            request: models.OperateRiskRequest,
            opts: Dict = None,
    ) -> models.OperateRiskResponse:
        """
        Risk operation example
        """
        
        kwargs = {}
        kwargs["action"] = "OperateRisk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OperateRiskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OperateRiskRulePolicy(
            self,
            request: models.OperateRiskRulePolicyRequest,
            opts: Dict = None,
    ) -> models.OperateRiskRulePolicyResponse:
        """
        Custom risk rule
        """
        
        kwargs = {}
        kwargs["action"] = "OperateRiskRulePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OperateRiskRulePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetDspmAssetAccountPassword(
            self,
            request: models.ResetDspmAssetAccountPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetDspmAssetAccountPasswordResponse:
        """
        Reset the Dspm asset account password.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetDspmAssetAccountPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetDspmAssetAccountPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RetryDspmExportLog(
            self,
            request: models.RetryDspmExportLogRequest,
            opts: Dict = None,
    ) -> models.RetryDspmExportLogResponse:
        """
        RetryExportLog
        """
        
        kwargs = {}
        kwargs["action"] = "RetryDspmExportLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RetryDspmExportLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RevertDspmAssetAccount(
            self,
            request: models.RevertDspmAssetAccountRequest,
            opts: Dict = None,
    ) -> models.RevertDspmAssetAccountResponse:
        """
        Restore a Dspm asset account.
        """
        
        kwargs = {}
        kwargs["action"] = "RevertDspmAssetAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RevertDspmAssetAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanBaselineAssetItemList(
            self,
            request: models.ScanBaselineAssetItemListRequest,
            opts: Dict = None,
    ) -> models.ScanBaselineAssetItemListResponse:
        """
        This API is used to trigger a rescan of some detection items for a single asset.
        """
        
        kwargs = {}
        kwargs["action"] = "ScanBaselineAssetItemList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanBaselineAssetItemListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanBaselineItemList(
            self,
            request: models.ScanBaselineItemListRequest,
            opts: Dict = None,
    ) -> models.ScanBaselineItemListResponse:
        """
        This API is used to rescan detection items under a specified policy.
        """
        
        kwargs = {}
        kwargs["action"] = "ScanBaselineItemList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanBaselineItemListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanBaselinePolicyList(
            self,
            request: models.ScanBaselinePolicyListRequest,
            opts: Dict = None,
    ) -> models.ScanBaselinePolicyListResponse:
        """
        Trigger a holistic rescan for a batch of baseline policies via the one-click scan entry on the strategy list page. All assets within the policy hit scope will be rescanned.
        """
        
        kwargs = {}
        kwargs["action"] = "ScanBaselinePolicyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanBaselinePolicyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanBaselineRiskList(
            self,
            request: models.ScanBaselineRiskListRequest,
            opts: Dict = None,
    ) -> models.ScanBaselineRiskListResponse:
        """
        Triggers a rescan for a batch of risk records. It is commonly used for rescanning after selecting multiple risks on the Risk List page.
        """
        
        kwargs = {}
        kwargs["action"] = "ScanBaselineRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanBaselineRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanCSIPTaskAgain(
            self,
            request: models.ScanCSIPTaskAgainRequest,
            opts: Dict = None,
    ) -> models.ScanCSIPTaskAgainResponse:
        """
        This API is used to delete CSIP manual scan tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "ScanCSIPTaskAgain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanCSIPTaskAgainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanEDRTaskAgain(
            self,
            request: models.ScanEDRTaskAgainRequest,
            opts: Dict = None,
    ) -> models.ScanEDRTaskAgainResponse:
        """
        Create a scan task based on the original task configuration. If AssetId is empty, get all asset info from TaskId. If AssetId is not empty, only the single asset is included.
        """
        
        kwargs = {}
        kwargs["action"] = "ScanEDRTaskAgain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanEDRTaskAgainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendDspmAssetLoginSmsCode(
            self,
            request: models.SendDspmAssetLoginSmsCodeRequest,
            opts: Dict = None,
    ) -> models.SendDspmAssetLoginSmsCodeResponse:
        """
        Sends the access verification code for a Dspm asset
        """
        
        kwargs = {}
        kwargs["action"] = "SendDspmAssetLoginSmsCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendDspmAssetLoginSmsCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendDspmCkafkaTest(
            self,
            request: models.SendDspmCkafkaTestRequest,
            opts: Dict = None,
    ) -> models.SendDspmCkafkaTestResponse:
        """
        This API is used to test the tenant CKafka connectivity.
        """
        
        kwargs = {}
        kwargs["action"] = "SendDspmCkafkaTest"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendDspmCkafkaTestResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartOrModifyPreventUninstall(
            self,
            request: models.StartOrModifyPreventUninstallRequest,
            opts: Dict = None,
    ) -> models.StartOrModifyPreventUninstallResponse:
        """
        Enable or modify the anti-uninstall feature configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "StartOrModifyPreventUninstall"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartOrModifyPreventUninstallResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartOrModifyProcessDaemon(
            self,
            request: models.StartOrModifyProcessDaemonRequest,
            opts: Dict = None,
    ) -> models.StartOrModifyProcessDaemonResponse:
        """
        This API is used to enable or modify process guard feature configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "StartOrModifyProcessDaemon"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartOrModifyProcessDaemonResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopBaselineScanTask(
            self,
            request: models.StopBaselineScanTaskRequest,
            opts: Dict = None,
    ) -> models.StopBaselineScanTaskResponse:
        """
        This API is used to stop a specified baseline scan main task. It only takes effect for tasks in the INIT, SUBTASK_CREATING, or SCANNING status.
        """
        
        kwargs = {}
        kwargs["action"] = "StopBaselineScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopBaselineScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopCSIPManualMalwareScan(
            self,
            request: models.StopCSIPManualMalwareScanRequest,
            opts: Dict = None,
    ) -> models.StopCSIPManualMalwareScanResponse:
        """
        CSIP manual scan stop API
        """
        
        kwargs = {}
        kwargs["action"] = "StopCSIPManualMalwareScan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopCSIPManualMalwareScanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopEDRScanTask(
            self,
            request: models.StopEDRScanTaskRequest,
            opts: Dict = None,
    ) -> models.StopEDRScanTaskResponse:
        """
        Stop or cancel a scan task. For tasks in SCANNING status, call RPC to stop them. For tasks in WAIT status, update the database directly to cancel them. Only the task creator can perform these operations.
        """
        
        kwargs = {}
        kwargs["action"] = "StopEDRScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopEDRScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopImageRegistryScanTask(
            self,
            request: models.StopImageRegistryScanTaskRequest,
            opts: Dict = None,
    ) -> models.StopImageRegistryScanTaskResponse:
        """
        Terminate an image scanning task in a mirror repository
        """
        
        kwargs = {}
        kwargs["action"] = "StopImageRegistryScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopImageRegistryScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopPreventUninstall(
            self,
            request: models.StopPreventUninstallRequest,
            opts: Dict = None,
    ) -> models.StopPreventUninstallResponse:
        """
        This API is used to disable the anti-uninstallation feature.
        """
        
        kwargs = {}
        kwargs["action"] = "StopPreventUninstall"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopPreventUninstallResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopProcessDaemon(
            self,
            request: models.StopProcessDaemonRequest,
            opts: Dict = None,
    ) -> models.StopProcessDaemonResponse:
        """
        This API is used to disable process guard.
        """
        
        kwargs = {}
        kwargs["action"] = "StopProcessDaemon"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopProcessDaemonResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopRiskCenterTask(
            self,
            request: models.StopRiskCenterTaskRequest,
            opts: Dict = None,
    ) -> models.StopRiskCenterTaskResponse:
        """
        Stop Scanning Tasks of Risk Center
        """
        
        kwargs = {}
        kwargs["action"] = "StopRiskCenterTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopRiskCenterTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopVulScanTask(
            self,
            request: models.StopVulScanTaskRequest,
            opts: Dict = None,
    ) -> models.StopVulScanTaskResponse:
        """
        Stop vulnerability scanning (task scan).
        """
        
        kwargs = {}
        kwargs["action"] = "StopVulScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopVulScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncDspmAssets(
            self,
            request: models.SyncDspmAssetsRequest,
            opts: Dict = None,
    ) -> models.SyncDspmAssetsResponse:
        """
        Synchronize assets supported by dspm
        """
        
        kwargs = {}
        kwargs["action"] = "SyncDspmAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncDspmAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncDspmUsers(
            self,
            request: models.SyncDspmUsersRequest,
            opts: Dict = None,
    ) -> models.SyncDspmUsersResponse:
        """
        Synchronize the list of dspm users.
        """
        
        kwargs = {}
        kwargs["action"] = "SyncDspmUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncDspmUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncImageRegistry(
            self,
            request: models.SyncImageRegistryRequest,
            opts: Dict = None,
    ) -> models.SyncImageRegistryResponse:
        """
        Synchronize the mirror repository
        """
        
        kwargs = {}
        kwargs["action"] = "SyncImageRegistry"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncImageRegistryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TestWebhookReceiver(
            self,
            request: models.TestWebhookReceiverRequest,
            opts: Dict = None,
    ) -> models.TestWebhookReceiverResponse:
        """
        Send a test message to the designated receiving robot to verify reachability and configuration. Use the "Test" button in the corresponding table row.
        """
        
        kwargs = {}
        kwargs["action"] = "TestWebhookReceiver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TestWebhookReceiverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UninstallClusterAgent(
            self,
            request: models.UninstallClusterAgentRequest,
            opts: Dict = None,
    ) -> models.UninstallClusterAgentResponse:
        """
        Uninstall the cluster container security Agent.
        """
        
        kwargs = {}
        kwargs["action"] = "UninstallClusterAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UninstallClusterAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UninstallKeySandboxSkill(
            self,
            request: models.UninstallKeySandboxSkillRequest,
            opts: Dict = None,
    ) -> models.UninstallKeySandboxSkillResponse:
        """
        Uninstall the key sandbox SKILL from designated machine instances. Support batch operations, allowing multiple instance IDs at once. After uninstallation, the AI Agent on the target machine will not be able to access credentials via the key sandbox proxy. Repeated calls on instances not installed will not trigger an error (idempotent), and are directly deemed successful.
        """
        
        kwargs = {}
        kwargs["action"] = "UninstallKeySandboxSkill"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UninstallKeySandboxSkillResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAccessKeyAlarmStatus(
            self,
            request: models.UpdateAccessKeyAlarmStatusRequest,
            opts: Dict = None,
    ) -> models.UpdateAccessKeyAlarmStatusResponse:
        """
        Tag risks or alarms as processed or ignored.
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
        Edit the remark of an access key/source IP.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAccessKeyRemark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAccessKeyRemarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAlertStatusList(
            self,
            request: models.UpdateAlertStatusListRequest,
            opts: Dict = None,
    ) -> models.UpdateAlertStatusListResponse:
        """
        This API is used to handle alarm status in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAlertStatusList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAlertStatusListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateClusterOwner(
            self,
            request: models.UpdateClusterOwnerRequest,
            opts: Dict = None,
    ) -> models.UpdateClusterOwnerResponse:
        """
        Bind and update a cluster owner
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateClusterOwner"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateClusterOwnerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyDspmAssetLoginCode(
            self,
            request: models.VerifyDspmAssetLoginCodeRequest,
            opts: Dict = None,
    ) -> models.VerifyDspmAssetLoginCodeResponse:
        """
        Verify the login verification code for a Dspm asset.
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyDspmAssetLoginCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyDspmAssetLoginCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)