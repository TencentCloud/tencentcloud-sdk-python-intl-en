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


class AcListsData(AbstractModel):
    """Access control list rule

    """

    def __init__(self):
        r"""
        :param _Id: Rule ID
        :type Id: int
        :param _SourceIp: Access source
Note: This field may return `null`, indicating that no valid value was found.
        :type SourceIp: str
        :param _TargetIp: Access destination
Note: This field may return `null`, indicating that no valid value was found.
        :type TargetIp: str
        :param _Protocol: Protocol
Note: This field may return `null`, indicating that no valid value was found.
        :type Protocol: str
        :param _Port: Port
Note: This field may return `null`, indicating that no valid value was found.
        :type Port: str
        :param _Strategy: Policy
Note: This field may return `null`, indicating that no valid value was found.
        :type Strategy: int
        :param _Detail: Description
Note: This field may return `null`, indicating that no valid value was found.
        :type Detail: str
        :param _Count: Hit count
        :type Count: int
        :param _OrderIndex: Priority
        :type OrderIndex: int
        :param _LogId: Alert rule ID
Note: This field may return `null`, indicating that no valid value was found.
        :type LogId: str
        """
        self._Id = None
        self._SourceIp = None
        self._TargetIp = None
        self._Protocol = None
        self._Port = None
        self._Strategy = None
        self._Detail = None
        self._Count = None
        self._OrderIndex = None
        self._LogId = None

    @property
    def Id(self):
        """Rule ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def SourceIp(self):
        """Access source
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._SourceIp

    @SourceIp.setter
    def SourceIp(self, SourceIp):
        self._SourceIp = SourceIp

    @property
    def TargetIp(self):
        """Access destination
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._TargetIp

    @TargetIp.setter
    def TargetIp(self, TargetIp):
        self._TargetIp = TargetIp

    @property
    def Protocol(self):
        """Protocol
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        """Port
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Strategy(self):
        """Policy
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def Detail(self):
        """Description
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Count(self):
        """Hit count
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def OrderIndex(self):
        """Priority
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def LogId(self):
        """Alert rule ID
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._LogId

    @LogId.setter
    def LogId(self, LogId):
        self._LogId = LogId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._SourceIp = params.get("SourceIp")
        self._TargetIp = params.get("TargetIp")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._Strategy = params.get("Strategy")
        self._Detail = params.get("Detail")
        self._Count = params.get("Count")
        self._OrderIndex = params.get("OrderIndex")
        self._LogId = params.get("LogId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddAcRuleRequest(AbstractModel):
    """AddAcRule request structure.

    """

    def __init__(self):
        r"""
        :param _OrderIndex: -1: lowest priority; 1: highest priority
        :type OrderIndex: str
        :param _RuleAction: The action that Cloud Firewall performs on the traffic. Valid values:
accept: allow
drop: deny
log: observe
        :type RuleAction: str
        :param _Direction: The traffic direction for access control rules. Valid values:
in: incoming traffic access control
out: outgoing traffic access control
        :type Direction: str
        :param _Description: The description of access control rules.
        :type Description: str
        :param _SourceType: The type of source address in access control rules. Valid values:
net: source IP or range (IP or CIDR)
location: source region
template: CFW address template
instance: instance ID
vendor: Cloud vendor
        :type SourceType: str
        :param _SourceContent: The source address in the access control policy. 
When `SourceType` is `net`, `SourceContent` is the source IP or CIDR block.
For example: 1.1.1.0/24

When `SourceType` is `template`, `SourceContent` must be the source address template ID.

When `SourceType` is `location`, `SourceContent` is the source region. 
For example, ["BJ11", "ZB"]

When `SourceType` is `instance`, `SourceContent` is the public IP of the instance.
For example, ins-xxxxx

When `SourceType` is `vendor`, `SourceContent` is the cloud service provider.
Values: `aws`, `huawei`, `tencent`, `aliyun`, `azure` and `all`. 
        :type SourceContent: str
        :param _DestType: The type of destination address in access control rules. Valid values:
net: destination IP or range (IP or CIDR)
location: source region
template: CFW address template
instance: instance ID
vendor: Cloud vendor
domain: Domain name or IP.
        :type DestType: str
        :param _DestContent: The destination address in the access control policy. 
When `DestType` is `net`, `DestContent` is the destination IP or CIDR block.
For example: 1.1.1.0/24

When `DestType` is `template`, `DestContent` is the destination address template ID.

When `DestType` is `location`, `DestContent` is the destination region. 
For example, ["BJ11", "ZB"]

When `DestType` is `instance`, `DestContent` is the public IP of the instance.
For example, ins-xxxxx

When `DestType` is `domain`, `DestContent` is the domain name associated with the instance.
For example, *.qq.com

When `DestType`, `DestContent` is the selected cloud service provider.
Values: `aws`, `huawei`, `tencent`, `aliyun`, `azure` and `all`. 
        :type DestContent: str
        :param _Port: The port to apply access control rules. Valid values:
-1/-1: all ports
80,443: 80 or 443
        :type Port: str
        :param _Protocol: The protocol type of traffic in access control rules. Valid value: TCP. Only TCP is supported for edge firewall rules. If this parameter is not specified, it defaults to TCP.
        :type Protocol: str
        :param _ApplicationName: The Layer 7 protocol. Valid values:
HTTP/HTTPS
TLS/SSL
        :type ApplicationName: str
        :param _Enable: Indicates whether to enable the rules. Default: enable. Valid values:
true: enable; false: disable
        :type Enable: str
        """
        self._OrderIndex = None
        self._RuleAction = None
        self._Direction = None
        self._Description = None
        self._SourceType = None
        self._SourceContent = None
        self._DestType = None
        self._DestContent = None
        self._Port = None
        self._Protocol = None
        self._ApplicationName = None
        self._Enable = None

    @property
    def OrderIndex(self):
        """-1: lowest priority; 1: highest priority
        :rtype: str
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def RuleAction(self):
        """The action that Cloud Firewall performs on the traffic. Valid values:
accept: allow
drop: deny
log: observe
        :rtype: str
        """
        return self._RuleAction

    @RuleAction.setter
    def RuleAction(self, RuleAction):
        self._RuleAction = RuleAction

    @property
    def Direction(self):
        """The traffic direction for access control rules. Valid values:
in: incoming traffic access control
out: outgoing traffic access control
        :rtype: str
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Description(self):
        """The description of access control rules.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SourceType(self):
        """The type of source address in access control rules. Valid values:
net: source IP or range (IP or CIDR)
location: source region
template: CFW address template
instance: instance ID
vendor: Cloud vendor
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def SourceContent(self):
        """The source address in the access control policy. 
When `SourceType` is `net`, `SourceContent` is the source IP or CIDR block.
For example: 1.1.1.0/24

When `SourceType` is `template`, `SourceContent` must be the source address template ID.

When `SourceType` is `location`, `SourceContent` is the source region. 
For example, ["BJ11", "ZB"]

When `SourceType` is `instance`, `SourceContent` is the public IP of the instance.
For example, ins-xxxxx

When `SourceType` is `vendor`, `SourceContent` is the cloud service provider.
Values: `aws`, `huawei`, `tencent`, `aliyun`, `azure` and `all`. 
        :rtype: str
        """
        return self._SourceContent

    @SourceContent.setter
    def SourceContent(self, SourceContent):
        self._SourceContent = SourceContent

    @property
    def DestType(self):
        """The type of destination address in access control rules. Valid values:
net: destination IP or range (IP or CIDR)
location: source region
template: CFW address template
instance: instance ID
vendor: Cloud vendor
domain: Domain name or IP.
        :rtype: str
        """
        return self._DestType

    @DestType.setter
    def DestType(self, DestType):
        self._DestType = DestType

    @property
    def DestContent(self):
        """The destination address in the access control policy. 
When `DestType` is `net`, `DestContent` is the destination IP or CIDR block.
For example: 1.1.1.0/24

When `DestType` is `template`, `DestContent` is the destination address template ID.

When `DestType` is `location`, `DestContent` is the destination region. 
For example, ["BJ11", "ZB"]

When `DestType` is `instance`, `DestContent` is the public IP of the instance.
For example, ins-xxxxx

When `DestType` is `domain`, `DestContent` is the domain name associated with the instance.
For example, *.qq.com

When `DestType`, `DestContent` is the selected cloud service provider.
Values: `aws`, `huawei`, `tencent`, `aliyun`, `azure` and `all`. 
        :rtype: str
        """
        return self._DestContent

    @DestContent.setter
    def DestContent(self, DestContent):
        self._DestContent = DestContent

    @property
    def Port(self):
        """The port to apply access control rules. Valid values:
-1/-1: all ports
80,443: 80 or 443
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Protocol(self):
        """The protocol type of traffic in access control rules. Valid value: TCP. Only TCP is supported for edge firewall rules. If this parameter is not specified, it defaults to TCP.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ApplicationName(self):
        """The Layer 7 protocol. Valid values:
HTTP/HTTPS
TLS/SSL
        :rtype: str
        """
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def Enable(self):
        """Indicates whether to enable the rules. Default: enable. Valid values:
true: enable; false: disable
        :rtype: str
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._OrderIndex = params.get("OrderIndex")
        self._RuleAction = params.get("RuleAction")
        self._Direction = params.get("Direction")
        self._Description = params.get("Description")
        self._SourceType = params.get("SourceType")
        self._SourceContent = params.get("SourceContent")
        self._DestType = params.get("DestType")
        self._DestContent = params.get("DestContent")
        self._Port = params.get("Port")
        self._Protocol = params.get("Protocol")
        self._ApplicationName = params.get("ApplicationName")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddAcRuleResponse(AbstractModel):
    """AddAcRule response structure.

    """

    def __init__(self):
        r"""
        :param _RuleUuid: UUID of the new rule
        :type RuleUuid: int
        :param _ReturnCode: 0: operation successful; -1: operation failed
        :type ReturnCode: int
        :param _ReturnMsg: success: operation successful; failed: operation failed
        :type ReturnMsg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleUuid = None
        self._ReturnCode = None
        self._ReturnMsg = None
        self._RequestId = None

    @property
    def RuleUuid(self):
        """UUID of the new rule
        :rtype: int
        """
        return self._RuleUuid

    @RuleUuid.setter
    def RuleUuid(self, RuleUuid):
        self._RuleUuid = RuleUuid

    @property
    def ReturnCode(self):
        """0: operation successful; -1: operation failed
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        """success: operation successful; failed: operation failed
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleUuid = params.get("RuleUuid")
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        self._RequestId = params.get("RequestId")


class AddEnterpriseSecurityGroupRulesRequest(AbstractModel):
    """AddEnterpriseSecurityGroupRules request structure.

    """

    def __init__(self):
        r"""
        :param _Data: Creates rule data
        :type Data: list of SecurityGroupRule
        :param _Type: Adding type. 0: add to the end; 1: add to the front; 2: insert. Default: 0
        :type Type: int
        :param _ClientToken: An identifier to ensure the idempotency of the request. The value of the ClientToken parameter is a unique string that is generated by your client and can contain up to 64 ASCII characters in length.
        :type ClientToken: str
        :param _IsDelay: Indicates whether to delay publishing. 1: delay; other values: do not delay
        :type IsDelay: int
        """
        self._Data = None
        self._Type = None
        self._ClientToken = None
        self._IsDelay = None

    @property
    def Data(self):
        """Creates rule data
        :rtype: list of SecurityGroupRule
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Type(self):
        """Adding type. 0: add to the end; 1: add to the front; 2: insert. Default: 0
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ClientToken(self):
        """An identifier to ensure the idempotency of the request. The value of the ClientToken parameter is a unique string that is generated by your client and can contain up to 64 ASCII characters in length.
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def IsDelay(self):
        """Indicates whether to delay publishing. 1: delay; other values: do not delay
        :rtype: int
        """
        return self._IsDelay

    @IsDelay.setter
    def IsDelay(self, IsDelay):
        self._IsDelay = IsDelay


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SecurityGroupRule()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Type = params.get("Type")
        self._ClientToken = params.get("ClientToken")
        self._IsDelay = params.get("IsDelay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddEnterpriseSecurityGroupRulesResponse(AbstractModel):
    """AddEnterpriseSecurityGroupRules response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Status value. 0: added successfully; non-0: failed to add
        :type Status: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """Status value. 0: added successfully; non-0: failed to add
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class AddNatAcRuleRequest(AbstractModel):
    """AddNatAcRule request structure.

    """

    def __init__(self):
        r"""
        :param _Rules: NAT access control rules to be added.
        :type Rules: list of CreateNatRuleItem
        :param _From: Source of the rules to be added. Generally, this parameter is not used. The value insert_rule indicates that rules in the specified location are inserted, and the value batch_import indicates that rules are imported in batches. If the parameter is left empty, rules defined in the API request are added.
        :type From: str
        """
        self._Rules = None
        self._From = None

    @property
    def Rules(self):
        """NAT access control rules to be added.
        :rtype: list of CreateNatRuleItem
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def From(self):
        """Source of the rules to be added. Generally, this parameter is not used. The value insert_rule indicates that rules in the specified location are inserted, and the value batch_import indicates that rules are imported in batches. If the parameter is left empty, rules defined in the API request are added.
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = CreateNatRuleItem()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._From = params.get("From")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddNatAcRuleResponse(AbstractModel):
    """AddNatAcRule response structure.

    """

    def __init__(self):
        r"""
        :param _RuleUuid: ID list of new rules.
        :type RuleUuid: list of int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleUuid = None
        self._RequestId = None

    @property
    def RuleUuid(self):
        """ID list of new rules.
        :rtype: list of int
        """
        return self._RuleUuid

    @RuleUuid.setter
    def RuleUuid(self, RuleUuid):
        self._RuleUuid = RuleUuid

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleUuid = params.get("RuleUuid")
        self._RequestId = params.get("RequestId")


class AssetZone(AbstractModel):
    """AssetZone

    """

    def __init__(self):
        r"""
        :param _Zone: Region
        :type Zone: str
        :param _ZoneEng: Region
        :type ZoneEng: str
        """
        self._Zone = None
        self._ZoneEng = None

    @property
    def Zone(self):
        """Region
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneEng(self):
        """Region
        :rtype: str
        """
        return self._ZoneEng

    @ZoneEng.setter
    def ZoneEng(self, ZoneEng):
        self._ZoneEng = ZoneEng


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ZoneEng = params.get("ZoneEng")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociatedInstanceInfo(AbstractModel):
    """Instance associated with an enterprise security group

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
Note: This field may return `null`, indicating that no valid value was found.
        :type InstanceId: str
        :param _InstanceName: Instance name
Note: This field may return `null`, indicating that no valid value was found.
        :type InstanceName: str
        :param _Type: Instance type. 3: CVM instance; 4: CLB instance; 5: ENI instance; 6: Cloud database
Note: This field may return `null`, indicating that no valid value was found.
        :type Type: int
        :param _VpcId: VPC ID
Note: This field may return `null`, indicating that no valid value was found.
        :type VpcId: str
        :param _VpcName: VPC name
Note: This field may return `null`, indicating that no valid value was found.
        :type VpcName: str
        :param _PublicIp: Public IP
Note: This field may return `null`, indicating that no valid value was found.
        :type PublicIp: str
        :param _Ip: Private IP
Note: This field may return `null`, indicating that no valid value was found.
        :type Ip: str
        :param _SecurityGroupCount: The number of associated security groups
Note: This field may return `null`, indicating that no valid value was found.
        :type SecurityGroupCount: int
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Type = None
        self._VpcId = None
        self._VpcName = None
        self._PublicIp = None
        self._Ip = None
        self._SecurityGroupCount = None

    @property
    def InstanceId(self):
        """Instance ID
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """Instance name
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Type(self):
        """Instance type. 3: CVM instance; 4: CLB instance; 5: ENI instance; 6: Cloud database
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def VpcId(self):
        """VPC ID
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        """VPC name
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def PublicIp(self):
        """Public IP
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def Ip(self):
        """Private IP
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def SecurityGroupCount(self):
        """The number of associated security groups
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._SecurityGroupCount

    @SecurityGroupCount.setter
    def SecurityGroupCount(self, SecurityGroupCount):
        self._SecurityGroupCount = SecurityGroupCount


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Type = params.get("Type")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._PublicIp = params.get("PublicIp")
        self._Ip = params.get("Ip")
        self._SecurityGroupCount = params.get("SecurityGroupCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BetaInfoByACL(AbstractModel):
    """Canary publish information of the rule

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskId: int
        :param _TaskName: Task name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskName: str
        :param _LastTime: Last execution time
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastTime: str
        """
        self._TaskId = None
        self._TaskName = None
        self._LastTime = None

    @property
    def TaskId(self):
        """Task ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        """Task name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def LastTime(self):
        """Last execution time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LastTime

    @LastTime.setter
    def LastTime(self, LastTime):
        self._LastTime = LastTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._LastTime = params.get("LastTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BlockIgnoreRule(AbstractModel):
    """Allowlist or blocklist for intrusion prevention

    """

    def __init__(self):
        r"""
        :param _Domain: Domain name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param _Ioc: Rule IP.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Ioc: str
        :param _Level: Threat level.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Level: str
        :param _EventName: Source event name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EventName: str
        :param _Direction: Direction. Valid values: 0: outbound; 1: inbound.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Direction: int
        :param _Protocol: Protocol.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param _Address: Address.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Address: str
        :param _Action: Rule type. Valid values: 1: block; 2: allow.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Action: int
        :param _StartTime: Time when a rule starts to take effect.
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param _EndTime: Time when a rule expires.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        :param _IgnoreReason: Reason for ignoring.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IgnoreReason: str
        :param _Source: Security event source.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Source: str
        :param _UniqueId: Rule ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UniqueId: str
        :param _MatchTimes: Number of rule matching times.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MatchTimes: int
        :param _Country: Country.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Country: str
        :param _Comment: 
        :type Comment: str
        """
        self._Domain = None
        self._Ioc = None
        self._Level = None
        self._EventName = None
        self._Direction = None
        self._Protocol = None
        self._Address = None
        self._Action = None
        self._StartTime = None
        self._EndTime = None
        self._IgnoreReason = None
        self._Source = None
        self._UniqueId = None
        self._MatchTimes = None
        self._Country = None
        self._Comment = None

    @property
    def Domain(self):
        """Domain name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Ioc(self):
        """Rule IP.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Ioc

    @Ioc.setter
    def Ioc(self, Ioc):
        self._Ioc = Ioc

    @property
    def Level(self):
        """Threat level.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def EventName(self):
        """Source event name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EventName

    @EventName.setter
    def EventName(self, EventName):
        self._EventName = EventName

    @property
    def Direction(self):
        """Direction. Valid values: 0: outbound; 1: inbound.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Protocol(self):
        """Protocol.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Address(self):
        """Address.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Action(self):
        """Rule type. Valid values: 1: block; 2: allow.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def StartTime(self):
        """Time when a rule starts to take effect.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Time when a rule expires.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def IgnoreReason(self):
        """Reason for ignoring.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IgnoreReason

    @IgnoreReason.setter
    def IgnoreReason(self, IgnoreReason):
        self._IgnoreReason = IgnoreReason

    @property
    def Source(self):
        """Security event source.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def UniqueId(self):
        """Rule ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UniqueId

    @UniqueId.setter
    def UniqueId(self, UniqueId):
        self._UniqueId = UniqueId

    @property
    def MatchTimes(self):
        """Number of rule matching times.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MatchTimes

    @MatchTimes.setter
    def MatchTimes(self, MatchTimes):
        self._MatchTimes = MatchTimes

    @property
    def Country(self):
        """Country.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Comment(self):
        """
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Ioc = params.get("Ioc")
        self._Level = params.get("Level")
        self._EventName = params.get("EventName")
        self._Direction = params.get("Direction")
        self._Protocol = params.get("Protocol")
        self._Address = params.get("Address")
        self._Action = params.get("Action")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._IgnoreReason = params.get("IgnoreReason")
        self._Source = params.get("Source")
        self._UniqueId = params.get("UniqueId")
        self._MatchTimes = params.get("MatchTimes")
        self._Country = params.get("Country")
        self._Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CfwNatDnatRule(AbstractModel):
    """NAT firewall DNAT rules

    """

    def __init__(self):
        r"""
        :param _IpProtocol: Network protocol. Valid values: TCP or UDP.
        :type IpProtocol: str
        :param _PublicIpAddress: Elastic IP.
        :type PublicIpAddress: str
        :param _PublicPort: Public port.
        :type PublicPort: int
        :param _PrivateIpAddress: Private address.
        :type PrivateIpAddress: str
        :param _PrivatePort: Private port.
        :type PrivatePort: int
        :param _Description: The description of NAT firewall forwarding rules.
        :type Description: str
        """
        self._IpProtocol = None
        self._PublicIpAddress = None
        self._PublicPort = None
        self._PrivateIpAddress = None
        self._PrivatePort = None
        self._Description = None

    @property
    def IpProtocol(self):
        """Network protocol. Valid values: TCP or UDP.
        :rtype: str
        """
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def PublicIpAddress(self):
        """Elastic IP.
        :rtype: str
        """
        return self._PublicIpAddress

    @PublicIpAddress.setter
    def PublicIpAddress(self, PublicIpAddress):
        self._PublicIpAddress = PublicIpAddress

    @property
    def PublicPort(self):
        """Public port.
        :rtype: int
        """
        return self._PublicPort

    @PublicPort.setter
    def PublicPort(self, PublicPort):
        self._PublicPort = PublicPort

    @property
    def PrivateIpAddress(self):
        """Private address.
        :rtype: str
        """
        return self._PrivateIpAddress

    @PrivateIpAddress.setter
    def PrivateIpAddress(self, PrivateIpAddress):
        self._PrivateIpAddress = PrivateIpAddress

    @property
    def PrivatePort(self):
        """Private port.
        :rtype: int
        """
        return self._PrivatePort

    @PrivatePort.setter
    def PrivatePort(self, PrivatePort):
        self._PrivatePort = PrivatePort

    @property
    def Description(self):
        """The description of NAT firewall forwarding rules.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._IpProtocol = params.get("IpProtocol")
        self._PublicIpAddress = params.get("PublicIpAddress")
        self._PublicPort = params.get("PublicPort")
        self._PrivateIpAddress = params.get("PrivateIpAddress")
        self._PrivatePort = params.get("PrivatePort")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonFilter(AbstractModel):
    """Common filters for search

    """

    def __init__(self):
        r"""
        :param _Name: Search key.
        :type Name: str
        :param _Values: Search values.
        :type Values: list of str
        :param _OperatorType: Enum of integers that represent relations between Name and Values.
enum FilterOperatorType {
    // Invalid
    FILTER_OPERATOR_TYPE_INVALID = 0;
    // Equal to
    FILTER_OPERATOR_TYPE_EQUAL = 1;
    // Greater than
    FILTER_OPERATOR_TYPE_GREATER = 2;
    // Less than
    FILTER_OPERATOR_TYPE_LESS = 3;
    // Greater than or equal to
    FILTER_OPERATOR_TYPE_GREATER_EQ = 4;
    // Less than or equal to
    FILTER_OPERATOR_TYPE_LESS_EQ = 5;
    // Not equal to
    FILTER_OPERATOR_TYPE_NO_EQ = 6;
    // In (contained in the array)
    FILTER_OPERATOR_TYPE_IN = 7;
    // Not in
    FILTER_OPERATOR_TYPE_NOT_IN = 8;
    // Fuzzily matched
    FILTER_OPERATOR_TYPE_FUZZINESS = 9;
    // Existing
    FILTER_OPERATOR_TYPE_EXIST = 10;
    // Not existing
    FILTER_OPERATOR_TYPE_NOT_EXIST = 11;
    // Regular
    FILTER_OPERATOR_TYPE_REGULAR = 12;
}
        :type OperatorType: int
        """
        self._Name = None
        self._Values = None
        self._OperatorType = None

    @property
    def Name(self):
        """Search key.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """Search values.
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def OperatorType(self):
        """Enum of integers that represent relations between Name and Values.
enum FilterOperatorType {
    // Invalid
    FILTER_OPERATOR_TYPE_INVALID = 0;
    // Equal to
    FILTER_OPERATOR_TYPE_EQUAL = 1;
    // Greater than
    FILTER_OPERATOR_TYPE_GREATER = 2;
    // Less than
    FILTER_OPERATOR_TYPE_LESS = 3;
    // Greater than or equal to
    FILTER_OPERATOR_TYPE_GREATER_EQ = 4;
    // Less than or equal to
    FILTER_OPERATOR_TYPE_LESS_EQ = 5;
    // Not equal to
    FILTER_OPERATOR_TYPE_NO_EQ = 6;
    // In (contained in the array)
    FILTER_OPERATOR_TYPE_IN = 7;
    // Not in
    FILTER_OPERATOR_TYPE_NOT_IN = 8;
    // Fuzzily matched
    FILTER_OPERATOR_TYPE_FUZZINESS = 9;
    // Existing
    FILTER_OPERATOR_TYPE_EXIST = 10;
    // Not existing
    FILTER_OPERATOR_TYPE_NOT_EXIST = 11;
    // Regular
    FILTER_OPERATOR_TYPE_REGULAR = 12;
}
        :rtype: int
        """
        return self._OperatorType

    @OperatorType.setter
    def OperatorType(self, OperatorType):
        self._OperatorType = OperatorType


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        self._OperatorType = params.get("OperatorType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAcRulesRequest(AbstractModel):
    """CreateAcRules request structure.

    """

    def __init__(self):
        r"""
        :param _Data: Creates rule data
        :type Data: list of RuleInfoData
        :param _Type: 0: add (default); 1: insert
        :type Type: int
        :param _EdgeId: Edge ID
        :type EdgeId: str
        :param _Enable: Access control rule status
        :type Enable: int
        :param _Overwrite: 0: add; 1: overwrite
        :type Overwrite: int
        :param _InstanceId: NAT instance ID, required when the parameter Area exists
        :type InstanceId: str
        :param _From: portScan: from port scanning; patchImport: from batch import
        :type From: str
        :param _Area: NAT region
        :type Area: str
        """
        self._Data = None
        self._Type = None
        self._EdgeId = None
        self._Enable = None
        self._Overwrite = None
        self._InstanceId = None
        self._From = None
        self._Area = None

    @property
    def Data(self):
        """Creates rule data
        :rtype: list of RuleInfoData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Type(self):
        """0: add (default); 1: insert
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EdgeId(self):
        """Edge ID
        :rtype: str
        """
        return self._EdgeId

    @EdgeId.setter
    def EdgeId(self, EdgeId):
        self._EdgeId = EdgeId

    @property
    def Enable(self):
        """Access control rule status
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Overwrite(self):
        """0: add; 1: overwrite
        :rtype: int
        """
        return self._Overwrite

    @Overwrite.setter
    def Overwrite(self, Overwrite):
        self._Overwrite = Overwrite

    @property
    def InstanceId(self):
        """NAT instance ID, required when the parameter Area exists
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def From(self):
        """portScan: from port scanning; patchImport: from batch import
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Area(self):
        """NAT region
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = RuleInfoData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Type = params.get("Type")
        self._EdgeId = params.get("EdgeId")
        self._Enable = params.get("Enable")
        self._Overwrite = params.get("Overwrite")
        self._InstanceId = params.get("InstanceId")
        self._From = params.get("From")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAcRulesResponse(AbstractModel):
    """CreateAcRules response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Status value. 0: operation successful
        :type Status: int
        :param _Info: Returns redundant information
Note: This field may return `null`, indicating that no valid value was found.
        :type Info: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._Info = None
        self._RequestId = None

    @property
    def Status(self):
        """Status value. 0: operation successful
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Info(self):
        """Returns redundant information
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Info = params.get("Info")
        self._RequestId = params.get("RequestId")


class CreateNatFwInstanceRequest(AbstractModel):
    """CreateNatFwInstance request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Firewall instance name
        :type Name: str
        :param _Width: Bandwidth
        :type Width: int
        :param _Mode: Mode. 1: use existing; 0: create new
        :type Mode: int
        :param _NewModeItems: Parameter passed for the Create New mode. Either NewModeItems or NatgwList is required.
        :type NewModeItems: :class:`tencentcloud.cfw.v20190904.models.NewModeItems`
        :param _NatGwList: NAT gateway list for the Using Existing mode. Either NewModeItems or NatgwList is required.
        :type NatGwList: list of str
        :param _Zone: Primary zone. The default zone is selected if it is empty.
        :type Zone: str
        :param _ZoneBak: Secondary zone. The default zone is selected if it is empty.
        :type ZoneBak: str
        :param _CrossAZone: Remote disaster recovery. 1: enable; 0: disable; empty: disable by default
        :type CrossAZone: int
        :param _FwCidrInfo: IP range of the firewall
        :type FwCidrInfo: :class:`tencentcloud.cfw.v20190904.models.FwCidrInfo`
        """
        self._Name = None
        self._Width = None
        self._Mode = None
        self._NewModeItems = None
        self._NatGwList = None
        self._Zone = None
        self._ZoneBak = None
        self._CrossAZone = None
        self._FwCidrInfo = None

    @property
    def Name(self):
        """Firewall instance name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Width(self):
        """Bandwidth
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Mode(self):
        """Mode. 1: use existing; 0: create new
        :rtype: int
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def NewModeItems(self):
        """Parameter passed for the Create New mode. Either NewModeItems or NatgwList is required.
        :rtype: :class:`tencentcloud.cfw.v20190904.models.NewModeItems`
        """
        return self._NewModeItems

    @NewModeItems.setter
    def NewModeItems(self, NewModeItems):
        self._NewModeItems = NewModeItems

    @property
    def NatGwList(self):
        """NAT gateway list for the Using Existing mode. Either NewModeItems or NatgwList is required.
        :rtype: list of str
        """
        return self._NatGwList

    @NatGwList.setter
    def NatGwList(self, NatGwList):
        self._NatGwList = NatGwList

    @property
    def Zone(self):
        """Primary zone. The default zone is selected if it is empty.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneBak(self):
        """Secondary zone. The default zone is selected if it is empty.
        :rtype: str
        """
        return self._ZoneBak

    @ZoneBak.setter
    def ZoneBak(self, ZoneBak):
        self._ZoneBak = ZoneBak

    @property
    def CrossAZone(self):
        """Remote disaster recovery. 1: enable; 0: disable; empty: disable by default
        :rtype: int
        """
        return self._CrossAZone

    @CrossAZone.setter
    def CrossAZone(self, CrossAZone):
        self._CrossAZone = CrossAZone

    @property
    def FwCidrInfo(self):
        """IP range of the firewall
        :rtype: :class:`tencentcloud.cfw.v20190904.models.FwCidrInfo`
        """
        return self._FwCidrInfo

    @FwCidrInfo.setter
    def FwCidrInfo(self, FwCidrInfo):
        self._FwCidrInfo = FwCidrInfo


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Width = params.get("Width")
        self._Mode = params.get("Mode")
        if params.get("NewModeItems") is not None:
            self._NewModeItems = NewModeItems()
            self._NewModeItems._deserialize(params.get("NewModeItems"))
        self._NatGwList = params.get("NatGwList")
        self._Zone = params.get("Zone")
        self._ZoneBak = params.get("ZoneBak")
        self._CrossAZone = params.get("CrossAZone")
        if params.get("FwCidrInfo") is not None:
            self._FwCidrInfo = FwCidrInfo()
            self._FwCidrInfo._deserialize(params.get("FwCidrInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNatFwInstanceResponse(AbstractModel):
    """CreateNatFwInstance response structure.

    """

    def __init__(self):
        r"""
        :param _CfwInsId: Firewall instance ID
        :type CfwInsId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CfwInsId = None
        self._RequestId = None

    @property
    def CfwInsId(self):
        """Firewall instance ID
        :rtype: str
        """
        return self._CfwInsId

    @CfwInsId.setter
    def CfwInsId(self, CfwInsId):
        self._CfwInsId = CfwInsId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CfwInsId = params.get("CfwInsId")
        self._RequestId = params.get("RequestId")


class CreateNatFwInstanceWithDomainRequest(AbstractModel):
    """CreateNatFwInstanceWithDomain request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Firewall instance name
        :type Name: str
        :param _Width: Bandwidth
        :type Width: int
        :param _Mode: Mode. 1: use existing; 0: create new
        :type Mode: int
        :param _NewModeItems: Parameter passed for the Create New mode. Either NewModeItems or NatgwList is required.
        :type NewModeItems: :class:`tencentcloud.cfw.v20190904.models.NewModeItems`
        :param _NatGwList: NAT gateway list for the Using Existing mode. Either NewModeItems or NatgwList is required.
        :type NatGwList: list of str
        :param _Zone: Primary zone. The default zone is selected if it is empty.
        :type Zone: str
        :param _ZoneBak: Secondary zone. The default zone is selected if it is empty.
        :type ZoneBak: str
        :param _CrossAZone: Remote disaster recovery. 1: enable; 0: disable; empty: disable by default
        :type CrossAZone: int
        :param _IsCreateDomain: 0: not create; 1: create
        :type IsCreateDomain: int
        :param _Domain: Required for creating a domain name
        :type Domain: str
        :param _FwCidrInfo: IP range of the firewall
        :type FwCidrInfo: :class:`tencentcloud.cfw.v20190904.models.FwCidrInfo`
        """
        self._Name = None
        self._Width = None
        self._Mode = None
        self._NewModeItems = None
        self._NatGwList = None
        self._Zone = None
        self._ZoneBak = None
        self._CrossAZone = None
        self._IsCreateDomain = None
        self._Domain = None
        self._FwCidrInfo = None

    @property
    def Name(self):
        """Firewall instance name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Width(self):
        """Bandwidth
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Mode(self):
        """Mode. 1: use existing; 0: create new
        :rtype: int
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def NewModeItems(self):
        """Parameter passed for the Create New mode. Either NewModeItems or NatgwList is required.
        :rtype: :class:`tencentcloud.cfw.v20190904.models.NewModeItems`
        """
        return self._NewModeItems

    @NewModeItems.setter
    def NewModeItems(self, NewModeItems):
        self._NewModeItems = NewModeItems

    @property
    def NatGwList(self):
        """NAT gateway list for the Using Existing mode. Either NewModeItems or NatgwList is required.
        :rtype: list of str
        """
        return self._NatGwList

    @NatGwList.setter
    def NatGwList(self, NatGwList):
        self._NatGwList = NatGwList

    @property
    def Zone(self):
        """Primary zone. The default zone is selected if it is empty.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneBak(self):
        """Secondary zone. The default zone is selected if it is empty.
        :rtype: str
        """
        return self._ZoneBak

    @ZoneBak.setter
    def ZoneBak(self, ZoneBak):
        self._ZoneBak = ZoneBak

    @property
    def CrossAZone(self):
        """Remote disaster recovery. 1: enable; 0: disable; empty: disable by default
        :rtype: int
        """
        return self._CrossAZone

    @CrossAZone.setter
    def CrossAZone(self, CrossAZone):
        self._CrossAZone = CrossAZone

    @property
    def IsCreateDomain(self):
        """0: not create; 1: create
        :rtype: int
        """
        return self._IsCreateDomain

    @IsCreateDomain.setter
    def IsCreateDomain(self, IsCreateDomain):
        self._IsCreateDomain = IsCreateDomain

    @property
    def Domain(self):
        """Required for creating a domain name
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def FwCidrInfo(self):
        """IP range of the firewall
        :rtype: :class:`tencentcloud.cfw.v20190904.models.FwCidrInfo`
        """
        return self._FwCidrInfo

    @FwCidrInfo.setter
    def FwCidrInfo(self, FwCidrInfo):
        self._FwCidrInfo = FwCidrInfo


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Width = params.get("Width")
        self._Mode = params.get("Mode")
        if params.get("NewModeItems") is not None:
            self._NewModeItems = NewModeItems()
            self._NewModeItems._deserialize(params.get("NewModeItems"))
        self._NatGwList = params.get("NatGwList")
        self._Zone = params.get("Zone")
        self._ZoneBak = params.get("ZoneBak")
        self._CrossAZone = params.get("CrossAZone")
        self._IsCreateDomain = params.get("IsCreateDomain")
        self._Domain = params.get("Domain")
        if params.get("FwCidrInfo") is not None:
            self._FwCidrInfo = FwCidrInfo()
            self._FwCidrInfo._deserialize(params.get("FwCidrInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNatFwInstanceWithDomainResponse(AbstractModel):
    """CreateNatFwInstanceWithDomain response structure.

    """

    def __init__(self):
        r"""
        :param _CfwInsId: NAT instance info
Note: This field may return `null`, indicating that no valid value was found.
        :type CfwInsId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CfwInsId = None
        self._RequestId = None

    @property
    def CfwInsId(self):
        """NAT instance info
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._CfwInsId

    @CfwInsId.setter
    def CfwInsId(self, CfwInsId):
        self._CfwInsId = CfwInsId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CfwInsId = params.get("CfwInsId")
        self._RequestId = params.get("RequestId")


class CreateNatRuleItem(AbstractModel):
    """Parameters for creating an NAT access control rule

    """

    def __init__(self):
        r"""
        :param _SourceContent: Access source. Example: `net: IP/CIDR(192.168.0.2)`
        :type SourceContent: str
        :param _SourceType: Access source type. Values for inbound rules: `ip`, `net`, `template`, and `location`. Values for outbound rules: `ip`, `net`, `template`, `instance`, `group`, and `tag`.
        :type SourceType: str
        :param _TargetContent: Access target. Example: `net: IP/CIDR(192.168.0.2); domain: domain name rule, e.g., *.qq.com
        :type TargetContent: str
        :param _TargetType: Access target type. Values for inbound rules: `ip`, `net`, `template`, `instance`, `group`, and `tag`. Values for outbound rules: `ip`, `net`, `domain`, `template`, and `location`.
        :type TargetType: str
        :param _Protocol: Protocol. Values: `TCP`, `UDP`, `ICMP`, `ANY`, `HTTP`, `HTTPS`, `HTTP/HTTPS`, `SMTP`, `SMTPS`, `SMTP/SMTPS`, `FTP`, and `DNS`.
        :type Protocol: str
        :param _RuleAction: Specify how the CFW instance deals with the traffic hit the access control rule. Values: `accept` (allow), `drop` (reject), and `log` (observe).
        :type RuleAction: str
        :param _Port: The port of the access control rule. Values: `-1/-1` (all ports) and `80` (Port 80)
        :type Port: str
        :param _Direction: Rule direction. Values: `1` (Inbound) and `0` (Outbound)
        :type Direction: int
        :param _OrderIndex: Rule sequence number
        :type OrderIndex: int
        :param _Enable: Rule status. `true` (Enabled); `false` (Disabled)
        :type Enable: str
        :param _Uuid: The unique ID of the rule, which is not required when you create a rule.
        :type Uuid: int
        :param _Description: Description
        :type Description: str
        """
        self._SourceContent = None
        self._SourceType = None
        self._TargetContent = None
        self._TargetType = None
        self._Protocol = None
        self._RuleAction = None
        self._Port = None
        self._Direction = None
        self._OrderIndex = None
        self._Enable = None
        self._Uuid = None
        self._Description = None

    @property
    def SourceContent(self):
        """Access source. Example: `net: IP/CIDR(192.168.0.2)`
        :rtype: str
        """
        return self._SourceContent

    @SourceContent.setter
    def SourceContent(self, SourceContent):
        self._SourceContent = SourceContent

    @property
    def SourceType(self):
        """Access source type. Values for inbound rules: `ip`, `net`, `template`, and `location`. Values for outbound rules: `ip`, `net`, `template`, `instance`, `group`, and `tag`.
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def TargetContent(self):
        """Access target. Example: `net: IP/CIDR(192.168.0.2); domain: domain name rule, e.g., *.qq.com
        :rtype: str
        """
        return self._TargetContent

    @TargetContent.setter
    def TargetContent(self, TargetContent):
        self._TargetContent = TargetContent

    @property
    def TargetType(self):
        """Access target type. Values for inbound rules: `ip`, `net`, `template`, `instance`, `group`, and `tag`. Values for outbound rules: `ip`, `net`, `domain`, `template`, and `location`.
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def Protocol(self):
        """Protocol. Values: `TCP`, `UDP`, `ICMP`, `ANY`, `HTTP`, `HTTPS`, `HTTP/HTTPS`, `SMTP`, `SMTPS`, `SMTP/SMTPS`, `FTP`, and `DNS`.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def RuleAction(self):
        """Specify how the CFW instance deals with the traffic hit the access control rule. Values: `accept` (allow), `drop` (reject), and `log` (observe).
        :rtype: str
        """
        return self._RuleAction

    @RuleAction.setter
    def RuleAction(self, RuleAction):
        self._RuleAction = RuleAction

    @property
    def Port(self):
        """The port of the access control rule. Values: `-1/-1` (all ports) and `80` (Port 80)
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Direction(self):
        """Rule direction. Values: `1` (Inbound) and `0` (Outbound)
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def OrderIndex(self):
        """Rule sequence number
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def Enable(self):
        """Rule status. `true` (Enabled); `false` (Disabled)
        :rtype: str
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Uuid(self):
        """The unique ID of the rule, which is not required when you create a rule.
        :rtype: int
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Description(self):
        """Description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._SourceContent = params.get("SourceContent")
        self._SourceType = params.get("SourceType")
        self._TargetContent = params.get("TargetContent")
        self._TargetType = params.get("TargetType")
        self._Protocol = params.get("Protocol")
        self._RuleAction = params.get("RuleAction")
        self._Port = params.get("Port")
        self._Direction = params.get("Direction")
        self._OrderIndex = params.get("OrderIndex")
        self._Enable = params.get("Enable")
        self._Uuid = params.get("Uuid")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityGroupRulesRequest(AbstractModel):
    """CreateSecurityGroupRules request structure.

    """

    def __init__(self):
        r"""
        :param _Data: Added enterprise security group rule data
        :type Data: list of SecurityGroupListData
        :param _Direction: Direction. 0: outbound; 1: inbound. 1 by default
        :type Direction: int
        :param _Type: 0: at the end; 1: at the top; 2: in the middle. 0 by default
        :type Type: int
        :param _Enable: Indicates whether to enable rules after addition. 0: disable; 1: enable. 1 by default
        :type Enable: int
        """
        self._Data = None
        self._Direction = None
        self._Type = None
        self._Enable = None

    @property
    def Data(self):
        """Added enterprise security group rule data
        :rtype: list of SecurityGroupListData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Direction(self):
        """Direction. 0: outbound; 1: inbound. 1 by default
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Type(self):
        """0: at the end; 1: at the top; 2: in the middle. 0 by default
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Enable(self):
        """Indicates whether to enable rules after addition. 0: disable; 1: enable. 1 by default
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SecurityGroupListData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Direction = params.get("Direction")
        self._Type = params.get("Type")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityGroupRulesResponse(AbstractModel):
    """CreateSecurityGroupRules response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Status value. 0: added successfully; non-0: failed to add
        :type Status: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """Status value. 0: added successfully; non-0: failed to add
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DeleteAcRuleRequest(AbstractModel):
    """DeleteAcRule request structure.

    """

    def __init__(self):
        r"""
        :param _Id: The ID of the rule to delete. It can be queried via the DescribeAcLists API.
        :type Id: int
        :param _Direction: Direction. 0: outbound; 1: inbound
        :type Direction: int
        :param _EdgeId: Edge ID between two VPCs
        :type EdgeId: str
        :param _Area: NAT region, e.g. ap-shanghai/ap-guangzhou/ap-chongqing
        :type Area: str
        """
        self._Id = None
        self._Direction = None
        self._EdgeId = None
        self._Area = None

    @property
    def Id(self):
        """The ID of the rule to delete. It can be queried via the DescribeAcLists API.
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Direction(self):
        """Direction. 0: outbound; 1: inbound
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def EdgeId(self):
        """Edge ID between two VPCs
        :rtype: str
        """
        return self._EdgeId

    @EdgeId.setter
    def EdgeId(self, EdgeId):
        self._EdgeId = EdgeId

    @property
    def Area(self):
        """NAT region, e.g. ap-shanghai/ap-guangzhou/ap-chongqing
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Direction = params.get("Direction")
        self._EdgeId = params.get("EdgeId")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAcRuleResponse(AbstractModel):
    """DeleteAcRule response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Status value. 0: deleted successfully; !0: deletion failed
        :type Status: int
        :param _Info: Returns redundant information
Note: This field may return `null`, indicating that no valid value was found.
        :type Info: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._Info = None
        self._RequestId = None

    @property
    def Status(self):
        """Status value. 0: deleted successfully; !0: deletion failed
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Info(self):
        """Returns redundant information
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Info = params.get("Info")
        self._RequestId = params.get("RequestId")


class DeleteAllAccessControlRuleRequest(AbstractModel):
    """DeleteAllAccessControlRule request structure.

    """

    def __init__(self):
        r"""
        :param _Direction: Direction. 0: outbound; 1: inbound. 0 by default
        :type Direction: int
        :param _EdgeId: Deletes all the access control rules for inter-VPC firewall toggles associated with the EdgeId. It is empty by default. Enter either EdgeId or Area.
        :type EdgeId: str
        :param _Area: Deletes all the access control rules for NAT firewalls of this region. It is empty by default. Enter either EdgeId or Area.
        :type Area: str
        """
        self._Direction = None
        self._EdgeId = None
        self._Area = None

    @property
    def Direction(self):
        """Direction. 0: outbound; 1: inbound. 0 by default
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def EdgeId(self):
        """Deletes all the access control rules for inter-VPC firewall toggles associated with the EdgeId. It is empty by default. Enter either EdgeId or Area.
        :rtype: str
        """
        return self._EdgeId

    @EdgeId.setter
    def EdgeId(self, EdgeId):
        self._EdgeId = EdgeId

    @property
    def Area(self):
        """Deletes all the access control rules for NAT firewalls of this region. It is empty by default. Enter either EdgeId or Area.
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._Direction = params.get("Direction")
        self._EdgeId = params.get("EdgeId")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAllAccessControlRuleResponse(AbstractModel):
    """DeleteAllAccessControlRule response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Status of the task. `0`: Modified successfully; Others: Modification failed
        :type Status: int
        :param _Info: Number of access control rules deleted.
Note: This field may return `null`, indicating that no valid value was found.
        :type Info: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._Info = None
        self._RequestId = None

    @property
    def Status(self):
        """Status of the task. `0`: Modified successfully; Others: Modification failed
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Info(self):
        """Number of access control rules deleted.
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Info = params.get("Info")
        self._RequestId = params.get("RequestId")


class DeleteResourceGroupRequest(AbstractModel):
    """DeleteResourceGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Group ID
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        """Group ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteResourceGroupResponse(AbstractModel):
    """DeleteResourceGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteSecurityGroupRuleRequest(AbstractModel):
    """DeleteSecurityGroupRule request structure.

    """

    def __init__(self):
        r"""
        :param _Id: ID of the rule to delete
        :type Id: int
        :param _Area: Tencent Cloud region (abbreviation)
        :type Area: str
        :param _Direction: Direction. 0: outbound; 1: inbound
        :type Direction: int
        :param _IsDelReverse: Indicates whether to delete the reverse rule. 0: no; 1: yes
        :type IsDelReverse: int
        """
        self._Id = None
        self._Area = None
        self._Direction = None
        self._IsDelReverse = None

    @property
    def Id(self):
        """ID of the rule to delete
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Area(self):
        """Tencent Cloud region (abbreviation)
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Direction(self):
        """Direction. 0: outbound; 1: inbound
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def IsDelReverse(self):
        """Indicates whether to delete the reverse rule. 0: no; 1: yes
        :rtype: int
        """
        return self._IsDelReverse

    @IsDelReverse.setter
    def IsDelReverse(self, IsDelReverse):
        self._IsDelReverse = IsDelReverse


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Area = params.get("Area")
        self._Direction = params.get("Direction")
        self._IsDelReverse = params.get("IsDelReverse")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityGroupRuleResponse(AbstractModel):
    """DeleteSecurityGroupRule response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Status value. 0: operation successful; non-0: operation failed
        :type Status: int
        :param _Info: Returns redundant information
Note: This field may return `null`, indicating that no valid value was found.
        :type Info: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._Info = None
        self._RequestId = None

    @property
    def Status(self):
        """Status value. 0: operation successful; non-0: operation failed
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Info(self):
        """Returns redundant information
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Info = params.get("Info")
        self._RequestId = params.get("RequestId")


class DeleteVpcInstanceRequest(AbstractModel):
    """DeleteVpcInstance request structure.

    """


class DeleteVpcInstanceResponse(AbstractModel):
    """DeleteVpcInstance response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescAcItem(AbstractModel):
    """Item in the access control list. Each item represents an access control rule.

    """

    def __init__(self):
        r"""
        :param _SourceContent: Access source.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SourceContent: str
        :param _TargetContent: Access destination.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetContent: str
        :param _Protocol: Protocol.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param _Port: Port.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Port: str
        :param _RuleAction: Action that Cloud Firewall performs on the traffic. Valid values: accept (allow), drop (reject), and log (monitor).
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleAction: str
        :param _Description: Description.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _Count: Number of rule matching times.
        :type Count: int
        :param _OrderIndex: Rule sequence number.
        :type OrderIndex: int
        :param _SourceType: Access source type. Valid values for an inbound rule: ip, net, template, and location; valid values for an outbound rule: ip, net, template, instance, group, and tag.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SourceType: str
        :param _TargetType: Access destination type. Valid values for an inbound rule: ip, net, template, instance, group, and tag; valid values for an outbound rule: ip, net, domain, template, and location.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetType: str
        :param _Uuid: Unique ID of the rule.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Uuid: int
        :param _Invalid: Rule validity.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Invalid: int
        :param _IsRegion: Valid values: 0: common rules; 1: regional rules.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsRegion: int
        :param _CountryCode: Country ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CountryCode: int
        :param _CityCode: City ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CityCode: int
        :param _CountryName: Country name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CountryName: str
        :param _CityName: City name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CityName: str
        :param _CloudCode: Cloud provider code.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CloudCode: str
        :param _IsCloud: Valid values: 0: common rules; 1: cloud provider rules.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsCloud: int
        :param _Enable: Rule status. Valid values: true: enabled; false: disabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Enable: str
        :param _Direction: Rule direction. Valid values: 1: inbound; 0: outbound.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Direction: int
        :param _InstanceName: Instance name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param _InternalUuid: UUID for internal use. Generally, this field is not required.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InternalUuid: int
        :param _Status: Rule status. This field is valid when you query rule matching details. Valid values: 0: new; 1: deleted; 2: edited and deleted.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _BetaList: Details of associated tasks
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type BetaList: list of BetaInfoByACL
        """
        self._SourceContent = None
        self._TargetContent = None
        self._Protocol = None
        self._Port = None
        self._RuleAction = None
        self._Description = None
        self._Count = None
        self._OrderIndex = None
        self._SourceType = None
        self._TargetType = None
        self._Uuid = None
        self._Invalid = None
        self._IsRegion = None
        self._CountryCode = None
        self._CityCode = None
        self._CountryName = None
        self._CityName = None
        self._CloudCode = None
        self._IsCloud = None
        self._Enable = None
        self._Direction = None
        self._InstanceName = None
        self._InternalUuid = None
        self._Status = None
        self._BetaList = None

    @property
    def SourceContent(self):
        """Access source.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SourceContent

    @SourceContent.setter
    def SourceContent(self, SourceContent):
        self._SourceContent = SourceContent

    @property
    def TargetContent(self):
        """Access destination.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TargetContent

    @TargetContent.setter
    def TargetContent(self, TargetContent):
        self._TargetContent = TargetContent

    @property
    def Protocol(self):
        """Protocol.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        """Port.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def RuleAction(self):
        """Action that Cloud Firewall performs on the traffic. Valid values: accept (allow), drop (reject), and log (monitor).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RuleAction

    @RuleAction.setter
    def RuleAction(self, RuleAction):
        self._RuleAction = RuleAction

    @property
    def Description(self):
        """Description.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Count(self):
        """Number of rule matching times.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def OrderIndex(self):
        """Rule sequence number.
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def SourceType(self):
        """Access source type. Valid values for an inbound rule: ip, net, template, and location; valid values for an outbound rule: ip, net, template, instance, group, and tag.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def TargetType(self):
        """Access destination type. Valid values for an inbound rule: ip, net, template, instance, group, and tag; valid values for an outbound rule: ip, net, domain, template, and location.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def Uuid(self):
        """Unique ID of the rule.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Invalid(self):
        """Rule validity.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Invalid

    @Invalid.setter
    def Invalid(self, Invalid):
        self._Invalid = Invalid

    @property
    def IsRegion(self):
        """Valid values: 0: common rules; 1: regional rules.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsRegion

    @IsRegion.setter
    def IsRegion(self, IsRegion):
        self._IsRegion = IsRegion

    @property
    def CountryCode(self):
        """Country ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def CityCode(self):
        """City ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CityCode

    @CityCode.setter
    def CityCode(self, CityCode):
        self._CityCode = CityCode

    @property
    def CountryName(self):
        """Country name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CountryName

    @CountryName.setter
    def CountryName(self, CountryName):
        self._CountryName = CountryName

    @property
    def CityName(self):
        """City name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CityName

    @CityName.setter
    def CityName(self, CityName):
        self._CityName = CityName

    @property
    def CloudCode(self):
        """Cloud provider code.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CloudCode

    @CloudCode.setter
    def CloudCode(self, CloudCode):
        self._CloudCode = CloudCode

    @property
    def IsCloud(self):
        """Valid values: 0: common rules; 1: cloud provider rules.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsCloud

    @IsCloud.setter
    def IsCloud(self, IsCloud):
        self._IsCloud = IsCloud

    @property
    def Enable(self):
        """Rule status. Valid values: true: enabled; false: disabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Direction(self):
        """Rule direction. Valid values: 1: inbound; 0: outbound.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def InstanceName(self):
        """Instance name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InternalUuid(self):
        """UUID for internal use. Generally, this field is not required.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._InternalUuid

    @InternalUuid.setter
    def InternalUuid(self, InternalUuid):
        self._InternalUuid = InternalUuid

    @property
    def Status(self):
        """Rule status. This field is valid when you query rule matching details. Valid values: 0: new; 1: deleted; 2: edited and deleted.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BetaList(self):
        """Details of associated tasks
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: list of BetaInfoByACL
        """
        return self._BetaList

    @BetaList.setter
    def BetaList(self, BetaList):
        self._BetaList = BetaList


    def _deserialize(self, params):
        self._SourceContent = params.get("SourceContent")
        self._TargetContent = params.get("TargetContent")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._RuleAction = params.get("RuleAction")
        self._Description = params.get("Description")
        self._Count = params.get("Count")
        self._OrderIndex = params.get("OrderIndex")
        self._SourceType = params.get("SourceType")
        self._TargetType = params.get("TargetType")
        self._Uuid = params.get("Uuid")
        self._Invalid = params.get("Invalid")
        self._IsRegion = params.get("IsRegion")
        self._CountryCode = params.get("CountryCode")
        self._CityCode = params.get("CityCode")
        self._CountryName = params.get("CountryName")
        self._CityName = params.get("CityName")
        self._CloudCode = params.get("CloudCode")
        self._IsCloud = params.get("IsCloud")
        self._Enable = params.get("Enable")
        self._Direction = params.get("Direction")
        self._InstanceName = params.get("InstanceName")
        self._InternalUuid = params.get("InternalUuid")
        self._Status = params.get("Status")
        if params.get("BetaList") is not None:
            self._BetaList = []
            for item in params.get("BetaList"):
                obj = BetaInfoByACL()
                obj._deserialize(item)
                self._BetaList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAcListsRequest(AbstractModel):
    """DescribeAcLists request structure.

    """

    def __init__(self):
        r"""
        :param _Protocol: Protocol
        :type Protocol: str
        :param _Strategy: Policy
        :type Strategy: str
        :param _SearchValue: Search value
        :type SearchValue: str
        :param _Limit: Number of entries per page
        :type Limit: int
        :param _Offset: Offset
        :type Offset: int
        :param _Direction: Indicates whether it is outbound or inbound. 1: inbound; 0: outbound
        :type Direction: int
        :param _EdgeId: EdgeId value
        :type EdgeId: str
        :param _Status: Indicates whether the rule is enabled. '0': disabled; '1': enabled. '0' by default
        :type Status: str
        :param _Area: Region
        :type Area: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        """
        self._Protocol = None
        self._Strategy = None
        self._SearchValue = None
        self._Limit = None
        self._Offset = None
        self._Direction = None
        self._EdgeId = None
        self._Status = None
        self._Area = None
        self._InstanceId = None

    @property
    def Protocol(self):
        """Protocol
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Strategy(self):
        """Policy
        :rtype: str
        """
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def SearchValue(self):
        """Search value
        :rtype: str
        """
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue

    @property
    def Limit(self):
        """Number of entries per page
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Direction(self):
        """Indicates whether it is outbound or inbound. 1: inbound; 0: outbound
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def EdgeId(self):
        """EdgeId value
        :rtype: str
        """
        return self._EdgeId

    @EdgeId.setter
    def EdgeId(self, EdgeId):
        self._EdgeId = EdgeId

    @property
    def Status(self):
        """Indicates whether the rule is enabled. '0': disabled; '1': enabled. '0' by default
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Area(self):
        """Region
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def InstanceId(self):
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._Strategy = params.get("Strategy")
        self._SearchValue = params.get("SearchValue")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Direction = params.get("Direction")
        self._EdgeId = params.get("EdgeId")
        self._Status = params.get("Status")
        self._Area = params.get("Area")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAcListsResponse(AbstractModel):
    """DescribeAcLists response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total entries
        :type Total: int
        :param _Data: Access control list data
        :type Data: list of AcListsData
        :param _AllTotal: Total entries excluding the filtered ones
        :type AllTotal: int
        :param _Enable: All access control rules enabled/disabled
Note: This field may return `null`, indicating that no valid value was found.
        :type Enable: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._AllTotal = None
        self._Enable = None
        self._RequestId = None

    @property
    def Total(self):
        """Total entries
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        """Access control list data
        :rtype: list of AcListsData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def AllTotal(self):
        """Total entries excluding the filtered ones
        :rtype: int
        """
        return self._AllTotal

    @AllTotal.setter
    def AllTotal(self, AllTotal):
        self._AllTotal = AllTotal

    @property
    def Enable(self):
        """All access control rules enabled/disabled
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AcListsData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._AllTotal = params.get("AllTotal")
        self._Enable = params.get("Enable")
        self._RequestId = params.get("RequestId")


class DescribeAssociatedInstanceListRequest(AbstractModel):
    """DescribeAssociatedInstanceList request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: List offset
        :type Offset: int
        :param _Limit: Number of records per page
        :type Limit: int
        :param _Area: Region code (e.g. ap-guangzhou). All Tencent Cloud regions are supported.
        :type Area: str
        :param _SearchValue: Additional search criteria (JSON string)
        :type SearchValue: str
        :param _By: Sorting field
        :type By: str
        :param _Order: Sort order. asc: ascending; desc: descending
        :type Order: str
        :param _SecurityGroupId: Security group ID
        :type SecurityGroupId: str
        :param _Type: Instance type. '3': CVM instance; '4': CLB instance; '5': ENI instance; '6': Cloud database
        :type Type: str
        """
        self._Offset = None
        self._Limit = None
        self._Area = None
        self._SearchValue = None
        self._By = None
        self._Order = None
        self._SecurityGroupId = None
        self._Type = None

    @property
    def Offset(self):
        """List offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of records per page
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Area(self):
        """Region code (e.g. ap-guangzhou). All Tencent Cloud regions are supported.
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def SearchValue(self):
        """Additional search criteria (JSON string)
        :rtype: str
        """
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue

    @property
    def By(self):
        """Sorting field
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By

    @property
    def Order(self):
        """Sort order. asc: ascending; desc: descending
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def SecurityGroupId(self):
        """Security group ID
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def Type(self):
        """Instance type. '3': CVM instance; '4': CLB instance; '5': ENI instance; '6': Cloud database
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Area = params.get("Area")
        self._SearchValue = params.get("SearchValue")
        self._By = params.get("By")
        self._Order = params.get("Order")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssociatedInstanceListResponse(AbstractModel):
    """DescribeAssociatedInstanceList response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Number of instances
Note: This field may return `null`, indicating that no valid value was found.
        :type Total: int
        :param _Data: Instance list
Note: This field may return `null`, indicating that no valid value was found.
        :type Data: list of AssociatedInstanceInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._RequestId = None

    @property
    def Total(self):
        """Number of instances
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        """Instance list
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: list of AssociatedInstanceInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AssociatedInstanceInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBlockByIpTimesListRequest(AbstractModel):
    """DescribeBlockByIpTimesList request structure.

    """

    def __init__(self):
        r"""
        :param _EndTime: End time
        :type EndTime: str
        :param _Ip: IP search criteria
        :type Ip: str
        :param _StartTime: Start time
        :type StartTime: str
        :param _Direction: Direction
        :type Direction: str
        :param _EdgeId: Inter-VPC firewall toggle edge ID
        :type EdgeId: str
        :param _LogSource: Log source. move: inter-VPC firewall
        :type LogSource: str
        :param _Source: Source
        :type Source: str
        :param _Zone: Region
        :type Zone: str
        """
        self._EndTime = None
        self._Ip = None
        self._StartTime = None
        self._Direction = None
        self._EdgeId = None
        self._LogSource = None
        self._Source = None
        self._Zone = None

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Ip(self):
        """IP search criteria
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Direction(self):
        """Direction
        :rtype: str
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def EdgeId(self):
        """Inter-VPC firewall toggle edge ID
        :rtype: str
        """
        return self._EdgeId

    @EdgeId.setter
    def EdgeId(self, EdgeId):
        self._EdgeId = EdgeId

    @property
    def LogSource(self):
        """Log source. move: inter-VPC firewall
        :rtype: str
        """
        return self._LogSource

    @LogSource.setter
    def LogSource(self, LogSource):
        self._LogSource = LogSource

    @property
    def Source(self):
        """Source
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Zone(self):
        """Region
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._EndTime = params.get("EndTime")
        self._Ip = params.get("Ip")
        self._StartTime = params.get("StartTime")
        self._Direction = params.get("Direction")
        self._EdgeId = params.get("EdgeId")
        self._LogSource = params.get("LogSource")
        self._Source = params.get("Source")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBlockByIpTimesListResponse(AbstractModel):
    """DescribeBlockByIpTimesList response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Response  data
        :type Data: list of IpStatic
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """Response  data
        :rtype: list of IpStatic
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
                obj = IpStatic()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBlockIgnoreListRequest(AbstractModel):
    """DescribeBlockIgnoreList request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of entries per page.
        :type Limit: int
        :param _Offset: Page offset.
        :type Offset: int
        :param _Direction: Direction. Valid values: 1: inbound public access; 0: outbound public access; 3: private network access; empty string: all access.
        :type Direction: str
        :param _RuleType: Rule type. Valid values: 1: block; 2: allow.
        :type RuleType: int
        :param _Order: Column by which rules are sorted. Valid values: EndTime: end time; StartTime: start time; MatchTimes: number of matching times.
        :type Order: str
        :param _By: Sort order. Valid values: desc: descending; asc: ascending.
        :type By: str
        :param _SearchValue: Search keys, in a JSON string. Valid values: {}: empty; domain: domain name; level: threat level; ignore_reason: reason for allowing access; rule_source: source of a security event; address: geographical location; common: fuzzy search.
        :type SearchValue: str
        """
        self._Limit = None
        self._Offset = None
        self._Direction = None
        self._RuleType = None
        self._Order = None
        self._By = None
        self._SearchValue = None

    @property
    def Limit(self):
        """Number of entries per page.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Page offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Direction(self):
        """Direction. Valid values: 1: inbound public access; 0: outbound public access; 3: private network access; empty string: all access.
        :rtype: str
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def RuleType(self):
        """Rule type. Valid values: 1: block; 2: allow.
        :rtype: int
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def Order(self):
        """Column by which rules are sorted. Valid values: EndTime: end time; StartTime: start time; MatchTimes: number of matching times.
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        """Sort order. Valid values: desc: descending; asc: ascending.
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By

    @property
    def SearchValue(self):
        """Search keys, in a JSON string. Valid values: {}: empty; domain: domain name; level: threat level; ignore_reason: reason for allowing access; rule_source: source of a security event; address: geographical location; common: fuzzy search.
        :rtype: str
        """
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Direction = params.get("Direction")
        self._RuleType = params.get("RuleType")
        self._Order = params.get("Order")
        self._By = params.get("By")
        self._SearchValue = params.get("SearchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBlockIgnoreListResponse(AbstractModel):
    """DescribeBlockIgnoreList response structure.

    """

    def __init__(self):
        r"""
        :param _Data: List data.
        :type Data: list of BlockIgnoreRule
        :param _Total: Total number of results, which is used for pagination.
        :type Total: int
        :param _ReturnCode: Status code. Valid values: 0: successful; others: failed.
        :type ReturnCode: int
        :param _ReturnMsg: Status message. Valid values: success: successful query; fail: failed query.
        :type ReturnMsg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._ReturnCode = None
        self._ReturnMsg = None
        self._RequestId = None

    @property
    def Data(self):
        """List data.
        :rtype: list of BlockIgnoreRule
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        """Total number of results, which is used for pagination.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ReturnCode(self):
        """Status code. Valid values: 0: successful; others: failed.
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        """Status message. Valid values: success: successful query; fail: failed query.
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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
                obj = BlockIgnoreRule()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        self._RequestId = params.get("RequestId")


class DescribeBlockStaticListRequest(AbstractModel):
    """DescribeBlockStaticList request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _QueryType: List type. Valid values: port, address, or IP
        :type QueryType: str
        :param _Top: Number of top results returned
        :type Top: int
        :param _SearchValue: Search criteria
        :type SearchValue: str
        """
        self._StartTime = None
        self._EndTime = None
        self._QueryType = None
        self._Top = None
        self._SearchValue = None

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def QueryType(self):
        """List type. Valid values: port, address, or IP
        :rtype: str
        """
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType

    @property
    def Top(self):
        """Number of top results returned
        :rtype: int
        """
        return self._Top

    @Top.setter
    def Top(self, Top):
        self._Top = Top

    @property
    def SearchValue(self):
        """Search criteria
        :rtype: str
        """
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._QueryType = params.get("QueryType")
        self._Top = params.get("Top")
        self._SearchValue = params.get("SearchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBlockStaticListResponse(AbstractModel):
    """DescribeBlockStaticList response structure.

    """

    def __init__(self):
        r"""
        :param _Data: None
        :type Data: list of StaticInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """None
        :rtype: list of StaticInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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
                obj = StaticInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDefenseSwitchRequest(AbstractModel):
    """DescribeDefenseSwitch request structure.

    """


class DescribeDefenseSwitchResponse(AbstractModel):
    """DescribeDefenseSwitch response structure.

    """

    def __init__(self):
        r"""
        :param _BasicRuleSwitch: Whether to enable the Basic Protection feature
        :type BasicRuleSwitch: int
        :param _BaselineAllSwitch: Whether to enable the Security Baseline feature
        :type BaselineAllSwitch: int
        :param _TiSwitch: Whether to enable the Treat Intelligence feature
        :type TiSwitch: int
        :param _VirtualPatchSwitch: Whether to enable the Virtual Patch feature
        :type VirtualPatchSwitch: int
        :param _HistoryOpen: Whether it has been enabled before
        :type HistoryOpen: int
        :param _ReturnCode: Status code. `0`: Succeeded. Others: Failed
        :type ReturnCode: int
        :param _ReturnMsg: Status message. `success` and `fail.
        :type ReturnMsg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BasicRuleSwitch = None
        self._BaselineAllSwitch = None
        self._TiSwitch = None
        self._VirtualPatchSwitch = None
        self._HistoryOpen = None
        self._ReturnCode = None
        self._ReturnMsg = None
        self._RequestId = None

    @property
    def BasicRuleSwitch(self):
        """Whether to enable the Basic Protection feature
        :rtype: int
        """
        return self._BasicRuleSwitch

    @BasicRuleSwitch.setter
    def BasicRuleSwitch(self, BasicRuleSwitch):
        self._BasicRuleSwitch = BasicRuleSwitch

    @property
    def BaselineAllSwitch(self):
        """Whether to enable the Security Baseline feature
        :rtype: int
        """
        return self._BaselineAllSwitch

    @BaselineAllSwitch.setter
    def BaselineAllSwitch(self, BaselineAllSwitch):
        self._BaselineAllSwitch = BaselineAllSwitch

    @property
    def TiSwitch(self):
        """Whether to enable the Treat Intelligence feature
        :rtype: int
        """
        return self._TiSwitch

    @TiSwitch.setter
    def TiSwitch(self, TiSwitch):
        self._TiSwitch = TiSwitch

    @property
    def VirtualPatchSwitch(self):
        """Whether to enable the Virtual Patch feature
        :rtype: int
        """
        return self._VirtualPatchSwitch

    @VirtualPatchSwitch.setter
    def VirtualPatchSwitch(self, VirtualPatchSwitch):
        self._VirtualPatchSwitch = VirtualPatchSwitch

    @property
    def HistoryOpen(self):
        """Whether it has been enabled before
        :rtype: int
        """
        return self._HistoryOpen

    @HistoryOpen.setter
    def HistoryOpen(self, HistoryOpen):
        self._HistoryOpen = HistoryOpen

    @property
    def ReturnCode(self):
        """Status code. `0`: Succeeded. Others: Failed
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        """Status message. `success` and `fail.
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BasicRuleSwitch = params.get("BasicRuleSwitch")
        self._BaselineAllSwitch = params.get("BaselineAllSwitch")
        self._TiSwitch = params.get("TiSwitch")
        self._VirtualPatchSwitch = params.get("VirtualPatchSwitch")
        self._HistoryOpen = params.get("HistoryOpen")
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        self._RequestId = params.get("RequestId")


class DescribeEnterpriseSecurityGroupRuleRequest(AbstractModel):
    """DescribeEnterpriseSecurityGroupRule request structure.

    """

    def __init__(self):
        r"""
        :param _PageNo: Page number of the current page displayed for query by page number.

1 by default.
        :type PageNo: str
        :param _PageSize: Maximum number of entries per page displayed for query by page number.

Maximum value: 50.
        :type PageSize: str
        :param _SourceContent: Source example:
net: IP/CIDR (192.168.0.2)
template: parameter template (ipm-dyodhpby)
instance: asset instance (ins-123456)
resourcegroup: asset group (/all groups/group 1/subgroup 1)
tag: resource tag ({"Key":"tag key","Value":"tag value"})
region: region (ap-gaungzhou)
Wildcards are supported.
        :type SourceContent: str
        :param _DestContent: Destination example:
net: IP/CIDR (192.168.0.2)
template: parameter template (ipm-dyodhpby)
instance: asset instance (ins-123456)
resourcegroup: asset group (/all groups/group 1/subgroup 1)
tag: resource tag ({"Key":"tag key","Value":"tag value"})
region: region (ap-gaungzhou)
Wildcards are supported.
        :type DestContent: str
        :param _Description: Rule description. Wildcards are supported.
        :type Description: str
        :param _RuleAction: The action that Cloud Firewall performs on the traffic. Valid values:
accept: allow
drop: deny
        :type RuleAction: str
        :param _Enable: Indicates whether to enable the rules. Default: enable. Valid values:
true: enable; false: disable
        :type Enable: str
        :param _Port: The port to apply access control rules. Valid values:
-1/-1: all ports
80: port 80
        :type Port: str
        :param _Protocol: Protocol. TCP/UDP/ICMP/ANY
        :type Protocol: str
        :param _ServiceTemplateId: Parameter template ID of port and protocol type; mutually exclusive with Protocol and Port
        :type ServiceTemplateId: str
        """
        self._PageNo = None
        self._PageSize = None
        self._SourceContent = None
        self._DestContent = None
        self._Description = None
        self._RuleAction = None
        self._Enable = None
        self._Port = None
        self._Protocol = None
        self._ServiceTemplateId = None

    @property
    def PageNo(self):
        """Page number of the current page displayed for query by page number.

1 by default.
        :rtype: str
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        """Maximum number of entries per page displayed for query by page number.

Maximum value: 50.
        :rtype: str
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def SourceContent(self):
        """Source example:
net: IP/CIDR (192.168.0.2)
template: parameter template (ipm-dyodhpby)
instance: asset instance (ins-123456)
resourcegroup: asset group (/all groups/group 1/subgroup 1)
tag: resource tag ({"Key":"tag key","Value":"tag value"})
region: region (ap-gaungzhou)
Wildcards are supported.
        :rtype: str
        """
        return self._SourceContent

    @SourceContent.setter
    def SourceContent(self, SourceContent):
        self._SourceContent = SourceContent

    @property
    def DestContent(self):
        """Destination example:
net: IP/CIDR (192.168.0.2)
template: parameter template (ipm-dyodhpby)
instance: asset instance (ins-123456)
resourcegroup: asset group (/all groups/group 1/subgroup 1)
tag: resource tag ({"Key":"tag key","Value":"tag value"})
region: region (ap-gaungzhou)
Wildcards are supported.
        :rtype: str
        """
        return self._DestContent

    @DestContent.setter
    def DestContent(self, DestContent):
        self._DestContent = DestContent

    @property
    def Description(self):
        """Rule description. Wildcards are supported.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RuleAction(self):
        """The action that Cloud Firewall performs on the traffic. Valid values:
accept: allow
drop: deny
        :rtype: str
        """
        return self._RuleAction

    @RuleAction.setter
    def RuleAction(self, RuleAction):
        self._RuleAction = RuleAction

    @property
    def Enable(self):
        """Indicates whether to enable the rules. Default: enable. Valid values:
true: enable; false: disable
        :rtype: str
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Port(self):
        """The port to apply access control rules. Valid values:
-1/-1: all ports
80: port 80
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Protocol(self):
        """Protocol. TCP/UDP/ICMP/ANY
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ServiceTemplateId(self):
        """Parameter template ID of port and protocol type; mutually exclusive with Protocol and Port
        :rtype: str
        """
        return self._ServiceTemplateId

    @ServiceTemplateId.setter
    def ServiceTemplateId(self, ServiceTemplateId):
        self._ServiceTemplateId = ServiceTemplateId


    def _deserialize(self, params):
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        self._SourceContent = params.get("SourceContent")
        self._DestContent = params.get("DestContent")
        self._Description = params.get("Description")
        self._RuleAction = params.get("RuleAction")
        self._Enable = params.get("Enable")
        self._Port = params.get("Port")
        self._Protocol = params.get("Protocol")
        self._ServiceTemplateId = params.get("ServiceTemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnterpriseSecurityGroupRuleResponse(AbstractModel):
    """DescribeEnterpriseSecurityGroupRule response structure.

    """

    def __init__(self):
        r"""
        :param _PageNo: Page number of the current page displayed for query by page number.
        :type PageNo: str
        :param _PageSize: Maximum number of entries per page displayed for query by page number.
        :type PageSize: str
        :param _Rules: Access control rule list
        :type Rules: list of SecurityGroupRule
        :param _TotalCount: Total number of access control rules
        :type TotalCount: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PageNo = None
        self._PageSize = None
        self._Rules = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def PageNo(self):
        """Page number of the current page displayed for query by page number.
        :rtype: str
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        """Maximum number of entries per page displayed for query by page number.
        :rtype: str
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Rules(self):
        """Access control rule list
        :rtype: list of SecurityGroupRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def TotalCount(self):
        """Total number of access control rules
        :rtype: str
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = SecurityGroupRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeGuideScanInfoRequest(AbstractModel):
    """DescribeGuideScanInfo request structure.

    """


class DescribeGuideScanInfoResponse(AbstractModel):
    """DescribeGuideScanInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Scan information
        :type Data: :class:`tencentcloud.cfw.v20190904.models.ScanInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """Scan information
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ScanInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = ScanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeIPStatusListRequest(AbstractModel):
    """DescribeIPStatusList request structure.

    """

    def __init__(self):
        r"""
        :param _IPList: Asset ID
        :type IPList: list of str
        """
        self._IPList = None

    @property
    def IPList(self):
        """Asset ID
        :rtype: list of str
        """
        return self._IPList

    @IPList.setter
    def IPList(self, IPList):
        self._IPList = IPList


    def _deserialize(self, params):
        self._IPList = params.get("IPList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIPStatusListResponse(AbstractModel):
    """DescribeIPStatusList response structure.

    """

    def __init__(self):
        r"""
        :param _StatusList: IP status information
        :type StatusList: list of IPDefendStatus
        :param _ReturnCode: Status code
        :type ReturnCode: int
        :param _ReturnMsg: Status information
        :type ReturnMsg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._StatusList = None
        self._ReturnCode = None
        self._ReturnMsg = None
        self._RequestId = None

    @property
    def StatusList(self):
        """IP status information
        :rtype: list of IPDefendStatus
        """
        return self._StatusList

    @StatusList.setter
    def StatusList(self, StatusList):
        self._StatusList = StatusList

    @property
    def ReturnCode(self):
        """Status code
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        """Status information
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("StatusList") is not None:
            self._StatusList = []
            for item in params.get("StatusList"):
                obj = IPDefendStatus()
                obj._deserialize(item)
                self._StatusList.append(obj)
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        self._RequestId = params.get("RequestId")


class DescribeNatAcRuleRequest(AbstractModel):
    """DescribeNatAcRule request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of entries per page.
        :type Limit: int
        :param _Offset: Page offset.
        :type Offset: int
        :param _Index: Index to be queried. This parameter is optional, and is used only in specific cases.
        :type Index: str
        :param _Filters: Filter condition combination.
        :type Filters: list of CommonFilter
        :param _StartTime: Start time for search. This parameter is optional.
        :type StartTime: str
        :param _EndTime: End time for search. This parameter is optional.
        :type EndTime: str
        :param _Order: Valid values: desc: descending; asc: ascending. The returned results are sorted by the value of By. If this parameter is specified, By is also required.
        :type Order: str
        :param _By: Field by which the returned results are sorted.
        :type By: str
        """
        self._Limit = None
        self._Offset = None
        self._Index = None
        self._Filters = None
        self._StartTime = None
        self._EndTime = None
        self._Order = None
        self._By = None

    @property
    def Limit(self):
        """Number of entries per page.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Page offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Index(self):
        """Index to be queried. This parameter is optional, and is used only in specific cases.
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Filters(self):
        """Filter condition combination.
        :rtype: list of CommonFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def StartTime(self):
        """Start time for search. This parameter is optional.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time for search. This parameter is optional.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Order(self):
        """Valid values: desc: descending; asc: ascending. The returned results are sorted by the value of By. If this parameter is specified, By is also required.
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        """Field by which the returned results are sorted.
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Index = params.get("Index")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = CommonFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Order = params.get("Order")
        self._By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNatAcRuleResponse(AbstractModel):
    """DescribeNatAcRule response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of entries.
        :type Total: int
        :param _Data: NAT access control list data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of DescAcItem
        :param _AllTotal: Total number of entries returned without filtering.
        :type AllTotal: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._AllTotal = None
        self._RequestId = None

    @property
    def Total(self):
        """Total number of entries.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        """NAT access control list data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of DescAcItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def AllTotal(self):
        """Total number of entries returned without filtering.
        :rtype: int
        """
        return self._AllTotal

    @AllTotal.setter
    def AllTotal(self, AllTotal):
        self._AllTotal = AllTotal

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DescAcItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._AllTotal = params.get("AllTotal")
        self._RequestId = params.get("RequestId")


class DescribeNatFwInfoCountRequest(AbstractModel):
    """DescribeNatFwInfoCount request structure.

    """


class DescribeNatFwInfoCountResponse(AbstractModel):
    """DescribeNatFwInfoCount response structure.

    """

    def __init__(self):
        r"""
        :param _ReturnMsg: Response parameter
Note: This field may return `null`, indicating that no valid value was found.
        :type ReturnMsg: str
        :param _NatFwInsCount: Number of NAT instances of the current tenant
Note: This field may return `null`, indicating that no valid value was found.
        :type NatFwInsCount: int
        :param _SubnetCount: Number of subnets connected by the current tenant
Note: This field may return `null`, indicating that no valid value was found.
        :type SubnetCount: int
        :param _OpenSwitchCount: Number of firewalls enabled
Note: This field may return `null`, indicating that no valid value was found.
        :type OpenSwitchCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ReturnMsg = None
        self._NatFwInsCount = None
        self._SubnetCount = None
        self._OpenSwitchCount = None
        self._RequestId = None

    @property
    def ReturnMsg(self):
        """Response parameter
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def NatFwInsCount(self):
        """Number of NAT instances of the current tenant
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._NatFwInsCount

    @NatFwInsCount.setter
    def NatFwInsCount(self, NatFwInsCount):
        self._NatFwInsCount = NatFwInsCount

    @property
    def SubnetCount(self):
        """Number of subnets connected by the current tenant
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._SubnetCount

    @SubnetCount.setter
    def SubnetCount(self, SubnetCount):
        self._SubnetCount = SubnetCount

    @property
    def OpenSwitchCount(self):
        """Number of firewalls enabled
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._OpenSwitchCount

    @OpenSwitchCount.setter
    def OpenSwitchCount(self, OpenSwitchCount):
        self._OpenSwitchCount = OpenSwitchCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReturnMsg = params.get("ReturnMsg")
        self._NatFwInsCount = params.get("NatFwInsCount")
        self._SubnetCount = params.get("SubnetCount")
        self._OpenSwitchCount = params.get("OpenSwitchCount")
        self._RequestId = params.get("RequestId")


class DescribeNatFwInstanceRequest(AbstractModel):
    """DescribeNatFwInstance request structure.

    """


class DescribeNatFwInstanceResponse(AbstractModel):
    """DescribeNatFwInstance response structure.

    """

    def __init__(self):
        r"""
        :param _NatinsLst: Instance array
        :type NatinsLst: list of NatFwInstance
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NatinsLst = None
        self._RequestId = None

    @property
    def NatinsLst(self):
        """Instance array
        :rtype: list of NatFwInstance
        """
        return self._NatinsLst

    @NatinsLst.setter
    def NatinsLst(self, NatinsLst):
        self._NatinsLst = NatinsLst

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("NatinsLst") is not None:
            self._NatinsLst = []
            for item in params.get("NatinsLst"):
                obj = NatFwInstance()
                obj._deserialize(item)
                self._NatinsLst.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNatFwInstanceWithRegionRequest(AbstractModel):
    """DescribeNatFwInstanceWithRegion request structure.

    """


class DescribeNatFwInstanceWithRegionResponse(AbstractModel):
    """DescribeNatFwInstanceWithRegion response structure.

    """

    def __init__(self):
        r"""
        :param _NatinsLst: Instance array
Note: This field may return `null`, indicating that no valid value was found.
        :type NatinsLst: list of NatFwInstance
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NatinsLst = None
        self._RequestId = None

    @property
    def NatinsLst(self):
        """Instance array
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: list of NatFwInstance
        """
        return self._NatinsLst

    @NatinsLst.setter
    def NatinsLst(self, NatinsLst):
        self._NatinsLst = NatinsLst

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("NatinsLst") is not None:
            self._NatinsLst = []
            for item in params.get("NatinsLst"):
                obj = NatFwInstance()
                obj._deserialize(item)
                self._NatinsLst.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNatFwInstancesInfoRequest(AbstractModel):
    """DescribeNatFwInstancesInfo request structure.

    """

    def __init__(self):
        r"""
        :param _Filter: Gets filtering fields of instance list
        :type Filter: list of NatFwFilter
        :param _Offset: Page number
        :type Offset: int
        :param _Limit: Page length
        :type Limit: int
        """
        self._Filter = None
        self._Offset = None
        self._Limit = None

    @property
    def Filter(self):
        """Gets filtering fields of instance list
        :rtype: list of NatFwFilter
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Offset(self):
        """Page number
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Page length
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = []
            for item in params.get("Filter"):
                obj = NatFwFilter()
                obj._deserialize(item)
                self._Filter.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNatFwInstancesInfoResponse(AbstractModel):
    """DescribeNatFwInstancesInfo response structure.

    """

    def __init__(self):
        r"""
        :param _NatinsLst: Instance card info array
Note: This field may return `null`, indicating that no valid value was found.
        :type NatinsLst: list of NatInstanceInfo
        :param _Total: Number of NAT firewalls
Note: This field may return `null`, indicating that no valid value was found.
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NatinsLst = None
        self._Total = None
        self._RequestId = None

    @property
    def NatinsLst(self):
        """Instance card info array
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: list of NatInstanceInfo
        """
        return self._NatinsLst

    @NatinsLst.setter
    def NatinsLst(self, NatinsLst):
        self._NatinsLst = NatinsLst

    @property
    def Total(self):
        """Number of NAT firewalls
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("NatinsLst") is not None:
            self._NatinsLst = []
            for item in params.get("NatinsLst"):
                obj = NatInstanceInfo()
                obj._deserialize(item)
                self._NatinsLst.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeNatFwVpcDnsLstRequest(AbstractModel):
    """DescribeNatFwVpcDnsLst request structure.

    """

    def __init__(self):
        r"""
        :param _NatFwInsId: NAT firewall instance ID
        :type NatFwInsId: str
        :param _NatInsIdFilter: Content filtered by NAT firewall, separated with ","
        :type NatInsIdFilter: str
        :param _Offset: Number of pages
        :type Offset: int
        :param _Limit: Maximum entries per page
        :type Limit: int
        """
        self._NatFwInsId = None
        self._NatInsIdFilter = None
        self._Offset = None
        self._Limit = None

    @property
    def NatFwInsId(self):
        """NAT firewall instance ID
        :rtype: str
        """
        return self._NatFwInsId

    @NatFwInsId.setter
    def NatFwInsId(self, NatFwInsId):
        self._NatFwInsId = NatFwInsId

    @property
    def NatInsIdFilter(self):
        """Content filtered by NAT firewall, separated with ","
        :rtype: str
        """
        return self._NatInsIdFilter

    @NatInsIdFilter.setter
    def NatInsIdFilter(self, NatInsIdFilter):
        self._NatInsIdFilter = NatInsIdFilter

    @property
    def Offset(self):
        """Number of pages
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Maximum entries per page
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._NatFwInsId = params.get("NatFwInsId")
        self._NatInsIdFilter = params.get("NatInsIdFilter")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNatFwVpcDnsLstResponse(AbstractModel):
    """DescribeNatFwVpcDnsLst response structure.

    """

    def __init__(self):
        r"""
        :param _VpcDnsSwitchLst: VPC DNS info array of NAT firewall
Note: This field may return `null`, indicating that no valid value was found.
        :type VpcDnsSwitchLst: list of VpcDnsInfo
        :param _ReturnMsg: Response parameter
Note: This field may return `null`, indicating that no valid value was found.
        :type ReturnMsg: str
        :param _Total: Total number of toggles
Note: This field may return `null`, indicating that no valid value was found.
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._VpcDnsSwitchLst = None
        self._ReturnMsg = None
        self._Total = None
        self._RequestId = None

    @property
    def VpcDnsSwitchLst(self):
        """VPC DNS info array of NAT firewall
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: list of VpcDnsInfo
        """
        return self._VpcDnsSwitchLst

    @VpcDnsSwitchLst.setter
    def VpcDnsSwitchLst(self, VpcDnsSwitchLst):
        self._VpcDnsSwitchLst = VpcDnsSwitchLst

    @property
    def ReturnMsg(self):
        """Response parameter
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def Total(self):
        """Total number of toggles
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("VpcDnsSwitchLst") is not None:
            self._VpcDnsSwitchLst = []
            for item in params.get("VpcDnsSwitchLst"):
                obj = VpcDnsInfo()
                obj._deserialize(item)
                self._VpcDnsSwitchLst.append(obj)
        self._ReturnMsg = params.get("ReturnMsg")
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeResourceGroupNewRequest(AbstractModel):
    """DescribeResourceGroupNew request structure.

    """

    def __init__(self):
        r"""
        :param _QueryType: Query type. Network–VPC; business recognition–resource; resource tag–tag
        :type QueryType: str
        :param _GroupId: Asset group ID, 0: all asset group IDs
        :type GroupId: str
        :param _ShowType: all: all, including subgroups; own: my asset groups only
        :type ShowType: str
        """
        self._QueryType = None
        self._GroupId = None
        self._ShowType = None

    @property
    def QueryType(self):
        """Query type. Network–VPC; business recognition–resource; resource tag–tag
        :rtype: str
        """
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType

    @property
    def GroupId(self):
        """Asset group ID, 0: all asset group IDs
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ShowType(self):
        """all: all, including subgroups; own: my asset groups only
        :rtype: str
        """
        return self._ShowType

    @ShowType.setter
    def ShowType(self, ShowType):
        self._ShowType = ShowType


    def _deserialize(self, params):
        self._QueryType = params.get("QueryType")
        self._GroupId = params.get("GroupId")
        self._ShowType = params.get("ShowType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceGroupNewResponse(AbstractModel):
    """DescribeResourceGroupNew response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returns a tree structure
        :type Data: str
        :param _UnResourceNum: Number of uncategorizd instances
        :type UnResourceNum: int
        :param _ReturnMsg: Response message
        :type ReturnMsg: str
        :param _ReturnCode: Return code. 0: Request successful
        :type ReturnCode: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._UnResourceNum = None
        self._ReturnMsg = None
        self._ReturnCode = None
        self._RequestId = None

    @property
    def Data(self):
        """Returns a tree structure
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def UnResourceNum(self):
        """Number of uncategorizd instances
        :rtype: int
        """
        return self._UnResourceNum

    @UnResourceNum.setter
    def UnResourceNum(self, UnResourceNum):
        self._UnResourceNum = UnResourceNum

    @property
    def ReturnMsg(self):
        """Response message
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def ReturnCode(self):
        """Return code. 0: Request successful
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._UnResourceNum = params.get("UnResourceNum")
        self._ReturnMsg = params.get("ReturnMsg")
        self._ReturnCode = params.get("ReturnCode")
        self._RequestId = params.get("RequestId")


class DescribeRuleOverviewRequest(AbstractModel):
    """DescribeRuleOverview request structure.

    """

    def __init__(self):
        r"""
        :param _Direction: Direction. 0: outbound; 1: inbound
        :type Direction: int
        """
        self._Direction = None

    @property
    def Direction(self):
        """Direction. 0: outbound; 1: inbound
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction


    def _deserialize(self, params):
        self._Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleOverviewResponse(AbstractModel):
    """DescribeRuleOverview response structure.

    """

    def __init__(self):
        r"""
        :param _AllTotal: Total number of rules
Note: This field may return `null`, indicating that no valid value was found.
        :type AllTotal: int
        :param _StrategyNum: Number of blocking rules
Note: This field may return `null`, indicating that no valid value was found.
        :type StrategyNum: int
        :param _StartRuleNum: Number of enabled rules
Note: This field may return `null`, indicating that no valid value was found.
        :type StartRuleNum: int
        :param _StopRuleNum: Number of disabled rules
Note: This field may return `null`, indicating that no valid value was found.
        :type StopRuleNum: int
        :param _RemainingNum: Remaining quota
Note: This field may return `null`, indicating that no valid value was found.
        :type RemainingNum: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AllTotal = None
        self._StrategyNum = None
        self._StartRuleNum = None
        self._StopRuleNum = None
        self._RemainingNum = None
        self._RequestId = None

    @property
    def AllTotal(self):
        """Total number of rules
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._AllTotal

    @AllTotal.setter
    def AllTotal(self, AllTotal):
        self._AllTotal = AllTotal

    @property
    def StrategyNum(self):
        """Number of blocking rules
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._StrategyNum

    @StrategyNum.setter
    def StrategyNum(self, StrategyNum):
        self._StrategyNum = StrategyNum

    @property
    def StartRuleNum(self):
        """Number of enabled rules
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._StartRuleNum

    @StartRuleNum.setter
    def StartRuleNum(self, StartRuleNum):
        self._StartRuleNum = StartRuleNum

    @property
    def StopRuleNum(self):
        """Number of disabled rules
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._StopRuleNum

    @StopRuleNum.setter
    def StopRuleNum(self, StopRuleNum):
        self._StopRuleNum = StopRuleNum

    @property
    def RemainingNum(self):
        """Remaining quota
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._RemainingNum

    @RemainingNum.setter
    def RemainingNum(self, RemainingNum):
        self._RemainingNum = RemainingNum

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AllTotal = params.get("AllTotal")
        self._StrategyNum = params.get("StrategyNum")
        self._StartRuleNum = params.get("StartRuleNum")
        self._StopRuleNum = params.get("StopRuleNum")
        self._RemainingNum = params.get("RemainingNum")
        self._RequestId = params.get("RequestId")


class DescribeSecurityGroupListRequest(AbstractModel):
    """DescribeSecurityGroupList request structure.

    """

    def __init__(self):
        r"""
        :param _Direction: 0: outbound rule; 1: inbound rule
        :type Direction: int
        :param _Area: Region code (e.g. ap-guangzhou ). All Tencent Cloud regions are supported.
        :type Area: str
        :param _SearchValue: Search value
        :type SearchValue: str
        :param _Limit: Number of entries per page. Default: 10
        :type Limit: int
        :param _Offset: Offset. Default: 0
        :type Offset: int
        :param _Status: Status. Null: all; '0': filter disabled rules; '1': filter enabled rules
        :type Status: str
        :param _Filter: 0: not filter; 1: filter out normal rules to retain abnormal rules
        :type Filter: int
        """
        self._Direction = None
        self._Area = None
        self._SearchValue = None
        self._Limit = None
        self._Offset = None
        self._Status = None
        self._Filter = None

    @property
    def Direction(self):
        """0: outbound rule; 1: inbound rule
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Area(self):
        """Region code (e.g. ap-guangzhou ). All Tencent Cloud regions are supported.
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def SearchValue(self):
        """Search value
        :rtype: str
        """
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue

    @property
    def Limit(self):
        """Number of entries per page. Default: 10
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Status(self):
        """Status. Null: all; '0': filter disabled rules; '1': filter enabled rules
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Filter(self):
        """0: not filter; 1: filter out normal rules to retain abnormal rules
        :rtype: int
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._Direction = params.get("Direction")
        self._Area = params.get("Area")
        self._SearchValue = params.get("SearchValue")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Status = params.get("Status")
        self._Filter = params.get("Filter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityGroupListResponse(AbstractModel):
    """DescribeSecurityGroupList response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total rules in the list
        :type Total: int
        :param _Data: Security group rule list data
        :type Data: list of SecurityGroupListData
        :param _AllTotal: Total entries excluding the filtered ones
        :type AllTotal: int
        :param _Enable: All access control rules enabled/disabled
Note: This field may return `null`, indicating that no valid value was found.
        :type Enable: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._AllTotal = None
        self._Enable = None
        self._RequestId = None

    @property
    def Total(self):
        """Total rules in the list
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        """Security group rule list data
        :rtype: list of SecurityGroupListData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def AllTotal(self):
        """Total entries excluding the filtered ones
        :rtype: int
        """
        return self._AllTotal

    @AllTotal.setter
    def AllTotal(self, AllTotal):
        self._AllTotal = AllTotal

    @property
    def Enable(self):
        """All access control rules enabled/disabled
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SecurityGroupListData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._AllTotal = params.get("AllTotal")
        self._Enable = params.get("Enable")
        self._RequestId = params.get("RequestId")


class DescribeSourceAssetRequest(AbstractModel):
    """DescribeSourceAsset request structure.

    """

    def __init__(self):
        r"""
        :param _FuzzySearch: Fuzzy search
        :type FuzzySearch: str
        :param _InsType: Asset type. 1: public network; 2: private network
        :type InsType: str
        :param _ChooseType: If ChooseType is 1, grouped assets are queried; if ChooseType is not 1, non-grouped assets are queried
        :type ChooseType: str
        :param _Zone: Region
        :type Zone: str
        :param _Limit: Maximum number of results returned per page. For example, if it is set to 10, 10 results will be returned at most.
        :type Limit: int
        :param _Offset: Offset of search results
        :type Offset: int
        """
        self._FuzzySearch = None
        self._InsType = None
        self._ChooseType = None
        self._Zone = None
        self._Limit = None
        self._Offset = None

    @property
    def FuzzySearch(self):
        """Fuzzy search
        :rtype: str
        """
        return self._FuzzySearch

    @FuzzySearch.setter
    def FuzzySearch(self, FuzzySearch):
        self._FuzzySearch = FuzzySearch

    @property
    def InsType(self):
        """Asset type. 1: public network; 2: private network
        :rtype: str
        """
        return self._InsType

    @InsType.setter
    def InsType(self, InsType):
        self._InsType = InsType

    @property
    def ChooseType(self):
        """If ChooseType is 1, grouped assets are queried; if ChooseType is not 1, non-grouped assets are queried
        :rtype: str
        """
        return self._ChooseType

    @ChooseType.setter
    def ChooseType(self, ChooseType):
        self._ChooseType = ChooseType

    @property
    def Zone(self):
        """Region
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Limit(self):
        """Maximum number of results returned per page. For example, if it is set to 10, 10 results will be returned at most.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset of search results
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._FuzzySearch = params.get("FuzzySearch")
        self._InsType = params.get("InsType")
        self._ChooseType = params.get("ChooseType")
        self._Zone = params.get("Zone")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSourceAssetResponse(AbstractModel):
    """DescribeSourceAsset response structure.

    """

    def __init__(self):
        r"""
        :param _ZoneList: Region collection
        :type ZoneList: list of AssetZone
        :param _Data: Data
        :type Data: list of InstanceInfo
        :param _Total: Total number of returned data
        :type Total: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ZoneList = None
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def ZoneList(self):
        """Region collection
        :rtype: list of AssetZone
        """
        return self._ZoneList

    @ZoneList.setter
    def ZoneList(self, ZoneList):
        self._ZoneList = ZoneList

    @property
    def Data(self):
        """Data
        :rtype: list of InstanceInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        """Total number of returned data
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ZoneList") is not None:
            self._ZoneList = []
            for item in params.get("ZoneList"):
                obj = AssetZone()
                obj._deserialize(item)
                self._ZoneList.append(obj)
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeSwitchListsRequest(AbstractModel):
    """DescribeSwitchLists request structure.

    """

    def __init__(self):
        r"""
        :param _Status: Firewall status. 0: disabled; 1: enabled
        :type Status: int
        :param _Type: Asset type, e.g. CVM/NAT/VPN/CLB/others
        :type Type: str
        :param _Area: Region, e.g. Shanghai, Chongqing, Guangzhou, etc.
        :type Area: str
        :param _SearchValue: Search value, e.g. "{"common":"106.54.189.45"}"
        :type SearchValue: str
        :param _Limit: Number of entries. Default: 10
        :type Limit: int
        :param _Offset: Offset. Default: 0
        :type Offset: int
        :param _Order: Sort order. desc: descending; asc: ascending
        :type Order: str
        :param _By: Sorting field. PortTimes (number of risky ports)
        :type By: str
        """
        self._Status = None
        self._Type = None
        self._Area = None
        self._SearchValue = None
        self._Limit = None
        self._Offset = None
        self._Order = None
        self._By = None

    @property
    def Status(self):
        """Firewall status. 0: disabled; 1: enabled
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        """Asset type, e.g. CVM/NAT/VPN/CLB/others
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Area(self):
        """Region, e.g. Shanghai, Chongqing, Guangzhou, etc.
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def SearchValue(self):
        """Search value, e.g. "{"common":"106.54.189.45"}"
        :rtype: str
        """
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue

    @property
    def Limit(self):
        """Number of entries. Default: 10
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        """Sort order. desc: descending; asc: ascending
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        """Sorting field. PortTimes (number of risky ports)
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._Area = params.get("Area")
        self._SearchValue = params.get("SearchValue")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        self._By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSwitchListsResponse(AbstractModel):
    """DescribeSwitchLists response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total entries
        :type Total: int
        :param _Data: List data
        :type Data: list of SwitchListsData
        :param _AreaLists: Region list
        :type AreaLists: list of str
        :param _OnNum: Number of enabled firewalls
Note: This field may return `null`, indicating that no valid value was found.
        :type OnNum: int
        :param _OffNum: Number of disabled firewalls
Note: This field may return `null`, indicating that no valid value was found.
        :type OffNum: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._AreaLists = None
        self._OnNum = None
        self._OffNum = None
        self._RequestId = None

    @property
    def Total(self):
        """Total entries
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        """List data
        :rtype: list of SwitchListsData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def AreaLists(self):
        """Region list
        :rtype: list of str
        """
        return self._AreaLists

    @AreaLists.setter
    def AreaLists(self, AreaLists):
        self._AreaLists = AreaLists

    @property
    def OnNum(self):
        """Number of enabled firewalls
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._OnNum

    @OnNum.setter
    def OnNum(self, OnNum):
        self._OnNum = OnNum

    @property
    def OffNum(self):
        """Number of disabled firewalls
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._OffNum

    @OffNum.setter
    def OffNum(self, OffNum):
        self._OffNum = OffNum

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SwitchListsData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._AreaLists = params.get("AreaLists")
        self._OnNum = params.get("OnNum")
        self._OffNum = params.get("OffNum")
        self._RequestId = params.get("RequestId")


class DescribeTLogInfoRequest(AbstractModel):
    """DescribeTLogInfo request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _QueryType: Type. 1: alert; 2: block
        :type QueryType: str
        :param _SearchValue: Search criteria
        :type SearchValue: str
        """
        self._StartTime = None
        self._EndTime = None
        self._QueryType = None
        self._SearchValue = None

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def QueryType(self):
        """Type. 1: alert; 2: block
        :rtype: str
        """
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType

    @property
    def SearchValue(self):
        """Search criteria
        :rtype: str
        """
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._QueryType = params.get("QueryType")
        self._SearchValue = params.get("SearchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTLogInfoResponse(AbstractModel):
    """DescribeTLogInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Data: `NetworkNum`: Number of detected network scans
 `HandleNum`: Number of pending processing events
"BanNum": 
  `VulNum`: Number of vulnerability exploits
  "OutNum`: Number of compromised servers
"BruteForceNum": 0
        :type Data: :class:`tencentcloud.cfw.v20190904.models.TLogInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """`NetworkNum`: Number of detected network scans
 `HandleNum`: Number of pending processing events
"BanNum": 
  `VulNum`: Number of vulnerability exploits
  "OutNum`: Number of compromised servers
"BruteForceNum": 0
        :rtype: :class:`tencentcloud.cfw.v20190904.models.TLogInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = TLogInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTLogIpListRequest(AbstractModel):
    """DescribeTLogIpList request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _QueryType: Type. 1: alert; 2: block
        :type QueryType: str
        :param _Top: Number of top results returned
        :type Top: int
        :param _SearchValue: Search criteria
        :type SearchValue: str
        """
        self._StartTime = None
        self._EndTime = None
        self._QueryType = None
        self._Top = None
        self._SearchValue = None

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def QueryType(self):
        """Type. 1: alert; 2: block
        :rtype: str
        """
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType

    @property
    def Top(self):
        """Number of top results returned
        :rtype: int
        """
        return self._Top

    @Top.setter
    def Top(self, Top):
        self._Top = Top

    @property
    def SearchValue(self):
        """Search criteria
        :rtype: str
        """
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._QueryType = params.get("QueryType")
        self._Top = params.get("Top")
        self._SearchValue = params.get("SearchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTLogIpListResponse(AbstractModel):
    """DescribeTLogIpList response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Data collection
        :type Data: list of StaticInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """Data collection
        :rtype: list of StaticInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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
                obj = StaticInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTableStatusRequest(AbstractModel):
    """DescribeTableStatus request structure.

    """

    def __init__(self):
        r"""
        :param _EdgeId: Edge ID between two VPCs, required for VPCs
        :type EdgeId: str
        :param _Status: Status value. 0: the only default value
        :type Status: int
        :param _Area: NAT region, required for NAT
        :type Area: str
        :param _Direction: Direction. 0: outbound; 1: inbound. 0 by default
        :type Direction: int
        """
        self._EdgeId = None
        self._Status = None
        self._Area = None
        self._Direction = None

    @property
    def EdgeId(self):
        """Edge ID between two VPCs, required for VPCs
        :rtype: str
        """
        return self._EdgeId

    @EdgeId.setter
    def EdgeId(self, EdgeId):
        self._EdgeId = EdgeId

    @property
    def Status(self):
        """Status value. 0: the only default value
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Area(self):
        """NAT region, required for NAT
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Direction(self):
        """Direction. 0: outbound; 1: inbound. 0 by default
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction


    def _deserialize(self, params):
        self._EdgeId = params.get("EdgeId")
        self._Status = params.get("Status")
        self._Area = params.get("Area")
        self._Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTableStatusResponse(AbstractModel):
    """DescribeTableStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Status: 0: normal; non-0: abnormal
Note: This field may return `null`, indicating that no valid value was found.
        :type Status: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """0: normal; non-0: abnormal
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeUnHandleEventTabListRequest(AbstractModel):
    """DescribeUnHandleEventTabList request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _AssetID: Gets example ID
        :type AssetID: str
        """
        self._StartTime = None
        self._EndTime = None
        self._AssetID = None

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def AssetID(self):
        """Gets example ID
        :rtype: str
        """
        return self._AssetID

    @AssetID.setter
    def AssetID(self, AssetID):
        self._AssetID = AssetID


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._AssetID = params.get("AssetID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUnHandleEventTabListResponse(AbstractModel):
    """DescribeUnHandleEventTabList response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Gets unhandled security events
Note: This field may return `null`, indicating that no valid value was found.
        :type Data: :class:`tencentcloud.cfw.v20190904.models.UnHandleEvent`
        :param _ReturnCode: Error code. 0: success; non-0: error
        :type ReturnCode: int
        :param _ReturnMsg: Return message: success
        :type ReturnMsg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._ReturnCode = None
        self._ReturnMsg = None
        self._RequestId = None

    @property
    def Data(self):
        """Gets unhandled security events
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: :class:`tencentcloud.cfw.v20190904.models.UnHandleEvent`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def ReturnCode(self):
        """Error code. 0: success; non-0: error
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        """Return message: success
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = UnHandleEvent()
            self._Data._deserialize(params.get("Data"))
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        self._RequestId = params.get("RequestId")


class DescribeVpcAcRuleRequest(AbstractModel):
    """DescribeVpcAcRule request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Limit
        :type Limit: int
        :param _Offset: Offset
        :type Offset: int
        :param _Index: Index to be queried, used in specific scenarios, can be left blank
        :type Index: str
        :param _Filters: Filter combinations
        :type Filters: list of CommonFilter
        :param _StartTime: Search start time
        :type StartTime: str
        :param _EndTime: Search end time
        :type EndTime: str
        :param _Order: Order Type:desc,asc
        :type Order: str
        :param _By: Order By FileName
        :type By: str
        """
        self._Limit = None
        self._Offset = None
        self._Index = None
        self._Filters = None
        self._StartTime = None
        self._EndTime = None
        self._Order = None
        self._By = None

    @property
    def Limit(self):
        """Limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Index(self):
        """Index to be queried, used in specific scenarios, can be left blank
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Filters(self):
        """Filter combinations
        :rtype: list of CommonFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def StartTime(self):
        """Search start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Search end time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Order(self):
        """Order Type:desc,asc
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        """Order By FileName
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Index = params.get("Index")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = CommonFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Order = params.get("Order")
        self._By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcAcRuleResponse(AbstractModel):
    """DescribeVpcAcRule response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total Data
        :type Total: int
        :param _Data: Data list
        :type Data: list of VpcRuleItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._RequestId = None

    @property
    def Total(self):
        """Total Data
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        """Data list
        :rtype: list of VpcRuleItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = VpcRuleItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DnsVpcSwitch(AbstractModel):
    """Sets the VPC DNS toggle of the NAT firewall

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _Status: 0: off; 1: on
        :type Status: int
        """
        self._VpcId = None
        self._Status = None

    @property
    def VpcId(self):
        """VPC ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Status(self):
        """0: off; 1: on
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExpandCfwVerticalRequest(AbstractModel):
    """ExpandCfwVertical request structure.

    """

    def __init__(self):
        r"""
        :param _FwType: nat: NAT firewall, ew: east-west firewall
        :type FwType: str
        :param _Width: Bandwidth value
        :type Width: int
        :param _CfwInstance: Firewall instance ID
        :type CfwInstance: str
        """
        self._FwType = None
        self._Width = None
        self._CfwInstance = None

    @property
    def FwType(self):
        """nat: NAT firewall, ew: east-west firewall
        :rtype: str
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType

    @property
    def Width(self):
        """Bandwidth value
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def CfwInstance(self):
        """Firewall instance ID
        :rtype: str
        """
        return self._CfwInstance

    @CfwInstance.setter
    def CfwInstance(self, CfwInstance):
        self._CfwInstance = CfwInstance


    def _deserialize(self, params):
        self._FwType = params.get("FwType")
        self._Width = params.get("Width")
        self._CfwInstance = params.get("CfwInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExpandCfwVerticalResponse(AbstractModel):
    """ExpandCfwVertical response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class FwCidrInfo(AbstractModel):
    """Firewall IP range information

    """

    def __init__(self):
        r"""
        :param _FwCidrType: The IP range type of the firewall. Values: `VpcSelf` (VPC IP range preferred); `Assis` (Secondary IP range preferred); `Custom` (Custom IP range)
        :type FwCidrType: str
        :param _FwCidrLst: The IP segment assigned for each VPC.
        :type FwCidrLst: list of FwVpcCidr
        :param _ComFwCidr: The IP segment used by other firewalls. Specify this if you want to assign a dedicated segment for the firewall.
        :type ComFwCidr: str
        """
        self._FwCidrType = None
        self._FwCidrLst = None
        self._ComFwCidr = None

    @property
    def FwCidrType(self):
        """The IP range type of the firewall. Values: `VpcSelf` (VPC IP range preferred); `Assis` (Secondary IP range preferred); `Custom` (Custom IP range)
        :rtype: str
        """
        return self._FwCidrType

    @FwCidrType.setter
    def FwCidrType(self, FwCidrType):
        self._FwCidrType = FwCidrType

    @property
    def FwCidrLst(self):
        """The IP segment assigned for each VPC.
        :rtype: list of FwVpcCidr
        """
        return self._FwCidrLst

    @FwCidrLst.setter
    def FwCidrLst(self, FwCidrLst):
        self._FwCidrLst = FwCidrLst

    @property
    def ComFwCidr(self):
        """The IP segment used by other firewalls. Specify this if you want to assign a dedicated segment for the firewall.
        :rtype: str
        """
        return self._ComFwCidr

    @ComFwCidr.setter
    def ComFwCidr(self, ComFwCidr):
        self._ComFwCidr = ComFwCidr


    def _deserialize(self, params):
        self._FwCidrType = params.get("FwCidrType")
        if params.get("FwCidrLst") is not None:
            self._FwCidrLst = []
            for item in params.get("FwCidrLst"):
                obj = FwVpcCidr()
                obj._deserialize(item)
                self._FwCidrLst.append(obj)
        self._ComFwCidr = params.get("ComFwCidr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FwVpcCidr(AbstractModel):
    """Firewall IP range of the VPC

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _FwCidr: IP range of the firewall. The mask must be at least /24.
        :type FwCidr: str
        """
        self._VpcId = None
        self._FwCidr = None

    @property
    def VpcId(self):
        """VPC ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def FwCidr(self):
        """IP range of the firewall. The mask must be at least /24.
        :rtype: str
        """
        return self._FwCidr

    @FwCidr.setter
    def FwCidr(self, FwCidr):
        self._FwCidr = FwCidr


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._FwCidr = params.get("FwCidr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPDefendStatus(AbstractModel):
    """IP protection status

    """

    def __init__(self):
        r"""
        :param _IP: IP address
        :type IP: str
        :param _Status: Protection status. 1: enabled; -1: incorrect address; others: disabled
        :type Status: int
        """
        self._IP = None
        self._Status = None

    @property
    def IP(self):
        """IP address
        :rtype: str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Status(self):
        """Protection status. 1: enabled; -1: incorrect address; others: disabled
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfo(AbstractModel):
    """// InstanceInfo instance details result
    type InstanceInfo struct {
    	AppID        string `json:"AppId" gorm:"column:appid"`
    	Region       string `json:"Region" gorm:"column:region"`
    	VPCID        string `json:"VpcId" gorm:"column:vpc_id"`
    	SubNetID     string `json:"SubnetId" gorm:"column:subnet_id"`
    	InstanceID   string `json:"InstanceId" gorm:"column:instance_id"`
    	InstanceName string `json:"InstanceName" gorm:"column:instance_name"`
    	//InsType common.CVM 3 is CVM instance, 4 is CLB instance, 5 is ENI instance, 6 is MySQL, 7 is Redis, 8 is NAT, 9 is VPN, 10 is ES, 11 is MariaDB, and 12 is Kafka
    	InsType   int    `json:"InsType" gorm:"column:instance_type"`
    	PublicIP  string `json:"PublicIp" gorm:"column:public_ip"`
    	PrivateIP string `json:"PrivateIp" gorm:"column:ip"`

    	// It is not required for rule publishing and is used for frontend display
    	PortNum          string `json:"PortNum" gorm:"column:port_num"`
    	LeakNum          string `json:"LeakNum" gorm:"column:leak_num"`
    	ResourceGroupNum int    `json:"ResourceGroupNum"`
    	VPCName          string `json:"VPCName" gorm:"column:VPCName"`
    }

    """

    def __init__(self):
        r"""
        :param _AppId: App ID
        :type AppId: str
        :param _Region: Region
        :type Region: str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _VPCName: VPC name
        :type VPCName: str
        :param _SubnetId: Subnet ID
        :type SubnetId: str
        :param _InstanceId: Asset ID
        :type InstanceId: str
        :param _InstanceName: Asset name
        :type InstanceName: str
        :param _InsType: Asset type
 3: CVM instance; 4: CLB instance; 5: ENI instance; 6: MySQL; 7: Redis; 8: NAT; 9: VPN; 10: ES; 11: MariaDB; 12: Kafka; 13: NATFW
        :type InsType: int
        :param _PublicIp: Public IP
        :type PublicIp: str
        :param _PrivateIp: Private IP
        :type PrivateIp: str
        :param _PortNum: Number of ports
        :type PortNum: str
        :param _LeakNum: Number of vulnerabilities
        :type LeakNum: str
        :param _InsSource: 1: public network; 2: private network
        :type InsSource: str
        :param _ResourcePath: [a,b]
Note: This field may return `null`, indicating that no valid value was found.
        :type ResourcePath: list of str
        """
        self._AppId = None
        self._Region = None
        self._VpcId = None
        self._VPCName = None
        self._SubnetId = None
        self._InstanceId = None
        self._InstanceName = None
        self._InsType = None
        self._PublicIp = None
        self._PrivateIp = None
        self._PortNum = None
        self._LeakNum = None
        self._InsSource = None
        self._ResourcePath = None

    @property
    def AppId(self):
        """App ID
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Region(self):
        """Region
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcId(self):
        """VPC ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VPCName(self):
        """VPC name
        :rtype: str
        """
        return self._VPCName

    @VPCName.setter
    def VPCName(self, VPCName):
        self._VPCName = VPCName

    @property
    def SubnetId(self):
        """Subnet ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def InstanceId(self):
        """Asset ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """Asset name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InsType(self):
        """Asset type
 3: CVM instance; 4: CLB instance; 5: ENI instance; 6: MySQL; 7: Redis; 8: NAT; 9: VPN; 10: ES; 11: MariaDB; 12: Kafka; 13: NATFW
        :rtype: int
        """
        return self._InsType

    @InsType.setter
    def InsType(self, InsType):
        self._InsType = InsType

    @property
    def PublicIp(self):
        """Public IP
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        """Private IP
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def PortNum(self):
        """Number of ports
        :rtype: str
        """
        return self._PortNum

    @PortNum.setter
    def PortNum(self, PortNum):
        self._PortNum = PortNum

    @property
    def LeakNum(self):
        """Number of vulnerabilities
        :rtype: str
        """
        return self._LeakNum

    @LeakNum.setter
    def LeakNum(self, LeakNum):
        self._LeakNum = LeakNum

    @property
    def InsSource(self):
        """1: public network; 2: private network
        :rtype: str
        """
        return self._InsSource

    @InsSource.setter
    def InsSource(self, InsSource):
        self._InsSource = InsSource

    @property
    def ResourcePath(self):
        """[a,b]
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: list of str
        """
        return self._ResourcePath

    @ResourcePath.setter
    def ResourcePath(self, ResourcePath):
        self._ResourcePath = ResourcePath


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._VPCName = params.get("VPCName")
        self._SubnetId = params.get("SubnetId")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InsType = params.get("InsType")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._PortNum = params.get("PortNum")
        self._LeakNum = params.get("LeakNum")
        self._InsSource = params.get("InsSource")
        self._ResourcePath = params.get("ResourcePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IocListData(AbstractModel):
    """Blocklist, allowlist, IOC list

    """

    def __init__(self):
        r"""
        :param _IP: IP address to be handled. Either IP or Domain is required.
        :type IP: str
        :param _Direction: 0 or 1. 0: outbound; 1: inbound
        :type Direction: int
        :param _Domain: Domain name to be handled. Either IP or Domain is required.
        :type Domain: str
        """
        self._IP = None
        self._Direction = None
        self._Domain = None

    @property
    def IP(self):
        """IP address to be handled. Either IP or Domain is required.
        :rtype: str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Direction(self):
        """0 or 1. 0: outbound; 1: inbound
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Domain(self):
        """Domain name to be handled. Either IP or Domain is required.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._Direction = params.get("Direction")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpStatic(AbstractModel):
    """Statistical line graph general structure

    """

    def __init__(self):
        r"""
        :param _Num: Value
        :type Num: int
        :param _StatTime: Time shown on the x-axis of the line graph
        :type StatTime: str
        """
        self._Num = None
        self._StatTime = None

    @property
    def Num(self):
        """Value
        :rtype: int
        """
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

    @property
    def StatTime(self):
        """Time shown on the x-axis of the line graph
        :rtype: str
        """
        return self._StatTime

    @StatTime.setter
    def StatTime(self, StatTime):
        self._StatTime = StatTime


    def _deserialize(self, params):
        self._Num = params.get("Num")
        self._StatTime = params.get("StatTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAcRuleRequest(AbstractModel):
    """ModifyAcRule request structure.

    """

    def __init__(self):
        r"""
        :param _Data: Array of rules
        :type Data: list of RuleInfoData
        :param _EdgeId: EdgeId value
        :type EdgeId: str
        :param _Enable: Access rule status
        :type Enable: int
        :param _Area: NAT region
        :type Area: str
        """
        self._Data = None
        self._EdgeId = None
        self._Enable = None
        self._Area = None

    @property
    def Data(self):
        """Array of rules
        :rtype: list of RuleInfoData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def EdgeId(self):
        """EdgeId value
        :rtype: str
        """
        return self._EdgeId

    @EdgeId.setter
    def EdgeId(self, EdgeId):
        self._EdgeId = EdgeId

    @property
    def Enable(self):
        """Access rule status
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Area(self):
        """NAT region
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = RuleInfoData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._EdgeId = params.get("EdgeId")
        self._Enable = params.get("Enable")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAcRuleResponse(AbstractModel):
    """ModifyAcRule response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Status value. 0: operation successful; non-0: operation failed
        :type Status: int
        :param _Info: Returns redundant information
Note: This field may return `null`, indicating that no valid value was found.
        :type Info: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._Info = None
        self._RequestId = None

    @property
    def Status(self):
        """Status value. 0: operation successful; non-0: operation failed
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Info(self):
        """Returns redundant information
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Info = params.get("Info")
        self._RequestId = params.get("RequestId")


class ModifyAllPublicIPSwitchStatusRequest(AbstractModel):
    """ModifyAllPublicIPSwitchStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Status: Status. 0: off; 1: on
        :type Status: int
        :param _FireWallPublicIPs: ID of the selected firewall toggle
        :type FireWallPublicIPs: list of str
        """
        self._Status = None
        self._FireWallPublicIPs = None

    @property
    def Status(self):
        """Status. 0: off; 1: on
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FireWallPublicIPs(self):
        """ID of the selected firewall toggle
        :rtype: list of str
        """
        return self._FireWallPublicIPs

    @FireWallPublicIPs.setter
    def FireWallPublicIPs(self, FireWallPublicIPs):
        self._FireWallPublicIPs = FireWallPublicIPs


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._FireWallPublicIPs = params.get("FireWallPublicIPs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAllPublicIPSwitchStatusResponse(AbstractModel):
    """ModifyAllPublicIPSwitchStatus response structure.

    """

    def __init__(self):
        r"""
        :param _ReturnMsg: Return message
Note: This field may return `null`, indicating that no valid value was found.
        :type ReturnMsg: str
        :param _ReturnCode: Error code. 0: success; non-0: failed
Note: This field may return `null`, indicating that no valid value was found.
        :type ReturnCode: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ReturnMsg = None
        self._ReturnCode = None
        self._RequestId = None

    @property
    def ReturnMsg(self):
        """Return message
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def ReturnCode(self):
        """Error code. 0: success; non-0: failed
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReturnMsg = params.get("ReturnMsg")
        self._ReturnCode = params.get("ReturnCode")
        self._RequestId = params.get("RequestId")


class ModifyAllRuleStatusRequest(AbstractModel):
    """ModifyAllRuleStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Status: Status. 0: all disabled; 1: all enabled
        :type Status: int
        :param _Direction: Direction. 0: outbound; 1: inbound
        :type Direction: int
        :param _EdgeId: Edge ID value
        :type EdgeId: str
        :param _Area: NAT region
        :type Area: str
        """
        self._Status = None
        self._Direction = None
        self._EdgeId = None
        self._Area = None

    @property
    def Status(self):
        """Status. 0: all disabled; 1: all enabled
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Direction(self):
        """Direction. 0: outbound; 1: inbound
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def EdgeId(self):
        """Edge ID value
        :rtype: str
        """
        return self._EdgeId

    @EdgeId.setter
    def EdgeId(self, EdgeId):
        self._EdgeId = EdgeId

    @property
    def Area(self):
        """NAT region
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Direction = params.get("Direction")
        self._EdgeId = params.get("EdgeId")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAllRuleStatusResponse(AbstractModel):
    """ModifyAllRuleStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Status: 0: modified successfully; non-0: modification failed
Note: This field may return `null`, indicating that no valid value was found.
        :type Status: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """0: modified successfully; non-0: modification failed
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ModifyAllVPCSwitchStatusRequest(AbstractModel):
    """ModifyAllVPCSwitchStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Status: Status. 0: off; 1: on
        :type Status: int
        :param _FireWallVpcIds: ID of the selected firewall toggle
        :type FireWallVpcIds: list of str
        """
        self._Status = None
        self._FireWallVpcIds = None

    @property
    def Status(self):
        """Status. 0: off; 1: on
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FireWallVpcIds(self):
        """ID of the selected firewall toggle
        :rtype: list of str
        """
        return self._FireWallVpcIds

    @FireWallVpcIds.setter
    def FireWallVpcIds(self, FireWallVpcIds):
        self._FireWallVpcIds = FireWallVpcIds


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._FireWallVpcIds = params.get("FireWallVpcIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAllVPCSwitchStatusResponse(AbstractModel):
    """ModifyAllVPCSwitchStatus response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyAssetScanRequest(AbstractModel):
    """ModifyAssetScan request structure.

    """

    def __init__(self):
        r"""
        :param _ScanRange: Scan range. 1: port; 2: port + vulnerability scan
        :type ScanRange: int
        :param _ScanDeep: Scan mode: 'heavy', 'medium', 'light'
        :type ScanDeep: str
        :param _RangeType: Scan type. 1: scan now; 2: periodic scan
        :type RangeType: int
        :param _ScanPeriod: Scheduled task time, required when RangeType is 2
        :type ScanPeriod: str
        :param _ScanFilterIp: Scans this field now and passes the filtered IPs
        :type ScanFilterIp: list of str
        :param _ScanType: 1: all; 2: single
        :type ScanType: int
        """
        self._ScanRange = None
        self._ScanDeep = None
        self._RangeType = None
        self._ScanPeriod = None
        self._ScanFilterIp = None
        self._ScanType = None

    @property
    def ScanRange(self):
        """Scan range. 1: port; 2: port + vulnerability scan
        :rtype: int
        """
        return self._ScanRange

    @ScanRange.setter
    def ScanRange(self, ScanRange):
        self._ScanRange = ScanRange

    @property
    def ScanDeep(self):
        """Scan mode: 'heavy', 'medium', 'light'
        :rtype: str
        """
        return self._ScanDeep

    @ScanDeep.setter
    def ScanDeep(self, ScanDeep):
        self._ScanDeep = ScanDeep

    @property
    def RangeType(self):
        """Scan type. 1: scan now; 2: periodic scan
        :rtype: int
        """
        return self._RangeType

    @RangeType.setter
    def RangeType(self, RangeType):
        self._RangeType = RangeType

    @property
    def ScanPeriod(self):
        """Scheduled task time, required when RangeType is 2
        :rtype: str
        """
        return self._ScanPeriod

    @ScanPeriod.setter
    def ScanPeriod(self, ScanPeriod):
        self._ScanPeriod = ScanPeriod

    @property
    def ScanFilterIp(self):
        """Scans this field now and passes the filtered IPs
        :rtype: list of str
        """
        return self._ScanFilterIp

    @ScanFilterIp.setter
    def ScanFilterIp(self, ScanFilterIp):
        self._ScanFilterIp = ScanFilterIp

    @property
    def ScanType(self):
        """1: all; 2: single
        :rtype: int
        """
        return self._ScanType

    @ScanType.setter
    def ScanType(self, ScanType):
        self._ScanType = ScanType


    def _deserialize(self, params):
        self._ScanRange = params.get("ScanRange")
        self._ScanDeep = params.get("ScanDeep")
        self._RangeType = params.get("RangeType")
        self._ScanPeriod = params.get("ScanPeriod")
        self._ScanFilterIp = params.get("ScanFilterIp")
        self._ScanType = params.get("ScanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAssetScanResponse(AbstractModel):
    """ModifyAssetScan response structure.

    """

    def __init__(self):
        r"""
        :param _ReturnMsg: Return message
Note: This field may return `null`, indicating that no valid value was found.
        :type ReturnMsg: str
        :param _ReturnCode: Error code. 0: success; non-0: failed
Note: This field may return `null`, indicating that no valid value was found.
        :type ReturnCode: int
        :param _Status: Status value. 0: success; 1: scanning; others: failed
        :type Status: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ReturnMsg = None
        self._ReturnCode = None
        self._Status = None
        self._RequestId = None

    @property
    def ReturnMsg(self):
        """Return message
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def ReturnCode(self):
        """Error code. 0: success; non-0: failed
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def Status(self):
        """Status value. 0: success; 1: scanning; others: failed
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReturnMsg = params.get("ReturnMsg")
        self._ReturnCode = params.get("ReturnCode")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ModifyBlockIgnoreListRequest(AbstractModel):
    """ModifyBlockIgnoreList request structure.

    """

    def __init__(self):
        r"""
        :param _RuleType: Type of the rule. Values: `1` (Blocklist); `2` (Allowlist)
        :type RuleType: int
        :param _IOC: Either IP or Domain is required
        :type IOC: list of IocListData
        :param _IocAction: Optional values: delete, edit, and add
        :type IocAction: str
        :param _StartTime: Time format: yyyy-MM-dd HH:mm:ss. Required when IocAction is edit or add
        :type StartTime: str
        :param _EndTime: End time of the period in the format of yyyy-MM-dd HH:mm:ss. It must be later than both the start time and the current time. It’s required when `IocAction` is `edit` or `add`. 
        :type EndTime: str
        """
        self._RuleType = None
        self._IOC = None
        self._IocAction = None
        self._StartTime = None
        self._EndTime = None

    @property
    def RuleType(self):
        """Type of the rule. Values: `1` (Blocklist); `2` (Allowlist)
        :rtype: int
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def IOC(self):
        """Either IP or Domain is required
        :rtype: list of IocListData
        """
        return self._IOC

    @IOC.setter
    def IOC(self, IOC):
        self._IOC = IOC

    @property
    def IocAction(self):
        """Optional values: delete, edit, and add
        :rtype: str
        """
        return self._IocAction

    @IocAction.setter
    def IocAction(self, IocAction):
        self._IocAction = IocAction

    @property
    def StartTime(self):
        """Time format: yyyy-MM-dd HH:mm:ss. Required when IocAction is edit or add
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time of the period in the format of yyyy-MM-dd HH:mm:ss. It must be later than both the start time and the current time. It’s required when `IocAction` is `edit` or `add`. 
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._RuleType = params.get("RuleType")
        if params.get("IOC") is not None:
            self._IOC = []
            for item in params.get("IOC"):
                obj = IocListData()
                obj._deserialize(item)
                self._IOC.append(obj)
        self._IocAction = params.get("IocAction")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBlockIgnoreListResponse(AbstractModel):
    """ModifyBlockIgnoreList response structure.

    """

    def __init__(self):
        r"""
        :param _ReturnMsg: Return message
        :type ReturnMsg: str
        :param _ReturnCode: Error code. 0: success; non-0: failed
        :type ReturnCode: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ReturnMsg = None
        self._ReturnCode = None
        self._RequestId = None

    @property
    def ReturnMsg(self):
        """Return message
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def ReturnCode(self):
        """Error code. 0: success; non-0: failed
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReturnMsg = params.get("ReturnMsg")
        self._ReturnCode = params.get("ReturnCode")
        self._RequestId = params.get("RequestId")


class ModifyBlockTopRequest(AbstractModel):
    """ModifyBlockTop request structure.

    """

    def __init__(self):
        r"""
        :param _UniqueId: Record ID
        :type UniqueId: str
        :param _OpeType: Operation type. 1: pin to top; 0: unpin
        :type OpeType: str
        """
        self._UniqueId = None
        self._OpeType = None

    @property
    def UniqueId(self):
        """Record ID
        :rtype: str
        """
        return self._UniqueId

    @UniqueId.setter
    def UniqueId(self, UniqueId):
        self._UniqueId = UniqueId

    @property
    def OpeType(self):
        """Operation type. 1: pin to top; 0: unpin
        :rtype: str
        """
        return self._OpeType

    @OpeType.setter
    def OpeType(self, OpeType):
        self._OpeType = OpeType


    def _deserialize(self, params):
        self._UniqueId = params.get("UniqueId")
        self._OpeType = params.get("OpeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBlockTopResponse(AbstractModel):
    """ModifyBlockTop response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyEnterpriseSecurityDispatchStatusRequest(AbstractModel):
    """ModifyEnterpriseSecurityDispatchStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Status: Status. Values: `0` (Publish now), `1` (Stop publishing)
        :type Status: int
        """
        self._Status = None

    @property
    def Status(self):
        """Status. Values: `0` (Publish now), `1` (Stop publishing)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEnterpriseSecurityDispatchStatusResponse(AbstractModel):
    """ModifyEnterpriseSecurityDispatchStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Status: `0`: Modified successfully; Others: Modification failed
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """`0`: Modified successfully; Others: Modification failed
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ModifyEnterpriseSecurityGroupRuleRequest(AbstractModel):
    """ModifyEnterpriseSecurityGroupRule request structure.

    """

    def __init__(self):
        r"""
        :param _RuleUuid: UUID of the rule, which can be obtained by querying the rule list
        :type RuleUuid: int
        :param _ModifyType: Modification type. Values: `0` (Modify rule content), `1` (Toggle on/off a rule) and `2` (Toggle on/off all rules)
        :type ModifyType: int
        :param _Data: The new rule content you want. It’s only required when you want to modify the rule content (`ModifyType=0`)
        :type Data: :class:`tencentcloud.cfw.v20190904.models.SecurityGroupRule`
        :param _Enable: `0`: Do not enable; `1`: Enable
        :type Enable: int
        """
        self._RuleUuid = None
        self._ModifyType = None
        self._Data = None
        self._Enable = None

    @property
    def RuleUuid(self):
        """UUID of the rule, which can be obtained by querying the rule list
        :rtype: int
        """
        return self._RuleUuid

    @RuleUuid.setter
    def RuleUuid(self, RuleUuid):
        self._RuleUuid = RuleUuid

    @property
    def ModifyType(self):
        """Modification type. Values: `0` (Modify rule content), `1` (Toggle on/off a rule) and `2` (Toggle on/off all rules)
        :rtype: int
        """
        return self._ModifyType

    @ModifyType.setter
    def ModifyType(self, ModifyType):
        self._ModifyType = ModifyType

    @property
    def Data(self):
        """The new rule content you want. It’s only required when you want to modify the rule content (`ModifyType=0`)
        :rtype: :class:`tencentcloud.cfw.v20190904.models.SecurityGroupRule`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Enable(self):
        """`0`: Do not enable; `1`: Enable
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._RuleUuid = params.get("RuleUuid")
        self._ModifyType = params.get("ModifyType")
        if params.get("Data") is not None:
            self._Data = SecurityGroupRule()
            self._Data._deserialize(params.get("Data"))
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEnterpriseSecurityGroupRuleResponse(AbstractModel):
    """ModifyEnterpriseSecurityGroupRule response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Status value. `0`: Edited successfully; Others: Failed to edit
        :type Status: int
        :param _NewRuleUuid: ID of new rule generated after the modification
        :type NewRuleUuid: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._NewRuleUuid = None
        self._RequestId = None

    @property
    def Status(self):
        """Status value. `0`: Edited successfully; Others: Failed to edit
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def NewRuleUuid(self):
        """ID of new rule generated after the modification
        :rtype: int
        """
        return self._NewRuleUuid

    @NewRuleUuid.setter
    def NewRuleUuid(self, NewRuleUuid):
        self._NewRuleUuid = NewRuleUuid

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._NewRuleUuid = params.get("NewRuleUuid")
        self._RequestId = params.get("RequestId")


class ModifyNatAcRuleRequest(AbstractModel):
    """ModifyNatAcRule request structure.

    """

    def __init__(self):
        r"""
        :param _Rules: Array of rules to be modified.
        :type Rules: list of CreateNatRuleItem
        """
        self._Rules = None

    @property
    def Rules(self):
        """Array of rules to be modified.
        :rtype: list of CreateNatRuleItem
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = CreateNatRuleItem()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNatAcRuleResponse(AbstractModel):
    """ModifyNatAcRule response structure.

    """

    def __init__(self):
        r"""
        :param _RuleUuid: ID list of new rules that have been successfully modified.
        :type RuleUuid: list of int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleUuid = None
        self._RequestId = None

    @property
    def RuleUuid(self):
        """ID list of new rules that have been successfully modified.
        :rtype: list of int
        """
        return self._RuleUuid

    @RuleUuid.setter
    def RuleUuid(self, RuleUuid):
        self._RuleUuid = RuleUuid

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleUuid = params.get("RuleUuid")
        self._RequestId = params.get("RequestId")


class ModifyNatFwReSelectRequest(AbstractModel):
    """ModifyNatFwReSelect request structure.

    """

    def __init__(self):
        r"""
        :param _Mode: Mode. 1: use existing; 0: create new
        :type Mode: int
        :param _CfwInstance: Firewall instance ID
        :type CfwInstance: str
        :param _NatGwList: List of NAT gateways reconnected for the Using Existing mode. Only one of NatGwList and VpcList can be passed.
        :type NatGwList: list of str
        :param _VpcList: List of VPCs reconnected for the Create New mode. Only one of NatGwList and VpcList can be passed.
        :type VpcList: list of str
        :param _FwCidrInfo: IP range of the firewall
        :type FwCidrInfo: :class:`tencentcloud.cfw.v20190904.models.FwCidrInfo`
        """
        self._Mode = None
        self._CfwInstance = None
        self._NatGwList = None
        self._VpcList = None
        self._FwCidrInfo = None

    @property
    def Mode(self):
        """Mode. 1: use existing; 0: create new
        :rtype: int
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def CfwInstance(self):
        """Firewall instance ID
        :rtype: str
        """
        return self._CfwInstance

    @CfwInstance.setter
    def CfwInstance(self, CfwInstance):
        self._CfwInstance = CfwInstance

    @property
    def NatGwList(self):
        """List of NAT gateways reconnected for the Using Existing mode. Only one of NatGwList and VpcList can be passed.
        :rtype: list of str
        """
        return self._NatGwList

    @NatGwList.setter
    def NatGwList(self, NatGwList):
        self._NatGwList = NatGwList

    @property
    def VpcList(self):
        """List of VPCs reconnected for the Create New mode. Only one of NatGwList and VpcList can be passed.
        :rtype: list of str
        """
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def FwCidrInfo(self):
        """IP range of the firewall
        :rtype: :class:`tencentcloud.cfw.v20190904.models.FwCidrInfo`
        """
        return self._FwCidrInfo

    @FwCidrInfo.setter
    def FwCidrInfo(self, FwCidrInfo):
        self._FwCidrInfo = FwCidrInfo


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._CfwInstance = params.get("CfwInstance")
        self._NatGwList = params.get("NatGwList")
        self._VpcList = params.get("VpcList")
        if params.get("FwCidrInfo") is not None:
            self._FwCidrInfo = FwCidrInfo()
            self._FwCidrInfo._deserialize(params.get("FwCidrInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNatFwReSelectResponse(AbstractModel):
    """ModifyNatFwReSelect response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyNatFwSwitchRequest(AbstractModel):
    """ModifyNatFwSwitch request structure.

    """

    def __init__(self):
        r"""
        :param _Enable: Status. 0: off; 1: on
        :type Enable: int
        :param _CfwInsIdList: List of firewall instance IDs. Only one of CfwInsIdList, SubnetIdList, and RouteTableIdList can be passed.
        :type CfwInsIdList: list of str
        :param _SubnetIdList: List of subnet IDs. Only one of CfwInsIdList, SubnetIdList, and RouteTableIdList can be passed.
        :type SubnetIdList: list of str
        :param _RouteTableIdList: List of route table IDs. Only one of CfwInsIdList, SubnetIdList, and RouteTableIdList can be passed.
        :type RouteTableIdList: list of str
        """
        self._Enable = None
        self._CfwInsIdList = None
        self._SubnetIdList = None
        self._RouteTableIdList = None

    @property
    def Enable(self):
        """Status. 0: off; 1: on
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def CfwInsIdList(self):
        """List of firewall instance IDs. Only one of CfwInsIdList, SubnetIdList, and RouteTableIdList can be passed.
        :rtype: list of str
        """
        return self._CfwInsIdList

    @CfwInsIdList.setter
    def CfwInsIdList(self, CfwInsIdList):
        self._CfwInsIdList = CfwInsIdList

    @property
    def SubnetIdList(self):
        """List of subnet IDs. Only one of CfwInsIdList, SubnetIdList, and RouteTableIdList can be passed.
        :rtype: list of str
        """
        return self._SubnetIdList

    @SubnetIdList.setter
    def SubnetIdList(self, SubnetIdList):
        self._SubnetIdList = SubnetIdList

    @property
    def RouteTableIdList(self):
        """List of route table IDs. Only one of CfwInsIdList, SubnetIdList, and RouteTableIdList can be passed.
        :rtype: list of str
        """
        return self._RouteTableIdList

    @RouteTableIdList.setter
    def RouteTableIdList(self, RouteTableIdList):
        self._RouteTableIdList = RouteTableIdList


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        self._CfwInsIdList = params.get("CfwInsIdList")
        self._SubnetIdList = params.get("SubnetIdList")
        self._RouteTableIdList = params.get("RouteTableIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNatFwSwitchResponse(AbstractModel):
    """ModifyNatFwSwitch response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyNatFwVpcDnsSwitchRequest(AbstractModel):
    """ModifyNatFwVpcDnsSwitch request structure.

    """

    def __init__(self):
        r"""
        :param _NatFwInsId: NAT firewall ID
        :type NatFwInsId: str
        :param _DnsVpcSwitchLst: DNS toggle list
        :type DnsVpcSwitchLst: list of DnsVpcSwitch
        """
        self._NatFwInsId = None
        self._DnsVpcSwitchLst = None

    @property
    def NatFwInsId(self):
        """NAT firewall ID
        :rtype: str
        """
        return self._NatFwInsId

    @NatFwInsId.setter
    def NatFwInsId(self, NatFwInsId):
        self._NatFwInsId = NatFwInsId

    @property
    def DnsVpcSwitchLst(self):
        """DNS toggle list
        :rtype: list of DnsVpcSwitch
        """
        return self._DnsVpcSwitchLst

    @DnsVpcSwitchLst.setter
    def DnsVpcSwitchLst(self, DnsVpcSwitchLst):
        self._DnsVpcSwitchLst = DnsVpcSwitchLst


    def _deserialize(self, params):
        self._NatFwInsId = params.get("NatFwInsId")
        if params.get("DnsVpcSwitchLst") is not None:
            self._DnsVpcSwitchLst = []
            for item in params.get("DnsVpcSwitchLst"):
                obj = DnsVpcSwitch()
                obj._deserialize(item)
                self._DnsVpcSwitchLst.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNatFwVpcDnsSwitchResponse(AbstractModel):
    """ModifyNatFwVpcDnsSwitch response structure.

    """

    def __init__(self):
        r"""
        :param _ReturnMsg: Modified successfully
Note: This field may return `null`, indicating that no valid value was found.
        :type ReturnMsg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ReturnMsg = None
        self._RequestId = None

    @property
    def ReturnMsg(self):
        """Modified successfully
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReturnMsg = params.get("ReturnMsg")
        self._RequestId = params.get("RequestId")


class ModifyNatSequenceRulesRequest(AbstractModel):
    """ModifyNatSequenceRules request structure.

    """

    def __init__(self):
        r"""
        :param _RuleChangeItems: Rule sequence number. Values: `OrderIndex` (Original sequence number), `NewOrderIndex` (New sequence number)
        :type RuleChangeItems: list of RuleChangeItem
        :param _Direction: Rule direction. Values: `1` (Inbound) and `0` (Outbound)
        :type Direction: int
        """
        self._RuleChangeItems = None
        self._Direction = None

    @property
    def RuleChangeItems(self):
        """Rule sequence number. Values: `OrderIndex` (Original sequence number), `NewOrderIndex` (New sequence number)
        :rtype: list of RuleChangeItem
        """
        return self._RuleChangeItems

    @RuleChangeItems.setter
    def RuleChangeItems(self, RuleChangeItems):
        self._RuleChangeItems = RuleChangeItems

    @property
    def Direction(self):
        """Rule direction. Values: `1` (Inbound) and `0` (Outbound)
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction


    def _deserialize(self, params):
        if params.get("RuleChangeItems") is not None:
            self._RuleChangeItems = []
            for item in params.get("RuleChangeItems"):
                obj = RuleChangeItem()
                obj._deserialize(item)
                self._RuleChangeItems.append(obj)
        self._Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNatSequenceRulesResponse(AbstractModel):
    """ModifyNatSequenceRules response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyPublicIPSwitchStatusRequest(AbstractModel):
    """ModifyPublicIPSwitchStatus request structure.

    """

    def __init__(self):
        r"""
        :param _FireWallPublicIP: Public IP
        :type FireWallPublicIP: str
        :param _Status: Status value. 0: off; 1: on
        :type Status: int
        """
        self._FireWallPublicIP = None
        self._Status = None

    @property
    def FireWallPublicIP(self):
        """Public IP
        :rtype: str
        """
        return self._FireWallPublicIP

    @FireWallPublicIP.setter
    def FireWallPublicIP(self, FireWallPublicIP):
        self._FireWallPublicIP = FireWallPublicIP

    @property
    def Status(self):
        """Status value. 0: off; 1: on
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._FireWallPublicIP = params.get("FireWallPublicIP")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPublicIPSwitchStatusResponse(AbstractModel):
    """ModifyPublicIPSwitchStatus response structure.

    """

    def __init__(self):
        r"""
        :param _ReturnMsg: Return message
Note: This field may return `null`, indicating that no valid value was found.
        :type ReturnMsg: str
        :param _ReturnCode: Error code. 0: success; non-0: failed
        :type ReturnCode: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ReturnMsg = None
        self._ReturnCode = None
        self._RequestId = None

    @property
    def ReturnMsg(self):
        """Return message
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def ReturnCode(self):
        """Error code. 0: success; non-0: failed
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReturnMsg = params.get("ReturnMsg")
        self._ReturnCode = params.get("ReturnCode")
        self._RequestId = params.get("RequestId")


class ModifyResourceGroupRequest(AbstractModel):
    """ModifyResourceGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Group ID
        :type GroupId: str
        :param _GroupName: Group name
        :type GroupName: str
        :param _ParentId: Parent group ID
        :type ParentId: str
        """
        self._GroupId = None
        self._GroupName = None
        self._ParentId = None

    @property
    def GroupId(self):
        """Group ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        """Group name
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ParentId(self):
        """Parent group ID
        :rtype: str
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._ParentId = params.get("ParentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourceGroupResponse(AbstractModel):
    """ModifyResourceGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyRunSyncAssetRequest(AbstractModel):
    """ModifyRunSyncAsset request structure.

    """

    def __init__(self):
        r"""
        :param _Type: 0: edge firewall toggle; 1: VPC firewall toggle
        :type Type: int
        """
        self._Type = None

    @property
    def Type(self):
        """0: edge firewall toggle; 1: VPC firewall toggle
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRunSyncAssetResponse(AbstractModel):
    """ModifyRunSyncAsset response structure.

    """

    def __init__(self):
        r"""
        :param _Status: 0: synced successfully, 1: updating assets, 2: failed to sync by calling the API at the backend
        :type Status: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """0: synced successfully, 1: updating assets, 2: failed to sync by calling the API at the backend
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ModifySecurityGroupItemRuleStatusRequest(AbstractModel):
    """ModifySecurityGroupItemRuleStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Direction: Direction. 0: outbound; 1: inbound. 1 by default
        :type Direction: int
        :param _Status: Toggle status. 0: off; 1: on
        :type Status: int
        :param _RuleSequence: Modified priority of enterprise security group rules
        :type RuleSequence: int
        """
        self._Direction = None
        self._Status = None
        self._RuleSequence = None

    @property
    def Direction(self):
        """Direction. 0: outbound; 1: inbound. 1 by default
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Status(self):
        """Toggle status. 0: off; 1: on
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RuleSequence(self):
        """Modified priority of enterprise security group rules
        :rtype: int
        """
        return self._RuleSequence

    @RuleSequence.setter
    def RuleSequence(self, RuleSequence):
        self._RuleSequence = RuleSequence


    def _deserialize(self, params):
        self._Direction = params.get("Direction")
        self._Status = params.get("Status")
        self._RuleSequence = params.get("RuleSequence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityGroupItemRuleStatusResponse(AbstractModel):
    """ModifySecurityGroupItemRuleStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Status value. 0: modified successfully; non-0: failed to modify
        :type Status: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """Status value. 0: modified successfully; non-0: failed to modify
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ModifySecurityGroupSequenceRulesRequest(AbstractModel):
    """ModifySecurityGroupSequenceRules request structure.

    """

    def __init__(self):
        r"""
        :param _Direction: Direction. 0: outbound; 1: inbound. 1 by default
        :type Direction: int
        :param _Data: Sorting data of enterprise security group rules
        :type Data: list of SecurityGroupOrderIndexData
        """
        self._Direction = None
        self._Data = None

    @property
    def Direction(self):
        """Direction. 0: outbound; 1: inbound. 1 by default
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Data(self):
        """Sorting data of enterprise security group rules
        :rtype: list of SecurityGroupOrderIndexData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Direction = params.get("Direction")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SecurityGroupOrderIndexData()
                obj._deserialize(item)
                self._Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityGroupSequenceRulesResponse(AbstractModel):
    """ModifySecurityGroupSequenceRules response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Status value. 0: modified successfully; non-0: failed to modify
        :type Status: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """Status value. 0: modified successfully; non-0: failed to modify
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ModifySequenceRulesRequest(AbstractModel):
    """ModifySequenceRules request structure.

    """

    def __init__(self):
        r"""
        :param _EdgeId: Edge ID value
        :type EdgeId: str
        :param _Data: Modifies data
        :type Data: list of SequenceData
        :param _Area: NAT region
        :type Area: str
        :param _Direction: Direction. 0: outbound; 1: inbound
        :type Direction: int
        """
        self._EdgeId = None
        self._Data = None
        self._Area = None
        self._Direction = None

    @property
    def EdgeId(self):
        """Edge ID value
        :rtype: str
        """
        return self._EdgeId

    @EdgeId.setter
    def EdgeId(self, EdgeId):
        self._EdgeId = EdgeId

    @property
    def Data(self):
        """Modifies data
        :rtype: list of SequenceData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Area(self):
        """NAT region
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Direction(self):
        """Direction. 0: outbound; 1: inbound
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction


    def _deserialize(self, params):
        self._EdgeId = params.get("EdgeId")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SequenceData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Area = params.get("Area")
        self._Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySequenceRulesResponse(AbstractModel):
    """ModifySequenceRules response structure.

    """

    def __init__(self):
        r"""
        :param _Status: 0: modified successfully; non-0: modification failed
Note: This field may return `null`, indicating that no valid value was found.
        :type Status: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """0: modified successfully; non-0: modification failed
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ModifyStorageSettingRequest(AbstractModel):
    """ModifyStorageSetting request structure.

    """


class ModifyStorageSettingResponse(AbstractModel):
    """ModifyStorageSetting response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyTableStatusRequest(AbstractModel):
    """ModifyTableStatus request structure.

    """

    def __init__(self):
        r"""
        :param _EdgeId: Edge ID between two VPCs
        :type EdgeId: str
        :param _Status: Status value. 1: table locked; 2: table unlocked
        :type Status: int
        :param _Area: NAT region
        :type Area: str
        :param _Direction: 0: outbound; 1: inbound
        :type Direction: int
        """
        self._EdgeId = None
        self._Status = None
        self._Area = None
        self._Direction = None

    @property
    def EdgeId(self):
        """Edge ID between two VPCs
        :rtype: str
        """
        return self._EdgeId

    @EdgeId.setter
    def EdgeId(self, EdgeId):
        self._EdgeId = EdgeId

    @property
    def Status(self):
        """Status value. 1: table locked; 2: table unlocked
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Area(self):
        """NAT region
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Direction(self):
        """0: outbound; 1: inbound
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction


    def _deserialize(self, params):
        self._EdgeId = params.get("EdgeId")
        self._Status = params.get("Status")
        self._Area = params.get("Area")
        self._Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTableStatusResponse(AbstractModel):
    """ModifyTableStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Status: 0: normal; -1: abnormal
Note: This field may return `null`, indicating that no valid value was found.
        :type Status: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """0: normal; -1: abnormal
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class NatFwFilter(AbstractModel):
    """The filter list displayed by the NAT firewall instance

    """

    def __init__(self):
        r"""
        :param _FilterType: Filter type, e.g., instance ID
        :type FilterType: str
        :param _FilterContent: Filtered content, separated with ","
        :type FilterContent: str
        """
        self._FilterType = None
        self._FilterContent = None

    @property
    def FilterType(self):
        """Filter type, e.g., instance ID
        :rtype: str
        """
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def FilterContent(self):
        """Filtered content, separated with ","
        :rtype: str
        """
        return self._FilterContent

    @FilterContent.setter
    def FilterContent(self, FilterContent):
        self._FilterContent = FilterContent


    def _deserialize(self, params):
        self._FilterType = params.get("FilterType")
        self._FilterContent = params.get("FilterContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NatFwInstance(AbstractModel):
    """NAT instance type

    """

    def __init__(self):
        r"""
        :param _NatinsId: NAT instance ID
        :type NatinsId: str
        :param _NatinsName: NAT instance name
        :type NatinsName: str
        :param _Region: Instance region
Note: This field may return `null`, indicating that no valid value was found.
        :type Region: str
        :param _FwMode: 0: create new; 1: use existing
Note: This field may return `null`, indicating that no valid value was found.
        :type FwMode: int
        :param _Status: 0: normal; 1: creating
Note: This field may return `null`, indicating that no valid value was found.
        :type Status: int
        :param _NatIp: NAT public IP
Note: This field may return `null`, indicating that no valid value was found.
        :type NatIp: str
        """
        self._NatinsId = None
        self._NatinsName = None
        self._Region = None
        self._FwMode = None
        self._Status = None
        self._NatIp = None

    @property
    def NatinsId(self):
        """NAT instance ID
        :rtype: str
        """
        return self._NatinsId

    @NatinsId.setter
    def NatinsId(self, NatinsId):
        self._NatinsId = NatinsId

    @property
    def NatinsName(self):
        """NAT instance name
        :rtype: str
        """
        return self._NatinsName

    @NatinsName.setter
    def NatinsName(self, NatinsName):
        self._NatinsName = NatinsName

    @property
    def Region(self):
        """Instance region
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def FwMode(self):
        """0: create new; 1: use existing
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._FwMode

    @FwMode.setter
    def FwMode(self, FwMode):
        self._FwMode = FwMode

    @property
    def Status(self):
        """0: normal; 1: creating
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def NatIp(self):
        """NAT public IP
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._NatIp

    @NatIp.setter
    def NatIp(self, NatIp):
        self._NatIp = NatIp


    def _deserialize(self, params):
        self._NatinsId = params.get("NatinsId")
        self._NatinsName = params.get("NatinsName")
        self._Region = params.get("Region")
        self._FwMode = params.get("FwMode")
        self._Status = params.get("Status")
        self._NatIp = params.get("NatIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NatInstanceInfo(AbstractModel):
    """NAT instance card details

    """

    def __init__(self):
        r"""
        :param _NatinsId: NAT instance ID
        :type NatinsId: str
        :param _NatinsName: NAT instance name
        :type NatinsName: str
        :param _Region: Instance region
        :type Region: str
        :param _FwMode: 0: create new; 1: use existing
        :type FwMode: int
        :param _BandWidth: Instance bandwidth (Mbps)
        :type BandWidth: int
        :param _InFlowMax: Inbound traffic peak bandwidth (bps)
        :type InFlowMax: int
        :param _OutFlowMax: Outbound traffic peak bandwidth (bps)
        :type OutFlowMax: int
        :param _RegionZh: Chinese region information
        :type RegionZh: str
        :param _EipAddress: Public IP array
Note: This field may return `null`, indicating that no valid value was found.
        :type EipAddress: list of str
        :param _VpcIp: Array of internal and external IPs
Note: This field may return `null`, indicating that no valid value was found.
        :type VpcIp: list of str
        :param _Subnets: Array of subnets associated with an instance
Note: This field may return `null`, indicating that no valid value was found.
        :type Subnets: list of str
        :param _Status: 0: normal 1: initializing
Note: This field may return `null`, indicating that no valid value was found.
        :type Status: int
        :param _RegionDetail: Region information
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionDetail: str
        :param _ZoneZh: Availability zone of the instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneZh: str
        :param _ZoneZhBak: Availability zone of the instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneZhBak: str
        :param _RuleUsed: Number of used rules.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleUsed: int
        :param _RuleMax: The maximum number of rules allowed in the instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RuleMax: int
        """
        self._NatinsId = None
        self._NatinsName = None
        self._Region = None
        self._FwMode = None
        self._BandWidth = None
        self._InFlowMax = None
        self._OutFlowMax = None
        self._RegionZh = None
        self._EipAddress = None
        self._VpcIp = None
        self._Subnets = None
        self._Status = None
        self._RegionDetail = None
        self._ZoneZh = None
        self._ZoneZhBak = None
        self._RuleUsed = None
        self._RuleMax = None

    @property
    def NatinsId(self):
        """NAT instance ID
        :rtype: str
        """
        return self._NatinsId

    @NatinsId.setter
    def NatinsId(self, NatinsId):
        self._NatinsId = NatinsId

    @property
    def NatinsName(self):
        """NAT instance name
        :rtype: str
        """
        return self._NatinsName

    @NatinsName.setter
    def NatinsName(self, NatinsName):
        self._NatinsName = NatinsName

    @property
    def Region(self):
        """Instance region
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def FwMode(self):
        """0: create new; 1: use existing
        :rtype: int
        """
        return self._FwMode

    @FwMode.setter
    def FwMode(self, FwMode):
        self._FwMode = FwMode

    @property
    def BandWidth(self):
        """Instance bandwidth (Mbps)
        :rtype: int
        """
        return self._BandWidth

    @BandWidth.setter
    def BandWidth(self, BandWidth):
        self._BandWidth = BandWidth

    @property
    def InFlowMax(self):
        """Inbound traffic peak bandwidth (bps)
        :rtype: int
        """
        return self._InFlowMax

    @InFlowMax.setter
    def InFlowMax(self, InFlowMax):
        self._InFlowMax = InFlowMax

    @property
    def OutFlowMax(self):
        """Outbound traffic peak bandwidth (bps)
        :rtype: int
        """
        return self._OutFlowMax

    @OutFlowMax.setter
    def OutFlowMax(self, OutFlowMax):
        self._OutFlowMax = OutFlowMax

    @property
    def RegionZh(self):
        """Chinese region information
        :rtype: str
        """
        return self._RegionZh

    @RegionZh.setter
    def RegionZh(self, RegionZh):
        self._RegionZh = RegionZh

    @property
    def EipAddress(self):
        """Public IP array
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: list of str
        """
        return self._EipAddress

    @EipAddress.setter
    def EipAddress(self, EipAddress):
        self._EipAddress = EipAddress

    @property
    def VpcIp(self):
        """Array of internal and external IPs
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: list of str
        """
        return self._VpcIp

    @VpcIp.setter
    def VpcIp(self, VpcIp):
        self._VpcIp = VpcIp

    @property
    def Subnets(self):
        """Array of subnets associated with an instance
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: list of str
        """
        return self._Subnets

    @Subnets.setter
    def Subnets(self, Subnets):
        self._Subnets = Subnets

    @property
    def Status(self):
        """0: normal 1: initializing
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RegionDetail(self):
        """Region information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RegionDetail

    @RegionDetail.setter
    def RegionDetail(self, RegionDetail):
        self._RegionDetail = RegionDetail

    @property
    def ZoneZh(self):
        """Availability zone of the instance
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ZoneZh

    @ZoneZh.setter
    def ZoneZh(self, ZoneZh):
        self._ZoneZh = ZoneZh

    @property
    def ZoneZhBak(self):
        """Availability zone of the instance
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ZoneZhBak

    @ZoneZhBak.setter
    def ZoneZhBak(self, ZoneZhBak):
        self._ZoneZhBak = ZoneZhBak

    @property
    def RuleUsed(self):
        """Number of used rules.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RuleUsed

    @RuleUsed.setter
    def RuleUsed(self, RuleUsed):
        self._RuleUsed = RuleUsed

    @property
    def RuleMax(self):
        """The maximum number of rules allowed in the instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RuleMax

    @RuleMax.setter
    def RuleMax(self, RuleMax):
        self._RuleMax = RuleMax


    def _deserialize(self, params):
        self._NatinsId = params.get("NatinsId")
        self._NatinsName = params.get("NatinsName")
        self._Region = params.get("Region")
        self._FwMode = params.get("FwMode")
        self._BandWidth = params.get("BandWidth")
        self._InFlowMax = params.get("InFlowMax")
        self._OutFlowMax = params.get("OutFlowMax")
        self._RegionZh = params.get("RegionZh")
        self._EipAddress = params.get("EipAddress")
        self._VpcIp = params.get("VpcIp")
        self._Subnets = params.get("Subnets")
        self._Status = params.get("Status")
        self._RegionDetail = params.get("RegionDetail")
        self._ZoneZh = params.get("ZoneZh")
        self._ZoneZhBak = params.get("ZoneZhBak")
        self._RuleUsed = params.get("RuleUsed")
        self._RuleMax = params.get("RuleMax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NewModeItems(AbstractModel):
    """Parameters passed for the Create New mode

    """

    def __init__(self):
        r"""
        :param _VpcList: VPC list for the Create New mode
        :type VpcList: list of str
        :param _Eips: The list of egress public EIPs bound for the Create New mode. Either Eips or AddCount is required.
        :type Eips: list of str
        :param _AddCount: The number of egress public EIPs newly bound for the Create New mode. Either Eips or AddCount is required.
        :type AddCount: int
        """
        self._VpcList = None
        self._Eips = None
        self._AddCount = None

    @property
    def VpcList(self):
        """VPC list for the Create New mode
        :rtype: list of str
        """
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def Eips(self):
        """The list of egress public EIPs bound for the Create New mode. Either Eips or AddCount is required.
        :rtype: list of str
        """
        return self._Eips

    @Eips.setter
    def Eips(self, Eips):
        self._Eips = Eips

    @property
    def AddCount(self):
        """The number of egress public EIPs newly bound for the Create New mode. Either Eips or AddCount is required.
        :rtype: int
        """
        return self._AddCount

    @AddCount.setter
    def AddCount(self, AddCount):
        self._AddCount = AddCount


    def _deserialize(self, params):
        self._VpcList = params.get("VpcList")
        self._Eips = params.get("Eips")
        self._AddCount = params.get("AddCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveAcRuleRequest(AbstractModel):
    """RemoveAcRule request structure.

    """

    def __init__(self):
        r"""
        :param _RuleUuid: UUID of the rule, which can be obtained by querying the rule list
        :type RuleUuid: int
        """
        self._RuleUuid = None

    @property
    def RuleUuid(self):
        """UUID of the rule, which can be obtained by querying the rule list
        :rtype: int
        """
        return self._RuleUuid

    @RuleUuid.setter
    def RuleUuid(self, RuleUuid):
        self._RuleUuid = RuleUuid


    def _deserialize(self, params):
        self._RuleUuid = params.get("RuleUuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveAcRuleResponse(AbstractModel):
    """RemoveAcRule response structure.

    """

    def __init__(self):
        r"""
        :param _RuleUuid: Returns the UUID of the deleted policy after the deletion is successful
        :type RuleUuid: int
        :param _ReturnCode: 0: operation successful; -1: operation failed
Note: This field may return `null`, indicating that no valid value was found.
        :type ReturnCode: int
        :param _ReturnMsg: success: operation successful; failed: operation failed
Note: This field may return `null`, indicating that no valid value was found.
        :type ReturnMsg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleUuid = None
        self._ReturnCode = None
        self._ReturnMsg = None
        self._RequestId = None

    @property
    def RuleUuid(self):
        """Returns the UUID of the deleted policy after the deletion is successful
        :rtype: int
        """
        return self._RuleUuid

    @RuleUuid.setter
    def RuleUuid(self, RuleUuid):
        self._RuleUuid = RuleUuid

    @property
    def ReturnCode(self):
        """0: operation successful; -1: operation failed
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        """success: operation successful; failed: operation failed
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleUuid = params.get("RuleUuid")
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        self._RequestId = params.get("RequestId")


class RemoveEnterpriseSecurityGroupRuleRequest(AbstractModel):
    """RemoveEnterpriseSecurityGroupRule request structure.

    """

    def __init__(self):
        r"""
        :param _RuleUuid: UUID of the rule, which can be obtained by querying the rule list
        :type RuleUuid: int
        :param _RemoveType: Type of deletion. 0: delete a single entry, and enter ID of the deleted rule for RuleUuid; 1: delete all, and enter 0 for RuleUuid
        :type RemoveType: int
        """
        self._RuleUuid = None
        self._RemoveType = None

    @property
    def RuleUuid(self):
        """UUID of the rule, which can be obtained by querying the rule list
        :rtype: int
        """
        return self._RuleUuid

    @RuleUuid.setter
    def RuleUuid(self, RuleUuid):
        self._RuleUuid = RuleUuid

    @property
    def RemoveType(self):
        """Type of deletion. 0: delete a single entry, and enter ID of the deleted rule for RuleUuid; 1: delete all, and enter 0 for RuleUuid
        :rtype: int
        """
        return self._RemoveType

    @RemoveType.setter
    def RemoveType(self, RemoveType):
        self._RemoveType = RemoveType


    def _deserialize(self, params):
        self._RuleUuid = params.get("RuleUuid")
        self._RemoveType = params.get("RemoveType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveEnterpriseSecurityGroupRuleResponse(AbstractModel):
    """RemoveEnterpriseSecurityGroupRule response structure.

    """

    def __init__(self):
        r"""
        :param _RuleUuid: Returns the UUID of the deleted policy after the deletion is successful
        :type RuleUuid: int
        :param _Status: 0: operation successful; -1: operation failed
Note: This field may return `null`, indicating that no valid value was found.
        :type Status: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleUuid = None
        self._Status = None
        self._RequestId = None

    @property
    def RuleUuid(self):
        """Returns the UUID of the deleted policy after the deletion is successful
        :rtype: int
        """
        return self._RuleUuid

    @RuleUuid.setter
    def RuleUuid(self, RuleUuid):
        self._RuleUuid = RuleUuid

    @property
    def Status(self):
        """0: operation successful; -1: operation failed
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleUuid = params.get("RuleUuid")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class RemoveNatAcRuleRequest(AbstractModel):
    """RemoveNatAcRule request structure.

    """

    def __init__(self):
        r"""
        :param _RuleUuid: UUIDs of the rules to delete, which can be obtained by querying the rule list. Note: If [-1] is passed in, all rules are deleted.
        :type RuleUuid: list of int
        :param _Direction: Rule direction. Valid values: 1: inbound; 0: outbound.
        :type Direction: int
        """
        self._RuleUuid = None
        self._Direction = None

    @property
    def RuleUuid(self):
        """UUIDs of the rules to delete, which can be obtained by querying the rule list. Note: If [-1] is passed in, all rules are deleted.
        :rtype: list of int
        """
        return self._RuleUuid

    @RuleUuid.setter
    def RuleUuid(self, RuleUuid):
        self._RuleUuid = RuleUuid

    @property
    def Direction(self):
        """Rule direction. Valid values: 1: inbound; 0: outbound.
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction


    def _deserialize(self, params):
        self._RuleUuid = params.get("RuleUuid")
        self._Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveNatAcRuleResponse(AbstractModel):
    """RemoveNatAcRule response structure.

    """

    def __init__(self):
        r"""
        :param _RuleUuid: UUID list of the deleted rules.
        :type RuleUuid: list of int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RuleUuid = None
        self._RequestId = None

    @property
    def RuleUuid(self):
        """UUID list of the deleted rules.
        :rtype: list of int
        """
        return self._RuleUuid

    @RuleUuid.setter
    def RuleUuid(self, RuleUuid):
        self._RuleUuid = RuleUuid

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleUuid = params.get("RuleUuid")
        self._RequestId = params.get("RequestId")


class RuleChangeItem(AbstractModel):
    """Changes of the rule sequence number.

    """

    def __init__(self):
        r"""
        :param _OrderIndex: Original sequence number
        :type OrderIndex: int
        :param _NewOrderIndex: New sequence number
        :type NewOrderIndex: int
        """
        self._OrderIndex = None
        self._NewOrderIndex = None

    @property
    def OrderIndex(self):
        """Original sequence number
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def NewOrderIndex(self):
        """New sequence number
        :rtype: int
        """
        return self._NewOrderIndex

    @NewOrderIndex.setter
    def NewOrderIndex(self, NewOrderIndex):
        self._NewOrderIndex = NewOrderIndex


    def _deserialize(self, params):
        self._OrderIndex = params.get("OrderIndex")
        self._NewOrderIndex = params.get("NewOrderIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleInfoData(AbstractModel):
    """Rule input object

    """

    def __init__(self):
        r"""
        :param _OrderIndex: Priority
        :type OrderIndex: int
        :param _SourceIp: Access source
        :type SourceIp: str
        :param _TargetIp: Access destination
        :type TargetIp: str
        :param _Protocol: Protocol
        :type Protocol: str
        :param _Strategy: Policy. 0: observe; 1: block; 2: allow
        :type Strategy: str
        :param _SourceType: Access source type. 1: IP; 3: domain name; 4: IP address template; 5: domain name address template
        :type SourceType: int
        :param _Direction: Direction. 0: outbound; 1: inbound
        :type Direction: int
        :param _Detail: Description
        :type Detail: str
        :param _TargetType: Access destination type. 1: IP, 3: domain name; 4: IP address template; 5: domain name address template
        :type TargetType: int
        :param _Port: Port
        :type Port: str
        :param _Id: ID value
        :type Id: int
        :param _LogId: Log ID, required when an alert log is created
        :type LogId: str
        :param _City: City code
        :type City: int
        :param _Country: Country code
        :type Country: int
        :param _CloudCode: Cloud vendor. Multiple vendors are supported and separated with commas. 1: Tencent Cloud (only in Hong Kong, China and overseas); 2: Alibaba Cloud; 3: Amazon Cloud; 4: Huawei Cloud; 5: Microsoft Cloud
        :type CloudCode: str
        :param _IsRegion: Indicates whether it is a region
        :type IsRegion: int
        :param _CityName: City name
        :type CityName: str
        :param _CountryName: Country name
        :type CountryName: str
        """
        self._OrderIndex = None
        self._SourceIp = None
        self._TargetIp = None
        self._Protocol = None
        self._Strategy = None
        self._SourceType = None
        self._Direction = None
        self._Detail = None
        self._TargetType = None
        self._Port = None
        self._Id = None
        self._LogId = None
        self._City = None
        self._Country = None
        self._CloudCode = None
        self._IsRegion = None
        self._CityName = None
        self._CountryName = None

    @property
    def OrderIndex(self):
        """Priority
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def SourceIp(self):
        """Access source
        :rtype: str
        """
        return self._SourceIp

    @SourceIp.setter
    def SourceIp(self, SourceIp):
        self._SourceIp = SourceIp

    @property
    def TargetIp(self):
        """Access destination
        :rtype: str
        """
        return self._TargetIp

    @TargetIp.setter
    def TargetIp(self, TargetIp):
        self._TargetIp = TargetIp

    @property
    def Protocol(self):
        """Protocol
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Strategy(self):
        """Policy. 0: observe; 1: block; 2: allow
        :rtype: str
        """
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def SourceType(self):
        """Access source type. 1: IP; 3: domain name; 4: IP address template; 5: domain name address template
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def Direction(self):
        """Direction. 0: outbound; 1: inbound
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Detail(self):
        """Description
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def TargetType(self):
        """Access destination type. 1: IP, 3: domain name; 4: IP address template; 5: domain name address template
        :rtype: int
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def Port(self):
        """Port
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Id(self):
        """ID value
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def LogId(self):
        """Log ID, required when an alert log is created
        :rtype: str
        """
        return self._LogId

    @LogId.setter
    def LogId(self, LogId):
        self._LogId = LogId

    @property
    def City(self):
        """City code
        :rtype: int
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Country(self):
        """Country code
        :rtype: int
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def CloudCode(self):
        """Cloud vendor. Multiple vendors are supported and separated with commas. 1: Tencent Cloud (only in Hong Kong, China and overseas); 2: Alibaba Cloud; 3: Amazon Cloud; 4: Huawei Cloud; 5: Microsoft Cloud
        :rtype: str
        """
        return self._CloudCode

    @CloudCode.setter
    def CloudCode(self, CloudCode):
        self._CloudCode = CloudCode

    @property
    def IsRegion(self):
        """Indicates whether it is a region
        :rtype: int
        """
        return self._IsRegion

    @IsRegion.setter
    def IsRegion(self, IsRegion):
        self._IsRegion = IsRegion

    @property
    def CityName(self):
        """City name
        :rtype: str
        """
        return self._CityName

    @CityName.setter
    def CityName(self, CityName):
        self._CityName = CityName

    @property
    def CountryName(self):
        """Country name
        :rtype: str
        """
        return self._CountryName

    @CountryName.setter
    def CountryName(self, CountryName):
        self._CountryName = CountryName


    def _deserialize(self, params):
        self._OrderIndex = params.get("OrderIndex")
        self._SourceIp = params.get("SourceIp")
        self._TargetIp = params.get("TargetIp")
        self._Protocol = params.get("Protocol")
        self._Strategy = params.get("Strategy")
        self._SourceType = params.get("SourceType")
        self._Direction = params.get("Direction")
        self._Detail = params.get("Detail")
        self._TargetType = params.get("TargetType")
        self._Port = params.get("Port")
        self._Id = params.get("Id")
        self._LogId = params.get("LogId")
        self._City = params.get("City")
        self._Country = params.get("Country")
        self._CloudCode = params.get("CloudCode")
        self._IsRegion = params.get("IsRegion")
        self._CityName = params.get("CityName")
        self._CountryName = params.get("CountryName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanInfo(AbstractModel):
    """Getting started on scanning information

    """

    def __init__(self):
        r"""
        :param _ScanResultInfo: Scanning result information
        :type ScanResultInfo: :class:`tencentcloud.cfw.v20190904.models.ScanResultInfo`
        :param _ScanStatus: Scanning status. 0: scanning; 1: completed; 2: auto scanning unselected
        :type ScanStatus: int
        :param _ScanPercent: Progress
        :type ScanPercent: float
        :param _ScanTime: Estimated completion time
        :type ScanTime: str
        """
        self._ScanResultInfo = None
        self._ScanStatus = None
        self._ScanPercent = None
        self._ScanTime = None

    @property
    def ScanResultInfo(self):
        """Scanning result information
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ScanResultInfo`
        """
        return self._ScanResultInfo

    @ScanResultInfo.setter
    def ScanResultInfo(self, ScanResultInfo):
        self._ScanResultInfo = ScanResultInfo

    @property
    def ScanStatus(self):
        """Scanning status. 0: scanning; 1: completed; 2: auto scanning unselected
        :rtype: int
        """
        return self._ScanStatus

    @ScanStatus.setter
    def ScanStatus(self, ScanStatus):
        self._ScanStatus = ScanStatus

    @property
    def ScanPercent(self):
        """Progress
        :rtype: float
        """
        return self._ScanPercent

    @ScanPercent.setter
    def ScanPercent(self, ScanPercent):
        self._ScanPercent = ScanPercent

    @property
    def ScanTime(self):
        """Estimated completion time
        :rtype: str
        """
        return self._ScanTime

    @ScanTime.setter
    def ScanTime(self, ScanTime):
        self._ScanTime = ScanTime


    def _deserialize(self, params):
        if params.get("ScanResultInfo") is not None:
            self._ScanResultInfo = ScanResultInfo()
            self._ScanResultInfo._deserialize(params.get("ScanResultInfo"))
        self._ScanStatus = params.get("ScanStatus")
        self._ScanPercent = params.get("ScanPercent")
        self._ScanTime = params.get("ScanTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanResultInfo(AbstractModel):
    """Getting started on scanning result information PortNum   int
    	LeakNum   int
    	IPNum     int
    	IPStatus  bool
    	IdpStatus bool
    	BanStatus bool

    """

    def __init__(self):
        r"""
        :param _LeakNum: Number of vulnerability exploits
        :type LeakNum: int
        :param _IPNum: Number of protected IPs
        :type IPNum: int
        :param _PortNum: Number of exposed ports
        :type PortNum: int
        :param _IPStatus: Protection status
        :type IPStatus: bool
        :param _IdpStatus: Attack blocking status
        :type IdpStatus: bool
        :param _BanStatus: Port blocking status
        :type BanStatus: bool
        """
        self._LeakNum = None
        self._IPNum = None
        self._PortNum = None
        self._IPStatus = None
        self._IdpStatus = None
        self._BanStatus = None

    @property
    def LeakNum(self):
        """Number of vulnerability exploits
        :rtype: int
        """
        return self._LeakNum

    @LeakNum.setter
    def LeakNum(self, LeakNum):
        self._LeakNum = LeakNum

    @property
    def IPNum(self):
        """Number of protected IPs
        :rtype: int
        """
        return self._IPNum

    @IPNum.setter
    def IPNum(self, IPNum):
        self._IPNum = IPNum

    @property
    def PortNum(self):
        """Number of exposed ports
        :rtype: int
        """
        return self._PortNum

    @PortNum.setter
    def PortNum(self, PortNum):
        self._PortNum = PortNum

    @property
    def IPStatus(self):
        """Protection status
        :rtype: bool
        """
        return self._IPStatus

    @IPStatus.setter
    def IPStatus(self, IPStatus):
        self._IPStatus = IPStatus

    @property
    def IdpStatus(self):
        """Attack blocking status
        :rtype: bool
        """
        return self._IdpStatus

    @IdpStatus.setter
    def IdpStatus(self, IdpStatus):
        self._IdpStatus = IdpStatus

    @property
    def BanStatus(self):
        """Port blocking status
        :rtype: bool
        """
        return self._BanStatus

    @BanStatus.setter
    def BanStatus(self, BanStatus):
        self._BanStatus = BanStatus


    def _deserialize(self, params):
        self._LeakNum = params.get("LeakNum")
        self._IPNum = params.get("IPNum")
        self._PortNum = params.get("PortNum")
        self._IPStatus = params.get("IPStatus")
        self._IdpStatus = params.get("IdpStatus")
        self._BanStatus = params.get("BanStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupBothWayInfo(AbstractModel):
    """Two-way enterprise security group rules

    """

    def __init__(self):
        r"""
        :param _OrderIndex: Priority
Note: This field may return `null`, indicating that no valid value was found.
        :type OrderIndex: int
        :param _SourceId: Access source
Note: This field may return `null`, indicating that no valid value was found.
        :type SourceId: str
        :param _SourceType: Access source type. Default: 0. 0: IP; 1: VPC; 2: SUBNET; 3: CVM; 4: CLB; 5: ENI; 6: CDB; 7: Parameter template. 100: asset group
Note: This field may return `null`, indicating that no valid value was found.
        :type SourceType: int
        :param _TargetId: Access destination
Note: This field may return `null`, indicating that no valid value was found.
        :type TargetId: str
        :param _TargetType: Access destination type. Default: 0. 0: IP; 1: VPC; 2: SUBNET; 3: CVM; 4: CLB; 5: ENI; 6: CDB; 7: Parameter template. 100: asset group
Note: This field may return `null`, indicating that no valid value was found.
        :type TargetType: int
        :param _Protocol: Protocol
Note: This field may return `null`, indicating that no valid value was found.
        :type Protocol: str
        :param _Port: Destination port
Note: This field may return `null`, indicating that no valid value was found.
        :type Port: str
        :param _Strategy: Policy. 1: block; 2: allow
Note: This field may return `null`, indicating that no valid value was found.
        :type Strategy: int
        :param _Direction: Direction. 0: outbound; 1: inbound. 1 by default
Note: This field may return `null`, indicating that no valid value was found.
        :type Direction: int
        :param _Region: Region
        :type Region: str
        :param _Detail: Description
Note: This field may return `null`, indicating that no valid value was found.
        :type Detail: str
        :param _Status: Toggle status. 0: off; 1: on
Note: This field may return `null`, indicating that no valid value was found.
        :type Status: int
        :param _IsNew: Indicates whether the rule is normal. 0: normal; 1: abnormal
Note: This field may return `null`, indicating that no valid value was found.
        :type IsNew: int
        :param _BothWay: One-way/two-way. 0: one-way; 1: two-way
Note: This field may return `null`, indicating that no valid value was found.
        :type BothWay: int
        :param _VpcId: VPC ID
Note: This field may return `null`, indicating that no valid value was found.
        :type VpcId: str
        :param _SubnetId: Subnet ID
Note: This field may return `null`, indicating that no valid value was found.
        :type SubnetId: str
        :param _InstanceName: Instance name
Note: This field may return `null`, indicating that no valid value was found.
        :type InstanceName: str
        :param _PublicIp: Public IP. Multiple IPs are separated by commas.
Note: This field may return `null`, indicating that no valid value was found.
        :type PublicIp: str
        :param _PrivateIp: Private IP. Multiple IPs are separated by commas.
Note: This field may return `null`, indicating that no valid value was found.
        :type PrivateIp: str
        :param _Cidr: Masked address. Multiple addresses are separated by commas.
Note: This field may return `null`, indicating that no valid value was found.
        :type Cidr: str
        :param _ServiceTemplateId: Port protocol template ID
Note: This field may return `null`, indicating that no valid value was found.
        :type ServiceTemplateId: str
        :param _ProtocolPortType: Indicates whether to use the port protocol template. 0: no; 1: yes
        :type ProtocolPortType: int
        """
        self._OrderIndex = None
        self._SourceId = None
        self._SourceType = None
        self._TargetId = None
        self._TargetType = None
        self._Protocol = None
        self._Port = None
        self._Strategy = None
        self._Direction = None
        self._Region = None
        self._Detail = None
        self._Status = None
        self._IsNew = None
        self._BothWay = None
        self._VpcId = None
        self._SubnetId = None
        self._InstanceName = None
        self._PublicIp = None
        self._PrivateIp = None
        self._Cidr = None
        self._ServiceTemplateId = None
        self._ProtocolPortType = None

    @property
    def OrderIndex(self):
        """Priority
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def SourceId(self):
        """Access source
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def SourceType(self):
        """Access source type. Default: 0. 0: IP; 1: VPC; 2: SUBNET; 3: CVM; 4: CLB; 5: ENI; 6: CDB; 7: Parameter template. 100: asset group
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def TargetId(self):
        """Access destination
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def TargetType(self):
        """Access destination type. Default: 0. 0: IP; 1: VPC; 2: SUBNET; 3: CVM; 4: CLB; 5: ENI; 6: CDB; 7: Parameter template. 100: asset group
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def Protocol(self):
        """Protocol
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        """Destination port
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Strategy(self):
        """Policy. 1: block; 2: allow
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def Direction(self):
        """Direction. 0: outbound; 1: inbound. 1 by default
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Region(self):
        """Region
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Detail(self):
        """Description
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Status(self):
        """Toggle status. 0: off; 1: on
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsNew(self):
        """Indicates whether the rule is normal. 0: normal; 1: abnormal
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def BothWay(self):
        """One-way/two-way. 0: one-way; 1: two-way
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._BothWay

    @BothWay.setter
    def BothWay(self, BothWay):
        self._BothWay = BothWay

    @property
    def VpcId(self):
        """VPC ID
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Subnet ID
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def InstanceName(self):
        """Instance name
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def PublicIp(self):
        """Public IP. Multiple IPs are separated by commas.
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        """Private IP. Multiple IPs are separated by commas.
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def Cidr(self):
        """Masked address. Multiple addresses are separated by commas.
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._Cidr

    @Cidr.setter
    def Cidr(self, Cidr):
        self._Cidr = Cidr

    @property
    def ServiceTemplateId(self):
        """Port protocol template ID
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._ServiceTemplateId

    @ServiceTemplateId.setter
    def ServiceTemplateId(self, ServiceTemplateId):
        self._ServiceTemplateId = ServiceTemplateId

    @property
    def ProtocolPortType(self):
        """Indicates whether to use the port protocol template. 0: no; 1: yes
        :rtype: int
        """
        return self._ProtocolPortType

    @ProtocolPortType.setter
    def ProtocolPortType(self, ProtocolPortType):
        self._ProtocolPortType = ProtocolPortType


    def _deserialize(self, params):
        self._OrderIndex = params.get("OrderIndex")
        self._SourceId = params.get("SourceId")
        self._SourceType = params.get("SourceType")
        self._TargetId = params.get("TargetId")
        self._TargetType = params.get("TargetType")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._Strategy = params.get("Strategy")
        self._Direction = params.get("Direction")
        self._Region = params.get("Region")
        self._Detail = params.get("Detail")
        self._Status = params.get("Status")
        self._IsNew = params.get("IsNew")
        self._BothWay = params.get("BothWay")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._InstanceName = params.get("InstanceName")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._Cidr = params.get("Cidr")
        self._ServiceTemplateId = params.get("ServiceTemplateId")
        self._ProtocolPortType = params.get("ProtocolPortType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupListData(AbstractModel):
    """Security group list data

    """

    def __init__(self):
        r"""
        :param _OrderIndex: Priority
        :type OrderIndex: int
        :param _SourceId: Access source
        :type SourceId: str
        :param _SourceType: Access source type. Default: 0. 1: VPC; 2: SUBNET; 3: CVM; 4: CLB; 5: ENI; 6: CDB; 7: Parameter template. 100: Resource group
        :type SourceType: int
        :param _TargetId: Access destination
        :type TargetId: str
        :param _TargetType: Access destination type. Default: 0. 1: VPC; 2: SUBNET; 3: CVM; 4: CLB; 5: ENI; 6: CDB; 7: Parameter template; 100: resource group
        :type TargetType: int
        :param _Protocol: Protocol
        :type Protocol: str
        :param _Port: Destination port
        :type Port: str
        :param _Strategy: Policy. 1: block; 2: allow
        :type Strategy: int
        :param _Detail: Description
        :type Detail: str
        :param _BothWay: One-way/two-way. 0: one-way; 1: two-way
        :type BothWay: int
        :param _Id: Rule ID
        :type Id: int
        :param _Status: Toggle status. 0: off; 1: on
        :type Status: int
        :param _IsNew: Indicates whether the rule is normal. 0: normal; 1: abnormal
        :type IsNew: int
        :param _VpcId: VPC ID
Note: This field may return `null`, indicating that no valid value was found.
        :type VpcId: str
        :param _SubnetId: Subnet ID
Note: This field may return `null`, indicating that no valid value was found.
        :type SubnetId: str
        :param _InstanceName: Instance name
Note: This field may return `null`, indicating that no valid value was found.
        :type InstanceName: str
        :param _PublicIp: Public IP. Multiple IPs are separated by commas.
Note: This field may return `null`, indicating that no valid value was found.
        :type PublicIp: str
        :param _PrivateIp: Private IP. Multiple IPs are separated by commas.
Note: This field may return `null`, indicating that no valid value was found.
        :type PrivateIp: str
        :param _Cidr: Masked address. Multiple addresses are separated by commas.
Note: This field may return `null`, indicating that no valid value was found.
        :type Cidr: str
        :param _ServiceTemplateId: Port protocol template ID
Note: This field may return `null`, indicating that no valid value was found.
        :type ServiceTemplateId: str
        :param _BothWayInfo: Two-way rules
Note: This field may return `null`, indicating that no valid value was found.
        :type BothWayInfo: list of SecurityGroupBothWayInfo
        :param _Direction: Direction. 0: outbound; 1: inbound. 1 by default
        :type Direction: int
        :param _ProtocolPortType: Indicates whether to use the port protocol template. 0: no; 1: yes
        :type ProtocolPortType: int
        """
        self._OrderIndex = None
        self._SourceId = None
        self._SourceType = None
        self._TargetId = None
        self._TargetType = None
        self._Protocol = None
        self._Port = None
        self._Strategy = None
        self._Detail = None
        self._BothWay = None
        self._Id = None
        self._Status = None
        self._IsNew = None
        self._VpcId = None
        self._SubnetId = None
        self._InstanceName = None
        self._PublicIp = None
        self._PrivateIp = None
        self._Cidr = None
        self._ServiceTemplateId = None
        self._BothWayInfo = None
        self._Direction = None
        self._ProtocolPortType = None

    @property
    def OrderIndex(self):
        """Priority
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def SourceId(self):
        """Access source
        :rtype: str
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def SourceType(self):
        """Access source type. Default: 0. 1: VPC; 2: SUBNET; 3: CVM; 4: CLB; 5: ENI; 6: CDB; 7: Parameter template. 100: Resource group
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def TargetId(self):
        """Access destination
        :rtype: str
        """
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def TargetType(self):
        """Access destination type. Default: 0. 1: VPC; 2: SUBNET; 3: CVM; 4: CLB; 5: ENI; 6: CDB; 7: Parameter template; 100: resource group
        :rtype: int
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def Protocol(self):
        """Protocol
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        """Destination port
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Strategy(self):
        """Policy. 1: block; 2: allow
        :rtype: int
        """
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def Detail(self):
        """Description
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def BothWay(self):
        """One-way/two-way. 0: one-way; 1: two-way
        :rtype: int
        """
        return self._BothWay

    @BothWay.setter
    def BothWay(self, BothWay):
        self._BothWay = BothWay

    @property
    def Id(self):
        """Rule ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Status(self):
        """Toggle status. 0: off; 1: on
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsNew(self):
        """Indicates whether the rule is normal. 0: normal; 1: abnormal
        :rtype: int
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def VpcId(self):
        """VPC ID
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Subnet ID
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def InstanceName(self):
        """Instance name
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def PublicIp(self):
        """Public IP. Multiple IPs are separated by commas.
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        """Private IP. Multiple IPs are separated by commas.
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def Cidr(self):
        """Masked address. Multiple addresses are separated by commas.
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._Cidr

    @Cidr.setter
    def Cidr(self, Cidr):
        self._Cidr = Cidr

    @property
    def ServiceTemplateId(self):
        """Port protocol template ID
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._ServiceTemplateId

    @ServiceTemplateId.setter
    def ServiceTemplateId(self, ServiceTemplateId):
        self._ServiceTemplateId = ServiceTemplateId

    @property
    def BothWayInfo(self):
        """Two-way rules
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: list of SecurityGroupBothWayInfo
        """
        return self._BothWayInfo

    @BothWayInfo.setter
    def BothWayInfo(self, BothWayInfo):
        self._BothWayInfo = BothWayInfo

    @property
    def Direction(self):
        """Direction. 0: outbound; 1: inbound. 1 by default
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def ProtocolPortType(self):
        """Indicates whether to use the port protocol template. 0: no; 1: yes
        :rtype: int
        """
        return self._ProtocolPortType

    @ProtocolPortType.setter
    def ProtocolPortType(self, ProtocolPortType):
        self._ProtocolPortType = ProtocolPortType


    def _deserialize(self, params):
        self._OrderIndex = params.get("OrderIndex")
        self._SourceId = params.get("SourceId")
        self._SourceType = params.get("SourceType")
        self._TargetId = params.get("TargetId")
        self._TargetType = params.get("TargetType")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._Strategy = params.get("Strategy")
        self._Detail = params.get("Detail")
        self._BothWay = params.get("BothWay")
        self._Id = params.get("Id")
        self._Status = params.get("Status")
        self._IsNew = params.get("IsNew")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._InstanceName = params.get("InstanceName")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._Cidr = params.get("Cidr")
        self._ServiceTemplateId = params.get("ServiceTemplateId")
        if params.get("BothWayInfo") is not None:
            self._BothWayInfo = []
            for item in params.get("BothWayInfo"):
                obj = SecurityGroupBothWayInfo()
                obj._deserialize(item)
                self._BothWayInfo.append(obj)
        self._Direction = params.get("Direction")
        self._ProtocolPortType = params.get("ProtocolPortType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupOrderIndexData(AbstractModel):
    """Change priority of enterprise security group rules

    """

    def __init__(self):
        r"""
        :param _OrderIndex: Current priority of enterprise security group rules
        :type OrderIndex: int
        :param _NewOrderIndex: New priority of enterprise security group rules
        :type NewOrderIndex: int
        """
        self._OrderIndex = None
        self._NewOrderIndex = None

    @property
    def OrderIndex(self):
        """Current priority of enterprise security group rules
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def NewOrderIndex(self):
        """New priority of enterprise security group rules
        :rtype: int
        """
        return self._NewOrderIndex

    @NewOrderIndex.setter
    def NewOrderIndex(self, NewOrderIndex):
        self._NewOrderIndex = NewOrderIndex


    def _deserialize(self, params):
        self._OrderIndex = params.get("OrderIndex")
        self._NewOrderIndex = params.get("NewOrderIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupRule(AbstractModel):
    """Security group rules

    """

    def __init__(self):
        r"""
        :param _SourceContent: Source example:
net: IP/CIDR (192.168.0.2)
template: parameter template (ipm-dyodhpby)
instance: asset instance (ins-123456)
resourcegroup: asset group (/all groups/group 1/subgroup 1)
tag: resource tag ({"Key":"tag key","Value":"tag value"})
region: region (ap-gaungzhou)
        :type SourceContent: str
        :param _SourceType: Access source type. Valid values: net|template|instance|resourcegroup|tag|region
        :type SourceType: str
        :param _DestContent: Destination example:
net: IP/CIDR (192.168.0.2)
template: parameter template (ipm-dyodhpby)
instance: asset instance (ins-123456)
resourcegroup: asset group (/all groups/group 1/subgroup 1)
tag: resource tag ({"Key":"tag key","Value":"tag value"})
region: region (ap-gaungzhou)
        :type DestContent: str
        :param _DestType: Access destination type. Valid values: net|template|instance|resourcegroup|tag|region
        :type DestType: str
        :param _RuleAction: The action that Cloud Firewall performs on the traffic. Valid values:
accept: allow
drop: deny
        :type RuleAction: str
        :param _Description: Description
        :type Description: str
        :param _OrderIndex: Rule priority. -1: lowest; 1: highest
        :type OrderIndex: str
        :param _Protocol: Protocol. TCP/UDP/ICMP/ANY
Note: This field may return `null`, indicating that no valid value was found.
        :type Protocol: str
        :param _Port: The port to apply access control rules. Valid values:
-1/-1: all ports
80: port 80
Note: This field may return `null`, indicating that no valid value was found.
        :type Port: str
        :param _ServiceTemplateId: Parameter template ID of port and protocol type; mutually exclusive with Protocol and Port
Note: This field may return `null`, indicating that no valid value was found.
        :type ServiceTemplateId: str
        :param _Id: The unique ID of the rule
        :type Id: str
        :param _Enable: Rule status. true: enabled; false: disabled
        :type Enable: str
        """
        self._SourceContent = None
        self._SourceType = None
        self._DestContent = None
        self._DestType = None
        self._RuleAction = None
        self._Description = None
        self._OrderIndex = None
        self._Protocol = None
        self._Port = None
        self._ServiceTemplateId = None
        self._Id = None
        self._Enable = None

    @property
    def SourceContent(self):
        """Source example:
net: IP/CIDR (192.168.0.2)
template: parameter template (ipm-dyodhpby)
instance: asset instance (ins-123456)
resourcegroup: asset group (/all groups/group 1/subgroup 1)
tag: resource tag ({"Key":"tag key","Value":"tag value"})
region: region (ap-gaungzhou)
        :rtype: str
        """
        return self._SourceContent

    @SourceContent.setter
    def SourceContent(self, SourceContent):
        self._SourceContent = SourceContent

    @property
    def SourceType(self):
        """Access source type. Valid values: net|template|instance|resourcegroup|tag|region
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def DestContent(self):
        """Destination example:
net: IP/CIDR (192.168.0.2)
template: parameter template (ipm-dyodhpby)
instance: asset instance (ins-123456)
resourcegroup: asset group (/all groups/group 1/subgroup 1)
tag: resource tag ({"Key":"tag key","Value":"tag value"})
region: region (ap-gaungzhou)
        :rtype: str
        """
        return self._DestContent

    @DestContent.setter
    def DestContent(self, DestContent):
        self._DestContent = DestContent

    @property
    def DestType(self):
        """Access destination type. Valid values: net|template|instance|resourcegroup|tag|region
        :rtype: str
        """
        return self._DestType

    @DestType.setter
    def DestType(self, DestType):
        self._DestType = DestType

    @property
    def RuleAction(self):
        """The action that Cloud Firewall performs on the traffic. Valid values:
accept: allow
drop: deny
        :rtype: str
        """
        return self._RuleAction

    @RuleAction.setter
    def RuleAction(self, RuleAction):
        self._RuleAction = RuleAction

    @property
    def Description(self):
        """Description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def OrderIndex(self):
        """Rule priority. -1: lowest; 1: highest
        :rtype: str
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def Protocol(self):
        """Protocol. TCP/UDP/ICMP/ANY
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        """The port to apply access control rules. Valid values:
-1/-1: all ports
80: port 80
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceTemplateId(self):
        """Parameter template ID of port and protocol type; mutually exclusive with Protocol and Port
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._ServiceTemplateId

    @ServiceTemplateId.setter
    def ServiceTemplateId(self, ServiceTemplateId):
        self._ServiceTemplateId = ServiceTemplateId

    @property
    def Id(self):
        """The unique ID of the rule
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Enable(self):
        """Rule status. true: enabled; false: disabled
        :rtype: str
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._SourceContent = params.get("SourceContent")
        self._SourceType = params.get("SourceType")
        self._DestContent = params.get("DestContent")
        self._DestType = params.get("DestType")
        self._RuleAction = params.get("RuleAction")
        self._Description = params.get("Description")
        self._OrderIndex = params.get("OrderIndex")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._ServiceTemplateId = params.get("ServiceTemplateId")
        self._Id = params.get("Id")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SequenceData(AbstractModel):
    """Priority

    """

    def __init__(self):
        r"""
        :param _Id: Rule ID
        :type Id: int
        :param _OrderIndex: Rule priority before change
        :type OrderIndex: int
        :param _NewOrderIndex: Rule priority after change
        :type NewOrderIndex: int
        """
        self._Id = None
        self._OrderIndex = None
        self._NewOrderIndex = None

    @property
    def Id(self):
        """Rule ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def OrderIndex(self):
        """Rule priority before change
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def NewOrderIndex(self):
        """Rule priority after change
        :rtype: int
        """
        return self._NewOrderIndex

    @NewOrderIndex.setter
    def NewOrderIndex(self, NewOrderIndex):
        self._NewOrderIndex = NewOrderIndex


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._OrderIndex = params.get("OrderIndex")
        self._NewOrderIndex = params.get("NewOrderIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetNatFwDnatRuleRequest(AbstractModel):
    """SetNatFwDnatRule request structure.

    """

    def __init__(self):
        r"""
        :param _Mode: 0: Create new; 1: Use existing
        :type Mode: int
        :param _OperationType: Operation type. Valid values: add, del, and modify.
        :type OperationType: str
        :param _CfwInstance: Firewall instance ID. This field is required.
        :type CfwInstance: str
        :param _AddOrDelDnatRules: List of added/deleted DNAT rules
        :type AddOrDelDnatRules: list of CfwNatDnatRule
        :param _OriginDnat: Original DNAT rule before change
        :type OriginDnat: :class:`tencentcloud.cfw.v20190904.models.CfwNatDnatRule`
        :param _NewDnat: New DNAT rule after change
        :type NewDnat: :class:`tencentcloud.cfw.v20190904.models.CfwNatDnatRule`
        """
        self._Mode = None
        self._OperationType = None
        self._CfwInstance = None
        self._AddOrDelDnatRules = None
        self._OriginDnat = None
        self._NewDnat = None

    @property
    def Mode(self):
        """0: Create new; 1: Use existing
        :rtype: int
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def OperationType(self):
        """Operation type. Valid values: add, del, and modify.
        :rtype: str
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType

    @property
    def CfwInstance(self):
        """Firewall instance ID. This field is required.
        :rtype: str
        """
        return self._CfwInstance

    @CfwInstance.setter
    def CfwInstance(self, CfwInstance):
        self._CfwInstance = CfwInstance

    @property
    def AddOrDelDnatRules(self):
        """List of added/deleted DNAT rules
        :rtype: list of CfwNatDnatRule
        """
        return self._AddOrDelDnatRules

    @AddOrDelDnatRules.setter
    def AddOrDelDnatRules(self, AddOrDelDnatRules):
        self._AddOrDelDnatRules = AddOrDelDnatRules

    @property
    def OriginDnat(self):
        """Original DNAT rule before change
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CfwNatDnatRule`
        """
        return self._OriginDnat

    @OriginDnat.setter
    def OriginDnat(self, OriginDnat):
        self._OriginDnat = OriginDnat

    @property
    def NewDnat(self):
        """New DNAT rule after change
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CfwNatDnatRule`
        """
        return self._NewDnat

    @NewDnat.setter
    def NewDnat(self, NewDnat):
        self._NewDnat = NewDnat


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._OperationType = params.get("OperationType")
        self._CfwInstance = params.get("CfwInstance")
        if params.get("AddOrDelDnatRules") is not None:
            self._AddOrDelDnatRules = []
            for item in params.get("AddOrDelDnatRules"):
                obj = CfwNatDnatRule()
                obj._deserialize(item)
                self._AddOrDelDnatRules.append(obj)
        if params.get("OriginDnat") is not None:
            self._OriginDnat = CfwNatDnatRule()
            self._OriginDnat._deserialize(params.get("OriginDnat"))
        if params.get("NewDnat") is not None:
            self._NewDnat = CfwNatDnatRule()
            self._NewDnat._deserialize(params.get("NewDnat"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetNatFwDnatRuleResponse(AbstractModel):
    """SetNatFwDnatRule response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SetNatFwEipRequest(AbstractModel):
    """SetNatFwEip request structure.

    """

    def __init__(self):
        r"""
        :param _OperationType: bind: bind EIP; unbind: unbind EIP; newAdd: add firewall EIP
        :type OperationType: str
        :param _CfwInstance: Firewall instance ID
        :type CfwInstance: str
        :param _EipList: This field is required when OperationType is "bind" or "unbind".
        :type EipList: list of str
        """
        self._OperationType = None
        self._CfwInstance = None
        self._EipList = None

    @property
    def OperationType(self):
        """bind: bind EIP; unbind: unbind EIP; newAdd: add firewall EIP
        :rtype: str
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType

    @property
    def CfwInstance(self):
        """Firewall instance ID
        :rtype: str
        """
        return self._CfwInstance

    @CfwInstance.setter
    def CfwInstance(self, CfwInstance):
        self._CfwInstance = CfwInstance

    @property
    def EipList(self):
        """This field is required when OperationType is "bind" or "unbind".
        :rtype: list of str
        """
        return self._EipList

    @EipList.setter
    def EipList(self, EipList):
        self._EipList = EipList


    def _deserialize(self, params):
        self._OperationType = params.get("OperationType")
        self._CfwInstance = params.get("CfwInstance")
        self._EipList = params.get("EipList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetNatFwEipResponse(AbstractModel):
    """SetNatFwEip response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StaticInfo(AbstractModel):
    """Most frequent attacker statistics


    """

    def __init__(self):
        r"""
        :param _Num: Number
        :type Num: int
        :param _Port: Port
        :type Port: str
        :param _Ip: IP
        :type Ip: str
        :param _Address: Address
        :type Address: str
        :param _InsID: Asset ID
        :type InsID: str
        :param _InsName: Asset name
        :type InsName: str
        """
        self._Num = None
        self._Port = None
        self._Ip = None
        self._Address = None
        self._InsID = None
        self._InsName = None

    @property
    def Num(self):
        """Number
        :rtype: int
        """
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

    @property
    def Port(self):
        """Port
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Ip(self):
        """IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Address(self):
        """Address
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def InsID(self):
        """Asset ID
        :rtype: str
        """
        return self._InsID

    @InsID.setter
    def InsID(self, InsID):
        self._InsID = InsID

    @property
    def InsName(self):
        """Asset name
        :rtype: str
        """
        return self._InsName

    @InsName.setter
    def InsName(self, InsName):
        self._InsName = InsName


    def _deserialize(self, params):
        self._Num = params.get("Num")
        self._Port = params.get("Port")
        self._Ip = params.get("Ip")
        self._Address = params.get("Address")
        self._InsID = params.get("InsID")
        self._InsName = params.get("InsName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopSecurityGroupRuleDispatchRequest(AbstractModel):
    """StopSecurityGroupRuleDispatch request structure.

    """

    def __init__(self):
        r"""
        :param _StopType: Stops all if set to 1
        :type StopType: int
        """
        self._StopType = None

    @property
    def StopType(self):
        """Stops all if set to 1
        :rtype: int
        """
        return self._StopType

    @StopType.setter
    def StopType(self, StopType):
        self._StopType = StopType


    def _deserialize(self, params):
        self._StopType = params.get("StopType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopSecurityGroupRuleDispatchResponse(AbstractModel):
    """StopSecurityGroupRuleDispatch response structure.

    """

    def __init__(self):
        r"""
        :param _Status: true: operation successful; false: error
Note: This field may return `null`, indicating that no valid value was found.
        :type Status: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """true: operation successful; false: error
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class SwitchListsData(AbstractModel):
    """Firewall status list

    """

    def __init__(self):
        r"""
        :param _PublicIp: Public IP
Note: This field may return `null`, indicating that no valid value was found.
        :type PublicIp: str
        :param _IntranetIp: Private IP
Note: This field may return `null`, indicating that no valid value was found.
        :type IntranetIp: str
        :param _InstanceName: Instance name
Note: This field may return `null`, indicating that no valid value was found.
        :type InstanceName: str
        :param _InstanceId: Instance ID
Note: This field may return `null`, indicating that no valid value was found.
        :type InstanceId: str
        :param _AssetType: Asset type
        :type AssetType: str
        :param _Area: Region
Note: This field may return `null`, indicating that no valid value was found.
        :type Area: str
        :param _Switch: Firewall toggle
        :type Switch: int
        :param _Id: ID value
        :type Id: int
        :param _PublicIpType: Public IP type
Note: This field may return `null`, indicating that no valid value was found.
        :type PublicIpType: int
        :param _PortTimes: Number of risky ports
Note: This field may return `null`, indicating that no valid value was found.
        :type PortTimes: int
        :param _LastTime: Last scan time
Note: This field may return `null`, indicating that no valid value was found.
        :type LastTime: str
        :param _ScanMode: Scan mode
Note: This field may return `null`, indicating that no valid value was found.
        :type ScanMode: str
        :param _ScanStatus: Scan status
Note: This field may return `null`, indicating that no valid value was found.
        :type ScanStatus: int
        """
        self._PublicIp = None
        self._IntranetIp = None
        self._InstanceName = None
        self._InstanceId = None
        self._AssetType = None
        self._Area = None
        self._Switch = None
        self._Id = None
        self._PublicIpType = None
        self._PortTimes = None
        self._LastTime = None
        self._ScanMode = None
        self._ScanStatus = None

    @property
    def PublicIp(self):
        """Public IP
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def IntranetIp(self):
        """Private IP
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._IntranetIp

    @IntranetIp.setter
    def IntranetIp(self, IntranetIp):
        self._IntranetIp = IntranetIp

    @property
    def InstanceName(self):
        """Instance name
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceId(self):
        """Instance ID
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AssetType(self):
        """Asset type
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def Area(self):
        """Region
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Switch(self):
        """Firewall toggle
        :rtype: int
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Id(self):
        """ID value
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PublicIpType(self):
        """Public IP type
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._PublicIpType

    @PublicIpType.setter
    def PublicIpType(self, PublicIpType):
        self._PublicIpType = PublicIpType

    @property
    def PortTimes(self):
        """Number of risky ports
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._PortTimes

    @PortTimes.setter
    def PortTimes(self, PortTimes):
        self._PortTimes = PortTimes

    @property
    def LastTime(self):
        """Last scan time
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._LastTime

    @LastTime.setter
    def LastTime(self, LastTime):
        self._LastTime = LastTime

    @property
    def ScanMode(self):
        """Scan mode
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._ScanMode

    @ScanMode.setter
    def ScanMode(self, ScanMode):
        self._ScanMode = ScanMode

    @property
    def ScanStatus(self):
        """Scan status
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._ScanStatus

    @ScanStatus.setter
    def ScanStatus(self, ScanStatus):
        self._ScanStatus = ScanStatus


    def _deserialize(self, params):
        self._PublicIp = params.get("PublicIp")
        self._IntranetIp = params.get("IntranetIp")
        self._InstanceName = params.get("InstanceName")
        self._InstanceId = params.get("InstanceId")
        self._AssetType = params.get("AssetType")
        self._Area = params.get("Area")
        self._Switch = params.get("Switch")
        self._Id = params.get("Id")
        self._PublicIpType = params.get("PublicIpType")
        self._PortTimes = params.get("PortTimes")
        self._LastTime = params.get("LastTime")
        self._ScanMode = params.get("ScanMode")
        self._ScanStatus = params.get("ScanStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TLogInfo(AbstractModel):
    """Alert monitoring data

    """

    def __init__(self):
        r"""
        :param _OutNum: Compromised servers
        :type OutNum: int
        :param _HandleNum: Unhandled alerts
        :type HandleNum: int
        :param _VulNum: Vulnerability attacks
        :type VulNum: int
        :param _NetworkNum: Detected networks
        :type NetworkNum: int
        :param _BanNum: Blocklist
        :type BanNum: int
        :param _BruteForceNum: Brute force attacks
        :type BruteForceNum: int
        """
        self._OutNum = None
        self._HandleNum = None
        self._VulNum = None
        self._NetworkNum = None
        self._BanNum = None
        self._BruteForceNum = None

    @property
    def OutNum(self):
        """Compromised servers
        :rtype: int
        """
        return self._OutNum

    @OutNum.setter
    def OutNum(self, OutNum):
        self._OutNum = OutNum

    @property
    def HandleNum(self):
        """Unhandled alerts
        :rtype: int
        """
        return self._HandleNum

    @HandleNum.setter
    def HandleNum(self, HandleNum):
        self._HandleNum = HandleNum

    @property
    def VulNum(self):
        """Vulnerability attacks
        :rtype: int
        """
        return self._VulNum

    @VulNum.setter
    def VulNum(self, VulNum):
        self._VulNum = VulNum

    @property
    def NetworkNum(self):
        """Detected networks
        :rtype: int
        """
        return self._NetworkNum

    @NetworkNum.setter
    def NetworkNum(self, NetworkNum):
        self._NetworkNum = NetworkNum

    @property
    def BanNum(self):
        """Blocklist
        :rtype: int
        """
        return self._BanNum

    @BanNum.setter
    def BanNum(self, BanNum):
        self._BanNum = BanNum

    @property
    def BruteForceNum(self):
        """Brute force attacks
        :rtype: int
        """
        return self._BruteForceNum

    @BruteForceNum.setter
    def BruteForceNum(self, BruteForceNum):
        self._BruteForceNum = BruteForceNum


    def _deserialize(self, params):
        self._OutNum = params.get("OutNum")
        self._HandleNum = params.get("HandleNum")
        self._VulNum = params.get("VulNum")
        self._NetworkNum = params.get("NetworkNum")
        self._BanNum = params.get("BanNum")
        self._BruteForceNum = params.get("BruteForceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnHandleEvent(AbstractModel):
    """Unhandled event details

    """

    def __init__(self):
        r"""
        :param _EventTableListStruct: Unhandled event type
        :type EventTableListStruct: list of UnHandleEventDetail
        :param _BaseLineUser: 1: yes; 0: no
        :type BaseLineUser: int
        :param _BaseLineInSwitch: 1: on; 0: off
        :type BaseLineInSwitch: int
        :param _BaseLineOutSwitch: 1: on; 0: off
        :type BaseLineOutSwitch: int
        :param _VpcFwCount: Number of inter-VPC firewall instances
Note: This field may return `null`, indicating that no valid value was found.
        :type VpcFwCount: int
        """
        self._EventTableListStruct = None
        self._BaseLineUser = None
        self._BaseLineInSwitch = None
        self._BaseLineOutSwitch = None
        self._VpcFwCount = None

    @property
    def EventTableListStruct(self):
        """Unhandled event type
        :rtype: list of UnHandleEventDetail
        """
        return self._EventTableListStruct

    @EventTableListStruct.setter
    def EventTableListStruct(self, EventTableListStruct):
        self._EventTableListStruct = EventTableListStruct

    @property
    def BaseLineUser(self):
        """1: yes; 0: no
        :rtype: int
        """
        return self._BaseLineUser

    @BaseLineUser.setter
    def BaseLineUser(self, BaseLineUser):
        self._BaseLineUser = BaseLineUser

    @property
    def BaseLineInSwitch(self):
        """1: on; 0: off
        :rtype: int
        """
        return self._BaseLineInSwitch

    @BaseLineInSwitch.setter
    def BaseLineInSwitch(self, BaseLineInSwitch):
        self._BaseLineInSwitch = BaseLineInSwitch

    @property
    def BaseLineOutSwitch(self):
        """1: on; 0: off
        :rtype: int
        """
        return self._BaseLineOutSwitch

    @BaseLineOutSwitch.setter
    def BaseLineOutSwitch(self, BaseLineOutSwitch):
        self._BaseLineOutSwitch = BaseLineOutSwitch

    @property
    def VpcFwCount(self):
        """Number of inter-VPC firewall instances
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._VpcFwCount

    @VpcFwCount.setter
    def VpcFwCount(self, VpcFwCount):
        self._VpcFwCount = VpcFwCount


    def _deserialize(self, params):
        if params.get("EventTableListStruct") is not None:
            self._EventTableListStruct = []
            for item in params.get("EventTableListStruct"):
                obj = UnHandleEventDetail()
                obj._deserialize(item)
                self._EventTableListStruct.append(obj)
        self._BaseLineUser = params.get("BaseLineUser")
        self._BaseLineInSwitch = params.get("BaseLineInSwitch")
        self._BaseLineOutSwitch = params.get("BaseLineOutSwitch")
        self._VpcFwCount = params.get("VpcFwCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnHandleEventDetail(AbstractModel):
    """Unhandled event statistics

    """

    def __init__(self):
        r"""
        :param _EventName: Security event name
        :type EventName: str
        :param _Total: Number of unhandled events
        :type Total: int
        """
        self._EventName = None
        self._Total = None

    @property
    def EventName(self):
        """Security event name
        :rtype: str
        """
        return self._EventName

    @EventName.setter
    def EventName(self, EventName):
        self._EventName = EventName

    @property
    def Total(self):
        """Number of unhandled events
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._EventName = params.get("EventName")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcDnsInfo(AbstractModel):
    """VPC DNS status of NAT firewall

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _VpcName: VPC name
        :type VpcName: str
        :param _FwMode: NAT firewall mode. 0: Create new; 1: Use existing
        :type FwMode: int
        :param _VpcIpv4Cidr: VPC IPv4 CIDR block (Classless Inter-Domain Routing)
        :type VpcIpv4Cidr: str
        :param _DNSEip: Public EIP, which is the firewall DNS resolution address
        :type DNSEip: str
        :param _NatInsId: NAT gateway ID
Note: This field may return `null`, indicating that no valid value was found.
        :type NatInsId: str
        :param _NatInsName: NAT gateway name
Note: This field may return `null`, indicating that no valid value was found.
        :type NatInsName: str
        :param _SwitchStatus: 0: off; 1: on
        :type SwitchStatus: int
        """
        self._VpcId = None
        self._VpcName = None
        self._FwMode = None
        self._VpcIpv4Cidr = None
        self._DNSEip = None
        self._NatInsId = None
        self._NatInsName = None
        self._SwitchStatus = None

    @property
    def VpcId(self):
        """VPC ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        """VPC name
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def FwMode(self):
        """NAT firewall mode. 0: Create new; 1: Use existing
        :rtype: int
        """
        return self._FwMode

    @FwMode.setter
    def FwMode(self, FwMode):
        self._FwMode = FwMode

    @property
    def VpcIpv4Cidr(self):
        """VPC IPv4 CIDR block (Classless Inter-Domain Routing)
        :rtype: str
        """
        return self._VpcIpv4Cidr

    @VpcIpv4Cidr.setter
    def VpcIpv4Cidr(self, VpcIpv4Cidr):
        self._VpcIpv4Cidr = VpcIpv4Cidr

    @property
    def DNSEip(self):
        """Public EIP, which is the firewall DNS resolution address
        :rtype: str
        """
        return self._DNSEip

    @DNSEip.setter
    def DNSEip(self, DNSEip):
        self._DNSEip = DNSEip

    @property
    def NatInsId(self):
        """NAT gateway ID
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._NatInsId

    @NatInsId.setter
    def NatInsId(self, NatInsId):
        self._NatInsId = NatInsId

    @property
    def NatInsName(self):
        """NAT gateway name
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._NatInsName

    @NatInsName.setter
    def NatInsName(self, NatInsName):
        self._NatInsName = NatInsName

    @property
    def SwitchStatus(self):
        """0: off; 1: on
        :rtype: int
        """
        return self._SwitchStatus

    @SwitchStatus.setter
    def SwitchStatus(self, SwitchStatus):
        self._SwitchStatus = SwitchStatus


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._FwMode = params.get("FwMode")
        self._VpcIpv4Cidr = params.get("VpcIpv4Cidr")
        self._DNSEip = params.get("DNSEip")
        self._NatInsId = params.get("NatInsId")
        self._NatInsName = params.get("NatInsName")
        self._SwitchStatus = params.get("SwitchStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcRuleItem(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _SourceContent: 
        :type SourceContent: str
        :param _SourceType: 
        :type SourceType: str
        :param _DestContent: 
        :type DestContent: str
        :param _DestType: 
        :type DestType: str
        :param _Protocol: 
        :type Protocol: str
        :param _RuleAction: 
        :type RuleAction: str
        :param _Port: 
        :type Port: str
        :param _Description: 
        :type Description: str
        :param _OrderIndex: 
        :type OrderIndex: int
        :param _Enable: 
        :type Enable: str
        :param _EdgeId: 
        :type EdgeId: str
        :param _Uuid: 
        :type Uuid: int
        :param _DetectedTimes: 
        :type DetectedTimes: int
        :param _EdgeName: 
        :type EdgeName: str
        :param _InternalUuid: 
        :type InternalUuid: int
        :param _Deleted: 
        :type Deleted: int
        :param _FwGroupId: 
        :type FwGroupId: str
        :param _FwGroupName: 
        :type FwGroupName: str
        :param _BetaList: 
        :type BetaList: list of BetaInfoByACL
        :param _ParamTemplateId: 
        :type ParamTemplateId: str
        :param _ParamTemplateName: 
        :type ParamTemplateName: str
        :param _TargetName: 
        :type TargetName: str
        :param _SourceName: 
        :type SourceName: str
        :param _IpVersion: 
        :type IpVersion: int
        :param _Invalid: 
        :type Invalid: int
        """
        self._SourceContent = None
        self._SourceType = None
        self._DestContent = None
        self._DestType = None
        self._Protocol = None
        self._RuleAction = None
        self._Port = None
        self._Description = None
        self._OrderIndex = None
        self._Enable = None
        self._EdgeId = None
        self._Uuid = None
        self._DetectedTimes = None
        self._EdgeName = None
        self._InternalUuid = None
        self._Deleted = None
        self._FwGroupId = None
        self._FwGroupName = None
        self._BetaList = None
        self._ParamTemplateId = None
        self._ParamTemplateName = None
        self._TargetName = None
        self._SourceName = None
        self._IpVersion = None
        self._Invalid = None

    @property
    def SourceContent(self):
        """
        :rtype: str
        """
        return self._SourceContent

    @SourceContent.setter
    def SourceContent(self, SourceContent):
        self._SourceContent = SourceContent

    @property
    def SourceType(self):
        """
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def DestContent(self):
        """
        :rtype: str
        """
        return self._DestContent

    @DestContent.setter
    def DestContent(self, DestContent):
        self._DestContent = DestContent

    @property
    def DestType(self):
        """
        :rtype: str
        """
        return self._DestType

    @DestType.setter
    def DestType(self, DestType):
        self._DestType = DestType

    @property
    def Protocol(self):
        """
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def RuleAction(self):
        """
        :rtype: str
        """
        return self._RuleAction

    @RuleAction.setter
    def RuleAction(self, RuleAction):
        self._RuleAction = RuleAction

    @property
    def Port(self):
        """
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Description(self):
        """
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def OrderIndex(self):
        """
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def Enable(self):
        """
        :rtype: str
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def EdgeId(self):
        """
        :rtype: str
        """
        return self._EdgeId

    @EdgeId.setter
    def EdgeId(self, EdgeId):
        self._EdgeId = EdgeId

    @property
    def Uuid(self):
        """
        :rtype: int
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def DetectedTimes(self):
        """
        :rtype: int
        """
        return self._DetectedTimes

    @DetectedTimes.setter
    def DetectedTimes(self, DetectedTimes):
        self._DetectedTimes = DetectedTimes

    @property
    def EdgeName(self):
        """
        :rtype: str
        """
        return self._EdgeName

    @EdgeName.setter
    def EdgeName(self, EdgeName):
        self._EdgeName = EdgeName

    @property
    def InternalUuid(self):
        """
        :rtype: int
        """
        return self._InternalUuid

    @InternalUuid.setter
    def InternalUuid(self, InternalUuid):
        self._InternalUuid = InternalUuid

    @property
    def Deleted(self):
        """
        :rtype: int
        """
        return self._Deleted

    @Deleted.setter
    def Deleted(self, Deleted):
        self._Deleted = Deleted

    @property
    def FwGroupId(self):
        """
        :rtype: str
        """
        return self._FwGroupId

    @FwGroupId.setter
    def FwGroupId(self, FwGroupId):
        self._FwGroupId = FwGroupId

    @property
    def FwGroupName(self):
        """
        :rtype: str
        """
        return self._FwGroupName

    @FwGroupName.setter
    def FwGroupName(self, FwGroupName):
        self._FwGroupName = FwGroupName

    @property
    def BetaList(self):
        """
        :rtype: list of BetaInfoByACL
        """
        return self._BetaList

    @BetaList.setter
    def BetaList(self, BetaList):
        self._BetaList = BetaList

    @property
    def ParamTemplateId(self):
        """
        :rtype: str
        """
        return self._ParamTemplateId

    @ParamTemplateId.setter
    def ParamTemplateId(self, ParamTemplateId):
        self._ParamTemplateId = ParamTemplateId

    @property
    def ParamTemplateName(self):
        """
        :rtype: str
        """
        return self._ParamTemplateName

    @ParamTemplateName.setter
    def ParamTemplateName(self, ParamTemplateName):
        self._ParamTemplateName = ParamTemplateName

    @property
    def TargetName(self):
        """
        :rtype: str
        """
        return self._TargetName

    @TargetName.setter
    def TargetName(self, TargetName):
        self._TargetName = TargetName

    @property
    def SourceName(self):
        """
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def IpVersion(self):
        """
        :rtype: int
        """
        return self._IpVersion

    @IpVersion.setter
    def IpVersion(self, IpVersion):
        self._IpVersion = IpVersion

    @property
    def Invalid(self):
        """
        :rtype: int
        """
        return self._Invalid

    @Invalid.setter
    def Invalid(self, Invalid):
        self._Invalid = Invalid


    def _deserialize(self, params):
        self._SourceContent = params.get("SourceContent")
        self._SourceType = params.get("SourceType")
        self._DestContent = params.get("DestContent")
        self._DestType = params.get("DestType")
        self._Protocol = params.get("Protocol")
        self._RuleAction = params.get("RuleAction")
        self._Port = params.get("Port")
        self._Description = params.get("Description")
        self._OrderIndex = params.get("OrderIndex")
        self._Enable = params.get("Enable")
        self._EdgeId = params.get("EdgeId")
        self._Uuid = params.get("Uuid")
        self._DetectedTimes = params.get("DetectedTimes")
        self._EdgeName = params.get("EdgeName")
        self._InternalUuid = params.get("InternalUuid")
        self._Deleted = params.get("Deleted")
        self._FwGroupId = params.get("FwGroupId")
        self._FwGroupName = params.get("FwGroupName")
        if params.get("BetaList") is not None:
            self._BetaList = []
            for item in params.get("BetaList"):
                obj = BetaInfoByACL()
                obj._deserialize(item)
                self._BetaList.append(obj)
        self._ParamTemplateId = params.get("ParamTemplateId")
        self._ParamTemplateName = params.get("ParamTemplateName")
        self._TargetName = params.get("TargetName")
        self._SourceName = params.get("SourceName")
        self._IpVersion = params.get("IpVersion")
        self._Invalid = params.get("Invalid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        