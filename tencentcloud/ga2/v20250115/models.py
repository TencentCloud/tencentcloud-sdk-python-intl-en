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


class AcceleratorAreas(AbstractModel):
    r"""Acceleration region information

    """

    def __init__(self):
        r"""
        :param _AccelerateRegion: <p>Acceleration region.</p>
        :type AccelerateRegion: str
        :param _Bandwidth: <p>Bandwidth.</p>
        :type Bandwidth: int
        :param _IspType: <p>Supports &#39;BGP&#39;, &#39;QUALITY_BGP&#39;, and &#39;STATIC_IP&#39;. Default: BGP.</p><p>Enumeration values:</p><ul><li>BGP: BGP</li><li>STATIC_IP: triple-network</li><li>QUALITY_BGP: dedicated BGP</li></ul>
        :type IspType: str
        :param _IpVersion: <p>Only IPv4 is supported, and IPv4 is selected by default.</p>
        :type IpVersion: str
        :param _AcceleratorAreaId: <p>Acceleration region ID.</p>
        :type AcceleratorAreaId: str
        :param _IpAddress: <p>IP.</p>
        :type IpAddress: list of str
        :param _IpAddressInfoSet: <p>IP information.</p>
        :type IpAddressInfoSet: list of IpAddressInfoSet
        """
        self._AccelerateRegion = None
        self._Bandwidth = None
        self._IspType = None
        self._IpVersion = None
        self._AcceleratorAreaId = None
        self._IpAddress = None
        self._IpAddressInfoSet = None

    @property
    def AccelerateRegion(self):
        r"""<p>Acceleration region.</p>
        :rtype: str
        """
        return self._AccelerateRegion

    @AccelerateRegion.setter
    def AccelerateRegion(self, AccelerateRegion):
        self._AccelerateRegion = AccelerateRegion

    @property
    def Bandwidth(self):
        r"""<p>Bandwidth.</p>
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def IspType(self):
        r"""<p>Supports &#39;BGP&#39;, &#39;QUALITY_BGP&#39;, and &#39;STATIC_IP&#39;. Default: BGP.</p><p>Enumeration values:</p><ul><li>BGP: BGP</li><li>STATIC_IP: triple-network</li><li>QUALITY_BGP: dedicated BGP</li></ul>
        :rtype: str
        """
        return self._IspType

    @IspType.setter
    def IspType(self, IspType):
        self._IspType = IspType

    @property
    def IpVersion(self):
        r"""<p>Only IPv4 is supported, and IPv4 is selected by default.</p>
        :rtype: str
        """
        return self._IpVersion

    @IpVersion.setter
    def IpVersion(self, IpVersion):
        self._IpVersion = IpVersion

    @property
    def AcceleratorAreaId(self):
        r"""<p>Acceleration region ID.</p>
        :rtype: str
        """
        return self._AcceleratorAreaId

    @AcceleratorAreaId.setter
    def AcceleratorAreaId(self, AcceleratorAreaId):
        self._AcceleratorAreaId = AcceleratorAreaId

    @property
    def IpAddress(self):
        r"""<p>IP.</p>
        :rtype: list of str
        """
        return self._IpAddress

    @IpAddress.setter
    def IpAddress(self, IpAddress):
        self._IpAddress = IpAddress

    @property
    def IpAddressInfoSet(self):
        r"""<p>IP information.</p>
        :rtype: list of IpAddressInfoSet
        """
        return self._IpAddressInfoSet

    @IpAddressInfoSet.setter
    def IpAddressInfoSet(self, IpAddressInfoSet):
        self._IpAddressInfoSet = IpAddressInfoSet


    def _deserialize(self, params):
        self._AccelerateRegion = params.get("AccelerateRegion")
        self._Bandwidth = params.get("Bandwidth")
        self._IspType = params.get("IspType")
        self._IpVersion = params.get("IpVersion")
        self._AcceleratorAreaId = params.get("AcceleratorAreaId")
        self._IpAddress = params.get("IpAddress")
        if params.get("IpAddressInfoSet") is not None:
            self._IpAddressInfoSet = []
            for item in params.get("IpAddressInfoSet"):
                obj = IpAddressInfoSet()
                obj._deserialize(item)
                self._IpAddressInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AcceleratorRegionSet(AbstractModel):
    r"""Acceleration region info

    """

    def __init__(self):
        r"""
        :param _Name: <p>Chinese Name of Region.</p>
        :type Name: str
        :param _IsAvailable: <p>Whether available; 0: unavailable, 1: available.</p>
        :type IsAvailable: int
        :param _Region: <p>Regional information.</p>
        :type Region: str
        :param _AreaName: <p>Zone name.</p>
        :type AreaName: str
        :param _IsChinaMainland: <p>Whether it is a China region.</p>
        :type IsChinaMainland: int
        :param _SupportIspType: <p>Support the IspType type.</p>
        :type SupportIspType: list of str
        :param _IsTencentRegion: <p>Whether it is a Tencent region.</p>
        :type IsTencentRegion: int
        """
        self._Name = None
        self._IsAvailable = None
        self._Region = None
        self._AreaName = None
        self._IsChinaMainland = None
        self._SupportIspType = None
        self._IsTencentRegion = None

    @property
    def Name(self):
        r"""<p>Chinese Name of Region.</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IsAvailable(self):
        r"""<p>Whether available; 0: unavailable, 1: available.</p>
        :rtype: int
        """
        return self._IsAvailable

    @IsAvailable.setter
    def IsAvailable(self, IsAvailable):
        self._IsAvailable = IsAvailable

    @property
    def Region(self):
        r"""<p>Regional information.</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AreaName(self):
        r"""<p>Zone name.</p>
        :rtype: str
        """
        return self._AreaName

    @AreaName.setter
    def AreaName(self, AreaName):
        self._AreaName = AreaName

    @property
    def IsChinaMainland(self):
        r"""<p>Whether it is a China region.</p>
        :rtype: int
        """
        return self._IsChinaMainland

    @IsChinaMainland.setter
    def IsChinaMainland(self, IsChinaMainland):
        self._IsChinaMainland = IsChinaMainland

    @property
    def SupportIspType(self):
        r"""<p>Support the IspType type.</p>
        :rtype: list of str
        """
        return self._SupportIspType

    @SupportIspType.setter
    def SupportIspType(self, SupportIspType):
        self._SupportIspType = SupportIspType

    @property
    def IsTencentRegion(self):
        r"""<p>Whether it is a Tencent region.</p>
        :rtype: int
        """
        return self._IsTencentRegion

    @IsTencentRegion.setter
    def IsTencentRegion(self, IsTencentRegion):
        self._IsTencentRegion = IsTencentRegion


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._IsAvailable = params.get("IsAvailable")
        self._Region = params.get("Region")
        self._AreaName = params.get("AreaName")
        self._IsChinaMainland = params.get("IsChinaMainland")
        self._SupportIspType = params.get("SupportIspType")
        self._IsTencentRegion = params.get("IsTencentRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclEntries(AbstractModel):
    r"""Acl information

    """

    def __init__(self):
        r"""
        :param _Protocol: <p>Protocol.</p><p>Input limits: supports configuration of 'TCP', 'UDP', 'ALL';</p>
        :type Protocol: str
        :param _Port: <p>Port.</p>
        :type Port: str
        :param _SourceCidrBlock: <p>IP range.</p>
        :type SourceCidrBlock: str
        :param _Policy: <p>Execute action.</p><p>Input parameter limit: can be configured with 'ACCEPT' and 'DROP';</p>
        :type Policy: str
        :param _Description: <p>Description. Maximum length cannot exceed 100 bytes.</p>
        :type Description: str
        """
        self._Protocol = None
        self._Port = None
        self._SourceCidrBlock = None
        self._Policy = None
        self._Description = None

    @property
    def Protocol(self):
        r"""<p>Protocol.</p><p>Input limits: supports configuration of 'TCP', 'UDP', 'ALL';</p>
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        r"""<p>Port.</p>
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def SourceCidrBlock(self):
        r"""<p>IP range.</p>
        :rtype: str
        """
        return self._SourceCidrBlock

    @SourceCidrBlock.setter
    def SourceCidrBlock(self, SourceCidrBlock):
        self._SourceCidrBlock = SourceCidrBlock

    @property
    def Policy(self):
        r"""<p>Execute action.</p><p>Input parameter limit: can be configured with 'ACCEPT' and 'DROP';</p>
        :rtype: str
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def Description(self):
        r"""<p>Description. Maximum length cannot exceed 100 bytes.</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._SourceCidrBlock = params.get("SourceCidrBlock")
        self._Policy = params.get("Policy")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccelerateAreasRequest(AbstractModel):
    r"""CreateAccelerateAreas request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>Global acceleration instance ID.</p>
        :type GlobalAcceleratorId: str
        :param _AcceleratorAreas: <p>Acceleration region info. Up to 10 acceleration region groups can be created at a time.</p>
        :type AcceleratorAreas: list of AcceleratorAreas
        """
        self._GlobalAcceleratorId = None
        self._AcceleratorAreas = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Global acceleration instance ID.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def AcceleratorAreas(self):
        r"""<p>Acceleration region info. Up to 10 acceleration region groups can be created at a time.</p>
        :rtype: list of AcceleratorAreas
        """
        return self._AcceleratorAreas

    @AcceleratorAreas.setter
    def AcceleratorAreas(self, AcceleratorAreas):
        self._AcceleratorAreas = AcceleratorAreas


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        if params.get("AcceleratorAreas") is not None:
            self._AcceleratorAreas = []
            for item in params.get("AcceleratorAreas"):
                obj = AcceleratorAreas()
                obj._deserialize(item)
                self._AcceleratorAreas.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccelerateAreasResponse(AbstractModel):
    r"""CreateAccelerateAreas response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>Asynchronous task ID.</p>
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>Asynchronous task ID.</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateEndpointGroupRequest(AbstractModel):
    r"""CreateEndpointGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>Global acceleration instance ID.</p>
        :type GlobalAcceleratorId: str
        :param _ListenerId: <p>Listener ID.</p>
        :type ListenerId: str
        :param _EndpointGroupType: <p>Node group type.</p><p>Enumeration values:</p><ul><li>VIRTUAL: custom endpoint node group</li><li>DEFAULT: default terminal node group</li></ul>
        :type EndpointGroupType: str
        :param _EndpointGroupConfiguration: <p>Terminal node group configuration.</p>
        :type EndpointGroupConfiguration: :class:`tencentcloud.ga2.v20250115.models.EndpointGroupConfiguration`
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._EndpointGroupType = None
        self._EndpointGroupConfiguration = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Global acceleration instance ID.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""<p>Listener ID.</p>
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def EndpointGroupType(self):
        r"""<p>Node group type.</p><p>Enumeration values:</p><ul><li>VIRTUAL: custom endpoint node group</li><li>DEFAULT: default terminal node group</li></ul>
        :rtype: str
        """
        return self._EndpointGroupType

    @EndpointGroupType.setter
    def EndpointGroupType(self, EndpointGroupType):
        self._EndpointGroupType = EndpointGroupType

    @property
    def EndpointGroupConfiguration(self):
        r"""<p>Terminal node group configuration.</p>
        :rtype: :class:`tencentcloud.ga2.v20250115.models.EndpointGroupConfiguration`
        """
        return self._EndpointGroupConfiguration

    @EndpointGroupConfiguration.setter
    def EndpointGroupConfiguration(self, EndpointGroupConfiguration):
        self._EndpointGroupConfiguration = EndpointGroupConfiguration


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._EndpointGroupType = params.get("EndpointGroupType")
        if params.get("EndpointGroupConfiguration") is not None:
            self._EndpointGroupConfiguration = EndpointGroupConfiguration()
            self._EndpointGroupConfiguration._deserialize(params.get("EndpointGroupConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEndpointGroupResponse(AbstractModel):
    r"""CreateEndpointGroup response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>Task ID.</p>
        :type TaskId: str
        :param _EndpointGroupId: <p>Instance ID of the terminal node group.</p>
        :type EndpointGroupId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._EndpointGroupId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>Task ID.</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def EndpointGroupId(self):
        r"""<p>Instance ID of the terminal node group.</p>
        :rtype: str
        """
        return self._EndpointGroupId

    @EndpointGroupId.setter
    def EndpointGroupId(self, EndpointGroupId):
        self._EndpointGroupId = EndpointGroupId

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
        self._TaskId = params.get("TaskId")
        self._EndpointGroupId = params.get("EndpointGroupId")
        self._RequestId = params.get("RequestId")


class CreateForwardingPolicyRequest(AbstractModel):
    r"""CreateForwardingPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>Global acceleration instance ID.</p>
        :type GlobalAcceleratorId: str
        :param _ListenerId: <p>Listener ID.</p>
        :type ListenerId: str
        :param _Host: <p>Domain name.</p><p>Parameter format: format, must meet the regular expression: ^(<a href="?:[a-z0-9-]{0,61}[a-z0-9]">a-z0-9</a>?.)+[a-z]{2,}$</p><p>Input limit: length range is 1-80.</p>
        :type Host: str
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._Host = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Global acceleration instance ID.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""<p>Listener ID.</p>
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Host(self):
        r"""<p>Domain name.</p><p>Parameter format: format, must meet the regular expression: ^(<a href="?:[a-z0-9-]{0,61}[a-z0-9]">a-z0-9</a>?.)+[a-z]{2,}$</p><p>Input limit: length range is 1-80.</p>
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateForwardingPolicyResponse(AbstractModel):
    r"""CreateForwardingPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>Asynchronous task ID.</p>
        :type TaskId: str
        :param _ForwardingPolicyId: <p>Layer-7 forwarding policy ID.</p>
        :type ForwardingPolicyId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._ForwardingPolicyId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>Asynchronous task ID.</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ForwardingPolicyId(self):
        r"""<p>Layer-7 forwarding policy ID.</p>
        :rtype: str
        """
        return self._ForwardingPolicyId

    @ForwardingPolicyId.setter
    def ForwardingPolicyId(self, ForwardingPolicyId):
        self._ForwardingPolicyId = ForwardingPolicyId

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
        self._TaskId = params.get("TaskId")
        self._ForwardingPolicyId = params.get("ForwardingPolicyId")
        self._RequestId = params.get("RequestId")


class CreateForwardingRuleRequest(AbstractModel):
    r"""CreateForwardingRule request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>Global acceleration instance ID.</p>
        :type GlobalAcceleratorId: str
        :param _ListenerId: <p>Listener ID.</p>
        :type ListenerId: str
        :param _ForwardingPolicyId: <p>Policy ID.</p>
        :type ForwardingPolicyId: str
        :param _RuleConditions: <p>Layer 7 forwarding rule conditional information.</p><p>Array length cannot exceed 1.</p>
        :type RuleConditions: list of RuleCondition
        :param _RuleActions: <p>Layer 7 forwarding rule behavior information.</p><p>The length of the array cannot exceed 1.</p>
        :type RuleActions: list of RuleAction
        :param _OriginHeaders: <p>Origin-pull Header information.</p><p>The maximum length of the array cannot exceed 5. This field is required when RuleActions.RuleActionType is ForwardGroup.</p>
        :type OriginHeaders: list of OriginHeader
        :param _EnableOriginSni: <p>Whether origin-pull sni is enabled.</p><p>Default value: False</p><p>This field is required when RuleActions.RuleActionType is ForwardGroup.</p>
        :type EnableOriginSni: bool
        :param _OriginSni: <p>Origin sni.</p><p>Input parameter limit: length cannot exceed 80.</p><p>This field is required when EnableOriginSni is True. This field is required when RuleActions.RuleActionType is ForwardGroup.</p>
        :type OriginSni: str
        :param _OriginHost: <p>Origin-pull host.</p><p>Input parameter limit: length not exceeding 80.</p><p>This field is required when RuleActions.RuleActionType is ForwardGroup.</p>
        :type OriginHost: str
        :param _ResponseHeaders: <p>Origin response headers</p><p>Array length not exceeding 5. An empty array can be passed, representing configuration clearing.</p>
        :type ResponseHeaders: list of ResponseHeaders
        :param _HideResponseHeaders: <p>Delete origin server response headers</p><p>Array length not exceeding 5. An empty array can be passed, representing configuration clearing.</p>
        :type HideResponseHeaders: list of HideResponseHeaders
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._ForwardingPolicyId = None
        self._RuleConditions = None
        self._RuleActions = None
        self._OriginHeaders = None
        self._EnableOriginSni = None
        self._OriginSni = None
        self._OriginHost = None
        self._ResponseHeaders = None
        self._HideResponseHeaders = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Global acceleration instance ID.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""<p>Listener ID.</p>
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ForwardingPolicyId(self):
        r"""<p>Policy ID.</p>
        :rtype: str
        """
        return self._ForwardingPolicyId

    @ForwardingPolicyId.setter
    def ForwardingPolicyId(self, ForwardingPolicyId):
        self._ForwardingPolicyId = ForwardingPolicyId

    @property
    def RuleConditions(self):
        r"""<p>Layer 7 forwarding rule conditional information.</p><p>Array length cannot exceed 1.</p>
        :rtype: list of RuleCondition
        """
        return self._RuleConditions

    @RuleConditions.setter
    def RuleConditions(self, RuleConditions):
        self._RuleConditions = RuleConditions

    @property
    def RuleActions(self):
        r"""<p>Layer 7 forwarding rule behavior information.</p><p>The length of the array cannot exceed 1.</p>
        :rtype: list of RuleAction
        """
        return self._RuleActions

    @RuleActions.setter
    def RuleActions(self, RuleActions):
        self._RuleActions = RuleActions

    @property
    def OriginHeaders(self):
        r"""<p>Origin-pull Header information.</p><p>The maximum length of the array cannot exceed 5. This field is required when RuleActions.RuleActionType is ForwardGroup.</p>
        :rtype: list of OriginHeader
        """
        return self._OriginHeaders

    @OriginHeaders.setter
    def OriginHeaders(self, OriginHeaders):
        self._OriginHeaders = OriginHeaders

    @property
    def EnableOriginSni(self):
        r"""<p>Whether origin-pull sni is enabled.</p><p>Default value: False</p><p>This field is required when RuleActions.RuleActionType is ForwardGroup.</p>
        :rtype: bool
        """
        return self._EnableOriginSni

    @EnableOriginSni.setter
    def EnableOriginSni(self, EnableOriginSni):
        self._EnableOriginSni = EnableOriginSni

    @property
    def OriginSni(self):
        r"""<p>Origin sni.</p><p>Input parameter limit: length cannot exceed 80.</p><p>This field is required when EnableOriginSni is True. This field is required when RuleActions.RuleActionType is ForwardGroup.</p>
        :rtype: str
        """
        return self._OriginSni

    @OriginSni.setter
    def OriginSni(self, OriginSni):
        self._OriginSni = OriginSni

    @property
    def OriginHost(self):
        r"""<p>Origin-pull host.</p><p>Input parameter limit: length not exceeding 80.</p><p>This field is required when RuleActions.RuleActionType is ForwardGroup.</p>
        :rtype: str
        """
        return self._OriginHost

    @OriginHost.setter
    def OriginHost(self, OriginHost):
        self._OriginHost = OriginHost

    @property
    def ResponseHeaders(self):
        r"""<p>Origin response headers</p><p>Array length not exceeding 5. An empty array can be passed, representing configuration clearing.</p>
        :rtype: list of ResponseHeaders
        """
        return self._ResponseHeaders

    @ResponseHeaders.setter
    def ResponseHeaders(self, ResponseHeaders):
        self._ResponseHeaders = ResponseHeaders

    @property
    def HideResponseHeaders(self):
        r"""<p>Delete origin server response headers</p><p>Array length not exceeding 5. An empty array can be passed, representing configuration clearing.</p>
        :rtype: list of HideResponseHeaders
        """
        return self._HideResponseHeaders

    @HideResponseHeaders.setter
    def HideResponseHeaders(self, HideResponseHeaders):
        self._HideResponseHeaders = HideResponseHeaders


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._ForwardingPolicyId = params.get("ForwardingPolicyId")
        if params.get("RuleConditions") is not None:
            self._RuleConditions = []
            for item in params.get("RuleConditions"):
                obj = RuleCondition()
                obj._deserialize(item)
                self._RuleConditions.append(obj)
        if params.get("RuleActions") is not None:
            self._RuleActions = []
            for item in params.get("RuleActions"):
                obj = RuleAction()
                obj._deserialize(item)
                self._RuleActions.append(obj)
        if params.get("OriginHeaders") is not None:
            self._OriginHeaders = []
            for item in params.get("OriginHeaders"):
                obj = OriginHeader()
                obj._deserialize(item)
                self._OriginHeaders.append(obj)
        self._EnableOriginSni = params.get("EnableOriginSni")
        self._OriginSni = params.get("OriginSni")
        self._OriginHost = params.get("OriginHost")
        if params.get("ResponseHeaders") is not None:
            self._ResponseHeaders = []
            for item in params.get("ResponseHeaders"):
                obj = ResponseHeaders()
                obj._deserialize(item)
                self._ResponseHeaders.append(obj)
        if params.get("HideResponseHeaders") is not None:
            self._HideResponseHeaders = []
            for item in params.get("HideResponseHeaders"):
                obj = HideResponseHeaders()
                obj._deserialize(item)
                self._HideResponseHeaders.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateForwardingRuleResponse(AbstractModel):
    r"""CreateForwardingRule response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>Asynchronous task ID.</p>
        :type TaskId: str
        :param _ForwardingRuleId: <p>Layer 7 forwarding rule ID.</p>
        :type ForwardingRuleId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._ForwardingRuleId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>Asynchronous task ID.</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ForwardingRuleId(self):
        r"""<p>Layer 7 forwarding rule ID.</p>
        :rtype: str
        """
        return self._ForwardingRuleId

    @ForwardingRuleId.setter
    def ForwardingRuleId(self, ForwardingRuleId):
        self._ForwardingRuleId = ForwardingRuleId

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
        self._TaskId = params.get("TaskId")
        self._ForwardingRuleId = params.get("ForwardingRuleId")
        self._RequestId = params.get("RequestId")


class CreateGlobalAcceleratorAccessLogRequest(AbstractModel):
    r"""CreateGlobalAcceleratorAccessLog request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>Unique Id of the sample GA</p>
        :type GlobalAcceleratorId: str
        :param _ListenerId: <p>Listener Id</p>
        :type ListenerId: str
        :param _EndpointGroupId: <p>Terminal node group Id</p>
        :type EndpointGroupId: str
        :param _CloudRegion: <p>Logset region</p>
        :type CloudRegion: str
        :param _CloudLogId: <p>Log topic Id</p>
        :type CloudLogId: str
        :param _CloudLogSetId: <p>Log Set Id</p>
        :type CloudLogSetId: str
        :param _FieldKeys: <p>Specify data collection fields</p><p>Enumeration values:</p><ul><li>session_time: Layer 4, session duration</li><li>upstream_bytes_received: Layer 4 and Layer 7, number of bytes received from the terminal node</li><li>upstream_bytes_sent: Layer 4 and Layer 7, number of bytes sent to the terminal node</li><li>request_method: Layer 7, GET/POST</li><li>scheme: Layer 7, http/https</li><li>request_uri: Layer 7, uri of the client's raw request</li><li>uri: Layer 7, uri of the current request</li><li>host: Layer 7, domain name accessed by the client (Layer 7)</li><li>remote_user: Layer 7, userName for basic authentication ("-" when unauthenticated)</li><li>http_user_agent: Layer 7, client browser identification</li><li>http_referer: Layer 7, request source URL ("-" when accessed directly from the address bar)</li><li>http_x_forwarded_for: Layer 7, records the client's original IP and the proxy server IP chain it transited</li><li>content_type: Layer 7, content_type</li><li>body_bytes_sent: Layer 7, http body size sent to the client, excluding the header</li><li>request_time: Layer 7, total time from receiving the first byte of the client request to sending the last byte of the response (unit: seconds)</li><li>sent_http_content_type: Layer 7, response content type</li><li>upstream_header_time: Layer 7, arrival time of the terminal node's response header</li><li>upstream_response_length: Layer 7, length of the response body returned by the terminal node</li><li>upstream_response_time: Layer 7, complete response time of the terminal node</li><li>upstream_status: Layer 7, http status code returned by the terminal node</li></ul>
        :type FieldKeys: list of str
        :param _FlowLogDescription: <p>Log description</p>
        :type FlowLogDescription: str
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._EndpointGroupId = None
        self._CloudRegion = None
        self._CloudLogId = None
        self._CloudLogSetId = None
        self._FieldKeys = None
        self._FlowLogDescription = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Unique Id of the sample GA</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""<p>Listener Id</p>
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def EndpointGroupId(self):
        r"""<p>Terminal node group Id</p>
        :rtype: str
        """
        return self._EndpointGroupId

    @EndpointGroupId.setter
    def EndpointGroupId(self, EndpointGroupId):
        self._EndpointGroupId = EndpointGroupId

    @property
    def CloudRegion(self):
        r"""<p>Logset region</p>
        :rtype: str
        """
        return self._CloudRegion

    @CloudRegion.setter
    def CloudRegion(self, CloudRegion):
        self._CloudRegion = CloudRegion

    @property
    def CloudLogId(self):
        r"""<p>Log topic Id</p>
        :rtype: str
        """
        return self._CloudLogId

    @CloudLogId.setter
    def CloudLogId(self, CloudLogId):
        self._CloudLogId = CloudLogId

    @property
    def CloudLogSetId(self):
        r"""<p>Log Set Id</p>
        :rtype: str
        """
        return self._CloudLogSetId

    @CloudLogSetId.setter
    def CloudLogSetId(self, CloudLogSetId):
        self._CloudLogSetId = CloudLogSetId

    @property
    def FieldKeys(self):
        r"""<p>Specify data collection fields</p><p>Enumeration values:</p><ul><li>session_time: Layer 4, session duration</li><li>upstream_bytes_received: Layer 4 and Layer 7, number of bytes received from the terminal node</li><li>upstream_bytes_sent: Layer 4 and Layer 7, number of bytes sent to the terminal node</li><li>request_method: Layer 7, GET/POST</li><li>scheme: Layer 7, http/https</li><li>request_uri: Layer 7, uri of the client's raw request</li><li>uri: Layer 7, uri of the current request</li><li>host: Layer 7, domain name accessed by the client (Layer 7)</li><li>remote_user: Layer 7, userName for basic authentication ("-" when unauthenticated)</li><li>http_user_agent: Layer 7, client browser identification</li><li>http_referer: Layer 7, request source URL ("-" when accessed directly from the address bar)</li><li>http_x_forwarded_for: Layer 7, records the client's original IP and the proxy server IP chain it transited</li><li>content_type: Layer 7, content_type</li><li>body_bytes_sent: Layer 7, http body size sent to the client, excluding the header</li><li>request_time: Layer 7, total time from receiving the first byte of the client request to sending the last byte of the response (unit: seconds)</li><li>sent_http_content_type: Layer 7, response content type</li><li>upstream_header_time: Layer 7, arrival time of the terminal node's response header</li><li>upstream_response_length: Layer 7, length of the response body returned by the terminal node</li><li>upstream_response_time: Layer 7, complete response time of the terminal node</li><li>upstream_status: Layer 7, http status code returned by the terminal node</li></ul>
        :rtype: list of str
        """
        return self._FieldKeys

    @FieldKeys.setter
    def FieldKeys(self, FieldKeys):
        self._FieldKeys = FieldKeys

    @property
    def FlowLogDescription(self):
        r"""<p>Log description</p>
        :rtype: str
        """
        return self._FlowLogDescription

    @FlowLogDescription.setter
    def FlowLogDescription(self, FlowLogDescription):
        self._FlowLogDescription = FlowLogDescription


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._EndpointGroupId = params.get("EndpointGroupId")
        self._CloudRegion = params.get("CloudRegion")
        self._CloudLogId = params.get("CloudLogId")
        self._CloudLogSetId = params.get("CloudLogSetId")
        self._FieldKeys = params.get("FieldKeys")
        self._FlowLogDescription = params.get("FlowLogDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGlobalAcceleratorAccessLogResponse(AbstractModel):
    r"""CreateGlobalAcceleratorAccessLog response structure.

    """

    def __init__(self):
        r"""
        :param _LogPushTaskId: <p>Log Task Unique Id</p>
        :type LogPushTaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LogPushTaskId = None
        self._RequestId = None

    @property
    def LogPushTaskId(self):
        r"""<p>Log Task Unique Id</p>
        :rtype: str
        """
        return self._LogPushTaskId

    @LogPushTaskId.setter
    def LogPushTaskId(self, LogPushTaskId):
        self._LogPushTaskId = LogPushTaskId

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
        self._LogPushTaskId = params.get("LogPushTaskId")
        self._RequestId = params.get("RequestId")


class CreateGlobalAcceleratorAclPolicyRequest(AbstractModel):
    r"""CreateGlobalAcceleratorAclPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>Global acceleration instance ID.</p>
        :type GlobalAcceleratorId: str
        :param _DefaultAction: <p>Default behavior.</p><p>Enumeration values:</p><ul><li>ACCEPT: Permit all traffic on the access channel by default</li><li>DROP: Deny all traffic on the access channel by default</li></ul>
        :type DefaultAction: str
        """
        self._GlobalAcceleratorId = None
        self._DefaultAction = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Global acceleration instance ID.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def DefaultAction(self):
        r"""<p>Default behavior.</p><p>Enumeration values:</p><ul><li>ACCEPT: Permit all traffic on the access channel by default</li><li>DROP: Deny all traffic on the access channel by default</li></ul>
        :rtype: str
        """
        return self._DefaultAction

    @DefaultAction.setter
    def DefaultAction(self, DefaultAction):
        self._DefaultAction = DefaultAction


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._DefaultAction = params.get("DefaultAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGlobalAcceleratorAclPolicyResponse(AbstractModel):
    r"""CreateGlobalAcceleratorAclPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>Asynchronous task ID.</p>
        :type TaskId: str
        :param _GlobalAcceleratorAclPolicyId: <p>Access control policy ID.</p>
        :type GlobalAcceleratorAclPolicyId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._GlobalAcceleratorAclPolicyId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>Asynchronous task ID.</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def GlobalAcceleratorAclPolicyId(self):
        r"""<p>Access control policy ID.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorAclPolicyId

    @GlobalAcceleratorAclPolicyId.setter
    def GlobalAcceleratorAclPolicyId(self, GlobalAcceleratorAclPolicyId):
        self._GlobalAcceleratorAclPolicyId = GlobalAcceleratorAclPolicyId

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
        self._TaskId = params.get("TaskId")
        self._GlobalAcceleratorAclPolicyId = params.get("GlobalAcceleratorAclPolicyId")
        self._RequestId = params.get("RequestId")


class CreateGlobalAcceleratorAclRuleRequest(AbstractModel):
    r"""CreateGlobalAcceleratorAclRule request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: Global acceleration instance ID.
        :type GlobalAcceleratorId: str
        :param _GlobalAcceleratorAclPolicyId: Security policy ID
        :type GlobalAcceleratorAclPolicyId: str
        :param _AclEntries: Acl information.
        :type AclEntries: list of AclEntries
        """
        self._GlobalAcceleratorId = None
        self._GlobalAcceleratorAclPolicyId = None
        self._AclEntries = None

    @property
    def GlobalAcceleratorId(self):
        r"""Global acceleration instance ID.
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def GlobalAcceleratorAclPolicyId(self):
        r"""Security policy ID
        :rtype: str
        """
        return self._GlobalAcceleratorAclPolicyId

    @GlobalAcceleratorAclPolicyId.setter
    def GlobalAcceleratorAclPolicyId(self, GlobalAcceleratorAclPolicyId):
        self._GlobalAcceleratorAclPolicyId = GlobalAcceleratorAclPolicyId

    @property
    def AclEntries(self):
        r"""Acl information.
        :rtype: list of AclEntries
        """
        return self._AclEntries

    @AclEntries.setter
    def AclEntries(self, AclEntries):
        self._AclEntries = AclEntries


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._GlobalAcceleratorAclPolicyId = params.get("GlobalAcceleratorAclPolicyId")
        if params.get("AclEntries") is not None:
            self._AclEntries = []
            for item in params.get("AclEntries"):
                obj = AclEntries()
                obj._deserialize(item)
                self._AclEntries.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGlobalAcceleratorAclRuleResponse(AbstractModel):
    r"""CreateGlobalAcceleratorAclRule response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Asynchronous task ID.
        :type TaskId: str
        :param _GlobalAcceleratorAclRuleIds: ACL rule ID.
        :type GlobalAcceleratorAclRuleIds: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._GlobalAcceleratorAclRuleIds = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Asynchronous task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def GlobalAcceleratorAclRuleIds(self):
        r"""ACL rule ID.
        :rtype: list of str
        """
        return self._GlobalAcceleratorAclRuleIds

    @GlobalAcceleratorAclRuleIds.setter
    def GlobalAcceleratorAclRuleIds(self, GlobalAcceleratorAclRuleIds):
        self._GlobalAcceleratorAclRuleIds = GlobalAcceleratorAclRuleIds

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
        self._TaskId = params.get("TaskId")
        self._GlobalAcceleratorAclRuleIds = params.get("GlobalAcceleratorAclRuleIds")
        self._RequestId = params.get("RequestId")


class CreateGlobalAcceleratorRequest(AbstractModel):
    r"""CreateGlobalAccelerator request structure.

    """

    def __init__(self):
        r"""
        :param _Name: <p>Name.</p><p>Parameter format: starting with a letter or Chinese characters, 2–128 characters in length, supporting letters, digits, Chinese characters, . - _</p>
        :type Name: str
        :param _InstanceChargeType: <p>Billing mode. PREPAID: prepaid mode, i.e., Monthly Subscription. POSTPAID: postpaid, i.e., pay-as-you-go. Default: POSTPAID. Currently, only pay-as-you-go is supported.</p>
        :type InstanceChargeType: str
        :param _Description: <p>Description.</p><p>Parameter format: should not exceed 100 characters.</p>
        :type Description: str
        :param _CrossBorderType: <p>Cross-border type; HighQuality: dedicated BGP-IP cross-border; Unicom: China Unicom Direct Connect cross-border.</p>
        :type CrossBorderType: str
        :param _CrossBorderPromiseFlag: <p>This Flag represents signing the cross-border service commitment. When using cross-border service, this field is required. True: represents signed.</p>
        :type CrossBorderPromiseFlag: bool
        :param _Tags: <p>Tag information.</p>
        :type Tags: list of Tag
        """
        self._Name = None
        self._InstanceChargeType = None
        self._Description = None
        self._CrossBorderType = None
        self._CrossBorderPromiseFlag = None
        self._Tags = None

    @property
    def Name(self):
        r"""<p>Name.</p><p>Parameter format: starting with a letter or Chinese characters, 2–128 characters in length, supporting letters, digits, Chinese characters, . - _</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def InstanceChargeType(self):
        r"""<p>Billing mode. PREPAID: prepaid mode, i.e., Monthly Subscription. POSTPAID: postpaid, i.e., pay-as-you-go. Default: POSTPAID. Currently, only pay-as-you-go is supported.</p>
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def Description(self):
        r"""<p>Description.</p><p>Parameter format: should not exceed 100 characters.</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CrossBorderType(self):
        r"""<p>Cross-border type; HighQuality: dedicated BGP-IP cross-border; Unicom: China Unicom Direct Connect cross-border.</p>
        :rtype: str
        """
        return self._CrossBorderType

    @CrossBorderType.setter
    def CrossBorderType(self, CrossBorderType):
        self._CrossBorderType = CrossBorderType

    @property
    def CrossBorderPromiseFlag(self):
        r"""<p>This Flag represents signing the cross-border service commitment. When using cross-border service, this field is required. True: represents signed.</p>
        :rtype: bool
        """
        return self._CrossBorderPromiseFlag

    @CrossBorderPromiseFlag.setter
    def CrossBorderPromiseFlag(self, CrossBorderPromiseFlag):
        self._CrossBorderPromiseFlag = CrossBorderPromiseFlag

    @property
    def Tags(self):
        r"""<p>Tag information.</p>
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._Description = params.get("Description")
        self._CrossBorderType = params.get("CrossBorderType")
        self._CrossBorderPromiseFlag = params.get("CrossBorderPromiseFlag")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGlobalAcceleratorResponse(AbstractModel):
    r"""CreateGlobalAccelerator response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>Task ID.</p>
        :type TaskId: str
        :param _GlobalAcceleratorId: <p>Global acceleration instance ID.</p>
        :type GlobalAcceleratorId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._GlobalAcceleratorId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>Task ID.</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Global acceleration instance ID.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

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
        self._TaskId = params.get("TaskId")
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._RequestId = params.get("RequestId")


class CreateListenerAdditionalCertRequest(AbstractModel):
    r"""CreateListenerAdditionalCert request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>Global acceleration instance ID.</p>
        :type GlobalAcceleratorId: str
        :param _ListenerId: <p>Listener ID.</p>
        :type ListenerId: str
        :param _AdditionalCertificates: <p>Certificate ID.</p><p>Currently, only server certificates can be added.</p>
        :type AdditionalCertificates: list of str
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._AdditionalCertificates = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Global acceleration instance ID.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""<p>Listener ID.</p>
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def AdditionalCertificates(self):
        r"""<p>Certificate ID.</p><p>Currently, only server certificates can be added.</p>
        :rtype: list of str
        """
        return self._AdditionalCertificates

    @AdditionalCertificates.setter
    def AdditionalCertificates(self, AdditionalCertificates):
        self._AdditionalCertificates = AdditionalCertificates


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._AdditionalCertificates = params.get("AdditionalCertificates")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateListenerAdditionalCertResponse(AbstractModel):
    r"""CreateListenerAdditionalCert response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>Task ID.</p>
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>Task ID.</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateListenerRequest(AbstractModel):
    r"""CreateListener request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>Global acceleration instance ID.</p>
        :type GlobalAcceleratorId: str
        :param _Name: <p>Name.</p><p>Parameter format: starting with a letter or Chinese characters, 2–128 characters in length, supporting letters, digits, Chinese characters, . - _</p>
        :type Name: str
        :param _PortRanges: <p>Port range.</p>
        :type PortRanges: :class:`tencentcloud.ga2.v20250115.models.PortRanges`
        :param _Description: <p>Description. Maximum length cannot exceed 100 characters.</p>
        :type Description: str
        :param _ListenerType: <p>Listening type, defaults to smart routing.</p><p>Enumeration values:</p><ul><li>Standard: Smart routing.</li></ul>
        :type ListenerType: str
        :param _Protocol: <p>Protocol. Default value: TCP. Supports configuration of 'TCP', 'UDP', 'HTTP', and 'HTTPS'.</p>
        :type Protocol: str
        :param _IdleTimeout: <p>Connection idle wait time.</p><p>1. For HTTP/HTTPS listener, the default value is 15, with a supported range of 1-60.<br>2. For TCP listener, the default value is 900, with a supported range of 10-900.<br>3. For UDP listener, the default value is 20, with a supported range of 10-20.</p>
        :type IdleTimeout: int
        :param _GetRealIpType: <p>Layer-4 source IP retrieval mode. Supports 'TOA', 'ProxyProtocol', and 'ProxyProtocolV2'.</p><p>This parameter can be filled in only when the Layer-4 source IP retrieval mode is enabled.</p>
        :type GetRealIpType: str
        :param _ClientAffinity: <p>Whether to enable session persistence. Supports configuration of 'Open' and 'Close'.</p><p>Enumeration values:</p><ul><li>Open: enable.</li><li>Close: disable.</li></ul><p>Only supported for layer-4 listeners. For layer-7 listeners, modification is not supported.</p>
        :type ClientAffinity: str
        :param _RequestTimeout: <p>Request timeout.</p><p>Value range: [1, 180]</p><p>Default value: 60</p><p>This parameter is configurable only for HTTPS listeners.</p>
        :type RequestTimeout: int
        :param _XForwardedForRealIp: <p>Whether to enable layer-7 source IP retrieval mode.</p>
        :type XForwardedForRealIp: bool
        :param _CertificationType: <p>Parsing method.</p><p>Enumeration values:</p><ul><li>UNIDIRECTIONAL: two-way.</li><li>U: one-way.</li></ul><p>For an HTTPS listener, this field is required.</p>
        :type CertificationType: str
        :param _CipherPolicyId: <p>Encryption algorithm kit. Supports configuration of 'tls_policy_1.0-2', 'tls_policy_1.1-2', 'tls_policy_1.2', 'tls_policy_1.2_strict', 'tls_policy_1.2_strict-1.3'.</p>
        :type CipherPolicyId: str
        :param _ServerCertificates: <p>Server certificate.</p><p>Input limit: currently only support importing one cert; to use multiple certs, use the cert api CreateListenerAdditionalCert to add other certs.</p><p>This field is required for HTTPS listeners.</p>
        :type ServerCertificates: list of str
        :param _ClientCaCertificates: <p>Client certificate.</p><p>Input limit: 1. Currently only support importing one cert. To use multiple certs, use the cert api CreateListenerAdditionalCert to add other certs. 2. The cert must be a CA certificate.</p><p>This field is required when HTTPS listener and mutual authentication are enabled.</p>
        :type ClientCaCertificates: list of str
        :param _HttpVersion: <p>HTTPS listener supports version selection</p><p>Enumeration values:</p><ul><li>HTTP/1.1: HTTP/1.1</li><li>HTTP/2: HTTP/2</li></ul>
        :type HttpVersion: str
        """
        self._GlobalAcceleratorId = None
        self._Name = None
        self._PortRanges = None
        self._Description = None
        self._ListenerType = None
        self._Protocol = None
        self._IdleTimeout = None
        self._GetRealIpType = None
        self._ClientAffinity = None
        self._RequestTimeout = None
        self._XForwardedForRealIp = None
        self._CertificationType = None
        self._CipherPolicyId = None
        self._ServerCertificates = None
        self._ClientCaCertificates = None
        self._HttpVersion = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Global acceleration instance ID.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def Name(self):
        r"""<p>Name.</p><p>Parameter format: starting with a letter or Chinese characters, 2–128 characters in length, supporting letters, digits, Chinese characters, . - _</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PortRanges(self):
        r"""<p>Port range.</p>
        :rtype: :class:`tencentcloud.ga2.v20250115.models.PortRanges`
        """
        return self._PortRanges

    @PortRanges.setter
    def PortRanges(self, PortRanges):
        self._PortRanges = PortRanges

    @property
    def Description(self):
        r"""<p>Description. Maximum length cannot exceed 100 characters.</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ListenerType(self):
        r"""<p>Listening type, defaults to smart routing.</p><p>Enumeration values:</p><ul><li>Standard: Smart routing.</li></ul>
        :rtype: str
        """
        return self._ListenerType

    @ListenerType.setter
    def ListenerType(self, ListenerType):
        self._ListenerType = ListenerType

    @property
    def Protocol(self):
        r"""<p>Protocol. Default value: TCP. Supports configuration of 'TCP', 'UDP', 'HTTP', and 'HTTPS'.</p>
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def IdleTimeout(self):
        r"""<p>Connection idle wait time.</p><p>1. For HTTP/HTTPS listener, the default value is 15, with a supported range of 1-60.<br>2. For TCP listener, the default value is 900, with a supported range of 10-900.<br>3. For UDP listener, the default value is 20, with a supported range of 10-20.</p>
        :rtype: int
        """
        return self._IdleTimeout

    @IdleTimeout.setter
    def IdleTimeout(self, IdleTimeout):
        self._IdleTimeout = IdleTimeout

    @property
    def GetRealIpType(self):
        r"""<p>Layer-4 source IP retrieval mode. Supports 'TOA', 'ProxyProtocol', and 'ProxyProtocolV2'.</p><p>This parameter can be filled in only when the Layer-4 source IP retrieval mode is enabled.</p>
        :rtype: str
        """
        return self._GetRealIpType

    @GetRealIpType.setter
    def GetRealIpType(self, GetRealIpType):
        self._GetRealIpType = GetRealIpType

    @property
    def ClientAffinity(self):
        r"""<p>Whether to enable session persistence. Supports configuration of 'Open' and 'Close'.</p><p>Enumeration values:</p><ul><li>Open: enable.</li><li>Close: disable.</li></ul><p>Only supported for layer-4 listeners. For layer-7 listeners, modification is not supported.</p>
        :rtype: str
        """
        return self._ClientAffinity

    @ClientAffinity.setter
    def ClientAffinity(self, ClientAffinity):
        self._ClientAffinity = ClientAffinity

    @property
    def RequestTimeout(self):
        r"""<p>Request timeout.</p><p>Value range: [1, 180]</p><p>Default value: 60</p><p>This parameter is configurable only for HTTPS listeners.</p>
        :rtype: int
        """
        return self._RequestTimeout

    @RequestTimeout.setter
    def RequestTimeout(self, RequestTimeout):
        self._RequestTimeout = RequestTimeout

    @property
    def XForwardedForRealIp(self):
        r"""<p>Whether to enable layer-7 source IP retrieval mode.</p>
        :rtype: bool
        """
        return self._XForwardedForRealIp

    @XForwardedForRealIp.setter
    def XForwardedForRealIp(self, XForwardedForRealIp):
        self._XForwardedForRealIp = XForwardedForRealIp

    @property
    def CertificationType(self):
        r"""<p>Parsing method.</p><p>Enumeration values:</p><ul><li>UNIDIRECTIONAL: two-way.</li><li>U: one-way.</li></ul><p>For an HTTPS listener, this field is required.</p>
        :rtype: str
        """
        return self._CertificationType

    @CertificationType.setter
    def CertificationType(self, CertificationType):
        self._CertificationType = CertificationType

    @property
    def CipherPolicyId(self):
        r"""<p>Encryption algorithm kit. Supports configuration of 'tls_policy_1.0-2', 'tls_policy_1.1-2', 'tls_policy_1.2', 'tls_policy_1.2_strict', 'tls_policy_1.2_strict-1.3'.</p>
        :rtype: str
        """
        return self._CipherPolicyId

    @CipherPolicyId.setter
    def CipherPolicyId(self, CipherPolicyId):
        self._CipherPolicyId = CipherPolicyId

    @property
    def ServerCertificates(self):
        r"""<p>Server certificate.</p><p>Input limit: currently only support importing one cert; to use multiple certs, use the cert api CreateListenerAdditionalCert to add other certs.</p><p>This field is required for HTTPS listeners.</p>
        :rtype: list of str
        """
        return self._ServerCertificates

    @ServerCertificates.setter
    def ServerCertificates(self, ServerCertificates):
        self._ServerCertificates = ServerCertificates

    @property
    def ClientCaCertificates(self):
        r"""<p>Client certificate.</p><p>Input limit: 1. Currently only support importing one cert. To use multiple certs, use the cert api CreateListenerAdditionalCert to add other certs. 2. The cert must be a CA certificate.</p><p>This field is required when HTTPS listener and mutual authentication are enabled.</p>
        :rtype: list of str
        """
        return self._ClientCaCertificates

    @ClientCaCertificates.setter
    def ClientCaCertificates(self, ClientCaCertificates):
        self._ClientCaCertificates = ClientCaCertificates

    @property
    def HttpVersion(self):
        r"""<p>HTTPS listener supports version selection</p><p>Enumeration values:</p><ul><li>HTTP/1.1: HTTP/1.1</li><li>HTTP/2: HTTP/2</li></ul>
        :rtype: str
        """
        return self._HttpVersion

    @HttpVersion.setter
    def HttpVersion(self, HttpVersion):
        self._HttpVersion = HttpVersion


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._Name = params.get("Name")
        if params.get("PortRanges") is not None:
            self._PortRanges = PortRanges()
            self._PortRanges._deserialize(params.get("PortRanges"))
        self._Description = params.get("Description")
        self._ListenerType = params.get("ListenerType")
        self._Protocol = params.get("Protocol")
        self._IdleTimeout = params.get("IdleTimeout")
        self._GetRealIpType = params.get("GetRealIpType")
        self._ClientAffinity = params.get("ClientAffinity")
        self._RequestTimeout = params.get("RequestTimeout")
        self._XForwardedForRealIp = params.get("XForwardedForRealIp")
        self._CertificationType = params.get("CertificationType")
        self._CipherPolicyId = params.get("CipherPolicyId")
        self._ServerCertificates = params.get("ServerCertificates")
        self._ClientCaCertificates = params.get("ClientCaCertificates")
        self._HttpVersion = params.get("HttpVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateListenerResponse(AbstractModel):
    r"""CreateListener response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>Task ID.</p>
        :type TaskId: str
        :param _ListenerId: <p>Listener ID.</p>
        :type ListenerId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._ListenerId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>Task ID.</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ListenerId(self):
        r"""<p>Listener ID.</p>
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

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
        self._TaskId = params.get("TaskId")
        self._ListenerId = params.get("ListenerId")
        self._RequestId = params.get("RequestId")


class DeleteAccelerateAreasRequest(AbstractModel):
    r"""DeleteAccelerateAreas request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: Global acceleration instance ID.
        :type GlobalAcceleratorId: str
        :param _AcceleratorAreaIds: Acceleration region ID.
        :type AcceleratorAreaIds: list of str
        """
        self._GlobalAcceleratorId = None
        self._AcceleratorAreaIds = None

    @property
    def GlobalAcceleratorId(self):
        r"""Global acceleration instance ID.
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def AcceleratorAreaIds(self):
        r"""Acceleration region ID.
        :rtype: list of str
        """
        return self._AcceleratorAreaIds

    @AcceleratorAreaIds.setter
    def AcceleratorAreaIds(self, AcceleratorAreaIds):
        self._AcceleratorAreaIds = AcceleratorAreaIds


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._AcceleratorAreaIds = params.get("AcceleratorAreaIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccelerateAreasResponse(AbstractModel):
    r"""DeleteAccelerateAreas response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Asynchronous task ID.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Asynchronous task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteEndpointGroupsRequest(AbstractModel):
    r"""DeleteEndpointGroups request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: Global acceleration instance ID.
        :type GlobalAcceleratorId: str
        :param _ListenerId: Listener ID.
        :type ListenerId: str
        :param _EndpointGroupIds: Terminal node group ID.
        :type EndpointGroupIds: list of str
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._EndpointGroupIds = None

    @property
    def GlobalAcceleratorId(self):
        r"""Global acceleration instance ID.
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""Listener ID.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def EndpointGroupIds(self):
        r"""Terminal node group ID.
        :rtype: list of str
        """
        return self._EndpointGroupIds

    @EndpointGroupIds.setter
    def EndpointGroupIds(self, EndpointGroupIds):
        self._EndpointGroupIds = EndpointGroupIds


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._EndpointGroupIds = params.get("EndpointGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEndpointGroupsResponse(AbstractModel):
    r"""DeleteEndpointGroups response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteForwardingPolicyRequest(AbstractModel):
    r"""DeleteForwardingPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: Global acceleration instance ID.
        :type GlobalAcceleratorId: str
        :param _ListenerId: Listener ID.
        :type ListenerId: str
        :param _ForwardingPolicyId: Policy ID.
        :type ForwardingPolicyId: str
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._ForwardingPolicyId = None

    @property
    def GlobalAcceleratorId(self):
        r"""Global acceleration instance ID.
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""Listener ID.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ForwardingPolicyId(self):
        r"""Policy ID.
        :rtype: str
        """
        return self._ForwardingPolicyId

    @ForwardingPolicyId.setter
    def ForwardingPolicyId(self, ForwardingPolicyId):
        self._ForwardingPolicyId = ForwardingPolicyId


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._ForwardingPolicyId = params.get("ForwardingPolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteForwardingPolicyResponse(AbstractModel):
    r"""DeleteForwardingPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Asynchronous task ID.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Asynchronous task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteForwardingRuleRequest(AbstractModel):
    r"""DeleteForwardingRule request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: Global acceleration instance ID.
        :type GlobalAcceleratorId: str
        :param _ListenerId: Listener ID.
        :type ListenerId: str
        :param _ForwardingPolicyId: Policy ID.
        :type ForwardingPolicyId: str
        :param _ForwardingRuleId: Layer 7 forwarding rule ID.
        :type ForwardingRuleId: str
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._ForwardingPolicyId = None
        self._ForwardingRuleId = None

    @property
    def GlobalAcceleratorId(self):
        r"""Global acceleration instance ID.
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""Listener ID.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ForwardingPolicyId(self):
        r"""Policy ID.
        :rtype: str
        """
        return self._ForwardingPolicyId

    @ForwardingPolicyId.setter
    def ForwardingPolicyId(self, ForwardingPolicyId):
        self._ForwardingPolicyId = ForwardingPolicyId

    @property
    def ForwardingRuleId(self):
        r"""Layer 7 forwarding rule ID.
        :rtype: str
        """
        return self._ForwardingRuleId

    @ForwardingRuleId.setter
    def ForwardingRuleId(self, ForwardingRuleId):
        self._ForwardingRuleId = ForwardingRuleId


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._ForwardingPolicyId = params.get("ForwardingPolicyId")
        self._ForwardingRuleId = params.get("ForwardingRuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteForwardingRuleResponse(AbstractModel):
    r"""DeleteForwardingRule response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Asynchronous task ID.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Asynchronous task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteGlobalAcceleratorAccessLogRequest(AbstractModel):
    r"""DeleteGlobalAcceleratorAccessLog request structure.

    """

    def __init__(self):
        r"""
        :param _LogPushTaskId: <p>Log Unique Id</p>
        :type LogPushTaskId: str
        :param _GlobalAcceleratorId: <p>Unique Id of the GA instance</p>
        :type GlobalAcceleratorId: str
        """
        self._LogPushTaskId = None
        self._GlobalAcceleratorId = None

    @property
    def LogPushTaskId(self):
        r"""<p>Log Unique Id</p>
        :rtype: str
        """
        return self._LogPushTaskId

    @LogPushTaskId.setter
    def LogPushTaskId(self, LogPushTaskId):
        self._LogPushTaskId = LogPushTaskId

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Unique Id of the GA instance</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId


    def _deserialize(self, params):
        self._LogPushTaskId = params.get("LogPushTaskId")
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGlobalAcceleratorAccessLogResponse(AbstractModel):
    r"""DeleteGlobalAcceleratorAccessLog response structure.

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


class DeleteGlobalAcceleratorAclPolicyRequest(AbstractModel):
    r"""DeleteGlobalAcceleratorAclPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: Global acceleration instance ID.
        :type GlobalAcceleratorId: str
        :param _GlobalAcceleratorAclPolicyId: Access control policy ID.
        :type GlobalAcceleratorAclPolicyId: str
        """
        self._GlobalAcceleratorId = None
        self._GlobalAcceleratorAclPolicyId = None

    @property
    def GlobalAcceleratorId(self):
        r"""Global acceleration instance ID.
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def GlobalAcceleratorAclPolicyId(self):
        r"""Access control policy ID.
        :rtype: str
        """
        return self._GlobalAcceleratorAclPolicyId

    @GlobalAcceleratorAclPolicyId.setter
    def GlobalAcceleratorAclPolicyId(self, GlobalAcceleratorAclPolicyId):
        self._GlobalAcceleratorAclPolicyId = GlobalAcceleratorAclPolicyId


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._GlobalAcceleratorAclPolicyId = params.get("GlobalAcceleratorAclPolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGlobalAcceleratorAclPolicyResponse(AbstractModel):
    r"""DeleteGlobalAcceleratorAclPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Asynchronous task ID.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Asynchronous task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteGlobalAcceleratorAclRuleRequest(AbstractModel):
    r"""DeleteGlobalAcceleratorAclRule request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: Global acceleration instance ID.
        :type GlobalAcceleratorId: str
        :param _GlobalAcceleratorAclPolicyId: Security policy ID
        :type GlobalAcceleratorAclPolicyId: str
        :param _GlobalAcceleratorAclRuleIds: Acl rule ID.
        :type GlobalAcceleratorAclRuleIds: list of str
        """
        self._GlobalAcceleratorId = None
        self._GlobalAcceleratorAclPolicyId = None
        self._GlobalAcceleratorAclRuleIds = None

    @property
    def GlobalAcceleratorId(self):
        r"""Global acceleration instance ID.
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def GlobalAcceleratorAclPolicyId(self):
        r"""Security policy ID
        :rtype: str
        """
        return self._GlobalAcceleratorAclPolicyId

    @GlobalAcceleratorAclPolicyId.setter
    def GlobalAcceleratorAclPolicyId(self, GlobalAcceleratorAclPolicyId):
        self._GlobalAcceleratorAclPolicyId = GlobalAcceleratorAclPolicyId

    @property
    def GlobalAcceleratorAclRuleIds(self):
        r"""Acl rule ID.
        :rtype: list of str
        """
        return self._GlobalAcceleratorAclRuleIds

    @GlobalAcceleratorAclRuleIds.setter
    def GlobalAcceleratorAclRuleIds(self, GlobalAcceleratorAclRuleIds):
        self._GlobalAcceleratorAclRuleIds = GlobalAcceleratorAclRuleIds


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._GlobalAcceleratorAclPolicyId = params.get("GlobalAcceleratorAclPolicyId")
        self._GlobalAcceleratorAclRuleIds = params.get("GlobalAcceleratorAclRuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGlobalAcceleratorAclRuleResponse(AbstractModel):
    r"""DeleteGlobalAcceleratorAclRule response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Asynchronous task ID.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Asynchronous task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteGlobalAcceleratorRequest(AbstractModel):
    r"""DeleteGlobalAccelerator request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: Global acceleration instance ID.
        :type GlobalAcceleratorId: str
        """
        self._GlobalAcceleratorId = None

    @property
    def GlobalAcceleratorId(self):
        r"""Global acceleration instance ID.
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGlobalAcceleratorResponse(AbstractModel):
    r"""DeleteGlobalAccelerator response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteListenerAdditionalCertRequest(AbstractModel):
    r"""DeleteListenerAdditionalCert request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: Global acceleration instance ID.
        :type GlobalAcceleratorId: str
        :param _ListenerId: Listener ID.
        :type ListenerId: str
        :param _AdditionalCertificates: Certificate ID.
        :type AdditionalCertificates: list of str
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._AdditionalCertificates = None

    @property
    def GlobalAcceleratorId(self):
        r"""Global acceleration instance ID.
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""Listener ID.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def AdditionalCertificates(self):
        r"""Certificate ID.
        :rtype: list of str
        """
        return self._AdditionalCertificates

    @AdditionalCertificates.setter
    def AdditionalCertificates(self, AdditionalCertificates):
        self._AdditionalCertificates = AdditionalCertificates


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._AdditionalCertificates = params.get("AdditionalCertificates")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteListenerAdditionalCertResponse(AbstractModel):
    r"""DeleteListenerAdditionalCert response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteListenerRequest(AbstractModel):
    r"""DeleteListener request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: Global acceleration instance ID.
        :type GlobalAcceleratorId: str
        :param _ListenerId: Listener ID.
        :type ListenerId: str
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None

    @property
    def GlobalAcceleratorId(self):
        r"""Global acceleration instance ID.
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""Listener ID.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteListenerResponse(AbstractModel):
    r"""DeleteListener response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DescribeAccelerateAreasRequest(AbstractModel):
    r"""DescribeAccelerateAreas request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>Global acceleration instance ID.</p>
        :type GlobalAcceleratorId: str
        :param _Offset: <p>Offset. The default is 0.</p>
        :type Offset: int
        :param _Limit: <p>Number of instances meeting conditions. Default value: 20. Maximum: 200.</p>
        :type Limit: int
        :param _Filters: <p>Filter criteria. accelerate-region - String - (Filter criterion) Terminal node group region.</p>
        :type Filters: list of Filter
        """
        self._GlobalAcceleratorId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Global acceleration instance ID.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def Offset(self):
        r"""<p>Offset. The default is 0.</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>Number of instances meeting conditions. Default value: 20. Maximum: 200.</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""<p>Filter criteria. accelerate-region - String - (Filter criterion) Terminal node group region.</p>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
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
        


class DescribeAccelerateAreasResponse(AbstractModel):
    r"""DescribeAccelerateAreas response structure.

    """

    def __init__(self):
        r"""
        :param _AccelerateAreaSet: <p>Acceleration region information.</p>
        :type AccelerateAreaSet: list of AcceleratorAreas
        :param _TotalCount: <p>Number of instances.</p>
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AccelerateAreaSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AccelerateAreaSet(self):
        r"""<p>Acceleration region information.</p>
        :rtype: list of AcceleratorAreas
        """
        return self._AccelerateAreaSet

    @AccelerateAreaSet.setter
    def AccelerateAreaSet(self, AccelerateAreaSet):
        self._AccelerateAreaSet = AccelerateAreaSet

    @property
    def TotalCount(self):
        r"""<p>Number of instances.</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("AccelerateAreaSet") is not None:
            self._AccelerateAreaSet = []
            for item in params.get("AccelerateAreaSet"):
                obj = AcceleratorAreas()
                obj._deserialize(item)
                self._AccelerateAreaSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeAccelerateRegionsRequest(AbstractModel):
    r"""DescribeAccelerateRegions request structure.

    """


class DescribeAccelerateRegionsResponse(AbstractModel):
    r"""DescribeAccelerateRegions response structure.

    """

    def __init__(self):
        r"""
        :param _AcceleratorRegionSet: Acceleration region information.
        :type AcceleratorRegionSet: list of AcceleratorRegionSet
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AcceleratorRegionSet = None
        self._RequestId = None

    @property
    def AcceleratorRegionSet(self):
        r"""Acceleration region information.
        :rtype: list of AcceleratorRegionSet
        """
        return self._AcceleratorRegionSet

    @AcceleratorRegionSet.setter
    def AcceleratorRegionSet(self, AcceleratorRegionSet):
        self._AcceleratorRegionSet = AcceleratorRegionSet

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
        if params.get("AcceleratorRegionSet") is not None:
            self._AcceleratorRegionSet = []
            for item in params.get("AcceleratorRegionSet"):
                obj = AcceleratorRegionSet()
                obj._deserialize(item)
                self._AcceleratorRegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAccessLogParamRequest(AbstractModel):
    r"""DescribeAccessLogParam request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: 
        :type GlobalAcceleratorId: str
        """
        self._GlobalAcceleratorId = None

    @property
    def GlobalAcceleratorId(self):
        r"""
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessLogParamResponse(AbstractModel):
    r"""DescribeAccessLogParam response structure.

    """

    def __init__(self):
        r"""
        :param _L7Param: <p>Layer-7 optional parameter.</p>
        :type L7Param: list of str
        :param _L4Param: <p>L4 optional parameter</p>
        :type L4Param: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._L7Param = None
        self._L4Param = None
        self._RequestId = None

    @property
    def L7Param(self):
        r"""<p>Layer-7 optional parameter.</p>
        :rtype: list of str
        """
        return self._L7Param

    @L7Param.setter
    def L7Param(self, L7Param):
        self._L7Param = L7Param

    @property
    def L4Param(self):
        r"""<p>L4 optional parameter</p>
        :rtype: list of str
        """
        return self._L4Param

    @L4Param.setter
    def L4Param(self, L4Param):
        self._L4Param = L4Param

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
        self._L7Param = params.get("L7Param")
        self._L4Param = params.get("L4Param")
        self._RequestId = params.get("RequestId")


class DescribeCrossBorderSettlementRequest(AbstractModel):
    r"""DescribeCrossBorderSettlement request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: Global acceleration instance ID.
        :type GlobalAcceleratorId: str
        :param _AccelerateRegion: Acceleration region.
        :type AccelerateRegion: str
        :param _EndpointGroupRegion: Region of the terminal node group.
        :type EndpointGroupRegion: str
        :param _SettlementMonth: Bill year and month time.
        :type SettlementMonth: int
        """
        self._GlobalAcceleratorId = None
        self._AccelerateRegion = None
        self._EndpointGroupRegion = None
        self._SettlementMonth = None

    @property
    def GlobalAcceleratorId(self):
        r"""Global acceleration instance ID.
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def AccelerateRegion(self):
        r"""Acceleration region.
        :rtype: str
        """
        return self._AccelerateRegion

    @AccelerateRegion.setter
    def AccelerateRegion(self, AccelerateRegion):
        self._AccelerateRegion = AccelerateRegion

    @property
    def EndpointGroupRegion(self):
        r"""Region of the terminal node group.
        :rtype: str
        """
        return self._EndpointGroupRegion

    @EndpointGroupRegion.setter
    def EndpointGroupRegion(self, EndpointGroupRegion):
        self._EndpointGroupRegion = EndpointGroupRegion

    @property
    def SettlementMonth(self):
        r"""Bill year and month time.
        :rtype: int
        """
        return self._SettlementMonth

    @SettlementMonth.setter
    def SettlementMonth(self, SettlementMonth):
        self._SettlementMonth = SettlementMonth


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._AccelerateRegion = params.get("AccelerateRegion")
        self._EndpointGroupRegion = params.get("EndpointGroupRegion")
        self._SettlementMonth = params.get("SettlementMonth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCrossBorderSettlementResponse(AbstractModel):
    r"""DescribeCrossBorderSettlement response structure.

    """

    def __init__(self):
        r"""
        :param _Traffic: Traffic amount in GB; precision is reserved to 6 decimal places.
        :type Traffic: float
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Traffic = None
        self._RequestId = None

    @property
    def Traffic(self):
        r"""Traffic amount in GB; precision is reserved to 6 decimal places.
        :rtype: float
        """
        return self._Traffic

    @Traffic.setter
    def Traffic(self, Traffic):
        self._Traffic = Traffic

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
        self._Traffic = params.get("Traffic")
        self._RequestId = params.get("RequestId")


class DescribeEndpointGroupsRequest(AbstractModel):
    r"""DescribeEndpointGroups request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>Global acceleration instance ID.</p>
        :type GlobalAcceleratorId: str
        :param _Offset: <p>Offset. Default value: 0.</p>
        :type Offset: int
        :param _Limit: <p>Number of returns. Default value: 10. Maximum value: 10.</p>
        :type Limit: int
        :param _Filters: <p>Filter criteria. endpoint-group-id - String - (Filter criterion) Terminal node group instance ID. endpoint-group-type - String - (Filter criterion) Terminal node group instance type.</p>
        :type Filters: list of Filter
        """
        self._GlobalAcceleratorId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Global acceleration instance ID.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def Offset(self):
        r"""<p>Offset. Default value: 0.</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>Number of returns. Default value: 10. Maximum value: 10.</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""<p>Filter criteria. endpoint-group-id - String - (Filter criterion) Terminal node group instance ID. endpoint-group-type - String - (Filter criterion) Terminal node group instance type.</p>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
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
        


class DescribeEndpointGroupsResponse(AbstractModel):
    r"""DescribeEndpointGroups response structure.

    """

    def __init__(self):
        r"""
        :param _EndpointGroupConfigurationSet: <p>Eligible terminal node group.</p>
        :type EndpointGroupConfigurationSet: list of EndpointGroupConfigurationSet
        :param _TotalCount: <p>Number of instances that meet the criteria.</p>
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EndpointGroupConfigurationSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def EndpointGroupConfigurationSet(self):
        r"""<p>Eligible terminal node group.</p>
        :rtype: list of EndpointGroupConfigurationSet
        """
        return self._EndpointGroupConfigurationSet

    @EndpointGroupConfigurationSet.setter
    def EndpointGroupConfigurationSet(self, EndpointGroupConfigurationSet):
        self._EndpointGroupConfigurationSet = EndpointGroupConfigurationSet

    @property
    def TotalCount(self):
        r"""<p>Number of instances that meet the criteria.</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("EndpointGroupConfigurationSet") is not None:
            self._EndpointGroupConfigurationSet = []
            for item in params.get("EndpointGroupConfigurationSet"):
                obj = EndpointGroupConfigurationSet()
                obj._deserialize(item)
                self._EndpointGroupConfigurationSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeForwardingPolicyRequest(AbstractModel):
    r"""DescribeForwardingPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: Global acceleration instance ID.
        :type GlobalAcceleratorId: str
        :param _ListenerId: Listener ID.
        :type ListenerId: str
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returns. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._Offset = None
        self._Limit = None

    @property
    def GlobalAcceleratorId(self):
        r"""Global acceleration instance ID.
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""Listener ID.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Offset(self):
        r"""Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of returns. Default value: 20. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeForwardingPolicyResponse(AbstractModel):
    r"""DescribeForwardingPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _ForwardingPolicySet: Policy information that meets the conditions.
        :type ForwardingPolicySet: list of ForwardingPolicySet
        :param _TotalCount: Number of instances that meet the criteria.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ForwardingPolicySet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ForwardingPolicySet(self):
        r"""Policy information that meets the conditions.
        :rtype: list of ForwardingPolicySet
        """
        return self._ForwardingPolicySet

    @ForwardingPolicySet.setter
    def ForwardingPolicySet(self, ForwardingPolicySet):
        self._ForwardingPolicySet = ForwardingPolicySet

    @property
    def TotalCount(self):
        r"""Number of instances that meet the criteria.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("ForwardingPolicySet") is not None:
            self._ForwardingPolicySet = []
            for item in params.get("ForwardingPolicySet"):
                obj = ForwardingPolicySet()
                obj._deserialize(item)
                self._ForwardingPolicySet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeForwardingRuleRequest(AbstractModel):
    r"""DescribeForwardingRule request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: Global acceleration instance ID.
        :type GlobalAcceleratorId: str
        :param _ListenerId: Listener ID.
        :type ListenerId: str
        :param _ForwardingPolicyId: Layer 7 forwarding rule ID.
        :type ForwardingPolicyId: str
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returns. Default value: 20. Maximum value: 100.
        :type Limit: int
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._ForwardingPolicyId = None
        self._Offset = None
        self._Limit = None

    @property
    def GlobalAcceleratorId(self):
        r"""Global acceleration instance ID.
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""Listener ID.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ForwardingPolicyId(self):
        r"""Layer 7 forwarding rule ID.
        :rtype: str
        """
        return self._ForwardingPolicyId

    @ForwardingPolicyId.setter
    def ForwardingPolicyId(self, ForwardingPolicyId):
        self._ForwardingPolicyId = ForwardingPolicyId

    @property
    def Offset(self):
        r"""Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of returns. Default value: 20. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._ForwardingPolicyId = params.get("ForwardingPolicyId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeForwardingRuleResponse(AbstractModel):
    r"""DescribeForwardingRule response structure.

    """

    def __init__(self):
        r"""
        :param _ForwardingRuleSet: Rule information that meets the conditions.
        :type ForwardingRuleSet: list of ForwardingRuleSet
        :param _TotalCount: Number of instances that meet the criteria.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ForwardingRuleSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ForwardingRuleSet(self):
        r"""Rule information that meets the conditions.
        :rtype: list of ForwardingRuleSet
        """
        return self._ForwardingRuleSet

    @ForwardingRuleSet.setter
    def ForwardingRuleSet(self, ForwardingRuleSet):
        self._ForwardingRuleSet = ForwardingRuleSet

    @property
    def TotalCount(self):
        r"""Number of instances that meet the criteria.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("ForwardingRuleSet") is not None:
            self._ForwardingRuleSet = []
            for item in params.get("ForwardingRuleSet"):
                obj = ForwardingRuleSet()
                obj._deserialize(item)
                self._ForwardingRuleSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeGlobalAcceleratorAccessLogRequest(AbstractModel):
    r"""DescribeGlobalAcceleratorAccessLog request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>Unique Id of the ga instance</p>
        :type GlobalAcceleratorId: str
        :param _Filters: <p>Query filter parameters. { &quot;Name&quot;: &quot;listener-id&quot;, &quot;Values&quot;: [&quot;listener unique id&quot;] },{ &quot;Name&quot;: &quot;endpoint-group-id&quot;, &quot;Values&quot;: [&quot;Terminal node group unique id&quot;] },{ &quot;Name&quot;: &quot;access_log_id&quot;, &quot;Values&quot;: [&quot;log unique id&quot;] }</p>
        :type Filters: list of Filter
        :param _Offset: <p>Offset. Default value: 0.</p>
        :type Offset: int
        :param _Limit: <p>Number of returned results.</p><p>Value range: [0, 200]</p>
        :type Limit: int
        """
        self._GlobalAcceleratorId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Unique Id of the ga instance</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def Filters(self):
        r"""<p>Query filter parameters. { &quot;Name&quot;: &quot;listener-id&quot;, &quot;Values&quot;: [&quot;listener unique id&quot;] },{ &quot;Name&quot;: &quot;endpoint-group-id&quot;, &quot;Values&quot;: [&quot;Terminal node group unique id&quot;] },{ &quot;Name&quot;: &quot;access_log_id&quot;, &quot;Values&quot;: [&quot;log unique id&quot;] }</p>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""<p>Offset. Default value: 0.</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>Number of returned results.</p><p>Value range: [0, 200]</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
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
        


class DescribeGlobalAcceleratorAccessLogResponse(AbstractModel):
    r"""DescribeGlobalAcceleratorAccessLog response structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorAccessLog: <p>Return log task detail</p>
        :type GlobalAcceleratorAccessLog: list of GlobalAcceleratorAccessLog
        :param _TotalCount: <p>Number of log task entries.</p>
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GlobalAcceleratorAccessLog = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def GlobalAcceleratorAccessLog(self):
        r"""<p>Return log task detail</p>
        :rtype: list of GlobalAcceleratorAccessLog
        """
        return self._GlobalAcceleratorAccessLog

    @GlobalAcceleratorAccessLog.setter
    def GlobalAcceleratorAccessLog(self, GlobalAcceleratorAccessLog):
        self._GlobalAcceleratorAccessLog = GlobalAcceleratorAccessLog

    @property
    def TotalCount(self):
        r"""<p>Number of log task entries.</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("GlobalAcceleratorAccessLog") is not None:
            self._GlobalAcceleratorAccessLog = []
            for item in params.get("GlobalAcceleratorAccessLog"):
                obj = GlobalAcceleratorAccessLog()
                obj._deserialize(item)
                self._GlobalAcceleratorAccessLog.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeGlobalAcceleratorAclPoliciesRequest(AbstractModel):
    r"""DescribeGlobalAcceleratorAclPolicies request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>Global acceleration instance ID.</p>
        :type GlobalAcceleratorId: str
        :param _Offset: <p>Offset. Default value: 0.</p>
        :type Offset: int
        :param _Limit: <p>Number of returns. Default value: 20. Maximum value: 200.</p>
        :type Limit: str
        """
        self._GlobalAcceleratorId = None
        self._Offset = None
        self._Limit = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Global acceleration instance ID.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def Offset(self):
        r"""<p>Offset. Default value: 0.</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>Number of returns. Default value: 20. Maximum value: 200.</p>
        :rtype: str
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGlobalAcceleratorAclPoliciesResponse(AbstractModel):
    r"""DescribeGlobalAcceleratorAclPolicies response structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorAclPolicySet: <p>Access control policy information.</p>
        :type GlobalAcceleratorAclPolicySet: list of GlobalAcceleratorAclPolicies
        :param _TotalCount: <p>Total number of instances that meet the criteria.</p>
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GlobalAcceleratorAclPolicySet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def GlobalAcceleratorAclPolicySet(self):
        r"""<p>Access control policy information.</p>
        :rtype: list of GlobalAcceleratorAclPolicies
        """
        return self._GlobalAcceleratorAclPolicySet

    @GlobalAcceleratorAclPolicySet.setter
    def GlobalAcceleratorAclPolicySet(self, GlobalAcceleratorAclPolicySet):
        self._GlobalAcceleratorAclPolicySet = GlobalAcceleratorAclPolicySet

    @property
    def TotalCount(self):
        r"""<p>Total number of instances that meet the criteria.</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("GlobalAcceleratorAclPolicySet") is not None:
            self._GlobalAcceleratorAclPolicySet = []
            for item in params.get("GlobalAcceleratorAclPolicySet"):
                obj = GlobalAcceleratorAclPolicies()
                obj._deserialize(item)
                self._GlobalAcceleratorAclPolicySet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeGlobalAcceleratorAclRulesRequest(AbstractModel):
    r"""DescribeGlobalAcceleratorAclRules request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorAclPolicyId: <p>Access control policy ID.</p>
        :type GlobalAcceleratorAclPolicyId: str
        :param _Offset: <p>Offset. Default value: 0.</p>
        :type Offset: int
        :param _Limit: <p>Number of returned results.</p><p>Value range: [1, 200]</p><p>Default value: 20</p>
        :type Limit: int
        """
        self._GlobalAcceleratorAclPolicyId = None
        self._Offset = None
        self._Limit = None

    @property
    def GlobalAcceleratorAclPolicyId(self):
        r"""<p>Access control policy ID.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorAclPolicyId

    @GlobalAcceleratorAclPolicyId.setter
    def GlobalAcceleratorAclPolicyId(self, GlobalAcceleratorAclPolicyId):
        self._GlobalAcceleratorAclPolicyId = GlobalAcceleratorAclPolicyId

    @property
    def Offset(self):
        r"""<p>Offset. Default value: 0.</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>Number of returned results.</p><p>Value range: [1, 200]</p><p>Default value: 20</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._GlobalAcceleratorAclPolicyId = params.get("GlobalAcceleratorAclPolicyId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGlobalAcceleratorAclRulesResponse(AbstractModel):
    r"""DescribeGlobalAcceleratorAclRules response structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorAclRuleSet: <p>Eligible Acl rule instance.</p>
        :type GlobalAcceleratorAclRuleSet: list of GlobalAcceleratorAclRuleSet
        :param _TotalCount: <p>Number of instances that meet the criteria.</p>
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GlobalAcceleratorAclRuleSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def GlobalAcceleratorAclRuleSet(self):
        r"""<p>Eligible Acl rule instance.</p>
        :rtype: list of GlobalAcceleratorAclRuleSet
        """
        return self._GlobalAcceleratorAclRuleSet

    @GlobalAcceleratorAclRuleSet.setter
    def GlobalAcceleratorAclRuleSet(self, GlobalAcceleratorAclRuleSet):
        self._GlobalAcceleratorAclRuleSet = GlobalAcceleratorAclRuleSet

    @property
    def TotalCount(self):
        r"""<p>Number of instances that meet the criteria.</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("GlobalAcceleratorAclRuleSet") is not None:
            self._GlobalAcceleratorAclRuleSet = []
            for item in params.get("GlobalAcceleratorAclRuleSet"):
                obj = GlobalAcceleratorAclRuleSet()
                obj._deserialize(item)
                self._GlobalAcceleratorAclRuleSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeGlobalAcceleratorsRequest(AbstractModel):
    r"""DescribeGlobalAccelerators request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: <p>Offset. Default value: 0.</p>
        :type Offset: int
        :param _Limit: <p>Number of returned results.</p><p>Value range: [1, 200]</p><p>Default value: 20</p>
        :type Limit: int
        :param _Filters: <p>Filter criteria. <li>global-accelerator-id - String - (Filter condition) Global acceleration instance ID.</li> <li>global-accelerator-state - String - (Filter condition) Global acceleration instance status.</li></p>
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        r"""<p>Offset. Default value: 0.</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>Number of returned results.</p><p>Value range: [1, 200]</p><p>Default value: 20</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""<p>Filter criteria. <li>global-accelerator-id - String - (Filter condition) Global acceleration instance ID.</li> <li>global-accelerator-state - String - (Filter condition) Global acceleration instance status.</li></p>
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
        


class DescribeGlobalAcceleratorsResponse(AbstractModel):
    r"""DescribeGlobalAccelerators response structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorSet: <p>Eligible global acceleration instances.</p>
        :type GlobalAcceleratorSet: list of GlobalAcceleratorSet
        :param _TotalCount: <p>Number of instances that meet the criteria.</p>
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GlobalAcceleratorSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def GlobalAcceleratorSet(self):
        r"""<p>Eligible global acceleration instances.</p>
        :rtype: list of GlobalAcceleratorSet
        """
        return self._GlobalAcceleratorSet

    @GlobalAcceleratorSet.setter
    def GlobalAcceleratorSet(self, GlobalAcceleratorSet):
        self._GlobalAcceleratorSet = GlobalAcceleratorSet

    @property
    def TotalCount(self):
        r"""<p>Number of instances that meet the criteria.</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("GlobalAcceleratorSet") is not None:
            self._GlobalAcceleratorSet = []
            for item in params.get("GlobalAcceleratorSet"):
                obj = GlobalAcceleratorSet()
                obj._deserialize(item)
                self._GlobalAcceleratorSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeListenersRequest(AbstractModel):
    r"""DescribeListeners request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: Global acceleration instance ID.
        :type GlobalAcceleratorId: str
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returns. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Filters: Filter criteria. listener-id - String - (Filter criteria) Listener instance ID.
        :type Filters: list of Filter
        """
        self._GlobalAcceleratorId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def GlobalAcceleratorId(self):
        r"""Global acceleration instance ID.
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def Offset(self):
        r"""Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of returns. Default value: 20. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""Filter criteria. listener-id - String - (Filter criteria) Listener instance ID.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
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
        


class DescribeListenersResponse(AbstractModel):
    r"""DescribeListeners response structure.

    """

    def __init__(self):
        r"""
        :param _ListenerSet: Eligible listener instance.
        :type ListenerSet: list of ListenerSet
        :param _TotalCount: Number of instances that meet the criteria.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ListenerSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ListenerSet(self):
        r"""Eligible listener instance.
        :rtype: list of ListenerSet
        """
        return self._ListenerSet

    @ListenerSet.setter
    def ListenerSet(self, ListenerSet):
        self._ListenerSet = ListenerSet

    @property
    def TotalCount(self):
        r"""Number of instances that meet the criteria.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("ListenerSet") is not None:
            self._ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = ListenerSet()
                obj._deserialize(item)
                self._ListenerSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTaskResultRequest(AbstractModel):
    r"""DescribeTaskResult request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Asynchronous task ID.
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""Asynchronous task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskResultResponse(AbstractModel):
    r"""DescribeTaskResult response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Task status.
        :type Status: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""Task status.
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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class EndpointConfigurations(AbstractModel):
    r"""Terminal node configuration

    """

    def __init__(self):
        r"""
        :param _EndpointType: <p>Domain type. Available values: 'Domain', 'PublicIp'.</p>
        :type EndpointType: str
        :param _EndpointService: <p>Domain name.</p>
        :type EndpointService: str
        :param _Weight: <p>Weight.</p>
        :type Weight: int
        :param _HealthCheckStatus: <p>Health check status; HEALTH: healthy; UNHEALTH: unhealthy.</p>
        :type HealthCheckStatus: str
        """
        self._EndpointType = None
        self._EndpointService = None
        self._Weight = None
        self._HealthCheckStatus = None

    @property
    def EndpointType(self):
        r"""<p>Domain type. Available values: 'Domain', 'PublicIp'.</p>
        :rtype: str
        """
        return self._EndpointType

    @EndpointType.setter
    def EndpointType(self, EndpointType):
        self._EndpointType = EndpointType

    @property
    def EndpointService(self):
        r"""<p>Domain name.</p>
        :rtype: str
        """
        return self._EndpointService

    @EndpointService.setter
    def EndpointService(self, EndpointService):
        self._EndpointService = EndpointService

    @property
    def Weight(self):
        r"""<p>Weight.</p>
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def HealthCheckStatus(self):
        r"""<p>Health check status; HEALTH: healthy; UNHEALTH: unhealthy.</p>
        :rtype: str
        """
        return self._HealthCheckStatus

    @HealthCheckStatus.setter
    def HealthCheckStatus(self, HealthCheckStatus):
        self._HealthCheckStatus = HealthCheckStatus


    def _deserialize(self, params):
        self._EndpointType = params.get("EndpointType")
        self._EndpointService = params.get("EndpointService")
        self._Weight = params.get("Weight")
        self._HealthCheckStatus = params.get("HealthCheckStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EndpointGroupConfiguration(AbstractModel):
    r"""Terminal node group configuration

    """

    def __init__(self):
        r"""
        :param _Name: <p>Terminal node group name.</p><p>Parameter format: starting with a letter or Chinese characters, 2–128 characters in length, supporting letters, digits, Chinese characters, . - _</p>
        :type Name: str
        :param _EndpointGroupRegion: <p>Region of the terminal node group.</p>
        :type EndpointGroupRegion: str
        :param _EndpointConfigurations: <p>Terminal node configuration.</p>
        :type EndpointConfigurations: list of EndpointConfigurations
        :param _CheckType: <p>Check protocol. Supports configuration of 'TCP', 'HTTP', 'PING', and 'CUSTOM'.</p><p>Enumeration values:</p><ul><li>TCP: When the CLB listener protocol where the terminal node group resides is TCP, choose TCP as the check protocol.</li><li>HTTP: When the CLB listener protocol where the terminal node group resides is HTTP or HTTPS, choose HTTP as the check protocol.</li><li>PING: When the CLB listener protocol where the terminal node group resides is UDP, choose PING as the check protocol.</li><li>CUSTOM: When the CLB listener protocol where the terminal node group resides is UDP or TCP, choose CUSTOM as the check protocol.</li></ul><p>This field is required when health check is enabled.</p>
        :type CheckType: str
        :param _Description: <p>Description.</p><p>Default value: empty by default, representing no configuration description.</p><p>Maximum length: 100 bytes.</p>
        :type Description: str
        :param _CheckPort: <p>Check port.</p><p>Input limit: range 1-65535.</p><p>This field is required when CheckType is CUSTOM.</p>
        :type CheckPort: str
        :param _ContextType: <p>Check content. Supports configuration 'TEXT'.</p><p>Enumeration values:</p><ul><li>TEXT: Text content.</li></ul><p>This field is required when CheckType is CUSTOM.</p>
        :type ContextType: str
        :param _CheckSendContext: <p>Check request.</p><p>Input parameter limit: The byte length must be within 1-500.</p><p>This field is required when CheckType is CUSTOM.</p>
        :type CheckSendContext: str
        :param _CheckRecvContext: <p>Check returned results.</p><p>Input parameter limit: The byte length must be within 1-500.</p><p>When CheckType is CUSTOM, this field is required.</p>
        :type CheckRecvContext: str
        :param _EnableHealthCheck: <p>Whether to enable health check.</p><p>Default value: False</p>
        :type EnableHealthCheck: bool
        :param _ConnectTimeout: <p>Response timeout.</p><p>Value range: [1, 100]</p><p>Default value: 2</p><p>This field is required when health check is enabled.</p>
        :type ConnectTimeout: int
        :param _HealthCheckInterval: <p>Health check interval.</p><p>Value range: [5, 300].</p><p>Default value: 30.</p><p>This field is required when health check is enabled.</p>
        :type HealthCheckInterval: int
        :param _UnhealthyThreshold: <p>Unhealthy threshold.</p><p>Value range: [1, 10]</p><p>Default value: 3</p><p>This field is required when health check is enabled.</p>
        :type UnhealthyThreshold: int
        :param _HealthyThreshold: <p>Health threshold.</p><p>Value range: [1, 10]</p><p>Default value: 3</p><p>This field is required when health check is enabled.</p>
        :type HealthyThreshold: int
        :param _ForwardProtocol: <p>Origin-pull protocol. HTTP and HTTPS can be configured.</p><p>Enumeration values:</p><ul><li>HTTP: HTTP origin-pull. HTTP can be configured when the listener protocol where the terminal node group resides is HTTP or HTTPS.</li><li>HTTPS: HTTPS origin-pull. HTTPS can be configured when the listener protocol where the terminal node group resides is HTTPS.</li></ul><p>This field is required when the listener protocol where the terminal node group resides is HTTP or HTTPS.</p>
        :type ForwardProtocol: str
        :param _CheckDomain: <p>Check domain name.</p><p>Input parameter limit: The byte length range is 3-80.</p><p>This field is required when CheckType is HTTP.</p>
        :type CheckDomain: str
        :param _CheckPath: <p>Check the URL.</p><p>Parameter format: must match the regular expression: ^[a-zA-Z0-9_.\-\/]{1,80}$</p><p>This field is required when CheckType is HTTP.</p>
        :type CheckPath: str
        :param _CheckMethod: <p>Request method. Supports configuration of 'GET' and 'HEAD'.</p><p>Enumeration values:</p><ul><li>GET: The request method is GET.</li><li>HEAD: The request method is HEAD.</li></ul><p>When CheckType is HTTP, this field is required.</p>
        :type CheckMethod: str
        :param _StatusMask: <p>Status check code. Supports configuring 'http_2xx', 'http_3xx', 'http_4xx', 'http_5xx'.</p><p>Enumeration values:</p><ul><li>http_2xx: HTTP codes beginning with 2.</li><li>http_3xx: HTTP codes beginning with 3.</li><li>http_4xx: HTTP codes beginning with 4.</li><li>http_5xx: HTTP codes beginning with 5.</li></ul><p>This field is required when CheckType is HTTP.</p>
        :type StatusMask: list of str
        :param _PortOverrides: <p>Port mapping.</p><p>Input limits: Layer 7 supports 1 port mapping, and Layer 4 supports up to 30 port mappings.</p>
        :type PortOverrides: list of PortOverride
        :param _IspType: <p>Operator type. Supports configuration 'CMCC', 'CTCC', 'CUCC'.</p><p>Enumeration values:</p><ul><li>CMCC: China Mobile</li><li>CUCC: China Unicom</li><li>CTCC: China Telecom</li></ul><p>This field is required when the terminal node group region is a triple-network region.</p>
        :type IspType: str
        :param _CipherPolicyId: <p>HPPTS encryption algorithm suite; supports configuration 'tls_policy_1.0-2', 'tls_policy_1.1-2', 'tls_policy_1.2', 'tls_policy_1.2_strict', 'tls_policy_1.2_strict-1.3';</p><p>Enumeration values:</p><ul><li>tls_policy_1.0-2: encryption algorithm suite.</li><li>tls_policy_1.1-2: encryption algorithm suite.</li><li>tls_policy_1.2: encryption algorithm suite.</li><li>tls_policy_1.2_strict: encryption algorithm suite.</li><li>tls_policy_1.2_strict-1.3: encryption algorithm suite.</li></ul><p>This field is required when the origin-pull protocol is HTTPS.</p>
        :type CipherPolicyId: str
        :param _HttpVersion: <p>Origin-pull protocol. Supports configuration of 'HTTP/1.1' and 'HTTP/2'.</p><p>Enumeration values:</p><ul><li>HTTP/1.1: version HTTP/1.1</li><li>HTTP/2: version HTTP/2</li></ul><p>This field is required when the origin-pull protocol is HTTPS.</p>
        :type HttpVersion: str
        """
        self._Name = None
        self._EndpointGroupRegion = None
        self._EndpointConfigurations = None
        self._CheckType = None
        self._Description = None
        self._CheckPort = None
        self._ContextType = None
        self._CheckSendContext = None
        self._CheckRecvContext = None
        self._EnableHealthCheck = None
        self._ConnectTimeout = None
        self._HealthCheckInterval = None
        self._UnhealthyThreshold = None
        self._HealthyThreshold = None
        self._ForwardProtocol = None
        self._CheckDomain = None
        self._CheckPath = None
        self._CheckMethod = None
        self._StatusMask = None
        self._PortOverrides = None
        self._IspType = None
        self._CipherPolicyId = None
        self._HttpVersion = None

    @property
    def Name(self):
        r"""<p>Terminal node group name.</p><p>Parameter format: starting with a letter or Chinese characters, 2–128 characters in length, supporting letters, digits, Chinese characters, . - _</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EndpointGroupRegion(self):
        r"""<p>Region of the terminal node group.</p>
        :rtype: str
        """
        return self._EndpointGroupRegion

    @EndpointGroupRegion.setter
    def EndpointGroupRegion(self, EndpointGroupRegion):
        self._EndpointGroupRegion = EndpointGroupRegion

    @property
    def EndpointConfigurations(self):
        r"""<p>Terminal node configuration.</p>
        :rtype: list of EndpointConfigurations
        """
        return self._EndpointConfigurations

    @EndpointConfigurations.setter
    def EndpointConfigurations(self, EndpointConfigurations):
        self._EndpointConfigurations = EndpointConfigurations

    @property
    def CheckType(self):
        r"""<p>Check protocol. Supports configuration of 'TCP', 'HTTP', 'PING', and 'CUSTOM'.</p><p>Enumeration values:</p><ul><li>TCP: When the CLB listener protocol where the terminal node group resides is TCP, choose TCP as the check protocol.</li><li>HTTP: When the CLB listener protocol where the terminal node group resides is HTTP or HTTPS, choose HTTP as the check protocol.</li><li>PING: When the CLB listener protocol where the terminal node group resides is UDP, choose PING as the check protocol.</li><li>CUSTOM: When the CLB listener protocol where the terminal node group resides is UDP or TCP, choose CUSTOM as the check protocol.</li></ul><p>This field is required when health check is enabled.</p>
        :rtype: str
        """
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType

    @property
    def Description(self):
        r"""<p>Description.</p><p>Default value: empty by default, representing no configuration description.</p><p>Maximum length: 100 bytes.</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CheckPort(self):
        r"""<p>Check port.</p><p>Input limit: range 1-65535.</p><p>This field is required when CheckType is CUSTOM.</p>
        :rtype: str
        """
        return self._CheckPort

    @CheckPort.setter
    def CheckPort(self, CheckPort):
        self._CheckPort = CheckPort

    @property
    def ContextType(self):
        r"""<p>Check content. Supports configuration 'TEXT'.</p><p>Enumeration values:</p><ul><li>TEXT: Text content.</li></ul><p>This field is required when CheckType is CUSTOM.</p>
        :rtype: str
        """
        return self._ContextType

    @ContextType.setter
    def ContextType(self, ContextType):
        self._ContextType = ContextType

    @property
    def CheckSendContext(self):
        r"""<p>Check request.</p><p>Input parameter limit: The byte length must be within 1-500.</p><p>This field is required when CheckType is CUSTOM.</p>
        :rtype: str
        """
        return self._CheckSendContext

    @CheckSendContext.setter
    def CheckSendContext(self, CheckSendContext):
        self._CheckSendContext = CheckSendContext

    @property
    def CheckRecvContext(self):
        r"""<p>Check returned results.</p><p>Input parameter limit: The byte length must be within 1-500.</p><p>When CheckType is CUSTOM, this field is required.</p>
        :rtype: str
        """
        return self._CheckRecvContext

    @CheckRecvContext.setter
    def CheckRecvContext(self, CheckRecvContext):
        self._CheckRecvContext = CheckRecvContext

    @property
    def EnableHealthCheck(self):
        r"""<p>Whether to enable health check.</p><p>Default value: False</p>
        :rtype: bool
        """
        return self._EnableHealthCheck

    @EnableHealthCheck.setter
    def EnableHealthCheck(self, EnableHealthCheck):
        self._EnableHealthCheck = EnableHealthCheck

    @property
    def ConnectTimeout(self):
        r"""<p>Response timeout.</p><p>Value range: [1, 100]</p><p>Default value: 2</p><p>This field is required when health check is enabled.</p>
        :rtype: int
        """
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def HealthCheckInterval(self):
        r"""<p>Health check interval.</p><p>Value range: [5, 300].</p><p>Default value: 30.</p><p>This field is required when health check is enabled.</p>
        :rtype: int
        """
        return self._HealthCheckInterval

    @HealthCheckInterval.setter
    def HealthCheckInterval(self, HealthCheckInterval):
        self._HealthCheckInterval = HealthCheckInterval

    @property
    def UnhealthyThreshold(self):
        r"""<p>Unhealthy threshold.</p><p>Value range: [1, 10]</p><p>Default value: 3</p><p>This field is required when health check is enabled.</p>
        :rtype: int
        """
        return self._UnhealthyThreshold

    @UnhealthyThreshold.setter
    def UnhealthyThreshold(self, UnhealthyThreshold):
        self._UnhealthyThreshold = UnhealthyThreshold

    @property
    def HealthyThreshold(self):
        r"""<p>Health threshold.</p><p>Value range: [1, 10]</p><p>Default value: 3</p><p>This field is required when health check is enabled.</p>
        :rtype: int
        """
        return self._HealthyThreshold

    @HealthyThreshold.setter
    def HealthyThreshold(self, HealthyThreshold):
        self._HealthyThreshold = HealthyThreshold

    @property
    def ForwardProtocol(self):
        r"""<p>Origin-pull protocol. HTTP and HTTPS can be configured.</p><p>Enumeration values:</p><ul><li>HTTP: HTTP origin-pull. HTTP can be configured when the listener protocol where the terminal node group resides is HTTP or HTTPS.</li><li>HTTPS: HTTPS origin-pull. HTTPS can be configured when the listener protocol where the terminal node group resides is HTTPS.</li></ul><p>This field is required when the listener protocol where the terminal node group resides is HTTP or HTTPS.</p>
        :rtype: str
        """
        return self._ForwardProtocol

    @ForwardProtocol.setter
    def ForwardProtocol(self, ForwardProtocol):
        self._ForwardProtocol = ForwardProtocol

    @property
    def CheckDomain(self):
        r"""<p>Check domain name.</p><p>Input parameter limit: The byte length range is 3-80.</p><p>This field is required when CheckType is HTTP.</p>
        :rtype: str
        """
        return self._CheckDomain

    @CheckDomain.setter
    def CheckDomain(self, CheckDomain):
        self._CheckDomain = CheckDomain

    @property
    def CheckPath(self):
        r"""<p>Check the URL.</p><p>Parameter format: must match the regular expression: ^[a-zA-Z0-9_.\-\/]{1,80}$</p><p>This field is required when CheckType is HTTP.</p>
        :rtype: str
        """
        return self._CheckPath

    @CheckPath.setter
    def CheckPath(self, CheckPath):
        self._CheckPath = CheckPath

    @property
    def CheckMethod(self):
        r"""<p>Request method. Supports configuration of 'GET' and 'HEAD'.</p><p>Enumeration values:</p><ul><li>GET: The request method is GET.</li><li>HEAD: The request method is HEAD.</li></ul><p>When CheckType is HTTP, this field is required.</p>
        :rtype: str
        """
        return self._CheckMethod

    @CheckMethod.setter
    def CheckMethod(self, CheckMethod):
        self._CheckMethod = CheckMethod

    @property
    def StatusMask(self):
        r"""<p>Status check code. Supports configuring 'http_2xx', 'http_3xx', 'http_4xx', 'http_5xx'.</p><p>Enumeration values:</p><ul><li>http_2xx: HTTP codes beginning with 2.</li><li>http_3xx: HTTP codes beginning with 3.</li><li>http_4xx: HTTP codes beginning with 4.</li><li>http_5xx: HTTP codes beginning with 5.</li></ul><p>This field is required when CheckType is HTTP.</p>
        :rtype: list of str
        """
        return self._StatusMask

    @StatusMask.setter
    def StatusMask(self, StatusMask):
        self._StatusMask = StatusMask

    @property
    def PortOverrides(self):
        r"""<p>Port mapping.</p><p>Input limits: Layer 7 supports 1 port mapping, and Layer 4 supports up to 30 port mappings.</p>
        :rtype: list of PortOverride
        """
        return self._PortOverrides

    @PortOverrides.setter
    def PortOverrides(self, PortOverrides):
        self._PortOverrides = PortOverrides

    @property
    def IspType(self):
        r"""<p>Operator type. Supports configuration 'CMCC', 'CTCC', 'CUCC'.</p><p>Enumeration values:</p><ul><li>CMCC: China Mobile</li><li>CUCC: China Unicom</li><li>CTCC: China Telecom</li></ul><p>This field is required when the terminal node group region is a triple-network region.</p>
        :rtype: str
        """
        return self._IspType

    @IspType.setter
    def IspType(self, IspType):
        self._IspType = IspType

    @property
    def CipherPolicyId(self):
        r"""<p>HPPTS encryption algorithm suite; supports configuration 'tls_policy_1.0-2', 'tls_policy_1.1-2', 'tls_policy_1.2', 'tls_policy_1.2_strict', 'tls_policy_1.2_strict-1.3';</p><p>Enumeration values:</p><ul><li>tls_policy_1.0-2: encryption algorithm suite.</li><li>tls_policy_1.1-2: encryption algorithm suite.</li><li>tls_policy_1.2: encryption algorithm suite.</li><li>tls_policy_1.2_strict: encryption algorithm suite.</li><li>tls_policy_1.2_strict-1.3: encryption algorithm suite.</li></ul><p>This field is required when the origin-pull protocol is HTTPS.</p>
        :rtype: str
        """
        return self._CipherPolicyId

    @CipherPolicyId.setter
    def CipherPolicyId(self, CipherPolicyId):
        self._CipherPolicyId = CipherPolicyId

    @property
    def HttpVersion(self):
        r"""<p>Origin-pull protocol. Supports configuration of 'HTTP/1.1' and 'HTTP/2'.</p><p>Enumeration values:</p><ul><li>HTTP/1.1: version HTTP/1.1</li><li>HTTP/2: version HTTP/2</li></ul><p>This field is required when the origin-pull protocol is HTTPS.</p>
        :rtype: str
        """
        return self._HttpVersion

    @HttpVersion.setter
    def HttpVersion(self, HttpVersion):
        self._HttpVersion = HttpVersion


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._EndpointGroupRegion = params.get("EndpointGroupRegion")
        if params.get("EndpointConfigurations") is not None:
            self._EndpointConfigurations = []
            for item in params.get("EndpointConfigurations"):
                obj = EndpointConfigurations()
                obj._deserialize(item)
                self._EndpointConfigurations.append(obj)
        self._CheckType = params.get("CheckType")
        self._Description = params.get("Description")
        self._CheckPort = params.get("CheckPort")
        self._ContextType = params.get("ContextType")
        self._CheckSendContext = params.get("CheckSendContext")
        self._CheckRecvContext = params.get("CheckRecvContext")
        self._EnableHealthCheck = params.get("EnableHealthCheck")
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._HealthCheckInterval = params.get("HealthCheckInterval")
        self._UnhealthyThreshold = params.get("UnhealthyThreshold")
        self._HealthyThreshold = params.get("HealthyThreshold")
        self._ForwardProtocol = params.get("ForwardProtocol")
        self._CheckDomain = params.get("CheckDomain")
        self._CheckPath = params.get("CheckPath")
        self._CheckMethod = params.get("CheckMethod")
        self._StatusMask = params.get("StatusMask")
        if params.get("PortOverrides") is not None:
            self._PortOverrides = []
            for item in params.get("PortOverrides"):
                obj = PortOverride()
                obj._deserialize(item)
                self._PortOverrides.append(obj)
        self._IspType = params.get("IspType")
        self._CipherPolicyId = params.get("CipherPolicyId")
        self._HttpVersion = params.get("HttpVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EndpointGroupConfigurationSet(AbstractModel):
    r"""Terminal node group information

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>Global acceleration instance ID.</p>
        :type GlobalAcceleratorId: str
        :param _ListenerId: <p>Listener instance ID.</p>
        :type ListenerId: str
        :param _EndpointGroupId: <p>Terminal node group ID.</p>
        :type EndpointGroupId: str
        :param _Name: <p>Name.</p>
        :type Name: str
        :param _EndpointGroupRegion: <p>Region.</p>
        :type EndpointGroupRegion: str
        :param _Description: <p>Description.</p>
        :type Description: str
        :param _EndpointConfigurations: <p>Endpoint information.</p>
        :type EndpointConfigurations: list of EndpointConfigurations
        :param _EnableHealthCheck: <p>Whether to enable health check.</p>
        :type EnableHealthCheck: bool
        :param _ConnectTimeout: <p>Response timeout.</p>
        :type ConnectTimeout: int
        :param _HealthCheckInterval: <p>Health check interval.</p>
        :type HealthCheckInterval: int
        :param _UnhealthyThreshold: <p>Unhealthy threshold.</p>
        :type UnhealthyThreshold: int
        :param _HealthyThreshold: <p>Health threshold.</p>
        :type HealthyThreshold: int
        :param _CheckType: <p>Select the protocol.</p>
        :type CheckType: str
        :param _CheckPort: <p>Check port.</p>
        :type CheckPort: int
        :param _ContextType: <p>Check content.</p>
        :type ContextType: str
        :param _CheckSendContext: <p>Check request.</p>
        :type CheckSendContext: str
        :param _CheckRecvContext: <p>Check returned results.</p>
        :type CheckRecvContext: str
        :param _CheckDomain: <p>Check domain name.</p>
        :type CheckDomain: str
        :param _CheckPath: <p>Check the URL.</p>
        :type CheckPath: str
        :param _CheckMethod: <p>Request method.</p>
        :type CheckMethod: str
        :param _StatusMask: <p>Status check code.</p>
        :type StatusMask: list of str
        :param _EndpointGroupType: <p>Terminal node group type.</p>
        :type EndpointGroupType: str
        :param _ForwardProtocol: <p>Origin-pull protocol.</p>
        :type ForwardProtocol: str
        :param _PortOverrides: <p>Port mapping info.</p>
        :type PortOverrides: list of PortOverride
        :param _VirtualExistForwardingRuleFlag: <p>Whether the custom endpoint group is bound to a Layer 7 forwarding rule.</p>
        :type VirtualExistForwardingRuleFlag: bool
        :param _OriginPublicIps: <p>Public IP address of the egress terminal node group.</p>
        :type OriginPublicIps: list of str
        :param _IspType: <p>Operator type. China Mobile (CMCC), China Unicom (CUCC), China Telecom (CTCC).</p>
        :type IspType: str
        :param _CipherPolicyId: <p>HPPTS encryption algorithm kit</p>
        :type CipherPolicyId: str
        :param _HttpVersion: <p>Only the HTTPS back-to-source protocol supports selecting ['HTTP/1.1', 'HTTP/2']</p><p>Enumeration values:</p><ul><li>HTTP/1.1: Version HTTP/1.1</li><li>HTTP/2: Version HTTP/2</li></ul>
        :type HttpVersion: str
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._EndpointGroupId = None
        self._Name = None
        self._EndpointGroupRegion = None
        self._Description = None
        self._EndpointConfigurations = None
        self._EnableHealthCheck = None
        self._ConnectTimeout = None
        self._HealthCheckInterval = None
        self._UnhealthyThreshold = None
        self._HealthyThreshold = None
        self._CheckType = None
        self._CheckPort = None
        self._ContextType = None
        self._CheckSendContext = None
        self._CheckRecvContext = None
        self._CheckDomain = None
        self._CheckPath = None
        self._CheckMethod = None
        self._StatusMask = None
        self._EndpointGroupType = None
        self._ForwardProtocol = None
        self._PortOverrides = None
        self._VirtualExistForwardingRuleFlag = None
        self._OriginPublicIps = None
        self._IspType = None
        self._CipherPolicyId = None
        self._HttpVersion = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Global acceleration instance ID.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""<p>Listener instance ID.</p>
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def EndpointGroupId(self):
        r"""<p>Terminal node group ID.</p>
        :rtype: str
        """
        return self._EndpointGroupId

    @EndpointGroupId.setter
    def EndpointGroupId(self, EndpointGroupId):
        self._EndpointGroupId = EndpointGroupId

    @property
    def Name(self):
        r"""<p>Name.</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EndpointGroupRegion(self):
        r"""<p>Region.</p>
        :rtype: str
        """
        return self._EndpointGroupRegion

    @EndpointGroupRegion.setter
    def EndpointGroupRegion(self, EndpointGroupRegion):
        self._EndpointGroupRegion = EndpointGroupRegion

    @property
    def Description(self):
        r"""<p>Description.</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def EndpointConfigurations(self):
        r"""<p>Endpoint information.</p>
        :rtype: list of EndpointConfigurations
        """
        return self._EndpointConfigurations

    @EndpointConfigurations.setter
    def EndpointConfigurations(self, EndpointConfigurations):
        self._EndpointConfigurations = EndpointConfigurations

    @property
    def EnableHealthCheck(self):
        r"""<p>Whether to enable health check.</p>
        :rtype: bool
        """
        return self._EnableHealthCheck

    @EnableHealthCheck.setter
    def EnableHealthCheck(self, EnableHealthCheck):
        self._EnableHealthCheck = EnableHealthCheck

    @property
    def ConnectTimeout(self):
        r"""<p>Response timeout.</p>
        :rtype: int
        """
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def HealthCheckInterval(self):
        r"""<p>Health check interval.</p>
        :rtype: int
        """
        return self._HealthCheckInterval

    @HealthCheckInterval.setter
    def HealthCheckInterval(self, HealthCheckInterval):
        self._HealthCheckInterval = HealthCheckInterval

    @property
    def UnhealthyThreshold(self):
        r"""<p>Unhealthy threshold.</p>
        :rtype: int
        """
        return self._UnhealthyThreshold

    @UnhealthyThreshold.setter
    def UnhealthyThreshold(self, UnhealthyThreshold):
        self._UnhealthyThreshold = UnhealthyThreshold

    @property
    def HealthyThreshold(self):
        r"""<p>Health threshold.</p>
        :rtype: int
        """
        return self._HealthyThreshold

    @HealthyThreshold.setter
    def HealthyThreshold(self, HealthyThreshold):
        self._HealthyThreshold = HealthyThreshold

    @property
    def CheckType(self):
        r"""<p>Select the protocol.</p>
        :rtype: str
        """
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType

    @property
    def CheckPort(self):
        r"""<p>Check port.</p>
        :rtype: int
        """
        return self._CheckPort

    @CheckPort.setter
    def CheckPort(self, CheckPort):
        self._CheckPort = CheckPort

    @property
    def ContextType(self):
        r"""<p>Check content.</p>
        :rtype: str
        """
        return self._ContextType

    @ContextType.setter
    def ContextType(self, ContextType):
        self._ContextType = ContextType

    @property
    def CheckSendContext(self):
        r"""<p>Check request.</p>
        :rtype: str
        """
        return self._CheckSendContext

    @CheckSendContext.setter
    def CheckSendContext(self, CheckSendContext):
        self._CheckSendContext = CheckSendContext

    @property
    def CheckRecvContext(self):
        r"""<p>Check returned results.</p>
        :rtype: str
        """
        return self._CheckRecvContext

    @CheckRecvContext.setter
    def CheckRecvContext(self, CheckRecvContext):
        self._CheckRecvContext = CheckRecvContext

    @property
    def CheckDomain(self):
        r"""<p>Check domain name.</p>
        :rtype: str
        """
        return self._CheckDomain

    @CheckDomain.setter
    def CheckDomain(self, CheckDomain):
        self._CheckDomain = CheckDomain

    @property
    def CheckPath(self):
        r"""<p>Check the URL.</p>
        :rtype: str
        """
        return self._CheckPath

    @CheckPath.setter
    def CheckPath(self, CheckPath):
        self._CheckPath = CheckPath

    @property
    def CheckMethod(self):
        r"""<p>Request method.</p>
        :rtype: str
        """
        return self._CheckMethod

    @CheckMethod.setter
    def CheckMethod(self, CheckMethod):
        self._CheckMethod = CheckMethod

    @property
    def StatusMask(self):
        r"""<p>Status check code.</p>
        :rtype: list of str
        """
        return self._StatusMask

    @StatusMask.setter
    def StatusMask(self, StatusMask):
        self._StatusMask = StatusMask

    @property
    def EndpointGroupType(self):
        r"""<p>Terminal node group type.</p>
        :rtype: str
        """
        return self._EndpointGroupType

    @EndpointGroupType.setter
    def EndpointGroupType(self, EndpointGroupType):
        self._EndpointGroupType = EndpointGroupType

    @property
    def ForwardProtocol(self):
        r"""<p>Origin-pull protocol.</p>
        :rtype: str
        """
        return self._ForwardProtocol

    @ForwardProtocol.setter
    def ForwardProtocol(self, ForwardProtocol):
        self._ForwardProtocol = ForwardProtocol

    @property
    def PortOverrides(self):
        r"""<p>Port mapping info.</p>
        :rtype: list of PortOverride
        """
        return self._PortOverrides

    @PortOverrides.setter
    def PortOverrides(self, PortOverrides):
        self._PortOverrides = PortOverrides

    @property
    def VirtualExistForwardingRuleFlag(self):
        r"""<p>Whether the custom endpoint group is bound to a Layer 7 forwarding rule.</p>
        :rtype: bool
        """
        return self._VirtualExistForwardingRuleFlag

    @VirtualExistForwardingRuleFlag.setter
    def VirtualExistForwardingRuleFlag(self, VirtualExistForwardingRuleFlag):
        self._VirtualExistForwardingRuleFlag = VirtualExistForwardingRuleFlag

    @property
    def OriginPublicIps(self):
        r"""<p>Public IP address of the egress terminal node group.</p>
        :rtype: list of str
        """
        return self._OriginPublicIps

    @OriginPublicIps.setter
    def OriginPublicIps(self, OriginPublicIps):
        self._OriginPublicIps = OriginPublicIps

    @property
    def IspType(self):
        r"""<p>Operator type. China Mobile (CMCC), China Unicom (CUCC), China Telecom (CTCC).</p>
        :rtype: str
        """
        return self._IspType

    @IspType.setter
    def IspType(self, IspType):
        self._IspType = IspType

    @property
    def CipherPolicyId(self):
        r"""<p>HPPTS encryption algorithm kit</p>
        :rtype: str
        """
        return self._CipherPolicyId

    @CipherPolicyId.setter
    def CipherPolicyId(self, CipherPolicyId):
        self._CipherPolicyId = CipherPolicyId

    @property
    def HttpVersion(self):
        r"""<p>Only the HTTPS back-to-source protocol supports selecting ['HTTP/1.1', 'HTTP/2']</p><p>Enumeration values:</p><ul><li>HTTP/1.1: Version HTTP/1.1</li><li>HTTP/2: Version HTTP/2</li></ul>
        :rtype: str
        """
        return self._HttpVersion

    @HttpVersion.setter
    def HttpVersion(self, HttpVersion):
        self._HttpVersion = HttpVersion


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._EndpointGroupId = params.get("EndpointGroupId")
        self._Name = params.get("Name")
        self._EndpointGroupRegion = params.get("EndpointGroupRegion")
        self._Description = params.get("Description")
        if params.get("EndpointConfigurations") is not None:
            self._EndpointConfigurations = []
            for item in params.get("EndpointConfigurations"):
                obj = EndpointConfigurations()
                obj._deserialize(item)
                self._EndpointConfigurations.append(obj)
        self._EnableHealthCheck = params.get("EnableHealthCheck")
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._HealthCheckInterval = params.get("HealthCheckInterval")
        self._UnhealthyThreshold = params.get("UnhealthyThreshold")
        self._HealthyThreshold = params.get("HealthyThreshold")
        self._CheckType = params.get("CheckType")
        self._CheckPort = params.get("CheckPort")
        self._ContextType = params.get("ContextType")
        self._CheckSendContext = params.get("CheckSendContext")
        self._CheckRecvContext = params.get("CheckRecvContext")
        self._CheckDomain = params.get("CheckDomain")
        self._CheckPath = params.get("CheckPath")
        self._CheckMethod = params.get("CheckMethod")
        self._StatusMask = params.get("StatusMask")
        self._EndpointGroupType = params.get("EndpointGroupType")
        self._ForwardProtocol = params.get("ForwardProtocol")
        if params.get("PortOverrides") is not None:
            self._PortOverrides = []
            for item in params.get("PortOverrides"):
                obj = PortOverride()
                obj._deserialize(item)
                self._PortOverrides.append(obj)
        self._VirtualExistForwardingRuleFlag = params.get("VirtualExistForwardingRuleFlag")
        self._OriginPublicIps = params.get("OriginPublicIps")
        self._IspType = params.get("IspType")
        self._CipherPolicyId = params.get("CipherPolicyId")
        self._HttpVersion = params.get("HttpVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""Filter.

    """

    def __init__(self):
        r"""
        :param _Name: Attribute name. If more than one Filter exists, the logical relation between these Filters is `AND`.
        :type Name: str
        :param _Values: Attribute value. If a filter has multiple values, the relationship among the values under the same filter is logical OR (OR). When the value type is boolean, it can be directly set to the string "TRUE" or "FALSE".
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""Attribute name. If more than one Filter exists, the logical relation between these Filters is `AND`.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""Attribute value. If a filter has multiple values, the relationship among the values under the same filter is logical OR (OR). When the value type is boolean, it can be directly set to the string "TRUE" or "FALSE".
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
        


class ForwardingPolicySet(AbstractModel):
    r"""Layer-7 forwarding policy information

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: Global acceleration instance ID.
        :type GlobalAcceleratorId: str
        :param _ListenerId: Listener ID.
        :type ListenerId: str
        :param _ForwardingPolicyId: Policy ID.
        :type ForwardingPolicyId: str
        :param _Host: Domain name.
        :type Host: str
        :param _DefaultHostFlag: Whether it is the default domain name.
        :type DefaultHostFlag: bool
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._ForwardingPolicyId = None
        self._Host = None
        self._DefaultHostFlag = None

    @property
    def GlobalAcceleratorId(self):
        r"""Global acceleration instance ID.
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""Listener ID.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ForwardingPolicyId(self):
        r"""Policy ID.
        :rtype: str
        """
        return self._ForwardingPolicyId

    @ForwardingPolicyId.setter
    def ForwardingPolicyId(self, ForwardingPolicyId):
        self._ForwardingPolicyId = ForwardingPolicyId

    @property
    def Host(self):
        r"""Domain name.
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def DefaultHostFlag(self):
        r"""Whether it is the default domain name.
        :rtype: bool
        """
        return self._DefaultHostFlag

    @DefaultHostFlag.setter
    def DefaultHostFlag(self, DefaultHostFlag):
        self._DefaultHostFlag = DefaultHostFlag


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._ForwardingPolicyId = params.get("ForwardingPolicyId")
        self._Host = params.get("Host")
        self._DefaultHostFlag = params.get("DefaultHostFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForwardingRuleSet(AbstractModel):
    r"""Layer-7 forwarding rule information

    """

    def __init__(self):
        r"""
        :param _RuleCondition: <p>Conditional information of Layer 7 forwarding rules.</p>
        :type RuleCondition: list of RuleCondition
        :param _RuleAction: <p>Behavior information of the Layer 7 forwarding rule.</p>
        :type RuleAction: list of RuleAction
        :param _EnableOriginSni: <p>Whether to enable origin-pull Sni.</p>
        :type EnableOriginSni: bool
        :param _OriginSni: <p>Origin-pull Sni.</p>
        :type OriginSni: str
        :param _OriginHeaders: <p>Origin-pull Header information.</p>
        :type OriginHeaders: list of OriginHeader
        :param _OriginHost: <p>Origin-pull Host.</p>
        :type OriginHost: str
        :param _GlobalAcceleratorId: <p>Global acceleration instance ID.</p>
        :type GlobalAcceleratorId: str
        :param _ListenerId: <p>Listener ID.</p>
        :type ListenerId: str
        :param _ForwardingPolicyId: <p>Layer-7 forwarding policy ID.</p>
        :type ForwardingPolicyId: str
        :param _ForwardingRuleId: <p>Layer 7 forwarding rule ID.</p>
        :type ForwardingRuleId: str
        :param _HideResponseHeaders: <p>Origin server response header</p>
        :type HideResponseHeaders: list of HideResponseHeaders
        :param _ResponseHeaders: <p>Delete origin server response headers</p>
        :type ResponseHeaders: list of ResponseHeaders
        """
        self._RuleCondition = None
        self._RuleAction = None
        self._EnableOriginSni = None
        self._OriginSni = None
        self._OriginHeaders = None
        self._OriginHost = None
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._ForwardingPolicyId = None
        self._ForwardingRuleId = None
        self._HideResponseHeaders = None
        self._ResponseHeaders = None

    @property
    def RuleCondition(self):
        r"""<p>Conditional information of Layer 7 forwarding rules.</p>
        :rtype: list of RuleCondition
        """
        return self._RuleCondition

    @RuleCondition.setter
    def RuleCondition(self, RuleCondition):
        self._RuleCondition = RuleCondition

    @property
    def RuleAction(self):
        r"""<p>Behavior information of the Layer 7 forwarding rule.</p>
        :rtype: list of RuleAction
        """
        return self._RuleAction

    @RuleAction.setter
    def RuleAction(self, RuleAction):
        self._RuleAction = RuleAction

    @property
    def EnableOriginSni(self):
        r"""<p>Whether to enable origin-pull Sni.</p>
        :rtype: bool
        """
        return self._EnableOriginSni

    @EnableOriginSni.setter
    def EnableOriginSni(self, EnableOriginSni):
        self._EnableOriginSni = EnableOriginSni

    @property
    def OriginSni(self):
        r"""<p>Origin-pull Sni.</p>
        :rtype: str
        """
        return self._OriginSni

    @OriginSni.setter
    def OriginSni(self, OriginSni):
        self._OriginSni = OriginSni

    @property
    def OriginHeaders(self):
        r"""<p>Origin-pull Header information.</p>
        :rtype: list of OriginHeader
        """
        return self._OriginHeaders

    @OriginHeaders.setter
    def OriginHeaders(self, OriginHeaders):
        self._OriginHeaders = OriginHeaders

    @property
    def OriginHost(self):
        r"""<p>Origin-pull Host.</p>
        :rtype: str
        """
        return self._OriginHost

    @OriginHost.setter
    def OriginHost(self, OriginHost):
        self._OriginHost = OriginHost

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Global acceleration instance ID.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""<p>Listener ID.</p>
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ForwardingPolicyId(self):
        r"""<p>Layer-7 forwarding policy ID.</p>
        :rtype: str
        """
        return self._ForwardingPolicyId

    @ForwardingPolicyId.setter
    def ForwardingPolicyId(self, ForwardingPolicyId):
        self._ForwardingPolicyId = ForwardingPolicyId

    @property
    def ForwardingRuleId(self):
        r"""<p>Layer 7 forwarding rule ID.</p>
        :rtype: str
        """
        return self._ForwardingRuleId

    @ForwardingRuleId.setter
    def ForwardingRuleId(self, ForwardingRuleId):
        self._ForwardingRuleId = ForwardingRuleId

    @property
    def HideResponseHeaders(self):
        r"""<p>Origin server response header</p>
        :rtype: list of HideResponseHeaders
        """
        return self._HideResponseHeaders

    @HideResponseHeaders.setter
    def HideResponseHeaders(self, HideResponseHeaders):
        self._HideResponseHeaders = HideResponseHeaders

    @property
    def ResponseHeaders(self):
        r"""<p>Delete origin server response headers</p>
        :rtype: list of ResponseHeaders
        """
        return self._ResponseHeaders

    @ResponseHeaders.setter
    def ResponseHeaders(self, ResponseHeaders):
        self._ResponseHeaders = ResponseHeaders


    def _deserialize(self, params):
        if params.get("RuleCondition") is not None:
            self._RuleCondition = []
            for item in params.get("RuleCondition"):
                obj = RuleCondition()
                obj._deserialize(item)
                self._RuleCondition.append(obj)
        if params.get("RuleAction") is not None:
            self._RuleAction = []
            for item in params.get("RuleAction"):
                obj = RuleAction()
                obj._deserialize(item)
                self._RuleAction.append(obj)
        self._EnableOriginSni = params.get("EnableOriginSni")
        self._OriginSni = params.get("OriginSni")
        if params.get("OriginHeaders") is not None:
            self._OriginHeaders = []
            for item in params.get("OriginHeaders"):
                obj = OriginHeader()
                obj._deserialize(item)
                self._OriginHeaders.append(obj)
        self._OriginHost = params.get("OriginHost")
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._ForwardingPolicyId = params.get("ForwardingPolicyId")
        self._ForwardingRuleId = params.get("ForwardingRuleId")
        if params.get("HideResponseHeaders") is not None:
            self._HideResponseHeaders = []
            for item in params.get("HideResponseHeaders"):
                obj = HideResponseHeaders()
                obj._deserialize(item)
                self._HideResponseHeaders.append(obj)
        if params.get("ResponseHeaders") is not None:
            self._ResponseHeaders = []
            for item in params.get("ResponseHeaders"):
                obj = ResponseHeaders()
                obj._deserialize(item)
                self._ResponseHeaders.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GlobalAcceleratorAccessLog(AbstractModel):
    r"""GA access log

    """

    def __init__(self):
        r"""
        :param _LogPushTaskId: <p>Log Unique Id</p>
        :type LogPushTaskId: str
        :param _GlobalAcceleratorId: <p>Unique Id of the GA instance.</p>
        :type GlobalAcceleratorId: str
        :param _ListenerId: <p>Unique Id of the listener</p>
        :type ListenerId: str
        :param _EndpointGroupId: <p>Unique Id of the terminal node group</p>
        :type EndpointGroupId: str
        :param _FlowLogDescription: <p>Log task description</p>
        :type FlowLogDescription: str
        :param _CloudRegion: <p>Region where the logs are located.</p>
        :type CloudRegion: str
        :param _CloudLogId: <p>Log topic Id</p>
        :type CloudLogId: str
        :param _CloudLogSetId: <p>Log Set Id</p>
        :type CloudLogSetId: str
        :param _FieldKeys: <p>Select log data collection field</p>
        :type FieldKeys: list of str
        :param _Status: <p>Log task status</p><p>Enumeration values:</p><ul><li>active: Running</li><li>stopped: Suspended</li></ul>
        :type Status: str
        """
        self._LogPushTaskId = None
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._EndpointGroupId = None
        self._FlowLogDescription = None
        self._CloudRegion = None
        self._CloudLogId = None
        self._CloudLogSetId = None
        self._FieldKeys = None
        self._Status = None

    @property
    def LogPushTaskId(self):
        r"""<p>Log Unique Id</p>
        :rtype: str
        """
        return self._LogPushTaskId

    @LogPushTaskId.setter
    def LogPushTaskId(self, LogPushTaskId):
        self._LogPushTaskId = LogPushTaskId

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Unique Id of the GA instance.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""<p>Unique Id of the listener</p>
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def EndpointGroupId(self):
        r"""<p>Unique Id of the terminal node group</p>
        :rtype: str
        """
        return self._EndpointGroupId

    @EndpointGroupId.setter
    def EndpointGroupId(self, EndpointGroupId):
        self._EndpointGroupId = EndpointGroupId

    @property
    def FlowLogDescription(self):
        r"""<p>Log task description</p>
        :rtype: str
        """
        return self._FlowLogDescription

    @FlowLogDescription.setter
    def FlowLogDescription(self, FlowLogDescription):
        self._FlowLogDescription = FlowLogDescription

    @property
    def CloudRegion(self):
        r"""<p>Region where the logs are located.</p>
        :rtype: str
        """
        return self._CloudRegion

    @CloudRegion.setter
    def CloudRegion(self, CloudRegion):
        self._CloudRegion = CloudRegion

    @property
    def CloudLogId(self):
        r"""<p>Log topic Id</p>
        :rtype: str
        """
        return self._CloudLogId

    @CloudLogId.setter
    def CloudLogId(self, CloudLogId):
        self._CloudLogId = CloudLogId

    @property
    def CloudLogSetId(self):
        r"""<p>Log Set Id</p>
        :rtype: str
        """
        return self._CloudLogSetId

    @CloudLogSetId.setter
    def CloudLogSetId(self, CloudLogSetId):
        self._CloudLogSetId = CloudLogSetId

    @property
    def FieldKeys(self):
        r"""<p>Select log data collection field</p>
        :rtype: list of str
        """
        return self._FieldKeys

    @FieldKeys.setter
    def FieldKeys(self, FieldKeys):
        self._FieldKeys = FieldKeys

    @property
    def Status(self):
        r"""<p>Log task status</p><p>Enumeration values:</p><ul><li>active: Running</li><li>stopped: Suspended</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._LogPushTaskId = params.get("LogPushTaskId")
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._EndpointGroupId = params.get("EndpointGroupId")
        self._FlowLogDescription = params.get("FlowLogDescription")
        self._CloudRegion = params.get("CloudRegion")
        self._CloudLogId = params.get("CloudLogId")
        self._CloudLogSetId = params.get("CloudLogSetId")
        self._FieldKeys = params.get("FieldKeys")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GlobalAcceleratorAclPolicies(AbstractModel):
    r"""Access control policy

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorAclPolicyId: Access control policy ID.
        :type GlobalAcceleratorAclPolicyId: str
        :param _DefaultAction: Default action.
        :type DefaultAction: str
        :param _Status: Status.
        :type Status: str
        """
        self._GlobalAcceleratorAclPolicyId = None
        self._DefaultAction = None
        self._Status = None

    @property
    def GlobalAcceleratorAclPolicyId(self):
        r"""Access control policy ID.
        :rtype: str
        """
        return self._GlobalAcceleratorAclPolicyId

    @GlobalAcceleratorAclPolicyId.setter
    def GlobalAcceleratorAclPolicyId(self, GlobalAcceleratorAclPolicyId):
        self._GlobalAcceleratorAclPolicyId = GlobalAcceleratorAclPolicyId

    @property
    def DefaultAction(self):
        r"""Default action.
        :rtype: str
        """
        return self._DefaultAction

    @DefaultAction.setter
    def DefaultAction(self, DefaultAction):
        self._DefaultAction = DefaultAction

    @property
    def Status(self):
        r"""Status.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._GlobalAcceleratorAclPolicyId = params.get("GlobalAcceleratorAclPolicyId")
        self._DefaultAction = params.get("DefaultAction")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GlobalAcceleratorAclRuleSet(AbstractModel):
    r"""Acl rule information

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorPolicyId: Access control policy ID.
        :type GlobalAcceleratorPolicyId: str
        :param _GlobalAcceleratorAclRuleId: Acl rule ID.
        :type GlobalAcceleratorAclRuleId: str
        :param _Protocol: Protocol.
        :type Protocol: str
        :param _Port: Port.
        :type Port: str
        :param _SourceCidrBlock: IP range.
        :type SourceCidrBlock: str
        :param _Policy: Action.
        :type Policy: str
        :param _Description: Description.
        :type Description: str
        """
        self._GlobalAcceleratorPolicyId = None
        self._GlobalAcceleratorAclRuleId = None
        self._Protocol = None
        self._Port = None
        self._SourceCidrBlock = None
        self._Policy = None
        self._Description = None

    @property
    def GlobalAcceleratorPolicyId(self):
        r"""Access control policy ID.
        :rtype: str
        """
        return self._GlobalAcceleratorPolicyId

    @GlobalAcceleratorPolicyId.setter
    def GlobalAcceleratorPolicyId(self, GlobalAcceleratorPolicyId):
        self._GlobalAcceleratorPolicyId = GlobalAcceleratorPolicyId

    @property
    def GlobalAcceleratorAclRuleId(self):
        r"""Acl rule ID.
        :rtype: str
        """
        return self._GlobalAcceleratorAclRuleId

    @GlobalAcceleratorAclRuleId.setter
    def GlobalAcceleratorAclRuleId(self, GlobalAcceleratorAclRuleId):
        self._GlobalAcceleratorAclRuleId = GlobalAcceleratorAclRuleId

    @property
    def Protocol(self):
        r"""Protocol.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        r"""Port.
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def SourceCidrBlock(self):
        r"""IP range.
        :rtype: str
        """
        return self._SourceCidrBlock

    @SourceCidrBlock.setter
    def SourceCidrBlock(self, SourceCidrBlock):
        self._SourceCidrBlock = SourceCidrBlock

    @property
    def Policy(self):
        r"""Action.
        :rtype: str
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def Description(self):
        r"""Description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._GlobalAcceleratorPolicyId = params.get("GlobalAcceleratorPolicyId")
        self._GlobalAcceleratorAclRuleId = params.get("GlobalAcceleratorAclRuleId")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._SourceCidrBlock = params.get("SourceCidrBlock")
        self._Policy = params.get("Policy")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GlobalAcceleratorSet(AbstractModel):
    r"""Global acceleration instance information

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>Global acceleration instance ID.</p>
        :type GlobalAcceleratorId: str
        :param _Name: <p>Global acceleration instance name.</p>
        :type Name: str
        :param _Description: <p>Global acceleration instance description.</p>
        :type Description: str
        :param _CreateTime: <p>Instance creation time of the global acceleration instance.</p>
        :type CreateTime: str
        :param _State: <p>Global acceleration instance status.</p>
        :type State: str
        :param _InstanceChargeType: <p>Billing type of a global acceleration instance.</p>
        :type InstanceChargeType: str
        :param _DdosId: <p>DDoS ID of the global acceleration instance.</p>
        :type DdosId: str
        :param _ListenerCounts: <p>Number of listeners of the associated acceleration instance.</p>
        :type ListenerCounts: int
        :param _AcceleratorAreaCounts: <p>Count of acceleration regions belonging to the acceleration instance.</p>
        :type AcceleratorAreaCounts: int
        :param _Status: <p>Global acceleration instance status.</p>
        :type Status: str
        :param _Cname: <p>Domain name.</p>
        :type Cname: str
        :param _CrossBorderType: <p>Cross-border type; HighQuality (high-quality cross-border), Unicom (China Unicom cross-border), NotAvailable (not enabled).</p>
        :type CrossBorderType: str
        :param _TagSet: <p>Tag information.</p>
        :type TagSet: list of Tag
        """
        self._GlobalAcceleratorId = None
        self._Name = None
        self._Description = None
        self._CreateTime = None
        self._State = None
        self._InstanceChargeType = None
        self._DdosId = None
        self._ListenerCounts = None
        self._AcceleratorAreaCounts = None
        self._Status = None
        self._Cname = None
        self._CrossBorderType = None
        self._TagSet = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Global acceleration instance ID.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def Name(self):
        r"""<p>Global acceleration instance name.</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>Global acceleration instance description.</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        r"""<p>Instance creation time of the global acceleration instance.</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def State(self):
        r"""<p>Global acceleration instance status.</p>
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def InstanceChargeType(self):
        r"""<p>Billing type of a global acceleration instance.</p>
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def DdosId(self):
        r"""<p>DDoS ID of the global acceleration instance.</p>
        :rtype: str
        """
        return self._DdosId

    @DdosId.setter
    def DdosId(self, DdosId):
        self._DdosId = DdosId

    @property
    def ListenerCounts(self):
        r"""<p>Number of listeners of the associated acceleration instance.</p>
        :rtype: int
        """
        return self._ListenerCounts

    @ListenerCounts.setter
    def ListenerCounts(self, ListenerCounts):
        self._ListenerCounts = ListenerCounts

    @property
    def AcceleratorAreaCounts(self):
        r"""<p>Count of acceleration regions belonging to the acceleration instance.</p>
        :rtype: int
        """
        return self._AcceleratorAreaCounts

    @AcceleratorAreaCounts.setter
    def AcceleratorAreaCounts(self, AcceleratorAreaCounts):
        self._AcceleratorAreaCounts = AcceleratorAreaCounts

    @property
    def Status(self):
        r"""<p>Global acceleration instance status.</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Cname(self):
        r"""<p>Domain name.</p>
        :rtype: str
        """
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def CrossBorderType(self):
        r"""<p>Cross-border type; HighQuality (high-quality cross-border), Unicom (China Unicom cross-border), NotAvailable (not enabled).</p>
        :rtype: str
        """
        return self._CrossBorderType

    @CrossBorderType.setter
    def CrossBorderType(self, CrossBorderType):
        self._CrossBorderType = CrossBorderType

    @property
    def TagSet(self):
        r"""<p>Tag information.</p>
        :rtype: list of Tag
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._State = params.get("State")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._DdosId = params.get("DdosId")
        self._ListenerCounts = params.get("ListenerCounts")
        self._AcceleratorAreaCounts = params.get("AcceleratorAreaCounts")
        self._Status = params.get("Status")
        self._Cname = params.get("Cname")
        self._CrossBorderType = params.get("CrossBorderType")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self._TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HideResponseHeaders(AbstractModel):
    r"""Hide Header

    """

    def __init__(self):
        r"""
        :param _Key: <p>key</p><p>Parameter format: 1. The string only contain printable ASCII characters. 2. Cannot contain these characters ()&lt;&gt;@,;:\&quot;/[ ]?={ }</p><p>Input limit: Length 1-40.</p>
        :type Key: str
        :param _Value: <p>value</p><p>Currently only support inputting an empty string ""</p>
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""<p>key</p><p>Parameter format: 1. The string only contain printable ASCII characters. 2. Cannot contain these characters ()&lt;&gt;@,;:\&quot;/[ ]?={ }</p><p>Input limit: Length 1-40.</p>
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""<p>value</p><p>Currently only support inputting an empty string ""</p>
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpAddressInfoSet(AbstractModel):
    r"""Public IP information in the acceleration region

    """

    def __init__(self):
        r"""
        :param _IpAddress: <p>IP address.</p>
        :type IpAddress: str
        :param _IspType: <p>IP type.</p>
        :type IspType: str
        :param _DdosProtectionType: <p>Ddos type</p>
        :type DdosProtectionType: str
        """
        self._IpAddress = None
        self._IspType = None
        self._DdosProtectionType = None

    @property
    def IpAddress(self):
        r"""<p>IP address.</p>
        :rtype: str
        """
        return self._IpAddress

    @IpAddress.setter
    def IpAddress(self, IpAddress):
        self._IpAddress = IpAddress

    @property
    def IspType(self):
        r"""<p>IP type.</p>
        :rtype: str
        """
        return self._IspType

    @IspType.setter
    def IspType(self, IspType):
        self._IspType = IspType

    @property
    def DdosProtectionType(self):
        r"""<p>Ddos type</p>
        :rtype: str
        """
        return self._DdosProtectionType

    @DdosProtectionType.setter
    def DdosProtectionType(self, DdosProtectionType):
        self._DdosProtectionType = DdosProtectionType


    def _deserialize(self, params):
        self._IpAddress = params.get("IpAddress")
        self._IspType = params.get("IspType")
        self._DdosProtectionType = params.get("DdosProtectionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListenerSet(AbstractModel):
    r"""Listener information

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: Global acceleration instance ID.
        :type GlobalAcceleratorId: str
        :param _ListenerId: Listener ID.
        :type ListenerId: str
        :param _Name: Listener name.
        :type Name: str
        :param _Description: Listener description.
        :type Description: str
        :param _Protocol: Protocol.
        :type Protocol: str
        :param _PortRanges: Port range.
        :type PortRanges: :class:`tencentcloud.ga2.v20250115.models.PortRanges`
        :param _XForwardedForRealIp: Whether to enable layer-7 access to source IP mode.
        :type XForwardedForRealIp: bool
        :param _ClientAffinity: Enable session persistence.
        :type ClientAffinity: str
        :param _ClientAffinityTime: Session persistence time.
        :type ClientAffinityTime: int
        :param _CertificationType: SSL decryption method.
        :type CertificationType: str
        :param _ServerCertificates: Server certificate.
        :type ServerCertificates: list of str
        :param _ClientCaCertificates: Client certificate.
        :type ClientCaCertificates: list of str
        :param _CipherPolicyId: TLS password suite package.
        :type CipherPolicyId: str
        :param _HttpVersion: HTTP version.
        :type HttpVersion: str
        :param _RequestTimeout: Request timeout.
        :type RequestTimeout: int
        :param _CreateTime: Creation time.
        :type CreateTime: str
        :param _ListenerType: Listener routing type.
        :type ListenerType: str
        :param _Status: Listener status.
        :type Status: str
        :param _EndpointGroupCounts: Number of terminal node groups belonging to the listener.
        :type EndpointGroupCounts: int
        :param _GetRealIpType: Method for obtaining the source IP at Layer 4.
        :type GetRealIpType: str
        :param _IdleTimeout: Connection timeout.
        :type IdleTimeout: int
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._Name = None
        self._Description = None
        self._Protocol = None
        self._PortRanges = None
        self._XForwardedForRealIp = None
        self._ClientAffinity = None
        self._ClientAffinityTime = None
        self._CertificationType = None
        self._ServerCertificates = None
        self._ClientCaCertificates = None
        self._CipherPolicyId = None
        self._HttpVersion = None
        self._RequestTimeout = None
        self._CreateTime = None
        self._ListenerType = None
        self._Status = None
        self._EndpointGroupCounts = None
        self._GetRealIpType = None
        self._IdleTimeout = None

    @property
    def GlobalAcceleratorId(self):
        r"""Global acceleration instance ID.
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""Listener ID.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Name(self):
        r"""Listener name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""Listener description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Protocol(self):
        r"""Protocol.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def PortRanges(self):
        r"""Port range.
        :rtype: :class:`tencentcloud.ga2.v20250115.models.PortRanges`
        """
        return self._PortRanges

    @PortRanges.setter
    def PortRanges(self, PortRanges):
        self._PortRanges = PortRanges

    @property
    def XForwardedForRealIp(self):
        r"""Whether to enable layer-7 access to source IP mode.
        :rtype: bool
        """
        return self._XForwardedForRealIp

    @XForwardedForRealIp.setter
    def XForwardedForRealIp(self, XForwardedForRealIp):
        self._XForwardedForRealIp = XForwardedForRealIp

    @property
    def ClientAffinity(self):
        r"""Enable session persistence.
        :rtype: str
        """
        return self._ClientAffinity

    @ClientAffinity.setter
    def ClientAffinity(self, ClientAffinity):
        self._ClientAffinity = ClientAffinity

    @property
    def ClientAffinityTime(self):
        r"""Session persistence time.
        :rtype: int
        """
        return self._ClientAffinityTime

    @ClientAffinityTime.setter
    def ClientAffinityTime(self, ClientAffinityTime):
        self._ClientAffinityTime = ClientAffinityTime

    @property
    def CertificationType(self):
        r"""SSL decryption method.
        :rtype: str
        """
        return self._CertificationType

    @CertificationType.setter
    def CertificationType(self, CertificationType):
        self._CertificationType = CertificationType

    @property
    def ServerCertificates(self):
        r"""Server certificate.
        :rtype: list of str
        """
        return self._ServerCertificates

    @ServerCertificates.setter
    def ServerCertificates(self, ServerCertificates):
        self._ServerCertificates = ServerCertificates

    @property
    def ClientCaCertificates(self):
        r"""Client certificate.
        :rtype: list of str
        """
        return self._ClientCaCertificates

    @ClientCaCertificates.setter
    def ClientCaCertificates(self, ClientCaCertificates):
        self._ClientCaCertificates = ClientCaCertificates

    @property
    def CipherPolicyId(self):
        r"""TLS password suite package.
        :rtype: str
        """
        return self._CipherPolicyId

    @CipherPolicyId.setter
    def CipherPolicyId(self, CipherPolicyId):
        self._CipherPolicyId = CipherPolicyId

    @property
    def HttpVersion(self):
        r"""HTTP version.
        :rtype: str
        """
        return self._HttpVersion

    @HttpVersion.setter
    def HttpVersion(self, HttpVersion):
        self._HttpVersion = HttpVersion

    @property
    def RequestTimeout(self):
        r"""Request timeout.
        :rtype: int
        """
        return self._RequestTimeout

    @RequestTimeout.setter
    def RequestTimeout(self, RequestTimeout):
        self._RequestTimeout = RequestTimeout

    @property
    def CreateTime(self):
        r"""Creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ListenerType(self):
        r"""Listener routing type.
        :rtype: str
        """
        return self._ListenerType

    @ListenerType.setter
    def ListenerType(self, ListenerType):
        self._ListenerType = ListenerType

    @property
    def Status(self):
        r"""Listener status.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EndpointGroupCounts(self):
        r"""Number of terminal node groups belonging to the listener.
        :rtype: int
        """
        return self._EndpointGroupCounts

    @EndpointGroupCounts.setter
    def EndpointGroupCounts(self, EndpointGroupCounts):
        self._EndpointGroupCounts = EndpointGroupCounts

    @property
    def GetRealIpType(self):
        r"""Method for obtaining the source IP at Layer 4.
        :rtype: str
        """
        return self._GetRealIpType

    @GetRealIpType.setter
    def GetRealIpType(self, GetRealIpType):
        self._GetRealIpType = GetRealIpType

    @property
    def IdleTimeout(self):
        r"""Connection timeout.
        :rtype: int
        """
        return self._IdleTimeout

    @IdleTimeout.setter
    def IdleTimeout(self, IdleTimeout):
        self._IdleTimeout = IdleTimeout


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Protocol = params.get("Protocol")
        if params.get("PortRanges") is not None:
            self._PortRanges = PortRanges()
            self._PortRanges._deserialize(params.get("PortRanges"))
        self._XForwardedForRealIp = params.get("XForwardedForRealIp")
        self._ClientAffinity = params.get("ClientAffinity")
        self._ClientAffinityTime = params.get("ClientAffinityTime")
        self._CertificationType = params.get("CertificationType")
        self._ServerCertificates = params.get("ServerCertificates")
        self._ClientCaCertificates = params.get("ClientCaCertificates")
        self._CipherPolicyId = params.get("CipherPolicyId")
        self._HttpVersion = params.get("HttpVersion")
        self._RequestTimeout = params.get("RequestTimeout")
        self._CreateTime = params.get("CreateTime")
        self._ListenerType = params.get("ListenerType")
        self._Status = params.get("Status")
        self._EndpointGroupCounts = params.get("EndpointGroupCounts")
        self._GetRealIpType = params.get("GetRealIpType")
        self._IdleTimeout = params.get("IdleTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccelerateAreasRequest(AbstractModel):
    r"""ModifyAccelerateAreas request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>Global acceleration instance ID.</p>
        :type GlobalAcceleratorId: str
        :param _AcceleratorAreas: <p>Acceleration region info.</p><p>Input limit: array length cannot exceed 10.</p>
        :type AcceleratorAreas: list of AcceleratorAreas
        """
        self._GlobalAcceleratorId = None
        self._AcceleratorAreas = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Global acceleration instance ID.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def AcceleratorAreas(self):
        r"""<p>Acceleration region info.</p><p>Input limit: array length cannot exceed 10.</p>
        :rtype: list of AcceleratorAreas
        """
        return self._AcceleratorAreas

    @AcceleratorAreas.setter
    def AcceleratorAreas(self, AcceleratorAreas):
        self._AcceleratorAreas = AcceleratorAreas


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        if params.get("AcceleratorAreas") is not None:
            self._AcceleratorAreas = []
            for item in params.get("AcceleratorAreas"):
                obj = AcceleratorAreas()
                obj._deserialize(item)
                self._AcceleratorAreas.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccelerateAreasResponse(AbstractModel):
    r"""ModifyAccelerateAreas response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>Asynchronous task ID.</p>
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>Asynchronous task ID.</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyAccessLogStatusRequest(AbstractModel):
    r"""ModifyAccessLogStatus request structure.

    """

    def __init__(self):
        r"""
        :param _LogPushTaskId: <p>Log Unique Id</p>
        :type LogPushTaskId: str
        :param _Status: <p>Status (Start START, Stop STOP)</p><p>Enumeration values:</p><ul><li>START: Start</li><li>STOP: Stop</li></ul>
        :type Status: str
        :param _GlobalAcceleratorId: <p>Unique Id of the GA instance.</p>
        :type GlobalAcceleratorId: str
        """
        self._LogPushTaskId = None
        self._Status = None
        self._GlobalAcceleratorId = None

    @property
    def LogPushTaskId(self):
        r"""<p>Log Unique Id</p>
        :rtype: str
        """
        return self._LogPushTaskId

    @LogPushTaskId.setter
    def LogPushTaskId(self, LogPushTaskId):
        self._LogPushTaskId = LogPushTaskId

    @property
    def Status(self):
        r"""<p>Status (Start START, Stop STOP)</p><p>Enumeration values:</p><ul><li>START: Start</li><li>STOP: Stop</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Unique Id of the GA instance.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId


    def _deserialize(self, params):
        self._LogPushTaskId = params.get("LogPushTaskId")
        self._Status = params.get("Status")
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccessLogStatusResponse(AbstractModel):
    r"""ModifyAccessLogStatus response structure.

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


class ModifyEndpointGroupRequest(AbstractModel):
    r"""ModifyEndpointGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>Global acceleration instance ID.</p>
        :type GlobalAcceleratorId: str
        :param _ListenerId: <p>Listener ID.</p>
        :type ListenerId: str
        :param _EndpointGroupId: <p>Terminal node group ID.</p>
        :type EndpointGroupId: str
        :param _EndpointConfigurations: <p>Terminal node configuration.</p>
        :type EndpointConfigurations: list of EndpointConfigurations
        :param _Name: <p>Name.</p><p>Parameter format: starting with a letter or Chinese characters, 2–128 characters in length, supporting letters, digits, Chinese characters, . - _</p>
        :type Name: str
        :param _Description: <p>Description.</p><p>Input limit: maximum length cannot exceed 100 bytes.</p>
        :type Description: str
        :param _EnableHealthCheck: <p>Whether to enable health check.</p>
        :type EnableHealthCheck: bool
        :param _ConnectTimeout: <p>Response timeout.</p><p>Value range: [1, 100]</p><p>This parameter is required when health check is enabled.</p>
        :type ConnectTimeout: int
        :param _HealthCheckInterval: <p>Health check interval.</p><p>Value range: [5, 300].</p><p>This parameter is required when health check is enabled.</p>
        :type HealthCheckInterval: int
        :param _UnhealthyThreshold: <p>Unhealthy threshold.</p><p>Value range: [1, 10]</p><p>This field is required when health check is enabled.</p>
        :type UnhealthyThreshold: int
        :param _HealthyThreshold: <p>Health threshold.</p><p>Value range: [1, 10]</p><p>This field is required when health check is enabled.</p>
        :type HealthyThreshold: int
        :param _CheckType: <p>Select the protocol.</p><p>Input parameter limits: support filling in: 'TCP', 'HTTP', 'PING', 'CUSTOM'.</p><p>1. When the listener is TCP, you can choose CUSTOM+TCP.<br>2. When the listener is UDP, you can choose PING+CUSTOM.<br>3. When the listener is HTTP or HTTPS, you can choose HTTP.</p>
        :type CheckType: str
        :param _CheckPort: <p>Check port.</p><p>Value range: [1, 65535]</p><p>This field is required when CheckType is CUSTOM.</p>
        :type CheckPort: int
        :param _ContextType: <p>Check content.</p><p>Input parameter limit: Only TEXT is supported.</p><p>This field is required when CheckType is CUSTOM.</p>
        :type ContextType: str
        :param _CheckSendContext: <p>Check request.</p><p>Input parameter limit: The length range is 1-500.</p><p>This field is required when CheckType is CUSTOM.</p>
        :type CheckSendContext: str
        :param _CheckRecvContext: <p>Check returned results.</p><p>Input parameter limit: length range is 1-500.</p><p>When CheckType is CUSTOM, this field is required.</p>
        :type CheckRecvContext: str
        :param _CheckDomain: <p>Check domain name.</p><p>Input parameter limit: The length range is 3-80.</p><p>This field is required when CheckType is HTTP.</p>
        :type CheckDomain: str
        :param _CheckPath: <p>Check the URL.</p><p>Input parameter limit: length range 3-80.</p><p>This field is required when CheckType is HTTP.</p>
        :type CheckPath: str
        :param _CheckMethod: <p>Request method.</p><p>Input parameter limit: support filling in 'GET', 'HEAD'.</p><p>This field is required when CheckType is HTTP.</p>
        :type CheckMethod: str
        :param _StatusMask: <p>Status check code.</p><p>Input parameter limits: support selecting 'http_2xx', 'http_3xx', 'http_4xx', 'http_5xx'.</p><p>This field is required when CheckType is HTTP.</p>
        :type StatusMask: list of str
        :param _ForwardProtocol: <p>Origin-pull protocol.</p><p>Input parameter limits. Supported values: 'HTTP', 'HTTPS'.</p><p>When the CLB listener protocol is HTTP, only HTTP can be configured. When it is HTTPS, HTTP or HTTPS can be configured.</p>
        :type ForwardProtocol: str
        :param _PortOverrides: <p>Port mapping.</p><p>When the CLB listener protocol is HTTP or HTTPS, one pair can be configured. When the CLB listener protocol is UDP or TCP, up to 30 pairs can be configured.</p>
        :type PortOverrides: list of PortOverride
        :param _CipherPolicyId: <p>HPPTS encryption algorithm kit</p><p>Input parameter limit: support selecting 'tls_policy_1.0-2', 'tls_policy_1.1-2', 'tls_policy_1.2', 'tls_policy_1.2_strict', 'tls_policy_1.2_strict-1.3'.</p><p>This parameter can be modified only when the CLB listener protocol is HTTPS.</p>
        :type CipherPolicyId: str
        :param _HttpVersion: <p>Only the HTTPS back-to-source protocol supports selecting ['HTTP/1.1', 'HTTP/2']</p><p>Enumeration values:</p><ul><li>HTTP/1.1: version HTTP/1.1</li><li>HTTP/2: version HTTP/2</li></ul>
        :type HttpVersion: str
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._EndpointGroupId = None
        self._EndpointConfigurations = None
        self._Name = None
        self._Description = None
        self._EnableHealthCheck = None
        self._ConnectTimeout = None
        self._HealthCheckInterval = None
        self._UnhealthyThreshold = None
        self._HealthyThreshold = None
        self._CheckType = None
        self._CheckPort = None
        self._ContextType = None
        self._CheckSendContext = None
        self._CheckRecvContext = None
        self._CheckDomain = None
        self._CheckPath = None
        self._CheckMethod = None
        self._StatusMask = None
        self._ForwardProtocol = None
        self._PortOverrides = None
        self._CipherPolicyId = None
        self._HttpVersion = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Global acceleration instance ID.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""<p>Listener ID.</p>
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def EndpointGroupId(self):
        r"""<p>Terminal node group ID.</p>
        :rtype: str
        """
        return self._EndpointGroupId

    @EndpointGroupId.setter
    def EndpointGroupId(self, EndpointGroupId):
        self._EndpointGroupId = EndpointGroupId

    @property
    def EndpointConfigurations(self):
        r"""<p>Terminal node configuration.</p>
        :rtype: list of EndpointConfigurations
        """
        return self._EndpointConfigurations

    @EndpointConfigurations.setter
    def EndpointConfigurations(self, EndpointConfigurations):
        self._EndpointConfigurations = EndpointConfigurations

    @property
    def Name(self):
        r"""<p>Name.</p><p>Parameter format: starting with a letter or Chinese characters, 2–128 characters in length, supporting letters, digits, Chinese characters, . - _</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>Description.</p><p>Input limit: maximum length cannot exceed 100 bytes.</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def EnableHealthCheck(self):
        r"""<p>Whether to enable health check.</p>
        :rtype: bool
        """
        return self._EnableHealthCheck

    @EnableHealthCheck.setter
    def EnableHealthCheck(self, EnableHealthCheck):
        self._EnableHealthCheck = EnableHealthCheck

    @property
    def ConnectTimeout(self):
        r"""<p>Response timeout.</p><p>Value range: [1, 100]</p><p>This parameter is required when health check is enabled.</p>
        :rtype: int
        """
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def HealthCheckInterval(self):
        r"""<p>Health check interval.</p><p>Value range: [5, 300].</p><p>This parameter is required when health check is enabled.</p>
        :rtype: int
        """
        return self._HealthCheckInterval

    @HealthCheckInterval.setter
    def HealthCheckInterval(self, HealthCheckInterval):
        self._HealthCheckInterval = HealthCheckInterval

    @property
    def UnhealthyThreshold(self):
        r"""<p>Unhealthy threshold.</p><p>Value range: [1, 10]</p><p>This field is required when health check is enabled.</p>
        :rtype: int
        """
        return self._UnhealthyThreshold

    @UnhealthyThreshold.setter
    def UnhealthyThreshold(self, UnhealthyThreshold):
        self._UnhealthyThreshold = UnhealthyThreshold

    @property
    def HealthyThreshold(self):
        r"""<p>Health threshold.</p><p>Value range: [1, 10]</p><p>This field is required when health check is enabled.</p>
        :rtype: int
        """
        return self._HealthyThreshold

    @HealthyThreshold.setter
    def HealthyThreshold(self, HealthyThreshold):
        self._HealthyThreshold = HealthyThreshold

    @property
    def CheckType(self):
        r"""<p>Select the protocol.</p><p>Input parameter limits: support filling in: 'TCP', 'HTTP', 'PING', 'CUSTOM'.</p><p>1. When the listener is TCP, you can choose CUSTOM+TCP.<br>2. When the listener is UDP, you can choose PING+CUSTOM.<br>3. When the listener is HTTP or HTTPS, you can choose HTTP.</p>
        :rtype: str
        """
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType

    @property
    def CheckPort(self):
        r"""<p>Check port.</p><p>Value range: [1, 65535]</p><p>This field is required when CheckType is CUSTOM.</p>
        :rtype: int
        """
        return self._CheckPort

    @CheckPort.setter
    def CheckPort(self, CheckPort):
        self._CheckPort = CheckPort

    @property
    def ContextType(self):
        r"""<p>Check content.</p><p>Input parameter limit: Only TEXT is supported.</p><p>This field is required when CheckType is CUSTOM.</p>
        :rtype: str
        """
        return self._ContextType

    @ContextType.setter
    def ContextType(self, ContextType):
        self._ContextType = ContextType

    @property
    def CheckSendContext(self):
        r"""<p>Check request.</p><p>Input parameter limit: The length range is 1-500.</p><p>This field is required when CheckType is CUSTOM.</p>
        :rtype: str
        """
        return self._CheckSendContext

    @CheckSendContext.setter
    def CheckSendContext(self, CheckSendContext):
        self._CheckSendContext = CheckSendContext

    @property
    def CheckRecvContext(self):
        r"""<p>Check returned results.</p><p>Input parameter limit: length range is 1-500.</p><p>When CheckType is CUSTOM, this field is required.</p>
        :rtype: str
        """
        return self._CheckRecvContext

    @CheckRecvContext.setter
    def CheckRecvContext(self, CheckRecvContext):
        self._CheckRecvContext = CheckRecvContext

    @property
    def CheckDomain(self):
        r"""<p>Check domain name.</p><p>Input parameter limit: The length range is 3-80.</p><p>This field is required when CheckType is HTTP.</p>
        :rtype: str
        """
        return self._CheckDomain

    @CheckDomain.setter
    def CheckDomain(self, CheckDomain):
        self._CheckDomain = CheckDomain

    @property
    def CheckPath(self):
        r"""<p>Check the URL.</p><p>Input parameter limit: length range 3-80.</p><p>This field is required when CheckType is HTTP.</p>
        :rtype: str
        """
        return self._CheckPath

    @CheckPath.setter
    def CheckPath(self, CheckPath):
        self._CheckPath = CheckPath

    @property
    def CheckMethod(self):
        r"""<p>Request method.</p><p>Input parameter limit: support filling in 'GET', 'HEAD'.</p><p>This field is required when CheckType is HTTP.</p>
        :rtype: str
        """
        return self._CheckMethod

    @CheckMethod.setter
    def CheckMethod(self, CheckMethod):
        self._CheckMethod = CheckMethod

    @property
    def StatusMask(self):
        r"""<p>Status check code.</p><p>Input parameter limits: support selecting 'http_2xx', 'http_3xx', 'http_4xx', 'http_5xx'.</p><p>This field is required when CheckType is HTTP.</p>
        :rtype: list of str
        """
        return self._StatusMask

    @StatusMask.setter
    def StatusMask(self, StatusMask):
        self._StatusMask = StatusMask

    @property
    def ForwardProtocol(self):
        r"""<p>Origin-pull protocol.</p><p>Input parameter limits. Supported values: 'HTTP', 'HTTPS'.</p><p>When the CLB listener protocol is HTTP, only HTTP can be configured. When it is HTTPS, HTTP or HTTPS can be configured.</p>
        :rtype: str
        """
        return self._ForwardProtocol

    @ForwardProtocol.setter
    def ForwardProtocol(self, ForwardProtocol):
        self._ForwardProtocol = ForwardProtocol

    @property
    def PortOverrides(self):
        r"""<p>Port mapping.</p><p>When the CLB listener protocol is HTTP or HTTPS, one pair can be configured. When the CLB listener protocol is UDP or TCP, up to 30 pairs can be configured.</p>
        :rtype: list of PortOverride
        """
        return self._PortOverrides

    @PortOverrides.setter
    def PortOverrides(self, PortOverrides):
        self._PortOverrides = PortOverrides

    @property
    def CipherPolicyId(self):
        r"""<p>HPPTS encryption algorithm kit</p><p>Input parameter limit: support selecting 'tls_policy_1.0-2', 'tls_policy_1.1-2', 'tls_policy_1.2', 'tls_policy_1.2_strict', 'tls_policy_1.2_strict-1.3'.</p><p>This parameter can be modified only when the CLB listener protocol is HTTPS.</p>
        :rtype: str
        """
        return self._CipherPolicyId

    @CipherPolicyId.setter
    def CipherPolicyId(self, CipherPolicyId):
        self._CipherPolicyId = CipherPolicyId

    @property
    def HttpVersion(self):
        r"""<p>Only the HTTPS back-to-source protocol supports selecting ['HTTP/1.1', 'HTTP/2']</p><p>Enumeration values:</p><ul><li>HTTP/1.1: version HTTP/1.1</li><li>HTTP/2: version HTTP/2</li></ul>
        :rtype: str
        """
        return self._HttpVersion

    @HttpVersion.setter
    def HttpVersion(self, HttpVersion):
        self._HttpVersion = HttpVersion


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._EndpointGroupId = params.get("EndpointGroupId")
        if params.get("EndpointConfigurations") is not None:
            self._EndpointConfigurations = []
            for item in params.get("EndpointConfigurations"):
                obj = EndpointConfigurations()
                obj._deserialize(item)
                self._EndpointConfigurations.append(obj)
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._EnableHealthCheck = params.get("EnableHealthCheck")
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._HealthCheckInterval = params.get("HealthCheckInterval")
        self._UnhealthyThreshold = params.get("UnhealthyThreshold")
        self._HealthyThreshold = params.get("HealthyThreshold")
        self._CheckType = params.get("CheckType")
        self._CheckPort = params.get("CheckPort")
        self._ContextType = params.get("ContextType")
        self._CheckSendContext = params.get("CheckSendContext")
        self._CheckRecvContext = params.get("CheckRecvContext")
        self._CheckDomain = params.get("CheckDomain")
        self._CheckPath = params.get("CheckPath")
        self._CheckMethod = params.get("CheckMethod")
        self._StatusMask = params.get("StatusMask")
        self._ForwardProtocol = params.get("ForwardProtocol")
        if params.get("PortOverrides") is not None:
            self._PortOverrides = []
            for item in params.get("PortOverrides"):
                obj = PortOverride()
                obj._deserialize(item)
                self._PortOverrides.append(obj)
        self._CipherPolicyId = params.get("CipherPolicyId")
        self._HttpVersion = params.get("HttpVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEndpointGroupResponse(AbstractModel):
    r"""ModifyEndpointGroup response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>Task ID.</p>
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>Task ID.</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyForwardingPolicyRequest(AbstractModel):
    r"""ModifyForwardingPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>Global acceleration instance ID.</p>
        :type GlobalAcceleratorId: str
        :param _ListenerId: <p>Listener ID.</p>
        :type ListenerId: str
        :param _ForwardingPolicyId: <p>Policy ID.</p>
        :type ForwardingPolicyId: str
        :param _Host: <p>Domain name.</p><p>Input limit: length range is 1-80.</p><p>The format must meet the regular expression: ^(<a href="?:[a-z0-9-]{0,61}[a-z0-9]">a-z0-9</a>?.)+[a-z]{2,}$</p>
        :type Host: str
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._ForwardingPolicyId = None
        self._Host = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Global acceleration instance ID.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""<p>Listener ID.</p>
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ForwardingPolicyId(self):
        r"""<p>Policy ID.</p>
        :rtype: str
        """
        return self._ForwardingPolicyId

    @ForwardingPolicyId.setter
    def ForwardingPolicyId(self, ForwardingPolicyId):
        self._ForwardingPolicyId = ForwardingPolicyId

    @property
    def Host(self):
        r"""<p>Domain name.</p><p>Input limit: length range is 1-80.</p><p>The format must meet the regular expression: ^(<a href="?:[a-z0-9-]{0,61}[a-z0-9]">a-z0-9</a>?.)+[a-z]{2,}$</p>
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._ForwardingPolicyId = params.get("ForwardingPolicyId")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyForwardingPolicyResponse(AbstractModel):
    r"""ModifyForwardingPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>Asynchronous task ID.</p>
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>Asynchronous task ID.</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyForwardingRuleRequest(AbstractModel):
    r"""ModifyForwardingRule request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>Global acceleration instance ID.</p>
        :type GlobalAcceleratorId: str
        :param _ListenerId: <p>Listener ID.</p>
        :type ListenerId: str
        :param _ForwardingPolicyId: <p>Policy ID.</p>
        :type ForwardingPolicyId: str
        :param _ForwardingRuleId: <p>Layer 7 forwarding rule ID.</p>
        :type ForwardingRuleId: str
        :param _RuleConditions: <p>Conditional information of Layer 7 forwarding rules.</p><p>Input parameter limit: The array length cannot exceed 1.</p>
        :type RuleConditions: list of RuleCondition
        :param _RuleActions: <p>Layer 7 forwarding rule behavior information.</p><p>Input parameter limit: array length cannot exceed 1.</p>
        :type RuleActions: list of RuleAction
        :param _OriginHeaders: <p>Origin-pull Header information.</p><p>Input limitation: The length of the array is between 1 and 5.</p>
        :type OriginHeaders: list of OriginHeader
        :param _EnableOriginSni: <p>Whether to enable origin-pull sni.</p>
        :type EnableOriginSni: bool
        :param _OriginSni: <p>Origin sni.</p><p>Input parameter limit: length cannot exceed 80.</p><p>This field is required when origin sni is enabled.</p>
        :type OriginSni: str
        :param _OriginHost: <p>Origin-pull host.</p><p>Input parameter limit: length cannot exceed 80.</p><p>This field is required when origin-pull sni is enabled.</p>
        :type OriginHost: str
        :param _ResponseHeaders: <p>Origin server response headers</p><p>Input limitation: The array length cannot exceed 5.</p>
        :type ResponseHeaders: list of ResponseHeaders
        :param _HideResponseHeaders: <p>Delete origin response headers</p><p>Input parameter limit: array length cannot exceed 5.</p>
        :type HideResponseHeaders: list of HideResponseHeaders
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._ForwardingPolicyId = None
        self._ForwardingRuleId = None
        self._RuleConditions = None
        self._RuleActions = None
        self._OriginHeaders = None
        self._EnableOriginSni = None
        self._OriginSni = None
        self._OriginHost = None
        self._ResponseHeaders = None
        self._HideResponseHeaders = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Global acceleration instance ID.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""<p>Listener ID.</p>
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ForwardingPolicyId(self):
        r"""<p>Policy ID.</p>
        :rtype: str
        """
        return self._ForwardingPolicyId

    @ForwardingPolicyId.setter
    def ForwardingPolicyId(self, ForwardingPolicyId):
        self._ForwardingPolicyId = ForwardingPolicyId

    @property
    def ForwardingRuleId(self):
        r"""<p>Layer 7 forwarding rule ID.</p>
        :rtype: str
        """
        return self._ForwardingRuleId

    @ForwardingRuleId.setter
    def ForwardingRuleId(self, ForwardingRuleId):
        self._ForwardingRuleId = ForwardingRuleId

    @property
    def RuleConditions(self):
        r"""<p>Conditional information of Layer 7 forwarding rules.</p><p>Input parameter limit: The array length cannot exceed 1.</p>
        :rtype: list of RuleCondition
        """
        return self._RuleConditions

    @RuleConditions.setter
    def RuleConditions(self, RuleConditions):
        self._RuleConditions = RuleConditions

    @property
    def RuleActions(self):
        r"""<p>Layer 7 forwarding rule behavior information.</p><p>Input parameter limit: array length cannot exceed 1.</p>
        :rtype: list of RuleAction
        """
        return self._RuleActions

    @RuleActions.setter
    def RuleActions(self, RuleActions):
        self._RuleActions = RuleActions

    @property
    def OriginHeaders(self):
        r"""<p>Origin-pull Header information.</p><p>Input limitation: The length of the array is between 1 and 5.</p>
        :rtype: list of OriginHeader
        """
        return self._OriginHeaders

    @OriginHeaders.setter
    def OriginHeaders(self, OriginHeaders):
        self._OriginHeaders = OriginHeaders

    @property
    def EnableOriginSni(self):
        r"""<p>Whether to enable origin-pull sni.</p>
        :rtype: bool
        """
        return self._EnableOriginSni

    @EnableOriginSni.setter
    def EnableOriginSni(self, EnableOriginSni):
        self._EnableOriginSni = EnableOriginSni

    @property
    def OriginSni(self):
        r"""<p>Origin sni.</p><p>Input parameter limit: length cannot exceed 80.</p><p>This field is required when origin sni is enabled.</p>
        :rtype: str
        """
        return self._OriginSni

    @OriginSni.setter
    def OriginSni(self, OriginSni):
        self._OriginSni = OriginSni

    @property
    def OriginHost(self):
        r"""<p>Origin-pull host.</p><p>Input parameter limit: length cannot exceed 80.</p><p>This field is required when origin-pull sni is enabled.</p>
        :rtype: str
        """
        return self._OriginHost

    @OriginHost.setter
    def OriginHost(self, OriginHost):
        self._OriginHost = OriginHost

    @property
    def ResponseHeaders(self):
        r"""<p>Origin server response headers</p><p>Input limitation: The array length cannot exceed 5.</p>
        :rtype: list of ResponseHeaders
        """
        return self._ResponseHeaders

    @ResponseHeaders.setter
    def ResponseHeaders(self, ResponseHeaders):
        self._ResponseHeaders = ResponseHeaders

    @property
    def HideResponseHeaders(self):
        r"""<p>Delete origin response headers</p><p>Input parameter limit: array length cannot exceed 5.</p>
        :rtype: list of HideResponseHeaders
        """
        return self._HideResponseHeaders

    @HideResponseHeaders.setter
    def HideResponseHeaders(self, HideResponseHeaders):
        self._HideResponseHeaders = HideResponseHeaders


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._ForwardingPolicyId = params.get("ForwardingPolicyId")
        self._ForwardingRuleId = params.get("ForwardingRuleId")
        if params.get("RuleConditions") is not None:
            self._RuleConditions = []
            for item in params.get("RuleConditions"):
                obj = RuleCondition()
                obj._deserialize(item)
                self._RuleConditions.append(obj)
        if params.get("RuleActions") is not None:
            self._RuleActions = []
            for item in params.get("RuleActions"):
                obj = RuleAction()
                obj._deserialize(item)
                self._RuleActions.append(obj)
        if params.get("OriginHeaders") is not None:
            self._OriginHeaders = []
            for item in params.get("OriginHeaders"):
                obj = OriginHeader()
                obj._deserialize(item)
                self._OriginHeaders.append(obj)
        self._EnableOriginSni = params.get("EnableOriginSni")
        self._OriginSni = params.get("OriginSni")
        self._OriginHost = params.get("OriginHost")
        if params.get("ResponseHeaders") is not None:
            self._ResponseHeaders = []
            for item in params.get("ResponseHeaders"):
                obj = ResponseHeaders()
                obj._deserialize(item)
                self._ResponseHeaders.append(obj)
        if params.get("HideResponseHeaders") is not None:
            self._HideResponseHeaders = []
            for item in params.get("HideResponseHeaders"):
                obj = HideResponseHeaders()
                obj._deserialize(item)
                self._HideResponseHeaders.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyForwardingRuleResponse(AbstractModel):
    r"""ModifyForwardingRule response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>Asynchronous task ID.</p>
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>Asynchronous task ID.</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyGlobalAcceleratorAccessLogRequest(AbstractModel):
    r"""ModifyGlobalAcceleratorAccessLog request structure.

    """

    def __init__(self):
        r"""
        :param _LogPushTaskId: <p>Unique Id of the log</p>
        :type LogPushTaskId: str
        :param _GlobalAcceleratorId: <p>Unique Id of a GA instance.</p>
        :type GlobalAcceleratorId: str
        :param _CloudLogId: <p>Log topic Id</p>
        :type CloudLogId: str
        :param _CloudLogSetId: <p>Log Set Id</p>
        :type CloudLogSetId: str
        :param _FieldKeys: <p>user-selectable log listening fields</p><p>Enumeration values:</p><ul><li>session_time: Layer 4, session duration</li><li>upstream_bytes_received: Layer 4 and Layer 7, number of bytes received from the terminal node</li><li>upstream_bytes_sent: Layer 4 and Layer 7, number of bytes sent to the terminal node</li><li>request_method: Layer 7, GET/POST</li><li>scheme: Layer 7, http/https</li><li>request_uri: Layer 7, uri of the client's original request</li><li>uri: Layer 7, uri of the current request</li><li>host: Layer 7, domain name accessed by the client (Layer 7)</li><li>remote_user: Layer 7, username for basic authentication ("-" if unauthenticated)</li><li>http_user_agent: Layer 7, client browser identification</li><li>http_referer: Layer 7, request source URL ("-" when accessed directly from the address bar)</li><li>http_x_forwarded_for: Layer 7, records the client's original IP and the chain of proxy server IPs it transited</li><li>content_type: Layer 7, content_type</li><li>body_bytes_sent: Layer 7, http body size sent to the client, excluding the header</li><li>request_time: Layer 7, total time from receiving the first byte of the client request to sending the last byte of the response (unit: seconds)</li><li>sent_http_content_type: Layer 7, response content type</li><li>upstream_header_time: Layer 7, arrival time of the response header from the terminal node</li><li>upstream_response_length: Layer 7, response body length returned by the terminal node</li><li>upstream_response_time: Layer 7, full response time of the terminal node</li><li>upstream_status: Layer 7, http status code returned by the terminal node</li></ul>
        :type FieldKeys: list of str
        :param _FlowLogDescription: <p>Log description</p>
        :type FlowLogDescription: str
        """
        self._LogPushTaskId = None
        self._GlobalAcceleratorId = None
        self._CloudLogId = None
        self._CloudLogSetId = None
        self._FieldKeys = None
        self._FlowLogDescription = None

    @property
    def LogPushTaskId(self):
        r"""<p>Unique Id of the log</p>
        :rtype: str
        """
        return self._LogPushTaskId

    @LogPushTaskId.setter
    def LogPushTaskId(self, LogPushTaskId):
        self._LogPushTaskId = LogPushTaskId

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Unique Id of a GA instance.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def CloudLogId(self):
        r"""<p>Log topic Id</p>
        :rtype: str
        """
        return self._CloudLogId

    @CloudLogId.setter
    def CloudLogId(self, CloudLogId):
        self._CloudLogId = CloudLogId

    @property
    def CloudLogSetId(self):
        r"""<p>Log Set Id</p>
        :rtype: str
        """
        return self._CloudLogSetId

    @CloudLogSetId.setter
    def CloudLogSetId(self, CloudLogSetId):
        self._CloudLogSetId = CloudLogSetId

    @property
    def FieldKeys(self):
        r"""<p>user-selectable log listening fields</p><p>Enumeration values:</p><ul><li>session_time: Layer 4, session duration</li><li>upstream_bytes_received: Layer 4 and Layer 7, number of bytes received from the terminal node</li><li>upstream_bytes_sent: Layer 4 and Layer 7, number of bytes sent to the terminal node</li><li>request_method: Layer 7, GET/POST</li><li>scheme: Layer 7, http/https</li><li>request_uri: Layer 7, uri of the client's original request</li><li>uri: Layer 7, uri of the current request</li><li>host: Layer 7, domain name accessed by the client (Layer 7)</li><li>remote_user: Layer 7, username for basic authentication ("-" if unauthenticated)</li><li>http_user_agent: Layer 7, client browser identification</li><li>http_referer: Layer 7, request source URL ("-" when accessed directly from the address bar)</li><li>http_x_forwarded_for: Layer 7, records the client's original IP and the chain of proxy server IPs it transited</li><li>content_type: Layer 7, content_type</li><li>body_bytes_sent: Layer 7, http body size sent to the client, excluding the header</li><li>request_time: Layer 7, total time from receiving the first byte of the client request to sending the last byte of the response (unit: seconds)</li><li>sent_http_content_type: Layer 7, response content type</li><li>upstream_header_time: Layer 7, arrival time of the response header from the terminal node</li><li>upstream_response_length: Layer 7, response body length returned by the terminal node</li><li>upstream_response_time: Layer 7, full response time of the terminal node</li><li>upstream_status: Layer 7, http status code returned by the terminal node</li></ul>
        :rtype: list of str
        """
        return self._FieldKeys

    @FieldKeys.setter
    def FieldKeys(self, FieldKeys):
        self._FieldKeys = FieldKeys

    @property
    def FlowLogDescription(self):
        r"""<p>Log description</p>
        :rtype: str
        """
        return self._FlowLogDescription

    @FlowLogDescription.setter
    def FlowLogDescription(self, FlowLogDescription):
        self._FlowLogDescription = FlowLogDescription


    def _deserialize(self, params):
        self._LogPushTaskId = params.get("LogPushTaskId")
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._CloudLogId = params.get("CloudLogId")
        self._CloudLogSetId = params.get("CloudLogSetId")
        self._FieldKeys = params.get("FieldKeys")
        self._FlowLogDescription = params.get("FlowLogDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGlobalAcceleratorAccessLogResponse(AbstractModel):
    r"""ModifyGlobalAcceleratorAccessLog response structure.

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


class ModifyGlobalAcceleratorAclPolicyRequest(AbstractModel):
    r"""ModifyGlobalAcceleratorAclPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>Global acceleration instance ID.</p>
        :type GlobalAcceleratorId: str
        :param _GlobalAcceleratorAclPolicyId: <p>Access control policy ID.</p>
        :type GlobalAcceleratorAclPolicyId: str
        :param _Status: <p>Access control policy status.</p><p>Enumeration values:</p><ul><li>OPEN: On.</li><li>CLOSE: Off.</li></ul>
        :type Status: str
        """
        self._GlobalAcceleratorId = None
        self._GlobalAcceleratorAclPolicyId = None
        self._Status = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Global acceleration instance ID.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def GlobalAcceleratorAclPolicyId(self):
        r"""<p>Access control policy ID.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorAclPolicyId

    @GlobalAcceleratorAclPolicyId.setter
    def GlobalAcceleratorAclPolicyId(self, GlobalAcceleratorAclPolicyId):
        self._GlobalAcceleratorAclPolicyId = GlobalAcceleratorAclPolicyId

    @property
    def Status(self):
        r"""<p>Access control policy status.</p><p>Enumeration values:</p><ul><li>OPEN: On.</li><li>CLOSE: Off.</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._GlobalAcceleratorAclPolicyId = params.get("GlobalAcceleratorAclPolicyId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGlobalAcceleratorAclPolicyResponse(AbstractModel):
    r"""ModifyGlobalAcceleratorAclPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>Asynchronous task ID.</p>
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>Asynchronous task ID.</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyGlobalAcceleratorAclRuleRequest(AbstractModel):
    r"""ModifyGlobalAcceleratorAclRule request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>Global acceleration instance ID.</p>
        :type GlobalAcceleratorId: str
        :param _GlobalAcceleratorAclPolicyId: <p>Security policy ID</p>
        :type GlobalAcceleratorAclPolicyId: str
        :param _GlobalAcceleratorAclRuleId: <p>Acl rule ID.</p>
        :type GlobalAcceleratorAclRuleId: str
        :param _Protocol: <p>Protocol.</p><p>Input parameter limit: support selecting 'TCP', 'UDP'.</p>
        :type Protocol: str
        :param _Port: <p>Port.</p>
        :type Port: str
        :param _SourceCidrBlock: <p>IP range.</p>
        :type SourceCidrBlock: str
        :param _Policy: <p>Action.</p><p>Input parameter limit: support selecting 'ACCEPT', 'DROP'.</p><p>Enumeration values:</p><ul><li>ACCEPT: permission.</li><li>DROP: deny.</li></ul>
        :type Policy: str
        :param _Description: <p>Description. Maximum length cannot exceed 100 bytes.</p>
        :type Description: str
        """
        self._GlobalAcceleratorId = None
        self._GlobalAcceleratorAclPolicyId = None
        self._GlobalAcceleratorAclRuleId = None
        self._Protocol = None
        self._Port = None
        self._SourceCidrBlock = None
        self._Policy = None
        self._Description = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Global acceleration instance ID.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def GlobalAcceleratorAclPolicyId(self):
        r"""<p>Security policy ID</p>
        :rtype: str
        """
        return self._GlobalAcceleratorAclPolicyId

    @GlobalAcceleratorAclPolicyId.setter
    def GlobalAcceleratorAclPolicyId(self, GlobalAcceleratorAclPolicyId):
        self._GlobalAcceleratorAclPolicyId = GlobalAcceleratorAclPolicyId

    @property
    def GlobalAcceleratorAclRuleId(self):
        r"""<p>Acl rule ID.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorAclRuleId

    @GlobalAcceleratorAclRuleId.setter
    def GlobalAcceleratorAclRuleId(self, GlobalAcceleratorAclRuleId):
        self._GlobalAcceleratorAclRuleId = GlobalAcceleratorAclRuleId

    @property
    def Protocol(self):
        r"""<p>Protocol.</p><p>Input parameter limit: support selecting 'TCP', 'UDP'.</p>
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        r"""<p>Port.</p>
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def SourceCidrBlock(self):
        r"""<p>IP range.</p>
        :rtype: str
        """
        return self._SourceCidrBlock

    @SourceCidrBlock.setter
    def SourceCidrBlock(self, SourceCidrBlock):
        self._SourceCidrBlock = SourceCidrBlock

    @property
    def Policy(self):
        r"""<p>Action.</p><p>Input parameter limit: support selecting 'ACCEPT', 'DROP'.</p><p>Enumeration values:</p><ul><li>ACCEPT: permission.</li><li>DROP: deny.</li></ul>
        :rtype: str
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def Description(self):
        r"""<p>Description. Maximum length cannot exceed 100 bytes.</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._GlobalAcceleratorAclPolicyId = params.get("GlobalAcceleratorAclPolicyId")
        self._GlobalAcceleratorAclRuleId = params.get("GlobalAcceleratorAclRuleId")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._SourceCidrBlock = params.get("SourceCidrBlock")
        self._Policy = params.get("Policy")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGlobalAcceleratorAclRuleResponse(AbstractModel):
    r"""ModifyGlobalAcceleratorAclRule response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>Asynchronous task ID.</p>
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>Asynchronous task ID.</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyGlobalAcceleratorRequest(AbstractModel):
    r"""ModifyGlobalAccelerator request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>Global acceleration instance ID.</p>
        :type GlobalAcceleratorId: str
        :param _Name: <p>Name.</p><p>Parameter format: starting with a letter or Chinese characters, 2–128 characters in length, supporting letters, digits, Chinese characters, . - _</p>
        :type Name: str
        :param _Description: <p>Description.</p><p>Parameter format: should not exceed 100 characters.</p>
        :type Description: str
        :param _CrossBorderType: <p>Cross-border type.</p><p>Enumeration values:</p><ul><li>HighQuality: high-quality cross-border.</li><li>Unicom: China Unicom cross-border.</li></ul>
        :type CrossBorderType: str
        :param _CrossBorderPromiseFlag: <p>Indicates whether to complete the cross-border service commitment.</p><p>When CrossBorderType is passed in, this field must be set to true, indicating the cross-border commitment is completed.</p>
        :type CrossBorderPromiseFlag: bool
        """
        self._GlobalAcceleratorId = None
        self._Name = None
        self._Description = None
        self._CrossBorderType = None
        self._CrossBorderPromiseFlag = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Global acceleration instance ID.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def Name(self):
        r"""<p>Name.</p><p>Parameter format: starting with a letter or Chinese characters, 2–128 characters in length, supporting letters, digits, Chinese characters, . - _</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>Description.</p><p>Parameter format: should not exceed 100 characters.</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CrossBorderType(self):
        r"""<p>Cross-border type.</p><p>Enumeration values:</p><ul><li>HighQuality: high-quality cross-border.</li><li>Unicom: China Unicom cross-border.</li></ul>
        :rtype: str
        """
        return self._CrossBorderType

    @CrossBorderType.setter
    def CrossBorderType(self, CrossBorderType):
        self._CrossBorderType = CrossBorderType

    @property
    def CrossBorderPromiseFlag(self):
        r"""<p>Indicates whether to complete the cross-border service commitment.</p><p>When CrossBorderType is passed in, this field must be set to true, indicating the cross-border commitment is completed.</p>
        :rtype: bool
        """
        return self._CrossBorderPromiseFlag

    @CrossBorderPromiseFlag.setter
    def CrossBorderPromiseFlag(self, CrossBorderPromiseFlag):
        self._CrossBorderPromiseFlag = CrossBorderPromiseFlag


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._CrossBorderType = params.get("CrossBorderType")
        self._CrossBorderPromiseFlag = params.get("CrossBorderPromiseFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGlobalAcceleratorResponse(AbstractModel):
    r"""ModifyGlobalAccelerator response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>Asynchronous task ID.</p>
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>Asynchronous task ID.</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyListenerRequest(AbstractModel):
    r"""ModifyListener request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>Global acceleration instance ID.</p>
        :type GlobalAcceleratorId: str
        :param _ListenerId: <p>Listener ID.</p>
        :type ListenerId: str
        :param _Name: <p>Name.</p><p>Parameter format: starting with a letter or Chinese characters, 2–128 characters in length, supporting letters, digits, Chinese characters, . - _</p>
        :type Name: str
        :param _Description: <p>Description. Maximum length cannot exceed 100 bytes.</p>
        :type Description: str
        :param _IdleTimeout: <p>Connection idle wait time.</p><p>1. For HTTP/HTTPS listener, the supported range is 1-60. 2. For TCP listener, the supported range is 10-900. 3. For UDP listener, the supported range is 10-20.</p>
        :type IdleTimeout: int
        :param _ClientAffinity: <p>Whether to enable session persistence.</p><p>Enumeration values:</p><ul><li>Open: on.</li><li>Close: off.</li></ul><p>TCP/UDP listeners support modification of this parameter.</p>
        :type ClientAffinity: str
        :param _ClientAffinityTime: <p>Session persistence duration.</p><p>Value range: [60, 3600]</p>
        :type ClientAffinityTime: int
        :param _RequestTimeout: <p>Request timeout.</p><p>Value range: [1, 180]</p><p>This parameter can be modified only for HTTPS listeners.</p>
        :type RequestTimeout: int
        :param _XForwardedForRealIp: <p>Whether to enable the layer 7 method of obtaining the client IP.</p><p>This parameter modification is supported only for HTTPS/HTTP listeners.</p>
        :type XForwardedForRealIp: bool
        :param _CertificationType: <p>Parsing method.</p><p>Enumeration values:</p><ul><li>UNIDIRECTIONAL: two-way.</li><li>MUTUAL: one-way.</li></ul><p>Only HTTPS/HTTP listeners support modifying this parameter.</p>
        :type CertificationType: str
        :param _CipherPolicyId: <p>Encryption algorithm kit.</p><p>Input limits: support selecting tls_policy_1.0-2', 'tls_policy_1.1-2', 'tls_policy_1.2', 'tls_policy_1.2_strict', 'tls_policy_1.2_strict-1.3'.</p><p>Only HTTPS listeners support modifying this parameter.</p>
        :type CipherPolicyId: str
        :param _ServerCertificates: <p>Server certificate.</p><p>Input limit: currently only support importing one cert; to use multiple certs, use the cert api CreateListenerAdditionalCert to add other certs.</p><p>Only HTTPS listeners support modification of this parameter.</p>
        :type ServerCertificates: list of str
        :param _ClientCaCertificates: <p>Client certificate.</p><p>Input limitations: 1. Currently only support importing one certificate; to use multiple certificates, use the certificate api CreateListenerAdditionalCert to add other certificates. 2. The certificate must be a CA certificate.</p><p>Only HTTPS listeners support modification of this parameter, and mutual authentication must be enabled.</p>
        :type ClientCaCertificates: list of str
        :param _GetRealIpType: <p>Method of obtaining the source IP.</p><p>Input parameter limits: support selecting 'ProxyProtocol', 'Close', 'ProxyProtocolV2', 'TOA'.</p><p>Only TCP listeners support modification of this parameter.</p>
        :type GetRealIpType: str
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._Name = None
        self._Description = None
        self._IdleTimeout = None
        self._ClientAffinity = None
        self._ClientAffinityTime = None
        self._RequestTimeout = None
        self._XForwardedForRealIp = None
        self._CertificationType = None
        self._CipherPolicyId = None
        self._ServerCertificates = None
        self._ClientCaCertificates = None
        self._GetRealIpType = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>Global acceleration instance ID.</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""<p>Listener ID.</p>
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Name(self):
        r"""<p>Name.</p><p>Parameter format: starting with a letter or Chinese characters, 2–128 characters in length, supporting letters, digits, Chinese characters, . - _</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>Description. Maximum length cannot exceed 100 bytes.</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def IdleTimeout(self):
        r"""<p>Connection idle wait time.</p><p>1. For HTTP/HTTPS listener, the supported range is 1-60. 2. For TCP listener, the supported range is 10-900. 3. For UDP listener, the supported range is 10-20.</p>
        :rtype: int
        """
        return self._IdleTimeout

    @IdleTimeout.setter
    def IdleTimeout(self, IdleTimeout):
        self._IdleTimeout = IdleTimeout

    @property
    def ClientAffinity(self):
        r"""<p>Whether to enable session persistence.</p><p>Enumeration values:</p><ul><li>Open: on.</li><li>Close: off.</li></ul><p>TCP/UDP listeners support modification of this parameter.</p>
        :rtype: str
        """
        return self._ClientAffinity

    @ClientAffinity.setter
    def ClientAffinity(self, ClientAffinity):
        self._ClientAffinity = ClientAffinity

    @property
    def ClientAffinityTime(self):
        r"""<p>Session persistence duration.</p><p>Value range: [60, 3600]</p>
        :rtype: int
        """
        return self._ClientAffinityTime

    @ClientAffinityTime.setter
    def ClientAffinityTime(self, ClientAffinityTime):
        self._ClientAffinityTime = ClientAffinityTime

    @property
    def RequestTimeout(self):
        r"""<p>Request timeout.</p><p>Value range: [1, 180]</p><p>This parameter can be modified only for HTTPS listeners.</p>
        :rtype: int
        """
        return self._RequestTimeout

    @RequestTimeout.setter
    def RequestTimeout(self, RequestTimeout):
        self._RequestTimeout = RequestTimeout

    @property
    def XForwardedForRealIp(self):
        r"""<p>Whether to enable the layer 7 method of obtaining the client IP.</p><p>This parameter modification is supported only for HTTPS/HTTP listeners.</p>
        :rtype: bool
        """
        return self._XForwardedForRealIp

    @XForwardedForRealIp.setter
    def XForwardedForRealIp(self, XForwardedForRealIp):
        self._XForwardedForRealIp = XForwardedForRealIp

    @property
    def CertificationType(self):
        r"""<p>Parsing method.</p><p>Enumeration values:</p><ul><li>UNIDIRECTIONAL: two-way.</li><li>MUTUAL: one-way.</li></ul><p>Only HTTPS/HTTP listeners support modifying this parameter.</p>
        :rtype: str
        """
        return self._CertificationType

    @CertificationType.setter
    def CertificationType(self, CertificationType):
        self._CertificationType = CertificationType

    @property
    def CipherPolicyId(self):
        r"""<p>Encryption algorithm kit.</p><p>Input limits: support selecting tls_policy_1.0-2', 'tls_policy_1.1-2', 'tls_policy_1.2', 'tls_policy_1.2_strict', 'tls_policy_1.2_strict-1.3'.</p><p>Only HTTPS listeners support modifying this parameter.</p>
        :rtype: str
        """
        return self._CipherPolicyId

    @CipherPolicyId.setter
    def CipherPolicyId(self, CipherPolicyId):
        self._CipherPolicyId = CipherPolicyId

    @property
    def ServerCertificates(self):
        r"""<p>Server certificate.</p><p>Input limit: currently only support importing one cert; to use multiple certs, use the cert api CreateListenerAdditionalCert to add other certs.</p><p>Only HTTPS listeners support modification of this parameter.</p>
        :rtype: list of str
        """
        return self._ServerCertificates

    @ServerCertificates.setter
    def ServerCertificates(self, ServerCertificates):
        self._ServerCertificates = ServerCertificates

    @property
    def ClientCaCertificates(self):
        r"""<p>Client certificate.</p><p>Input limitations: 1. Currently only support importing one certificate; to use multiple certificates, use the certificate api CreateListenerAdditionalCert to add other certificates. 2. The certificate must be a CA certificate.</p><p>Only HTTPS listeners support modification of this parameter, and mutual authentication must be enabled.</p>
        :rtype: list of str
        """
        return self._ClientCaCertificates

    @ClientCaCertificates.setter
    def ClientCaCertificates(self, ClientCaCertificates):
        self._ClientCaCertificates = ClientCaCertificates

    @property
    def GetRealIpType(self):
        r"""<p>Method of obtaining the source IP.</p><p>Input parameter limits: support selecting 'ProxyProtocol', 'Close', 'ProxyProtocolV2', 'TOA'.</p><p>Only TCP listeners support modification of this parameter.</p>
        :rtype: str
        """
        return self._GetRealIpType

    @GetRealIpType.setter
    def GetRealIpType(self, GetRealIpType):
        self._GetRealIpType = GetRealIpType


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._IdleTimeout = params.get("IdleTimeout")
        self._ClientAffinity = params.get("ClientAffinity")
        self._ClientAffinityTime = params.get("ClientAffinityTime")
        self._RequestTimeout = params.get("RequestTimeout")
        self._XForwardedForRealIp = params.get("XForwardedForRealIp")
        self._CertificationType = params.get("CertificationType")
        self._CipherPolicyId = params.get("CipherPolicyId")
        self._ServerCertificates = params.get("ServerCertificates")
        self._ClientCaCertificates = params.get("ClientCaCertificates")
        self._GetRealIpType = params.get("GetRealIpType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyListenerResponse(AbstractModel):
    r"""ModifyListener response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>Task ID.</p>
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>Task ID.</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class OriginHeader(AbstractModel):
    r"""Origin-pull Header information

    """

    def __init__(self):
        r"""
        :param _Key: <p>Key.</p><p>Parameter format: 1. The string literal only contains printable ASCII characters. 2. Cannot contain these characters ()&lt;&gt;@,;:\&quot;/[ ]?={ }</p><p>Input parameter limitation: length 1-40.</p>
        :type Key: str
        :param _Value: <p>Value.</p><p>Input parameter limit: length cannot exceed 128.</p><p>If the string contains $, you can only configure '$remote_addr', '$remote_port'; otherwise, it is not supported.</p>
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""<p>Key.</p><p>Parameter format: 1. The string literal only contains printable ASCII characters. 2. Cannot contain these characters ()&lt;&gt;@,;:\&quot;/[ ]?={ }</p><p>Input parameter limitation: length 1-40.</p>
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""<p>Value.</p><p>Input parameter limit: length cannot exceed 128.</p><p>If the string contains $, you can only configure '$remote_addr', '$remote_port'; otherwise, it is not supported.</p>
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortOverride(AbstractModel):
    r"""Port mapping

    """

    def __init__(self):
        r"""
        :param _ListenerPort: Listening port.
        :type ListenerPort: int
        :param _EndpointPort: Mapping port.
        :type EndpointPort: int
        """
        self._ListenerPort = None
        self._EndpointPort = None

    @property
    def ListenerPort(self):
        r"""Listening port.
        :rtype: int
        """
        return self._ListenerPort

    @ListenerPort.setter
    def ListenerPort(self, ListenerPort):
        self._ListenerPort = ListenerPort

    @property
    def EndpointPort(self):
        r"""Mapping port.
        :rtype: int
        """
        return self._EndpointPort

    @EndpointPort.setter
    def EndpointPort(self, EndpointPort):
        self._EndpointPort = EndpointPort


    def _deserialize(self, params):
        self._ListenerPort = params.get("ListenerPort")
        self._EndpointPort = params.get("EndpointPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortRanges(AbstractModel):
    r"""Port range

    """

    def __init__(self):
        r"""
        :param _FromPort: Start port.
        :type FromPort: int
        :param _ToPort: Destination port.
        :type ToPort: int
        """
        self._FromPort = None
        self._ToPort = None

    @property
    def FromPort(self):
        r"""Start port.
        :rtype: int
        """
        return self._FromPort

    @FromPort.setter
    def FromPort(self, FromPort):
        self._FromPort = FromPort

    @property
    def ToPort(self):
        r"""Destination port.
        :rtype: int
        """
        return self._ToPort

    @ToPort.setter
    def ToPort(self, ToPort):
        self._ToPort = ToPort


    def _deserialize(self, params):
        self._FromPort = params.get("FromPort")
        self._ToPort = params.get("ToPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceListenerAdditionalCertRequest(AbstractModel):
    r"""ReplaceListenerAdditionalCert request structure.

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: Global acceleration instance ID.
        :type GlobalAcceleratorId: str
        :param _ListenerId: Listener ID.
        :type ListenerId: str
        :param _AdditionalCertificate: Certificate ID.
        :type AdditionalCertificate: str
        :param _OldCertificate: Old certificate ID.
        :type OldCertificate: str
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._AdditionalCertificate = None
        self._OldCertificate = None

    @property
    def GlobalAcceleratorId(self):
        r"""Global acceleration instance ID.
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""Listener ID.
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def AdditionalCertificate(self):
        r"""Certificate ID.
        :rtype: str
        """
        return self._AdditionalCertificate

    @AdditionalCertificate.setter
    def AdditionalCertificate(self, AdditionalCertificate):
        self._AdditionalCertificate = AdditionalCertificate

    @property
    def OldCertificate(self):
        r"""Old certificate ID.
        :rtype: str
        """
        return self._OldCertificate

    @OldCertificate.setter
    def OldCertificate(self, OldCertificate):
        self._OldCertificate = OldCertificate


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._AdditionalCertificate = params.get("AdditionalCertificate")
        self._OldCertificate = params.get("OldCertificate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceListenerAdditionalCertResponse(AbstractModel):
    r"""ReplaceListenerAdditionalCert response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ResponseHeaders(AbstractModel):
    r"""Header

    """

    def __init__(self):
        r"""
        :param _Key: <p>key</p><p>Parameter format: 1. The string only contain printable ASCII characters. 2. Cannot contain these characters ()&lt;&gt;@,;:\&quot;/[ ]?={ }</p><p>Input limit: Length 1-40.</p>
        :type Key: str
        :param _Value: <p>value</p><p>Input limit: length cannot exceed 128</p><p>If the string contains $, you can only configure '$remote_addr' and '$remote_port'. Otherwise, it is not supported.</p>
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""<p>key</p><p>Parameter format: 1. The string only contain printable ASCII characters. 2. Cannot contain these characters ()&lt;&gt;@,;:\&quot;/[ ]?={ }</p><p>Input limit: Length 1-40.</p>
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""<p>value</p><p>Input limit: length cannot exceed 128</p><p>If the string contains $, you can only configure '$remote_addr' and '$remote_port'. Otherwise, it is not supported.</p>
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleAction(AbstractModel):
    r"""Behavior information of Layer 7 forwarding rules

    """

    def __init__(self):
        r"""
        :param _RuleActionType: <p>Behavior type of the Layer 7 forwarding rule</p><p>Enumeration values:</p><ul><li>ForwardGroup: The forwarding policy forwards to a terminal node group.</li><li>Drop: The forwarding policy drops the request.</li></ul>
        :type RuleActionType: str
        :param _RuleActionValue: <p>Layer 7 forwarding rule action value</p><p>This field is not required to input when RuleActionType is Drop. This field is required when RuleActionType is ForwardGroup, which requires filling in the custom terminal node group ID. The default terminal node group cannot be configured.</p>
        :type RuleActionValue: str
        """
        self._RuleActionType = None
        self._RuleActionValue = None

    @property
    def RuleActionType(self):
        r"""<p>Behavior type of the Layer 7 forwarding rule</p><p>Enumeration values:</p><ul><li>ForwardGroup: The forwarding policy forwards to a terminal node group.</li><li>Drop: The forwarding policy drops the request.</li></ul>
        :rtype: str
        """
        return self._RuleActionType

    @RuleActionType.setter
    def RuleActionType(self, RuleActionType):
        self._RuleActionType = RuleActionType

    @property
    def RuleActionValue(self):
        r"""<p>Layer 7 forwarding rule action value</p><p>This field is not required to input when RuleActionType is Drop. This field is required when RuleActionType is ForwardGroup, which requires filling in the custom terminal node group ID. The default terminal node group cannot be configured.</p>
        :rtype: str
        """
        return self._RuleActionValue

    @RuleActionValue.setter
    def RuleActionValue(self, RuleActionValue):
        self._RuleActionValue = RuleActionValue


    def _deserialize(self, params):
        self._RuleActionType = params.get("RuleActionType")
        self._RuleActionValue = params.get("RuleActionValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleCondition(AbstractModel):
    r"""Conditional information of Layer 7 forwarding rules

    """

    def __init__(self):
        r"""
        :param _RuleConditionType: <p>Condition type of Layer 7 forwarding rule</p><p>Enumeration values:</p><ul><li>Path: Path</li></ul>
        :type RuleConditionType: str
        :param _RuleConditionValue: <p>Layer 7 forwarding rule condition value</p><p>Parameter format: The format must match the regular expression: ^[a-zA-Z0-9_.-/]{1,80}$</p><p>The array length cannot exceed 1.</p>
        :type RuleConditionValue: list of str
        """
        self._RuleConditionType = None
        self._RuleConditionValue = None

    @property
    def RuleConditionType(self):
        r"""<p>Condition type of Layer 7 forwarding rule</p><p>Enumeration values:</p><ul><li>Path: Path</li></ul>
        :rtype: str
        """
        return self._RuleConditionType

    @RuleConditionType.setter
    def RuleConditionType(self, RuleConditionType):
        self._RuleConditionType = RuleConditionType

    @property
    def RuleConditionValue(self):
        r"""<p>Layer 7 forwarding rule condition value</p><p>Parameter format: The format must match the regular expression: ^[a-zA-Z0-9_.-/]{1,80}$</p><p>The array length cannot exceed 1.</p>
        :rtype: list of str
        """
        return self._RuleConditionValue

    @RuleConditionValue.setter
    def RuleConditionValue(self, RuleConditionValue):
        self._RuleConditionValue = RuleConditionValue


    def _deserialize(self, params):
        self._RuleConditionType = params.get("RuleConditionType")
        self._RuleConditionValue = params.get("RuleConditionValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    r"""Tag key-value pair.

    """

    def __init__(self):
        r"""
        :param _Key: Tag key.
        :type Key: str
        :param _Value: Tag value.
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""Tag key.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""Tag value.
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        