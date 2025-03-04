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


class AccessInfo(AbstractModel):
    """Access information.

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
        """Address.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

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
        


class CBSSpec(AbstractModel):
    """Disk specifications.

    """

    def __init__(self):
        r"""
        :param _DiskType: Disk type.
        :type DiskType: str
        :param _DiskSize: Size.
        :type DiskSize: int
        :param _DiskCount: Number.
        :type DiskCount: int
        """
        self._DiskType = None
        self._DiskSize = None
        self._DiskCount = None

    @property
    def DiskType(self):
        """Disk type.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        """Size.
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskCount(self):
        """Number.
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
    """Disk information.

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
        """Disk type.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        """Size.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskCount(self):
        """Number.Note: This field may return null, indicating that no valid values can be obtained.
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
        


class ChargeProperties(AbstractModel):
    """Billing time parameter.

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
        """1: requires auto-renewal.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def TimeSpan(self):
        """Order time range.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        """Time unit. Valid values: h and m.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def PayMode(self):
        """Billing type: 0 indicates pay-as-you-go and 1 indicates monthly subscription.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ChargeType(self):
        """PREPAID and POSTPAID_BY_HOUR
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
        


class CreateInstanceByApiRequest(AbstractModel):
    """CreateInstanceByApi request structure.

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
        :param _Tags: Tag list.
        :type Tags: :class:`tencentcloud.cdwpg.v20201230.models.Tag`
        :param _ProductVersion: Version.
        :type ProductVersion: str
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

    @property
    def InstanceName(self):
        """Instance name.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Zone(self):
        """Availability zone.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def UserVPCId(self):
        """Virtual Private Cloud (VPC).
        :rtype: str
        """
        return self._UserVPCId

    @UserVPCId.setter
    def UserVPCId(self, UserVPCId):
        self._UserVPCId = UserVPCId

    @property
    def UserSubnetId(self):
        """Subnet.
        :rtype: str
        """
        return self._UserSubnetId

    @UserSubnetId.setter
    def UserSubnetId(self, UserSubnetId):
        self._UserSubnetId = UserSubnetId

    @property
    def ChargeProperties(self):
        """Billing method.
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.ChargeProperties`
        """
        return self._ChargeProperties

    @ChargeProperties.setter
    def ChargeProperties(self, ChargeProperties):
        self._ChargeProperties = ChargeProperties

    @property
    def AdminPassword(self):
        """Instance password.
        :rtype: str
        """
        return self._AdminPassword

    @AdminPassword.setter
    def AdminPassword(self, AdminPassword):
        self._AdminPassword = AdminPassword

    @property
    def Resources(self):
        """Resource information.
        :rtype: list of ResourceSpecNew
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def Tags(self):
        """Tag list.
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.Tag`
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ProductVersion(self):
        """Version.
        :rtype: str
        """
        return self._ProductVersion

    @ProductVersion.setter
    def ProductVersion(self, ProductVersion):
        self._ProductVersion = ProductVersion


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceByApiResponse(AbstractModel):
    """CreateInstanceByApi response structure.

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
        """Process ID.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceId(self):
        """Instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ErrorMsg(self):
        """Error message.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._FlowId = params.get("FlowId")
        self._InstanceId = params.get("InstanceId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DescribeInstanceInfoRequest(AbstractModel):
    """DescribeInstanceInfo request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: instance ID.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """instance ID.
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
    """DescribeInstanceInfo response structure.

    """

    def __init__(self):
        r"""
        :param _SimpleInstanceInfo: Instance simple information
        :type SimpleInstanceInfo: :class:`tencentcloud.cdwpg.v20201230.models.SimpleInstanceInfo`
        :param _ErrorMsg: Error Message
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SimpleInstanceInfo = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def SimpleInstanceInfo(self):
        """Instance simple information
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.SimpleInstanceInfo`
        """
        return self._SimpleInstanceInfo

    @SimpleInstanceInfo.setter
    def SimpleInstanceInfo(self, SimpleInstanceInfo):
        self._SimpleInstanceInfo = SimpleInstanceInfo

    @property
    def ErrorMsg(self):
        """Error Message
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        if params.get("SimpleInstanceInfo") is not None:
            self._SimpleInstanceInfo = SimpleInstanceInfo()
            self._SimpleInstanceInfo._deserialize(params.get("SimpleInstanceInfo"))
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DescribeInstanceRequest(AbstractModel):
    """DescribeInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: instance ID.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """instance ID.
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
    """DescribeInstance response structure.

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
        """Instance description information.
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.InstanceInfo`
        """
        return self._InstanceInfo

    @InstanceInfo.setter
    def InstanceInfo(self, InstanceInfo):
        self._InstanceInfo = InstanceInfo

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
        if params.get("InstanceInfo") is not None:
            self._InstanceInfo = InstanceInfo()
            self._InstanceInfo._deserialize(params.get("InstanceInfo"))
        self._RequestId = params.get("RequestId")


class DescribeInstanceStateRequest(AbstractModel):
    """DescribeInstanceState request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId:  Instance id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """ Instance id
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
    """DescribeInstanceState response structure.

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
        :param _InstanceStateDesc: Cluster status description. Example: running.Note: This field may return null, indicating that no valid values can be obtained.
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
        """Instance status. Example: serving.
        :rtype: str
        """
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def FlowCreateTime(self):
        """Creation time of instance operation.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FlowCreateTime

    @FlowCreateTime.setter
    def FlowCreateTime(self, FlowCreateTime):
        self._FlowCreateTime = FlowCreateTime

    @property
    def FlowName(self):
        """Instance operation name.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def FlowProgress(self):
        """Instance operation progress.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._FlowProgress

    @FlowProgress.setter
    def FlowProgress(self, FlowProgress):
        self._FlowProgress = FlowProgress

    @property
    def InstanceStateDesc(self):
        """Cluster status description. Example: running.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceStateDesc

    @InstanceStateDesc.setter
    def InstanceStateDesc(self, InstanceStateDesc):
        self._InstanceStateDesc = InstanceStateDesc

    @property
    def FlowMsg(self):
        """Instance process error messages. Example: "Creation failed, insufficient resources."
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FlowMsg

    @FlowMsg.setter
    def FlowMsg(self, FlowMsg):
        self._FlowMsg = FlowMsg

    @property
    def ProcessName(self):
        """The name of the current step. Example: "Purchasing resources."Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def BackupStatus(self):
        """Enabling status of the instance backup task.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._BackupStatus

    @BackupStatus.setter
    def BackupStatus(self, BackupStatus):
        self._BackupStatus = BackupStatus

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
    """DescribeInstances request structure.

    """

    def __init__(self):
        r"""
        :param _SearchInstanceId: The name of the Instance ID for the search.
        :type SearchInstanceId: str
        :param _SearchInstanceName: The instance name for the search.
        :type SearchInstanceName: str
        :param _Offset: Pagination parameter. The first page is 0, and the second page is 10.
        :type Offset: int
        :param _Limit: Pagination parameter. Pagination step length. It is 10 by default.
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
        """The name of the Instance ID for the search.
        :rtype: str
        """
        return self._SearchInstanceId

    @SearchInstanceId.setter
    def SearchInstanceId(self, SearchInstanceId):
        self._SearchInstanceId = SearchInstanceId

    @property
    def SearchInstanceName(self):
        """The instance name for the search.
        :rtype: str
        """
        return self._SearchInstanceName

    @SearchInstanceName.setter
    def SearchInstanceName(self, SearchInstanceName):
        self._SearchInstanceName = SearchInstanceName

    @property
    def Offset(self):
        """Pagination parameter. The first page is 0, and the second page is 10.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Pagination parameter. Pagination step length. It is 10 by default.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchTags(self):
        """Searched tag list.
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
    """DescribeInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of instances.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _InstancesList: Instance array.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstancesList: list of InstanceInfo
        :param _ErrorMsg:  -Note: This field may return null, indicating that no valid values can be obtained.
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
        """Total number of instances.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstancesList(self):
        """Instance array.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of InstanceInfo
        """
        return self._InstancesList

    @InstancesList.setter
    def InstancesList(self, InstancesList):
        self._InstancesList = InstancesList

    @property
    def ErrorMsg(self):
        """ -Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
    """DescribeSimpleInstances request structure.

    """

    def __init__(self):
        r"""
        :param _SearchInstanceId: Search Instance Id
        :type SearchInstanceId: str
        :param _SearchInstanceName: Search Instance Name
        :type SearchInstanceName: str
        :param _Offset: 	
Offset
        :type Offset: int
        :param _Limit: Limit
        :type Limit: int
        :param _SearchTags: Search Tags
        :type SearchTags: list of str
        """
        self._SearchInstanceId = None
        self._SearchInstanceName = None
        self._Offset = None
        self._Limit = None
        self._SearchTags = None

    @property
    def SearchInstanceId(self):
        """Search Instance Id
        :rtype: str
        """
        return self._SearchInstanceId

    @SearchInstanceId.setter
    def SearchInstanceId(self, SearchInstanceId):
        self._SearchInstanceId = SearchInstanceId

    @property
    def SearchInstanceName(self):
        """Search Instance Name
        :rtype: str
        """
        return self._SearchInstanceName

    @SearchInstanceName.setter
    def SearchInstanceName(self, SearchInstanceName):
        self._SearchInstanceName = SearchInstanceName

    @property
    def Offset(self):
        """	
Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

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
    def SearchTags(self):
        """Search Tags
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
    """DescribeSimpleInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total Count
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _InstancesList: Instances List
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstancesList: list of InstanceSimpleInfoNew
        :param _ErrorMsg:  Error Message
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
        """Total Count
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstancesList(self):
        """Instances List
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of InstanceSimpleInfoNew
        """
        return self._InstancesList

    @InstancesList.setter
    def InstancesList(self, InstancesList):
        self._InstancesList = InstancesList

    @property
    def ErrorMsg(self):
        """ Error Message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._TotalCount = params.get("TotalCount")
        if params.get("InstancesList") is not None:
            self._InstancesList = []
            for item in params.get("InstancesList"):
                obj = InstanceSimpleInfoNew()
                obj._deserialize(item)
                self._InstancesList.append(obj)
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DestroyInstanceByApiRequest(AbstractModel):
    """DestroyInstanceByApi request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance id. Example: "cdwpg-xxxx".
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """Instance id. Example: "cdwpg-xxxx".
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
    """DestroyInstanceByApi response structure.

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
        """Destroy  process ID.
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ErrorMsg(self):
        """Error message.
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._FlowId = params.get("FlowId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DiskSpecPlus(AbstractModel):
    """Disk specifications.

    """

    def __init__(self):
        r"""
        :param _DiskCount: Disk Count
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskCount: int
        :param _MaxDiskSize: Max Disk Size
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxDiskSize: int
        :param _MinDiskSize: Min Disk Size
Note: This field may return null, indicating that no valid values can be obtained.
        :type MinDiskSize: int
        :param _DiskType: Disk Type
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskType: str
        :param _DiskDesc: Disk Description
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskDesc: str
        :param _CvmClass: Cvm Class
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
        """Disk Count
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount

    @property
    def MaxDiskSize(self):
        """Max Disk Size
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MaxDiskSize

    @MaxDiskSize.setter
    def MaxDiskSize(self, MaxDiskSize):
        self._MaxDiskSize = MaxDiskSize

    @property
    def MinDiskSize(self):
        """Min Disk Size
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MinDiskSize

    @MinDiskSize.setter
    def MinDiskSize(self, MinDiskSize):
        self._MinDiskSize = MinDiskSize

    @property
    def DiskType(self):
        """Disk Type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskDesc(self):
        """Disk Description
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DiskDesc

    @DiskDesc.setter
    def DiskDesc(self, DiskDesc):
        self._DiskDesc = DiskDesc

    @property
    def CvmClass(self):
        """Cvm Class
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
        


class InstanceInfo(AbstractModel):
    """instance information.

    """

    def __init__(self):
        r"""
        :param _ID: Instance ID 
Note: This field may return null, indicating that no valid values can be obtained.
        :type ID: int
        :param _InstanceType: cn/dn or others.Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceType: str
        :param _InstanceName: Instance Name
.Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param _Status: Instance Status ,such as  2
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _StatusDesc: Instance Status  Description ,such as Running.
Note: This field may return null, indicating that no valid values can be obtained.
        :type StatusDesc: str
        :param _InstanceStateInfo: Instance State Infomation
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceStateInfo: :class:`tencentcloud.cdwpg.v20201230.models.InstanceStateInfo`
        :param _InstanceID: Instance ID 
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceID: str
        :param _CreateTime: CreateTime ,such as 2022-09-05 20:00:01
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _Region: Region ,such as ap-chongqing.Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _Zone: Zone : This field may return null, indicating that no valid values can be obtained.
        :type Zone: str
        :param _RegionDesc: Region.Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionDesc: str
        :param _ZoneDesc: Zone.Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneDesc: str
        :param _Tags: Tag.Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _Version: Version.Note: This field may return null, indicating that no valid values can be obtained.
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
        :param _RegionId:  Region Id
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionId: int
        :param _ZoneId: Zone Id
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneId: int
        :param _VpcId: Vpc Id
Note: This field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param _SubnetId: Subnet Id
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param _ExpireTime: Expire Time
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param _PayMode: Pay Mode
Note: This field may return null, indicating that no valid values can be obtained.
        :type PayMode: str
        :param _RenewFlag: Renew Flag
Note: This field may return null, indicating that no valid values can be obtained.
        :type RenewFlag: bool
        :param _InstanceId: Instance Id
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
        """Instance ID 
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def InstanceType(self):
        """cn/dn or others.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceName(self):
        """Instance Name
.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Status(self):
        """Instance Status ,such as  2
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        """Instance Status  Description ,such as Running.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def InstanceStateInfo(self):
        """Instance State Infomation
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.InstanceStateInfo`
        """
        return self._InstanceStateInfo

    @InstanceStateInfo.setter
    def InstanceStateInfo(self, InstanceStateInfo):
        self._InstanceStateInfo = InstanceStateInfo

    @property
    def InstanceID(self):
        """Instance ID 
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def CreateTime(self):
        """CreateTime ,such as 2022-09-05 20:00:01
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Region(self):
        """Region ,such as ap-chongqing.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        """Zone : This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def RegionDesc(self):
        """Region.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RegionDesc

    @RegionDesc.setter
    def RegionDesc(self, RegionDesc):
        self._RegionDesc = RegionDesc

    @property
    def ZoneDesc(self):
        """Zone.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ZoneDesc

    @ZoneDesc.setter
    def ZoneDesc(self, ZoneDesc):
        self._ZoneDesc = ZoneDesc

    @property
    def Tags(self):
        """Tag.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Version(self):
        """Version.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Charset(self):
        """Character set.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def CNNodes(self):
        """CN node list.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of InstanceNodeGroup
        """
        return self._CNNodes

    @CNNodes.setter
    def CNNodes(self, CNNodes):
        self._CNNodes = CNNodes

    @property
    def DNNodes(self):
        """DN node list.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of InstanceNodeGroup
        """
        return self._DNNodes

    @DNNodes.setter
    def DNNodes(self, DNNodes):
        self._DNNodes = DNNodes

    @property
    def RegionId(self):
        """ Region Id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        """Zone Id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcId(self):
        """Vpc Id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Subnet Id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ExpireTime(self):
        """Expire Time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def PayMode(self):
        """Pay Mode
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def RenewFlag(self):
        """Renew Flag
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def InstanceId(self):
        """Instance Id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AccessDetails(self):
        """Access information.
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
        


class InstanceNodeGroup(AbstractModel):
    """Instance node information.

    """

    def __init__(self):
        r"""
        :param _SpecName: Spec Name
Note: This field may return null, indicating that no valid values can be obtained.
        :type SpecName: str
        :param _DataDisk: Data Disk
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataDisk: :class:`tencentcloud.cdwpg.v20201230.models.DiskSpecPlus`
        :param _CvmCount: Cvm Count
Note: This field may return null, indicating that no valid values can be obtained.
        :type CvmCount: int
        """
        self._SpecName = None
        self._DataDisk = None
        self._CvmCount = None

    @property
    def SpecName(self):
        """Spec Name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def DataDisk(self):
        """Data Disk
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.DiskSpecPlus`
        """
        return self._DataDisk

    @DataDisk.setter
    def DataDisk(self, DataDisk):
        self._DataDisk = DataDisk

    @property
    def CvmCount(self):
        """Cvm Count
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
        


class InstanceSimpleInfoNew(AbstractModel):
    """Simplified instance information.

    """

    def __init__(self):
        r"""
        :param _ID: ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ID: int
        :param _InstanceId: Instance Id
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _InstanceName: Instance Name
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param _Version: Version
Note: This field may return null, indicating that no valid values can be obtained.
        :type Version: str
        :param _Region: Region
Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _RegionId: Region Id
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionId: int
        :param _RegionDesc: Region Desc
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionDesc: str
        :param _Zone: Zone
Note: This field may return null, indicating that no valid values can be obtained.
        :type Zone: str
        :param _ZoneId: Zone Id
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneId: int
        :param _ZoneDesc: Zone Desc
Note: This field may return null, indicating that no valid values can be obtained.
        :type ZoneDesc: str
        :param _VpcId: Vpc Id
Note: This field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param _SubnetId: Subnet Id
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param _CreateTime: CreateTime
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _ExpireTime: ExpireTime
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param _AccessInfo: Access Infomation
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccessInfo: str
        :param _PayMode: Pay Mode
Note: This field may return null, indicating that no valid values can be obtained.
        :type PayMode: str
        :param _RenewFlag: Renew Flag
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
        """ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def InstanceId(self):
        """Instance Id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """Instance Name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Version(self):
        """Version
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Region(self):
        """Region
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionId(self):
        """Region Id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionDesc(self):
        """Region Desc
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RegionDesc

    @RegionDesc.setter
    def RegionDesc(self, RegionDesc):
        self._RegionDesc = RegionDesc

    @property
    def Zone(self):
        """Zone
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneId(self):
        """Zone Id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneDesc(self):
        """Zone Desc
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ZoneDesc

    @ZoneDesc.setter
    def ZoneDesc(self, ZoneDesc):
        self._ZoneDesc = ZoneDesc

    @property
    def VpcId(self):
        """Vpc Id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Subnet Id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def CreateTime(self):
        """CreateTime
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        """ExpireTime
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def AccessInfo(self):
        """Access Infomation
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AccessInfo

    @AccessInfo.setter
    def AccessInfo(self, AccessInfo):
        self._AccessInfo = AccessInfo

    @property
    def PayMode(self):
        """Pay Mode
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def RenewFlag(self):
        """Renew Flag
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
    """Instance State Information

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
        :param _RequestId: Request Id
Note: This field may return null, indicating that no valid values can be obtained.
        :type RequestId: str
        :param _BackupOpenStatus: Backup Open Status
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
        """Instance status. Example: serving.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def FlowCreateTime(self):
        """Creation time of instance operation.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FlowCreateTime

    @FlowCreateTime.setter
    def FlowCreateTime(self, FlowCreateTime):
        self._FlowCreateTime = FlowCreateTime

    @property
    def FlowName(self):
        """Instance operation name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def FlowProgress(self):
        """Instance operation progress.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._FlowProgress

    @FlowProgress.setter
    def FlowProgress(self, FlowProgress):
        self._FlowProgress = FlowProgress

    @property
    def InstanceStateDesc(self):
        """Instance status description. Example: running.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceStateDesc

    @InstanceStateDesc.setter
    def InstanceStateDesc(self, InstanceStateDesc):
        self._InstanceStateDesc = InstanceStateDesc

    @property
    def FlowMsg(self):
        """Instance process error messages. Example: "Creation failed, insufficient resources."
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FlowMsg

    @FlowMsg.setter
    def FlowMsg(self, FlowMsg):
        self._FlowMsg = FlowMsg

    @property
    def ProcessName(self):
        """The name of the current step. Example: "Purchasing resources."
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def BackupStatus(self):
        """Indicates whether there is a backup task in the instance. 1 indicates yes and 0 indicates no.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._BackupStatus

    @BackupStatus.setter
    def BackupStatus(self, BackupStatus):
        self._BackupStatus = BackupStatus

    @property
    def RequestId(self):
        """Request Id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def BackupOpenStatus(self):
        """Backup Open Status
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
        


class ModifyInstanceRequest(AbstractModel):
    """ModifyInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _InstanceName: Name of the newly modified instance.
        :type InstanceName: str
        """
        self._InstanceId = None
        self._InstanceName = None

    @property
    def InstanceId(self):
        """Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """Name of the newly modified instance.
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
    """ModifyInstance response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ResourceInfo(AbstractModel):
    """Resource information.

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
        :param _Type: Resource type.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        """
        self._SpecName = None
        self._Count = None
        self._DiskSpec = None
        self._Type = None

    @property
    def SpecName(self):
        """Resource name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def Count(self):
        """Resource count.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def DiskSpec(self):
        """Disk information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.CBSSpecInfo`
        """
        return self._DiskSpec

    @DiskSpec.setter
    def DiskSpec(self, DiskSpec):
        self._DiskSpec = DiskSpec

    @property
    def Type(self):
        """Resource type.
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
    """Resource specifications.

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
        """Resource name.
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def Count(self):
        """Resource count.
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def DiskSpec(self):
        """Disk information.
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.CBSSpec`
        """
        return self._DiskSpec

    @DiskSpec.setter
    def DiskSpec(self, DiskSpec):
        self._DiskSpec = DiskSpec

    @property
    def Type(self):
        """Resource type, DATA.
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
        


class SearchTags(AbstractModel):
    """List of tags searched on the list page.

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
        """Tag key.
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """Tag value.
        :rtype: str
        """
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def AllValue(self):
        """1 means only the Tag key is entered without a value, and 0 means both the key and the value are entered.
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
    """Cluster information.

    """

    def __init__(self):
        r"""
        :param _ID: ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ID: int
        :param _InstanceId: Instance Id
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _InstanceName: Instance Name
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param _Version: Version
Note: This field may return null, indicating that no valid values can be obtained.
        :type Version: str
        :param _Region: Region
Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _Zone: Zone
Note: This field may return null, indicating that no valid values can be obtained.
        :type Zone: str
        :param _UserVPCID: User VPC ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserVPCID: str
        :param _UserSubnetID: User Subnet ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserSubnetID: str
        :param _CreateTime: CreateTime
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _ExpireTime: ExpireTime
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param _AccessInfo: Access Infomation
Note: This field may return null, indicating that no valid values can be obtained.
        :type AccessInfo: str
        :param _RenewFlag: Renew Flag
Note: This field may return null, indicating that no valid values can be obtained.
        :type RenewFlag: int
        :param _ChargeProperties: Charge Properties
Note: This field may return null, indicating that no valid values can be obtained.
        :type ChargeProperties: :class:`tencentcloud.cdwpg.v20201230.models.ChargeProperties`
        :param _Resources: Resources
Note: This field may return null, indicating that no valid values can be obtained.
        :type Resources: list of ResourceInfo
        :param _Tags: Tags
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _Status: Status
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
        """ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def InstanceId(self):
        """Instance Id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """Instance Name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Version(self):
        """Version
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Region(self):
        """Region
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        """Zone
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def UserVPCID(self):
        """User VPC ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UserVPCID

    @UserVPCID.setter
    def UserVPCID(self, UserVPCID):
        self._UserVPCID = UserVPCID

    @property
    def UserSubnetID(self):
        """User Subnet ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UserSubnetID

    @UserSubnetID.setter
    def UserSubnetID(self, UserSubnetID):
        self._UserSubnetID = UserSubnetID

    @property
    def CreateTime(self):
        """CreateTime
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        """ExpireTime
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def AccessInfo(self):
        """Access Infomation
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AccessInfo

    @AccessInfo.setter
    def AccessInfo(self, AccessInfo):
        self._AccessInfo = AccessInfo

    @property
    def RenewFlag(self):
        """Renew Flag
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def ChargeProperties(self):
        """Charge Properties
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.ChargeProperties`
        """
        return self._ChargeProperties

    @ChargeProperties.setter
    def ChargeProperties(self, ChargeProperties):
        self._ChargeProperties = ChargeProperties

    @property
    def Resources(self):
        """Resources
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ResourceInfo
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def Tags(self):
        """Tags
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Status(self):
        """Status
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
        


class Tag(AbstractModel):
    """Tag description.

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
        """Tag key.
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """Tag value.
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
        