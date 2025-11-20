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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.tdid.v20210519 import models
from typing import Dict


class TdidClient(AbstractClient):
    _apiVersion = '2021-05-19'
    _endpoint = 'tdid.intl.tencentcloudapi.com'
    _service = 'tdid'

    async def AddLabel(
            self,
            request: models.AddLabelRequest,
            opts: Dict = None,
    ) -> models.AddLabelResponse:
        """
        This API is used to add a label to a DID.
        """
        
        kwargs = {}
        kwargs["action"] = "AddLabel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddLabelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelAuthorityIssuer(
            self,
            request: models.CancelAuthorityIssuerRequest,
            opts: Dict = None,
    ) -> models.CancelAuthorityIssuerResponse:
        """
        This API is used to revoke the certification of an issuing authority.
        """
        
        kwargs = {}
        kwargs["action"] = "CancelAuthorityIssuer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelAuthorityIssuerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckChain(
            self,
            request: models.CheckChainRequest,
            opts: Dict = None,
    ) -> models.CheckChainResponse:
        """
        This API is used to get blockchain information.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckChain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckChainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckDidDeploy(
            self,
            request: models.CheckDidDeployRequest,
            opts: Dict = None,
    ) -> models.CheckDidDeployResponse:
        """
        This API is used to query a deployment task.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckDidDeploy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckDidDeployResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCredential(
            self,
            request: models.CreateCredentialRequest,
            opts: Dict = None,
    ) -> models.CreateCredentialResponse:
        """
        This API is used to create a credential.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCredentialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDidService(
            self,
            request: models.CreateDidServiceRequest,
            opts: Dict = None,
    ) -> models.CreateDidServiceResponse:
        """
        This API is used to create a DID service.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDidService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDidServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLabel(
            self,
            request: models.CreateLabelRequest,
            opts: Dict = None,
    ) -> models.CreateLabelResponse:
        """
        This API is used to create a label.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLabel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLabelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSelectiveCredential(
            self,
            request: models.CreateSelectiveCredentialRequest,
            opts: Dict = None,
    ) -> models.CreateSelectiveCredentialResponse:
        """
        This API is used to create a selective disclosure credential.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSelectiveCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSelectiveCredentialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTDid(
            self,
            request: models.CreateTDidRequest,
            opts: Dict = None,
    ) -> models.CreateTDidResponse:
        """
        This API is used to create an organization DID.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTDid"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTDidResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTDidByPrivateKey(
            self,
            request: models.CreateTDidByPrivateKeyRequest,
            opts: Dict = None,
    ) -> models.CreateTDidByPrivateKeyResponse:
        """
        This API is used to generate a TDID by private key.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTDidByPrivateKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTDidByPrivateKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTDidByPublicKey(
            self,
            request: models.CreateTDidByPublicKeyRequest,
            opts: Dict = None,
    ) -> models.CreateTDidByPublicKeyResponse:
        """
        This API is used to generate a TDID by public key.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTDidByPublicKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTDidByPublicKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeployByName(
            self,
            request: models.DeployByNameRequest,
            opts: Dict = None,
    ) -> models.DeployByNameResponse:
        """
        This API is used to deploy a TDID contract by name.
        """
        
        kwargs = {}
        kwargs["action"] = "DeployByName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeployByNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DownCpt(
            self,
            request: models.DownCptRequest,
            opts: Dict = None,
    ) -> models.DownCptResponse:
        """
        This API is used to download a claim protocol type (CPT).
        """
        
        kwargs = {}
        kwargs["action"] = "DownCpt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DownCptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableHash(
            self,
            request: models.EnableHashRequest,
            opts: Dict = None,
    ) -> models.EnableHashResponse:
        """
        This API is used to enable a contract.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableHash"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableHashResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAgencyTDid(
            self,
            request: models.GetAgencyTDidRequest,
            opts: Dict = None,
    ) -> models.GetAgencyTDidResponse:
        """
        该接口已废弃

        This API is used to get the DID details of the current organization.
        """
        
        kwargs = {}
        kwargs["action"] = "GetAgencyTDid"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAgencyTDidResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAuthoritiesList(
            self,
            request: models.GetAuthoritiesListRequest,
            opts: Dict = None,
    ) -> models.GetAuthoritiesListResponse:
        """
        This API is used to query authorities.
        """
        
        kwargs = {}
        kwargs["action"] = "GetAuthoritiesList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAuthoritiesListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAuthorityIssuer(
            self,
            request: models.GetAuthorityIssuerRequest,
            opts: Dict = None,
    ) -> models.GetAuthorityIssuerResponse:
        """
        This API is used to get the information of an issuing authority.
        """
        
        kwargs = {}
        kwargs["action"] = "GetAuthorityIssuer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAuthorityIssuerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetConsortiumClusterList(
            self,
            request: models.GetConsortiumClusterListRequest,
            opts: Dict = None,
    ) -> models.GetConsortiumClusterListResponse:
        """
        This API is used to query the BCOS networks of a consortium.
        """
        
        kwargs = {}
        kwargs["action"] = "GetConsortiumClusterList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetConsortiumClusterListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetConsortiumList(
            self,
            request: models.GetConsortiumListRequest,
            opts: Dict = None,
    ) -> models.GetConsortiumListResponse:
        """
        This API is used to query consortiums.
        """
        
        kwargs = {}
        kwargs["action"] = "GetConsortiumList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetConsortiumListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetCptInfo(
            self,
            request: models.GetCptInfoRequest,
            opts: Dict = None,
    ) -> models.GetCptInfoResponse:
        """
        This API is used to get the information of a claim protocol type (CPT).
        """
        
        kwargs = {}
        kwargs["action"] = "GetCptInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetCptInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetCptList(
            self,
            request: models.GetCptListRequest,
            opts: Dict = None,
    ) -> models.GetCptListResponse:
        """
        This API is used to query claim protocol types (CPT).
        """
        
        kwargs = {}
        kwargs["action"] = "GetCptList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetCptListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetCredentialCptRank(
            self,
            request: models.GetCredentialCptRankRequest,
            opts: Dict = None,
    ) -> models.GetCredentialCptRankResponse:
        """
        This API is used to get the rankings of claim protocol types (CPT).
        """
        
        kwargs = {}
        kwargs["action"] = "GetCredentialCptRank"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetCredentialCptRankResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetCredentialIssueRank(
            self,
            request: models.GetCredentialIssueRankRequest,
            opts: Dict = None,
    ) -> models.GetCredentialIssueRankResponse:
        """
        This API is used to get the rankings of issuers.
        """
        
        kwargs = {}
        kwargs["action"] = "GetCredentialIssueRank"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetCredentialIssueRankResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetCredentialIssueTrend(
            self,
            request: models.GetCredentialIssueTrendRequest,
            opts: Dict = None,
    ) -> models.GetCredentialIssueTrendResponse:
        """
        This API is used to query credential issuing trends.
        """
        
        kwargs = {}
        kwargs["action"] = "GetCredentialIssueTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetCredentialIssueTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetCredentialStatus(
            self,
            request: models.GetCredentialStatusRequest,
            opts: Dict = None,
    ) -> models.GetCredentialStatusResponse:
        """
        This API is used to query the on-chain status of a credential.
        """
        
        kwargs = {}
        kwargs["action"] = "GetCredentialStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetCredentialStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDataPanel(
            self,
            request: models.GetDataPanelRequest,
            opts: Dict = None,
    ) -> models.GetDataPanelResponse:
        """
        This API is used to query the overall statistics of a network.
        """
        
        kwargs = {}
        kwargs["action"] = "GetDataPanel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDataPanelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDeployInfo(
            self,
            request: models.GetDeployInfoRequest,
            opts: Dict = None,
    ) -> models.GetDeployInfoResponse:
        """
        This API is used to query the deployment information of a contract.
        """
        
        kwargs = {}
        kwargs["action"] = "GetDeployInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDeployInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDeployList(
            self,
            request: models.GetDeployListRequest,
            opts: Dict = None,
    ) -> models.GetDeployListResponse:
        """
        This API is used to query deployed contracts.
        """
        
        kwargs = {}
        kwargs["action"] = "GetDeployList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDeployListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDidClusterDetail(
            self,
            request: models.GetDidClusterDetailRequest,
            opts: Dict = None,
    ) -> models.GetDidClusterDetailResponse:
        """
        This API is used to get the information of a DID blockchain network.
        """
        
        kwargs = {}
        kwargs["action"] = "GetDidClusterDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDidClusterDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDidClusterList(
            self,
            request: models.GetDidClusterListRequest,
            opts: Dict = None,
    ) -> models.GetDidClusterListResponse:
        """
        This API is used to query your DID networks.
        """
        
        kwargs = {}
        kwargs["action"] = "GetDidClusterList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDidClusterListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDidDetail(
            self,
            request: models.GetDidDetailRequest,
            opts: Dict = None,
    ) -> models.GetDidDetailResponse:
        """
        This API is used to get the information of a DID.
        """
        
        kwargs = {}
        kwargs["action"] = "GetDidDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDidDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDidDocument(
            self,
            request: models.GetDidDocumentRequest,
            opts: Dict = None,
    ) -> models.GetDidDocumentResponse:
        """
        This API is used to get the document of a DID.
        """
        
        kwargs = {}
        kwargs["action"] = "GetDidDocument"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDidDocumentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDidList(
            self,
            request: models.GetDidListRequest,
            opts: Dict = None,
    ) -> models.GetDidListResponse:
        """
        This API is used to query DIDs.
        """
        
        kwargs = {}
        kwargs["action"] = "GetDidList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDidListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDidRegisterTrend(
            self,
            request: models.GetDidRegisterTrendRequest,
            opts: Dict = None,
    ) -> models.GetDidRegisterTrendResponse:
        """
        This API is used to query DID registration trends.
        """
        
        kwargs = {}
        kwargs["action"] = "GetDidRegisterTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDidRegisterTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDidServiceDetail(
            self,
            request: models.GetDidServiceDetailRequest,
            opts: Dict = None,
    ) -> models.GetDidServiceDetailResponse:
        """
        This API is used to get the information of a DID service.
        """
        
        kwargs = {}
        kwargs["action"] = "GetDidServiceDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDidServiceDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDidServiceList(
            self,
            request: models.GetDidServiceListRequest,
            opts: Dict = None,
    ) -> models.GetDidServiceListResponse:
        """
        This API is used to query DID services.
        """
        
        kwargs = {}
        kwargs["action"] = "GetDidServiceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDidServiceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetGroupList(
            self,
            request: models.GetGroupListRequest,
            opts: Dict = None,
    ) -> models.GetGroupListResponse:
        """
        This API is used to query main groups.
        """
        
        kwargs = {}
        kwargs["action"] = "GetGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetLabelList(
            self,
            request: models.GetLabelListRequest,
            opts: Dict = None,
    ) -> models.GetLabelListResponse:
        """
        This API is used to query labels.
        """
        
        kwargs = {}
        kwargs["action"] = "GetLabelList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetLabelListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetPolicyList(
            self,
            request: models.GetPolicyListRequest,
            opts: Dict = None,
    ) -> models.GetPolicyListResponse:
        """
        This API is used to query disclosure policies.
        """
        
        kwargs = {}
        kwargs["action"] = "GetPolicyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetPolicyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetPublicKey(
            self,
            request: models.GetPublicKeyRequest,
            opts: Dict = None,
    ) -> models.GetPublicKeyResponse:
        """
        This API is used to get the public key of a DID.
        """
        
        kwargs = {}
        kwargs["action"] = "GetPublicKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetPublicKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryPolicy(
            self,
            request: models.QueryPolicyRequest,
            opts: Dict = None,
    ) -> models.QueryPolicyResponse:
        """
        This API is used to get the information of a disclosure policy.
        """
        
        kwargs = {}
        kwargs["action"] = "QueryPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeAuthorityIssuer(
            self,
            request: models.RecognizeAuthorityIssuerRequest,
            opts: Dict = None,
    ) -> models.RecognizeAuthorityIssuerResponse:
        """
        This API is used to certify an issuing authority.
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeAuthorityIssuer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeAuthorityIssuerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterClaimPolicy(
            self,
            request: models.RegisterClaimPolicyRequest,
            opts: Dict = None,
    ) -> models.RegisterClaimPolicyResponse:
        """
        This API is used to register a disclosure policy.
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterClaimPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterClaimPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterCpt(
            self,
            request: models.RegisterCptRequest,
            opts: Dict = None,
    ) -> models.RegisterCptResponse:
        """
        This API is used to create a claim protocol type (CPT).
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterCpt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterCptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterIssuer(
            self,
            request: models.RegisterIssuerRequest,
            opts: Dict = None,
    ) -> models.RegisterIssuerResponse:
        """
        This API is used to register an issuing authority.
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterIssuer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterIssuerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveHash(
            self,
            request: models.RemoveHashRequest,
            opts: Dict = None,
    ) -> models.RemoveHashResponse:
        """
        This API is used to delete a contract.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveHash"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveHashResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetCredentialStatus(
            self,
            request: models.SetCredentialStatusRequest,
            opts: Dict = None,
    ) -> models.SetCredentialStatusResponse:
        """
        This API is used to change the on-chain status of a credential.
        """
        
        kwargs = {}
        kwargs["action"] = "SetCredentialStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetCredentialStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyCredential(
            self,
            request: models.VerifyCredentialRequest,
            opts: Dict = None,
    ) -> models.VerifyCredentialResponse:
        """
        This API is used to verify a credential.
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyCredentialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)