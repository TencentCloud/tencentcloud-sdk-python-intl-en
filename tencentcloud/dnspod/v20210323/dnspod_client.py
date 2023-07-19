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
from tencentcloud.dnspod.v20210323 import models


class DnspodClient(AbstractClient):
    _apiVersion = '2021-03-23'
    _endpoint = 'dnspod.tencentcloudapi.com'
    _service = 'dnspod'


    def CreateDomain(self, request):
        """This API is used to add a domain.

        :param request: Request instance for CreateDomain.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.CreateDomainRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.CreateDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDomainAlias(self, request):
        """This API is used to create a domain alias.

        :param request: Request instance for CreateDomainAlias.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.CreateDomainAliasRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.CreateDomainAliasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDomainAlias", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDomainAliasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDomainBatch(self, request):
        """This API is used to bulk add domains.

        :param request: Request instance for CreateDomainBatch.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.CreateDomainBatchRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.CreateDomainBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDomainBatch", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDomainBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDomainGroup(self, request):
        """This API is used to create a domain group.

        :param request: Request instance for CreateDomainGroup.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.CreateDomainGroupRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.CreateDomainGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDomainGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDomainGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRecord(self, request):
        """This API is used to add a record.

        :param request: Request instance for CreateRecord.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.CreateRecordRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.CreateRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRecord", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRecordBatch(self, request):
        """This API is used to bulk add records.

        :param request: Request instance for CreateRecordBatch.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.CreateRecordBatchRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.CreateRecordBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRecordBatch", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRecordBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRecordGroup(self, request):
        """This API is used to add a record group.

        :param request: Request instance for CreateRecordGroup.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.CreateRecordGroupRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.CreateRecordGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRecordGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRecordGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDomain(self, request):
        """This API is used to delete a domain.

        :param request: Request instance for DeleteDomain.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DeleteDomainRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DeleteDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDomainAlias(self, request):
        """This API is used to delete a domain alias.

        :param request: Request instance for DeleteDomainAlias.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DeleteDomainAliasRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DeleteDomainAliasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDomainAlias", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDomainAliasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDomainBatch(self, request):
        """This API is used to batch delete domains.

        :param request: Request instance for DeleteDomainBatch.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DeleteDomainBatchRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DeleteDomainBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDomainBatch", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDomainBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRecord(self, request):
        """This API is used to delete a record.

        :param request: Request instance for DeleteRecord.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DeleteRecordRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DeleteRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRecordGroup(self, request):
        """This API is used to delete a record group.

        :param request: Request instance for DeleteRecordGroup.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DeleteRecordGroupRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DeleteRecordGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRecordGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRecordGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteShareDomain(self, request):
        """This API is used to unshare a domain.

        :param request: Request instance for DeleteShareDomain.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DeleteShareDomainRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DeleteShareDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteShareDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteShareDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomain(self, request):
        """This API is used to get the information of a domain.

        :param request: Request instance for DescribeDomain.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainAliasList(self, request):
        """This API is used to get the list of domain aliases.

        :param request: Request instance for DescribeDomainAliasList.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainAliasListRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainAliasListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainAliasList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainAliasListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainGroupList(self, request):
        """This API is used to get the list of domain groups.

        :param request: Request instance for DescribeDomainGroupList.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainGroupListRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainList(self, request):
        """This API is used to get the list of domains.

        :param request: Request instance for DescribeDomainList.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainListRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainLogList(self, request):
        """This API is used to get the log of a domain.

        :param request: Request instance for DescribeDomainLogList.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainLogListRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainPurview(self, request):
        """This API is used to get the permissions of a domain.

        :param request: Request instance for DescribeDomainPurview.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainPurviewRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainPurviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainPurview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainPurviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainShareInfo(self, request):
        """This API is used to get the domain sharing information.

        :param request: Request instance for DescribeDomainShareInfo.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainShareInfoRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainShareInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainShareInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainShareInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecord(self, request):
        """This API is used to get the information of a record.

        :param request: Request instance for DescribeRecord.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordGroupList(self, request):
        """This API is used to query the list of DNS record groups.

        :param request: Request instance for DescribeRecordGroupList.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordGroupListRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordLineList(self, request):
        """This API is used to get the split zones allowed by the domain level.

        :param request: Request instance for DescribeRecordLineList.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordLineListRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordLineListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordLineList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordLineListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordList(self, request):
        """This API is used to get the DNS records of a domain.

        :param request: Request instance for DescribeRecordList.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordListRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordType(self, request):
        """This API is used to get the record type allowed by the domain level.

        :param request: Request instance for DescribeRecordType.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordTypeRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubdomainAnalytics(self, request):
        """This API is used to collect statistics on the DNS query volume of a subdomain. It helps you understand the traffic and time period distribution and allows you to view statistics in the last three months. It is available only for domains under a paid plan.

        :param request: Request instance for DescribeSubdomainAnalytics.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeSubdomainAnalyticsRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeSubdomainAnalyticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubdomainAnalytics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubdomainAnalyticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomainLock(self, request):
        """This API is used to lock a domain.

        :param request: Request instance for ModifyDomainLock.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainLockRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainLockResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainLock", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainLockResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomainOwner(self, request):
        """This API is used to transfer ownership of a domain.

        :param request: Request instance for ModifyDomainOwner.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainOwnerRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainOwnerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainOwner", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainOwnerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomainRemark(self, request):
        """This API is used to set the remarks of a domain.

        :param request: Request instance for ModifyDomainRemark.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainRemarkRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainRemarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainRemark", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainRemarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomainStatus(self, request):
        """This API is used to modify the status of a domain.

        :param request: Request instance for ModifyDomainStatus.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainStatusRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomainUnlock(self, request):
        """This API is used to unlock a domain.

        :param request: Request instance for ModifyDomainUnlock.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainUnlockRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainUnlockResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainUnlock", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainUnlockResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRecord(self, request):
        """This API is used to modify a record.

        :param request: Request instance for ModifyRecord.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRecord", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRecordBatch(self, request):
        """This API is used to bulk modify records.

        :param request: Request instance for ModifyRecordBatch.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordBatchRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRecordBatch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRecordBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRecordGroup(self, request):
        """This API is used to modify a record group.

        :param request: Request instance for ModifyRecordGroup.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordGroupRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRecordGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRecordGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRecordRemark(self, request):
        """This API is used to set the remarks of a record.

        :param request: Request instance for ModifyRecordRemark.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordRemarkRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordRemarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRecordRemark", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRecordRemarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRecordStatus(self, request):
        """This API is used to modify the DNS record status.

        :param request: Request instance for ModifyRecordStatus.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordStatusRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRecordStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRecordStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRecordToGroup(self, request):
        """This API is used to add a record to a group.

        :param request: Request instance for ModifyRecordToGroup.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordToGroupRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordToGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRecordToGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRecordToGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))