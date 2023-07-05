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
        :param _RecordType: Record type. For more information, see the `DescribeRecordType` API.
        :type RecordType: str
        :param _Value: Record value.
        :type Value: str
        :param _SubDomain: Subdomain (host record), which is `@` by default.
        :type SubDomain: str
        :param _RecordLine: Split zone of the DNS record. For more information, see the `DescribeRecordLineList` API. If neither `RecordLine` nor `RecordLineId` is specified, the default split zone will be used.
        :type RecordLine: str
        :param _RecordLineId: Split zone ID of the DNS record. If both `RecordLine` and `RecordLineId` are specified, `RecordLineId` will be used.
        :type RecordLineId: str
        :param _Weight: The record weight (not supported).
        :type Weight: int
        :param _MX: MX record value. It is `0` by default for non-MX records and required for MX records.
        :type MX: int
        :param _TTL: TTL value of the record, which is `600` by default.
        :type TTL: int
        :param _Enabled: Record status (not supported). Valid values: `0` (disabled); `1` (enabled). Default value: `1`.
        :type Enabled: int
        :param _Remark: Record remarks (not supported).
        :type Remark: str
        """
        self._RecordType = None
        self._Value = None
        self._SubDomain = None
        self._RecordLine = None
        self._RecordLineId = None
        self._Weight = None
        self._MX = None
        self._TTL = None
        self._Enabled = None
        self._Remark = None

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordLine(self):
        return self._RecordLine

    @RecordLine.setter
    def RecordLine(self, RecordLine):
        self._RecordLine = RecordLine

    @property
    def RecordLineId(self):
        return self._RecordLineId

    @RecordLineId.setter
    def RecordLineId(self, RecordLineId):
        self._RecordLineId = RecordLineId

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def MX(self):
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX

    @property
    def TTL(self):
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._RecordType = params.get("RecordType")
        self._Value = params.get("Value")
        self._SubDomain = params.get("SubDomain")
        self._RecordLine = params.get("RecordLine")
        self._RecordLineId = params.get("RecordLineId")
        self._Weight = params.get("Weight")
        self._MX = params.get("MX")
        self._TTL = params.get("TTL")
        self._Enabled = params.get("Enabled")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchRecordInfo(AbstractModel):
    """Record information in the bulk task

    """

    def __init__(self):
        r"""
        :param _RecordId: Record ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordId: int
        :param _SubDomain: Subdomain (host record).
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubDomain: str
        :param _RecordType: Record type. For more information, see the `DescribeRecordType` API.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordType: str
        :param _RecordLine: Split zone of the DNS record. For more information, see the `DescribeRecordLineList` API.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordLine: str
        :param _Value: Record value
Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: str
        :param _TTL: TTL value of the record
Note: This field may return null, indicating that no valid values can be obtained.
        :type TTL: int
        :param _Status: Record adding status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _Operation: Operation type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Operation: str
        :param _ErrMsg: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrMsg: str
        :param _Id: ID of the record in the list
        :type Id: int
        :param _Enabled: Record status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Enabled: int
        :param _MX: MX weight of the record
Note: This field may return null, indicating that no valid values can be obtained.
        :type MX: int
        :param _Weight: The record weight.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Weight: int
        """
        self._RecordId = None
        self._SubDomain = None
        self._RecordType = None
        self._RecordLine = None
        self._Value = None
        self._TTL = None
        self._Status = None
        self._Operation = None
        self._ErrMsg = None
        self._Id = None
        self._Enabled = None
        self._MX = None
        self._Weight = None

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RecordLine(self):
        return self._RecordLine

    @RecordLine.setter
    def RecordLine(self, RecordLine):
        self._RecordLine = RecordLine

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def TTL(self):
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def MX(self):
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._RecordId = params.get("RecordId")
        self._SubDomain = params.get("SubDomain")
        self._RecordType = params.get("RecordType")
        self._RecordLine = params.get("RecordLine")
        self._Value = params.get("Value")
        self._TTL = params.get("TTL")
        self._Status = params.get("Status")
        self._Operation = params.get("Operation")
        self._ErrMsg = params.get("ErrMsg")
        self._Id = params.get("Id")
        self._Enabled = params.get("Enabled")
        self._MX = params.get("MX")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainAliasRequest(AbstractModel):
    """CreateDomainAlias request structure.

    """

    def __init__(self):
        r"""
        :param _DomainAlias: Domain alias
        :type DomainAlias: str
        :param _Domain: Domain
        :type Domain: str
        :param _DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self._DomainAlias = None
        self._Domain = None
        self._DomainId = None

    @property
    def DomainAlias(self):
        return self._DomainAlias

    @DomainAlias.setter
    def DomainAlias(self, DomainAlias):
        self._DomainAlias = DomainAlias

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._DomainAlias = params.get("DomainAlias")
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainAliasResponse(AbstractModel):
    """CreateDomainAlias response structure.

    """

    def __init__(self):
        r"""
        :param _DomainAliasId: Domain alias ID
        :type DomainAliasId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DomainAliasId = None
        self._RequestId = None

    @property
    def DomainAliasId(self):
        return self._DomainAliasId

    @DomainAliasId.setter
    def DomainAliasId(self, DomainAliasId):
        self._DomainAliasId = DomainAliasId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DomainAliasId = params.get("DomainAliasId")
        self._RequestId = params.get("RequestId")


class CreateDomainBatchDetail(AbstractModel):
    """Response structure for bulk adding domains

    """

    def __init__(self):
        r"""
        :param _RecordList: See `RecordInfoBatch`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordList: list of CreateDomainBatchRecord
        :param _Id: Task ID
        :type Id: int
        :param _Domain: Domain
Note: This field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param _DomainGrade: Domain level
Note: This field may return null, indicating that no valid values can be obtained.
        :type DomainGrade: str
        :param _ErrMsg: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrMsg: str
        :param _Status: Task running status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _Operation: Operation type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Operation: str
        """
        self._RecordList = None
        self._Id = None
        self._Domain = None
        self._DomainGrade = None
        self._ErrMsg = None
        self._Status = None
        self._Operation = None

    @property
    def RecordList(self):
        return self._RecordList

    @RecordList.setter
    def RecordList(self, RecordList):
        self._RecordList = RecordList

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainGrade(self):
        return self._DomainGrade

    @DomainGrade.setter
    def DomainGrade(self, DomainGrade):
        self._DomainGrade = DomainGrade

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation


    def _deserialize(self, params):
        if params.get("RecordList") is not None:
            self._RecordList = []
            for item in params.get("RecordList"):
                obj = CreateDomainBatchRecord()
                obj._deserialize(item)
                self._RecordList.append(obj)
        self._Id = params.get("Id")
        self._Domain = params.get("Domain")
        self._DomainGrade = params.get("DomainGrade")
        self._ErrMsg = params.get("ErrMsg")
        self._Status = params.get("Status")
        self._Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainBatchRecord(AbstractModel):
    """Record information in the task of bulk adding domains

    """

    def __init__(self):
        r"""
        :param _SubDomain: Subdomain (host record).
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubDomain: str
        :param _RecordType: Record type. For more information, see the `DescribeRecordType` API.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordType: str
        :param _RecordLine: Split zone of the DNS record. For more information, see the `DescribeRecordLineList` API.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordLine: str
        :param _Value: Record value
Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: str
        :param _TTL: TTL value of the record
Note: This field may return null, indicating that no valid values can be obtained.
        :type TTL: int
        :param _Status: Record adding status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _Operation: Operation type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Operation: str
        :param _ErrMsg: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrMsg: str
        :param _Id: ID of the record in the list
        :type Id: int
        """
        self._SubDomain = None
        self._RecordType = None
        self._RecordLine = None
        self._Value = None
        self._TTL = None
        self._Status = None
        self._Operation = None
        self._ErrMsg = None
        self._Id = None

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RecordLine(self):
        return self._RecordLine

    @RecordLine.setter
    def RecordLine(self, RecordLine):
        self._RecordLine = RecordLine

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def TTL(self):
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._SubDomain = params.get("SubDomain")
        self._RecordType = params.get("RecordType")
        self._RecordLine = params.get("RecordLine")
        self._Value = params.get("Value")
        self._TTL = params.get("TTL")
        self._Status = params.get("Status")
        self._Operation = params.get("Operation")
        self._ErrMsg = params.get("ErrMsg")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainBatchRequest(AbstractModel):
    """CreateDomainBatch request structure.

    """

    def __init__(self):
        r"""
        :param _DomainList: Domain array
        :type DomainList: list of str
        :param _RecordValue: Add A records of @ and www for each domain with the record value of the IP. If this parameter is not passed in or is set to an empty string or null, only the domain but not the records will be added.
        :type RecordValue: str
        """
        self._DomainList = None
        self._RecordValue = None

    @property
    def DomainList(self):
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList

    @property
    def RecordValue(self):
        return self._RecordValue

    @RecordValue.setter
    def RecordValue(self, RecordValue):
        self._RecordValue = RecordValue


    def _deserialize(self, params):
        self._DomainList = params.get("DomainList")
        self._RecordValue = params.get("RecordValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainBatchResponse(AbstractModel):
    """CreateDomainBatch response structure.

    """

    def __init__(self):
        r"""
        :param _DetailList: Information of the bulk added domains
        :type DetailList: list of CreateDomainBatchDetail
        :param _JobId: Bulk task ID
        :type JobId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DetailList = None
        self._JobId = None
        self._RequestId = None

    @property
    def DetailList(self):
        return self._DetailList

    @DetailList.setter
    def DetailList(self, DetailList):
        self._DetailList = DetailList

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DetailList") is not None:
            self._DetailList = []
            for item in params.get("DetailList"):
                obj = CreateDomainBatchDetail()
                obj._deserialize(item)
                self._DetailList.append(obj)
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class CreateDomainGroupRequest(AbstractModel):
    """CreateDomainGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GroupName: Domain group
        :type GroupName: str
        """
        self._GroupName = None

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainGroupResponse(AbstractModel):
    """CreateDomainGroup response structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Domain group ID
        :type GroupId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class CreateDomainRequest(AbstractModel):
    """CreateDomain request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain
        :type Domain: str
        :param _GroupId: The group ID of the domain. You can view the group information of this domain via the `DescribeDomainGroupList` API.
        :type GroupId: int
        :param _IsMark: Whether the domain is starred. Valid values: yes, no.
        :type IsMark: str
        """
        self._Domain = None
        self._GroupId = None
        self._IsMark = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def IsMark(self):
        return self._IsMark

    @IsMark.setter
    def IsMark(self, IsMark):
        self._IsMark = IsMark


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._GroupId = params.get("GroupId")
        self._IsMark = params.get("IsMark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainResponse(AbstractModel):
    """CreateDomain response structure.

    """

    def __init__(self):
        r"""
        :param _DomainInfo: Domain information
        :type DomainInfo: :class:`tencentcloud.dnspod.v20210323.models.DomainCreateInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DomainInfo = None
        self._RequestId = None

    @property
    def DomainInfo(self):
        return self._DomainInfo

    @DomainInfo.setter
    def DomainInfo(self, DomainInfo):
        self._DomainInfo = DomainInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DomainInfo") is not None:
            self._DomainInfo = DomainCreateInfo()
            self._DomainInfo._deserialize(params.get("DomainInfo"))
        self._RequestId = params.get("RequestId")


class CreateRecordBatchDetail(AbstractModel):
    """Response structure for bulk adding records

    """

    def __init__(self):
        r"""
        :param _RecordList: See `RecordInfoBatch`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordList: list of CreateRecordBatchRecord
        :param _Id: Task ID
        :type Id: int
        :param _Domain: Domain
Note: This field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param _DomainGrade: Domain level
Note: This field may return null, indicating that no valid values can be obtained.
        :type DomainGrade: str
        :param _ErrMsg: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrMsg: str
        :param _Status: Task running status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _Operation: Operation type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Operation: str
        :param _DomainId: Domain ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type DomainId: int
        """
        self._RecordList = None
        self._Id = None
        self._Domain = None
        self._DomainGrade = None
        self._ErrMsg = None
        self._Status = None
        self._Operation = None
        self._DomainId = None

    @property
    def RecordList(self):
        return self._RecordList

    @RecordList.setter
    def RecordList(self, RecordList):
        self._RecordList = RecordList

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainGrade(self):
        return self._DomainGrade

    @DomainGrade.setter
    def DomainGrade(self, DomainGrade):
        self._DomainGrade = DomainGrade

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        if params.get("RecordList") is not None:
            self._RecordList = []
            for item in params.get("RecordList"):
                obj = CreateRecordBatchRecord()
                obj._deserialize(item)
                self._RecordList.append(obj)
        self._Id = params.get("Id")
        self._Domain = params.get("Domain")
        self._DomainGrade = params.get("DomainGrade")
        self._ErrMsg = params.get("ErrMsg")
        self._Status = params.get("Status")
        self._Operation = params.get("Operation")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordBatchRecord(AbstractModel):
    """Record information in the task of bulk adding records

    """

    def __init__(self):
        r"""
        :param _SubDomain: Subdomain (host record).
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubDomain: str
        :param _RecordType: Record type. For more information, see the `DescribeRecordType` API.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordType: str
        :param _RecordLine: Split zone of the DNS record. For more information, see the `DescribeRecordLineList` API.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordLine: str
        :param _Value: Record value
Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: str
        :param _TTL: TTL value of the record
Note: This field may return null, indicating that no valid values can be obtained.
        :type TTL: int
        :param _Status: Record adding status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _Operation: Operation type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Operation: str
        :param _ErrMsg: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrMsg: str
        :param _Id: ID of the record in the list
        :type Id: int
        :param _MX: MX weight of the record
Note: This field may return null, indicating that no valid values can be obtained.
        :type MX: int
        :param _Weight: The record weight.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Weight: int
        """
        self._SubDomain = None
        self._RecordType = None
        self._RecordLine = None
        self._Value = None
        self._TTL = None
        self._Status = None
        self._Operation = None
        self._ErrMsg = None
        self._Id = None
        self._MX = None
        self._Weight = None

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RecordLine(self):
        return self._RecordLine

    @RecordLine.setter
    def RecordLine(self, RecordLine):
        self._RecordLine = RecordLine

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def TTL(self):
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MX(self):
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._SubDomain = params.get("SubDomain")
        self._RecordType = params.get("RecordType")
        self._RecordLine = params.get("RecordLine")
        self._Value = params.get("Value")
        self._TTL = params.get("TTL")
        self._Status = params.get("Status")
        self._Operation = params.get("Operation")
        self._ErrMsg = params.get("ErrMsg")
        self._Id = params.get("Id")
        self._MX = params.get("MX")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordBatchRequest(AbstractModel):
    """CreateRecordBatch request structure.

    """

    def __init__(self):
        r"""
        :param _DomainIdList: Domain ID. Separate multiple ones by comma.
        :type DomainIdList: list of str
        :param _RecordList: Record array
        :type RecordList: list of AddRecordBatch
        """
        self._DomainIdList = None
        self._RecordList = None

    @property
    def DomainIdList(self):
        return self._DomainIdList

    @DomainIdList.setter
    def DomainIdList(self, DomainIdList):
        self._DomainIdList = DomainIdList

    @property
    def RecordList(self):
        return self._RecordList

    @RecordList.setter
    def RecordList(self, RecordList):
        self._RecordList = RecordList


    def _deserialize(self, params):
        self._DomainIdList = params.get("DomainIdList")
        if params.get("RecordList") is not None:
            self._RecordList = []
            for item in params.get("RecordList"):
                obj = AddRecordBatch()
                obj._deserialize(item)
                self._RecordList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordBatchResponse(AbstractModel):
    """CreateRecordBatch response structure.

    """

    def __init__(self):
        r"""
        :param _DetailList: Information of the bulk added domains
        :type DetailList: list of CreateRecordBatchDetail
        :param _JobId: Bulk task ID
        :type JobId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DetailList = None
        self._JobId = None
        self._RequestId = None

    @property
    def DetailList(self):
        return self._DetailList

    @DetailList.setter
    def DetailList(self, DetailList):
        self._DetailList = DetailList

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DetailList") is not None:
            self._DetailList = []
            for item in params.get("DetailList"):
                obj = CreateRecordBatchDetail()
                obj._deserialize(item)
                self._DetailList.append(obj)
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class CreateRecordGroupRequest(AbstractModel):
    """CreateRecordGroup request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain
        :type Domain: str
        :param _GroupName: Group name
        :type GroupName: str
        :param _DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored.
        :type DomainId: int
        """
        self._Domain = None
        self._GroupName = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._GroupName = params.get("GroupName")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordGroupResponse(AbstractModel):
    """CreateRecordGroup response structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: New group ID
        :type GroupId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class CreateRecordRequest(AbstractModel):
    """CreateRecord request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain
        :type Domain: str
        :param _RecordType: Record type, which is obtained through the record type API. The value contains uppercase letters, such as `A`.
        :type RecordType: str
        :param _RecordLine: Record split zone, which is obtained through the record split zone API.
        :type RecordLine: str
        :param _Value: Record value, such as `IP : 200.200.200.200`, `CNAME : cname.dnspod.com`, and `MX : mail.dnspod.com`.
        :type Value: str
        :param _DomainId: Domain ID. The `DomainId` parameter has a higher priority than `Domain`. If `DomainId` is passed in, `Domain` will be ignored.
        :type DomainId: int
        :param _SubDomain: Host record such as `www`. If it is not passed in, it will be `@` by default.
        :type SubDomain: str
        :param _RecordLineId: Split zone ID, which is obtained through the record split zone API. The value is a string such as `10=1`. The `RecordLineId` parameter has a higher priority than `RecordLine`. If both of them are passed in, `RecordLineId` will be used first.
        :type RecordLineId: str
        :param _MX: MX priority, which is required for an MX record and will take effect if the record type is MX. Value range: 1–20.
        :type MX: int
        :param _TTL: TTL. Value range: 1–604800. The minimum value varies by domain level.
        :type TTL: int
        :param _Weight: Weight information, which is an integer between 0 and 100. It is supported only for enterprise VIP domains. `0` indicates not to pass in this parameter, i.e., not to set the weight.
        :type Weight: int
        :param _Status: Initial status of the record. Valid values: ENABLE, DISABLE. Default value: ENABLE. If `DISABLE` is passed in, the DNS record won't take effect, and the limit on round-robin DNS won't be verified.
        :type Status: str
        """
        self._Domain = None
        self._RecordType = None
        self._RecordLine = None
        self._Value = None
        self._DomainId = None
        self._SubDomain = None
        self._RecordLineId = None
        self._MX = None
        self._TTL = None
        self._Weight = None
        self._Status = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RecordLine(self):
        return self._RecordLine

    @RecordLine.setter
    def RecordLine(self, RecordLine):
        self._RecordLine = RecordLine

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordLineId(self):
        return self._RecordLineId

    @RecordLineId.setter
    def RecordLineId(self, RecordLineId):
        self._RecordLineId = RecordLineId

    @property
    def MX(self):
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX

    @property
    def TTL(self):
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._RecordType = params.get("RecordType")
        self._RecordLine = params.get("RecordLine")
        self._Value = params.get("Value")
        self._DomainId = params.get("DomainId")
        self._SubDomain = params.get("SubDomain")
        self._RecordLineId = params.get("RecordLineId")
        self._MX = params.get("MX")
        self._TTL = params.get("TTL")
        self._Weight = params.get("Weight")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordResponse(AbstractModel):
    """CreateRecord response structure.

    """

    def __init__(self):
        r"""
        :param _RecordId: Record ID
        :type RecordId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RecordId = None
        self._RequestId = None

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RecordId = params.get("RecordId")
        self._RequestId = params.get("RequestId")


class DeleteDomainAliasRequest(AbstractModel):
    """DeleteDomainAlias request structure.

    """

    def __init__(self):
        r"""
        :param _DomainAliasId: Domain alias ID. You can view all domain aliases and their IDs via the `DescribeDomainAliasList` API.
        :type DomainAliasId: int
        :param _Domain: Domain
        :type Domain: str
        :param _DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self._DomainAliasId = None
        self._Domain = None
        self._DomainId = None

    @property
    def DomainAliasId(self):
        return self._DomainAliasId

    @DomainAliasId.setter
    def DomainAliasId(self, DomainAliasId):
        self._DomainAliasId = DomainAliasId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._DomainAliasId = params.get("DomainAliasId")
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainAliasResponse(AbstractModel):
    """DeleteDomainAlias response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteDomainBatchDetail(AbstractModel):
    """Details of batch deleting domains

    """

    def __init__(self):
        r"""
        :param _DomainId: The domain ID.
        :type DomainId: int
        :param _Domain: The domain name.
        :type Domain: str
        :param _Error: The error message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Error: str
        :param _Status: The domain deletion status.
        :type Status: str
        :param _Operation: The operation.
        :type Operation: str
        """
        self._DomainId = None
        self._Domain = None
        self._Error = None
        self._Status = None
        self._Operation = None

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Error(self):
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        self._Domain = params.get("Domain")
        self._Error = params.get("Error")
        self._Status = params.get("Status")
        self._Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainBatchRequest(AbstractModel):
    """DeleteDomainBatch request structure.

    """

    def __init__(self):
        r"""
        :param _DomainList: The domain array.
        :type DomainList: list of str
        """
        self._DomainList = None

    @property
    def DomainList(self):
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList


    def _deserialize(self, params):
        self._DomainList = params.get("DomainList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainBatchResponse(AbstractModel):
    """DeleteDomainBatch response structure.

    """

    def __init__(self):
        r"""
        :param _JobId: The task ID.
        :type JobId: int
        :param _DetailList: The array of task details.
        :type DetailList: list of DeleteDomainBatchDetail
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._JobId = None
        self._DetailList = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def DetailList(self):
        return self._DetailList

    @DetailList.setter
    def DetailList(self, DetailList):
        self._DetailList = DetailList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        if params.get("DetailList") is not None:
            self._DetailList = []
            for item in params.get("DetailList"):
                obj = DeleteDomainBatchDetail()
                obj._deserialize(item)
                self._DetailList.append(obj)
        self._RequestId = params.get("RequestId")


class DeleteDomainRequest(AbstractModel):
    """DeleteDomain request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain
        :type Domain: str
        :param _DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self._Domain = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainResponse(AbstractModel):
    """DeleteDomain response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteRecordGroupRequest(AbstractModel):
    """DeleteRecordGroup request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain
        :type Domain: str
        :param _GroupId: Group ID
        :type GroupId: int
        :param _DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored.
        :type DomainId: int
        """
        self._Domain = None
        self._GroupId = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._GroupId = params.get("GroupId")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordGroupResponse(AbstractModel):
    """DeleteRecordGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteRecordRequest(AbstractModel):
    """DeleteRecord request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain
        :type Domain: str
        :param _RecordId: The record ID. You can view all DNS records and their IDs via the `DescribeRecordList` API.
        :type RecordId: int
        :param _DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self._Domain = None
        self._RecordId = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._RecordId = params.get("RecordId")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordResponse(AbstractModel):
    """DeleteRecord response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteShareDomainRequest(AbstractModel):
    """DeleteShareDomain request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain
        :type Domain: str
        :param _Account: Account of the domain to be shared
        :type Account: str
        :param _DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self._Domain = None
        self._Account = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Account(self):
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Account = params.get("Account")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteShareDomainResponse(AbstractModel):
    """DeleteShareDomain response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeDomainAliasListRequest(AbstractModel):
    """DescribeDomainAliasList request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain
        :type Domain: str
        :param _DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self._Domain = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainAliasListResponse(AbstractModel):
    """DescribeDomainAliasList response structure.

    """

    def __init__(self):
        r"""
        :param _DomainAliasList: List of domain aliases
        :type DomainAliasList: list of DomainAliasInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DomainAliasList = None
        self._RequestId = None

    @property
    def DomainAliasList(self):
        return self._DomainAliasList

    @DomainAliasList.setter
    def DomainAliasList(self, DomainAliasList):
        self._DomainAliasList = DomainAliasList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DomainAliasList") is not None:
            self._DomainAliasList = []
            for item in params.get("DomainAliasList"):
                obj = DomainAliasInfo()
                obj._deserialize(item)
                self._DomainAliasList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainGroupListRequest(AbstractModel):
    """DescribeDomainGroupList request structure.

    """


class DescribeDomainGroupListResponse(AbstractModel):
    """DescribeDomainGroupList response structure.

    """

    def __init__(self):
        r"""
        :param _GroupList: Group list
        :type GroupList: list of GroupInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GroupList = None
        self._RequestId = None

    @property
    def GroupList(self):
        return self._GroupList

    @GroupList.setter
    def GroupList(self, GroupList):
        self._GroupList = GroupList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GroupList") is not None:
            self._GroupList = []
            for item in params.get("GroupList"):
                obj = GroupInfo()
                obj._deserialize(item)
                self._GroupList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainListRequest(AbstractModel):
    """DescribeDomainList request structure.

    """

    def __init__(self):
        r"""
        :param _Type: The domain group type. Valid values: `ALL` (default), `MINE`, `SHARE`, `ISMARK`, `PAUSE`, `VIP`, `RECENT`, `SHARE_OUT`, and `FREE`.
        :type Type: str
        :param _Offset: Record offset starting from `0`. Default value: `0`.
        :type Offset: int
        :param _Limit: Number of domains to be obtained. For example, `20` indicates to obtain 20 domains. Default value: `3000`.
        :type Limit: int
        :param _GroupId: Group ID, which can be passed in to get all domains in the specified group
        :type GroupId: int
        :param _Keyword: Keyword for searching for a domain
        :type Keyword: str
        """
        self._Type = None
        self._Offset = None
        self._Limit = None
        self._GroupId = None
        self._Keyword = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._GroupId = params.get("GroupId")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainListResponse(AbstractModel):
    """DescribeDomainList response structure.

    """

    def __init__(self):
        r"""
        :param _DomainCountInfo: Statistics on the list page
        :type DomainCountInfo: :class:`tencentcloud.dnspod.v20210323.models.DomainCountInfo`
        :param _DomainList: Domain list
        :type DomainList: list of DomainListItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DomainCountInfo = None
        self._DomainList = None
        self._RequestId = None

    @property
    def DomainCountInfo(self):
        return self._DomainCountInfo

    @DomainCountInfo.setter
    def DomainCountInfo(self, DomainCountInfo):
        self._DomainCountInfo = DomainCountInfo

    @property
    def DomainList(self):
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DomainCountInfo") is not None:
            self._DomainCountInfo = DomainCountInfo()
            self._DomainCountInfo._deserialize(params.get("DomainCountInfo"))
        if params.get("DomainList") is not None:
            self._DomainList = []
            for item in params.get("DomainList"):
                obj = DomainListItem()
                obj._deserialize(item)
                self._DomainList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainLogListRequest(AbstractModel):
    """DescribeDomainLogList request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain
        :type Domain: str
        :param _DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        :param _Offset: Record offset starting from `0`. Default value: `0`.
        :type Offset: int
        :param _Limit: Total number of logs to be obtained. For example, `20` indicates to obtain 20 logs. Default value: `500`. Maximum value: `500`.
        :type Limit: int
        """
        self._Domain = None
        self._DomainId = None
        self._Offset = None
        self._Limit = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainLogListResponse(AbstractModel):
    """DescribeDomainLogList response structure.

    """

    def __init__(self):
        r"""
        :param _LogList: Domain information
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogList: list of str
        :param _PageSize: Number of results per page
        :type PageSize: int
        :param _TotalCount: Total number of logs
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LogList = None
        self._PageSize = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def LogList(self):
        return self._LogList

    @LogList.setter
    def LogList(self, LogList):
        self._LogList = LogList

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LogList = params.get("LogList")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDomainPurviewRequest(AbstractModel):
    """DescribeDomainPurview request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain
        :type Domain: str
        :param _DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self._Domain = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainPurviewResponse(AbstractModel):
    """DescribeDomainPurview response structure.

    """

    def __init__(self):
        r"""
        :param _PurviewList: Permission list of the domain
        :type PurviewList: list of PurviewInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PurviewList = None
        self._RequestId = None

    @property
    def PurviewList(self):
        return self._PurviewList

    @PurviewList.setter
    def PurviewList(self, PurviewList):
        self._PurviewList = PurviewList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PurviewList") is not None:
            self._PurviewList = []
            for item in params.get("PurviewList"):
                obj = PurviewInfo()
                obj._deserialize(item)
                self._PurviewList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainRequest(AbstractModel):
    """DescribeDomain request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain
        :type Domain: str
        :param _DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self._Domain = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainResponse(AbstractModel):
    """DescribeDomain response structure.

    """

    def __init__(self):
        r"""
        :param _DomainInfo: Domain information
        :type DomainInfo: :class:`tencentcloud.dnspod.v20210323.models.DomainInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DomainInfo = None
        self._RequestId = None

    @property
    def DomainInfo(self):
        return self._DomainInfo

    @DomainInfo.setter
    def DomainInfo(self, DomainInfo):
        self._DomainInfo = DomainInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DomainInfo") is not None:
            self._DomainInfo = DomainInfo()
            self._DomainInfo._deserialize(params.get("DomainInfo"))
        self._RequestId = params.get("RequestId")


class DescribeDomainShareInfoRequest(AbstractModel):
    """DescribeDomainShareInfo request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain
        :type Domain: str
        :param _DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self._Domain = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainShareInfoResponse(AbstractModel):
    """DescribeDomainShareInfo response structure.

    """

    def __init__(self):
        r"""
        :param _ShareList: Domain sharing information
        :type ShareList: list of DomainShareInfo
        :param _Owner: Owner account of the domain
        :type Owner: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ShareList = None
        self._Owner = None
        self._RequestId = None

    @property
    def ShareList(self):
        return self._ShareList

    @ShareList.setter
    def ShareList(self, ShareList):
        self._ShareList = ShareList

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ShareList") is not None:
            self._ShareList = []
            for item in params.get("ShareList"):
                obj = DomainShareInfo()
                obj._deserialize(item)
                self._ShareList.append(obj)
        self._Owner = params.get("Owner")
        self._RequestId = params.get("RequestId")


class DescribeRecordGroupListRequest(AbstractModel):
    """DescribeRecordGroupList request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain
        :type Domain: str
        :param _DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored.
        :type DomainId: int
        :param _Offset: Pagination offset
        :type Offset: int
        :param _Limit: Number of items per page for pagination
        :type Limit: int
        """
        self._Domain = None
        self._DomainId = None
        self._Offset = None
        self._Limit = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordGroupListResponse(AbstractModel):
    """DescribeRecordGroupList response structure.

    """

    def __init__(self):
        r"""
        :param _GroupList: Group list
        :type GroupList: list of RecordGroupInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GroupList = None
        self._RequestId = None

    @property
    def GroupList(self):
        return self._GroupList

    @GroupList.setter
    def GroupList(self, GroupList):
        self._GroupList = GroupList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GroupList") is not None:
            self._GroupList = []
            for item in params.get("GroupList"):
                obj = RecordGroupInfo()
                obj._deserialize(item)
                self._GroupList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRecordLineListRequest(AbstractModel):
    """DescribeRecordLineList request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain.
        :type Domain: str
        :param _DomainGrade: Domain level.
+ Original plan. Valid values: `D_FREE` (Free Plan); `D_PLUS` (Individual Plus Plan); `D_EXTRA` (Enterprise 1 Plan); `D_EXPERT` (Enterprise 2 Plan); `D_ULTRA` (Enterprise 3 Plan).
+ New plan. Valid values: `DP_FREE` (Free Version); `DP_PLUS` (Professional); `DP_EXTRA` (Enterprise Basic); `DP_EXPERT` (Enterprise); `DP_ULTRA` (Ultimate).
        :type DomainGrade: str
        :param _DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self._Domain = None
        self._DomainGrade = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainGrade(self):
        return self._DomainGrade

    @DomainGrade.setter
    def DomainGrade(self, DomainGrade):
        self._DomainGrade = DomainGrade

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainGrade = params.get("DomainGrade")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordLineListResponse(AbstractModel):
    """DescribeRecordLineList response structure.

    """

    def __init__(self):
        r"""
        :param _LineList: List of split zones.
        :type LineList: list of LineInfo
        :param _LineGroupList: List of split zone groups.
        :type LineGroupList: list of LineGroupInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LineList = None
        self._LineGroupList = None
        self._RequestId = None

    @property
    def LineList(self):
        return self._LineList

    @LineList.setter
    def LineList(self, LineList):
        self._LineList = LineList

    @property
    def LineGroupList(self):
        return self._LineGroupList

    @LineGroupList.setter
    def LineGroupList(self, LineGroupList):
        self._LineGroupList = LineGroupList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LineList") is not None:
            self._LineList = []
            for item in params.get("LineList"):
                obj = LineInfo()
                obj._deserialize(item)
                self._LineList.append(obj)
        if params.get("LineGroupList") is not None:
            self._LineGroupList = []
            for item in params.get("LineGroupList"):
                obj = LineGroupInfo()
                obj._deserialize(item)
                self._LineGroupList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRecordListRequest(AbstractModel):
    """DescribeRecordList request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: The domain for which DNS records are to be obtained.
        :type Domain: str
        :param _DomainId: The ID of the domain whose DNS records are requested. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        :param _Subdomain: The host header of a DNS record. If this parameter is passed in, only the DNS record corresponding to this host header will be returned.
        :type Subdomain: str
        :param _RecordType: The type of DNS record, such as A, CNAME, NS, AAAA, explicit URL, implicit URL, CAA, or SPF record.
        :type RecordType: str
        :param _RecordLine: The name of the split zone for which DNS records are requested. You can view split zones allowed by this domain via the `DescribeRecordLineList` API.
        :type RecordLine: str
        :param _RecordLineId: The ID of the split zone for which DNS records are requested. If `RecordLineId` is passed in, `RecordLine` is ignored. You can view split zones allowed by this domain via the `DescribeRecordLineList` API.
        :type RecordLineId: str
        :param _GroupId: The group ID passed in to get DNS records in the group.
        :type GroupId: int
        :param _Keyword: The keyword for searching for DNS records. Host headers and record values are supported.
        :type Keyword: str
        :param _SortField: The sorting field. Available values: `name`, `line`, `type`, `value`, `weight`, `mx`, and `ttl,updated_on`.
        :type SortField: str
        :param _SortType: The sorting type. Valid values: `ASC` (ascending, default), `DESC` (descending).
        :type SortType: str
        :param _Offset: The offset. Default value: `0`.
        :type Offset: int
        :param _Limit: The limit. It defaults to 100 and can be up to 3,000.
        :type Limit: int
        """
        self._Domain = None
        self._DomainId = None
        self._Subdomain = None
        self._RecordType = None
        self._RecordLine = None
        self._RecordLineId = None
        self._GroupId = None
        self._Keyword = None
        self._SortField = None
        self._SortType = None
        self._Offset = None
        self._Limit = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def Subdomain(self):
        return self._Subdomain

    @Subdomain.setter
    def Subdomain(self, Subdomain):
        self._Subdomain = Subdomain

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RecordLine(self):
        return self._RecordLine

    @RecordLine.setter
    def RecordLine(self, RecordLine):
        self._RecordLine = RecordLine

    @property
    def RecordLineId(self):
        return self._RecordLineId

    @RecordLineId.setter
    def RecordLineId(self, RecordLineId):
        self._RecordLineId = RecordLineId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def SortField(self):
        return self._SortField

    @SortField.setter
    def SortField(self, SortField):
        self._SortField = SortField

    @property
    def SortType(self):
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        self._Subdomain = params.get("Subdomain")
        self._RecordType = params.get("RecordType")
        self._RecordLine = params.get("RecordLine")
        self._RecordLineId = params.get("RecordLineId")
        self._GroupId = params.get("GroupId")
        self._Keyword = params.get("Keyword")
        self._SortField = params.get("SortField")
        self._SortType = params.get("SortType")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordListResponse(AbstractModel):
    """DescribeRecordList response structure.

    """

    def __init__(self):
        r"""
        :param _RecordCountInfo: The record count info.
        :type RecordCountInfo: :class:`tencentcloud.dnspod.v20210323.models.RecordCountInfo`
        :param _RecordList: The record list result.
        :type RecordList: list of RecordListItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RecordCountInfo = None
        self._RecordList = None
        self._RequestId = None

    @property
    def RecordCountInfo(self):
        return self._RecordCountInfo

    @RecordCountInfo.setter
    def RecordCountInfo(self, RecordCountInfo):
        self._RecordCountInfo = RecordCountInfo

    @property
    def RecordList(self):
        return self._RecordList

    @RecordList.setter
    def RecordList(self, RecordList):
        self._RecordList = RecordList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RecordCountInfo") is not None:
            self._RecordCountInfo = RecordCountInfo()
            self._RecordCountInfo._deserialize(params.get("RecordCountInfo"))
        if params.get("RecordList") is not None:
            self._RecordList = []
            for item in params.get("RecordList"):
                obj = RecordListItem()
                obj._deserialize(item)
                self._RecordList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRecordRequest(AbstractModel):
    """DescribeRecord request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain
        :type Domain: str
        :param _RecordId: The record ID. You can view all DNS records and their IDs via the `DescribeRecordList` API.
        :type RecordId: int
        :param _DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self._Domain = None
        self._RecordId = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._RecordId = params.get("RecordId")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordResponse(AbstractModel):
    """DescribeRecord response structure.

    """

    def __init__(self):
        r"""
        :param _RecordInfo: Record information
        :type RecordInfo: :class:`tencentcloud.dnspod.v20210323.models.RecordInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RecordInfo = None
        self._RequestId = None

    @property
    def RecordInfo(self):
        return self._RecordInfo

    @RecordInfo.setter
    def RecordInfo(self, RecordInfo):
        self._RecordInfo = RecordInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RecordInfo") is not None:
            self._RecordInfo = RecordInfo()
            self._RecordInfo._deserialize(params.get("RecordInfo"))
        self._RequestId = params.get("RequestId")


class DescribeRecordTypeRequest(AbstractModel):
    """DescribeRecordType request structure.

    """

    def __init__(self):
        r"""
        :param _DomainGrade: Domain level.
+ Original plan. Valid values: `D_FREE` (Free Plan); `D_PLUS` (Individual Plus Plan); `D_EXTRA` (Enterprise 1 Plan); `D_EXPERT` (Enterprise 2 Plan); `D_ULTRA` (Enterprise 3 Plan).
+ New plan. Valid values: `DP_FREE` (Free Version); `DP_PLUS` (Professional); `DP_EXTRA` (Enterprise Basic); `DP_EXPERT` (Enterprise); `DP_ULTRA` (Ultimate).
        :type DomainGrade: str
        """
        self._DomainGrade = None

    @property
    def DomainGrade(self):
        return self._DomainGrade

    @DomainGrade.setter
    def DomainGrade(self, DomainGrade):
        self._DomainGrade = DomainGrade


    def _deserialize(self, params):
        self._DomainGrade = params.get("DomainGrade")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordTypeResponse(AbstractModel):
    """DescribeRecordType response structure.

    """

    def __init__(self):
        r"""
        :param _TypeList: List of record types
        :type TypeList: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TypeList = None
        self._RequestId = None

    @property
    def TypeList(self):
        return self._TypeList

    @TypeList.setter
    def TypeList(self, TypeList):
        self._TypeList = TypeList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TypeList = params.get("TypeList")
        self._RequestId = params.get("RequestId")


class DescribeSubdomainAnalyticsRequest(AbstractModel):
    """DescribeSubdomainAnalytics request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: The domain of the DNS query volume to be queried
        :type Domain: str
        :param _StartDate: Query start date in the format of `YYYY-MM-DD`
        :type StartDate: str
        :param _EndDate: Query end date in the format of `YYYY-MM-DD`
        :type EndDate: str
        :param _Subdomain: The subdomain of the DNS query volume to be queried
        :type Subdomain: str
        :param _DnsFormat: `DATE`: Daily. `HOUR`: Hourly
        :type DnsFormat: str
        :param _DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self._Domain = None
        self._StartDate = None
        self._EndDate = None
        self._Subdomain = None
        self._DnsFormat = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def StartDate(self):
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Subdomain(self):
        return self._Subdomain

    @Subdomain.setter
    def Subdomain(self, Subdomain):
        self._Subdomain = Subdomain

    @property
    def DnsFormat(self):
        return self._DnsFormat

    @DnsFormat.setter
    def DnsFormat(self, DnsFormat):
        self._DnsFormat = DnsFormat

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Subdomain = params.get("Subdomain")
        self._DnsFormat = params.get("DnsFormat")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubdomainAnalyticsResponse(AbstractModel):
    """DescribeSubdomainAnalytics response structure.

    """

    def __init__(self):
        r"""
        :param _Data: DNS query volume in the current statistical dimension
        :type Data: list of DomainAnalyticsDetail
        :param _Info: Statistics on the DNS query volume of a subdomain
        :type Info: :class:`tencentcloud.dnspod.v20210323.models.SubdomainAnalyticsInfo`
        :param _AliasData: DNS query volume of the subdomain alias
        :type AliasData: list of SubdomainAliasAnalyticsItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Info = None
        self._AliasData = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def AliasData(self):
        return self._AliasData

    @AliasData.setter
    def AliasData(self, AliasData):
        self._AliasData = AliasData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DomainAnalyticsDetail()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("Info") is not None:
            self._Info = SubdomainAnalyticsInfo()
            self._Info._deserialize(params.get("Info"))
        if params.get("AliasData") is not None:
            self._AliasData = []
            for item in params.get("AliasData"):
                obj = SubdomainAliasAnalyticsItem()
                obj._deserialize(item)
                self._AliasData.append(obj)
        self._RequestId = params.get("RequestId")


class DomainAliasInfo(AbstractModel):
    """Information of a domain alias

    """

    def __init__(self):
        r"""
        :param _Id: Domain alias ID
        :type Id: int
        :param _DomainAlias: Domain alias
        :type DomainAlias: str
        """
        self._Id = None
        self._DomainAlias = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DomainAlias(self):
        return self._DomainAlias

    @DomainAlias.setter
    def DomainAlias(self, DomainAlias):
        self._DomainAlias = DomainAlias


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._DomainAlias = params.get("DomainAlias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainAnalyticsDetail(AbstractModel):
    """DNS query volume in the current statistical dimension

    """

    def __init__(self):
        r"""
        :param _Num: DNS query volume in the current statistical dimension
        :type Num: int
        :param _DateKey: Collection date for daily collection
        :type DateKey: str
        :param _HourKey: The last hour (0–23) for hourly collection. For example, if `HourKey` is `23`, the DNS query volume in the statistical period of 22:00–23:00 will be collected.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HourKey: int
        """
        self._Num = None
        self._DateKey = None
        self._HourKey = None

    @property
    def Num(self):
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

    @property
    def DateKey(self):
        return self._DateKey

    @DateKey.setter
    def DateKey(self, DateKey):
        self._DateKey = DateKey

    @property
    def HourKey(self):
        return self._HourKey

    @HourKey.setter
    def HourKey(self, HourKey):
        self._HourKey = HourKey


    def _deserialize(self, params):
        self._Num = params.get("Num")
        self._DateKey = params.get("DateKey")
        self._HourKey = params.get("HourKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainCountInfo(AbstractModel):
    """List statistics by page

    """

    def __init__(self):
        r"""
        :param _DomainTotal: Number of eligible domains
        :type DomainTotal: int
        :param _AllTotal: Number of all domains that can be viewed by the user
        :type AllTotal: int
        :param _MineTotal: Number of domains added under the user account
        :type MineTotal: int
        :param _ShareTotal: Number of domains shared with the user
        :type ShareTotal: int
        :param _VipTotal: Number of paid domains
        :type VipTotal: int
        :param _PauseTotal: Number of suspended domains
        :type PauseTotal: int
        :param _ErrorTotal: Number of domains with a DNS configuration error
        :type ErrorTotal: int
        :param _LockTotal: Number of locked domains
        :type LockTotal: int
        :param _SpamTotal: Number of blocked domains
        :type SpamTotal: int
        :param _VipExpire: Number of domains that will expire within 30 days
        :type VipExpire: int
        :param _ShareOutTotal: Number of domains shared with others
        :type ShareOutTotal: int
        :param _GroupTotal: Number of domains in the specified group
        :type GroupTotal: int
        """
        self._DomainTotal = None
        self._AllTotal = None
        self._MineTotal = None
        self._ShareTotal = None
        self._VipTotal = None
        self._PauseTotal = None
        self._ErrorTotal = None
        self._LockTotal = None
        self._SpamTotal = None
        self._VipExpire = None
        self._ShareOutTotal = None
        self._GroupTotal = None

    @property
    def DomainTotal(self):
        return self._DomainTotal

    @DomainTotal.setter
    def DomainTotal(self, DomainTotal):
        self._DomainTotal = DomainTotal

    @property
    def AllTotal(self):
        return self._AllTotal

    @AllTotal.setter
    def AllTotal(self, AllTotal):
        self._AllTotal = AllTotal

    @property
    def MineTotal(self):
        return self._MineTotal

    @MineTotal.setter
    def MineTotal(self, MineTotal):
        self._MineTotal = MineTotal

    @property
    def ShareTotal(self):
        return self._ShareTotal

    @ShareTotal.setter
    def ShareTotal(self, ShareTotal):
        self._ShareTotal = ShareTotal

    @property
    def VipTotal(self):
        return self._VipTotal

    @VipTotal.setter
    def VipTotal(self, VipTotal):
        self._VipTotal = VipTotal

    @property
    def PauseTotal(self):
        return self._PauseTotal

    @PauseTotal.setter
    def PauseTotal(self, PauseTotal):
        self._PauseTotal = PauseTotal

    @property
    def ErrorTotal(self):
        return self._ErrorTotal

    @ErrorTotal.setter
    def ErrorTotal(self, ErrorTotal):
        self._ErrorTotal = ErrorTotal

    @property
    def LockTotal(self):
        return self._LockTotal

    @LockTotal.setter
    def LockTotal(self, LockTotal):
        self._LockTotal = LockTotal

    @property
    def SpamTotal(self):
        return self._SpamTotal

    @SpamTotal.setter
    def SpamTotal(self, SpamTotal):
        self._SpamTotal = SpamTotal

    @property
    def VipExpire(self):
        return self._VipExpire

    @VipExpire.setter
    def VipExpire(self, VipExpire):
        self._VipExpire = VipExpire

    @property
    def ShareOutTotal(self):
        return self._ShareOutTotal

    @ShareOutTotal.setter
    def ShareOutTotal(self, ShareOutTotal):
        self._ShareOutTotal = ShareOutTotal

    @property
    def GroupTotal(self):
        return self._GroupTotal

    @GroupTotal.setter
    def GroupTotal(self, GroupTotal):
        self._GroupTotal = GroupTotal


    def _deserialize(self, params):
        self._DomainTotal = params.get("DomainTotal")
        self._AllTotal = params.get("AllTotal")
        self._MineTotal = params.get("MineTotal")
        self._ShareTotal = params.get("ShareTotal")
        self._VipTotal = params.get("VipTotal")
        self._PauseTotal = params.get("PauseTotal")
        self._ErrorTotal = params.get("ErrorTotal")
        self._LockTotal = params.get("LockTotal")
        self._SpamTotal = params.get("SpamTotal")
        self._VipExpire = params.get("VipExpire")
        self._ShareOutTotal = params.get("ShareOutTotal")
        self._GroupTotal = params.get("GroupTotal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainCreateInfo(AbstractModel):
    """Domain information returned during domain creation

    """

    def __init__(self):
        r"""
        :param _Id: Domain ID
        :type Id: int
        :param _Domain: Domain
        :type Domain: str
        :param _Punycode: Domain Punycode
        :type Punycode: str
        :param _GradeNsList: NS list of the domain
        :type GradeNsList: list of str
        """
        self._Id = None
        self._Domain = None
        self._Punycode = None
        self._GradeNsList = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Punycode(self):
        return self._Punycode

    @Punycode.setter
    def Punycode(self, Punycode):
        self._Punycode = Punycode

    @property
    def GradeNsList(self):
        return self._GradeNsList

    @GradeNsList.setter
    def GradeNsList(self, GradeNsList):
        self._GradeNsList = GradeNsList


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Domain = params.get("Domain")
        self._Punycode = params.get("Punycode")
        self._GradeNsList = params.get("GradeNsList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainInfo(AbstractModel):
    """Domain details

    """

    def __init__(self):
        r"""
        :param _DomainId: Domain ID
        :type DomainId: int
        :param _Status: Domain status
        :type Status: str
        :param _Grade: DNS plan level
        :type Grade: str
        :param _GroupId: Domain group ID
        :type GroupId: int
        :param _IsMark: Whether the domain is starred
        :type IsMark: str
        :param _TTL: TTL (DNS record cache time)
        :type TTL: int
        :param _CnameSpeedup: Whether CNAME flattening is enabled
        :type CnameSpeedup: str
        :param _Remark: Domain remarks
Note: This field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param _Punycode: Domain Punycode
        :type Punycode: str
        :param _DnsStatus: DNS status of the domain
        :type DnsStatus: str
        :param _DnspodNsList: NS list of the domain
        :type DnspodNsList: list of str
        :param _Domain: Domain
        :type Domain: str
        :param _GradeLevel: Domain level ID
        :type GradeLevel: int
        :param _UserId: Domain user ID
        :type UserId: int
        :param _IsVip: Whether the domain is a VIP domain
        :type IsVip: str
        :param _Owner: Domain owner account
        :type Owner: str
        :param _GradeTitle: Domain level description
        :type GradeTitle: str
        :param _CreatedOn: Domain creation time
        :type CreatedOn: str
        :param _UpdatedOn: Last update time
        :type UpdatedOn: str
        :param _Uin: Tencent Cloud account `Uin`
        :type Uin: str
        :param _ActualNsList: NS list actually used by the domain
Note: This field may return null, indicating that no valid values can be obtained.
        :type ActualNsList: list of str
        :param _RecordCount: Number of domain records
        :type RecordCount: int
        :param _OwnerNick: Alias of the domain account owner
Note: This field may return null, indicating that no valid values can be obtained.
        :type OwnerNick: str
        """
        self._DomainId = None
        self._Status = None
        self._Grade = None
        self._GroupId = None
        self._IsMark = None
        self._TTL = None
        self._CnameSpeedup = None
        self._Remark = None
        self._Punycode = None
        self._DnsStatus = None
        self._DnspodNsList = None
        self._Domain = None
        self._GradeLevel = None
        self._UserId = None
        self._IsVip = None
        self._Owner = None
        self._GradeTitle = None
        self._CreatedOn = None
        self._UpdatedOn = None
        self._Uin = None
        self._ActualNsList = None
        self._RecordCount = None
        self._OwnerNick = None

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Grade(self):
        return self._Grade

    @Grade.setter
    def Grade(self, Grade):
        self._Grade = Grade

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def IsMark(self):
        return self._IsMark

    @IsMark.setter
    def IsMark(self, IsMark):
        self._IsMark = IsMark

    @property
    def TTL(self):
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def CnameSpeedup(self):
        return self._CnameSpeedup

    @CnameSpeedup.setter
    def CnameSpeedup(self, CnameSpeedup):
        self._CnameSpeedup = CnameSpeedup

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Punycode(self):
        return self._Punycode

    @Punycode.setter
    def Punycode(self, Punycode):
        self._Punycode = Punycode

    @property
    def DnsStatus(self):
        return self._DnsStatus

    @DnsStatus.setter
    def DnsStatus(self, DnsStatus):
        self._DnsStatus = DnsStatus

    @property
    def DnspodNsList(self):
        return self._DnspodNsList

    @DnspodNsList.setter
    def DnspodNsList(self, DnspodNsList):
        self._DnspodNsList = DnspodNsList

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def GradeLevel(self):
        return self._GradeLevel

    @GradeLevel.setter
    def GradeLevel(self, GradeLevel):
        self._GradeLevel = GradeLevel

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def IsVip(self):
        return self._IsVip

    @IsVip.setter
    def IsVip(self, IsVip):
        self._IsVip = IsVip

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def GradeTitle(self):
        return self._GradeTitle

    @GradeTitle.setter
    def GradeTitle(self, GradeTitle):
        self._GradeTitle = GradeTitle

    @property
    def CreatedOn(self):
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def UpdatedOn(self):
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ActualNsList(self):
        return self._ActualNsList

    @ActualNsList.setter
    def ActualNsList(self, ActualNsList):
        self._ActualNsList = ActualNsList

    @property
    def RecordCount(self):
        return self._RecordCount

    @RecordCount.setter
    def RecordCount(self, RecordCount):
        self._RecordCount = RecordCount

    @property
    def OwnerNick(self):
        return self._OwnerNick

    @OwnerNick.setter
    def OwnerNick(self, OwnerNick):
        self._OwnerNick = OwnerNick


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        self._Status = params.get("Status")
        self._Grade = params.get("Grade")
        self._GroupId = params.get("GroupId")
        self._IsMark = params.get("IsMark")
        self._TTL = params.get("TTL")
        self._CnameSpeedup = params.get("CnameSpeedup")
        self._Remark = params.get("Remark")
        self._Punycode = params.get("Punycode")
        self._DnsStatus = params.get("DnsStatus")
        self._DnspodNsList = params.get("DnspodNsList")
        self._Domain = params.get("Domain")
        self._GradeLevel = params.get("GradeLevel")
        self._UserId = params.get("UserId")
        self._IsVip = params.get("IsVip")
        self._Owner = params.get("Owner")
        self._GradeTitle = params.get("GradeTitle")
        self._CreatedOn = params.get("CreatedOn")
        self._UpdatedOn = params.get("UpdatedOn")
        self._Uin = params.get("Uin")
        self._ActualNsList = params.get("ActualNsList")
        self._RecordCount = params.get("RecordCount")
        self._OwnerNick = params.get("OwnerNick")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainListItem(AbstractModel):
    """Element in the domain list

    """

    def __init__(self):
        r"""
        :param _DomainId: Unique ID assigned to the domain by the system
        :type DomainId: int
        :param _Name: Original format of the domain
        :type Name: str
        :param _Status: Domain status. Valid values: `ENABLE` (normal), `PAUSE` (suspended), `SPAM` (blocked).
        :type Status: str
        :param _TTL: Default TTL of the default DNS record of the domain
        :type TTL: int
        :param _CNAMESpeedup: Whether CNAME flattening is enabled. Valid values: `ENABLE` (enabled); `DISABLE` (disabled).
        :type CNAMESpeedup: str
        :param _DNSStatus: DNS configuration status. Valid values: `DNSERROR` (error), an empty string (normal).
        :type DNSStatus: str
        :param _Grade: Plan level code of the domain
        :type Grade: str
        :param _GroupId: Group ID of the domain
        :type GroupId: int
        :param _SearchEnginePush: Whether search engine push optimization is enabled. Valid values: `YES` (yes), `NO` (no).
        :type SearchEnginePush: str
        :param _Remark: Domain remarks
        :type Remark: str
        :param _Punycode: Punycode-encoded domain format
        :type Punycode: str
        :param _EffectiveDNS: Effective DNS assigned to the domain by the system
        :type EffectiveDNS: list of str
        :param _GradeLevel: Number corresponding to the plan level of the domain
        :type GradeLevel: int
        :param _GradeTitle: Plan name
        :type GradeTitle: str
        :param _IsVip: Whether it is a paid plan
        :type IsVip: str
        :param _VipStartAt: Activation time of the paid plan
        :type VipStartAt: str
        :param _VipEndAt: Expiry time of the paid plan
        :type VipEndAt: str
        :param _VipAutoRenew: Whether VIP automatic renewal is enabled for the domain. Valid values: `YES` (yes); `NO` (no). Default value: `DEFAULT`.
        :type VipAutoRenew: str
        :param _RecordCount: Number of records under the domain
        :type RecordCount: int
        :param _CreatedOn: Domain adding time
        :type CreatedOn: str
        :param _UpdatedOn: Domain update time
        :type UpdatedOn: str
        :param _Owner: Account of the domain
        :type Owner: str
        """
        self._DomainId = None
        self._Name = None
        self._Status = None
        self._TTL = None
        self._CNAMESpeedup = None
        self._DNSStatus = None
        self._Grade = None
        self._GroupId = None
        self._SearchEnginePush = None
        self._Remark = None
        self._Punycode = None
        self._EffectiveDNS = None
        self._GradeLevel = None
        self._GradeTitle = None
        self._IsVip = None
        self._VipStartAt = None
        self._VipEndAt = None
        self._VipAutoRenew = None
        self._RecordCount = None
        self._CreatedOn = None
        self._UpdatedOn = None
        self._Owner = None

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TTL(self):
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def CNAMESpeedup(self):
        return self._CNAMESpeedup

    @CNAMESpeedup.setter
    def CNAMESpeedup(self, CNAMESpeedup):
        self._CNAMESpeedup = CNAMESpeedup

    @property
    def DNSStatus(self):
        return self._DNSStatus

    @DNSStatus.setter
    def DNSStatus(self, DNSStatus):
        self._DNSStatus = DNSStatus

    @property
    def Grade(self):
        return self._Grade

    @Grade.setter
    def Grade(self, Grade):
        self._Grade = Grade

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def SearchEnginePush(self):
        return self._SearchEnginePush

    @SearchEnginePush.setter
    def SearchEnginePush(self, SearchEnginePush):
        self._SearchEnginePush = SearchEnginePush

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Punycode(self):
        return self._Punycode

    @Punycode.setter
    def Punycode(self, Punycode):
        self._Punycode = Punycode

    @property
    def EffectiveDNS(self):
        return self._EffectiveDNS

    @EffectiveDNS.setter
    def EffectiveDNS(self, EffectiveDNS):
        self._EffectiveDNS = EffectiveDNS

    @property
    def GradeLevel(self):
        return self._GradeLevel

    @GradeLevel.setter
    def GradeLevel(self, GradeLevel):
        self._GradeLevel = GradeLevel

    @property
    def GradeTitle(self):
        return self._GradeTitle

    @GradeTitle.setter
    def GradeTitle(self, GradeTitle):
        self._GradeTitle = GradeTitle

    @property
    def IsVip(self):
        return self._IsVip

    @IsVip.setter
    def IsVip(self, IsVip):
        self._IsVip = IsVip

    @property
    def VipStartAt(self):
        return self._VipStartAt

    @VipStartAt.setter
    def VipStartAt(self, VipStartAt):
        self._VipStartAt = VipStartAt

    @property
    def VipEndAt(self):
        return self._VipEndAt

    @VipEndAt.setter
    def VipEndAt(self, VipEndAt):
        self._VipEndAt = VipEndAt

    @property
    def VipAutoRenew(self):
        return self._VipAutoRenew

    @VipAutoRenew.setter
    def VipAutoRenew(self, VipAutoRenew):
        self._VipAutoRenew = VipAutoRenew

    @property
    def RecordCount(self):
        return self._RecordCount

    @RecordCount.setter
    def RecordCount(self, RecordCount):
        self._RecordCount = RecordCount

    @property
    def CreatedOn(self):
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def UpdatedOn(self):
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._TTL = params.get("TTL")
        self._CNAMESpeedup = params.get("CNAMESpeedup")
        self._DNSStatus = params.get("DNSStatus")
        self._Grade = params.get("Grade")
        self._GroupId = params.get("GroupId")
        self._SearchEnginePush = params.get("SearchEnginePush")
        self._Remark = params.get("Remark")
        self._Punycode = params.get("Punycode")
        self._EffectiveDNS = params.get("EffectiveDNS")
        self._GradeLevel = params.get("GradeLevel")
        self._GradeTitle = params.get("GradeTitle")
        self._IsVip = params.get("IsVip")
        self._VipStartAt = params.get("VipStartAt")
        self._VipEndAt = params.get("VipEndAt")
        self._VipAutoRenew = params.get("VipAutoRenew")
        self._RecordCount = params.get("RecordCount")
        self._CreatedOn = params.get("CreatedOn")
        self._UpdatedOn = params.get("UpdatedOn")
        self._Owner = params.get("Owner")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainShareInfo(AbstractModel):
    """Domain sharing information

    """

    def __init__(self):
        r"""
        :param _ShareTo: Account with which the domain is shared
        :type ShareTo: str
        :param _Mode: Sharing mode. Valid values: `rw` (read/write), `r` (read-only).
        :type Mode: str
        :param _Status: Sharing status. Valid values: `enabled` (shared successfully); `pending` (the account shared to does not exist and is pending registration).
        :type Status: str
        """
        self._ShareTo = None
        self._Mode = None
        self._Status = None

    @property
    def ShareTo(self):
        return self._ShareTo

    @ShareTo.setter
    def ShareTo(self, ShareTo):
        self._ShareTo = ShareTo

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ShareTo = params.get("ShareTo")
        self._Mode = params.get("Mode")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfo(AbstractModel):
    """List of domain groups

    """

    def __init__(self):
        r"""
        :param _GroupId: Group ID
        :type GroupId: int
        :param _GroupName: Group name
        :type GroupName: str
        :param _GroupType: Group type
        :type GroupType: str
        :param _Size: Number of domains in the group
        :type Size: int
        """
        self._GroupId = None
        self._GroupName = None
        self._GroupType = None
        self._Size = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupType(self):
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._GroupType = params.get("GroupType")
        self._Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LineGroupInfo(AbstractModel):
    """Information of a split zone group

    """

    def __init__(self):
        r"""
        :param _LineId: Split zone group ID
        :type LineId: str
        :param _Name: Split zone group name
        :type Name: str
        :param _Type: Group type
        :type Type: str
        :param _LineList: List of split zones in the split zone group
        :type LineList: list of str
        """
        self._LineId = None
        self._Name = None
        self._Type = None
        self._LineList = None

    @property
    def LineId(self):
        return self._LineId

    @LineId.setter
    def LineId(self, LineId):
        self._LineId = LineId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def LineList(self):
        return self._LineList

    @LineList.setter
    def LineList(self, LineList):
        self._LineList = LineList


    def _deserialize(self, params):
        self._LineId = params.get("LineId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._LineList = params.get("LineList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LineInfo(AbstractModel):
    """Information of a split zone

    """

    def __init__(self):
        r"""
        :param _Name: Split zone name
        :type Name: str
        :param _LineId: Split zone ID
        :type LineId: str
        """
        self._Name = None
        self._LineId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def LineId(self):
        return self._LineId

    @LineId.setter
    def LineId(self, LineId):
        self._LineId = LineId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._LineId = params.get("LineId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LockInfo(AbstractModel):
    """Domain lock information

    """

    def __init__(self):
        r"""
        :param _DomainId: Domain ID
        :type DomainId: int
        :param _LockCode: Domain unlock code
        :type LockCode: str
        :param _LockEnd: Automatic unlock date of the domain
        :type LockEnd: str
        """
        self._DomainId = None
        self._LockCode = None
        self._LockEnd = None

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def LockCode(self):
        return self._LockCode

    @LockCode.setter
    def LockCode(self, LockCode):
        self._LockCode = LockCode

    @property
    def LockEnd(self):
        return self._LockEnd

    @LockEnd.setter
    def LockEnd(self, LockEnd):
        self._LockEnd = LockEnd


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        self._LockCode = params.get("LockCode")
        self._LockEnd = params.get("LockEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainLockRequest(AbstractModel):
    """ModifyDomainLock request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain
        :type Domain: str
        :param _LockDays: Number of days to lock the domain. The maximum number of locked days can be obtained by calling the API for getting the permissions of a domain.
        :type LockDays: int
        :param _DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self._Domain = None
        self._LockDays = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def LockDays(self):
        return self._LockDays

    @LockDays.setter
    def LockDays(self, LockDays):
        self._LockDays = LockDays

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._LockDays = params.get("LockDays")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainLockResponse(AbstractModel):
    """ModifyDomainLock response structure.

    """

    def __init__(self):
        r"""
        :param _LockInfo: Domain lock information
        :type LockInfo: :class:`tencentcloud.dnspod.v20210323.models.LockInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LockInfo = None
        self._RequestId = None

    @property
    def LockInfo(self):
        return self._LockInfo

    @LockInfo.setter
    def LockInfo(self, LockInfo):
        self._LockInfo = LockInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LockInfo") is not None:
            self._LockInfo = LockInfo()
            self._LockInfo._deserialize(params.get("LockInfo"))
        self._RequestId = params.get("RequestId")


class ModifyDomainOwnerRequest(AbstractModel):
    """ModifyDomainOwner request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain
        :type Domain: str
        :param _Account: The account to which to transfer the domain, which can be an UIN or email address
        :type Account: str
        :param _DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self._Domain = None
        self._Account = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Account(self):
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Account = params.get("Account")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainOwnerResponse(AbstractModel):
    """ModifyDomainOwner response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDomainRemarkRequest(AbstractModel):
    """ModifyDomainRemark request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain
        :type Domain: str
        :param _DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        :param _Remark: Domain remarks. To delete the remarks, submit empty content.
        :type Remark: str
        """
        self._Domain = None
        self._DomainId = None
        self._Remark = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainRemarkResponse(AbstractModel):
    """ModifyDomainRemark response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDomainStatusRequest(AbstractModel):
    """ModifyDomainStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain
        :type Domain: str
        :param _Status: Domain status. Valid values: enable; disable.
        :type Status: str
        :param _DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self._Domain = None
        self._Status = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Status = params.get("Status")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainStatusResponse(AbstractModel):
    """ModifyDomainStatus response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDomainUnlockRequest(AbstractModel):
    """ModifyDomainUnlock request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain
        :type Domain: str
        :param _LockCode: Domain unlock code, which will be returned when the domain is locked.
        :type LockCode: str
        :param _DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self._Domain = None
        self._LockCode = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def LockCode(self):
        return self._LockCode

    @LockCode.setter
    def LockCode(self, LockCode):
        self._LockCode = LockCode

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._LockCode = params.get("LockCode")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainUnlockResponse(AbstractModel):
    """ModifyDomainUnlock response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyRecordBatchDetail(AbstractModel):
    """Response structure for bulk adding records

    """

    def __init__(self):
        r"""
        :param _RecordList: See `RecordInfoBatchModify`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RecordList: list of BatchRecordInfo
        :param _Id: Task ID
        :type Id: int
        :param _Domain: Domain
Note: This field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param _DomainGrade: Domain level
Note: This field may return null, indicating that no valid values can be obtained.
        :type DomainGrade: str
        :param _ErrMsg: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrMsg: str
        :param _Status: Task running status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _Operation: Operation type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Operation: str
        :param _DomainId: Domain ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type DomainId: int
        """
        self._RecordList = None
        self._Id = None
        self._Domain = None
        self._DomainGrade = None
        self._ErrMsg = None
        self._Status = None
        self._Operation = None
        self._DomainId = None

    @property
    def RecordList(self):
        return self._RecordList

    @RecordList.setter
    def RecordList(self, RecordList):
        self._RecordList = RecordList

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainGrade(self):
        return self._DomainGrade

    @DomainGrade.setter
    def DomainGrade(self, DomainGrade):
        self._DomainGrade = DomainGrade

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        if params.get("RecordList") is not None:
            self._RecordList = []
            for item in params.get("RecordList"):
                obj = BatchRecordInfo()
                obj._deserialize(item)
                self._RecordList.append(obj)
        self._Id = params.get("Id")
        self._Domain = params.get("Domain")
        self._DomainGrade = params.get("DomainGrade")
        self._ErrMsg = params.get("ErrMsg")
        self._Status = params.get("Status")
        self._Operation = params.get("Operation")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordBatchRequest(AbstractModel):
    """ModifyRecordBatch request structure.

    """

    def __init__(self):
        r"""
        :param _RecordIdList: Array of record IDs. You can view all DNS records and their IDs via the `DescribeRecordList` API.
        :type RecordIdList: list of int non-negative
        :param _Change: The field to be modified. Valid values: `sub_domain`, `record_type`, `area`, `value`, `mx`, `ttl`, `status`.
        :type Change: str
        :param _ChangeTo: The value to be changed to, which is required and subject to the `change` field.
        :type ChangeTo: str
        :param _Value: The record value to be changed to, which is required only if the `change` field is `record_type`.
        :type Value: str
        :param _MX: MX record priority, which is required only if the `Change` field is `mx`.
        :type MX: str
        """
        self._RecordIdList = None
        self._Change = None
        self._ChangeTo = None
        self._Value = None
        self._MX = None

    @property
    def RecordIdList(self):
        return self._RecordIdList

    @RecordIdList.setter
    def RecordIdList(self, RecordIdList):
        self._RecordIdList = RecordIdList

    @property
    def Change(self):
        return self._Change

    @Change.setter
    def Change(self, Change):
        self._Change = Change

    @property
    def ChangeTo(self):
        return self._ChangeTo

    @ChangeTo.setter
    def ChangeTo(self, ChangeTo):
        self._ChangeTo = ChangeTo

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def MX(self):
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX


    def _deserialize(self, params):
        self._RecordIdList = params.get("RecordIdList")
        self._Change = params.get("Change")
        self._ChangeTo = params.get("ChangeTo")
        self._Value = params.get("Value")
        self._MX = params.get("MX")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordBatchResponse(AbstractModel):
    """ModifyRecordBatch response structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Bulk task ID
        :type JobId: int
        :param _DetailList: See `modifyRecordBatchDetail`.
        :type DetailList: list of ModifyRecordBatchDetail
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._JobId = None
        self._DetailList = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def DetailList(self):
        return self._DetailList

    @DetailList.setter
    def DetailList(self, DetailList):
        self._DetailList = DetailList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        if params.get("DetailList") is not None:
            self._DetailList = []
            for item in params.get("DetailList"):
                obj = ModifyRecordBatchDetail()
                obj._deserialize(item)
                self._DetailList.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyRecordGroupRequest(AbstractModel):
    """ModifyRecordGroup request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain
        :type Domain: str
        :param _GroupName: Group name
        :type GroupName: str
        :param _GroupId: ID of the group to be modified
        :type GroupId: int
        :param _DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored.
        :type DomainId: int
        """
        self._Domain = None
        self._GroupName = None
        self._GroupId = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._GroupName = params.get("GroupName")
        self._GroupId = params.get("GroupId")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordGroupResponse(AbstractModel):
    """ModifyRecordGroup response structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: ID of the modified group
        :type GroupId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class ModifyRecordRemarkRequest(AbstractModel):
    """ModifyRecordRemark request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain
        :type Domain: str
        :param _RecordId: The record ID. You can view all DNS records and their IDs via the `DescribeRecordList` API.
        :type RecordId: int
        :param _DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        :param _Remark: DNS record remarks. To delete the remarks, submit empty content.
        :type Remark: str
        """
        self._Domain = None
        self._RecordId = None
        self._DomainId = None
        self._Remark = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._RecordId = params.get("RecordId")
        self._DomainId = params.get("DomainId")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordRemarkResponse(AbstractModel):
    """ModifyRecordRemark response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyRecordRequest(AbstractModel):
    """ModifyRecord request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain
        :type Domain: str
        :param _RecordType: Record type, which is obtained through the record type API. The value contains uppercase letters, such as `A`.
        :type RecordType: str
        :param _RecordLine: Record split zone, which is obtained through the record split zone API.
        :type RecordLine: str
        :param _Value: Record value, such as `IP : 200.200.200.200`, `CNAME : cname.dnspod.com`, and `MX : mail.dnspod.com`.
        :type Value: str
        :param _RecordId: The record ID. You can view all DNS records and their IDs via the `DescribeRecordList` API.
        :type RecordId: int
        :param _DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        :param _SubDomain: Host record such as `www`. If it is not passed in, it will be `@` by default.
        :type SubDomain: str
        :param _RecordLineId: Split zone ID, which is obtained through the record split zone API. The value is a string such as `10=1`. The `RecordLineId` parameter has a higher priority than `RecordLine`. If both of them are passed in, `RecordLineId` will be used first.
        :type RecordLineId: str
        :param _MX: MX priority, which is required for an MX record and will take effect if the record type is MX. Value range: 1–20.
        :type MX: int
        :param _TTL: TTL. Value range: 1–604800. The minimum value varies by domain level.
        :type TTL: int
        :param _Weight: Weight information, which is an integer between 0 and 100. It is supported only for enterprise VIP domains. `0` indicates not to pass in this parameter, i.e., not to set the weight.
        :type Weight: int
        :param _Status: Initial status of the record. Valid values: ENABLE, DISABLE. Default value: ENABLE. If `DISABLE` is passed in, the DNS record won't take effect, and the limit on round-robin DNS won't be verified.
        :type Status: str
        """
        self._Domain = None
        self._RecordType = None
        self._RecordLine = None
        self._Value = None
        self._RecordId = None
        self._DomainId = None
        self._SubDomain = None
        self._RecordLineId = None
        self._MX = None
        self._TTL = None
        self._Weight = None
        self._Status = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RecordLine(self):
        return self._RecordLine

    @RecordLine.setter
    def RecordLine(self, RecordLine):
        self._RecordLine = RecordLine

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordLineId(self):
        return self._RecordLineId

    @RecordLineId.setter
    def RecordLineId(self, RecordLineId):
        self._RecordLineId = RecordLineId

    @property
    def MX(self):
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX

    @property
    def TTL(self):
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._RecordType = params.get("RecordType")
        self._RecordLine = params.get("RecordLine")
        self._Value = params.get("Value")
        self._RecordId = params.get("RecordId")
        self._DomainId = params.get("DomainId")
        self._SubDomain = params.get("SubDomain")
        self._RecordLineId = params.get("RecordLineId")
        self._MX = params.get("MX")
        self._TTL = params.get("TTL")
        self._Weight = params.get("Weight")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordResponse(AbstractModel):
    """ModifyRecord response structure.

    """

    def __init__(self):
        r"""
        :param _RecordId: Record ID
        :type RecordId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RecordId = None
        self._RequestId = None

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RecordId = params.get("RecordId")
        self._RequestId = params.get("RequestId")


class ModifyRecordStatusRequest(AbstractModel):
    """ModifyRecordStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain
        :type Domain: str
        :param _RecordId: The record ID. You can view all DNS records and their IDs via the `DescribeRecordList` API.
        :type RecordId: int
        :param _Status: Record status. Valid values: `ENABLE`, `DISABLE`. If `DISABLE` is passed in, the DNS record won't take effect, and the limit on round-robin DNS won't be verified.
        :type Status: str
        :param _DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored. You can view all `Domain` and `DomainId` values via the `DescribeDomainList` API.
        :type DomainId: int
        """
        self._Domain = None
        self._RecordId = None
        self._Status = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._RecordId = params.get("RecordId")
        self._Status = params.get("Status")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordStatusResponse(AbstractModel):
    """ModifyRecordStatus response structure.

    """

    def __init__(self):
        r"""
        :param _RecordId: Record ID.
        :type RecordId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RecordId = None
        self._RequestId = None

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RecordId = params.get("RecordId")
        self._RequestId = params.get("RequestId")


class ModifyRecordToGroupRequest(AbstractModel):
    """ModifyRecordToGroup request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain
        :type Domain: str
        :param _GroupId: Group ID
        :type GroupId: int
        :param _RecordId: Record ID. Separate multiple IDs by vertical bar ("|").
        :type RecordId: str
        :param _DomainId: The domain ID. `DomainId` takes priority over `Domain`. If `DomainId` is passed in, `Domain` is ignored.
        :type DomainId: int
        """
        self._Domain = None
        self._GroupId = None
        self._RecordId = None
        self._DomainId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._GroupId = params.get("GroupId")
        self._RecordId = params.get("RecordId")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordToGroupResponse(AbstractModel):
    """ModifyRecordToGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class PurviewInfo(AbstractModel):
    """Domain permission

    """

    def __init__(self):
        r"""
        :param _Name: Permission name
        :type Name: str
        :param _Value: Permission value
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordCountInfo(AbstractModel):
    """Count info of the queried record list

    """

    def __init__(self):
        r"""
        :param _SubdomainCount: The subdomain count.
        :type SubdomainCount: int
        :param _ListCount: The count of records returned in the list.
        :type ListCount: int
        :param _TotalCount: The total record count.
        :type TotalCount: int
        """
        self._SubdomainCount = None
        self._ListCount = None
        self._TotalCount = None

    @property
    def SubdomainCount(self):
        return self._SubdomainCount

    @SubdomainCount.setter
    def SubdomainCount(self, SubdomainCount):
        self._SubdomainCount = SubdomainCount

    @property
    def ListCount(self):
        return self._ListCount

    @ListCount.setter
    def ListCount(self, ListCount):
        self._ListCount = ListCount

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        self._SubdomainCount = params.get("SubdomainCount")
        self._ListCount = params.get("ListCount")
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordGroupInfo(AbstractModel):
    """Information of a DNS record group

    """

    def __init__(self):
        r"""
        :param _GroupId: Group ID
        :type GroupId: int
        :param _GroupName: Group name
        :type GroupName: str
        :param _GroupType: Group type. Valid values: `system`, `user`.
        :type GroupType: str
        """
        self._GroupId = None
        self._GroupName = None
        self._GroupType = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupType(self):
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._GroupType = params.get("GroupType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordInfo(AbstractModel):
    """Record information

    """

    def __init__(self):
        r"""
        :param _Id: Record ID.
        :type Id: int
        :param _SubDomain: Subdomain (host record).
        :type SubDomain: str
        :param _RecordType: Record type. For more information, see the `DescribeRecordType` API.
        :type RecordType: str
        :param _RecordLine: Split zone of the DNS record. For more information, see the `DescribeRecordLineList` API.
        :type RecordLine: str
        :param _RecordLineId: Split zone ID of the DNS record. For more information, see the `DescribeRecordLineList` API.
        :type RecordLineId: str
        :param _Value: Record value.
        :type Value: str
        :param _Weight: Record weight.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Weight: int
        :param _MX: MX record value. It is 0 by default for non-MX records.
        :type MX: int
        :param _TTL: TTL value of the record.
        :type TTL: int
        :param _Enabled: Record status. Valid values: 0 (disabled); 1 (enabled).
        :type Enabled: int
        :param _MonitorStatus: D-Monitor status of the record.
"Ok" : The server is normal.
"Warn" : There is an alarm on this record, and the server returns 4XX.
"Down" : The server is down.
"" : D-Monitor is disabled for this record.
        :type MonitorStatus: str
        :param _Remark: Record remarks.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param _UpdatedOn: Last update time of the record.
        :type UpdatedOn: str
        :param _DomainId: Domain ID.
        :type DomainId: int
        """
        self._Id = None
        self._SubDomain = None
        self._RecordType = None
        self._RecordLine = None
        self._RecordLineId = None
        self._Value = None
        self._Weight = None
        self._MX = None
        self._TTL = None
        self._Enabled = None
        self._MonitorStatus = None
        self._Remark = None
        self._UpdatedOn = None
        self._DomainId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RecordLine(self):
        return self._RecordLine

    @RecordLine.setter
    def RecordLine(self, RecordLine):
        self._RecordLine = RecordLine

    @property
    def RecordLineId(self):
        return self._RecordLineId

    @RecordLineId.setter
    def RecordLineId(self, RecordLineId):
        self._RecordLineId = RecordLineId

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def MX(self):
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX

    @property
    def TTL(self):
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def MonitorStatus(self):
        return self._MonitorStatus

    @MonitorStatus.setter
    def MonitorStatus(self, MonitorStatus):
        self._MonitorStatus = MonitorStatus

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def UpdatedOn(self):
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._SubDomain = params.get("SubDomain")
        self._RecordType = params.get("RecordType")
        self._RecordLine = params.get("RecordLine")
        self._RecordLineId = params.get("RecordLineId")
        self._Value = params.get("Value")
        self._Weight = params.get("Weight")
        self._MX = params.get("MX")
        self._TTL = params.get("TTL")
        self._Enabled = params.get("Enabled")
        self._MonitorStatus = params.get("MonitorStatus")
        self._Remark = params.get("Remark")
        self._UpdatedOn = params.get("UpdatedOn")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordListItem(AbstractModel):
    """Record list elements

    """

    def __init__(self):
        r"""
        :param _RecordId: The record ID.
        :type RecordId: int
        :param _Value: The record value.
        :type Value: str
        :param _Status: The record status. Valid values: `ENABLE` (enabled), `DISABLE` (disabled).
        :type Status: str
        :param _UpdatedOn: The update time.
        :type UpdatedOn: str
        :param _Name: The host name.
        :type Name: str
        :param _Line: The record split zone.
        :type Line: str
        :param _LineId: The split zone ID.
        :type LineId: str
        :param _Type: The record type.
        :type Type: str
        :param _Weight: The record weight, which is required for round-robin DNS records.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Weight: int
        :param _MonitorStatus: The monitoring status of the record. Valid values: `OK` (normal), `WARN` (warning), and `DOWN` (downtime). It is empty if no monitoring is set or the monitoring is suspended.
        :type MonitorStatus: str
        :param _Remark: The record remarks.
        :type Remark: str
        :param _TTL: The record cache time.
        :type TTL: int
        :param _MX: The MX value, applicable to the MX record only.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MX: int
        :param _DefaultNS: Whether it is a default NS record.
        :type DefaultNS: bool
        """
        self._RecordId = None
        self._Value = None
        self._Status = None
        self._UpdatedOn = None
        self._Name = None
        self._Line = None
        self._LineId = None
        self._Type = None
        self._Weight = None
        self._MonitorStatus = None
        self._Remark = None
        self._TTL = None
        self._MX = None
        self._DefaultNS = None

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UpdatedOn(self):
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Line(self):
        return self._Line

    @Line.setter
    def Line(self, Line):
        self._Line = Line

    @property
    def LineId(self):
        return self._LineId

    @LineId.setter
    def LineId(self, LineId):
        self._LineId = LineId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def MonitorStatus(self):
        return self._MonitorStatus

    @MonitorStatus.setter
    def MonitorStatus(self, MonitorStatus):
        self._MonitorStatus = MonitorStatus

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def TTL(self):
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def MX(self):
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX

    @property
    def DefaultNS(self):
        return self._DefaultNS

    @DefaultNS.setter
    def DefaultNS(self, DefaultNS):
        self._DefaultNS = DefaultNS


    def _deserialize(self, params):
        self._RecordId = params.get("RecordId")
        self._Value = params.get("Value")
        self._Status = params.get("Status")
        self._UpdatedOn = params.get("UpdatedOn")
        self._Name = params.get("Name")
        self._Line = params.get("Line")
        self._LineId = params.get("LineId")
        self._Type = params.get("Type")
        self._Weight = params.get("Weight")
        self._MonitorStatus = params.get("MonitorStatus")
        self._Remark = params.get("Remark")
        self._TTL = params.get("TTL")
        self._MX = params.get("MX")
        self._DefaultNS = params.get("DefaultNS")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubdomainAliasAnalyticsItem(AbstractModel):
    """DNS query volume of the subdomain alias

    """

    def __init__(self):
        r"""
        :param _Info: Statistics on the DNS query volume of a subdomain
        :type Info: :class:`tencentcloud.dnspod.v20210323.models.SubdomainAnalyticsInfo`
        :param _Data: DNS query volume in the current statistical dimension
        :type Data: list of DomainAnalyticsDetail
        """
        self._Info = None
        self._Data = None

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self._Info = SubdomainAnalyticsInfo()
            self._Info._deserialize(params.get("Info"))
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DomainAnalyticsDetail()
                obj._deserialize(item)
                self._Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubdomainAnalyticsInfo(AbstractModel):
    """Statistics on the DNS query volume of a subdomain

    """

    def __init__(self):
        r"""
        :param _DnsFormat: `DATE`: Daily; `HOUR`: Hourly
        :type DnsFormat: str
        :param _DnsTotal: Total DNS query volume for the current statistical period
        :type DnsTotal: int
        :param _Domain: The queried domain
        :type Domain: str
        :param _StartDate: Start date of the current statistical period
        :type StartDate: str
        :param _EndDate: End date of the current statistical period
        :type EndDate: str
        :param _Subdomain: Subdomain
        :type Subdomain: str
        """
        self._DnsFormat = None
        self._DnsTotal = None
        self._Domain = None
        self._StartDate = None
        self._EndDate = None
        self._Subdomain = None

    @property
    def DnsFormat(self):
        return self._DnsFormat

    @DnsFormat.setter
    def DnsFormat(self, DnsFormat):
        self._DnsFormat = DnsFormat

    @property
    def DnsTotal(self):
        return self._DnsTotal

    @DnsTotal.setter
    def DnsTotal(self, DnsTotal):
        self._DnsTotal = DnsTotal

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def StartDate(self):
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Subdomain(self):
        return self._Subdomain

    @Subdomain.setter
    def Subdomain(self, Subdomain):
        self._Subdomain = Subdomain


    def _deserialize(self, params):
        self._DnsFormat = params.get("DnsFormat")
        self._DnsTotal = params.get("DnsTotal")
        self._Domain = params.get("Domain")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Subdomain = params.get("Subdomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        