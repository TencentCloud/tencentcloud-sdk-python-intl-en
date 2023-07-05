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
        :param _UniqVpcId: VpcId: vpc-xadsafsdasd
        :type UniqVpcId: str
        :param _Region: VPC region: ap-guangzhou, ap-shanghai
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Region: str
        :param _Uin: VPC account: 123456789
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Uin: str
        :param _VpcName: VPC name: testname
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type VpcName: str
        """
        self._UniqVpcId = None
        self._Region = None
        self._Uin = None
        self._VpcName = None

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName


    def _deserialize(self, params):
        self._UniqVpcId = params.get("UniqVpcId")
        self._Region = params.get("Region")
        self._Uin = params.get("Uin")
        self._VpcName = params.get("VpcName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountVpcInfoOut(AbstractModel):
    """Output parameters of the associated VPC

    """

    def __init__(self):
        r"""
        :param _VpcId: VpcId: vpc-xadsafsdasd
        :type VpcId: str
        :param _Region: Region: ap-guangzhou, ap-shanghai
        :type Region: str
        :param _Uin: VPC ID: 123456789
        :type Uin: str
        :param _VpcName: VPC name: testname
        :type VpcName: str
        """
        self._VpcId = None
        self._Region = None
        self._Uin = None
        self._VpcName = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._Region = params.get("Region")
        self._Uin = params.get("Uin")
        self._VpcName = params.get("VpcName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountVpcInfoOutput(AbstractModel):
    """Output parameters of the associated VPC

    """

    def __init__(self):
        r"""
        :param _Uin: UIN of the VPC account
        :type Uin: str
        :param _UniqVpcId: VPC ID
        :type UniqVpcId: str
        :param _Region: Region
        :type Region: str
        """
        self._Uin = None
        self._UniqVpcId = None
        self._Region = None

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._UniqVpcId = params.get("UniqVpcId")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditLog(AbstractModel):
    """Operation log

    """

    def __init__(self):
        r"""
        :param _Resource: Log type
        :type Resource: str
        :param _Metric: Log table name
        :type Metric: str
        :param _TotalCount: Total number of logs
        :type TotalCount: int
        :param _DataSet: List of logs
        :type DataSet: list of AuditLogInfo
        """
        self._Resource = None
        self._Metric = None
        self._TotalCount = None
        self._DataSet = None

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DataSet(self):
        return self._DataSet

    @DataSet.setter
    def DataSet(self, DataSet):
        self._DataSet = DataSet


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._Metric = params.get("Metric")
        self._TotalCount = params.get("TotalCount")
        if params.get("DataSet") is not None:
            self._DataSet = []
            for item in params.get("DataSet"):
                obj = AuditLogInfo()
                obj._deserialize(item)
                self._DataSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditLogInfo(AbstractModel):
    """Log details

    """

    def __init__(self):
        r"""
        :param _Date: Time
        :type Date: str
        :param _OperatorUin: Operator UIN
        :type OperatorUin: str
        :param _Content: Log content
        :type Content: str
        """
        self._Date = None
        self._OperatorUin = None
        self._Content = None

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def OperatorUin(self):
        return self._OperatorUin

    @OperatorUin.setter
    def OperatorUin(self, OperatorUin):
        self._OperatorUin = OperatorUin

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Date = params.get("Date")
        self._OperatorUin = params.get("OperatorUin")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrivateDNSAccountRequest(AbstractModel):
    """CreatePrivateDNSAccount request structure.

    """

    def __init__(self):
        r"""
        :param _Account: Private DNS account
        :type Account: :class:`tencentcloud.privatedns.v20201028.models.PrivateDNSAccount`
        """
        self._Account = None

    @property
    def Account(self):
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account


    def _deserialize(self, params):
        if params.get("Account") is not None:
            self._Account = PrivateDNSAccount()
            self._Account._deserialize(params.get("Account"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrivateDNSAccountResponse(AbstractModel):
    """CreatePrivateDNSAccount response structure.

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


class CreatePrivateZoneRecordRequest(AbstractModel):
    """CreatePrivateZoneRecord request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Private domain ID
        :type ZoneId: str
        :param _RecordType: Record type. Valid values: "A", "AAAA", "CNAME", "MX", "TXT", "PTR"
        :type RecordType: str
        :param _SubDomain: Subdomain, such as "www", "m", and "@"
        :type SubDomain: str
        :param _RecordValue: Record value, such as IP: 192.168.10.2, CNAME: cname.qcloud.com., and MX: mail.qcloud.com.
        :type RecordValue: str
        :param _Weight: Record weight. Value range: 1–100
        :type Weight: int
        :param _MX: MX priority, which is required when the record type is MX. Valid values: 5, 10, 15, 20, 30, 40, 50
        :type MX: int
        :param _TTL: Record cache time. The smaller the value, the faster the record will take effect. Value range: 1–86400s. Default value: 600
        :type TTL: int
        """
        self._ZoneId = None
        self._RecordType = None
        self._SubDomain = None
        self._RecordValue = None
        self._Weight = None
        self._MX = None
        self._TTL = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordValue(self):
        return self._RecordValue

    @RecordValue.setter
    def RecordValue(self, RecordValue):
        self._RecordValue = RecordValue

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


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RecordType = params.get("RecordType")
        self._SubDomain = params.get("SubDomain")
        self._RecordValue = params.get("RecordValue")
        self._Weight = params.get("Weight")
        self._MX = params.get("MX")
        self._TTL = params.get("TTL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrivateZoneRecordResponse(AbstractModel):
    """CreatePrivateZoneRecord response structure.

    """

    def __init__(self):
        r"""
        :param _RecordId: Record ID
        :type RecordId: str
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


class CreatePrivateZoneRequest(AbstractModel):
    """CreatePrivateZone request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain name, which must be in the format of standard TLD
        :type Domain: str
        :param _TagSet: Tags the private domain when it is created
        :type TagSet: list of TagInfo
        :param _VpcSet: Associates the private domain to a VPC when it is created
        :type VpcSet: list of VpcInfo
        :param _Remark: Remarks
        :type Remark: str
        :param _DnsForwardStatus: Whether to enable subdomain recursive DNS. Valid values: `ENABLED` (default) and `DISABLED`.
        :type DnsForwardStatus: str
        :param _Vpcs: Associates the private domain to a VPC when it is created
        :type Vpcs: list of VpcInfo
        :param _AccountVpcSet: List of authorized accounts' VPCs to associate with the private domain
        :type AccountVpcSet: list of AccountVpcInfo
        :param _CnameSpeedupStatus: Whether to enable CNAME flattening. Valid values: `ENABLED` (default) and `DISABLED`.
        :type CnameSpeedupStatus: str
        """
        self._Domain = None
        self._TagSet = None
        self._VpcSet = None
        self._Remark = None
        self._DnsForwardStatus = None
        self._Vpcs = None
        self._AccountVpcSet = None
        self._CnameSpeedupStatus = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def TagSet(self):
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def VpcSet(self):
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def DnsForwardStatus(self):
        return self._DnsForwardStatus

    @DnsForwardStatus.setter
    def DnsForwardStatus(self, DnsForwardStatus):
        self._DnsForwardStatus = DnsForwardStatus

    @property
    def Vpcs(self):
        return self._Vpcs

    @Vpcs.setter
    def Vpcs(self, Vpcs):
        self._Vpcs = Vpcs

    @property
    def AccountVpcSet(self):
        return self._AccountVpcSet

    @AccountVpcSet.setter
    def AccountVpcSet(self, AccountVpcSet):
        self._AccountVpcSet = AccountVpcSet

    @property
    def CnameSpeedupStatus(self):
        return self._CnameSpeedupStatus

    @CnameSpeedupStatus.setter
    def CnameSpeedupStatus(self, CnameSpeedupStatus):
        self._CnameSpeedupStatus = CnameSpeedupStatus


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = TagInfo()
                obj._deserialize(item)
                self._TagSet.append(obj)
        if params.get("VpcSet") is not None:
            self._VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcSet.append(obj)
        self._Remark = params.get("Remark")
        self._DnsForwardStatus = params.get("DnsForwardStatus")
        if params.get("Vpcs") is not None:
            self._Vpcs = []
            for item in params.get("Vpcs"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._Vpcs.append(obj)
        if params.get("AccountVpcSet") is not None:
            self._AccountVpcSet = []
            for item in params.get("AccountVpcSet"):
                obj = AccountVpcInfo()
                obj._deserialize(item)
                self._AccountVpcSet.append(obj)
        self._CnameSpeedupStatus = params.get("CnameSpeedupStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrivateZoneResponse(AbstractModel):
    """CreatePrivateZone response structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Private domain ID, such as zone-xxxxxx
        :type ZoneId: str
        :param _Domain: Private domain
        :type Domain: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ZoneId = None
        self._Domain = None
        self._RequestId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Domain = params.get("Domain")
        self._RequestId = params.get("RequestId")


class DatePoint(AbstractModel):
    """Time statistics

    """

    def __init__(self):
        r"""
        :param _Date: Time
        :type Date: str
        :param _Value: Value
        :type Value: int
        """
        self._Date = None
        self._Value = None

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Date = params.get("Date")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountVpcListRequest(AbstractModel):
    """DescribeAccountVpcList request structure.

    """

    def __init__(self):
        r"""
        :param _AccountUin: UIN of account
        :type AccountUin: str
        :param _Offset: Pagination offset, starting from 0
        :type Offset: int
        :param _Limit: Number of entries per page. Maximum value: `100`. Default value: `20`
        :type Limit: int
        :param _Filters: Filter parameters
        :type Filters: list of Filter
        """
        self._AccountUin = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def AccountUin(self):
        return self._AccountUin

    @AccountUin.setter
    def AccountUin(self, AccountUin):
        self._AccountUin = AccountUin

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._AccountUin = params.get("AccountUin")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountVpcListResponse(AbstractModel):
    """DescribeAccountVpcList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of VPCs
        :type TotalCount: int
        :param _VpcSet: VPC list
        :type VpcSet: list of AccountVpcInfoOut
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._VpcSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VpcSet(self):
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("VpcSet") is not None:
            self._VpcSet = []
            for item in params.get("VpcSet"):
                obj = AccountVpcInfoOut()
                obj._deserialize(item)
                self._VpcSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAuditLogRequest(AbstractModel):
    """DescribeAuditLog request structure.

    """

    def __init__(self):
        r"""
        :param _TimeRangeBegin: Request volume statistics start time
        :type TimeRangeBegin: str
        :param _Filters: Filter parameter. Valid values: ZoneId (private domain ID), Domain (private domain), OperatorUin (operator account ID)
        :type Filters: list of Filter
        :param _TimeRangeEnd: Request volume statistics end time
        :type TimeRangeEnd: str
        :param _Offset: Pagination offset, starting from 0
        :type Offset: int
        :param _Limit: Number of entries per page. Maximum value: 100. Default value: 20
        :type Limit: int
        """
        self._TimeRangeBegin = None
        self._Filters = None
        self._TimeRangeEnd = None
        self._Offset = None
        self._Limit = None

    @property
    def TimeRangeBegin(self):
        return self._TimeRangeBegin

    @TimeRangeBegin.setter
    def TimeRangeBegin(self, TimeRangeBegin):
        self._TimeRangeBegin = TimeRangeBegin

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TimeRangeEnd(self):
        return self._TimeRangeEnd

    @TimeRangeEnd.setter
    def TimeRangeEnd(self, TimeRangeEnd):
        self._TimeRangeEnd = TimeRangeEnd

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
        self._TimeRangeBegin = params.get("TimeRangeBegin")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._TimeRangeEnd = params.get("TimeRangeEnd")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditLogResponse(AbstractModel):
    """DescribeAuditLog response structure.

    """

    def __init__(self):
        r"""
        :param _Data: List of operation logs
        :type Data: list of AuditLog
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
                obj = AuditLog()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDashboardRequest(AbstractModel):
    """DescribeDashboard request structure.

    """


class DescribeDashboardResponse(AbstractModel):
    """DescribeDashboard response structure.

    """

    def __init__(self):
        r"""
        :param _ZoneTotal: Total number of private domain DNS records
        :type ZoneTotal: int
        :param _ZoneVpcCount: Number of VPCs associated with private domain
        :type ZoneVpcCount: int
        :param _RequestTotalCount: Total number of historical requests
        :type RequestTotalCount: int
        :param _FlowUsage: Traffic package usage
        :type FlowUsage: list of FlowUsage
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ZoneTotal = None
        self._ZoneVpcCount = None
        self._RequestTotalCount = None
        self._FlowUsage = None
        self._RequestId = None

    @property
    def ZoneTotal(self):
        return self._ZoneTotal

    @ZoneTotal.setter
    def ZoneTotal(self, ZoneTotal):
        self._ZoneTotal = ZoneTotal

    @property
    def ZoneVpcCount(self):
        return self._ZoneVpcCount

    @ZoneVpcCount.setter
    def ZoneVpcCount(self, ZoneVpcCount):
        self._ZoneVpcCount = ZoneVpcCount

    @property
    def RequestTotalCount(self):
        return self._RequestTotalCount

    @RequestTotalCount.setter
    def RequestTotalCount(self, RequestTotalCount):
        self._RequestTotalCount = RequestTotalCount

    @property
    def FlowUsage(self):
        return self._FlowUsage

    @FlowUsage.setter
    def FlowUsage(self, FlowUsage):
        self._FlowUsage = FlowUsage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ZoneTotal = params.get("ZoneTotal")
        self._ZoneVpcCount = params.get("ZoneVpcCount")
        self._RequestTotalCount = params.get("RequestTotalCount")
        if params.get("FlowUsage") is not None:
            self._FlowUsage = []
            for item in params.get("FlowUsage"):
                obj = FlowUsage()
                obj._deserialize(item)
                self._FlowUsage.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrivateDNSAccountListRequest(AbstractModel):
    """DescribePrivateDNSAccountList request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Pagination offset, starting from `0`
        :type Offset: int
        :param _Limit: Number of entries per page. Maximum value: `100`. Default value: `20`
        :type Limit: int
        :param _Filters: Filter parameters
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrivateDNSAccountListResponse(AbstractModel):
    """DescribePrivateDNSAccountList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of Private DNS accounts
        :type TotalCount: int
        :param _AccountSet: List of Private DNS accounts
        :type AccountSet: list of PrivateDNSAccount
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._AccountSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AccountSet(self):
        return self._AccountSet

    @AccountSet.setter
    def AccountSet(self, AccountSet):
        self._AccountSet = AccountSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AccountSet") is not None:
            self._AccountSet = []
            for item in params.get("AccountSet"):
                obj = PrivateDNSAccount()
                obj._deserialize(item)
                self._AccountSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrivateZoneServiceRequest(AbstractModel):
    """DescribePrivateZoneService request structure.

    """


class DescribePrivateZoneServiceResponse(AbstractModel):
    """DescribePrivateZoneService response structure.

    """

    def __init__(self):
        r"""
        :param _ServiceStatus: Private DNS service activation status. Valid values: ENABLED, DISABLED
        :type ServiceStatus: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ServiceStatus = None
        self._RequestId = None

    @property
    def ServiceStatus(self):
        return self._ServiceStatus

    @ServiceStatus.setter
    def ServiceStatus(self, ServiceStatus):
        self._ServiceStatus = ServiceStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ServiceStatus = params.get("ServiceStatus")
        self._RequestId = params.get("RequestId")


class DescribeQuotaUsageRequest(AbstractModel):
    """DescribeQuotaUsage request structure.

    """


class DescribeQuotaUsageResponse(AbstractModel):
    """DescribeQuotaUsage response structure.

    """

    def __init__(self):
        r"""
        :param _TldQuota: TLD quota usage
        :type TldQuota: :class:`tencentcloud.privatedns.v20201028.models.TldQuota`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TldQuota = None
        self._RequestId = None

    @property
    def TldQuota(self):
        return self._TldQuota

    @TldQuota.setter
    def TldQuota(self, TldQuota):
        self._TldQuota = TldQuota

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TldQuota") is not None:
            self._TldQuota = TldQuota()
            self._TldQuota._deserialize(params.get("TldQuota"))
        self._RequestId = params.get("RequestId")


class DescribeRequestDataRequest(AbstractModel):
    """DescribeRequestData request structure.

    """

    def __init__(self):
        r"""
        :param _TimeRangeBegin: Request volume statistics start time in the format of 2020-11-22 00:00:00
        :type TimeRangeBegin: str
        :param _Filters: Filter parameter:
        :type Filters: list of Filter
        :param _TimeRangeEnd: Request volume statistics end time in the format of 2020-11-22 23:59:59
        :type TimeRangeEnd: str
        """
        self._TimeRangeBegin = None
        self._Filters = None
        self._TimeRangeEnd = None

    @property
    def TimeRangeBegin(self):
        return self._TimeRangeBegin

    @TimeRangeBegin.setter
    def TimeRangeBegin(self, TimeRangeBegin):
        self._TimeRangeBegin = TimeRangeBegin

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TimeRangeEnd(self):
        return self._TimeRangeEnd

    @TimeRangeEnd.setter
    def TimeRangeEnd(self, TimeRangeEnd):
        self._TimeRangeEnd = TimeRangeEnd


    def _deserialize(self, params):
        self._TimeRangeBegin = params.get("TimeRangeBegin")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._TimeRangeEnd = params.get("TimeRangeEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRequestDataResponse(AbstractModel):
    """DescribeRequestData response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Request volume statistics table
        :type Data: list of MetricData
        :param _Interval: Request volume unit time. Valid values: Day, Hour
        :type Interval: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Interval = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

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
                obj = MetricData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Interval = params.get("Interval")
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """Filter parameter

    """

    def __init__(self):
        r"""
        :param _Name: Parameter name
        :type Name: str
        :param _Values: Array of parameter values
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowUsage(AbstractModel):
    """Traffic package usage

    """

    def __init__(self):
        r"""
        :param _FlowType: Traffic package type, Valid values: ZONE (private domain); TRAFFIC (DNS traffic package)
        :type FlowType: str
        :param _TotalQuantity: Traffic package quota
        :type TotalQuantity: int
        :param _AvailableQuantity: Available quota of traffic package
        :type AvailableQuantity: int
        """
        self._FlowType = None
        self._TotalQuantity = None
        self._AvailableQuantity = None

    @property
    def FlowType(self):
        return self._FlowType

    @FlowType.setter
    def FlowType(self, FlowType):
        self._FlowType = FlowType

    @property
    def TotalQuantity(self):
        return self._TotalQuantity

    @TotalQuantity.setter
    def TotalQuantity(self, TotalQuantity):
        self._TotalQuantity = TotalQuantity

    @property
    def AvailableQuantity(self):
        return self._AvailableQuantity

    @AvailableQuantity.setter
    def AvailableQuantity(self, AvailableQuantity):
        self._AvailableQuantity = AvailableQuantity


    def _deserialize(self, params):
        self._FlowType = params.get("FlowType")
        self._TotalQuantity = params.get("TotalQuantity")
        self._AvailableQuantity = params.get("AvailableQuantity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricData(AbstractModel):
    """Statistics table

    """

    def __init__(self):
        r"""
        :param _Resource: Resource description
        :type Resource: str
        :param _Metric: Table name
        :type Metric: str
        :param _DataSet: Table data
        :type DataSet: list of DatePoint
        :param _MetricCount: The total number of requests within the query scope.
Note: This field may return null, indicating that no valid value can be obtained.
        :type MetricCount: int
        """
        self._Resource = None
        self._Metric = None
        self._DataSet = None
        self._MetricCount = None

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def DataSet(self):
        return self._DataSet

    @DataSet.setter
    def DataSet(self, DataSet):
        self._DataSet = DataSet

    @property
    def MetricCount(self):
        return self._MetricCount

    @MetricCount.setter
    def MetricCount(self, MetricCount):
        self._MetricCount = MetricCount


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._Metric = params.get("Metric")
        if params.get("DataSet") is not None:
            self._DataSet = []
            for item in params.get("DataSet"):
                obj = DatePoint()
                obj._deserialize(item)
                self._DataSet.append(obj)
        self._MetricCount = params.get("MetricCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrivateZoneRecordRequest(AbstractModel):
    """ModifyPrivateZoneRecord request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Private domain ID
        :type ZoneId: str
        :param _RecordId: Record ID
        :type RecordId: str
        :param _RecordType: Record type. Valid values: "A", "AAAA", "CNAME", "MX", "TXT", "PTR"
        :type RecordType: str
        :param _SubDomain: Subdomain, such as "www", "m", and "@"
        :type SubDomain: str
        :param _RecordValue: Record value, such as IP: 192.168.10.2, CNAME: cname.qcloud.com., and MX: mail.qcloud.com.
        :type RecordValue: str
        :param _Weight: Record weight. Value range: 1–100
        :type Weight: int
        :param _MX: MX priority, which is required when the record type is MX. Valid values: 5, 10, 15, 20, 30, 40, 50
        :type MX: int
        :param _TTL: Record cache time. The smaller the value, the faster the record will take effect. Value range: 1–86400s. Default value: 600
        :type TTL: int
        """
        self._ZoneId = None
        self._RecordId = None
        self._RecordType = None
        self._SubDomain = None
        self._RecordValue = None
        self._Weight = None
        self._MX = None
        self._TTL = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordValue(self):
        return self._RecordValue

    @RecordValue.setter
    def RecordValue(self, RecordValue):
        self._RecordValue = RecordValue

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


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RecordId = params.get("RecordId")
        self._RecordType = params.get("RecordType")
        self._SubDomain = params.get("SubDomain")
        self._RecordValue = params.get("RecordValue")
        self._Weight = params.get("Weight")
        self._MX = params.get("MX")
        self._TTL = params.get("TTL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrivateZoneRecordResponse(AbstractModel):
    """ModifyPrivateZoneRecord response structure.

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


class ModifyPrivateZoneRequest(AbstractModel):
    """ModifyPrivateZone request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Private domain ID
        :type ZoneId: str
        :param _Remark: Remarks
        :type Remark: str
        :param _DnsForwardStatus: Whether to enable subdomain recursive DNS. Valid values: ENABLED, DISABLED
        :type DnsForwardStatus: str
        :param _CnameSpeedupStatus: Whether to enable CNAME flattening. Valid values: `ENABLED` and `DISABLED`.
        :type CnameSpeedupStatus: str
        """
        self._ZoneId = None
        self._Remark = None
        self._DnsForwardStatus = None
        self._CnameSpeedupStatus = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def DnsForwardStatus(self):
        return self._DnsForwardStatus

    @DnsForwardStatus.setter
    def DnsForwardStatus(self, DnsForwardStatus):
        self._DnsForwardStatus = DnsForwardStatus

    @property
    def CnameSpeedupStatus(self):
        return self._CnameSpeedupStatus

    @CnameSpeedupStatus.setter
    def CnameSpeedupStatus(self, CnameSpeedupStatus):
        self._CnameSpeedupStatus = CnameSpeedupStatus


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Remark = params.get("Remark")
        self._DnsForwardStatus = params.get("DnsForwardStatus")
        self._CnameSpeedupStatus = params.get("CnameSpeedupStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrivateZoneResponse(AbstractModel):
    """ModifyPrivateZone response structure.

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


class ModifyPrivateZoneVpcRequest(AbstractModel):
    """ModifyPrivateZoneVpc request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Private domain ID
        :type ZoneId: str
        :param _VpcSet: List of all VPCs associated with private domain
        :type VpcSet: list of VpcInfo
        :param _AccountVpcSet: List of authorized accounts' VPCs to associate with the private domain
        :type AccountVpcSet: list of AccountVpcInfo
        """
        self._ZoneId = None
        self._VpcSet = None
        self._AccountVpcSet = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcSet(self):
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

    @property
    def AccountVpcSet(self):
        return self._AccountVpcSet

    @AccountVpcSet.setter
    def AccountVpcSet(self, AccountVpcSet):
        self._AccountVpcSet = AccountVpcSet


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("VpcSet") is not None:
            self._VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcSet.append(obj)
        if params.get("AccountVpcSet") is not None:
            self._AccountVpcSet = []
            for item in params.get("AccountVpcSet"):
                obj = AccountVpcInfo()
                obj._deserialize(item)
                self._AccountVpcSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrivateZoneVpcResponse(AbstractModel):
    """ModifyPrivateZoneVpc response structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Private domain ID, such as zone-xxxxxx
        :type ZoneId: str
        :param _VpcSet: List of VPCs associated with domain
        :type VpcSet: list of VpcInfo
        :param _AccountVpcSet: List of authorized accounts' VPCs associated with the private domain
        :type AccountVpcSet: list of AccountVpcInfoOutput
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ZoneId = None
        self._VpcSet = None
        self._AccountVpcSet = None
        self._RequestId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcSet(self):
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

    @property
    def AccountVpcSet(self):
        return self._AccountVpcSet

    @AccountVpcSet.setter
    def AccountVpcSet(self, AccountVpcSet):
        self._AccountVpcSet = AccountVpcSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("VpcSet") is not None:
            self._VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcSet.append(obj)
        if params.get("AccountVpcSet") is not None:
            self._AccountVpcSet = []
            for item in params.get("AccountVpcSet"):
                obj = AccountVpcInfoOutput()
                obj._deserialize(item)
                self._AccountVpcSet.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyRecordsStatusRequest(AbstractModel):
    """ModifyRecordsStatus request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: The private domain ID
        :type ZoneId: str
        :param _RecordIds: The DNS record IDs.
        :type RecordIds: list of int
        :param _Status: `enabled`: Enable; `disabled`: Disable.
        :type Status: str
        """
        self._ZoneId = None
        self._RecordIds = None
        self._Status = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RecordIds(self):
        return self._RecordIds

    @RecordIds.setter
    def RecordIds(self, RecordIds):
        self._RecordIds = RecordIds

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RecordIds = params.get("RecordIds")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordsStatusResponse(AbstractModel):
    """ModifyRecordsStatus response structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: The private domain ID
        :type ZoneId: str
        :param _RecordIds: The DNS record IDs.
        :type RecordIds: list of int
        :param _Status: `enabled`: Enabled; `disabled`: Disabled.
        :type Status: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ZoneId = None
        self._RecordIds = None
        self._Status = None
        self._RequestId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RecordIds(self):
        return self._RecordIds

    @RecordIds.setter
    def RecordIds(self, RecordIds):
        self._RecordIds = RecordIds

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RecordIds = params.get("RecordIds")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class PrivateDNSAccount(AbstractModel):
    """Private DNS account

    """

    def __init__(self):
        r"""
        :param _Uin: Root account UIN
        :type Uin: str
        :param _Account: Root account name
        :type Account: str
        :param _Nickname: Account name
        :type Nickname: str
        """
        self._Uin = None
        self._Account = None
        self._Nickname = None

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Account(self):
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def Nickname(self):
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._Account = params.get("Account")
        self._Nickname = params.get("Nickname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
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
        :param _ServiceStatus: Private DNS service activation status
        :type ServiceStatus: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ServiceStatus = None
        self._RequestId = None

    @property
    def ServiceStatus(self):
        return self._ServiceStatus

    @ServiceStatus.setter
    def ServiceStatus(self, ServiceStatus):
        self._ServiceStatus = ServiceStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ServiceStatus = params.get("ServiceStatus")
        self._RequestId = params.get("RequestId")


class TagInfo(AbstractModel):
    """Tag

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
        :type TagKey: str
        :param _TagValue: Tag value
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TldQuota(AbstractModel):
    """TLD quota

    """

    def __init__(self):
        r"""
        :param _Total: Total quota
        :type Total: int
        :param _Used: Used quota
        :type Used: int
        :param _Stock: Available quota
        :type Stock: int
        :param _Quota: User’s quota
        :type Quota: int
        """
        self._Total = None
        self._Used = None
        self._Stock = None
        self._Quota = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Used(self):
        return self._Used

    @Used.setter
    def Used(self, Used):
        self._Used = Used

    @property
    def Stock(self):
        return self._Stock

    @Stock.setter
    def Stock(self, Stock):
        self._Stock = Stock

    @property
    def Quota(self):
        return self._Quota

    @Quota.setter
    def Quota(self, Quota):
        self._Quota = Quota


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._Used = params.get("Used")
        self._Stock = params.get("Stock")
        self._Quota = params.get("Quota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcInfo(AbstractModel):
    """VPC information

    """

    def __init__(self):
        r"""
        :param _UniqVpcId: VpcId: vpc-xadsafsdasd
        :type UniqVpcId: str
        :param _Region: VPC region: ap-guangzhou, ap-shanghai
        :type Region: str
        """
        self._UniqVpcId = None
        self._Region = None

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._UniqVpcId = params.get("UniqVpcId")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        