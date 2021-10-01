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


class AccountVpcInfo(AbstractModel):
    """VPC information of a Private DNS account

    """

    def __init__(self):
        r"""
        :param UniqVpcId: VpcId: vpc-xadsafsdasd
        :type UniqVpcId: str
        :param Region: VPC region: ap-guangzhou, ap-shanghai
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Region: str
        :param Uin: VPC account: 123456789
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Uin: str
        :param VpcName: VPC name: testname
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type VpcName: str
        """
        self.UniqVpcId = None
        self.Region = None
        self.Uin = None
        self.VpcName = None


    def _deserialize(self, params):
        self.UniqVpcId = params.get("UniqVpcId")
        self.Region = params.get("Region")
        self.Uin = params.get("Uin")
        self.VpcName = params.get("VpcName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountVpcInfoOutput(AbstractModel):
    """Output parameters of the associated VPC

    """

    def __init__(self):
        r"""
        :param Uin: UIN of the VPC account
        :type Uin: str
        :param UniqVpcId: VPC ID
        :type UniqVpcId: str
        :param Region: Region
        :type Region: str
        """
        self.Uin = None
        self.UniqVpcId = None
        self.Region = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.UniqVpcId = params.get("UniqVpcId")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditLog(AbstractModel):
    """Operation log

    """

    def __init__(self):
        r"""
        :param Resource: Log type
        :type Resource: str
        :param Metric: Log table name
        :type Metric: str
        :param TotalCount: Total number of logs
        :type TotalCount: int
        :param DataSet: List of logs
        :type DataSet: list of AuditLogInfo
        """
        self.Resource = None
        self.Metric = None
        self.TotalCount = None
        self.DataSet = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        self.Metric = params.get("Metric")
        self.TotalCount = params.get("TotalCount")
        if params.get("DataSet") is not None:
            self.DataSet = []
            for item in params.get("DataSet"):
                obj = AuditLogInfo()
                obj._deserialize(item)
                self.DataSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditLogInfo(AbstractModel):
    """Log details

    """

    def __init__(self):
        r"""
        :param Date: Time
        :type Date: str
        :param OperatorUin: Operator UIN
        :type OperatorUin: str
        :param Content: Log content
        :type Content: str
        """
        self.Date = None
        self.OperatorUin = None
        self.Content = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.OperatorUin = params.get("OperatorUin")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrivateZoneRecordRequest(AbstractModel):
    """CreatePrivateZoneRecord request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Private domain ID
        :type ZoneId: str
        :param RecordType: Record type. Valid values: "A", "AAAA", "CNAME", "MX", "TXT", "PTR"
        :type RecordType: str
        :param SubDomain: Subdomain, such as "www", "m", and "@"
        :type SubDomain: str
        :param RecordValue: Record value, such as IP: 192.168.10.2, CNAME: cname.qcloud.com., and MX: mail.qcloud.com.
        :type RecordValue: str
        :param Weight: Record weight. Value range: 1–100
        :type Weight: int
        :param MX: MX priority, which is required when the record type is MX. Valid values: 5, 10, 15, 20, 30, 40, 50
        :type MX: int
        :param TTL: Record cache time. The smaller the value, the faster the record will take effect. Value range: 1–86400s. Default value: 600
        :type TTL: int
        """
        self.ZoneId = None
        self.RecordType = None
        self.SubDomain = None
        self.RecordValue = None
        self.Weight = None
        self.MX = None
        self.TTL = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.RecordType = params.get("RecordType")
        self.SubDomain = params.get("SubDomain")
        self.RecordValue = params.get("RecordValue")
        self.Weight = params.get("Weight")
        self.MX = params.get("MX")
        self.TTL = params.get("TTL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrivateZoneRecordResponse(AbstractModel):
    """CreatePrivateZoneRecord response structure.

    """

    def __init__(self):
        r"""
        :param RecordId: Record ID
        :type RecordId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RecordId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RecordId = params.get("RecordId")
        self.RequestId = params.get("RequestId")


class CreatePrivateZoneRequest(AbstractModel):
    """CreatePrivateZone request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain name, which must be in the format of standard TLD
        :type Domain: str
        :param TagSet: Tags the private domain when it is created
        :type TagSet: list of TagInfo
        :param VpcSet: Associates the private domain to a VPC when it is created
        :type VpcSet: list of VpcInfo
        :param Remark: Remarks
        :type Remark: str
        :param DnsForwardStatus: Whether to enable subdomain recursive DNS. Valid values: ENABLED, DISABLED. Default value: DISABLED
        :type DnsForwardStatus: str
        :param Vpcs: Associates the private domain to a VPC when it is created
        :type Vpcs: list of VpcInfo
        :param AccountVpcSet: List of authorized accounts' VPCs to associate with the private domain
        :type AccountVpcSet: list of AccountVpcInfo
        """
        self.Domain = None
        self.TagSet = None
        self.VpcSet = None
        self.Remark = None
        self.DnsForwardStatus = None
        self.Vpcs = None
        self.AccountVpcSet = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = TagInfo()
                obj._deserialize(item)
                self.TagSet.append(obj)
        if params.get("VpcSet") is not None:
            self.VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self.VpcSet.append(obj)
        self.Remark = params.get("Remark")
        self.DnsForwardStatus = params.get("DnsForwardStatus")
        if params.get("Vpcs") is not None:
            self.Vpcs = []
            for item in params.get("Vpcs"):
                obj = VpcInfo()
                obj._deserialize(item)
                self.Vpcs.append(obj)
        if params.get("AccountVpcSet") is not None:
            self.AccountVpcSet = []
            for item in params.get("AccountVpcSet"):
                obj = AccountVpcInfo()
                obj._deserialize(item)
                self.AccountVpcSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrivateZoneResponse(AbstractModel):
    """CreatePrivateZone response structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Private domain ID, such as zone-xxxxxx
        :type ZoneId: str
        :param Domain: Private domain
        :type Domain: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ZoneId = None
        self.Domain = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Domain = params.get("Domain")
        self.RequestId = params.get("RequestId")


class DatePoint(AbstractModel):
    """Time statistics

    """

    def __init__(self):
        r"""
        :param Date: Time
        :type Date: str
        :param Value: Value
        :type Value: int
        """
        self.Date = None
        self.Value = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrivateZoneRecordRequest(AbstractModel):
    """DeletePrivateZoneRecord request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Private domain ID
        :type ZoneId: str
        :param RecordId: Record ID
        :type RecordId: str
        :param RecordIdSet: Array of record IDs. `RecordId` takes precedence.
        :type RecordIdSet: list of str
        """
        self.ZoneId = None
        self.RecordId = None
        self.RecordIdSet = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.RecordId = params.get("RecordId")
        self.RecordIdSet = params.get("RecordIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrivateZoneRecordResponse(AbstractModel):
    """DeletePrivateZoneRecord response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePrivateZoneRequest(AbstractModel):
    """DeletePrivateZone request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Private domain ID
        :type ZoneId: str
        :param ZoneIdSet: Array of private domain IDs. `ZoneId` takes precedence.
        :type ZoneIdSet: list of str
        """
        self.ZoneId = None
        self.ZoneIdSet = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneIdSet = params.get("ZoneIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrivateZoneResponse(AbstractModel):
    """DeletePrivateZone response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAuditLogRequest(AbstractModel):
    """DescribeAuditLog request structure.

    """

    def __init__(self):
        r"""
        :param TimeRangeBegin: Request volume statistics start time
        :type TimeRangeBegin: str
        :param Filters: Filter parameter. Valid values: ZoneId (private domain ID), Domain (private domain), OperatorUin (operator account ID)
        :type Filters: list of Filter
        :param TimeRangeEnd: Request volume statistics end time
        :type TimeRangeEnd: str
        :param Offset: Pagination offset, starting from 0
        :type Offset: int
        :param Limit: Number of entries per page. Maximum value: 100. Default value: 20
        :type Limit: int
        """
        self.TimeRangeBegin = None
        self.Filters = None
        self.TimeRangeEnd = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.TimeRangeBegin = params.get("TimeRangeBegin")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.TimeRangeEnd = params.get("TimeRangeEnd")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditLogResponse(AbstractModel):
    """DescribeAuditLog response structure.

    """

    def __init__(self):
        r"""
        :param Data: List of operation logs
        :type Data: list of AuditLog
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = AuditLog()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDashboardRequest(AbstractModel):
    """DescribeDashboard request structure.

    """


class DescribeDashboardResponse(AbstractModel):
    """DescribeDashboard response structure.

    """

    def __init__(self):
        r"""
        :param ZoneTotal: Total number of private domain DNS records
        :type ZoneTotal: int
        :param ZoneVpcCount: Number of VPCs associated with private domain
        :type ZoneVpcCount: int
        :param RequestTotalCount: Total number of historical requests
        :type RequestTotalCount: int
        :param FlowUsage: Traffic package usage
        :type FlowUsage: list of FlowUsage
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ZoneTotal = None
        self.ZoneVpcCount = None
        self.RequestTotalCount = None
        self.FlowUsage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ZoneTotal = params.get("ZoneTotal")
        self.ZoneVpcCount = params.get("ZoneVpcCount")
        self.RequestTotalCount = params.get("RequestTotalCount")
        if params.get("FlowUsage") is not None:
            self.FlowUsage = []
            for item in params.get("FlowUsage"):
                obj = FlowUsage()
                obj._deserialize(item)
                self.FlowUsage.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePrivateDNSAccountListRequest(AbstractModel):
    """DescribePrivateDNSAccountList request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Pagination offset, starting from `0`
        :type Offset: int
        :param Limit: Number of entries per page. Maximum value: `100`. Default value: `20`
        :type Limit: int
        :param Filters: Filter parameters
        :type Filters: list of Filter
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
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrivateDNSAccountListResponse(AbstractModel):
    """DescribePrivateDNSAccountList response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of Private DNS accounts
        :type TotalCount: int
        :param AccountSet: List of Private DNS accounts
        :type AccountSet: list of PrivateDNSAccount
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.AccountSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AccountSet") is not None:
            self.AccountSet = []
            for item in params.get("AccountSet"):
                obj = PrivateDNSAccount()
                obj._deserialize(item)
                self.AccountSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePrivateZoneListRequest(AbstractModel):
    """DescribePrivateZoneList request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Pagination offset, starting from 0
        :type Offset: int
        :param Limit: Number of entries per page. Maximum value: 100. Default value: 20
        :type Limit: int
        :param Filters: Filter parameter
        :type Filters: list of Filter
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
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrivateZoneListResponse(AbstractModel):
    """DescribePrivateZoneList response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of private domains
        :type TotalCount: int
        :param PrivateZoneSet: List of private domains
        :type PrivateZoneSet: list of PrivateZone
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.PrivateZoneSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PrivateZoneSet") is not None:
            self.PrivateZoneSet = []
            for item in params.get("PrivateZoneSet"):
                obj = PrivateZone()
                obj._deserialize(item)
                self.PrivateZoneSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePrivateZoneRecordListRequest(AbstractModel):
    """DescribePrivateZoneRecordList request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Private domain ID: zone-xxxxxx
        :type ZoneId: str
        :param Filters: Filter parameter
        :type Filters: list of Filter
        :param Offset: Pagination offset, starting from 0
        :type Offset: int
        :param Limit: Number of entries per page. Maximum value: 100. Default value: 20
        :type Limit: int
        """
        self.ZoneId = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrivateZoneRecordListResponse(AbstractModel):
    """DescribePrivateZoneRecordList response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of DNS records
        :type TotalCount: int
        :param RecordSet: List of DNS records
        :type RecordSet: list of PrivateZoneRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.RecordSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RecordSet") is not None:
            self.RecordSet = []
            for item in params.get("RecordSet"):
                obj = PrivateZoneRecord()
                obj._deserialize(item)
                self.RecordSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePrivateZoneRequest(AbstractModel):
    """DescribePrivateZone request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Domain name, which must be in the format of standard TLD
        :type ZoneId: str
        """
        self.ZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrivateZoneResponse(AbstractModel):
    """DescribePrivateZone response structure.

    """

    def __init__(self):
        r"""
        :param PrivateZone: Private domain details
        :type PrivateZone: :class:`tencentcloud.privatedns.v20201028.models.PrivateZone`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PrivateZone = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PrivateZone") is not None:
            self.PrivateZone = PrivateZone()
            self.PrivateZone._deserialize(params.get("PrivateZone"))
        self.RequestId = params.get("RequestId")


class DescribePrivateZoneServiceRequest(AbstractModel):
    """DescribePrivateZoneService request structure.

    """


class DescribePrivateZoneServiceResponse(AbstractModel):
    """DescribePrivateZoneService response structure.

    """

    def __init__(self):
        r"""
        :param ServiceStatus: Private DNS service activation status. Valid values: ENABLED, DISABLED
        :type ServiceStatus: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ServiceStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServiceStatus = params.get("ServiceStatus")
        self.RequestId = params.get("RequestId")


class DescribeRequestDataRequest(AbstractModel):
    """DescribeRequestData request structure.

    """

    def __init__(self):
        r"""
        :param TimeRangeBegin: Request volume statistics start time in the format of 2020-11-22 00:00:00
        :type TimeRangeBegin: str
        :param Filters: Filter parameter:
        :type Filters: list of Filter
        :param TimeRangeEnd: Request volume statistics end time in the format of 2020-11-22 23:59:59
        :type TimeRangeEnd: str
        """
        self.TimeRangeBegin = None
        self.Filters = None
        self.TimeRangeEnd = None


    def _deserialize(self, params):
        self.TimeRangeBegin = params.get("TimeRangeBegin")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.TimeRangeEnd = params.get("TimeRangeEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRequestDataResponse(AbstractModel):
    """DescribeRequestData response structure.

    """

    def __init__(self):
        r"""
        :param Data: Request volume statistics table
        :type Data: list of MetricData
        :param Interval: Request volume unit time. Valid values: Day, Hour
        :type Interval: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.Interval = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = MetricData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Interval = params.get("Interval")
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """Filter parameter

    """

    def __init__(self):
        r"""
        :param Name: Parameter name
        :type Name: str
        :param Values: Array of parameter values
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowUsage(AbstractModel):
    """Traffic package usage

    """

    def __init__(self):
        r"""
        :param FlowType: Traffic package type, Valid values: ZONE (private domain); TRAFFIC (DNS traffic package)
        :type FlowType: str
        :param TotalQuantity: Traffic package quota
        :type TotalQuantity: int
        :param AvailableQuantity: Available quota of traffic package
        :type AvailableQuantity: int
        """
        self.FlowType = None
        self.TotalQuantity = None
        self.AvailableQuantity = None


    def _deserialize(self, params):
        self.FlowType = params.get("FlowType")
        self.TotalQuantity = params.get("TotalQuantity")
        self.AvailableQuantity = params.get("AvailableQuantity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricData(AbstractModel):
    """Statistics table

    """

    def __init__(self):
        r"""
        :param Resource: Resource description
        :type Resource: str
        :param Metric: Table name
        :type Metric: str
        :param DataSet: Table data
        :type DataSet: list of DatePoint
        """
        self.Resource = None
        self.Metric = None
        self.DataSet = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        self.Metric = params.get("Metric")
        if params.get("DataSet") is not None:
            self.DataSet = []
            for item in params.get("DataSet"):
                obj = DatePoint()
                obj._deserialize(item)
                self.DataSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrivateZoneRecordRequest(AbstractModel):
    """ModifyPrivateZoneRecord request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Private domain ID
        :type ZoneId: str
        :param RecordId: Record ID
        :type RecordId: str
        :param RecordType: Record type. Valid values: "A", "AAAA", "CNAME", "MX", "TXT", "PTR"
        :type RecordType: str
        :param SubDomain: Subdomain, such as "www", "m", and "@"
        :type SubDomain: str
        :param RecordValue: Record value, such as IP: 192.168.10.2, CNAME: cname.qcloud.com., and MX: mail.qcloud.com.
        :type RecordValue: str
        :param Weight: Record weight. Value range: 1–100
        :type Weight: int
        :param MX: MX priority, which is required when the record type is MX. Valid values: 5, 10, 15, 20, 30, 40, 50
        :type MX: int
        :param TTL: Record cache time. The smaller the value, the faster the record will take effect. Value range: 1–86400s. Default value: 600
        :type TTL: int
        """
        self.ZoneId = None
        self.RecordId = None
        self.RecordType = None
        self.SubDomain = None
        self.RecordValue = None
        self.Weight = None
        self.MX = None
        self.TTL = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.RecordId = params.get("RecordId")
        self.RecordType = params.get("RecordType")
        self.SubDomain = params.get("SubDomain")
        self.RecordValue = params.get("RecordValue")
        self.Weight = params.get("Weight")
        self.MX = params.get("MX")
        self.TTL = params.get("TTL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrivateZoneRecordResponse(AbstractModel):
    """ModifyPrivateZoneRecord response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPrivateZoneRequest(AbstractModel):
    """ModifyPrivateZone request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Private domain ID
        :type ZoneId: str
        :param Remark: Remarks
        :type Remark: str
        :param DnsForwardStatus: Whether to enable subdomain recursive DNS. Valid values: ENABLED, DISABLED
        :type DnsForwardStatus: str
        """
        self.ZoneId = None
        self.Remark = None
        self.DnsForwardStatus = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Remark = params.get("Remark")
        self.DnsForwardStatus = params.get("DnsForwardStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrivateZoneResponse(AbstractModel):
    """ModifyPrivateZone response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPrivateZoneVpcRequest(AbstractModel):
    """ModifyPrivateZoneVpc request structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Private domain ID
        :type ZoneId: str
        :param VpcSet: List of all VPCs associated with private domain
        :type VpcSet: list of VpcInfo
        :param AccountVpcSet: List of authorized accounts' VPCs to associate with the private domain
        :type AccountVpcSet: list of AccountVpcInfo
        """
        self.ZoneId = None
        self.VpcSet = None
        self.AccountVpcSet = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("VpcSet") is not None:
            self.VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self.VpcSet.append(obj)
        if params.get("AccountVpcSet") is not None:
            self.AccountVpcSet = []
            for item in params.get("AccountVpcSet"):
                obj = AccountVpcInfo()
                obj._deserialize(item)
                self.AccountVpcSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrivateZoneVpcResponse(AbstractModel):
    """ModifyPrivateZoneVpc response structure.

    """

    def __init__(self):
        r"""
        :param ZoneId: Private domain ID, such as zone-xxxxxx
        :type ZoneId: str
        :param VpcSet: List of VPCs associated with domain
        :type VpcSet: list of VpcInfo
        :param AccountVpcSet: List of authorized accounts' VPCs associated with the private domain
        :type AccountVpcSet: list of AccountVpcInfoOutput
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ZoneId = None
        self.VpcSet = None
        self.AccountVpcSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("VpcSet") is not None:
            self.VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self.VpcSet.append(obj)
        if params.get("AccountVpcSet") is not None:
            self.AccountVpcSet = []
            for item in params.get("AccountVpcSet"):
                obj = AccountVpcInfoOutput()
                obj._deserialize(item)
                self.AccountVpcSet.append(obj)
        self.RequestId = params.get("RequestId")


class PrivateDNSAccount(AbstractModel):
    """Private DNS account

    """

    def __init__(self):
        r"""
        :param Uin: Root account UIN
        :type Uin: str
        :param Account: Root account name
        :type Account: str
        :param Nickname: Account name
        :type Nickname: str
        """
        self.Uin = None
        self.Account = None
        self.Nickname = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Account = params.get("Account")
        self.Nickname = params.get("Nickname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivateZone(AbstractModel):
    """Private domain information

    """

    def __init__(self):
        r"""
        :param ZoneId: Private domain ID: zone-xxxxxxxx
        :type ZoneId: str
        :param OwnerUin: Domain name owner UIN
        :type OwnerUin: int
        :param Domain: Private domain
        :type Domain: str
        :param CreatedOn: Creation time
        :type CreatedOn: str
        :param UpdatedOn: Modification time
        :type UpdatedOn: str
        :param RecordCount: Number of results
        :type RecordCount: int
        :param Remark: Remarks
Note: this field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param VpcSet: List of bound VPCs
        :type VpcSet: list of VpcInfo
        :param Status: Private domain status. Valid values: ENABLED (DNS enabled); SUSPEND (DNS paused); FROZEN (locked)
        :type Status: str
        :param DnsForwardStatus: Subdomain recursive DNS status. Valid values: ENABLED, DISABLED
        :type DnsForwardStatus: str
        :param Tags: Set of tag key-value pairs
        :type Tags: list of TagInfo
        :param AccountVpcSet: List of authorized accounts' VPCs associated with the private domain
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AccountVpcSet: list of AccountVpcInfoOutput
        """
        self.ZoneId = None
        self.OwnerUin = None
        self.Domain = None
        self.CreatedOn = None
        self.UpdatedOn = None
        self.RecordCount = None
        self.Remark = None
        self.VpcSet = None
        self.Status = None
        self.DnsForwardStatus = None
        self.Tags = None
        self.AccountVpcSet = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.OwnerUin = params.get("OwnerUin")
        self.Domain = params.get("Domain")
        self.CreatedOn = params.get("CreatedOn")
        self.UpdatedOn = params.get("UpdatedOn")
        self.RecordCount = params.get("RecordCount")
        self.Remark = params.get("Remark")
        if params.get("VpcSet") is not None:
            self.VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self.VpcSet.append(obj)
        self.Status = params.get("Status")
        self.DnsForwardStatus = params.get("DnsForwardStatus")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("AccountVpcSet") is not None:
            self.AccountVpcSet = []
            for item in params.get("AccountVpcSet"):
                obj = AccountVpcInfoOutput()
                obj._deserialize(item)
                self.AccountVpcSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivateZoneRecord(AbstractModel):
    """Private domain information

    """

    def __init__(self):
        r"""
        :param RecordId: Record ID
        :type RecordId: str
        :param ZoneId: Private domain ID: zone-xxxxxxxx
        :type ZoneId: str
        :param SubDomain: Subdomain
        :type SubDomain: str
        :param RecordType: Record type. Valid values: "A", "AAAA", "CNAME", "MX", "TXT", "PTR"
        :type RecordType: str
        :param RecordValue: Record value
        :type RecordValue: str
        :param TTL: Record cache time. The smaller the value, the faster the record will take effect. Value range: 1–86400s. Default value: 600
        :type TTL: int
        :param MX: MX priority, which is required when the record type is MX. Valid values: 5, 10, 15, 20, 30, 40, 50
Note: this field may return null, indicating that no valid values can be obtained.
        :type MX: int
        :param Status: Record status: ENABLED
        :type Status: str
        :param Weight: Record weight. Value range: 1–100
Note: this field may return null, indicating that no valid values can be obtained.
        :type Weight: int
        :param CreatedOn: Record creation time
        :type CreatedOn: str
        :param UpdatedOn: Record update time
        :type UpdatedOn: str
        :param Extra: Additional information
Note: this field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        """
        self.RecordId = None
        self.ZoneId = None
        self.SubDomain = None
        self.RecordType = None
        self.RecordValue = None
        self.TTL = None
        self.MX = None
        self.Status = None
        self.Weight = None
        self.CreatedOn = None
        self.UpdatedOn = None
        self.Extra = None


    def _deserialize(self, params):
        self.RecordId = params.get("RecordId")
        self.ZoneId = params.get("ZoneId")
        self.SubDomain = params.get("SubDomain")
        self.RecordType = params.get("RecordType")
        self.RecordValue = params.get("RecordValue")
        self.TTL = params.get("TTL")
        self.MX = params.get("MX")
        self.Status = params.get("Status")
        self.Weight = params.get("Weight")
        self.CreatedOn = params.get("CreatedOn")
        self.UpdatedOn = params.get("UpdatedOn")
        self.Extra = params.get("Extra")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribePrivateZoneServiceRequest(AbstractModel):
    """SubscribePrivateZoneService request structure.

    """


class SubscribePrivateZoneServiceResponse(AbstractModel):
    """SubscribePrivateZoneService response structure.

    """

    def __init__(self):
        r"""
        :param ServiceStatus: Private DNS service activation status
        :type ServiceStatus: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ServiceStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServiceStatus = params.get("ServiceStatus")
        self.RequestId = params.get("RequestId")


class TagInfo(AbstractModel):
    """Tag

    """

    def __init__(self):
        r"""
        :param TagKey: Tag key
        :type TagKey: str
        :param TagValue: Tag value
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcInfo(AbstractModel):
    """VPC information

    """

    def __init__(self):
        r"""
        :param UniqVpcId: VpcId: vpc-xadsafsdasd
        :type UniqVpcId: str
        :param Region: VPC region: ap-guangzhou, ap-shanghai
        :type Region: str
        """
        self.UniqVpcId = None
        self.Region = None


    def _deserialize(self, params):
        self.UniqVpcId = params.get("UniqVpcId")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        