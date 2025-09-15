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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AccountVpcInfo(AbstractModel):
    r"""VPC information of a Private DNS account

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
        r"""VpcId: vpc-xadsafsdasd
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Region(self):
        r"""VPC region: ap-guangzhou, ap-shanghai
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Uin(self):
        r"""VPC account: 123456789
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def VpcName(self):
        r"""VPC name: testname
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
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
    r"""Output parameters of the associated VPC

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
        r"""VpcId: vpc-xadsafsdasd
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Region(self):
        r"""Region: ap-guangzhou, ap-shanghai
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Uin(self):
        r"""VPC ID: 123456789
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def VpcName(self):
        r"""VPC name: testname
        :rtype: str
        """
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
    r"""Output parameters of the associated VPC

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
        r"""UIN of the VPC account
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def UniqVpcId(self):
        r"""VPC ID
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Region(self):
        r"""Region
        :rtype: str
        """
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
    r"""Operation log

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
        r"""Log type
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Metric(self):
        r"""Log table name
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def TotalCount(self):
        r"""Total number of logs
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DataSet(self):
        r"""List of logs
        :rtype: list of AuditLogInfo
        """
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
    r"""Log details

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
        r"""Time
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def OperatorUin(self):
        r"""Operator UIN
        :rtype: str
        """
        return self._OperatorUin

    @OperatorUin.setter
    def OperatorUin(self, OperatorUin):
        self._OperatorUin = OperatorUin

    @property
    def Content(self):
        r"""Log content
        :rtype: str
        """
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
        


class CreateEndPointAndEndPointServiceRequest(AbstractModel):
    r"""CreateEndPointAndEndPointService request structure.

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC instance ID.
        :type VpcId: str
        :param _AutoAcceptFlag: Whether automatic forwarding is supported.
        :type AutoAcceptFlag: bool
        :param _ServiceInstanceId: Backend service ID.
        :type ServiceInstanceId: str
        :param _EndPointName: Endpoint name.
        :type EndPointName: str
        :param _EndPointRegion: Endpoint region, which should be consistent with the region of the endpoint service.
        :type EndPointRegion: str
        :param _EndPointServiceName: Endpoint service name.
        :type EndPointServiceName: str
        :param _ServiceType: Mounted PaaS service type. Valid values: CLB, CDB, and CRS.
        :type ServiceType: str
        :param _IpNum: Number of endpoint IP addresses.
        :type IpNum: int
        """
        self._VpcId = None
        self._AutoAcceptFlag = None
        self._ServiceInstanceId = None
        self._EndPointName = None
        self._EndPointRegion = None
        self._EndPointServiceName = None
        self._ServiceType = None
        self._IpNum = None

    @property
    def VpcId(self):
        r"""VPC instance ID.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def AutoAcceptFlag(self):
        r"""Whether automatic forwarding is supported.
        :rtype: bool
        """
        return self._AutoAcceptFlag

    @AutoAcceptFlag.setter
    def AutoAcceptFlag(self, AutoAcceptFlag):
        self._AutoAcceptFlag = AutoAcceptFlag

    @property
    def ServiceInstanceId(self):
        r"""Backend service ID.
        :rtype: str
        """
        return self._ServiceInstanceId

    @ServiceInstanceId.setter
    def ServiceInstanceId(self, ServiceInstanceId):
        self._ServiceInstanceId = ServiceInstanceId

    @property
    def EndPointName(self):
        r"""Endpoint name.
        :rtype: str
        """
        return self._EndPointName

    @EndPointName.setter
    def EndPointName(self, EndPointName):
        self._EndPointName = EndPointName

    @property
    def EndPointRegion(self):
        r"""Endpoint region, which should be consistent with the region of the endpoint service.
        :rtype: str
        """
        return self._EndPointRegion

    @EndPointRegion.setter
    def EndPointRegion(self, EndPointRegion):
        self._EndPointRegion = EndPointRegion

    @property
    def EndPointServiceName(self):
        r"""Endpoint service name.
        :rtype: str
        """
        return self._EndPointServiceName

    @EndPointServiceName.setter
    def EndPointServiceName(self, EndPointServiceName):
        self._EndPointServiceName = EndPointServiceName

    @property
    def ServiceType(self):
        r"""Mounted PaaS service type. Valid values: CLB, CDB, and CRS.
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def IpNum(self):
        r"""Number of endpoint IP addresses.
        :rtype: int
        """
        return self._IpNum

    @IpNum.setter
    def IpNum(self, IpNum):
        self._IpNum = IpNum


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._AutoAcceptFlag = params.get("AutoAcceptFlag")
        self._ServiceInstanceId = params.get("ServiceInstanceId")
        self._EndPointName = params.get("EndPointName")
        self._EndPointRegion = params.get("EndPointRegion")
        self._EndPointServiceName = params.get("EndPointServiceName")
        self._ServiceType = params.get("ServiceType")
        self._IpNum = params.get("IpNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEndPointAndEndPointServiceResponse(AbstractModel):
    r"""CreateEndPointAndEndPointService response structure.

    """

    def __init__(self):
        r"""
        :param _EndPointId: Endpoint ID.
        :type EndPointId: str
        :param _EndPointName: Endpoint name.
        :type EndPointName: str
        :param _EndPointServiceId: Endpoint service ID.
        :type EndPointServiceId: str
        :param _EndPointVipSet: IP address list of the endpoint.
        :type EndPointVipSet: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EndPointId = None
        self._EndPointName = None
        self._EndPointServiceId = None
        self._EndPointVipSet = None
        self._RequestId = None

    @property
    def EndPointId(self):
        r"""Endpoint ID.
        :rtype: str
        """
        return self._EndPointId

    @EndPointId.setter
    def EndPointId(self, EndPointId):
        self._EndPointId = EndPointId

    @property
    def EndPointName(self):
        r"""Endpoint name.
        :rtype: str
        """
        return self._EndPointName

    @EndPointName.setter
    def EndPointName(self, EndPointName):
        self._EndPointName = EndPointName

    @property
    def EndPointServiceId(self):
        r"""Endpoint service ID.
        :rtype: str
        """
        return self._EndPointServiceId

    @EndPointServiceId.setter
    def EndPointServiceId(self, EndPointServiceId):
        self._EndPointServiceId = EndPointServiceId

    @property
    def EndPointVipSet(self):
        r"""IP address list of the endpoint.
        :rtype: list of str
        """
        return self._EndPointVipSet

    @EndPointVipSet.setter
    def EndPointVipSet(self, EndPointVipSet):
        self._EndPointVipSet = EndPointVipSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EndPointId = params.get("EndPointId")
        self._EndPointName = params.get("EndPointName")
        self._EndPointServiceId = params.get("EndPointServiceId")
        self._EndPointVipSet = params.get("EndPointVipSet")
        self._RequestId = params.get("RequestId")


class CreateEndPointRequest(AbstractModel):
    r"""CreateEndPoint request structure.

    """

    def __init__(self):
        r"""
        :param _EndPointName: Endpoint name.
        :type EndPointName: str
        :param _EndPointServiceId: Endpoint service ID (namely, VPC endpoint service ID).
        :type EndPointServiceId: str
        :param _EndPointRegion: Endpoint region, which should be consistent with the region of the endpoint service.
        :type EndPointRegion: str
        :param _IpNum: Number of endpoint IP addresses.
        :type IpNum: int
        """
        self._EndPointName = None
        self._EndPointServiceId = None
        self._EndPointRegion = None
        self._IpNum = None

    @property
    def EndPointName(self):
        r"""Endpoint name.
        :rtype: str
        """
        return self._EndPointName

    @EndPointName.setter
    def EndPointName(self, EndPointName):
        self._EndPointName = EndPointName

    @property
    def EndPointServiceId(self):
        r"""Endpoint service ID (namely, VPC endpoint service ID).
        :rtype: str
        """
        return self._EndPointServiceId

    @EndPointServiceId.setter
    def EndPointServiceId(self, EndPointServiceId):
        self._EndPointServiceId = EndPointServiceId

    @property
    def EndPointRegion(self):
        r"""Endpoint region, which should be consistent with the region of the endpoint service.
        :rtype: str
        """
        return self._EndPointRegion

    @EndPointRegion.setter
    def EndPointRegion(self, EndPointRegion):
        self._EndPointRegion = EndPointRegion

    @property
    def IpNum(self):
        r"""Number of endpoint IP addresses.
        :rtype: int
        """
        return self._IpNum

    @IpNum.setter
    def IpNum(self, IpNum):
        self._IpNum = IpNum


    def _deserialize(self, params):
        self._EndPointName = params.get("EndPointName")
        self._EndPointServiceId = params.get("EndPointServiceId")
        self._EndPointRegion = params.get("EndPointRegion")
        self._IpNum = params.get("IpNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEndPointResponse(AbstractModel):
    r"""CreateEndPoint response structure.

    """

    def __init__(self):
        r"""
        :param _EndPointId: Endpoint ID.
        :type EndPointId: str
        :param _EndPointName: Endpoint name.
        :type EndPointName: str
        :param _EndPointServiceId: Endpoint service ID.
        :type EndPointServiceId: str
        :param _EndPointVipSet: IP address list of the endpoint.
        :type EndPointVipSet: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EndPointId = None
        self._EndPointName = None
        self._EndPointServiceId = None
        self._EndPointVipSet = None
        self._RequestId = None

    @property
    def EndPointId(self):
        r"""Endpoint ID.
        :rtype: str
        """
        return self._EndPointId

    @EndPointId.setter
    def EndPointId(self, EndPointId):
        self._EndPointId = EndPointId

    @property
    def EndPointName(self):
        r"""Endpoint name.
        :rtype: str
        """
        return self._EndPointName

    @EndPointName.setter
    def EndPointName(self, EndPointName):
        self._EndPointName = EndPointName

    @property
    def EndPointServiceId(self):
        r"""Endpoint service ID.
        :rtype: str
        """
        return self._EndPointServiceId

    @EndPointServiceId.setter
    def EndPointServiceId(self, EndPointServiceId):
        self._EndPointServiceId = EndPointServiceId

    @property
    def EndPointVipSet(self):
        r"""IP address list of the endpoint.
        :rtype: list of str
        """
        return self._EndPointVipSet

    @EndPointVipSet.setter
    def EndPointVipSet(self, EndPointVipSet):
        self._EndPointVipSet = EndPointVipSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EndPointId = params.get("EndPointId")
        self._EndPointName = params.get("EndPointName")
        self._EndPointServiceId = params.get("EndPointServiceId")
        self._EndPointVipSet = params.get("EndPointVipSet")
        self._RequestId = params.get("RequestId")


class CreateExtendEndpointRequest(AbstractModel):
    r"""CreateExtendEndpoint request structure.

    """

    def __init__(self):
        r"""
        :param _EndpointName: Outbound endpoint name.
        :type EndpointName: str
        :param _EndpointRegion: The region of the outbound endpoint must be consistent with the region of the forwarding target VIP.
        :type EndpointRegion: str
        :param _ForwardIp: Forwarding target.
        :type ForwardIp: :class:`tencentcloud.privatedns.v20201028.models.ForwardIp`
        """
        self._EndpointName = None
        self._EndpointRegion = None
        self._ForwardIp = None

    @property
    def EndpointName(self):
        r"""Outbound endpoint name.
        :rtype: str
        """
        return self._EndpointName

    @EndpointName.setter
    def EndpointName(self, EndpointName):
        self._EndpointName = EndpointName

    @property
    def EndpointRegion(self):
        r"""The region of the outbound endpoint must be consistent with the region of the forwarding target VIP.
        :rtype: str
        """
        return self._EndpointRegion

    @EndpointRegion.setter
    def EndpointRegion(self, EndpointRegion):
        self._EndpointRegion = EndpointRegion

    @property
    def ForwardIp(self):
        r"""Forwarding target.
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.ForwardIp`
        """
        return self._ForwardIp

    @ForwardIp.setter
    def ForwardIp(self, ForwardIp):
        self._ForwardIp = ForwardIp


    def _deserialize(self, params):
        self._EndpointName = params.get("EndpointName")
        self._EndpointRegion = params.get("EndpointRegion")
        if params.get("ForwardIp") is not None:
            self._ForwardIp = ForwardIp()
            self._ForwardIp._deserialize(params.get("ForwardIp"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateExtendEndpointResponse(AbstractModel):
    r"""CreateExtendEndpoint response structure.

    """

    def __init__(self):
        r"""
        :param _EndpointId: Endpoint ID.
        :type EndpointId: str
        :param _EndpointName: Endpoint name.
        :type EndpointName: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EndpointId = None
        self._EndpointName = None
        self._RequestId = None

    @property
    def EndpointId(self):
        r"""Endpoint ID.
        :rtype: str
        """
        return self._EndpointId

    @EndpointId.setter
    def EndpointId(self, EndpointId):
        self._EndpointId = EndpointId

    @property
    def EndpointName(self):
        r"""Endpoint name.
        :rtype: str
        """
        return self._EndpointName

    @EndpointName.setter
    def EndpointName(self, EndpointName):
        self._EndpointName = EndpointName

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EndpointId = params.get("EndpointId")
        self._EndpointName = params.get("EndpointName")
        self._RequestId = params.get("RequestId")


class CreateForwardRuleRequest(AbstractModel):
    r"""CreateForwardRule request structure.

    """

    def __init__(self):
        r"""
        :param _RuleName: Forwarding rule name.
        :type RuleName: str
        :param _RuleType: Forwarding rule type. DOWN: From cloud to off-cloud; UP: From off-cloud to cloud.
        :type RuleType: str
        :param _ZoneId: Private domain ID, which can be viewed on the private domain list page.
        :type ZoneId: str
        :param _EndPointId: Endpoint ID.
        :type EndPointId: str
        """
        self._RuleName = None
        self._RuleType = None
        self._ZoneId = None
        self._EndPointId = None

    @property
    def RuleName(self):
        r"""Forwarding rule name.
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RuleType(self):
        r"""Forwarding rule type. DOWN: From cloud to off-cloud; UP: From off-cloud to cloud.
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def ZoneId(self):
        r"""Private domain ID, which can be viewed on the private domain list page.
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def EndPointId(self):
        r"""Endpoint ID.
        :rtype: str
        """
        return self._EndPointId

    @EndPointId.setter
    def EndPointId(self, EndPointId):
        self._EndPointId = EndPointId


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        self._RuleType = params.get("RuleType")
        self._ZoneId = params.get("ZoneId")
        self._EndPointId = params.get("EndPointId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateForwardRuleResponse(AbstractModel):
    r"""CreateForwardRule response structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: Forwarding rule ID.
        :type RuleId: str
        :param _RuleName: Forwarding rule name.
        :type RuleName: str
        :param _RuleType: Forwarding rule type.
        :type RuleType: str
        :param _ZoneId: Private domain ID.
        :type ZoneId: str
        :param _EndPointId: Endpoint ID.
        :type EndPointId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleId = None
        self._RuleName = None
        self._RuleType = None
        self._ZoneId = None
        self._EndPointId = None
        self._RequestId = None

    @property
    def RuleId(self):
        r"""Forwarding rule ID.
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        r"""Forwarding rule name.
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RuleType(self):
        r"""Forwarding rule type.
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def ZoneId(self):
        r"""Private domain ID.
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def EndPointId(self):
        r"""Endpoint ID.
        :rtype: str
        """
        return self._EndPointId

    @EndPointId.setter
    def EndPointId(self, EndPointId):
        self._EndPointId = EndPointId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._RuleType = params.get("RuleType")
        self._ZoneId = params.get("ZoneId")
        self._EndPointId = params.get("EndPointId")
        self._RequestId = params.get("RequestId")


class CreatePrivateDNSAccountRequest(AbstractModel):
    r"""CreatePrivateDNSAccount request structure.

    """

    def __init__(self):
        r"""
        :param _Account: Private DNS account
        :type Account: :class:`tencentcloud.privatedns.v20201028.models.PrivateDNSAccount`
        """
        self._Account = None

    @property
    def Account(self):
        r"""Private DNS account
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.PrivateDNSAccount`
        """
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
    r"""CreatePrivateDNSAccount response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreatePrivateZoneRecordRequest(AbstractModel):
    r"""CreatePrivateZoneRecord request structure.

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
        r"""Private domain ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RecordType(self):
        r"""Record type. Valid values: "A", "AAAA", "CNAME", "MX", "TXT", "PTR"
        :rtype: str
        """
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def SubDomain(self):
        r"""Subdomain, such as "www", "m", and "@"
        :rtype: str
        """
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordValue(self):
        r"""Record value, such as IP: 192.168.10.2, CNAME: cname.qcloud.com., and MX: mail.qcloud.com.
        :rtype: str
        """
        return self._RecordValue

    @RecordValue.setter
    def RecordValue(self, RecordValue):
        self._RecordValue = RecordValue

    @property
    def Weight(self):
        r"""Record weight. Value range: 1–100
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def MX(self):
        r"""MX priority, which is required when the record type is MX. Valid values: 5, 10, 15, 20, 30, 40, 50
        :rtype: int
        """
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX

    @property
    def TTL(self):
        r"""Record cache time. The smaller the value, the faster the record will take effect. Value range: 1–86400s. Default value: 600
        :rtype: int
        """
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
    r"""CreatePrivateZoneRecord response structure.

    """

    def __init__(self):
        r"""
        :param _RecordId: Record ID
        :type RecordId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RecordId = None
        self._RequestId = None

    @property
    def RecordId(self):
        r"""Record ID
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RecordId = params.get("RecordId")
        self._RequestId = params.get("RequestId")


class CreatePrivateZoneRequest(AbstractModel):
    r"""CreatePrivateZone request structure.

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
        r"""Domain name, which must be in the format of standard TLD
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def TagSet(self):
        r"""Tags the private domain when it is created
        :rtype: list of TagInfo
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def VpcSet(self):
        r"""Associates the private domain to a VPC when it is created
        :rtype: list of VpcInfo
        """
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

    @property
    def Remark(self):
        r"""Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def DnsForwardStatus(self):
        r"""Whether to enable subdomain recursive DNS. Valid values: `ENABLED` (default) and `DISABLED`.
        :rtype: str
        """
        return self._DnsForwardStatus

    @DnsForwardStatus.setter
    def DnsForwardStatus(self, DnsForwardStatus):
        self._DnsForwardStatus = DnsForwardStatus

    @property
    def Vpcs(self):
        warnings.warn("parameter `Vpcs` is deprecated", DeprecationWarning) 

        r"""Associates the private domain to a VPC when it is created
        :rtype: list of VpcInfo
        """
        return self._Vpcs

    @Vpcs.setter
    def Vpcs(self, Vpcs):
        warnings.warn("parameter `Vpcs` is deprecated", DeprecationWarning) 

        self._Vpcs = Vpcs

    @property
    def AccountVpcSet(self):
        r"""List of authorized accounts' VPCs to associate with the private domain
        :rtype: list of AccountVpcInfo
        """
        return self._AccountVpcSet

    @AccountVpcSet.setter
    def AccountVpcSet(self, AccountVpcSet):
        self._AccountVpcSet = AccountVpcSet

    @property
    def CnameSpeedupStatus(self):
        r"""Whether to enable CNAME flattening. Valid values: `ENABLED` (default) and `DISABLED`.
        :rtype: str
        """
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
    r"""CreatePrivateZone response structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Private domain ID, such as zone-xxxxxx
        :type ZoneId: str
        :param _Domain: Private domain
        :type Domain: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ZoneId = None
        self._Domain = None
        self._RequestId = None

    @property
    def ZoneId(self):
        r"""Private domain ID, such as zone-xxxxxx
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Domain(self):
        r"""Private domain
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Domain = params.get("Domain")
        self._RequestId = params.get("RequestId")


class DatePoint(AbstractModel):
    r"""Time statistics

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
        r"""Time
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Value(self):
        r"""Value
        :rtype: int
        """
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
        


class DeleteEndPointRequest(AbstractModel):
    r"""DeleteEndPoint request structure.

    """

    def __init__(self):
        r"""
        :param _EndPointId: Endpoint ID.
        :type EndPointId: str
        """
        self._EndPointId = None

    @property
    def EndPointId(self):
        r"""Endpoint ID.
        :rtype: str
        """
        return self._EndPointId

    @EndPointId.setter
    def EndPointId(self, EndPointId):
        self._EndPointId = EndPointId


    def _deserialize(self, params):
        self._EndPointId = params.get("EndPointId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEndPointResponse(AbstractModel):
    r"""DeleteEndPoint response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteForwardRuleRequest(AbstractModel):
    r"""DeleteForwardRule request structure.

    """

    def __init__(self):
        r"""
        :param _RuleIdSet: Array of forwarding rule IDs.
        :type RuleIdSet: list of str
        """
        self._RuleIdSet = None

    @property
    def RuleIdSet(self):
        r"""Array of forwarding rule IDs.
        :rtype: list of str
        """
        return self._RuleIdSet

    @RuleIdSet.setter
    def RuleIdSet(self, RuleIdSet):
        self._RuleIdSet = RuleIdSet


    def _deserialize(self, params):
        self._RuleIdSet = params.get("RuleIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteForwardRuleResponse(AbstractModel):
    r"""DeleteForwardRule response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeletePrivateZoneRecordRequest(AbstractModel):
    r"""DeletePrivateZoneRecord request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Private domain ID
        :type ZoneId: str
        :param _RecordId: Record ID
        :type RecordId: str
        :param _RecordIdSet: Array of record IDs. `RecordId` takes precedence.
        :type RecordIdSet: list of str
        """
        self._ZoneId = None
        self._RecordId = None
        self._RecordIdSet = None

    @property
    def ZoneId(self):
        r"""Private domain ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RecordId(self):
        r"""Record ID
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def RecordIdSet(self):
        r"""Array of record IDs. `RecordId` takes precedence.
        :rtype: list of str
        """
        return self._RecordIdSet

    @RecordIdSet.setter
    def RecordIdSet(self, RecordIdSet):
        self._RecordIdSet = RecordIdSet


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RecordId = params.get("RecordId")
        self._RecordIdSet = params.get("RecordIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrivateZoneRecordResponse(AbstractModel):
    r"""DeletePrivateZoneRecord response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAccountVpcListRequest(AbstractModel):
    r"""DescribeAccountVpcList request structure.

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
        r"""UIN of account
        :rtype: str
        """
        return self._AccountUin

    @AccountUin.setter
    def AccountUin(self, AccountUin):
        self._AccountUin = AccountUin

    @property
    def Offset(self):
        r"""Pagination offset, starting from 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of entries per page. Maximum value: `100`. Default value: `20`
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""Filter parameters
        :rtype: list of Filter
        """
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
    r"""DescribeAccountVpcList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of VPCs
        :type TotalCount: int
        :param _VpcSet: VPC list
        :type VpcSet: list of AccountVpcInfoOut
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._VpcSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of VPCs
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VpcSet(self):
        r"""VPC list
        :rtype: list of AccountVpcInfoOut
        """
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
    r"""DescribeAuditLog request structure.

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
        r"""Request volume statistics start time
        :rtype: str
        """
        return self._TimeRangeBegin

    @TimeRangeBegin.setter
    def TimeRangeBegin(self, TimeRangeBegin):
        self._TimeRangeBegin = TimeRangeBegin

    @property
    def Filters(self):
        r"""Filter parameter. Valid values: ZoneId (private domain ID), Domain (private domain), OperatorUin (operator account ID)
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TimeRangeEnd(self):
        r"""Request volume statistics end time
        :rtype: str
        """
        return self._TimeRangeEnd

    @TimeRangeEnd.setter
    def TimeRangeEnd(self, TimeRangeEnd):
        self._TimeRangeEnd = TimeRangeEnd

    @property
    def Offset(self):
        r"""Pagination offset, starting from 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of entries per page. Maximum value: 100. Default value: 20
        :rtype: int
        """
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
    r"""DescribeAuditLog response structure.

    """

    def __init__(self):
        r"""
        :param _Data: List of operation logs
        :type Data: list of AuditLog
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""List of operation logs
        :rtype: list of AuditLog
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
    r"""DescribeDashboard request structure.

    """


class DescribeDashboardResponse(AbstractModel):
    r"""DescribeDashboard response structure.

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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ZoneTotal = None
        self._ZoneVpcCount = None
        self._RequestTotalCount = None
        self._FlowUsage = None
        self._RequestId = None

    @property
    def ZoneTotal(self):
        r"""Total number of private domain DNS records
        :rtype: int
        """
        return self._ZoneTotal

    @ZoneTotal.setter
    def ZoneTotal(self, ZoneTotal):
        self._ZoneTotal = ZoneTotal

    @property
    def ZoneVpcCount(self):
        r"""Number of VPCs associated with private domain
        :rtype: int
        """
        return self._ZoneVpcCount

    @ZoneVpcCount.setter
    def ZoneVpcCount(self, ZoneVpcCount):
        self._ZoneVpcCount = ZoneVpcCount

    @property
    def RequestTotalCount(self):
        r"""Total number of historical requests
        :rtype: int
        """
        return self._RequestTotalCount

    @RequestTotalCount.setter
    def RequestTotalCount(self, RequestTotalCount):
        self._RequestTotalCount = RequestTotalCount

    @property
    def FlowUsage(self):
        r"""Traffic package usage
        :rtype: list of FlowUsage
        """
        return self._FlowUsage

    @FlowUsage.setter
    def FlowUsage(self, FlowUsage):
        self._FlowUsage = FlowUsage

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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


class DescribeEndPointListRequest(AbstractModel):
    r"""DescribeEndPointList request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Pagination offset, starting from 0.
        :type Offset: int
        :param _Limit: Pagination limit. Maximum value: 100. Default value: 20.
        :type Limit: int
        :param _Filters: Filter parameters. Valid values: EndPointName, EndPointId, EndPointServiceId, and EndPointVip.
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        r"""Pagination offset, starting from 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Pagination limit. Maximum value: 100. Default value: 20.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""Filter parameters. Valid values: EndPointName, EndPointId, EndPointServiceId, and EndPointVip.
        :rtype: list of Filter
        """
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
        


class DescribeEndPointListResponse(AbstractModel):
    r"""DescribeEndPointList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of endpoints.
        :type TotalCount: int
        :param _EndPointSet: Endpoint list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndPointSet: list of EndPointInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._EndPointSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of endpoints.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def EndPointSet(self):
        r"""Endpoint list.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of EndPointInfo
        """
        return self._EndPointSet

    @EndPointSet.setter
    def EndPointSet(self, EndPointSet):
        self._EndPointSet = EndPointSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("EndPointSet") is not None:
            self._EndPointSet = []
            for item in params.get("EndPointSet"):
                obj = EndPointInfo()
                obj._deserialize(item)
                self._EndPointSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEndPointRegionRequest(AbstractModel):
    r"""DescribeEndPointRegion request structure.

    """


class DescribeEndPointRegionResponse(AbstractModel):
    r"""DescribeEndPointRegion response structure.

    """

    def __init__(self):
        r"""
        :param _RegionSet: Region array.
        :type RegionSet: list of RegionInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RegionSet = None
        self._RequestId = None

    @property
    def RegionSet(self):
        r"""Region array.
        :rtype: list of RegionInfo
        """
        return self._RegionSet

    @RegionSet.setter
    def RegionSet(self, RegionSet):
        self._RegionSet = RegionSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RegionSet") is not None:
            self._RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self._RegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeExtendEndpointListRequest(AbstractModel):
    r"""DescribeExtendEndpointList request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Pagination offset, starting from 0.
        :type Offset: int
        :param _Limit: Pagination limit. Maximum value: 100. Default value: 20.
        :type Limit: int
        :param _Filters: Filter parameters. Valid values: EndpointName, EndpointId.
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        r"""Pagination offset, starting from 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Pagination limit. Maximum value: 100. Default value: 20.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""Filter parameters. Valid values: EndpointName, EndpointId.
        :rtype: list of Filter
        """
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
        


class DescribeExtendEndpointListResponse(AbstractModel):
    r"""DescribeExtendEndpointList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of endpoints.
        :type TotalCount: int
        :param _OutboundEndpointSet: Endpoint list.
        :type OutboundEndpointSet: list of OutboundEndpoint
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._OutboundEndpointSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of endpoints.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def OutboundEndpointSet(self):
        r"""Endpoint list.
        :rtype: list of OutboundEndpoint
        """
        return self._OutboundEndpointSet

    @OutboundEndpointSet.setter
    def OutboundEndpointSet(self, OutboundEndpointSet):
        self._OutboundEndpointSet = OutboundEndpointSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("OutboundEndpointSet") is not None:
            self._OutboundEndpointSet = []
            for item in params.get("OutboundEndpointSet"):
                obj = OutboundEndpoint()
                obj._deserialize(item)
                self._OutboundEndpointSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeForwardRuleListRequest(AbstractModel):
    r"""DescribeForwardRuleList request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Pagination offset, starting from 0.
        :type Offset: int
        :param _Limit: Pagination limit. Maximum value: 100. Default value: 20.
        :type Limit: int
        :param _Filters: Filter parameters.
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        r"""Pagination offset, starting from 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Pagination limit. Maximum value: 100. Default value: 20.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""Filter parameters.
        :rtype: list of Filter
        """
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
        


class DescribeForwardRuleListResponse(AbstractModel):
    r"""DescribeForwardRuleList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of private domains.
        :type TotalCount: int
        :param _ForwardRuleSet: Private domain list.
        :type ForwardRuleSet: list of ForwardRule
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ForwardRuleSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of private domains.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ForwardRuleSet(self):
        r"""Private domain list.
        :rtype: list of ForwardRule
        """
        return self._ForwardRuleSet

    @ForwardRuleSet.setter
    def ForwardRuleSet(self, ForwardRuleSet):
        self._ForwardRuleSet = ForwardRuleSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ForwardRuleSet") is not None:
            self._ForwardRuleSet = []
            for item in params.get("ForwardRuleSet"):
                obj = ForwardRule()
                obj._deserialize(item)
                self._ForwardRuleSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeForwardRuleRequest(AbstractModel):
    r"""DescribeForwardRule request structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: Forwarding rule ID.
        :type RuleId: str
        """
        self._RuleId = None

    @property
    def RuleId(self):
        r"""Forwarding rule ID.
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeForwardRuleResponse(AbstractModel):
    r"""DescribeForwardRule response structure.

    """

    def __init__(self):
        r"""
        :param _ForwardRule: Forwarding rule details.
        :type ForwardRule: :class:`tencentcloud.privatedns.v20201028.models.ForwardRule`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ForwardRule = None
        self._RequestId = None

    @property
    def ForwardRule(self):
        r"""Forwarding rule details.
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.ForwardRule`
        """
        return self._ForwardRule

    @ForwardRule.setter
    def ForwardRule(self, ForwardRule):
        self._ForwardRule = ForwardRule

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ForwardRule") is not None:
            self._ForwardRule = ForwardRule()
            self._ForwardRule._deserialize(params.get("ForwardRule"))
        self._RequestId = params.get("RequestId")


class DescribePrivateDNSAccountListRequest(AbstractModel):
    r"""DescribePrivateDNSAccountList request structure.

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
        r"""Pagination offset, starting from `0`
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of entries per page. Maximum value: `100`. Default value: `20`
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""Filter parameters
        :rtype: list of Filter
        """
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
    r"""DescribePrivateDNSAccountList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of Private DNS accounts
        :type TotalCount: int
        :param _AccountSet: List of Private DNS accounts
        :type AccountSet: list of PrivateDNSAccount
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._AccountSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of Private DNS accounts
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AccountSet(self):
        r"""List of Private DNS accounts
        :rtype: list of PrivateDNSAccount
        """
        return self._AccountSet

    @AccountSet.setter
    def AccountSet(self, AccountSet):
        self._AccountSet = AccountSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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


class DescribePrivateZoneListRequest(AbstractModel):
    r"""DescribePrivateZoneList request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Pagination offset, starting from 0.
        :type Offset: int
        :param _Limit: Pagination limit. Maximum value: 100. Default value: 20.
        :type Limit: int
        :param _Filters: Filter parameters.
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        r"""Pagination offset, starting from 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Pagination limit. Maximum value: 100. Default value: 20.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""Filter parameters.
        :rtype: list of Filter
        """
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
        


class DescribePrivateZoneListResponse(AbstractModel):
    r"""DescribePrivateZoneList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of private domains.
        :type TotalCount: int
        :param _PrivateZoneSet: Private domain list.
        :type PrivateZoneSet: list of PrivateZone
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._PrivateZoneSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of private domains.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PrivateZoneSet(self):
        r"""Private domain list.
        :rtype: list of PrivateZone
        """
        return self._PrivateZoneSet

    @PrivateZoneSet.setter
    def PrivateZoneSet(self, PrivateZoneSet):
        self._PrivateZoneSet = PrivateZoneSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("PrivateZoneSet") is not None:
            self._PrivateZoneSet = []
            for item in params.get("PrivateZoneSet"):
                obj = PrivateZone()
                obj._deserialize(item)
                self._PrivateZoneSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrivateZoneRecordListRequest(AbstractModel):
    r"""DescribePrivateZoneRecordList request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Private domain ID: zone-xxxxxx
        :type ZoneId: str
        :param _Filters: Filter parameter
        :type Filters: list of Filter
        :param _Offset: Pagination offset, starting from 0
        :type Offset: int
        :param _Limit: Number of entries per page. Maximum value: 100. Default value: 20
        :type Limit: int
        """
        self._ZoneId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ZoneId(self):
        r"""Private domain ID: zone-xxxxxx
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Filters(self):
        r"""Filter parameter
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""Pagination offset, starting from 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of entries per page. Maximum value: 100. Default value: 20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrivateZoneRecordListResponse(AbstractModel):
    r"""DescribePrivateZoneRecordList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of DNS records
        :type TotalCount: int
        :param _RecordSet: List of DNS records
        :type RecordSet: list of PrivateZoneRecord
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RecordSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of DNS records
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RecordSet(self):
        r"""List of DNS records
        :rtype: list of PrivateZoneRecord
        """
        return self._RecordSet

    @RecordSet.setter
    def RecordSet(self, RecordSet):
        self._RecordSet = RecordSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RecordSet") is not None:
            self._RecordSet = []
            for item in params.get("RecordSet"):
                obj = PrivateZoneRecord()
                obj._deserialize(item)
                self._RecordSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrivateZoneServiceRequest(AbstractModel):
    r"""DescribePrivateZoneService request structure.

    """


class DescribePrivateZoneServiceResponse(AbstractModel):
    r"""DescribePrivateZoneService response structure.

    """

    def __init__(self):
        r"""
        :param _ServiceStatus: Private DNS service activation status. Valid values: ENABLED, DISABLED
        :type ServiceStatus: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ServiceStatus = None
        self._RequestId = None

    @property
    def ServiceStatus(self):
        r"""Private DNS service activation status. Valid values: ENABLED, DISABLED
        :rtype: str
        """
        return self._ServiceStatus

    @ServiceStatus.setter
    def ServiceStatus(self, ServiceStatus):
        self._ServiceStatus = ServiceStatus

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ServiceStatus = params.get("ServiceStatus")
        self._RequestId = params.get("RequestId")


class DescribeQuotaUsageRequest(AbstractModel):
    r"""DescribeQuotaUsage request structure.

    """


class DescribeQuotaUsageResponse(AbstractModel):
    r"""DescribeQuotaUsage response structure.

    """

    def __init__(self):
        r"""
        :param _TldQuota: TLD quota usage
        :type TldQuota: :class:`tencentcloud.privatedns.v20201028.models.TldQuota`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TldQuota = None
        self._RequestId = None

    @property
    def TldQuota(self):
        r"""TLD quota usage
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.TldQuota`
        """
        return self._TldQuota

    @TldQuota.setter
    def TldQuota(self, TldQuota):
        self._TldQuota = TldQuota

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TldQuota") is not None:
            self._TldQuota = TldQuota()
            self._TldQuota._deserialize(params.get("TldQuota"))
        self._RequestId = params.get("RequestId")


class DescribeRecordRequest(AbstractModel):
    r"""DescribeRecord request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Private domain ID.
        :type ZoneId: str
        :param _RecordId: Record ID
        :type RecordId: str
        """
        self._ZoneId = None
        self._RecordId = None

    @property
    def ZoneId(self):
        r"""Private domain ID.
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RecordId(self):
        r"""Record ID
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RecordId = params.get("RecordId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordResponse(AbstractModel):
    r"""DescribeRecord response structure.

    """

    def __init__(self):
        r"""
        :param _RecordInfo: Record information.
        :type RecordInfo: :class:`tencentcloud.privatedns.v20201028.models.RecordInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RecordInfo = None
        self._RequestId = None

    @property
    def RecordInfo(self):
        r"""Record information.
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.RecordInfo`
        """
        return self._RecordInfo

    @RecordInfo.setter
    def RecordInfo(self, RecordInfo):
        self._RecordInfo = RecordInfo

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RecordInfo") is not None:
            self._RecordInfo = RecordInfo()
            self._RecordInfo._deserialize(params.get("RecordInfo"))
        self._RequestId = params.get("RequestId")


class DescribeRequestDataRequest(AbstractModel):
    r"""DescribeRequestData request structure.

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
        r"""Request volume statistics start time in the format of 2020-11-22 00:00:00
        :rtype: str
        """
        return self._TimeRangeBegin

    @TimeRangeBegin.setter
    def TimeRangeBegin(self, TimeRangeBegin):
        self._TimeRangeBegin = TimeRangeBegin

    @property
    def Filters(self):
        r"""Filter parameter:
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TimeRangeEnd(self):
        r"""Request volume statistics end time in the format of 2020-11-22 23:59:59
        :rtype: str
        """
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
    r"""DescribeRequestData response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Request volume statistics table
        :type Data: list of MetricData
        :param _Interval: Request volume unit time. Valid values: Day, Hour
        :type Interval: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Interval = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Request volume statistics table
        :rtype: list of MetricData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Interval(self):
        r"""Request volume unit time. Valid values: Day, Hour
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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


class EndPointInfo(AbstractModel):
    r"""Endpoint information.

    """

    def __init__(self):
        r"""
        :param _EndPointId: Endpoint ID.
        :type EndPointId: str
        :param _EndPointName: Endpoint name.
        :type EndPointName: str
        :param _EndPointServiceId: Endpoint service ID.
        :type EndPointServiceId: str
        :param _EndPointVipSet: VIP list of the endpoint.
        :type EndPointVipSet: list of str
        :param _RegionCode: ap-guangzhou
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionCode: str
        :param _Tags: Tag key-value pair collection.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of TagInfo
        """
        self._EndPointId = None
        self._EndPointName = None
        self._EndPointServiceId = None
        self._EndPointVipSet = None
        self._RegionCode = None
        self._Tags = None

    @property
    def EndPointId(self):
        r"""Endpoint ID.
        :rtype: str
        """
        return self._EndPointId

    @EndPointId.setter
    def EndPointId(self, EndPointId):
        self._EndPointId = EndPointId

    @property
    def EndPointName(self):
        r"""Endpoint name.
        :rtype: str
        """
        return self._EndPointName

    @EndPointName.setter
    def EndPointName(self, EndPointName):
        self._EndPointName = EndPointName

    @property
    def EndPointServiceId(self):
        r"""Endpoint service ID.
        :rtype: str
        """
        return self._EndPointServiceId

    @EndPointServiceId.setter
    def EndPointServiceId(self, EndPointServiceId):
        self._EndPointServiceId = EndPointServiceId

    @property
    def EndPointVipSet(self):
        r"""VIP list of the endpoint.
        :rtype: list of str
        """
        return self._EndPointVipSet

    @EndPointVipSet.setter
    def EndPointVipSet(self, EndPointVipSet):
        self._EndPointVipSet = EndPointVipSet

    @property
    def RegionCode(self):
        r"""ap-guangzhou
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RegionCode

    @RegionCode.setter
    def RegionCode(self, RegionCode):
        self._RegionCode = RegionCode

    @property
    def Tags(self):
        r"""Tag key-value pair collection.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._EndPointId = params.get("EndPointId")
        self._EndPointName = params.get("EndPointName")
        self._EndPointServiceId = params.get("EndPointServiceId")
        self._EndPointVipSet = params.get("EndPointVipSet")
        self._RegionCode = params.get("RegionCode")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EndpointService(AbstractModel):
    r"""PrivateDNS outbound endpoint forwarding IP

    """

    def __init__(self):
        r"""
        :param _AccessType: Specifies the forwarding target IP network access type.
CLB: Specifies that the forwarding IP is the private CLB VIP.
CCN: Specifies forwarding IP through CCN routing.
        :type AccessType: str
        :param _Pip: Specifies the forwarding target IP address.
        :type Pip: str
        :param _Pport: Specifies the forwarding IP port number.
        :type Pport: int
        :param _VpcId: Specifies the unique VPC ID.
        :type VpcId: str
        :param _Vip: Specifies the forwarding target IP proxy IP.
        :type Vip: str
        :param _Vport: Specifies the forwarding target IP proxy port.
        :type Vport: int
        :param _Proto: Specifies the forwarding target IP protocol.
        :type Proto: str
        :param _SubnetId: Specifies the unique subnet ID.
Required if the access type is CCN.
        :type SubnetId: str
        :param _AccessGatewayId: ccn id
Required if the access type is CCN.
        :type AccessGatewayId: str
        :param _SnatVipCidr: The SNAT CIDR block of the outbound endpoint.
        :type SnatVipCidr: str
        :param _SnatVipSet: The SNAT IP list of the outbound endpoint.
        :type SnatVipSet: str
        :param _Region: The region of the outbound endpoint service.
        :type Region: str
        """
        self._AccessType = None
        self._Pip = None
        self._Pport = None
        self._VpcId = None
        self._Vip = None
        self._Vport = None
        self._Proto = None
        self._SubnetId = None
        self._AccessGatewayId = None
        self._SnatVipCidr = None
        self._SnatVipSet = None
        self._Region = None

    @property
    def AccessType(self):
        r"""Specifies the forwarding target IP network access type.
CLB: Specifies that the forwarding IP is the private CLB VIP.
CCN: Specifies forwarding IP through CCN routing.
        :rtype: str
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def Pip(self):
        r"""Specifies the forwarding target IP address.
        :rtype: str
        """
        return self._Pip

    @Pip.setter
    def Pip(self, Pip):
        self._Pip = Pip

    @property
    def Pport(self):
        r"""Specifies the forwarding IP port number.
        :rtype: int
        """
        return self._Pport

    @Pport.setter
    def Pport(self, Pport):
        self._Pport = Pport

    @property
    def VpcId(self):
        r"""Specifies the unique VPC ID.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Vip(self):
        r"""Specifies the forwarding target IP proxy IP.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        r"""Specifies the forwarding target IP proxy port.
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Proto(self):
        r"""Specifies the forwarding target IP protocol.
        :rtype: str
        """
        return self._Proto

    @Proto.setter
    def Proto(self, Proto):
        self._Proto = Proto

    @property
    def SubnetId(self):
        r"""Specifies the unique subnet ID.
Required if the access type is CCN.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def AccessGatewayId(self):
        r"""ccn id
Required if the access type is CCN.
        :rtype: str
        """
        return self._AccessGatewayId

    @AccessGatewayId.setter
    def AccessGatewayId(self, AccessGatewayId):
        self._AccessGatewayId = AccessGatewayId

    @property
    def SnatVipCidr(self):
        r"""The SNAT CIDR block of the outbound endpoint.
        :rtype: str
        """
        return self._SnatVipCidr

    @SnatVipCidr.setter
    def SnatVipCidr(self, SnatVipCidr):
        self._SnatVipCidr = SnatVipCidr

    @property
    def SnatVipSet(self):
        r"""The SNAT IP list of the outbound endpoint.
        :rtype: str
        """
        return self._SnatVipSet

    @SnatVipSet.setter
    def SnatVipSet(self, SnatVipSet):
        self._SnatVipSet = SnatVipSet

    @property
    def Region(self):
        r"""The region of the outbound endpoint service.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._AccessType = params.get("AccessType")
        self._Pip = params.get("Pip")
        self._Pport = params.get("Pport")
        self._VpcId = params.get("VpcId")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._Proto = params.get("Proto")
        self._SubnetId = params.get("SubnetId")
        self._AccessGatewayId = params.get("AccessGatewayId")
        self._SnatVipCidr = params.get("SnatVipCidr")
        self._SnatVipSet = params.get("SnatVipSet")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""Filter parameter

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
        r"""Parameter name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""Array of parameter values
        :rtype: list of str
        """
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
    r"""Traffic package usage

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
        r"""Traffic package type, Valid values: ZONE (private domain); TRAFFIC (DNS traffic package)
        :rtype: str
        """
        return self._FlowType

    @FlowType.setter
    def FlowType(self, FlowType):
        self._FlowType = FlowType

    @property
    def TotalQuantity(self):
        r"""Traffic package quota
        :rtype: int
        """
        return self._TotalQuantity

    @TotalQuantity.setter
    def TotalQuantity(self, TotalQuantity):
        self._TotalQuantity = TotalQuantity

    @property
    def AvailableQuantity(self):
        r"""Available quota of traffic package
        :rtype: int
        """
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
        


class ForwardIp(AbstractModel):
    r"""PrivateDNS outbound endpoint forwarding IP

    """

    def __init__(self):
        r"""
        :param _AccessType: Forwarding target IP network access type.
CLB: The forwarding IP is the internal CLB VIP.
CCN: Forwarding IP through CCN routing.
        :type AccessType: str
        :param _Host: Forwarding target IP address.
        :type Host: str
        :param _Port: Specifies the forwarding IP port number.
        :type Port: int
        :param _IpNum: Specifies the number of outbound endpoints.
Minimum 1, maximum 6.
        :type IpNum: int
        :param _VpcId: Unique VPC ID.
        :type VpcId: str
        :param _SubnetId: Unique subnet ID.
Required when the access type is CCN.
        :type SubnetId: str
        :param _AccessGatewayId: ccn id
Required when the access type is CCN.
        :type AccessGatewayId: str
        """
        self._AccessType = None
        self._Host = None
        self._Port = None
        self._IpNum = None
        self._VpcId = None
        self._SubnetId = None
        self._AccessGatewayId = None

    @property
    def AccessType(self):
        r"""Forwarding target IP network access type.
CLB: The forwarding IP is the internal CLB VIP.
CCN: Forwarding IP through CCN routing.
        :rtype: str
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def Host(self):
        r"""Forwarding target IP address.
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Port(self):
        r"""Specifies the forwarding IP port number.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def IpNum(self):
        r"""Specifies the number of outbound endpoints.
Minimum 1, maximum 6.
        :rtype: int
        """
        return self._IpNum

    @IpNum.setter
    def IpNum(self, IpNum):
        self._IpNum = IpNum

    @property
    def VpcId(self):
        r"""Unique VPC ID.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""Unique subnet ID.
Required when the access type is CCN.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def AccessGatewayId(self):
        r"""ccn id
Required when the access type is CCN.
        :rtype: str
        """
        return self._AccessGatewayId

    @AccessGatewayId.setter
    def AccessGatewayId(self, AccessGatewayId):
        self._AccessGatewayId = AccessGatewayId


    def _deserialize(self, params):
        self._AccessType = params.get("AccessType")
        self._Host = params.get("Host")
        self._Port = params.get("Port")
        self._IpNum = params.get("IpNum")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._AccessGatewayId = params.get("AccessGatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForwardRule(AbstractModel):
    r"""Forwarding rule details.

    """

    def __init__(self):
        r"""
        :param _Domain: Private domain name.
        :type Domain: str
        :param _RuleName: Forwarding rule name.
        :type RuleName: str
        :param _RuleId: Rule ID
        :type RuleId: str
        :param _RuleType: Forwarding rule type. DOWN: From cloud to off-cloud; UP: From off-cloud to cloud.
        :type RuleType: str
        :param _CreatedAt: Creation time
        :type CreatedAt: str
        :param _UpdatedAt: Update time
        :type UpdatedAt: str
        :param _EndPointName: Endpoint name.
        :type EndPointName: str
        :param _EndPointId: Endpoint ID.
        :type EndPointId: str
        :param _ForwardAddress: Forwarding address.
        :type ForwardAddress: list of str
        :param _VpcSet: List of VPCs bound to the private domain.
        :type VpcSet: list of VpcInfo
        :param _ZoneId: ID of the bound private domain.
        :type ZoneId: str
        :param _Tags: Tag
        :type Tags: list of TagInfo
        """
        self._Domain = None
        self._RuleName = None
        self._RuleId = None
        self._RuleType = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._EndPointName = None
        self._EndPointId = None
        self._ForwardAddress = None
        self._VpcSet = None
        self._ZoneId = None
        self._Tags = None

    @property
    def Domain(self):
        r"""Private domain name.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RuleName(self):
        r"""Forwarding rule name.
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RuleId(self):
        r"""Rule ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleType(self):
        r"""Forwarding rule type. DOWN: From cloud to off-cloud; UP: From off-cloud to cloud.
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def CreatedAt(self):
        r"""Creation time
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""Update time
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def EndPointName(self):
        r"""Endpoint name.
        :rtype: str
        """
        return self._EndPointName

    @EndPointName.setter
    def EndPointName(self, EndPointName):
        self._EndPointName = EndPointName

    @property
    def EndPointId(self):
        r"""Endpoint ID.
        :rtype: str
        """
        return self._EndPointId

    @EndPointId.setter
    def EndPointId(self, EndPointId):
        self._EndPointId = EndPointId

    @property
    def ForwardAddress(self):
        r"""Forwarding address.
        :rtype: list of str
        """
        return self._ForwardAddress

    @ForwardAddress.setter
    def ForwardAddress(self, ForwardAddress):
        self._ForwardAddress = ForwardAddress

    @property
    def VpcSet(self):
        r"""List of VPCs bound to the private domain.
        :rtype: list of VpcInfo
        """
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

    @property
    def ZoneId(self):
        r"""ID of the bound private domain.
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Tags(self):
        r"""Tag
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._RuleName = params.get("RuleName")
        self._RuleId = params.get("RuleId")
        self._RuleType = params.get("RuleType")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._EndPointName = params.get("EndPointName")
        self._EndPointId = params.get("EndPointId")
        self._ForwardAddress = params.get("ForwardAddress")
        if params.get("VpcSet") is not None:
            self._VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcSet.append(obj)
        self._ZoneId = params.get("ZoneId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricData(AbstractModel):
    r"""Statistics table

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
        r"""Resource description
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Metric(self):
        r"""Table name
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def DataSet(self):
        r"""Table data
        :rtype: list of DatePoint
        """
        return self._DataSet

    @DataSet.setter
    def DataSet(self, DataSet):
        self._DataSet = DataSet

    @property
    def MetricCount(self):
        r"""The total number of requests within the query scope.
Note: This field may return null, indicating that no valid value can be obtained.
        :rtype: int
        """
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
        


class ModifyForwardRuleRequest(AbstractModel):
    r"""ModifyForwardRule request structure.

    """

    def __init__(self):
        r"""
        :param _RuleId: Forwarding rule ID.
        :type RuleId: str
        :param _RuleName: Forwarding rule name.
        :type RuleName: str
        :param _EndPointId: Endpoint ID.
        :type EndPointId: str
        """
        self._RuleId = None
        self._RuleName = None
        self._EndPointId = None

    @property
    def RuleId(self):
        r"""Forwarding rule ID.
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        r"""Forwarding rule name.
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def EndPointId(self):
        r"""Endpoint ID.
        :rtype: str
        """
        return self._EndPointId

    @EndPointId.setter
    def EndPointId(self, EndPointId):
        self._EndPointId = EndPointId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._EndPointId = params.get("EndPointId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyForwardRuleResponse(AbstractModel):
    r"""ModifyForwardRule response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyPrivateZoneRecordRequest(AbstractModel):
    r"""ModifyPrivateZoneRecord request structure.

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
        r"""Private domain ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RecordId(self):
        r"""Record ID
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def RecordType(self):
        r"""Record type. Valid values: "A", "AAAA", "CNAME", "MX", "TXT", "PTR"
        :rtype: str
        """
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def SubDomain(self):
        r"""Subdomain, such as "www", "m", and "@"
        :rtype: str
        """
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordValue(self):
        r"""Record value, such as IP: 192.168.10.2, CNAME: cname.qcloud.com., and MX: mail.qcloud.com.
        :rtype: str
        """
        return self._RecordValue

    @RecordValue.setter
    def RecordValue(self, RecordValue):
        self._RecordValue = RecordValue

    @property
    def Weight(self):
        r"""Record weight. Value range: 1–100
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def MX(self):
        r"""MX priority, which is required when the record type is MX. Valid values: 5, 10, 15, 20, 30, 40, 50
        :rtype: int
        """
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX

    @property
    def TTL(self):
        r"""Record cache time. The smaller the value, the faster the record will take effect. Value range: 1–86400s. Default value: 600
        :rtype: int
        """
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
    r"""ModifyPrivateZoneRecord response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyPrivateZoneRequest(AbstractModel):
    r"""ModifyPrivateZone request structure.

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
        r"""Private domain ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Remark(self):
        r"""Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def DnsForwardStatus(self):
        r"""Whether to enable subdomain recursive DNS. Valid values: ENABLED, DISABLED
        :rtype: str
        """
        return self._DnsForwardStatus

    @DnsForwardStatus.setter
    def DnsForwardStatus(self, DnsForwardStatus):
        self._DnsForwardStatus = DnsForwardStatus

    @property
    def CnameSpeedupStatus(self):
        r"""Whether to enable CNAME flattening. Valid values: `ENABLED` and `DISABLED`.
        :rtype: str
        """
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
    r"""ModifyPrivateZone response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyPrivateZoneVpcRequest(AbstractModel):
    r"""ModifyPrivateZoneVpc request structure.

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
        r"""Private domain ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcSet(self):
        r"""List of all VPCs associated with private domain
        :rtype: list of VpcInfo
        """
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

    @property
    def AccountVpcSet(self):
        r"""List of authorized accounts' VPCs to associate with the private domain
        :rtype: list of AccountVpcInfo
        """
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
    r"""ModifyPrivateZoneVpc response structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Private domain ID, such as zone-xxxxxx
        :type ZoneId: str
        :param _VpcSet: List of VPCs associated with domain
        :type VpcSet: list of VpcInfo
        :param _AccountVpcSet: List of authorized accounts' VPCs associated with the private domain
        :type AccountVpcSet: list of AccountVpcInfoOutput
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ZoneId = None
        self._VpcSet = None
        self._AccountVpcSet = None
        self._RequestId = None

    @property
    def ZoneId(self):
        r"""Private domain ID, such as zone-xxxxxx
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcSet(self):
        r"""List of VPCs associated with domain
        :rtype: list of VpcInfo
        """
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

    @property
    def AccountVpcSet(self):
        r"""List of authorized accounts' VPCs associated with the private domain
        :rtype: list of AccountVpcInfoOutput
        """
        return self._AccountVpcSet

    @AccountVpcSet.setter
    def AccountVpcSet(self, AccountVpcSet):
        self._AccountVpcSet = AccountVpcSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
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
    r"""ModifyRecordsStatus request structure.

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
        r"""The private domain ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RecordIds(self):
        r"""The DNS record IDs.
        :rtype: list of int
        """
        return self._RecordIds

    @RecordIds.setter
    def RecordIds(self, RecordIds):
        self._RecordIds = RecordIds

    @property
    def Status(self):
        r"""`enabled`: Enable; `disabled`: Disable.
        :rtype: str
        """
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
    r"""ModifyRecordsStatus response structure.

    """

    def __init__(self):
        r"""
        :param _ZoneId: The private domain ID
        :type ZoneId: str
        :param _RecordIds: The DNS record IDs.
        :type RecordIds: list of int
        :param _Status: `enabled`: Enabled; `disabled`: Disabled.
        :type Status: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ZoneId = None
        self._RecordIds = None
        self._Status = None
        self._RequestId = None

    @property
    def ZoneId(self):
        r"""The private domain ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RecordIds(self):
        r"""The DNS record IDs.
        :rtype: list of int
        """
        return self._RecordIds

    @RecordIds.setter
    def RecordIds(self, RecordIds):
        self._RecordIds = RecordIds

    @property
    def Status(self):
        r"""`enabled`: Enabled; `disabled`: Disabled.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RecordIds = params.get("RecordIds")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class OutboundEndpoint(AbstractModel):
    r"""Outbound endpoint.

    """

    def __init__(self):
        r"""
        :param _EndpointId: Outbound endpoint ID.
        :type EndpointId: str
        :param _EndpointName: Outbound endpoint name.
        :type EndpointName: str
        :param _Region: The region of the outbound endpoint.
        :type Region: str
        :param _Tags: Tag
        :type Tags: list of TagInfo
        :param _EndpointServiceSet: Outbound endpoint information.
Returned only when the forwarding architecture is V2R.
        :type EndpointServiceSet: list of EndpointService
        :param _ForwardLinkArch: Forwarding link architecture.
V2V: privatelink
V2R: jnsgw
        :type ForwardLinkArch: str
        :param _EndPointServiceId: Endpoint service ID.

Returned only when the forwarding architecture is V2V.

        :type EndPointServiceId: str
        :param _EndPointVipSet: VIP list of the endpoint.

Returned only when the forwarding architecture is V2V.
        :type EndPointVipSet: list of str
        """
        self._EndpointId = None
        self._EndpointName = None
        self._Region = None
        self._Tags = None
        self._EndpointServiceSet = None
        self._ForwardLinkArch = None
        self._EndPointServiceId = None
        self._EndPointVipSet = None

    @property
    def EndpointId(self):
        r"""Outbound endpoint ID.
        :rtype: str
        """
        return self._EndpointId

    @EndpointId.setter
    def EndpointId(self, EndpointId):
        self._EndpointId = EndpointId

    @property
    def EndpointName(self):
        r"""Outbound endpoint name.
        :rtype: str
        """
        return self._EndpointName

    @EndpointName.setter
    def EndpointName(self, EndpointName):
        self._EndpointName = EndpointName

    @property
    def Region(self):
        r"""The region of the outbound endpoint.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Tags(self):
        r"""Tag
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def EndpointServiceSet(self):
        r"""Outbound endpoint information.
Returned only when the forwarding architecture is V2R.
        :rtype: list of EndpointService
        """
        return self._EndpointServiceSet

    @EndpointServiceSet.setter
    def EndpointServiceSet(self, EndpointServiceSet):
        self._EndpointServiceSet = EndpointServiceSet

    @property
    def ForwardLinkArch(self):
        r"""Forwarding link architecture.
V2V: privatelink
V2R: jnsgw
        :rtype: str
        """
        return self._ForwardLinkArch

    @ForwardLinkArch.setter
    def ForwardLinkArch(self, ForwardLinkArch):
        self._ForwardLinkArch = ForwardLinkArch

    @property
    def EndPointServiceId(self):
        r"""Endpoint service ID.

Returned only when the forwarding architecture is V2V.

        :rtype: str
        """
        return self._EndPointServiceId

    @EndPointServiceId.setter
    def EndPointServiceId(self, EndPointServiceId):
        self._EndPointServiceId = EndPointServiceId

    @property
    def EndPointVipSet(self):
        r"""VIP list of the endpoint.

Returned only when the forwarding architecture is V2V.
        :rtype: list of str
        """
        return self._EndPointVipSet

    @EndPointVipSet.setter
    def EndPointVipSet(self, EndPointVipSet):
        self._EndPointVipSet = EndPointVipSet


    def _deserialize(self, params):
        self._EndpointId = params.get("EndpointId")
        self._EndpointName = params.get("EndpointName")
        self._Region = params.get("Region")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("EndpointServiceSet") is not None:
            self._EndpointServiceSet = []
            for item in params.get("EndpointServiceSet"):
                obj = EndpointService()
                obj._deserialize(item)
                self._EndpointServiceSet.append(obj)
        self._ForwardLinkArch = params.get("ForwardLinkArch")
        self._EndPointServiceId = params.get("EndPointServiceId")
        self._EndPointVipSet = params.get("EndPointVipSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivateDNSAccount(AbstractModel):
    r"""Private DNS account

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
        r"""Root account UIN
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Account(self):
        r"""Root account name
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def Nickname(self):
        r"""Account name
        :rtype: str
        """
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
        


class PrivateZone(AbstractModel):
    r"""Private domain information.

    """

    def __init__(self):
        r"""
        :param _ZoneId: Private domain ID, which is in zone-xxxxxxxx format.
        :type ZoneId: str
        :param _OwnerUin: UIN of the domain name owner.
        :type OwnerUin: int
        :param _Domain: Private domain name.
        :type Domain: str
        :param _CreatedOn: Creation time
        :type CreatedOn: str
        :param _UpdatedOn: Modification time
        :type UpdatedOn: str
        :param _RecordCount: Number of records.
        :type RecordCount: int
        :param _Remark: Remarks.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param _VpcSet: List of bound VPCs.
        :type VpcSet: list of VpcInfo
        :param _Status: Status of the VPC bound with the private domain. SUSPEND: The VPC is not associated; ENABLED: the VPC has been associated.
, FAILED: the VPC fails to be associated.
        :type Status: str
        :param _DnsForwardStatus: Recursive resolution status of the domain name. ENABLED: enabled; DISABLED: disabled.
        :type DnsForwardStatus: str
        :param _Tags: Tag key-value pair collection.
        :type Tags: list of TagInfo
        :param _AccountVpcSet: List of bound VPCs of the associated account.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccountVpcSet: list of AccountVpcInfoOutput
        :param _IsCustomTld: Whether the TLD is a custom one.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsCustomTld: bool
        :param _CnameSpeedupStatus: CNAME acceleration status. ENABLED: enabled; DISABLED: disabled.
        :type CnameSpeedupStatus: str
        :param _ForwardRuleName: Forwarding rule name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ForwardRuleName: str
        :param _ForwardRuleType: Forwarding rule type. DOWN: from cloud to off-cloud; UP: from off-cloud to cloud. Currently, only DOWN is supported.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ForwardRuleType: str
        :param _ForwardAddress: Forwarding address.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ForwardAddress: str
        :param _EndPointName: Endpoint name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndPointName: str
        :param _DeletedVpcSet: Deleted VPC.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DeletedVpcSet: list of VpcInfo
        """
        self._ZoneId = None
        self._OwnerUin = None
        self._Domain = None
        self._CreatedOn = None
        self._UpdatedOn = None
        self._RecordCount = None
        self._Remark = None
        self._VpcSet = None
        self._Status = None
        self._DnsForwardStatus = None
        self._Tags = None
        self._AccountVpcSet = None
        self._IsCustomTld = None
        self._CnameSpeedupStatus = None
        self._ForwardRuleName = None
        self._ForwardRuleType = None
        self._ForwardAddress = None
        self._EndPointName = None
        self._DeletedVpcSet = None

    @property
    def ZoneId(self):
        r"""Private domain ID, which is in zone-xxxxxxxx format.
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def OwnerUin(self):
        r"""UIN of the domain name owner.
        :rtype: int
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Domain(self):
        r"""Private domain name.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CreatedOn(self):
        r"""Creation time
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def UpdatedOn(self):
        r"""Modification time
        :rtype: str
        """
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn

    @property
    def RecordCount(self):
        r"""Number of records.
        :rtype: int
        """
        return self._RecordCount

    @RecordCount.setter
    def RecordCount(self, RecordCount):
        self._RecordCount = RecordCount

    @property
    def Remark(self):
        r"""Remarks.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def VpcSet(self):
        r"""List of bound VPCs.
        :rtype: list of VpcInfo
        """
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

    @property
    def Status(self):
        r"""Status of the VPC bound with the private domain. SUSPEND: The VPC is not associated; ENABLED: the VPC has been associated.
, FAILED: the VPC fails to be associated.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DnsForwardStatus(self):
        r"""Recursive resolution status of the domain name. ENABLED: enabled; DISABLED: disabled.
        :rtype: str
        """
        return self._DnsForwardStatus

    @DnsForwardStatus.setter
    def DnsForwardStatus(self, DnsForwardStatus):
        self._DnsForwardStatus = DnsForwardStatus

    @property
    def Tags(self):
        r"""Tag key-value pair collection.
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AccountVpcSet(self):
        r"""List of bound VPCs of the associated account.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of AccountVpcInfoOutput
        """
        return self._AccountVpcSet

    @AccountVpcSet.setter
    def AccountVpcSet(self, AccountVpcSet):
        self._AccountVpcSet = AccountVpcSet

    @property
    def IsCustomTld(self):
        r"""Whether the TLD is a custom one.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsCustomTld

    @IsCustomTld.setter
    def IsCustomTld(self, IsCustomTld):
        self._IsCustomTld = IsCustomTld

    @property
    def CnameSpeedupStatus(self):
        r"""CNAME acceleration status. ENABLED: enabled; DISABLED: disabled.
        :rtype: str
        """
        return self._CnameSpeedupStatus

    @CnameSpeedupStatus.setter
    def CnameSpeedupStatus(self, CnameSpeedupStatus):
        self._CnameSpeedupStatus = CnameSpeedupStatus

    @property
    def ForwardRuleName(self):
        r"""Forwarding rule name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ForwardRuleName

    @ForwardRuleName.setter
    def ForwardRuleName(self, ForwardRuleName):
        self._ForwardRuleName = ForwardRuleName

    @property
    def ForwardRuleType(self):
        r"""Forwarding rule type. DOWN: from cloud to off-cloud; UP: from off-cloud to cloud. Currently, only DOWN is supported.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ForwardRuleType

    @ForwardRuleType.setter
    def ForwardRuleType(self, ForwardRuleType):
        self._ForwardRuleType = ForwardRuleType

    @property
    def ForwardAddress(self):
        r"""Forwarding address.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ForwardAddress

    @ForwardAddress.setter
    def ForwardAddress(self, ForwardAddress):
        self._ForwardAddress = ForwardAddress

    @property
    def EndPointName(self):
        r"""Endpoint name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EndPointName

    @EndPointName.setter
    def EndPointName(self, EndPointName):
        self._EndPointName = EndPointName

    @property
    def DeletedVpcSet(self):
        r"""Deleted VPC.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of VpcInfo
        """
        return self._DeletedVpcSet

    @DeletedVpcSet.setter
    def DeletedVpcSet(self, DeletedVpcSet):
        self._DeletedVpcSet = DeletedVpcSet


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._OwnerUin = params.get("OwnerUin")
        self._Domain = params.get("Domain")
        self._CreatedOn = params.get("CreatedOn")
        self._UpdatedOn = params.get("UpdatedOn")
        self._RecordCount = params.get("RecordCount")
        self._Remark = params.get("Remark")
        if params.get("VpcSet") is not None:
            self._VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcSet.append(obj)
        self._Status = params.get("Status")
        self._DnsForwardStatus = params.get("DnsForwardStatus")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("AccountVpcSet") is not None:
            self._AccountVpcSet = []
            for item in params.get("AccountVpcSet"):
                obj = AccountVpcInfoOutput()
                obj._deserialize(item)
                self._AccountVpcSet.append(obj)
        self._IsCustomTld = params.get("IsCustomTld")
        self._CnameSpeedupStatus = params.get("CnameSpeedupStatus")
        self._ForwardRuleName = params.get("ForwardRuleName")
        self._ForwardRuleType = params.get("ForwardRuleType")
        self._ForwardAddress = params.get("ForwardAddress")
        self._EndPointName = params.get("EndPointName")
        if params.get("DeletedVpcSet") is not None:
            self._DeletedVpcSet = []
            for item in params.get("DeletedVpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._DeletedVpcSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivateZoneRecord(AbstractModel):
    r"""Private domain information

    """

    def __init__(self):
        r"""
        :param _RecordId: Record ID
        :type RecordId: str
        :param _ZoneId: Private domain ID: zone-xxxxxxxx
        :type ZoneId: str
        :param _SubDomain: Subdomain
        :type SubDomain: str
        :param _RecordType: Record type. Valid values: "A", "AAAA", "CNAME", "MX", "TXT", "PTR"
        :type RecordType: str
        :param _RecordValue: Record value
        :type RecordValue: str
        :param _TTL: Record cache time. The smaller the value, the faster the record will take effect. Value range: 1–86400s. Default value: 600
        :type TTL: int
        :param _MX: MX priority, which is required when the record type is MX. Valid values: 5, 10, 15, 20, 30, 40, 50
Note: this field may return null, indicating that no valid values can be obtained.
        :type MX: int
        :param _Status: Record status: ENABLED
        :type Status: str
        :param _Weight: Record weight. Value range: 1–100
Note: this field may return null, indicating that no valid values can be obtained.
        :type Weight: int
        :param _CreatedOn: Record creation time
        :type CreatedOn: str
        :param _UpdatedOn: Record update time
        :type UpdatedOn: str
        :param _Extra: Additional information
Note: this field may return null, indicating that no valid values can be obtained.
        :type Extra: str
        """
        self._RecordId = None
        self._ZoneId = None
        self._SubDomain = None
        self._RecordType = None
        self._RecordValue = None
        self._TTL = None
        self._MX = None
        self._Status = None
        self._Weight = None
        self._CreatedOn = None
        self._UpdatedOn = None
        self._Extra = None

    @property
    def RecordId(self):
        r"""Record ID
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def ZoneId(self):
        r"""Private domain ID: zone-xxxxxxxx
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def SubDomain(self):
        r"""Subdomain
        :rtype: str
        """
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordType(self):
        r"""Record type. Valid values: "A", "AAAA", "CNAME", "MX", "TXT", "PTR"
        :rtype: str
        """
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RecordValue(self):
        r"""Record value
        :rtype: str
        """
        return self._RecordValue

    @RecordValue.setter
    def RecordValue(self, RecordValue):
        self._RecordValue = RecordValue

    @property
    def TTL(self):
        r"""Record cache time. The smaller the value, the faster the record will take effect. Value range: 1–86400s. Default value: 600
        :rtype: int
        """
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def MX(self):
        r"""MX priority, which is required when the record type is MX. Valid values: 5, 10, 15, 20, 30, 40, 50
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX

    @property
    def Status(self):
        r"""Record status: ENABLED
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Weight(self):
        r"""Record weight. Value range: 1–100
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def CreatedOn(self):
        r"""Record creation time
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def UpdatedOn(self):
        r"""Record update time
        :rtype: str
        """
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn

    @property
    def Extra(self):
        r"""Additional information
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra


    def _deserialize(self, params):
        self._RecordId = params.get("RecordId")
        self._ZoneId = params.get("ZoneId")
        self._SubDomain = params.get("SubDomain")
        self._RecordType = params.get("RecordType")
        self._RecordValue = params.get("RecordValue")
        self._TTL = params.get("TTL")
        self._MX = params.get("MX")
        self._Status = params.get("Status")
        self._Weight = params.get("Weight")
        self._CreatedOn = params.get("CreatedOn")
        self._UpdatedOn = params.get("UpdatedOn")
        self._Extra = params.get("Extra")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordInfo(AbstractModel):
    r"""Private domain information.

    """

    def __init__(self):
        r"""
        :param _RecordId: Record ID.
        :type RecordId: str
        :param _ZoneId: Private domain ID, which is in zone-xxxxxxxx format.
        :type ZoneId: str
        :param _SubDomain: Subdomain name.
        :type SubDomain: str
        :param _RecordType: Record type. Valid values: A, AAAA, CNAME, MX, TXT, and PTR.
        :type RecordType: str
        :param _RecordValue: Record value.
        :type RecordValue: str
        :param _TTL: Record cache time. The smaller the value, the faster the record will take effect. Value range: 1-86,400s. Default value: 600.
        :type TTL: int
        :param _MX: MX priority, which is required when the record type is mx. valid values: 5, 10, 15, 20, 30, 40, and 50.
        :type MX: int
        :param _Weight: Record weight. valid values: 1–100.
        :type Weight: int
        :param _CreatedOn: Record creation time.
        :type CreatedOn: str
        :param _UpdatedOn: Record update time.
        :type UpdatedOn: str
        :param _Enabled: 0 suspend 1 enable.
        :type Enabled: int
        :param _Remark: Remarks
        :type Remark: str
        """
        self._RecordId = None
        self._ZoneId = None
        self._SubDomain = None
        self._RecordType = None
        self._RecordValue = None
        self._TTL = None
        self._MX = None
        self._Weight = None
        self._CreatedOn = None
        self._UpdatedOn = None
        self._Enabled = None
        self._Remark = None

    @property
    def RecordId(self):
        r"""Record ID.
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def ZoneId(self):
        r"""Private domain ID, which is in zone-xxxxxxxx format.
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def SubDomain(self):
        r"""Subdomain name.
        :rtype: str
        """
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordType(self):
        r"""Record type. Valid values: A, AAAA, CNAME, MX, TXT, and PTR.
        :rtype: str
        """
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RecordValue(self):
        r"""Record value.
        :rtype: str
        """
        return self._RecordValue

    @RecordValue.setter
    def RecordValue(self, RecordValue):
        self._RecordValue = RecordValue

    @property
    def TTL(self):
        r"""Record cache time. The smaller the value, the faster the record will take effect. Value range: 1-86,400s. Default value: 600.
        :rtype: int
        """
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def MX(self):
        r"""MX priority, which is required when the record type is mx. valid values: 5, 10, 15, 20, 30, 40, and 50.
        :rtype: int
        """
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX

    @property
    def Weight(self):
        r"""Record weight. valid values: 1–100.
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def CreatedOn(self):
        r"""Record creation time.
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def UpdatedOn(self):
        r"""Record update time.
        :rtype: str
        """
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn

    @property
    def Enabled(self):
        r"""0 suspend 1 enable.
        :rtype: int
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Remark(self):
        r"""Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._RecordId = params.get("RecordId")
        self._ZoneId = params.get("ZoneId")
        self._SubDomain = params.get("SubDomain")
        self._RecordType = params.get("RecordType")
        self._RecordValue = params.get("RecordValue")
        self._TTL = params.get("TTL")
        self._MX = params.get("MX")
        self._Weight = params.get("Weight")
        self._CreatedOn = params.get("CreatedOn")
        self._UpdatedOn = params.get("UpdatedOn")
        self._Enabled = params.get("Enabled")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionInfo(AbstractModel):
    r"""Region information

    """

    def __init__(self):
        r"""
        :param _RegionCode: Region encoding
        :type RegionCode: str
        :param _CnName: Region name

Note: This field may return null, indicating that no valid values can be obtained.
        :type CnName: str
        :param _EnName: English name of the region
        :type EnName: str
        :param _RegionId: Region ID

Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionId: int
        :param _AvailableZoneNum: Number of AZs

Note: This field may return null, indicating that no valid values can be obtained.
        :type AvailableZoneNum: int
        """
        self._RegionCode = None
        self._CnName = None
        self._EnName = None
        self._RegionId = None
        self._AvailableZoneNum = None

    @property
    def RegionCode(self):
        r"""Region encoding
        :rtype: str
        """
        return self._RegionCode

    @RegionCode.setter
    def RegionCode(self, RegionCode):
        self._RegionCode = RegionCode

    @property
    def CnName(self):
        r"""Region name

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CnName

    @CnName.setter
    def CnName(self, CnName):
        self._CnName = CnName

    @property
    def EnName(self):
        r"""English name of the region
        :rtype: str
        """
        return self._EnName

    @EnName.setter
    def EnName(self, EnName):
        self._EnName = EnName

    @property
    def RegionId(self):
        r"""Region ID

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def AvailableZoneNum(self):
        r"""Number of AZs

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AvailableZoneNum

    @AvailableZoneNum.setter
    def AvailableZoneNum(self, AvailableZoneNum):
        self._AvailableZoneNum = AvailableZoneNum


    def _deserialize(self, params):
        self._RegionCode = params.get("RegionCode")
        self._CnName = params.get("CnName")
        self._EnName = params.get("EnName")
        self._RegionId = params.get("RegionId")
        self._AvailableZoneNum = params.get("AvailableZoneNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribePrivateZoneServiceRequest(AbstractModel):
    r"""SubscribePrivateZoneService request structure.

    """


class SubscribePrivateZoneServiceResponse(AbstractModel):
    r"""SubscribePrivateZoneService response structure.

    """

    def __init__(self):
        r"""
        :param _ServiceStatus: Private DNS service activation status
        :type ServiceStatus: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ServiceStatus = None
        self._RequestId = None

    @property
    def ServiceStatus(self):
        r"""Private DNS service activation status
        :rtype: str
        """
        return self._ServiceStatus

    @ServiceStatus.setter
    def ServiceStatus(self, ServiceStatus):
        self._ServiceStatus = ServiceStatus

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ServiceStatus = params.get("ServiceStatus")
        self._RequestId = params.get("RequestId")


class TagInfo(AbstractModel):
    r"""Tag

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
        r"""Tag key
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""Tag value
        :rtype: str
        """
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
    r"""TLD quota

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
        r"""Total quota
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Used(self):
        r"""Used quota
        :rtype: int
        """
        return self._Used

    @Used.setter
    def Used(self, Used):
        self._Used = Used

    @property
    def Stock(self):
        r"""Available quota
        :rtype: int
        """
        return self._Stock

    @Stock.setter
    def Stock(self, Stock):
        self._Stock = Stock

    @property
    def Quota(self):
        r"""User’s quota
        :rtype: int
        """
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
    r"""VPC information

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
        r"""VpcId: vpc-xadsafsdasd
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Region(self):
        r"""VPC region: ap-guangzhou, ap-shanghai
        :rtype: str
        """
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
        