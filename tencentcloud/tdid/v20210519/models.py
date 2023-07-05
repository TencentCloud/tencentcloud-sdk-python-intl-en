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


class AddLabelRequest(AbstractModel):
    """AddLabel request structure.

    """

    def __init__(self):
        r"""
        :param _LabelId: The label ID.
        :type LabelId: int
        :param _Did: 
        :type Did: str
        """
        self._LabelId = None
        self._Did = None

    @property
    def LabelId(self):
        return self._LabelId

    @LabelId.setter
    def LabelId(self, LabelId):
        self._LabelId = LabelId

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did


    def _deserialize(self, params):
        self._LabelId = params.get("LabelId")
        self._Did = params.get("Did")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddLabelResponse(AbstractModel):
    """AddLabel response structure.

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


class Authority(AbstractModel):
    """The information of an authority.

    """

    def __init__(self):
        r"""
        :param _Id: The authority ID.
        :type Id: int
        :param _DidId: The DID.
        :type DidId: int
        :param _Did: The details of the DID.
        :type Did: str
        :param _Name: The authority name.
        :type Name: str
        :param _Status: Whether the authority is certified. `1`: Yes; `2`: No.
        :type Status: int
        :param _DidServiceId: The DID service ID.
        :type DidServiceId: int
        :param _ContractAppId: The application ID.
        :type ContractAppId: int
        :param _Remark: Remarks
        :type Remark: str
        :param _RegisterTime: The registration time.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RegisterTime: str
        :param _RecognizeTime: The recognition time.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RecognizeTime: str
        :param _CreateTime: The creation time.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _UpdateTime: The last updated time.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param _ClusterId: The network ID.
        :type ClusterId: str
        :param _GroupId: The group ID.
        :type GroupId: int
        :param _AppName: The application name.
        :type AppName: str
        :param _LabelName: The on-chain label.
        :type LabelName: str
        """
        self._Id = None
        self._DidId = None
        self._Did = None
        self._Name = None
        self._Status = None
        self._DidServiceId = None
        self._ContractAppId = None
        self._Remark = None
        self._RegisterTime = None
        self._RecognizeTime = None
        self._CreateTime = None
        self._UpdateTime = None
        self._ClusterId = None
        self._GroupId = None
        self._AppName = None
        self._LabelName = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DidId(self):
        return self._DidId

    @DidId.setter
    def DidId(self, DidId):
        self._DidId = DidId

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did

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
    def DidServiceId(self):
        return self._DidServiceId

    @DidServiceId.setter
    def DidServiceId(self, DidServiceId):
        self._DidServiceId = DidServiceId

    @property
    def ContractAppId(self):
        return self._ContractAppId

    @ContractAppId.setter
    def ContractAppId(self, ContractAppId):
        self._ContractAppId = ContractAppId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def RegisterTime(self):
        return self._RegisterTime

    @RegisterTime.setter
    def RegisterTime(self, RegisterTime):
        self._RegisterTime = RegisterTime

    @property
    def RecognizeTime(self):
        return self._RecognizeTime

    @RecognizeTime.setter
    def RecognizeTime(self, RecognizeTime):
        self._RecognizeTime = RecognizeTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def LabelName(self):
        return self._LabelName

    @LabelName.setter
    def LabelName(self, LabelName):
        self._LabelName = LabelName


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._DidId = params.get("DidId")
        self._Did = params.get("Did")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._DidServiceId = params.get("DidServiceId")
        self._ContractAppId = params.get("ContractAppId")
        self._Remark = params.get("Remark")
        self._RegisterTime = params.get("RegisterTime")
        self._RecognizeTime = params.get("RecognizeTime")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._ClusterId = params.get("ClusterId")
        self._GroupId = params.get("GroupId")
        self._AppName = params.get("AppName")
        self._LabelName = params.get("LabelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BcosClusterItem(AbstractModel):
    """The information of a BCOS network.

    """

    def __init__(self):
        r"""
        :param _ChainId: The network ID.
        :type ChainId: int
        :param _ChainName: The network name.
        :type ChainName: str
        :param _AgencyCount: The number of organizations.
        :type AgencyCount: int
        :param _ConsortiumId: The consortium ID.
        :type ConsortiumId: int
        :param _CreateTime: The creation time.
        :type CreateTime: str
        :param _ExpireTime: The expiration time.
        :type ExpireTime: str
        :param _ChainStatus: The network status.
        :type ChainStatus: int
        :param _ResourceId: The resource ID.
        :type ResourceId: str
        :param _ClusterId: The cluster ID.
        :type ClusterId: str
        :param _ConsortiumName: The consortium name.
        :type ConsortiumName: str
        :param _AgencyId: The organization ID.
        :type AgencyId: int
        :param _AutoRenewFlag: The renewal status.
        :type AutoRenewFlag: int
        :param _TotalNetworkNode: The network mode.
        :type TotalNetworkNode: int
        :param _TotalCreateNode: The number of nodes created.
        :type TotalCreateNode: int
        :param _TotalGroups: The total number of groups.
        :type TotalGroups: int
        """
        self._ChainId = None
        self._ChainName = None
        self._AgencyCount = None
        self._ConsortiumId = None
        self._CreateTime = None
        self._ExpireTime = None
        self._ChainStatus = None
        self._ResourceId = None
        self._ClusterId = None
        self._ConsortiumName = None
        self._AgencyId = None
        self._AutoRenewFlag = None
        self._TotalNetworkNode = None
        self._TotalCreateNode = None
        self._TotalGroups = None

    @property
    def ChainId(self):
        return self._ChainId

    @ChainId.setter
    def ChainId(self, ChainId):
        self._ChainId = ChainId

    @property
    def ChainName(self):
        return self._ChainName

    @ChainName.setter
    def ChainName(self, ChainName):
        self._ChainName = ChainName

    @property
    def AgencyCount(self):
        return self._AgencyCount

    @AgencyCount.setter
    def AgencyCount(self, AgencyCount):
        self._AgencyCount = AgencyCount

    @property
    def ConsortiumId(self):
        return self._ConsortiumId

    @ConsortiumId.setter
    def ConsortiumId(self, ConsortiumId):
        self._ConsortiumId = ConsortiumId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ChainStatus(self):
        return self._ChainStatus

    @ChainStatus.setter
    def ChainStatus(self, ChainStatus):
        self._ChainStatus = ChainStatus

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ConsortiumName(self):
        return self._ConsortiumName

    @ConsortiumName.setter
    def ConsortiumName(self, ConsortiumName):
        self._ConsortiumName = ConsortiumName

    @property
    def AgencyId(self):
        return self._AgencyId

    @AgencyId.setter
    def AgencyId(self, AgencyId):
        self._AgencyId = AgencyId

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def TotalNetworkNode(self):
        return self._TotalNetworkNode

    @TotalNetworkNode.setter
    def TotalNetworkNode(self, TotalNetworkNode):
        self._TotalNetworkNode = TotalNetworkNode

    @property
    def TotalCreateNode(self):
        return self._TotalCreateNode

    @TotalCreateNode.setter
    def TotalCreateNode(self, TotalCreateNode):
        self._TotalCreateNode = TotalCreateNode

    @property
    def TotalGroups(self):
        return self._TotalGroups

    @TotalGroups.setter
    def TotalGroups(self, TotalGroups):
        self._TotalGroups = TotalGroups


    def _deserialize(self, params):
        self._ChainId = params.get("ChainId")
        self._ChainName = params.get("ChainName")
        self._AgencyCount = params.get("AgencyCount")
        self._ConsortiumId = params.get("ConsortiumId")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._ChainStatus = params.get("ChainStatus")
        self._ResourceId = params.get("ResourceId")
        self._ClusterId = params.get("ClusterId")
        self._ConsortiumName = params.get("ConsortiumName")
        self._AgencyId = params.get("AgencyId")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._TotalNetworkNode = params.get("TotalNetworkNode")
        self._TotalCreateNode = params.get("TotalCreateNode")
        self._TotalGroups = params.get("TotalGroups")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelAuthorityIssuerRequest(AbstractModel):
    """CancelAuthorityIssuer request structure.

    """

    def __init__(self):
        r"""
        :param _Did: The details of the DID.
        :type Did: str
        """
        self._Did = None

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did


    def _deserialize(self, params):
        self._Did = params.get("Did")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelAuthorityIssuerResponse(AbstractModel):
    """CancelAuthorityIssuer response structure.

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


class CheckChainRequest(AbstractModel):
    """CheckChain request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: The group ID.
        :type GroupId: int
        :param _ClusterId: The network ID.
        :type ClusterId: str
        :param _AgencyName: The name of the DID organization.
        :type AgencyName: str
        """
        self._GroupId = None
        self._ClusterId = None
        self._AgencyName = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def AgencyName(self):
        return self._AgencyName

    @AgencyName.setter
    def AgencyName(self, AgencyName):
        self._AgencyName = AgencyName


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._ClusterId = params.get("ClusterId")
        self._AgencyName = params.get("AgencyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckChainResponse(AbstractModel):
    """CheckChain response structure.

    """

    def __init__(self):
        r"""
        :param _RoleType: Whether you are the owner of the consortium. `1`: Yes; `0`: No.
        :type RoleType: int
        :param _ChainId: The chain ID.
        :type ChainId: str
        :param _AppName: The application name.
        :type AppName: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RoleType = None
        self._ChainId = None
        self._AppName = None
        self._RequestId = None

    @property
    def RoleType(self):
        return self._RoleType

    @RoleType.setter
    def RoleType(self, RoleType):
        self._RoleType = RoleType

    @property
    def ChainId(self):
        return self._ChainId

    @ChainId.setter
    def ChainId(self, ChainId):
        self._ChainId = ChainId

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RoleType = params.get("RoleType")
        self._ChainId = params.get("ChainId")
        self._AppName = params.get("AppName")
        self._RequestId = params.get("RequestId")


class CheckDidDeployRequest(AbstractModel):
    """CheckDidDeploy request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: The task ID.
        :type TaskId: int
        """
        self._TaskId = None

    @property
    def TaskId(self):
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
        


class CheckDidDeployResponse(AbstractModel):
    """CheckDidDeploy response structure.

    """

    def __init__(self):
        r"""
        :param _Task: The service information.
        :type Task: :class:`tencentcloud.tdid.v20210519.models.Task`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Task = None
        self._RequestId = None

    @property
    def Task(self):
        return self._Task

    @Task.setter
    def Task(self, Task):
        self._Task = Task

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Task") is not None:
            self._Task = Task()
            self._Task._deserialize(params.get("Task"))
        self._RequestId = params.get("RequestId")


class ConsortiumItem(AbstractModel):
    """The information of a consortium.

    """

    def __init__(self):
        r"""
        :param _Id: The consortium ID.
        :type Id: int
        :param _Name: The consortium name.
        :type Name: str
        """
        self._Id = None
        self._Name = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Contract(AbstractModel):
    """The information of a deployed contract.

    """

    def __init__(self):
        r"""
        :param _ApplyName: The application name.
        :type ApplyName: str
        :param _Enable: The contract status. `true`: Enabled; `false`: Not enabled.
        :type Enable: bool
        :param _Hash: The CNS address of the contract.
        :type Hash: str
        :param _HashShow: The desensitized CNS address.
        :type HashShow: str
        :param _WeId: The DID of the organization that deployed the contract.
        :type WeId: str
        :param _DeployName: The name of the organization that deployed the contract.
        :type DeployName: str
        :param _GroupId: The group.
        :type GroupId: str
        :param _CreateTime: The deployment time.
        :type CreateTime: str
        """
        self._ApplyName = None
        self._Enable = None
        self._Hash = None
        self._HashShow = None
        self._WeId = None
        self._DeployName = None
        self._GroupId = None
        self._CreateTime = None

    @property
    def ApplyName(self):
        return self._ApplyName

    @ApplyName.setter
    def ApplyName(self, ApplyName):
        self._ApplyName = ApplyName

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Hash(self):
        return self._Hash

    @Hash.setter
    def Hash(self, Hash):
        self._Hash = Hash

    @property
    def HashShow(self):
        return self._HashShow

    @HashShow.setter
    def HashShow(self, HashShow):
        self._HashShow = HashShow

    @property
    def WeId(self):
        return self._WeId

    @WeId.setter
    def WeId(self, WeId):
        self._WeId = WeId

    @property
    def DeployName(self):
        return self._DeployName

    @DeployName.setter
    def DeployName(self, DeployName):
        self._DeployName = DeployName

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ApplyName = params.get("ApplyName")
        self._Enable = params.get("Enable")
        self._Hash = params.get("Hash")
        self._HashShow = params.get("HashShow")
        self._WeId = params.get("WeId")
        self._DeployName = params.get("DeployName")
        self._GroupId = params.get("GroupId")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CptIssueRank(AbstractModel):
    """Claim protocol type (CPT) rankings by the number of credentials issued.

    """

    def __init__(self):
        r"""
        :param _CptName: The (claim protocol type) CPT name.
        :type CptName: str
        :param _Rank: The ranking.
        :type Rank: int
        :param _Count: The number of credentials issued.
        :type Count: int
        :param _ApplyName: The application name.
        :type ApplyName: str
        :param _ApplyId: The application ID.
        :type ApplyId: int
        """
        self._CptName = None
        self._Rank = None
        self._Count = None
        self._ApplyName = None
        self._ApplyId = None

    @property
    def CptName(self):
        return self._CptName

    @CptName.setter
    def CptName(self, CptName):
        self._CptName = CptName

    @property
    def Rank(self):
        return self._Rank

    @Rank.setter
    def Rank(self, Rank):
        self._Rank = Rank

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def ApplyName(self):
        return self._ApplyName

    @ApplyName.setter
    def ApplyName(self, ApplyName):
        self._ApplyName = ApplyName

    @property
    def ApplyId(self):
        return self._ApplyId

    @ApplyId.setter
    def ApplyId(self, ApplyId):
        self._ApplyId = ApplyId


    def _deserialize(self, params):
        self._CptName = params.get("CptName")
        self._Rank = params.get("Rank")
        self._Count = params.get("Count")
        self._ApplyName = params.get("ApplyName")
        self._ApplyId = params.get("ApplyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CptListData(AbstractModel):
    """The information of claim protocol types (CPT).

    """

    def __init__(self):
        r"""
        :param _Id: The CPT ID.
        :type Id: int
        :param _Name: The name of the claim protocol type (CPT).
        :type Name: str
        :param _ClusterId: The network ID.
        :type ClusterId: str
        :param _GroupId: The group ID.
        :type GroupId: int
        :param _ServiceId: The service ID.
        :type ServiceId: int
        :param _ContractAppId: The application ID of the contract.
        :type ContractAppId: int
        :param _CptId: The claim protocol type (CPT) ID.
        :type CptId: int
        :param _CptType: The type. `1`: System CPTs; `2`: Authorization CPTs; `3`: General CPTs
        :type CptType: int
        :param _Description: The description of the claim protocol type (CPT).
        :type Description: str
        :param _CptJson: The JSON file of the claim protocol type (CPT).
        :type CptJson: str
        :param _CreateTime: The creation time.
        :type CreateTime: str
        :param _UpdateTime: The last updated time.
        :type UpdateTime: str
        :param _CreatorDid: The DID of the creator.
        :type CreatorDid: str
        :param _AppName: The application name.
        :type AppName: str
        """
        self._Id = None
        self._Name = None
        self._ClusterId = None
        self._GroupId = None
        self._ServiceId = None
        self._ContractAppId = None
        self._CptId = None
        self._CptType = None
        self._Description = None
        self._CptJson = None
        self._CreateTime = None
        self._UpdateTime = None
        self._CreatorDid = None
        self._AppName = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ContractAppId(self):
        return self._ContractAppId

    @ContractAppId.setter
    def ContractAppId(self, ContractAppId):
        self._ContractAppId = ContractAppId

    @property
    def CptId(self):
        return self._CptId

    @CptId.setter
    def CptId(self, CptId):
        self._CptId = CptId

    @property
    def CptType(self):
        return self._CptType

    @CptType.setter
    def CptType(self, CptType):
        self._CptType = CptType

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CptJson(self):
        return self._CptJson

    @CptJson.setter
    def CptJson(self, CptJson):
        self._CptJson = CptJson

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreatorDid(self):
        return self._CreatorDid

    @CreatorDid.setter
    def CreatorDid(self, CreatorDid):
        self._CreatorDid = CreatorDid

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._ClusterId = params.get("ClusterId")
        self._GroupId = params.get("GroupId")
        self._ServiceId = params.get("ServiceId")
        self._ContractAppId = params.get("ContractAppId")
        self._CptId = params.get("CptId")
        self._CptType = params.get("CptType")
        self._Description = params.get("Description")
        self._CptJson = params.get("CptJson")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._CreatorDid = params.get("CreatorDid")
        self._AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCredentialRequest(AbstractModel):
    """CreateCredential request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionArg: A parameter set. For details, see the example.
        :type FunctionArg: :class:`tencentcloud.tdid.v20210519.models.FunctionArg`
        :param _TransactionArg: A parameter set. For details, see the example.
        :type TransactionArg: :class:`tencentcloud.tdid.v20210519.models.TransactionArg`
        :param _VersionCredential: The version.
        :type VersionCredential: str
        :param _UnSigned: Whether the credential is unsigned.
        :type UnSigned: bool
        """
        self._FunctionArg = None
        self._TransactionArg = None
        self._VersionCredential = None
        self._UnSigned = None

    @property
    def FunctionArg(self):
        return self._FunctionArg

    @FunctionArg.setter
    def FunctionArg(self, FunctionArg):
        self._FunctionArg = FunctionArg

    @property
    def TransactionArg(self):
        return self._TransactionArg

    @TransactionArg.setter
    def TransactionArg(self, TransactionArg):
        self._TransactionArg = TransactionArg

    @property
    def VersionCredential(self):
        return self._VersionCredential

    @VersionCredential.setter
    def VersionCredential(self, VersionCredential):
        self._VersionCredential = VersionCredential

    @property
    def UnSigned(self):
        return self._UnSigned

    @UnSigned.setter
    def UnSigned(self, UnSigned):
        self._UnSigned = UnSigned


    def _deserialize(self, params):
        if params.get("FunctionArg") is not None:
            self._FunctionArg = FunctionArg()
            self._FunctionArg._deserialize(params.get("FunctionArg"))
        if params.get("TransactionArg") is not None:
            self._TransactionArg = TransactionArg()
            self._TransactionArg._deserialize(params.get("TransactionArg"))
        self._VersionCredential = params.get("VersionCredential")
        self._UnSigned = params.get("UnSigned")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCredentialResponse(AbstractModel):
    """CreateCredential response structure.

    """

    def __init__(self):
        r"""
        :param _CredentialData: The information of the credential.
        :type CredentialData: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CredentialData = None
        self._RequestId = None

    @property
    def CredentialData(self):
        return self._CredentialData

    @CredentialData.setter
    def CredentialData(self, CredentialData):
        self._CredentialData = CredentialData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CredentialData = params.get("CredentialData")
        self._RequestId = params.get("RequestId")


class CreateDidServiceRequest(AbstractModel):
    """CreateDidService request structure.

    """

    def __init__(self):
        r"""
        :param _ConsortiumName: The consortium name.
        :type ConsortiumName: str
        :param _ConsortiumId: The consortium ID.
        :type ConsortiumId: int
        :param _GroupId: The group ID.
        :type GroupId: int
        :param _AgencyName: The organization name.
        :type AgencyName: str
        :param _AppName: The application name.
        :type AppName: str
        :param _ClusterId: The network ID.
        :type ClusterId: str
        :param _GroupName: The group name.
        :type GroupName: str
        """
        self._ConsortiumName = None
        self._ConsortiumId = None
        self._GroupId = None
        self._AgencyName = None
        self._AppName = None
        self._ClusterId = None
        self._GroupName = None

    @property
    def ConsortiumName(self):
        return self._ConsortiumName

    @ConsortiumName.setter
    def ConsortiumName(self, ConsortiumName):
        self._ConsortiumName = ConsortiumName

    @property
    def ConsortiumId(self):
        return self._ConsortiumId

    @ConsortiumId.setter
    def ConsortiumId(self, ConsortiumId):
        self._ConsortiumId = ConsortiumId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def AgencyName(self):
        return self._AgencyName

    @AgencyName.setter
    def AgencyName(self, AgencyName):
        self._AgencyName = AgencyName

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName


    def _deserialize(self, params):
        self._ConsortiumName = params.get("ConsortiumName")
        self._ConsortiumId = params.get("ConsortiumId")
        self._GroupId = params.get("GroupId")
        self._AgencyName = params.get("AgencyName")
        self._AppName = params.get("AppName")
        self._ClusterId = params.get("ClusterId")
        self._GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDidServiceResponse(AbstractModel):
    """CreateDidService response structure.

    """

    def __init__(self):
        r"""
        :param _Task: The service information.
        :type Task: :class:`tencentcloud.tdid.v20210519.models.Task`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Task = None
        self._RequestId = None

    @property
    def Task(self):
        return self._Task

    @Task.setter
    def Task(self, Task):
        self._Task = Task

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Task") is not None:
            self._Task = Task()
            self._Task._deserialize(params.get("Task"))
        self._RequestId = params.get("RequestId")


class CreateLabelRequest(AbstractModel):
    """CreateLabel request structure.

    """

    def __init__(self):
        r"""
        :param _LabelName: The label name.
        :type LabelName: str
        :param _ClusterId: The network ID.
        :type ClusterId: str
        :param _GroupId: The group ID.
        :type GroupId: int
        """
        self._LabelName = None
        self._ClusterId = None
        self._GroupId = None

    @property
    def LabelName(self):
        return self._LabelName

    @LabelName.setter
    def LabelName(self, LabelName):
        self._LabelName = LabelName

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._LabelName = params.get("LabelName")
        self._ClusterId = params.get("ClusterId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLabelResponse(AbstractModel):
    """CreateLabel response structure.

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


class CreateSelectiveCredentialRequest(AbstractModel):
    """CreateSelectiveCredential request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionArg: A parameter set.
        :type FunctionArg: :class:`tencentcloud.tdid.v20210519.models.VerifyFunctionArg`
        :param _PolicyId: The disclosure policy ID.
        :type PolicyId: int
        """
        self._FunctionArg = None
        self._PolicyId = None

    @property
    def FunctionArg(self):
        return self._FunctionArg

    @FunctionArg.setter
    def FunctionArg(self, FunctionArg):
        self._FunctionArg = FunctionArg

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        if params.get("FunctionArg") is not None:
            self._FunctionArg = VerifyFunctionArg()
            self._FunctionArg._deserialize(params.get("FunctionArg"))
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSelectiveCredentialResponse(AbstractModel):
    """CreateSelectiveCredential response structure.

    """

    def __init__(self):
        r"""
        :param _CredentialData: The credential string.
        :type CredentialData: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CredentialData = None
        self._RequestId = None

    @property
    def CredentialData(self):
        return self._CredentialData

    @CredentialData.setter
    def CredentialData(self, CredentialData):
        self._CredentialData = CredentialData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CredentialData = params.get("CredentialData")
        self._RequestId = params.get("RequestId")


class CreateTDidByPrivateKeyRequest(AbstractModel):
    """CreateTDidByPrivateKey request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: The network ID.
        :type ClusterId: str
        :param _GroupId: The group ID.
        :type GroupId: int
        :param _PrivateKey: The private key.
        :type PrivateKey: str
        """
        self._ClusterId = None
        self._GroupId = None
        self._PrivateKey = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def PrivateKey(self):
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._GroupId = params.get("GroupId")
        self._PrivateKey = params.get("PrivateKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTDidByPrivateKeyResponse(AbstractModel):
    """CreateTDidByPrivateKey response structure.

    """

    def __init__(self):
        r"""
        :param _Did: The DID.
        :type Did: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Did = None
        self._RequestId = None

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Did = params.get("Did")
        self._RequestId = params.get("RequestId")


class CreateTDidByPublicKeyRequest(AbstractModel):
    """CreateTDidByPublicKey request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: The network ID.
        :type ClusterId: str
        :param _GroupId: The group ID.
        :type GroupId: int
        :param _PublicKey: The public key.
        :type PublicKey: str
        :param _EncryptPubKey: The encrypted public key.
        :type EncryptPubKey: str
        """
        self._ClusterId = None
        self._GroupId = None
        self._PublicKey = None
        self._EncryptPubKey = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def EncryptPubKey(self):
        return self._EncryptPubKey

    @EncryptPubKey.setter
    def EncryptPubKey(self, EncryptPubKey):
        self._EncryptPubKey = EncryptPubKey


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._GroupId = params.get("GroupId")
        self._PublicKey = params.get("PublicKey")
        self._EncryptPubKey = params.get("EncryptPubKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTDidByPublicKeyResponse(AbstractModel):
    """CreateTDidByPublicKey response structure.

    """

    def __init__(self):
        r"""
        :param _Did: The DID.
        :type Did: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Did = None
        self._RequestId = None

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Did = params.get("Did")
        self._RequestId = params.get("RequestId")


class CreateTDidRequest(AbstractModel):
    """CreateTDid request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: The group ID.
        :type GroupId: int
        :param _ClusterId: The network ID.
        :type ClusterId: str
        :param _Relegation:  
        :type Relegation: int
        """
        self._GroupId = None
        self._ClusterId = None
        self._Relegation = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Relegation(self):
        return self._Relegation

    @Relegation.setter
    def Relegation(self, Relegation):
        self._Relegation = Relegation


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._ClusterId = params.get("ClusterId")
        self._Relegation = params.get("Relegation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTDidResponse(AbstractModel):
    """CreateTDid response structure.

    """

    def __init__(self):
        r"""
        :param _Did: The DID.
        :type Did: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Did = None
        self._RequestId = None

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Did = params.get("Did")
        self._RequestId = params.get("RequestId")


class CredentialStatus(AbstractModel):
    """The on-chain status of the credential.

    """

    def __init__(self):
        r"""
        :param _CredentialId: The credential ID.
        :type CredentialId: str
        :param _Status: The credential status. `0`: Invalid; `1`: Valid.
        :type Status: int
        :param _Issuer: The DID of the issuer.
        :type Issuer: str
        :param _Digest: A summary of the credential.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Digest: str
        :param _Signature: The credential signature.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Signature: str
        :param _TimeStamp: The last updated timestamp.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TimeStamp: int
        """
        self._CredentialId = None
        self._Status = None
        self._Issuer = None
        self._Digest = None
        self._Signature = None
        self._TimeStamp = None

    @property
    def CredentialId(self):
        return self._CredentialId

    @CredentialId.setter
    def CredentialId(self, CredentialId):
        self._CredentialId = CredentialId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Issuer(self):
        return self._Issuer

    @Issuer.setter
    def Issuer(self, Issuer):
        self._Issuer = Issuer

    @property
    def Digest(self):
        return self._Digest

    @Digest.setter
    def Digest(self, Digest):
        self._Digest = Digest

    @property
    def Signature(self):
        return self._Signature

    @Signature.setter
    def Signature(self, Signature):
        self._Signature = Signature

    @property
    def TimeStamp(self):
        return self._TimeStamp

    @TimeStamp.setter
    def TimeStamp(self, TimeStamp):
        self._TimeStamp = TimeStamp


    def _deserialize(self, params):
        self._CredentialId = params.get("CredentialId")
        self._Status = params.get("Status")
        self._Issuer = params.get("Issuer")
        self._Digest = params.get("Digest")
        self._Signature = params.get("Signature")
        self._TimeStamp = params.get("TimeStamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployByNameRequest(AbstractModel):
    """DeployByName request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationName: The application name.
        :type ApplicationName: str
        :param _ClusterId: The network ID.
        :type ClusterId: str
        :param _GroupId: The group ID.
        :type GroupId: int
        """
        self._ApplicationName = None
        self._ClusterId = None
        self._GroupId = None

    @property
    def ApplicationName(self):
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._ApplicationName = params.get("ApplicationName")
        self._ClusterId = params.get("ClusterId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployByNameResponse(AbstractModel):
    """DeployByName response structure.

    """

    def __init__(self):
        r"""
        :param _Hash: The hash value.
        :type Hash: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Hash = None
        self._RequestId = None

    @property
    def Hash(self):
        return self._Hash

    @Hash.setter
    def Hash(self, Hash):
        self._Hash = Hash

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Hash = params.get("Hash")
        self._RequestId = params.get("RequestId")


class DidCluster(AbstractModel):
    """The information of DID blockchain networks.

    """

    def __init__(self):
        r"""
        :param _ChainId: The chain ID.
        :type ChainId: int
        :param _ChainName: The chain name.
        :type ChainName: str
        :param _AgencyCount: The number of organizations.
        :type AgencyCount: int
        :param _ConsortiumId: The consortium ID.
        :type ConsortiumId: int
        :param _CreateTime: The creation time.
        :type CreateTime: str
        :param _ExpireTime: The expiration time.
        :type ExpireTime: str
        :param _ChainStatus: The network status.
        :type ChainStatus: int
        :param _ResourceId: The resource ID.
        :type ResourceId: str
        :param _ClusterId: The network ID.
        :type ClusterId: str
        :param _ConsortiumName: The consortium name.
        :type ConsortiumName: str
        :param _AgencyId: The organization ID.
        :type AgencyId: int
        :param _AutoRenewFlag: Whether auto-renewal is enabled.
        :type AutoRenewFlag: int
        :param _TotalNetworkNode: The total number of network nodes.
        :type TotalNetworkNode: int
        :param _TotalCreateNode: The number of nodes of the current organization.
        :type TotalCreateNode: int
        :param _TotalGroups: The total number of groups.
        :type TotalGroups: int
        :param _DidCount: The total number of DIDs.
        :type DidCount: int
        """
        self._ChainId = None
        self._ChainName = None
        self._AgencyCount = None
        self._ConsortiumId = None
        self._CreateTime = None
        self._ExpireTime = None
        self._ChainStatus = None
        self._ResourceId = None
        self._ClusterId = None
        self._ConsortiumName = None
        self._AgencyId = None
        self._AutoRenewFlag = None
        self._TotalNetworkNode = None
        self._TotalCreateNode = None
        self._TotalGroups = None
        self._DidCount = None

    @property
    def ChainId(self):
        return self._ChainId

    @ChainId.setter
    def ChainId(self, ChainId):
        self._ChainId = ChainId

    @property
    def ChainName(self):
        return self._ChainName

    @ChainName.setter
    def ChainName(self, ChainName):
        self._ChainName = ChainName

    @property
    def AgencyCount(self):
        return self._AgencyCount

    @AgencyCount.setter
    def AgencyCount(self, AgencyCount):
        self._AgencyCount = AgencyCount

    @property
    def ConsortiumId(self):
        return self._ConsortiumId

    @ConsortiumId.setter
    def ConsortiumId(self, ConsortiumId):
        self._ConsortiumId = ConsortiumId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ChainStatus(self):
        return self._ChainStatus

    @ChainStatus.setter
    def ChainStatus(self, ChainStatus):
        self._ChainStatus = ChainStatus

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ConsortiumName(self):
        return self._ConsortiumName

    @ConsortiumName.setter
    def ConsortiumName(self, ConsortiumName):
        self._ConsortiumName = ConsortiumName

    @property
    def AgencyId(self):
        return self._AgencyId

    @AgencyId.setter
    def AgencyId(self, AgencyId):
        self._AgencyId = AgencyId

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def TotalNetworkNode(self):
        return self._TotalNetworkNode

    @TotalNetworkNode.setter
    def TotalNetworkNode(self, TotalNetworkNode):
        self._TotalNetworkNode = TotalNetworkNode

    @property
    def TotalCreateNode(self):
        return self._TotalCreateNode

    @TotalCreateNode.setter
    def TotalCreateNode(self, TotalCreateNode):
        self._TotalCreateNode = TotalCreateNode

    @property
    def TotalGroups(self):
        return self._TotalGroups

    @TotalGroups.setter
    def TotalGroups(self, TotalGroups):
        self._TotalGroups = TotalGroups

    @property
    def DidCount(self):
        return self._DidCount

    @DidCount.setter
    def DidCount(self, DidCount):
        self._DidCount = DidCount


    def _deserialize(self, params):
        self._ChainId = params.get("ChainId")
        self._ChainName = params.get("ChainName")
        self._AgencyCount = params.get("AgencyCount")
        self._ConsortiumId = params.get("ConsortiumId")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._ChainStatus = params.get("ChainStatus")
        self._ResourceId = params.get("ResourceId")
        self._ClusterId = params.get("ClusterId")
        self._ConsortiumName = params.get("ConsortiumName")
        self._AgencyId = params.get("AgencyId")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._TotalNetworkNode = params.get("TotalNetworkNode")
        self._TotalCreateNode = params.get("TotalCreateNode")
        self._TotalGroups = params.get("TotalGroups")
        self._DidCount = params.get("DidCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DidData(AbstractModel):
    """The information of DIDs.

    """

    def __init__(self):
        r"""
        :param _ServiceId: The service ID.
        :type ServiceId: int
        :param _GroupId: The group ID.
        :type GroupId: int
        :param _AppName: The application name.
        :type AppName: str
        :param _Did: The DID.
        :type Did: str
        :param _Remark: Remarks
        :type Remark: str
        :param _AuthorityState: The status of the authority. `1`: Not registered; `2`: Not certified; `3`: Certified.
        :type AuthorityState: int
        :param _LabelName: The label of the DID.
        :type LabelName: str
        :param _CreatedAt: The DID creation time.
        :type CreatedAt: str
        :param _ClusterId: The network ID.
        :type ClusterId: str
        :param _AllianceName: The consortium name.
        :type AllianceName: str
        :param _LabelId: The label ID.
        :type LabelId: int
        """
        self._ServiceId = None
        self._GroupId = None
        self._AppName = None
        self._Did = None
        self._Remark = None
        self._AuthorityState = None
        self._LabelName = None
        self._CreatedAt = None
        self._ClusterId = None
        self._AllianceName = None
        self._LabelId = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def AuthorityState(self):
        return self._AuthorityState

    @AuthorityState.setter
    def AuthorityState(self, AuthorityState):
        self._AuthorityState = AuthorityState

    @property
    def LabelName(self):
        return self._LabelName

    @LabelName.setter
    def LabelName(self, LabelName):
        self._LabelName = LabelName

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def AllianceName(self):
        return self._AllianceName

    @AllianceName.setter
    def AllianceName(self, AllianceName):
        self._AllianceName = AllianceName

    @property
    def LabelId(self):
        return self._LabelId

    @LabelId.setter
    def LabelId(self, LabelId):
        self._LabelId = LabelId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._GroupId = params.get("GroupId")
        self._AppName = params.get("AppName")
        self._Did = params.get("Did")
        self._Remark = params.get("Remark")
        self._AuthorityState = params.get("AuthorityState")
        self._LabelName = params.get("LabelName")
        self._CreatedAt = params.get("CreatedAt")
        self._ClusterId = params.get("ClusterId")
        self._AllianceName = params.get("AllianceName")
        self._LabelId = params.get("LabelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DidServiceInfo(AbstractModel):
    """The DID service information.

    """

    def __init__(self):
        r"""
        :param _Id: The DID service ID.
        :type Id: int
        :param _Appid: The application ID.
        :type Appid: int
        :param _Uin: The account ID.
        :type Uin: str
        :param _ConsortiumId: The consortium ID.
        :type ConsortiumId: int
        :param _ConsortiumName: The consortium name.
        :type ConsortiumName: str
        :param _ClusterId: The network ID.
        :type ClusterId: str
        :param _GroupId: The group ID.
        :type GroupId: int
        :param _ChainId: The chain ID.
        :type ChainId: str
        :param _RoleType: Whether you are the owner of the consortium. `1`: Yes; `0`: No.
        :type RoleType: int
        :param _AgencyDid: The organization DID.
        :type AgencyDid: str
        :param _CreateOrg: The organization name.
        :type CreateOrg: str
        :param _Endpoint: The endpoint.
        :type Endpoint: str
        :param _CreateTime: The creation time.
        :type CreateTime: str
        :param _UpdateTime: The last updated time.
        :type UpdateTime: str
        :param _GroupName: The group name.
        :type GroupName: str
        """
        self._Id = None
        self._Appid = None
        self._Uin = None
        self._ConsortiumId = None
        self._ConsortiumName = None
        self._ClusterId = None
        self._GroupId = None
        self._ChainId = None
        self._RoleType = None
        self._AgencyDid = None
        self._CreateOrg = None
        self._Endpoint = None
        self._CreateTime = None
        self._UpdateTime = None
        self._GroupName = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Appid(self):
        return self._Appid

    @Appid.setter
    def Appid(self, Appid):
        self._Appid = Appid

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ConsortiumId(self):
        return self._ConsortiumId

    @ConsortiumId.setter
    def ConsortiumId(self, ConsortiumId):
        self._ConsortiumId = ConsortiumId

    @property
    def ConsortiumName(self):
        return self._ConsortiumName

    @ConsortiumName.setter
    def ConsortiumName(self, ConsortiumName):
        self._ConsortiumName = ConsortiumName

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ChainId(self):
        return self._ChainId

    @ChainId.setter
    def ChainId(self, ChainId):
        self._ChainId = ChainId

    @property
    def RoleType(self):
        return self._RoleType

    @RoleType.setter
    def RoleType(self, RoleType):
        self._RoleType = RoleType

    @property
    def AgencyDid(self):
        return self._AgencyDid

    @AgencyDid.setter
    def AgencyDid(self, AgencyDid):
        self._AgencyDid = AgencyDid

    @property
    def CreateOrg(self):
        return self._CreateOrg

    @CreateOrg.setter
    def CreateOrg(self, CreateOrg):
        self._CreateOrg = CreateOrg

    @property
    def Endpoint(self):
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Appid = params.get("Appid")
        self._Uin = params.get("Uin")
        self._ConsortiumId = params.get("ConsortiumId")
        self._ConsortiumName = params.get("ConsortiumName")
        self._ClusterId = params.get("ClusterId")
        self._GroupId = params.get("GroupId")
        self._ChainId = params.get("ChainId")
        self._RoleType = params.get("RoleType")
        self._AgencyDid = params.get("AgencyDid")
        self._CreateOrg = params.get("CreateOrg")
        self._Endpoint = params.get("Endpoint")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownCptRequest(AbstractModel):
    """DownCpt request structure.

    """

    def __init__(self):
        r"""
        :param _CptIndex: The claim protocol type (CPT) index.
        :type CptIndex: int
        """
        self._CptIndex = None

    @property
    def CptIndex(self):
        return self._CptIndex

    @CptIndex.setter
    def CptIndex(self, CptIndex):
        self._CptIndex = CptIndex


    def _deserialize(self, params):
        self._CptIndex = params.get("CptIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownCptResponse(AbstractModel):
    """DownCpt response structure.

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


class EnableHashRequest(AbstractModel):
    """EnableHash request structure.

    """

    def __init__(self):
        r"""
        :param _Hash: The CNS address of the contract.
        :type Hash: str
        """
        self._Hash = None

    @property
    def Hash(self):
        return self._Hash

    @Hash.setter
    def Hash(self, Hash):
        self._Hash = Hash


    def _deserialize(self, params):
        self._Hash = params.get("Hash")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableHashResponse(AbstractModel):
    """EnableHash response structure.

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


class FunctionArg(AbstractModel):
    """The input parameters for creating a credential.

    """

    def __init__(self):
        r"""
        :param _CptId: The claim protocol type (CPT) ID.
        :type CptId: int
        :param _Issuer: The DID of the issuer.
        :type Issuer: str
        :param _ExpirationDate: The expiration time.
        :type ExpirationDate: str
        :param _ClaimJson: The claim.
        :type ClaimJson: str
        """
        self._CptId = None
        self._Issuer = None
        self._ExpirationDate = None
        self._ClaimJson = None

    @property
    def CptId(self):
        return self._CptId

    @CptId.setter
    def CptId(self, CptId):
        self._CptId = CptId

    @property
    def Issuer(self):
        return self._Issuer

    @Issuer.setter
    def Issuer(self, Issuer):
        self._Issuer = Issuer

    @property
    def ExpirationDate(self):
        return self._ExpirationDate

    @ExpirationDate.setter
    def ExpirationDate(self, ExpirationDate):
        self._ExpirationDate = ExpirationDate

    @property
    def ClaimJson(self):
        return self._ClaimJson

    @ClaimJson.setter
    def ClaimJson(self, ClaimJson):
        self._ClaimJson = ClaimJson


    def _deserialize(self, params):
        self._CptId = params.get("CptId")
        self._Issuer = params.get("Issuer")
        self._ExpirationDate = params.get("ExpirationDate")
        self._ClaimJson = params.get("ClaimJson")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAgencyTDidRequest(AbstractModel):
    """GetAgencyTDid request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: The network ID.
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAgencyTDidResponse(AbstractModel):
    """GetAgencyTDid response structure.

    """

    def __init__(self):
        r"""
        :param _Prefix: The prefix (fixed).
        :type Prefix: str
        :param _Identity: The details of the DID.
        :type Identity: list of Identity
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Prefix = None
        self._Identity = None
        self._RequestId = None

    @property
    def Prefix(self):
        return self._Prefix

    @Prefix.setter
    def Prefix(self, Prefix):
        self._Prefix = Prefix

    @property
    def Identity(self):
        return self._Identity

    @Identity.setter
    def Identity(self, Identity):
        self._Identity = Identity

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Prefix = params.get("Prefix")
        if params.get("Identity") is not None:
            self._Identity = []
            for item in params.get("Identity"):
                obj = Identity()
                obj._deserialize(item)
                self._Identity.append(obj)
        self._RequestId = params.get("RequestId")


class GetAuthoritiesListRequest(AbstractModel):
    """GetAuthoritiesList request structure.

    """

    def __init__(self):
        r"""
        :param _PageNumber: The page number, beginning from 1.
        :type PageNumber: int
        :param _PageSize: The number of records per page.
        :type PageSize: int
        :param _Did: The DID.
        :type Did: str
        :param _Status: Whether to query certified or uncertified authorities. `1`: Certified; `2`: Uncertified.
        :type Status: int
        """
        self._PageNumber = None
        self._PageSize = None
        self._Did = None
        self._Status = None

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Did = params.get("Did")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAuthoritiesListResponse(AbstractModel):
    """GetAuthoritiesList response structure.

    """

    def __init__(self):
        r"""
        :param _ResultList: A data set.
        :type ResultList: list of Authority
        :param _AllCount: The total number of records.
        :type AllCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ResultList = None
        self._AllCount = None
        self._RequestId = None

    @property
    def ResultList(self):
        return self._ResultList

    @ResultList.setter
    def ResultList(self, ResultList):
        self._ResultList = ResultList

    @property
    def AllCount(self):
        return self._AllCount

    @AllCount.setter
    def AllCount(self, AllCount):
        self._AllCount = AllCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ResultList") is not None:
            self._ResultList = []
            for item in params.get("ResultList"):
                obj = Authority()
                obj._deserialize(item)
                self._ResultList.append(obj)
        self._AllCount = params.get("AllCount")
        self._RequestId = params.get("RequestId")


class GetAuthorityIssuerRequest(AbstractModel):
    """GetAuthorityIssuer request structure.

    """

    def __init__(self):
        r"""
        :param _Did: The DID.
        :type Did: str
        """
        self._Did = None

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did


    def _deserialize(self, params):
        self._Did = params.get("Did")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAuthorityIssuerResponse(AbstractModel):
    """GetAuthorityIssuer response structure.

    """

    def __init__(self):
        r"""
        :param _Name: The authority name.
        :type Name: str
        :param _ClusterId: The blockchain network ID.
        :type ClusterId: str
        :param _GroupId: The blockchain group ID.
        :type GroupId: int
        :param _Did: The DID of the authority.
        :type Did: str
        :param _Remark: Remarks.
        :type Remark: str
        :param _RegisterTime: The registration time.
        :type RegisterTime: str
        :param _RecognizeTime: The recognition time.
        :type RecognizeTime: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Name = None
        self._ClusterId = None
        self._GroupId = None
        self._Did = None
        self._Remark = None
        self._RegisterTime = None
        self._RecognizeTime = None
        self._RequestId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def RegisterTime(self):
        return self._RegisterTime

    @RegisterTime.setter
    def RegisterTime(self, RegisterTime):
        self._RegisterTime = RegisterTime

    @property
    def RecognizeTime(self):
        return self._RecognizeTime

    @RecognizeTime.setter
    def RecognizeTime(self, RecognizeTime):
        self._RecognizeTime = RecognizeTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ClusterId = params.get("ClusterId")
        self._GroupId = params.get("GroupId")
        self._Did = params.get("Did")
        self._Remark = params.get("Remark")
        self._RegisterTime = params.get("RegisterTime")
        self._RecognizeTime = params.get("RecognizeTime")
        self._RequestId = params.get("RequestId")


class GetConsortiumClusterListRequest(AbstractModel):
    """GetConsortiumClusterList request structure.

    """

    def __init__(self):
        r"""
        :param _ConsortiumId: The consortium ID.
        :type ConsortiumId: int
        """
        self._ConsortiumId = None

    @property
    def ConsortiumId(self):
        return self._ConsortiumId

    @ConsortiumId.setter
    def ConsortiumId(self, ConsortiumId):
        self._ConsortiumId = ConsortiumId


    def _deserialize(self, params):
        self._ConsortiumId = params.get("ConsortiumId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetConsortiumClusterListResponse(AbstractModel):
    """GetConsortiumClusterList response structure.

    """

    def __init__(self):
        r"""
        :param _ClusterList: A list of networks.
        :type ClusterList: list of BcosClusterItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClusterList = None
        self._RequestId = None

    @property
    def ClusterList(self):
        return self._ClusterList

    @ClusterList.setter
    def ClusterList(self, ClusterList):
        self._ClusterList = ClusterList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ClusterList") is not None:
            self._ClusterList = []
            for item in params.get("ClusterList"):
                obj = BcosClusterItem()
                obj._deserialize(item)
                self._ClusterList.append(obj)
        self._RequestId = params.get("RequestId")


class GetConsortiumListRequest(AbstractModel):
    """GetConsortiumList request structure.

    """


class GetConsortiumListResponse(AbstractModel):
    """GetConsortiumList response structure.

    """

    def __init__(self):
        r"""
        :param _ConsortiumList: A list of the consortiums.
        :type ConsortiumList: list of ConsortiumItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ConsortiumList = None
        self._RequestId = None

    @property
    def ConsortiumList(self):
        return self._ConsortiumList

    @ConsortiumList.setter
    def ConsortiumList(self, ConsortiumList):
        self._ConsortiumList = ConsortiumList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ConsortiumList") is not None:
            self._ConsortiumList = []
            for item in params.get("ConsortiumList"):
                obj = ConsortiumItem()
                obj._deserialize(item)
                self._ConsortiumList.append(obj)
        self._RequestId = params.get("RequestId")


class GetCptInfoRequest(AbstractModel):
    """GetCptInfo request structure.

    """

    def __init__(self):
        r"""
        :param _CptIndex: The claim protocol type (CPT) index.
        :type CptIndex: int
        """
        self._CptIndex = None

    @property
    def CptIndex(self):
        return self._CptIndex

    @CptIndex.setter
    def CptIndex(self, CptIndex):
        self._CptIndex = CptIndex


    def _deserialize(self, params):
        self._CptIndex = params.get("CptIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCptInfoResponse(AbstractModel):
    """GetCptInfo response structure.

    """

    def __init__(self):
        r"""
        :param _CptJsonData: The JSON data of the claim protocol type (CPT).
        :type CptJsonData: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CptJsonData = None
        self._RequestId = None

    @property
    def CptJsonData(self):
        return self._CptJsonData

    @CptJsonData.setter
    def CptJsonData(self, CptJsonData):
        self._CptJsonData = CptJsonData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CptJsonData = params.get("CptJsonData")
        self._RequestId = params.get("RequestId")


class GetCptListRequest(AbstractModel):
    """GetCptList request structure.

    """

    def __init__(self):
        r"""
        :param _DisplayStart: The start.
        :type DisplayStart: int
        :param _DisplayLength: The maximum number of records to return.
        :type DisplayLength: int
        :param _CptType: The type. `0`: All CPTs; `1`: System CPTs; `2`: Authorization CPTs; `3`: General CPTs
        :type CptType: int
        """
        self._DisplayStart = None
        self._DisplayLength = None
        self._CptType = None

    @property
    def DisplayStart(self):
        return self._DisplayStart

    @DisplayStart.setter
    def DisplayStart(self, DisplayStart):
        self._DisplayStart = DisplayStart

    @property
    def DisplayLength(self):
        return self._DisplayLength

    @DisplayLength.setter
    def DisplayLength(self, DisplayLength):
        self._DisplayLength = DisplayLength

    @property
    def CptType(self):
        return self._CptType

    @CptType.setter
    def CptType(self, CptType):
        self._CptType = CptType


    def _deserialize(self, params):
        self._DisplayStart = params.get("DisplayStart")
        self._DisplayLength = params.get("DisplayLength")
        self._CptType = params.get("CptType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCptListResponse(AbstractModel):
    """GetCptList response structure.

    """

    def __init__(self):
        r"""
        :param _CptDataList: The information of claim protocol types (CPT).
        :type CptDataList: list of CptListData
        :param _AllCount: The total number of claim protocol types (CPT).
        :type AllCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CptDataList = None
        self._AllCount = None
        self._RequestId = None

    @property
    def CptDataList(self):
        return self._CptDataList

    @CptDataList.setter
    def CptDataList(self, CptDataList):
        self._CptDataList = CptDataList

    @property
    def AllCount(self):
        return self._AllCount

    @AllCount.setter
    def AllCount(self, AllCount):
        self._AllCount = AllCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CptDataList") is not None:
            self._CptDataList = []
            for item in params.get("CptDataList"):
                obj = CptListData()
                obj._deserialize(item)
                self._CptDataList.append(obj)
        self._AllCount = params.get("AllCount")
        self._RequestId = params.get("RequestId")


class GetCredentialCptRankRequest(AbstractModel):
    """GetCredentialCptRank request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: The start date (as early as 2021-4-23).
        :type StartTime: str
        :param _EndTime: The end date (as early as 2021-4-23).
        :type EndTime: str
        :param _ClusterId: The network ID.
        :type ClusterId: str
        """
        self._StartTime = None
        self._EndTime = None
        self._ClusterId = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCredentialCptRankResponse(AbstractModel):
    """GetCredentialCptRank response structure.

    """

    def __init__(self):
        r"""
        :param _RankIssueResult: The rankings.
        :type RankIssueResult: list of CptIssueRank
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RankIssueResult = None
        self._RequestId = None

    @property
    def RankIssueResult(self):
        return self._RankIssueResult

    @RankIssueResult.setter
    def RankIssueResult(self, RankIssueResult):
        self._RankIssueResult = RankIssueResult

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RankIssueResult") is not None:
            self._RankIssueResult = []
            for item in params.get("RankIssueResult"):
                obj = CptIssueRank()
                obj._deserialize(item)
                self._RankIssueResult.append(obj)
        self._RequestId = params.get("RequestId")


class GetCredentialIssueRankRequest(AbstractModel):
    """GetCredentialIssueRank request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: The start date (as early as 2021-4-23).
        :type StartTime: str
        :param _EndTime: The end date (as early as 2021-4-23).
        :type EndTime: str
        :param _ClusterId: The network ID.
        :type ClusterId: str
        """
        self._StartTime = None
        self._EndTime = None
        self._ClusterId = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCredentialIssueRankResponse(AbstractModel):
    """GetCredentialIssueRank response structure.

    """

    def __init__(self):
        r"""
        :param _RankIssueResult: The rankings.
        :type RankIssueResult: list of CptIssueRank
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RankIssueResult = None
        self._RequestId = None

    @property
    def RankIssueResult(self):
        return self._RankIssueResult

    @RankIssueResult.setter
    def RankIssueResult(self, RankIssueResult):
        self._RankIssueResult = RankIssueResult

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RankIssueResult") is not None:
            self._RankIssueResult = []
            for item in params.get("RankIssueResult"):
                obj = CptIssueRank()
                obj._deserialize(item)
                self._RankIssueResult.append(obj)
        self._RequestId = params.get("RequestId")


class GetCredentialIssueTrendRequest(AbstractModel):
    """GetCredentialIssueTrend request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: The start date (as early as 2021-4-23).
        :type StartTime: str
        :param _EndTime: The end date (as early as 2021-4-23).
        :type EndTime: str
        :param _ClusterId: The network ID.
        :type ClusterId: str
        """
        self._StartTime = None
        self._EndTime = None
        self._ClusterId = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCredentialIssueTrendResponse(AbstractModel):
    """GetCredentialIssueTrend response structure.

    """

    def __init__(self):
        r"""
        :param _Trend: The trend information.
        :type Trend: list of Trend
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Trend = None
        self._RequestId = None

    @property
    def Trend(self):
        return self._Trend

    @Trend.setter
    def Trend(self, Trend):
        self._Trend = Trend

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Trend") is not None:
            self._Trend = []
            for item in params.get("Trend"):
                obj = Trend()
                obj._deserialize(item)
                self._Trend.append(obj)
        self._RequestId = params.get("RequestId")


class GetCredentialStatusRequest(AbstractModel):
    """GetCredentialStatus request structure.

    """

    def __init__(self):
        r"""
        :param _CredentialId: The credential ID.
        :type CredentialId: str
        """
        self._CredentialId = None

    @property
    def CredentialId(self):
        return self._CredentialId

    @CredentialId.setter
    def CredentialId(self, CredentialId):
        self._CredentialId = CredentialId


    def _deserialize(self, params):
        self._CredentialId = params.get("CredentialId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCredentialStatusResponse(AbstractModel):
    """GetCredentialStatus response structure.

    """

    def __init__(self):
        r"""
        :param _CredentialStatus: The credential status.
        :type CredentialStatus: :class:`tencentcloud.tdid.v20210519.models.CredentialStatus`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CredentialStatus = None
        self._RequestId = None

    @property
    def CredentialStatus(self):
        return self._CredentialStatus

    @CredentialStatus.setter
    def CredentialStatus(self, CredentialStatus):
        self._CredentialStatus = CredentialStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CredentialStatus") is not None:
            self._CredentialStatus = CredentialStatus()
            self._CredentialStatus._deserialize(params.get("CredentialStatus"))
        self._RequestId = params.get("RequestId")


class GetDataPanelRequest(AbstractModel):
    """GetDataPanel request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: The network ID.
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDataPanelResponse(AbstractModel):
    """GetDataPanel response structure.

    """

    def __init__(self):
        r"""
        :param _BlockNetworkCount: The number of blockchain networks.
        :type BlockNetworkCount: int
        :param _BlockNetworkName: The blockchain network name.
        :type BlockNetworkName: str
        :param _BlockHeight: The current block height.
        :type BlockHeight: int
        :param _BlockNetworkType: The blockchain network type.
        :type BlockNetworkType: int
        :param _DidCount: The number of DIDs.
        :type DidCount: int
        :param _CptCount: The number of claim protocol types (CPT).
        :type CptCount: int
        :param _CertificatedAuthCount: The number of certified authorities.
        :type CertificatedAuthCount: int
        :param _IssueCptCount: The number of credentials issued.
        :type IssueCptCount: int
        :param _NewDidCount: The number of new DIDs in the current week.
        :type NewDidCount: int
        :param _BcosCount: The number of BCOS networks.
        :type BcosCount: int
        :param _FabricCount: The number of Fabric networks.
        :type FabricCount: int
        :param _ChainMakerCount: The number of ChainMaker networks.
        :type ChainMakerCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BlockNetworkCount = None
        self._BlockNetworkName = None
        self._BlockHeight = None
        self._BlockNetworkType = None
        self._DidCount = None
        self._CptCount = None
        self._CertificatedAuthCount = None
        self._IssueCptCount = None
        self._NewDidCount = None
        self._BcosCount = None
        self._FabricCount = None
        self._ChainMakerCount = None
        self._RequestId = None

    @property
    def BlockNetworkCount(self):
        return self._BlockNetworkCount

    @BlockNetworkCount.setter
    def BlockNetworkCount(self, BlockNetworkCount):
        self._BlockNetworkCount = BlockNetworkCount

    @property
    def BlockNetworkName(self):
        return self._BlockNetworkName

    @BlockNetworkName.setter
    def BlockNetworkName(self, BlockNetworkName):
        self._BlockNetworkName = BlockNetworkName

    @property
    def BlockHeight(self):
        return self._BlockHeight

    @BlockHeight.setter
    def BlockHeight(self, BlockHeight):
        self._BlockHeight = BlockHeight

    @property
    def BlockNetworkType(self):
        return self._BlockNetworkType

    @BlockNetworkType.setter
    def BlockNetworkType(self, BlockNetworkType):
        self._BlockNetworkType = BlockNetworkType

    @property
    def DidCount(self):
        return self._DidCount

    @DidCount.setter
    def DidCount(self, DidCount):
        self._DidCount = DidCount

    @property
    def CptCount(self):
        return self._CptCount

    @CptCount.setter
    def CptCount(self, CptCount):
        self._CptCount = CptCount

    @property
    def CertificatedAuthCount(self):
        return self._CertificatedAuthCount

    @CertificatedAuthCount.setter
    def CertificatedAuthCount(self, CertificatedAuthCount):
        self._CertificatedAuthCount = CertificatedAuthCount

    @property
    def IssueCptCount(self):
        return self._IssueCptCount

    @IssueCptCount.setter
    def IssueCptCount(self, IssueCptCount):
        self._IssueCptCount = IssueCptCount

    @property
    def NewDidCount(self):
        return self._NewDidCount

    @NewDidCount.setter
    def NewDidCount(self, NewDidCount):
        self._NewDidCount = NewDidCount

    @property
    def BcosCount(self):
        return self._BcosCount

    @BcosCount.setter
    def BcosCount(self, BcosCount):
        self._BcosCount = BcosCount

    @property
    def FabricCount(self):
        return self._FabricCount

    @FabricCount.setter
    def FabricCount(self, FabricCount):
        self._FabricCount = FabricCount

    @property
    def ChainMakerCount(self):
        return self._ChainMakerCount

    @ChainMakerCount.setter
    def ChainMakerCount(self, ChainMakerCount):
        self._ChainMakerCount = ChainMakerCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BlockNetworkCount = params.get("BlockNetworkCount")
        self._BlockNetworkName = params.get("BlockNetworkName")
        self._BlockHeight = params.get("BlockHeight")
        self._BlockNetworkType = params.get("BlockNetworkType")
        self._DidCount = params.get("DidCount")
        self._CptCount = params.get("CptCount")
        self._CertificatedAuthCount = params.get("CertificatedAuthCount")
        self._IssueCptCount = params.get("IssueCptCount")
        self._NewDidCount = params.get("NewDidCount")
        self._BcosCount = params.get("BcosCount")
        self._FabricCount = params.get("FabricCount")
        self._ChainMakerCount = params.get("ChainMakerCount")
        self._RequestId = params.get("RequestId")


class GetDeployInfoRequest(AbstractModel):
    """GetDeployInfo request structure.

    """

    def __init__(self):
        r"""
        :param _Hash: The CNS address of the contract.
        :type Hash: str
        """
        self._Hash = None

    @property
    def Hash(self):
        return self._Hash

    @Hash.setter
    def Hash(self, Hash):
        self._Hash = Hash


    def _deserialize(self, params):
        self._Hash = params.get("Hash")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeployInfoResponse(AbstractModel):
    """GetDeployInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Hash: The CNS address of the contract.
        :type Hash: str
        :param _GroupId: The main group ID of the contract.
        :type GroupId: str
        :param _DeployDid: The DID of the organization that deployed the contract.
        :type DeployDid: str
        :param _SdkVersion: The TDID SDK version.
        :type SdkVersion: str
        :param _ContractVersion: The TDID contract version.
        :type ContractVersion: str
        :param _BlockVersion: The blockchain node version.
        :type BlockVersion: str
        :param _BlockIp: The IP address of the blockchain node.
        :type BlockIp: str
        :param _DidAddress: The address of the DID contract.
        :type DidAddress: str
        :param _CptAddress: The address of the claim protocol type (CPT) contract.
        :type CptAddress: str
        :param _AuthorityAddress: The address of the authority.
        :type AuthorityAddress: str
        :param _EvidenceAddress: The evidence contract address.
        :type EvidenceAddress: str
        :param _SpecificAddress: The contract address of the specific issuer.
        :type SpecificAddress: str
        :param _ChainId: The chain ID.
        :type ChainId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Hash = None
        self._GroupId = None
        self._DeployDid = None
        self._SdkVersion = None
        self._ContractVersion = None
        self._BlockVersion = None
        self._BlockIp = None
        self._DidAddress = None
        self._CptAddress = None
        self._AuthorityAddress = None
        self._EvidenceAddress = None
        self._SpecificAddress = None
        self._ChainId = None
        self._RequestId = None

    @property
    def Hash(self):
        return self._Hash

    @Hash.setter
    def Hash(self, Hash):
        self._Hash = Hash

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def DeployDid(self):
        return self._DeployDid

    @DeployDid.setter
    def DeployDid(self, DeployDid):
        self._DeployDid = DeployDid

    @property
    def SdkVersion(self):
        return self._SdkVersion

    @SdkVersion.setter
    def SdkVersion(self, SdkVersion):
        self._SdkVersion = SdkVersion

    @property
    def ContractVersion(self):
        return self._ContractVersion

    @ContractVersion.setter
    def ContractVersion(self, ContractVersion):
        self._ContractVersion = ContractVersion

    @property
    def BlockVersion(self):
        return self._BlockVersion

    @BlockVersion.setter
    def BlockVersion(self, BlockVersion):
        self._BlockVersion = BlockVersion

    @property
    def BlockIp(self):
        return self._BlockIp

    @BlockIp.setter
    def BlockIp(self, BlockIp):
        self._BlockIp = BlockIp

    @property
    def DidAddress(self):
        return self._DidAddress

    @DidAddress.setter
    def DidAddress(self, DidAddress):
        self._DidAddress = DidAddress

    @property
    def CptAddress(self):
        return self._CptAddress

    @CptAddress.setter
    def CptAddress(self, CptAddress):
        self._CptAddress = CptAddress

    @property
    def AuthorityAddress(self):
        return self._AuthorityAddress

    @AuthorityAddress.setter
    def AuthorityAddress(self, AuthorityAddress):
        self._AuthorityAddress = AuthorityAddress

    @property
    def EvidenceAddress(self):
        return self._EvidenceAddress

    @EvidenceAddress.setter
    def EvidenceAddress(self, EvidenceAddress):
        self._EvidenceAddress = EvidenceAddress

    @property
    def SpecificAddress(self):
        return self._SpecificAddress

    @SpecificAddress.setter
    def SpecificAddress(self, SpecificAddress):
        self._SpecificAddress = SpecificAddress

    @property
    def ChainId(self):
        return self._ChainId

    @ChainId.setter
    def ChainId(self, ChainId):
        self._ChainId = ChainId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Hash = params.get("Hash")
        self._GroupId = params.get("GroupId")
        self._DeployDid = params.get("DeployDid")
        self._SdkVersion = params.get("SdkVersion")
        self._ContractVersion = params.get("ContractVersion")
        self._BlockVersion = params.get("BlockVersion")
        self._BlockIp = params.get("BlockIp")
        self._DidAddress = params.get("DidAddress")
        self._CptAddress = params.get("CptAddress")
        self._AuthorityAddress = params.get("AuthorityAddress")
        self._EvidenceAddress = params.get("EvidenceAddress")
        self._SpecificAddress = params.get("SpecificAddress")
        self._ChainId = params.get("ChainId")
        self._RequestId = params.get("RequestId")


class GetDeployListRequest(AbstractModel):
    """GetDeployList request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: The network ID.
        :type ClusterId: str
        :param _GroupId: The group ID.
        :type GroupId: int
        :param _DisplayStart: The start.
        :type DisplayStart: int
        :param _DisplayLength: The maximum number of records to return.
        :type DisplayLength: int
        """
        self._ClusterId = None
        self._GroupId = None
        self._DisplayStart = None
        self._DisplayLength = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def DisplayStart(self):
        return self._DisplayStart

    @DisplayStart.setter
    def DisplayStart(self, DisplayStart):
        self._DisplayStart = DisplayStart

    @property
    def DisplayLength(self):
        return self._DisplayLength

    @DisplayLength.setter
    def DisplayLength(self, DisplayLength):
        self._DisplayLength = DisplayLength


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._GroupId = params.get("GroupId")
        self._DisplayStart = params.get("DisplayStart")
        self._DisplayLength = params.get("DisplayLength")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeployListResponse(AbstractModel):
    """GetDeployList response structure.

    """

    def __init__(self):
        r"""
        :param _AllCount: The total number of contracts.
        :type AllCount: int
        :param _Result: A list of deployed contracts.
        :type Result: list of Contract
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AllCount = None
        self._Result = None
        self._RequestId = None

    @property
    def AllCount(self):
        return self._AllCount

    @AllCount.setter
    def AllCount(self, AllCount):
        self._AllCount = AllCount

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AllCount = params.get("AllCount")
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = Contract()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class GetDidClusterDetailRequest(AbstractModel):
    """GetDidClusterDetail request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: The DID network ID.
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDidClusterDetailResponse(AbstractModel):
    """GetDidClusterDetail response structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: The network ID.
        :type ClusterId: str
        :param _ConsortiumName: The consortium name.
        :type ConsortiumName: str
        :param _ChainAgency: The name of the blockchain organization.
        :type ChainAgency: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClusterId = None
        self._ConsortiumName = None
        self._ChainAgency = None
        self._RequestId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ConsortiumName(self):
        return self._ConsortiumName

    @ConsortiumName.setter
    def ConsortiumName(self, ConsortiumName):
        self._ConsortiumName = ConsortiumName

    @property
    def ChainAgency(self):
        return self._ChainAgency

    @ChainAgency.setter
    def ChainAgency(self, ChainAgency):
        self._ChainAgency = ChainAgency

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ConsortiumName = params.get("ConsortiumName")
        self._ChainAgency = params.get("ChainAgency")
        self._RequestId = params.get("RequestId")


class GetDidClusterListRequest(AbstractModel):
    """GetDidClusterList request structure.

    """


class GetDidClusterListResponse(AbstractModel):
    """GetDidClusterList response structure.

    """

    def __init__(self):
        r"""
        :param _DidClusterList: A list of the DID networks.
        :type DidClusterList: list of DidCluster
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DidClusterList = None
        self._RequestId = None

    @property
    def DidClusterList(self):
        return self._DidClusterList

    @DidClusterList.setter
    def DidClusterList(self, DidClusterList):
        self._DidClusterList = DidClusterList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DidClusterList") is not None:
            self._DidClusterList = []
            for item in params.get("DidClusterList"):
                obj = DidCluster()
                obj._deserialize(item)
                self._DidClusterList.append(obj)
        self._RequestId = params.get("RequestId")


class GetDidDetailRequest(AbstractModel):
    """GetDidDetail request structure.

    """

    def __init__(self):
        r"""
        :param _Did: The DID.
        :type Did: str
        """
        self._Did = None

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did


    def _deserialize(self, params):
        self._Did = params.get("Did")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDidDetailResponse(AbstractModel):
    """GetDidDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Did: The DID.
        :type Did: str
        :param _Remark: Remarks
        :type Remark: str
        :param _PublicKey: The public key.
        :type PublicKey: str
        :param _AuthorityState: Whether the DID is a certified authority.
        :type AuthorityState: int
        :param _ConsortiumId: The consortium ID.
        :type ConsortiumId: int
        :param _ConsortiumName: The consortium name.
        :type ConsortiumName: str
        :param _GroupId: The group ID.
        :type GroupId: int
        :param _ClusterId: The network ID.
        :type ClusterId: str
        :param _ResChainId: The BCOS resource ID.
        :type ResChainId: str
        :param _CreateTime: The creation time.
        :type CreateTime: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Did = None
        self._Remark = None
        self._PublicKey = None
        self._AuthorityState = None
        self._ConsortiumId = None
        self._ConsortiumName = None
        self._GroupId = None
        self._ClusterId = None
        self._ResChainId = None
        self._CreateTime = None
        self._RequestId = None

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def AuthorityState(self):
        return self._AuthorityState

    @AuthorityState.setter
    def AuthorityState(self, AuthorityState):
        self._AuthorityState = AuthorityState

    @property
    def ConsortiumId(self):
        return self._ConsortiumId

    @ConsortiumId.setter
    def ConsortiumId(self, ConsortiumId):
        self._ConsortiumId = ConsortiumId

    @property
    def ConsortiumName(self):
        return self._ConsortiumName

    @ConsortiumName.setter
    def ConsortiumName(self, ConsortiumName):
        self._ConsortiumName = ConsortiumName

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ResChainId(self):
        return self._ResChainId

    @ResChainId.setter
    def ResChainId(self, ResChainId):
        self._ResChainId = ResChainId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Did = params.get("Did")
        self._Remark = params.get("Remark")
        self._PublicKey = params.get("PublicKey")
        self._AuthorityState = params.get("AuthorityState")
        self._ConsortiumId = params.get("ConsortiumId")
        self._ConsortiumName = params.get("ConsortiumName")
        self._GroupId = params.get("GroupId")
        self._ClusterId = params.get("ClusterId")
        self._ResChainId = params.get("ResChainId")
        self._CreateTime = params.get("CreateTime")
        self._RequestId = params.get("RequestId")


class GetDidDocumentRequest(AbstractModel):
    """GetDidDocument request structure.

    """

    def __init__(self):
        r"""
        :param _Did: The DID.
        :type Did: str
        """
        self._Did = None

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did


    def _deserialize(self, params):
        self._Did = params.get("Did")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDidDocumentResponse(AbstractModel):
    """GetDidDocument response structure.

    """

    def __init__(self):
        r"""
        :param _Name: The name.
        :type Name: str
        :param _Document: The DID document.
        :type Document: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Name = None
        self._Document = None
        self._RequestId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Document(self):
        return self._Document

    @Document.setter
    def Document(self, Document):
        self._Document = Document

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Document = params.get("Document")
        self._RequestId = params.get("RequestId")


class GetDidListRequest(AbstractModel):
    """GetDidList request structure.

    """

    def __init__(self):
        r"""
        :param _PageSize: The number of records per page.
        :type PageSize: int
        :param _PageNumber: The page number, beginning from 1.
        :type PageNumber: int
        :param _Did: The DID.
        :type Did: str
        :param _ClusterId: The network ID.
        :type ClusterId: str
        :param _GroupId: The group ID.
        :type GroupId: int
        """
        self._PageSize = None
        self._PageNumber = None
        self._Did = None
        self._ClusterId = None
        self._GroupId = None

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._Did = params.get("Did")
        self._ClusterId = params.get("ClusterId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDidListResponse(AbstractModel):
    """GetDidList response structure.

    """

    def __init__(self):
        r"""
        :param _DataList: A list of DIDs.
        :type DataList: list of DidData
        :param _AllCount: The total number of records.
        :type AllCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DataList = None
        self._AllCount = None
        self._RequestId = None

    @property
    def DataList(self):
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList

    @property
    def AllCount(self):
        return self._AllCount

    @AllCount.setter
    def AllCount(self, AllCount):
        self._AllCount = AllCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = DidData()
                obj._deserialize(item)
                self._DataList.append(obj)
        self._AllCount = params.get("AllCount")
        self._RequestId = params.get("RequestId")


class GetDidRegisterTrendRequest(AbstractModel):
    """GetDidRegisterTrend request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: The start date (as early as 2021-4-23).
        :type StartTime: str
        :param _EndTime: The end date (as early as 2021-4-23).
        :type EndTime: str
        :param _ClusterId: The network ID.
        :type ClusterId: str
        """
        self._StartTime = None
        self._EndTime = None
        self._ClusterId = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDidRegisterTrendResponse(AbstractModel):
    """GetDidRegisterTrend response structure.

    """

    def __init__(self):
        r"""
        :param _Trend: The trend information.
        :type Trend: list of Trend
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Trend = None
        self._RequestId = None

    @property
    def Trend(self):
        return self._Trend

    @Trend.setter
    def Trend(self, Trend):
        self._Trend = Trend

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Trend") is not None:
            self._Trend = []
            for item in params.get("Trend"):
                obj = Trend()
                obj._deserialize(item)
                self._Trend.append(obj)
        self._RequestId = params.get("RequestId")


class GetDidServiceDetailRequest(AbstractModel):
    """GetDidServiceDetail request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: The DID service ID.
        :type ServiceId: int
        """
        self._ServiceId = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDidServiceDetailResponse(AbstractModel):
    """GetDidServiceDetail response structure.

    """

    def __init__(self):
        r"""
        :param _DidService: The DID service information.
        :type DidService: :class:`tencentcloud.tdid.v20210519.models.DidServiceInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DidService = None
        self._RequestId = None

    @property
    def DidService(self):
        return self._DidService

    @DidService.setter
    def DidService(self, DidService):
        self._DidService = DidService

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DidService") is not None:
            self._DidService = DidServiceInfo()
            self._DidService._deserialize(params.get("DidService"))
        self._RequestId = params.get("RequestId")


class GetDidServiceListRequest(AbstractModel):
    """GetDidServiceList request structure.

    """

    def __init__(self):
        r"""
        :param _Type: `1`: Return results at the network level; `0`: Return results at the service level.
        :type Type: int
        """
        self._Type = None

    @property
    def Type(self):
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
        


class GetDidServiceListResponse(AbstractModel):
    """GetDidServiceList response structure.

    """

    def __init__(self):
        r"""
        :param _DidServiceList: A list of DID services.
        :type DidServiceList: list of DidServiceInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DidServiceList = None
        self._RequestId = None

    @property
    def DidServiceList(self):
        return self._DidServiceList

    @DidServiceList.setter
    def DidServiceList(self, DidServiceList):
        self._DidServiceList = DidServiceList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DidServiceList") is not None:
            self._DidServiceList = []
            for item in params.get("DidServiceList"):
                obj = DidServiceInfo()
                obj._deserialize(item)
                self._DidServiceList.append(obj)
        self._RequestId = params.get("RequestId")


class GetGroupListRequest(AbstractModel):
    """GetGroupList request structure.

    """

    def __init__(self):
        r"""
        :param _Status: `0`: Groups with no DID services; `1`: Groups with DID services.
        :type Status: int
        :param _ClusterId: The network ID.
        :type ClusterId: str
        """
        self._Status = None
        self._ClusterId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGroupListResponse(AbstractModel):
    """GetGroupList response structure.

    """

    def __init__(self):
        r"""
        :param _Result: A list of groups.
        :type Result: list of Group
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = Group()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class GetLabelListRequest(AbstractModel):
    """GetLabelList request structure.

    """

    def __init__(self):
        r"""
        :param _PageSize: The number of records per page.
        :type PageSize: int
        :param _PageNumber: The page number, beginning from 1.
        :type PageNumber: int
        :param _ClusterId: The network ID.
        :type ClusterId: str
        :param _GroupId: The group ID.
        :type GroupId: int
        """
        self._PageSize = None
        self._PageNumber = None
        self._ClusterId = None
        self._GroupId = None

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._ClusterId = params.get("ClusterId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetLabelListResponse(AbstractModel):
    """GetLabelList response structure.

    """

    def __init__(self):
        r"""
        :param _Result: A data set.
        :type Result: list of Label
        :param _TotalCount: The total number of records.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = Label()
                obj._deserialize(item)
                self._Result.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class GetPolicyListRequest(AbstractModel):
    """GetPolicyList request structure.

    """

    def __init__(self):
        r"""
        :param _DisplayStart: The start.
        :type DisplayStart: int
        :param _DisplayLength: The maximum number of records to return.
        :type DisplayLength: int
        """
        self._DisplayStart = None
        self._DisplayLength = None

    @property
    def DisplayStart(self):
        return self._DisplayStart

    @DisplayStart.setter
    def DisplayStart(self, DisplayStart):
        self._DisplayStart = DisplayStart

    @property
    def DisplayLength(self):
        return self._DisplayLength

    @DisplayLength.setter
    def DisplayLength(self, DisplayLength):
        self._DisplayLength = DisplayLength


    def _deserialize(self, params):
        self._DisplayStart = params.get("DisplayStart")
        self._DisplayLength = params.get("DisplayLength")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPolicyListResponse(AbstractModel):
    """GetPolicyList response structure.

    """

    def __init__(self):
        r"""
        :param _PolicyDataList: A list of disclosure policies.
        :type PolicyDataList: list of Policy
        :param _AllCount: The total number of records.
        :type AllCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PolicyDataList = None
        self._AllCount = None
        self._RequestId = None

    @property
    def PolicyDataList(self):
        return self._PolicyDataList

    @PolicyDataList.setter
    def PolicyDataList(self, PolicyDataList):
        self._PolicyDataList = PolicyDataList

    @property
    def AllCount(self):
        return self._AllCount

    @AllCount.setter
    def AllCount(self, AllCount):
        self._AllCount = AllCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PolicyDataList") is not None:
            self._PolicyDataList = []
            for item in params.get("PolicyDataList"):
                obj = Policy()
                obj._deserialize(item)
                self._PolicyDataList.append(obj)
        self._AllCount = params.get("AllCount")
        self._RequestId = params.get("RequestId")


class GetPublicKeyRequest(AbstractModel):
    """GetPublicKey request structure.

    """

    def __init__(self):
        r"""
        :param _Did: The DID.
        :type Did: str
        """
        self._Did = None

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did


    def _deserialize(self, params):
        self._Did = params.get("Did")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPublicKeyResponse(AbstractModel):
    """GetPublicKey response structure.

    """

    def __init__(self):
        r"""
        :param _Did: The DID.
        :type Did: str
        :param _PublicKey: The public key.
        :type PublicKey: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Did = None
        self._PublicKey = None
        self._RequestId = None

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did

    @property
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Did = params.get("Did")
        self._PublicKey = params.get("PublicKey")
        self._RequestId = params.get("RequestId")


class Group(AbstractModel):
    """The group information.

    """

    def __init__(self):
        r"""
        :param _GroupId: The group ID.
        :type GroupId: int
        :param _NodeCount: The number of nodes.
        :type NodeCount: int
        :param _NodeCountOfAgency: The number of nodes of the organization.
        :type NodeCountOfAgency: int
        :param _Description: The description of the group.
        :type Description: str
        :param _RoleType: Whether you are the owner of the consortium or not.
        :type RoleType: int
        :param _ChainId: The chain ID.
        :type ChainId: str
        """
        self._GroupId = None
        self._NodeCount = None
        self._NodeCountOfAgency = None
        self._Description = None
        self._RoleType = None
        self._ChainId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def NodeCount(self):
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def NodeCountOfAgency(self):
        return self._NodeCountOfAgency

    @NodeCountOfAgency.setter
    def NodeCountOfAgency(self, NodeCountOfAgency):
        self._NodeCountOfAgency = NodeCountOfAgency

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RoleType(self):
        return self._RoleType

    @RoleType.setter
    def RoleType(self, RoleType):
        self._RoleType = RoleType

    @property
    def ChainId(self):
        return self._ChainId

    @ChainId.setter
    def ChainId(self, ChainId):
        self._ChainId = ChainId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._NodeCount = params.get("NodeCount")
        self._NodeCountOfAgency = params.get("NodeCountOfAgency")
        self._Description = params.get("Description")
        self._RoleType = params.get("RoleType")
        self._ChainId = params.get("ChainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Identity(AbstractModel):
    """The details of the DID.

    """

    def __init__(self):
        r"""
        :param _AccountIdentifier: The account identifier.
        :type AccountIdentifier: str
        :param _ChainID: The chain ID.
        :type ChainID: str
        :param _Did: The DID.
        :type Did: str
        :param _GroupId: The group ID.
        :type GroupId: int
        :param _GroupName: The group name.
        :type GroupName: str
        """
        self._AccountIdentifier = None
        self._ChainID = None
        self._Did = None
        self._GroupId = None
        self._GroupName = None

    @property
    def AccountIdentifier(self):
        return self._AccountIdentifier

    @AccountIdentifier.setter
    def AccountIdentifier(self, AccountIdentifier):
        self._AccountIdentifier = AccountIdentifier

    @property
    def ChainID(self):
        return self._ChainID

    @ChainID.setter
    def ChainID(self, ChainID):
        self._ChainID = ChainID

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did

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


    def _deserialize(self, params):
        self._AccountIdentifier = params.get("AccountIdentifier")
        self._ChainID = params.get("ChainID")
        self._Did = params.get("Did")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Label(AbstractModel):
    """The label information.

    """

    def __init__(self):
        r"""
        :param _LabelId: The label ID.
        :type LabelId: int
        :param _LabelName: The label name.
        :type LabelName: str
        :param _DidCount: The number of DIDs.
        :type DidCount: int
        :param _Did: The DID of the creator.
        :type Did: str
        :param _ClusterId: The network ID.
        :type ClusterId: str
        :param _CreateTime: The creation time.
        :type CreateTime: str
        :param _GroupId: The group ID.
        :type GroupId: int
        """
        self._LabelId = None
        self._LabelName = None
        self._DidCount = None
        self._Did = None
        self._ClusterId = None
        self._CreateTime = None
        self._GroupId = None

    @property
    def LabelId(self):
        return self._LabelId

    @LabelId.setter
    def LabelId(self, LabelId):
        self._LabelId = LabelId

    @property
    def LabelName(self):
        return self._LabelName

    @LabelName.setter
    def LabelName(self, LabelName):
        self._LabelName = LabelName

    @property
    def DidCount(self):
        return self._DidCount

    @DidCount.setter
    def DidCount(self, DidCount):
        self._DidCount = DidCount

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._LabelId = params.get("LabelId")
        self._LabelName = params.get("LabelName")
        self._DidCount = params.get("DidCount")
        self._Did = params.get("Did")
        self._ClusterId = params.get("ClusterId")
        self._CreateTime = params.get("CreateTime")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Policy(AbstractModel):
    """The policy information.

    """

    def __init__(self):
        r"""
        :param _Id: The policy index.
        :type Id: int
        :param _Name: The policy name.
        :type Name: str
        :param _ClusterId: The network ID.
        :type ClusterId: str
        :param _GroupId: The group ID.
        :type GroupId: int
        :param _ServiceId: The service ID.
        :type ServiceId: int
        :param _ContractAppId: The application ID of the contract.
        :type ContractAppId: int
        :param _PolicyId: The policy ID.
        :type PolicyId: int
        :param _CptId: The claim protocol type (CPT) ID.
        :type CptId: int
        :param _PolicyJson: The JSON data.
        :type PolicyJson: str
        :param _CreateTime: The creation time.
        :type CreateTime: str
        :param _UpdateTime: The last updated time.
        :type UpdateTime: str
        :param _CreatorDid: The DID of the creator.
        :type CreatorDid: str
        :param _AppName: The application name.
        :type AppName: str
        :param _CptIndex: The claim protocol type (CPT) index.
        :type CptIndex: int
        """
        self._Id = None
        self._Name = None
        self._ClusterId = None
        self._GroupId = None
        self._ServiceId = None
        self._ContractAppId = None
        self._PolicyId = None
        self._CptId = None
        self._PolicyJson = None
        self._CreateTime = None
        self._UpdateTime = None
        self._CreatorDid = None
        self._AppName = None
        self._CptIndex = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ContractAppId(self):
        return self._ContractAppId

    @ContractAppId.setter
    def ContractAppId(self, ContractAppId):
        self._ContractAppId = ContractAppId

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def CptId(self):
        return self._CptId

    @CptId.setter
    def CptId(self, CptId):
        self._CptId = CptId

    @property
    def PolicyJson(self):
        return self._PolicyJson

    @PolicyJson.setter
    def PolicyJson(self, PolicyJson):
        self._PolicyJson = PolicyJson

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreatorDid(self):
        return self._CreatorDid

    @CreatorDid.setter
    def CreatorDid(self, CreatorDid):
        self._CreatorDid = CreatorDid

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def CptIndex(self):
        return self._CptIndex

    @CptIndex.setter
    def CptIndex(self, CptIndex):
        self._CptIndex = CptIndex


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._ClusterId = params.get("ClusterId")
        self._GroupId = params.get("GroupId")
        self._ServiceId = params.get("ServiceId")
        self._ContractAppId = params.get("ContractAppId")
        self._PolicyId = params.get("PolicyId")
        self._CptId = params.get("CptId")
        self._PolicyJson = params.get("PolicyJson")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._CreatorDid = params.get("CreatorDid")
        self._AppName = params.get("AppName")
        self._CptIndex = params.get("CptIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Proof(AbstractModel):
    """The credential signature.

    """

    def __init__(self):
        r"""
        :param _Created: The creation time.
        :type Created: int
        :param _Creator: The DID of the creator.
        :type Creator: str
        :param _SaltJson: The salt value.
        :type SaltJson: str
        :param _SignatureValue: The signature.
        :type SignatureValue: str
        :param _Type: The type.
        :type Type: str
        """
        self._Created = None
        self._Creator = None
        self._SaltJson = None
        self._SignatureValue = None
        self._Type = None

    @property
    def Created(self):
        return self._Created

    @Created.setter
    def Created(self, Created):
        self._Created = Created

    @property
    def Creator(self):
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def SaltJson(self):
        return self._SaltJson

    @SaltJson.setter
    def SaltJson(self, SaltJson):
        self._SaltJson = SaltJson

    @property
    def SignatureValue(self):
        return self._SignatureValue

    @SignatureValue.setter
    def SignatureValue(self, SignatureValue):
        self._SignatureValue = SignatureValue

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Created = params.get("Created")
        self._Creator = params.get("Creator")
        self._SaltJson = params.get("SaltJson")
        self._SignatureValue = params.get("SignatureValue")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryPolicyRequest(AbstractModel):
    """QueryPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _PolicyIndex: The policy index.
        :type PolicyIndex: int
        """
        self._PolicyIndex = None

    @property
    def PolicyIndex(self):
        return self._PolicyIndex

    @PolicyIndex.setter
    def PolicyIndex(self, PolicyIndex):
        self._PolicyIndex = PolicyIndex


    def _deserialize(self, params):
        self._PolicyIndex = params.get("PolicyIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryPolicyResponse(AbstractModel):
    """QueryPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _Id: The policy index.
        :type Id: int
        :param _PolicyId: The policy ID.
        :type PolicyId: int
        :param _CptId: The claim protocol type (CPT) ID.
        :type CptId: int
        :param _PolicyData: The content of the policy.
        :type PolicyData: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._PolicyId = None
        self._CptId = None
        self._PolicyData = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def CptId(self):
        return self._CptId

    @CptId.setter
    def CptId(self, CptId):
        self._CptId = CptId

    @property
    def PolicyData(self):
        return self._PolicyData

    @PolicyData.setter
    def PolicyData(self, PolicyData):
        self._PolicyData = PolicyData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._PolicyId = params.get("PolicyId")
        self._CptId = params.get("CptId")
        self._PolicyData = params.get("PolicyData")
        self._RequestId = params.get("RequestId")


class RecognizeAuthorityIssuerRequest(AbstractModel):
    """RecognizeAuthorityIssuer request structure.

    """

    def __init__(self):
        r"""
        :param _Did: The DID.
        :type Did: str
        """
        self._Did = None

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did


    def _deserialize(self, params):
        self._Did = params.get("Did")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeAuthorityIssuerResponse(AbstractModel):
    """RecognizeAuthorityIssuer response structure.

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


class RegisterClaimPolicyRequest(AbstractModel):
    """RegisterClaimPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _CptIndex: The claim protocol type (CPT) index.
        :type CptIndex: int
        :param _Policy: The disclosure policy.
        :type Policy: str
        """
        self._CptIndex = None
        self._Policy = None

    @property
    def CptIndex(self):
        return self._CptIndex

    @CptIndex.setter
    def CptIndex(self, CptIndex):
        self._CptIndex = CptIndex

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy


    def _deserialize(self, params):
        self._CptIndex = params.get("CptIndex")
        self._Policy = params.get("Policy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterClaimPolicyResponse(AbstractModel):
    """RegisterClaimPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _Id: The policy index.
        :type Id: int
        :param _PolicyId: The policy ID.
        :type PolicyId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._PolicyId = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._PolicyId = params.get("PolicyId")
        self._RequestId = params.get("RequestId")


class RegisterCptRequest(AbstractModel):
    """RegisterCpt request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: The group ID.
        :type GroupId: int
        :param _ClusterId: The network ID.
        :type ClusterId: str
        :param _CptJson: The JSON data of the credential claim type (CPT).
        :type CptJson: str
        :param _CptId: If you do not specify this, the ID will auto increment.
        :type CptId: int
        """
        self._GroupId = None
        self._ClusterId = None
        self._CptJson = None
        self._CptId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def CptJson(self):
        return self._CptJson

    @CptJson.setter
    def CptJson(self, CptJson):
        self._CptJson = CptJson

    @property
    def CptId(self):
        return self._CptId

    @CptId.setter
    def CptId(self, CptId):
        self._CptId = CptId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._ClusterId = params.get("ClusterId")
        self._CptJson = params.get("CptJson")
        self._CptId = params.get("CptId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterCptResponse(AbstractModel):
    """RegisterCpt response structure.

    """

    def __init__(self):
        r"""
        :param _Id: The claim protocol type (CPT) index.
        :type Id: int
        :param _CptId: The claim protocol type (CPT) ID.
        :type CptId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._CptId = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CptId(self):
        return self._CptId

    @CptId.setter
    def CptId(self, CptId):
        self._CptId = CptId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CptId = params.get("CptId")
        self._RequestId = params.get("RequestId")


class RegisterIssuerRequest(AbstractModel):
    """RegisterIssuer request structure.

    """

    def __init__(self):
        r"""
        :param _Did: The DID.
        :type Did: str
        :param _Name: The issuing authority name.
        :type Name: str
        :param _Description: Remarks
        :type Description: str
        """
        self._Did = None
        self._Name = None
        self._Description = None

    @property
    def Did(self):
        return self._Did

    @Did.setter
    def Did(self, Did):
        self._Did = Did

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Did = params.get("Did")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterIssuerResponse(AbstractModel):
    """RegisterIssuer response structure.

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


class RemoveHashRequest(AbstractModel):
    """RemoveHash request structure.

    """

    def __init__(self):
        r"""
        :param _Hash: The CNS address of the contract.
        :type Hash: str
        """
        self._Hash = None

    @property
    def Hash(self):
        return self._Hash

    @Hash.setter
    def Hash(self, Hash):
        self._Hash = Hash


    def _deserialize(self, params):
        self._Hash = params.get("Hash")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveHashResponse(AbstractModel):
    """RemoveHash response structure.

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


class SetCredentialStatusRequest(AbstractModel):
    """SetCredentialStatus request structure.

    """

    def __init__(self):
        r"""
        :param _CredentialStatus: The credential status.
        :type CredentialStatus: :class:`tencentcloud.tdid.v20210519.models.CredentialStatus`
        """
        self._CredentialStatus = None

    @property
    def CredentialStatus(self):
        return self._CredentialStatus

    @CredentialStatus.setter
    def CredentialStatus(self, CredentialStatus):
        self._CredentialStatus = CredentialStatus


    def _deserialize(self, params):
        if params.get("CredentialStatus") is not None:
            self._CredentialStatus = CredentialStatus()
            self._CredentialStatus._deserialize(params.get("CredentialStatus"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetCredentialStatusResponse(AbstractModel):
    """SetCredentialStatus response structure.

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


class Task(AbstractModel):
    """The output parameter of `CreateDidService` and `CheckDidDeploy`.

    """

    def __init__(self):
        r"""
        :param _Id: The task ID.
        :type Id: int
        :param _AppId: The application ID.
        :type AppId: int
        :param _ClusterId: The network ID.
        :type ClusterId: str
        :param _GroupId: The group ID.
        :type GroupId: int
        :param _ServiceId: The service ID.
        :type ServiceId: int
        :param _Status: `0`: Under deployment; `1`: Deployed successfully; other values: Deployment failed.
        :type Status: int
        :param _ErrorCode: The error code.
        :type ErrorCode: str
        :param _ErrorMsg: The error message.
        :type ErrorMsg: str
        :param _CreateTime: The creation time.
        :type CreateTime: str
        :param _UpdateTime: The last updated time.
        :type UpdateTime: str
        """
        self._Id = None
        self._AppId = None
        self._ClusterId = None
        self._GroupId = None
        self._ServiceId = None
        self._Status = None
        self._ErrorCode = None
        self._ErrorMsg = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._AppId = params.get("AppId")
        self._ClusterId = params.get("ClusterId")
        self._GroupId = params.get("GroupId")
        self._ServiceId = params.get("ServiceId")
        self._Status = params.get("Status")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMsg = params.get("ErrorMsg")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransactionArg(AbstractModel):
    """The transaction parameters.

    """

    def __init__(self):
        r"""
        :param _InvokerTDid: The credential ID.
        :type InvokerTDid: str
        """
        self._InvokerTDid = None

    @property
    def InvokerTDid(self):
        return self._InvokerTDid

    @InvokerTDid.setter
    def InvokerTDid(self, InvokerTDid):
        self._InvokerTDid = InvokerTDid


    def _deserialize(self, params):
        self._InvokerTDid = params.get("InvokerTDid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Trend(AbstractModel):
    """The trends.

    """

    def __init__(self):
        r"""
        :param _Time: The time point.
        :type Time: str
        :param _Count: The count.
        :type Count: int
        """
        self._Time = None
        self._Count = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyCredentialRequest(AbstractModel):
    """VerifyCredential request structure.

    """

    def __init__(self):
        r"""
        :param _FunctionArg: A parameter set.
        :type FunctionArg: :class:`tencentcloud.tdid.v20210519.models.VerifyFunctionArg`
        """
        self._FunctionArg = None

    @property
    def FunctionArg(self):
        return self._FunctionArg

    @FunctionArg.setter
    def FunctionArg(self, FunctionArg):
        self._FunctionArg = FunctionArg


    def _deserialize(self, params):
        if params.get("FunctionArg") is not None:
            self._FunctionArg = VerifyFunctionArg()
            self._FunctionArg._deserialize(params.get("FunctionArg"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyCredentialResponse(AbstractModel):
    """VerifyCredential response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether the verification is successful.
        :type Result: bool
        :param _VerifyCode: The verification code.
        :type VerifyCode: int
        :param _VerifyMessage: The verification message.
        :type VerifyMessage: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._VerifyCode = None
        self._VerifyMessage = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def VerifyCode(self):
        return self._VerifyCode

    @VerifyCode.setter
    def VerifyCode(self, VerifyCode):
        self._VerifyCode = VerifyCode

    @property
    def VerifyMessage(self):
        return self._VerifyMessage

    @VerifyMessage.setter
    def VerifyMessage(self, VerifyMessage):
        self._VerifyMessage = VerifyMessage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._VerifyCode = params.get("VerifyCode")
        self._VerifyMessage = params.get("VerifyMessage")
        self._RequestId = params.get("RequestId")


class VerifyFunctionArg(AbstractModel):
    """The credential verification parameters.

    """

    def __init__(self):
        r"""
        :param _CptId: The claim protocol type (CPT) ID.
        :type CptId: int
        :param _Issuer: The issuer DID.
        :type Issuer: str
        :param _ExpirationDate: The expiration time.
        :type ExpirationDate: int
        :param _ClaimJson: The claim.
        :type ClaimJson: str
        :param _IssuanceDate: The time when the credential was issued.
        :type IssuanceDate: int
        :param _Context: The context.
        :type Context: str
        :param _Id: The ID.
        :type Id: str
        :param _Proof: The signature.
        :type Proof: :class:`tencentcloud.tdid.v20210519.models.Proof`
        :param _Type: The type.
        :type Type: list of str
        """
        self._CptId = None
        self._Issuer = None
        self._ExpirationDate = None
        self._ClaimJson = None
        self._IssuanceDate = None
        self._Context = None
        self._Id = None
        self._Proof = None
        self._Type = None

    @property
    def CptId(self):
        return self._CptId

    @CptId.setter
    def CptId(self, CptId):
        self._CptId = CptId

    @property
    def Issuer(self):
        return self._Issuer

    @Issuer.setter
    def Issuer(self, Issuer):
        self._Issuer = Issuer

    @property
    def ExpirationDate(self):
        return self._ExpirationDate

    @ExpirationDate.setter
    def ExpirationDate(self, ExpirationDate):
        self._ExpirationDate = ExpirationDate

    @property
    def ClaimJson(self):
        return self._ClaimJson

    @ClaimJson.setter
    def ClaimJson(self, ClaimJson):
        self._ClaimJson = ClaimJson

    @property
    def IssuanceDate(self):
        return self._IssuanceDate

    @IssuanceDate.setter
    def IssuanceDate(self, IssuanceDate):
        self._IssuanceDate = IssuanceDate

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Proof(self):
        return self._Proof

    @Proof.setter
    def Proof(self, Proof):
        self._Proof = Proof

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._CptId = params.get("CptId")
        self._Issuer = params.get("Issuer")
        self._ExpirationDate = params.get("ExpirationDate")
        self._ClaimJson = params.get("ClaimJson")
        self._IssuanceDate = params.get("IssuanceDate")
        self._Context = params.get("Context")
        self._Id = params.get("Id")
        if params.get("Proof") is not None:
            self._Proof = Proof()
            self._Proof._deserialize(params.get("Proof"))
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        