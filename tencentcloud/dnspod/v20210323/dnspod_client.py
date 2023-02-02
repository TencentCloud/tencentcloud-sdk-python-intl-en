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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)