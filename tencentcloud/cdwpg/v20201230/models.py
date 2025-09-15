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


class AccessInfo(AbstractModel):
    r"""Access information.

    """

    def __init__(self):
        r"""
        :param _Address: Address.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Address: str
        :param _Protocol: Protocol.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        """
        self._Address = None
        self._Protocol = None

    @property
    def Address(self):
        r"""Address.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Protocol(self):
        r"""Protocol.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._Address = params.get("Address")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountInfo(AbstractModel):
    r"""Description of the account name and instance IDs under the account

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _UserName: Account name.
        :type UserName: str
        :param _Perms: Account attribute.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Perms: list of str
        """
        self._InstanceId = None
        self._UserName = None
        self._Perms = None

    @property
    def InstanceId(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        r"""Account name.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Perms(self):
        r"""Account attribute.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Perms

    @Perms.setter
    def Perms(self, Perms):
        self._Perms = Perms


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._Perms = params.get("Perms")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CBSSpec(AbstractModel):
    r"""Disk specifications.

    """

    def __init__(self):
        r"""
        :param _DiskType: Disk type.

Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskType: str
        :param _DiskSize: Size.

Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskSize: int
        :param _DiskCount: Number.

Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskCount: int
        """
        self._DiskType = None
        self._DiskSize = None
        self._DiskCount = None

    @property
    def DiskType(self):
        r"""Disk type.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        r"""Size.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskCount(self):
        r"""Number.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._DiskCount = params.get("DiskCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CBSSpecInfo(AbstractModel):
    r"""Disk information.

    """

    def __init__(self):
        r"""
        :param _DiskType: Disk type.Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskType: str
        :param _DiskSize: Size.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskSize: int
        :param _DiskCount: Number.Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskCount: int
        """
        self._DiskType = None
        self._DiskSize = None
        self._DiskCount = None

    @property
    def DiskType(self):
        r"""Disk type.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        r"""Size.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskCount(self):
        r"""Number.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._DiskCount = params.get("DiskCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CNResourceSpec(AbstractModel):
    r"""Description of resource specifications

    """

    def __init__(self):
        r"""
        :param _Type: Node type.
        :type Type: str
        :param _SpecName: Model.


        :type SpecName: str
        :param _Count: Number of nodes.
        :type Count: int
        :param _DiskSpec: Disk information.
        :type DiskSpec: :class:`tencentcloud.cdwpg.v20201230.models.CBSSpec`
        """
        self._Type = None
        self._SpecName = None
        self._Count = None
        self._DiskSpec = None

    @property
    def Type(self):
        r"""Node type.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SpecName(self):
        r"""Model.


        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def Count(self):
        r"""Number of nodes.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def DiskSpec(self):
        r"""Disk information.
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.CBSSpec`
        """
        return self._DiskSpec

    @DiskSpec.setter
    def DiskSpec(self, DiskSpec):
        self._DiskSpec = DiskSpec


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._SpecName = params.get("SpecName")
        self._Count = params.get("Count")
        if params.get("DiskSpec") is not None:
            self._DiskSpec = CBSSpec()
            self._DiskSpec._deserialize(params.get("DiskSpec"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChargeProperties(AbstractModel):
    r"""Billing time parameter.

    """

    def __init__(self):
        r"""
        :param _RenewFlag: 1: requires auto-renewal.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RenewFlag: int
        :param _TimeSpan: Order time range.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TimeSpan: int
        :param _TimeUnit: Time unit. Valid values: h and m.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TimeUnit: str
        :param _PayMode: Billing type: 0 indicates pay-as-you-go and 1 indicates monthly subscription.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PayMode: int
        :param _ChargeType: PREPAID and POSTPAID_BY_HOUR
Note: This field may return null, indicating that no valid values can be obtained.
        :type ChargeType: str
        """
        self._RenewFlag = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._PayMode = None
        self._ChargeType = None

    @property
    def RenewFlag(self):
        r"""1: requires auto-renewal.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def TimeSpan(self):
        r"""Order time range.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        r"""Time unit. Valid values: h and m.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def PayMode(self):
        r"""Billing type: 0 indicates pay-as-you-go and 1 indicates monthly subscription.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ChargeType(self):
        r"""PREPAID and POSTPAID_BY_HOUR
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType


    def _deserialize(self, params):
        self._RenewFlag = params.get("RenewFlag")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._PayMode = params.get("PayMode")
        self._ChargeType = params.get("ChargeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigHistory(AbstractModel):
    r"""ConfigHistory1

    """

    def __init__(self):
        r"""
        :param _Id: id
        :type Id: int
        :param _InstanceId: Instance name.
        :type InstanceId: str
        :param _CreatedAt: Creation time.


        :type CreatedAt: str
        :param _UpdatedAt: Update time.
        :type UpdatedAt: str
        :param _NodeType: dn/cn
        :type NodeType: str
        :param _ParamName: Parameter name.
        :type ParamName: str
        :param _ParamNewValue: New parameter value.
        :type ParamNewValue: str
        :param _ParamOldValue: Old parameter value.
        :type ParamOldValue: str
        :param _Status: Status. Valid values: doing and success.
        :type Status: str
        """
        self._Id = None
        self._InstanceId = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._NodeType = None
        self._ParamName = None
        self._ParamNewValue = None
        self._ParamOldValue = None
        self._Status = None

    @property
    def Id(self):
        r"""id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def InstanceId(self):
        r"""Instance name.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CreatedAt(self):
        r"""Creation time.


        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""Update time.
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def NodeType(self):
        r"""dn/cn
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def ParamName(self):
        r"""Parameter name.
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ParamNewValue(self):
        r"""New parameter value.
        :rtype: str
        """
        return self._ParamNewValue

    @ParamNewValue.setter
    def ParamNewValue(self, ParamNewValue):
        self._ParamNewValue = ParamNewValue

    @property
    def ParamOldValue(self):
        r"""Old parameter value.
        :rtype: str
        """
        return self._ParamOldValue

    @ParamOldValue.setter
    def ParamOldValue(self, ParamOldValue):
        self._ParamOldValue = ParamOldValue

    @property
    def Status(self):
        r"""Status. Valid values: doing and success.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._InstanceId = params.get("InstanceId")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._NodeType = params.get("NodeType")
        self._ParamName = params.get("ParamName")
        self._ParamNewValue = params.get("ParamNewValue")
        self._ParamOldValue = params.get("ParamOldValue")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigParams(AbstractModel):
    r"""Parameters

    """

    def __init__(self):
        r"""
        :param _ParameterName: Name.

Note: This field may return null, indicating that no valid values can be obtained.
        :type ParameterName: str
        :param _ParameterValue: Value.

Note: This field may return null, indicating that no valid values can be obtained.
        :type ParameterValue: str
        :param _ParameterOldValue: Value before modification.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ParameterOldValue: str
        """
        self._ParameterName = None
        self._ParameterValue = None
        self._ParameterOldValue = None

    @property
    def ParameterName(self):
        r"""Name.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ParameterName

    @ParameterName.setter
    def ParameterName(self, ParameterName):
        self._ParameterName = ParameterName

    @property
    def ParameterValue(self):
        r"""Value.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ParameterValue

    @ParameterValue.setter
    def ParameterValue(self, ParameterValue):
        self._ParameterValue = ParameterValue

    @property
    def ParameterOldValue(self):
        r"""Value before modification.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ParameterOldValue

    @ParameterOldValue.setter
    def ParameterOldValue(self, ParameterOldValue):
        self._ParameterOldValue = ParameterOldValue


    def _deserialize(self, params):
        self._ParameterName = params.get("ParameterName")
        self._ParameterValue = params.get("ParameterValue")
        self._ParameterOldValue = params.get("ParameterOldValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceByApiRequest(AbstractModel):
    r"""CreateInstanceByApi request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceName: Instance name.
        :type InstanceName: str
        :param _Zone: Availability zone.
        :type Zone: str
        :param _UserVPCId: Virtual Private Cloud (VPC).
        :type UserVPCId: str
        :param _UserSubnetId: Subnet.
        :type UserSubnetId: str
        :param _ChargeProperties: Billing method.
        :type ChargeProperties: :class:`tencentcloud.cdwpg.v20201230.models.ChargeProperties`
        :param _AdminPassword: Instance password.
        :type AdminPassword: str
        :param _Resources: Resource information.
        :type Resources: list of ResourceSpecNew
        :param _Tags: Tag list.Deprecated, use TagItems.
        :type Tags: :class:`tencentcloud.cdwpg.v20201230.models.Tag`
        :param _ProductVersion: Version.
        :type ProductVersion: str
        :param _TagItems:  TagItems list.
        :type TagItems: list of Tag
        """
        self._InstanceName = None
        self._Zone = None
        self._UserVPCId = None
        self._UserSubnetId = None
        self._ChargeProperties = None
        self._AdminPassword = None
        self._Resources = None
        self._Tags = None
        self._ProductVersion = None
        self._TagItems = None

    @property
    def InstanceName(self):
        r"""Instance name.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Zone(self):
        r"""Availability zone.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def UserVPCId(self):
        r"""Virtual Private Cloud (VPC).
        :rtype: str
        """
        return self._UserVPCId

    @UserVPCId.setter
    def UserVPCId(self, UserVPCId):
        self._UserVPCId = UserVPCId

    @property
    def UserSubnetId(self):
        r"""Subnet.
        :rtype: str
        """
        return self._UserSubnetId

    @UserSubnetId.setter
    def UserSubnetId(self, UserSubnetId):
        self._UserSubnetId = UserSubnetId

    @property
    def ChargeProperties(self):
        r"""Billing method.
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.ChargeProperties`
        """
        return self._ChargeProperties

    @ChargeProperties.setter
    def ChargeProperties(self, ChargeProperties):
        self._ChargeProperties = ChargeProperties

    @property
    def AdminPassword(self):
        r"""Instance password.
        :rtype: str
        """
        return self._AdminPassword

    @AdminPassword.setter
    def AdminPassword(self, AdminPassword):
        self._AdminPassword = AdminPassword

    @property
    def Resources(self):
        r"""Resource information.
        :rtype: list of ResourceSpecNew
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def Tags(self):
        r"""Tag list.Deprecated, use TagItems.
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.Tag`
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ProductVersion(self):
        r"""Version.
        :rtype: str
        """
        return self._ProductVersion

    @ProductVersion.setter
    def ProductVersion(self, ProductVersion):
        self._ProductVersion = ProductVersion

    @property
    def TagItems(self):
        r""" TagItems list.
        :rtype: list of Tag
        """
        return self._TagItems

    @TagItems.setter
    def TagItems(self, TagItems):
        self._TagItems = TagItems


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._Zone = params.get("Zone")
        self._UserVPCId = params.get("UserVPCId")
        self._UserSubnetId = params.get("UserSubnetId")
        if params.get("ChargeProperties") is not None:
            self._ChargeProperties = ChargeProperties()
            self._ChargeProperties._deserialize(params.get("ChargeProperties"))
        self._AdminPassword = params.get("AdminPassword")
        if params.get("Resources") is not None:
            self._Resources = []
            for item in params.get("Resources"):
                obj = ResourceSpecNew()
                obj._deserialize(item)
                self._Resources.append(obj)
        if params.get("Tags") is not None:
            self._Tags = Tag()
            self._Tags._deserialize(params.get("Tags"))
        self._ProductVersion = params.get("ProductVersion")
        if params.get("TagItems") is not None:
            self._TagItems = []
            for item in params.get("TagItems"):
                obj = Tag()
                obj._deserialize(item)
                self._TagItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceByApiResponse(AbstractModel):
    r"""CreateInstanceByApi response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Process ID.Note: This field may return null, indicating that no valid values can be obtained.
        :type FlowId: str
        :param _InstanceId: Instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _ErrorMsg: Error message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._InstanceId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Process ID.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceId(self):
        r"""Instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ErrorMsg(self):
        r"""Error message.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._FlowId = params.get("FlowId")
        self._InstanceId = params.get("InstanceId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    r"""DescribeAccounts request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Limit.
        :type Limit: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        r"""Limit.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountsResponse(AbstractModel):
    r"""DescribeAccounts response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of instances.

Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _Accounts: Account array.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Accounts: list of AccountInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Accounts = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of instances.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Accounts(self):
        r"""Account array.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of AccountInfo
        """
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

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
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = AccountInfo()
                obj._deserialize(item)
                self._Accounts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBConfigHistoryRequest(AbstractModel):
    r"""DescribeDBConfigHistory request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _Limit: Limit.
        :type Limit: int
        :param _Offset: Offset.
        :type Offset: int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        r"""Limit.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBConfigHistoryResponse(AbstractModel):
    r"""DescribeDBConfigHistory response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total count.
        :type TotalCount: int
        :param _ConfigHistory: DBConfig history.
        :type ConfigHistory: list of ConfigHistory
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ConfigHistory = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total count.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ConfigHistory(self):
        r"""DBConfig history.
        :rtype: list of ConfigHistory
        """
        return self._ConfigHistory

    @ConfigHistory.setter
    def ConfigHistory(self, ConfigHistory):
        self._ConfigHistory = ConfigHistory

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
        if params.get("ConfigHistory") is not None:
            self._ConfigHistory = []
            for item in params.get("ConfigHistory"):
                obj = ConfigHistory()
                obj._deserialize(item)
                self._ConfigHistory.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDBParamsRequest(AbstractModel):
    r"""DescribeDBParams request structure.

    """

    def __init__(self):
        r"""
        :param _NodeTypes: cn/dn
        :type NodeTypes: list of str
        :param _Limit: Limit.
        :type Limit: int
        :param _Offset: Offset.
        :type Offset: int
        :param _InstanceId: InstanceId.
        :type InstanceId: str
        """
        self._NodeTypes = None
        self._Limit = None
        self._Offset = None
        self._InstanceId = None

    @property
    def NodeTypes(self):
        r"""cn/dn
        :rtype: list of str
        """
        return self._NodeTypes

    @NodeTypes.setter
    def NodeTypes(self, NodeTypes):
        self._NodeTypes = NodeTypes

    @property
    def Limit(self):
        r"""Limit.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def InstanceId(self):
        r"""InstanceId.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._NodeTypes = params.get("NodeTypes")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBParamsResponse(AbstractModel):
    r"""DescribeDBParams response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total count.
        :type TotalCount: int
        :param _Items: Parameters information.
        :type Items: list of ParamItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Items = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total count.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Items(self):
        r"""Parameters information.
        :rtype: list of ParamItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ParamItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeErrorLogRequest(AbstractModel):
    r"""DescribeErrorLog request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _StartTime: Start time.
        :type StartTime: str
        :param _EndTime: End time.
        :type EndTime: str
        :param _Limit: Limit.
        :type Limit: int
        :param _Offset: Offset.
        :type Offset: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        r"""Start time.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        r"""Limit.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeErrorLogResponse(AbstractModel):
    r"""DescribeErrorLog response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total count of messages returned.
        :type TotalCount: int
        :param _ErrorLogDetails: Error log details.
        :type ErrorLogDetails: list of ErrorLogDetail
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ErrorLogDetails = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total count of messages returned.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ErrorLogDetails(self):
        r"""Error log details.
        :rtype: list of ErrorLogDetail
        """
        return self._ErrorLogDetails

    @ErrorLogDetails.setter
    def ErrorLogDetails(self, ErrorLogDetails):
        self._ErrorLogDetails = ErrorLogDetails

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
        if params.get("ErrorLogDetails") is not None:
            self._ErrorLogDetails = []
            for item in params.get("ErrorLogDetails"):
                obj = ErrorLogDetail()
                obj._deserialize(item)
                self._ErrorLogDetails.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceInfoRequest(AbstractModel):
    r"""DescribeInstanceInfo request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceInfoResponse(AbstractModel):
    r"""DescribeInstanceInfo response structure.

    """

    def __init__(self):
        r"""
        :param _SimpleInstanceInfo: Instance description information.
        :type SimpleInstanceInfo: :class:`tencentcloud.cdwpg.v20201230.models.SimpleInstanceInfo`
        :param _ErrorMsg: Error message.
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SimpleInstanceInfo = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def SimpleInstanceInfo(self):
        r"""Instance description information.
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.SimpleInstanceInfo`
        """
        return self._SimpleInstanceInfo

    @SimpleInstanceInfo.setter
    def SimpleInstanceInfo(self, SimpleInstanceInfo):
        self._SimpleInstanceInfo = SimpleInstanceInfo

    @property
    def ErrorMsg(self):
        r"""Error message.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        if params.get("SimpleInstanceInfo") is not None:
            self._SimpleInstanceInfo = SimpleInstanceInfo()
            self._SimpleInstanceInfo._deserialize(params.get("SimpleInstanceInfo"))
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DescribeInstanceNodesRequest(AbstractModel):
    r"""DescribeInstanceNodes request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: InstanceId.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""InstanceId.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceNodesResponse(AbstractModel):
    r"""DescribeInstanceNodes response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: error msg
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _InstanceNodes: Node list.

Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceNodes: list of InstanceNode
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._InstanceNodes = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        r"""error msg
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def InstanceNodes(self):
        r"""Node list.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of InstanceNode
        """
        return self._InstanceNodes

    @InstanceNodes.setter
    def InstanceNodes(self, InstanceNodes):
        self._InstanceNodes = InstanceNodes

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
        self._ErrorMsg = params.get("ErrorMsg")
        if params.get("InstanceNodes") is not None:
            self._InstanceNodes = []
            for item in params.get("InstanceNodes"):
                obj = InstanceNode()
                obj._deserialize(item)
                self._InstanceNodes.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceOperationsRequest(AbstractModel):
    r"""DescribeInstanceOperations request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: InstanceId.
        :type InstanceId: str
        :param _Offset: Offset.
        :type Offset: int
        :param _Limit: Limit.
        :type Limit: int
        :param _StartTime: Start time.
        :type StartTime: str
        :param _EndTime: End time.
        :type EndTime: str
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._StartTime = None
        self._EndTime = None

    @property
    def InstanceId(self):
        r"""InstanceId.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        r"""Offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Limit.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def StartTime(self):
        r"""Start time.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceOperationsResponse(AbstractModel):
    r"""DescribeInstanceOperations response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total count of operation records.
        :type TotalCount: int
        :param _Operations: operation records.

Note: This field may return null, indicating that no valid values can be obtained.
        :type Operations: list of InstanceOperation
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Operations = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total count of operation records.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Operations(self):
        r"""operation records.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of InstanceOperation
        """
        return self._Operations

    @Operations.setter
    def Operations(self, Operations):
        self._Operations = Operations

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
        if params.get("Operations") is not None:
            self._Operations = []
            for item in params.get("Operations"):
                obj = InstanceOperation()
                obj._deserialize(item)
                self._Operations.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceRequest(AbstractModel):
    r"""DescribeInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: instance ID.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceResponse(AbstractModel):
    r"""DescribeInstance response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceInfo: Instance description information.
        :type InstanceInfo: :class:`tencentcloud.cdwpg.v20201230.models.InstanceInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceInfo = None
        self._RequestId = None

    @property
    def InstanceInfo(self):
        r"""Instance description information.
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.InstanceInfo`
        """
        return self._InstanceInfo

    @InstanceInfo.setter
    def InstanceInfo(self, InstanceInfo):
        self._InstanceInfo = InstanceInfo

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
        if params.get("InstanceInfo") is not None:
            self._InstanceInfo = InstanceInfo()
            self._InstanceInfo._deserialize(params.get("InstanceInfo"))
        self._RequestId = params.get("RequestId")


class DescribeInstanceStateRequest(AbstractModel):
    r"""DescribeInstanceState request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId:  InstanceId.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r""" InstanceId.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceStateResponse(AbstractModel):
    r"""DescribeInstanceState response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceState: Instance status. Example: serving.
        :type InstanceState: str
        :param _FlowCreateTime: Creation time of instance operation.Note: This field may return null, indicating that no valid values can be obtained.
        :type FlowCreateTime: str
        :param _FlowName: Instance operation name.Note: This field may return null, indicating that no valid values can be obtained.
        :type FlowName: str
        :param _FlowProgress: Instance operation progress.Note: This field may return null, indicating that no valid values can be obtained.
        :type FlowProgress: float
        :param _InstanceStateDesc: Instance status description. Example: running.Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceStateDesc: str
        :param _FlowMsg: Instance process error messages. Example: "Creation failed, insufficient resources."
Note: This field may return null, indicating that no valid values can be obtained.
        :type FlowMsg: str
        :param _ProcessName: The name of the current step. Example: "Purchasing resources."Note: This field may return null, indicating that no valid values can be obtained.
        :type ProcessName: str
        :param _BackupStatus: Enabling status of the instance backup task.Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupStatus: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceState = None
        self._FlowCreateTime = None
        self._FlowName = None
        self._FlowProgress = None
        self._InstanceStateDesc = None
        self._FlowMsg = None
        self._ProcessName = None
        self._BackupStatus = None
        self._RequestId = None

    @property
    def InstanceState(self):
        r"""Instance status. Example: serving.
        :rtype: str
        """
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def FlowCreateTime(self):
        r"""Creation time of instance operation.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FlowCreateTime

    @FlowCreateTime.setter
    def FlowCreateTime(self, FlowCreateTime):
        self._FlowCreateTime = FlowCreateTime

    @property
    def FlowName(self):
        r"""Instance operation name.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def FlowProgress(self):
        r"""Instance operation progress.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._FlowProgress

    @FlowProgress.setter
    def FlowProgress(self, FlowProgress):
        self._FlowProgress = FlowProgress

    @property
    def InstanceStateDesc(self):
        r"""Instance status description. Example: running.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceStateDesc

    @InstanceStateDesc.setter
    def InstanceStateDesc(self, InstanceStateDesc):
        self._InstanceStateDesc = InstanceStateDesc

    @property
    def FlowMsg(self):
        r"""Instance process error messages. Example: "Creation failed, insufficient resources."
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FlowMsg

    @FlowMsg.setter
    def FlowMsg(self, FlowMsg):
        self._FlowMsg = FlowMsg

    @property
    def ProcessName(self):
        r"""The name of the current step. Example: "Purchasing resources."Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def BackupStatus(self):
        r"""Enabling status of the instance backup task.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._BackupStatus

    @BackupStatus.setter
    def BackupStatus(self, BackupStatus):
        self._BackupStatus = BackupStatus

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
        self._InstanceState = params.get("InstanceState")
        self._FlowCreateTime = params.get("FlowCreateTime")
        self._FlowName = params.get("FlowName")
        self._FlowProgress = params.get("FlowProgress")
        self._InstanceStateDesc = params.get("InstanceStateDesc")
        self._FlowMsg = params.get("FlowMsg")
        self._ProcessName = params.get("ProcessName")
        self._BackupStatus = params.get("BackupStatus")
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    r"""DescribeInstances request structure.

    """

    def __init__(self):
        r"""
        :param _SearchInstanceId: Searches by instance ID.
        :type SearchInstanceId: str
        :param _SearchInstanceName: Searches by instance name.
        :type SearchInstanceName: str
        :param _Offset: Offset.
        :type Offset: int
        :param _Limit: Limit.
        :type Limit: int
        :param _SearchTags: Searched tag list.
        :type SearchTags: list of SearchTags
        """
        self._SearchInstanceId = None
        self._SearchInstanceName = None
        self._Offset = None
        self._Limit = None
        self._SearchTags = None

    @property
    def SearchInstanceId(self):
        r"""Searches by instance ID.
        :rtype: str
        """
        return self._SearchInstanceId

    @SearchInstanceId.setter
    def SearchInstanceId(self, SearchInstanceId):
        self._SearchInstanceId = SearchInstanceId

    @property
    def SearchInstanceName(self):
        r"""Searches by instance name.
        :rtype: str
        """
        return self._SearchInstanceName

    @SearchInstanceName.setter
    def SearchInstanceName(self, SearchInstanceName):
        self._SearchInstanceName = SearchInstanceName

    @property
    def Offset(self):
        r"""Offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Limit.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchTags(self):
        r"""Searched tag list.
        :rtype: list of SearchTags
        """
        return self._SearchTags

    @SearchTags.setter
    def SearchTags(self, SearchTags):
        self._SearchTags = SearchTags


    def _deserialize(self, params):
        self._SearchInstanceId = params.get("SearchInstanceId")
        self._SearchInstanceName = params.get("SearchInstanceName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("SearchTags") is not None:
            self._SearchTags = []
            for item in params.get("SearchTags"):
                obj = SearchTags()
                obj._deserialize(item)
                self._SearchTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    r"""DescribeInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total count of instances.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _InstancesList: Instance array.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstancesList: list of InstanceInfo
        :param _ErrorMsg: Error message.

Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstancesList = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total count of instances.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstancesList(self):
        r"""Instance array.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of InstanceInfo
        """
        return self._InstancesList

    @InstancesList.setter
    def InstancesList(self, InstancesList):
        self._InstancesList = InstancesList

    @property
    def ErrorMsg(self):
        r"""Error message.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        if params.get("InstancesList") is not None:
            self._InstancesList = []
            for item in params.get("InstancesList"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self._InstancesList.append(obj)
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DescribeSimpleInstancesRequest(AbstractModel):
    r"""DescribeSimpleInstances request structure.

    """

    def __init__(self):
        r"""
        :param _SearchInstanceId: Searches by instance ID.
        :type SearchInstanceId: str
        :param _SearchInstanceName: Searches by instance name.
        :type SearchInstanceName: str
        :param _Offset: Offset.
        :type Offset: int
        :param _Limit: Limit.
        :type Limit: int
        :param _SearchTags: Searches by tag list.
        :type SearchTags: list of str
        """
        self._SearchInstanceId = None
        self._SearchInstanceName = None
        self._Offset = None
        self._Limit = None
        self._SearchTags = None

    @property
    def SearchInstanceId(self):
        r"""Searches by instance ID.
        :rtype: str
        """
        return self._SearchInstanceId

    @SearchInstanceId.setter
    def SearchInstanceId(self, SearchInstanceId):
        self._SearchInstanceId = SearchInstanceId

    @property
    def SearchInstanceName(self):
        r"""Searches by instance name.
        :rtype: str
        """
        return self._SearchInstanceName

    @SearchInstanceName.setter
    def SearchInstanceName(self, SearchInstanceName):
        self._SearchInstanceName = SearchInstanceName

    @property
    def Offset(self):
        r"""Offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Limit.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchTags(self):
        r"""Searches by tag list.
        :rtype: list of str
        """
        return self._SearchTags

    @SearchTags.setter
    def SearchTags(self, SearchTags):
        self._SearchTags = SearchTags


    def _deserialize(self, params):
        self._SearchInstanceId = params.get("SearchInstanceId")
        self._SearchInstanceName = params.get("SearchInstanceName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchTags = params.get("SearchTags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSimpleInstancesResponse(AbstractModel):
    r"""DescribeSimpleInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total count of instance lists.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _InstancesList: Instance list details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstancesList: list of InstanceSimpleInfoNew
        :param _ErrorMsg: Error message.

Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstancesList = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total count of instance lists.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstancesList(self):
        r"""Instance list details.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of InstanceSimpleInfoNew
        """
        return self._InstancesList

    @InstancesList.setter
    def InstancesList(self, InstancesList):
        self._InstancesList = InstancesList

    @property
    def ErrorMsg(self):
        r"""Error message.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        if params.get("InstancesList") is not None:
            self._InstancesList = []
            for item in params.get("InstancesList"):
                obj = InstanceSimpleInfoNew()
                obj._deserialize(item)
                self._InstancesList.append(obj)
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DescribeSlowLogRequest(AbstractModel):
    r"""DescribeSlowLog request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: InstanceId.
        :type InstanceId: str
        :param _StartTime: Start time.
        :type StartTime: str
        :param _EndTime: End time.
        :type EndTime: str
        :param _Limit: Limit.
        :type Limit: int
        :param _Offset: Offset.
        :type Offset: int
        :param _Database: Database.
        :type Database: str
        :param _OrderBy: Sorting method.
        :type OrderBy: str
        :param _OrderByType: Ascending or descending order.
        :type OrderByType: str
        :param _Duration: Duration.
        :type Duration: float
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._Database = None
        self._OrderBy = None
        self._OrderByType = None
        self._Duration = None

    @property
    def InstanceId(self):
        r"""InstanceId.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        r"""Start time.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        r"""Limit.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Database(self):
        r"""Database.
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def OrderBy(self):
        r"""Sorting method.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderByType(self):
        r"""Ascending or descending order.
        :rtype: str
        """
        return self._OrderByType

    @OrderByType.setter
    def OrderByType(self, OrderByType):
        self._OrderByType = OrderByType

    @property
    def Duration(self):
        r"""Duration.
        :rtype: float
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Database = params.get("Database")
        self._OrderBy = params.get("OrderBy")
        self._OrderByType = params.get("OrderByType")
        self._Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogResponse(AbstractModel):
    r"""DescribeSlowLog response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total count of messages returned.
        :type TotalCount: int
        :param _SlowLogDetails: Slow SQL log details.
        :type SlowLogDetails: :class:`tencentcloud.cdwpg.v20201230.models.SlowLogDetail`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._SlowLogDetails = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total count of messages returned.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SlowLogDetails(self):
        r"""Slow SQL log details.
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.SlowLogDetail`
        """
        return self._SlowLogDetails

    @SlowLogDetails.setter
    def SlowLogDetails(self, SlowLogDetails):
        self._SlowLogDetails = SlowLogDetails

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
        if params.get("SlowLogDetails") is not None:
            self._SlowLogDetails = SlowLogDetail()
            self._SlowLogDetails._deserialize(params.get("SlowLogDetails"))
        self._RequestId = params.get("RequestId")


class DescribeUpgradeListRequest(AbstractModel):
    r"""DescribeUpgradeList request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: InstanceId.
        :type InstanceId: str
        :param _Offset: Offset.
        :type Offset: int
        :param _Limit: Limit.
        :type Limit: int
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        r"""InstanceId.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        r"""Offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Limit.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUpgradeListResponse(AbstractModel):
    r"""DescribeUpgradeList response structure.

    """

    def __init__(self):
        r"""
        :param _UpgradeItems: Details of instance upgrade records.Note: This field may return null, indicating that no valid values can be obtained.
        :type UpgradeItems: list of UpgradeItem
        :param _TotalCount: Total count of upgrade records.
        :type TotalCount: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UpgradeItems = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def UpgradeItems(self):
        r"""Details of instance upgrade records.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of UpgradeItem
        """
        return self._UpgradeItems

    @UpgradeItems.setter
    def UpgradeItems(self, UpgradeItems):
        self._UpgradeItems = UpgradeItems

    @property
    def TotalCount(self):
        r"""Total count of upgrade records.
        :rtype: str
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
        if params.get("UpgradeItems") is not None:
            self._UpgradeItems = []
            for item in params.get("UpgradeItems"):
                obj = UpgradeItem()
                obj._deserialize(item)
                self._UpgradeItems.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeUserHbaConfigRequest(AbstractModel):
    r"""DescribeUserHbaConfig request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: InstanceId.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""InstanceId.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserHbaConfigResponse(AbstractModel):
    r"""DescribeUserHbaConfig response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of instances.

Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _HbaConfigs: Hba Config array.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HbaConfigs: list of HbaConfig
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._HbaConfigs = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of instances.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def HbaConfigs(self):
        r"""Hba Config array.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of HbaConfig
        """
        return self._HbaConfigs

    @HbaConfigs.setter
    def HbaConfigs(self, HbaConfigs):
        self._HbaConfigs = HbaConfigs

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
        if params.get("HbaConfigs") is not None:
            self._HbaConfigs = []
            for item in params.get("HbaConfigs"):
                obj = HbaConfig()
                obj._deserialize(item)
                self._HbaConfigs.append(obj)
        self._RequestId = params.get("RequestId")


class DestroyInstanceByApiRequest(AbstractModel):
    r"""DestroyInstanceByApi request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance id. Example: "cdwpg-xxxx".
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Instance id. Example: "cdwpg-xxxx".
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyInstanceByApiResponse(AbstractModel):
    r"""DestroyInstanceByApi response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Destroy  process ID.
        :type FlowId: str
        :param _ErrorMsg: Error message.
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""Destroy  process ID.
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ErrorMsg(self):
        r"""Error message.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._FlowId = params.get("FlowId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DiskSpecPlus(AbstractModel):
    r"""Disk specifications.

    """

    def __init__(self):
        r"""
        :param _DiskCount: Number of disks.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskCount: int
        :param _MaxDiskSize: Maximum disk capacity.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxDiskSize: int
        :param _MinDiskSize: Minimum disk capacity.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MinDiskSize: int
        :param _DiskType: Disk type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskType: str
        :param _DiskDesc: Disk type details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskDesc: str
        :param _CvmClass: Model type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CvmClass: str
        """
        self._DiskCount = None
        self._MaxDiskSize = None
        self._MinDiskSize = None
        self._DiskType = None
        self._DiskDesc = None
        self._CvmClass = None

    @property
    def DiskCount(self):
        r"""Number of disks.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount

    @property
    def MaxDiskSize(self):
        r"""Maximum disk capacity.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MaxDiskSize

    @MaxDiskSize.setter
    def MaxDiskSize(self, MaxDiskSize):
        self._MaxDiskSize = MaxDiskSize

    @property
    def MinDiskSize(self):
        r"""Minimum disk capacity.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MinDiskSize

    @MinDiskSize.setter
    def MinDiskSize(self, MinDiskSize):
        self._MinDiskSize = MinDiskSize

    @property
    def DiskType(self):
        r"""Disk type.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskDesc(self):
        r"""Disk type details.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DiskDesc

    @DiskDesc.setter
    def DiskDesc(self, DiskDesc):
        self._DiskDesc = DiskDesc

    @property
    def CvmClass(self):
        r"""Model type.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CvmClass

    @CvmClass.setter
    def CvmClass(self, CvmClass):
        self._CvmClass = CvmClass


    def _deserialize(self, params):
        self._DiskCount = params.get("DiskCount")
        self._MaxDiskSize = params.get("MaxDiskSize")
        self._MinDiskSize = params.get("MinDiskSize")
        self._DiskType = params.get("DiskType")
        self._DiskDesc = params.get("DiskDesc")
        self._CvmClass = params.get("CvmClass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrorLogDetail(AbstractModel):
    r"""Error log details

    """

    def __init__(self):
        r"""
        :param _UserName: Username.

Note: This field may return null, indicating that no valid values can be obtained.
        :type UserName: str
        :param _Database: Database.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Database: str
        :param _ErrorTime: The time an error was reported.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorTime: str
        :param _ErrorMessage: Error message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMessage: str
        """
        self._UserName = None
        self._Database = None
        self._ErrorTime = None
        self._ErrorMessage = None

    @property
    def UserName(self):
        r"""Username.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Database(self):
        r"""Database.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def ErrorTime(self):
        r"""The time an error was reported.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorTime

    @ErrorTime.setter
    def ErrorTime(self, ErrorTime):
        self._ErrorTime = ErrorTime

    @property
    def ErrorMessage(self):
        r"""Error message.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Database = params.get("Database")
        self._ErrorTime = params.get("ErrorTime")
        self._ErrorMessage = params.get("ErrorMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HbaConfig(AbstractModel):
    r"""user_config

    """

    def __init__(self):
        r"""
        :param _Type: Type.
        :type Type: str
        :param _Database: Database.
        :type Database: str
        :param _User: User.
        :type User: str
        :param _Address: IP address.
        :type Address: str
        :param _Method: Method.
        :type Method: str
        :param _Mask: Indicates whether to perform overwriting.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Mask: str
        """
        self._Type = None
        self._Database = None
        self._User = None
        self._Address = None
        self._Method = None
        self._Mask = None

    @property
    def Type(self):
        r"""Type.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Database(self):
        r"""Database.
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def User(self):
        r"""User.
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Address(self):
        r"""IP address.
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Method(self):
        r"""Method.
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Mask(self):
        r"""Indicates whether to perform overwriting.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Mask

    @Mask.setter
    def Mask(self, Mask):
        self._Mask = Mask


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Database = params.get("Database")
        self._User = params.get("User")
        self._Address = params.get("Address")
        self._Method = params.get("Method")
        self._Mask = params.get("Mask")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfo(AbstractModel):
    r"""instance information.

    """

    def __init__(self):
        r"""
        :param _ID: Instance ID 
Note: This field may return null, indicating that no valid values can be obtained.
        :type ID: int
        :param _InstanceType: Kernel version type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceType: str
        :param _InstanceName: Cluster name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param _Status: Cluster status.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _StatusDesc: Cluster status details.Note: This field may return null, indicating that no valid values can be obtained.
        :type StatusDesc: str
        :param _InstanceStateInfo: Cluster status information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceStateInfo: :class:`tencentcloud.cdwpg.v20201230.models.InstanceStateInfo`
        :param _InstanceID: Cluster ID.

Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceID: str
        :param _CreateTime: Creation time.

Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _Region: Region.

Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _Zone: Region.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Zone: str
        :param _RegionDesc: Region details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionDesc: str
        :param _ZoneDesc: Region details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneDesc: str
        :param _Tags: Tag.Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _Version: Kernel version.

Note: This field may return null, indicating that no valid values can be obtained.
        :type Version: str
        :param _Charset: Character set.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Charset: str
        :param _CNNodes: CN node list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CNNodes: list of InstanceNodeGroup
        :param _DNNodes: DN node list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DNNodes: list of InstanceNodeGroup
        :param _RegionId: Region ID.

Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionId: int
        :param _ZoneId: Region ID.

Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneId: int
        :param _VpcId: Virtual Private Cloud (VPC).

Note: This field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param _SubnetId: Subnet.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param _ExpireTime: Expiration time.

Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param _PayMode: Billing mode.

Note: This field may return null, indicating that no valid values can be obtained.
        :type PayMode: str
        :param _RenewFlag: Automatic renewal.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RenewFlag: bool
        :param _InstanceId: Cluster ID.

Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _AccessDetails: Access information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccessDetails: list of AccessInfo
        """
        self._ID = None
        self._InstanceType = None
        self._InstanceName = None
        self._Status = None
        self._StatusDesc = None
        self._InstanceStateInfo = None
        self._InstanceID = None
        self._CreateTime = None
        self._Region = None
        self._Zone = None
        self._RegionDesc = None
        self._ZoneDesc = None
        self._Tags = None
        self._Version = None
        self._Charset = None
        self._CNNodes = None
        self._DNNodes = None
        self._RegionId = None
        self._ZoneId = None
        self._VpcId = None
        self._SubnetId = None
        self._ExpireTime = None
        self._PayMode = None
        self._RenewFlag = None
        self._InstanceId = None
        self._AccessDetails = None

    @property
    def ID(self):
        r"""Instance ID 
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def InstanceType(self):
        r"""Kernel version type.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceName(self):
        r"""Cluster name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Status(self):
        r"""Cluster status.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        r"""Cluster status details.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def InstanceStateInfo(self):
        r"""Cluster status information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.InstanceStateInfo`
        """
        return self._InstanceStateInfo

    @InstanceStateInfo.setter
    def InstanceStateInfo(self, InstanceStateInfo):
        self._InstanceStateInfo = InstanceStateInfo

    @property
    def InstanceID(self):
        r"""Cluster ID.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def CreateTime(self):
        r"""Creation time.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Region(self):
        r"""Region.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        r"""Region.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def RegionDesc(self):
        r"""Region details.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RegionDesc

    @RegionDesc.setter
    def RegionDesc(self, RegionDesc):
        self._RegionDesc = RegionDesc

    @property
    def ZoneDesc(self):
        r"""Region details.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ZoneDesc

    @ZoneDesc.setter
    def ZoneDesc(self, ZoneDesc):
        self._ZoneDesc = ZoneDesc

    @property
    def Tags(self):
        r"""Tag.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Version(self):
        r"""Kernel version.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Charset(self):
        r"""Character set.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def CNNodes(self):
        r"""CN node list.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of InstanceNodeGroup
        """
        return self._CNNodes

    @CNNodes.setter
    def CNNodes(self, CNNodes):
        self._CNNodes = CNNodes

    @property
    def DNNodes(self):
        r"""DN node list.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of InstanceNodeGroup
        """
        return self._DNNodes

    @DNNodes.setter
    def DNNodes(self, DNNodes):
        self._DNNodes = DNNodes

    @property
    def RegionId(self):
        r"""Region ID.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        r"""Region ID.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcId(self):
        r"""Virtual Private Cloud (VPC).

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""Subnet.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ExpireTime(self):
        r"""Expiration time.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def PayMode(self):
        r"""Billing mode.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def RenewFlag(self):
        r"""Automatic renewal.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def InstanceId(self):
        r"""Cluster ID.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AccessDetails(self):
        r"""Access information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of AccessInfo
        """
        return self._AccessDetails

    @AccessDetails.setter
    def AccessDetails(self, AccessDetails):
        self._AccessDetails = AccessDetails


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._InstanceType = params.get("InstanceType")
        self._InstanceName = params.get("InstanceName")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        if params.get("InstanceStateInfo") is not None:
            self._InstanceStateInfo = InstanceStateInfo()
            self._InstanceStateInfo._deserialize(params.get("InstanceStateInfo"))
        self._InstanceID = params.get("InstanceID")
        self._CreateTime = params.get("CreateTime")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._RegionDesc = params.get("RegionDesc")
        self._ZoneDesc = params.get("ZoneDesc")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Version = params.get("Version")
        self._Charset = params.get("Charset")
        if params.get("CNNodes") is not None:
            self._CNNodes = []
            for item in params.get("CNNodes"):
                obj = InstanceNodeGroup()
                obj._deserialize(item)
                self._CNNodes.append(obj)
        if params.get("DNNodes") is not None:
            self._DNNodes = []
            for item in params.get("DNNodes"):
                obj = InstanceNodeGroup()
                obj._deserialize(item)
                self._DNNodes.append(obj)
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._ExpireTime = params.get("ExpireTime")
        self._PayMode = params.get("PayMode")
        self._RenewFlag = params.get("RenewFlag")
        self._InstanceId = params.get("InstanceId")
        if params.get("AccessDetails") is not None:
            self._AccessDetails = []
            for item in params.get("AccessDetails"):
                obj = AccessInfo()
                obj._deserialize(item)
                self._AccessDetails.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNode(AbstractModel):
    r"""Instance node

    """

    def __init__(self):
        r"""
        :param _NodeId: id
        :type NodeId: int
        :param _NodeType: cn
        :type NodeType: str
        :param _NodeIp: ip
        :type NodeIp: str
        """
        self._NodeId = None
        self._NodeType = None
        self._NodeIp = None

    @property
    def NodeId(self):
        r"""id
        :rtype: int
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeType(self):
        r"""cn
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def NodeIp(self):
        r"""ip
        :rtype: str
        """
        return self._NodeIp

    @NodeIp.setter
    def NodeIp(self, NodeIp):
        self._NodeIp = NodeIp


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._NodeType = params.get("NodeType")
        self._NodeIp = params.get("NodeIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNodeGroup(AbstractModel):
    r"""Instance node information.

    """

    def __init__(self):
        r"""
        :param _SpecName: Model.

Note: This field may return null, indicating that no valid values can be obtained.
        :type SpecName: str
        :param _DataDisk: Disk information.

Note: This field may return null, indicating that no valid values can be obtained.
        :type DataDisk: :class:`tencentcloud.cdwpg.v20201230.models.DiskSpecPlus`
        :param _CvmCount: Number of machines.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CvmCount: int
        """
        self._SpecName = None
        self._DataDisk = None
        self._CvmCount = None

    @property
    def SpecName(self):
        r"""Model.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def DataDisk(self):
        r"""Disk information.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.DiskSpecPlus`
        """
        return self._DataDisk

    @DataDisk.setter
    def DataDisk(self, DataDisk):
        self._DataDisk = DataDisk

    @property
    def CvmCount(self):
        r"""Number of machines.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CvmCount

    @CvmCount.setter
    def CvmCount(self, CvmCount):
        self._CvmCount = CvmCount


    def _deserialize(self, params):
        self._SpecName = params.get("SpecName")
        if params.get("DataDisk") is not None:
            self._DataDisk = DiskSpecPlus()
            self._DataDisk._deserialize(params.get("DataDisk"))
        self._CvmCount = params.get("CvmCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceOperation(AbstractModel):
    r"""Cluster operation description

    """

    def __init__(self):
        r"""
        :param _Id: Operation name, such as create_instance, and scaleout_instance
        :type Id: int
        :param _InstanceId: Cluster ID.

Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _Action: Operation name description, such as creating, and modifying the cluster name.

Note: This field may return null, indicating that no valid values can be obtained.
        :type Action: str
        :param _Status: Status.

Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _StartTime: Operation start time.

Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param _EndTime: Operation end time.

Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        :param _Context: Operation context.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Context: str
        :param _UpdateTime: Operation update time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param _Uin: Operation UIN.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Uin: str
        """
        self._Id = None
        self._InstanceId = None
        self._Action = None
        self._Status = None
        self._StartTime = None
        self._EndTime = None
        self._Context = None
        self._UpdateTime = None
        self._Uin = None

    @property
    def Id(self):
        r"""Operation name, such as create_instance, and scaleout_instance
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def InstanceId(self):
        r"""Cluster ID.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Action(self):
        r"""Operation name description, such as creating, and modifying the cluster name.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Status(self):
        r"""Status.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        r"""Operation start time.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Operation end time.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Context(self):
        r"""Operation context.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def UpdateTime(self):
        r"""Operation update time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Uin(self):
        r"""Operation UIN.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._InstanceId = params.get("InstanceId")
        self._Action = params.get("Action")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Context = params.get("Context")
        self._UpdateTime = params.get("UpdateTime")
        self._Uin = params.get("Uin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceSimpleInfoNew(AbstractModel):
    r"""Simplified instance information.

    """

    def __init__(self):
        r"""
        :param _ID: ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ID: int
        :param _InstanceId: Cluster ID.

Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _InstanceName: Cluster name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param _Version: Kernel version.

Note: This field may return null, indicating that no valid values can be obtained.
        :type Version: str
        :param _Region: Region.

Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _RegionId: Region ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionId: int
        :param _RegionDesc: Region details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionDesc: str
        :param _Zone: Region.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Zone: str
        :param _ZoneId: Region ID.

Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneId: int
        :param _ZoneDesc: Region details.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneDesc: str
        :param _VpcId: Virtual Private Cloud (VPC).

Note: This field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param _SubnetId: Subnet.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param _CreateTime: Start time.

Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _ExpireTime: Expiration time.

Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param _AccessInfo: Access address.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccessInfo: str
        :param _PayMode: Billing mode.

Note: This field may return null, indicating that no valid values can be obtained.
        :type PayMode: str
        :param _RenewFlag: Automatic renewal.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RenewFlag: bool
        """
        self._ID = None
        self._InstanceId = None
        self._InstanceName = None
        self._Version = None
        self._Region = None
        self._RegionId = None
        self._RegionDesc = None
        self._Zone = None
        self._ZoneId = None
        self._ZoneDesc = None
        self._VpcId = None
        self._SubnetId = None
        self._CreateTime = None
        self._ExpireTime = None
        self._AccessInfo = None
        self._PayMode = None
        self._RenewFlag = None

    @property
    def ID(self):
        r"""ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def InstanceId(self):
        r"""Cluster ID.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""Cluster name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Version(self):
        r"""Kernel version.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Region(self):
        r"""Region.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionId(self):
        r"""Region ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionDesc(self):
        r"""Region details.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RegionDesc

    @RegionDesc.setter
    def RegionDesc(self, RegionDesc):
        self._RegionDesc = RegionDesc

    @property
    def Zone(self):
        r"""Region.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneId(self):
        r"""Region ID.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneDesc(self):
        r"""Region details.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ZoneDesc

    @ZoneDesc.setter
    def ZoneDesc(self, ZoneDesc):
        self._ZoneDesc = ZoneDesc

    @property
    def VpcId(self):
        r"""Virtual Private Cloud (VPC).

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""Subnet.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def CreateTime(self):
        r"""Start time.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        r"""Expiration time.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def AccessInfo(self):
        r"""Access address.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AccessInfo

    @AccessInfo.setter
    def AccessInfo(self, AccessInfo):
        self._AccessInfo = AccessInfo

    @property
    def PayMode(self):
        r"""Billing mode.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def RenewFlag(self):
        r"""Automatic renewal.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Version = params.get("Version")
        self._Region = params.get("Region")
        self._RegionId = params.get("RegionId")
        self._RegionDesc = params.get("RegionDesc")
        self._Zone = params.get("Zone")
        self._ZoneId = params.get("ZoneId")
        self._ZoneDesc = params.get("ZoneDesc")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._AccessInfo = params.get("AccessInfo")
        self._PayMode = params.get("PayMode")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceStateInfo(AbstractModel):
    r"""Instance State Information

    """

    def __init__(self):
        r"""
        :param _InstanceState: Instance status. Example: serving.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceState: str
        :param _FlowCreateTime: Creation time of instance operation.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FlowCreateTime: str
        :param _FlowName: Instance operation name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FlowName: str
        :param _FlowProgress: Instance operation progress.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FlowProgress: int
        :param _InstanceStateDesc: Instance status description. Example: running.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceStateDesc: str
        :param _FlowMsg: Instance process error messages. Example: "Creation failed, insufficient resources."
Note: This field may return null, indicating that no valid values can be obtained.
        :type FlowMsg: str
        :param _ProcessName: The name of the current step. Example: "Purchasing resources."
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProcessName: str
        :param _BackupStatus: Indicates whether there is a backup task in the instance. 1 indicates yes and 0 indicates no.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupStatus: int
        :param _RequestId: Request ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RequestId: str
        :param _BackupOpenStatus: Indicates whether there is a backup task in the cluster. 1 indicates yes and 0 indicates no.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BackupOpenStatus: int
        """
        self._InstanceState = None
        self._FlowCreateTime = None
        self._FlowName = None
        self._FlowProgress = None
        self._InstanceStateDesc = None
        self._FlowMsg = None
        self._ProcessName = None
        self._BackupStatus = None
        self._RequestId = None
        self._BackupOpenStatus = None

    @property
    def InstanceState(self):
        r"""Instance status. Example: serving.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def FlowCreateTime(self):
        r"""Creation time of instance operation.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FlowCreateTime

    @FlowCreateTime.setter
    def FlowCreateTime(self, FlowCreateTime):
        self._FlowCreateTime = FlowCreateTime

    @property
    def FlowName(self):
        r"""Instance operation name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def FlowProgress(self):
        r"""Instance operation progress.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._FlowProgress

    @FlowProgress.setter
    def FlowProgress(self, FlowProgress):
        self._FlowProgress = FlowProgress

    @property
    def InstanceStateDesc(self):
        r"""Instance status description. Example: running.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceStateDesc

    @InstanceStateDesc.setter
    def InstanceStateDesc(self, InstanceStateDesc):
        self._InstanceStateDesc = InstanceStateDesc

    @property
    def FlowMsg(self):
        r"""Instance process error messages. Example: "Creation failed, insufficient resources."
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FlowMsg

    @FlowMsg.setter
    def FlowMsg(self, FlowMsg):
        self._FlowMsg = FlowMsg

    @property
    def ProcessName(self):
        r"""The name of the current step. Example: "Purchasing resources."
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def BackupStatus(self):
        r"""Indicates whether there is a backup task in the instance. 1 indicates yes and 0 indicates no.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._BackupStatus

    @BackupStatus.setter
    def BackupStatus(self, BackupStatus):
        self._BackupStatus = BackupStatus

    @property
    def RequestId(self):
        r"""Request ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def BackupOpenStatus(self):
        r"""Indicates whether there is a backup task in the cluster. 1 indicates yes and 0 indicates no.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._BackupOpenStatus

    @BackupOpenStatus.setter
    def BackupOpenStatus(self, BackupOpenStatus):
        self._BackupOpenStatus = BackupOpenStatus


    def _deserialize(self, params):
        self._InstanceState = params.get("InstanceState")
        self._FlowCreateTime = params.get("FlowCreateTime")
        self._FlowName = params.get("FlowName")
        self._FlowProgress = params.get("FlowProgress")
        self._InstanceStateDesc = params.get("InstanceStateDesc")
        self._FlowMsg = params.get("FlowMsg")
        self._ProcessName = params.get("ProcessName")
        self._BackupStatus = params.get("BackupStatus")
        self._RequestId = params.get("RequestId")
        self._BackupOpenStatus = params.get("BackupOpenStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBParametersRequest(AbstractModel):
    r"""ModifyDBParameters request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: InstanceId.
        :type InstanceId: str
        :param _NodeConfigParams: Node parameter.
        :type NodeConfigParams: list of NodeConfigParams
        """
        self._InstanceId = None
        self._NodeConfigParams = None

    @property
    def InstanceId(self):
        r"""InstanceId.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NodeConfigParams(self):
        r"""Node parameter.
        :rtype: list of NodeConfigParams
        """
        return self._NodeConfigParams

    @NodeConfigParams.setter
    def NodeConfigParams(self, NodeConfigParams):
        self._NodeConfigParams = NodeConfigParams


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("NodeConfigParams") is not None:
            self._NodeConfigParams = []
            for item in params.get("NodeConfigParams"):
                obj = NodeConfigParams()
                obj._deserialize(item)
                self._NodeConfigParams.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBParametersResponse(AbstractModel):
    r"""ModifyDBParameters response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Asynchronous process ID.
        :type TaskId: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Asynchronous process ID.
        :rtype: int
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


class ModifyInstanceRequest(AbstractModel):
    r"""ModifyInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: InstanceId.
        :type InstanceId: str
        :param _InstanceName: Name of the newly modified instance.
        :type InstanceName: str
        """
        self._InstanceId = None
        self._InstanceName = None

    @property
    def InstanceId(self):
        r"""InstanceId.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""Name of the newly modified instance.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceResponse(AbstractModel):
    r"""ModifyInstance response structure.

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


class ModifyUserHbaRequest(AbstractModel):
    r"""ModifyUserHba request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: InstanceId.
        :type InstanceId: str
        :param _HbaConfigs: Hba array.
        :type HbaConfigs: list of HbaConfig
        """
        self._InstanceId = None
        self._HbaConfigs = None

    @property
    def InstanceId(self):
        r"""InstanceId.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def HbaConfigs(self):
        r"""Hba array.
        :rtype: list of HbaConfig
        """
        return self._HbaConfigs

    @HbaConfigs.setter
    def HbaConfigs(self, HbaConfigs):
        self._HbaConfigs = HbaConfigs


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("HbaConfigs") is not None:
            self._HbaConfigs = []
            for item in params.get("HbaConfigs"):
                obj = HbaConfig()
                obj._deserialize(item)
                self._HbaConfigs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserHbaResponse(AbstractModel):
    r"""ModifyUserHba response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID.

Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskId: int
        :param _ErrorMsg: Error message.

Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""Task ID.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ErrorMsg(self):
        r"""Error message.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class NodeConfigParams(AbstractModel):
    r"""Node parameter

    """

    def __init__(self):
        r"""
        :param _NodeType: Node type.
        :type NodeType: str
        :param _ConfigParams: Parameter.
        :type ConfigParams: list of ConfigParams
        """
        self._NodeType = None
        self._ConfigParams = None

    @property
    def NodeType(self):
        r"""Node type.
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def ConfigParams(self):
        r"""Parameter.
        :rtype: list of ConfigParams
        """
        return self._ConfigParams

    @ConfigParams.setter
    def ConfigParams(self, ConfigParams):
        self._ConfigParams = ConfigParams


    def _deserialize(self, params):
        self._NodeType = params.get("NodeType")
        if params.get("ConfigParams") is not None:
            self._ConfigParams = []
            for item in params.get("ConfigParams"):
                obj = ConfigParams()
                obj._deserialize(item)
                self._ConfigParams.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NormQueryItem(AbstractModel):
    r"""Slow query item information

    """

    def __init__(self):
        r"""
        :param _CallTimes: Number of calls.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CallTimes: int
        :param _SharedReadBlocks: Number of read-only shared memory blocks.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SharedReadBlocks: int
        :param _SharedWriteBlocks: Number of write-only shared memory blocks.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SharedWriteBlocks: int
        :param _DatabaseName: Database.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DatabaseName: str
        :param _NormalQuery: Statement after masking.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NormalQuery: str
        :param _MaxElapsedQuery: The statement with the longest execution time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxElapsedQuery: str
        :param _CostTime: Total consumption time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CostTime: float
        :param _ClientIp: Client IP address.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClientIp: str
        :param _UserName: Username.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserName: str
        :param _TotalCallTimesPercent: Proportion of total count.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCallTimesPercent: float
        :param _TotalCostTimePercent: Proportion of total consumption time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCostTimePercent: float
        :param _MinCostTime: Minimum consumption time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MinCostTime: float
        :param _MaxCostTime: Maximum consumption time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxCostTime: float
        :param _FirstTime: Time of the earliest item.Note: This field may return null, indicating that no valid values can be obtained.
        :type FirstTime: str
        :param _LastTime: Time of the latest item.Note: This field may return null, indicating that no valid values can be obtained.
        :type LastTime: str
        :param _ReadCostTime: Total consumption time of I/O reading.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ReadCostTime: float
        :param _WriteCostTime: Total consumption time I/O writing.
Note: This field may return null, indicating that no valid values can be obtained.
        :type WriteCostTime: float
        """
        self._CallTimes = None
        self._SharedReadBlocks = None
        self._SharedWriteBlocks = None
        self._DatabaseName = None
        self._NormalQuery = None
        self._MaxElapsedQuery = None
        self._CostTime = None
        self._ClientIp = None
        self._UserName = None
        self._TotalCallTimesPercent = None
        self._TotalCostTimePercent = None
        self._MinCostTime = None
        self._MaxCostTime = None
        self._FirstTime = None
        self._LastTime = None
        self._ReadCostTime = None
        self._WriteCostTime = None

    @property
    def CallTimes(self):
        r"""Number of calls.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CallTimes

    @CallTimes.setter
    def CallTimes(self, CallTimes):
        self._CallTimes = CallTimes

    @property
    def SharedReadBlocks(self):
        r"""Number of read-only shared memory blocks.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SharedReadBlocks

    @SharedReadBlocks.setter
    def SharedReadBlocks(self, SharedReadBlocks):
        self._SharedReadBlocks = SharedReadBlocks

    @property
    def SharedWriteBlocks(self):
        r"""Number of write-only shared memory blocks.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._SharedWriteBlocks

    @SharedWriteBlocks.setter
    def SharedWriteBlocks(self, SharedWriteBlocks):
        self._SharedWriteBlocks = SharedWriteBlocks

    @property
    def DatabaseName(self):
        r"""Database.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def NormalQuery(self):
        r"""Statement after masking.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NormalQuery

    @NormalQuery.setter
    def NormalQuery(self, NormalQuery):
        self._NormalQuery = NormalQuery

    @property
    def MaxElapsedQuery(self):
        r"""The statement with the longest execution time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MaxElapsedQuery

    @MaxElapsedQuery.setter
    def MaxElapsedQuery(self, MaxElapsedQuery):
        self._MaxElapsedQuery = MaxElapsedQuery

    @property
    def CostTime(self):
        r"""Total consumption time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime

    @property
    def ClientIp(self):
        r"""Client IP address.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def UserName(self):
        r"""Username.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def TotalCallTimesPercent(self):
        r"""Proportion of total count.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._TotalCallTimesPercent

    @TotalCallTimesPercent.setter
    def TotalCallTimesPercent(self, TotalCallTimesPercent):
        self._TotalCallTimesPercent = TotalCallTimesPercent

    @property
    def TotalCostTimePercent(self):
        r"""Proportion of total consumption time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._TotalCostTimePercent

    @TotalCostTimePercent.setter
    def TotalCostTimePercent(self, TotalCostTimePercent):
        self._TotalCostTimePercent = TotalCostTimePercent

    @property
    def MinCostTime(self):
        r"""Minimum consumption time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._MinCostTime

    @MinCostTime.setter
    def MinCostTime(self, MinCostTime):
        self._MinCostTime = MinCostTime

    @property
    def MaxCostTime(self):
        r"""Maximum consumption time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._MaxCostTime

    @MaxCostTime.setter
    def MaxCostTime(self, MaxCostTime):
        self._MaxCostTime = MaxCostTime

    @property
    def FirstTime(self):
        r"""Time of the earliest item.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FirstTime

    @FirstTime.setter
    def FirstTime(self, FirstTime):
        self._FirstTime = FirstTime

    @property
    def LastTime(self):
        r"""Time of the latest item.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LastTime

    @LastTime.setter
    def LastTime(self, LastTime):
        self._LastTime = LastTime

    @property
    def ReadCostTime(self):
        r"""Total consumption time of I/O reading.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._ReadCostTime

    @ReadCostTime.setter
    def ReadCostTime(self, ReadCostTime):
        self._ReadCostTime = ReadCostTime

    @property
    def WriteCostTime(self):
        r"""Total consumption time I/O writing.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._WriteCostTime

    @WriteCostTime.setter
    def WriteCostTime(self, WriteCostTime):
        self._WriteCostTime = WriteCostTime


    def _deserialize(self, params):
        self._CallTimes = params.get("CallTimes")
        self._SharedReadBlocks = params.get("SharedReadBlocks")
        self._SharedWriteBlocks = params.get("SharedWriteBlocks")
        self._DatabaseName = params.get("DatabaseName")
        self._NormalQuery = params.get("NormalQuery")
        self._MaxElapsedQuery = params.get("MaxElapsedQuery")
        self._CostTime = params.get("CostTime")
        self._ClientIp = params.get("ClientIp")
        self._UserName = params.get("UserName")
        self._TotalCallTimesPercent = params.get("TotalCallTimesPercent")
        self._TotalCostTimePercent = params.get("TotalCostTimePercent")
        self._MinCostTime = params.get("MinCostTime")
        self._MaxCostTime = params.get("MaxCostTime")
        self._FirstTime = params.get("FirstTime")
        self._LastTime = params.get("LastTime")
        self._ReadCostTime = params.get("ReadCostTime")
        self._WriteCostTime = params.get("WriteCostTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamDetail(AbstractModel):
    r"""ParamDetail

    """

    def __init__(self):
        r"""
        :param _ParamName: Parameter name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ParamName: str
        :param _DefaultValue: Default value.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DefaultValue: str
        :param _NeedRestart: Indicates whether the restart is required.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NeedRestart: bool
        :param _RunningValue: Current value.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RunningValue: str
        :param _ValueRange: Value range.
        :type ValueRange: :class:`tencentcloud.cdwpg.v20201230.models.ValueRange`
        :param _Unit: Unit.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Unit: str
        :param _ShortDesc: Introduction in English.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ShortDesc: str
        :param _ParameterName: Parameter name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ParameterName: str
        """
        self._ParamName = None
        self._DefaultValue = None
        self._NeedRestart = None
        self._RunningValue = None
        self._ValueRange = None
        self._Unit = None
        self._ShortDesc = None
        self._ParameterName = None

    @property
    def ParamName(self):
        r"""Parameter name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def DefaultValue(self):
        r"""Default value.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def NeedRestart(self):
        r"""Indicates whether the restart is required.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._NeedRestart

    @NeedRestart.setter
    def NeedRestart(self, NeedRestart):
        self._NeedRestart = NeedRestart

    @property
    def RunningValue(self):
        r"""Current value.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RunningValue

    @RunningValue.setter
    def RunningValue(self, RunningValue):
        self._RunningValue = RunningValue

    @property
    def ValueRange(self):
        r"""Value range.
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.ValueRange`
        """
        return self._ValueRange

    @ValueRange.setter
    def ValueRange(self, ValueRange):
        self._ValueRange = ValueRange

    @property
    def Unit(self):
        r"""Unit.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def ShortDesc(self):
        r"""Introduction in English.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ShortDesc

    @ShortDesc.setter
    def ShortDesc(self, ShortDesc):
        self._ShortDesc = ShortDesc

    @property
    def ParameterName(self):
        r"""Parameter name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ParameterName

    @ParameterName.setter
    def ParameterName(self, ParameterName):
        self._ParameterName = ParameterName


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._DefaultValue = params.get("DefaultValue")
        self._NeedRestart = params.get("NeedRestart")
        self._RunningValue = params.get("RunningValue")
        if params.get("ValueRange") is not None:
            self._ValueRange = ValueRange()
            self._ValueRange._deserialize(params.get("ValueRange"))
        self._Unit = params.get("Unit")
        self._ShortDesc = params.get("ShortDesc")
        self._ParameterName = params.get("ParameterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamItem(AbstractModel):
    r"""ParamItem information

    """

    def __init__(self):
        r"""
        :param _NodeType: Node type. Valid values: cn and dn.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NodeType: str
        :param _NodeName: Node name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NodeName: str
        :param _TotalCount: Number of parameters.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _Details: Parameter information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Details: list of ParamDetail
        """
        self._NodeType = None
        self._NodeName = None
        self._TotalCount = None
        self._Details = None

    @property
    def NodeType(self):
        r"""Node type. Valid values: cn and dn.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def NodeName(self):
        r"""Node name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def TotalCount(self):
        r"""Number of parameters.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Details(self):
        r"""Parameter information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ParamDetail
        """
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details


    def _deserialize(self, params):
        self._NodeType = params.get("NodeType")
        self._NodeName = params.get("NodeName")
        self._TotalCount = params.get("TotalCount")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = ParamDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Range(AbstractModel):
    r"""Range

    """

    def __init__(self):
        r"""
        :param _Min: Minimum value.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Min: str
        :param _Max: Maximum value.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Max: str
        """
        self._Min = None
        self._Max = None

    @property
    def Min(self):
        r"""Minimum value.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def Max(self):
        r"""Maximum value.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max


    def _deserialize(self, params):
        self._Min = params.get("Min")
        self._Max = params.get("Max")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAccountPasswordRequest(AbstractModel):
    r"""ResetAccountPassword request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instanceid.
        :type InstanceId: str
        :param _UserName: The username to be modified.
        :type UserName: str
        :param _NewPassword: New password.
        :type NewPassword: str
        """
        self._InstanceId = None
        self._UserName = None
        self._NewPassword = None

    @property
    def InstanceId(self):
        r"""Instanceid.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UserName(self):
        r"""The username to be modified.
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def NewPassword(self):
        r"""New password.
        :rtype: str
        """
        return self._NewPassword

    @NewPassword.setter
    def NewPassword(self, NewPassword):
        self._NewPassword = NewPassword


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._UserName = params.get("UserName")
        self._NewPassword = params.get("NewPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAccountPasswordResponse(AbstractModel):
    r"""ResetAccountPassword response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: Error message.

Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        r"""Error message.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ResourceInfo(AbstractModel):
    r"""Resource information.

    """

    def __init__(self):
        r"""
        :param _SpecName: Resource name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SpecName: str
        :param _Count: Resource count.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Count: int
        :param _DiskSpec: Disk information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskSpec: :class:`tencentcloud.cdwpg.v20201230.models.CBSSpecInfo`
        :param _Type: Node type. Valid values: cn and dn.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        """
        self._SpecName = None
        self._Count = None
        self._DiskSpec = None
        self._Type = None

    @property
    def SpecName(self):
        r"""Resource name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def Count(self):
        r"""Resource count.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def DiskSpec(self):
        r"""Disk information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.CBSSpecInfo`
        """
        return self._DiskSpec

    @DiskSpec.setter
    def DiskSpec(self, DiskSpec):
        self._DiskSpec = DiskSpec

    @property
    def Type(self):
        r"""Node type. Valid values: cn and dn.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._SpecName = params.get("SpecName")
        self._Count = params.get("Count")
        if params.get("DiskSpec") is not None:
            self._DiskSpec = CBSSpecInfo()
            self._DiskSpec._deserialize(params.get("DiskSpec"))
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceSpecNew(AbstractModel):
    r"""Resource specifications.

    """

    def __init__(self):
        r"""
        :param _SpecName: Resource name.
        :type SpecName: str
        :param _Count: Resource count.
        :type Count: int
        :param _DiskSpec: Disk information.
        :type DiskSpec: :class:`tencentcloud.cdwpg.v20201230.models.CBSSpec`
        :param _Type: Resource type, DATA.
        :type Type: str
        """
        self._SpecName = None
        self._Count = None
        self._DiskSpec = None
        self._Type = None

    @property
    def SpecName(self):
        r"""Resource name.
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def Count(self):
        r"""Resource count.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def DiskSpec(self):
        r"""Disk information.
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.CBSSpec`
        """
        return self._DiskSpec

    @DiskSpec.setter
    def DiskSpec(self, DiskSpec):
        self._DiskSpec = DiskSpec

    @property
    def Type(self):
        r"""Resource type, DATA.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._SpecName = params.get("SpecName")
        self._Count = params.get("Count")
        if params.get("DiskSpec") is not None:
            self._DiskSpec = CBSSpec()
            self._DiskSpec._deserialize(params.get("DiskSpec"))
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartInstanceRequest(AbstractModel):
    r"""RestartInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance name. Example: cdwpg-xxxx.
        :type InstanceId: str
        :param _NodeTypes: Types of node that need to restart. Valid values: gtm, cn, dn and fn.
        :type NodeTypes: list of str
        :param _NodeIds: Specifies th ID of nodes that need to restart.
        :type NodeIds: list of str
        """
        self._InstanceId = None
        self._NodeTypes = None
        self._NodeIds = None

    @property
    def InstanceId(self):
        r"""Instance name. Example: cdwpg-xxxx.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NodeTypes(self):
        r"""Types of node that need to restart. Valid values: gtm, cn, dn and fn.
        :rtype: list of str
        """
        return self._NodeTypes

    @NodeTypes.setter
    def NodeTypes(self, NodeTypes):
        self._NodeTypes = NodeTypes

    @property
    def NodeIds(self):
        r"""Specifies th ID of nodes that need to restart.
        :rtype: list of str
        """
        return self._NodeIds

    @NodeIds.setter
    def NodeIds(self, NodeIds):
        self._NodeIds = NodeIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NodeTypes = params.get("NodeTypes")
        self._NodeIds = params.get("NodeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartInstanceResponse(AbstractModel):
    r"""RestartInstance response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: FlowId.
        :type FlowId: int
        :param _ErrorMsg: Error message.
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""FlowId.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ErrorMsg(self):
        r"""Error message.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._FlowId = params.get("FlowId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ScaleOutInstanceRequest(AbstractModel):
    r"""ScaleOutInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: InstanceId.
        :type InstanceId: str
        :param _NodeType: Node type.
        :type NodeType: str
        :param _ScaleOutCount: Number of scale-out nodes.
        :type ScaleOutCount: int
        """
        self._InstanceId = None
        self._NodeType = None
        self._ScaleOutCount = None

    @property
    def InstanceId(self):
        r"""InstanceId.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NodeType(self):
        r"""Node type.
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def ScaleOutCount(self):
        r"""Number of scale-out nodes.
        :rtype: int
        """
        return self._ScaleOutCount

    @ScaleOutCount.setter
    def ScaleOutCount(self, ScaleOutCount):
        self._ScaleOutCount = ScaleOutCount


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._NodeType = params.get("NodeType")
        self._ScaleOutCount = params.get("ScaleOutCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleOutInstanceResponse(AbstractModel):
    r"""ScaleOutInstance response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: FlowId.
        :type FlowId: str
        :param _ErrorMsg: Error message.

Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""FlowId.
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ErrorMsg(self):
        r"""Error message.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._FlowId = params.get("FlowId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ScaleUpInstanceRequest(AbstractModel):
    r"""ScaleUpInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: InstanceId.
        :type InstanceId: str
        :param _Case: Modifies the resource type.
        :type Case: str
        :param _ModifySpec: Modified parameters.
        :type ModifySpec: :class:`tencentcloud.cdwpg.v20201230.models.CNResourceSpec`
        :param _InstanceName: Instance name.
        :type InstanceName: str
        """
        self._InstanceId = None
        self._Case = None
        self._ModifySpec = None
        self._InstanceName = None

    @property
    def InstanceId(self):
        r"""InstanceId.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Case(self):
        r"""Modifies the resource type.
        :rtype: str
        """
        return self._Case

    @Case.setter
    def Case(self, Case):
        self._Case = Case

    @property
    def ModifySpec(self):
        r"""Modified parameters.
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.CNResourceSpec`
        """
        return self._ModifySpec

    @ModifySpec.setter
    def ModifySpec(self, ModifySpec):
        self._ModifySpec = ModifySpec

    @property
    def InstanceName(self):
        r"""Instance name.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Case = params.get("Case")
        if params.get("ModifySpec") is not None:
            self._ModifySpec = CNResourceSpec()
            self._ModifySpec._deserialize(params.get("ModifySpec"))
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleUpInstanceResponse(AbstractModel):
    r"""ScaleUpInstance response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: FlowId.
        :type FlowId: int
        :param _ErrorMsg: Specific error.
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""FlowId.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ErrorMsg(self):
        r"""Specific error.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._FlowId = params.get("FlowId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class SearchTags(AbstractModel):
    r"""List of tags searched on the list page.

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key.
        :type TagKey: str
        :param _TagValue: Tag value.
        :type TagValue: str
        :param _AllValue: 1 means only the Tag key is entered without a value, and 0 means both the key and the value are entered.
        :type AllValue: int
        """
        self._TagKey = None
        self._TagValue = None
        self._AllValue = None

    @property
    def TagKey(self):
        r"""Tag key.
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""Tag value.
        :rtype: str
        """
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def AllValue(self):
        r"""1 means only the Tag key is entered without a value, and 0 means both the key and the value are entered.
        :rtype: int
        """
        return self._AllValue

    @AllValue.setter
    def AllValue(self, AllValue):
        self._AllValue = AllValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        self._AllValue = params.get("AllValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SimpleInstanceInfo(AbstractModel):
    r"""Cluster information.

    """

    def __init__(self):
        r"""
        :param _ID: ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ID: int
        :param _InstanceId: Cluster ID.

Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _InstanceName: Cluster name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param _Version: Kernel version.

Note: This field may return null, indicating that no valid values can be obtained.
        :type Version: str
        :param _Region: Region.

Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _Zone: Region.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Zone: str
        :param _UserVPCID: Virtual Private Cloud (VPC).

Note: This field may return null, indicating that no valid values can be obtained.
        :type UserVPCID: str
        :param _UserSubnetID: Subnet.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserSubnetID: str
        :param _CreateTime: Start time.

Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _ExpireTime: Expiration time.

Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param _AccessInfo: Access address.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccessInfo: str
        :param _RenewFlag: Automatic renewal switch. 0 indicates automatic renewal is not enabled, and 1 indicates automatic renewal is enabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RenewFlag: int
        :param _ChargeProperties: Billing mode.

Note: This field may return null, indicating that no valid values can be obtained.
        :type ChargeProperties: :class:`tencentcloud.cdwpg.v20201230.models.ChargeProperties`
        :param _Resources: Resource collection.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Resources: list of ResourceInfo
        :param _Tags: Tag list.

Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _Status: Cluster status.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        """
        self._ID = None
        self._InstanceId = None
        self._InstanceName = None
        self._Version = None
        self._Region = None
        self._Zone = None
        self._UserVPCID = None
        self._UserSubnetID = None
        self._CreateTime = None
        self._ExpireTime = None
        self._AccessInfo = None
        self._RenewFlag = None
        self._ChargeProperties = None
        self._Resources = None
        self._Tags = None
        self._Status = None

    @property
    def ID(self):
        r"""ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def InstanceId(self):
        r"""Cluster ID.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""Cluster name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Version(self):
        r"""Kernel version.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Region(self):
        r"""Region.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        r"""Region.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def UserVPCID(self):
        r"""Virtual Private Cloud (VPC).

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UserVPCID

    @UserVPCID.setter
    def UserVPCID(self, UserVPCID):
        self._UserVPCID = UserVPCID

    @property
    def UserSubnetID(self):
        r"""Subnet.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UserSubnetID

    @UserSubnetID.setter
    def UserSubnetID(self, UserSubnetID):
        self._UserSubnetID = UserSubnetID

    @property
    def CreateTime(self):
        r"""Start time.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        r"""Expiration time.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def AccessInfo(self):
        r"""Access address.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AccessInfo

    @AccessInfo.setter
    def AccessInfo(self, AccessInfo):
        self._AccessInfo = AccessInfo

    @property
    def RenewFlag(self):
        r"""Automatic renewal switch. 0 indicates automatic renewal is not enabled, and 1 indicates automatic renewal is enabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def ChargeProperties(self):
        r"""Billing mode.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.ChargeProperties`
        """
        return self._ChargeProperties

    @ChargeProperties.setter
    def ChargeProperties(self, ChargeProperties):
        self._ChargeProperties = ChargeProperties

    @property
    def Resources(self):
        r"""Resource collection.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ResourceInfo
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def Tags(self):
        r"""Tag list.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Status(self):
        r"""Cluster status.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Version = params.get("Version")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._UserVPCID = params.get("UserVPCID")
        self._UserSubnetID = params.get("UserSubnetID")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._AccessInfo = params.get("AccessInfo")
        self._RenewFlag = params.get("RenewFlag")
        if params.get("ChargeProperties") is not None:
            self._ChargeProperties = ChargeProperties()
            self._ChargeProperties._deserialize(params.get("ChargeProperties"))
        if params.get("Resources") is not None:
            self._Resources = []
            for item in params.get("Resources"):
                obj = ResourceInfo()
                obj._deserialize(item)
                self._Resources.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogDetail(AbstractModel):
    r"""Slow SQL logs

    """

    def __init__(self):
        r"""
        :param _TotalTime: Total consumption time.
        :type TotalTime: float
        :param _TotalCallTimes: Total number of calls.
        :type TotalCallTimes: int
        :param _NormalQuerys: Slow SQL.
        :type NormalQuerys: list of NormQueryItem
        """
        self._TotalTime = None
        self._TotalCallTimes = None
        self._NormalQuerys = None

    @property
    def TotalTime(self):
        r"""Total consumption time.
        :rtype: float
        """
        return self._TotalTime

    @TotalTime.setter
    def TotalTime(self, TotalTime):
        self._TotalTime = TotalTime

    @property
    def TotalCallTimes(self):
        r"""Total number of calls.
        :rtype: int
        """
        return self._TotalCallTimes

    @TotalCallTimes.setter
    def TotalCallTimes(self, TotalCallTimes):
        self._TotalCallTimes = TotalCallTimes

    @property
    def NormalQuerys(self):
        r"""Slow SQL.
        :rtype: list of NormQueryItem
        """
        return self._NormalQuerys

    @NormalQuerys.setter
    def NormalQuerys(self, NormalQuerys):
        self._NormalQuerys = NormalQuerys


    def _deserialize(self, params):
        self._TotalTime = params.get("TotalTime")
        self._TotalCallTimes = params.get("TotalCallTimes")
        if params.get("NormalQuerys") is not None:
            self._NormalQuerys = []
            for item in params.get("NormalQuerys"):
                obj = NormQueryItem()
                obj._deserialize(item)
                self._NormalQuerys.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    r"""Tag description.

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key.
        :type TagKey: str
        :param _TagValue: Tag value.
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""Tag key.
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""Tag value.
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
        


class UpgradeInstanceRequest(AbstractModel):
    r"""UpgradeInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: InstanceId.
        :type InstanceId: str
        :param _PackageVersion: Installation package version.
        :type PackageVersion: str
        """
        self._InstanceId = None
        self._PackageVersion = None

    @property
    def InstanceId(self):
        r"""InstanceId.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PackageVersion(self):
        r"""Installation package version.
        :rtype: str
        """
        return self._PackageVersion

    @PackageVersion.setter
    def PackageVersion(self, PackageVersion):
        self._PackageVersion = PackageVersion


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PackageVersion = params.get("PackageVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceResponse(AbstractModel):
    r"""UpgradeInstance response structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: FlowId.
        :type FlowId: int
        :param _ErrorMsg: Error message.
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FlowId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        r"""FlowId.
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ErrorMsg(self):
        r"""Error message.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._FlowId = params.get("FlowId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class UpgradeItem(AbstractModel):
    r"""Upgrade information

    """

    def __init__(self):
        r"""
        :param _TaskName: Task name.

Note: This field may return null, indicating that no valid values can be obtained.
        :type TaskName: str
        :param _SourceVersion: Original kernel version.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SourceVersion: str
        :param _TargetVersion: Target kernel version.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetVersion: str
        :param _CreateTime: Task creation time.

Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _EndTime: Task end time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        :param _Status: Task completion status.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _OperateUin: Operator.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OperateUin: str
        """
        self._TaskName = None
        self._SourceVersion = None
        self._TargetVersion = None
        self._CreateTime = None
        self._EndTime = None
        self._Status = None
        self._OperateUin = None

    @property
    def TaskName(self):
        r"""Task name.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def SourceVersion(self):
        r"""Original kernel version.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SourceVersion

    @SourceVersion.setter
    def SourceVersion(self, SourceVersion):
        self._SourceVersion = SourceVersion

    @property
    def TargetVersion(self):
        r"""Target kernel version.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TargetVersion

    @TargetVersion.setter
    def TargetVersion(self, TargetVersion):
        self._TargetVersion = TargetVersion

    @property
    def CreateTime(self):
        r"""Task creation time.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EndTime(self):
        r"""Task end time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        r"""Task completion status.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OperateUin(self):
        r"""Operator.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OperateUin

    @OperateUin.setter
    def OperateUin(self, OperateUin):
        self._OperateUin = OperateUin


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._SourceVersion = params.get("SourceVersion")
        self._TargetVersion = params.get("TargetVersion")
        self._CreateTime = params.get("CreateTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._OperateUin = params.get("OperateUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ValueRange(AbstractModel):
    r"""ValueRange

    """

    def __init__(self):
        r"""
        :param _Type: Parameter types. Valid values: enum, string, and section. Enum indicates enumeration, namely utf8, latin1, gbk. String indicates that the returned parameter value is a string. Section indicates that the returned parameter value is a value range, for example, 4-8.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param _Range: Response parameter when the type is a section.Note: This field may return null, indicating that no valid values can be obtained.
        :type Range: :class:`tencentcloud.cdwpg.v20201230.models.Range`
        :param _Enum: Response parameter when the type is an enum.Note: This field may return null, indicating that no valid values can be obtained.
        :type Enum: list of str
        :param _String: Response parameter when the type is a string.Note: This field may return null, indicating that no valid values can be obtained.
        :type String: str
        """
        self._Type = None
        self._Range = None
        self._Enum = None
        self._String = None

    @property
    def Type(self):
        r"""Parameter types. Valid values: enum, string, and section. Enum indicates enumeration, namely utf8, latin1, gbk. String indicates that the returned parameter value is a string. Section indicates that the returned parameter value is a value range, for example, 4-8.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Range(self):
        r"""Response parameter when the type is a section.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.Range`
        """
        return self._Range

    @Range.setter
    def Range(self, Range):
        self._Range = Range

    @property
    def Enum(self):
        r"""Response parameter when the type is an enum.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Enum

    @Enum.setter
    def Enum(self, Enum):
        self._Enum = Enum

    @property
    def String(self):
        r"""Response parameter when the type is a string.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._String

    @String.setter
    def String(self, String):
        self._String = String


    def _deserialize(self, params):
        self._Type = params.get("Type")
        if params.get("Range") is not None:
            self._Range = Range()
            self._Range._deserialize(params.get("Range"))
        self._Enum = params.get("Enum")
        self._String = params.get("String")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        