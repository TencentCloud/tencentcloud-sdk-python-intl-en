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
from tencentcloud.tem.v20210701 import models
from typing import Dict


class TemClient(AbstractClient):
    _apiVersion = '2021-07-01'
    _endpoint = 'tem.intl.tencentcloudapi.com'
    _service = 'tem'

    async def CreateApplication(
            self,
            request: models.CreateApplicationRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationResponse:
        """
        This API is used to create an application.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApplicationAutoscaler(
            self,
            request: models.CreateApplicationAutoscalerRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationAutoscalerResponse:
        """
        This API is used to create a scaling rule.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplicationAutoscaler"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationAutoscalerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApplicationService(
            self,
            request: models.CreateApplicationServiceRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationServiceResponse:
        """
        This API is used to create an access policy.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplicationService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConfigData(
            self,
            request: models.CreateConfigDataRequest,
            opts: Dict = None,
    ) -> models.CreateConfigDataResponse:
        """
        This API is used to create a configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConfigData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConfigDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCosToken(
            self,
            request: models.CreateCosTokenRequest,
            opts: Dict = None,
    ) -> models.CreateCosTokenResponse:
        """
        This API is used to generate a COS temporary key.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCosToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCosTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEnvironment(
            self,
            request: models.CreateEnvironmentRequest,
            opts: Dict = None,
    ) -> models.CreateEnvironmentResponse:
        """
        This API is used to create an environment.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLogConfig(
            self,
            request: models.CreateLogConfigRequest,
            opts: Dict = None,
    ) -> models.CreateLogConfigResponse:
        """
        This API is used to create a log collecting configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateResource(
            self,
            request: models.CreateResourceRequest,
            opts: Dict = None,
    ) -> models.CreateResourceResponse:
        """
        This API is used to bind a cloud resource.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApplication(
            self,
            request: models.DeleteApplicationRequest,
            opts: Dict = None,
    ) -> models.DeleteApplicationResponse:
        """
        This API is used to delete an application.
          - Stop running the current application
          - Delete resources related to the application
          - Delete the application
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApplicationAutoscaler(
            self,
            request: models.DeleteApplicationAutoscalerRequest,
            opts: Dict = None,
    ) -> models.DeleteApplicationAutoscalerResponse:
        """
        This API is used to delete a scaling rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApplicationAutoscaler"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApplicationAutoscalerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApplicationService(
            self,
            request: models.DeleteApplicationServiceRequest,
            opts: Dict = None,
    ) -> models.DeleteApplicationServiceResponse:
        """
        This API is used to delete an access policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApplicationService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApplicationServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIngress(
            self,
            request: models.DeleteIngressRequest,
            opts: Dict = None,
    ) -> models.DeleteIngressResponse:
        """
        This API is used to delete an ingress rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIngress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIngressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeployApplication(
            self,
            request: models.DeployApplicationRequest,
            opts: Dict = None,
    ) -> models.DeployApplicationResponse:
        """
        This API is used to deploy an application.
        """
        
        kwargs = {}
        kwargs["action"] = "DeployApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeployApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationAutoscalerList(
            self,
            request: models.DescribeApplicationAutoscalerListRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationAutoscalerListResponse:
        """
        This API is used to query the scaling rules of an application.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationAutoscalerList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationAutoscalerListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationInfo(
            self,
            request: models.DescribeApplicationInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationInfoResponse:
        """
        This API is used to check the basic information of an application.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationPods(
            self,
            request: models.DescribeApplicationPodsRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationPodsResponse:
        """
        This API is used to get the list of application pods.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationPods"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationPodsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationServiceList(
            self,
            request: models.DescribeApplicationServiceListRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationServiceListResponse:
        """
        This API is used to query the list of access policies.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationServiceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationServiceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplications(
            self,
            request: models.DescribeApplicationsRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationsResponse:
        """
        This API is to query the list of running applications.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplications"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationsStatus(
            self,
            request: models.DescribeApplicationsStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationsStatusResponse:
        """
        This API is used to query the status of all applications in an envrionment.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationsStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationsStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigData(
            self,
            request: models.DescribeConfigDataRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigDataResponse:
        """
        This API is used to query details of a configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigDataList(
            self,
            request: models.DescribeConfigDataListRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigDataListResponse:
        """
        This API is used to query the list of configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigDataList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigDataListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnvironment(
            self,
            request: models.DescribeEnvironmentRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvironmentResponse:
        """
        This API is used to obtain the basic information of an environment.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnvironmentStatus(
            self,
            request: models.DescribeEnvironmentStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvironmentStatusResponse:
        """
        This API is used to obtain the environment status.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvironmentStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvironmentStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnvironments(
            self,
            request: models.DescribeEnvironmentsRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvironmentsResponse:
        """
        This API is used to obtain the list of environments.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvironments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvironmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIngress(
            self,
            request: models.DescribeIngressRequest,
            opts: Dict = None,
    ) -> models.DescribeIngressResponse:
        """
        This API is used to query an ingress rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIngress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIngressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIngresses(
            self,
            request: models.DescribeIngressesRequest,
            opts: Dict = None,
    ) -> models.DescribeIngressesResponse:
        """
        This API is used to query the list of ingress rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIngresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIngressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogConfig(
            self,
            request: models.DescribeLogConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeLogConfigResponse:
        """
        This API is used to query details of a log collecting configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePagedLogConfigList(
            self,
            request: models.DescribePagedLogConfigListRequest,
            opts: Dict = None,
    ) -> models.DescribePagedLogConfigListResponse:
        """
        This API is used to querying the list of log collecting configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePagedLogConfigList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePagedLogConfigListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRelatedIngresses(
            self,
            request: models.DescribeRelatedIngressesRequest,
            opts: Dict = None,
    ) -> models.DescribeRelatedIngressesResponse:
        """
        This API is used to query the list of ingress rules associated with the application.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRelatedIngresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRelatedIngressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyConfigData(
            self,
            request: models.DestroyConfigDataRequest,
            opts: Dict = None,
    ) -> models.DestroyConfigDataResponse:
        """
        This API is used to terminate a configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyConfigData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyConfigDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyEnvironment(
            self,
            request: models.DestroyEnvironmentRequest,
            opts: Dict = None,
    ) -> models.DestroyEnvironmentResponse:
        """
        This API is used to terminate an environment.
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyLogConfig(
            self,
            request: models.DestroyLogConfigRequest,
            opts: Dict = None,
    ) -> models.DestroyLogConfigResponse:
        """
        This API is used to terminate a log collecting configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyLogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyLogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableApplicationAutoscaler(
            self,
            request: models.DisableApplicationAutoscalerRequest,
            opts: Dict = None,
    ) -> models.DisableApplicationAutoscalerResponse:
        """
        This API is used to disable a scaling rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableApplicationAutoscaler"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableApplicationAutoscalerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableApplicationAutoscaler(
            self,
            request: models.EnableApplicationAutoscalerRequest,
            opts: Dict = None,
    ) -> models.EnableApplicationAutoscalerResponse:
        """
        This API is used to enable a scaling rule.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableApplicationAutoscaler"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableApplicationAutoscalerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenerateApplicationPackageDownloadUrl(
            self,
            request: models.GenerateApplicationPackageDownloadUrlRequest,
            opts: Dict = None,
    ) -> models.GenerateApplicationPackageDownloadUrlResponse:
        """
        This API is used to generate the pre-signed download URL for the specified application package.
        """
        
        kwargs = {}
        kwargs["action"] = "GenerateApplicationPackageDownloadUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenerateApplicationPackageDownloadUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplicationAutoscaler(
            self,
            request: models.ModifyApplicationAutoscalerRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationAutoscalerResponse:
        """
        This API is used to modify a scaling rule.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplicationAutoscaler"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationAutoscalerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplicationInfo(
            self,
            request: models.ModifyApplicationInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationInfoResponse:
        """
        This API is used to modify the basic information of an application.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplicationInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplicationService(
            self,
            request: models.ModifyApplicationServiceRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationServiceResponse:
        """
        This API is used to modify an access policy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplicationService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConfigData(
            self,
            request: models.ModifyConfigDataRequest,
            opts: Dict = None,
    ) -> models.ModifyConfigDataResponse:
        """
        This API is used to modify a configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConfigData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConfigDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEnvironment(
            self,
            request: models.ModifyEnvironmentRequest,
            opts: Dict = None,
    ) -> models.ModifyEnvironmentResponse:
        """
        This API is used to edit an environment.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIngress(
            self,
            request: models.ModifyIngressRequest,
            opts: Dict = None,
    ) -> models.ModifyIngressResponse:
        """
        This API is used to create or update an ingress rule.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIngress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIngressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLogConfig(
            self,
            request: models.ModifyLogConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyLogConfigResponse:
        """
        This API is used to modify a log collecting configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartApplication(
            self,
            request: models.RestartApplicationRequest,
            opts: Dict = None,
    ) -> models.RestartApplicationResponse:
        """
        This API is used to restart an application.
        """
        
        kwargs = {}
        kwargs["action"] = "RestartApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartApplicationPod(
            self,
            request: models.RestartApplicationPodRequest,
            opts: Dict = None,
    ) -> models.RestartApplicationPodResponse:
        """
        This API is used to restart an application pod.
        """
        
        kwargs = {}
        kwargs["action"] = "RestartApplicationPod"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartApplicationPodResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RollingUpdateApplicationByVersion(
            self,
            request: models.RollingUpdateApplicationByVersionRequest,
            opts: Dict = None,
    ) -> models.RollingUpdateApplicationByVersionResponse:
        """
        This API is used to configure the rolling update policy for an application.
        """
        
        kwargs = {}
        kwargs["action"] = "RollingUpdateApplicationByVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RollingUpdateApplicationByVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopApplication(
            self,
            request: models.StopApplicationRequest,
            opts: Dict = None,
    ) -> models.StopApplicationResponse:
        """
        This API is used to stop an application.
        """
        
        kwargs = {}
        kwargs["action"] = "StopApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)