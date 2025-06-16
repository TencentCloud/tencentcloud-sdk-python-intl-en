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
from tencentcloud.lke.v20231130 import models


class LkeClient(AbstractClient):
    _apiVersion = '2023-11-30'
    _endpoint = 'lke.intl.tencentcloudapi.com'
    _service = 'lke'


    def CheckAttributeLabelExist(self, request):
        """This API is used to check if the label name under an attribute exist.

        :param request: Request instance for CheckAttributeLabelExist.
        :type request: :class:`tencentcloud.lke.v20231130.models.CheckAttributeLabelExistRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.CheckAttributeLabelExistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckAttributeLabelExist", params, headers=headers)
            response = json.loads(body)
            model = models.CheckAttributeLabelExistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckAttributeLabelRefer(self, request):
        """This API is used to check attribute label references.

        :param request: Request instance for CheckAttributeLabelRefer.
        :type request: :class:`tencentcloud.lke.v20231130.models.CheckAttributeLabelReferRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.CheckAttributeLabelReferResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckAttributeLabelRefer", params, headers=headers)
            response = json.loads(body)
            model = models.CheckAttributeLabelReferResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApp(self, request):
        """This API is used to create knowledge engine applications.

        :param request: Request instance for CreateApp.
        :type request: :class:`tencentcloud.lke.v20231130.models.CreateAppRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.CreateAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAttributeLabel(self, request):
        """This API is used to create attributes.

        :param request: Request instance for CreateAttributeLabel.
        :type request: :class:`tencentcloud.lke.v20231130.models.CreateAttributeLabelRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.CreateAttributeLabelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAttributeLabel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAttributeLabelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCorp(self, request):
        """This API is used to create enterprises.

        :param request: Request instance for CreateCorp.
        :type request: :class:`tencentcloud.lke.v20231130.models.CreateCorpRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.CreateCorpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCorp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCorpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDocCate(self, request):
        """This API is used to create doc categories.

        :param request: Request instance for CreateDocCate.
        :type request: :class:`tencentcloud.lke.v20231130.models.CreateDocCateRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.CreateDocCateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDocCate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDocCateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateQA(self, request):
        """This API is used to enter Q&As.

        :param request: Request instance for CreateQA.
        :type request: :class:`tencentcloud.lke.v20231130.models.CreateQARequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.CreateQAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateQA", params, headers=headers)
            response = json.loads(body)
            model = models.CreateQAResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateQACate(self, request):
        """This API is used to create Q&A categories.

        :param request: Request instance for CreateQACate.
        :type request: :class:`tencentcloud.lke.v20231130.models.CreateQACateRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.CreateQACateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateQACate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateQACateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateReconstructDocumentFlow(self, request):
        """This API is used to initiate requests for this asynchronous API, for initiating document parsing tasks.
        Document parsing supports converting images or PDF files into Markdown format files, and can parse content elements including tables, formulas, images, headings, paragraphs, headers, and footers, and intelligently convert the content into reading order.
        During the trial period, the QPS limit for a single account is only 1. If you need to access officially, please contact our R&D team.

        :param request: Request instance for CreateReconstructDocumentFlow.
        :type request: :class:`tencentcloud.lke.v20231130.models.CreateReconstructDocumentFlowRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.CreateReconstructDocumentFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReconstructDocumentFlow", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReconstructDocumentFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRejectedQuestion(self, request):
        """This API is used to create rejected questions.

        :param request: Request instance for CreateRejectedQuestion.
        :type request: :class:`tencentcloud.lke.v20231130.models.CreateRejectedQuestionRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.CreateRejectedQuestionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRejectedQuestion", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRejectedQuestionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRelease(self, request):
        """This API is used to create a release.

        :param request: Request instance for CreateRelease.
        :type request: :class:`tencentcloud.lke.v20231130.models.CreateReleaseRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.CreateReleaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRelease", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReleaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApp(self, request):
        """This API is used to delete applications.

        :param request: Request instance for DeleteApp.
        :type request: :class:`tencentcloud.lke.v20231130.models.DeleteAppRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DeleteAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApp", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAttributeLabel(self, request):
        """This API is used to delete attribute labels.

        :param request: Request instance for DeleteAttributeLabel.
        :type request: :class:`tencentcloud.lke.v20231130.models.DeleteAttributeLabelRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DeleteAttributeLabelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAttributeLabel", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAttributeLabelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDoc(self, request):
        """This API is used to delete documents.

        :param request: Request instance for DeleteDoc.
        :type request: :class:`tencentcloud.lke.v20231130.models.DeleteDocRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DeleteDocResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDoc", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDocResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDocCate(self, request):
        """This API is used to delete Doc categories.

        :param request: Request instance for DeleteDocCate.
        :type request: :class:`tencentcloud.lke.v20231130.models.DeleteDocCateRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DeleteDocCateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDocCate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDocCateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteQA(self, request):
        """This API is used to delete Q&As.

        :param request: Request instance for DeleteQA.
        :type request: :class:`tencentcloud.lke.v20231130.models.DeleteQARequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DeleteQAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteQA", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteQAResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteQACate(self, request):
        """This API is used to delete categories.

        :param request: Request instance for DeleteQACate.
        :type request: :class:`tencentcloud.lke.v20231130.models.DeleteQACateRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DeleteQACateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteQACate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteQACateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRejectedQuestion(self, request):
        """This API is used to delete rejected questions.

        :param request: Request instance for DeleteRejectedQuestion.
        :type request: :class:`tencentcloud.lke.v20231130.models.DeleteRejectedQuestionRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DeleteRejectedQuestionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRejectedQuestion", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRejectedQuestionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApp(self, request):
        """This API is used to obtain application details under the corporate.

        :param request: Request instance for DescribeApp.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeAppRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApp", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAttributeLabel(self, request):
        """This API is used to query attribute label details.

        :param request: Request instance for DescribeAttributeLabel.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeAttributeLabelRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeAttributeLabelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttributeLabel", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttributeLabelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCallStatsGraph(self, request):
        """This API is used to show line chart of API calls.

        :param request: Request instance for DescribeCallStatsGraph.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeCallStatsGraphRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeCallStatsGraphResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCallStatsGraph", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCallStatsGraphResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConcurrencyUsage(self, request):
        """This API is used to response to concurrent calls.

        :param request: Request instance for DescribeConcurrencyUsage.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeConcurrencyUsageRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeConcurrencyUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConcurrencyUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConcurrencyUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConcurrencyUsageGraph(self, request):
        """This API is used to show line chart of concurrent calls.

        :param request: Request instance for DescribeConcurrencyUsageGraph.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeConcurrencyUsageGraphRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeConcurrencyUsageGraphResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConcurrencyUsageGraph", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConcurrencyUsageGraphResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCorp(self, request):
        """This API is used to query corporate details.

        :param request: Request instance for DescribeCorp.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeCorpRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeCorpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCorp", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCorpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDoc(self, request):
        """This API is used to query document details.

        :param request: Request instance for DescribeDoc.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeDocRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeDocResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDoc", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDocResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKnowledgeUsage(self, request):
        """This API is used to query the knowledge library usage.

        :param request: Request instance for DescribeKnowledgeUsage.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeKnowledgeUsageRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeKnowledgeUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKnowledgeUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKnowledgeUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKnowledgeUsagePieGraph(self, request):
        """This API is used to query pie chart of the enterprise knowledge base capacity .

        :param request: Request instance for DescribeKnowledgeUsagePieGraph.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeKnowledgeUsagePieGraphRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeKnowledgeUsagePieGraphResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKnowledgeUsagePieGraph", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKnowledgeUsagePieGraphResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQA(self, request):
        """This API is used to query Q&A details.

        :param request: Request instance for DescribeQA.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeQARequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeQAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQA", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQAResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRefer(self, request):
        """This API is used to get the reference source details list.

        :param request: Request instance for DescribeRefer.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeReferRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeReferResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRefer", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReferResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRelease(self, request):
        """This API is used to query release details.

        :param request: Request instance for DescribeRelease.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeReleaseRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeReleaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRelease", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReleaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReleaseInfo(self, request):
        """This API is used to pull the release button status and last release time.

        :param request: Request instance for DescribeReleaseInfo.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeReleaseInfoRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeReleaseInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReleaseInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReleaseInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRobotBizIDByAppKey(self, request):
        """This API is used to get application business ID through appKey.

        :param request: Request instance for DescribeRobotBizIDByAppKey.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeRobotBizIDByAppKeyRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeRobotBizIDByAppKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRobotBizIDByAppKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRobotBizIDByAppKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSearchStatsGraph(self, request):
        """This API is used to query line chart of search service calls.

        :param request: Request instance for DescribeSearchStatsGraph.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeSearchStatsGraphRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeSearchStatsGraphResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSearchStatsGraph", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSearchStatsGraphResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSegments(self, request):
        """This API is used to get fragment details.

        :param request: Request instance for DescribeSegments.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeSegmentsRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeSegmentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSegments", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSegmentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStorageCredential(self, request):
        """This API is used to get the temporary key for file upload.

        :param request: Request instance for DescribeStorageCredential.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeStorageCredentialRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeStorageCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStorageCredential", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStorageCredentialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTokenUsage(self, request):
        """This API is used to query API call token details.

        :param request: Request instance for DescribeTokenUsage.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeTokenUsageRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeTokenUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTokenUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTokenUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTokenUsageGraph(self, request):
        """This API is used to show API call token line chart.

        :param request: Request instance for DescribeTokenUsageGraph.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeTokenUsageGraphRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeTokenUsageGraphResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTokenUsageGraph", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTokenUsageGraphResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUnsatisfiedReplyContext(self, request):
        """This API is used to get the context of dissatisfied responses.

        :param request: Request instance for DescribeUnsatisfiedReplyContext.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeUnsatisfiedReplyContextRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeUnsatisfiedReplyContextResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUnsatisfiedReplyContext", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUnsatisfiedReplyContextResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAttributeLabel(self, request):
        """This API is used to export attribute labels.

        :param request: Request instance for ExportAttributeLabel.
        :type request: :class:`tencentcloud.lke.v20231130.models.ExportAttributeLabelRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ExportAttributeLabelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAttributeLabel", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAttributeLabelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportQAList(self, request):
        """This API is used to export Q&A list.

        :param request: Request instance for ExportQAList.
        :type request: :class:`tencentcloud.lke.v20231130.models.ExportQAListRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ExportQAListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportQAList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportQAListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportUnsatisfiedReply(self, request):
        """This API is used to export dissatisfied responses.

        :param request: Request instance for ExportUnsatisfiedReply.
        :type request: :class:`tencentcloud.lke.v20231130.models.ExportUnsatisfiedReplyRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ExportUnsatisfiedReplyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportUnsatisfiedReply", params, headers=headers)
            response = json.loads(body)
            model = models.ExportUnsatisfiedReplyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GenerateQA(self, request):
        """This API is used to generate Q%A from document.

        :param request: Request instance for GenerateQA.
        :type request: :class:`tencentcloud.lke.v20231130.models.GenerateQARequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.GenerateQAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenerateQA", params, headers=headers)
            response = json.loads(body)
            model = models.GenerateQAResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAnswerTypeDataCount(self, request):
        """This API is used to get response type data statistics.

        :param request: Request instance for GetAnswerTypeDataCount.
        :type request: :class:`tencentcloud.lke.v20231130.models.GetAnswerTypeDataCountRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.GetAnswerTypeDataCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAnswerTypeDataCount", params, headers=headers)
            response = json.loads(body)
            model = models.GetAnswerTypeDataCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAppKnowledgeCount(self, request):
        """This API is used to get a model list.

        :param request: Request instance for GetAppKnowledgeCount.
        :type request: :class:`tencentcloud.lke.v20231130.models.GetAppKnowledgeCountRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.GetAppKnowledgeCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAppKnowledgeCount", params, headers=headers)
            response = json.loads(body)
            model = models.GetAppKnowledgeCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAppSecret(self, request):
        """This API is used to get application secret keys.

        :param request: Request instance for GetAppSecret.
        :type request: :class:`tencentcloud.lke.v20231130.models.GetAppSecretRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.GetAppSecretResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAppSecret", params, headers=headers)
            response = json.loads(body)
            model = models.GetAppSecretResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDocPreview(self, request):
        """This API is used to get document preview information.

        :param request: Request instance for GetDocPreview.
        :type request: :class:`tencentcloud.lke.v20231130.models.GetDocPreviewRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.GetDocPreviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDocPreview", params, headers=headers)
            response = json.loads(body)
            model = models.GetDocPreviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetLikeDataCount(self, request):
        """This API is used to get likes and dislikes data statistics.

        :param request: Request instance for GetLikeDataCount.
        :type request: :class:`tencentcloud.lke.v20231130.models.GetLikeDataCountRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.GetLikeDataCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetLikeDataCount", params, headers=headers)
            response = json.loads(body)
            model = models.GetLikeDataCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetMsgRecord(self, request):
        """This API is used to obtain chat history based on the session ID (only historical session data within the past 180 days will be retained).

        :param request: Request instance for GetMsgRecord.
        :type request: :class:`tencentcloud.lke.v20231130.models.GetMsgRecordRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.GetMsgRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetMsgRecord", params, headers=headers)
            response = json.loads(body)
            model = models.GetMsgRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetReconstructDocumentResult(self, request):
        """This is an asynchronous APIs, used to get document parsing task results.

        :param request: Request instance for GetReconstructDocumentResult.
        :type request: :class:`tencentcloud.lke.v20231130.models.GetReconstructDocumentResultRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.GetReconstructDocumentResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetReconstructDocumentResult", params, headers=headers)
            response = json.loads(body)
            model = models.GetReconstructDocumentResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTaskStatus(self, request):
        """This API is used to get the task status.

        :param request: Request instance for GetTaskStatus.
        :type request: :class:`tencentcloud.lke.v20231130.models.GetTaskStatusRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.GetTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.GetTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetWsToken(self, request):
        """This API is used to get ws token.

        :param request: Request instance for GetWsToken.
        :type request: :class:`tencentcloud.lke.v20231130.models.GetWsTokenRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.GetWsTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetWsToken", params, headers=headers)
            response = json.loads(body)
            model = models.GetWsTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GroupDoc(self, request):
        """DocGroup.

        :param request: Request instance for GroupDoc.
        :type request: :class:`tencentcloud.lke.v20231130.models.GroupDocRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.GroupDocResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GroupDoc", params, headers=headers)
            response = json.loads(body)
            model = models.GroupDocResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GroupQA(self, request):
        """Q&A Group.

        :param request: Request instance for GroupQA.
        :type request: :class:`tencentcloud.lke.v20231130.models.GroupQARequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.GroupQAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GroupQA", params, headers=headers)
            response = json.loads(body)
            model = models.GroupQAResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IgnoreUnsatisfiedReply(self, request):
        """This API is used to ignore dissatisfied responses.

        :param request: Request instance for IgnoreUnsatisfiedReply.
        :type request: :class:`tencentcloud.lke.v20231130.models.IgnoreUnsatisfiedReplyRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.IgnoreUnsatisfiedReplyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IgnoreUnsatisfiedReply", params, headers=headers)
            response = json.loads(body)
            model = models.IgnoreUnsatisfiedReplyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListApp(self, request):
        """This API is used to get the application list under the corporate.

        :param request: Request instance for ListApp.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListAppRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListApp", params, headers=headers)
            response = json.loads(body)
            model = models.ListAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAppCategory(self, request):
        """This API is used to get list of application types.

        :param request: Request instance for ListAppCategory.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListAppCategoryRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListAppCategoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAppCategory", params, headers=headers)
            response = json.loads(body)
            model = models.ListAppCategoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAppKnowledgeDetail(self, request):
        """This API is used to query the knowledge base capacity details in a list.

        :param request: Request instance for ListAppKnowledgeDetail.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListAppKnowledgeDetailRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListAppKnowledgeDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAppKnowledgeDetail", params, headers=headers)
            response = json.loads(body)
            model = models.ListAppKnowledgeDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAttributeLabel(self, request):
        """This API is used to query attribute label lists.

        :param request: Request instance for ListAttributeLabel.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListAttributeLabelRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListAttributeLabelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAttributeLabel", params, headers=headers)
            response = json.loads(body)
            model = models.ListAttributeLabelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListDoc(self, request):
        """This API is used to get document list.

        :param request: Request instance for ListDoc.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListDocRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListDocResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDoc", params, headers=headers)
            response = json.loads(body)
            model = models.ListDocResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListDocCate(self, request):
        """This API is used to get document category.

        :param request: Request instance for ListDocCate.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListDocCateRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListDocCateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDocCate", params, headers=headers)
            response = json.loads(body)
            model = models.ListDocCateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListModel(self, request):
        """This API is used to get the model list.

        :param request: Request instance for ListModel.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListModelRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListModel", params, headers=headers)
            response = json.loads(body)
            model = models.ListModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListQA(self, request):
        """This API is used to query Q&A lists.

        :param request: Request instance for ListQA.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListQARequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListQAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListQA", params, headers=headers)
            response = json.loads(body)
            model = models.ListQAResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListQACate(self, request):
        """This API is used to get Q&A categories.

        :param request: Request instance for ListQACate.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListQACateRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListQACateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListQACate", params, headers=headers)
            response = json.loads(body)
            model = models.ListQACateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRejectedQuestion(self, request):
        """This API is used to get rejected questions.

        :param request: Request instance for ListRejectedQuestion.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListRejectedQuestionRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListRejectedQuestionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRejectedQuestion", params, headers=headers)
            response = json.loads(body)
            model = models.ListRejectedQuestionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRejectedQuestionPreview(self, request):
        """This API is used to release a preview of rejected questions.

        :param request: Request instance for ListRejectedQuestionPreview.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListRejectedQuestionPreviewRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListRejectedQuestionPreviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRejectedQuestionPreview", params, headers=headers)
            response = json.loads(body)
            model = models.ListRejectedQuestionPreviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRelease(self, request):
        """This API is used to get the release list.

        :param request: Request instance for ListRelease.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListReleaseRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListReleaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRelease", params, headers=headers)
            response = json.loads(body)
            model = models.ListReleaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListReleaseConfigPreview(self, request):
        """This API is used to preview the release configuration items.

        :param request: Request instance for ListReleaseConfigPreview.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListReleaseConfigPreviewRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListReleaseConfigPreviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListReleaseConfigPreview", params, headers=headers)
            response = json.loads(body)
            model = models.ListReleaseConfigPreviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListReleaseDocPreview(self, request):
        """This API is used to preview released documents.

        :param request: Request instance for ListReleaseDocPreview.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListReleaseDocPreviewRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListReleaseDocPreviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListReleaseDocPreview", params, headers=headers)
            response = json.loads(body)
            model = models.ListReleaseDocPreviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListReleaseQAPreview(self, request):
        """List of documents.

        :param request: Request instance for ListReleaseQAPreview.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListReleaseQAPreviewRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListReleaseQAPreviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListReleaseQAPreview", params, headers=headers)
            response = json.loads(body)
            model = models.ListReleaseQAPreviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListSelectDoc(self, request):
        """This API is used to get account information.

        :param request: Request instance for ListSelectDoc.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListSelectDocRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListSelectDocResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListSelectDoc", params, headers=headers)
            response = json.loads(body)
            model = models.ListSelectDocResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListUnsatisfiedReply(self, request):
        """This API is used to query a list of dissatisfied responses.

        :param request: Request instance for ListUnsatisfiedReply.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListUnsatisfiedReplyRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListUnsatisfiedReplyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListUnsatisfiedReply", params, headers=headers)
            response = json.loads(body)
            model = models.ListUnsatisfiedReplyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListUsageCallDetail(self, request):
        """This API is used to query single call details in a list.

        :param request: Request instance for ListUsageCallDetail.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListUsageCallDetailRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListUsageCallDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListUsageCallDetail", params, headers=headers)
            response = json.loads(body)
            model = models.ListUsageCallDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApp(self, request):
        """This API is used to modify application request structure.

        :param request: Request instance for ModifyApp.
        :type request: :class:`tencentcloud.lke.v20231130.models.ModifyAppRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ModifyAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApp", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAttributeLabel(self, request):
        """This API is used to edit attribute labels.

        :param request: Request instance for ModifyAttributeLabel.
        :type request: :class:`tencentcloud.lke.v20231130.models.ModifyAttributeLabelRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ModifyAttributeLabelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAttributeLabel", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAttributeLabelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDoc(self, request):
        """This API is used to modify documents.

        :param request: Request instance for ModifyDoc.
        :type request: :class:`tencentcloud.lke.v20231130.models.ModifyDocRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ModifyDocResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDoc", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDocResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDocAttrRange(self, request):
        """This API is used to modify applicable scope of the document in batches.

        :param request: Request instance for ModifyDocAttrRange.
        :type request: :class:`tencentcloud.lke.v20231130.models.ModifyDocAttrRangeRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ModifyDocAttrRangeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDocAttrRange", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDocAttrRangeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDocCate(self, request):
        """This API is used to modify Doc categories.

        :param request: Request instance for ModifyDocCate.
        :type request: :class:`tencentcloud.lke.v20231130.models.ModifyDocCateRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ModifyDocCateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDocCate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDocCateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyQA(self, request):
        """This API is used to update Q&As.

        :param request: Request instance for ModifyQA.
        :type request: :class:`tencentcloud.lke.v20231130.models.ModifyQARequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ModifyQAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyQA", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyQAResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyQAAttrRange(self, request):
        """This API is used to modify Q&A applicable scope in batches.

        :param request: Request instance for ModifyQAAttrRange.
        :type request: :class:`tencentcloud.lke.v20231130.models.ModifyQAAttrRangeRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ModifyQAAttrRangeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyQAAttrRange", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyQAAttrRangeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyQACate(self, request):
        """This API is used to modify Q&A categories.

        :param request: Request instance for ModifyQACate.
        :type request: :class:`tencentcloud.lke.v20231130.models.ModifyQACateRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ModifyQACateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyQACate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyQACateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRejectedQuestion(self, request):
        """This API is used to modify rejected questions.

        :param request: Request instance for ModifyRejectedQuestion.
        :type request: :class:`tencentcloud.lke.v20231130.models.ModifyRejectedQuestionRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ModifyRejectedQuestionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRejectedQuestion", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRejectedQuestionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RateMsgRecord(self, request):
        """This API is used to show messages for likes and dislikes.

        :param request: Request instance for RateMsgRecord.
        :type request: :class:`tencentcloud.lke.v20231130.models.RateMsgRecordRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.RateMsgRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RateMsgRecord", params, headers=headers)
            response = json.loads(body)
            model = models.RateMsgRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenameDoc(self, request):
        """This API is used to rename a document.

        :param request: Request instance for RenameDoc.
        :type request: :class:`tencentcloud.lke.v20231130.models.RenameDocRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.RenameDocResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenameDoc", params, headers=headers)
            response = json.loads(body)
            model = models.RenameDocResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RetryDocAudit(self, request):
        """This API is used to retry document parsing.

        :param request: Request instance for RetryDocAudit.
        :type request: :class:`tencentcloud.lke.v20231130.models.RetryDocAuditRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.RetryDocAuditResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RetryDocAudit", params, headers=headers)
            response = json.loads(body)
            model = models.RetryDocAuditResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RetryDocParse(self, request):
        """This API is used to retry document parsing.

        :param request: Request instance for RetryDocParse.
        :type request: :class:`tencentcloud.lke.v20231130.models.RetryDocParseRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.RetryDocParseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RetryDocParse", params, headers=headers)
            response = json.loads(body)
            model = models.RetryDocParseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RetryRelease(self, request):
        """This API is used to retry after release suspension.

        :param request: Request instance for RetryRelease.
        :type request: :class:`tencentcloud.lke.v20231130.models.RetryReleaseRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.RetryReleaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RetryRelease", params, headers=headers)
            response = json.loads(body)
            model = models.RetryReleaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SaveDoc(self, request):
        """This API is used to save a knowledge base document Q&As.
        Three steps to store a file in the knowledge library of the application:
        1. Obtain a temporary key. For more information, see [API Documentation](https://cloud.tencent.com/document/product/1759/105050). Different parameter combinations of the temporary key have different permissions. For more information, see [Tencent Cloud Agent Development Platform/TCADP COS Guide](https://cloud.tencent.com/document/product/1759/116238).
        2. Call the COS storage API provided by Tencent Cloud to store the file in the COS of TCADP. For details, see [COS SDK Overview](https://cloud.tencent.com/document/product/436/6474). Note that the temporary key method is used to operate COS.
        3. Call this API to store the basic information of the file in TCADP.
        For the above steps, see [Documentation](https://cloud.tencent.com/document/product/1759/108903). At the end of the documentation, there is a [code demo](https://cloud.tencent.com/document/product/1759/108903#demo), which can be used as a reference.

        :param request: Request instance for SaveDoc.
        :type request: :class:`tencentcloud.lke.v20231130.models.SaveDocRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.SaveDocResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SaveDoc", params, headers=headers)
            response = json.loads(body)
            model = models.SaveDocResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopDocParse(self, request):
        """This API is used to terminate document parsing.

        :param request: Request instance for StopDocParse.
        :type request: :class:`tencentcloud.lke.v20231130.models.StopDocParseRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.StopDocParseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopDocParse", params, headers=headers)
            response = json.loads(body)
            model = models.StopDocParseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadAttributeLabel(self, request):
        """This API is used to upload and import attribute labels.

        :param request: Request instance for UploadAttributeLabel.
        :type request: :class:`tencentcloud.lke.v20231130.models.UploadAttributeLabelRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.UploadAttributeLabelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadAttributeLabel", params, headers=headers)
            response = json.loads(body)
            model = models.UploadAttributeLabelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VerifyQA(self, request):
        """This API is used to verify Q&A.

        :param request: Request instance for VerifyQA.
        :type request: :class:`tencentcloud.lke.v20231130.models.VerifyQARequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.VerifyQAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifyQA", params, headers=headers)
            response = json.loads(body)
            model = models.VerifyQAResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))