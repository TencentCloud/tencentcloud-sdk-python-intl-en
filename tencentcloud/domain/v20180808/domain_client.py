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
from tencentcloud.domain.v20180808 import models


class DomainClient(AbstractClient):
    _apiVersion = '2018-08-08'
    _endpoint = 'domain.intl.tencentcloudapi.com'
    _service = 'domain'


    def BatchModifyIntlDomainDNS(self, request):
        """This API is used to bulk modify DNS servers for domains.

        :param request: Request instance for BatchModifyIntlDomainDNS.
        :type request: :class:`tencentcloud.domain.v20180808.models.BatchModifyIntlDomainDNSRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.BatchModifyIntlDomainDNSResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchModifyIntlDomainDNS", params, headers=headers)
            response = json.loads(body)
            model = models.BatchModifyIntlDomainDNSResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchModifyIntlDomainInfo(self, request):
        """This API is used to bulk modify registrant information.

        :param request: Request instance for BatchModifyIntlDomainInfo.
        :type request: :class:`tencentcloud.domain.v20180808.models.BatchModifyIntlDomainInfoRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.BatchModifyIntlDomainInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchModifyIntlDomainInfo", params, headers=headers)
            response = json.loads(body)
            model = models.BatchModifyIntlDomainInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckIntlDomainNew(self, request):
        """This API is used to check whether a domain is available for registration.

        :param request: Request instance for CheckIntlDomainNew.
        :type request: :class:`tencentcloud.domain.v20180808.models.CheckIntlDomainNewRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.CheckIntlDomainNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckIntlDomainNew", params, headers=headers)
            response = json.loads(body)
            model = models.CheckIntlDomainNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIntlDomainBatch(self, request):
        """This API is used to bulk register domains.

        :param request: Request instance for CreateIntlDomainBatch.
        :type request: :class:`tencentcloud.domain.v20180808.models.CreateIntlDomainBatchRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.CreateIntlDomainBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIntlDomainBatch", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIntlDomainBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIntlPhoneEmail(self, request):
        """This API is used to verify a mobile number or an email address via a verification code.

        :param request: Request instance for CreateIntlPhoneEmail.
        :type request: :class:`tencentcloud.domain.v20180808.models.CreateIntlPhoneEmailRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.CreateIntlPhoneEmailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIntlPhoneEmail", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIntlPhoneEmailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIntlTemplate(self, request):
        """This API is used to add a registrant profile.

        :param request: Request instance for CreateIntlTemplate.
        :type request: :class:`tencentcloud.domain.v20180808.models.CreateIntlTemplateRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.CreateIntlTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIntlTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIntlTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIntlPhoneEmail(self, request):
        """This API is used to delete a mobile number or an email address.

        :param request: Request instance for DeleteIntlPhoneEmail.
        :type request: :class:`tencentcloud.domain.v20180808.models.DeleteIntlPhoneEmailRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DeleteIntlPhoneEmailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIntlPhoneEmail", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIntlPhoneEmailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIntlTemplate(self, request):
        """This API is used to delete a registrant profile.

        :param request: Request instance for DeleteIntlTemplate.
        :type request: :class:`tencentcloud.domain.v20180808.models.DeleteIntlTemplateRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DeleteIntlTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIntlTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIntlTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntlBatchDetailStatus(self, request):
        """This API is used to query the status of a bulk task.

        :param request: Request instance for DescribeIntlBatchDetailStatus.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeIntlBatchDetailStatusRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeIntlBatchDetailStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntlBatchDetailStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntlBatchDetailStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntlBatchOperationLogs(self, request):
        """This API is used to query the logs of bulk domain purchase.

        :param request: Request instance for DescribeIntlBatchOperationLogs.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeIntlBatchOperationLogsRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeIntlBatchOperationLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntlBatchOperationLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntlBatchOperationLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntlDomain(self, request):
        """This API is used to query domain information.

        :param request: Request instance for DescribeIntlDomain.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeIntlDomainRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeIntlDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntlDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntlDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntlDomainBatchDetails(self, request):
        """This API is used to get the log details of bulk domain purchase.

        :param request: Request instance for DescribeIntlDomainBatchDetails.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeIntlDomainBatchDetailsRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeIntlDomainBatchDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntlDomainBatchDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntlDomainBatchDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntlDomainList(self, request):
        """This API is used to query the "My domains" list.

        :param request: Request instance for DescribeIntlDomainList.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeIntlDomainListRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeIntlDomainListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntlDomainList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntlDomainListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntlDomainPriceNewList(self, request):
        """This API is used to get the price list by domain suffix.

        :param request: Request instance for DescribeIntlDomainPriceNewList.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeIntlDomainPriceNewListRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeIntlDomainPriceNewListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntlDomainPriceNewList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntlDomainPriceNewListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntlPhoneEmailList(self, request):
        """This API is used to get the list of verified mobile numbers and email addresses.

        :param request: Request instance for DescribeIntlPhoneEmailList.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeIntlPhoneEmailListRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeIntlPhoneEmailListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntlPhoneEmailList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntlPhoneEmailListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntlTemplate(self, request):
        """This API is used to get the details of a registrant profile.

        :param request: Request instance for DescribeIntlTemplate.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeIntlTemplateRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeIntlTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntlTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntlTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntlTemplateList(self, request):
        """This API is used to get the list of registrant profiles.

        :param request: Request instance for DescribeIntlTemplateList.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeIntlTemplateListRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeIntlTemplateListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntlTemplateList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntlTemplateListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyOwnerIntlBatch(self, request):
        """This API is used to bulk transfer domains to another account.

        :param request: Request instance for ModifyOwnerIntlBatch.
        :type request: :class:`tencentcloud.domain.v20180808.models.ModifyOwnerIntlBatchRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.ModifyOwnerIntlBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOwnerIntlBatch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyOwnerIntlBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewIntlDomainBatch(self, request):
        """This API is used to bulk renew domains.

        :param request: Request instance for RenewIntlDomainBatch.
        :type request: :class:`tencentcloud.domain.v20180808.models.RenewIntlDomainBatchRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.RenewIntlDomainBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewIntlDomainBatch", params, headers=headers)
            response = json.loads(body)
            model = models.RenewIntlDomainBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SendIntlPhoneEmailCode(self, request):
        """This API is used to send a verification code to a mobile number or an email address.

        :param request: Request instance for SendIntlPhoneEmailCode.
        :type request: :class:`tencentcloud.domain.v20180808.models.SendIntlPhoneEmailCodeRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.SendIntlPhoneEmailCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendIntlPhoneEmailCode", params, headers=headers)
            response = json.loads(body)
            model = models.SendIntlPhoneEmailCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetIntlDomainAutoRenew(self, request):
        """This API is used to set auto-renewal.

        :param request: Request instance for SetIntlDomainAutoRenew.
        :type request: :class:`tencentcloud.domain.v20180808.models.SetIntlDomainAutoRenewRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.SetIntlDomainAutoRenewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetIntlDomainAutoRenew", params, headers=headers)
            response = json.loads(body)
            model = models.SetIntlDomainAutoRenewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TransferInIntlDomainBatch(self, request):
        """This API is used to bulk transfer domains in.

        :param request: Request instance for TransferInIntlDomainBatch.
        :type request: :class:`tencentcloud.domain.v20180808.models.TransferInIntlDomainBatchRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.TransferInIntlDomainBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TransferInIntlDomainBatch", params, headers=headers)
            response = json.loads(body)
            model = models.TransferInIntlDomainBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TransferProhibitionIntlBatch(self, request):
        """This API is used to bulk set transfer prohibition for domains.

        :param request: Request instance for TransferProhibitionIntlBatch.
        :type request: :class:`tencentcloud.domain.v20180808.models.TransferProhibitionIntlBatchRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.TransferProhibitionIntlBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TransferProhibitionIntlBatch", params, headers=headers)
            response = json.loads(body)
            model = models.TransferProhibitionIntlBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateProhibitionIntlBatch(self, request):
        """This API is used to bulk set update prohibition for domains.

        :param request: Request instance for UpdateProhibitionIntlBatch.
        :type request: :class:`tencentcloud.domain.v20180808.models.UpdateProhibitionIntlBatchRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.UpdateProhibitionIntlBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateProhibitionIntlBatch", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateProhibitionIntlBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))