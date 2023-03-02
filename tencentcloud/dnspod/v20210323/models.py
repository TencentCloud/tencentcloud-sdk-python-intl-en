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


class AddRecordBatch(AbstractModel):
    """Records to be bulk added

    """

    def __init__(self):
        r"""
        :param RecordType: Record type. For more information, see the `DescribeRecordType` API.
        :type RecordType: str
        :param Value: Record value.
        :type Value: str
        :param SubDomain: Subdomain (host record), which is `@` by default.
        :type SubDomain: str
        :param RecordLine: Split zone of the DNS record. For more information, see the `DescribeRecordLineList` API. If neither `RecordLine` nor `RecordLineId` is specified, the default split zone will be used.
        :type RecordLine: str
        :param RecordLineId: Split zone ID of the DNS record. If both `RecordLine` and `RecordLineId` are specified, `RecordLineId` will be used.
        :type RecordLineId: str
        :param Weight: Record weight (not supported).
Note: This field may return null, indicating that no valid values can be obtained.
        :type Weight: int
        :param MX: MX record value. It is `0` by default for non-MX records and required for MX records.
        :type MX: int
        :param TTL: TTL value of the record, which is `600` by default.
        :type TTL: int
        :param Enabled: Record status (not supported). Valid values: `0` (disabled); `1` (enabled). Default value: `1`.
        :type Enabled: int
        :param Remark: Record remarks (not supported).
        :type Remark: str
        """
        self.RecordType = None
        self.Value = None
        self.SubDomain = None
        self.RecordLine = None
        self.RecordLineId = None
        self.Weight = None
        self.MX = None
        self.TTL = None
        self.Enabled = None
        self.Remark = None


    def _deserialize(self, params):
        self.RecordType = params.get("RecordType")
        self.Value = params.get("Value")
        self.SubDomain = params.get("SubDomain")
        self.RecordLine = params.get("RecordLine")
        self.RecordLineId = params.get("RecordLineId")
        self.Weight = params.get("Weight")
        self.MX = params.get("MX")
        self.TTL = params.get("TTL")
        self.Enabled = params.get("Enabled")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchRecordInfo(AbstractModel):
    """Record information in the bulk task

    """

    def __init__(self):
        r"""
        :param RecordId: Record ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordId: int
        :param SubDomain: Subdomain (host record).
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubDomain: str
        :param RecordType: Record type. For more information, see the `DescribeRecordType` API.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordType: str
        :param RecordLine: Split zone of the DNS record. For more information, see the `DescribeRecordLineList` API.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordLine: str
        :param Value: Record value
Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: str
        :param TTL: TTL value of the record
Note: This field may return null, indicating that no valid values can be obtained.
        :type TTL: int
        :param Status: Record adding status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param Operation: Operation type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Operation: str
        :param ErrMsg: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrMsg: str
        :param Id: ID of the record in the list
        :type Id: int
        :param Enabled: Record status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Enabled: int
        :param MX: MX weight of the record
Note: This field may return null, indicating that no valid values can be obtained.
        :type MX: int
        """
        self.RecordId = None
        self.SubDomain = None
        self.RecordType = None
        self.RecordLine = None
        self.Value = None
        self.TTL = None
        self.Status = None
        self.Operation = None
        self.ErrMsg = None
        self.Id = None
        self.Enabled = None
        self.MX = None


    def _deserialize(self, params):
        self.RecordId = params.get("RecordId")
        self.SubDomain = params.get("SubDomain")
        self.RecordType = params.get("RecordType")
        self.RecordLine = params.get("RecordLine")
        self.Value = params.get("Value")
        self.TTL = params.get("TTL")
        self.Status = params.get("Status")
        self.Operation = params.get("Operation")
        self.ErrMsg = params.get("ErrMsg")
        self.Id = params.get("Id")
        self.Enabled = params.get("Enabled")
        self.MX = params.get("MX")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainAliasRequest(AbstractModel):
    """CreateDomainAlias request structure.

    """

    def __init__(self):
        r"""
        :param DomainAlias: Domain alias
        :type DomainAlias: str
        :param Domain: Domain
        :type Domain: str
        :param DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self.DomainAlias = None
        self.Domain = None
        self.DomainId = None


    def _deserialize(self, params):
        self.DomainAlias = params.get("DomainAlias")
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainAliasResponse(AbstractModel):
    """CreateDomainAlias response structure.

    """

    def __init__(self):
        r"""
        :param DomainAliasId: Domain alias ID
        :type DomainAliasId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DomainAliasId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DomainAliasId = params.get("DomainAliasId")
        self.RequestId = params.get("RequestId")


class CreateDomainBatchDetail(AbstractModel):
    """Response structure for bulk adding domains

    """

    def __init__(self):
        r"""
        :param RecordList: See `RecordInfoBatch`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordList: list of CreateDomainBatchRecord
        :param Id: Task ID
        :type Id: int
        :param Domain: Domain
Note: This field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param DomainGrade: Domain level
Note: This field may return null, indicating that no valid values can be obtained.
        :type DomainGrade: str
        :param ErrMsg: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrMsg: str
        :param Status: Task running status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param Operation: Operation type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Operation: str
        """
        self.RecordList = None
        self.Id = None
        self.Domain = None
        self.DomainGrade = None
        self.ErrMsg = None
        self.Status = None
        self.Operation = None


    def _deserialize(self, params):
        if params.get("RecordList") is not None:
            self.RecordList = []
            for item in params.get("RecordList"):
                obj = CreateDomainBatchRecord()
                obj._deserialize(item)
                self.RecordList.append(obj)
        self.Id = params.get("Id")
        self.Domain = params.get("Domain")
        self.DomainGrade = params.get("DomainGrade")
        self.ErrMsg = params.get("ErrMsg")
        self.Status = params.get("Status")
        self.Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainBatchRecord(AbstractModel):
    """Record information in the task of bulk adding domains

    """

    def __init__(self):
        r"""
        :param SubDomain: Subdomain (host record).
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubDomain: str
        :param RecordType: Record type. For more information, see the `DescribeRecordType` API.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordType: str
        :param RecordLine: Split zone of the DNS record. For more information, see the `DescribeRecordLineList` API.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordLine: str
        :param Value: Record value
Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: str
        :param TTL: TTL value of the record
Note: This field may return null, indicating that no valid values can be obtained.
        :type TTL: int
        :param Status: Record adding status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param Operation: Operation type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Operation: str
        :param ErrMsg: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrMsg: str
        :param Id: ID of the record in the list
        :type Id: int
        """
        self.SubDomain = None
        self.RecordType = None
        self.RecordLine = None
        self.Value = None
        self.TTL = None
        self.Status = None
        self.Operation = None
        self.ErrMsg = None
        self.Id = None


    def _deserialize(self, params):
        self.SubDomain = params.get("SubDomain")
        self.RecordType = params.get("RecordType")
        self.RecordLine = params.get("RecordLine")
        self.Value = params.get("Value")
        self.TTL = params.get("TTL")
        self.Status = params.get("Status")
        self.Operation = params.get("Operation")
        self.ErrMsg = params.get("ErrMsg")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainBatchRequest(AbstractModel):
    """CreateDomainBatch request structure.

    """

    def __init__(self):
        r"""
        :param DomainList: Domain array
        :type DomainList: list of str
        :param RecordValue: Add A records of @ and www for each domain with the record value of the IP. If this parameter is not passed in or is set to an empty string or null, only the domain but not the records will be added.
        :type RecordValue: str
        """
        self.DomainList = None
        self.RecordValue = None


    def _deserialize(self, params):
        self.DomainList = params.get("DomainList")
        self.RecordValue = params.get("RecordValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainBatchResponse(AbstractModel):
    """CreateDomainBatch response structure.

    """

    def __init__(self):
        r"""
        :param DetailList: Information of the bulk added domains
        :type DetailList: list of CreateDomainBatchDetail
        :param JobId: Bulk task ID
        :type JobId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DetailList = None
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DetailList") is not None:
            self.DetailList = []
            for item in params.get("DetailList"):
                obj = CreateDomainBatchDetail()
                obj._deserialize(item)
                self.DetailList.append(obj)
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class CreateDomainGroupRequest(AbstractModel):
    """CreateDomainGroup request structure.

    """

    def __init__(self):
        r"""
        :param GroupName: Domain group
        :type GroupName: str
        """
        self.GroupName = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainGroupResponse(AbstractModel):
    """CreateDomainGroup response structure.

    """

    def __init__(self):
        r"""
        :param GroupId: Domain group ID
        :type GroupId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")


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


class CreateRecordBatchDetail(AbstractModel):
    """Response structure for bulk adding records

    """

    def __init__(self):
        r"""
        :param RecordList: See `RecordInfoBatch`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordList: list of CreateRecordBatchRecord
        :param Id: Task ID
        :type Id: int
        :param Domain: Domain
Note: This field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param DomainGrade: Domain level
Note: This field may return null, indicating that no valid values can be obtained.
        :type DomainGrade: str
        :param ErrMsg: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrMsg: str
        :param Status: Task running status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param Operation: Operation type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Operation: str
        :param DomainId: Domain ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type DomainId: int
        """
        self.RecordList = None
        self.Id = None
        self.Domain = None
        self.DomainGrade = None
        self.ErrMsg = None
        self.Status = None
        self.Operation = None
        self.DomainId = None


    def _deserialize(self, params):
        if params.get("RecordList") is not None:
            self.RecordList = []
            for item in params.get("RecordList"):
                obj = CreateRecordBatchRecord()
                obj._deserialize(item)
                self.RecordList.append(obj)
        self.Id = params.get("Id")
        self.Domain = params.get("Domain")
        self.DomainGrade = params.get("DomainGrade")
        self.ErrMsg = params.get("ErrMsg")
        self.Status = params.get("Status")
        self.Operation = params.get("Operation")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordBatchRecord(AbstractModel):
    """Record information in the task of bulk adding records

    """

    def __init__(self):
        r"""
        :param SubDomain: Subdomain (host record).
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubDomain: str
        :param RecordType: Record type. For more information, see the `DescribeRecordType` API.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordType: str
        :param RecordLine: Split zone of the DNS record. For more information, see the `DescribeRecordLineList` API.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordLine: str
        :param Value: Record value
Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: str
        :param TTL: TTL value of the record
Note: This field may return null, indicating that no valid values can be obtained.
        :type TTL: int
        :param Status: Record adding status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param Operation: Operation type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Operation: str
        :param ErrMsg: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrMsg: str
        :param Id: ID of the record in the list
        :type Id: int
        :param MX: MX weight of the record
Note: This field may return null, indicating that no valid values can be obtained.
        :type MX: int
        """
        self.SubDomain = None
        self.RecordType = None
        self.RecordLine = None
        self.Value = None
        self.TTL = None
        self.Status = None
        self.Operation = None
        self.ErrMsg = None
        self.Id = None
        self.MX = None


    def _deserialize(self, params):
        self.SubDomain = params.get("SubDomain")
        self.RecordType = params.get("RecordType")
        self.RecordLine = params.get("RecordLine")
        self.Value = params.get("Value")
        self.TTL = params.get("TTL")
        self.Status = params.get("Status")
        self.Operation = params.get("Operation")
        self.ErrMsg = params.get("ErrMsg")
        self.Id = params.get("Id")
        self.MX = params.get("MX")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordBatchRequest(AbstractModel):
    """CreateRecordBatch request structure.

    """

    def __init__(self):
        r"""
        :param DomainIdList: Domain ID. Separate multiple ones by comma.
        :type DomainIdList: list of str
        :param RecordList: Record array
        :type RecordList: list of AddRecordBatch
        """
        self.DomainIdList = None
        self.RecordList = None


    def _deserialize(self, params):
        self.DomainIdList = params.get("DomainIdList")
        if params.get("RecordList") is not None:
            self.RecordList = []
            for item in params.get("RecordList"):
                obj = AddRecordBatch()
                obj._deserialize(item)
                self.RecordList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordBatchResponse(AbstractModel):
    """CreateRecordBatch response structure.

    """

    def __init__(self):
        r"""
        :param DetailList: Information of the bulk added domains
        :type DetailList: list of CreateRecordBatchDetail
        :param JobId: Bulk task ID
        :type JobId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DetailList = None
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DetailList") is not None:
            self.DetailList = []
            for item in params.get("DetailList"):
                obj = CreateRecordBatchDetail()
                obj._deserialize(item)
                self.DetailList.append(obj)
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class CreateRecordGroupRequest(AbstractModel):
    """CreateRecordGroup request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain
        :type Domain: str
        :param GroupName: Group name
        :type GroupName: str
        :param DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored.
        :type DomainId: int
        """
        self.Domain = None
        self.GroupName = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.GroupName = params.get("GroupName")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordGroupResponse(AbstractModel):
    """CreateRecordGroup response structure.

    """

    def __init__(self):
        r"""
        :param GroupId: New group ID
        :type GroupId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
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


class DeleteDomainAliasRequest(AbstractModel):
    """DeleteDomainAlias request structure.

    """

    def __init__(self):
        r"""
        :param DomainAliasId: Domain alias ID. You can view all domain aliases and their IDs via the `DescribeDomainAliasList` API.
        :type DomainAliasId: int
        :param Domain: Domain
        :type Domain: str
        :param DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self.DomainAliasId = None
        self.Domain = None
        self.DomainId = None


    def _deserialize(self, params):
        self.DomainAliasId = params.get("DomainAliasId")
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainAliasResponse(AbstractModel):
    """DeleteDomainAlias response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDomainBatchDetail(AbstractModel):
    """Details of batch deleting domains

    """

    def __init__(self):
        r"""
        :param DomainId: The domain ID.
        :type DomainId: int
        :param Domain: The domain name.
        :type Domain: str
        :param Error: The error message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Error: str
        :param Status: The domain deletion status.
        :type Status: str
        :param Operation: The operation.
        :type Operation: str
        """
        self.DomainId = None
        self.Domain = None
        self.Error = None
        self.Status = None
        self.Operation = None


    def _deserialize(self, params):
        self.DomainId = params.get("DomainId")
        self.Domain = params.get("Domain")
        self.Error = params.get("Error")
        self.Status = params.get("Status")
        self.Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainBatchRequest(AbstractModel):
    """DeleteDomainBatch request structure.

    """

    def __init__(self):
        r"""
        :param DomainList: The domain array.
        :type DomainList: list of str
        """
        self.DomainList = None


    def _deserialize(self, params):
        self.DomainList = params.get("DomainList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainBatchResponse(AbstractModel):
    """DeleteDomainBatch response structure.

    """

    def __init__(self):
        r"""
        :param JobId: The task ID.
        :type JobId: int
        :param DetailList: The array of task details.
        :type DetailList: list of DeleteDomainBatchDetail
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.JobId = None
        self.DetailList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        if params.get("DetailList") is not None:
            self.DetailList = []
            for item in params.get("DetailList"):
                obj = DeleteDomainBatchDetail()
                obj._deserialize(item)
                self.DetailList.append(obj)
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


class DeleteRecordGroupRequest(AbstractModel):
    """DeleteRecordGroup request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain
        :type Domain: str
        :param GroupId: Group ID
        :type GroupId: int
        :param DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored.
        :type DomainId: int
        """
        self.Domain = None
        self.GroupId = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.GroupId = params.get("GroupId")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordGroupResponse(AbstractModel):
    """DeleteRecordGroup response structure.

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


class DeleteShareDomainRequest(AbstractModel):
    """DeleteShareDomain request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain
        :type Domain: str
        :param Account: Account of the domain to be shared
        :type Account: str
        :param DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self.Domain = None
        self.Account = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Account = params.get("Account")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteShareDomainResponse(AbstractModel):
    """DeleteShareDomain response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDomainAliasListRequest(AbstractModel):
    """DescribeDomainAliasList request structure.

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
        


class DescribeDomainAliasListResponse(AbstractModel):
    """DescribeDomainAliasList response structure.

    """

    def __init__(self):
        r"""
        :param DomainAliasList: List of domain aliases
        :type DomainAliasList: list of DomainAliasInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DomainAliasList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainAliasList") is not None:
            self.DomainAliasList = []
            for item in params.get("DomainAliasList"):
                obj = DomainAliasInfo()
                obj._deserialize(item)
                self.DomainAliasList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDomainGroupListRequest(AbstractModel):
    """DescribeDomainGroupList request structure.

    """


class DescribeDomainGroupListResponse(AbstractModel):
    """DescribeDomainGroupList response structure.

    """

    def __init__(self):
        r"""
        :param GroupList: Group list
        :type GroupList: list of GroupInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.GroupList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GroupList") is not None:
            self.GroupList = []
            for item in params.get("GroupList"):
                obj = GroupInfo()
                obj._deserialize(item)
                self.GroupList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDomainListRequest(AbstractModel):
    """DescribeDomainList request structure.

    """

    def __init__(self):
        r"""
        :param Type: Domain group type. Valid values: `ALL`, `MINE`, `SHARE`, `ISMARK`, `PAUSE`, `VIP`, `RECENT`, `SHARE_OUT`. Default value: `ALL`.
        :type Type: str
        :param Offset: Record offset starting from `0`. Default value: `0`.
        :type Offset: int
        :param Limit: Number of domains to be obtained. For example, `20` indicates to obtain 20 domains. Default value: `3000`.
        :type Limit: int
        :param GroupId: Group ID, which can be passed in to get all domains in the specified group
        :type GroupId: int
        :param Keyword: Keyword for searching for a domain
        :type Keyword: str
        """
        self.Type = None
        self.Offset = None
        self.Limit = None
        self.GroupId = None
        self.Keyword = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.GroupId = params.get("GroupId")
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainListResponse(AbstractModel):
    """DescribeDomainList response structure.

    """

    def __init__(self):
        r"""
        :param DomainCountInfo: Statistics on the list page
        :type DomainCountInfo: :class:`tencentcloud.dnspod.v20210323.models.DomainCountInfo`
        :param DomainList: Domain list
        :type DomainList: list of DomainListItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DomainCountInfo = None
        self.DomainList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainCountInfo") is not None:
            self.DomainCountInfo = DomainCountInfo()
            self.DomainCountInfo._deserialize(params.get("DomainCountInfo"))
        if params.get("DomainList") is not None:
            self.DomainList = []
            for item in params.get("DomainList"):
                obj = DomainListItem()
                obj._deserialize(item)
                self.DomainList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDomainLogListRequest(AbstractModel):
    """DescribeDomainLogList request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain
        :type Domain: str
        :param DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        :param Offset: Record offset starting from `0`. Default value: `0`.
        :type Offset: int
        :param Limit: Total number of logs to be obtained. For example, `20` indicates to obtain 20 logs. Default value: `500`. Maximum value: `500`.
        :type Limit: int
        """
        self.Domain = None
        self.DomainId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainLogListResponse(AbstractModel):
    """DescribeDomainLogList response structure.

    """

    def __init__(self):
        r"""
        :param LogList: Domain information
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogList: list of str
        :param PageSize: Number of results per page
        :type PageSize: int
        :param TotalCount: Total number of logs
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LogList = None
        self.PageSize = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogList = params.get("LogList")
        self.PageSize = params.get("PageSize")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDomainPurviewRequest(AbstractModel):
    """DescribeDomainPurview request structure.

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
        


class DescribeDomainPurviewResponse(AbstractModel):
    """DescribeDomainPurview response structure.

    """

    def __init__(self):
        r"""
        :param PurviewList: Permission list of the domain
        :type PurviewList: list of PurviewInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PurviewList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PurviewList") is not None:
            self.PurviewList = []
            for item in params.get("PurviewList"):
                obj = PurviewInfo()
                obj._deserialize(item)
                self.PurviewList.append(obj)
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


class DescribeDomainShareInfoRequest(AbstractModel):
    """DescribeDomainShareInfo request structure.

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
        


class DescribeDomainShareInfoResponse(AbstractModel):
    """DescribeDomainShareInfo response structure.

    """

    def __init__(self):
        r"""
        :param ShareList: Domain sharing information
        :type ShareList: list of DomainShareInfo
        :param Owner: Owner account of the domain
        :type Owner: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ShareList = None
        self.Owner = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ShareList") is not None:
            self.ShareList = []
            for item in params.get("ShareList"):
                obj = DomainShareInfo()
                obj._deserialize(item)
                self.ShareList.append(obj)
        self.Owner = params.get("Owner")
        self.RequestId = params.get("RequestId")


class DescribeRecordGroupListRequest(AbstractModel):
    """DescribeRecordGroupList request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain
        :type Domain: str
        :param DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored.
        :type DomainId: int
        :param Offset: Pagination offset
        :type Offset: int
        :param Limit: Number of items per page for pagination
        :type Limit: int
        """
        self.Domain = None
        self.DomainId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordGroupListResponse(AbstractModel):
    """DescribeRecordGroupList response structure.

    """

    def __init__(self):
        r"""
        :param GroupList: Group list
        :type GroupList: list of RecordGroupInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.GroupList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GroupList") is not None:
            self.GroupList = []
            for item in params.get("GroupList"):
                obj = RecordGroupInfo()
                obj._deserialize(item)
                self.GroupList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRecordLineListRequest(AbstractModel):
    """DescribeRecordLineList request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain.
        :type Domain: str
        :param DomainGrade: Domain level.
+ Original plan. Valid values: `D_FREE` (Free Plan); `D_PLUS` (Individual Plus Plan); `D_EXTRA` (Enterprise 1 Plan); `D_EXPERT` (Enterprise 2 Plan); `D_ULTRA` (Enterprise 3 Plan).
+ New plan. Valid values: `DP_FREE` (Free Version); `DP_PLUS` (Professional); `DP_EXTRA` (Enterprise Basic); `DP_EXPERT` (Enterprise); `DP_ULTRA` (Ultimate).
        :type DomainGrade: str
        :param DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self.Domain = None
        self.DomainGrade = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainGrade = params.get("DomainGrade")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordLineListResponse(AbstractModel):
    """DescribeRecordLineList response structure.

    """

    def __init__(self):
        r"""
        :param LineList: List of split zones.
        :type LineList: list of LineInfo
        :param LineGroupList: List of split zone groups.
        :type LineGroupList: list of LineGroupInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LineList = None
        self.LineGroupList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LineList") is not None:
            self.LineList = []
            for item in params.get("LineList"):
                obj = LineInfo()
                obj._deserialize(item)
                self.LineList.append(obj)
        if params.get("LineGroupList") is not None:
            self.LineGroupList = []
            for item in params.get("LineGroupList"):
                obj = LineGroupInfo()
                obj._deserialize(item)
                self.LineGroupList.append(obj)
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


class DescribeRecordTypeRequest(AbstractModel):
    """DescribeRecordType request structure.

    """

    def __init__(self):
        r"""
        :param DomainGrade: Domain level.
+ Original plan. Valid values: `D_FREE` (Free Plan); `D_PLUS` (Individual Plus Plan); `D_EXTRA` (Enterprise 1 Plan); `D_EXPERT` (Enterprise 2 Plan); `D_ULTRA` (Enterprise 3 Plan).
+ New plan. Valid values: `DP_FREE` (Free Version); `DP_PLUS` (Professional); `DP_EXTRA` (Enterprise Basic); `DP_EXPERT` (Enterprise); `DP_ULTRA` (Ultimate).
        :type DomainGrade: str
        """
        self.DomainGrade = None


    def _deserialize(self, params):
        self.DomainGrade = params.get("DomainGrade")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordTypeResponse(AbstractModel):
    """DescribeRecordType response structure.

    """

    def __init__(self):
        r"""
        :param TypeList: List of record types
        :type TypeList: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TypeList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TypeList = params.get("TypeList")
        self.RequestId = params.get("RequestId")


class DescribeSubdomainAnalyticsRequest(AbstractModel):
    """DescribeSubdomainAnalytics request structure.

    """

    def __init__(self):
        r"""
        :param Domain: The domain of the DNS query volume to be queried
        :type Domain: str
        :param StartDate: Query start date in the format of `YYYY-MM-DD`
        :type StartDate: str
        :param EndDate: Query end date in the format of `YYYY-MM-DD`
        :type EndDate: str
        :param Subdomain: The subdomain of the DNS query volume to be queried
        :type Subdomain: str
        :param DnsFormat: `DATE`: Daily. `HOUR`: Hourly
        :type DnsFormat: str
        :param DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self.Domain = None
        self.StartDate = None
        self.EndDate = None
        self.Subdomain = None
        self.DnsFormat = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Subdomain = params.get("Subdomain")
        self.DnsFormat = params.get("DnsFormat")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubdomainAnalyticsResponse(AbstractModel):
    """DescribeSubdomainAnalytics response structure.

    """

    def __init__(self):
        r"""
        :param Data: DNS query volume in the current statistical dimension
        :type Data: list of DomainAnalyticsDetail
        :param Info: Statistics on the DNS query volume of a subdomain
        :type Info: :class:`tencentcloud.dnspod.v20210323.models.SubdomainAnalyticsInfo`
        :param AliasData: DNS query volume of the subdomain alias
        :type AliasData: list of SubdomainAliasAnalyticsItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.Info = None
        self.AliasData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DomainAnalyticsDetail()
                obj._deserialize(item)
                self.Data.append(obj)
        if params.get("Info") is not None:
            self.Info = SubdomainAnalyticsInfo()
            self.Info._deserialize(params.get("Info"))
        if params.get("AliasData") is not None:
            self.AliasData = []
            for item in params.get("AliasData"):
                obj = SubdomainAliasAnalyticsItem()
                obj._deserialize(item)
                self.AliasData.append(obj)
        self.RequestId = params.get("RequestId")


class DomainAliasInfo(AbstractModel):
    """Information of a domain alias

    """

    def __init__(self):
        r"""
        :param Id: Domain alias ID
        :type Id: int
        :param DomainAlias: Domain alias
        :type DomainAlias: str
        """
        self.Id = None
        self.DomainAlias = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.DomainAlias = params.get("DomainAlias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainAnalyticsDetail(AbstractModel):
    """DNS query volume in the current statistical dimension

    """

    def __init__(self):
        r"""
        :param Num: DNS query volume in the current statistical dimension
        :type Num: int
        :param DateKey: Collection date for daily collection
        :type DateKey: str
        :param HourKey: The last hour (0–23) for hourly collection. For example, if `HourKey` is `23`, the DNS query volume in the statistical period of 22:00–23:00 will be collected.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HourKey: int
        """
        self.Num = None
        self.DateKey = None
        self.HourKey = None


    def _deserialize(self, params):
        self.Num = params.get("Num")
        self.DateKey = params.get("DateKey")
        self.HourKey = params.get("HourKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainCountInfo(AbstractModel):
    """List statistics by page

    """

    def __init__(self):
        r"""
        :param DomainTotal: Number of eligible domains
        :type DomainTotal: int
        :param AllTotal: Number of all domains that can be viewed by the user
        :type AllTotal: int
        :param MineTotal: Number of domains added under the user account
        :type MineTotal: int
        :param ShareTotal: Number of domains shared with the user
        :type ShareTotal: int
        :param VipTotal: Number of paid domains
        :type VipTotal: int
        :param PauseTotal: Number of suspended domains
        :type PauseTotal: int
        :param ErrorTotal: Number of domains with a DNS configuration error
        :type ErrorTotal: int
        :param LockTotal: Number of locked domains
        :type LockTotal: int
        :param SpamTotal: Number of blocked domains
        :type SpamTotal: int
        :param VipExpire: Number of domains that will expire within 30 days
        :type VipExpire: int
        :param ShareOutTotal: Number of domains shared with others
        :type ShareOutTotal: int
        :param GroupTotal: Number of domains in the specified group
        :type GroupTotal: int
        """
        self.DomainTotal = None
        self.AllTotal = None
        self.MineTotal = None
        self.ShareTotal = None
        self.VipTotal = None
        self.PauseTotal = None
        self.ErrorTotal = None
        self.LockTotal = None
        self.SpamTotal = None
        self.VipExpire = None
        self.ShareOutTotal = None
        self.GroupTotal = None


    def _deserialize(self, params):
        self.DomainTotal = params.get("DomainTotal")
        self.AllTotal = params.get("AllTotal")
        self.MineTotal = params.get("MineTotal")
        self.ShareTotal = params.get("ShareTotal")
        self.VipTotal = params.get("VipTotal")
        self.PauseTotal = params.get("PauseTotal")
        self.ErrorTotal = params.get("ErrorTotal")
        self.LockTotal = params.get("LockTotal")
        self.SpamTotal = params.get("SpamTotal")
        self.VipExpire = params.get("VipExpire")
        self.ShareOutTotal = params.get("ShareOutTotal")
        self.GroupTotal = params.get("GroupTotal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        


class DomainListItem(AbstractModel):
    """Element in the domain list

    """

    def __init__(self):
        r"""
        :param DomainId: Unique ID assigned to the domain by the system
        :type DomainId: int
        :param Name: Original format of the domain
        :type Name: str
        :param Status: Domain status. Valid values: `ENABLE` (normal), `PAUSE` (suspended), `SPAM` (blocked).
        :type Status: str
        :param TTL: Default TTL of the default DNS record of the domain
        :type TTL: int
        :param CNAMESpeedup: Whether CNAME flattening is enabled. Valid values: `ENABLE` (enabled); `DISABLE` (disabled).
        :type CNAMESpeedup: str
        :param DNSStatus: DNS configuration status. Valid values: `DNSERROR` (error), an empty string (normal).
        :type DNSStatus: str
        :param Grade: Plan level code of the domain
        :type Grade: str
        :param GroupId: Group ID of the domain
        :type GroupId: int
        :param SearchEnginePush: Whether search engine push optimization is enabled. Valid values: `YES` (yes), `NO` (no).
        :type SearchEnginePush: str
        :param Remark: Domain remarks
        :type Remark: str
        :param Punycode: Punycode-encoded domain format
        :type Punycode: str
        :param EffectiveDNS: Effective DNS assigned to the domain by the system
        :type EffectiveDNS: list of str
        :param GradeLevel: Number corresponding to the plan level of the domain
        :type GradeLevel: int
        :param GradeTitle: Plan name
        :type GradeTitle: str
        :param IsVip: Whether it is a paid plan
        :type IsVip: str
        :param VipStartAt: Activation time of the paid plan
        :type VipStartAt: str
        :param VipEndAt: Expiry time of the paid plan
        :type VipEndAt: str
        :param VipAutoRenew: Whether VIP automatic renewal is enabled for the domain. Valid values: `YES` (yes); `NO` (no). Default value: `DEFAULT`.
        :type VipAutoRenew: str
        :param RecordCount: Number of records under the domain
        :type RecordCount: int
        :param CreatedOn: Domain adding time
        :type CreatedOn: str
        :param UpdatedOn: Domain update time
        :type UpdatedOn: str
        :param Owner: Account of the domain
        :type Owner: str
        """
        self.DomainId = None
        self.Name = None
        self.Status = None
        self.TTL = None
        self.CNAMESpeedup = None
        self.DNSStatus = None
        self.Grade = None
        self.GroupId = None
        self.SearchEnginePush = None
        self.Remark = None
        self.Punycode = None
        self.EffectiveDNS = None
        self.GradeLevel = None
        self.GradeTitle = None
        self.IsVip = None
        self.VipStartAt = None
        self.VipEndAt = None
        self.VipAutoRenew = None
        self.RecordCount = None
        self.CreatedOn = None
        self.UpdatedOn = None
        self.Owner = None


    def _deserialize(self, params):
        self.DomainId = params.get("DomainId")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.TTL = params.get("TTL")
        self.CNAMESpeedup = params.get("CNAMESpeedup")
        self.DNSStatus = params.get("DNSStatus")
        self.Grade = params.get("Grade")
        self.GroupId = params.get("GroupId")
        self.SearchEnginePush = params.get("SearchEnginePush")
        self.Remark = params.get("Remark")
        self.Punycode = params.get("Punycode")
        self.EffectiveDNS = params.get("EffectiveDNS")
        self.GradeLevel = params.get("GradeLevel")
        self.GradeTitle = params.get("GradeTitle")
        self.IsVip = params.get("IsVip")
        self.VipStartAt = params.get("VipStartAt")
        self.VipEndAt = params.get("VipEndAt")
        self.VipAutoRenew = params.get("VipAutoRenew")
        self.RecordCount = params.get("RecordCount")
        self.CreatedOn = params.get("CreatedOn")
        self.UpdatedOn = params.get("UpdatedOn")
        self.Owner = params.get("Owner")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainShareInfo(AbstractModel):
    """Domain sharing information

    """

    def __init__(self):
        r"""
        :param ShareTo: Account with which the domain is shared
        :type ShareTo: str
        :param Mode: Sharing mode. Valid values: `rw` (read/write), `r` (read-only).
        :type Mode: str
        :param Status: Sharing status. Valid values: `enabled` (shared successfully); `pending` (the account shared to does not exist and is pending registration).
        :type Status: str
        """
        self.ShareTo = None
        self.Mode = None
        self.Status = None


    def _deserialize(self, params):
        self.ShareTo = params.get("ShareTo")
        self.Mode = params.get("Mode")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfo(AbstractModel):
    """List of domain groups

    """

    def __init__(self):
        r"""
        :param GroupId: Group ID
        :type GroupId: int
        :param GroupName: Group name
        :type GroupName: str
        :param GroupType: Group type
        :type GroupType: str
        :param Size: Number of domains in the group
        :type Size: int
        """
        self.GroupId = None
        self.GroupName = None
        self.GroupType = None
        self.Size = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.GroupType = params.get("GroupType")
        self.Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LineGroupInfo(AbstractModel):
    """Information of a split zone group

    """

    def __init__(self):
        r"""
        :param LineId: Split zone group ID
        :type LineId: str
        :param Name: Split zone group name
        :type Name: str
        :param Type: Group type
        :type Type: str
        :param LineList: List of split zones in the split zone group
        :type LineList: list of str
        """
        self.LineId = None
        self.Name = None
        self.Type = None
        self.LineList = None


    def _deserialize(self, params):
        self.LineId = params.get("LineId")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.LineList = params.get("LineList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LineInfo(AbstractModel):
    """Information of a split zone

    """

    def __init__(self):
        r"""
        :param Name: Split zone name
        :type Name: str
        :param LineId: Split zone ID
        :type LineId: str
        """
        self.Name = None
        self.LineId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.LineId = params.get("LineId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LockInfo(AbstractModel):
    """Domain lock information

    """

    def __init__(self):
        r"""
        :param DomainId: Domain ID
        :type DomainId: int
        :param LockCode: Domain unlock code
        :type LockCode: str
        :param LockEnd: Automatic unlock date of the domain
        :type LockEnd: str
        """
        self.DomainId = None
        self.LockCode = None
        self.LockEnd = None


    def _deserialize(self, params):
        self.DomainId = params.get("DomainId")
        self.LockCode = params.get("LockCode")
        self.LockEnd = params.get("LockEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainLockRequest(AbstractModel):
    """ModifyDomainLock request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain
        :type Domain: str
        :param LockDays: Number of days to lock the domain. The maximum number of locked days can be obtained by calling the API for getting the permissions of a domain.
        :type LockDays: int
        :param DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self.Domain = None
        self.LockDays = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.LockDays = params.get("LockDays")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainLockResponse(AbstractModel):
    """ModifyDomainLock response structure.

    """

    def __init__(self):
        r"""
        :param LockInfo: Domain lock information
        :type LockInfo: :class:`tencentcloud.dnspod.v20210323.models.LockInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LockInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LockInfo") is not None:
            self.LockInfo = LockInfo()
            self.LockInfo._deserialize(params.get("LockInfo"))
        self.RequestId = params.get("RequestId")


class ModifyDomainOwnerRequest(AbstractModel):
    """ModifyDomainOwner request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain
        :type Domain: str
        :param Account: The account to which to transfer the domain, which can be an UIN or email address
        :type Account: str
        :param DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self.Domain = None
        self.Account = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Account = params.get("Account")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainOwnerResponse(AbstractModel):
    """ModifyDomainOwner response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


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


class ModifyDomainUnlockRequest(AbstractModel):
    """ModifyDomainUnlock request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain
        :type Domain: str
        :param LockCode: Domain unlock code, which will be returned when the domain is locked.
        :type LockCode: str
        :param DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self.Domain = None
        self.LockCode = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.LockCode = params.get("LockCode")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainUnlockResponse(AbstractModel):
    """ModifyDomainUnlock response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRecordBatchDetail(AbstractModel):
    """Response structure for bulk adding records

    """

    def __init__(self):
        r"""
        :param RecordList: See `RecordInfoBatchModify`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordList: list of BatchRecordInfo
        :param Id: Task ID
        :type Id: int
        :param Domain: Domain
Note: This field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param DomainGrade: Domain level
Note: This field may return null, indicating that no valid values can be obtained.
        :type DomainGrade: str
        :param ErrMsg: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrMsg: str
        :param Status: Task running status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param Operation: Operation type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Operation: str
        :param DomainId: Domain ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type DomainId: int
        """
        self.RecordList = None
        self.Id = None
        self.Domain = None
        self.DomainGrade = None
        self.ErrMsg = None
        self.Status = None
        self.Operation = None
        self.DomainId = None


    def _deserialize(self, params):
        if params.get("RecordList") is not None:
            self.RecordList = []
            for item in params.get("RecordList"):
                obj = BatchRecordInfo()
                obj._deserialize(item)
                self.RecordList.append(obj)
        self.Id = params.get("Id")
        self.Domain = params.get("Domain")
        self.DomainGrade = params.get("DomainGrade")
        self.ErrMsg = params.get("ErrMsg")
        self.Status = params.get("Status")
        self.Operation = params.get("Operation")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordBatchRequest(AbstractModel):
    """ModifyRecordBatch request structure.

    """

    def __init__(self):
        r"""
        :param RecordIdList: Array of record IDs. You can view all DNS records and their IDs via the `DescribeRecordList` API.
        :type RecordIdList: list of int non-negative
        :param Change: The field to be modified. Valid values: `sub_domain`, `record_type`, `area`, `value`, `mx`, `ttl`, `status`.
        :type Change: str
        :param ChangeTo: The value to be changed to, which is required and subject to the `change` field.
        :type ChangeTo: str
        :param Value: The record value to be changed to, which is required only if the `change` field is `record_type`.
        :type Value: str
        :param MX: MX record priority, which is required only if the `Change` field is `mx`.
        :type MX: str
        """
        self.RecordIdList = None
        self.Change = None
        self.ChangeTo = None
        self.Value = None
        self.MX = None


    def _deserialize(self, params):
        self.RecordIdList = params.get("RecordIdList")
        self.Change = params.get("Change")
        self.ChangeTo = params.get("ChangeTo")
        self.Value = params.get("Value")
        self.MX = params.get("MX")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordBatchResponse(AbstractModel):
    """ModifyRecordBatch response structure.

    """

    def __init__(self):
        r"""
        :param JobId: Bulk task ID
        :type JobId: int
        :param DetailList: See `modifyRecordBatchDetail`.
        :type DetailList: list of ModifyRecordBatchDetail
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.JobId = None
        self.DetailList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        if params.get("DetailList") is not None:
            self.DetailList = []
            for item in params.get("DetailList"):
                obj = ModifyRecordBatchDetail()
                obj._deserialize(item)
                self.DetailList.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyRecordGroupRequest(AbstractModel):
    """ModifyRecordGroup request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain
        :type Domain: str
        :param GroupName: Group name
        :type GroupName: str
        :param GroupId: ID of the group to be modified
        :type GroupId: int
        :param DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored.
        :type DomainId: int
        """
        self.Domain = None
        self.GroupName = None
        self.GroupId = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.GroupName = params.get("GroupName")
        self.GroupId = params.get("GroupId")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordGroupResponse(AbstractModel):
    """ModifyRecordGroup response structure.

    """

    def __init__(self):
        r"""
        :param GroupId: ID of the modified group
        :type GroupId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")


class ModifyRecordRemarkRequest(AbstractModel):
    """ModifyRecordRemark request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain
        :type Domain: str
        :param RecordId: The record ID. You can view all DNS records and their IDs via the `DescribeRecordList` API.
        :type RecordId: int
        :param DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        :param Remark: DNS record remarks. To delete the remarks, submit empty content.
        :type Remark: str
        """
        self.Domain = None
        self.RecordId = None
        self.DomainId = None
        self.Remark = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.RecordId = params.get("RecordId")
        self.DomainId = params.get("DomainId")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordRemarkResponse(AbstractModel):
    """ModifyRecordRemark response structure.

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


class ModifyRecordStatusRequest(AbstractModel):
    """ModifyRecordStatus request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain
        :type Domain: str
        :param RecordId: The record ID. You can view all DNS records and their IDs via the `DescribeRecordList` API.
        :type RecordId: int
        :param Status: Record status. Valid values: `ENABLE`, `DISABLE`. If `DISABLE` is passed in, the DNS record won't take effect, and the limit on round-robin DNS won't be verified.
        :type Status: str
        :param DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self.Domain = None
        self.RecordId = None
        self.Status = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.RecordId = params.get("RecordId")
        self.Status = params.get("Status")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordStatusResponse(AbstractModel):
    """ModifyRecordStatus response structure.

    """

    def __init__(self):
        r"""
        :param RecordId: Record ID.
        :type RecordId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RecordId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RecordId = params.get("RecordId")
        self.RequestId = params.get("RequestId")


class ModifyRecordToGroupRequest(AbstractModel):
    """ModifyRecordToGroup request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain
        :type Domain: str
        :param GroupId: Group ID
        :type GroupId: int
        :param RecordId: Record ID. Separate multiple IDs by vertical bar ("|").
        :type RecordId: str
        :param DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored.
        :type DomainId: int
        """
        self.Domain = None
        self.GroupId = None
        self.RecordId = None
        self.DomainId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.GroupId = params.get("GroupId")
        self.RecordId = params.get("RecordId")
        self.DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordToGroupResponse(AbstractModel):
    """ModifyRecordToGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PurviewInfo(AbstractModel):
    """Domain permission

    """

    def __init__(self):
        r"""
        :param Name: Permission name
        :type Name: str
        :param Value: Permission value
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
        


class RecordGroupInfo(AbstractModel):
    """Information of a DNS record group

    """

    def __init__(self):
        r"""
        :param GroupId: Group ID
        :type GroupId: int
        :param GroupName: Group name
        :type GroupName: str
        :param GroupType: Group type. Valid values: `system`, `user`.
        :type GroupType: str
        """
        self.GroupId = None
        self.GroupName = None
        self.GroupType = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.GroupType = params.get("GroupType")
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
        :param DefaultNS: Whether it is a default NS record.
        :type DefaultNS: bool
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
        self.DefaultNS = None


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
        self.DefaultNS = params.get("DefaultNS")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubdomainAliasAnalyticsItem(AbstractModel):
    """DNS query volume of the subdomain alias

    """

    def __init__(self):
        r"""
        :param Info: Statistics on the DNS query volume of a subdomain
        :type Info: :class:`tencentcloud.dnspod.v20210323.models.SubdomainAnalyticsInfo`
        :param Data: DNS query volume in the current statistical dimension
        :type Data: list of DomainAnalyticsDetail
        """
        self.Info = None
        self.Data = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = SubdomainAnalyticsInfo()
            self.Info._deserialize(params.get("Info"))
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DomainAnalyticsDetail()
                obj._deserialize(item)
                self.Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubdomainAnalyticsInfo(AbstractModel):
    """Statistics on the DNS query volume of a subdomain

    """

    def __init__(self):
        r"""
        :param DnsFormat: `DATE`: Daily; `HOUR`: Hourly
        :type DnsFormat: str
        :param DnsTotal: Total DNS query volume for the current statistical period
        :type DnsTotal: int
        :param Domain: The queried domain
        :type Domain: str
        :param StartDate: Start date of the current statistical period
        :type StartDate: str
        :param EndDate: End date of the current statistical period
        :type EndDate: str
        :param Subdomain: Subdomain
        :type Subdomain: str
        """
        self.DnsFormat = None
        self.DnsTotal = None
        self.Domain = None
        self.StartDate = None
        self.EndDate = None
        self.Subdomain = None


    def _deserialize(self, params):
        self.DnsFormat = params.get("DnsFormat")
        self.DnsTotal = params.get("DnsTotal")
        self.Domain = params.get("Domain")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Subdomain = params.get("Subdomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        