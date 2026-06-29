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
from tencentcloud.tokenhub.v20260322 import models


class TokenhubClient(AbstractClient):
    _apiVersion = '2026-03-22'
    _endpoint = 'tokenhub.intl.tencentcloudapi.com'
    _service = 'tokenhub'


    def CreateGlossary(self, request):
        r"""Create a Termbase.

        Create a new Termbase in this application for custom definition source to target language terminology mapping. Return the Termbase ID upon success, which can be used to carry out other management operations on terminology entries.

        :param request: Request instance for CreateGlossary.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.CreateGlossaryRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.CreateGlossaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGlossary", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGlossaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGlossaryEntries(self, request):
        r"""Create terminology entries in batches.

        Create terminology entries in batches under the designated Termbase. You can create up to 100 entries at a time.

        :param request: Request instance for CreateGlossaryEntries.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.CreateGlossaryEntriesRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.CreateGlossaryEntriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGlossaryEntries", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGlossaryEntriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGlossary(self, request):
        r"""Delete a termbase.

        This API is used to delete specified Termbase and ALL terminology entries under it. The deletion is idempotent and returns a successful result for non-existing Termbase. After calling the API, if the corresponding Termbase cannot be found via DescribeGlossaries, it indicates successful deletion.

        :param request: Request instance for DeleteGlossary.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DeleteGlossaryRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DeleteGlossaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGlossary", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGlossaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGlossaryEntries(self, request):
        r"""Delete terminology entries in batches.

        Delete terminology entries in batches under the specified Termbase. You can delete up to 200 entries at a time. If the Termbase is nonexistent or NOT_IN this application, it returns a ResourceNotFound error.

        :param request: Request instance for DeleteGlossaryEntries.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DeleteGlossaryEntriesRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DeleteGlossaryEntriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGlossaryEntries", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGlossaryEntriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGlossaries(self, request):
        r"""Query the terminology repository list.

        Query the Termbase list under this application. Support paginate, filter, and sort.

        :param request: Request instance for DescribeGlossaries.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DescribeGlossariesRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DescribeGlossariesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGlossaries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGlossariesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGlossaryEntries(self, request):
        r"""Query the terminology entry list.

        Query specified entries in a Termbase. Support pagination.

        :param request: Request instance for DescribeGlossaryEntries.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DescribeGlossaryEntriesRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DescribeGlossaryEntriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGlossaryEntries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGlossaryEntriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGlossaryEntries(self, request):
        r"""Batch modify terminology entries.

        This API is used to batch modify terminology entries in a designated Termbase. You can modify up to 200 entries at a time.

        :param request: Request instance for ModifyGlossaryEntries.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.ModifyGlossaryEntriesRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.ModifyGlossaryEntriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGlossaryEntries", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGlossaryEntriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))