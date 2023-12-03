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
from tencentcloud.ssl.v20191205 import models


class SslClient(AbstractClient):
    _apiVersion = '2019-12-05'
    _endpoint = 'ssl.tencentcloudapi.com'
    _service = 'ssl'


    def ApplyCertificate(self, request):
        """This API is used to apply for a free certificate.

        :param request: Request instance for ApplyCertificate.
        :type request: :class:`tencentcloud.ssl.v20191205.models.ApplyCertificateRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.ApplyCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchDeleteCSR(self, request):
        """This API is used to batch delete CSRs.

        :param request: Request instance for BatchDeleteCSR.
        :type request: :class:`tencentcloud.ssl.v20191205.models.BatchDeleteCSRRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.BatchDeleteCSRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeleteCSR", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeleteCSRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelAuditCertificate(self, request):
        """This API is used to cancel certificate review.

        :param request: Request instance for CancelAuditCertificate.
        :type request: :class:`tencentcloud.ssl.v20191205.models.CancelAuditCertificateRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.CancelAuditCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelAuditCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.CancelAuditCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelCertificateOrder(self, request):
        """This API is used to cancel a certificate order.

        :param request: Request instance for CancelCertificateOrder.
        :type request: :class:`tencentcloud.ssl.v20191205.models.CancelCertificateOrderRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.CancelCertificateOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelCertificateOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CancelCertificateOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CommitCertificateInformation(self, request):
        """This API is used to submit a certificate order.

        :param request: Request instance for CommitCertificateInformation.
        :type request: :class:`tencentcloud.ssl.v20191205.models.CommitCertificateInformationRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.CommitCertificateInformationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CommitCertificateInformation", params, headers=headers)
            response = json.loads(body)
            model = models.CommitCertificateInformationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCSR(self, request):
        """This API is used to create a CSR.

        :param request: Request instance for CreateCSR.
        :type request: :class:`tencentcloud.ssl.v20191205.models.CreateCSRRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.CreateCSRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCSR", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCSRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCertificate(self, request):
        """This API is used to purchase a certificate.

        :param request: Request instance for CreateCertificate.
        :type request: :class:`tencentcloud.ssl.v20191205.models.CreateCertificateRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.CreateCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCertificateBindResourceSyncTask(self, request):
        """This API is used to create an async task for querying the cloud resources associated with a certificate. If such a task already exists under the certificate ID, the ID of this task is returned as the result. The following types of cloud resources are supported: CLB, CDN, WAF, LIVE, VOD, DDOS, TKE, APIGATEWAY, TCB, and TEO (EDGEONE). You can query the result of this task using the `DescribeCertificateBindResourceTaskResult` API.

        :param request: Request instance for CreateCertificateBindResourceSyncTask.
        :type request: :class:`tencentcloud.ssl.v20191205.models.CreateCertificateBindResourceSyncTaskRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.CreateCertificateBindResourceSyncTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCertificateBindResourceSyncTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCertificateBindResourceSyncTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCertificate(self, request):
        """This API is used to delete a certificate.

        :param request: Request instance for DeleteCertificate.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DeleteCertificateRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DeleteCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCSR(self, request):
        """This API is used to query the details of a CSR.

        :param request: Request instance for DescribeCSR.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeCSRRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeCSRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCSR", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCSRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCSRSet(self, request):
        """This API is used to query the CSR list.

        :param request: Request instance for DescribeCSRSet.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeCSRSetRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeCSRSetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCSRSet", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCSRSetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCertificate(self, request):
        """This API is used to get certificate information.

        :param request: Request instance for DescribeCertificate.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificateRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCertificateBindResourceTaskDetail(self, request):
        """This API is used to query the result of an async task created with `CreateCertificateBindResourceSyncTask` to query cloud resources associated with a certificate. The following types of cloud resources are supported: CLB, CDN, WAF, LIVE, VOD, DDOS, TKE, APIGATEWAY, TCB, and TEO (EDGEONE).

        :param request: Request instance for DescribeCertificateBindResourceTaskDetail.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificateBindResourceTaskDetailRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificateBindResourceTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCertificateBindResourceTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCertificateBindResourceTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCertificateBindResourceTaskResult(self, request):
        """This API is used to query the result of an async task created with `CreateCertificateBindResourceSyncTask` to query cloud resources associated with a certificate. The following types of cloud resources are supported: CLB, CDN, WAF, LIVE, VOD, DDOS, TKE, APIGATEWAY, TCB, and TEO (EDGEONE).

        :param request: Request instance for DescribeCertificateBindResourceTaskResult.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificateBindResourceTaskResultRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificateBindResourceTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCertificateBindResourceTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCertificateBindResourceTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCertificateDetail(self, request):
        """This API is used to get certificate details.

        :param request: Request instance for DescribeCertificateDetail.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificateDetailRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificateDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCertificateDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCertificateDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCertificateOperateLogs(self, request):
        """This API is used to get certificate operation logs in the current account.

        :param request: Request instance for DescribeCertificateOperateLogs.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificateOperateLogsRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificateOperateLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCertificateOperateLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCertificateOperateLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCertificates(self, request):
        """This API is used to get the certificate list.

        :param request: Request instance for DescribeCertificates.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificatesRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCertificates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCertificatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostTeoInstanceList(self, request):
        """This API is used to query the list of EDGEONE instances to which a certificate can be deployed.

        :param request: Request instance for DescribeHostTeoInstanceList.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeHostTeoInstanceListRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeHostTeoInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostTeoInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostTeoInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostUpdateRecord(self, request):
        """Query certificate cloud resource update record list

        :param request: Request instance for DescribeHostUpdateRecord.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeHostUpdateRecordRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeHostUpdateRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostUpdateRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostUpdateRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostUpdateRecordDetail(self, request):
        """Query certificate cloud resource update record details list

        :param request: Request instance for DescribeHostUpdateRecordDetail.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeHostUpdateRecordDetailRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeHostUpdateRecordDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostUpdateRecordDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostUpdateRecordDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DownloadCertificate(self, request):
        """This API is used to download a certificate.

        :param request: Request instance for DownloadCertificate.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DownloadCertificateRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DownloadCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCSR(self, request):
        """This API is used to modify the information of a CSR.

        :param request: Request instance for ModifyCSR.
        :type request: :class:`tencentcloud.ssl.v20191205.models.ModifyCSRRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.ModifyCSRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCSR", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCSRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCertificateAlias(self, request):
        """This API is used to modify a certificate alias by passing in the certificate ID and new alias.

        :param request: Request instance for ModifyCertificateAlias.
        :type request: :class:`tencentcloud.ssl.v20191205.models.ModifyCertificateAliasRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.ModifyCertificateAliasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCertificateAlias", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCertificateAliasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCertificateProject(self, request):
        """This API is used to modify the projects of multiple certificates.

        :param request: Request instance for ModifyCertificateProject.
        :type request: :class:`tencentcloud.ssl.v20191205.models.ModifyCertificateProjectRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.ModifyCertificateProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCertificateProject", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCertificateProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCertificateResubmit(self, request):
        """This API is used to re-submit a review application for a paid certificate whose review failed or was canceled.

        :param request: Request instance for ModifyCertificateResubmit.
        :type request: :class:`tencentcloud.ssl.v20191205.models.ModifyCertificateResubmitRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.ModifyCertificateResubmitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCertificateResubmit", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCertificateResubmitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReplaceCertificate(self, request):
        """This API is used to reissue a certificate. Note that if you have applied for a free certificate, only an RSA-2048 certificate will be reissued, and the certificate can be reissued only once.

        :param request: Request instance for ReplaceCertificate.
        :type request: :class:`tencentcloud.ssl.v20191205.models.ReplaceCertificateRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.ReplaceCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplaceCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.ReplaceCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitCertificateInformation(self, request):
        """This API is used to submit certificate information.

        :param request: Request instance for SubmitCertificateInformation.
        :type request: :class:`tencentcloud.ssl.v20191205.models.SubmitCertificateInformationRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.SubmitCertificateInformationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitCertificateInformation", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitCertificateInformationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCertificateInstance(self, request):
        """This API is used to update old certificate resources with one click and is an asynchronous interface. After this API is called, the returned DeployRecordId being 0 indicates that the task is in progress, and the returned DeployRecordId being greater than 0 indicates that the task is successfully created. If the creation fails, an exception is returned.

        :param request: Request instance for UpdateCertificateInstance.
        :type request: :class:`tencentcloud.ssl.v20191205.models.UpdateCertificateInstanceRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.UpdateCertificateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCertificateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCertificateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCertificateRecordRetry(self, request):
        """Cloud resource update deployment retry record

        :param request: Request instance for UpdateCertificateRecordRetry.
        :type request: :class:`tencentcloud.ssl.v20191205.models.UpdateCertificateRecordRetryRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.UpdateCertificateRecordRetryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCertificateRecordRetry", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCertificateRecordRetryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCertificateRecordRollback(self, request):
        """Cloud resource update one-click rollback

        :param request: Request instance for UpdateCertificateRecordRollback.
        :type request: :class:`tencentcloud.ssl.v20191205.models.UpdateCertificateRecordRollbackRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.UpdateCertificateRecordRollbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCertificateRecordRollback", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCertificateRecordRollbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadCertificate(self, request):
        """This API is used to upload a certificate.

        :param request: Request instance for UploadCertificate.
        :type request: :class:`tencentcloud.ssl.v20191205.models.UploadCertificateRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.UploadCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.UploadCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadConfirmLetter(self, request):
        """This API is used to upload the confirmation letter for a certificate.

        :param request: Request instance for UploadConfirmLetter.
        :type request: :class:`tencentcloud.ssl.v20191205.models.UploadConfirmLetterRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.UploadConfirmLetterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadConfirmLetter", params, headers=headers)
            response = json.loads(body)
            model = models.UploadConfirmLetterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))