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
from tencentcloud.tcmpp.v20240801 import models


class TcmppClient(AbstractClient):
    _apiVersion = '2024-08-01'
    _endpoint = 'tcmpp.tencentcloudapi.com'
    _service = 'tcmpp'


    def AddTeamMember(self, request):
        """This API is used to add users to a team

        :param request: Request instance for AddTeamMember.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.AddTeamMemberRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.AddTeamMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddTeamMember", params, headers=headers)
            response = json.loads(body)
            model = models.AddTeamMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckGlobalDomain(self, request):
        """This API is used to query if the domain is in the allowlist or blocklist

        :param request: Request instance for CheckGlobalDomain.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.CheckGlobalDomainRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.CheckGlobalDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckGlobalDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CheckGlobalDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApplication(self, request):
        """This API is used to add an application

        :param request: Request instance for CreateApplication.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.CreateApplicationRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.CreateApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplication", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateConsoleMNPVersionCompileTask(self, request):
        """This API is used to add new mini program version to the console

        :param request: Request instance for CreateConsoleMNPVersionCompileTask.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.CreateConsoleMNPVersionCompileTaskRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.CreateConsoleMNPVersionCompileTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConsoleMNPVersionCompileTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConsoleMNPVersionCompileTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDomain(self, request):
        """This API is used to create a mini program service domain

        :param request: Request instance for CreateDomain.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.CreateDomainRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.CreateDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGlobalDomain(self, request):
        """This API is used to add domains to allowlist or blocklist

        :param request: Request instance for CreateGlobalDomain.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.CreateGlobalDomainRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.CreateGlobalDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGlobalDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGlobalDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMNP(self, request):
        """This API is used to create a mini program

        :param request: Request instance for CreateMNP.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.CreateMNPRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.CreateMNPResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMNP", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMNPResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOnlineApply(self, request):
        """This API is used to release the mini program

        :param request: Request instance for CreateOnlineApply.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.CreateOnlineApplyRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.CreateOnlineApplyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOnlineApply", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOnlineApplyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePlatformAudit(self, request):
        """This API is used to submit mini program version for approval

        :param request: Request instance for CreatePlatformAudit.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.CreatePlatformAuditRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.CreatePlatformAuditResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePlatformAudit", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePlatformAuditResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePresetKey(self, request):
        """This API is used to obtain the encryption key

        :param request: Request instance for CreatePresetKey.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.CreatePresetKeyRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.CreatePresetKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePresetKey", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePresetKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSensitiveAPI(self, request):
        """This API is used to add a sensitive API

        :param request: Request instance for CreateSensitiveAPI.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.CreateSensitiveAPIRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.CreateSensitiveAPIResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSensitiveAPI", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSensitiveAPIResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSensitiveApiApply(self, request):
        """This API is used to apply for sensitive API call permissions

        :param request: Request instance for CreateSensitiveApiApply.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.CreateSensitiveApiApplyRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.CreateSensitiveApiApplyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSensitiveApiApply", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSensitiveApiApplyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTeam(self, request):
        """This API is used to create a team

        :param request: Request instance for CreateTeam.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.CreateTeamRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.CreateTeamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTeam", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTeamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTeamMember(self, request):
        """This API is used to add team members

        :param request: Request instance for CreateTeamMember.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.CreateTeamMemberRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.CreateTeamMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTeamMember", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTeamMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUser(self, request):
        """This API is used to create a user

        :param request: Request instance for CreateUser.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.CreateUserRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.CreateUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUser", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApplication(self, request):
        """This API is used to delete applications

        :param request: Request instance for DeleteApplication.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DeleteApplicationRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DeleteApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApplication", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGlobalDomain(self, request):
        """This API is used to delete domains from allowlist or blocklist

        :param request: Request instance for DeleteGlobalDomain.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DeleteGlobalDomainRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DeleteGlobalDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGlobalDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGlobalDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMNP(self, request):
        """This API is used to delete the mini program

        :param request: Request instance for DeleteMNP.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DeleteMNPRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DeleteMNPResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMNP", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMNPResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSensitiveAPI(self, request):
        """This API is used to delete a sensitive API

        :param request: Request instance for DeleteSensitiveAPI.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DeleteSensitiveAPIRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DeleteSensitiveAPIResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSensitiveAPI", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSensitiveAPIResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTeam(self, request):
        """This API is used to delete a team

        :param request: Request instance for DeleteTeam.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DeleteTeamRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DeleteTeamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTeam", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTeamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTeamMember(self, request):
        """This API is used to delete a team member

        :param request: Request instance for DeleteTeamMember.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DeleteTeamMemberRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DeleteTeamMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTeamMember", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTeamMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUser(self, request):
        """This API is used to delete a user

        :param request: Request instance for DeleteUser.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DeleteUserRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DeleteUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUser", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplication(self, request):
        """This API is used to query application details

        :param request: Request instance for DescribeApplication.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeApplicationRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplication", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationConfig(self, request):
        """This API is used to query application configuration information

        :param request: Request instance for DescribeApplicationConfig.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeApplicationConfigRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeApplicationConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationList(self, request):
        """This API is used to query application list data

        :param request: Request instance for DescribeApplicationList.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeApplicationListRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeApplicationListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationMNPVersionAuditList(self, request):
        """This API is used to query the approval list of the mini program versions

        :param request: Request instance for DescribeApplicationMNPVersionAuditList.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeApplicationMNPVersionAuditListRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeApplicationMNPVersionAuditListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationMNPVersionAuditList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationMNPVersionAuditListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConsoleMNPVersionCompileTask(self, request):
        """This API is used to query if the mini program version is uploaded successfully

        :param request: Request instance for DescribeConsoleMNPVersionCompileTask.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeConsoleMNPVersionCompileTaskRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeConsoleMNPVersionCompileTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConsoleMNPVersionCompileTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConsoleMNPVersionCompileTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainInfo(self, request):
        """This API is used to query the domain name list configured for the mini program

        :param request: Request instance for DescribeDomainInfo.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeDomainInfoRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeDomainInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainTeamList(self, request):
        """This API is used to query the list of teams with domains that obtained the ICP filing

        :param request: Request instance for DescribeDomainTeamList.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeDomainTeamListRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeDomainTeamListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainTeamList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainTeamListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGlobalDomainList(self, request):
        """This API is used to query domain allowlist and blocklist

        :param request: Request instance for DescribeGlobalDomainList.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeGlobalDomainListRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeGlobalDomainListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGlobalDomainList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGlobalDomainListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPBoard(self, request):
        """This API is used to query the mini program version management information

        :param request: Request instance for DescribeMNPBoard.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeMNPBoardRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeMNPBoardResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPBoard", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPBoardResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPDetail(self, request):
        """This API is used to query mini program details

        :param request: Request instance for DescribeMNPDetail.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeMNPDetailRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeMNPDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPManagerDetail(self, request):
        """This API is used to query mini program details in the mini program list

        :param request: Request instance for DescribeMNPManagerDetail.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeMNPManagerDetailRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeMNPManagerDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPManagerDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPManagerDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPManagerList(self, request):
        """This API is used to query the mini program list

        :param request: Request instance for DescribeMNPManagerList.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeMNPManagerListRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeMNPManagerListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPManagerList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPManagerListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPPrivacy(self, request):
        """This API is used to query the details filled in the service description

        :param request: Request instance for DescribeMNPPrivacy.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeMNPPrivacyRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeMNPPrivacyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPPrivacy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPPrivacyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPType(self, request):
        """This API is used to query the mini program type list

        :param request: Request instance for DescribeMNPType.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeMNPTypeRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeMNPTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPVersionPreview(self, request):
        """This API is used to query the details of the mini program trial version

        :param request: Request instance for DescribeMNPVersionPreview.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeMNPVersionPreviewRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeMNPVersionPreviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPVersionPreview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPVersionPreviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOfflineMNPPackage(self, request):
        """This API is used to query offline mini program packages

        :param request: Request instance for DescribeOfflineMNPPackage.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeOfflineMNPPackageRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeOfflineMNPPackageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOfflineMNPPackage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOfflineMNPPackageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOnlineVersion(self, request):
        """This API is used to query the current release version of the mini program

        :param request: Request instance for DescribeOnlineVersion.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeOnlineVersionRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeOnlineVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOnlineVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOnlineVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRoleDetail(self, request):
        """This API is used to query role permission information

        :param request: Request instance for DescribeRoleDetail.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeRoleDetailRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeRoleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoleDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRoleDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRoleList(self, request):
        """This API is used to query role list data

        :param request: Request instance for DescribeRoleList.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeRoleListRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeRoleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRoleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSensitiveAPIAuditList(self, request):
        """This API is used to query sensitive API approval list

        :param request: Request instance for DescribeSensitiveAPIAuditList.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeSensitiveAPIAuditListRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeSensitiveAPIAuditListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSensitiveAPIAuditList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSensitiveAPIAuditListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSensitiveAPIList(self, request):
        """This API is used to query all sensitive APIs list

        :param request: Request instance for DescribeSensitiveAPIList.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeSensitiveAPIListRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeSensitiveAPIListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSensitiveAPIList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSensitiveAPIListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSensitiveApiApplyDetail(self, request):
        """This API is used to query sensitive API call details

        :param request: Request instance for DescribeSensitiveApiApplyDetail.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeSensitiveApiApplyDetailRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeSensitiveApiApplyDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSensitiveApiApplyDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSensitiveApiApplyDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSensitiveApiAuthList(self, request):
        """This API is used to query the sensitive APIs that require permission

        :param request: Request instance for DescribeSensitiveApiAuthList.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeSensitiveApiAuthListRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeSensitiveApiAuthListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSensitiveApiAuthList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSensitiveApiAuthListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSimpleApplicationInfoList(self, request):
        """This API is used to query application list information

        :param request: Request instance for DescribeSimpleApplicationInfoList.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeSimpleApplicationInfoListRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeSimpleApplicationInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSimpleApplicationInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSimpleApplicationInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSimpleTeamList(self, request):
        """This API is used to query the team information list

        :param request: Request instance for DescribeSimpleTeamList.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeSimpleTeamListRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeSimpleTeamListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSimpleTeamList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSimpleTeamListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTeam(self, request):
        """This API is used to query team details

        :param request: Request instance for DescribeTeam.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeTeamRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeTeamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTeam", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTeamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTeamDomainList(self, request):
        """This API is used to query a specified team’s domains that obtained ICP filing

        :param request: Request instance for DescribeTeamDomainList.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeTeamDomainListRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeTeamDomainListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTeamDomainList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTeamDomainListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTeamList(self, request):
        """This API is used to query the team list that can be viewed by the current role permissions

        :param request: Request instance for DescribeTeamList.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeTeamListRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeTeamListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTeamList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTeamListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTeamMemberList(self, request):
        """This API is used to query team member list

        :param request: Request instance for DescribeTeamMemberList.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeTeamMemberListRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeTeamMemberListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTeamMemberList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTeamMemberListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTeamMembers(self, request):
        """This API is used to query the member list of a specified team

        :param request: Request instance for DescribeTeamMembers.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeTeamMembersRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeTeamMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTeamMembers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTeamMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTempSecret4UploadFile2Cos(self, request):
        """This API is used to obtain a temporary key for file uploads

        :param request: Request instance for DescribeTempSecret4UploadFile2Cos.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeTempSecret4UploadFile2CosRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeTempSecret4UploadFile2CosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTempSecret4UploadFile2Cos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTempSecret4UploadFile2CosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserDetail(self, request):
        """This API is used to query user details

        :param request: Request instance for DescribeUserDetail.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeUserDetailRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeUserDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserList(self, request):
        """This API is used to query the user list

        :param request: Request instance for DescribeUserList.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DescribeUserListRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DescribeUserListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableTeamDomain(self, request):
        """This API is used to disable the company’s domain name that obtained the ICP filing

        :param request: Request instance for DisableTeamDomain.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.DisableTeamDomainRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.DisableTeamDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableTeamDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DisableTeamDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplication(self, request):
        """This API is used to change application information

        :param request: Request instance for ModifyApplication.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.ModifyApplicationRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.ModifyApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplication", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplicationAppKey(self, request):
        """This API is used to modify the application package name

        :param request: Request instance for ModifyApplicationAppKey.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.ModifyApplicationAppKeyRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.ModifyApplicationAppKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationAppKey", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationAppKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplicationAppUrl(self, request):
        """This API is used to change the app download address

        :param request: Request instance for ModifyApplicationAppUrl.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.ModifyApplicationAppUrlRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.ModifyApplicationAppUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationAppUrl", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationAppUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomain(self, request):
        """This API is used to edit the mini program domain information

        :param request: Request instance for ModifyDomain.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.ModifyDomainRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.ModifyDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomain", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGlobalDomain(self, request):
        """This API is used to modify domain allowlist or blocklist

        :param request: Request instance for ModifyGlobalDomain.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.ModifyGlobalDomainRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.ModifyGlobalDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGlobalDomain", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGlobalDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMNP(self, request):
        """This API is used to modify mini program information

        :param request: Request instance for ModifyMNP.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.ModifyMNPRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.ModifyMNPResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMNP", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMNPResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMNPStatusOffline(self, request):
        """This API is used to remove the mini program

        :param request: Request instance for ModifyMNPStatusOffline.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.ModifyMNPStatusOfflineRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.ModifyMNPStatusOfflineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMNPStatusOffline", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMNPStatusOfflineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMNPVersionPreview(self, request):
        """This API is used to configure the mini program trial version

        :param request: Request instance for ModifyMNPVersionPreview.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.ModifyMNPVersionPreviewRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.ModifyMNPVersionPreviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMNPVersionPreview", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMNPVersionPreviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyOnlineVersion(self, request):
        """This API is used to rollback a mini program release version

        :param request: Request instance for ModifyOnlineVersion.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.ModifyOnlineVersionRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.ModifyOnlineVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOnlineVersion", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyOnlineVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPlatformAuditStatus(self, request):
        """This API is used to approve the release of the mini program version

        :param request: Request instance for ModifyPlatformAuditStatus.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.ModifyPlatformAuditStatusRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.ModifyPlatformAuditStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPlatformAuditStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPlatformAuditStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySensitiveAPIAuditStatus(self, request):
        """This API is used to approve sensitive API call permission

        :param request: Request instance for ModifySensitiveAPIAuditStatus.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.ModifySensitiveAPIAuditStatusRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.ModifySensitiveAPIAuditStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySensitiveAPIAuditStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySensitiveAPIAuditStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTeam(self, request):
        """This API is used to change team information

        :param request: Request instance for ModifyTeam.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.ModifyTeamRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.ModifyTeamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTeam", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTeamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTeamMember(self, request):
        """This API is used to change team member roles

        :param request: Request instance for ModifyTeamMember.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.ModifyTeamMemberRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.ModifyTeamMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTeamMember", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTeamMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUser(self, request):
        """This API is used to edit user information

        :param request: Request instance for ModifyUser.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.ModifyUserRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.ModifyUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUser", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserPassword(self, request):
        """This API is used to reset user password

        :param request: Request instance for ModifyUserPassword.
        :type request: :class:`tencentcloud.tcmpp.v20240801.models.ModifyUserPasswordRequest`
        :rtype: :class:`tencentcloud.tcmpp.v20240801.models.ModifyUserPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))