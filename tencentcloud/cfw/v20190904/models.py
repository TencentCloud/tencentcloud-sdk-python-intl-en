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
        :param Id: Rule ID
        :type Id: int
        :param SourceIp: Access source
Note: This field may return `null`, indicating that no valid value was found.
        :type SourceIp: str
        :param TargetIp: Access destination
Note: This field may return `null`, indicating that no valid value was found.
        :type TargetIp: str
        :param Protocol: Protocol
Note: This field may return `null`, indicating that no valid value was found.
        :type Protocol: str
        :param Port: Port
Note: This field may return `null`, indicating that no valid value was found.
        :type Port: str
        :param Strategy: Policy
Note: This field may return `null`, indicating that no valid value was found.
        :type Strategy: int
        :param Detail: Description
Note: This field may return `null`, indicating that no valid value was found.
        :type Detail: str
        :param Count: Hit count
        :type Count: int
        :param OrderIndex: Priority
        :type OrderIndex: int
        :param LogId: Alert rule ID
Note: This field may return `null`, indicating that no valid value was found.
        :type LogId: str
        """
        self.Id = None
        self.SourceIp = None
        self.TargetIp = None
        self.Protocol = None
        self.Port = None
        self.Strategy = None
        self.Detail = None
        self.Count = None
        self.OrderIndex = None
        self.LogId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.SourceIp = params.get("SourceIp")
        self.TargetIp = params.get("TargetIp")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        self.Strategy = params.get("Strategy")
        self.Detail = params.get("Detail")
        self.Count = params.get("Count")
        self.OrderIndex = params.get("OrderIndex")
        self.LogId = params.get("LogId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddAcRuleRequest(AbstractModel):
    """AddAcRule request structure.

    """

    def __init__(self):
        r"""
        :param OrderIndex: -1: lowest priority; 1: highest priority
        :type OrderIndex: str
        :param RuleAction: The action that Cloud Firewall performs on the traffic. Valid values:
accept: allow
drop: deny
log: observe
        :type RuleAction: str
        :param Direction: The traffic direction for access control rules. Valid values:
in: incoming traffic access control
out: outgoing traffic access control
        :type Direction: str
        :param Description: The description of access control rules.
        :type Description: str
        :param SourceType: The type of source address in access control rules. Valid values:
net: source IP or range (IP or CIDR)
location: source region
template: CFW address template
instance: instance ID
vendor: Cloud vendor
        :type SourceType: str
        :param SourceContent: The source address in the access control policy. 
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
        :param DestType: The type of destination address in access control rules. Valid values:
net: destination IP or range (IP or CIDR)
location: source region
template: CFW address template
instance: instance ID
vendor: Cloud vendor
domain: Domain name or IP.
        :type DestType: str
        :param DestContent: The destination address in the access control policy. 
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
        :param Port: The port to apply access control rules. Valid values:
-1/-1: all ports
80,443: 80 or 443
        :type Port: str
        :param Protocol: The protocol type of traffic in access control rules. Valid value: TCP. Only TCP is supported for edge firewall rules. If this parameter is not specified, it defaults to TCP.
        :type Protocol: str
        :param ApplicationName: The Layer 7 protocol. Valid values:
HTTP/HTTPS
TLS/SSL
        :type ApplicationName: str
        :param Enable: Indicates whether to enable the rules. Default: enable. Valid values:
true: enable; false: disable
        :type Enable: str
        """
        self.OrderIndex = None
        self.RuleAction = None
        self.Direction = None
        self.Description = None
        self.SourceType = None
        self.SourceContent = None
        self.DestType = None
        self.DestContent = None
        self.Port = None
        self.Protocol = None
        self.ApplicationName = None
        self.Enable = None


    def _deserialize(self, params):
        self.OrderIndex = params.get("OrderIndex")
        self.RuleAction = params.get("RuleAction")
        self.Direction = params.get("Direction")
        self.Description = params.get("Description")
        self.SourceType = params.get("SourceType")
        self.SourceContent = params.get("SourceContent")
        self.DestType = params.get("DestType")
        self.DestContent = params.get("DestContent")
        self.Port = params.get("Port")
        self.Protocol = params.get("Protocol")
        self.ApplicationName = params.get("ApplicationName")
        self.Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddAcRuleResponse(AbstractModel):
    """AddAcRule response structure.

    """

    def __init__(self):
        r"""
        :param RuleUuid: UUID of the new rule
        :type RuleUuid: int
        :param ReturnCode: 0: operation successful; -1: operation failed
        :type ReturnCode: int
        :param ReturnMsg: success: operation successful; failed: operation failed
        :type ReturnMsg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RuleUuid = None
        self.ReturnCode = None
        self.ReturnMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleUuid = params.get("RuleUuid")
        self.ReturnCode = params.get("ReturnCode")
        self.ReturnMsg = params.get("ReturnMsg")
        self.RequestId = params.get("RequestId")


class AddEnterpriseSecurityGroupRulesRequest(AbstractModel):
    """AddEnterpriseSecurityGroupRules request structure.

    """

    def __init__(self):
        r"""
        :param Data: Creates rule data
        :type Data: list of SecurityGroupRule
        :param Type: Adding type. 0: add to the end; 1: add to the front; 2: insert. Default: 0
        :type Type: int
        :param ClientToken: An identifier to ensure the idempotency of the request. The value of the ClientToken parameter is a unique string that is generated by your client and can contain up to 64 ASCII characters in length.
        :type ClientToken: str
        :param IsDelay: Indicates whether to delay publishing. 1: delay; other values: do not delay
        :type IsDelay: int
        """
        self.Data = None
        self.Type = None
        self.ClientToken = None
        self.IsDelay = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecurityGroupRule()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Type = params.get("Type")
        self.ClientToken = params.get("ClientToken")
        self.IsDelay = params.get("IsDelay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddEnterpriseSecurityGroupRulesResponse(AbstractModel):
    """AddEnterpriseSecurityGroupRules response structure.

    """

    def __init__(self):
        r"""
        :param Status: Status value. 0: added successfully; non-0: failed to add
        :type Status: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class AssetZone(AbstractModel):
    """AssetZone

    """

    def __init__(self):
        r"""
        :param Zone: Region
        :type Zone: str
        :param ZoneEng: Region
        :type ZoneEng: str
        """
        self.Zone = None
        self.ZoneEng = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneEng = params.get("ZoneEng")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociatedInstanceInfo(AbstractModel):
    """Instance associated with an enterprise security group

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
Note: This field may return `null`, indicating that no valid value was found.
        :type InstanceId: str
        :param InstanceName: Instance name
Note: This field may return `null`, indicating that no valid value was found.
        :type InstanceName: str
        :param Type: Instance type. 3: CVM instance; 4: CLB instance; 5: ENI instance; 6: Cloud database
Note: This field may return `null`, indicating that no valid value was found.
        :type Type: int
        :param VpcId: VPC ID
Note: This field may return `null`, indicating that no valid value was found.
        :type VpcId: str
        :param VpcName: VPC name
Note: This field may return `null`, indicating that no valid value was found.
        :type VpcName: str
        :param PublicIp: Public IP
Note: This field may return `null`, indicating that no valid value was found.
        :type PublicIp: str
        :param Ip: Private IP
Note: This field may return `null`, indicating that no valid value was found.
        :type Ip: str
        :param SecurityGroupCount: The number of associated security groups
Note: This field may return `null`, indicating that no valid value was found.
        :type SecurityGroupCount: int
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Type = None
        self.VpcId = None
        self.VpcName = None
        self.PublicIp = None
        self.Ip = None
        self.SecurityGroupCount = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Type = params.get("Type")
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.PublicIp = params.get("PublicIp")
        self.Ip = params.get("Ip")
        self.SecurityGroupCount = params.get("SecurityGroupCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CfwNatDnatRule(AbstractModel):
    """NAT firewall DNAT rules

    """

    def __init__(self):
        r"""
        :param IpProtocol: Network protocol. Valid values: TCP or UDP.
        :type IpProtocol: str
        :param PublicIpAddress: Elastic IP.
        :type PublicIpAddress: str
        :param PublicPort: Public port.
        :type PublicPort: int
        :param PrivateIpAddress: Private address.
        :type PrivateIpAddress: str
        :param PrivatePort: Private port.
        :type PrivatePort: int
        :param Description: The description of NAT firewall forwarding rules.
        :type Description: str
        """
        self.IpProtocol = None
        self.PublicIpAddress = None
        self.PublicPort = None
        self.PrivateIpAddress = None
        self.PrivatePort = None
        self.Description = None


    def _deserialize(self, params):
        self.IpProtocol = params.get("IpProtocol")
        self.PublicIpAddress = params.get("PublicIpAddress")
        self.PublicPort = params.get("PublicPort")
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        self.PrivatePort = params.get("PrivatePort")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAcRulesRequest(AbstractModel):
    """CreateAcRules request structure.

    """

    def __init__(self):
        r"""
        :param Data: Creates rule data
        :type Data: list of RuleInfoData
        :param Type: 0: add (default); 1: insert
        :type Type: int
        :param EdgeId: Edge ID
        :type EdgeId: str
        :param Enable: Access control rule status
        :type Enable: int
        :param Overwrite: 0: add; 1: overwrite
        :type Overwrite: int
        :param InstanceId: NAT instance ID, required when the parameter Area exists
        :type InstanceId: str
        :param From: portScan: from port scanning; patchImport: from batch import
        :type From: str
        :param Area: NAT region
        :type Area: str
        """
        self.Data = None
        self.Type = None
        self.EdgeId = None
        self.Enable = None
        self.Overwrite = None
        self.InstanceId = None
        self.From = None
        self.Area = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = RuleInfoData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Type = params.get("Type")
        self.EdgeId = params.get("EdgeId")
        self.Enable = params.get("Enable")
        self.Overwrite = params.get("Overwrite")
        self.InstanceId = params.get("InstanceId")
        self.From = params.get("From")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAcRulesResponse(AbstractModel):
    """CreateAcRules response structure.

    """

    def __init__(self):
        r"""
        :param Status: Status value. 0: operation successful
        :type Status: int
        :param Info: Returns redundant information
Note: This field may return `null`, indicating that no valid value was found.
        :type Info: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Info = params.get("Info")
        self.RequestId = params.get("RequestId")


class CreateNatFwInstanceRequest(AbstractModel):
    """CreateNatFwInstance request structure.

    """

    def __init__(self):
        r"""
        :param Name: Firewall instance name
        :type Name: str
        :param Width: Bandwidth
        :type Width: int
        :param Mode: Mode. 1: use existing; 0: create new
        :type Mode: int
        :param NewModeItems: Parameter passed for the Create New mode. Either NewModeItems or NatgwList is required.
        :type NewModeItems: :class:`tencentcloud.cfw.v20190904.models.NewModeItems`
        :param NatGwList: NAT gateway list for the Using Existing mode. Either NewModeItems or NatgwList is required.
        :type NatGwList: list of str
        :param Zone: Primary zone. The default zone is selected if it is empty.
        :type Zone: str
        :param ZoneBak: Secondary zone. The default zone is selected if it is empty.
        :type ZoneBak: str
        :param CrossAZone: Remote disaster recovery. 1: enable; 0: disable; empty: disable by default
        :type CrossAZone: int
        """
        self.Name = None
        self.Width = None
        self.Mode = None
        self.NewModeItems = None
        self.NatGwList = None
        self.Zone = None
        self.ZoneBak = None
        self.CrossAZone = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Mode = params.get("Mode")
        if params.get("NewModeItems") is not None:
            self.NewModeItems = NewModeItems()
            self.NewModeItems._deserialize(params.get("NewModeItems"))
        self.NatGwList = params.get("NatGwList")
        self.Zone = params.get("Zone")
        self.ZoneBak = params.get("ZoneBak")
        self.CrossAZone = params.get("CrossAZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNatFwInstanceResponse(AbstractModel):
    """CreateNatFwInstance response structure.

    """

    def __init__(self):
        r"""
        :param CfwInsId: Firewall instance ID
        :type CfwInsId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CfwInsId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CfwInsId = params.get("CfwInsId")
        self.RequestId = params.get("RequestId")


class CreateNatFwInstanceWithDomainRequest(AbstractModel):
    """CreateNatFwInstanceWithDomain request structure.

    """

    def __init__(self):
        r"""
        :param Name: Firewall instance name
        :type Name: str
        :param Width: Bandwidth
        :type Width: int
        :param Mode: Mode. 1: use existing; 0: create new
        :type Mode: int
        :param NewModeItems: Parameter passed for the Create New mode. Either NewModeItems or NatgwList is required.
        :type NewModeItems: :class:`tencentcloud.cfw.v20190904.models.NewModeItems`
        :param NatGwList: NAT gateway list for the Using Existing mode. Either NewModeItems or NatgwList is required.
        :type NatGwList: list of str
        :param Zone: Primary zone. The default zone is selected if it is empty.
        :type Zone: str
        :param ZoneBak: Secondary zone. The default zone is selected if it is empty.
        :type ZoneBak: str
        :param CrossAZone: Remote disaster recovery. 1: enable; 0: disable; empty: disable by default
        :type CrossAZone: int
        :param IsCreateDomain: 0: not create; 1: create
        :type IsCreateDomain: int
        :param Domain: Required for creating a domain name
        :type Domain: str
        """
        self.Name = None
        self.Width = None
        self.Mode = None
        self.NewModeItems = None
        self.NatGwList = None
        self.Zone = None
        self.ZoneBak = None
        self.CrossAZone = None
        self.IsCreateDomain = None
        self.Domain = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Mode = params.get("Mode")
        if params.get("NewModeItems") is not None:
            self.NewModeItems = NewModeItems()
            self.NewModeItems._deserialize(params.get("NewModeItems"))
        self.NatGwList = params.get("NatGwList")
        self.Zone = params.get("Zone")
        self.ZoneBak = params.get("ZoneBak")
        self.CrossAZone = params.get("CrossAZone")
        self.IsCreateDomain = params.get("IsCreateDomain")
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNatFwInstanceWithDomainResponse(AbstractModel):
    """CreateNatFwInstanceWithDomain response structure.

    """

    def __init__(self):
        r"""
        :param CfwInsId: NAT instance info
Note: This field may return `null`, indicating that no valid value was found.
        :type CfwInsId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CfwInsId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CfwInsId = params.get("CfwInsId")
        self.RequestId = params.get("RequestId")


class CreateSecurityGroupRulesRequest(AbstractModel):
    """CreateSecurityGroupRules request structure.

    """

    def __init__(self):
        r"""
        :param Data: Added enterprise security group rule data
        :type Data: list of SecurityGroupListData
        :param Direction: Direction. 0: outbound; 1: inbound. 1 by default
        :type Direction: int
        :param Type: 0: at the end; 1: at the top; 2: in the middle. 0 by default
        :type Type: int
        :param Enable: Indicates whether to enable rules after addition. 0: disable; 1: enable. 1 by default
        :type Enable: int
        """
        self.Data = None
        self.Direction = None
        self.Type = None
        self.Enable = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecurityGroupListData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Direction = params.get("Direction")
        self.Type = params.get("Type")
        self.Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityGroupRulesResponse(AbstractModel):
    """CreateSecurityGroupRules response structure.

    """

    def __init__(self):
        r"""
        :param Status: Status value. 0: added successfully; non-0: failed to add
        :type Status: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DeleteAcRuleRequest(AbstractModel):
    """DeleteAcRule request structure.

    """

    def __init__(self):
        r"""
        :param Id: The ID of the rule to delete. It can be queried via the DescribeAcLists API.
        :type Id: int
        :param Direction: Direction. 0: outbound; 1: inbound
        :type Direction: int
        :param EdgeId: Edge ID between two VPCs
        :type EdgeId: str
        :param Area: NAT region, e.g. ap-shanghai/ap-guangzhou/ap-chongqing
        :type Area: str
        """
        self.Id = None
        self.Direction = None
        self.EdgeId = None
        self.Area = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Direction = params.get("Direction")
        self.EdgeId = params.get("EdgeId")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAcRuleResponse(AbstractModel):
    """DeleteAcRule response structure.

    """

    def __init__(self):
        r"""
        :param Status: Status value. 0: deleted successfully; !0: deletion failed
        :type Status: int
        :param Info: Returns redundant information
Note: This field may return `null`, indicating that no valid value was found.
        :type Info: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Info = params.get("Info")
        self.RequestId = params.get("RequestId")


class DeleteAllAccessControlRuleRequest(AbstractModel):
    """DeleteAllAccessControlRule request structure.

    """

    def __init__(self):
        r"""
        :param Direction: Direction. 0: outbound; 1: inbound. 0 by default
        :type Direction: int
        :param EdgeId: Deletes all the access control rules for inter-VPC firewall toggles associated with the EdgeId. It is empty by default. Enter either EdgeId or Area.
        :type EdgeId: str
        :param Area: Deletes all the access control rules for NAT firewalls of this region. It is empty by default. Enter either EdgeId or Area.
        :type Area: str
        """
        self.Direction = None
        self.EdgeId = None
        self.Area = None


    def _deserialize(self, params):
        self.Direction = params.get("Direction")
        self.EdgeId = params.get("EdgeId")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAllAccessControlRuleResponse(AbstractModel):
    """DeleteAllAccessControlRule response structure.

    """

    def __init__(self):
        r"""
        :param Status: Status value. 0: modified successfully; !0: modification failed
        :type Status: int
        :param Info: Number of access control rules deleted.
Note: This field may return `null`, indicating that no valid value was found.
        :type Info: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Info = params.get("Info")
        self.RequestId = params.get("RequestId")


class DeleteResourceGroupRequest(AbstractModel):
    """DeleteResourceGroup request structure.

    """

    def __init__(self):
        r"""
        :param GroupId: Group ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteResourceGroupResponse(AbstractModel):
    """DeleteResourceGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSecurityGroupRuleRequest(AbstractModel):
    """DeleteSecurityGroupRule request structure.

    """

    def __init__(self):
        r"""
        :param Id: ID of the rule to delete
        :type Id: int
        :param Area: Tencent Cloud region (abbreviation)
        :type Area: str
        :param Direction: Direction. 0: outbound; 1: inbound
        :type Direction: int
        :param IsDelReverse: Indicates whether to delete the reverse rule. 0: no; 1: yes
        :type IsDelReverse: int
        """
        self.Id = None
        self.Area = None
        self.Direction = None
        self.IsDelReverse = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Area = params.get("Area")
        self.Direction = params.get("Direction")
        self.IsDelReverse = params.get("IsDelReverse")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityGroupRuleResponse(AbstractModel):
    """DeleteSecurityGroupRule response structure.

    """

    def __init__(self):
        r"""
        :param Status: Status value. 0: operation successful; non-0: operation failed
        :type Status: int
        :param Info: Returns redundant information
Note: This field may return `null`, indicating that no valid value was found.
        :type Info: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Info = params.get("Info")
        self.RequestId = params.get("RequestId")


class DeleteVpcInstanceRequest(AbstractModel):
    """DeleteVpcInstance request structure.

    """


class DeleteVpcInstanceResponse(AbstractModel):
    """DeleteVpcInstance response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAcListsRequest(AbstractModel):
    """DescribeAcLists request structure.

    """

    def __init__(self):
        r"""
        :param Protocol: Protocol
        :type Protocol: str
        :param Strategy: Policy
        :type Strategy: str
        :param SearchValue: Search value
        :type SearchValue: str
        :param Limit: Number of entries per page
        :type Limit: int
        :param Offset: Offset
        :type Offset: int
        :param Direction: Indicates whether it is outbound or inbound. 1: inbound; 0: outbound
        :type Direction: int
        :param EdgeId: EdgeId value
        :type EdgeId: str
        :param Status: Indicates whether the rule is enabled. '0': disabled; '1': enabled. '0' by default
        :type Status: str
        :param Area: Region
        :type Area: str
        :param InstanceId: Instance ID
        :type InstanceId: str
        """
        self.Protocol = None
        self.Strategy = None
        self.SearchValue = None
        self.Limit = None
        self.Offset = None
        self.Direction = None
        self.EdgeId = None
        self.Status = None
        self.Area = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Strategy = params.get("Strategy")
        self.SearchValue = params.get("SearchValue")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Direction = params.get("Direction")
        self.EdgeId = params.get("EdgeId")
        self.Status = params.get("Status")
        self.Area = params.get("Area")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAcListsResponse(AbstractModel):
    """DescribeAcLists response structure.

    """

    def __init__(self):
        r"""
        :param Total: Total entries
        :type Total: int
        :param Data: Access control list data
        :type Data: list of AcListsData
        :param AllTotal: Total entries excluding the filtered ones
        :type AllTotal: int
        :param Enable: All access control rules enabled/disabled
Note: This field may return `null`, indicating that no valid value was found.
        :type Enable: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.Data = None
        self.AllTotal = None
        self.Enable = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = AcListsData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.AllTotal = params.get("AllTotal")
        self.Enable = params.get("Enable")
        self.RequestId = params.get("RequestId")


class DescribeAssociatedInstanceListRequest(AbstractModel):
    """DescribeAssociatedInstanceList request structure.

    """

    def __init__(self):
        r"""
        :param Offset: List offset
        :type Offset: int
        :param Limit: Number of records per page
        :type Limit: int
        :param Area: Region code (e.g. ap-guangzhou). All Tencent Cloud regions are supported.
        :type Area: str
        :param SearchValue: Additional search criteria (JSON string)
        :type SearchValue: str
        :param By: Sorting field
        :type By: str
        :param Order: Sort order. asc: ascending; desc: descending
        :type Order: str
        :param SecurityGroupId: Security group ID
        :type SecurityGroupId: str
        :param Type: Instance type. '3': CVM instance; '4': CLB instance; '5': ENI instance; '6': Cloud database
        :type Type: str
        """
        self.Offset = None
        self.Limit = None
        self.Area = None
        self.SearchValue = None
        self.By = None
        self.Order = None
        self.SecurityGroupId = None
        self.Type = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Area = params.get("Area")
        self.SearchValue = params.get("SearchValue")
        self.By = params.get("By")
        self.Order = params.get("Order")
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssociatedInstanceListResponse(AbstractModel):
    """DescribeAssociatedInstanceList response structure.

    """

    def __init__(self):
        r"""
        :param Total: Number of instances
Note: This field may return `null`, indicating that no valid value was found.
        :type Total: int
        :param Data: Instance list
Note: This field may return `null`, indicating that no valid value was found.
        :type Data: list of AssociatedInstanceInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = AssociatedInstanceInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBlockByIpTimesListRequest(AbstractModel):
    """DescribeBlockByIpTimesList request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param Ip: IP search criteria
        :type Ip: str
        :param Zone: Region
        :type Zone: str
        :param Direction: Direction
        :type Direction: str
        :param Source: Source
        :type Source: str
        :param EdgeId: Inter-VPC firewall toggle edge ID
        :type EdgeId: str
        :param LogSource: Log source. move: inter-VPC firewall
        :type LogSource: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Ip = None
        self.Zone = None
        self.Direction = None
        self.Source = None
        self.EdgeId = None
        self.LogSource = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Ip = params.get("Ip")
        self.Zone = params.get("Zone")
        self.Direction = params.get("Direction")
        self.Source = params.get("Source")
        self.EdgeId = params.get("EdgeId")
        self.LogSource = params.get("LogSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBlockByIpTimesListResponse(AbstractModel):
    """DescribeBlockByIpTimesList response structure.

    """

    def __init__(self):
        r"""
        :param Data: Response data
        :type Data: list of IpStatic
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = IpStatic()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBlockStaticListRequest(AbstractModel):
    """DescribeBlockStaticList request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param QueryType: List type. Valid values: port, address, or IP
        :type QueryType: str
        :param Top: Number of top results returned
        :type Top: int
        :param SearchValue: Search criteria
        :type SearchValue: str
        """
        self.StartTime = None
        self.EndTime = None
        self.QueryType = None
        self.Top = None
        self.SearchValue = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.QueryType = params.get("QueryType")
        self.Top = params.get("Top")
        self.SearchValue = params.get("SearchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBlockStaticListResponse(AbstractModel):
    """DescribeBlockStaticList response structure.

    """

    def __init__(self):
        r"""
        :param Data: None
        :type Data: list of StaticInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = StaticInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDefenseSwitchRequest(AbstractModel):
    """DescribeDefenseSwitch request structure.

    """


class DescribeDefenseSwitchResponse(AbstractModel):
    """DescribeDefenseSwitch response structure.

    """

    def __init__(self):
        r"""
        :param BasicRuleSwitch: Whether to enable the Basic Protection feature
        :type BasicRuleSwitch: int
        :param BaselineAllSwitch: Whether to enable the Security Baseline feature
        :type BaselineAllSwitch: int
        :param TiSwitch: Whether to enable the Treat Intelligence feature
        :type TiSwitch: int
        :param VirtualPatchSwitch: Whether to enable the Virtual Patch feature
        :type VirtualPatchSwitch: int
        :param HistoryOpen: Whether it has been enabled before
        :type HistoryOpen: int
        :param ReturnCode: Status code. `0`: Succeeded. Others: Failed
        :type ReturnCode: int
        :param ReturnMsg: Status message. `success` and `fail.
        :type ReturnMsg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.BasicRuleSwitch = None
        self.BaselineAllSwitch = None
        self.TiSwitch = None
        self.VirtualPatchSwitch = None
        self.HistoryOpen = None
        self.ReturnCode = None
        self.ReturnMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BasicRuleSwitch = params.get("BasicRuleSwitch")
        self.BaselineAllSwitch = params.get("BaselineAllSwitch")
        self.TiSwitch = params.get("TiSwitch")
        self.VirtualPatchSwitch = params.get("VirtualPatchSwitch")
        self.HistoryOpen = params.get("HistoryOpen")
        self.ReturnCode = params.get("ReturnCode")
        self.ReturnMsg = params.get("ReturnMsg")
        self.RequestId = params.get("RequestId")


class DescribeEnterpriseSecurityGroupRuleRequest(AbstractModel):
    """DescribeEnterpriseSecurityGroupRule request structure.

    """

    def __init__(self):
        r"""
        :param PageNo: Page number of the current page displayed for query by page number.

1 by default.
        :type PageNo: str
        :param PageSize: Maximum number of entries per page displayed for query by page number.

Maximum value: 50.
        :type PageSize: str
        :param SourceContent: Source example:
net: IP/CIDR (192.168.0.2)
template: parameter template (ipm-dyodhpby)
instance: asset instance (ins-123456)
resourcegroup: asset group (/all groups/group 1/subgroup 1)
tag: resource tag ({"Key":"tag key","Value":"tag value"})
region: region (ap-gaungzhou)
Wildcards are supported.
        :type SourceContent: str
        :param DestContent: Destination example:
net: IP/CIDR (192.168.0.2)
template: parameter template (ipm-dyodhpby)
instance: asset instance (ins-123456)
resourcegroup: asset group (/all groups/group 1/subgroup 1)
tag: resource tag ({"Key":"tag key","Value":"tag value"})
region: region (ap-gaungzhou)
Wildcards are supported.
        :type DestContent: str
        :param Description: Rule description. Wildcards are supported.
        :type Description: str
        :param RuleAction: The action that Cloud Firewall performs on the traffic. Valid values:
accept: allow
drop: deny
        :type RuleAction: str
        :param Enable: Indicates whether to enable the rules. Default: enable. Valid values:
true: enable; false: disable
        :type Enable: str
        :param Port: The port to apply access control rules. Valid values:
-1/-1: all ports
80: port 80
        :type Port: str
        :param Protocol: Protocol. TCP/UDP/ICMP/ANY
        :type Protocol: str
        :param ServiceTemplateId: Parameter template ID of port and protocol type; mutually exclusive with Protocol and Port
        :type ServiceTemplateId: str
        """
        self.PageNo = None
        self.PageSize = None
        self.SourceContent = None
        self.DestContent = None
        self.Description = None
        self.RuleAction = None
        self.Enable = None
        self.Port = None
        self.Protocol = None
        self.ServiceTemplateId = None


    def _deserialize(self, params):
        self.PageNo = params.get("PageNo")
        self.PageSize = params.get("PageSize")
        self.SourceContent = params.get("SourceContent")
        self.DestContent = params.get("DestContent")
        self.Description = params.get("Description")
        self.RuleAction = params.get("RuleAction")
        self.Enable = params.get("Enable")
        self.Port = params.get("Port")
        self.Protocol = params.get("Protocol")
        self.ServiceTemplateId = params.get("ServiceTemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnterpriseSecurityGroupRuleResponse(AbstractModel):
    """DescribeEnterpriseSecurityGroupRule response structure.

    """

    def __init__(self):
        r"""
        :param PageNo: Page number of the current page displayed for query by page number.
        :type PageNo: str
        :param PageSize: Maximum number of entries per page displayed for query by page number.
        :type PageSize: str
        :param Rules: Access control rule list
        :type Rules: list of SecurityGroupRule
        :param TotalCount: Total number of access control rules
        :type TotalCount: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PageNo = None
        self.PageSize = None
        self.Rules = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PageNo = params.get("PageNo")
        self.PageSize = params.get("PageSize")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = SecurityGroupRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeGuideScanInfoRequest(AbstractModel):
    """DescribeGuideScanInfo request structure.

    """


class DescribeGuideScanInfoResponse(AbstractModel):
    """DescribeGuideScanInfo response structure.

    """

    def __init__(self):
        r"""
        :param Data: Scan information
        :type Data: :class:`tencentcloud.cfw.v20190904.models.ScanInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = ScanInfo()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeIPStatusListRequest(AbstractModel):
    """DescribeIPStatusList request structure.

    """

    def __init__(self):
        r"""
        :param IPList: Asset ID
        :type IPList: list of str
        """
        self.IPList = None


    def _deserialize(self, params):
        self.IPList = params.get("IPList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIPStatusListResponse(AbstractModel):
    """DescribeIPStatusList response structure.

    """

    def __init__(self):
        r"""
        :param StatusList: IP status information
        :type StatusList: list of IPDefendStatus
        :param ReturnCode: Status code
        :type ReturnCode: int
        :param ReturnMsg: Status information
        :type ReturnMsg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.StatusList = None
        self.ReturnCode = None
        self.ReturnMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("StatusList") is not None:
            self.StatusList = []
            for item in params.get("StatusList"):
                obj = IPDefendStatus()
                obj._deserialize(item)
                self.StatusList.append(obj)
        self.ReturnCode = params.get("ReturnCode")
        self.ReturnMsg = params.get("ReturnMsg")
        self.RequestId = params.get("RequestId")


class DescribeNatFwInfoCountRequest(AbstractModel):
    """DescribeNatFwInfoCount request structure.

    """


class DescribeNatFwInfoCountResponse(AbstractModel):
    """DescribeNatFwInfoCount response structure.

    """

    def __init__(self):
        r"""
        :param ReturnMsg: Response parameter
Note: This field may return `null`, indicating that no valid value was found.
        :type ReturnMsg: str
        :param NatFwInsCount: Number of NAT instances of the current tenant
Note: This field may return `null`, indicating that no valid value was found.
        :type NatFwInsCount: int
        :param SubnetCount: Number of subnets connected by the current tenant
Note: This field may return `null`, indicating that no valid value was found.
        :type SubnetCount: int
        :param OpenSwitchCount: Number of firewalls enabled
Note: This field may return `null`, indicating that no valid value was found.
        :type OpenSwitchCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ReturnMsg = None
        self.NatFwInsCount = None
        self.SubnetCount = None
        self.OpenSwitchCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReturnMsg = params.get("ReturnMsg")
        self.NatFwInsCount = params.get("NatFwInsCount")
        self.SubnetCount = params.get("SubnetCount")
        self.OpenSwitchCount = params.get("OpenSwitchCount")
        self.RequestId = params.get("RequestId")


class DescribeNatFwInstanceRequest(AbstractModel):
    """DescribeNatFwInstance request structure.

    """


class DescribeNatFwInstanceResponse(AbstractModel):
    """DescribeNatFwInstance response structure.

    """

    def __init__(self):
        r"""
        :param NatinsLst: Instance array
        :type NatinsLst: list of NatFwInstance
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NatinsLst = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NatinsLst") is not None:
            self.NatinsLst = []
            for item in params.get("NatinsLst"):
                obj = NatFwInstance()
                obj._deserialize(item)
                self.NatinsLst.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNatFwInstanceWithRegionRequest(AbstractModel):
    """DescribeNatFwInstanceWithRegion request structure.

    """


class DescribeNatFwInstanceWithRegionResponse(AbstractModel):
    """DescribeNatFwInstanceWithRegion response structure.

    """

    def __init__(self):
        r"""
        :param NatinsLst: Instance array
Note: This field may return `null`, indicating that no valid value was found.
        :type NatinsLst: list of NatFwInstance
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NatinsLst = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NatinsLst") is not None:
            self.NatinsLst = []
            for item in params.get("NatinsLst"):
                obj = NatFwInstance()
                obj._deserialize(item)
                self.NatinsLst.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNatFwInstancesInfoRequest(AbstractModel):
    """DescribeNatFwInstancesInfo request structure.

    """

    def __init__(self):
        r"""
        :param Filter: Gets filtering fields of instance list
        :type Filter: list of NatFwFilter
        :param Offset: Page number
        :type Offset: int
        :param Limit: Page length
        :type Limit: int
        """
        self.Filter = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self.Filter = []
            for item in params.get("Filter"):
                obj = NatFwFilter()
                obj._deserialize(item)
                self.Filter.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNatFwInstancesInfoResponse(AbstractModel):
    """DescribeNatFwInstancesInfo response structure.

    """

    def __init__(self):
        r"""
        :param NatinsLst: Instance card info array
Note: This field may return `null`, indicating that no valid value was found.
        :type NatinsLst: list of NatInstanceInfo
        :param Total: Number of NAT firewalls
Note: This field may return `null`, indicating that no valid value was found.
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NatinsLst = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NatinsLst") is not None:
            self.NatinsLst = []
            for item in params.get("NatinsLst"):
                obj = NatInstanceInfo()
                obj._deserialize(item)
                self.NatinsLst.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeNatFwVpcDnsLstRequest(AbstractModel):
    """DescribeNatFwVpcDnsLst request structure.

    """

    def __init__(self):
        r"""
        :param NatFwInsId: NAT firewall instance ID
        :type NatFwInsId: str
        :param NatInsIdFilter: Content filtered by NAT firewall, separated with ","
        :type NatInsIdFilter: str
        :param Offset: Number of pages
        :type Offset: int
        :param Limit: Maximum entries per page
        :type Limit: int
        """
        self.NatFwInsId = None
        self.NatInsIdFilter = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NatFwInsId = params.get("NatFwInsId")
        self.NatInsIdFilter = params.get("NatInsIdFilter")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNatFwVpcDnsLstResponse(AbstractModel):
    """DescribeNatFwVpcDnsLst response structure.

    """

    def __init__(self):
        r"""
        :param VpcDnsSwitchLst: VPC DNS info array of NAT firewall
Note: This field may return `null`, indicating that no valid value was found.
        :type VpcDnsSwitchLst: list of VpcDnsInfo
        :param ReturnMsg: Response parameter
Note: This field may return `null`, indicating that no valid value was found.
        :type ReturnMsg: str
        :param Total: Total number of toggles
Note: This field may return `null`, indicating that no valid value was found.
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.VpcDnsSwitchLst = None
        self.ReturnMsg = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VpcDnsSwitchLst") is not None:
            self.VpcDnsSwitchLst = []
            for item in params.get("VpcDnsSwitchLst"):
                obj = VpcDnsInfo()
                obj._deserialize(item)
                self.VpcDnsSwitchLst.append(obj)
        self.ReturnMsg = params.get("ReturnMsg")
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeResourceGroupNewRequest(AbstractModel):
    """DescribeResourceGroupNew request structure.

    """

    def __init__(self):
        r"""
        :param QueryType: Query type. Network–VPC; business recognition–resource; resource tag–tag
        :type QueryType: str
        :param GroupId: Asset group ID, 0: all asset group IDs
        :type GroupId: str
        :param ShowType: all: all, including subgroups; own: my asset groups only
        :type ShowType: str
        """
        self.QueryType = None
        self.GroupId = None
        self.ShowType = None


    def _deserialize(self, params):
        self.QueryType = params.get("QueryType")
        self.GroupId = params.get("GroupId")
        self.ShowType = params.get("ShowType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceGroupNewResponse(AbstractModel):
    """DescribeResourceGroupNew response structure.

    """

    def __init__(self):
        r"""
        :param Data: Returns a tree structure
        :type Data: str
        :param UnResourceNum: Number of uncategorizd instances
        :type UnResourceNum: int
        :param ReturnMsg: Response message
        :type ReturnMsg: str
        :param ReturnCode: Return code. 0: Request successful
        :type ReturnCode: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.UnResourceNum = None
        self.ReturnMsg = None
        self.ReturnCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.UnResourceNum = params.get("UnResourceNum")
        self.ReturnMsg = params.get("ReturnMsg")
        self.ReturnCode = params.get("ReturnCode")
        self.RequestId = params.get("RequestId")


class DescribeRuleOverviewRequest(AbstractModel):
    """DescribeRuleOverview request structure.

    """

    def __init__(self):
        r"""
        :param Direction: Direction. 0: outbound; 1: inbound
        :type Direction: int
        """
        self.Direction = None


    def _deserialize(self, params):
        self.Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleOverviewResponse(AbstractModel):
    """DescribeRuleOverview response structure.

    """

    def __init__(self):
        r"""
        :param AllTotal: Total number of rules
Note: This field may return `null`, indicating that no valid value was found.
        :type AllTotal: int
        :param StrategyNum: Number of blocking rules
Note: This field may return `null`, indicating that no valid value was found.
        :type StrategyNum: int
        :param StartRuleNum: Number of enabled rules
Note: This field may return `null`, indicating that no valid value was found.
        :type StartRuleNum: int
        :param StopRuleNum: Number of disabled rules
Note: This field may return `null`, indicating that no valid value was found.
        :type StopRuleNum: int
        :param RemainingNum: Remaining quota
Note: This field may return `null`, indicating that no valid value was found.
        :type RemainingNum: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AllTotal = None
        self.StrategyNum = None
        self.StartRuleNum = None
        self.StopRuleNum = None
        self.RemainingNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AllTotal = params.get("AllTotal")
        self.StrategyNum = params.get("StrategyNum")
        self.StartRuleNum = params.get("StartRuleNum")
        self.StopRuleNum = params.get("StopRuleNum")
        self.RemainingNum = params.get("RemainingNum")
        self.RequestId = params.get("RequestId")


class DescribeSecurityGroupListRequest(AbstractModel):
    """DescribeSecurityGroupList request structure.

    """

    def __init__(self):
        r"""
        :param Direction: 0: outbound rule; 1: inbound rule
        :type Direction: int
        :param Area: Region code (e.g. ap-guangzhou ). All Tencent Cloud regions are supported.
        :type Area: str
        :param SearchValue: Search value
        :type SearchValue: str
        :param Limit: Number of entries per page. Default: 10
        :type Limit: int
        :param Offset: Offset. Default: 0
        :type Offset: int
        :param Status: Status. Null: all; '0': filter disabled rules; '1': filter enabled rules
        :type Status: str
        :param Filter: 0: not filter; 1: filter out normal rules to retain abnormal rules
        :type Filter: int
        """
        self.Direction = None
        self.Area = None
        self.SearchValue = None
        self.Limit = None
        self.Offset = None
        self.Status = None
        self.Filter = None


    def _deserialize(self, params):
        self.Direction = params.get("Direction")
        self.Area = params.get("Area")
        self.SearchValue = params.get("SearchValue")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Status = params.get("Status")
        self.Filter = params.get("Filter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityGroupListResponse(AbstractModel):
    """DescribeSecurityGroupList response structure.

    """

    def __init__(self):
        r"""
        :param Total: Total rules in the list
        :type Total: int
        :param Data: Security group rule list data
        :type Data: list of SecurityGroupListData
        :param AllTotal: Total entries excluding the filtered ones
        :type AllTotal: int
        :param Enable: All access control rules enabled/disabled
Note: This field may return `null`, indicating that no valid value was found.
        :type Enable: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.Data = None
        self.AllTotal = None
        self.Enable = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecurityGroupListData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.AllTotal = params.get("AllTotal")
        self.Enable = params.get("Enable")
        self.RequestId = params.get("RequestId")


class DescribeSourceAssetRequest(AbstractModel):
    """DescribeSourceAsset request structure.

    """

    def __init__(self):
        r"""
        :param FuzzySearch: Fuzzy search
        :type FuzzySearch: str
        :param InsType: Asset type. 1: public network; 2: private network
        :type InsType: str
        :param ChooseType: If ChooseType is 1, grouped assets are queried; if ChooseType is not 1, non-grouped assets are queried
        :type ChooseType: str
        :param Zone: Region
        :type Zone: str
        :param Limit: Maximum number of results returned per page. For example, if it is set to 10, 10 results will be returned at most.
        :type Limit: int
        :param Offset: Offset of search results
        :type Offset: int
        """
        self.FuzzySearch = None
        self.InsType = None
        self.ChooseType = None
        self.Zone = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.FuzzySearch = params.get("FuzzySearch")
        self.InsType = params.get("InsType")
        self.ChooseType = params.get("ChooseType")
        self.Zone = params.get("Zone")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSourceAssetResponse(AbstractModel):
    """DescribeSourceAsset response structure.

    """

    def __init__(self):
        r"""
        :param ZoneList: Region collection
        :type ZoneList: list of AssetZone
        :param Data: Data
        :type Data: list of InstanceInfo
        :param Total: Total number of returned data
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ZoneList = None
        self.Data = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ZoneList") is not None:
            self.ZoneList = []
            for item in params.get("ZoneList"):
                obj = AssetZone()
                obj._deserialize(item)
                self.ZoneList.append(obj)
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeSwitchListsRequest(AbstractModel):
    """DescribeSwitchLists request structure.

    """

    def __init__(self):
        r"""
        :param Status: Firewall status. 0: disabled; 1: enabled
        :type Status: int
        :param Type: Asset type, e.g. CVM/NAT/VPN/CLB/others
        :type Type: str
        :param Area: Region, e.g. Shanghai, Chongqing, Guangzhou, etc.
        :type Area: str
        :param SearchValue: Search value, e.g. "{"common":"106.54.189.45"}"
        :type SearchValue: str
        :param Limit: Number of entries. Default: 10
        :type Limit: int
        :param Offset: Offset. Default: 0
        :type Offset: int
        :param Order: Sort order. desc: descending; asc: ascending
        :type Order: str
        :param By: Sorting field. PortTimes (number of risky ports)
        :type By: str
        """
        self.Status = None
        self.Type = None
        self.Area = None
        self.SearchValue = None
        self.Limit = None
        self.Offset = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.Area = params.get("Area")
        self.SearchValue = params.get("SearchValue")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSwitchListsResponse(AbstractModel):
    """DescribeSwitchLists response structure.

    """

    def __init__(self):
        r"""
        :param Total: Total entries
        :type Total: int
        :param Data: List data
        :type Data: list of SwitchListsData
        :param AreaLists: Region list
        :type AreaLists: list of str
        :param OnNum: Number of enabled firewalls
Note: This field may return `null`, indicating that no valid value was found.
        :type OnNum: int
        :param OffNum: Number of disabled firewalls
Note: This field may return `null`, indicating that no valid value was found.
        :type OffNum: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.Data = None
        self.AreaLists = None
        self.OnNum = None
        self.OffNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SwitchListsData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.AreaLists = params.get("AreaLists")
        self.OnNum = params.get("OnNum")
        self.OffNum = params.get("OffNum")
        self.RequestId = params.get("RequestId")


class DescribeTLogInfoRequest(AbstractModel):
    """DescribeTLogInfo request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param QueryType: Type. 1: alert; 2: block
        :type QueryType: str
        :param SearchValue: Search criteria
        :type SearchValue: str
        """
        self.StartTime = None
        self.EndTime = None
        self.QueryType = None
        self.SearchValue = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.QueryType = params.get("QueryType")
        self.SearchValue = params.get("SearchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTLogInfoResponse(AbstractModel):
    """DescribeTLogInfo response structure.

    """

    def __init__(self):
        r"""
        :param Data: None
        :type Data: :class:`tencentcloud.cfw.v20190904.models.TLogInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = TLogInfo()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeTLogIpListRequest(AbstractModel):
    """DescribeTLogIpList request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param QueryType: Type. 1: alert; 2: block
        :type QueryType: str
        :param Top: Number of top results returned
        :type Top: int
        :param SearchValue: Search criteria
        :type SearchValue: str
        """
        self.StartTime = None
        self.EndTime = None
        self.QueryType = None
        self.Top = None
        self.SearchValue = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.QueryType = params.get("QueryType")
        self.Top = params.get("Top")
        self.SearchValue = params.get("SearchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTLogIpListResponse(AbstractModel):
    """DescribeTLogIpList response structure.

    """

    def __init__(self):
        r"""
        :param Data: Data collection
        :type Data: list of StaticInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = StaticInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTableStatusRequest(AbstractModel):
    """DescribeTableStatus request structure.

    """

    def __init__(self):
        r"""
        :param EdgeId: Edge ID between two VPCs, required for VPCs
        :type EdgeId: str
        :param Status: Status value. 0: the only default value
        :type Status: int
        :param Area: NAT region, required for NAT
        :type Area: str
        :param Direction: Direction. 0: outbound; 1: inbound. 0 by default
        :type Direction: int
        """
        self.EdgeId = None
        self.Status = None
        self.Area = None
        self.Direction = None


    def _deserialize(self, params):
        self.EdgeId = params.get("EdgeId")
        self.Status = params.get("Status")
        self.Area = params.get("Area")
        self.Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTableStatusResponse(AbstractModel):
    """DescribeTableStatus response structure.

    """

    def __init__(self):
        r"""
        :param Status: 0: normal; non-0: abnormal
Note: This field may return `null`, indicating that no valid value was found.
        :type Status: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeUnHandleEventTabListRequest(AbstractModel):
    """DescribeUnHandleEventTabList request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time
        :type StartTime: str
        :param EndTime: End time
        :type EndTime: str
        :param AssetID: Gets example ID
        :type AssetID: str
        """
        self.StartTime = None
        self.EndTime = None
        self.AssetID = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.AssetID = params.get("AssetID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUnHandleEventTabListResponse(AbstractModel):
    """DescribeUnHandleEventTabList response structure.

    """

    def __init__(self):
        r"""
        :param Data: Gets unhandled security events
Note: This field may return `null`, indicating that no valid value was found.
        :type Data: :class:`tencentcloud.cfw.v20190904.models.UnHandleEvent`
        :param ReturnCode: Error code. 0: success; non-0: error
        :type ReturnCode: int
        :param ReturnMsg: Return message: success
        :type ReturnMsg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.ReturnCode = None
        self.ReturnMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = UnHandleEvent()
            self.Data._deserialize(params.get("Data"))
        self.ReturnCode = params.get("ReturnCode")
        self.ReturnMsg = params.get("ReturnMsg")
        self.RequestId = params.get("RequestId")


class DnsVpcSwitch(AbstractModel):
    """Sets the VPC DNS toggle of the NAT firewall

    """

    def __init__(self):
        r"""
        :param VpcId: VPC ID
        :type VpcId: str
        :param Status: 0: off; 1: on
        :type Status: int
        """
        self.VpcId = None
        self.Status = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExpandCfwVerticalRequest(AbstractModel):
    """ExpandCfwVertical request structure.

    """

    def __init__(self):
        r"""
        :param FwType: nat: NAT firewall, ew: east-west firewall
        :type FwType: str
        :param Width: Bandwidth value
        :type Width: int
        :param CfwInstance: Firewall instance ID
        :type CfwInstance: str
        """
        self.FwType = None
        self.Width = None
        self.CfwInstance = None


    def _deserialize(self, params):
        self.FwType = params.get("FwType")
        self.Width = params.get("Width")
        self.CfwInstance = params.get("CfwInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExpandCfwVerticalResponse(AbstractModel):
    """ExpandCfwVertical response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class IPDefendStatus(AbstractModel):
    """IP protection status

    """

    def __init__(self):
        r"""
        :param IP: IP address
        :type IP: str
        :param Status: Protection status. 1: enabled; -1: incorrect address; others: disabled
        :type Status: int
        """
        self.IP = None
        self.Status = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
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
        :param AppId: App ID
        :type AppId: str
        :param Region: Region
        :type Region: str
        :param VpcId: VPC ID
        :type VpcId: str
        :param VPCName: VPC name
        :type VPCName: str
        :param SubnetId: Subnet ID
        :type SubnetId: str
        :param InstanceId: Asset ID
        :type InstanceId: str
        :param InstanceName: Asset name
        :type InstanceName: str
        :param InsType: Asset type
 3: CVM instance; 4: CLB instance; 5: ENI instance; 6: MySQL; 7: Redis; 8: NAT; 9: VPN; 10: ES; 11: MariaDB; 12: Kafka; 13: NATFW
        :type InsType: int
        :param PublicIp: Public IP
        :type PublicIp: str
        :param PrivateIp: Private IP
        :type PrivateIp: str
        :param PortNum: Number of ports
        :type PortNum: str
        :param LeakNum: Number of vulnerabilities
        :type LeakNum: str
        :param InsSource: 1: public network; 2: private network
        :type InsSource: str
        :param ResourcePath: [a,b]
Note: This field may return `null`, indicating that no valid value was found.
        :type ResourcePath: list of str
        """
        self.AppId = None
        self.Region = None
        self.VpcId = None
        self.VPCName = None
        self.SubnetId = None
        self.InstanceId = None
        self.InstanceName = None
        self.InsType = None
        self.PublicIp = None
        self.PrivateIp = None
        self.PortNum = None
        self.LeakNum = None
        self.InsSource = None
        self.ResourcePath = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.Region = params.get("Region")
        self.VpcId = params.get("VpcId")
        self.VPCName = params.get("VPCName")
        self.SubnetId = params.get("SubnetId")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.InsType = params.get("InsType")
        self.PublicIp = params.get("PublicIp")
        self.PrivateIp = params.get("PrivateIp")
        self.PortNum = params.get("PortNum")
        self.LeakNum = params.get("LeakNum")
        self.InsSource = params.get("InsSource")
        self.ResourcePath = params.get("ResourcePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IocListData(AbstractModel):
    """Blocklist, allowlist, IOC list

    """

    def __init__(self):
        r"""
        :param IP: IP address to be handled. Either IP or Domain is required.
        :type IP: str
        :param Direction: 0 or 1. 0: outbound; 1: inbound
        :type Direction: int
        :param Domain: Domain name to be handled. Either IP or Domain is required.
        :type Domain: str
        """
        self.IP = None
        self.Direction = None
        self.Domain = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.Direction = params.get("Direction")
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpStatic(AbstractModel):
    """Statistical line graph general structure

    """

    def __init__(self):
        r"""
        :param Num: Value
        :type Num: int
        :param StatTime: Time shown on the x-axis of the line graph
        :type StatTime: str
        """
        self.Num = None
        self.StatTime = None


    def _deserialize(self, params):
        self.Num = params.get("Num")
        self.StatTime = params.get("StatTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAcRuleRequest(AbstractModel):
    """ModifyAcRule request structure.

    """

    def __init__(self):
        r"""
        :param Data: Array of rules
        :type Data: list of RuleInfoData
        :param EdgeId: EdgeId value
        :type EdgeId: str
        :param Enable: Access rule status
        :type Enable: int
        :param Area: NAT region
        :type Area: str
        """
        self.Data = None
        self.EdgeId = None
        self.Enable = None
        self.Area = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = RuleInfoData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.EdgeId = params.get("EdgeId")
        self.Enable = params.get("Enable")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAcRuleResponse(AbstractModel):
    """ModifyAcRule response structure.

    """

    def __init__(self):
        r"""
        :param Status: Status value. 0: operation successful; non-0: operation failed
        :type Status: int
        :param Info: Returns redundant information
Note: This field may return `null`, indicating that no valid value was found.
        :type Info: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Info = params.get("Info")
        self.RequestId = params.get("RequestId")


class ModifyAllPublicIPSwitchStatusRequest(AbstractModel):
    """ModifyAllPublicIPSwitchStatus request structure.

    """

    def __init__(self):
        r"""
        :param Status: Status. 0: off; 1: on
        :type Status: int
        :param FireWallPublicIPs: ID of the selected firewall toggle
        :type FireWallPublicIPs: list of str
        """
        self.Status = None
        self.FireWallPublicIPs = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.FireWallPublicIPs = params.get("FireWallPublicIPs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAllPublicIPSwitchStatusResponse(AbstractModel):
    """ModifyAllPublicIPSwitchStatus response structure.

    """

    def __init__(self):
        r"""
        :param ReturnMsg: Return message
Note: This field may return `null`, indicating that no valid value was found.
        :type ReturnMsg: str
        :param ReturnCode: Error code. 0: success; non-0: failed
Note: This field may return `null`, indicating that no valid value was found.
        :type ReturnCode: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ReturnMsg = None
        self.ReturnCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReturnMsg = params.get("ReturnMsg")
        self.ReturnCode = params.get("ReturnCode")
        self.RequestId = params.get("RequestId")


class ModifyAllRuleStatusRequest(AbstractModel):
    """ModifyAllRuleStatus request structure.

    """

    def __init__(self):
        r"""
        :param Status: Status. 0: all disabled; 1: all enabled
        :type Status: int
        :param Direction: Direction. 0: outbound; 1: inbound
        :type Direction: int
        :param EdgeId: Edge ID value
        :type EdgeId: str
        :param Area: NAT region
        :type Area: str
        """
        self.Status = None
        self.Direction = None
        self.EdgeId = None
        self.Area = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Direction = params.get("Direction")
        self.EdgeId = params.get("EdgeId")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAllRuleStatusResponse(AbstractModel):
    """ModifyAllRuleStatus response structure.

    """

    def __init__(self):
        r"""
        :param Status: 0: modified successfully; non-0: modification failed
Note: This field may return `null`, indicating that no valid value was found.
        :type Status: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ModifyAllVPCSwitchStatusRequest(AbstractModel):
    """ModifyAllVPCSwitchStatus request structure.

    """

    def __init__(self):
        r"""
        :param Status: Status. 0: off; 1: on
        :type Status: int
        :param FireWallVpcIds: ID of the selected firewall toggle
        :type FireWallVpcIds: list of str
        """
        self.Status = None
        self.FireWallVpcIds = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.FireWallVpcIds = params.get("FireWallVpcIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAllVPCSwitchStatusResponse(AbstractModel):
    """ModifyAllVPCSwitchStatus response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAssetScanRequest(AbstractModel):
    """ModifyAssetScan request structure.

    """

    def __init__(self):
        r"""
        :param ScanRange: Scan range. 1: port; 2: port + vulnerability scan
        :type ScanRange: int
        :param ScanDeep: Scan mode: 'heavy', 'medium', 'light'
        :type ScanDeep: str
        :param RangeType: Scan type. 1: scan now; 2: periodic scan
        :type RangeType: int
        :param ScanPeriod: Scheduled task time, required when RangeType is 2
        :type ScanPeriod: str
        :param ScanFilterIp: Scans this field now and passes the filtered IPs
        :type ScanFilterIp: list of str
        :param ScanType: 1: all; 2: single
        :type ScanType: int
        """
        self.ScanRange = None
        self.ScanDeep = None
        self.RangeType = None
        self.ScanPeriod = None
        self.ScanFilterIp = None
        self.ScanType = None


    def _deserialize(self, params):
        self.ScanRange = params.get("ScanRange")
        self.ScanDeep = params.get("ScanDeep")
        self.RangeType = params.get("RangeType")
        self.ScanPeriod = params.get("ScanPeriod")
        self.ScanFilterIp = params.get("ScanFilterIp")
        self.ScanType = params.get("ScanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAssetScanResponse(AbstractModel):
    """ModifyAssetScan response structure.

    """

    def __init__(self):
        r"""
        :param ReturnMsg: Return message
Note: This field may return `null`, indicating that no valid value was found.
        :type ReturnMsg: str
        :param ReturnCode: Error code. 0: success; non-0: failed
Note: This field may return `null`, indicating that no valid value was found.
        :type ReturnCode: int
        :param Status: Status value. 0: success; 1: scanning; others: failed
        :type Status: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ReturnMsg = None
        self.ReturnCode = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReturnMsg = params.get("ReturnMsg")
        self.ReturnCode = params.get("ReturnCode")
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ModifyBlockIgnoreListRequest(AbstractModel):
    """ModifyBlockIgnoreList request structure.

    """

    def __init__(self):
        r"""
        :param RuleType: 1: blocklist; 2: ignore list
        :type RuleType: int
        :param IOC: Either IP or Domain is required
        :type IOC: list of IocListData
        :param IocAction: Optional values: delete, edit, and add
        :type IocAction: str
        :param StartTime: Time format: yyyy-MM-dd HH:mm:ss. Required when IocAction is edit or add
        :type StartTime: str
        :param EndTime: Time format: yyyy-MM-dd HH:mm:ss. Required when IocAction is edit or add
        :type EndTime: str
        """
        self.RuleType = None
        self.IOC = None
        self.IocAction = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.RuleType = params.get("RuleType")
        if params.get("IOC") is not None:
            self.IOC = []
            for item in params.get("IOC"):
                obj = IocListData()
                obj._deserialize(item)
                self.IOC.append(obj)
        self.IocAction = params.get("IocAction")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBlockIgnoreListResponse(AbstractModel):
    """ModifyBlockIgnoreList response structure.

    """

    def __init__(self):
        r"""
        :param ReturnMsg: Return message
        :type ReturnMsg: str
        :param ReturnCode: Error code. 0: success; non-0: failed
        :type ReturnCode: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ReturnMsg = None
        self.ReturnCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReturnMsg = params.get("ReturnMsg")
        self.ReturnCode = params.get("ReturnCode")
        self.RequestId = params.get("RequestId")


class ModifyBlockTopRequest(AbstractModel):
    """ModifyBlockTop request structure.

    """

    def __init__(self):
        r"""
        :param UniqueId: Record ID
        :type UniqueId: str
        :param OpeType: Operation type. 1: pin to top; 0: unpin
        :type OpeType: str
        """
        self.UniqueId = None
        self.OpeType = None


    def _deserialize(self, params):
        self.UniqueId = params.get("UniqueId")
        self.OpeType = params.get("OpeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBlockTopResponse(AbstractModel):
    """ModifyBlockTop response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNatFwReSelectRequest(AbstractModel):
    """ModifyNatFwReSelect request structure.

    """

    def __init__(self):
        r"""
        :param Mode: Mode. 1: use existing; 0: create new
        :type Mode: int
        :param CfwInstance: Firewall instance ID
        :type CfwInstance: str
        :param NatGwList: List of NAT gateways reconnected for the Using Existing mode. Only one of NatGwList and VpcList can be passed.
        :type NatGwList: list of str
        :param VpcList: List of VPCs reconnected for the Create New mode. Only one of NatGwList and VpcList can be passed.
        :type VpcList: list of str
        """
        self.Mode = None
        self.CfwInstance = None
        self.NatGwList = None
        self.VpcList = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        self.CfwInstance = params.get("CfwInstance")
        self.NatGwList = params.get("NatGwList")
        self.VpcList = params.get("VpcList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNatFwReSelectResponse(AbstractModel):
    """ModifyNatFwReSelect response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNatFwSwitchRequest(AbstractModel):
    """ModifyNatFwSwitch request structure.

    """

    def __init__(self):
        r"""
        :param Enable: Status. 0: off; 1: on
        :type Enable: int
        :param CfwInsIdList: List of firewall instance IDs. Only one of CfwInsIdList, SubnetIdList, and RouteTableIdList can be passed.
        :type CfwInsIdList: list of str
        :param SubnetIdList: List of subnet IDs. Only one of CfwInsIdList, SubnetIdList, and RouteTableIdList can be passed.
        :type SubnetIdList: list of str
        :param RouteTableIdList: List of route table IDs. Only one of CfwInsIdList, SubnetIdList, and RouteTableIdList can be passed.
        :type RouteTableIdList: list of str
        """
        self.Enable = None
        self.CfwInsIdList = None
        self.SubnetIdList = None
        self.RouteTableIdList = None


    def _deserialize(self, params):
        self.Enable = params.get("Enable")
        self.CfwInsIdList = params.get("CfwInsIdList")
        self.SubnetIdList = params.get("SubnetIdList")
        self.RouteTableIdList = params.get("RouteTableIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNatFwSwitchResponse(AbstractModel):
    """ModifyNatFwSwitch response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNatFwVpcDnsSwitchRequest(AbstractModel):
    """ModifyNatFwVpcDnsSwitch request structure.

    """

    def __init__(self):
        r"""
        :param NatFwInsId: NAT firewall ID
        :type NatFwInsId: str
        :param DnsVpcSwitchLst: DNS toggle list
        :type DnsVpcSwitchLst: list of DnsVpcSwitch
        """
        self.NatFwInsId = None
        self.DnsVpcSwitchLst = None


    def _deserialize(self, params):
        self.NatFwInsId = params.get("NatFwInsId")
        if params.get("DnsVpcSwitchLst") is not None:
            self.DnsVpcSwitchLst = []
            for item in params.get("DnsVpcSwitchLst"):
                obj = DnsVpcSwitch()
                obj._deserialize(item)
                self.DnsVpcSwitchLst.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNatFwVpcDnsSwitchResponse(AbstractModel):
    """ModifyNatFwVpcDnsSwitch response structure.

    """

    def __init__(self):
        r"""
        :param ReturnMsg: Modified successfully
Note: This field may return `null`, indicating that no valid value was found.
        :type ReturnMsg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ReturnMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReturnMsg = params.get("ReturnMsg")
        self.RequestId = params.get("RequestId")


class ModifyPublicIPSwitchStatusRequest(AbstractModel):
    """ModifyPublicIPSwitchStatus request structure.

    """

    def __init__(self):
        r"""
        :param FireWallPublicIP: Public IP
        :type FireWallPublicIP: str
        :param Status: Status value. 0: off; 1: on
        :type Status: int
        """
        self.FireWallPublicIP = None
        self.Status = None


    def _deserialize(self, params):
        self.FireWallPublicIP = params.get("FireWallPublicIP")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPublicIPSwitchStatusResponse(AbstractModel):
    """ModifyPublicIPSwitchStatus response structure.

    """

    def __init__(self):
        r"""
        :param ReturnMsg: Return message
Note: This field may return `null`, indicating that no valid value was found.
        :type ReturnMsg: str
        :param ReturnCode: Error code. 0: success; non-0: failed
        :type ReturnCode: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ReturnMsg = None
        self.ReturnCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReturnMsg = params.get("ReturnMsg")
        self.ReturnCode = params.get("ReturnCode")
        self.RequestId = params.get("RequestId")


class ModifyResourceGroupRequest(AbstractModel):
    """ModifyResourceGroup request structure.

    """

    def __init__(self):
        r"""
        :param GroupId: Group ID
        :type GroupId: str
        :param GroupName: Group name
        :type GroupName: str
        :param ParentId: Parent group ID
        :type ParentId: str
        """
        self.GroupId = None
        self.GroupName = None
        self.ParentId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.ParentId = params.get("ParentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourceGroupResponse(AbstractModel):
    """ModifyResourceGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRunSyncAssetRequest(AbstractModel):
    """ModifyRunSyncAsset request structure.

    """

    def __init__(self):
        r"""
        :param Type: 0: edge firewall toggle; 1: VPC firewall toggle
        :type Type: int
        """
        self.Type = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRunSyncAssetResponse(AbstractModel):
    """ModifyRunSyncAsset response structure.

    """

    def __init__(self):
        r"""
        :param Status: 0: synced successfully, 1: updating assets, 2: failed to sync by calling the API at the backend
        :type Status: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ModifySecurityGroupItemRuleStatusRequest(AbstractModel):
    """ModifySecurityGroupItemRuleStatus request structure.

    """

    def __init__(self):
        r"""
        :param Direction: Direction. 0: outbound; 1: inbound. 1 by default
        :type Direction: int
        :param Status: Toggle status. 0: off; 1: on
        :type Status: int
        :param RuleSequence: Modified priority of enterprise security group rules
        :type RuleSequence: int
        """
        self.Direction = None
        self.Status = None
        self.RuleSequence = None


    def _deserialize(self, params):
        self.Direction = params.get("Direction")
        self.Status = params.get("Status")
        self.RuleSequence = params.get("RuleSequence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityGroupItemRuleStatusResponse(AbstractModel):
    """ModifySecurityGroupItemRuleStatus response structure.

    """

    def __init__(self):
        r"""
        :param Status: Status value. 0: modified successfully; non-0: failed to modify
        :type Status: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ModifySecurityGroupSequenceRulesRequest(AbstractModel):
    """ModifySecurityGroupSequenceRules request structure.

    """

    def __init__(self):
        r"""
        :param Direction: Direction. 0: outbound; 1: inbound. 1 by default
        :type Direction: int
        :param Data: Sorting data of enterprise security group rules
        :type Data: list of SecurityGroupOrderIndexData
        """
        self.Direction = None
        self.Data = None


    def _deserialize(self, params):
        self.Direction = params.get("Direction")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecurityGroupOrderIndexData()
                obj._deserialize(item)
                self.Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityGroupSequenceRulesResponse(AbstractModel):
    """ModifySecurityGroupSequenceRules response structure.

    """

    def __init__(self):
        r"""
        :param Status: Status value. 0: modified successfully; non-0: failed to modify
        :type Status: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ModifySequenceRulesRequest(AbstractModel):
    """ModifySequenceRules request structure.

    """

    def __init__(self):
        r"""
        :param EdgeId: Edge ID value
        :type EdgeId: str
        :param Data: Modifies data
        :type Data: list of SequenceData
        :param Area: NAT region
        :type Area: str
        :param Direction: Direction. 0: outbound; 1: inbound
        :type Direction: int
        """
        self.EdgeId = None
        self.Data = None
        self.Area = None
        self.Direction = None


    def _deserialize(self, params):
        self.EdgeId = params.get("EdgeId")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SequenceData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Area = params.get("Area")
        self.Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySequenceRulesResponse(AbstractModel):
    """ModifySequenceRules response structure.

    """

    def __init__(self):
        r"""
        :param Status: 0: modified successfully; non-0: modification failed
Note: This field may return `null`, indicating that no valid value was found.
        :type Status: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ModifyTableStatusRequest(AbstractModel):
    """ModifyTableStatus request structure.

    """

    def __init__(self):
        r"""
        :param EdgeId: Edge ID between two VPCs
        :type EdgeId: str
        :param Status: Status value. 1: table locked; 2: table unlocked
        :type Status: int
        :param Area: NAT region
        :type Area: str
        :param Direction: 0: outbound; 1: inbound
        :type Direction: int
        """
        self.EdgeId = None
        self.Status = None
        self.Area = None
        self.Direction = None


    def _deserialize(self, params):
        self.EdgeId = params.get("EdgeId")
        self.Status = params.get("Status")
        self.Area = params.get("Area")
        self.Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTableStatusResponse(AbstractModel):
    """ModifyTableStatus response structure.

    """

    def __init__(self):
        r"""
        :param Status: 0: normal; -1: abnormal
Note: This field may return `null`, indicating that no valid value was found.
        :type Status: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class NatFwFilter(AbstractModel):
    """The filter list displayed by the NAT firewall instance

    """

    def __init__(self):
        r"""
        :param FilterType: Filter type, e.g., instance ID
        :type FilterType: str
        :param FilterContent: Filtered content, separated with ","
        :type FilterContent: str
        """
        self.FilterType = None
        self.FilterContent = None


    def _deserialize(self, params):
        self.FilterType = params.get("FilterType")
        self.FilterContent = params.get("FilterContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NatFwInstance(AbstractModel):
    """NAT instance type

    """

    def __init__(self):
        r"""
        :param NatinsId: NAT instance ID
        :type NatinsId: str
        :param NatinsName: NAT instance name
        :type NatinsName: str
        :param Region: Instance region
Note: This field may return `null`, indicating that no valid value was found.
        :type Region: str
        :param FwMode: 0: create new; 1: use existing
Note: This field may return `null`, indicating that no valid value was found.
        :type FwMode: int
        :param Status: 0: normal; 1: creating
Note: This field may return `null`, indicating that no valid value was found.
        :type Status: int
        :param NatIp: NAT public IP
Note: This field may return `null`, indicating that no valid value was found.
        :type NatIp: str
        """
        self.NatinsId = None
        self.NatinsName = None
        self.Region = None
        self.FwMode = None
        self.Status = None
        self.NatIp = None


    def _deserialize(self, params):
        self.NatinsId = params.get("NatinsId")
        self.NatinsName = params.get("NatinsName")
        self.Region = params.get("Region")
        self.FwMode = params.get("FwMode")
        self.Status = params.get("Status")
        self.NatIp = params.get("NatIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NatInstanceInfo(AbstractModel):
    """NAT instance card details

    """

    def __init__(self):
        r"""
        :param NatinsId: NAT instance ID
        :type NatinsId: str
        :param NatinsName: NAT instance name
        :type NatinsName: str
        :param Region: Instance region
        :type Region: str
        :param FwMode: 0: create new; 1: use existing
        :type FwMode: int
        :param BandWidth: Instance bandwidth (Mbps)
        :type BandWidth: int
        :param InFlowMax: Inbound traffic peak bandwidth (bps)
        :type InFlowMax: int
        :param OutFlowMax: Outbound traffic peak bandwidth (bps)
        :type OutFlowMax: int
        :param RegionZh: Chinese region information
        :type RegionZh: str
        :param EipAddress: Public IP array
Note: This field may return `null`, indicating that no valid value was found.
        :type EipAddress: list of str
        :param VpcIp: Array of internal and external IPs
Note: This field may return `null`, indicating that no valid value was found.
        :type VpcIp: list of str
        :param Subnets: Array of subnets associated with an instance
Note: This field may return `null`, indicating that no valid value was found.
        :type Subnets: list of str
        :param Status: 0: normal 1: initializing
Note: This field may return `null`, indicating that no valid value was found.
        :type Status: int
        :param RegionDetail: Region information
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionDetail: str
        :param ZoneZh: Availability zone of the instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneZh: str
        :param ZoneZhBak: Availability zone of the instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneZhBak: str
        """
        self.NatinsId = None
        self.NatinsName = None
        self.Region = None
        self.FwMode = None
        self.BandWidth = None
        self.InFlowMax = None
        self.OutFlowMax = None
        self.RegionZh = None
        self.EipAddress = None
        self.VpcIp = None
        self.Subnets = None
        self.Status = None
        self.RegionDetail = None
        self.ZoneZh = None
        self.ZoneZhBak = None


    def _deserialize(self, params):
        self.NatinsId = params.get("NatinsId")
        self.NatinsName = params.get("NatinsName")
        self.Region = params.get("Region")
        self.FwMode = params.get("FwMode")
        self.BandWidth = params.get("BandWidth")
        self.InFlowMax = params.get("InFlowMax")
        self.OutFlowMax = params.get("OutFlowMax")
        self.RegionZh = params.get("RegionZh")
        self.EipAddress = params.get("EipAddress")
        self.VpcIp = params.get("VpcIp")
        self.Subnets = params.get("Subnets")
        self.Status = params.get("Status")
        self.RegionDetail = params.get("RegionDetail")
        self.ZoneZh = params.get("ZoneZh")
        self.ZoneZhBak = params.get("ZoneZhBak")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NewModeItems(AbstractModel):
    """Parameters passed for the Create New mode

    """

    def __init__(self):
        r"""
        :param VpcList: VPC list for the Create New mode
        :type VpcList: list of str
        :param Eips: The list of egress public EIPs bound for the Create New mode. Either Eips or AddCount is required.
        :type Eips: list of str
        :param AddCount: The number of egress public EIPs newly bound for the Create New mode. Either Eips or AddCount is required.
        :type AddCount: int
        """
        self.VpcList = None
        self.Eips = None
        self.AddCount = None


    def _deserialize(self, params):
        self.VpcList = params.get("VpcList")
        self.Eips = params.get("Eips")
        self.AddCount = params.get("AddCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveAcRuleRequest(AbstractModel):
    """RemoveAcRule request structure.

    """

    def __init__(self):
        r"""
        :param RuleUuid: UUID of the rule, which can be obtained by querying the rule list
        :type RuleUuid: int
        """
        self.RuleUuid = None


    def _deserialize(self, params):
        self.RuleUuid = params.get("RuleUuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveAcRuleResponse(AbstractModel):
    """RemoveAcRule response structure.

    """

    def __init__(self):
        r"""
        :param RuleUuid: Returns the UUID of the deleted policy after the deletion is successful
        :type RuleUuid: int
        :param ReturnCode: 0: operation successful; -1: operation failed
Note: This field may return `null`, indicating that no valid value was found.
        :type ReturnCode: int
        :param ReturnMsg: success: operation successful; failed: operation failed
Note: This field may return `null`, indicating that no valid value was found.
        :type ReturnMsg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RuleUuid = None
        self.ReturnCode = None
        self.ReturnMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleUuid = params.get("RuleUuid")
        self.ReturnCode = params.get("ReturnCode")
        self.ReturnMsg = params.get("ReturnMsg")
        self.RequestId = params.get("RequestId")


class RemoveEnterpriseSecurityGroupRuleRequest(AbstractModel):
    """RemoveEnterpriseSecurityGroupRule request structure.

    """

    def __init__(self):
        r"""
        :param RuleUuid: UUID of the rule, which can be obtained by querying the rule list
        :type RuleUuid: int
        :param RemoveType: Type of deletion. 0: delete a single entry, and enter ID of the deleted rule for RuleUuid; 1: delete all, and enter 0 for RuleUuid
        :type RemoveType: int
        """
        self.RuleUuid = None
        self.RemoveType = None


    def _deserialize(self, params):
        self.RuleUuid = params.get("RuleUuid")
        self.RemoveType = params.get("RemoveType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveEnterpriseSecurityGroupRuleResponse(AbstractModel):
    """RemoveEnterpriseSecurityGroupRule response structure.

    """

    def __init__(self):
        r"""
        :param RuleUuid: Returns the UUID of the deleted policy after the deletion is successful
        :type RuleUuid: int
        :param Status: 0: operation successful; -1: operation failed
Note: This field may return `null`, indicating that no valid value was found.
        :type Status: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RuleUuid = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleUuid = params.get("RuleUuid")
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class RuleInfoData(AbstractModel):
    """Rule input object

    """

    def __init__(self):
        r"""
        :param OrderIndex: Priority
        :type OrderIndex: int
        :param SourceIp: Access source
        :type SourceIp: str
        :param TargetIp: Access destination
        :type TargetIp: str
        :param Protocol: Protocol
        :type Protocol: str
        :param Strategy: Policy. 0: observe; 1: block; 2: allow
        :type Strategy: str
        :param SourceType: Access source type. 1: IP; 3: domain name; 4: IP address template; 5: domain name address template
        :type SourceType: int
        :param Direction: Direction. 0: outbound; 1: inbound
        :type Direction: int
        :param Detail: Description
        :type Detail: str
        :param TargetType: Access destination type. 1: IP, 3: domain name; 4: IP address template; 5: domain name address template
        :type TargetType: int
        :param Port: Port
        :type Port: str
        :param Id: ID value
        :type Id: int
        :param LogId: Log ID, required when an alert log is created
        :type LogId: str
        :param City: City code
        :type City: int
        :param Country: Country code
        :type Country: int
        :param CloudCode: Cloud vendor. Multiple vendors are supported and separated with commas. 1: Tencent Cloud (only in Hong Kong, China and overseas); 2: Alibaba Cloud; 3: Amazon Cloud; 4: Huawei Cloud; 5: Microsoft Cloud
        :type CloudCode: str
        :param IsRegion: Indicates whether it is a region
        :type IsRegion: int
        :param CityName: City name
        :type CityName: str
        :param CountryName: Country name
        :type CountryName: str
        """
        self.OrderIndex = None
        self.SourceIp = None
        self.TargetIp = None
        self.Protocol = None
        self.Strategy = None
        self.SourceType = None
        self.Direction = None
        self.Detail = None
        self.TargetType = None
        self.Port = None
        self.Id = None
        self.LogId = None
        self.City = None
        self.Country = None
        self.CloudCode = None
        self.IsRegion = None
        self.CityName = None
        self.CountryName = None


    def _deserialize(self, params):
        self.OrderIndex = params.get("OrderIndex")
        self.SourceIp = params.get("SourceIp")
        self.TargetIp = params.get("TargetIp")
        self.Protocol = params.get("Protocol")
        self.Strategy = params.get("Strategy")
        self.SourceType = params.get("SourceType")
        self.Direction = params.get("Direction")
        self.Detail = params.get("Detail")
        self.TargetType = params.get("TargetType")
        self.Port = params.get("Port")
        self.Id = params.get("Id")
        self.LogId = params.get("LogId")
        self.City = params.get("City")
        self.Country = params.get("Country")
        self.CloudCode = params.get("CloudCode")
        self.IsRegion = params.get("IsRegion")
        self.CityName = params.get("CityName")
        self.CountryName = params.get("CountryName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanInfo(AbstractModel):
    """Getting started on scanning information

    """

    def __init__(self):
        r"""
        :param ScanResultInfo: Scanning result information
        :type ScanResultInfo: :class:`tencentcloud.cfw.v20190904.models.ScanResultInfo`
        :param ScanStatus: Scanning status. 0: scanning; 1: completed; 2: auto scanning unselected
        :type ScanStatus: int
        :param ScanPercent: Progress
        :type ScanPercent: float
        :param ScanTime: Estimated completion time
        :type ScanTime: str
        """
        self.ScanResultInfo = None
        self.ScanStatus = None
        self.ScanPercent = None
        self.ScanTime = None


    def _deserialize(self, params):
        if params.get("ScanResultInfo") is not None:
            self.ScanResultInfo = ScanResultInfo()
            self.ScanResultInfo._deserialize(params.get("ScanResultInfo"))
        self.ScanStatus = params.get("ScanStatus")
        self.ScanPercent = params.get("ScanPercent")
        self.ScanTime = params.get("ScanTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
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
        :param LeakNum: Number of vulnerability exploits
        :type LeakNum: int
        :param IPNum: Number of protected IPs
        :type IPNum: int
        :param PortNum: Number of exposed ports
        :type PortNum: int
        :param IPStatus: Protection status
        :type IPStatus: bool
        :param IdpStatus: Attack blocking status
        :type IdpStatus: bool
        :param BanStatus: Port blocking status
        :type BanStatus: bool
        """
        self.LeakNum = None
        self.IPNum = None
        self.PortNum = None
        self.IPStatus = None
        self.IdpStatus = None
        self.BanStatus = None


    def _deserialize(self, params):
        self.LeakNum = params.get("LeakNum")
        self.IPNum = params.get("IPNum")
        self.PortNum = params.get("PortNum")
        self.IPStatus = params.get("IPStatus")
        self.IdpStatus = params.get("IdpStatus")
        self.BanStatus = params.get("BanStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupBothWayInfo(AbstractModel):
    """Two-way enterprise security group rules

    """

    def __init__(self):
        r"""
        :param OrderIndex: Priority
Note: This field may return `null`, indicating that no valid value was found.
        :type OrderIndex: int
        :param SourceId: Access source
Note: This field may return `null`, indicating that no valid value was found.
        :type SourceId: str
        :param SourceType: Access source type. Default: 0. 0: IP; 1: VPC; 2: SUBNET; 3: CVM; 4: CLB; 5: ENI; 6: CDB; 7: Parameter template. 100: asset group
Note: This field may return `null`, indicating that no valid value was found.
        :type SourceType: int
        :param TargetId: Access destination
Note: This field may return `null`, indicating that no valid value was found.
        :type TargetId: str
        :param TargetType: Access destination type. Default: 0. 0: IP; 1: VPC; 2: SUBNET; 3: CVM; 4: CLB; 5: ENI; 6: CDB; 7: Parameter template. 100: asset group
Note: This field may return `null`, indicating that no valid value was found.
        :type TargetType: int
        :param Protocol: Protocol
Note: This field may return `null`, indicating that no valid value was found.
        :type Protocol: str
        :param Port: Destination port
Note: This field may return `null`, indicating that no valid value was found.
        :type Port: str
        :param Strategy: Policy. 1: block; 2: allow
Note: This field may return `null`, indicating that no valid value was found.
        :type Strategy: int
        :param Direction: Direction. 0: outbound; 1: inbound. 1 by default
Note: This field may return `null`, indicating that no valid value was found.
        :type Direction: int
        :param Region: Region
        :type Region: str
        :param Detail: Description
Note: This field may return `null`, indicating that no valid value was found.
        :type Detail: str
        :param Status: Toggle status. 0: off; 1: on
Note: This field may return `null`, indicating that no valid value was found.
        :type Status: int
        :param IsNew: Indicates whether the rule is normal. 0: normal; 1: abnormal
Note: This field may return `null`, indicating that no valid value was found.
        :type IsNew: int
        :param BothWay: One-way/two-way. 0: one-way; 1: two-way
Note: This field may return `null`, indicating that no valid value was found.
        :type BothWay: int
        :param VpcId: VPC ID
Note: This field may return `null`, indicating that no valid value was found.
        :type VpcId: str
        :param SubnetId: Subnet ID
Note: This field may return `null`, indicating that no valid value was found.
        :type SubnetId: str
        :param InstanceName: Instance name
Note: This field may return `null`, indicating that no valid value was found.
        :type InstanceName: str
        :param PublicIp: Public IP. Multiple IPs are separated by commas.
Note: This field may return `null`, indicating that no valid value was found.
        :type PublicIp: str
        :param PrivateIp: Private IP. Multiple IPs are separated by commas.
Note: This field may return `null`, indicating that no valid value was found.
        :type PrivateIp: str
        :param Cidr: Masked address. Multiple addresses are separated by commas.
Note: This field may return `null`, indicating that no valid value was found.
        :type Cidr: str
        :param ServiceTemplateId: Port protocol template ID
Note: This field may return `null`, indicating that no valid value was found.
        :type ServiceTemplateId: str
        :param ProtocolPortType: Indicates whether to use the port protocol template. 0: no; 1: yes
        :type ProtocolPortType: int
        """
        self.OrderIndex = None
        self.SourceId = None
        self.SourceType = None
        self.TargetId = None
        self.TargetType = None
        self.Protocol = None
        self.Port = None
        self.Strategy = None
        self.Direction = None
        self.Region = None
        self.Detail = None
        self.Status = None
        self.IsNew = None
        self.BothWay = None
        self.VpcId = None
        self.SubnetId = None
        self.InstanceName = None
        self.PublicIp = None
        self.PrivateIp = None
        self.Cidr = None
        self.ServiceTemplateId = None
        self.ProtocolPortType = None


    def _deserialize(self, params):
        self.OrderIndex = params.get("OrderIndex")
        self.SourceId = params.get("SourceId")
        self.SourceType = params.get("SourceType")
        self.TargetId = params.get("TargetId")
        self.TargetType = params.get("TargetType")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        self.Strategy = params.get("Strategy")
        self.Direction = params.get("Direction")
        self.Region = params.get("Region")
        self.Detail = params.get("Detail")
        self.Status = params.get("Status")
        self.IsNew = params.get("IsNew")
        self.BothWay = params.get("BothWay")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.InstanceName = params.get("InstanceName")
        self.PublicIp = params.get("PublicIp")
        self.PrivateIp = params.get("PrivateIp")
        self.Cidr = params.get("Cidr")
        self.ServiceTemplateId = params.get("ServiceTemplateId")
        self.ProtocolPortType = params.get("ProtocolPortType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupListData(AbstractModel):
    """Security group list data

    """

    def __init__(self):
        r"""
        :param OrderIndex: Priority
        :type OrderIndex: int
        :param SourceId: Access source
        :type SourceId: str
        :param SourceType: Access source type. Default: 0. 1: VPC; 2: SUBNET; 3: CVM; 4: CLB; 5: ENI; 6: CDB; 7: Parameter template. 100: Resource group
        :type SourceType: int
        :param TargetId: Access destination
        :type TargetId: str
        :param TargetType: Access destination type. Default: 0. 1: VPC; 2: SUBNET; 3: CVM; 4: CLB; 5: ENI; 6: CDB; 7: Parameter template; 100: resource group
        :type TargetType: int
        :param Protocol: Protocol
        :type Protocol: str
        :param Port: Destination port
        :type Port: str
        :param Strategy: Policy. 1: block; 2: allow
        :type Strategy: int
        :param Detail: Description
        :type Detail: str
        :param BothWay: One-way/two-way. 0: one-way; 1: two-way
        :type BothWay: int
        :param Id: Rule ID
        :type Id: int
        :param Status: Toggle status. 0: off; 1: on
        :type Status: int
        :param IsNew: Indicates whether the rule is normal. 0: normal; 1: abnormal
        :type IsNew: int
        :param VpcId: VPC ID
Note: This field may return `null`, indicating that no valid value was found.
        :type VpcId: str
        :param SubnetId: Subnet ID
Note: This field may return `null`, indicating that no valid value was found.
        :type SubnetId: str
        :param InstanceName: Instance name
Note: This field may return `null`, indicating that no valid value was found.
        :type InstanceName: str
        :param PublicIp: Public IP. Multiple IPs are separated by commas.
Note: This field may return `null`, indicating that no valid value was found.
        :type PublicIp: str
        :param PrivateIp: Private IP. Multiple IPs are separated by commas.
Note: This field may return `null`, indicating that no valid value was found.
        :type PrivateIp: str
        :param Cidr: Masked address. Multiple addresses are separated by commas.
Note: This field may return `null`, indicating that no valid value was found.
        :type Cidr: str
        :param ServiceTemplateId: Port protocol template ID
Note: This field may return `null`, indicating that no valid value was found.
        :type ServiceTemplateId: str
        :param BothWayInfo: Two-way rules
Note: This field may return `null`, indicating that no valid value was found.
        :type BothWayInfo: list of SecurityGroupBothWayInfo
        :param Direction: Direction. 0: outbound; 1: inbound. 1 by default
        :type Direction: int
        :param ProtocolPortType: Indicates whether to use the port protocol template. 0: no; 1: yes
        :type ProtocolPortType: int
        """
        self.OrderIndex = None
        self.SourceId = None
        self.SourceType = None
        self.TargetId = None
        self.TargetType = None
        self.Protocol = None
        self.Port = None
        self.Strategy = None
        self.Detail = None
        self.BothWay = None
        self.Id = None
        self.Status = None
        self.IsNew = None
        self.VpcId = None
        self.SubnetId = None
        self.InstanceName = None
        self.PublicIp = None
        self.PrivateIp = None
        self.Cidr = None
        self.ServiceTemplateId = None
        self.BothWayInfo = None
        self.Direction = None
        self.ProtocolPortType = None


    def _deserialize(self, params):
        self.OrderIndex = params.get("OrderIndex")
        self.SourceId = params.get("SourceId")
        self.SourceType = params.get("SourceType")
        self.TargetId = params.get("TargetId")
        self.TargetType = params.get("TargetType")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        self.Strategy = params.get("Strategy")
        self.Detail = params.get("Detail")
        self.BothWay = params.get("BothWay")
        self.Id = params.get("Id")
        self.Status = params.get("Status")
        self.IsNew = params.get("IsNew")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.InstanceName = params.get("InstanceName")
        self.PublicIp = params.get("PublicIp")
        self.PrivateIp = params.get("PrivateIp")
        self.Cidr = params.get("Cidr")
        self.ServiceTemplateId = params.get("ServiceTemplateId")
        if params.get("BothWayInfo") is not None:
            self.BothWayInfo = []
            for item in params.get("BothWayInfo"):
                obj = SecurityGroupBothWayInfo()
                obj._deserialize(item)
                self.BothWayInfo.append(obj)
        self.Direction = params.get("Direction")
        self.ProtocolPortType = params.get("ProtocolPortType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupOrderIndexData(AbstractModel):
    """Change priority of enterprise security group rules

    """

    def __init__(self):
        r"""
        :param OrderIndex: Current priority of enterprise security group rules
        :type OrderIndex: int
        :param NewOrderIndex: New priority of enterprise security group rules
        :type NewOrderIndex: int
        """
        self.OrderIndex = None
        self.NewOrderIndex = None


    def _deserialize(self, params):
        self.OrderIndex = params.get("OrderIndex")
        self.NewOrderIndex = params.get("NewOrderIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupRule(AbstractModel):
    """Security group rules

    """

    def __init__(self):
        r"""
        :param SourceContent: Source example:
net: IP/CIDR (192.168.0.2)
template: parameter template (ipm-dyodhpby)
instance: asset instance (ins-123456)
resourcegroup: asset group (/all groups/group 1/subgroup 1)
tag: resource tag ({"Key":"tag key","Value":"tag value"})
region: region (ap-gaungzhou)
        :type SourceContent: str
        :param SourceType: Access source type. Valid values: net|template|instance|resourcegroup|tag|region
        :type SourceType: str
        :param DestContent: Destination example:
net: IP/CIDR (192.168.0.2)
template: parameter template (ipm-dyodhpby)
instance: asset instance (ins-123456)
resourcegroup: asset group (/all groups/group 1/subgroup 1)
tag: resource tag ({"Key":"tag key","Value":"tag value"})
region: region (ap-gaungzhou)
        :type DestContent: str
        :param DestType: Access destination type. Valid values: net|template|instance|resourcegroup|tag|region
        :type DestType: str
        :param RuleAction: The action that Cloud Firewall performs on the traffic. Valid values:
accept: allow
drop: deny
        :type RuleAction: str
        :param Description: Description
        :type Description: str
        :param OrderIndex: Rule priority. -1: lowest; 1: highest
        :type OrderIndex: str
        :param Protocol: Protocol. TCP/UDP/ICMP/ANY
Note: This field may return `null`, indicating that no valid value was found.
        :type Protocol: str
        :param Port: The port to apply access control rules. Valid values:
-1/-1: all ports
80: port 80
Note: This field may return `null`, indicating that no valid value was found.
        :type Port: str
        :param ServiceTemplateId: Parameter template ID of port and protocol type; mutually exclusive with Protocol and Port
Note: This field may return `null`, indicating that no valid value was found.
        :type ServiceTemplateId: str
        :param Id: The unique ID of the rule
        :type Id: str
        :param Enable: Rule status. true: enabled; false: disabled
        :type Enable: str
        """
        self.SourceContent = None
        self.SourceType = None
        self.DestContent = None
        self.DestType = None
        self.RuleAction = None
        self.Description = None
        self.OrderIndex = None
        self.Protocol = None
        self.Port = None
        self.ServiceTemplateId = None
        self.Id = None
        self.Enable = None


    def _deserialize(self, params):
        self.SourceContent = params.get("SourceContent")
        self.SourceType = params.get("SourceType")
        self.DestContent = params.get("DestContent")
        self.DestType = params.get("DestType")
        self.RuleAction = params.get("RuleAction")
        self.Description = params.get("Description")
        self.OrderIndex = params.get("OrderIndex")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        self.ServiceTemplateId = params.get("ServiceTemplateId")
        self.Id = params.get("Id")
        self.Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SequenceData(AbstractModel):
    """Priority

    """

    def __init__(self):
        r"""
        :param Id: Rule ID
        :type Id: int
        :param OrderIndex: Rule priority before change
        :type OrderIndex: int
        :param NewOrderIndex: Rule priority after change
        :type NewOrderIndex: int
        """
        self.Id = None
        self.OrderIndex = None
        self.NewOrderIndex = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.OrderIndex = params.get("OrderIndex")
        self.NewOrderIndex = params.get("NewOrderIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetNatFwDnatRuleRequest(AbstractModel):
    """SetNatFwDnatRule request structure.

    """

    def __init__(self):
        r"""
        :param Mode: 0: Create new; 1: Use existing
        :type Mode: int
        :param OperationType: Operation type. Valid values: add, del, and modify.
        :type OperationType: str
        :param CfwInstance: Firewall instance ID. This field is required.
        :type CfwInstance: str
        :param AddOrDelDnatRules: List of added/deleted DNAT rules
        :type AddOrDelDnatRules: list of CfwNatDnatRule
        :param OriginDnat: Original DNAT rule before change
        :type OriginDnat: :class:`tencentcloud.cfw.v20190904.models.CfwNatDnatRule`
        :param NewDnat: New DNAT rule after change
        :type NewDnat: :class:`tencentcloud.cfw.v20190904.models.CfwNatDnatRule`
        """
        self.Mode = None
        self.OperationType = None
        self.CfwInstance = None
        self.AddOrDelDnatRules = None
        self.OriginDnat = None
        self.NewDnat = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        self.OperationType = params.get("OperationType")
        self.CfwInstance = params.get("CfwInstance")
        if params.get("AddOrDelDnatRules") is not None:
            self.AddOrDelDnatRules = []
            for item in params.get("AddOrDelDnatRules"):
                obj = CfwNatDnatRule()
                obj._deserialize(item)
                self.AddOrDelDnatRules.append(obj)
        if params.get("OriginDnat") is not None:
            self.OriginDnat = CfwNatDnatRule()
            self.OriginDnat._deserialize(params.get("OriginDnat"))
        if params.get("NewDnat") is not None:
            self.NewDnat = CfwNatDnatRule()
            self.NewDnat._deserialize(params.get("NewDnat"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetNatFwDnatRuleResponse(AbstractModel):
    """SetNatFwDnatRule response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetNatFwEipRequest(AbstractModel):
    """SetNatFwEip request structure.

    """

    def __init__(self):
        r"""
        :param OperationType: bind: bind EIP; unbind: unbind EIP; newAdd: add firewall EIP
        :type OperationType: str
        :param CfwInstance: Firewall instance ID
        :type CfwInstance: str
        :param EipList: This field is required when OperationType is "bind" or "unbind".
        :type EipList: list of str
        """
        self.OperationType = None
        self.CfwInstance = None
        self.EipList = None


    def _deserialize(self, params):
        self.OperationType = params.get("OperationType")
        self.CfwInstance = params.get("CfwInstance")
        self.EipList = params.get("EipList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetNatFwEipResponse(AbstractModel):
    """SetNatFwEip response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StaticInfo(AbstractModel):
    """Most frequent attacker statistics


    """

    def __init__(self):
        r"""
        :param Num: Number
        :type Num: int
        :param Port: Port
        :type Port: str
        :param Ip: IP
        :type Ip: str
        :param Address: Address
        :type Address: str
        :param InsID: Asset ID
        :type InsID: str
        :param InsName: Asset name
        :type InsName: str
        """
        self.Num = None
        self.Port = None
        self.Ip = None
        self.Address = None
        self.InsID = None
        self.InsName = None


    def _deserialize(self, params):
        self.Num = params.get("Num")
        self.Port = params.get("Port")
        self.Ip = params.get("Ip")
        self.Address = params.get("Address")
        self.InsID = params.get("InsID")
        self.InsName = params.get("InsName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopSecurityGroupRuleDispatchRequest(AbstractModel):
    """StopSecurityGroupRuleDispatch request structure.

    """

    def __init__(self):
        r"""
        :param StopType: Stops all if set to 1
        :type StopType: int
        """
        self.StopType = None


    def _deserialize(self, params):
        self.StopType = params.get("StopType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopSecurityGroupRuleDispatchResponse(AbstractModel):
    """StopSecurityGroupRuleDispatch response structure.

    """

    def __init__(self):
        r"""
        :param Status: true: operation successful; false: error
Note: This field may return `null`, indicating that no valid value was found.
        :type Status: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class SwitchListsData(AbstractModel):
    """Firewall status list

    """

    def __init__(self):
        r"""
        :param PublicIp: Public IP
Note: This field may return `null`, indicating that no valid value was found.
        :type PublicIp: str
        :param IntranetIp: Private IP
Note: This field may return `null`, indicating that no valid value was found.
        :type IntranetIp: str
        :param InstanceName: Instance name
Note: This field may return `null`, indicating that no valid value was found.
        :type InstanceName: str
        :param InstanceId: Instance ID
Note: This field may return `null`, indicating that no valid value was found.
        :type InstanceId: str
        :param AssetType: Asset type
        :type AssetType: str
        :param Area: Region
Note: This field may return `null`, indicating that no valid value was found.
        :type Area: str
        :param Switch: Firewall toggle
        :type Switch: int
        :param Id: ID value
        :type Id: int
        :param PublicIpType: Public IP type
Note: This field may return `null`, indicating that no valid value was found.
        :type PublicIpType: int
        :param PortTimes: Number of risky ports
Note: This field may return `null`, indicating that no valid value was found.
        :type PortTimes: int
        :param LastTime: Last scan time
Note: This field may return `null`, indicating that no valid value was found.
        :type LastTime: str
        :param ScanMode: Scan mode
Note: This field may return `null`, indicating that no valid value was found.
        :type ScanMode: str
        :param ScanStatus: Scan status
Note: This field may return `null`, indicating that no valid value was found.
        :type ScanStatus: int
        """
        self.PublicIp = None
        self.IntranetIp = None
        self.InstanceName = None
        self.InstanceId = None
        self.AssetType = None
        self.Area = None
        self.Switch = None
        self.Id = None
        self.PublicIpType = None
        self.PortTimes = None
        self.LastTime = None
        self.ScanMode = None
        self.ScanStatus = None


    def _deserialize(self, params):
        self.PublicIp = params.get("PublicIp")
        self.IntranetIp = params.get("IntranetIp")
        self.InstanceName = params.get("InstanceName")
        self.InstanceId = params.get("InstanceId")
        self.AssetType = params.get("AssetType")
        self.Area = params.get("Area")
        self.Switch = params.get("Switch")
        self.Id = params.get("Id")
        self.PublicIpType = params.get("PublicIpType")
        self.PortTimes = params.get("PortTimes")
        self.LastTime = params.get("LastTime")
        self.ScanMode = params.get("ScanMode")
        self.ScanStatus = params.get("ScanStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TLogInfo(AbstractModel):
    """Alert monitoring data

    """

    def __init__(self):
        r"""
        :param OutNum: Compromised servers
        :type OutNum: int
        :param HandleNum: Unhandled alerts
        :type HandleNum: int
        :param VulNum: Vulnerability attacks
        :type VulNum: int
        :param NetworkNum: Detected networks
        :type NetworkNum: int
        :param BanNum: Blocklist
        :type BanNum: int
        :param BruteForceNum: Brute force attacks
        :type BruteForceNum: int
        """
        self.OutNum = None
        self.HandleNum = None
        self.VulNum = None
        self.NetworkNum = None
        self.BanNum = None
        self.BruteForceNum = None


    def _deserialize(self, params):
        self.OutNum = params.get("OutNum")
        self.HandleNum = params.get("HandleNum")
        self.VulNum = params.get("VulNum")
        self.NetworkNum = params.get("NetworkNum")
        self.BanNum = params.get("BanNum")
        self.BruteForceNum = params.get("BruteForceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnHandleEvent(AbstractModel):
    """Unhandled event details

    """

    def __init__(self):
        r"""
        :param EventTableListStruct: Unhandled event type
        :type EventTableListStruct: list of UnHandleEventDetail
        :param BaseLineUser: 1: yes; 0: no
        :type BaseLineUser: int
        :param BaseLineInSwitch: 1: on; 0: off
        :type BaseLineInSwitch: int
        :param BaseLineOutSwitch: 1: on; 0: off
        :type BaseLineOutSwitch: int
        :param VpcFwCount: Number of inter-VPC firewall instances
Note: This field may return `null`, indicating that no valid value was found.
        :type VpcFwCount: int
        """
        self.EventTableListStruct = None
        self.BaseLineUser = None
        self.BaseLineInSwitch = None
        self.BaseLineOutSwitch = None
        self.VpcFwCount = None


    def _deserialize(self, params):
        if params.get("EventTableListStruct") is not None:
            self.EventTableListStruct = []
            for item in params.get("EventTableListStruct"):
                obj = UnHandleEventDetail()
                obj._deserialize(item)
                self.EventTableListStruct.append(obj)
        self.BaseLineUser = params.get("BaseLineUser")
        self.BaseLineInSwitch = params.get("BaseLineInSwitch")
        self.BaseLineOutSwitch = params.get("BaseLineOutSwitch")
        self.VpcFwCount = params.get("VpcFwCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnHandleEventDetail(AbstractModel):
    """Unhandled event statistics

    """

    def __init__(self):
        r"""
        :param EventName: Security event name
        :type EventName: str
        :param Total: Number of unhandled events
        :type Total: int
        """
        self.EventName = None
        self.Total = None


    def _deserialize(self, params):
        self.EventName = params.get("EventName")
        self.Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcDnsInfo(AbstractModel):
    """VPC DNS status of NAT firewall

    """

    def __init__(self):
        r"""
        :param VpcId: VPC ID
        :type VpcId: str
        :param VpcName: VPC name
        :type VpcName: str
        :param FwMode: NAT firewall mode. 0: Create new; 1: Use existing
        :type FwMode: int
        :param VpcIpv4Cidr: VPC IPv4 CIDR block (Classless Inter-Domain Routing)
        :type VpcIpv4Cidr: str
        :param DNSEip: Public EIP, which is the firewall DNS resolution address
        :type DNSEip: str
        :param NatInsId: NAT gateway ID
Note: This field may return `null`, indicating that no valid value was found.
        :type NatInsId: str
        :param NatInsName: NAT gateway name
Note: This field may return `null`, indicating that no valid value was found.
        :type NatInsName: str
        :param SwitchStatus: 0: off; 1: on
        :type SwitchStatus: int
        """
        self.VpcId = None
        self.VpcName = None
        self.FwMode = None
        self.VpcIpv4Cidr = None
        self.DNSEip = None
        self.NatInsId = None
        self.NatInsName = None
        self.SwitchStatus = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.FwMode = params.get("FwMode")
        self.VpcIpv4Cidr = params.get("VpcIpv4Cidr")
        self.DNSEip = params.get("DNSEip")
        self.NatInsId = params.get("NatInsId")
        self.NatInsName = params.get("NatInsName")
        self.SwitchStatus = params.get("SwitchStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        