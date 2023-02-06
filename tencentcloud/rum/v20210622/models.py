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


class CreateLogExportRequest(AbstractModel):
    """CreateLogExport request structure.

    """

    def __init__(self):
        r"""
        :param ID: Project ID
        :type ID: int
        :param StartTime: Log export start time
        :type StartTime: str
        :param EndTime: Log export end time
        :type EndTime: str
        :param Query: Log export search statement
        :type Query: str
        :param Count: Number of logs to be exported. Maximum value: 10 million
        :type Count: int
        :param Order: Exported log sorting order by time. Valid values: asc: ascending; desc: descending. Default value: desc
        :type Order: str
        :param Format: Exported log data format. Valid values: json, csv. Default value: json
        :type Format: str
        """
        self.ID = None
        self.StartTime = None
        self.EndTime = None
        self.Query = None
        self.Count = None
        self.Order = None
        self.Format = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Query = params.get("Query")
        self.Count = params.get("Count")
        self.Order = params.get("Order")
        self.Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLogExportResponse(AbstractModel):
    """CreateLogExport response structure.

    """

    def __init__(self):
        r"""
        :param ExportID: Log export ID
        :type ExportID: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ExportID = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ExportID = params.get("ExportID")
        self.RequestId = params.get("RequestId")


class CreateOfflineLogConfigRequest(AbstractModel):
    """CreateOfflineLogConfig request structure.

    """

    def __init__(self):
        r"""
        :param ProjectKey: Unique project key for reporting
        :type ProjectKey: str
        :param UniqueID: Unique identifier of the user to be listened on (`aid` or `uin`)
        :type UniqueID: str
        """
        self.ProjectKey = None
        self.UniqueID = None


    def _deserialize(self, params):
        self.ProjectKey = params.get("ProjectKey")
        self.UniqueID = params.get("UniqueID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOfflineLogConfigResponse(AbstractModel):
    """CreateOfflineLogConfig response structure.

    """

    def __init__(self):
        r"""
        :param Msg: API response information
        :type Msg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class CreateProjectRequest(AbstractModel):
    """CreateProject request structure.

    """

    def __init__(self):
        r"""
        :param Name: Name of the created project (required and up to 200 characters)
        :type Name: str
        :param InstanceID: Business system ID
        :type InstanceID: str
        :param Rate: Project sampling rate (greater than or equal to 0)
        :type Rate: str
        :param EnableURLGroup: Whether to enable aggregation
        :type EnableURLGroup: int
        :param Type: Project type (valid values: "web", "mp", "android", "ios", "node", "hippy", "weex", "viola", "rn")
        :type Type: str
        :param Repo: Repository address of the project (optional and up to 256 characters)
        :type Repo: str
        :param URL: Webpage address of the project (optional and up to 256 characters)
        :type URL: str
        :param Desc: Description of the created project (optional and up to 1,000 characters)
        :type Desc: str
        """
        self.Name = None
        self.InstanceID = None
        self.Rate = None
        self.EnableURLGroup = None
        self.Type = None
        self.Repo = None
        self.URL = None
        self.Desc = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.InstanceID = params.get("InstanceID")
        self.Rate = params.get("Rate")
        self.EnableURLGroup = params.get("EnableURLGroup")
        self.Type = params.get("Type")
        self.Repo = params.get("Repo")
        self.URL = params.get("URL")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProjectResponse(AbstractModel):
    """CreateProject response structure.

    """

    def __init__(self):
        r"""
        :param ID: Project ID
        :type ID: int
        :param Key: Unique project key
        :type Key: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ID = None
        self.Key = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.Key = params.get("Key")
        self.RequestId = params.get("RequestId")


class CreateReleaseFileRequest(AbstractModel):
    """CreateReleaseFile request structure.

    """

    def __init__(self):
        r"""
        :param ProjectID: Project ID
        :type ProjectID: int
        :param Files: File information list
        :type Files: list of ReleaseFile
        """
        self.ProjectID = None
        self.Files = None


    def _deserialize(self, params):
        self.ProjectID = params.get("ProjectID")
        if params.get("Files") is not None:
            self.Files = []
            for item in params.get("Files"):
                obj = ReleaseFile()
                obj._deserialize(item)
                self.Files.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReleaseFileResponse(AbstractModel):
    """CreateReleaseFile response structure.

    """

    def __init__(self):
        r"""
        :param Msg: Call result
        :type Msg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class CreateStarProjectRequest(AbstractModel):
    """CreateStarProject request structure.

    """

    def __init__(self):
        r"""
        :param InstanceID: Instance ID, such as taw-123
        :type InstanceID: str
        :param ID: Project ID
        :type ID: int
        """
        self.InstanceID = None
        self.ID = None


    def _deserialize(self, params):
        self.InstanceID = params.get("InstanceID")
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStarProjectResponse(AbstractModel):
    """CreateStarProject response structure.

    """

    def __init__(self):
        r"""
        :param Msg: API response information
        :type Msg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class CreateTawInstanceRequest(AbstractModel):
    """CreateTawInstance request structure.

    """

    def __init__(self):
        r"""
        :param AreaId: Region ID (at least greater than 0)
        :type AreaId: int
        :param ChargeType: Billing type (1: Pay-as-you-go).
        :type ChargeType: int
        :param DataRetentionDays: Data retention period (at least greater than 0)
        :type DataRetentionDays: int
        :param InstanceName: Instance name (up to 255 bytes)
        :type InstanceName: str
        :param Tags: Tag list
        :type Tags: list of Tag
        :param InstanceDesc: Instance description (up to 1,024 bytes)
        :type InstanceDesc: str
        :param CountNum: Number of data entries reported per day
        :type CountNum: str
        :param PeriodRetain: Billing for data storage
        :type PeriodRetain: str
        :param BuyingChannel: Instance purchase channel. Valid value: `cdn`.
        :type BuyingChannel: str
        :param ResourcePackageType: Type of prepaid resource pack (only required for prepaid mode)
        :type ResourcePackageType: int
        :param ResourcePackageNum: The number of prepaid resource packs (only required for prepaid mode)
        :type ResourcePackageNum: int
        """
        self.AreaId = None
        self.ChargeType = None
        self.DataRetentionDays = None
        self.InstanceName = None
        self.Tags = None
        self.InstanceDesc = None
        self.CountNum = None
        self.PeriodRetain = None
        self.BuyingChannel = None
        self.ResourcePackageType = None
        self.ResourcePackageNum = None


    def _deserialize(self, params):
        self.AreaId = params.get("AreaId")
        self.ChargeType = params.get("ChargeType")
        self.DataRetentionDays = params.get("DataRetentionDays")
        self.InstanceName = params.get("InstanceName")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.InstanceDesc = params.get("InstanceDesc")
        self.CountNum = params.get("CountNum")
        self.PeriodRetain = params.get("PeriodRetain")
        self.BuyingChannel = params.get("BuyingChannel")
        self.ResourcePackageType = params.get("ResourcePackageType")
        self.ResourcePackageNum = params.get("ResourcePackageNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTawInstanceResponse(AbstractModel):
    """CreateTawInstance response structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param DealName: ID of prepaid order
Note: This field may return null, indicating that no valid values can be obtained.
        :type DealName: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceId = None
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class CreateWhitelistRequest(AbstractModel):
    """CreateWhitelist request structure.

    """

    def __init__(self):
        r"""
        :param InstanceID: Instance ID, such as taw-123
        :type InstanceID: str
        :param Remark: Remarks
        :type Remark: str
        :param WhitelistUin: uin: business identifier
        :type WhitelistUin: str
        :param Aid: Business identifier
        :type Aid: str
        """
        self.InstanceID = None
        self.Remark = None
        self.WhitelistUin = None
        self.Aid = None


    def _deserialize(self, params):
        self.InstanceID = params.get("InstanceID")
        self.Remark = params.get("Remark")
        self.WhitelistUin = params.get("WhitelistUin")
        self.Aid = params.get("Aid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWhitelistResponse(AbstractModel):
    """CreateWhitelist response structure.

    """

    def __init__(self):
        r"""
        :param Msg: Message
        :type Msg: str
        :param ID: Allowlist ID
        :type ID: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Msg = None
        self.ID = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.ID = params.get("ID")
        self.RequestId = params.get("RequestId")


class DeleteInstanceRequest(AbstractModel):
    """DeleteInstance request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: ID of the instance to be deleted
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceResponse(AbstractModel):
    """DeleteInstance response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLogExportRequest(AbstractModel):
    """DeleteLogExport request structure.

    """

    def __init__(self):
        r"""
        :param ID: Project ID
        :type ID: int
        :param ExportID: Log export ID
        :type ExportID: str
        """
        self.ID = None
        self.ExportID = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.ExportID = params.get("ExportID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLogExportResponse(AbstractModel):
    """DeleteLogExport response structure.

    """

    def __init__(self):
        r"""
        :param Msg: Whether it is successful. If so, `success` will be returned; otherwise, `Error` rather than this parameter will be returned
Note: this field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DeleteOfflineLogConfigRequest(AbstractModel):
    """DeleteOfflineLogConfig request structure.

    """

    def __init__(self):
        r"""
        :param ProjectKey: Unique project key for reporting
        :type ProjectKey: str
        :param UniqueID: Unique user identifier (uin or aid)
        :type UniqueID: str
        """
        self.ProjectKey = None
        self.UniqueID = None


    def _deserialize(self, params):
        self.ProjectKey = params.get("ProjectKey")
        self.UniqueID = params.get("UniqueID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOfflineLogConfigResponse(AbstractModel):
    """DeleteOfflineLogConfig response structure.

    """

    def __init__(self):
        r"""
        :param Msg: API call information
        :type Msg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DeleteOfflineLogRecordRequest(AbstractModel):
    """DeleteOfflineLogRecord request structure.

    """

    def __init__(self):
        r"""
        :param ProjectKey: Unique project key for reporting
        :type ProjectKey: str
        :param FileID: Offline log file ID
        :type FileID: str
        """
        self.ProjectKey = None
        self.FileID = None


    def _deserialize(self, params):
        self.ProjectKey = params.get("ProjectKey")
        self.FileID = params.get("FileID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOfflineLogRecordResponse(AbstractModel):
    """DeleteOfflineLogRecord response structure.

    """

    def __init__(self):
        r"""
        :param Msg: API call information
        :type Msg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DeleteProjectRequest(AbstractModel):
    """DeleteProject request structure.

    """

    def __init__(self):
        r"""
        :param ID: ID of the project to be deleted
        :type ID: int
        """
        self.ID = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProjectResponse(AbstractModel):
    """DeleteProject response structure.

    """

    def __init__(self):
        r"""
        :param Msg: Operation information
        :type Msg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DeleteReleaseFileRequest(AbstractModel):
    """DeleteReleaseFile request structure.

    """

    def __init__(self):
        r"""
        :param ID: File ID
        :type ID: int
        """
        self.ID = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReleaseFileResponse(AbstractModel):
    """DeleteReleaseFile response structure.

    """

    def __init__(self):
        r"""
        :param Msg: Response string of the API request
        :type Msg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DeleteStarProjectRequest(AbstractModel):
    """DeleteStarProject request structure.

    """

    def __init__(self):
        r"""
        :param InstanceID: Instance ID, such as taw-123
        :type InstanceID: str
        :param ID: Project ID
        :type ID: int
        """
        self.InstanceID = None
        self.ID = None


    def _deserialize(self, params):
        self.InstanceID = params.get("InstanceID")
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStarProjectResponse(AbstractModel):
    """DeleteStarProject response structure.

    """

    def __init__(self):
        r"""
        :param Msg: Response message
Note: this field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DeleteWhitelistRequest(AbstractModel):
    """DeleteWhitelist request structure.

    """

    def __init__(self):
        r"""
        :param InstanceID: Instance ID
        :type InstanceID: str
        :param ID: List ID
        :type ID: str
        """
        self.InstanceID = None
        self.ID = None


    def _deserialize(self, params):
        self.InstanceID = params.get("InstanceID")
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWhitelistResponse(AbstractModel):
    """DeleteWhitelist response structure.

    """

    def __init__(self):
        r"""
        :param Msg: Success message
        :type Msg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DescribeDataCustomUrlRequest(AbstractModel):
    """DescribeDataCustomUrl request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: int
        :param Type: `top`: top resources view; `allcount`: performance view; `day`: 14-day data; `condition`: condition list; `pagepv`: PV view; `area`: request speed distribution; `nettype`/`version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: network/platform view; version view; device view; ISP view; region view; browser view; custom view, and so on.
        :type Type: str
        :param EndTime: End time
        :type EndTime: int
        :param ID: Project ID
        :type ID: int
        :param ExtSecond: Custom 2
        :type ExtSecond: str
        :param Engine: Browser engine
        :type Engine: str
        :param Isp: ISP
        :type Isp: str
        :param From: Source page
        :type From: str
        :param Level: Log level
        :type Level: str
        :param Brand: Brand
        :type Brand: str
        :param Area: Region
        :type Area: str
        :param VersionNum: Version
        :type VersionNum: str
        :param Platform: Platform
        :type Platform: str
        :param ExtThird: Custom 3
        :type ExtThird: str
        :param ExtFirst: Custom 1
        :type ExtFirst: str
        :param NetType: Network type
        :type NetType: str
        :param Device: Model
        :type Device: str
        :param IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param Os: OS
        :type Os: str
        :param Browser: Browser
        :type Browser: str
        :param CostType: Duration calculation method
        :type CostType: str
        :param Url: Key value of the custom speed test
        :type Url: str
        :param Env: Environment
        :type Env: str
        """
        self.StartTime = None
        self.Type = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.CostType = None
        self.Url = None
        self.Env = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.CostType = params.get("CostType")
        self.Url = params.get("Url")
        self.Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataCustomUrlResponse(AbstractModel):
    """DescribeDataCustomUrl response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned value
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataEventUrlRequest(AbstractModel):
    """DescribeDataEventUrl request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: int
        :param Type: `allcount`: performance view; `day`: 14-day data; `condition`: condition list; `ckuv`: UV trend; `ckpv`: PV trend; `nettype`/`version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: network/platform view; version view; device view; ISP view; region view; browser view; custom view, and so on.
        :type Type: str
        :param EndTime: End time
        :type EndTime: int
        :param ID: Project ID
        :type ID: int
        :param ExtSecond: Custom 2
        :type ExtSecond: str
        :param Engine: Browser engine
        :type Engine: str
        :param Isp: ISP
        :type Isp: str
        :param From: Source page
        :type From: str
        :param Level: Log level
        :type Level: str
        :param Brand: Brand
        :type Brand: str
        :param Area: Region
        :type Area: str
        :param VersionNum: Version
        :type VersionNum: str
        :param Platform: Platform
        :type Platform: str
        :param ExtThird: Custom 3
        :type ExtThird: str
        :param ExtFirst: Custom 1
        :type ExtFirst: str
        :param NetType: Network type
        :type NetType: str
        :param Device: Model
        :type Device: str
        :param IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param Os: OS
        :type Os: str
        :param Browser: Browser
        :type Browser: str
        :param Name: Filter
        :type Name: str
        :param Env: Environment
        :type Env: str
        """
        self.StartTime = None
        self.Type = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.Name = None
        self.Env = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.Name = params.get("Name")
        self.Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataEventUrlResponse(AbstractModel):
    """DescribeDataEventUrl response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned value
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataFetchProjectRequest(AbstractModel):
    """DescribeDataFetchProject request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: int
        :param Type: `allcount`: performance view; `day`: 14-day data; `condition`: condition list; `area`: request speed distribution; `nettype`/`version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: network/platform view; version view; device view; ISP view; region view; browser view; custom view, and so on.
        :type Type: str
        :param EndTime: End time
        :type EndTime: int
        :param ID: Project ID
        :type ID: int
        :param ExtSecond: Custom 2
        :type ExtSecond: str
        :param Engine: Browser engine
        :type Engine: str
        :param Isp: ISP
        :type Isp: str
        :param From: Source page
        :type From: str
        :param Level: Log level
        :type Level: str
        :param Brand: Brand
        :type Brand: str
        :param Area: Region
        :type Area: str
        :param VersionNum: Version
        :type VersionNum: str
        :param Platform: Platform
        :type Platform: str
        :param ExtThird: Custom 3
        :type ExtThird: str
        :param ExtFirst: Custom 1
        :type ExtFirst: str
        :param NetType: Network type
        :type NetType: str
        :param Device: Model
        :type Device: str
        :param IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param Os: OS
        :type Os: str
        :param Browser: Browser
        :type Browser: str
        :param CostType: Duration calculation method
        :type CostType: str
        :param Url: Source
        :type Url: str
        :param Env: Environment
        :type Env: str
        :param Status: HTTP status code.
        :type Status: str
        :param Ret: retcode
        :type Ret: str
        """
        self.StartTime = None
        self.Type = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.CostType = None
        self.Url = None
        self.Env = None
        self.Status = None
        self.Ret = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.CostType = params.get("CostType")
        self.Url = params.get("Url")
        self.Env = params.get("Env")
        self.Status = params.get("Status")
        self.Ret = params.get("Ret")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataFetchProjectResponse(AbstractModel):
    """DescribeDataFetchProject response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned value
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataFetchUrlInfoRequest(AbstractModel):
    """DescribeDataFetchUrlInfo request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: int
        :param Type: Type
        :type Type: str
        :param EndTime: End time
        :type EndTime: int
        :param ID: Project ID
        :type ID: int
        :param ExtSecond: Custom 2
        :type ExtSecond: str
        :param Engine: Browser engine
        :type Engine: str
        :param Isp: ISP
        :type Isp: str
        :param From: Source page
        :type From: str
        :param Level: Log level
        :type Level: str
        :param Brand: Brand
        :type Brand: str
        :param Area: Region
        :type Area: str
        :param VersionNum: Version
        :type VersionNum: str
        :param Platform: Platform
        :type Platform: str
        :param ExtThird: Custom 3
        :type ExtThird: str
        :param ExtFirst: Custom 1
        :type ExtFirst: str
        :param NetType: Network type
        :type NetType: str
        :param Device: Model
        :type Device: str
        :param IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param Os: OS
        :type Os: str
        :param Browser: Browser
        :type Browser: str
        :param CostType: Duration calculation method
        :type CostType: str
        :param Url: Source
        :type Url: str
        :param Env: Environment
        :type Env: str
        """
        self.StartTime = None
        self.Type = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.CostType = None
        self.Url = None
        self.Env = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.CostType = params.get("CostType")
        self.Url = params.get("Url")
        self.Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataFetchUrlInfoResponse(AbstractModel):
    """DescribeDataFetchUrlInfo response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned value
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataFetchUrlRequest(AbstractModel):
    """DescribeDataFetchUrl request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: int
        :param Type: `allcount`: performance view; `day`: 14-day data; `count40x`: HTTP status codes 40X view; `count50x`: HTTP status codes 50X view; `count5xand4x`: HTTP status codes 40X∑50X view; `top`: top resources view; `nettype`/`version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: network/platform view; version view; device view; ISP view; region view; browser view; custom view, and so on.
        :type Type: str
        :param EndTime: End time
        :type EndTime: int
        :param ID: Project ID
        :type ID: int
        :param ExtSecond: Custom 2
        :type ExtSecond: str
        :param Engine: Browser engine
        :type Engine: str
        :param Isp: ISP
        :type Isp: str
        :param From: Source page
        :type From: str
        :param Level: Log level
        :type Level: str
        :param Brand: Brand
        :type Brand: str
        :param Area: Region
        :type Area: str
        :param VersionNum: Version
        :type VersionNum: str
        :param Platform: Platform
        :type Platform: str
        :param ExtThird: Custom 3
        :type ExtThird: str
        :param ExtFirst: Custom 1
        :type ExtFirst: str
        :param NetType: Network type
        :type NetType: str
        :param Device: Model
        :type Device: str
        :param IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param Os: OS
        :type Os: str
        :param Browser: Browser
        :type Browser: str
        :param CostType: Duration calculation method
        :type CostType: str
        :param Url: Source
        :type Url: str
        :param Env: Environment
        :type Env: str
        :param Status: HTTP status code.
        :type Status: str
        :param Ret: retcode
        :type Ret: str
        :param NetStatus: Network status
        :type NetStatus: str
        """
        self.StartTime = None
        self.Type = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.CostType = None
        self.Url = None
        self.Env = None
        self.Status = None
        self.Ret = None
        self.NetStatus = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.CostType = params.get("CostType")
        self.Url = params.get("Url")
        self.Env = params.get("Env")
        self.Status = params.get("Status")
        self.Ret = params.get("Ret")
        self.NetStatus = params.get("NetStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataFetchUrlResponse(AbstractModel):
    """DescribeDataFetchUrl response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned value
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataLogUrlInfoRequest(AbstractModel):
    """DescribeDataLogUrlInfo request structure.

    """

    def __init__(self):
        r"""
        :param ID: Project ID
        :type ID: int
        :param StartTime: Timestamp
        :type StartTime: int
        :param EndTime: Timestamp
        :type EndTime: int
        """
        self.ID = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataLogUrlInfoResponse(AbstractModel):
    """DescribeDataLogUrlInfo response structure.

    """

    def __init__(self):
        r"""
        :param Result: Response string
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataLogUrlStatisticsRequest(AbstractModel):
    """DescribeDataLogUrlStatistics request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: int
        :param Type: `analysis`: exception analysis; `compare`: exception list comparison; `allcount`: performance view; `condition`: condition list; `nettype`/`version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: network/platform view; version view; device view; ISP view; region view; browser view; custom view, and so on.
        :type Type: str
        :param EndTime: End time
        :type EndTime: int
        :param ID: Project ID
        :type ID: int
        :param ExtSecond: Custom 2
        :type ExtSecond: str
        :param Engine: Browser engine
        :type Engine: str
        :param Isp: ISP
        :type Isp: str
        :param From: Source page
        :type From: str
        :param Level: Log level
        :type Level: str
        :param Brand: Brand
        :type Brand: str
        :param Area: Region
        :type Area: str
        :param VersionNum: Version
        :type VersionNum: str
        :param Platform: Platform
        :type Platform: str
        :param ExtThird: Custom 3
        :type ExtThird: str
        :param ExtFirst: Custom 1
        :type ExtFirst: str
        :param NetType: Network type
        :type NetType: str
        :param Device: Model
        :type Device: str
        :param IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param Os: OS
        :type Os: str
        :param Browser: Browser
        :type Browser: str
        :param Env: Environment
        :type Env: str
        """
        self.StartTime = None
        self.Type = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.Env = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataLogUrlStatisticsResponse(AbstractModel):
    """DescribeDataLogUrlStatistics response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned value
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataPerformancePageRequest(AbstractModel):
    """DescribeDataPerformancePage request structure.

    """

    def __init__(self):
        r"""
        :param ID: Project ID
        :type ID: int
        :param StartTime: Start time
        :type StartTime: int
        :param EndTime: End time
        :type EndTime: int
        :param Type: `pagepv`: PV view; `allcount`: performance view; `falls`: page loading waterfall plot; `samp`: FMP, `day`: 14-day data, `nettype`: network/platform view; `performance`: top underperformed pages view; `version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: version view; device view; ISP view; region view; browser view, and so on.
        :type Type: str
        :param Level: Log level
        :type Level: str
        :param Isp: ISP
        :type Isp: str
        :param Area: Region
        :type Area: str
        :param NetType: Network type
        :type NetType: str
        :param Platform: Platform
        :type Platform: str
        :param Device: Model
        :type Device: str
        :param VersionNum: Version
        :type VersionNum: str
        :param ExtFirst: Custom 1
        :type ExtFirst: str
        :param ExtSecond: Custom 2
        :type ExtSecond: str
        :param ExtThird: Custom 3
        :type ExtThird: str
        :param IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param Browser: Browser
        :type Browser: str
        :param Os: OS
        :type Os: str
        :param Engine: Browser engine
        :type Engine: str
        :param Brand: Brand
        :type Brand: str
        :param From: Source page
        :type From: str
        :param CostType: Duration calculation method
        :type CostType: str
        :param Env: Environment variable
        :type Env: str
        :param NetStatus: Network status
        :type NetStatus: str
        """
        self.ID = None
        self.StartTime = None
        self.EndTime = None
        self.Type = None
        self.Level = None
        self.Isp = None
        self.Area = None
        self.NetType = None
        self.Platform = None
        self.Device = None
        self.VersionNum = None
        self.ExtFirst = None
        self.ExtSecond = None
        self.ExtThird = None
        self.IsAbroad = None
        self.Browser = None
        self.Os = None
        self.Engine = None
        self.Brand = None
        self.From = None
        self.CostType = None
        self.Env = None
        self.NetStatus = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Type = params.get("Type")
        self.Level = params.get("Level")
        self.Isp = params.get("Isp")
        self.Area = params.get("Area")
        self.NetType = params.get("NetType")
        self.Platform = params.get("Platform")
        self.Device = params.get("Device")
        self.VersionNum = params.get("VersionNum")
        self.ExtFirst = params.get("ExtFirst")
        self.ExtSecond = params.get("ExtSecond")
        self.ExtThird = params.get("ExtThird")
        self.IsAbroad = params.get("IsAbroad")
        self.Browser = params.get("Browser")
        self.Os = params.get("Os")
        self.Engine = params.get("Engine")
        self.Brand = params.get("Brand")
        self.From = params.get("From")
        self.CostType = params.get("CostType")
        self.Env = params.get("Env")
        self.NetStatus = params.get("NetStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataPerformancePageResponse(AbstractModel):
    """DescribeDataPerformancePage response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned value
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataPerformanceProjectRequest(AbstractModel):
    """DescribeDataPerformanceProject request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: int
        :param Type: `allcount`; performance view; `falls`: page loading waterfall plot; `samp`: FMP, `day`: 14-day data, `nettype`: network/platform view; `performance`: top underperformed pages view; `condition`: condition list; `area`: request speed distribution; `version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: version view; device view; ISP view; region view; browser view, and so on.
        :type Type: str
        :param EndTime: End time
        :type EndTime: int
        :param ID: Project ID
        :type ID: int
        :param ExtSecond: Custom 2
        :type ExtSecond: str
        :param Engine: Browser engine
        :type Engine: str
        :param Isp: ISP
        :type Isp: str
        :param From: Source page
        :type From: str
        :param Level: Log level
        :type Level: str
        :param Brand: Brand
        :type Brand: str
        :param Area: Region
        :type Area: str
        :param VersionNum: Version
        :type VersionNum: str
        :param Platform: Platform
        :type Platform: str
        :param ExtThird: Custom 3
        :type ExtThird: str
        :param ExtFirst: Custom 1
        :type ExtFirst: str
        :param NetType: Network type
        :type NetType: str
        :param Device: Model
        :type Device: str
        :param IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param Os: OS
        :type Os: str
        :param Browser: Browser
        :type Browser: str
        :param CostType: Duration calculation
        :type CostType: str
        :param Env: Environment
        :type Env: str
        """
        self.StartTime = None
        self.Type = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.CostType = None
        self.Env = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.CostType = params.get("CostType")
        self.Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataPerformanceProjectResponse(AbstractModel):
    """DescribeDataPerformanceProject response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned value
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataPvUrlInfoRequest(AbstractModel):
    """DescribeDataPvUrlInfo request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: int
        :param Type: Type
        :type Type: str
        :param EndTime: End time
        :type EndTime: int
        :param ID: Project ID
        :type ID: int
        :param ExtSecond: Custom 2
        :type ExtSecond: str
        :param Engine: Browser engine
        :type Engine: str
        :param Isp: ISP
        :type Isp: str
        :param From: Source page
        :type From: str
        :param Level: Log level
        :type Level: str
        :param Brand: Brand
        :type Brand: str
        :param Area: Region
        :type Area: str
        :param VersionNum: Version
        :type VersionNum: str
        :param Platform: Platform
        :type Platform: str
        :param ExtThird: Custom 3
        :type ExtThird: str
        :param ExtFirst: Custom 1
        :type ExtFirst: str
        :param NetType: Network type
        :type NetType: str
        :param Device: Model
        :type Device: str
        :param IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param Os: OS
        :type Os: str
        :param Browser: Browser
        :type Browser: str
        :param Env: Environment
        :type Env: str
        """
        self.StartTime = None
        self.Type = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.Env = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataPvUrlInfoResponse(AbstractModel):
    """DescribeDataPvUrlInfo response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned value
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataPvUrlStatisticsRequest(AbstractModel):
    """DescribeDataPvUrlStatistics request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: int
        :param Type: `allcount`; performance view; `day`: 14-day data, `vp`: performance; `ckuv`: UV; `ckpv`: PV; `condition`: condition list; `nettype`/`version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: network/platform view; version view; device view; ISP view; region view; browser view; custom view, and so on.
        :type Type: str
        :param EndTime: End time
        :type EndTime: int
        :param ID: Project ID
        :type ID: int
        :param ExtSecond: Custom 2
        :type ExtSecond: str
        :param Engine: Browser engine
        :type Engine: str
        :param Isp: ISP
        :type Isp: str
        :param From: Source page
        :type From: str
        :param Level: Log level
        :type Level: str
        :param Brand: Brand
        :type Brand: str
        :param Area: Region
        :type Area: str
        :param VersionNum: Version
        :type VersionNum: str
        :param Platform: Platform
        :type Platform: str
        :param ExtThird: Custom 3
        :type ExtThird: str
        :param ExtFirst: Custom 1
        :type ExtFirst: str
        :param NetType: Network type
        :type NetType: str
        :param Device: Model
        :type Device: str
        :param IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param Os: OS
        :type Os: str
        :param Browser: Browser
        :type Browser: str
        :param Env: Environment
        :type Env: str
        """
        self.StartTime = None
        self.Type = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.Env = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataPvUrlStatisticsResponse(AbstractModel):
    """DescribeDataPvUrlStatistics response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned value
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataReportCountRequest(AbstractModel):
    """DescribeDataReportCount request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: int
        :param EndTime: End time
        :type EndTime: int
        :param ID: Project ID
        :type ID: int
        :param ReportType: Reporting type
        :type ReportType: str
        :param InstanceID: Instance ID
        :type InstanceID: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ID = None
        self.ReportType = None
        self.InstanceID = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ReportType = params.get("ReportType")
        self.InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataReportCountResponse(AbstractModel):
    """DescribeDataReportCount response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned value
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataRequest(AbstractModel):
    """DescribeData request structure.

    """

    def __init__(self):
        r"""
        :param Query: Query string
        :type Query: str
        :param ID: Project ID
        :type ID: int
        """
        self.Query = None
        self.ID = None


    def _deserialize(self, params):
        self.Query = params.get("Query")
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataResponse(AbstractModel):
    """DescribeData response structure.

    """

    def __init__(self):
        r"""
        :param Result: Response string
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataSetUrlStatisticsRequest(AbstractModel):
    """DescribeDataSetUrlStatistics request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: int
        :param Type: `allcount`: performance view; `data`: mini program; `component`: mini program-related components; `day`: 14-day data; `nettype`: network/platform view; `performance`: top underperformed pages view; `version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: version view; device view; ISP view; region view; browser view, and so on.
        :type Type: str
        :param EndTime: End time
        :type EndTime: int
        :param ID: Project ID
        :type ID: int
        :param ExtSecond: Custom 2
        :type ExtSecond: str
        :param Engine: Browser engine
        :type Engine: str
        :param Isp: ISP
        :type Isp: str
        :param From: Source page
        :type From: str
        :param Level: Log level
        :type Level: str
        :param Brand: Brand
        :type Brand: str
        :param Area: Region
        :type Area: str
        :param VersionNum: Version
        :type VersionNum: str
        :param Platform: Platform
        :type Platform: str
        :param ExtThird: Custom 3
        :type ExtThird: str
        :param ExtFirst: Custom 1
        :type ExtFirst: str
        :param NetType: Network type
        :type NetType: str
        :param Device: Model
        :type Device: str
        :param IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param Os: OS
        :type Os: str
        :param Browser: Browser
        :type Browser: str
        :param CostType: Duration calculation
        :type CostType: str
        :param Env: Environment
        :type Env: str
        :param PackageType: The obtained package.
        :type PackageType: str
        """
        self.StartTime = None
        self.Type = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.CostType = None
        self.Env = None
        self.PackageType = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.CostType = params.get("CostType")
        self.Env = params.get("Env")
        self.PackageType = params.get("PackageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataSetUrlStatisticsResponse(AbstractModel):
    """DescribeDataSetUrlStatistics response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned value
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataStaticProjectRequest(AbstractModel):
    """DescribeDataStaticProject request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: int
        :param Type: `allcount`: performance view; `day`: 14-day data; `condition`: condition list; `area`: request speed distribution; `nettype`/`version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: network/platform view; version view; device view; ISP view; region view; browser view; custom view, and so on.
        :type Type: str
        :param EndTime: End time
        :type EndTime: int
        :param ID: Project ID
        :type ID: int
        :param ExtSecond: Custom 2
        :type ExtSecond: str
        :param Engine: Browser engine
        :type Engine: str
        :param Isp: ISP
        :type Isp: str
        :param From: Source page
        :type From: str
        :param Level: Log level
        :type Level: str
        :param Brand: Brand
        :type Brand: str
        :param Area: Region
        :type Area: str
        :param VersionNum: Version
        :type VersionNum: str
        :param Platform: Platform
        :type Platform: str
        :param ExtThird: Custom 3
        :type ExtThird: str
        :param ExtFirst: Custom 1
        :type ExtFirst: str
        :param NetType: Network type
        :type NetType: str
        :param Device: Model
        :type Device: str
        :param IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param Os: OS
        :type Os: str
        :param Browser: Browser
        :type Browser: str
        :param CostType: Duration calculation
        :type CostType: str
        :param Url: Source
        :type Url: list of str
        :param Env: Environment
        :type Env: str
        """
        self.StartTime = None
        self.Type = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.CostType = None
        self.Url = None
        self.Env = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.CostType = params.get("CostType")
        self.Url = params.get("Url")
        self.Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataStaticProjectResponse(AbstractModel):
    """DescribeDataStaticProject response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned value
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataStaticResourceRequest(AbstractModel):
    """DescribeDataStaticResource request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: int
        :param Type: `top`: top resources view; `count40x`: HTTP status codes 40X view; `nettype`/`version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: network/platform view; version view; device view; ISP view; region view; browser view; custom view, and so on.
        :type Type: str
        :param EndTime: End time
        :type EndTime: int
        :param ID: Project ID
        :type ID: int
        :param ExtSecond: Custom 2
        :type ExtSecond: str
        :param Engine: Browser engine
        :type Engine: str
        :param Isp: ISP
        :type Isp: str
        :param From: Source page
        :type From: str
        :param Level: Log level
        :type Level: str
        :param Brand: Brand
        :type Brand: str
        :param Area: Region
        :type Area: str
        :param VersionNum: Version
        :type VersionNum: str
        :param Platform: Platform
        :type Platform: str
        :param ExtThird: Custom 3
        :type ExtThird: str
        :param ExtFirst: Custom 1
        :type ExtFirst: str
        :param NetType: Network type
        :type NetType: str
        :param Device: Model
        :type Device: str
        :param IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param Os: OS
        :type Os: str
        :param Browser: Browser
        :type Browser: str
        :param CostType: Duration calculation method
        :type CostType: str
        :param Url: Source
        :type Url: str
        :param Env: Environment
        :type Env: str
        """
        self.StartTime = None
        self.Type = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.CostType = None
        self.Url = None
        self.Env = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.CostType = params.get("CostType")
        self.Url = params.get("Url")
        self.Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataStaticResourceResponse(AbstractModel):
    """DescribeDataStaticResource response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned value
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataStaticUrlRequest(AbstractModel):
    """DescribeDataStaticUrl request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: int
        :param Type: `pagepv`: page view; `nettype`/`version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: network/platform view; version view; device view; ISP view; region view; browser view; custom view, and so on.
        :type Type: str
        :param EndTime: End time
        :type EndTime: int
        :param ID: Project ID
        :type ID: int
        :param ExtSecond: Custom 2
        :type ExtSecond: str
        :param Engine: Browser engine
        :type Engine: str
        :param Isp: ISP
        :type Isp: str
        :param From: Source page
        :type From: str
        :param Level: Log level
        :type Level: str
        :param Brand: Brand
        :type Brand: str
        :param Area: Region
        :type Area: str
        :param VersionNum: Version
        :type VersionNum: str
        :param Platform: Platform
        :type Platform: str
        :param ExtThird: Custom 3
        :type ExtThird: str
        :param ExtFirst: Custom 1
        :type ExtFirst: str
        :param NetType: Network type
        :type NetType: str
        :param Device: Model
        :type Device: str
        :param IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param Os: OS
        :type Os: str
        :param Browser: Browser
        :type Browser: str
        :param CostType: Duration calculation method
        :type CostType: str
        :param Url: Source
        :type Url: str
        :param Env: Environment
        :type Env: str
        """
        self.StartTime = None
        self.Type = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.CostType = None
        self.Url = None
        self.Env = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.CostType = params.get("CostType")
        self.Url = params.get("Url")
        self.Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataStaticUrlResponse(AbstractModel):
    """DescribeDataStaticUrl response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned value
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataWebVitalsPageRequest(AbstractModel):
    """DescribeDataWebVitalsPage request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: int
        :param EndTime: End time
        :type EndTime: int
        :param ID: Project ID
        :type ID: int
        :param ExtSecond: Custom 2
        :type ExtSecond: str
        :param Engine: Browser engine
        :type Engine: str
        :param Isp: ISP
        :type Isp: str
        :param From: Source page
        :type From: str
        :param Level: Log level
        :type Level: str
        :param Type: No type yet
        :type Type: str
        :param Brand: Brand
        :type Brand: str
        :param Area: Region
        :type Area: str
        :param VersionNum: Version
        :type VersionNum: str
        :param Platform: Platform
        :type Platform: str
        :param ExtThird: Custom 3
        :type ExtThird: str
        :param ExtFirst: Custom 1
        :type ExtFirst: str
        :param NetType: Network type
        :type NetType: str
        :param Device: Model
        :type Device: str
        :param IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param Os: OS
        :type Os: str
        :param Browser: Browser
        :type Browser: str
        :param CostType: Duration calculation
        :type CostType: str
        :param Env: Environment
        :type Env: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Type = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.CostType = None
        self.Env = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Type = params.get("Type")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.CostType = params.get("CostType")
        self.Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataWebVitalsPageResponse(AbstractModel):
    """DescribeDataWebVitalsPage response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned value
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeErrorRequest(AbstractModel):
    """DescribeError request structure.

    """

    def __init__(self):
        r"""
        :param Date: Date
        :type Date: str
        :param ID: Project ID
        :type ID: int
        """
        self.Date = None
        self.ID = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeErrorResponse(AbstractModel):
    """DescribeError response structure.

    """

    def __init__(self):
        r"""
        :param Content: Content
        :type Content: str
        :param ID: Project ID
        :type ID: int
        :param CreateTime: Time
        :type CreateTime: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Content = None
        self.ID = None
        self.CreateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.ID = params.get("ID")
        self.CreateTime = params.get("CreateTime")
        self.RequestId = params.get("RequestId")


class DescribeLogExportsRequest(AbstractModel):
    """DescribeLogExports request structure.

    """

    def __init__(self):
        r"""
        :param ID: Project ID
        :type ID: int
        """
        self.ID = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogExportsResponse(AbstractModel):
    """DescribeLogExports response structure.

    """

    def __init__(self):
        r"""
        :param LogExportSet: List of log export records
        :type LogExportSet: list of LogExport
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LogExportSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LogExportSet") is not None:
            self.LogExportSet = []
            for item in params.get("LogExportSet"):
                obj = LogExport()
                obj._deserialize(item)
                self.LogExportSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLogListRequest(AbstractModel):
    """DescribeLogList request structure.

    """

    def __init__(self):
        r"""
        :param Sort: Sorting order (required). Valid values: `desc`, `asc`.
        :type Sort: str
        :param ActionType: This parameter is required. Valid values: `searchlog`, `histogram`.
        :type ActionType: str
        :param ID: Project ID (required)
        :type ID: int
        :param StartTime: Start time (required)
        :type StartTime: str
        :param Limit: The number of raw logs returned for a single query. This parameter is required. Maximum value: 100.
        :type Limit: int
        :param Context: Context, which is used to load more logs. Pass through the last `Context` value returned to get more log content (up to 10,000 raw logs). It will expire after 1 hour
        :type Context: str
        :param Query: Query statement, which is required and can contain up to 4,096 characters, such as "id:120001 AND type:\"log\"".
        :type Query: str
        :param EndTime: End time (required)
        :type EndTime: str
        """
        self.Sort = None
        self.ActionType = None
        self.ID = None
        self.StartTime = None
        self.Limit = None
        self.Context = None
        self.Query = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Sort = params.get("Sort")
        self.ActionType = params.get("ActionType")
        self.ID = params.get("ID")
        self.StartTime = params.get("StartTime")
        self.Limit = params.get("Limit")
        self.Context = params.get("Context")
        self.Query = params.get("Query")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogListResponse(AbstractModel):
    """DescribeLogList response structure.

    """

    def __init__(self):
        r"""
        :param Result: Response string
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeOfflineLogConfigsRequest(AbstractModel):
    """DescribeOfflineLogConfigs request structure.

    """

    def __init__(self):
        r"""
        :param ProjectKey: Unique project key for reporting
        :type ProjectKey: str
        """
        self.ProjectKey = None


    def _deserialize(self, params):
        self.ProjectKey = params.get("ProjectKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOfflineLogConfigsResponse(AbstractModel):
    """DescribeOfflineLogConfigs response structure.

    """

    def __init__(self):
        r"""
        :param Msg: API call information
        :type Msg: str
        :param UniqueIDSet: Array of unique user identifiers
        :type UniqueIDSet: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Msg = None
        self.UniqueIDSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.UniqueIDSet = params.get("UniqueIDSet")
        self.RequestId = params.get("RequestId")


class DescribeOfflineLogRecordsRequest(AbstractModel):
    """DescribeOfflineLogRecords request structure.

    """

    def __init__(self):
        r"""
        :param ProjectKey: Unique project key for reporting
        :type ProjectKey: str
        """
        self.ProjectKey = None


    def _deserialize(self, params):
        self.ProjectKey = params.get("ProjectKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOfflineLogRecordsResponse(AbstractModel):
    """DescribeOfflineLogRecords response structure.

    """

    def __init__(self):
        r"""
        :param Msg: API call information
        :type Msg: str
        :param RecordSet: Array of record IDs
        :type RecordSet: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Msg = None
        self.RecordSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.RecordSet = params.get("RecordSet")
        self.RequestId = params.get("RequestId")


class DescribeOfflineLogsRequest(AbstractModel):
    """DescribeOfflineLogs request structure.

    """

    def __init__(self):
        r"""
        :param ProjectKey: Unique project key for reporting
        :type ProjectKey: str
        :param FileIDs: List of offline log file IDs
        :type FileIDs: list of str
        """
        self.ProjectKey = None
        self.FileIDs = None


    def _deserialize(self, params):
        self.ProjectKey = params.get("ProjectKey")
        self.FileIDs = params.get("FileIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOfflineLogsResponse(AbstractModel):
    """DescribeOfflineLogs response structure.

    """

    def __init__(self):
        r"""
        :param Msg: API call response
        :type Msg: str
        :param LogSet: Log list
        :type LogSet: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Msg = None
        self.LogSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.LogSet = params.get("LogSet")
        self.RequestId = params.get("RequestId")


class DescribeProjectLimitsRequest(AbstractModel):
    """DescribeProjectLimits request structure.

    """

    def __init__(self):
        r"""
        :param ProjectID: Project ID
        :type ProjectID: int
        """
        self.ProjectID = None


    def _deserialize(self, params):
        self.ProjectID = params.get("ProjectID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectLimitsResponse(AbstractModel):
    """DescribeProjectLimits response structure.

    """

    def __init__(self):
        r"""
        :param ProjectLimitSet: Array of reporting rates
        :type ProjectLimitSet: list of ProjectLimit
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ProjectLimitSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProjectLimitSet") is not None:
            self.ProjectLimitSet = []
            for item in params.get("ProjectLimitSet"):
                obj = ProjectLimit()
                obj._deserialize(item)
                self.ProjectLimitSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProjectsRequest(AbstractModel):
    """DescribeProjects request structure.

    """

    def __init__(self):
        r"""
        :param Limit: Number of items per page (integer)
        :type Limit: int
        :param Offset: Page number (integer)
        :type Offset: int
        :param Filters: Filter parameter. Pass in {"Name": "IsDemo", "Values":["1"]} for the demo mode.
        :type Filters: list of Filter
        :param IsDemo: This parameter has been disused. You need to indicate whether the demo mode is used in `Filters`.
        :type IsDemo: int
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.IsDemo = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.IsDemo = params.get("IsDemo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectsResponse(AbstractModel):
    """DescribeProjects response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of items in the list
        :type TotalCount: int
        :param ProjectSet: Project list
        :type ProjectSet: list of RumProject
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.ProjectSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ProjectSet") is not None:
            self.ProjectSet = []
            for item in params.get("ProjectSet"):
                obj = RumProject()
                obj._deserialize(item)
                self.ProjectSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePvListRequest(AbstractModel):
    """DescribePvList request structure.

    """

    def __init__(self):
        r"""
        :param ProjectId: ID
        :type ProjectId: int
        :param EndTime: End time
        :type EndTime: str
        :param StartTime: Start time
        :type StartTime: str
        :param Dimension: Get day:d (leave this parameter empty if to get min)
        :type Dimension: str
        """
        self.ProjectId = None
        self.EndTime = None
        self.StartTime = None
        self.Dimension = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        self.Dimension = params.get("Dimension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePvListResponse(AbstractModel):
    """DescribePvList response structure.

    """

    def __init__(self):
        r"""
        :param ProjectPvSet: PV list
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectPvSet: list of RumPvInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ProjectPvSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProjectPvSet") is not None:
            self.ProjectPvSet = []
            for item in params.get("ProjectPvSet"):
                obj = RumPvInfo()
                obj._deserialize(item)
                self.ProjectPvSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeReleaseFileSignRequest(AbstractModel):
    """DescribeReleaseFileSign request structure.

    """

    def __init__(self):
        r"""
        :param Timeout: Timeout period. If it is not set, it will be 5 minutes by default
        :type Timeout: int
        """
        self.Timeout = None


    def _deserialize(self, params):
        self.Timeout = params.get("Timeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReleaseFileSignResponse(AbstractModel):
    """DescribeReleaseFileSign response structure.

    """

    def __init__(self):
        r"""
        :param SecretKey: Temporary key
        :type SecretKey: str
        :param SecretID: Temporary key ID
        :type SecretID: str
        :param SessionToken: Temporary key token
        :type SessionToken: str
        :param StartTime: Start timestamp
        :type StartTime: int
        :param ExpiredTime: Expiration timestamp
        :type ExpiredTime: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SecretKey = None
        self.SecretID = None
        self.SessionToken = None
        self.StartTime = None
        self.ExpiredTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretKey = params.get("SecretKey")
        self.SecretID = params.get("SecretID")
        self.SessionToken = params.get("SessionToken")
        self.StartTime = params.get("StartTime")
        self.ExpiredTime = params.get("ExpiredTime")
        self.RequestId = params.get("RequestId")


class DescribeReleaseFilesRequest(AbstractModel):
    """DescribeReleaseFiles request structure.

    """

    def __init__(self):
        r"""
        :param ProjectID: Project ID
        :type ProjectID: int
        :param FileVersion: File version
        :type FileVersion: str
        """
        self.ProjectID = None
        self.FileVersion = None


    def _deserialize(self, params):
        self.ProjectID = params.get("ProjectID")
        self.FileVersion = params.get("FileVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReleaseFilesResponse(AbstractModel):
    """DescribeReleaseFiles response structure.

    """

    def __init__(self):
        r"""
        :param Files: File information list
        :type Files: list of ReleaseFile
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Files = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Files") is not None:
            self.Files = []
            for item in params.get("Files"):
                obj = ReleaseFile()
                obj._deserialize(item)
                self.Files.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRumGroupLogRequest(AbstractModel):
    """DescribeRumGroupLog request structure.

    """

    def __init__(self):
        r"""
        :param OrderBy: Sorting order (required). Valid values: `desc`, `asc`.
        :type OrderBy: str
        :param StartTime: Start time (required)
        :type StartTime: str
        :param Limit: The number of raw logs returned for a single query. This parameter is required. Maximum value: `100`.
        :type Limit: int
        :param Page: Page number
        :type Page: int
        :param Query: Query statement, which is required and can contain up to 4,096 characters.
        :type Query: str
        :param EndTime: End time (required)
        :type EndTime: str
        :param ID: Project ID (required)
        :type ID: int
        :param GroupField: Aggregate field
        :type GroupField: str
        """
        self.OrderBy = None
        self.StartTime = None
        self.Limit = None
        self.Page = None
        self.Query = None
        self.EndTime = None
        self.ID = None
        self.GroupField = None


    def _deserialize(self, params):
        self.OrderBy = params.get("OrderBy")
        self.StartTime = params.get("StartTime")
        self.Limit = params.get("Limit")
        self.Page = params.get("Page")
        self.Query = params.get("Query")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.GroupField = params.get("GroupField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumGroupLogResponse(AbstractModel):
    """DescribeRumGroupLog response structure.

    """

    def __init__(self):
        r"""
        :param Result: Response string
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeRumLogListRequest(AbstractModel):
    """DescribeRumLogList request structure.

    """

    def __init__(self):
        r"""
        :param OrderBy: Sorting order (required). Valid values: `desc`, `asc`.
        :type OrderBy: str
        :param StartTime: Start time (required)
        :type StartTime: str
        :param Limit: The number of raw logs returned for a single query. This parameter is required. Maximum value: `100`.
        :type Limit: int
        :param Page: Page number
        :type Page: int
        :param Query: Query statement, which is required and can contain up to 4,096 characters.
        :type Query: str
        :param EndTime: End time (required)
        :type EndTime: str
        :param ID: Project ID (required)
        :type ID: int
        """
        self.OrderBy = None
        self.StartTime = None
        self.Limit = None
        self.Page = None
        self.Query = None
        self.EndTime = None
        self.ID = None


    def _deserialize(self, params):
        self.OrderBy = params.get("OrderBy")
        self.StartTime = params.get("StartTime")
        self.Limit = params.get("Limit")
        self.Page = params.get("Page")
        self.Query = params.get("Query")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumLogListResponse(AbstractModel):
    """DescribeRumLogList response structure.

    """

    def __init__(self):
        r"""
        :param Result: Response string
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeRumStatsLogListRequest(AbstractModel):
    """DescribeRumStatsLogList request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time (required)
        :type StartTime: str
        :param Limit: The number of raw logs returned for a single query. This parameter is required. Maximum value: `100`.
        :type Limit: int
        :param Query: Query statement, which is required and can contain up to 4,096 characters.
        :type Query: str
        :param EndTime: End time (required)
        :type EndTime: str
        :param ID: Project ID (required)
        :type ID: int
        """
        self.StartTime = None
        self.Limit = None
        self.Query = None
        self.EndTime = None
        self.ID = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Limit = params.get("Limit")
        self.Query = params.get("Query")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumStatsLogListResponse(AbstractModel):
    """DescribeRumStatsLogList response structure.

    """

    def __init__(self):
        r"""
        :param Result: Response string
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeScoresRequest(AbstractModel):
    """DescribeScores request structure.

    """

    def __init__(self):
        r"""
        :param EndTime: End time
        :type EndTime: str
        :param StartTime: Start time
        :type StartTime: str
        :param ID: Project ID
        :type ID: int
        :param IsDemo: This parameter has been disused.
        :type IsDemo: int
        """
        self.EndTime = None
        self.StartTime = None
        self.ID = None
        self.IsDemo = None


    def _deserialize(self, params):
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        self.ID = params.get("ID")
        self.IsDemo = params.get("IsDemo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScoresResponse(AbstractModel):
    """DescribeScores response structure.

    """

    def __init__(self):
        r"""
        :param ScoreSet: Array
        :type ScoreSet: list of ScoreInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ScoreSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ScoreSet") is not None:
            self.ScoreSet = []
            for item in params.get("ScoreSet"):
                obj = ScoreInfo()
                obj._deserialize(item)
                self.ScoreSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTawAreasRequest(AbstractModel):
    """DescribeTawAreas request structure.

    """

    def __init__(self):
        r"""
        :param AreaIds: Region ID
        :type AreaIds: list of int
        :param AreaKeys: Region key
        :type AreaKeys: list of str
        :param Limit: Pagination limit
        :type Limit: int
        :param AreaStatuses: Region status (1: valid; 2: invalid)
        :type AreaStatuses: list of int
        :param Offset: Pagination offset
        :type Offset: int
        """
        self.AreaIds = None
        self.AreaKeys = None
        self.Limit = None
        self.AreaStatuses = None
        self.Offset = None


    def _deserialize(self, params):
        self.AreaIds = params.get("AreaIds")
        self.AreaKeys = params.get("AreaKeys")
        self.Limit = params.get("Limit")
        self.AreaStatuses = params.get("AreaStatuses")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTawAreasResponse(AbstractModel):
    """DescribeTawAreas response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of regions
        :type TotalCount: int
        :param AreaSet: Region list
        :type AreaSet: list of RumAreaInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.AreaSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AreaSet") is not None:
            self.AreaSet = []
            for item in params.get("AreaSet"):
                obj = RumAreaInfo()
                obj._deserialize(item)
                self.AreaSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUvListRequest(AbstractModel):
    """DescribeUvList request structure.

    """

    def __init__(self):
        r"""
        :param ProjectId: ID
        :type ProjectId: int
        :param EndTime: End time
        :type EndTime: str
        :param StartTime: Start time
        :type StartTime: str
        :param Dimension: Get day:d min:m
        :type Dimension: str
        """
        self.ProjectId = None
        self.EndTime = None
        self.StartTime = None
        self.Dimension = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        self.Dimension = params.get("Dimension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUvListResponse(AbstractModel):
    """DescribeUvList response structure.

    """

    def __init__(self):
        r"""
        :param ProjectUvSet: UV list
        :type ProjectUvSet: list of RumUvInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ProjectUvSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProjectUvSet") is not None:
            self.ProjectUvSet = []
            for item in params.get("ProjectUvSet"):
                obj = RumUvInfo()
                obj._deserialize(item)
                self.ProjectUvSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWhitelistsRequest(AbstractModel):
    """DescribeWhitelists request structure.

    """

    def __init__(self):
        r"""
        :param InstanceID: Instance ID
        :type InstanceID: str
        """
        self.InstanceID = None


    def _deserialize(self, params):
        self.InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhitelistsResponse(AbstractModel):
    """DescribeWhitelists response structure.

    """

    def __init__(self):
        r"""
        :param WhitelistSet: Allowlist list
        :type WhitelistSet: list of Whitelist
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.WhitelistSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WhitelistSet") is not None:
            self.WhitelistSet = []
            for item in params.get("WhitelistSet"):
                obj = Whitelist()
                obj._deserialize(item)
                self.WhitelistSet.append(obj)
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """Key-Value pair filter for conditional filtering queries, such as filtering ID, name, status, etc.

    · If more than one filter exists, the logical relationship between these filters is `AND`.
    · If multiple values exist in one filter, the logical relationship between these values is `OR`.

    """

    def __init__(self):
        r"""
        :param Values: One or more filter values.
        :type Values: list of str
        :param Name: Filter name.
        :type Name: str
        """
        self.Values = None
        self.Name = None


    def _deserialize(self, params):
        self.Values = params.get("Values")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogExport(AbstractModel):
    """Log export record

    """

    def __init__(self):
        r"""
        :param CosPath: Log export path
        :type CosPath: str
        :param Count: Number of logs to be exported
        :type Count: int
        :param CreateTime: Log export task creation time
        :type CreateTime: str
        :param ExportID: Log export task ID
        :type ExportID: str
        :param FileName: Log export filename
        :type FileName: str
        :param FileSize: Log file size
        :type FileSize: int
        :param Format: Log export format
        :type Format: str
        :param Order: Log export time sorting
        :type Order: str
        :param Query: Log export query statement
        :type Query: str
        :param StartTime: Log export start time
        :type StartTime: str
        :param EndTime: Log export end time
        :type EndTime: str
        :param Status: Log download status. Valid values: Queuing: queuing; Processing: exporting; Complete: completed; Failed: failed; Expired: expired (3-day validity period).
        :type Status: str
        """
        self.CosPath = None
        self.Count = None
        self.CreateTime = None
        self.ExportID = None
        self.FileName = None
        self.FileSize = None
        self.Format = None
        self.Order = None
        self.Query = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None


    def _deserialize(self, params):
        self.CosPath = params.get("CosPath")
        self.Count = params.get("Count")
        self.CreateTime = params.get("CreateTime")
        self.ExportID = params.get("ExportID")
        self.FileName = params.get("FileName")
        self.FileSize = params.get("FileSize")
        self.Format = params.get("Format")
        self.Order = params.get("Order")
        self.Query = params.get("Query")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceRequest(AbstractModel):
    """ModifyInstance request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: ID of the instance to be modified
        :type InstanceId: str
        :param InstanceName: New instance name (up to 255 characters)
        :type InstanceName: str
        :param InstanceDesc: New instance description (up to 1,024 characters)
        :type InstanceDesc: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.InstanceDesc = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.InstanceDesc = params.get("InstanceDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceResponse(AbstractModel):
    """ModifyInstance response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyProjectLimitRequest(AbstractModel):
    """ModifyProjectLimit request structure.

    """

    def __init__(self):
        r"""
        :param ProjectID: Project ID
        :type ProjectID: int
        :param ProjectInterface: Project API
        :type ProjectInterface: str
        :param ReportRate: Reporting rate. 10 means 10%
        :type ReportRate: int
        :param ReportType: Reporting type. 1: rate; 2: number of reported data entries
        :type ReportType: int
        :param ID: Primary key ID
        :type ID: int
        """
        self.ProjectID = None
        self.ProjectInterface = None
        self.ReportRate = None
        self.ReportType = None
        self.ID = None


    def _deserialize(self, params):
        self.ProjectID = params.get("ProjectID")
        self.ProjectInterface = params.get("ProjectInterface")
        self.ReportRate = params.get("ReportRate")
        self.ReportType = params.get("ReportType")
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProjectLimitResponse(AbstractModel):
    """ModifyProjectLimit response structure.

    """

    def __init__(self):
        r"""
        :param Msg: Returned message
Note: this field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class ModifyProjectRequest(AbstractModel):
    """ModifyProject request structure.

    """

    def __init__(self):
        r"""
        :param ID: Project ID
        :type ID: int
        :param Name: Project name (optional, not empty, and up to 200 characters)
        :type Name: str
        :param URL: Project webpage URL (optional and up to 256 characters)
        :type URL: str
        :param Repo: Project repository address (optional and up to 256 characters)
        :type Repo: str
        :param InstanceID: ID of the instance to which to move the project (optional)
        :type InstanceID: str
        :param Rate: Project sample rate (optional)
        :type Rate: str
        :param EnableURLGroup: Whether to enable aggregation (optional)
        :type EnableURLGroup: int
        :param Type: Project type (valid values: "web", "mp", "android", "ios", "node", "hippy", "weex", "viola", "rn")
        :type Type: str
        :param Desc: Project description (optional and up to 1,000 characters)
        :type Desc: str
        """
        self.ID = None
        self.Name = None
        self.URL = None
        self.Repo = None
        self.InstanceID = None
        self.Rate = None
        self.EnableURLGroup = None
        self.Type = None
        self.Desc = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.Name = params.get("Name")
        self.URL = params.get("URL")
        self.Repo = params.get("Repo")
        self.InstanceID = params.get("InstanceID")
        self.Rate = params.get("Rate")
        self.EnableURLGroup = params.get("EnableURLGroup")
        self.Type = params.get("Type")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProjectResponse(AbstractModel):
    """ModifyProject response structure.

    """

    def __init__(self):
        r"""
        :param Msg: Operation information
        :type Msg: str
        :param ID: Project ID
        :type ID: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Msg = None
        self.ID = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.ID = params.get("ID")
        self.RequestId = params.get("RequestId")


class ProjectLimit(AbstractModel):
    """Project API restriction type

    """

    def __init__(self):
        r"""
        :param ID: Primary key ID
        :type ID: int
        :param ProjectID: Project ID
        :type ProjectID: int
        :param ProjectInterface: API
        :type ProjectInterface: str
        :param ReportRate: Reporting rate
        :type ReportRate: int
        :param ReportType: Reporting type. 1: reporting rate; 2: reporting count limit
        :type ReportType: int
        """
        self.ID = None
        self.ProjectID = None
        self.ProjectInterface = None
        self.ReportRate = None
        self.ReportType = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.ProjectID = params.get("ProjectID")
        self.ProjectInterface = params.get("ProjectInterface")
        self.ReportRate = params.get("ReportRate")
        self.ReportType = params.get("ReportType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseFile(AbstractModel):
    """Release file list (sourcemap)

    """

    def __init__(self):
        r"""
        :param Version: File version
        :type Version: str
        :param FileKey: Unique file key
        :type FileKey: str
        :param FileName: Filename
        :type FileName: str
        :param FileHash: File hash
        :type FileHash: str
        :param ID: File ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ID: int
        """
        self.Version = None
        self.FileKey = None
        self.FileName = None
        self.FileHash = None
        self.ID = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        self.FileKey = params.get("FileKey")
        self.FileName = params.get("FileName")
        self.FileHash = params.get("FileHash")
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeInstanceRequest(AbstractModel):
    """ResumeInstance request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: ID of the instance to be resumed
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeInstanceResponse(AbstractModel):
    """ResumeInstance response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RumAreaInfo(AbstractModel):
    """RUM region information

    """

    def __init__(self):
        r"""
        :param AreaId: Region ID
        :type AreaId: int
        :param AreaStatus: Region status (1: valid; 2: invalid)
        :type AreaStatus: int
        :param AreaName: Region name
        :type AreaName: str
        :param AreaKey: Region key
        :type AreaKey: str
        :param AreaRegionID: Region ID.
        :type AreaRegionID: str
        :param AreaRegionCode: Region code, such as “ap-xxx” (xxx is the region name).
        :type AreaRegionCode: str
        :param AreaAbbr: Region abbreviation.
        :type AreaAbbr: str
        """
        self.AreaId = None
        self.AreaStatus = None
        self.AreaName = None
        self.AreaKey = None
        self.AreaRegionID = None
        self.AreaRegionCode = None
        self.AreaAbbr = None


    def _deserialize(self, params):
        self.AreaId = params.get("AreaId")
        self.AreaStatus = params.get("AreaStatus")
        self.AreaName = params.get("AreaName")
        self.AreaKey = params.get("AreaKey")
        self.AreaRegionID = params.get("AreaRegionID")
        self.AreaRegionCode = params.get("AreaRegionCode")
        self.AreaAbbr = params.get("AreaAbbr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RumProject(AbstractModel):
    """RUM project information

    """

    def __init__(self):
        r"""
        :param Name: Project name
        :type Name: str
        :param Creator: Creator ID
        :type Creator: str
        :param InstanceID: Instance ID
        :type InstanceID: str
        :param Type: Project type
        :type Type: str
        :param CreateTime: Creation time
        :type CreateTime: str
        :param Repo: Project repository address
Note: this field may return null, indicating that no valid values can be obtained.
        :type Repo: str
        :param URL: Project URL
Note: this field may return null, indicating that no valid values can be obtained.
        :type URL: str
        :param Rate: Project sample rate
        :type Rate: str
        :param Key: Unique project key (12 characters)
        :type Key: str
        :param EnableURLGroup: Whether to enable URL aggregation
        :type EnableURLGroup: int
        :param InstanceName: Instance name
        :type InstanceName: str
        :param ID: Project ID
        :type ID: int
        :param InstanceKey: Instance key
        :type InstanceKey: str
        :param Desc: Project description
Note: this field may return null, indicating that no valid values can be obtained.
        :type Desc: str
        :param IsStar: Starred status. 1: yes; 0: no
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsStar: int
        :param ProjectStatus: Project status (`1`: Creating; `2`: Running; `3`: Abnormal; `4`: Restarting; `5`: Stopping; `6`: Stopped; `7`: Terminating; `8`: Terminated)
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ProjectStatus: int
        """
        self.Name = None
        self.Creator = None
        self.InstanceID = None
        self.Type = None
        self.CreateTime = None
        self.Repo = None
        self.URL = None
        self.Rate = None
        self.Key = None
        self.EnableURLGroup = None
        self.InstanceName = None
        self.ID = None
        self.InstanceKey = None
        self.Desc = None
        self.IsStar = None
        self.ProjectStatus = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Creator = params.get("Creator")
        self.InstanceID = params.get("InstanceID")
        self.Type = params.get("Type")
        self.CreateTime = params.get("CreateTime")
        self.Repo = params.get("Repo")
        self.URL = params.get("URL")
        self.Rate = params.get("Rate")
        self.Key = params.get("Key")
        self.EnableURLGroup = params.get("EnableURLGroup")
        self.InstanceName = params.get("InstanceName")
        self.ID = params.get("ID")
        self.InstanceKey = params.get("InstanceKey")
        self.Desc = params.get("Desc")
        self.IsStar = params.get("IsStar")
        self.ProjectStatus = params.get("ProjectStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RumPvInfo(AbstractModel):
    """RUM log object

    """

    def __init__(self):
        r"""
        :param ProjectId: Project ID
        :type ProjectId: int
        :param Pv: Number of PVs
Note: this field may return null, indicating that no valid values can be obtained.
        :type Pv: str
        :param CreateTime: Time
        :type CreateTime: str
        """
        self.ProjectId = None
        self.Pv = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Pv = params.get("Pv")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RumUvInfo(AbstractModel):
    """Number of RUM UVs

    """

    def __init__(self):
        r"""
        :param ProjectId: Project ID
        :type ProjectId: int
        :param Uv: Number of UVs
        :type Uv: str
        :param CreateTime: Creation time
        :type CreateTime: str
        """
        self.ProjectId = None
        self.Uv = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Uv = params.get("Uv")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScoreInfo(AbstractModel):
    """Project score entity

    """

    def __init__(self):
        r"""
        :param StaticDuration: duration
        :type StaticDuration: str
        :param PagePv: pv
        :type PagePv: str
        :param ApiFail: Failure
        :type ApiFail: str
        :param ApiNum: Request
        :type ApiNum: str
        :param StaticFail: fail
        :type StaticFail: str
        :param ProjectID: Project ID
        :type ProjectID: int
        :param PageUv: uv
        :type PageUv: str
        :param ApiDuration: Number of requests
        :type ApiDuration: str
        :param Score: Score
        :type Score: str
        :param PageError: error
        :type PageError: str
        :param StaticNum: num
        :type StaticNum: str
        :param RecordNum: num
        :type RecordNum: int
        :param PageDuration: Duration
        :type PageDuration: str
        :param CreateTime: Time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        """
        self.StaticDuration = None
        self.PagePv = None
        self.ApiFail = None
        self.ApiNum = None
        self.StaticFail = None
        self.ProjectID = None
        self.PageUv = None
        self.ApiDuration = None
        self.Score = None
        self.PageError = None
        self.StaticNum = None
        self.RecordNum = None
        self.PageDuration = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.StaticDuration = params.get("StaticDuration")
        self.PagePv = params.get("PagePv")
        self.ApiFail = params.get("ApiFail")
        self.ApiNum = params.get("ApiNum")
        self.StaticFail = params.get("StaticFail")
        self.ProjectID = params.get("ProjectID")
        self.PageUv = params.get("PageUv")
        self.ApiDuration = params.get("ApiDuration")
        self.Score = params.get("Score")
        self.PageError = params.get("PageError")
        self.StaticNum = params.get("StaticNum")
        self.RecordNum = params.get("RecordNum")
        self.PageDuration = params.get("PageDuration")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopInstanceRequest(AbstractModel):
    """StopInstance request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: ID of the instance to be stopped
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopInstanceResponse(AbstractModel):
    """StopInstance response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopProjectRequest(AbstractModel):
    """StopProject request structure.

    """

    def __init__(self):
        r"""
        :param ProjectId: Project ID
        :type ProjectId: int
        """
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopProjectResponse(AbstractModel):
    """StopProject response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """Tag

    """

    def __init__(self):
        r"""
        :param Key: Tag key
        :type Key: str
        :param Value: Tag value
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Whitelist(AbstractModel):
    """Allowlist

    """

    def __init__(self):
        r"""
        :param Remark: Remarks
        :type Remark: str
        :param InstanceID: Instance ID
        :type InstanceID: str
        :param Ttl: End time
        :type Ttl: str
        :param ID: Auto-Increment allowlist ID
        :type ID: str
        :param WhitelistUin: Unique business identifier
        :type WhitelistUin: str
        :param CreateUser: Creator ID
        :type CreateUser: str
        :param Aid: aid
        :type Aid: str
        :param CreateTime: Creation time
        :type CreateTime: str
        """
        self.Remark = None
        self.InstanceID = None
        self.Ttl = None
        self.ID = None
        self.WhitelistUin = None
        self.CreateUser = None
        self.Aid = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.Remark = params.get("Remark")
        self.InstanceID = params.get("InstanceID")
        self.Ttl = params.get("Ttl")
        self.ID = params.get("ID")
        self.WhitelistUin = params.get("WhitelistUin")
        self.CreateUser = params.get("CreateUser")
        self.Aid = params.get("Aid")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        