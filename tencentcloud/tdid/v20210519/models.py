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
        :param LabelId: The label ID.
        :type LabelId: int
        :param Did: 
        :type Did: str
        """
        self.LabelId = None
        self.Did = None


    def _deserialize(self, params):
        self.LabelId = params.get("LabelId")
        self.Did = params.get("Did")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddLabelResponse(AbstractModel):
    """AddLabel response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Authority(AbstractModel):
    """The information of an authority.

    """

    def __init__(self):
        r"""
        :param Id: The authority ID.
        :type Id: int
        :param DidId: The DID.
        :type DidId: int
        :param Did: The details of the DID.
        :type Did: str
        :param Name: The authority name.
        :type Name: str
        :param Status: Whether the authority is certified. `1`: Yes; `2`: No.
        :type Status: int
        :param DidServiceId: The DID service ID.
        :type DidServiceId: int
        :param ContractAppId: The application ID.
        :type ContractAppId: int
        :param Remark: Remarks
        :type Remark: str
        :param RegisterTime: The registration time.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RegisterTime: str
        :param RecognizeTime: The recognition time.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RecognizeTime: str
        :param CreateTime: The creation time.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param UpdateTime: The last updated time.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param ClusterId: The network ID.
        :type ClusterId: str
        :param GroupId: The group ID.
        :type GroupId: int
        :param AppName: The application name.
        :type AppName: str
        :param LabelName: The on-chain label.
        :type LabelName: str
        """
        self.Id = None
        self.DidId = None
        self.Did = None
        self.Name = None
        self.Status = None
        self.DidServiceId = None
        self.ContractAppId = None
        self.Remark = None
        self.RegisterTime = None
        self.RecognizeTime = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ClusterId = None
        self.GroupId = None
        self.AppName = None
        self.LabelName = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.DidId = params.get("DidId")
        self.Did = params.get("Did")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.DidServiceId = params.get("DidServiceId")
        self.ContractAppId = params.get("ContractAppId")
        self.Remark = params.get("Remark")
        self.RegisterTime = params.get("RegisterTime")
        self.RecognizeTime = params.get("RecognizeTime")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        self.AppName = params.get("AppName")
        self.LabelName = params.get("LabelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BcosClusterItem(AbstractModel):
    """The information of a BCOS network.

    """

    def __init__(self):
        r"""
        :param ChainId: The network ID.
        :type ChainId: int
        :param ChainName: The network name.
        :type ChainName: str
        :param AgencyCount: The number of organizations.
        :type AgencyCount: int
        :param ConsortiumId: The consortium ID.
        :type ConsortiumId: int
        :param CreateTime: The creation time.
        :type CreateTime: str
        :param ExpireTime: The expiration time.
        :type ExpireTime: str
        :param ChainStatus: The network status.
        :type ChainStatus: int
        :param ResourceId: The resource ID.
        :type ResourceId: str
        :param ClusterId: The cluster ID.
        :type ClusterId: str
        :param ConsortiumName: The consortium name.
        :type ConsortiumName: str
        :param AgencyId: The organization ID.
        :type AgencyId: int
        :param AutoRenewFlag: The renewal status.
        :type AutoRenewFlag: int
        :param TotalNetworkNode: The network mode.
        :type TotalNetworkNode: int
        :param TotalCreateNode: The number of nodes created.
        :type TotalCreateNode: int
        :param TotalGroups: The total number of groups.
        :type TotalGroups: int
        """
        self.ChainId = None
        self.ChainName = None
        self.AgencyCount = None
        self.ConsortiumId = None
        self.CreateTime = None
        self.ExpireTime = None
        self.ChainStatus = None
        self.ResourceId = None
        self.ClusterId = None
        self.ConsortiumName = None
        self.AgencyId = None
        self.AutoRenewFlag = None
        self.TotalNetworkNode = None
        self.TotalCreateNode = None
        self.TotalGroups = None


    def _deserialize(self, params):
        self.ChainId = params.get("ChainId")
        self.ChainName = params.get("ChainName")
        self.AgencyCount = params.get("AgencyCount")
        self.ConsortiumId = params.get("ConsortiumId")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.ChainStatus = params.get("ChainStatus")
        self.ResourceId = params.get("ResourceId")
        self.ClusterId = params.get("ClusterId")
        self.ConsortiumName = params.get("ConsortiumName")
        self.AgencyId = params.get("AgencyId")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.TotalNetworkNode = params.get("TotalNetworkNode")
        self.TotalCreateNode = params.get("TotalCreateNode")
        self.TotalGroups = params.get("TotalGroups")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelAuthorityIssuerRequest(AbstractModel):
    """CancelAuthorityIssuer request structure.

    """

    def __init__(self):
        r"""
        :param Did: The details of the DID.
        :type Did: str
        """
        self.Did = None


    def _deserialize(self, params):
        self.Did = params.get("Did")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelAuthorityIssuerResponse(AbstractModel):
    """CancelAuthorityIssuer response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CheckChainRequest(AbstractModel):
    """CheckChain request structure.

    """

    def __init__(self):
        r"""
        :param GroupId: The group ID.
        :type GroupId: int
        :param ClusterId: The network ID.
        :type ClusterId: str
        :param AgencyName: The name of the DID organization.
        :type AgencyName: str
        """
        self.GroupId = None
        self.ClusterId = None
        self.AgencyName = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.ClusterId = params.get("ClusterId")
        self.AgencyName = params.get("AgencyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckChainResponse(AbstractModel):
    """CheckChain response structure.

    """

    def __init__(self):
        r"""
        :param RoleType: Whether you are the owner of the consortium. `1`: Yes; `0`: No.
        :type RoleType: int
        :param ChainId: The chain ID.
        :type ChainId: str
        :param AppName: The application name.
        :type AppName: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RoleType = None
        self.ChainId = None
        self.AppName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RoleType = params.get("RoleType")
        self.ChainId = params.get("ChainId")
        self.AppName = params.get("AppName")
        self.RequestId = params.get("RequestId")


class CheckDidDeployRequest(AbstractModel):
    """CheckDidDeploy request structure.

    """

    def __init__(self):
        r"""
        :param TaskId: The task ID.
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckDidDeployResponse(AbstractModel):
    """CheckDidDeploy response structure.

    """

    def __init__(self):
        r"""
        :param Task: The service information.
        :type Task: :class:`tencentcloud.tdid.v20210519.models.Task`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Task = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Task") is not None:
            self.Task = Task()
            self.Task._deserialize(params.get("Task"))
        self.RequestId = params.get("RequestId")


class ConsortiumItem(AbstractModel):
    """The information of a consortium.

    """

    def __init__(self):
        r"""
        :param Id: The consortium ID.
        :type Id: int
        :param Name: The consortium name.
        :type Name: str
        """
        self.Id = None
        self.Name = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Contract(AbstractModel):
    """The information of a deployed contract.

    """

    def __init__(self):
        r"""
        :param ApplyName: The application name.
        :type ApplyName: str
        :param Enable: The contract status. `true`: Enabled; `false`: Not enabled.
        :type Enable: bool
        :param Hash: The CNS address of the contract.
        :type Hash: str
        :param HashShow: The desensitized CNS address.
        :type HashShow: str
        :param WeId: The DID of the organization that deployed the contract.
        :type WeId: str
        :param DeployName: The name of the organization that deployed the contract.
        :type DeployName: str
        :param GroupId: The group.
        :type GroupId: str
        :param CreateTime: The deployment time.
        :type CreateTime: str
        """
        self.ApplyName = None
        self.Enable = None
        self.Hash = None
        self.HashShow = None
        self.WeId = None
        self.DeployName = None
        self.GroupId = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.ApplyName = params.get("ApplyName")
        self.Enable = params.get("Enable")
        self.Hash = params.get("Hash")
        self.HashShow = params.get("HashShow")
        self.WeId = params.get("WeId")
        self.DeployName = params.get("DeployName")
        self.GroupId = params.get("GroupId")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CptIssueRank(AbstractModel):
    """Claim protocol type (CPT) rankings by the number of credentials issued.

    """

    def __init__(self):
        r"""
        :param CptName: The (claim protocol type) CPT name.
        :type CptName: str
        :param Rank: The ranking.
        :type Rank: int
        :param Count: The number of credentials issued.
        :type Count: int
        :param ApplyName: The application name.
        :type ApplyName: str
        :param ApplyId: The application ID.
        :type ApplyId: int
        """
        self.CptName = None
        self.Rank = None
        self.Count = None
        self.ApplyName = None
        self.ApplyId = None


    def _deserialize(self, params):
        self.CptName = params.get("CptName")
        self.Rank = params.get("Rank")
        self.Count = params.get("Count")
        self.ApplyName = params.get("ApplyName")
        self.ApplyId = params.get("ApplyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CptListData(AbstractModel):
    """The information of claim protocol types (CPT).

    """

    def __init__(self):
        r"""
        :param Id: The CPT ID.
        :type Id: int
        :param Name: The name of the claim protocol type (CPT).
        :type Name: str
        :param ClusterId: The network ID.
        :type ClusterId: str
        :param GroupId: The group ID.
        :type GroupId: int
        :param ServiceId: The service ID.
        :type ServiceId: int
        :param ContractAppId: The application ID of the contract.
        :type ContractAppId: int
        :param CptId: The claim protocol type (CPT) ID.
        :type CptId: int
        :param CptType: The type. `1`: System CPTs; `2`: Authorization CPTs; `3`: General CPTs
        :type CptType: int
        :param Description: The description of the claim protocol type (CPT).
        :type Description: str
        :param CptJson: The JSON file of the claim protocol type (CPT).
        :type CptJson: str
        :param CreateTime: The creation time.
        :type CreateTime: str
        :param UpdateTime: The last updated time.
        :type UpdateTime: str
        :param CreatorDid: The DID of the creator.
        :type CreatorDid: str
        :param AppName: The application name.
        :type AppName: str
        """
        self.Id = None
        self.Name = None
        self.ClusterId = None
        self.GroupId = None
        self.ServiceId = None
        self.ContractAppId = None
        self.CptId = None
        self.CptType = None
        self.Description = None
        self.CptJson = None
        self.CreateTime = None
        self.UpdateTime = None
        self.CreatorDid = None
        self.AppName = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        self.ServiceId = params.get("ServiceId")
        self.ContractAppId = params.get("ContractAppId")
        self.CptId = params.get("CptId")
        self.CptType = params.get("CptType")
        self.Description = params.get("Description")
        self.CptJson = params.get("CptJson")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.CreatorDid = params.get("CreatorDid")
        self.AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCredentialRequest(AbstractModel):
    """CreateCredential request structure.

    """

    def __init__(self):
        r"""
        :param FunctionArg: A parameter set. For details, see the example.
        :type FunctionArg: :class:`tencentcloud.tdid.v20210519.models.FunctionArg`
        :param TransactionArg: A parameter set. For details, see the example.
        :type TransactionArg: :class:`tencentcloud.tdid.v20210519.models.TransactionArg`
        :param VersionCredential: The version.
        :type VersionCredential: str
        :param UnSigned: Whether the credential is unsigned.
        :type UnSigned: bool
        """
        self.FunctionArg = None
        self.TransactionArg = None
        self.VersionCredential = None
        self.UnSigned = None


    def _deserialize(self, params):
        if params.get("FunctionArg") is not None:
            self.FunctionArg = FunctionArg()
            self.FunctionArg._deserialize(params.get("FunctionArg"))
        if params.get("TransactionArg") is not None:
            self.TransactionArg = TransactionArg()
            self.TransactionArg._deserialize(params.get("TransactionArg"))
        self.VersionCredential = params.get("VersionCredential")
        self.UnSigned = params.get("UnSigned")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCredentialResponse(AbstractModel):
    """CreateCredential response structure.

    """

    def __init__(self):
        r"""
        :param CredentialData: The information of the credential.
        :type CredentialData: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CredentialData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CredentialData = params.get("CredentialData")
        self.RequestId = params.get("RequestId")


class CreateDidServiceRequest(AbstractModel):
    """CreateDidService request structure.

    """

    def __init__(self):
        r"""
        :param ConsortiumName: The consortium name.
        :type ConsortiumName: str
        :param ConsortiumId: The consortium ID.
        :type ConsortiumId: int
        :param GroupId: The group ID.
        :type GroupId: int
        :param AgencyName: The organization name.
        :type AgencyName: str
        :param AppName: The application name.
        :type AppName: str
        :param ClusterId: The network ID.
        :type ClusterId: str
        :param GroupName: The group name.
        :type GroupName: str
        """
        self.ConsortiumName = None
        self.ConsortiumId = None
        self.GroupId = None
        self.AgencyName = None
        self.AppName = None
        self.ClusterId = None
        self.GroupName = None


    def _deserialize(self, params):
        self.ConsortiumName = params.get("ConsortiumName")
        self.ConsortiumId = params.get("ConsortiumId")
        self.GroupId = params.get("GroupId")
        self.AgencyName = params.get("AgencyName")
        self.AppName = params.get("AppName")
        self.ClusterId = params.get("ClusterId")
        self.GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDidServiceResponse(AbstractModel):
    """CreateDidService response structure.

    """

    def __init__(self):
        r"""
        :param Task: The service information.
        :type Task: :class:`tencentcloud.tdid.v20210519.models.Task`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Task = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Task") is not None:
            self.Task = Task()
            self.Task._deserialize(params.get("Task"))
        self.RequestId = params.get("RequestId")


class CreateLabelRequest(AbstractModel):
    """CreateLabel request structure.

    """

    def __init__(self):
        r"""
        :param LabelName: The label name.
        :type LabelName: str
        :param ClusterId: The network ID.
        :type ClusterId: str
        :param GroupId: The group ID.
        :type GroupId: int
        """
        self.LabelName = None
        self.ClusterId = None
        self.GroupId = None


    def _deserialize(self, params):
        self.LabelName = params.get("LabelName")
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLabelResponse(AbstractModel):
    """CreateLabel response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSelectiveCredentialRequest(AbstractModel):
    """CreateSelectiveCredential request structure.

    """

    def __init__(self):
        r"""
        :param FunctionArg: A parameter set.
        :type FunctionArg: :class:`tencentcloud.tdid.v20210519.models.VerifyFunctionArg`
        :param PolicyId: The disclosure policy ID.
        :type PolicyId: int
        """
        self.FunctionArg = None
        self.PolicyId = None


    def _deserialize(self, params):
        if params.get("FunctionArg") is not None:
            self.FunctionArg = VerifyFunctionArg()
            self.FunctionArg._deserialize(params.get("FunctionArg"))
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSelectiveCredentialResponse(AbstractModel):
    """CreateSelectiveCredential response structure.

    """

    def __init__(self):
        r"""
        :param CredentialData: The credential string.
        :type CredentialData: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CredentialData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CredentialData = params.get("CredentialData")
        self.RequestId = params.get("RequestId")


class CreateTDidByPrivateKeyRequest(AbstractModel):
    """CreateTDidByPrivateKey request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: The network ID.
        :type ClusterId: str
        :param GroupId: The group ID.
        :type GroupId: int
        :param PrivateKey: The private key.
        :type PrivateKey: str
        """
        self.ClusterId = None
        self.GroupId = None
        self.PrivateKey = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        self.PrivateKey = params.get("PrivateKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTDidByPrivateKeyResponse(AbstractModel):
    """CreateTDidByPrivateKey response structure.

    """

    def __init__(self):
        r"""
        :param Did: The DID.
        :type Did: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Did = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Did = params.get("Did")
        self.RequestId = params.get("RequestId")


class CreateTDidByPublicKeyRequest(AbstractModel):
    """CreateTDidByPublicKey request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: The network ID.
        :type ClusterId: str
        :param GroupId: The group ID.
        :type GroupId: int
        :param PublicKey: The public key.
        :type PublicKey: str
        :param EncryptPubKey: The encrypted public key.
        :type EncryptPubKey: str
        """
        self.ClusterId = None
        self.GroupId = None
        self.PublicKey = None
        self.EncryptPubKey = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        self.PublicKey = params.get("PublicKey")
        self.EncryptPubKey = params.get("EncryptPubKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTDidByPublicKeyResponse(AbstractModel):
    """CreateTDidByPublicKey response structure.

    """

    def __init__(self):
        r"""
        :param Did: The DID.
        :type Did: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Did = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Did = params.get("Did")
        self.RequestId = params.get("RequestId")


class CreateTDidRequest(AbstractModel):
    """CreateTDid request structure.

    """

    def __init__(self):
        r"""
        :param GroupId: The group ID.
        :type GroupId: int
        :param ClusterId: The network ID.
        :type ClusterId: str
        :param Relegation:  
        :type Relegation: int
        """
        self.GroupId = None
        self.ClusterId = None
        self.Relegation = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.ClusterId = params.get("ClusterId")
        self.Relegation = params.get("Relegation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTDidResponse(AbstractModel):
    """CreateTDid response structure.

    """

    def __init__(self):
        r"""
        :param Did: The DID.
        :type Did: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Did = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Did = params.get("Did")
        self.RequestId = params.get("RequestId")


class CredentialStatus(AbstractModel):
    """The on-chain status of the credential.

    """

    def __init__(self):
        r"""
        :param CredentialId: The credential ID.
        :type CredentialId: str
        :param Status: The credential status. `0`: Invalid; `1`: Valid.
        :type Status: int
        :param Issuer: The DID of the issuer.
        :type Issuer: str
        :param Digest: A summary of the credential.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Digest: str
        :param Signature: The credential signature.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Signature: str
        :param TimeStamp: The last updated timestamp.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TimeStamp: int
        """
        self.CredentialId = None
        self.Status = None
        self.Issuer = None
        self.Digest = None
        self.Signature = None
        self.TimeStamp = None


    def _deserialize(self, params):
        self.CredentialId = params.get("CredentialId")
        self.Status = params.get("Status")
        self.Issuer = params.get("Issuer")
        self.Digest = params.get("Digest")
        self.Signature = params.get("Signature")
        self.TimeStamp = params.get("TimeStamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployByNameRequest(AbstractModel):
    """DeployByName request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationName: The application name.
        :type ApplicationName: str
        :param ClusterId: The network ID.
        :type ClusterId: str
        :param GroupId: The group ID.
        :type GroupId: int
        """
        self.ApplicationName = None
        self.ClusterId = None
        self.GroupId = None


    def _deserialize(self, params):
        self.ApplicationName = params.get("ApplicationName")
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployByNameResponse(AbstractModel):
    """DeployByName response structure.

    """

    def __init__(self):
        r"""
        :param Hash: The hash value.
        :type Hash: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Hash = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Hash = params.get("Hash")
        self.RequestId = params.get("RequestId")


class DidCluster(AbstractModel):
    """The information of DID blockchain networks.

    """

    def __init__(self):
        r"""
        :param ChainId: The chain ID.
        :type ChainId: int
        :param ChainName: The chain name.
        :type ChainName: str
        :param AgencyCount: The number of organizations.
        :type AgencyCount: int
        :param ConsortiumId: The consortium ID.
        :type ConsortiumId: int
        :param CreateTime: The creation time.
        :type CreateTime: str
        :param ExpireTime: The expiration time.
        :type ExpireTime: str
        :param ChainStatus: The network status.
        :type ChainStatus: int
        :param ResourceId: The resource ID.
        :type ResourceId: str
        :param ClusterId: The network ID.
        :type ClusterId: str
        :param ConsortiumName: The consortium name.
        :type ConsortiumName: str
        :param AgencyId: The organization ID.
        :type AgencyId: int
        :param AutoRenewFlag: Whether auto-renewal is enabled.
        :type AutoRenewFlag: int
        :param TotalNetworkNode: The total number of network nodes.
        :type TotalNetworkNode: int
        :param TotalCreateNode: The number of nodes of the current organization.
        :type TotalCreateNode: int
        :param TotalGroups: The total number of groups.
        :type TotalGroups: int
        :param DidCount: The total number of DIDs.
        :type DidCount: int
        """
        self.ChainId = None
        self.ChainName = None
        self.AgencyCount = None
        self.ConsortiumId = None
        self.CreateTime = None
        self.ExpireTime = None
        self.ChainStatus = None
        self.ResourceId = None
        self.ClusterId = None
        self.ConsortiumName = None
        self.AgencyId = None
        self.AutoRenewFlag = None
        self.TotalNetworkNode = None
        self.TotalCreateNode = None
        self.TotalGroups = None
        self.DidCount = None


    def _deserialize(self, params):
        self.ChainId = params.get("ChainId")
        self.ChainName = params.get("ChainName")
        self.AgencyCount = params.get("AgencyCount")
        self.ConsortiumId = params.get("ConsortiumId")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.ChainStatus = params.get("ChainStatus")
        self.ResourceId = params.get("ResourceId")
        self.ClusterId = params.get("ClusterId")
        self.ConsortiumName = params.get("ConsortiumName")
        self.AgencyId = params.get("AgencyId")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.TotalNetworkNode = params.get("TotalNetworkNode")
        self.TotalCreateNode = params.get("TotalCreateNode")
        self.TotalGroups = params.get("TotalGroups")
        self.DidCount = params.get("DidCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DidData(AbstractModel):
    """The information of DIDs.

    """

    def __init__(self):
        r"""
        :param ServiceId: The service ID.
        :type ServiceId: int
        :param GroupId: The group ID.
        :type GroupId: int
        :param AppName: The application name.
        :type AppName: str
        :param Did: The DID.
        :type Did: str
        :param Remark: Remarks
        :type Remark: str
        :param AuthorityState: The status of the authority. `1`: Not registered; `2`: Not certified; `3`: Certified.
        :type AuthorityState: int
        :param LabelName: The label of the DID.
        :type LabelName: str
        :param CreatedAt: The DID creation time.
        :type CreatedAt: str
        :param ClusterId: The network ID.
        :type ClusterId: str
        :param AllianceName: The consortium name.
        :type AllianceName: str
        :param LabelId: The label ID.
        :type LabelId: int
        """
        self.ServiceId = None
        self.GroupId = None
        self.AppName = None
        self.Did = None
        self.Remark = None
        self.AuthorityState = None
        self.LabelName = None
        self.CreatedAt = None
        self.ClusterId = None
        self.AllianceName = None
        self.LabelId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.GroupId = params.get("GroupId")
        self.AppName = params.get("AppName")
        self.Did = params.get("Did")
        self.Remark = params.get("Remark")
        self.AuthorityState = params.get("AuthorityState")
        self.LabelName = params.get("LabelName")
        self.CreatedAt = params.get("CreatedAt")
        self.ClusterId = params.get("ClusterId")
        self.AllianceName = params.get("AllianceName")
        self.LabelId = params.get("LabelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DidServiceInfo(AbstractModel):
    """The DID service information.

    """

    def __init__(self):
        r"""
        :param Id: The DID service ID.
        :type Id: int
        :param Appid: The application ID.
        :type Appid: int
        :param Uin: The account ID.
        :type Uin: str
        :param ConsortiumId: The consortium ID.
        :type ConsortiumId: int
        :param ConsortiumName: The consortium name.
        :type ConsortiumName: str
        :param ClusterId: The network ID.
        :type ClusterId: str
        :param GroupId: The group ID.
        :type GroupId: int
        :param ChainId: The chain ID.
        :type ChainId: str
        :param RoleType: Whether you are the owner of the consortium. `1`: Yes; `0`: No.
        :type RoleType: int
        :param AgencyDid: The organization DID.
        :type AgencyDid: str
        :param CreateOrg: The organization name.
        :type CreateOrg: str
        :param Endpoint: The endpoint.
        :type Endpoint: str
        :param CreateTime: The creation time.
        :type CreateTime: str
        :param UpdateTime: The last updated time.
        :type UpdateTime: str
        :param GroupName: The group name.
        :type GroupName: str
        """
        self.Id = None
        self.Appid = None
        self.Uin = None
        self.ConsortiumId = None
        self.ConsortiumName = None
        self.ClusterId = None
        self.GroupId = None
        self.ChainId = None
        self.RoleType = None
        self.AgencyDid = None
        self.CreateOrg = None
        self.Endpoint = None
        self.CreateTime = None
        self.UpdateTime = None
        self.GroupName = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Appid = params.get("Appid")
        self.Uin = params.get("Uin")
        self.ConsortiumId = params.get("ConsortiumId")
        self.ConsortiumName = params.get("ConsortiumName")
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        self.ChainId = params.get("ChainId")
        self.RoleType = params.get("RoleType")
        self.AgencyDid = params.get("AgencyDid")
        self.CreateOrg = params.get("CreateOrg")
        self.Endpoint = params.get("Endpoint")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownCptRequest(AbstractModel):
    """DownCpt request structure.

    """

    def __init__(self):
        r"""
        :param CptIndex: The claim protocol type (CPT) index.
        :type CptIndex: int
        """
        self.CptIndex = None


    def _deserialize(self, params):
        self.CptIndex = params.get("CptIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownCptResponse(AbstractModel):
    """DownCpt response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableHashRequest(AbstractModel):
    """EnableHash request structure.

    """

    def __init__(self):
        r"""
        :param Hash: The CNS address of the contract.
        :type Hash: str
        """
        self.Hash = None


    def _deserialize(self, params):
        self.Hash = params.get("Hash")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableHashResponse(AbstractModel):
    """EnableHash response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class FunctionArg(AbstractModel):
    """The input parameters for creating a credential.

    """

    def __init__(self):
        r"""
        :param CptId: The claim protocol type (CPT) ID.
        :type CptId: int
        :param Issuer: The DID of the issuer.
        :type Issuer: str
        :param ExpirationDate: The expiration time.
        :type ExpirationDate: str
        :param ClaimJson: The claim.
        :type ClaimJson: str
        """
        self.CptId = None
        self.Issuer = None
        self.ExpirationDate = None
        self.ClaimJson = None


    def _deserialize(self, params):
        self.CptId = params.get("CptId")
        self.Issuer = params.get("Issuer")
        self.ExpirationDate = params.get("ExpirationDate")
        self.ClaimJson = params.get("ClaimJson")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAgencyTDidRequest(AbstractModel):
    """GetAgencyTDid request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: The network ID.
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAgencyTDidResponse(AbstractModel):
    """GetAgencyTDid response structure.

    """

    def __init__(self):
        r"""
        :param Prefix: The prefix (fixed).
        :type Prefix: str
        :param Identity: The details of the DID.
        :type Identity: list of Identity
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Prefix = None
        self.Identity = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Prefix = params.get("Prefix")
        if params.get("Identity") is not None:
            self.Identity = []
            for item in params.get("Identity"):
                obj = Identity()
                obj._deserialize(item)
                self.Identity.append(obj)
        self.RequestId = params.get("RequestId")


class GetAuthoritiesListRequest(AbstractModel):
    """GetAuthoritiesList request structure.

    """

    def __init__(self):
        r"""
        :param PageNumber: The page number, beginning from 1.
        :type PageNumber: int
        :param PageSize: The number of records per page.
        :type PageSize: int
        :param Did: The DID.
        :type Did: str
        :param Status: Whether to query certified or uncertified authorities. `1`: Certified; `2`: Uncertified.
        :type Status: int
        """
        self.PageNumber = None
        self.PageSize = None
        self.Did = None
        self.Status = None


    def _deserialize(self, params):
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        self.Did = params.get("Did")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAuthoritiesListResponse(AbstractModel):
    """GetAuthoritiesList response structure.

    """

    def __init__(self):
        r"""
        :param ResultList: A data set.
        :type ResultList: list of Authority
        :param AllCount: The total number of records.
        :type AllCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ResultList = None
        self.AllCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResultList") is not None:
            self.ResultList = []
            for item in params.get("ResultList"):
                obj = Authority()
                obj._deserialize(item)
                self.ResultList.append(obj)
        self.AllCount = params.get("AllCount")
        self.RequestId = params.get("RequestId")


class GetAuthorityIssuerRequest(AbstractModel):
    """GetAuthorityIssuer request structure.

    """

    def __init__(self):
        r"""
        :param Did: The DID.
        :type Did: str
        """
        self.Did = None


    def _deserialize(self, params):
        self.Did = params.get("Did")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAuthorityIssuerResponse(AbstractModel):
    """GetAuthorityIssuer response structure.

    """

    def __init__(self):
        r"""
        :param Name: The authority name.
        :type Name: str
        :param ClusterId: The blockchain network ID.
        :type ClusterId: str
        :param GroupId: The blockchain group ID.
        :type GroupId: int
        :param Did: The DID of the authority.
        :type Did: str
        :param Remark: Remarks.
        :type Remark: str
        :param RegisterTime: The registration time.
        :type RegisterTime: str
        :param RecognizeTime: The recognition time.
        :type RecognizeTime: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Name = None
        self.ClusterId = None
        self.GroupId = None
        self.Did = None
        self.Remark = None
        self.RegisterTime = None
        self.RecognizeTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        self.Did = params.get("Did")
        self.Remark = params.get("Remark")
        self.RegisterTime = params.get("RegisterTime")
        self.RecognizeTime = params.get("RecognizeTime")
        self.RequestId = params.get("RequestId")


class GetConsortiumClusterListRequest(AbstractModel):
    """GetConsortiumClusterList request structure.

    """

    def __init__(self):
        r"""
        :param ConsortiumId: The consortium ID.
        :type ConsortiumId: int
        """
        self.ConsortiumId = None


    def _deserialize(self, params):
        self.ConsortiumId = params.get("ConsortiumId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetConsortiumClusterListResponse(AbstractModel):
    """GetConsortiumClusterList response structure.

    """

    def __init__(self):
        r"""
        :param ClusterList: A list of networks.
        :type ClusterList: list of BcosClusterItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ClusterList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClusterList") is not None:
            self.ClusterList = []
            for item in params.get("ClusterList"):
                obj = BcosClusterItem()
                obj._deserialize(item)
                self.ClusterList.append(obj)
        self.RequestId = params.get("RequestId")


class GetConsortiumListRequest(AbstractModel):
    """GetConsortiumList request structure.

    """


class GetConsortiumListResponse(AbstractModel):
    """GetConsortiumList response structure.

    """

    def __init__(self):
        r"""
        :param ConsortiumList: A list of the consortiums.
        :type ConsortiumList: list of ConsortiumItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ConsortiumList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ConsortiumList") is not None:
            self.ConsortiumList = []
            for item in params.get("ConsortiumList"):
                obj = ConsortiumItem()
                obj._deserialize(item)
                self.ConsortiumList.append(obj)
        self.RequestId = params.get("RequestId")


class GetCptInfoRequest(AbstractModel):
    """GetCptInfo request structure.

    """

    def __init__(self):
        r"""
        :param CptIndex: The claim protocol type (CPT) index.
        :type CptIndex: int
        """
        self.CptIndex = None


    def _deserialize(self, params):
        self.CptIndex = params.get("CptIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCptInfoResponse(AbstractModel):
    """GetCptInfo response structure.

    """

    def __init__(self):
        r"""
        :param CptJsonData: The JSON data of the claim protocol type (CPT).
        :type CptJsonData: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CptJsonData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CptJsonData = params.get("CptJsonData")
        self.RequestId = params.get("RequestId")


class GetCptListRequest(AbstractModel):
    """GetCptList request structure.

    """

    def __init__(self):
        r"""
        :param DisplayStart: The start.
        :type DisplayStart: int
        :param DisplayLength: The maximum number of records to return.
        :type DisplayLength: int
        :param CptType: The type. `0`: All CPTs; `1`: System CPTs; `2`: Authorization CPTs; `3`: General CPTs
        :type CptType: int
        """
        self.DisplayStart = None
        self.DisplayLength = None
        self.CptType = None


    def _deserialize(self, params):
        self.DisplayStart = params.get("DisplayStart")
        self.DisplayLength = params.get("DisplayLength")
        self.CptType = params.get("CptType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCptListResponse(AbstractModel):
    """GetCptList response structure.

    """

    def __init__(self):
        r"""
        :param CptDataList: The information of claim protocol types (CPT).
        :type CptDataList: list of CptListData
        :param AllCount: The total number of claim protocol types (CPT).
        :type AllCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CptDataList = None
        self.AllCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CptDataList") is not None:
            self.CptDataList = []
            for item in params.get("CptDataList"):
                obj = CptListData()
                obj._deserialize(item)
                self.CptDataList.append(obj)
        self.AllCount = params.get("AllCount")
        self.RequestId = params.get("RequestId")


class GetCredentialCptRankRequest(AbstractModel):
    """GetCredentialCptRank request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start date (as early as 2021-4-23).
        :type StartTime: str
        :param EndTime: The end date (as early as 2021-4-23).
        :type EndTime: str
        :param ClusterId: The network ID.
        :type ClusterId: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCredentialCptRankResponse(AbstractModel):
    """GetCredentialCptRank response structure.

    """

    def __init__(self):
        r"""
        :param RankIssueResult: The rankings.
        :type RankIssueResult: list of CptIssueRank
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RankIssueResult = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RankIssueResult") is not None:
            self.RankIssueResult = []
            for item in params.get("RankIssueResult"):
                obj = CptIssueRank()
                obj._deserialize(item)
                self.RankIssueResult.append(obj)
        self.RequestId = params.get("RequestId")


class GetCredentialIssueRankRequest(AbstractModel):
    """GetCredentialIssueRank request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start date (as early as 2021-4-23).
        :type StartTime: str
        :param EndTime: The end date (as early as 2021-4-23).
        :type EndTime: str
        :param ClusterId: The network ID.
        :type ClusterId: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCredentialIssueRankResponse(AbstractModel):
    """GetCredentialIssueRank response structure.

    """

    def __init__(self):
        r"""
        :param RankIssueResult: The rankings.
        :type RankIssueResult: list of CptIssueRank
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RankIssueResult = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RankIssueResult") is not None:
            self.RankIssueResult = []
            for item in params.get("RankIssueResult"):
                obj = CptIssueRank()
                obj._deserialize(item)
                self.RankIssueResult.append(obj)
        self.RequestId = params.get("RequestId")


class GetCredentialIssueTrendRequest(AbstractModel):
    """GetCredentialIssueTrend request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start date (as early as 2021-4-23).
        :type StartTime: str
        :param EndTime: The end date (as early as 2021-4-23).
        :type EndTime: str
        :param ClusterId: The network ID.
        :type ClusterId: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCredentialIssueTrendResponse(AbstractModel):
    """GetCredentialIssueTrend response structure.

    """

    def __init__(self):
        r"""
        :param Trend: The trend information.
        :type Trend: list of Trend
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Trend = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Trend") is not None:
            self.Trend = []
            for item in params.get("Trend"):
                obj = Trend()
                obj._deserialize(item)
                self.Trend.append(obj)
        self.RequestId = params.get("RequestId")


class GetCredentialStatusRequest(AbstractModel):
    """GetCredentialStatus request structure.

    """

    def __init__(self):
        r"""
        :param CredentialId: The credential ID.
        :type CredentialId: str
        """
        self.CredentialId = None


    def _deserialize(self, params):
        self.CredentialId = params.get("CredentialId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCredentialStatusResponse(AbstractModel):
    """GetCredentialStatus response structure.

    """

    def __init__(self):
        r"""
        :param CredentialStatus: The credential status.
        :type CredentialStatus: :class:`tencentcloud.tdid.v20210519.models.CredentialStatus`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CredentialStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CredentialStatus") is not None:
            self.CredentialStatus = CredentialStatus()
            self.CredentialStatus._deserialize(params.get("CredentialStatus"))
        self.RequestId = params.get("RequestId")


class GetDataPanelRequest(AbstractModel):
    """GetDataPanel request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: The network ID.
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDataPanelResponse(AbstractModel):
    """GetDataPanel response structure.

    """

    def __init__(self):
        r"""
        :param BlockNetworkCount: The number of blockchain networks.
        :type BlockNetworkCount: int
        :param BlockNetworkName: The blockchain network name.
        :type BlockNetworkName: str
        :param BlockHeight: The current block height.
        :type BlockHeight: int
        :param BlockNetworkType: The blockchain network type.
        :type BlockNetworkType: int
        :param DidCount: The number of DIDs.
        :type DidCount: int
        :param CptCount: The number of claim protocol types (CPT).
        :type CptCount: int
        :param CertificatedAuthCount: The number of certified authorities.
        :type CertificatedAuthCount: int
        :param IssueCptCount: The number of credentials issued.
        :type IssueCptCount: int
        :param NewDidCount: The number of new DIDs in the current week.
        :type NewDidCount: int
        :param BcosCount: The number of BCOS networks.
        :type BcosCount: int
        :param FabricCount: The number of Fabric networks.
        :type FabricCount: int
        :param ChainMakerCount: The number of ChainMaker networks.
        :type ChainMakerCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.BlockNetworkCount = None
        self.BlockNetworkName = None
        self.BlockHeight = None
        self.BlockNetworkType = None
        self.DidCount = None
        self.CptCount = None
        self.CertificatedAuthCount = None
        self.IssueCptCount = None
        self.NewDidCount = None
        self.BcosCount = None
        self.FabricCount = None
        self.ChainMakerCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BlockNetworkCount = params.get("BlockNetworkCount")
        self.BlockNetworkName = params.get("BlockNetworkName")
        self.BlockHeight = params.get("BlockHeight")
        self.BlockNetworkType = params.get("BlockNetworkType")
        self.DidCount = params.get("DidCount")
        self.CptCount = params.get("CptCount")
        self.CertificatedAuthCount = params.get("CertificatedAuthCount")
        self.IssueCptCount = params.get("IssueCptCount")
        self.NewDidCount = params.get("NewDidCount")
        self.BcosCount = params.get("BcosCount")
        self.FabricCount = params.get("FabricCount")
        self.ChainMakerCount = params.get("ChainMakerCount")
        self.RequestId = params.get("RequestId")


class GetDeployInfoRequest(AbstractModel):
    """GetDeployInfo request structure.

    """

    def __init__(self):
        r"""
        :param Hash: The CNS address of the contract.
        :type Hash: str
        """
        self.Hash = None


    def _deserialize(self, params):
        self.Hash = params.get("Hash")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeployInfoResponse(AbstractModel):
    """GetDeployInfo response structure.

    """

    def __init__(self):
        r"""
        :param Hash: The CNS address of the contract.
        :type Hash: str
        :param GroupId: The main group ID of the contract.
        :type GroupId: str
        :param DeployDid: The DID of the organization that deployed the contract.
        :type DeployDid: str
        :param SdkVersion: The TDID SDK version.
        :type SdkVersion: str
        :param ContractVersion: The TDID contract version.
        :type ContractVersion: str
        :param BlockVersion: The blockchain node version.
        :type BlockVersion: str
        :param BlockIp: The IP address of the blockchain node.
        :type BlockIp: str
        :param DidAddress: The address of the DID contract.
        :type DidAddress: str
        :param CptAddress: The address of the claim protocol type (CPT) contract.
        :type CptAddress: str
        :param AuthorityAddress: The address of the authority.
        :type AuthorityAddress: str
        :param EvidenceAddress: The evidence contract address.
        :type EvidenceAddress: str
        :param SpecificAddress: The contract address of the specific issuer.
        :type SpecificAddress: str
        :param ChainId: The chain ID.
        :type ChainId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Hash = None
        self.GroupId = None
        self.DeployDid = None
        self.SdkVersion = None
        self.ContractVersion = None
        self.BlockVersion = None
        self.BlockIp = None
        self.DidAddress = None
        self.CptAddress = None
        self.AuthorityAddress = None
        self.EvidenceAddress = None
        self.SpecificAddress = None
        self.ChainId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Hash = params.get("Hash")
        self.GroupId = params.get("GroupId")
        self.DeployDid = params.get("DeployDid")
        self.SdkVersion = params.get("SdkVersion")
        self.ContractVersion = params.get("ContractVersion")
        self.BlockVersion = params.get("BlockVersion")
        self.BlockIp = params.get("BlockIp")
        self.DidAddress = params.get("DidAddress")
        self.CptAddress = params.get("CptAddress")
        self.AuthorityAddress = params.get("AuthorityAddress")
        self.EvidenceAddress = params.get("EvidenceAddress")
        self.SpecificAddress = params.get("SpecificAddress")
        self.ChainId = params.get("ChainId")
        self.RequestId = params.get("RequestId")


class GetDeployListRequest(AbstractModel):
    """GetDeployList request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: The network ID.
        :type ClusterId: str
        :param GroupId: The group ID.
        :type GroupId: int
        :param DisplayStart: The start.
        :type DisplayStart: int
        :param DisplayLength: The maximum number of records to return.
        :type DisplayLength: int
        """
        self.ClusterId = None
        self.GroupId = None
        self.DisplayStart = None
        self.DisplayLength = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        self.DisplayStart = params.get("DisplayStart")
        self.DisplayLength = params.get("DisplayLength")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeployListResponse(AbstractModel):
    """GetDeployList response structure.

    """

    def __init__(self):
        r"""
        :param AllCount: The total number of contracts.
        :type AllCount: int
        :param Result: A list of deployed contracts.
        :type Result: list of Contract
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AllCount = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AllCount = params.get("AllCount")
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = Contract()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class GetDidClusterDetailRequest(AbstractModel):
    """GetDidClusterDetail request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: The DID network ID.
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDidClusterDetailResponse(AbstractModel):
    """GetDidClusterDetail response structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: The network ID.
        :type ClusterId: str
        :param ConsortiumName: The consortium name.
        :type ConsortiumName: str
        :param ChainAgency: The name of the blockchain organization.
        :type ChainAgency: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ClusterId = None
        self.ConsortiumName = None
        self.ChainAgency = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ConsortiumName = params.get("ConsortiumName")
        self.ChainAgency = params.get("ChainAgency")
        self.RequestId = params.get("RequestId")


class GetDidClusterListRequest(AbstractModel):
    """GetDidClusterList request structure.

    """


class GetDidClusterListResponse(AbstractModel):
    """GetDidClusterList response structure.

    """

    def __init__(self):
        r"""
        :param DidClusterList: A list of the DID networks.
        :type DidClusterList: list of DidCluster
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DidClusterList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DidClusterList") is not None:
            self.DidClusterList = []
            for item in params.get("DidClusterList"):
                obj = DidCluster()
                obj._deserialize(item)
                self.DidClusterList.append(obj)
        self.RequestId = params.get("RequestId")


class GetDidDetailRequest(AbstractModel):
    """GetDidDetail request structure.

    """

    def __init__(self):
        r"""
        :param Did: The DID.
        :type Did: str
        """
        self.Did = None


    def _deserialize(self, params):
        self.Did = params.get("Did")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDidDetailResponse(AbstractModel):
    """GetDidDetail response structure.

    """

    def __init__(self):
        r"""
        :param Did: The DID.
        :type Did: str
        :param Remark: Remarks
        :type Remark: str
        :param PublicKey: The public key.
        :type PublicKey: str
        :param AuthorityState: Whether the DID is a certified authority.
        :type AuthorityState: int
        :param ConsortiumId: The consortium ID.
        :type ConsortiumId: int
        :param ConsortiumName: The consortium name.
        :type ConsortiumName: str
        :param GroupId: The group ID.
        :type GroupId: int
        :param ClusterId: The network ID.
        :type ClusterId: str
        :param ResChainId: The BCOS resource ID.
        :type ResChainId: str
        :param CreateTime: The creation time.
        :type CreateTime: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Did = None
        self.Remark = None
        self.PublicKey = None
        self.AuthorityState = None
        self.ConsortiumId = None
        self.ConsortiumName = None
        self.GroupId = None
        self.ClusterId = None
        self.ResChainId = None
        self.CreateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Did = params.get("Did")
        self.Remark = params.get("Remark")
        self.PublicKey = params.get("PublicKey")
        self.AuthorityState = params.get("AuthorityState")
        self.ConsortiumId = params.get("ConsortiumId")
        self.ConsortiumName = params.get("ConsortiumName")
        self.GroupId = params.get("GroupId")
        self.ClusterId = params.get("ClusterId")
        self.ResChainId = params.get("ResChainId")
        self.CreateTime = params.get("CreateTime")
        self.RequestId = params.get("RequestId")


class GetDidDocumentRequest(AbstractModel):
    """GetDidDocument request structure.

    """

    def __init__(self):
        r"""
        :param Did: The DID.
        :type Did: str
        """
        self.Did = None


    def _deserialize(self, params):
        self.Did = params.get("Did")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDidDocumentResponse(AbstractModel):
    """GetDidDocument response structure.

    """

    def __init__(self):
        r"""
        :param Name: The name.
        :type Name: str
        :param Document: The DID document.
        :type Document: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Name = None
        self.Document = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Document = params.get("Document")
        self.RequestId = params.get("RequestId")


class GetDidListRequest(AbstractModel):
    """GetDidList request structure.

    """

    def __init__(self):
        r"""
        :param PageSize: The number of records per page.
        :type PageSize: int
        :param PageNumber: The page number, beginning from 1.
        :type PageNumber: int
        :param Did: The DID.
        :type Did: str
        :param ClusterId: The network ID.
        :type ClusterId: str
        :param GroupId: The group ID.
        :type GroupId: int
        """
        self.PageSize = None
        self.PageNumber = None
        self.Did = None
        self.ClusterId = None
        self.GroupId = None


    def _deserialize(self, params):
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        self.Did = params.get("Did")
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDidListResponse(AbstractModel):
    """GetDidList response structure.

    """

    def __init__(self):
        r"""
        :param DataList: A list of DIDs.
        :type DataList: list of DidData
        :param AllCount: The total number of records.
        :type AllCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DataList = None
        self.AllCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataList") is not None:
            self.DataList = []
            for item in params.get("DataList"):
                obj = DidData()
                obj._deserialize(item)
                self.DataList.append(obj)
        self.AllCount = params.get("AllCount")
        self.RequestId = params.get("RequestId")


class GetDidRegisterTrendRequest(AbstractModel):
    """GetDidRegisterTrend request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start date (as early as 2021-4-23).
        :type StartTime: str
        :param EndTime: The end date (as early as 2021-4-23).
        :type EndTime: str
        :param ClusterId: The network ID.
        :type ClusterId: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDidRegisterTrendResponse(AbstractModel):
    """GetDidRegisterTrend response structure.

    """

    def __init__(self):
        r"""
        :param Trend: The trend information.
        :type Trend: list of Trend
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Trend = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Trend") is not None:
            self.Trend = []
            for item in params.get("Trend"):
                obj = Trend()
                obj._deserialize(item)
                self.Trend.append(obj)
        self.RequestId = params.get("RequestId")


class GetDidServiceDetailRequest(AbstractModel):
    """GetDidServiceDetail request structure.

    """

    def __init__(self):
        r"""
        :param ServiceId: The DID service ID.
        :type ServiceId: int
        """
        self.ServiceId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDidServiceDetailResponse(AbstractModel):
    """GetDidServiceDetail response structure.

    """

    def __init__(self):
        r"""
        :param DidService: The DID service information.
        :type DidService: :class:`tencentcloud.tdid.v20210519.models.DidServiceInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DidService = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DidService") is not None:
            self.DidService = DidServiceInfo()
            self.DidService._deserialize(params.get("DidService"))
        self.RequestId = params.get("RequestId")


class GetDidServiceListRequest(AbstractModel):
    """GetDidServiceList request structure.

    """

    def __init__(self):
        r"""
        :param Type: `1`: Return results at the network level; `0`: Return results at the service level.
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
        


class GetDidServiceListResponse(AbstractModel):
    """GetDidServiceList response structure.

    """

    def __init__(self):
        r"""
        :param DidServiceList: A list of DID services.
        :type DidServiceList: list of DidServiceInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DidServiceList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DidServiceList") is not None:
            self.DidServiceList = []
            for item in params.get("DidServiceList"):
                obj = DidServiceInfo()
                obj._deserialize(item)
                self.DidServiceList.append(obj)
        self.RequestId = params.get("RequestId")


class GetGroupListRequest(AbstractModel):
    """GetGroupList request structure.

    """

    def __init__(self):
        r"""
        :param Status: `0`: Groups with no DID services; `1`: Groups with DID services.
        :type Status: int
        :param ClusterId: The network ID.
        :type ClusterId: str
        """
        self.Status = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGroupListResponse(AbstractModel):
    """GetGroupList response structure.

    """

    def __init__(self):
        r"""
        :param Result: A list of groups.
        :type Result: list of Group
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = Group()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class GetLabelListRequest(AbstractModel):
    """GetLabelList request structure.

    """

    def __init__(self):
        r"""
        :param PageSize: The number of records per page.
        :type PageSize: int
        :param PageNumber: The page number, beginning from 1.
        :type PageNumber: int
        :param ClusterId: The network ID.
        :type ClusterId: str
        :param GroupId: The group ID.
        :type GroupId: int
        """
        self.PageSize = None
        self.PageNumber = None
        self.ClusterId = None
        self.GroupId = None


    def _deserialize(self, params):
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetLabelListResponse(AbstractModel):
    """GetLabelList response structure.

    """

    def __init__(self):
        r"""
        :param Result: A data set.
        :type Result: list of Label
        :param TotalCount: The total number of records.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = Label()
                obj._deserialize(item)
                self.Result.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class GetPolicyListRequest(AbstractModel):
    """GetPolicyList request structure.

    """

    def __init__(self):
        r"""
        :param DisplayStart: The start.
        :type DisplayStart: int
        :param DisplayLength: The maximum number of records to return.
        :type DisplayLength: int
        """
        self.DisplayStart = None
        self.DisplayLength = None


    def _deserialize(self, params):
        self.DisplayStart = params.get("DisplayStart")
        self.DisplayLength = params.get("DisplayLength")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPolicyListResponse(AbstractModel):
    """GetPolicyList response structure.

    """

    def __init__(self):
        r"""
        :param PolicyDataList: A list of disclosure policies.
        :type PolicyDataList: list of Policy
        :param AllCount: The total number of records.
        :type AllCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PolicyDataList = None
        self.AllCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PolicyDataList") is not None:
            self.PolicyDataList = []
            for item in params.get("PolicyDataList"):
                obj = Policy()
                obj._deserialize(item)
                self.PolicyDataList.append(obj)
        self.AllCount = params.get("AllCount")
        self.RequestId = params.get("RequestId")


class GetPublicKeyRequest(AbstractModel):
    """GetPublicKey request structure.

    """

    def __init__(self):
        r"""
        :param Did: The DID.
        :type Did: str
        """
        self.Did = None


    def _deserialize(self, params):
        self.Did = params.get("Did")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPublicKeyResponse(AbstractModel):
    """GetPublicKey response structure.

    """

    def __init__(self):
        r"""
        :param Did: The DID.
        :type Did: str
        :param PublicKey: The public key.
        :type PublicKey: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Did = None
        self.PublicKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Did = params.get("Did")
        self.PublicKey = params.get("PublicKey")
        self.RequestId = params.get("RequestId")


class Group(AbstractModel):
    """The group information.

    """

    def __init__(self):
        r"""
        :param GroupId: The group ID.
        :type GroupId: int
        :param NodeCount: The number of nodes.
        :type NodeCount: int
        :param NodeCountOfAgency: The number of nodes of the organization.
        :type NodeCountOfAgency: int
        :param Description: The description of the group.
        :type Description: str
        :param RoleType: Whether you are the owner of the consortium or not.
        :type RoleType: int
        :param ChainId: The chain ID.
        :type ChainId: str
        """
        self.GroupId = None
        self.NodeCount = None
        self.NodeCountOfAgency = None
        self.Description = None
        self.RoleType = None
        self.ChainId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.NodeCount = params.get("NodeCount")
        self.NodeCountOfAgency = params.get("NodeCountOfAgency")
        self.Description = params.get("Description")
        self.RoleType = params.get("RoleType")
        self.ChainId = params.get("ChainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Identity(AbstractModel):
    """The details of the DID.

    """

    def __init__(self):
        r"""
        :param AccountIdentifier: The account identifier.
        :type AccountIdentifier: str
        :param ChainID: The chain ID.
        :type ChainID: str
        :param Did: The DID.
        :type Did: str
        :param GroupId: The group ID.
        :type GroupId: int
        :param GroupName: The group name.
        :type GroupName: str
        """
        self.AccountIdentifier = None
        self.ChainID = None
        self.Did = None
        self.GroupId = None
        self.GroupName = None


    def _deserialize(self, params):
        self.AccountIdentifier = params.get("AccountIdentifier")
        self.ChainID = params.get("ChainID")
        self.Did = params.get("Did")
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Label(AbstractModel):
    """The label information.

    """

    def __init__(self):
        r"""
        :param LabelId: The label ID.
        :type LabelId: int
        :param LabelName: The label name.
        :type LabelName: str
        :param DidCount: The number of DIDs.
        :type DidCount: int
        :param Did: The DID of the creator.
        :type Did: str
        :param ClusterId: The network ID.
        :type ClusterId: str
        :param CreateTime: The creation time.
        :type CreateTime: str
        :param GroupId: The group ID.
        :type GroupId: int
        """
        self.LabelId = None
        self.LabelName = None
        self.DidCount = None
        self.Did = None
        self.ClusterId = None
        self.CreateTime = None
        self.GroupId = None


    def _deserialize(self, params):
        self.LabelId = params.get("LabelId")
        self.LabelName = params.get("LabelName")
        self.DidCount = params.get("DidCount")
        self.Did = params.get("Did")
        self.ClusterId = params.get("ClusterId")
        self.CreateTime = params.get("CreateTime")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Policy(AbstractModel):
    """The policy information.

    """

    def __init__(self):
        r"""
        :param Id: The policy index.
        :type Id: int
        :param Name: The policy name.
        :type Name: str
        :param ClusterId: The network ID.
        :type ClusterId: str
        :param GroupId: The group ID.
        :type GroupId: int
        :param ServiceId: The service ID.
        :type ServiceId: int
        :param ContractAppId: The application ID of the contract.
        :type ContractAppId: int
        :param PolicyId: The policy ID.
        :type PolicyId: int
        :param CptId: The claim protocol type (CPT) ID.
        :type CptId: int
        :param PolicyJson: The JSON data.
        :type PolicyJson: str
        :param CreateTime: The creation time.
        :type CreateTime: str
        :param UpdateTime: The last updated time.
        :type UpdateTime: str
        :param CreatorDid: The DID of the creator.
        :type CreatorDid: str
        :param AppName: The application name.
        :type AppName: str
        :param CptIndex: The claim protocol type (CPT) index.
        :type CptIndex: int
        """
        self.Id = None
        self.Name = None
        self.ClusterId = None
        self.GroupId = None
        self.ServiceId = None
        self.ContractAppId = None
        self.PolicyId = None
        self.CptId = None
        self.PolicyJson = None
        self.CreateTime = None
        self.UpdateTime = None
        self.CreatorDid = None
        self.AppName = None
        self.CptIndex = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        self.ServiceId = params.get("ServiceId")
        self.ContractAppId = params.get("ContractAppId")
        self.PolicyId = params.get("PolicyId")
        self.CptId = params.get("CptId")
        self.PolicyJson = params.get("PolicyJson")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.CreatorDid = params.get("CreatorDid")
        self.AppName = params.get("AppName")
        self.CptIndex = params.get("CptIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Proof(AbstractModel):
    """The credential signature.

    """

    def __init__(self):
        r"""
        :param Created: The creation time.
        :type Created: int
        :param Creator: The DID of the creator.
        :type Creator: str
        :param SaltJson: The salt value.
        :type SaltJson: str
        :param SignatureValue: The signature.
        :type SignatureValue: str
        :param Type: The type.
        :type Type: str
        """
        self.Created = None
        self.Creator = None
        self.SaltJson = None
        self.SignatureValue = None
        self.Type = None


    def _deserialize(self, params):
        self.Created = params.get("Created")
        self.Creator = params.get("Creator")
        self.SaltJson = params.get("SaltJson")
        self.SignatureValue = params.get("SignatureValue")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryPolicyRequest(AbstractModel):
    """QueryPolicy request structure.

    """

    def __init__(self):
        r"""
        :param PolicyIndex: The policy index.
        :type PolicyIndex: int
        """
        self.PolicyIndex = None


    def _deserialize(self, params):
        self.PolicyIndex = params.get("PolicyIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryPolicyResponse(AbstractModel):
    """QueryPolicy response structure.

    """

    def __init__(self):
        r"""
        :param Id: The policy index.
        :type Id: int
        :param PolicyId: The policy ID.
        :type PolicyId: int
        :param CptId: The claim protocol type (CPT) ID.
        :type CptId: int
        :param PolicyData: The content of the policy.
        :type PolicyData: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.PolicyId = None
        self.CptId = None
        self.PolicyData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.PolicyId = params.get("PolicyId")
        self.CptId = params.get("CptId")
        self.PolicyData = params.get("PolicyData")
        self.RequestId = params.get("RequestId")


class RecognizeAuthorityIssuerRequest(AbstractModel):
    """RecognizeAuthorityIssuer request structure.

    """

    def __init__(self):
        r"""
        :param Did: The DID.
        :type Did: str
        """
        self.Did = None


    def _deserialize(self, params):
        self.Did = params.get("Did")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeAuthorityIssuerResponse(AbstractModel):
    """RecognizeAuthorityIssuer response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegisterClaimPolicyRequest(AbstractModel):
    """RegisterClaimPolicy request structure.

    """

    def __init__(self):
        r"""
        :param CptIndex: The claim protocol type (CPT) index.
        :type CptIndex: int
        :param Policy: The disclosure policy.
        :type Policy: str
        """
        self.CptIndex = None
        self.Policy = None


    def _deserialize(self, params):
        self.CptIndex = params.get("CptIndex")
        self.Policy = params.get("Policy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterClaimPolicyResponse(AbstractModel):
    """RegisterClaimPolicy response structure.

    """

    def __init__(self):
        r"""
        :param Id: The policy index.
        :type Id: int
        :param PolicyId: The policy ID.
        :type PolicyId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.PolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.PolicyId = params.get("PolicyId")
        self.RequestId = params.get("RequestId")


class RegisterCptRequest(AbstractModel):
    """RegisterCpt request structure.

    """

    def __init__(self):
        r"""
        :param GroupId: The group ID.
        :type GroupId: int
        :param ClusterId: The network ID.
        :type ClusterId: str
        :param CptJson: The JSON data of the credential claim type (CPT).
        :type CptJson: str
        :param CptId: If you do not specify this, the ID will auto increment.
        :type CptId: int
        """
        self.GroupId = None
        self.ClusterId = None
        self.CptJson = None
        self.CptId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.ClusterId = params.get("ClusterId")
        self.CptJson = params.get("CptJson")
        self.CptId = params.get("CptId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterCptResponse(AbstractModel):
    """RegisterCpt response structure.

    """

    def __init__(self):
        r"""
        :param Id: The claim protocol type (CPT) index.
        :type Id: int
        :param CptId: The claim protocol type (CPT) ID.
        :type CptId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.CptId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.CptId = params.get("CptId")
        self.RequestId = params.get("RequestId")


class RegisterIssuerRequest(AbstractModel):
    """RegisterIssuer request structure.

    """

    def __init__(self):
        r"""
        :param Did: The DID.
        :type Did: str
        :param Name: The issuing authority name.
        :type Name: str
        :param Description: Remarks
        :type Description: str
        """
        self.Did = None
        self.Name = None
        self.Description = None


    def _deserialize(self, params):
        self.Did = params.get("Did")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterIssuerResponse(AbstractModel):
    """RegisterIssuer response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RemoveHashRequest(AbstractModel):
    """RemoveHash request structure.

    """

    def __init__(self):
        r"""
        :param Hash: The CNS address of the contract.
        :type Hash: str
        """
        self.Hash = None


    def _deserialize(self, params):
        self.Hash = params.get("Hash")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveHashResponse(AbstractModel):
    """RemoveHash response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetCredentialStatusRequest(AbstractModel):
    """SetCredentialStatus request structure.

    """

    def __init__(self):
        r"""
        :param CredentialStatus: The credential status.
        :type CredentialStatus: :class:`tencentcloud.tdid.v20210519.models.CredentialStatus`
        """
        self.CredentialStatus = None


    def _deserialize(self, params):
        if params.get("CredentialStatus") is not None:
            self.CredentialStatus = CredentialStatus()
            self.CredentialStatus._deserialize(params.get("CredentialStatus"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetCredentialStatusResponse(AbstractModel):
    """SetCredentialStatus response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Task(AbstractModel):
    """The output parameter of `CreateDidService` and `CheckDidDeploy`.

    """

    def __init__(self):
        r"""
        :param Id: The task ID.
        :type Id: int
        :param AppId: The application ID.
        :type AppId: int
        :param ClusterId: The network ID.
        :type ClusterId: str
        :param GroupId: The group ID.
        :type GroupId: int
        :param ServiceId: The service ID.
        :type ServiceId: int
        :param Status: `0`: Under deployment; `1`: Deployed successfully; other values: Deployment failed.
        :type Status: int
        :param ErrorCode: The error code.
        :type ErrorCode: str
        :param ErrorMsg: The error message.
        :type ErrorMsg: str
        :param CreateTime: The creation time.
        :type CreateTime: str
        :param UpdateTime: The last updated time.
        :type UpdateTime: str
        """
        self.Id = None
        self.AppId = None
        self.ClusterId = None
        self.GroupId = None
        self.ServiceId = None
        self.Status = None
        self.ErrorCode = None
        self.ErrorMsg = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.AppId = params.get("AppId")
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        self.ServiceId = params.get("ServiceId")
        self.Status = params.get("Status")
        self.ErrorCode = params.get("ErrorCode")
        self.ErrorMsg = params.get("ErrorMsg")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransactionArg(AbstractModel):
    """The transaction parameters.

    """

    def __init__(self):
        r"""
        :param InvokerTDid: The credential ID.
        :type InvokerTDid: str
        """
        self.InvokerTDid = None


    def _deserialize(self, params):
        self.InvokerTDid = params.get("InvokerTDid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Trend(AbstractModel):
    """The trends.

    """

    def __init__(self):
        r"""
        :param Time: The time point.
        :type Time: str
        :param Count: The count.
        :type Count: int
        """
        self.Time = None
        self.Count = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyCredentialRequest(AbstractModel):
    """VerifyCredential request structure.

    """

    def __init__(self):
        r"""
        :param FunctionArg: A parameter set.
        :type FunctionArg: :class:`tencentcloud.tdid.v20210519.models.VerifyFunctionArg`
        """
        self.FunctionArg = None


    def _deserialize(self, params):
        if params.get("FunctionArg") is not None:
            self.FunctionArg = VerifyFunctionArg()
            self.FunctionArg._deserialize(params.get("FunctionArg"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyCredentialResponse(AbstractModel):
    """VerifyCredential response structure.

    """

    def __init__(self):
        r"""
        :param Result: Whether the verification is successful.
        :type Result: bool
        :param VerifyCode: The verification code.
        :type VerifyCode: int
        :param VerifyMessage: The verification message.
        :type VerifyMessage: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.VerifyCode = None
        self.VerifyMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.VerifyCode = params.get("VerifyCode")
        self.VerifyMessage = params.get("VerifyMessage")
        self.RequestId = params.get("RequestId")


class VerifyFunctionArg(AbstractModel):
    """The credential verification parameters.

    """

    def __init__(self):
        r"""
        :param CptId: The claim protocol type (CPT) ID.
        :type CptId: int
        :param Issuer: The issuer DID.
        :type Issuer: str
        :param ExpirationDate: The expiration time.
        :type ExpirationDate: int
        :param ClaimJson: The claim.
        :type ClaimJson: str
        :param IssuanceDate: The time when the credential was issued.
        :type IssuanceDate: int
        :param Context: The context.
        :type Context: str
        :param Id: The ID.
        :type Id: str
        :param Proof: The signature.
        :type Proof: :class:`tencentcloud.tdid.v20210519.models.Proof`
        :param Type: The type.
        :type Type: list of str
        """
        self.CptId = None
        self.Issuer = None
        self.ExpirationDate = None
        self.ClaimJson = None
        self.IssuanceDate = None
        self.Context = None
        self.Id = None
        self.Proof = None
        self.Type = None


    def _deserialize(self, params):
        self.CptId = params.get("CptId")
        self.Issuer = params.get("Issuer")
        self.ExpirationDate = params.get("ExpirationDate")
        self.ClaimJson = params.get("ClaimJson")
        self.IssuanceDate = params.get("IssuanceDate")
        self.Context = params.get("Context")
        self.Id = params.get("Id")
        if params.get("Proof") is not None:
            self.Proof = Proof()
            self.Proof._deserialize(params.get("Proof"))
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        