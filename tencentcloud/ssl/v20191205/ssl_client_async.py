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
from tencentcloud.ssl.v20191205 import models
from typing import Dict


class SslClient(AbstractClient):
    _apiVersion = '2019-12-05'
    _endpoint = 'ssl.intl.tencentcloudapi.com'
    _service = 'ssl'

    async def ApplyCertificate(
            self,
            request: models.ApplyCertificateRequest,
            opts: Dict = None,
    ) -> models.ApplyCertificateResponse:
        """
        This API is used to apply for a free certificate.
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchDeleteCSR(
            self,
            request: models.BatchDeleteCSRRequest,
            opts: Dict = None,
    ) -> models.BatchDeleteCSRResponse:
        """
        This API is used to batch delete CSRs.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDeleteCSR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDeleteCSRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelAuditCertificate(
            self,
            request: models.CancelAuditCertificateRequest,
            opts: Dict = None,
    ) -> models.CancelAuditCertificateResponse:
        """
        This API is used to cancel certificate review.
        """
        
        kwargs = {}
        kwargs["action"] = "CancelAuditCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelAuditCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelCertificateOrder(
            self,
            request: models.CancelCertificateOrderRequest,
            opts: Dict = None,
    ) -> models.CancelCertificateOrderResponse:
        """
        This API is used to cancel a certificate order.
        """
        
        kwargs = {}
        kwargs["action"] = "CancelCertificateOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelCertificateOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CommitCertificateInformation(
            self,
            request: models.CommitCertificateInformationRequest,
            opts: Dict = None,
    ) -> models.CommitCertificateInformationResponse:
        """
        Submit payment certificate orders; This API does not maintain new features, and you can use the new API to submit orders. [CertificateOrderSubmit](https://intl.cloud.tencent.com/document/product/400/116032?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "CommitCertificateInformation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CommitCertificateInformationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCSR(
            self,
            request: models.CreateCSRRequest,
            opts: Dict = None,
    ) -> models.CreateCSRResponse:
        """
        This API is used to create a CSR.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCSR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCSRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCertificate(
            self,
            request: models.CreateCertificateRequest,
            opts: Dict = None,
    ) -> models.CreateCertificateResponse:
        """
        This API is used to purchase a certificate.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCertificateBindResourceSyncTask(
            self,
            request: models.CreateCertificateBindResourceSyncTaskRequest,
            opts: Dict = None,
    ) -> models.CreateCertificateBindResourceSyncTaskResponse:
        """
        This API is used to create an async task for querying the cloud resources associated with a certificate. If such a task already exists under the certificate ID, the ID of this task is returned as the result. The following types of cloud resources are supported: CLB, CDN, WAF, LIVE, VOD, DDOS, TKE, APIGATEWAY, TCB, and TEO (EDGEONE). You can query the result of this task using the `DescribeCertificateBindResourceTaskResult` API.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCertificateBindResourceSyncTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCertificateBindResourceSyncTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCertificate(
            self,
            request: models.DeleteCertificateRequest,
            opts: Dict = None,
    ) -> models.DeleteCertificateResponse:
        """
        This API is used to delete a certificate.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCSR(
            self,
            request: models.DescribeCSRRequest,
            opts: Dict = None,
    ) -> models.DescribeCSRResponse:
        """
        This API is used to query the details of a CSR.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCSR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCSRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCSRSet(
            self,
            request: models.DescribeCSRSetRequest,
            opts: Dict = None,
    ) -> models.DescribeCSRSetResponse:
        """
        This API is used to query the CSR list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCSRSet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCSRSetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCertificate(
            self,
            request: models.DescribeCertificateRequest,
            opts: Dict = None,
    ) -> models.DescribeCertificateResponse:
        """
        This API is used to get certificate information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCertificateBindResourceTaskDetail(
            self,
            request: models.DescribeCertificateBindResourceTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCertificateBindResourceTaskDetailResponse:
        """
        This API is used to query the task result of CreateCertificateBindResourceSyncTask, returning the asynchronous task result of the certificate associated with cloud resources, supporting the following cloud resources: clb, cdn, waf, live, vod, ddos, tke, apigateway, tcb, teo (edgeOne), cos.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCertificateBindResourceTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCertificateBindResourceTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCertificateBindResourceTaskResult(
            self,
            request: models.DescribeCertificateBindResourceTaskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeCertificateBindResourceTaskResultResponse:
        """
        This API is used to query the result of an async task created with `CreateCertificateBindResourceSyncTask` to query cloud resources associated with a certificate. The following types of cloud resources are supported: CLB, CDN, WAF, LIVE, VOD, DDOS, TKE, APIGATEWAY, TCB, and TEO (EDGEONE).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCertificateBindResourceTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCertificateBindResourceTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCertificateDetail(
            self,
            request: models.DescribeCertificateDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCertificateDetailResponse:
        """
        This API is used to get certificate details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCertificateDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCertificateDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCertificateOperateLogs(
            self,
            request: models.DescribeCertificateOperateLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeCertificateOperateLogsResponse:
        """
        This API is used to get certificate operation logs in the current account.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCertificateOperateLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCertificateOperateLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCertificates(
            self,
            request: models.DescribeCertificatesRequest,
            opts: Dict = None,
    ) -> models.DescribeCertificatesResponse:
        """
        This API is used to get the certificate list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCertificates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCertificatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostTeoInstanceList(
            self,
            request: models.DescribeHostTeoInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeHostTeoInstanceListResponse:
        """
        This API is used to query the list of EdgeOne instances to which a certificate can be deployed.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostTeoInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostTeoInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostUpdateRecord(
            self,
            request: models.DescribeHostUpdateRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeHostUpdateRecordResponse:
        """
        Query certificate cloud resource update record list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostUpdateRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostUpdateRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostUpdateRecordDetail(
            self,
            request: models.DescribeHostUpdateRecordDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeHostUpdateRecordDetailResponse:
        """
        This API is used to query the update record details of certificate cloud resources.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostUpdateRecordDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostUpdateRecordDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostUploadUpdateRecord(
            self,
            request: models.DescribeHostUploadUpdateRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeHostUploadUpdateRecordResponse:
        """
        This API is used to query the record list of cloud resource updates for certificates (certificate ID unchanged).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostUploadUpdateRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostUploadUpdateRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostUploadUpdateRecordDetail(
            self,
            request: models.DescribeHostUploadUpdateRecordDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeHostUploadUpdateRecordDetailResponse:
        """
        This API is used to query the deployment record details of certificate update records (certificate ID unchanged).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostUploadUpdateRecordDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostUploadUpdateRecordDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DownloadCertificate(
            self,
            request: models.DownloadCertificateRequest,
            opts: Dict = None,
    ) -> models.DownloadCertificateResponse:
        """
        This API is used to download a certificate.
        """
        
        kwargs = {}
        kwargs["action"] = "DownloadCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DownloadCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCSR(
            self,
            request: models.ModifyCSRRequest,
            opts: Dict = None,
    ) -> models.ModifyCSRResponse:
        """
        This API is used to modify the information of a CSR.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCSR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCSRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCertificateAlias(
            self,
            request: models.ModifyCertificateAliasRequest,
            opts: Dict = None,
    ) -> models.ModifyCertificateAliasResponse:
        """
        This API is used to modify a certificate alias by passing in the certificate ID and new alias.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCertificateAlias"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCertificateAliasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCertificateProject(
            self,
            request: models.ModifyCertificateProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyCertificateProjectResponse:
        """
        This API is used to modify the projects of multiple certificates.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCertificateProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCertificateProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCertificateResubmit(
            self,
            request: models.ModifyCertificateResubmitRequest,
            opts: Dict = None,
    ) -> models.ModifyCertificateResubmitResponse:
        """
        This API is used to re-submit a review application for a paid certificate whose review failed or was canceled.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCertificateResubmit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCertificateResubmitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCertificatesExpiringNotificationSwitch(
            self,
            request: models.ModifyCertificatesExpiringNotificationSwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyCertificatesExpiringNotificationSwitchResponse:
        """
        Modify to ignore certificate expiration notifications. Enable or disable certificate expiration notifications.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCertificatesExpiringNotificationSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCertificatesExpiringNotificationSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceCertificate(
            self,
            request: models.ReplaceCertificateRequest,
            opts: Dict = None,
    ) -> models.ReplaceCertificateResponse:
        """
        This API is used to reissue a certificate. Note that if you have applied for a free certificate, only an RSA-2048 certificate will be reissued, and the certificate can be reissued only once.
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitCertificateInformation(
            self,
            request: models.SubmitCertificateInformationRequest,
            opts: Dict = None,
    ) -> models.SubmitCertificateInformationResponse:
        """
        Submit documentation for paid certificates; This API does not maintain new features, and you can use the new API to submit documentation. [CertificateInfoSubmit](https://intl.cloud.tencent.com/document/product/400/116033?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitCertificateInformation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitCertificateInformationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCertificateInstance(
            self,
            request: models.UpdateCertificateInstanceRequest,
            opts: Dict = None,
    ) -> models.UpdateCertificateInstanceResponse:
        """
        This API is used to one-click update old certificate resources. This API is asynchronous. After calling it, if DeployRecordId is 0, it means the task is in progress. Repeat the request to this API. When the returned DeployRecordId is greater than 0, it means the task creation is successful. If it is not created successfully, an exception will be thrown.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCertificateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCertificateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCertificateRecordRetry(
            self,
            request: models.UpdateCertificateRecordRetryRequest,
            opts: Dict = None,
    ) -> models.UpdateCertificateRecordRetryResponse:
        """
        Cloud resource update deployment retry record
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCertificateRecordRetry"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCertificateRecordRetryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCertificateRecordRollback(
            self,
            request: models.UpdateCertificateRecordRollbackRequest,
            opts: Dict = None,
    ) -> models.UpdateCertificateRecordRollbackResponse:
        """
        Cloud resource update one-click rollback
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCertificateRecordRollback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCertificateRecordRollbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadCertificate(
            self,
            request: models.UploadCertificateRequest,
            opts: Dict = None,
    ) -> models.UploadCertificateResponse:
        """
        This API is used to upload a certificate.
        """
        
        kwargs = {}
        kwargs["action"] = "UploadCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadConfirmLetter(
            self,
            request: models.UploadConfirmLetterRequest,
            opts: Dict = None,
    ) -> models.UploadConfirmLetterResponse:
        """
        This API is used to upload the confirmation letter for a certificate.
        """
        
        kwargs = {}
        kwargs["action"] = "UploadConfirmLetter"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadConfirmLetterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadUpdateCertificateInstance(
            self,
            request: models.UploadUpdateCertificateInstanceRequest,
            opts: Dict = None,
    ) -> models.UploadUpdateCertificateInstanceResponse:
        """
        This API is used to update certificate content (certificate ID unchanged) and update associated Tencent Cloud resources. This is an asynchronous API. After calling, a DeployRecordId of 0 indicates that the task is in progress. Repeatedly request this API, and when DeployRecordId is greater than 0, it means the task has been successfully created. If the task is not successfully created, an exception will be thrown.
        """
        
        kwargs = {}
        kwargs["action"] = "UploadUpdateCertificateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadUpdateCertificateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadUpdateCertificateRecordRetry(
            self,
            request: models.UploadUpdateCertificateRecordRetryRequest,
            opts: Dict = None,
    ) -> models.UploadUpdateCertificateRecordRetryResponse:
        """
        Cloud Resource Update (Certificate ID Unchanged) Deployment Retry Record.
        """
        
        kwargs = {}
        kwargs["action"] = "UploadUpdateCertificateRecordRetry"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadUpdateCertificateRecordRetryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadUpdateCertificateRecordRollback(
            self,
            request: models.UploadUpdateCertificateRecordRollbackRequest,
            opts: Dict = None,
    ) -> models.UploadUpdateCertificateRecordRollbackResponse:
        """
        This API is used to roll back the full task when cloud resource update succeeds with unchanged certificate ID.
        """
        
        kwargs = {}
        kwargs["action"] = "UploadUpdateCertificateRecordRollback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadUpdateCertificateRecordRollbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)