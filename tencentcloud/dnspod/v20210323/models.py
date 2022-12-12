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


class CreateDomainRequest(AbstractModel):
    """CreateDomain request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain
        :type Domain: str
        :param GroupId: The group ID of the domain. You can view the group information of this domain via the `DescribeDomainGroupList` API.
        :type GroupId: int
        :param IsMark: Whether the domain is starred. Valid values: yes, no.
        :type IsMark: str
        """
        self.Domain = None
        self.GroupId = None
        self.IsMark = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.GroupId = params.get("GroupId")
        self.IsMark = params.get("IsMark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainResponse(AbstractModel):
    """CreateDomain response structure.

    """

    def __init__(self):
        r"""
        :param DomainInfo: Domain information
        :type DomainInfo: :class:`tencentcloud.dnspod.v20210323.models.DomainCreateInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DomainInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainInfo") is not None:
            self.DomainInfo = DomainCreateInfo()
            self.DomainInfo._deserialize(params.get("DomainInfo"))
        self.RequestId = params.get("RequestId")


class CreateRecordRequest(AbstractModel):
    """CreateRecord request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain
        :type Domain: str
        :param RecordType: Record type, which is obtained through the record type API. The value contains uppercase letters, such as `A`.
        :type RecordType: str
        :param RecordLine: Record split zone, which is obtained through the record split zone API.
        :type RecordLine: str
        :param Value: Record value, such as `IP : 200.200.200.200`, `CNAME : cname.dnspod.com`, and `MX : mail.dnspod.com`.
        :type Value: str
        :param DomainId: Domain ID. The `DomainId` parameter has a higher priority than `Domain`. If `DomainId` is passed in, `Domain` will be ignored.
        :type DomainId: int
        :param SubDomain: Host record such as `www`. If it is not passed in, it will be `@` by default.
        :type SubDomain: str
        :param RecordLineId: Split zone ID, which is obtained through the record split zone API. The value is a string such as `10=1`. The `RecordLineId` parameter has a higher priority than `RecordLine`. If both of them are passed in, `RecordLineId` will be used first.
        :type RecordLineId: str
        :param MX: MX priority, which is required for an MX record and will take effect if the record type is MX. Value range: 1–20.
        :type MX: int
        :param TTL: TTL. Value range: 1–604800. The minimum value varies by domain level.
        :type TTL: int
        :param Weight: Weight information, which is an integer between 0 and 100. It is supported only for enterprise VIP domains. `0` indicates not to pass in this parameter, i.e., not to set the weight.
        :type Weight: int
        :param Status: Initial status of the record. Valid values: ENABLE, DISABLE. Default value: ENABLE. If `DISABLE` is passed in, the DNS record won't take effect, and the limit on round-robin DNS won't be verified.
        :type Status: str
        """
        self.Domain = None
        self.RecordType = None
        self.RecordLine = None
        self.Value = None
        self.DomainId = None
        self.SubDomain = None
        self.RecordLineId = None
        self.MX = None
        self.TTL = None
        self.Weight = None
        self.Status = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.RecordType = params.get("RecordType")
        self.RecordLine = params.get("RecordLine")
        self.Value = params.get("Value")
        self.DomainId = params.get("DomainId")
        self.SubDomain = params.get("SubDomain")
        self.RecordLineId = params.get("RecordLineId")
        self.MX = params.get("MX")
        self.TTL = params.get("TTL")
        self.Weight = params.get("Weight")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordResponse(AbstractModel):
    """CreateRecord response structure.

    """

    def __init__(self):
        r"""
        :param RecordId: Record ID
        :type RecordId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RecordId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RecordId = params.get("RecordId")
        self.RequestId = params.get("RequestId")


class DeleteDomainRequest(AbstractModel):
    """DeleteDomain request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain
        :type Domain: str
        :param DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self.Domain = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainResponse(AbstractModel):
    """DeleteDomain response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRecordRequest(AbstractModel):
    """DeleteRecord request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain
        :type Domain: str
        :param RecordId: The record ID. You can view all DNS records and their IDs via the `DescribeRecordList` API.
        :type RecordId: int
        :param DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self.Domain = None
        self.RecordId = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.RecordId = params.get("RecordId")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordResponse(AbstractModel):
    """DeleteRecord response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDomainRequest(AbstractModel):
    """DescribeDomain request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain
        :type Domain: str
        :param DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self.Domain = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainResponse(AbstractModel):
    """DescribeDomain response structure.

    """

    def __init__(self):
        r"""
        :param DomainInfo: Domain information
        :type DomainInfo: :class:`tencentcloud.dnspod.v20210323.models.DomainInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DomainInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainInfo") is not None:
            self.DomainInfo = DomainInfo()
            self.DomainInfo._deserialize(params.get("DomainInfo"))
        self.RequestId = params.get("RequestId")


class DescribeRecordListRequest(AbstractModel):
    """DescribeRecordList request structure.

    """

    def __init__(self):
        r"""
        :param Domain: The domain for which DNS records are to be obtained.
        :type Domain: str
        :param DomainId: The ID of the domain whose DNS records are requested. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        :param Subdomain: The host header of a DNS record. If this parameter is passed in, only the DNS record corresponding to this host header will be returned.
        :type Subdomain: str
        :param RecordType: The type of DNS record, such as A, CNAME, NS, AAAA, explicit URL, implicit URL, CAA, or SPF record.
        :type RecordType: str
        :param RecordLine: The name of the split zone for which DNS records are requested. You can view split zones allowed by this domain via the `DescribeRecordLineList` API.
        :type RecordLine: str
        :param RecordLineId: The ID of the split zone for which DNS records are requested. If `RecordLineId` is passed in, `RecordLine` is ignored. You can view split zones allowed by this domain via the `DescribeRecordLineList` API.
        :type RecordLineId: str
        :param GroupId: The group ID passed in to get DNS records in the group.
        :type GroupId: int
        :param Keyword: The keyword for searching for DNS records. Host headers and record values are supported.
        :type Keyword: str
        :param SortField: The sorting field. Available values: `name`, `line`, `type`, `value`, `weight`, `mx`, and `ttl,updated_on`.
        :type SortField: str
        :param SortType: The sorting type. Valid values: `ASC` (ascending, default), `DESC` (descending).
        :type SortType: str
        :param Offset: The offset. Default value: `0`.
        :type Offset: int
        :param Limit: The limit. It defaults to 100 and can be up to 3,000.
        :type Limit: int
        """
        self.Domain = None
        self.DomainId = None
        self.Subdomain = None
        self.RecordType = None
        self.RecordLine = None
        self.RecordLineId = None
        self.GroupId = None
        self.Keyword = None
        self.SortField = None
        self.SortType = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        self.Subdomain = params.get("Subdomain")
        self.RecordType = params.get("RecordType")
        self.RecordLine = params.get("RecordLine")
        self.RecordLineId = params.get("RecordLineId")
        self.GroupId = params.get("GroupId")
        self.Keyword = params.get("Keyword")
        self.SortField = params.get("SortField")
        self.SortType = params.get("SortType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordListResponse(AbstractModel):
    """DescribeRecordList response structure.

    """

    def __init__(self):
        r"""
        :param RecordCountInfo: The record count info.
        :type RecordCountInfo: :class:`tencentcloud.dnspod.v20210323.models.RecordCountInfo`
        :param RecordList: The record list result.
        :type RecordList: list of RecordListItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RecordCountInfo = None
        self.RecordList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RecordCountInfo") is not None:
            self.RecordCountInfo = RecordCountInfo()
            self.RecordCountInfo._deserialize(params.get("RecordCountInfo"))
        if params.get("RecordList") is not None:
            self.RecordList = []
            for item in params.get("RecordList"):
                obj = RecordListItem()
                obj._deserialize(item)
                self.RecordList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRecordRequest(AbstractModel):
    """DescribeRecord request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain
        :type Domain: str
        :param RecordId: The record ID. You can view all DNS records and their IDs via the `DescribeRecordList` API.
        :type RecordId: int
        :param DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self.Domain = None
        self.RecordId = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.RecordId = params.get("RecordId")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordResponse(AbstractModel):
    """DescribeRecord response structure.

    """

    def __init__(self):
        r"""
        :param RecordInfo: Record information
        :type RecordInfo: :class:`tencentcloud.dnspod.v20210323.models.RecordInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RecordInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RecordInfo") is not None:
            self.RecordInfo = RecordInfo()
            self.RecordInfo._deserialize(params.get("RecordInfo"))
        self.RequestId = params.get("RequestId")


class DomainCreateInfo(AbstractModel):
    """Domain information returned during domain creation

    """

    def __init__(self):
        r"""
        :param Id: Domain ID
        :type Id: int
        :param Domain: Domain
        :type Domain: str
        :param Punycode: Domain Punycode
        :type Punycode: str
        :param GradeNsList: NS list of the domain
        :type GradeNsList: list of str
        """
        self.Id = None
        self.Domain = None
        self.Punycode = None
        self.GradeNsList = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Domain = params.get("Domain")
        self.Punycode = params.get("Punycode")
        self.GradeNsList = params.get("GradeNsList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainInfo(AbstractModel):
    """Domain details

    """

    def __init__(self):
        r"""
        :param DomainId: Domain ID
        :type DomainId: int
        :param Status: Domain status
        :type Status: str
        :param Grade: DNS plan level
        :type Grade: str
        :param GroupId: Domain group ID
        :type GroupId: int
        :param IsMark: Whether the domain is starred
        :type IsMark: str
        :param TTL: TTL (DNS record cache time)
        :type TTL: int
        :param CnameSpeedup: Whether CNAME flattening is enabled
        :type CnameSpeedup: str
        :param Remark: Domain remarks
Note: This field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param Punycode: Domain Punycode
        :type Punycode: str
        :param DnsStatus: DNS status of the domain
        :type DnsStatus: str
        :param DnspodNsList: NS list of the domain
        :type DnspodNsList: list of str
        :param Domain: Domain
        :type Domain: str
        :param GradeLevel: Domain level ID
        :type GradeLevel: int
        :param UserId: Domain user ID
        :type UserId: int
        :param IsVip: Whether the domain is a VIP domain
        :type IsVip: str
        :param Owner: Domain owner account
        :type Owner: str
        :param GradeTitle: Domain level description
        :type GradeTitle: str
        :param CreatedOn: Domain creation time
        :type CreatedOn: str
        :param UpdatedOn: Last update time
        :type UpdatedOn: str
        :param Uin: Tencent Cloud account `Uin`
        :type Uin: str
        :param ActualNsList: NS list actually used by the domain
Note: This field may return null, indicating that no valid values can be obtained.
        :type ActualNsList: list of str
        :param RecordCount: Number of domain records
        :type RecordCount: int
        :param OwnerNick: Alias of the domain account owner
Note: This field may return null, indicating that no valid values can be obtained.
        :type OwnerNick: str
        """
        self.DomainId = None
        self.Status = None
        self.Grade = None
        self.GroupId = None
        self.IsMark = None
        self.TTL = None
        self.CnameSpeedup = None
        self.Remark = None
        self.Punycode = None
        self.DnsStatus = None
        self.DnspodNsList = None
        self.Domain = None
        self.GradeLevel = None
        self.UserId = None
        self.IsVip = None
        self.Owner = None
        self.GradeTitle = None
        self.CreatedOn = None
        self.UpdatedOn = None
        self.Uin = None
        self.ActualNsList = None
        self.RecordCount = None
        self.OwnerNick = None


    def _deserialize(self, params):
        self.DomainId = params.get("DomainId")
        self.Status = params.get("Status")
        self.Grade = params.get("Grade")
        self.GroupId = params.get("GroupId")
        self.IsMark = params.get("IsMark")
        self.TTL = params.get("TTL")
        self.CnameSpeedup = params.get("CnameSpeedup")
        self.Remark = params.get("Remark")
        self.Punycode = params.get("Punycode")
        self.DnsStatus = params.get("DnsStatus")
        self.DnspodNsList = params.get("DnspodNsList")
        self.Domain = params.get("Domain")
        self.GradeLevel = params.get("GradeLevel")
        self.UserId = params.get("UserId")
        self.IsVip = params.get("IsVip")
        self.Owner = params.get("Owner")
        self.GradeTitle = params.get("GradeTitle")
        self.CreatedOn = params.get("CreatedOn")
        self.UpdatedOn = params.get("UpdatedOn")
        self.Uin = params.get("Uin")
        self.ActualNsList = params.get("ActualNsList")
        self.RecordCount = params.get("RecordCount")
        self.OwnerNick = params.get("OwnerNick")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainRemarkRequest(AbstractModel):
    """ModifyDomainRemark request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain
        :type Domain: str
        :param DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        :param Remark: Domain remarks. To delete the remarks, submit empty content.
        :type Remark: str
        """
        self.Domain = None
        self.DomainId = None
        self.Remark = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainRemarkResponse(AbstractModel):
    """ModifyDomainRemark response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDomainStatusRequest(AbstractModel):
    """ModifyDomainStatus request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain
        :type Domain: str
        :param Status: Domain status. Valid values: enable; disable.
        :type Status: str
        :param DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self.Domain = None
        self.Status = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Status = params.get("Status")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainStatusResponse(AbstractModel):
    """ModifyDomainStatus response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRecordRequest(AbstractModel):
    """ModifyRecord request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain
        :type Domain: str
        :param RecordType: Record type, which is obtained through the record type API. The value contains uppercase letters, such as `A`.
        :type RecordType: str
        :param RecordLine: Record split zone, which is obtained through the record split zone API.
        :type RecordLine: str
        :param Value: Record value, such as `IP : 200.200.200.200`, `CNAME : cname.dnspod.com`, and `MX : mail.dnspod.com`.
        :type Value: str
        :param RecordId: The record ID. You can view all DNS records and their IDs via the `DescribeRecordList` API.
        :type RecordId: int
        :param DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        :param SubDomain: Host record such as `www`. If it is not passed in, it will be `@` by default.
        :type SubDomain: str
        :param RecordLineId: Split zone ID, which is obtained through the record split zone API. The value is a string such as `10=1`. The `RecordLineId` parameter has a higher priority than `RecordLine`. If both of them are passed in, `RecordLineId` will be used first.
        :type RecordLineId: str
        :param MX: MX priority, which is required for an MX record and will take effect if the record type is MX. Value range: 1–20.
        :type MX: int
        :param TTL: TTL. Value range: 1–604800. The minimum value varies by domain level.
        :type TTL: int
        :param Weight: Weight information, which is an integer between 0 and 100. It is supported only for enterprise VIP domains. `0` indicates not to pass in this parameter, i.e., not to set the weight.
        :type Weight: int
        :param Status: Initial status of the record. Valid values: ENABLE, DISABLE. Default value: ENABLE. If `DISABLE` is passed in, the DNS record won't take effect, and the limit on round-robin DNS won't be verified.
        :type Status: str
        """
        self.Domain = None
        self.RecordType = None
        self.RecordLine = None
        self.Value = None
        self.RecordId = None
        self.DomainId = None
        self.SubDomain = None
        self.RecordLineId = None
        self.MX = None
        self.TTL = None
        self.Weight = None
        self.Status = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.RecordType = params.get("RecordType")
        self.RecordLine = params.get("RecordLine")
        self.Value = params.get("Value")
        self.RecordId = params.get("RecordId")
        self.DomainId = params.get("DomainId")
        self.SubDomain = params.get("SubDomain")
        self.RecordLineId = params.get("RecordLineId")
        self.MX = params.get("MX")
        self.TTL = params.get("TTL")
        self.Weight = params.get("Weight")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordResponse(AbstractModel):
    """ModifyRecord response structure.

    """

    def __init__(self):
        r"""
        :param RecordId: Record ID
        :type RecordId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RecordId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RecordId = params.get("RecordId")
        self.RequestId = params.get("RequestId")


class RecordCountInfo(AbstractModel):
    """Count info of the queried record list

    """

    def __init__(self):
        r"""
        :param SubdomainCount: The subdomain count.
        :type SubdomainCount: int
        :param ListCount: The count of records returned in the list.
        :type ListCount: int
        :param TotalCount: The total record count.
        :type TotalCount: int
        """
        self.SubdomainCount = None
        self.ListCount = None
        self.TotalCount = None


    def _deserialize(self, params):
        self.SubdomainCount = params.get("SubdomainCount")
        self.ListCount = params.get("ListCount")
        self.TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordInfo(AbstractModel):
    """Record information

    """

    def __init__(self):
        r"""
        :param Id: Record ID.
        :type Id: int
        :param SubDomain: Subdomain (host record).
        :type SubDomain: str
        :param RecordType: Record type. For more information, see the `DescribeRecordType` API.
        :type RecordType: str
        :param RecordLine: Split zone of the DNS record. For more information, see the `DescribeRecordLineList` API.
        :type RecordLine: str
        :param RecordLineId: Split zone ID of the DNS record. For more information, see the `DescribeRecordLineList` API.
        :type RecordLineId: str
        :param Value: Record value.
        :type Value: str
        :param Weight: Record weight.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Weight: int
        :param MX: MX record value. It is 0 by default for non-MX records.
        :type MX: int
        :param TTL: TTL value of the record.
        :type TTL: int
        :param Enabled: Record status. Valid values: 0 (disabled); 1 (enabled).
        :type Enabled: int
        :param MonitorStatus: D-Monitor status of the record.
"Ok" : The server is normal.
"Warn" : There is an alarm on this record, and the server returns 4XX.
"Down" : The server is down.
"" : D-Monitor is disabled for this record.
        :type MonitorStatus: str
        :param Remark: Record remarks.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param UpdatedOn: Last update time of the record.
        :type UpdatedOn: str
        :param DomainId: Domain ID.
        :type DomainId: int
        """
        self.Id = None
        self.SubDomain = None
        self.RecordType = None
        self.RecordLine = None
        self.RecordLineId = None
        self.Value = None
        self.Weight = None
        self.MX = None
        self.TTL = None
        self.Enabled = None
        self.MonitorStatus = None
        self.Remark = None
        self.UpdatedOn = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.SubDomain = params.get("SubDomain")
        self.RecordType = params.get("RecordType")
        self.RecordLine = params.get("RecordLine")
        self.RecordLineId = params.get("RecordLineId")
        self.Value = params.get("Value")
        self.Weight = params.get("Weight")
        self.MX = params.get("MX")
        self.TTL = params.get("TTL")
        self.Enabled = params.get("Enabled")
        self.MonitorStatus = params.get("MonitorStatus")
        self.Remark = params.get("Remark")
        self.UpdatedOn = params.get("UpdatedOn")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordListItem(AbstractModel):
    """Record list elements

    """

    def __init__(self):
        r"""
        :param RecordId: The record ID.
        :type RecordId: int
        :param Value: The record value.
        :type Value: str
        :param Status: The record status. Valid values: `ENABLE` (enabled), `DISABLE` (disabled).
        :type Status: str
        :param UpdatedOn: The update time.
        :type UpdatedOn: str
        :param Name: The host name.
        :type Name: str
        :param Line: The record split zone.
        :type Line: str
        :param LineId: The split zone ID.
        :type LineId: str
        :param Type: The record type.
        :type Type: str
        :param Weight: The record weight, which is required for round-robin DNS records.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Weight: int
        :param MonitorStatus: The monitoring status of the record. Valid values: `OK` (normal), `WARN` (warning), and `DOWN` (downtime). It is empty if no monitoring is set or the monitoring is suspended.
        :type MonitorStatus: str
        :param Remark: The record remarks.
        :type Remark: str
        :param TTL: The record cache time.
        :type TTL: int
        :param MX: The MX value, applicable to the MX record only.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MX: int
        """
        self.RecordId = None
        self.Value = None
        self.Status = None
        self.UpdatedOn = None
        self.Name = None
        self.Line = None
        self.LineId = None
        self.Type = None
        self.Weight = None
        self.MonitorStatus = None
        self.Remark = None
        self.TTL = None
        self.MX = None


    def _deserialize(self, params):
        self.RecordId = params.get("RecordId")
        self.Value = params.get("Value")
        self.Status = params.get("Status")
        self.UpdatedOn = params.get("UpdatedOn")
        self.Name = params.get("Name")
        self.Line = params.get("Line")
        self.LineId = params.get("LineId")
        self.Type = params.get("Type")
        self.Weight = params.get("Weight")
        self.MonitorStatus = params.get("MonitorStatus")
        self.Remark = params.get("Remark")
        self.TTL = params.get("TTL")
        self.MX = params.get("MX")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        