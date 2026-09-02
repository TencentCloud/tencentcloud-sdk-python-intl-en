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
from tencentcloud.csip.v20221121 import models


class CsipClient(AbstractClient):
    _apiVersion = '2022-11-21'
    _endpoint = 'csip.intl.tencentcloudapi.com'
    _service = 'csip'


    def AccessAIAnalysisSMTP(self, request):
        r"""This API is used to create or modify SMTP mailbox access requests.

        :param request: Request instance for AccessAIAnalysisSMTP.
        :type request: :class:`tencentcloud.csip.v20221121.models.AccessAIAnalysisSMTPRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.AccessAIAnalysisSMTPResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AccessAIAnalysisSMTP", params, headers=headers)
            response = json.loads(body)
            model = models.AccessAIAnalysisSMTPResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddDspmAssetManager(self, request):
        r"""Add asset administrator

        :param request: Request instance for AddDspmAssetManager.
        :type request: :class:`tencentcloud.csip.v20221121.models.AddDspmAssetManagerRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.AddDspmAssetManagerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddDspmAssetManager", params, headers=headers)
            response = json.loads(body)
            model = models.AddDspmAssetManagerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddImageRegistry(self, request):
        r"""Add mirror repository information.

        :param request: Request instance for AddImageRegistry.
        :type request: :class:`tencentcloud.csip.v20221121.models.AddImageRegistryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.AddImageRegistryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddImageRegistry", params, headers=headers)
            response = json.loads(body)
            model = models.AddImageRegistryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddLoginWhiteLists(self, request):
        r"""This API is used to add cross-region log-in allowlists in batches.

        :param request: Request instance for AddLoginWhiteLists.
        :type request: :class:`tencentcloud.csip.v20221121.models.AddLoginWhiteListsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.AddLoginWhiteListsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddLoginWhiteLists", params, headers=headers)
            response = json.loads(body)
            model = models.AddLoginWhiteListsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddNewBindRoleUser(self, request):
        r"""CSIP Role Authorization Binding API

        :param request: Request instance for AddNewBindRoleUser.
        :type request: :class:`tencentcloud.csip.v20221121.models.AddNewBindRoleUserRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.AddNewBindRoleUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddNewBindRoleUser", params, headers=headers)
            response = json.loads(body)
            model = models.AddNewBindRoleUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddVulWhitelist(self, request):
        r"""Add a vulnerability allowlist

        :param request: Request instance for AddVulWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.AddVulWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.AddVulWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddVulWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.AddVulWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchModifyBaselinePolicy(self, request):
        r"""Batch modify the "periodic scan configuration / automatic synchronization of newly-added detection items / detection item hit configuration / customized detection items" settings in the baseline policy. Only fields passed in the request are modified.

        :param request: Request instance for BatchModifyBaselinePolicy.
        :type request: :class:`tencentcloud.csip.v20221121.models.BatchModifyBaselinePolicyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.BatchModifyBaselinePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchModifyBaselinePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.BatchModifyBaselinePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchModifyImageRegistryTimedScanTaskConfig(self, request):
        r"""Batch modify the scheduled scan task configurations of image repositories.

        :param request: Request instance for BatchModifyImageRegistryTimedScanTaskConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.BatchModifyImageRegistryTimedScanTaskConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.BatchModifyImageRegistryTimedScanTaskConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchModifyImageRegistryTimedScanTaskConfig", params, headers=headers)
            response = json.loads(body)
            model = models.BatchModifyImageRegistryTimedScanTaskConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchModifyImageSensitiveWhitelist(self, request):
        r"""Batch Modify Sensitive Information Allowlist for Container Images

        :param request: Request instance for BatchModifyImageSensitiveWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.BatchModifyImageSensitiveWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.BatchModifyImageSensitiveWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchModifyImageSensitiveWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.BatchModifyImageSensitiveWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchModifyImageVirusWhitelist(self, request):
        r"""Batch modify the Trojan allowlist for images.

        :param request: Request instance for BatchModifyImageVirusWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.BatchModifyImageVirusWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.BatchModifyImageVirusWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchModifyImageVirusWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.BatchModifyImageVirusWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchModifyImageVulWhitelist(self, request):
        r"""Batch Modify Vulnerability Allowlist for Container Images

        :param request: Request instance for BatchModifyImageVulWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.BatchModifyImageVulWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.BatchModifyImageVulWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchModifyImageVulWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.BatchModifyImageVulWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelEdrAlertIgnore(self, request):
        r"""Cancel a permanently ignored EDR multi-behavior alarm. Remove the corresponding host and rule record from the AI-Link permanent ignore allowlist and restore the alarm status to PENDING.

        :param request: Request instance for CancelEdrAlertIgnore.
        :type request: :class:`tencentcloud.csip.v20221121.models.CancelEdrAlertIgnoreRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CancelEdrAlertIgnoreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelEdrAlertIgnore", params, headers=headers)
            response = json.loads(body)
            model = models.CancelEdrAlertIgnoreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckCWPExposePathPermission(self, request):
        r"""Determine whether the current user is on the flagship edition for hosts.

        :param request: Request instance for CheckCWPExposePathPermission.
        :type request: :class:`tencentcloud.csip.v20221121.models.CheckCWPExposePathPermissionRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CheckCWPExposePathPermissionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckCWPExposePathPermission", params, headers=headers)
            response = json.loads(body)
            model = models.CheckCWPExposePathPermissionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckImageRegistryInstanceNameDuplicate(self, request):
        r"""Check whether the image repository instance name is duplicate.

        :param request: Request instance for CheckImageRegistryInstanceNameDuplicate.
        :type request: :class:`tencentcloud.csip.v20221121.models.CheckImageRegistryInstanceNameDuplicateRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CheckImageRegistryInstanceNameDuplicateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckImageRegistryInstanceNameDuplicate", params, headers=headers)
            response = json.loads(body)
            model = models.CheckImageRegistryInstanceNameDuplicateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckIsUltimateVersion(self, request):
        r"""Determine whether the current user is on the flagship edition.

        :param request: Request instance for CheckIsUltimateVersion.
        :type request: :class:`tencentcloud.csip.v20221121.models.CheckIsUltimateVersionRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CheckIsUltimateVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckIsUltimateVersion", params, headers=headers)
            response = json.loads(body)
            model = models.CheckIsUltimateVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckRisk(self, request):
        r"""Risk verification example

        :param request: Request instance for CheckRisk.
        :type request: :class:`tencentcloud.csip.v20221121.models.CheckRiskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CheckRiskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckRisk", params, headers=headers)
            response = json.loads(body)
            model = models.CheckRiskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CopyBaselinePolicy(self, request):
        r"""Replicate a custom baseline policy.

        :param request: Request instance for CopyBaselinePolicy.
        :type request: :class:`tencentcloud.csip.v20221121.models.CopyBaselinePolicyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CopyBaselinePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyBaselinePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CopyBaselinePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAISchedule(self, request):
        r"""Create an AI scheduled task.

        Create an AI scheduled task by entering the task name, prompt content, and trigger configuration. The AI scheduled task ID will be returned after successful creation.

        :param request: Request instance for CreateAISchedule.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateAIScheduleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateAIScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAISchedule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAIScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAccessKeyCheckTask(self, request):
        r"""Detect async tasks of AK

        :param request: Request instance for CreateAccessKeyCheckTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateAccessKeyCheckTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateAccessKeyCheckTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccessKeyCheckTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAccessKeyCheckTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAccessKeySyncTask(self, request):
        r"""Trigger an AK asset sync task.

        :param request: Request instance for CreateAccessKeySyncTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateAccessKeySyncTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateAccessKeySyncTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccessKeySyncTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAccessKeySyncTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAllAssetsExportJob(self, request):
        r"""Creates a task to export all assets.

        :param request: Request instance for CreateAllAssetsExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateAllAssetsExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateAllAssetsExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAllAssetsExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAllAssetsExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAssetComponentListExportJob(self, request):
        r"""Creates a component list export task for image assets.

        :param request: Request instance for CreateAssetComponentListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateAssetComponentListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateAssetComponentListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetComponentListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAssetComponentListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAssetComponentRelatedImageListExportJob(self, request):
        r"""Create a mirror repository component associated image list export task.

        :param request: Request instance for CreateAssetComponentRelatedImageListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateAssetComponentRelatedImageListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateAssetComponentRelatedImageListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetComponentRelatedImageListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAssetComponentRelatedImageListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAssetFilterView(self, request):
        r"""Create an asset search view.

        :param request: Request instance for CreateAssetFilterView.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateAssetFilterViewRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateAssetFilterViewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetFilterView", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAssetFilterViewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAssetProcessExportJob(self, request):
        r"""Create a host process list export task

        :param request: Request instance for CreateAssetProcessExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateAssetProcessExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateAssetProcessExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetProcessExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAssetProcessExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAssetSyncTask(self, request):
        r"""This API is used to create an asset sync task.

        :param request: Request instance for CreateAssetSyncTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateAssetSyncTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateAssetSyncTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetSyncTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAssetSyncTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAssetTag(self, request):
        r"""Create an asset tag.

        :param request: Request instance for CreateAssetTag.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateAssetTagRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateAssetTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetTag", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAssetTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAssetViewRisksExportJob(self, request):
        r"""Create a sample risk list export task from the asset perspective

        :param request: Request instance for CreateAssetViewRisksExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateAssetViewRisksExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateAssetViewRisksExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetViewRisksExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAssetViewRisksExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBaselineAggregatedItemExportJob(self, request):
        r"""Create a baseline aggregation detection item export task. Use ExportType to select exporting statistics or risk details. You can limit the range by conditions such as policy and category. The task executes asynchronously in the backend. Once completed, you can download the result file from the export task list.

        :param request: Request instance for CreateBaselineAggregatedItemExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateBaselineAggregatedItemExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateBaselineAggregatedItemExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBaselineAggregatedItemExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBaselineAggregatedItemExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBaselineFixRecordExportJob(self, request):
        r"""This API is used to create a baseline fix record export task to export the records of fixed detection items, including detection item information, asset information, and repair time. The task executes asynchronously in the backend. Once completed, the result file can be downloaded from the export task list.

        :param request: Request instance for CreateBaselineFixRecordExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateBaselineFixRecordExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateBaselineFixRecordExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBaselineFixRecordExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBaselineFixRecordExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBaselineMainTaskExportJob(self, request):
        r"""Create a baseline main task export task to export detection items and subtask data under the specified main task. The task executes asynchronously in the backend. Once completed, the result file can be downloaded in the export task list.

        :param request: Request instance for CreateBaselineMainTaskExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateBaselineMainTaskExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateBaselineMainTaskExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBaselineMainTaskExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBaselineMainTaskExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCFGRiskPDFReportExportJob(self, request):
        r"""Example of creating an export task for a cloud resource configuration detection PDF report.

        :param request: Request instance for CreateCFGRiskPDFReportExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateCFGRiskPDFReportExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateCFGRiskPDFReportExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCFGRiskPDFReportExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCFGRiskPDFReportExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCFGRisksExportJob(self, request):
        r"""Example of creating an asset perspective risk list export task

        :param request: Request instance for CreateCFGRisksExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateCFGRisksExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateCFGRisksExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCFGRisksExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCFGRisksExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCSIPManualMalwareScan(self, request):
        r"""This API is used to create a CSIP manual scan.

        :param request: Request instance for CreateCSIPManualMalwareScan.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateCSIPManualMalwareScanRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateCSIPManualMalwareScanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCSIPManualMalwareScan", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCSIPManualMalwareScanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCheckViewRisksExportJob(self, request):
        r"""Create a sample risk list export task from the asset perspective

        :param request: Request instance for CreateCheckViewRisksExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateCheckViewRisksExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateCheckViewRisksExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCheckViewRisksExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCheckViewRisksExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudFunctionExportJob(self, request):
        r"""This API is used to create an SCF export task.

        :param request: Request instance for CreateCloudFunctionExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateCloudFunctionExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateCloudFunctionExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudFunctionExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudFunctionExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClusterAssetSyncTask(self, request):
        r"""This API is used to create a cluster asset sync task.

        :param request: Request instance for CreateClusterAssetSyncTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateClusterAssetSyncTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateClusterAssetSyncTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterAssetSyncTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterAssetSyncTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClusterContainerListExportJob(self, request):
        r"""Creates a cluster container list export task

        :param request: Request instance for CreateClusterContainerListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateClusterContainerListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateClusterContainerListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterContainerListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterContainerListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClusterListExportJob(self, request):
        r"""Create a cluster list export task

        :param request: Request instance for CreateClusterListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateClusterListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateClusterListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClusterNamespaceListExportJob(self, request):
        r"""Creates a cluster namespace list export task. The export fields include namespace name, Labels, and creation time. Filter filtering is supported. Export is implemented through an async task. After JobId is returned, the frontend polls to query the export task status.

        :param request: Request instance for CreateClusterNamespaceListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateClusterNamespaceListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateClusterNamespaceListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterNamespaceListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterNamespaceListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClusterNodeListExportJob(self, request):
        r"""This API is used to create a cluster node list export task. The export fields include node ID, node name, public IP address, private IP address, node type, cores, client status, and running state. NodeType, ClientStatus, and RunStatus are internationalized. Filter filtering is supported, including ClientStatus memory filtering. Export is implemented through an async task. After JobId is returned, the frontend polls to query the export task status.

        :param request: Request instance for CreateClusterNodeListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateClusterNodeListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateClusterNodeListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterNodeListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterNodeListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateComplianceRiskExportJob(self, request):
        r"""Example of creating a risk list export task from a compliance standard aggregation perspective

        :param request: Request instance for CreateComplianceRiskExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateComplianceRiskExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateComplianceRiskExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateComplianceRiskExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateComplianceRiskExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDomainAndIp(self, request):
        r"""Create Domain and IP Information

        :param request: Request instance for CreateDomainAndIp.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDomainAndIpRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDomainAndIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDomainAndIp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDomainAndIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmAccessExportJob(self, request):
        r"""Creates a Dspm access record export task

        :param request: Request instance for CreateDspmAccessExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmAccessExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmAccessExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmAccessExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmAccessExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmApplyOrder(self, request):
        r"""This API is used to create a Dspm application.

        :param request: Request instance for CreateDspmApplyOrder.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmApplyOrderRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmApplyOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmApplyOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmApplyOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmApproveHistoryExportJob(self, request):
        r"""Creates a Dspm approval history export task

        :param request: Request instance for CreateDspmApproveHistoryExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmApproveHistoryExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmApproveHistoryExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmApproveHistoryExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmApproveHistoryExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmAssetAccessTopologyExportJob(self, request):
        r"""This API is used to create a Dspm asset access topology export task.

        :param request: Request instance for CreateDspmAssetAccessTopologyExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmAssetAccessTopologyExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmAssetAccessTopologyExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmAssetAccessTopologyExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmAssetAccessTopologyExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmAssetIdentifyInfoExportJob(self, request):
        r"""Create an asset list export task for Dspm.

        :param request: Request instance for CreateDspmAssetIdentifyInfoExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmAssetIdentifyInfoExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmAssetIdentifyInfoExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmAssetIdentifyInfoExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmAssetIdentifyInfoExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmAssetsExportJob(self, request):
        r"""Creates a Dspm asset list export task

        :param request: Request instance for CreateDspmAssetsExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmAssetsExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmAssetsExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmAssetsExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmAssetsExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmAuditFilterStrategy(self, request):
        r"""This API is used to create a Dspm audit filter policy.

        :param request: Request instance for CreateDspmAuditFilterStrategy.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmAuditFilterStrategyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmAuditFilterStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmAuditFilterStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmAuditFilterStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmExportTask(self, request):
        r"""This API is used to create log export tasks.

        :param request: Request instance for CreateDspmExportTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmExportTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmExportTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmExportTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmExportTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmIdentifyCategory(self, request):
        r"""This API is used to create a dspm data identification category.

        :param request: Request instance for CreateDspmIdentifyCategory.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyCategoryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyCategoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmIdentifyCategory", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmIdentifyCategoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmIdentifyComplianceCategoryRelation(self, request):
        r"""This API is used to create a dspm data identification template category association.

        :param request: Request instance for CreateDspmIdentifyComplianceCategoryRelation.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyComplianceCategoryRelationRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyComplianceCategoryRelationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmIdentifyComplianceCategoryRelation", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmIdentifyComplianceCategoryRelationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmIdentifyComplianceGroup(self, request):
        r"""This API is used to create a dspm data identification template.

        :param request: Request instance for CreateDspmIdentifyComplianceGroup.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyComplianceGroupRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyComplianceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmIdentifyComplianceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmIdentifyComplianceGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmIdentifyComplianceGroupCopy(self, request):
        r"""Replicate a dspm data identification template.

        :param request: Request instance for CreateDspmIdentifyComplianceGroupCopy.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyComplianceGroupCopyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyComplianceGroupCopyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmIdentifyComplianceGroupCopy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmIdentifyComplianceGroupCopyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmIdentifyComplianceRuleRelation(self, request):
        r"""Creates a dspm data identification template data item association

        :param request: Request instance for CreateDspmIdentifyComplianceRuleRelation.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyComplianceRuleRelationRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyComplianceRuleRelationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmIdentifyComplianceRuleRelation", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmIdentifyComplianceRuleRelationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmIdentifyInfoListExportJob(self, request):
        r"""This API is used to create a Dspm identity list export task.

        :param request: Request instance for CreateDspmIdentifyInfoListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyInfoListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyInfoListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmIdentifyInfoListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmIdentifyInfoListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmIdentifyLevelGroup(self, request):
        r"""Creating a dspm Data Identification and Classification Group

        :param request: Request instance for CreateDspmIdentifyLevelGroup.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyLevelGroupRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyLevelGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmIdentifyLevelGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmIdentifyLevelGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmIdentifyRule(self, request):
        r"""This API is used to create a dspm identification data item.

        :param request: Request instance for CreateDspmIdentifyRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmIdentifyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmIdentifyRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmIdentifyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmPersonalIdentify(self, request):
        r"""Create a Dspm personal identity id.

        :param request: Request instance for CreateDspmPersonalIdentify.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmPersonalIdentifyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmPersonalIdentifyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmPersonalIdentify", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmPersonalIdentifyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmResource(self, request):
        r"""Create a Dspm instance

        :param request: Request instance for CreateDspmResource.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmResourceRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmResource", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmRiskExportJob(self, request):
        r"""Create a Dspm risk export task

        :param request: Request instance for CreateDspmRiskExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmRiskExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmRiskExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmRiskExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmRiskExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmRiskStrategy(self, request):
        r"""This API is used to create a Dspm custom risk policy.

        :param request: Request instance for CreateDspmRiskStrategy.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmRiskStrategyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmRiskStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmRiskStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmRiskStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDspmWhitelistStrategy(self, request):
        r"""Create a Dspm allowlist policy.

        :param request: Request instance for CreateDspmWhitelistStrategy.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDspmWhitelistStrategyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDspmWhitelistStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDspmWhitelistStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDspmWhitelistStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDynamicAssetsExportJob(self, request):
        r"""Creates a public network asset export task

        :param request: Request instance for CreateDynamicAssetsExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDynamicAssetsExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDynamicAssetsExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDynamicAssetsExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDynamicAssetsExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEDRManualScan(self, request):
        r"""Triggered after you click start scanning. It supports multi-account and multiple asset types. When both hosts and container clusters are selected, it splits into two independent tasks (host + container).

        :param request: Request instance for CreateEDRManualScan.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateEDRManualScanRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateEDRManualScanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEDRManualScan", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEDRManualScanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEdrAlertExportJob(self, request):
        r"""This API is used to create an EDR alert export task.

        :param request: Request instance for CreateEdrAlertExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateEdrAlertExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateEdrAlertExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEdrAlertExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEdrAlertExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEdrLessAlertExportJob(self, request):
        r"""This API is used to create an EDR alert ordinary export task.

        :param request: Request instance for CreateEdrLessAlertExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateEdrLessAlertExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateEdrLessAlertExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEdrLessAlertExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEdrLessAlertExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateExposureAutoTagRule(self, request):
        r"""Create rules for automatic cloud boundary tagging.

        :param request: Request instance for CreateExposureAutoTagRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateExposureAutoTagRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateExposureAutoTagRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateExposureAutoTagRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateExposureAutoTagRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateExposuresExportJob(self, request):
        r"""Export Task for Exposed Assets

        :param request: Request instance for CreateExposuresExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateExposuresExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateExposuresExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateExposuresExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateExposuresExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHighBaseLineRisksExportJob(self, request):
        r"""This API is used to create a high-risk baseline risk export task.

        :param request: Request instance for CreateHighBaseLineRisksExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateHighBaseLineRisksExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateHighBaseLineRisksExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHighBaseLineRisksExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHighBaseLineRisksExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHostImageListExportJob(self, request):
        r"""Create a local image list export task. The export fields include image ID, image name, mirror version, number of associated containers, number of associated hosts, creation time, account nickname, and risk fields such as scan status, vulnerability, Trojan, and sensitive information. Filtering is supported. Export is implemented through an async task. After JobId is returned, the frontend polls to query the export task status. In single account mode, the NickName field is automatically excluded.

        :param request: Request instance for CreateHostImageListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateHostImageListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateHostImageListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHostImageListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHostImageListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHostVulExportJob(self, request):
        r"""This API is used to create a host vulnerability table export task.

        :param request: Request instance for CreateHostVulExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateHostVulExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateHostVulExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHostVulExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHostVulExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIaCAccessToken(self, request):
        r"""Create an IaC detection integration Token.

        :param request: Request instance for CreateIaCAccessToken.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateIaCAccessTokenRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateIaCAccessTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIaCAccessToken", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIaCAccessTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIaCFileExportJob(self, request):
        r"""Creates an IaC detection file export task

        :param request: Request instance for CreateIaCFileExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateIaCFileExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateIaCFileExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIaCFileExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIaCFileExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIaCFileReScanTask(self, request):
        r"""This API is used to create an IaC detection file rescan task.

        :param request: Request instance for CreateIaCFileReScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateIaCFileReScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateIaCFileReScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIaCFileReScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIaCFileReScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageAssetListExportJob(self, request):
        r"""Create an image asset list export task

        :param request: Request instance for CreateImageAssetListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageAssetListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageAssetListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageAssetListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageAssetListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageAssociatedContainerListExportJob(self, request):
        r"""Create an image associated container asset export task

        :param request: Request instance for CreateImageAssociatedContainerListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageAssociatedContainerListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageAssociatedContainerListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageAssociatedContainerListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageAssociatedContainerListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageAssociatedHostListExportJob(self, request):
        r"""Create image associated host asset list export task

        :param request: Request instance for CreateImageAssociatedHostListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageAssociatedHostListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageAssociatedHostListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageAssociatedHostListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageAssociatedHostListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageComponentListExportJob(self, request):
        r"""Create an image component list export task.

        :param request: Request instance for CreateImageComponentListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageComponentListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageComponentListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageComponentListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageComponentListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageLayerVulListExportJob(self, request):
        r"""Create Image Layer Vulnerability List Export Task

        :param request: Request instance for CreateImageLayerVulListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageLayerVulListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageLayerVulListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageLayerVulListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageLayerVulListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageRegistryConnectivityTask(self, request):
        r"""This API is used to create a mirror repository connectivity check task.

        :param request: Request instance for CreateImageRegistryConnectivityTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageRegistryConnectivityTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageRegistryConnectivityTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageRegistryConnectivityTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageRegistryConnectivityTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageRegistryListExportJob(self, request):
        r"""This API is used to create an image repository list export task.

        :param request: Request instance for CreateImageRegistryListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageRegistryListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageRegistryListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageRegistryListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageRegistryListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageRegistryScanTask(self, request):
        r"""Creating an Image Scanning Task

        :param request: Request instance for CreateImageRegistryScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageRegistryScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageRegistryScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageRegistryScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageRegistryScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageRegistryTimedScanTaskConfig(self, request):
        r"""Create an image scanning task configuration for an image repository

        :param request: Request instance for CreateImageRegistryTimedScanTaskConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageRegistryTimedScanTaskConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageRegistryTimedScanTaskConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageRegistryTimedScanTaskConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageRegistryTimedScanTaskConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageSensitiveInfoListExportJob(self, request):
        r"""Create Image Sensitive Information List Export Task

        :param request: Request instance for CreateImageSensitiveInfoListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageSensitiveInfoListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageSensitiveInfoListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageSensitiveInfoListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageSensitiveInfoListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageSensitiveWhitelist(self, request):
        r"""This API is used to create an allowlist for sensitive information in container images.

        :param request: Request instance for CreateImageSensitiveWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageSensitiveWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageSensitiveWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageSensitiveWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageSensitiveWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageVirusListExportJob(self, request):
        r"""Create an image Trojan virus list export task

        :param request: Request instance for CreateImageVirusListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageVirusListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageVirusListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageVirusListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageVirusListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageVirusWhitelist(self, request):
        r"""This API is used to create an image Trojan allowlist.

        :param request: Request instance for CreateImageVirusWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageVirusWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageVirusWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageVirusWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageVirusWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageVulListExportJob(self, request):
        r"""This API is used to create a task of exporting the image vulnerability list.

        :param request: Request instance for CreateImageVulListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageVulListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageVulListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageVulListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageVulListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageVulSummaryListExportJob(self, request):
        r"""Creates an export task for the vulnerability overview list of an image.

        :param request: Request instance for CreateImageVulSummaryListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageVulSummaryListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageVulSummaryListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageVulSummaryListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageVulSummaryListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageVulWhitelist(self, request):
        r"""This API is used to create a vulnerability allowlist for container images.

        :param request: Request instance for CreateImageVulWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateImageVulWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateImageVulWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageVulWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageVulWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePodContainerListExportJob(self, request):
        r"""This API is used to create a Pod associated container list export task. Export fields include container ID, container name, running state, node ID, node type, image ID, image name, and isolation status. Filtering is supported. Export is implemented through an async task. After JobId is returned, front-end polling is used to query the export task status.

        :param request: Request instance for CreatePodContainerListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreatePodContainerListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreatePodContainerListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePodContainerListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePodContainerListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePodServiceListExportJob(self, request):
        r"""Creates a Pod Association service list export task. The export fields include service name, type, Selector, namespace, and creation time. Filtering is supported. When PodUniqueID is input, the Pod Association matching logic of DescribeClusterServiceList is reused. Export is implemented through an async task, and after JobId is returned, the frontend polls to query the export task status.

        :param request: Request instance for CreatePodServiceListExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreatePodServiceListExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreatePodServiceListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePodServiceListExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePodServiceListExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePublicAssetsExportJob(self, request):
        r"""This API is used to create a public network asset export task.

        :param request: Request instance for CreatePublicAssetsExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreatePublicAssetsExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreatePublicAssetsExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePublicAssetsExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePublicAssetsExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRiskCenterScanTask(self, request):
        r"""Create Risk Center Scan Task

        :param request: Request instance for CreateRiskCenterScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateRiskCenterScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateRiskCenterScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRiskCenterScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRiskCenterScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRiskDetailExportJob(self, request):
        r"""Sample code for creating a cloud resource configuration check risk details export task

        :param request: Request instance for CreateRiskDetailExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateRiskDetailExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateRiskDetailExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRiskDetailExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRiskDetailExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSandboxACLRule(self, request):
        r"""This API is used to create an ACL user access control rule. You can refer to several system rules or define a custom rule. At least one of them must be provided.

        :param request: Request instance for CreateSandboxACLRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateSandboxACLRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateSandboxACLRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSandboxACLRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSandboxACLRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSandboxDLPRule(self, request):
        r"""Create a DLP user rule. You can reference several system rules (SystemRuleIDList) or define a custom rule (UserRuleContent, name + regular). At least one of both is required. UserRuleInfo is a newly-added optional structured input parameter. When it is passed together with UserRuleContent, UserRuleInfo takes precedence.

        :param request: Request instance for CreateSandboxDLPRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateSandboxDLPRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateSandboxDLPRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSandboxDLPRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSandboxDLPRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSandboxFileRule(self, request):
        r"""Create command sandbox file access policy

        :param request: Request instance for CreateSandboxFileRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateSandboxFileRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateSandboxFileRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSandboxFileRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSandboxFileRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSandboxLLMAuditRule(self, request):
        r"""This API is used to create an LLM audit user rule. It must refer to at least one system rule and does not support user customization of rule content.

        :param request: Request instance for CreateSandboxLLMAuditRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateSandboxLLMAuditRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateSandboxLLMAuditRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSandboxLLMAuditRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSandboxLLMAuditRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateScanStatisticExportJob(self, request):
        r"""Exported task for exposed surface scanning results

        :param request: Request instance for CreateScanStatisticExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateScanStatisticExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateScanStatisticExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateScanStatisticExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateScanStatisticExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateScanTask(self, request):
        r"""This API is used to create an immediate detection task.

        :param request: Request instance for CreateScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSkillScan(self, request):
        r"""Upload a Skill ZIP file to trigger asynchronous security detection. After a successful upload, poll the DescribeSkillScanResult API using the returned ContentHash and EngineVersion to obtain the result. The upload API is idempotent. Re-uploading a file with the same Hash does not create a repetition task. Detection results are retained for 90 days. Re-upload for detection after the retention period expires.

        :param request: Request instance for CreateSkillScan.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateSkillScanRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateSkillScanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSkillScan", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSkillScanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVulFixRetryTask(self, request):
        r"""Retry the vulnerability repair task that failed to fix, and redispatch the repair instruction only for the hosts of the original task that failed to fix. Retry is allowed only when the task status is partially or totally failed to fix.

        :param request: Request instance for CreateVulFixRetryTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateVulFixRetryTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateVulFixRetryTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulFixRetryTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVulFixRetryTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVulFixTask(self, request):
        r"""Users manually submit vulnerability repair tasks, specify the vulnerabilities and target hosts that need to be repaired, and the system creates fixing tasks and dispatches execution. It supports options such as specifying the repair timeout period and whether to create a snapshot. The FixItems array is used to precisely control which hosts each vulnerability or KB patch repairs.

        :param request: Request instance for CreateVulFixTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateVulFixTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateVulFixTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulFixTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVulFixTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVulFixedExportJob(self, request):
        r"""Create an export task for the list of fixed vulnerabilities. It supports the same filter criteria as DescribeVulFixedList. The export is implemented via an asynchronous task. After a JobID is returned, the frontend polls to query the export task status. The export fields include vulnerability ID, vulnerability name, vulnerability level, VPR rating, vulnerability type, CVE ID, host name, instance ID, associated component & path, and repair time.

        :param request: Request instance for CreateVulFixedExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateVulFixedExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateVulFixedExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulFixedExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVulFixedExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVulReScan(self, request):
        r"""This API is used to create a vulnerability rescan

        :param request: Request instance for CreateVulReScan.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateVulReScanRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateVulReScanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulReScan", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVulReScanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVulRisksExportJob(self, request):
        r"""This API is used to create a vulnerability risk export task.

        :param request: Request instance for CreateVulRisksExportJob.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateVulRisksExportJobRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateVulRisksExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulRisksExportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVulRisksExportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVulScanManual(self, request):
        r"""This API is used to create a vulnerability scanning (one-click scan).

        :param request: Request instance for CreateVulScanManual.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateVulScanManualRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateVulScanManualResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulScanManual", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVulScanManualResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAIAnalysisSMTPAccess(self, request):
        r"""Delete the SMTP mailbox access information of the AI assistant.

        :param request: Request instance for DeleteAIAnalysisSMTPAccess.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteAIAnalysisSMTPAccessRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteAIAnalysisSMTPAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAIAnalysisSMTPAccess", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAIAnalysisSMTPAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAISchedule(self, request):
        r"""This API is used to delete AI scheduled tasks.

        This API is used to delete a scheduled task based on the specified AI scheduled task ID. Deletion is irreversible.

        :param request: Request instance for DeleteAISchedule.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteAIScheduleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteAIScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAISchedule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAIScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAssetFilterView(self, request):
        r"""Delete the search view of a user-created specified asset

        :param request: Request instance for DeleteAssetFilterView.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteAssetFilterViewRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteAssetFilterViewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAssetFilterView", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAssetFilterViewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAssetTag(self, request):
        r"""Delete asset tag

        :param request: Request instance for DeleteAssetTag.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteAssetTagRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteAssetTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAssetTag", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAssetTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBaselineSelfDefinedPolicyList(self, request):
        r"""Delete custom baseline policies in batches. Only support deletion of policies with PolicyType=SELF. After deletion, historical risk records are retained, but no new results are generated.

        :param request: Request instance for DeleteBaselineSelfDefinedPolicyList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteBaselineSelfDefinedPolicyListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteBaselineSelfDefinedPolicyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBaselineSelfDefinedPolicyList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBaselineSelfDefinedPolicyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCSIPMalwareScanTask(self, request):
        r"""CSIP manual scan task delete API

        :param request: Request instance for DeleteCSIPMalwareScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteCSIPMalwareScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteCSIPMalwareScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCSIPMalwareScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCSIPMalwareScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCluster(self, request):
        r"""Deleting a cluster

        :param request: Request instance for DeleteCluster.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteClusterRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCluster", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDomainAndIp(self, request):
        r"""Delete Domain and IP Request

        :param request: Request instance for DeleteDomainAndIp.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDomainAndIpRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDomainAndIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDomainAndIp", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDomainAndIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmApplyOrder(self, request):
        r"""Deletes a Dspm application form.

        :param request: Request instance for DeleteDspmApplyOrder.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmApplyOrderRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmApplyOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmApplyOrder", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmApplyOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmAssetAccount(self, request):
        r"""Delete a Dspm asset account

        :param request: Request instance for DeleteDspmAssetAccount.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmAssetAccountRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmAssetAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmAssetAccount", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmAssetAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmAuditFilterStrategy(self, request):
        r"""Delete a Dspm audit filter policy

        :param request: Request instance for DeleteDspmAuditFilterStrategy.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmAuditFilterStrategyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmAuditFilterStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmAuditFilterStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmAuditFilterStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmBackupLogList(self, request):
        r"""This API is used to delete the backup logs.

        :param request: Request instance for DeleteDspmBackupLogList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmBackupLogListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmBackupLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmBackupLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmBackupLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmCkafkaConfig(self, request):
        r"""This API is used to cancel the log shipping configuration.

        :param request: Request instance for DeleteDspmCkafkaConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmCkafkaConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmCkafkaConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmCkafkaConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmCkafkaConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmExportTask(self, request):
        r"""This API is used to delete export tasks.

        :param request: Request instance for DeleteDspmExportTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmExportTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmExportTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmExportTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmExportTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmIdentifyCategory(self, request):
        r"""Delete dspm data identification category

        :param request: Request instance for DeleteDspmIdentifyCategory.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmIdentifyCategoryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmIdentifyCategoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmIdentifyCategory", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmIdentifyCategoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmIdentifyComplianceCategoryRelation(self, request):
        r"""Deletes classification association from a dspm identification template

        :param request: Request instance for DeleteDspmIdentifyComplianceCategoryRelation.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmIdentifyComplianceCategoryRelationRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmIdentifyComplianceCategoryRelationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmIdentifyComplianceCategoryRelation", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmIdentifyComplianceCategoryRelationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmIdentifyComplianceGroup(self, request):
        r"""Delete dspm data identification template

        :param request: Request instance for DeleteDspmIdentifyComplianceGroup.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmIdentifyComplianceGroupRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmIdentifyComplianceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmIdentifyComplianceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmIdentifyComplianceGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmIdentifyComplianceRuleRelation(self, request):
        r"""Delete dspm data identification template data item association

        :param request: Request instance for DeleteDspmIdentifyComplianceRuleRelation.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmIdentifyComplianceRuleRelationRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmIdentifyComplianceRuleRelationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmIdentifyComplianceRuleRelation", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmIdentifyComplianceRuleRelationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmIdentifyLevelGroup(self, request):
        r"""Delete a dspm data identification classification group

        :param request: Request instance for DeleteDspmIdentifyLevelGroup.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmIdentifyLevelGroupRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmIdentifyLevelGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmIdentifyLevelGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmIdentifyLevelGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmIdentifyRule(self, request):
        r"""Delete dspm data identification data item

        :param request: Request instance for DeleteDspmIdentifyRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmIdentifyRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmIdentifyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmIdentifyRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmIdentifyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmPersonalIdentify(self, request):
        r"""Delete a Dspm personal identity id.

        :param request: Request instance for DeleteDspmPersonalIdentify.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmPersonalIdentifyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmPersonalIdentifyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmPersonalIdentify", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmPersonalIdentifyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmRestoreLogList(self, request):
        r"""Delete restore logs

        :param request: Request instance for DeleteDspmRestoreLogList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmRestoreLogListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmRestoreLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmRestoreLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmRestoreLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmRiskStrategy(self, request):
        r"""This API is used to delete a DSPM custom risk policy. It only supports deletion of custom policies with rule_source=custom. Built-in policies are non-deletable. Disable them by setting IsEnabled in ModifyDspmRiskStrategy.

        :param request: Request instance for DeleteDspmRiskStrategy.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmRiskStrategyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmRiskStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmRiskStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmRiskStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmShareUserData(self, request):
        r"""Delete dspmg shared account data

        :param request: Request instance for DeleteDspmShareUserData.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmShareUserDataRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmShareUserDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmShareUserData", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmShareUserDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDspmWhitelistStrategy(self, request):
        r"""Delete a Dspm allowlist policy.

        :param request: Request instance for DeleteDspmWhitelistStrategy.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDspmWhitelistStrategyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDspmWhitelistStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDspmWhitelistStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDspmWhitelistStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEDRRules(self, request):
        r"""This API is used to delete EDR policies.

        :param request: Request instance for DeleteEDRRules.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteEDRRulesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteEDRRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEDRRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEDRRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEDRScanTask(self, request):
        r"""This API is used to delete terminated scan tasks by physically deleting the primary and detailed tables. Only tasks in the final state can be deleted, and only the creator can perform the deletion.

        :param request: Request instance for DeleteEDRScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteEDRScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteEDRScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEDRScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEDRScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEdrLogCollectPaths(self, request):
        r"""Delete EDR log collection path configurations in batches.

        :param request: Request instance for DeleteEdrLogCollectPaths.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteEdrLogCollectPathsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteEdrLogCollectPathsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEdrLogCollectPaths", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEdrLogCollectPathsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteExposureAutoTagRule(self, request):
        r"""Delete rules for automatic cloud boundary tagging.

        :param request: Request instance for DeleteExposureAutoTagRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteExposureAutoTagRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteExposureAutoTagRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteExposureAutoTagRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteExposureAutoTagRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIaCAccessToken(self, request):
        r"""Delete an IaC detection integration Token

        :param request: Request instance for DeleteIaCAccessToken.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteIaCAccessTokenRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteIaCAccessTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIaCAccessToken", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIaCAccessTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIaCFile(self, request):
        r"""Delete an IaC detection file

        :param request: Request instance for DeleteIaCFile.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteIaCFileRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteIaCFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIaCFile", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIaCFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImageRegistry(self, request):
        r"""Delete image repository information.

        :param request: Request instance for DeleteImageRegistry.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteImageRegistryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteImageRegistryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImageRegistry", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImageRegistryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImageRegistryScanTask(self, request):
        r"""Deletes an image repository scanning task.

        :param request: Request instance for DeleteImageRegistryScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteImageRegistryScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteImageRegistryScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImageRegistryScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImageRegistryScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImageRegistryTimedScanTaskConfig(self, request):
        r"""Delete the scheduled scan task configuration of an image repository.

        :param request: Request instance for DeleteImageRegistryTimedScanTaskConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteImageRegistryTimedScanTaskConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteImageRegistryTimedScanTaskConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImageRegistryTimedScanTaskConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImageRegistryTimedScanTaskConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImageSensitiveWhitelist(self, request):
        r"""This API is used to delete an allowlist for sensitive information from a container image.

        :param request: Request instance for DeleteImageSensitiveWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteImageSensitiveWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteImageSensitiveWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImageSensitiveWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImageSensitiveWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImageVirusWhitelist(self, request):
        r"""This API is used to delete the image Trojan allowlist.

        :param request: Request instance for DeleteImageVirusWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteImageVirusWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteImageVirusWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImageVirusWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImageVirusWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImageVulWhitelist(self, request):
        r"""Deletes the vulnerability allowlist of a container image

        :param request: Request instance for DeleteImageVulWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteImageVulWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteImageVulWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImageVulWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImageVulWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLoginWhiteList(self, request):
        r"""This API is used to delete the cross-region log-in allowlist rules.

        :param request: Request instance for DeleteLoginWhiteList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteLoginWhiteListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteLoginWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLoginWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLoginWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMachineClearHistory(self, request):
        r"""This API is used to delete clearing records of a machine.

        :param request: Request instance for DeleteMachineClearHistory.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteMachineClearHistoryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteMachineClearHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMachineClearHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMachineClearHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRiskScanTask(self, request):
        r"""Delete Risk Center Scan Task

        :param request: Request instance for DeleteRiskScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteRiskScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteRiskScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRiskScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRiskScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSandboxACLRule(self, request):
        r"""Delete ACL user rules in batches. After deletion, rules are no longer returned in list queries and no longer take effect on traffic. If any ID does not exist or belongs to another tenant, an error is returned overall.

        :param request: Request instance for DeleteSandboxACLRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteSandboxACLRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteSandboxACLRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSandboxACLRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSandboxACLRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSandboxDLPRule(self, request):
        r"""Batch delete DLP user rules. If any ID does not exist or belongs to another tenant, an error is returned for the entire request.

        :param request: Request instance for DeleteSandboxDLPRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteSandboxDLPRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteSandboxDLPRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSandboxDLPRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSandboxDLPRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSandboxFileRule(self, request):
        r"""Create command sandbox file access policy

        :param request: Request instance for DeleteSandboxFileRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteSandboxFileRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteSandboxFileRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSandboxFileRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSandboxFileRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSandboxLLMAuditRule(self, request):
        r"""Batch delete LLM audit user rules. If any ID does not exist or belongs to another tenant, an error is returned overall.

        :param request: Request instance for DeleteSandboxLLMAuditRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteSandboxLLMAuditRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteSandboxLLMAuditRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSandboxLLMAuditRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSandboxLLMAuditRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVulWhitelist(self, request):
        r"""This API is used to delete a vulnerability allowlist.

        :param request: Request instance for DeleteVulWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteVulWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteVulWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVulWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVulWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWebhookPolicies(self, request):
        r"""Delete notification policies in batches.

        :param request: Request instance for DeleteWebhookPolicies.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteWebhookPoliciesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteWebhookPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWebhookPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWebhookPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWebhookReceivers(self, request):
        r"""Delete receiving robots in batches. Before deletion, the reference relationships are automatically removed from all policies that refer to these robots.

        :param request: Request instance for DeleteWebhookReceivers.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteWebhookReceiversRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteWebhookReceiversResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWebhookReceivers", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWebhookReceiversResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIAgentAssetList(self, request):
        r"""Search for AI agent asset list.

        :param request: Request instance for DescribeAIAgentAssetList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAIAgentAssetListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAIAgentAssetListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIAgentAssetList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIAgentAssetListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIAgentCredentialList(self, request):
        r"""Retrieves the scan list of AIAgent asset credentials

        :param request: Request instance for DescribeAIAgentCredentialList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAIAgentCredentialListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAIAgentCredentialListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIAgentCredentialList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIAgentCredentialListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIAgentCredentialLocationList(self, request):
        r"""This API is used to query the leaked location list of one credential by credential group row ID in pages. It is used with the DescribeAIAgentCredentialList interface in the split and unfold scenario to avoid performance issues caused by pulling hundreds of thousands of locations at once in data skew scenarios.

        :param request: Request instance for DescribeAIAgentCredentialLocationList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAIAgentCredentialLocationListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAIAgentCredentialLocationListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIAgentCredentialLocationList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIAgentCredentialLocationListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIAgentSkillList(self, request):
        r"""Search the skill list of an AI Agent

        :param request: Request instance for DescribeAIAgentSkillList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAIAgentSkillListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAIAgentSkillListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIAgentSkillList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIAgentSkillListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIAnalysisFileDownloadURL(self, request):
        r"""Get the temporary download link of an AI analysis file.

        The original address of the input file. Returns a signed temporary download link with a validity period of 2 hours.

        :param request: Request instance for DescribeAIAnalysisFileDownloadURL.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAIAnalysisFileDownloadURLRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAIAnalysisFileDownloadURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIAnalysisFileDownloadURL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIAnalysisFileDownloadURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIAnalysisHistory(self, request):
        r"""Retrieve historical analysis records of the cloud security AI assistant.

        :param request: Request instance for DescribeAIAnalysisHistory.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAIAnalysisHistoryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAIAnalysisHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIAnalysisHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIAnalysisHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIAnalysisRecommendQuestions(self, request):
        r"""Retrieve recommended questions for AI QA.

        :param request: Request instance for DescribeAIAnalysisRecommendQuestions.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAIAnalysisRecommendQuestionsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAIAnalysisRecommendQuestionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIAnalysisRecommendQuestions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIAnalysisRecommendQuestionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIAnalysisRobotInfo(self, request):
        r"""This API is used to obtain basic information of the Cloud Security AI Assistant.

        :param request: Request instance for DescribeAIAnalysisRobotInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAIAnalysisRobotInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAIAnalysisRobotInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIAnalysisRobotInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIAnalysisRobotInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIAnalysisSMTP(self, request):
        r"""Query SMTP mailbox access information of the AI assistant

        :param request: Request instance for DescribeAIAnalysisSMTP.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAIAnalysisSMTPRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAIAnalysisSMTPResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIAnalysisSMTP", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIAnalysisSMTPResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAILinkSetting(self, request):
        r"""Query the AI-Link engine configuration

        :param request: Request instance for DescribeAILinkSetting.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAILinkSettingRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAILinkSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAILinkSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAILinkSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIScheduleList(self, request):
        r"""Query the list of AI scheduled tasks.

        Supports paging query and status filtering, and returns the scheduled task list and total number of entries.

        :param request: Request instance for DescribeAIScheduleList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAIScheduleListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAIScheduleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIScheduleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIScheduleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAISchedulePlanList(self, request):
        r"""Queries AI scheduled task trigger plans.

        This API is used to query the future trigger plan list of a specified AI scheduled task within a given time window.

        :param request: Request instance for DescribeAISchedulePlanList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAISchedulePlanListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAISchedulePlanListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAISchedulePlanList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAISchedulePlanListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIScheduleStats(self, request):
        r"""Queries AI scheduled task statistics information.

        Returns the total number of scheduled tasks and the number of running tasks for the current user.

        :param request: Request instance for DescribeAIScheduleStats.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAIScheduleStatsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAIScheduleStatsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIScheduleStats", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIScheduleStatsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIScheduleTaskDetail(self, request):
        r"""Queries the details of AI scheduled task executions.

        This API is used to query the detailed information of a specified task execution by task ID, including the execution status and results.

        :param request: Request instance for DescribeAIScheduleTaskDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAIScheduleTaskDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAIScheduleTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIScheduleTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIScheduleTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIScheduleTaskList(self, request):
        r"""This API is used to query the scheduled AI task execution list.

        Queries the historical execution records of AI scheduled tasks. Supports pagination and filtering by scheduled task ID.

        :param request: Request instance for DescribeAIScheduleTaskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAIScheduleTaskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAIScheduleTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIScheduleTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIScheduleTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAKAnalysisDetail(self, request):
        r"""Access key alarm record AI analysis result details

        :param request: Request instance for DescribeAKAnalysisDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAKAnalysisDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAKAnalysisDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAKAnalysisDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAKAnalysisDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAbTestUser(self, request):
        r"""Determine whether the user is a grayscale user

        :param request: Request instance for DescribeAbTestUser.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAbTestUserRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAbTestUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAbTestUser", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAbTestUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAbnormalCallRecord(self, request):
        r"""Get the call record list

        :param request: Request instance for DescribeAbnormalCallRecord.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAbnormalCallRecordRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAbnormalCallRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAbnormalCallRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAbnormalCallRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessKeyAlarm(self, request):
        r"""List of access key alarm records

        :param request: Request instance for DescribeAccessKeyAlarm.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyAlarmRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyAlarmResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessKeyAlarm", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessKeyAlarmResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessKeyAlarmDetail(self, request):
        r"""Access key alarm record details

        :param request: Request instance for DescribeAccessKeyAlarmDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyAlarmDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyAlarmDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessKeyAlarmDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessKeyAlarmDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessKeyAsset(self, request):
        r"""Retrieve the user access key asset list

        :param request: Request instance for DescribeAccessKeyAsset.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyAssetRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyAssetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessKeyAsset", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessKeyAssetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessKeyRisk(self, request):
        r"""List of access key risk records

        :param request: Request instance for DescribeAccessKeyRisk.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyRiskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyRiskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessKeyRisk", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessKeyRiskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessKeyRiskDetail(self, request):
        r"""Access key risk record details

        :param request: Request instance for DescribeAccessKeyRiskDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyRiskDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyRiskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessKeyRiskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessKeyRiskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessKeyUserDetail(self, request):
        r"""This API is used to query account details of a user.

        :param request: Request instance for DescribeAccessKeyUserDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyUserDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyUserDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessKeyUserDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessKeyUserDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessKeyUserList(self, request):
        r"""Query user account list

        :param request: Request instance for DescribeAccessKeyUserList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyUserListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyUserListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessKeyUserList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessKeyUserListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessKeyWhiteList(self, request):
        r"""Access key alarm record list

        :param request: Request instance for DescribeAccessKeyWhiteList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyWhiteListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAccessKeyWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessKeyWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessKeyWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentConfigSetting(self, request):
        r"""Query client configuration settings (configuration group). This is a standalone API split from DescribeAgentRunMode.

        :param request: Request instance for DescribeAgentConfigSetting.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAgentConfigSettingRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAgentConfigSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentConfigSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentConfigSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentRunMode(self, request):
        r"""Get the client running mode and runtime configuration information

        :param request: Request instance for DescribeAgentRunMode.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAgentRunModeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAgentRunModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentRunMode", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentRunModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentRunPolicy(self, request):
        r"""Query client running policies (policy groups). This is a standalone API split from DescribeAgentRunMode.

        :param request: Request instance for DescribeAgentRunPolicy.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAgentRunPolicyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAgentRunPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentRunPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentRunPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlertList(self, request):
        r"""Alarm Center full alarm list API

        :param request: Request instance for DescribeAlertList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAlertListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAlertListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlertList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlertListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetComponentList(self, request):
        r"""Query the component list in an asset.

        :param request: Request instance for DescribeAssetComponentList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetComponentListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetComponentListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetComponentList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetComponentListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetComponentRelatedImageList(self, request):
        r"""Queries the list of associated images of image repository components.

        :param request: Request instance for DescribeAssetComponentRelatedImageList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetComponentRelatedImageListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetComponentRelatedImageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetComponentRelatedImageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetComponentRelatedImageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetDetail(self, request):
        r"""Asset detail information

        :param request: Request instance for DescribeAssetDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetFilterViews(self, request):
        r"""Asset search view

        :param request: Request instance for DescribeAssetFilterViews.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetFilterViewsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetFilterViewsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetFilterViews", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetFilterViewsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetInfo(self, request):
        r"""Asset information

        :param request: Request instance for DescribeAssetInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetLastSyncTime(self, request):
        r"""Last Synchronization Time of Assets

        :param request: Request instance for DescribeAssetLastSyncTime.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetLastSyncTimeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetLastSyncTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetLastSyncTime", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetLastSyncTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetOverview(self, request):
        r"""Asset Overview statistics

        :param request: Request instance for DescribeAssetOverview.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetOverviewRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetProcessList(self, request):
        r"""This API is used to query the process list of host nodes on exposed paths in cloud boundary analysis.

        :param request: Request instance for DescribeAssetProcessList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetProcessListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetProcessListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetProcessList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetProcessListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetRiskDetail(self, request):
        r"""Asset risk details

        :param request: Request instance for DescribeAssetRiskDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetRiskDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetRiskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetRiskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetRiskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetRiskList(self, request):
        r"""Cloud resource configuration risk list from the asset perspective

        :param request: Request instance for DescribeAssetRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetSyncTaskStatus(self, request):
        r"""Asset sync task status

        :param request: Request instance for DescribeAssetSyncTaskStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetSyncTaskStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetSyncTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetSyncTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetSyncTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetTagAttributes(self, request):
        r"""Retrieves asset tag attributes

        :param request: Request instance for DescribeAssetTagAttributes.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetTagAttributesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetTagAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetTagAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetTagAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetTagTree(self, request):
        r"""Asset tag tree structured data

        :param request: Request instance for DescribeAssetTagTree.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetTagTreeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetTagTreeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetTagTree", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetTagTreeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetTags(self, request):
        r"""All assets

        :param request: Request instance for DescribeAssetTags.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetTagsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetTags", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetTree(self, request):
        r"""Asset tree structure

        :param request: Request instance for DescribeAssetTree.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetTreeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetTreeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetTree", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetTreeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetViewVulRiskList(self, request):
        r"""Obtain Vulnerability Risk List from Asset's Perspective

        :param request: Request instance for DescribeAssetViewVulRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeAssetViewVulRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeAssetViewVulRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetViewVulRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetViewVulRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackendScanEngineRegionList(self, request):
        r"""This API is used to query the region list of the backend scanning engine.

        :param request: Request instance for DescribeBackendScanEngineRegionList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBackendScanEngineRegionListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBackendScanEngineRegionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackendScanEngineRegionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackendScanEngineRegionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBanMode(self, request):
        r"""This API is used to obtain the brute-force blocking mode.

        :param request: Request instance for DescribeBanMode.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBanModeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBanModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBanMode", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBanModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBanStatus(self, request):
        r"""This API is used to obtain the block button status.

        :param request: Request instance for DescribeBanStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBanStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBanStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBanStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBanStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineAggregatedItemList(self, request):
        r"""This API is used to obtain the aggregated scan result list by detection item, for showing the number of passed and failed assets by detection item on the "Detection Item" Tab of the policy details page.

        :param request: Request instance for DescribeBaselineAggregatedItemList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineAggregatedItemListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineAggregatedItemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineAggregatedItemList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineAggregatedItemListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineAggregatedPolicyList(self, request):
        r"""This API is used to get the aggregation scan result list by baseline policy dimension, for the "Baseline Scan Policy" module on the overview page to display pass/fail status by policy.

        :param request: Request instance for DescribeBaselineAggregatedPolicyList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineAggregatedPolicyListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineAggregatedPolicyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineAggregatedPolicyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineAggregatedPolicyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineCalculatingStatisticsPolicyIDList(self, request):
        r"""Queries the list of Policy IDs currently at the "statistical calculation" status, used for frontend polling to judge whether the scan results statistics are ready.

        :param request: Request instance for DescribeBaselineCalculatingStatisticsPolicyIDList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineCalculatingStatisticsPolicyIDListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineCalculatingStatisticsPolicyIDListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineCalculatingStatisticsPolicyIDList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineCalculatingStatisticsPolicyIDListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineCategoryItemList(self, request):
        r"""This API is used to query the detection item list of a category.

        :param request: Request instance for DescribeBaselineCategoryItemList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineCategoryItemListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineCategoryItemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineCategoryItemList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineCategoryItemListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineFixRecordList(self, request):
        r"""Get the historical record list of baseline risk corrections, used to show fixed detection items and corresponding assets on the "Correction Record" page.

        :param request: Request instance for DescribeBaselineFixRecordList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineFixRecordListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineFixRecordListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineFixRecordList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineFixRecordListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineItemRiskList(self, request):
        r"""This API is used to retrieve the risk record list of detection item dimensions.

        :param request: Request instance for DescribeBaselineItemRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineItemRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineItemRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineItemRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineItemRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineMainTaskItemList(self, request):
        r"""Get the detection item list of built-in baseline classifications (parent category -> subcategory -> built-in detection item ID list) for selecting baseline detection items on the policy editing page.

        :param request: Request instance for DescribeBaselineMainTaskItemList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineMainTaskItemListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineMainTaskItemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineMainTaskItemList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineMainTaskItemListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineMainTaskList(self, request):
        r"""Get the scan main task list for the Task Record page to show the history and results of one-click scan, period scanning, and disperse scan.

        :param request: Request instance for DescribeBaselineMainTaskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineMainTaskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineMainTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineMainTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineMainTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineOverview(self, request):
        r"""Retrieve header data of the baseline overview page, including the total count of failed detection items, the number of fixes in the past one year, the last scan time, and whether period scanning is currently enabled.

        :param request: Request instance for DescribeBaselineOverview.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineOverviewRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselinePolicyCategoryList(self, request):
        r"""This API is used to retrieve the built-in baseline classification tree (parent category → subcategory → built-in detection item ID list) for policy details display.

        :param request: Request instance for DescribeBaselinePolicyCategoryList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselinePolicyCategoryListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselinePolicyCategoryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselinePolicyCategoryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselinePolicyCategoryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselinePolicyItemList(self, request):
        r"""Get the Detection Item List configured in a policy.

        :param request: Request instance for DescribeBaselinePolicyItemList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselinePolicyItemListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselinePolicyItemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselinePolicyItemList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselinePolicyItemListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselinePolicyList(self, request):
        r"""This API is used to obtain the list of baseline policies for list page display of system and custom policies and their configuration status in scenarios such as cycle plan management.

        :param request: Request instance for DescribeBaselinePolicyList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselinePolicyListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselinePolicyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselinePolicyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselinePolicyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselinePolicyNameExistAppidList(self, request):
        r"""This API is used to obtain the list of existing users for a baseline policy name.

        :param request: Request instance for DescribeBaselinePolicyNameExistAppidList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselinePolicyNameExistAppidListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselinePolicyNameExistAppidListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselinePolicyNameExistAppidList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselinePolicyNameExistAppidListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineSubTaskList(self, request):
        r"""Get the scan subtask list to show the scan status and failure reason of each host or cluster in the "Asset dimension" section of the task details page.

        :param request: Request instance for DescribeBaselineSubTaskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineSubTaskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineSubTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineSubTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineSubTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineSyncConf(self, request):
        r"""This API is used to get the baseline synchronization configuration of the current admin account. Only the Group Administrator can call this API. For ordinary member accounts, please use DescribeBaselineUserOtherConf.

        :param request: Request instance for DescribeBaselineSyncConf.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineSyncConfRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineSyncConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineSyncConf", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineSyncConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineSystemCategoryList(self, request):
        r"""Obtain the system built-in baseline classification tree (parent category → subcategory → built-in detection item ID list), used for selecting baseline detection items on the policy editing page.

        :param request: Request instance for DescribeBaselineSystemCategoryList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineSystemCategoryListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineSystemCategoryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineSystemCategoryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineSystemCategoryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineUserOtherConf(self, request):
        r"""Retrieve user-level baseline configuration for the current account.

        :param request: Request instance for DescribeBaselineUserOtherConf.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineUserOtherConfRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineUserOtherConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineUserOtherConf", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineUserOtherConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineUserWeakPasswordConf(self, request):
        r"""This API is used to search for the custom dictionary of weak passwords for users under the current account.

        :param request: Request instance for DescribeBaselineUserWeakPasswordConf.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineUserWeakPasswordConfRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBaselineUserWeakPasswordConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineUserWeakPasswordConf", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineUserWeakPasswordConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBruteAttackRules(self, request):
        r"""This API is used to obtain brute force cracking rules.

        :param request: Request instance for DescribeBruteAttackRules.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeBruteAttackRulesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeBruteAttackRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBruteAttackRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBruteAttackRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCFGRiskReportStatistics(self, request):
        r"""Risk statistics for cloud resource configuration check reports

        :param request: Request instance for DescribeCFGRiskReportStatistics.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCFGRiskReportStatisticsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCFGRiskReportStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCFGRiskReportStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCFGRiskReportStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCFGRiskStatistics(self, request):
        r"""Query the statistical information of scanning results.

        :param request: Request instance for DescribeCFGRiskStatistics.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCFGRiskStatisticsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCFGRiskStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCFGRiskStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCFGRiskStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCFWAssetStatistics(self, request):
        r"""Cloud Defense Asset Center Statistics

        :param request: Request instance for DescribeCFWAssetStatistics.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCFWAssetStatisticsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCFWAssetStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCFWAssetStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCFWAssetStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCLSLogIndexV3(self, request):
        r"""Get log index information

        :param request: Request instance for DescribeCLSLogIndexV3.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCLSLogIndexV3Request`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCLSLogIndexV3Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCLSLogIndexV3", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCLSLogIndexV3Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCLSLogListV3(self, request):
        r"""Log analytics retrieval interface v3

        :param request: Request instance for DescribeCLSLogListV3.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCLSLogListV3Request`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCLSLogListV3Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCLSLogListV3", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCLSLogListV3Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCSCPayInfo(self, request):
        r"""Query the consolidated billing information of the current account, including order status, payment mode, quotas, and other detailed information.

        :param request: Request instance for DescribeCSCPayInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCSCPayInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCSCPayInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCSCPayInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCSCPayInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCSIPLicenseBindSchedule(self, request):
        r"""Query the progress of the async binding task returned by ModifyCSIPLicenseBinds.

        :param request: Request instance for DescribeCSIPLicenseBindSchedule.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCSIPLicenseBindScheduleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCSIPLicenseBindScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCSIPLicenseBindSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCSIPLicenseBindScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCSIPMalwareScanTaskDetail(self, request):
        r"""This API is used to get host details of a CSIP scan task.

        :param request: Request instance for DescribeCSIPMalwareScanTaskDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCSIPMalwareScanTaskDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCSIPMalwareScanTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCSIPMalwareScanTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCSIPMalwareScanTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCSIPMalwareScanTaskProgress(self, request):
        r"""This API is used to query the progress of CSIP manual scan.

        :param request: Request instance for DescribeCSIPMalwareScanTaskProgress.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCSIPMalwareScanTaskProgressRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCSIPMalwareScanTaskProgressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCSIPMalwareScanTaskProgress", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCSIPMalwareScanTaskProgressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCSIPRiskStatistics(self, request):
        r"""Obtain risk center risk overview sample code

        :param request: Request instance for DescribeCSIPRiskStatistics.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCSIPRiskStatisticsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCSIPRiskStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCSIPRiskStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCSIPRiskStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCSPMPayInfo(self, request):
        r"""This API is used to obtain purchased CSPM order information.

        :param request: Request instance for DescribeCSPMPayInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCSPMPayInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCSPMPayInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCSPMPayInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCSPMPayInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCVMAssetInfo(self, request):
        r"""CVM Details

        :param request: Request instance for DescribeCVMAssetInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCVMAssetInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCVMAssetInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCVMAssetInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCVMAssetInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCVMAssets(self, request):
        r"""Get cvm list

        :param request: Request instance for DescribeCVMAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCVMAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCVMAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCVMAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCVMAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCWPExposePath(self, request):
        r"""Queries cloud boundary analysis path nodes (dedicated for hosts)

        :param request: Request instance for DescribeCWPExposePath.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCWPExposePathRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCWPExposePathResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCWPExposePath", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCWPExposePathResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCWPExposures(self, request):
        r"""Cloud boundary analysis asset list (suitable for host assets)

        :param request: Request instance for DescribeCWPExposures.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCWPExposuresRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCWPExposuresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCWPExposures", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCWPExposuresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCWPLicenseBindSchedule(self, request):
        r"""This API is used to query the binding task progress of the authorization.

        :param request: Request instance for DescribeCWPLicenseBindSchedule.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCWPLicenseBindScheduleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCWPLicenseBindScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCWPLicenseBindSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCWPLicenseBindScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCWPMachineDetail(self, request):
        r"""Host details

        :param request: Request instance for DescribeCWPMachineDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCWPMachineDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCWPMachineDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCWPMachineDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCWPMachineDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCWPMachineOsList(self, request):
        r"""This API is used to query the machine operating system list.

        :param request: Request instance for DescribeCWPMachineOsList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCWPMachineOsListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCWPMachineOsListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCWPMachineOsList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCWPMachineOsListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCWPMachines(self, request):
        r"""Host list

        :param request: Request instance for DescribeCWPMachines.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCWPMachinesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCWPMachinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCWPMachines", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCWPMachinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCWPOrderList(self, request):
        r"""Query the resource order list.

        :param request: Request instance for DescribeCWPOrderList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCWPOrderListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCWPOrderListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCWPOrderList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCWPOrderListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCWPScanIpInfo(self, request):
        r"""Query Tencent Cloud scan IP information

        :param request: Request instance for DescribeCWPScanIpInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCWPScanIpInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCWPScanIpInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCWPScanIpInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCWPScanIpInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCWPTaskDuration(self, request):
        r"""Obtain Task Distribution Duration

        :param request: Request instance for DescribeCWPTaskDuration.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCWPTaskDurationRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCWPTaskDurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCWPTaskDuration", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCWPTaskDurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCallRecord(self, request):
        r"""Query the call record list

        :param request: Request instance for DescribeCallRecord.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCallRecordRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCallRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCallRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCallRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCheckConnectivityHostList(self, request):
        r"""Query the list of connectivity detection hosts

        :param request: Request instance for DescribeCheckConnectivityHostList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCheckConnectivityHostListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCheckConnectivityHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCheckConnectivityHostList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCheckConnectivityHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCheckViewRisks(self, request):
        r"""Cloud resource configuration risk list from the check perspective

        :param request: Request instance for DescribeCheckViewRisks.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCheckViewRisksRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCheckViewRisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCheckViewRisks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCheckViewRisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClbListenerList(self, request):
        r"""Queries the listener list corresponding to a specified Tencent Cloud CLB instance.

        :param request: Request instance for DescribeClbListenerList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClbListenerListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClbListenerListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClbListenerList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClbListenerListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClbListenerRules(self, request):
        r"""Queries the list of Layer 7 forwarding rules corresponding to a specified CLB instance.

        :param request: Request instance for DescribeClbListenerRules.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClbListenerRulesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClbListenerRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClbListenerRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClbListenerRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClbTargets(self, request):
        r"""Query the CLB backend service list

        :param request: Request instance for DescribeClbTargets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClbTargetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClbTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClbTargets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClbTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudAssets(self, request):
        r"""All assets

        :param request: Request instance for DescribeCloudAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCloudAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCloudAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudFunctionList(self, request):
        r"""Function list

        :param request: Request instance for DescribeCloudFunctionList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCloudFunctionListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCloudFunctionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudFunctionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudFunctionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterAssetList(self, request):
        r"""Queries the asset list of a container cluster

        :param request: Request instance for DescribeClusterAssetList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterAssetListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterAssetListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterAssetList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterAssetListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterAssetSyncTaskStatus(self, request):
        r"""This API is used to query the synchronization task status of cluster assets.

        :param request: Request instance for DescribeClusterAssetSyncTaskStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterAssetSyncTaskStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterAssetSyncTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterAssetSyncTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterAssetSyncTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterAssets(self, request):
        r"""This example shows you how to obtain the cluster list.

        :param request: Request instance for DescribeClusterAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterContainerAppList(self, request):
        r"""This API is used to query the associated application list of a container. It retrieves associated application service information by container ID and supports pagination.

        :param request: Request instance for DescribeClusterContainerAppList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerAppListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerAppListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterContainerAppList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterContainerAppListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterContainerComponentList(self, request):
        r"""Query the list of components associated with a container. Get associated component information by container ID. Pagination is supported.

        :param request: Request instance for DescribeClusterContainerComponentList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerComponentListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerComponentListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterContainerComponentList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterContainerComponentListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterContainerDetail(self, request):
        r"""This API is used to query cluster container details. It retrieves basic container info, mirror information, mount information, network info, and associated node information by container ID.

        :param request: Request instance for DescribeClusterContainerDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterContainerDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterContainerDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterContainerList(self, request):
        r"""Query the container list of a cluster.

        :param request: Request instance for DescribeClusterContainerList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterContainerList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterContainerListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterContainerPortList(self, request):
        r"""Query the list of ports associated with a container. This API is used to obtain associated port information by container ID and supports pagination.

        :param request: Request instance for DescribeClusterContainerPortList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerPortListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerPortListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterContainerPortList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterContainerPortListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterContainerProcessList(self, request):
        r"""This API is used to query the associated process list of a container. It obtains associated process information by container ID, supports time sorting and pagination. Filter.By supports StartTime; Filter.Order supports ASC/DESC.

        :param request: Request instance for DescribeClusterContainerProcessList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerProcessListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerProcessListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterContainerProcessList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterContainerProcessListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterContainerWebServiceList(self, request):
        r"""This API is used to query the associated Web Service List of a container. It retrieves associated web service information by container ID and supports pagination.

        :param request: Request instance for DescribeClusterContainerWebServiceList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerWebServiceListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterContainerWebServiceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterContainerWebServiceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterContainerWebServiceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterDetail(self, request):
        r"""Querying Cluster Details

        :param request: Request instance for DescribeClusterDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterInstallCommand(self, request):
        r"""Query the cluster installation command

        :param request: Request instance for DescribeClusterInstallCommand.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterInstallCommandRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterInstallCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterInstallCommand", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterInstallCommandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterNamespaceList(self, request):
        r"""Query the cluster namespace list.

        :param request: Request instance for DescribeClusterNamespaceList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterNamespaceListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterNamespaceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterNamespaceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterNamespaceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterNodeList(self, request):
        r"""Query the cluster node list.

        :param request: Request instance for DescribeClusterNodeList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterNodeListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterNodeListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterNodeList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterNodeListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterPodAssets(self, request):
        r"""Cluster Pod List

        :param request: Request instance for DescribeClusterPodAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterPodAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterPodAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterPodAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterPodAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterPodDetail(self, request):
        r"""This API is used to query Pod details in A cluster. It is A new Type A API for the container asset revision and serves as the main entrance to the Pod Asset Details Page. The input parameter is only UniqueID. The output parameters cover asset information, cluster, namespace, node, Workload, as well as the number of risk events and alarm events grouped by four risk levels.

        :param request: Request instance for DescribeClusterPodDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterPodDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterPodDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterPodDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterPodDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterPodList(self, request):
        r"""Inquires the cluster pod list

        :param request: Request instance for DescribeClusterPodList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterPodListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterPodListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterPodList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterPodListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterServiceList(self, request):
        r"""Query the cluster service list.

        :param request: Request instance for DescribeClusterServiceList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterServiceListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterServiceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterServiceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterServiceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterSummary(self, request):
        r"""Query cluster overview data

        :param request: Request instance for DescribeClusterSummary.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterSummaryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterSuperNodeInfo(self, request):
        r"""This API is used to query super node details in a cluster and return basic info (region, availability zone, last asset update time, node origin, subnet, and core count) and cluster information (cluster name, Cluster ID, cluster status, Kubernetes version, and Kubelet version).

        :param request: Request instance for DescribeClusterSuperNodeInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterSuperNodeInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterSuperNodeInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterSuperNodeInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterSuperNodeInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeComplianceOverview(self, request):
        r"""Cloud resource configuration detection compliance overview

        :param request: Request instance for DescribeComplianceOverview.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeComplianceOverviewRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeComplianceOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComplianceOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComplianceOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeComplianceRiskList(self, request):
        r"""Cloud resource configuration risk list from the compliance standard aggregation perspective

        :param request: Request instance for DescribeComplianceRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeComplianceRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeComplianceRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComplianceRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComplianceRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeComplianceStandardTermTree(self, request):
        r"""Cloud resource configuration inspection standard chapter clause tree

        :param request: Request instance for DescribeComplianceStandardTermTree.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeComplianceStandardTermTreeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeComplianceStandardTermTreeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComplianceStandardTermTree", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComplianceStandardTermTreeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeComplianceStatistics(self, request):
        r"""Category statistics for cloud resource configuration detection specifications

        :param request: Request instance for DescribeComplianceStatistics.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeComplianceStatisticsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeComplianceStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComplianceStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComplianceStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigCheckRules(self, request):
        r"""Example of cloud resource configuration risk rule list

        :param request: Request instance for DescribeConfigCheckRules.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeConfigCheckRulesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeConfigCheckRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigCheckRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigCheckRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCspmShardConfig(self, request):
        r"""This API is used to query the CSPM auto quota shared configuration.

        :param request: Request instance for DescribeCspmShardConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCspmShardConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCspmShardConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCspmShardConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCspmShardConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomAssetTagCount(self, request):
        r"""number of user-customized tags

        :param request: Request instance for DescribeCustomAssetTagCount.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCustomAssetTagCountRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCustomAssetTagCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomAssetTagCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomAssetTagCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomRiskRuleDetail(self, request):
        r"""Example of a custom risk rule configuration detail list

        :param request: Request instance for DescribeCustomRiskRuleDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCustomRiskRuleDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCustomRiskRuleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomRiskRuleDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomRiskRuleDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomRiskRules(self, request):
        r"""Lists the configuration of custom risk rules

        :param request: Request instance for DescribeCustomRiskRules.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCustomRiskRulesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCustomRiskRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomRiskRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomRiskRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDbAssetInfo(self, request):
        r"""DB Asset Details

        :param request: Request instance for DescribeDbAssetInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDbAssetInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDbAssetInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDbAssetInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDbAssetInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDbAssets(self, request):
        r"""Database Asset List

        :param request: Request instance for DescribeDbAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDbAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDbAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDbAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDbAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDefaultSecurityScoreRule(self, request):
        r"""Retrieve the built-in default security scoring rules for resetting custom rules.

        :param request: Request instance for DescribeDefaultSecurityScoreRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDefaultSecurityScoreRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDefaultSecurityScoreRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDefaultSecurityScoreRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDefaultSecurityScoreRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainAssets(self, request):
        r"""Domain name list

        :param request: Request instance for DescribeDomainAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDomainAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDomainAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAccessRecord(self, request):
        r"""Query Dspm access records

        :param request: Request instance for DescribeDspmAccessRecord.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAccessRecordRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAccessRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAccessRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAccessRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAccessTopologyAccounts(self, request):
        r"""Queries the Dspm access topology account list

        :param request: Request instance for DescribeDspmAccessTopologyAccounts.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAccessTopologyAccountsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAccessTopologyAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAccessTopologyAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAccessTopologyAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAccessTopologyAssets(self, request):
        r"""Query the Dspm access topology asset list

        :param request: Request instance for DescribeDspmAccessTopologyAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAccessTopologyAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAccessTopologyAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAccessTopologyAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAccessTopologyAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAccessTopologyIps(self, request):
        r"""Query the Dspm access topology ip list

        :param request: Request instance for DescribeDspmAccessTopologyIps.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAccessTopologyIpsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAccessTopologyIpsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAccessTopologyIps", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAccessTopologyIpsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmApplyHistory(self, request):
        r"""Queries Dspm application history

        :param request: Request instance for DescribeDspmApplyHistory.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmApplyHistoryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmApplyHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmApplyHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmApplyHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmApplyOrderList(self, request):
        r"""Queries the Dspm application form list

        :param request: Request instance for DescribeDspmApplyOrderList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmApplyOrderListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmApplyOrderListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmApplyOrderList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmApplyOrderListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmApproveHistory(self, request):
        r"""Query Dspm approval history

        :param request: Request instance for DescribeDspmApproveHistory.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmApproveHistoryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmApproveHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmApproveHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmApproveHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmApproveOrderList(self, request):
        r"""Queries Dspm approval form list

        :param request: Request instance for DescribeDspmApproveOrderList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmApproveOrderListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmApproveOrderListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmApproveOrderList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmApproveOrderListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetAccessTopology(self, request):
        r"""Query the Dspm asset access topology

        :param request: Request instance for DescribeDspmAssetAccessTopology.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetAccessTopologyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetAccessTopologyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetAccessTopology", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetAccessTopologyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetAccountIdentify(self, request):
        r"""Query Dspm asset account identity information

        :param request: Request instance for DescribeDspmAssetAccountIdentify.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetAccountIdentifyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetAccountIdentifyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetAccountIdentify", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetAccountIdentifyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetAccountPresetPrivileges(self, request):
        r"""Querying preset privileged information of Dspm asset accounts

        :param request: Request instance for DescribeDspmAssetAccountPresetPrivileges.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetAccountPresetPrivilegesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetAccountPresetPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetAccountPresetPrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetAccountPresetPrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetAccountRecycledPrivileges(self, request):
        r"""Querying privileged information of Dspm asset accounts after recycling

        :param request: Request instance for DescribeDspmAssetAccountRecycledPrivileges.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetAccountRecycledPrivilegesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetAccountRecycledPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetAccountRecycledPrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetAccountRecycledPrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetAccounts(self, request):
        r"""Query the Dspm asset account list.

        :param request: Request instance for DescribeDspmAssetAccounts.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetAccountsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetDatabaseList(self, request):
        r"""This API is used to query asset database information.

        :param request: Request instance for DescribeDspmAssetDatabaseList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetDatabaseListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetDatabaseListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetDatabaseList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetDatabaseListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetDatabases(self, request):
        r"""This API is used to query the list of Dspm asset databases.

        :param request: Request instance for DescribeDspmAssetDatabases.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetDatabasesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetDatabasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetDatabases", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetDatabasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetFieldList(self, request):
        r"""Queries the dspm asset field information

        :param request: Request instance for DescribeDspmAssetFieldList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetFieldListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetFieldListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetFieldList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetFieldListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetFieldSamples(self, request):
        r"""Query sample values of dspm asset fields

        :param request: Request instance for DescribeDspmAssetFieldSamples.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetFieldSamplesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetFieldSamplesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetFieldSamples", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetFieldSamplesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetIdentifyInfoList(self, request):
        r"""Queries the dspm asset data recognition information list

        :param request: Request instance for DescribeDspmAssetIdentifyInfoList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetIdentifyInfoListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetIdentifyInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetIdentifyInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetIdentifyInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetIds(self, request):
        r"""Queries the list of Dspm asset IDs

        :param request: Request instance for DescribeDspmAssetIds.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetIdsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetIds", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetLoginCredential(self, request):
        r"""Query Dspm asset login credentials

        :param request: Request instance for DescribeDspmAssetLoginCredential.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetLoginCredentialRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetLoginCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetLoginCredential", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetLoginCredentialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetSecurityAnalyseStatus(self, request):
        r"""Query the security analysis status of Dspm assets.

        :param request: Request instance for DescribeDspmAssetSecurityAnalyseStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetSecurityAnalyseStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetSecurityAnalyseStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetSecurityAnalyseStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetSecurityAnalyseStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetSupportedPrivileges(self, request):
        r"""Queries supported permissions for Dspm assets

        :param request: Request instance for DescribeDspmAssetSupportedPrivileges.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetSupportedPrivilegesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetSupportedPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetSupportedPrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetSupportedPrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssetTableList(self, request):
        r"""This API is used to query asset table information.

        :param request: Request instance for DescribeDspmAssetTableList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetTableListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetTableListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssetTableList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetTableListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAssets(self, request):
        r"""Queries the Dspm asset list.

        :param request: Request instance for DescribeDspmAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmAuditFilterStrategy(self, request):
        r"""Query dspm audit filter policies

        :param request: Request instance for DescribeDspmAuditFilterStrategy.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAuditFilterStrategyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmAuditFilterStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmAuditFilterStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmAuditFilterStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmBackupLogList(self, request):
        r"""This API is used to query the backup log list.

        :param request: Request instance for DescribeDspmBackupLogList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmBackupLogListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmBackupLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmBackupLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmBackupLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmBackupSetting(self, request):
        r"""This API is used to query the log backup configuration.

        :param request: Request instance for DescribeDspmBackupSetting.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmBackupSettingRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmBackupSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmBackupSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmBackupSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmCkafkaRouteList(self, request):
        r"""This API is used to query the routing information of the CKafka instance.

        :param request: Request instance for DescribeDspmCkafkaRouteList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmCkafkaRouteListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmCkafkaRouteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmCkafkaRouteList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmCkafkaRouteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmCkafkaTopicList(self, request):
        r"""This API is used to query the topic list of the instance.

        :param request: Request instance for DescribeDspmCkafkaTopicList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmCkafkaTopicListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmCkafkaTopicListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmCkafkaTopicList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmCkafkaTopicListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmDictionaryList(self, request):
        r"""Query the list of dspm dictionary information

        :param request: Request instance for DescribeDspmDictionaryList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmDictionaryListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmDictionaryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmDictionaryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmDictionaryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmExportTask(self, request):
        r"""This API is used to query export tasks.

        :param request: Request instance for DescribeDspmExportTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmExportTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmExportTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmExportTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmExportTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmIdentifyCategoryList(self, request):
        r"""Querying the dspm data identification classification list

        :param request: Request instance for DescribeDspmIdentifyCategoryList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyCategoryListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyCategoryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmIdentifyCategoryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmIdentifyCategoryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmIdentifyComplianceCategoryRuleList(self, request):
        r"""This API is used to query the list of data items associated with dspm data recognition template classifications.

        :param request: Request instance for DescribeDspmIdentifyComplianceCategoryRuleList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyComplianceCategoryRuleListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyComplianceCategoryRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmIdentifyComplianceCategoryRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmIdentifyComplianceCategoryRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmIdentifyComplianceGroupDetail(self, request):
        r"""Query dspm identification template details

        :param request: Request instance for DescribeDspmIdentifyComplianceGroupDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyComplianceGroupDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyComplianceGroupDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmIdentifyComplianceGroupDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmIdentifyComplianceGroupDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmIdentifyComplianceGroupList(self, request):
        r"""Queries the dspm data identification template list

        :param request: Request instance for DescribeDspmIdentifyComplianceGroupList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyComplianceGroupListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyComplianceGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmIdentifyComplianceGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmIdentifyComplianceGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmIdentifyDistributionStatistics(self, request):
        r"""Querying dspm data identification distribution statistics

        :param request: Request instance for DescribeDspmIdentifyDistributionStatistics.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyDistributionStatisticsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyDistributionStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmIdentifyDistributionStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmIdentifyDistributionStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmIdentifyIdList(self, request):
        r"""Query the Dspm identity ID list.

        :param request: Request instance for DescribeDspmIdentifyIdList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyIdListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyIdListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmIdentifyIdList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmIdentifyIdListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmIdentifyInfo(self, request):
        r"""Queries the Dspm identity information.

        :param request: Request instance for DescribeDspmIdentifyInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmIdentifyInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmIdentifyInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmIdentifyInfoList(self, request):
        r"""Query the Dspm identity information list

        :param request: Request instance for DescribeDspmIdentifyInfoList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyInfoListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmIdentifyInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmIdentifyInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmIdentifyLevelGroupList(self, request):
        r"""Query the dspm data identification classification group list

        :param request: Request instance for DescribeDspmIdentifyLevelGroupList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyLevelGroupListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyLevelGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmIdentifyLevelGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmIdentifyLevelGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmIdentifyRuleDetail(self, request):
        r"""Queries the dspm data identification data item details

        :param request: Request instance for DescribeDspmIdentifyRuleDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyRuleDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyRuleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmIdentifyRuleDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmIdentifyRuleDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmIdentifyRuleList(self, request):
        r"""Query the list of dspm identification data items.

        :param request: Request instance for DescribeDspmIdentifyRuleList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyRuleListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmIdentifyRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmIdentifyRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmIdentifyRuleTestResult(self, request):
        r"""This API is used to query verification results of dspm data identification data items.

        :param request: Request instance for DescribeDspmIdentifyRuleTestResult.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyRuleTestResultRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmIdentifyRuleTestResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmIdentifyRuleTestResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmIdentifyRuleTestResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmLogDeliveryType(self, request):
        r"""This API is used to query the log type for log shipping.

        :param request: Request instance for DescribeDspmLogDeliveryType.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmLogDeliveryTypeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmLogDeliveryTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmLogDeliveryType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmLogDeliveryTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmLogList(self, request):
        r"""This API is used to query the log list information.

        :param request: Request instance for DescribeDspmLogList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmLogListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmLogTypeConfigList(self, request):
        r"""This API is used to query the log shipping configuration of a tenant.

        :param request: Request instance for DescribeDspmLogTypeConfigList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmLogTypeConfigListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmLogTypeConfigListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmLogTypeConfigList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmLogTypeConfigListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmPayInfo(self, request):
        r"""Get purchased Dspm order information

        :param request: Request instance for DescribeDspmPayInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmPayInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmPayInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmPayInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmPayInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmPersonApplyHistory(self, request):
        r"""Queries Dspm visitor application records.

        :param request: Request instance for DescribeDspmPersonApplyHistory.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmPersonApplyHistoryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmPersonApplyHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmPersonApplyHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmPersonApplyHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmPersonalIdentifyList(self, request):
        r"""Query the list of Dspm personal identification information.

        :param request: Request instance for DescribeDspmPersonalIdentifyList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmPersonalIdentifyListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmPersonalIdentifyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmPersonalIdentifyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmPersonalIdentifyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmResource(self, request):
        r"""Queries Dspm instances

        :param request: Request instance for DescribeDspmResource.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmResourceRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmResource", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmRisk(self, request):
        r"""Queries Dspm risk records

        :param request: Request instance for DescribeDspmRisk.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmRiskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmRiskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmRisk", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmRiskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmRiskDetail(self, request):
        r"""Queries Dspm risk details

        :param request: Request instance for DescribeDspmRiskDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmRiskDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmRiskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmRiskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmRiskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmRiskStrategy(self, request):
        r"""Queries Dspm risk policies

        :param request: Request instance for DescribeDspmRiskStrategy.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmRiskStrategyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmRiskStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmRiskStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmRiskStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmRiskStrategyGroup(self, request):
        r"""Query Dspm risk group policies

        :param request: Request instance for DescribeDspmRiskStrategyGroup.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmRiskStrategyGroupRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmRiskStrategyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmRiskStrategyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmRiskStrategyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmRiskTendency(self, request):
        r"""Query Dspm risk trends.

        :param request: Request instance for DescribeDspmRiskTendency.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmRiskTendencyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmRiskTendencyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmRiskTendency", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmRiskTendencyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmSessionList(self, request):
        r"""This API is used to query the audit session list information.

        :param request: Request instance for DescribeDspmSessionList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmSessionListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmSessionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmSessionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmSessionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmStatistics(self, request):
        r"""Query Dspm statistical information

        :param request: Request instance for DescribeDspmStatistics.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmStatisticsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmSupportedAssetType(self, request):
        r"""Queries information on asset types supported by Dspm.

        :param request: Request instance for DescribeDspmSupportedAssetType.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmSupportedAssetTypeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmSupportedAssetTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmSupportedAssetType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmSupportedAssetTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmSyncAssetsStatus(self, request):
        r"""Query the Dspm asset status synchronization.

        :param request: Request instance for DescribeDspmSyncAssetsStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmSyncAssetsStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmSyncAssetsStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmSyncAssetsStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmSyncAssetsStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmSyncUsersStatus(self, request):
        r"""Query the Dspm user synchronization status.

        :param request: Request instance for DescribeDspmSyncUsersStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmSyncUsersStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmSyncUsersStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmSyncUsersStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmSyncUsersStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmUserCkafkaInstanceList(self, request):
        r"""This API is used to query the tenant CKafka instance list.

        :param request: Request instance for DescribeDspmUserCkafkaInstanceList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmUserCkafkaInstanceListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmUserCkafkaInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmUserCkafkaInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmUserCkafkaInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDspmWhitelistStrategy(self, request):
        r"""Query the Dspm allowlist policy.

        :param request: Request instance for DescribeDspmWhitelistStrategy.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDspmWhitelistStrategyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDspmWhitelistStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDspmWhitelistStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDspmWhitelistStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDynamicAssets(self, request):
        r"""List of specified asset types

        :param request: Request instance for DescribeDynamicAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDynamicAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDynamicAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDynamicAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDynamicAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEDRRuleList(self, request):
        r"""This API is used to obtain the list of EDR policies.

        :param request: Request instance for DescribeEDRRuleList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEDRRuleListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEDRRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEDRRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEDRRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEDRScanRecordList(self, request):
        r"""This API is used to query the scan task list. Filter.Filters supports Name: Keyword (blurry, OperatorType=9), ScanType (MANUAL/CYCLE), TaskType (HOST/CONTAINER), Status (WAIT/SCANNING/FINISHED/FAILED/CANCELED), AppId (account).

        :param request: Request instance for DescribeEDRScanRecordList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEDRScanRecordListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEDRScanRecordListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEDRScanRecordList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEDRScanRecordListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEDRScanTaskDetail(self, request):
        r"""Query scan task details. Filter.Filters supports Name: Status (asset scan status, OperatorType=7 IN match, Value: WAIT/SCANNING/FINISHED/FAILED).

        :param request: Request instance for DescribeEDRScanTaskDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEDRScanTaskDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEDRScanTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEDRScanTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEDRScanTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdrAlertCountForAsset(self, request):
        r"""This API is used to obtain EDR alarm quantity statistics for the asset module. It queries the EDR alarm table based on the passed-in MemberId and InstanceIDs and returns the number of alarm records. If InstanceIDs is empty, summarized statistics are returned. Otherwise, statistics are returned by InstanceID granularity.

        :param request: Request instance for DescribeEdrAlertCountForAsset.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertCountForAssetRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertCountForAssetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdrAlertCountForAsset", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdrAlertCountForAssetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdrAlertCountForContainer(self, request):
        r"""Alarm quantity statistics in the container scenario.

        :param request: Request instance for DescribeEdrAlertCountForContainer.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertCountForContainerRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertCountForContainerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdrAlertCountForContainer", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdrAlertCountForContainerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdrAlertInfo(self, request):
        r"""This API is used to obtain EDR alert details, including complete information such as alert content JSON, asset enrichment, and intelligence enrichment.

        :param request: Request instance for DescribeEdrAlertInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdrAlertInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdrAlertInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdrAlertList(self, request):
        r"""Query the EDR alarm list.

        :param request: Request instance for DescribeEdrAlertList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdrAlertList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdrAlertListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdrAlertMultiAttackStages(self, request):
        r"""EDR alert multi-attack stage queries

        :param request: Request instance for DescribeEdrAlertMultiAttackStages.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertMultiAttackStagesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertMultiAttackStagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdrAlertMultiAttackStages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdrAlertMultiAttackStagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdrAlertSummary(self, request):
        r"""Retrieves EDR alarm statistics

        :param request: Request instance for DescribeEdrAlertSummary.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertSummaryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdrAlertSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdrAlertSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdrAlertThreatTags(self, request):
        r"""This API is used to query EDR alarm tags in batches.

        :param request: Request instance for DescribeEdrAlertThreatTags.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertThreatTagsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEdrAlertThreatTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdrAlertThreatTags", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdrAlertThreatTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdrExcludeNetworkSegments(self, request):
        r"""This API is used to query the exclusion network segment configurations for EDR log collection. TCP logs from network segments in the exclusion list will not be collected. If no user configuration exists, the system-recommended default network segments will be returned.

        :param request: Request instance for DescribeEdrExcludeNetworkSegments.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEdrExcludeNetworkSegmentsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEdrExcludeNetworkSegmentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdrExcludeNetworkSegments", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdrExcludeNetworkSegmentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdrExportJobDownloadURL(self, request):
        r"""Query the EDR export download link

        :param request: Request instance for DescribeEdrExportJobDownloadURL.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEdrExportJobDownloadURLRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEdrExportJobDownloadURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdrExportJobDownloadURL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdrExportJobDownloadURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdrExportJobList(self, request):
        r"""Export the EDR task list.

        :param request: Request instance for DescribeEdrExportJobList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEdrExportJobListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEdrExportJobListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdrExportJobList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdrExportJobListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdrLogCollectPaths(self, request):
        r"""This API is used to query the collection path configuration.

        :param request: Request instance for DescribeEdrLogCollectPaths.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeEdrLogCollectPathsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeEdrLogCollectPathsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdrLogCollectPaths", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdrLogCollectPathsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExportJobDownloadURL(self, request):
        r"""Result download URL of an export task

        :param request: Request instance for DescribeExportJobDownloadURL.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeExportJobDownloadURLRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeExportJobDownloadURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExportJobDownloadURL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExportJobDownloadURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExportJobManageList(self, request):
        r"""Exports the task list

        :param request: Request instance for DescribeExportJobManageList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeExportJobManageListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeExportJobManageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExportJobManageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExportJobManageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExposeAssetCategory(self, request):
        r"""Cloud boundary analysis asset category

        :param request: Request instance for DescribeExposeAssetCategory.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeExposeAssetCategoryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeExposeAssetCategoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExposeAssetCategory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExposeAssetCategoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExposePath(self, request):
        r"""Query the cloud boundary analysis path node

        :param request: Request instance for DescribeExposePath.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeExposePathRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeExposePathResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExposePath", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExposePathResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExposeRiskStatistics(self, request):
        r"""Pending risks to be governed for cloud boundaries

        :param request: Request instance for DescribeExposeRiskStatistics.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeExposeRiskStatisticsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeExposeRiskStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExposeRiskStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExposeRiskStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExposeRisks(self, request):
        r"""List of pending risks in cloud boundaries

        :param request: Request instance for DescribeExposeRisks.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeExposeRisksRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeExposeRisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExposeRisks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExposeRisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExposeRules(self, request):
        r"""List of boundary rules

        :param request: Request instance for DescribeExposeRules.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeExposeRulesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeExposeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExposeRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExposeRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExposureAutoTagAttribute(self, request):
        r"""Rule attributes for automatic tagging at cloud boundaries

        :param request: Request instance for DescribeExposureAutoTagAttribute.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeExposureAutoTagAttributeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeExposureAutoTagAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExposureAutoTagAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExposureAutoTagAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExposureAutoTagRules(self, request):
        r"""Automatic tagging of cloud boundaries - rule list

        :param request: Request instance for DescribeExposureAutoTagRules.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeExposureAutoTagRulesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeExposureAutoTagRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExposureAutoTagRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExposureAutoTagRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExposureTrend(self, request):
        r"""Query Internet exposure cycle count trend statistics.

        :param request: Request instance for DescribeExposureTrend.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeExposureTrendRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeExposureTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExposureTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExposureTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExposures(self, request):
        r"""Cloud boundary analysis asset list

        :param request: Request instance for DescribeExposures.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeExposuresRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeExposuresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExposures", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExposuresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGatewayAssets(self, request):
        r"""Obtain Gateway List

        :param request: Request instance for DescribeGatewayAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeGatewayAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeGatewayAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGatewayAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGatewayAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHighBaseLineRiskList(self, request):
        r"""Query the high-risk baseline risk list of host nodes under the cloud boundary analysis exposed path.

        :param request: Request instance for DescribeHighBaseLineRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeHighBaseLineRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeHighBaseLineRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHighBaseLineRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHighBaseLineRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostKBRiskList(self, request):
        r"""Search the host kb risk list.

        :param request: Request instance for DescribeHostKBRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeHostKBRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeHostKBRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostKBRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostKBRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostVulItemVPRInfo(self, request):
        r"""This API is used to obtain host vulnerability VPR information.

        :param request: Request instance for DescribeHostVulItemVPRInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeHostVulItemVPRInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeHostVulItemVPRInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostVulItemVPRInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostVulItemVPRInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostVulOverview(self, request):
        r"""This API is used to obtain the host vulnerability overview.

        :param request: Request instance for DescribeHostVulOverview.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeHostVulOverviewRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeHostVulOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostVulOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostVulOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostVulRiskList(self, request):
        r"""This API is used to retrieve the host vulnerability risk list.

        :param request: Request instance for DescribeHostVulRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeHostVulRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeHostVulRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostVulRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostVulRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIaCFileList(self, request):
        r"""Retrieve the IaC detection file list.

        :param request: Request instance for DescribeIaCFileList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeIaCFileListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeIaCFileListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIaCFileList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIaCFileListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIaCFileOverview(self, request):
        r"""Obtain the IaC detection file overview.

        :param request: Request instance for DescribeIaCFileOverview.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeIaCFileOverviewRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeIaCFileOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIaCFileOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIaCFileOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIaCFileReport(self, request):
        r"""Obtain the IaC detection file report.

        :param request: Request instance for DescribeIaCFileReport.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeIaCFileReportRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeIaCFileReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIaCFileReport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIaCFileReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIaCTokenList(self, request):
        r"""This API is used to search the IaC detection integration Token list.

        :param request: Request instance for DescribeIaCTokenList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeIaCTokenListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeIaCTokenListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIaCTokenList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIaCTokenListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageAssetDetail(self, request):
        r"""Queries image asset details.

        :param request: Request instance for DescribeImageAssetDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageAssetDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageAssetDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageAssetDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageAssetDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageAssetList(self, request):
        r"""Query the image asset list

        :param request: Request instance for DescribeImageAssetList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageAssetListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageAssetListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageAssetList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageAssetListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageAssociatedAssetCount(self, request):
        r"""Query the number of related assets of an image.

        :param request: Request instance for DescribeImageAssociatedAssetCount.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageAssociatedAssetCountRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageAssociatedAssetCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageAssociatedAssetCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageAssociatedAssetCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageAssociatedContainerList(self, request):
        r"""Queries the container assets associated with an image.

        :param request: Request instance for DescribeImageAssociatedContainerList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageAssociatedContainerListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageAssociatedContainerListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageAssociatedContainerList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageAssociatedContainerListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageAssociatedHostList(self, request):
        r"""Query the asset list of hosts associated with the image.

        :param request: Request instance for DescribeImageAssociatedHostList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageAssociatedHostListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageAssociatedHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageAssociatedHostList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageAssociatedHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageComponentList(self, request):
        r"""Queries the image component list.

        :param request: Request instance for DescribeImageComponentList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageComponentListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageComponentListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageComponentList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageComponentListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageExportJobList(self, request):
        r"""Queries the image repository export task list

        :param request: Request instance for DescribeImageExportJobList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageExportJobListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageExportJobListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageExportJobList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageExportJobListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageLayerList(self, request):
        r"""Query the image layer information list

        :param request: Request instance for DescribeImageLayerList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageLayerListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageLayerListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageLayerList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageLayerListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageLayerVulList(self, request):
        r"""Queries the list of vulnerabilities in an image layer

        :param request: Request instance for DescribeImageLayerVulList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageLayerVulListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageLayerVulListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageLayerVulList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageLayerVulListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageRegistryAssetOverview(self, request):
        r"""Query the repository asset overview of images

        :param request: Request instance for DescribeImageRegistryAssetOverview.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryAssetOverviewRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryAssetOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageRegistryAssetOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageRegistryAssetOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageRegistryConnectivityTaskResult(self, request):
        r"""Query the connectivity check task result of an image repository.

        :param request: Request instance for DescribeImageRegistryConnectivityTaskResult.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryConnectivityTaskResultRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryConnectivityTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageRegistryConnectivityTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageRegistryConnectivityTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageRegistryList(self, request):
        r"""This API is used to query the image repository list.

        :param request: Request instance for DescribeImageRegistryList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageRegistryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageRegistryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageRegistryNamespaceList(self, request):
        r"""This API is used to query the mirror repository namespace list.

        :param request: Request instance for DescribeImageRegistryNamespaceList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryNamespaceListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryNamespaceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageRegistryNamespaceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageRegistryNamespaceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageRegistryScanSubTaskList(self, request):
        r"""Query subtask information of image repository scanning

        :param request: Request instance for DescribeImageRegistryScanSubTaskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryScanSubTaskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryScanSubTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageRegistryScanSubTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageRegistryScanSubTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageRegistryScanTaskList(self, request):
        r"""Query the image repository scan task list

        :param request: Request instance for DescribeImageRegistryScanTaskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryScanTaskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryScanTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageRegistryScanTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageRegistryScanTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageRegistryTimedScanTaskConfig(self, request):
        r"""View the scheduled scan task configuration of a mirror repository

        :param request: Request instance for DescribeImageRegistryTimedScanTaskConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryTimedScanTaskConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryTimedScanTaskConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageRegistryTimedScanTaskConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageRegistryTimedScanTaskConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageRegistryTimedScanTaskPreview(self, request):
        r"""Query the preview of a scheduled scan task in the mirror repository

        :param request: Request instance for DescribeImageRegistryTimedScanTaskPreview.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryTimedScanTaskPreviewRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageRegistryTimedScanTaskPreviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageRegistryTimedScanTaskPreview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageRegistryTimedScanTaskPreviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageSensitiveInfoList(self, request):
        r"""Query the sensitive information list of an image

        :param request: Request instance for DescribeImageSensitiveInfoList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageSensitiveInfoListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageSensitiveInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageSensitiveInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageSensitiveInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageSensitiveWhitelist(self, request):
        r"""Query the sensitive information allowlist for container images

        :param request: Request instance for DescribeImageSensitiveWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageSensitiveWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageSensitiveWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageSensitiveWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageSensitiveWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageVirusList(self, request):
        r"""Queries the Trojan virus list of an image

        :param request: Request instance for DescribeImageVirusList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageVirusListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageVirusListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageVirusList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageVirusListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageVirusWhitelist(self, request):
        r"""This API is used to query the Trojan allowlist of an image.

        :param request: Request instance for DescribeImageVirusWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageVirusWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageVirusWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageVirusWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageVirusWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageVirusWhitelistDetail(self, request):
        r"""Queries the detailed information of the Trojan allowlist of an image.

        :param request: Request instance for DescribeImageVirusWhitelistDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageVirusWhitelistDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageVirusWhitelistDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageVirusWhitelistDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageVirusWhitelistDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageVulList(self, request):
        r"""This API is used to query the image vulnerability list.

        :param request: Request instance for DescribeImageVulList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageVulListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageVulListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageVulList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageVulListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageVulSummaryList(self, request):
        r"""Queries the image vulnerability overview list

        :param request: Request instance for DescribeImageVulSummaryList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageVulSummaryListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageVulSummaryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageVulSummaryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageVulSummaryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageVulWhitelist(self, request):
        r"""This API is used to query the vulnerability allowlist of a container image.

        :param request: Request instance for DescribeImageVulWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeImageVulWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeImageVulWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageVulWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageVulWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKBDetail(self, request):
        r"""Query the details of a single Windows KB patch based on the user's input KB internal ID, and return the basic KB info, release time, whether restart is required, as well as the list of vulnerabilities associated with the KB.

        :param request: Request instance for DescribeKBDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeKBDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeKBDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKBDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKBDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKBUpdatableMachineList(self, request):
        r"""Query the list of hosts that can update a specified KB patch. This API is used for Windows patch repair scenarios to query which hosts lack the patch and support auto-update before user-submitted KB patch update tasks.

        :param request: Request instance for DescribeKBUpdatableMachineList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeKBUpdatableMachineListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeKBUpdatableMachineListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKBUpdatableMachineList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKBUpdatableMachineListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKeySandboxCredential(self, request):
        r"""This API is used to query credential details and return credential metadata and masked credential data. The access type returns an Access array (original Key, masked Value), and the sts type returns an STS object (original System, masked SecretID and SecretKey).

        :param request: Request instance for DescribeKeySandboxCredential.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeKeySandboxCredentialRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeKeySandboxCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKeySandboxCredential", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKeySandboxCredentialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKeySandboxCredentialList(self, request):
        r"""Query the voucher list.

        :param request: Request instance for DescribeKeySandboxCredentialList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeKeySandboxCredentialListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeKeySandboxCredentialListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKeySandboxCredentialList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKeySandboxCredentialListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLastScanTaskInfo(self, request):
        r"""Get last check-now task info

        :param request: Request instance for DescribeLastScanTaskInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeLastScanTaskInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeLastScanTaskInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLastScanTaskInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLastScanTaskInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLicenseStatus(self, request):
        r"""Queries the overall status of all valid authorizations under the current account, returns total count, used, remaining, and expiry time grouped by billing item, and also returns the auto-purchase switch status and merged remaining unbind count. The output sequence is fixed as: flagship edition → pro edition → RASP → other.

        :param request: Request instance for DescribeLicenseStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeLicenseStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeLicenseStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLicenseStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLicenseStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLighthouseFirewallRules(self, request):
        r"""Query the firewall rules of a lightweight application server

        :param request: Request instance for DescribeLighthouseFirewallRules.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeLighthouseFirewallRulesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeLighthouseFirewallRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLighthouseFirewallRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLighthouseFirewallRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListenerList(self, request):
        r"""Query CLB Listener List

        :param request: Request instance for DescribeListenerList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeListenerListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeListenerListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListenerList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListenerListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoginTypeGlobalConf(self, request):
        r"""This API is used to obtain the global configuration for anti-uninstallation.

        :param request: Request instance for DescribeLoginTypeGlobalConf.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeLoginTypeGlobalConfRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeLoginTypeGlobalConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoginTypeGlobalConf", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoginTypeGlobalConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoginTypeHost(self, request):
        r"""Get the host list for QR code log-in

        :param request: Request instance for DescribeLoginTypeHost.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeLoginTypeHostRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeLoginTypeHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoginTypeHost", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoginTypeHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoginWhiteCombinedList(self, request):
        r"""This API is used to obtain the list of cross-region log-in allowlists after merge.

        :param request: Request instance for DescribeLoginWhiteCombinedList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeLoginWhiteCombinedListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeLoginWhiteCombinedListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoginWhiteCombinedList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoginWhiteCombinedListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoginWhiteHostList(self, request):
        r"""This API is used to query the list of allowlisted machines after merge.

        :param request: Request instance for DescribeLoginWhiteHostList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeLoginWhiteHostListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeLoginWhiteHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoginWhiteHostList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoginWhiteHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineClearHistory(self, request):
        r"""This API is used to query the clearing history records of a machine.

        :param request: Request instance for DescribeMachineClearHistory.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeMachineClearHistoryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeMachineClearHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineClearHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineClearHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineGeneral(self, request):
        r"""This API is used to query the information of the host overview.

        :param request: Request instance for DescribeMachineGeneral.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeMachineGeneralRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeMachineGeneralResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineGeneral", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineGeneralResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineLoginType(self, request):
        r"""This API is used to obtain the host login method.

        :param request: Request instance for DescribeMachineLoginType.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeMachineLoginTypeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeMachineLoginTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineLoginType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineLoginTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMalwareTimingScanSetting(self, request):
        r"""This API is used to query the scheduled scan configuration for file scan and removal.

        :param request: Request instance for DescribeMalwareTimingScanSetting.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeMalwareTimingScanSettingRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeMalwareTimingScanSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMalwareTimingScanSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMalwareTimingScanSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMandatoryVulSet(self, request):
        r"""Show mandatory vulnerability intelligence for businesses.

        :param request: Request instance for DescribeMandatoryVulSet.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeMandatoryVulSetRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeMandatoryVulSetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMandatoryVulSet", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMandatoryVulSetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModifyMachinesLoginTypeTasks(self, request):
        r"""This API is used to obtain a list of batch tasks for modification of host login methods.

        :param request: Request instance for DescribeModifyMachinesLoginTypeTasks.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeModifyMachinesLoginTypeTasksRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeModifyMachinesLoginTypeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModifyMachinesLoginTypeTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModifyMachinesLoginTypeTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMultiCloudAssetCount(self, request):
        r"""Retrieve the total number of assets integrated across multiple clouds (Tencent Cloud, Alibaba Cloud, AWS, Huawei Cloud, Azure, etc.) and the details of asset counts for each cloud service provider.

        :param request: Request instance for DescribeMultiCloudAssetCount.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeMultiCloudAssetCountRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeMultiCloudAssetCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMultiCloudAssetCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMultiCloudAssetCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNFSScanConf(self, request):
        r"""This API is used to obtain the global configuration for NFS scanning.

        :param request: Request instance for DescribeNFSScanConf.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeNFSScanConfRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeNFSScanConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNFSScanConf", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNFSScanConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNFSScanHost(self, request):
        r"""This API is used to query the host list for QR code log-in.

        :param request: Request instance for DescribeNFSScanHost.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeNFSScanHostRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeNFSScanHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNFSScanHost", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNFSScanHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNICAssets(self, request):
        r"""Obtain Network Interface Card List

        :param request: Request instance for DescribeNICAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeNICAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeNICAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNICAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNICAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNatRules(self, request):
        r"""Query the nat policy corresponding to a Tencent Cloud nat gateway instance

        :param request: Request instance for DescribeNatRules.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeNatRulesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeNatRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetAttackSetting(self, request):
        r"""Query the cyber attack detection switch and asset scope configuration

        :param request: Request instance for DescribeNetAttackSetting.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeNetAttackSettingRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeNetAttackSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetAttackSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetAttackSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNotifyAgentOfflineDuration(self, request):
        r"""Query client offline duration

        :param request: Request instance for DescribeNotifyAgentOfflineDuration.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeNotifyAgentOfflineDurationRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeNotifyAgentOfflineDurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNotifyAgentOfflineDuration", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNotifyAgentOfflineDurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNotifyAssetConfig(self, request):
        r"""Get the notification asset scope configuration.

        :param request: Request instance for DescribeNotifyAssetConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeNotifyAssetConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeNotifyAssetConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNotifyAssetConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNotifyAssetConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNotifySetting(self, request):
        r"""Get notification settings

        :param request: Request instance for DescribeNotifySetting.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeNotifySettingRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeNotifySettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNotifySetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNotifySettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNotifySettingAk(self, request):
        r"""Gets notification settings for risk governance.

        :param request: Request instance for DescribeNotifySettingAk.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeNotifySettingAkRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeNotifySettingAkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNotifySettingAk", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNotifySettingAkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNotifySettingAlert(self, request):
        r"""This API is used to obtain advanced configurations for alarm center notifications.

        :param request: Request instance for DescribeNotifySettingAlert.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeNotifySettingAlertRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeNotifySettingAlertResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNotifySettingAlert", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNotifySettingAlertResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationInfo(self, request):
        r"""Query Group Account Details

        :param request: Request instance for DescribeOrganizationInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeOrganizationInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeOrganizationInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationUserInfo(self, request):
        r"""Query Group Account User List

        :param request: Request instance for DescribeOrganizationUserInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeOrganizationUserInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeOrganizationUserInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationUserInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationUserInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOtherCloudAssets(self, request):
        r"""Asset list

        :param request: Request instance for DescribeOtherCloudAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeOtherCloudAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeOtherCloudAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOtherCloudAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOtherCloudAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePodContainerList(self, request):
        r"""Query the container list associated with a Pod

        :param request: Request instance for DescribePodContainerList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribePodContainerListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribePodContainerListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePodContainerList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePodContainerListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePortDetectList(self, request):
        r"""Port detection list

        :param request: Request instance for DescribePortDetectList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribePortDetectListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribePortDetectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePortDetectList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePortDetectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePortScanTaskCount(self, request):
        r"""Query the number of port scanning tasks under the current account.

        :param request: Request instance for DescribePortScanTaskCount.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribePortScanTaskCountRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribePortScanTaskCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePortScanTaskCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePortScanTaskCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePreventUninstallGlobalConf(self, request):
        r"""This API is used to obtain the global configuration for anti-uninstallation.

        :param request: Request instance for DescribePreventUninstallGlobalConf.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribePreventUninstallGlobalConfRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribePreventUninstallGlobalConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePreventUninstallGlobalConf", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePreventUninstallGlobalConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePreventUninstallHost(self, request):
        r"""Retrieve the host list for uninstallation prevention.

        :param request: Request instance for DescribePreventUninstallHost.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribePreventUninstallHostRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribePreventUninstallHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePreventUninstallHost", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePreventUninstallHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProcessDaemonGlobalConf(self, request):
        r"""Obtain the global configuration for process protection.

        :param request: Request instance for DescribeProcessDaemonGlobalConf.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeProcessDaemonGlobalConfRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeProcessDaemonGlobalConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProcessDaemonGlobalConf", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProcessDaemonGlobalConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProcessDaemonHost(self, request):
        r"""Get the process daemon host list.

        :param request: Request instance for DescribeProcessDaemonHost.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeProcessDaemonHostRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeProcessDaemonHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProcessDaemonHost", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProcessDaemonHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePublicCloudAssets(self, request):
        r"""Public network asset

        :param request: Request instance for DescribePublicCloudAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribePublicCloudAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribePublicCloudAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublicCloudAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublicCloudAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePublicIpAssets(self, request):
        r"""IP Public Network List

        :param request: Request instance for DescribePublicIpAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribePublicIpAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribePublicIpAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublicIpAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublicIpAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRaspLicenseList(self, request):
        r"""This API is used to query the authorization list for application protection.

        :param request: Request instance for DescribeRaspLicenseList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRaspLicenseListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRaspLicenseListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRaspLicenseList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRaspLicenseListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegistryOverview(self, request):
        r"""Query repository overview

        :param request: Request instance for DescribeRegistryOverview.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRegistryOverviewRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRegistryOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegistryOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegistryOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegistryRegionList(self, request):
        r"""Queries the region list of an image repository.

        :param request: Request instance for DescribeRegistryRegionList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRegistryRegionListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRegistryRegionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegistryRegionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegistryRegionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRepositoryImageAssets(self, request):
        r"""Repository Image List

        :param request: Request instance for DescribeRepositoryImageAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRepositoryImageAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRepositoryImageAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRepositoryImageAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRepositoryImageAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReverseShellSystemPolicyConfig(self, request):
        r"""This API is used to query the intranet alert and asset scope configuration for rebound Shell.

        :param request: Request instance for DescribeReverseShellSystemPolicyConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeReverseShellSystemPolicyConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeReverseShellSystemPolicyConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReverseShellSystemPolicyConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReverseShellSystemPolicyConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCallRecord(self, request):
        r"""This API is used to obtain the risk call record list.

        :param request: Request instance for DescribeRiskCallRecord.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCallRecordRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCallRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCallRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCallRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCenterAssetViewCFGRiskList(self, request):
        r"""Obtain Configuration Risk List from Asset's Perspective

        :param request: Request instance for DescribeRiskCenterAssetViewCFGRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterAssetViewCFGRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterAssetViewCFGRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCenterAssetViewCFGRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCenterAssetViewCFGRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCenterAssetViewPortRiskList(self, request):
        r"""Obtain Port Risk List from Asset's Perspective

        :param request: Request instance for DescribeRiskCenterAssetViewPortRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterAssetViewPortRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterAssetViewPortRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCenterAssetViewPortRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCenterAssetViewPortRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCenterAssetViewVULRiskList(self, request):
        r"""Obtain Vulnerability Risk List from Asset's Perspective

        :param request: Request instance for DescribeRiskCenterAssetViewVULRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterAssetViewVULRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterAssetViewVULRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCenterAssetViewVULRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCenterAssetViewVULRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCenterAssetViewWeakPasswordRiskList(self, request):
        r"""Obtain Weak Password Risk List from Asset's Perspective

        :param request: Request instance for DescribeRiskCenterAssetViewWeakPasswordRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterAssetViewWeakPasswordRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterAssetViewWeakPasswordRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCenterAssetViewWeakPasswordRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCenterAssetViewWeakPasswordRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCenterCFGViewCFGRiskList(self, request):
        r"""Obtain Configuration Risk List from Configuration's Perspective

        :param request: Request instance for DescribeRiskCenterCFGViewCFGRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterCFGViewCFGRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterCFGViewCFGRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCenterCFGViewCFGRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCenterCFGViewCFGRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCenterPortViewPortRiskList(self, request):
        r"""Obtain Port Risk List from Port's Perspective

        :param request: Request instance for DescribeRiskCenterPortViewPortRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterPortViewPortRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterPortViewPortRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCenterPortViewPortRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCenterPortViewPortRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCenterRiskTrendAnalysis(self, request):
        r"""Sample code for obtaining risk trend analysis

        :param request: Request instance for DescribeRiskCenterRiskTrendAnalysis.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterRiskTrendAnalysisRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterRiskTrendAnalysisResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCenterRiskTrendAnalysis", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCenterRiskTrendAnalysisResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCenterServerRiskList(self, request):
        r"""Obtain Risk Service List

        :param request: Request instance for DescribeRiskCenterServerRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterServerRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterServerRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCenterServerRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCenterServerRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCenterVULViewVULRiskList(self, request):
        r"""Obtain Vulnerability Risk List from Vulnerability's Perspective

        :param request: Request instance for DescribeRiskCenterVULViewVULRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterVULViewVULRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterVULViewVULRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCenterVULViewVULRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCenterVULViewVULRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCenterWebsiteRiskList(self, request):
        r"""Obtain Content Risk List

        :param request: Request instance for DescribeRiskCenterWebsiteRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterWebsiteRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterWebsiteRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCenterWebsiteRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCenterWebsiteRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskDetailList(self, request):
        r"""Sample risk detail list

        :param request: Request instance for DescribeRiskDetailList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskDetailListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskDetailListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskDetailList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskDetailListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskRuleDetail(self, request):
        r"""Sample code for querying risk rule details

        :param request: Request instance for DescribeRiskRuleDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskRuleDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskRuleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskRuleDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskRuleDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskRules(self, request):
        r"""Illustrative example of the advanced configuration risk rule list

        :param request: Request instance for DescribeRiskRules.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskRulesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskScanCronConfig(self, request):
        r"""Get the periodic schedule for risk scans

        :param request: Request instance for DescribeRiskScanCronConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskScanCronConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskScanCronConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskScanCronConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskScanCronConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSCFAliasList(self, request):
        r"""Queries the alias list of a specified SCF function.

        :param request: Request instance for DescribeSCFAliasList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSCFAliasListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSCFAliasListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSCFAliasList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSCFAliasListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSCFFunctionList(self, request):
        r"""Query the list of SCF functions in the specified namespace. Only functions of the Event trigger type are returned.

        :param request: Request instance for DescribeSCFFunctionList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSCFFunctionListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSCFFunctionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSCFFunctionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSCFFunctionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSCFFunctionVersionList(self, request):
        r"""Queries the version list of a specified SCF function.

        :param request: Request instance for DescribeSCFFunctionVersionList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSCFFunctionVersionListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSCFFunctionVersionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSCFFunctionVersionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSCFFunctionVersionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSCFNamespaceList(self, request):
        r"""Queries the namespace list of SCF in the designated region for the current user.

        :param request: Request instance for DescribeSCFNamespaceList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSCFNamespaceListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSCFNamespaceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSCFNamespaceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSCFNamespaceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSandboxACLAlertList(self, request):
        r"""This API is used to query the ACL access control alarm log list by paging. It supports precise filtering of a single alarm by Filter.Name=ID for the details page scenario.

        :param request: Request instance for DescribeSandboxACLAlertList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxACLAlertListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxACLAlertListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSandboxACLAlertList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSandboxACLAlertListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSandboxACLRuleList(self, request):
        r"""This API is used to query the access control rule list for ACL users under the current tenant. Import Filter.Name=RuleID to query an individual rule precisely.

        :param request: Request instance for DescribeSandboxACLRuleList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxACLRuleListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxACLRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSandboxACLRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSandboxACLRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSandboxACLSystemRuleList(self, request):
        r"""Queries the traffic sandbox access control (ACL) system rule list. System rules are built into the CSIP platform and can be referenced by user rules.

        :param request: Request instance for DescribeSandboxACLSystemRuleList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxACLSystemRuleListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxACLSystemRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSandboxACLSystemRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSandboxACLSystemRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSandboxDLPAlertList(self, request):
        r"""Paging query for the DLP data leakage alert log list. Supports precise filtering of a single alert by Filter.Name=ID for the details page scenario.

        :param request: Request instance for DescribeSandboxDLPAlertList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxDLPAlertListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxDLPAlertListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSandboxDLPAlertList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSandboxDLPAlertListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSandboxDLPRuleList(self, request):
        r"""Query the DLP user rule list of the current tenant. Input Filter.Name=RuleID to query an individual rule for the details page scenario.

        :param request: Request instance for DescribeSandboxDLPRuleList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxDLPRuleListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxDLPRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSandboxDLPRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSandboxDLPRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSandboxDLPSystemRuleList(self, request):
        r"""Queries the traffic sandbox data leakage protection (DLP) system rule list. System rules are built into the CSIP platform and can be referenced by user rules.

        :param request: Request instance for DescribeSandboxDLPSystemRuleList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxDLPSystemRuleListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxDLPSystemRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSandboxDLPSystemRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSandboxDLPSystemRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSandboxFileRuleList(self, request):
        r"""Query the command sandbox file rule list.

        :param request: Request instance for DescribeSandboxFileRuleList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxFileRuleListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxFileRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSandboxFileRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSandboxFileRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSandboxLLMAuditAlertList(self, request):
        r"""Paging query for the LLM audit alarm log list. Supports precise filtering of a single alarm by Filter.Name=ID for the details page scenario.

        :param request: Request instance for DescribeSandboxLLMAuditAlertList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxLLMAuditAlertListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxLLMAuditAlertListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSandboxLLMAuditAlertList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSandboxLLMAuditAlertListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSandboxLLMAuditRuleList(self, request):
        r"""Queries the LLM audit user rule list for the current tenant. LLM audit rules do not support user-defined content and can only refer to system rule composites. Import Filter.Name=RuleID for exact querying of an individual rule (for details page scenarios).

        :param request: Request instance for DescribeSandboxLLMAuditRuleList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxLLMAuditRuleListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxLLMAuditRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSandboxLLMAuditRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSandboxLLMAuditRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSandboxLLMAuditSystemRuleList(self, request):
        r"""This API is used to query the rule list of the LLM audit system. System rules are built into the CSIP platform and originate from the LLM audit system rule base. They are split into two flat rule arrays by LLM reasoning protection and ToolCall protection and can be referenced by user rules.

        :param request: Request instance for DescribeSandboxLLMAuditSystemRuleList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxLLMAuditSystemRuleListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSandboxLLMAuditSystemRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSandboxLLMAuditSystemRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSandboxLLMAuditSystemRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanReportList(self, request):
        r"""Obtain Scan Report List

        :param request: Request instance for DescribeScanReportList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeScanReportListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeScanReportListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanReportList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanReportListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanStatistic(self, request):
        r"""This API is used to query result statistics of cloud boundary analysis scans.

        :param request: Request instance for DescribeScanStatistic.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeScanStatisticRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeScanStatisticResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanStatistic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanStatisticResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanTaskList(self, request):
        r"""Obtain Scan Task List

        :param request: Request instance for DescribeScanTaskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeScanTaskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeScanTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanTaskRecordList(self, request):
        r"""This API is used to query the scan task record list.

        :param request: Request instance for DescribeScanTaskRecordList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeScanTaskRecordListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeScanTaskRecordListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanTaskRecordList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanTaskRecordListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScfCustomDomainEndpoints(self, request):
        r"""Query the list of custom domain name endpoints for Tencent Cloud SCF

        :param request: Request instance for DescribeScfCustomDomainEndpoints.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeScfCustomDomainEndpointsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeScfCustomDomainEndpointsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScfCustomDomainEndpoints", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScfCustomDomainEndpointsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSearchBugInfo(self, request):
        r"""Query vulnerability information in the three-dimensional protection center.

        :param request: Request instance for DescribeSearchBugInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSearchBugInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSearchBugInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSearchBugInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSearchBugInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityGroupPolicy(self, request):
        r"""Query the security group rules correspond to the specified security group ID.

        :param request: Request instance for DescribeSecurityGroupPolicy.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSecurityGroupPolicyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSecurityGroupPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityGroupPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityGroupPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityRiskTrend(self, request):
        r"""This API is used to obtain security risk trends and return the daily number of risks grouped by dimension.

        :param request: Request instance for DescribeSecurityRiskTrend.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSecurityRiskTrendRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSecurityRiskTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityRiskTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityRiskTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityScoreOverview(self, request):
        r"""This API is used to obtain the security score overview and real-time compute point deductions in each dimension and sub-item.

        :param request: Request instance for DescribeSecurityScoreOverview.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSecurityScoreOverviewRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSecurityScoreOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityScoreOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityScoreOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityScoreRule(self, request):
        r"""Retrieve the security scoring rules for the current account. If no custom rules exist, return the built-in default.

        :param request: Request instance for DescribeSecurityScoreRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSecurityScoreRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSecurityScoreRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityScoreRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityScoreRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSkillScanAlertDetail(self, request):
        r"""This API is used to query Skill security detection alarm details, including local alarm information and engine real-time detection data.

        :param request: Request instance for DescribeSkillScanAlertDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSkillScanAlertDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSkillScanAlertDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSkillScanAlertDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSkillScanAlertDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSkillScanAlertList(self, request):
        r"""Queries the Skill security detection alarm list with pagination, filtering, and sorting supported.

        :param request: Request instance for DescribeSkillScanAlertList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSkillScanAlertListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSkillScanAlertListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSkillScanAlertList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSkillScanAlertListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSkillScanPayInfo(self, request):
        r"""This API is used to query Skill security detection billing information, including order status, total quota, consumed quota, expiration time, and payment mode. If no order exists, zero values are returned (only TimeNow and BetaEndTime). Trial orders are claimed through ModifyTrialStatus(Module=9), and official orders are created through the billing system.

        :param request: Request instance for DescribeSkillScanPayInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSkillScanPayInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSkillScanPayInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSkillScanPayInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSkillScanPayInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSkillScanResult(self, request):
        r"""Queries the security detection result of a skill. After calling CreateSkillScan successfully, use the returned ContentHash + EngineVersion to poll this API to obtain the result. We recommend polling for the first time 5 minutes after a successful upload. If detection is not completed, poll once every 1 minute afterward. The response uses the Status field to distinguish four statuses: detection completed (SUCCESS), detecting (SCANNING), no record (NOT_FOUND), and detection failed (FAILED). Note: Detection results are retained for 90 days. NOT_FOUND will be returned after they expire.

        :param request: Request instance for DescribeSkillScanResult.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSkillScanResultRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSkillScanResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSkillScanResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSkillScanResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSourceIPAsset(self, request):
        r"""Retrieve the user access key asset list from an IP perspective.

        :param request: Request instance for DescribeSourceIPAsset.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSourceIPAssetRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSourceIPAssetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSourceIPAsset", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSourceIPAssetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSourceIPDetail(self, request):
        r"""This API is used to query user access key asset list from source IP perspective.

        :param request: Request instance for DescribeSourceIPDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSourceIPDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSourceIPDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSourceIPDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSourceIPDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubUserInfo(self, request):
        r"""Query the sub-account list of a group

        :param request: Request instance for DescribeSubUserInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSubUserInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSubUserInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubUserInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubUserInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubnetAssets(self, request):
        r"""Obtain Subnet List

        :param request: Request instance for DescribeSubnetAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSubnetAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSubnetAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubnetAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubnetAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTCRInstanceList(self, request):
        r"""This API is used to obtain the TCR instance list.

        :param request: Request instance for DescribeTCRInstanceList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeTCRInstanceListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeTCRInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTCRInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTCRInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTagRuleAssets(self, request):
        r"""Tagging policy enforcement asset list

        :param request: Request instance for DescribeTagRuleAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeTagRuleAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeTagRuleAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTagRuleAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagRuleAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskLogList(self, request):
        r"""Obtain Task Scan Report List

        :param request: Request instance for DescribeTaskLogList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeTaskLogListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeTaskLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskLogURL(self, request):
        r"""Obtain the Temporary Link for Report Download

        :param request: Request instance for DescribeTaskLogURL.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeTaskLogURLRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeTaskLogURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskLogURL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskLogURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskPredictCostQuota(self, request):
        r"""Obtain the pre-consumed quota for scans.

        :param request: Request instance for DescribeTaskPredictCostQuota.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeTaskPredictCostQuotaRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeTaskPredictCostQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskPredictCostQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskPredictCostQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopAttackInfo(self, request):
        r"""Query TOP attack information

        :param request: Request instance for DescribeTopAttackInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeTopAttackInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeTopAttackInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopAttackInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopAttackInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUebaBehaviorSummary(self, request):
        r"""Queries the behavior overview of user behavior analysis.

        :param request: Request instance for DescribeUebaBehaviorSummary.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeUebaBehaviorSummaryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeUebaBehaviorSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUebaBehaviorSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUebaBehaviorSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUebaRule(self, request):
        r"""Query the list of user behavior analysis policies

        :param request: Request instance for DescribeUebaRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeUebaRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeUebaRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUebaRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUebaRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUebaUserSummary(self, request):
        r"""This API is used to get the user overview of the user behavior analysis module.

        :param request: Request instance for DescribeUebaUserSummary.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeUebaUserSummaryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeUebaUserSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUebaUserSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUebaUserSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserAKInfoList(self, request):
        r"""Obtain AK information of the account

        :param request: Request instance for DescribeUserAKInfoList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeUserAKInfoListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeUserAKInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserAKInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserAKInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserCSPMInfoList(self, request):
        r"""This API is used to obtain CSPM information of an account.

        :param request: Request instance for DescribeUserCSPMInfoList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeUserCSPMInfoListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeUserCSPMInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserCSPMInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserCSPMInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserCallRecord(self, request):
        r"""This API is used to obtain the account call record list.

        :param request: Request instance for DescribeUserCallRecord.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeUserCallRecordRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeUserCallRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserCallRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserCallRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserDspmInfoList(self, request):
        r"""Get the dspm information list of an account

        :param request: Request instance for DescribeUserDspmInfoList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeUserDspmInfoListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeUserDspmInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserDspmInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserDspmInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserInfo(self, request):
        r"""CSPM quota information of a user

        :param request: Request instance for DescribeUserInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeUserInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeUserInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVULList(self, request):
        r"""Vulnerability list in the risk center of the new security center

        :param request: Request instance for DescribeVULList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVULListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVULListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVULList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVULListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVULRiskAdvanceCFGList(self, request):
        r"""Query Vulnerability Risk Advanced Configuration

        :param request: Request instance for DescribeVULRiskAdvanceCFGList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVULRiskAdvanceCFGListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVULRiskAdvanceCFGListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVULRiskAdvanceCFGList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVULRiskAdvanceCFGListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVULRiskDetail(self, request):
        r"""Retrieve vulnerability details

        :param request: Request instance for DescribeVULRiskDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVULRiskDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVULRiskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVULRiskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVULRiskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVdbAndPocInfo(self, request):
        r"""This API is used to obtain virus database and POC updates.

        :param request: Request instance for DescribeVdbAndPocInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVdbAndPocInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVdbAndPocInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVdbAndPocInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVdbAndPocInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVoucherEligibility(self, request):
        r"""Check whether the current user is eligible to claim vouchers for the designated promotion.

        :param request: Request instance for DescribeVoucherEligibility.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVoucherEligibilityRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVoucherEligibilityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVoucherEligibility", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVoucherEligibilityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcAssets(self, request):
        r"""Obtain VPC List

        :param request: Request instance for DescribeVpcAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVpcAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVpcAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulComponentRelateHost(self, request):
        r"""This API is used to query the associated server of a vulnerable component.

        :param request: Request instance for DescribeVulComponentRelateHost.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulComponentRelateHostRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulComponentRelateHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulComponentRelateHost", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulComponentRelateHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulFixTaskDetail(self, request):
        r"""This API is used to query the details of a specified vulnerability repair task, including detailed data such as remediation status and snapshot status for each host, and supports pagination and filtering.

        :param request: Request instance for DescribeVulFixTaskDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulFixTaskDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulFixTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulFixTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulFixTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulFixTaskList(self, request):
        r"""This API is used to query the vulnerability repair task record list with paging, support by conditional filtering such as remediation status and time range, and show summary information for each repair task.

        :param request: Request instance for DescribeVulFixTaskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulFixTaskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulFixTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulFixTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulFixTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulFixableMachineList(self, request):
        r"""This API is used to query the host list where specified vulnerabilities can be repaired. Before a user submits a repair task, it is necessary to query which hosts support automatic fix, providing data support for users to select repair targets.

        :param request: Request instance for DescribeVulFixableMachineList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulFixableMachineListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulFixableMachineListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulFixableMachineList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulFixableMachineListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulFixedHostDetail(self, request):
        r"""This API is used to query the repair details of a certain fixed vulnerability on a specified host, including basic information about the vulnerability, repair host information, and a detailed list of associated components and paths (component name, version number hit, associated path, repair command).

        :param request: Request instance for DescribeVulFixedHostDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulFixedHostDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulFixedHostDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulFixedHostDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulFixedHostDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulFixedList(self, request):
        r"""This API is used to query the list of repaired vulnerabilities, show vulnerability information with successful fixes and statistics on repair conditions, helping users understand the repair results.

        :param request: Request instance for DescribeVulFixedList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulFixedListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulFixedListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulFixedList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulFixedListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulHostRelateComponent(self, request):
        r"""This API is used to query host-associated vulnerability components.

        :param request: Request instance for DescribeVulHostRelateComponent.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulHostRelateComponentRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulHostRelateComponentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulHostRelateComponent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulHostRelateComponentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulIgnoreRuleList(self, request):
        r"""This API is used to retrieve the vulnerability ignore list.

        :param request: Request instance for DescribeVulIgnoreRuleList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulIgnoreRuleListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulIgnoreRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulIgnoreRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulIgnoreRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulItemList(self, request):
        r"""This API is used to obtain vulnerability list

        :param request: Request instance for DescribeVulItemList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulItemListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulItemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulItemList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulItemListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulLabelList(self, request):
        r"""Obtains the vulnerability tag list

        :param request: Request instance for DescribeVulLabelList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulLabelListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulLabelListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulLabelList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulLabelListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulRiskList(self, request):
        r"""Query the list of vulnerabilities on host nodes under the exposed path in cloud boundary analysis.

        :param request: Request instance for DescribeVulRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulRiskRelateComponent(self, request):
        r"""Retrieve the associated component of a vulnerability

        :param request: Request instance for DescribeVulRiskRelateComponent.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulRiskRelateComponentRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulRiskRelateComponentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulRiskRelateComponent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulRiskRelateComponentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulRiskRelateHost(self, request):
        r"""Search for hosts associated with vulnerabilities or KBs

        :param request: Request instance for DescribeVulRiskRelateHost.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulRiskRelateHostRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulRiskRelateHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulRiskRelateHost", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulRiskRelateHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulScanPeriodic(self, request):
        r"""This API is used to obtain vulnerability scanning (period scanning).

        :param request: Request instance for DescribeVulScanPeriodic.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulScanPeriodicRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulScanPeriodicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulScanPeriodic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulScanPeriodicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulScanTaskDetail(self, request):
        r"""This API is used to retrieve vulnerability scanning task detail

        :param request: Request instance for DescribeVulScanTaskDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulScanTaskDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulScanTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulScanTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulScanTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulScanTaskList(self, request):
        r"""This API is used to search vulnerability scanning task history

        :param request: Request instance for DescribeVulScanTaskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulScanTaskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulScanTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulScanTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulScanTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulViewVulRiskList(self, request):
        r"""Obtain Vulnerability Risk List from Vulnerability's Perspective

        :param request: Request instance for DescribeVulViewVulRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVulViewVulRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVulViewVulRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulViewVulRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulViewVulRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebhookPolicyList(self, request):
        r"""This API is used to query the notification policy list for the current tenant by page, corresponding to the table on the Notification Policy Configuration Tab in Notification Center - Robot Notification. The returned fields are simplified info required for row display. Use DescribeWebhookPolicy for complete configuration in editing scenarios. Each tenant can have up to 100 notification policies.

        :param request: Request instance for DescribeWebhookPolicyList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeWebhookPolicyListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeWebhookPolicyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebhookPolicyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebhookPolicyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebhookReceiverList(self, request):
        r"""This API is used to query the list of receiving robots for the current tenant by page, corresponding to the table on the Receive Bot Management Tab in Notification Center - Robot Notification. Each tenant can have up to 50 robots.

        :param request: Request instance for DescribeWebhookReceiverList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeWebhookReceiverListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeWebhookReceiverListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebhookReceiverList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebhookReceiverListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableAISchedule(self, request):
        r"""Disable scheduled AI tasks.

        Set the status of the specified AI scheduled task to disabled. After it is disabled, the task will suspend automatic execution.

        :param request: Request instance for DisableAISchedule.
        :type request: :class:`tencentcloud.csip.v20221121.models.DisableAIScheduleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DisableAIScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableAISchedule", params, headers=headers)
            response = json.loads(body)
            model = models.DisableAIScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DownloadDspmExportLog(self, request):
        r"""This API is used to download export logs.

        :param request: Request instance for DownloadDspmExportLog.
        :type request: :class:`tencentcloud.csip.v20221121.models.DownloadDspmExportLogRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DownloadDspmExportLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadDspmExportLog", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadDspmExportLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableAISchedule(self, request):
        r"""Enable AI scheduled tasks.

        Set the status of the specified AI scheduled task to enabled. After it is enabled, the task will automatically execute based on the trigger configuration.

        :param request: Request instance for EnableAISchedule.
        :type request: :class:`tencentcloud.csip.v20221121.models.EnableAIScheduleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.EnableAIScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableAISchedule", params, headers=headers)
            response = json.loads(body)
            model = models.EnableAIScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportCSIPMalwareScanTaskDetail(self, request):
        r"""Exports host details of a CSIP scan task to Excel files. This API is used to query the download link through DescribeExportMachines after asynchronous generation.

        :param request: Request instance for ExportCSIPMalwareScanTaskDetail.
        :type request: :class:`tencentcloud.csip.v20221121.models.ExportCSIPMalwareScanTaskDetailRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ExportCSIPMalwareScanTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportCSIPMalwareScanTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.ExportCSIPMalwareScanTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportClientSettingHostList(self, request):
        r"""Export the host list for client settings.

        :param request: Request instance for ExportClientSettingHostList.
        :type request: :class:`tencentcloud.csip.v20221121.models.ExportClientSettingHostListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ExportClientSettingHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportClientSettingHostList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportClientSettingHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportEDRRules(self, request):
        r"""This API is used to export the EDR policy list.

        :param request: Request instance for ExportEDRRules.
        :type request: :class:`tencentcloud.csip.v20221121.models.ExportEDRRulesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ExportEDRRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportEDRRules", params, headers=headers)
            response = json.loads(body)
            model = models.ExportEDRRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportTasks(self, request):
        r"""This API is used to export log files with large data volumes asynchronously.

        :param request: Request instance for ExportTasks.
        :type request: :class:`tencentcloud.csip.v20221121.models.ExportTasksRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ExportTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ExportTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InstallClusterAgent(self, request):
        r"""Install Agent for cluster container security (parallel container installation method).

        capi layer processing process:
        1. Query the DB cluster list by ClusterCaMD5List (only used for resolving the appid ownership of each cluster, not for existence/type verification)
        2. Group by appid and pass through to the access side ClusterInstall RPC

        Description (container asset revision 2026 H1): This API is a passthrough API. The capi layer does not verify the existence, data type, or format of ClusterCaMD5. ClusterCaMD5 values that miss in the DB are silently skipped with no error reported.

        :param request: Request instance for InstallClusterAgent.
        :type request: :class:`tencentcloud.csip.v20221121.models.InstallClusterAgentRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.InstallClusterAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InstallClusterAgent", params, headers=headers)
            response = json.loads(body)
            model = models.InstallClusterAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InstallKeySandboxSkill(self, request):
        r"""Install the key sandbox SKILL on specified machine instances. Batch operations are supported, allowing input of multiple instance IDs at once. After installation, the AI Agent on the target machine can access credentials through the key sandbox proxy without being exposed to plaintext keys. Duplicate invocations on installed instances will not trigger an error (idempotent) and are deemed successful.

        :param request: Request instance for InstallKeySandboxSkill.
        :type request: :class:`tencentcloud.csip.v20221121.models.InstallKeySandboxSkillRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.InstallKeySandboxSkillResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InstallKeySandboxSkill", params, headers=headers)
            response = json.loads(body)
            model = models.InstallKeySandboxSkillResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InstallSandboxPlugin(self, request):
        r"""Trigger installation of the traffic sandbox plugin to AI Agent assets in a specified range. Use BelongAssetType to distinguish host or container dimensions, and use EffectScope to specify the installation target (INCLUDE = install only to specified assets, EXCLUDE = all assets minus specified assets). This API only triggers the action and does not wait for completion.

        :param request: Request instance for InstallSandboxPlugin.
        :type request: :class:`tencentcloud.csip.v20221121.models.InstallSandboxPluginRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.InstallSandboxPluginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InstallSandboxPlugin", params, headers=headers)
            response = json.loads(body)
            model = models.InstallSandboxPluginResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAILinkSetting(self, request):
        r"""Modify the AI-Link engine configuration.

        :param request: Request instance for ModifyAILinkSetting.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyAILinkSettingRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyAILinkSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAILinkSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAILinkSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAISchedule(self, request):
        r"""Modify a scheduled AI task.

        Partial update is supported. Only the passed-in optional fields are updated. Whether the trigger list is fully replaced is controlled by the UpdateTriggers flag.

        :param request: Request instance for ModifyAISchedule.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyAIScheduleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyAIScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAISchedule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAIScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAgentConfigSetting(self, request):
        r"""This API is used to modify client log collection settings exclusive to CSIP. It allows you to set the log collection type and asset scope for which the settings take effect.

        :param request: Request instance for ModifyAgentConfigSetting.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyAgentConfigSettingRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyAgentConfigSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAgentConfigSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAgentConfigSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAgentRunMode(self, request):
        r"""Set the client running mode and configuration

        :param request: Request instance for ModifyAgentRunMode.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyAgentRunModeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyAgentRunModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAgentRunMode", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAgentRunModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAgentRunPolicy(self, request):
        r"""Modify the client running policy group. This API is used to set custom policies and associate machine lists.

        :param request: Request instance for ModifyAgentRunPolicy.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyAgentRunPolicyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyAgentRunPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAgentRunPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAgentRunPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAssetCoreAttribute(self, request):
        r"""Tag an asset as core or not.

        :param request: Request instance for ModifyAssetCoreAttribute.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyAssetCoreAttributeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyAssetCoreAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAssetCoreAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAssetCoreAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAssetFilterView(self, request):
        r"""Update the asset search view.

        :param request: Request instance for ModifyAssetFilterView.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyAssetFilterViewRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyAssetFilterViewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAssetFilterView", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAssetFilterViewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAssetTag(self, request):
        r"""This API is used to edit asset tags.

        :param request: Request instance for ModifyAssetTag.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyAssetTagRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyAssetTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAssetTag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAssetTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAssetTags(self, request):
        r"""Operate assets to edit tags.

        :param request: Request instance for ModifyAssetTags.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyAssetTagsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyAssetTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAssetTags", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAssetTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAssetTagsByAssetInfo(self, request):
        r"""Operate assets and edit tags.

        :param request: Request instance for ModifyAssetTagsByAssetInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyAssetTagsByAssetInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyAssetTagsByAssetInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAssetTagsByAssetInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAssetTagsByAssetInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBanMode(self, request):
        r"""This API is used to modify the brute-force blocking mode.

        :param request: Request instance for ModifyBanMode.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyBanModeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyBanModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBanMode", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBanModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBaselinePolicy(self, request):
        r"""Create or edit a baseline policy. Policy.ID 0 means create, non-zero means edit. Name is required when creating or editing. CheckAssetType and Type must comply with the CheckAssetType and PolicyType enums.

        :param request: Request instance for ModifyBaselinePolicy.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyBaselinePolicyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyBaselinePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBaselinePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBaselinePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBaselinePolicyEnable(self, request):
        r"""Batch enable or disable baseline policies. Once disabled, a policy will no longer be included in scans and statistics.

        :param request: Request instance for ModifyBaselinePolicyEnable.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyBaselinePolicyEnableRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyBaselinePolicyEnableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBaselinePolicyEnable", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBaselinePolicyEnableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBaselineSyncConf(self, request):
        r"""This API is used to update the baseline synchronization configuration of the current account (admin). When AutoSync is true, TargetAppidList cannot be empty and its elements cannot be 0.

        :param request: Request instance for ModifyBaselineSyncConf.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyBaselineSyncConfRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyBaselineSyncConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBaselineSyncConf", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBaselineSyncConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBaselineUserOtherConf(self, request):
        r"""This API is used to update user-level baseline configurations for the current account, including sync permission, offline risk clearing, and Agent scan timeout.

        :param request: Request instance for ModifyBaselineUserOtherConf.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyBaselineUserOtherConfRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyBaselineUserOtherConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBaselineUserOtherConf", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBaselineUserOtherConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBaselineUserWeakPasswordConf(self, request):
        r"""Update the custom "user weak password" dictionary for the current account. The dictionary content is stored after server encryption. Input an empty string to clear it.

        :param request: Request instance for ModifyBaselineUserWeakPasswordConf.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyBaselineUserWeakPasswordConfRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyBaselineUserWeakPasswordConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBaselineUserWeakPasswordConf", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBaselineUserWeakPasswordConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBruteAttackBanStatus(self, request):
        r"""This API is used to set the status of brute force attack blocking.

        :param request: Request instance for ModifyBruteAttackBanStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyBruteAttackBanStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyBruteAttackBanStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBruteAttackBanStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBruteAttackBanStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBruteAttackRules(self, request):
        r"""This API is used to modify brute force cracking rules.

        :param request: Request instance for ModifyBruteAttackRules.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyBruteAttackRulesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyBruteAttackRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBruteAttackRules", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBruteAttackRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCSIPLicenseBinds(self, request):
        r"""Bind host authorization or RASP authorization to a specified order. Execute asynchronously and return TaskId to query progress. Specify the authorized version by LicenseType.

        :param request: Request instance for ModifyCSIPLicenseBinds.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyCSIPLicenseBindsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyCSIPLicenseBindsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCSIPLicenseBinds", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCSIPLicenseBindsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCSIPLicenseUnBinds(self, request):
        r"""Manually unbind host authorization. Execute synchronously and return results directly. Only unbind host authorization (category=0, including Pro and Ultimate editions). In single order mode, appid can locate the order without the need to pass ResourceId. For RASP unbinding, use ModifyCSIPRaspLicenseUnBinds.

        :param request: Request instance for ModifyCSIPLicenseUnBinds.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyCSIPLicenseUnBindsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyCSIPLicenseUnBindsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCSIPLicenseUnBinds", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCSIPLicenseUnBindsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCSIPRaspLicenseBinds(self, request):
        r"""Bind RASP or Flagship Edition Authorization to a specified order. Execute asynchronously and return TaskId to query progress. LicenseType=rasp binds RASP, LicenseType=enterprise_hp binds flagship host authorization. AssetType is case-sensitive for host/container node/EKS.

        :param request: Request instance for ModifyCSIPRaspLicenseBinds.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyCSIPRaspLicenseBindsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyCSIPRaspLicenseBindsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCSIPRaspLicenseBinds", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCSIPRaspLicenseBindsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCSIPRaspLicenseUnBinds(self, request):
        r"""Manually unbind RASP authorization. Execute synchronously and return results directly. Only unbind RASP authorization (category=1), with no unbinding frequency limit. In single order mode, appid can locate the order without the need to pass ResourceId.

        :param request: Request instance for ModifyCSIPRaspLicenseUnBinds.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyCSIPRaspLicenseUnBindsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyCSIPRaspLicenseUnBindsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCSIPRaspLicenseUnBinds", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCSIPRaspLicenseUnBindsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterDefendStatus(self, request):
        r"""Modify the cluster protection status.

        :param request: Request instance for ModifyClusterDefendStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyClusterDefendStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyClusterDefendStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterDefendStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterDefendStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCosAuditBucketMonitorStatus(self, request):
        r"""Modify the bucket monitoring status.

        :param request: Request instance for ModifyCosAuditBucketMonitorStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyCosAuditBucketMonitorStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyCosAuditBucketMonitorStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCosAuditBucketMonitorStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCosAuditBucketMonitorStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCspmShardConfig(self, request):
        r"""Updates the CSPM automated quota manager shared switch.

        :param request: Request instance for ModifyCspmShardConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyCspmShardConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyCspmShardConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCspmShardConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCspmShardConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmAccessRecord(self, request):
        r"""Modify Dspm access management information

        :param request: Request instance for ModifyDspmAccessRecord.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAccessRecordRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAccessRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmAccessRecord", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmAccessRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmApplyingIdentifyComplianceGroup(self, request):
        r"""Modifies the data identification template of the current dspm application

        :param request: Request instance for ModifyDspmApplyingIdentifyComplianceGroup.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmApplyingIdentifyComplianceGroupRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmApplyingIdentifyComplianceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmApplyingIdentifyComplianceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmApplyingIdentifyComplianceGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmApproveStatus(self, request):
        r"""Modifies the Dspm approval form status.

        :param request: Request instance for ModifyDspmApproveStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmApproveStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmApproveStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmApproveStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmApproveStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmAssetAccount(self, request):
        r"""Modify Dspm asset account information.

        :param request: Request instance for ModifyDspmAssetAccount.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAssetAccountRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAssetAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmAssetAccount", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmAssetAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmAssetAccountPrivileges(self, request):
        r"""Modify Dspm asset account permissions

        :param request: Request instance for ModifyDspmAssetAccountPrivileges.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAssetAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAssetAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmAssetAccountPrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmAssetAccountPrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmAssetDataScanTask(self, request):
        r"""Modifies a Dspm Asset Data scan task

        :param request: Request instance for ModifyDspmAssetDataScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAssetDataScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAssetDataScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmAssetDataScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmAssetDataScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmAssetDataScanTaskStatus(self, request):
        r"""Modify the status of a Dspm Asset Data scan task

        :param request: Request instance for ModifyDspmAssetDataScanTaskStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAssetDataScanTaskStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAssetDataScanTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmAssetDataScanTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmAssetDataScanTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmAssetLogDeliverySwitch(self, request):
        r"""Modify the Dspm asset log delivery switch.

        :param request: Request instance for ModifyDspmAssetLogDeliverySwitch.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAssetLogDeliverySwitchRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAssetLogDeliverySwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmAssetLogDeliverySwitch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmAssetLogDeliverySwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmAssetSecurityAnalysisSwitch(self, request):
        r"""Modify the Dspm asset log delivery switch

        :param request: Request instance for ModifyDspmAssetSecurityAnalysisSwitch.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAssetSecurityAnalysisSwitchRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAssetSecurityAnalysisSwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmAssetSecurityAnalysisSwitch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmAssetSecurityAnalysisSwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmAuditFilterStrategy(self, request):
        r"""Modify a Dspm audit filter policy

        :param request: Request instance for ModifyDspmAuditFilterStrategy.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAuditFilterStrategyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmAuditFilterStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmAuditFilterStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmAuditFilterStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmBackupSetting(self, request):
        r"""This API is used to modify the log backup settings.

        :param request: Request instance for ModifyDspmBackupSetting.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmBackupSettingRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmBackupSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmBackupSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmBackupSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmCkafkaSave(self, request):
        r"""This API is used to save the tenant CKafka configuration.

        :param request: Request instance for ModifyDspmCkafkaSave.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmCkafkaSaveRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmCkafkaSaveResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmCkafkaSave", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmCkafkaSaveResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmCkafkaStart(self, request):
        r"""This API is used to enable the log shipping.

        :param request: Request instance for ModifyDspmCkafkaStart.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmCkafkaStartRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmCkafkaStartResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmCkafkaStart", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmCkafkaStartResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmCkafkaStop(self, request):
        r"""This API is used to disable the log type shipping.

        :param request: Request instance for ModifyDspmCkafkaStop.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmCkafkaStopRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmCkafkaStopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmCkafkaStop", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmCkafkaStopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmIdentifyCategory(self, request):
        r"""Modifies dspm data identification categorization

        :param request: Request instance for ModifyDspmIdentifyCategory.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyCategoryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyCategoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmIdentifyCategory", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmIdentifyCategoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmIdentifyComplianceGroup(self, request):
        r"""Modifies a dspm data identification template

        :param request: Request instance for ModifyDspmIdentifyComplianceGroup.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyComplianceGroupRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyComplianceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmIdentifyComplianceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmIdentifyComplianceGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmIdentifyComplianceGroupStatus(self, request):
        r"""Modifies the status of a dspm data identification template

        :param request: Request instance for ModifyDspmIdentifyComplianceGroupStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyComplianceGroupStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyComplianceGroupStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmIdentifyComplianceGroupStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmIdentifyComplianceGroupStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmIdentifyComplianceRuleLevelInfo(self, request):
        r"""This API is used to modify association level information of dspm data identification template data items.

        :param request: Request instance for ModifyDspmIdentifyComplianceRuleLevelInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyComplianceRuleLevelInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyComplianceRuleLevelInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmIdentifyComplianceRuleLevelInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmIdentifyComplianceRuleLevelInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmIdentifyInfo(self, request):
        r"""Modify Dspm identity information.

        :param request: Request instance for ModifyDspmIdentifyInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmIdentifyInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmIdentifyInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmIdentifyLevelGroup(self, request):
        r"""Modifies dspm data identification classification groups

        :param request: Request instance for ModifyDspmIdentifyLevelGroup.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyLevelGroupRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyLevelGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmIdentifyLevelGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmIdentifyLevelGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmIdentifyLevelItem(self, request):
        r"""Modify dspm data identification grading information.

        :param request: Request instance for ModifyDspmIdentifyLevelItem.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyLevelItemRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyLevelItemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmIdentifyLevelItem", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmIdentifyLevelItemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmIdentifyRule(self, request):
        r"""Modify a dspm identification data item

        :param request: Request instance for ModifyDspmIdentifyRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmIdentifyRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmIdentifyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmIdentifyRuleStatus(self, request):
        r"""Modifies the status of a dspm identification data item

        :param request: Request instance for ModifyDspmIdentifyRuleStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyRuleStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIdentifyRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmIdentifyRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmIdentifyRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmIpInfo(self, request):
        r"""Modify DspmIp information.

        :param request: Request instance for ModifyDspmIpInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIpInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmIpInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmIpInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmIpInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmLogDeliveryType(self, request):
        r"""This API is used to modify the log shipping configuration information.

        :param request: Request instance for ModifyDspmLogDeliveryType.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmLogDeliveryTypeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmLogDeliveryTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmLogDeliveryType", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmLogDeliveryTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmPersonalIdentify(self, request):
        r"""Modifies the Dspm personal identity ID.

        :param request: Request instance for ModifyDspmPersonalIdentify.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmPersonalIdentifyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmPersonalIdentifyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmPersonalIdentify", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmPersonalIdentifyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmRestoreLogTask(self, request):
        r"""This API is used to restore the backup logs.

        :param request: Request instance for ModifyDspmRestoreLogTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmRestoreLogTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmRestoreLogTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmRestoreLogTask", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmRestoreLogTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmRiskInfo(self, request):
        r"""Modifies Dspm risk information

        :param request: Request instance for ModifyDspmRiskInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmRiskInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmRiskInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmRiskInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmRiskInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmRiskStrategy(self, request):
        r"""Modifies Dspm risk policies

        :param request: Request instance for ModifyDspmRiskStrategy.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmRiskStrategyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmRiskStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmRiskStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmRiskStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDspmWhitelistStrategy(self, request):
        r"""Modify the Dspm allowlist policy

        :param request: Request instance for ModifyDspmWhitelistStrategy.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyDspmWhitelistStrategyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyDspmWhitelistStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDspmWhitelistStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDspmWhitelistStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEDRRule(self, request):
        r"""This API is used to edit or create an EDR policy.

        :param request: Request instance for ModifyEDRRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyEDRRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyEDRRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEDRRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEDRRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEDRRuleStatus(self, request):
        r"""This API is used to modify the switch status of EDR policies.

        :param request: Request instance for ModifyEDRRuleStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyEDRRuleStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyEDRRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEDRRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEDRRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEDRRulesAction(self, request):
        r"""Batch modify EDR policy actions.

        :param request: Request instance for ModifyEDRRulesAction.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyEDRRulesActionRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyEDRRulesActionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEDRRulesAction", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEDRRulesActionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEdrAlertIsolation(self, request):
        r"""EDR alert quarantine and recovery

        :param request: Request instance for ModifyEdrAlertIsolation.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyEdrAlertIsolationRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyEdrAlertIsolationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEdrAlertIsolation", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEdrAlertIsolationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEdrAlertPermanentIgnore(self, request):
        r"""Permanently ignore EDR multi-behavior alarms. Add the host and rule corresponding to the alarm to the AI-Link permanent ignore allowlist. Subsequently, alarms of the same type will be automatically discarded.

        :param request: Request instance for ModifyEdrAlertPermanentIgnore.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyEdrAlertPermanentIgnoreRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyEdrAlertPermanentIgnoreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEdrAlertPermanentIgnore", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEdrAlertPermanentIgnoreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEdrAlertStatus(self, request):
        r"""Handle the status of an EDR alert

        :param request: Request instance for ModifyEdrAlertStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyEdrAlertStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyEdrAlertStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEdrAlertStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEdrAlertStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEdrExcludeNetworkSegments(self, request):
        r"""This API is used to modify the CIDR block exclusion settings for log collection. IPs, IP ranges, and CIDR formats are supported, with up to 100 entries.

        :param request: Request instance for ModifyEdrExcludeNetworkSegments.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyEdrExcludeNetworkSegmentsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyEdrExcludeNetworkSegmentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEdrExcludeNetworkSegments", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEdrExcludeNetworkSegmentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEdrLogCollectPath(self, request):
        r"""This API is used to modify path configurations for application log collection.

        :param request: Request instance for ModifyEdrLogCollectPath.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyEdrLogCollectPathRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyEdrLogCollectPathResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEdrLogCollectPath", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEdrLogCollectPathResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyExposureAutoTagRule(self, request):
        r"""Update automatic cloud boundary tagging rules

        :param request: Request instance for ModifyExposureAutoTagRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyExposureAutoTagRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyExposureAutoTagRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyExposureAutoTagRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyExposureAutoTagRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyExposureAutoTagRuleStatus(self, request):
        r"""Enable or disable automatic cloud boundary tagging rules.

        :param request: Request instance for ModifyExposureAutoTagRuleStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyExposureAutoTagRuleStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyExposureAutoTagRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyExposureAutoTagRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyExposureAutoTagRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyExposureTag(self, request):
        r"""Update custom tags for cloud boundaries

        :param request: Request instance for ModifyExposureTag.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyExposureTagRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyExposureTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyExposureTag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyExposureTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIaCTokenPeriod(self, request):
        r"""Modify the storage cycle of IaC detection integration tokens.

        :param request: Request instance for ModifyIaCTokenPeriod.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyIaCTokenPeriodRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyIaCTokenPeriodResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIaCTokenPeriod", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIaCTokenPeriodResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyImageRegistry(self, request):
        r"""Modify image repository information.

        :param request: Request instance for ModifyImageRegistry.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyImageRegistryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyImageRegistryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyImageRegistry", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyImageRegistryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyImageRegistryTimedScanTaskConfig(self, request):
        r"""Modify the scheduled scan task configuration of an image repository

        :param request: Request instance for ModifyImageRegistryTimedScanTaskConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyImageRegistryTimedScanTaskConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyImageRegistryTimedScanTaskConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyImageRegistryTimedScanTaskConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyImageRegistryTimedScanTaskConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyImageSensitiveWhitelist(self, request):
        r"""Modifies the Sensitive Information Allowlist of a Container Image

        :param request: Request instance for ModifyImageSensitiveWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyImageSensitiveWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyImageSensitiveWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyImageSensitiveWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyImageSensitiveWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyImageVirusWhitelist(self, request):
        r"""This API is used to query asset database information.

        :param request: Request instance for ModifyImageVirusWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyImageVirusWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyImageVirusWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyImageVirusWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyImageVirusWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyImageVulWhitelist(self, request):
        r"""Modifies the vulnerability allowlist of a container image.

        :param request: Request instance for ModifyImageVulWhitelist.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyImageVulWhitelistRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyImageVulWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyImageVulWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyImageVulWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLoginWhiteRecord(self, request):
        r"""This API is used to update the log-in audit allowlist information. (The number of server lists needs to be less than 1,000.)

        :param request: Request instance for ModifyLoginWhiteRecord.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyLoginWhiteRecordRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyLoginWhiteRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoginWhiteRecord", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoginWhiteRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMachineAutoClearConfig(self, request):
        r"""This API is used to modify the cleanup configuration of the machine.

        :param request: Request instance for ModifyMachineAutoClearConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyMachineAutoClearConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyMachineAutoClearConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMachineAutoClearConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMachineAutoClearConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMachineRemark(self, request):
        r"""Modify the remark information of a host asset

        :param request: Request instance for ModifyMachineRemark.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyMachineRemarkRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyMachineRemarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMachineRemark", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMachineRemarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMachinesLoginType(self, request):
        r"""This API is used to modify host login methods in batches.

        :param request: Request instance for ModifyMachinesLoginType.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyMachinesLoginTypeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyMachinesLoginTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMachinesLoginType", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMachinesLoginTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMalwareTimingScanSettings(self, request):
        r"""Modify the scheduled scan configuration for malicious file scan, including scan cycle, detection mode, asset scope, engine selection, and quarantine configuration.

        :param request: Request instance for ModifyMalwareTimingScanSettings.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyMalwareTimingScanSettingsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyMalwareTimingScanSettingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMalwareTimingScanSettings", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMalwareTimingScanSettingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNFSScanConf(self, request):
        r"""This API is used to add or update the global configuration for NFS scanning.

        :param request: Request instance for ModifyNFSScanConf.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyNFSScanConfRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyNFSScanConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNFSScanConf", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNFSScanConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNFSScanHost(self, request):
        r"""This API is used to disable process guard.

        :param request: Request instance for ModifyNFSScanHost.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyNFSScanHostRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyNFSScanHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNFSScanHost", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNFSScanHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNetAttackSetting(self, request):
        r"""Modify the network attack detection switch and asset scope configuration.

        :param request: Request instance for ModifyNetAttackSetting.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyNetAttackSettingRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyNetAttackSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNetAttackSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNetAttackSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNotifyAgentOfflineDuration(self, request):
        r"""This API is used to modify client offline duration.

        :param request: Request instance for ModifyNotifyAgentOfflineDuration.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyNotifyAgentOfflineDurationRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyNotifyAgentOfflineDurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNotifyAgentOfflineDuration", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNotifyAgentOfflineDurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNotifyAssetConfig(self, request):
        r"""Modify the asset scope configuration for notifications

        :param request: Request instance for ModifyNotifyAssetConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyNotifyAssetConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyNotifyAssetConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNotifyAssetConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNotifyAssetConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNotifyMember(self, request):
        r"""Modify the member account for notification.

        :param request: Request instance for ModifyNotifyMember.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyNotifyMemberRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyNotifyMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNotifyMember", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNotifyMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNotifySetting(self, request):
        r"""Modifies notification settings

        :param request: Request instance for ModifyNotifySetting.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyNotifySettingRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyNotifySettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNotifySetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNotifySettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNotifySettingAk(self, request):
        r"""Modify notification settings

        :param request: Request instance for ModifyNotifySettingAk.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyNotifySettingAkRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyNotifySettingAkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNotifySettingAk", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNotifySettingAkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNotifySettingAlert(self, request):
        r"""Modify alarm center notification advanced configuration

        :param request: Request instance for ModifyNotifySettingAlert.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyNotifySettingAlertRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyNotifySettingAlertResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNotifySettingAlert", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNotifySettingAlertResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyOrganizationAccountStatus(self, request):
        r"""Modify Group Account Status

        :param request: Request instance for ModifyOrganizationAccountStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyOrganizationAccountStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyOrganizationAccountStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOrganizationAccountStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyOrganizationAccountStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPayConfig(self, request):
        r"""Modify the auto-scaling configuration (multi-module and expandable; only the CWP module is available in the current period).

        Auto-scaling is an external user-oriented concept equivalent to automatic purchase (auto_repurchase) at the underlying layer: when an account has new assets, the desired authorization is automatically purchased.

        Supplemental description:
        1. In the current period, only the HostConfig module is implemented for host security. Subsequent scalability allows named module fields for container security and AI-Agent security. Configuration fields of each module can be heterogeneous.
        2. Partial update semantics: An empty module object indicates that the module is not modified, and an empty field in the module indicates that this field is not modified;
        3. HostConfig.Switch linkage map: auto_repurchase_switch; auto_bind_switch is always on and not modified by this API.
        4. Auto renewal (renew_flag) is not modified by this API; to query the limit/amount, call DescribeLicenseStatus.
        5. The top auto scaling global switch state is aggregated by the frontend based on each module switch. The backend does not store or return the global switch.

        :param request: Request instance for ModifyPayConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyPayConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyPayConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPayConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPayConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProtectionSetting(self, request):
        r"""This API is used to configure protection settings for the major event protection package.

        :param request: Request instance for ModifyProtectionSetting.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyProtectionSettingRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyProtectionSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProtectionSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProtectionSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRaspLicenseBinds(self, request):
        r"""Bind an important period guarantee protection authorization package.

        :param request: Request instance for ModifyRaspLicenseBinds.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyRaspLicenseBindsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyRaspLicenseBindsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRaspLicenseBinds", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRaspLicenseBindsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyReverseShellSystemPolicyConfig(self, request):
        r"""This API is used to modify the intranet alert and asset scope configuration for rebound Shell.

        :param request: Request instance for ModifyReverseShellSystemPolicyConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyReverseShellSystemPolicyConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyReverseShellSystemPolicyConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyReverseShellSystemPolicyConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyReverseShellSystemPolicyConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRiskCenterRiskStatus(self, request):
        r"""Modify Risk Center Risk Status

        :param request: Request instance for ModifyRiskCenterRiskStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyRiskCenterRiskStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyRiskCenterRiskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRiskCenterRiskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRiskCenterRiskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRiskCenterScanTask(self, request):
        r"""Modify Risk Center Scan Task

        :param request: Request instance for ModifyRiskCenterScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyRiskCenterScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyRiskCenterScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRiskCenterScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRiskCenterScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRiskScanCronConfig(self, request):
        r"""Update the periodic scanning plan

        :param request: Request instance for ModifyRiskScanCronConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyRiskScanCronConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyRiskScanCronConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRiskScanCronConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRiskScanCronConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySandboxACLRule(self, request):
        r"""Modify an existing ACL user rule. Fields not passed retain their original values, and partial field update is supported.

        :param request: Request instance for ModifySandboxACLRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifySandboxACLRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifySandboxACLRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySandboxACLRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySandboxACLRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySandboxACLRuleStatus(self, request):
        r"""Batch switch the enable/disable status of ACL user rules. If any rule does not exist, belongs to another tenant, or has been deleted, an error is returned for the entirety.

        :param request: Request instance for ModifySandboxACLRuleStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifySandboxACLRuleStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifySandboxACLRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySandboxACLRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySandboxACLRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySandboxAlertStatus(self, request):
        r"""Batch update traffic sandbox alarms (overwrite ACL, DLP, and LLM audit). Locate the alarm source by AlertType + BelongAssetType. Status supports HANDLED / IGNORE to modify status, as well as DELETE to delete. If any alarm ID does not exist or belongs to another tenant, an error is returned overall. Note: Whitelisting (PASS) is not handled by this interface. It is triggered by Create/Modify***Rule writing back through AlertID.

        :param request: Request instance for ModifySandboxAlertStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifySandboxAlertStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifySandboxAlertStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySandboxAlertStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySandboxAlertStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySandboxDLPRule(self, request):
        r"""Modify an existing DLP user rule. Fields not passed retain their original values, and partial field update is supported. BelongAssetType cannot be modified.

        :param request: Request instance for ModifySandboxDLPRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifySandboxDLPRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifySandboxDLPRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySandboxDLPRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySandboxDLPRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySandboxDLPRuleStatus(self, request):
        r"""Batch switch the enable/disable status of DLP user rules. If any rule does not exist, belongs to another tenant, or has been deleted, an error is returned for the entirety.

        :param request: Request instance for ModifySandboxDLPRuleStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifySandboxDLPRuleStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifySandboxDLPRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySandboxDLPRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySandboxDLPRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySandboxFileRule(self, request):
        r"""Modify command sandbox file access rule

        :param request: Request instance for ModifySandboxFileRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifySandboxFileRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifySandboxFileRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySandboxFileRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySandboxFileRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySandboxFileRuleStatus(self, request):
        r"""Batch enable or disable command sandbox file access rules.

        :param request: Request instance for ModifySandboxFileRuleStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifySandboxFileRuleStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifySandboxFileRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySandboxFileRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySandboxFileRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySandboxLLMAuditRule(self, request):
        r"""Modify an existing LLM audit user rule. Fields not passed retain their original values, and partial field update is supported.

        :param request: Request instance for ModifySandboxLLMAuditRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifySandboxLLMAuditRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifySandboxLLMAuditRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySandboxLLMAuditRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySandboxLLMAuditRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySandboxLLMAuditRuleStatus(self, request):
        r"""Batch switch the enable or disable status of LLM audit user rules. If any rule does not exist, belongs to another tenant, or has been deleted, an error is returned overall.

        :param request: Request instance for ModifySandboxLLMAuditRuleStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifySandboxLLMAuditRuleStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifySandboxLLMAuditRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySandboxLLMAuditRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySandboxLLMAuditRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityScoreRule(self, request):
        r"""Modify a security scoring rule. You need to pass in a complete rule set.

        :param request: Request instance for ModifySecurityScoreRule.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifySecurityScoreRuleRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifySecurityScoreRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityScoreRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityScoreRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyShareUserAK(self, request):
        r"""Edit the ak monitoring account.

        :param request: Request instance for ModifyShareUserAK.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyShareUserAKRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyShareUserAKResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyShareUserAK", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyShareUserAKResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyShareUserCSPM(self, request):
        r"""Edit a CSPM shared account

        :param request: Request instance for ModifyShareUserCSPM.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyShareUserCSPMRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyShareUserCSPMResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyShareUserCSPM", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyShareUserCSPMResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyShareUserDspm(self, request):
        r"""Edit dspm monitored account

        :param request: Request instance for ModifyShareUserDspm.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyShareUserDspmRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyShareUserDspmResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyShareUserDspm", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyShareUserDspmResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySkillScanAlertStatus(self, request):
        r"""Batch modify the processing status of Skill security detection alarms.

        :param request: Request instance for ModifySkillScanAlertStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifySkillScanAlertStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifySkillScanAlertStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySkillScanAlertStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySkillScanAlertStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUebaRuleSwitch(self, request):
        r"""Update the switch of a custom policy

        :param request: Request instance for ModifyUebaRuleSwitch.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyUebaRuleSwitchRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyUebaRuleSwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUebaRuleSwitch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUebaRuleSwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVulScanPeriodic(self, request):
        r"""This API is used to modify vulnerability scanning (period scanning).

        :param request: Request instance for ModifyVulScanPeriodic.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyVulScanPeriodicRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyVulScanPeriodicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVulScanPeriodic", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVulScanPeriodicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVulWhitelistConfig(self, request):
        r"""This API is used to modify the vulnerability allowlist configuration.

        :param request: Request instance for ModifyVulWhitelistConfig.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyVulWhitelistConfigRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyVulWhitelistConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVulWhitelistConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVulWhitelistConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVulWhitelistSwitch(self, request):
        r"""This API is used to modify the vulnerability allowlist switch.

        :param request: Request instance for ModifyVulWhitelistSwitch.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyVulWhitelistSwitchRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyVulWhitelistSwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVulWhitelistSwitch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVulWhitelistSwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebhookPolicy(self, request):
        r"""Add or modify a notification policy. ID > 0 means modification; ID = 0 or not passed means adding new. When MemberAppIds is configured as empty, the policy only acts on current root account events; when not empty, it acts on the self account + listed member accounts at the same time.

        :param request: Request instance for ModifyWebhookPolicy.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyWebhookPolicyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyWebhookPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebhookPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebhookPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebhookPolicyStatus(self, request):
        r"""Switch the enable status of the notification policy.

        :param request: Request instance for ModifyWebhookPolicyStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyWebhookPolicyStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyWebhookPolicyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebhookPolicyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebhookPolicyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebhookReceiver(self, request):
        r"""Add or modify a receiving robot. ID > 0 means modifying an existing record; ID = 0 or not passed means adding new. The robot type is determined by the Type field. When Type=WEBHOOK, WebhookAddr is required. When Type=SCF, SCFRegion/Namespace/FunctionName/FunctionVersion/Alias/MaxWaitSeconds are all required. Type is not allowed to be changed during modification.

        :param request: Request instance for ModifyWebhookReceiver.
        :type request: :class:`tencentcloud.csip.v20221121.models.ModifyWebhookReceiverRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ModifyWebhookReceiverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebhookReceiver", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebhookReceiverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OperateRisk(self, request):
        r"""Risk operation example

        :param request: Request instance for OperateRisk.
        :type request: :class:`tencentcloud.csip.v20221121.models.OperateRiskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.OperateRiskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OperateRisk", params, headers=headers)
            response = json.loads(body)
            model = models.OperateRiskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OperateRiskRulePolicy(self, request):
        r"""Custom risk rule

        :param request: Request instance for OperateRiskRulePolicy.
        :type request: :class:`tencentcloud.csip.v20221121.models.OperateRiskRulePolicyRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.OperateRiskRulePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OperateRiskRulePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.OperateRiskRulePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetDspmAssetAccountPassword(self, request):
        r"""Reset the Dspm asset account password.

        :param request: Request instance for ResetDspmAssetAccountPassword.
        :type request: :class:`tencentcloud.csip.v20221121.models.ResetDspmAssetAccountPasswordRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ResetDspmAssetAccountPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetDspmAssetAccountPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetDspmAssetAccountPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RetryDspmExportLog(self, request):
        r"""RetryExportLog

        :param request: Request instance for RetryDspmExportLog.
        :type request: :class:`tencentcloud.csip.v20221121.models.RetryDspmExportLogRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.RetryDspmExportLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RetryDspmExportLog", params, headers=headers)
            response = json.loads(body)
            model = models.RetryDspmExportLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RevertDspmAssetAccount(self, request):
        r"""Restore a Dspm asset account.

        :param request: Request instance for RevertDspmAssetAccount.
        :type request: :class:`tencentcloud.csip.v20221121.models.RevertDspmAssetAccountRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.RevertDspmAssetAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RevertDspmAssetAccount", params, headers=headers)
            response = json.loads(body)
            model = models.RevertDspmAssetAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanBaselineAssetItemList(self, request):
        r"""This API is used to trigger a rescan of some detection items for a single asset.

        :param request: Request instance for ScanBaselineAssetItemList.
        :type request: :class:`tencentcloud.csip.v20221121.models.ScanBaselineAssetItemListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ScanBaselineAssetItemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanBaselineAssetItemList", params, headers=headers)
            response = json.loads(body)
            model = models.ScanBaselineAssetItemListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanBaselineItemList(self, request):
        r"""This API is used to rescan detection items under a specified policy.

        :param request: Request instance for ScanBaselineItemList.
        :type request: :class:`tencentcloud.csip.v20221121.models.ScanBaselineItemListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ScanBaselineItemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanBaselineItemList", params, headers=headers)
            response = json.loads(body)
            model = models.ScanBaselineItemListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanBaselinePolicyList(self, request):
        r"""Trigger a holistic rescan for a batch of baseline policies via the one-click scan entry on the strategy list page. All assets within the policy hit scope will be rescanned.

        :param request: Request instance for ScanBaselinePolicyList.
        :type request: :class:`tencentcloud.csip.v20221121.models.ScanBaselinePolicyListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ScanBaselinePolicyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanBaselinePolicyList", params, headers=headers)
            response = json.loads(body)
            model = models.ScanBaselinePolicyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanBaselineRiskList(self, request):
        r"""Triggers a rescan for a batch of risk records. It is commonly used for rescanning after selecting multiple risks on the Risk List page.

        :param request: Request instance for ScanBaselineRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.ScanBaselineRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ScanBaselineRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanBaselineRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.ScanBaselineRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanCSIPTaskAgain(self, request):
        r"""This API is used to delete CSIP manual scan tasks.

        :param request: Request instance for ScanCSIPTaskAgain.
        :type request: :class:`tencentcloud.csip.v20221121.models.ScanCSIPTaskAgainRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ScanCSIPTaskAgainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanCSIPTaskAgain", params, headers=headers)
            response = json.loads(body)
            model = models.ScanCSIPTaskAgainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanEDRTaskAgain(self, request):
        r"""Create a scan task based on the original task configuration. If AssetId is empty, get all asset info from TaskId. If AssetId is not empty, only the single asset is included.

        :param request: Request instance for ScanEDRTaskAgain.
        :type request: :class:`tencentcloud.csip.v20221121.models.ScanEDRTaskAgainRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.ScanEDRTaskAgainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanEDRTaskAgain", params, headers=headers)
            response = json.loads(body)
            model = models.ScanEDRTaskAgainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SendDspmAssetLoginSmsCode(self, request):
        r"""Sends the access verification code for a Dspm asset

        :param request: Request instance for SendDspmAssetLoginSmsCode.
        :type request: :class:`tencentcloud.csip.v20221121.models.SendDspmAssetLoginSmsCodeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.SendDspmAssetLoginSmsCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendDspmAssetLoginSmsCode", params, headers=headers)
            response = json.loads(body)
            model = models.SendDspmAssetLoginSmsCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SendDspmCkafkaTest(self, request):
        r"""This API is used to test the tenant CKafka connectivity.

        :param request: Request instance for SendDspmCkafkaTest.
        :type request: :class:`tencentcloud.csip.v20221121.models.SendDspmCkafkaTestRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.SendDspmCkafkaTestResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendDspmCkafkaTest", params, headers=headers)
            response = json.loads(body)
            model = models.SendDspmCkafkaTestResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartOrModifyPreventUninstall(self, request):
        r"""Enable or modify the anti-uninstall feature configuration.

        :param request: Request instance for StartOrModifyPreventUninstall.
        :type request: :class:`tencentcloud.csip.v20221121.models.StartOrModifyPreventUninstallRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.StartOrModifyPreventUninstallResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartOrModifyPreventUninstall", params, headers=headers)
            response = json.loads(body)
            model = models.StartOrModifyPreventUninstallResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartOrModifyProcessDaemon(self, request):
        r"""This API is used to enable or modify process guard feature configurations.

        :param request: Request instance for StartOrModifyProcessDaemon.
        :type request: :class:`tencentcloud.csip.v20221121.models.StartOrModifyProcessDaemonRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.StartOrModifyProcessDaemonResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartOrModifyProcessDaemon", params, headers=headers)
            response = json.loads(body)
            model = models.StartOrModifyProcessDaemonResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopBaselineScanTask(self, request):
        r"""This API is used to stop a specified baseline scan main task. It only takes effect for tasks in the INIT, SUBTASK_CREATING, or SCANNING status.

        :param request: Request instance for StopBaselineScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.StopBaselineScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.StopBaselineScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopBaselineScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopBaselineScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopCSIPManualMalwareScan(self, request):
        r"""CSIP manual scan stop API

        :param request: Request instance for StopCSIPManualMalwareScan.
        :type request: :class:`tencentcloud.csip.v20221121.models.StopCSIPManualMalwareScanRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.StopCSIPManualMalwareScanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopCSIPManualMalwareScan", params, headers=headers)
            response = json.loads(body)
            model = models.StopCSIPManualMalwareScanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopEDRScanTask(self, request):
        r"""Stop or cancel a scan task. For tasks in SCANNING status, call RPC to stop them. For tasks in WAIT status, update the database directly to cancel them. Only the task creator can perform these operations.

        :param request: Request instance for StopEDRScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.StopEDRScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.StopEDRScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopEDRScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopEDRScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopImageRegistryScanTask(self, request):
        r"""Terminate an image scanning task in a mirror repository

        :param request: Request instance for StopImageRegistryScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.StopImageRegistryScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.StopImageRegistryScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopImageRegistryScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopImageRegistryScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopPreventUninstall(self, request):
        r"""This API is used to disable the anti-uninstallation feature.

        :param request: Request instance for StopPreventUninstall.
        :type request: :class:`tencentcloud.csip.v20221121.models.StopPreventUninstallRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.StopPreventUninstallResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopPreventUninstall", params, headers=headers)
            response = json.loads(body)
            model = models.StopPreventUninstallResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopProcessDaemon(self, request):
        r"""This API is used to disable process guard.

        :param request: Request instance for StopProcessDaemon.
        :type request: :class:`tencentcloud.csip.v20221121.models.StopProcessDaemonRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.StopProcessDaemonResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopProcessDaemon", params, headers=headers)
            response = json.loads(body)
            model = models.StopProcessDaemonResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopRiskCenterTask(self, request):
        r"""Stop Scanning Tasks of Risk Center

        :param request: Request instance for StopRiskCenterTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.StopRiskCenterTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.StopRiskCenterTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopRiskCenterTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopRiskCenterTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopVulScanTask(self, request):
        r"""Stop vulnerability scanning (task scan).

        :param request: Request instance for StopVulScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.StopVulScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.StopVulScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopVulScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopVulScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SyncDspmAssets(self, request):
        r"""Synchronize assets supported by dspm

        :param request: Request instance for SyncDspmAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.SyncDspmAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.SyncDspmAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncDspmAssets", params, headers=headers)
            response = json.loads(body)
            model = models.SyncDspmAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SyncDspmUsers(self, request):
        r"""Synchronize the list of dspm users.

        :param request: Request instance for SyncDspmUsers.
        :type request: :class:`tencentcloud.csip.v20221121.models.SyncDspmUsersRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.SyncDspmUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncDspmUsers", params, headers=headers)
            response = json.loads(body)
            model = models.SyncDspmUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SyncImageRegistry(self, request):
        r"""Synchronize the mirror repository

        :param request: Request instance for SyncImageRegistry.
        :type request: :class:`tencentcloud.csip.v20221121.models.SyncImageRegistryRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.SyncImageRegistryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncImageRegistry", params, headers=headers)
            response = json.loads(body)
            model = models.SyncImageRegistryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TestWebhookReceiver(self, request):
        r"""Send a test message to the designated receiving robot to verify reachability and configuration. Use the "Test" button in the corresponding table row.

        :param request: Request instance for TestWebhookReceiver.
        :type request: :class:`tencentcloud.csip.v20221121.models.TestWebhookReceiverRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.TestWebhookReceiverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TestWebhookReceiver", params, headers=headers)
            response = json.loads(body)
            model = models.TestWebhookReceiverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UninstallClusterAgent(self, request):
        r"""Uninstall the cluster container security Agent.

        :param request: Request instance for UninstallClusterAgent.
        :type request: :class:`tencentcloud.csip.v20221121.models.UninstallClusterAgentRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.UninstallClusterAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UninstallClusterAgent", params, headers=headers)
            response = json.loads(body)
            model = models.UninstallClusterAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UninstallKeySandboxSkill(self, request):
        r"""Uninstall the key sandbox SKILL from designated machine instances. Support batch operations, allowing multiple instance IDs at once. After uninstallation, the AI Agent on the target machine will not be able to access credentials via the key sandbox proxy. Repeated calls on instances not installed will not trigger an error (idempotent), and are directly deemed successful.

        :param request: Request instance for UninstallKeySandboxSkill.
        :type request: :class:`tencentcloud.csip.v20221121.models.UninstallKeySandboxSkillRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.UninstallKeySandboxSkillResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UninstallKeySandboxSkill", params, headers=headers)
            response = json.loads(body)
            model = models.UninstallKeySandboxSkillResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAccessKeyAlarmStatus(self, request):
        r"""Tag risks or alarms as processed or ignored.

        :param request: Request instance for UpdateAccessKeyAlarmStatus.
        :type request: :class:`tencentcloud.csip.v20221121.models.UpdateAccessKeyAlarmStatusRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.UpdateAccessKeyAlarmStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAccessKeyAlarmStatus", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAccessKeyAlarmStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAccessKeyRemark(self, request):
        r"""Edit the remark of an access key/source IP.

        :param request: Request instance for UpdateAccessKeyRemark.
        :type request: :class:`tencentcloud.csip.v20221121.models.UpdateAccessKeyRemarkRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.UpdateAccessKeyRemarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAccessKeyRemark", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAccessKeyRemarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAlertStatusList(self, request):
        r"""This API is used to handle alarm status in batches.

        :param request: Request instance for UpdateAlertStatusList.
        :type request: :class:`tencentcloud.csip.v20221121.models.UpdateAlertStatusListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.UpdateAlertStatusListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAlertStatusList", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAlertStatusListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateClusterOwner(self, request):
        r"""Bind and update a cluster owner

        :param request: Request instance for UpdateClusterOwner.
        :type request: :class:`tencentcloud.csip.v20221121.models.UpdateClusterOwnerRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.UpdateClusterOwnerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateClusterOwner", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateClusterOwnerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VerifyDspmAssetLoginCode(self, request):
        r"""Verify the login verification code for a Dspm asset.

        :param request: Request instance for VerifyDspmAssetLoginCode.
        :type request: :class:`tencentcloud.csip.v20221121.models.VerifyDspmAssetLoginCodeRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.VerifyDspmAssetLoginCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifyDspmAssetLoginCode", params, headers=headers)
            response = json.loads(body)
            model = models.VerifyDspmAssetLoginCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))