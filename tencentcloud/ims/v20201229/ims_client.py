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
from tencentcloud.ims.v20201229 import models


class ImsClient(AbstractClient):
    _apiVersion = '2020-12-29'
    _endpoint = 'ims.tencentcloudapi.com'
    _service = 'ims'


    def ImageModeration(self, request):
        """This API is used to submit an image for smart moderation. Before using it, you need to log in to the console with the Tencent Cloud root account [to activate IMS](https://console.cloud.tencent.com/cms/image/package) and adjust the business configuration.
        ### API use instructions
        - Go to the "[CMS console - IMS](https://console.cloud.tencent.com/cms/image/package)" to activate IMS.
        - This API is a paid API. For its billing mode, see [IMS Pricing](https://intl.cloud.tencent.com/product/ims/pricing?from_cn_redirect=1).

        ### API feature description
        - It can detect images or links and recognize content that may be offensive, unsafe, or inappropriate based on the deep learning technology;
        - It can capture frames from or split GIF/long images for detection;
        - It can recognize various non-compliant scenarios, including vulgarity, law or regulation violations, pornography, and advertising;
        - It can detect multiple types of objects (such as object, advertising logo, and QR code) and recognize text in images based on OCR;
        - It allows you to customize moderation policies based on different business scenarios;
        - You can select image risk libraries to filter non-compliant images of custom types (currently, only blocklist configuration is supported);
        - You can associate account or device information when moderating an image to recognize the account or device involved.

        ### API call description
        - Supported image file size: **< 5 MB**
        - Supported image file resolution: **a resolution of 256x256 or higher** is recommended; otherwise, the recognition effect may be affected.
        - Supported image file formats: PNG, JPG, JPEG, BMP, GIF, and WEBP.
        - Supported image URL transfer protocols: HTTP and HTTPS.
        - If you pass in the access URL of an image, you need to **limit the image download time to 3 seconds**. To ensure the stability and reliability of the image to be detected, we recommend you use Tencent Cloud COS for storage or CDN for caching.
        - Default API request rate limit: **100 requests/sec**. If this limit is exceeded, an error will be reported.

        <div class="rno-api-explorer" style="margin-bottom:20px">
            <div class="rno-api-explorer-inner">
                <div class="rno-api-explorer-hd">
                    <div class="rno-api-explorer-title">
                        Version iteration description
                    </div>
                </div>
                <div class="rno-api-explorer-body">
                    <div class="rno-api-explorer-cont">
                        <p>The version described on this page is 2020. The IMS APIs connected to before November 3, 2020 are on v2019, and you can directly access the following URL to perform maintenance operations: <a href="https://intl.cloud.tencent.com/document/product/1125/38206?from_cn_redirect=1" target="_blank">IMS APIs v2019</a></p>
                        <p>v2020 is an upgrade to v2019 to support more flexible multi-scenario business policy configuration and richer recognition callback information, meeting the recognition requirements of different businesses. We recommend you upgrade the APIs according to the v2020 connection guide. Meanwhile, we will continue to maintain v2019 until users no longer use it.</p>
                    </div>
                </div>
            </div>
        </div>

        :param request: Request instance for ImageModeration.
        :type request: :class:`tencentcloud.ims.v20201229.models.ImageModerationRequest`
        :rtype: :class:`tencentcloud.ims.v20201229.models.ImageModerationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImageModeration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImageModerationResponse()
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