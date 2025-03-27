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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.tdid.v20210519 import models


class TdidClient(AbstractClient):
    _apiVersion = '2021-05-19'
    _endpoint = 'tdid.intl.tencentcloudapi.com'
    _service = 'tdid'


    def AddLabel(self, request):
        """This API is used to add a label to a DID.

        :param request: Request instance for AddLabel.
        :type request: :class:`tencentcloud.tdid.v20210519.models.AddLabelRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.AddLabelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddLabel", params, headers=headers)
            response = json.loads(body)
            model = models.AddLabelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelAuthorityIssuer(self, request):
        """This API is used to revoke the certification of an issuing authority.

        :param request: Request instance for CancelAuthorityIssuer.
        :type request: :class:`tencentcloud.tdid.v20210519.models.CancelAuthorityIssuerRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.CancelAuthorityIssuerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelAuthorityIssuer", params, headers=headers)
            response = json.loads(body)
            model = models.CancelAuthorityIssuerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckChain(self, request):
        """This API is used to get blockchain information.

        :param request: Request instance for CheckChain.
        :type request: :class:`tencentcloud.tdid.v20210519.models.CheckChainRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.CheckChainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckChain", params, headers=headers)
            response = json.loads(body)
            model = models.CheckChainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckDidDeploy(self, request):
        """This API is used to query a deployment task.

        :param request: Request instance for CheckDidDeploy.
        :type request: :class:`tencentcloud.tdid.v20210519.models.CheckDidDeployRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.CheckDidDeployResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckDidDeploy", params, headers=headers)
            response = json.loads(body)
            model = models.CheckDidDeployResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCredential(self, request):
        """This API is used to create a credential.

        :param request: Request instance for CreateCredential.
        :type request: :class:`tencentcloud.tdid.v20210519.models.CreateCredentialRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.CreateCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCredential", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCredentialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDidService(self, request):
        """This API is used to create a DID service.

        :param request: Request instance for CreateDidService.
        :type request: :class:`tencentcloud.tdid.v20210519.models.CreateDidServiceRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.CreateDidServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDidService", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDidServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLabel(self, request):
        """This API is used to create a label.

        :param request: Request instance for CreateLabel.
        :type request: :class:`tencentcloud.tdid.v20210519.models.CreateLabelRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.CreateLabelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLabel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLabelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSelectiveCredential(self, request):
        """This API is used to create a selective disclosure credential.

        :param request: Request instance for CreateSelectiveCredential.
        :type request: :class:`tencentcloud.tdid.v20210519.models.CreateSelectiveCredentialRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.CreateSelectiveCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSelectiveCredential", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSelectiveCredentialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTDid(self, request):
        """This API is used to create an organization DID.

        :param request: Request instance for CreateTDid.
        :type request: :class:`tencentcloud.tdid.v20210519.models.CreateTDidRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.CreateTDidResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTDid", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTDidResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTDidByPrivateKey(self, request):
        """This API is used to generate a TDID by private key.

        :param request: Request instance for CreateTDidByPrivateKey.
        :type request: :class:`tencentcloud.tdid.v20210519.models.CreateTDidByPrivateKeyRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.CreateTDidByPrivateKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTDidByPrivateKey", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTDidByPrivateKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTDidByPublicKey(self, request):
        """This API is used to generate a TDID by public key.

        :param request: Request instance for CreateTDidByPublicKey.
        :type request: :class:`tencentcloud.tdid.v20210519.models.CreateTDidByPublicKeyRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.CreateTDidByPublicKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTDidByPublicKey", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTDidByPublicKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeployByName(self, request):
        """This API is used to deploy a TDID contract by name.

        :param request: Request instance for DeployByName.
        :type request: :class:`tencentcloud.tdid.v20210519.models.DeployByNameRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.DeployByNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeployByName", params, headers=headers)
            response = json.loads(body)
            model = models.DeployByNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DownCpt(self, request):
        """This API is used to download a claim protocol type (CPT).

        :param request: Request instance for DownCpt.
        :type request: :class:`tencentcloud.tdid.v20210519.models.DownCptRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.DownCptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownCpt", params, headers=headers)
            response = json.loads(body)
            model = models.DownCptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableHash(self, request):
        """This API is used to enable a contract.

        :param request: Request instance for EnableHash.
        :type request: :class:`tencentcloud.tdid.v20210519.models.EnableHashRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.EnableHashResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableHash", params, headers=headers)
            response = json.loads(body)
            model = models.EnableHashResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAgencyTDid(self, request):
        """该接口已废弃

        This API is used to get the DID details of the current organization.

        :param request: Request instance for GetAgencyTDid.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetAgencyTDidRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetAgencyTDidResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAgencyTDid", params, headers=headers)
            response = json.loads(body)
            model = models.GetAgencyTDidResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAuthoritiesList(self, request):
        """This API is used to query authorities.

        :param request: Request instance for GetAuthoritiesList.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetAuthoritiesListRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetAuthoritiesListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAuthoritiesList", params, headers=headers)
            response = json.loads(body)
            model = models.GetAuthoritiesListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAuthorityIssuer(self, request):
        """This API is used to get the information of an issuing authority.

        :param request: Request instance for GetAuthorityIssuer.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetAuthorityIssuerRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetAuthorityIssuerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAuthorityIssuer", params, headers=headers)
            response = json.loads(body)
            model = models.GetAuthorityIssuerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetConsortiumClusterList(self, request):
        """This API is used to query the BCOS networks of a consortium.

        :param request: Request instance for GetConsortiumClusterList.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetConsortiumClusterListRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetConsortiumClusterListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetConsortiumClusterList", params, headers=headers)
            response = json.loads(body)
            model = models.GetConsortiumClusterListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetConsortiumList(self, request):
        """This API is used to query consortiums.

        :param request: Request instance for GetConsortiumList.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetConsortiumListRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetConsortiumListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetConsortiumList", params, headers=headers)
            response = json.loads(body)
            model = models.GetConsortiumListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetCptInfo(self, request):
        """This API is used to get the information of a claim protocol type (CPT).

        :param request: Request instance for GetCptInfo.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetCptInfoRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetCptInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCptInfo", params, headers=headers)
            response = json.loads(body)
            model = models.GetCptInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetCptList(self, request):
        """This API is used to query claim protocol types (CPT).

        :param request: Request instance for GetCptList.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetCptListRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetCptListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCptList", params, headers=headers)
            response = json.loads(body)
            model = models.GetCptListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetCredentialCptRank(self, request):
        """This API is used to get the rankings of claim protocol types (CPT).

        :param request: Request instance for GetCredentialCptRank.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetCredentialCptRankRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetCredentialCptRankResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCredentialCptRank", params, headers=headers)
            response = json.loads(body)
            model = models.GetCredentialCptRankResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetCredentialIssueRank(self, request):
        """This API is used to get the rankings of issuers.

        :param request: Request instance for GetCredentialIssueRank.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetCredentialIssueRankRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetCredentialIssueRankResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCredentialIssueRank", params, headers=headers)
            response = json.loads(body)
            model = models.GetCredentialIssueRankResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetCredentialIssueTrend(self, request):
        """This API is used to query credential issuing trends.

        :param request: Request instance for GetCredentialIssueTrend.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetCredentialIssueTrendRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetCredentialIssueTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCredentialIssueTrend", params, headers=headers)
            response = json.loads(body)
            model = models.GetCredentialIssueTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetCredentialStatus(self, request):
        """This API is used to query the on-chain status of a credential.

        :param request: Request instance for GetCredentialStatus.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetCredentialStatusRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetCredentialStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCredentialStatus", params, headers=headers)
            response = json.loads(body)
            model = models.GetCredentialStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDataPanel(self, request):
        """This API is used to query the overall statistics of a network.

        :param request: Request instance for GetDataPanel.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetDataPanelRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetDataPanelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDataPanel", params, headers=headers)
            response = json.loads(body)
            model = models.GetDataPanelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDeployInfo(self, request):
        """This API is used to query the deployment information of a contract.

        :param request: Request instance for GetDeployInfo.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetDeployInfoRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetDeployInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDeployInfo", params, headers=headers)
            response = json.loads(body)
            model = models.GetDeployInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDeployList(self, request):
        """This API is used to query deployed contracts.

        :param request: Request instance for GetDeployList.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetDeployListRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetDeployListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDeployList", params, headers=headers)
            response = json.loads(body)
            model = models.GetDeployListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDidClusterDetail(self, request):
        """This API is used to get the information of a DID blockchain network.

        :param request: Request instance for GetDidClusterDetail.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetDidClusterDetailRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetDidClusterDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDidClusterDetail", params, headers=headers)
            response = json.loads(body)
            model = models.GetDidClusterDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDidClusterList(self, request):
        """This API is used to query your DID networks.

        :param request: Request instance for GetDidClusterList.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetDidClusterListRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetDidClusterListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDidClusterList", params, headers=headers)
            response = json.loads(body)
            model = models.GetDidClusterListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDidDetail(self, request):
        """This API is used to get the information of a DID.

        :param request: Request instance for GetDidDetail.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetDidDetailRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetDidDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDidDetail", params, headers=headers)
            response = json.loads(body)
            model = models.GetDidDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDidDocument(self, request):
        """This API is used to get the document of a DID.

        :param request: Request instance for GetDidDocument.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetDidDocumentRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetDidDocumentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDidDocument", params, headers=headers)
            response = json.loads(body)
            model = models.GetDidDocumentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDidList(self, request):
        """This API is used to query DIDs.

        :param request: Request instance for GetDidList.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetDidListRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetDidListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDidList", params, headers=headers)
            response = json.loads(body)
            model = models.GetDidListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDidRegisterTrend(self, request):
        """This API is used to query DID registration trends.

        :param request: Request instance for GetDidRegisterTrend.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetDidRegisterTrendRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetDidRegisterTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDidRegisterTrend", params, headers=headers)
            response = json.loads(body)
            model = models.GetDidRegisterTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDidServiceDetail(self, request):
        """This API is used to get the information of a DID service.

        :param request: Request instance for GetDidServiceDetail.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetDidServiceDetailRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetDidServiceDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDidServiceDetail", params, headers=headers)
            response = json.loads(body)
            model = models.GetDidServiceDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDidServiceList(self, request):
        """This API is used to query DID services.

        :param request: Request instance for GetDidServiceList.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetDidServiceListRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetDidServiceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDidServiceList", params, headers=headers)
            response = json.loads(body)
            model = models.GetDidServiceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetGroupList(self, request):
        """This API is used to query main groups.

        :param request: Request instance for GetGroupList.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetGroupListRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.GetGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetLabelList(self, request):
        """This API is used to query labels.

        :param request: Request instance for GetLabelList.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetLabelListRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetLabelListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetLabelList", params, headers=headers)
            response = json.loads(body)
            model = models.GetLabelListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetPolicyList(self, request):
        """This API is used to query disclosure policies.

        :param request: Request instance for GetPolicyList.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetPolicyListRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetPolicyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetPolicyList", params, headers=headers)
            response = json.loads(body)
            model = models.GetPolicyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetPublicKey(self, request):
        """This API is used to get the public key of a DID.

        :param request: Request instance for GetPublicKey.
        :type request: :class:`tencentcloud.tdid.v20210519.models.GetPublicKeyRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.GetPublicKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetPublicKey", params, headers=headers)
            response = json.loads(body)
            model = models.GetPublicKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryPolicy(self, request):
        """This API is used to get the information of a disclosure policy.

        :param request: Request instance for QueryPolicy.
        :type request: :class:`tencentcloud.tdid.v20210519.models.QueryPolicyRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.QueryPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.QueryPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecognizeAuthorityIssuer(self, request):
        """This API is used to certify an issuing authority.

        :param request: Request instance for RecognizeAuthorityIssuer.
        :type request: :class:`tencentcloud.tdid.v20210519.models.RecognizeAuthorityIssuerRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.RecognizeAuthorityIssuerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizeAuthorityIssuer", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizeAuthorityIssuerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterClaimPolicy(self, request):
        """This API is used to register a disclosure policy.

        :param request: Request instance for RegisterClaimPolicy.
        :type request: :class:`tencentcloud.tdid.v20210519.models.RegisterClaimPolicyRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.RegisterClaimPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterClaimPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterClaimPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterCpt(self, request):
        """This API is used to create a claim protocol type (CPT).

        :param request: Request instance for RegisterCpt.
        :type request: :class:`tencentcloud.tdid.v20210519.models.RegisterCptRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.RegisterCptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterCpt", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterCptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterIssuer(self, request):
        """This API is used to register an issuing authority.

        :param request: Request instance for RegisterIssuer.
        :type request: :class:`tencentcloud.tdid.v20210519.models.RegisterIssuerRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.RegisterIssuerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterIssuer", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterIssuerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveHash(self, request):
        """This API is used to delete a contract.

        :param request: Request instance for RemoveHash.
        :type request: :class:`tencentcloud.tdid.v20210519.models.RemoveHashRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.RemoveHashResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveHash", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveHashResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetCredentialStatus(self, request):
        """This API is used to change the on-chain status of a credential.

        :param request: Request instance for SetCredentialStatus.
        :type request: :class:`tencentcloud.tdid.v20210519.models.SetCredentialStatusRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.SetCredentialStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetCredentialStatus", params, headers=headers)
            response = json.loads(body)
            model = models.SetCredentialStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VerifyCredential(self, request):
        """This API is used to verify a credential.

        :param request: Request instance for VerifyCredential.
        :type request: :class:`tencentcloud.tdid.v20210519.models.VerifyCredentialRequest`
        :rtype: :class:`tencentcloud.tdid.v20210519.models.VerifyCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifyCredential", params, headers=headers)
            response = json.loads(body)
            model = models.VerifyCredentialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))