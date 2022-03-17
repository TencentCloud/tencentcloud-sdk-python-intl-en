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
from tencentcloud.cloudaudit.v20190319 import models


class CloudauditClient(AbstractClient):
    _apiVersion = '2019-03-19'
    _endpoint = 'cloudaudit.tencentcloudapi.com'
    _service = 'cloudaudit'


    def CreateAudit(self, request):
        """Parameter requirements:
        1. If the value of `IsCreateNewBucket` exists, `cosRegion` and `osBucketName` are required.
        2. If the value of `IsEnableCmqNotify` is 1, `IsCreateNewQueue`, `CmqRegion`, and `CmqQueueName` are required.
        3. If the value of `IsEnableCmqNotify` is 0, `IsCreateNewQueue`, `CmqRegion`, and `CmqQueueName` cannot be passed in.
        4. If the value of `IsEnableKmsEncry` is 1, `KmsRegion` and `KeyId` are required.

        :param request: Request instance for CreateAudit.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.CreateAuditRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.CreateAuditResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAudit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAuditResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAuditTrack(self, request):
        """This API is used to create a tracking set.

        :param request: Request instance for CreateAuditTrack.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.CreateAuditTrackRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.CreateAuditTrackResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAuditTrack", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAuditTrackResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAudit(self, request):
        """This API is used to delete a tracking set.

        :param request: Request instance for DeleteAudit.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.DeleteAuditRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.DeleteAuditResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAudit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAuditResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAuditTrack(self, request):
        """This API is used to delete a CloudAudit tracking set.

        :param request: Request instance for DeleteAuditTrack.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.DeleteAuditTrackRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.DeleteAuditTrackResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAuditTrack", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAuditTrackResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAudit(self, request):
        """This API is used to query the details of a tracking set.

        :param request: Request instance for DescribeAudit.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.DescribeAuditRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.DescribeAuditResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAudit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAuditResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAuditTracks(self, request):
        """This API is used to query the CloudAudit tracking set list.

        :param request: Request instance for DescribeAuditTracks.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.DescribeAuditTracksRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.DescribeAuditTracksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAuditTracks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAuditTracksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEvents(self, request):
        """This API is used to query CloudAudit logs.

        :param request: Request instance for DescribeEvents.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.DescribeEventsRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.DescribeEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEventsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetAttributeKey(self, request):
        """This API is used to query the valid values of `AttributeKey`.

        :param request: Request instance for GetAttributeKey.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.GetAttributeKeyRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.GetAttributeKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetAttributeKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetAttributeKeyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquireAuditCredit(self, request):
        """This API is used to query the number of tracking sets that can be created.

        :param request: Request instance for InquireAuditCredit.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.InquireAuditCreditRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.InquireAuditCreditResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquireAuditCredit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquireAuditCreditResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListAudits(self, request):
        """This API is used to query the summary of tracking sets.

        :param request: Request instance for ListAudits.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.ListAuditsRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.ListAuditsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListAudits", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListAuditsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListCmqEnableRegion(self, request):
        """This API is used to query CloudAudit-enabled CMQ AZs.

        :param request: Request instance for ListCmqEnableRegion.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.ListCmqEnableRegionRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.ListCmqEnableRegionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListCmqEnableRegion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListCmqEnableRegionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListCosEnableRegion(self, request):
        """This API is used to query CloudAudit-enabled COS AZs.

        :param request: Request instance for ListCosEnableRegion.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.ListCosEnableRegionRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.ListCosEnableRegionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListCosEnableRegion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListCosEnableRegionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def LookUpEvents(self, request):
        """This API is used to search for operation logs to help query relevant operation information.

        :param request: Request instance for LookUpEvents.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.LookUpEventsRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.LookUpEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("LookUpEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.LookUpEventsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAuditTrack(self, request):
        """This API is used to modify a CloudAudit tracking set.

        :param request: Request instance for ModifyAuditTrack.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.ModifyAuditTrackRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.ModifyAuditTrackResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAuditTrack", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAuditTrackResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StartLogging(self, request):
        """This API is used to enable a tracking set.

        :param request: Request instance for StartLogging.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.StartLoggingRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.StartLoggingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartLogging", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartLoggingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopLogging(self, request):
        """This API is used to disable a tracking set.

        :param request: Request instance for StopLogging.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.StopLoggingRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.StopLoggingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopLogging", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopLoggingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateAudit(self, request):
        """Parameter requirements:
        1. If the value of `IsCreateNewBucket` exists, `cosRegion` and `osBucketName` are required.
        2. If the value of `IsEnableCmqNotify` is 1, `IsCreateNewQueue`, `CmqRegion`, and `CmqQueueName` are required.
        3. If the value of `IsEnableCmqNotify` is 0, `IsCreateNewQueue`, `CmqRegion`, and `CmqQueueName` cannot be passed in.
        4. If the value of `IsEnableKmsEncry` is 1, `KmsRegion` and `KeyId` are required.

        :param request: Request instance for UpdateAudit.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.UpdateAuditRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.UpdateAuditResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateAudit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateAuditResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)