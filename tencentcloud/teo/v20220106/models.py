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


class CreatePrefetchTaskRequest(AbstractModel):
    """CreatePrefetchTask request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param Targets: List of resources to be pre-warmed, for example:
http://www.example.com/example.txt
        :type Targets: list of str
        :param EncodeUrl: Specifies whether to encode the URL
Note that if it’s enabled, the purging is based on the converted URLs.
        :type EncodeUrl: bool
        :param Headers: HTTP header information
        :type Headers: list of Header
        """
        self.ZoneId = None
        self.Targets = None
        self.EncodeUrl = None
        self.Headers = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Targets = params.get("Targets")
        self.EncodeUrl = params.get("EncodeUrl")
        if params.get("Headers") is not None:
            self.Headers = []
            for item in params.get("Headers"):
                obj = Header()
                obj._deserialize(item)
                self.Headers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrefetchTaskResponse(AbstractModel):
    """CreatePrefetchTask response structure.

    """

    def __init__(self):
        r"""
        :param JobId: Task ID
        :type JobId: str
        :param FailedList: List of failed tasks
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FailedList: list of FailReason
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.JobId = None
        self.FailedList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        if params.get("FailedList") is not None:
            self.FailedList = []
            for item in params.get("FailedList"):
                obj = FailReason()
                obj._deserialize(item)
                self.FailedList.append(obj)
        self.RequestId = params.get("RequestId")


class CreatePurgeTaskRequest(AbstractModel):
    """CreatePurgeTask request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param Type: Type of the purging task. Values:
- `purge_url`: Purge by the URL
- `purge_prefix`: Purge by the prefix
- `purge_host`: Purge by the Hostname
- `purge_all`: Purge all cached contents
        :type Type: str
        :param Targets: Target resource to be purged, which depends on the `Type` field.
1. When `Type = purge_host`:
Hostnames are purged, such as www.example.com and foo.bar.example.com.
2. When `Type = purge_prefix`:
Prefixes are purged, such as http://www.example.com/example.
3. When `Type = purge_url`:
URLs are purged, such as https://www.example.com/example.jpg.
4. When `Type = purge_all`: All types of resources are purged.
`Targets` is not a required field.
        :type Targets: list of str
        :param EncodeUrl: Specifies whether to transcode non-ASCII URLs according to RFC3986.
Note that if it’s enabled, the purging is based on the converted URLs.
        :type EncodeUrl: bool
        """
        self.ZoneId = None
        self.Type = None
        self.Targets = None
        self.EncodeUrl = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Type = params.get("Type")
        self.Targets = params.get("Targets")
        self.EncodeUrl = params.get("EncodeUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePurgeTaskResponse(AbstractModel):
    """CreatePurgeTask response structure.

    """

    def __init__(self):
        r"""
        :param JobId: Task ID
        :type JobId: str
        :param FailedList: List of failed tasks and reasons
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FailedList: list of FailReason
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.JobId = None
        self.FailedList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        if params.get("FailedList") is not None:
            self.FailedList = []
            for item in params.get("FailedList"):
                obj = FailReason()
                obj._deserialize(item)
                self.FailedList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePrefetchTasksRequest(AbstractModel):
    """DescribePrefetchTasks request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Task ID
        :type JobId: str
        :param StartTime: Start time of the query
        :type StartTime: str
        :param EndTime: End time of the query
        :type EndTime: str
        :param Offset: Offset of the query
        :type Offset: int
        :param Limit: Maximum number of results returned
        :type Limit: int
        :param Statuses: Statuses of tasks to be queried. Values:
`processing`, `success`, `failed`, `timeout` and `invalid`
        :type Statuses: list of str
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param Domains: List of domain names queried
        :type Domains: list of str
        :param Target: Resources queried
        :type Target: str
        """
        self.JobId = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.Statuses = None
        self.ZoneId = None
        self.Domains = None
        self.Target = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Statuses = params.get("Statuses")
        self.ZoneId = params.get("ZoneId")
        self.Domains = params.get("Domains")
        self.Target = params.get("Target")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrefetchTasksResponse(AbstractModel):
    """DescribePrefetchTasks response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total entries that match the specified query condition
        :type TotalCount: int
        :param Tasks: List of tasks returned
        :type Tasks: list of Task
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePurgeTasksRequest(AbstractModel):
    """DescribePurgeTasks request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Task ID
        :type JobId: str
        :param Type: Type of the purging task
        :type Type: str
        :param StartTime: Start time of the query
        :type StartTime: str
        :param EndTime: End time of the query
        :type EndTime: str
        :param Offset: Offset of the query
        :type Offset: int
        :param Limit: Maximum number of results returned
        :type Limit: int
        :param Statuses: Statuses of tasks to be queried. Values:
`processing`, `success`, `failed`, `timeout` and `invalid`
        :type Statuses: list of str
        :param ZoneId: ID of the site
        :type ZoneId: str
        :param Domains: List of domain names queried
        :type Domains: list of str
        :param Target: Queries content
        :type Target: str
        """
        self.JobId = None
        self.Type = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.Statuses = None
        self.ZoneId = None
        self.Domains = None
        self.Target = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.Type = params.get("Type")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Statuses = params.get("Statuses")
        self.ZoneId = params.get("ZoneId")
        self.Domains = params.get("Domains")
        self.Target = params.get("Target")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePurgeTasksResponse(AbstractModel):
    """DescribePurgeTasks response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total entries that match the specified query condition
        :type TotalCount: int
        :param Tasks: List of tasks returned
        :type Tasks: list of Task
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Pagination parameter, which specifies the offset.
        :type Offset: int
        :param Limit: Pagination parameter, which specifies the number of sites returned in each page.
        :type Limit: int
        :param Filters: Query condition filter, which supports complex type.
        :type Filters: list of ZoneFilter
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = ZoneFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZonesResponse(AbstractModel):
    """DescribeZones response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of sites that match the specified conditions
        :type TotalCount: int
        :param Zones: Details of sites
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Zones: list of Zone
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Zones = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Zones") is not None:
            self.Zones = []
            for item in params.get("Zones"):
                obj = Zone()
                obj._deserialize(item)
                self.Zones.append(obj)
        self.RequestId = params.get("RequestId")


class DownloadL7LogsRequest(AbstractModel):
    """DownloadL7Logs request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time. It must conform to the RFC3339 standard.
        :type StartTime: str
        :param EndTime: End time. It must conform to the RFC3339 standard.
        :type EndTime: str
        :param PageSize: Number of entries per page
        :type PageSize: int
        :param PageNo: Current page
        :type PageNo: int
        :param Zones: List of sites
        :type Zones: list of str
        :param Domains: List of domain names
        :type Domains: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.PageSize = None
        self.PageNo = None
        self.Zones = None
        self.Domains = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.Zones = params.get("Zones")
        self.Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadL7LogsResponse(AbstractModel):
    """DownloadL7Logs response structure.

    """

    def __init__(self):
        r"""
        :param Data: Layer-7 offline log data
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Data: list of L7OfflineLog
        :param PageSize: Page size
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PageSize: int
        :param PageNo: Page number
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PageNo: int
        :param Pages: Total number of pages
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Pages: int
        :param TotalSize: Total number of entries
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TotalSize: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.PageSize = None
        self.PageNo = None
        self.Pages = None
        self.TotalSize = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = L7OfflineLog()
                obj._deserialize(item)
                self.Data.append(obj)
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.Pages = params.get("Pages")
        self.TotalSize = params.get("TotalSize")
        self.RequestId = params.get("RequestId")


class FailReason(AbstractModel):
    """Failure reason

    """

    def __init__(self):
        r"""
        :param Reason: Failure reason
        :type Reason: str
        :param Targets: List of resources failed to be processed. 
 
        :type Targets: list of str
        """
        self.Reason = None
        self.Targets = None


    def _deserialize(self, params):
        self.Reason = params.get("Reason")
        self.Targets = params.get("Targets")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Header(AbstractModel):
    """HTTP header, used as input for the CreatePrefetchTask API

    """

    def __init__(self):
        r"""
        :param Name: HTTP header name
        :type Name: str
        :param Value: HTTP header value
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7OfflineLog(AbstractModel):
    """Layer-7 offline log details

    """

    def __init__(self):
        r"""
        :param LogTime: Start time of the log packaging
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type LogTime: int
        :param Domain: Site name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Domain: str
        :param Size: Log size, in bytes
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Size: int
        :param Url: Download address
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Url: str
        :param LogPacketName: Log package name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type LogPacketName: str
        """
        self.LogTime = None
        self.Domain = None
        self.Size = None
        self.Url = None
        self.LogPacketName = None


    def _deserialize(self, params):
        self.LogTime = params.get("LogTime")
        self.Domain = params.get("Domain")
        self.Size = params.get("Size")
        self.Url = params.get("Url")
        self.LogPacketName = params.get("LogPacketName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Task(AbstractModel):
    """Content management task result

    """

    def __init__(self):
        r"""
        :param JobId: Task ID
        :type JobId: str
        :param Status: Status of the task
        :type Status: str
        :param Target: Resource
        :type Target: str
        :param Type: Task type
        :type Type: str
        :param CreateTime: Task creation time
        :type CreateTime: str
        :param UpdateTime: Task completion time
        :type UpdateTime: str
        """
        self.JobId = None
        self.Status = None
        self.Target = None
        self.Type = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.Status = params.get("Status")
        self.Target = params.get("Target")
        self.Type = params.get("Type")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Zone(AbstractModel):
    """Site information

    """

    def __init__(self):
        r"""
        :param Id: Site ID
        :type Id: str
        :param Name: Site name
        :type Name: str
        :param OriginalNameServers: List of name servers used by the site
        :type OriginalNameServers: list of str
        :param NameServers: List of name servers assigned by Tencent Cloud
        :type NameServers: list of str
        :param Status: Site status
- `active`: The name server is switched.
- `pending`: The name server is not switched.
- `moved`: The name server is moved.
- `deactivated`: The name server is blocked.
        :type Status: str
        :param Type: How the site is connected to EdgeOne.
- `full`: The site is connected via name server.
- `partial`: The site is connected via CNAME.
        :type Type: str
        :param Paused: Indicates whether the site is disabled
        :type Paused: bool
        :param CreatedOn: Site creation date
        :type CreatedOn: str
        :param ModifiedOn: Site modification date
        :type ModifiedOn: str
        """
        self.Id = None
        self.Name = None
        self.OriginalNameServers = None
        self.NameServers = None
        self.Status = None
        self.Type = None
        self.Paused = None
        self.CreatedOn = None
        self.ModifiedOn = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.OriginalNameServers = params.get("OriginalNameServers")
        self.NameServers = params.get("NameServers")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.Paused = params.get("Paused")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneFilter(AbstractModel):
    """Site query filter

    """

    def __init__(self):
        r"""
        :param Name: Filters by the field name. Vaules:
- `name`: Site name.
- `status`: Site status.
        :type Name: str
        :param Values: Filters by the field value
        :type Values: list of str
        :param Fuzzy: Specifies whether to enable fuzzy query. It’s only available when filter name is `name`. If it’s enabled, the length of `Values` must be 1.
        :type Fuzzy: bool
        """
        self.Name = None
        self.Values = None
        self.Fuzzy = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        self.Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        