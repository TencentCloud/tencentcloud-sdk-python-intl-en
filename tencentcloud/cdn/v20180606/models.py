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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class CreateScdnFailedLogTaskRequest(AbstractModel):
    """CreateScdnFailedLogTask request structure.

    """

    def __init__(self):
        r"""
        :param TaskId: ID of the failed task to retry
        :type TaskId: str
        :param Area: Region. Valid values: `mainland` and `overseas`.
        :type Area: str
        """
        self.TaskId = None
        self.Area = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateScdnFailedLogTaskResponse(AbstractModel):
    """CreateScdnFailedLogTask response structure.

    """

    def __init__(self):
        r"""
        :param Result: Creation result. 
0: Creation succeeded
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class PurgePathCacheRequest(AbstractModel):
    """PurgePathCache request structure.

    """

    def __init__(self):
        r"""
        :param Paths: List of directories. The protocol header such as "http://" or "https://" needs to be included.
        :type Paths: list of str
        :param FlushType: Purge type:
`flush`: purges updated resources
`delete`: purges all resources
        :type FlushType: str
        :param UrlEncode: Whether to encode Chinese characters before purge.
        :type UrlEncode: bool
        """
        self.Paths = None
        self.FlushType = None
        self.UrlEncode = None


    def _deserialize(self, params):
        self.Paths = params.get("Paths")
        self.FlushType = params.get("FlushType")
        self.UrlEncode = params.get("UrlEncode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurgePathCacheResponse(AbstractModel):
    """PurgePathCache response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: Purge task ID. Directories submitted in one request share a task ID.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class PushUrlsCacheRequest(AbstractModel):
    """PushUrlsCache request structure.

    """

    def __init__(self):
        r"""
        :param Urls: List of URLs. The protocol header such as "http://" or "https://" needs to be included.
        :type Urls: list of str
        :param UserAgent: Specifies the User-Agent header of an HTTP prefetch request when it is forwarded to the origin server
Default value: `TencentCdn`
        :type UserAgent: str
        :param Area: Destination region for the prefetch
`mainland`: prefetches resources to nodes within Mainland China
`overseas`: prefetches resources to nodes outside Mainland China
`global`: prefetches resources to global nodes
Default value: `mainland`. You can prefetch a URL to nodes in a region provided that CDN service has been enabled for the domain name in the URL in the region.
        :type Area: str
        :param Layer: If this parameter is `middle` or left empty, prefetch will be performed onto the intermediate node.
Note: resources prefetched outside the Chinese mainland will be cached to CDN nodes outside the Chinese mainland and the traffic generated will incur costs.
        :type Layer: str
        :param ParseM3U8: Whether to recursively resolve the M3U8 index file and prefetch the TS shards in it.
Notes:
1. This feature requires that the M3U8 index file can be directly requested and obtained.
2. In the M3U8 index file, currently only the TS shards at the first to the third level can be recursively resolved.
3. Prefetching the TS shards obtained through recursive resolution consumes the daily prefetch quota. If the usage exceeds the quota, the feature will be disabled and TS shards will not be prefetched.
        :type ParseM3U8: bool
        """
        self.Urls = None
        self.UserAgent = None
        self.Area = None
        self.Layer = None
        self.ParseM3U8 = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")
        self.UserAgent = params.get("UserAgent")
        self.Area = params.get("Area")
        self.Layer = params.get("Layer")
        self.ParseM3U8 = params.get("ParseM3U8")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PushUrlsCacheResponse(AbstractModel):
    """PushUrlsCache response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: ID of the submitted task
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")