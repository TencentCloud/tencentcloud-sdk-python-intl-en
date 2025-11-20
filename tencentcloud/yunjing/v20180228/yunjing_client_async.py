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
from tencentcloud.yunjing.v20180228 import models
from typing import Dict


class YunjingClient(AbstractClient):
    _apiVersion = '2018-02-28'
    _endpoint = 'yunjing.intl.tencentcloudapi.com'
    _service = 'yunjing'

    async def AddLoginWhiteList(
            self,
            request: models.AddLoginWhiteListRequest,
            opts: Dict = None,
    ) -> models.AddLoginWhiteListResponse:
        """
        This API is used to add a allowlist rule.
        """
        
        kwargs = {}
        kwargs["action"] = "AddLoginWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddLoginWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddMachineTag(
            self,
            request: models.AddMachineTagRequest,
            opts: Dict = None,
    ) -> models.AddMachineTagResponse:
        """
        This API is used to add a tag to a server.
        """
        
        kwargs = {}
        kwargs["action"] = "AddMachineTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddMachineTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseProVersion(
            self,
            request: models.CloseProVersionRequest,
            opts: Dict = None,
    ) -> models.CloseProVersionResponse:
        """
        This API is used to deactivate CWP Pro.
        """
        
        kwargs = {}
        kwargs["action"] = "CloseProVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseProVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOpenPortTask(
            self,
            request: models.CreateOpenPortTaskRequest,
            opts: Dict = None,
    ) -> models.CreateOpenPortTaskResponse:
        """
        This API is used to create a real-time port acquisition task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOpenPortTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOpenPortTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProcessTask(
            self,
            request: models.CreateProcessTaskRequest,
            opts: Dict = None,
    ) -> models.CreateProcessTaskResponse:
        """
        This API is used to create a real-time process pulling task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProcessTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProcessTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUsualLoginPlaces(
            self,
            request: models.CreateUsualLoginPlacesRequest,
            opts: Dict = None,
    ) -> models.CreateUsualLoginPlacesResponse:
        """
        This API is used to add one or more usual login locations.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUsualLoginPlaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUsualLoginPlacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBruteAttacks(
            self,
            request: models.DeleteBruteAttacksRequest,
            opts: Dict = None,
    ) -> models.DeleteBruteAttacksResponse:
        """
        This API is used to delete brute force attack records.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBruteAttacks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBruteAttacksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLoginWhiteList(
            self,
            request: models.DeleteLoginWhiteListRequest,
            opts: Dict = None,
    ) -> models.DeleteLoginWhiteListResponse:
        """
        This API is used to delete a allowlist rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLoginWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLoginWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMachine(
            self,
            request: models.DeleteMachineRequest,
            opts: Dict = None,
    ) -> models.DeleteMachineResponse:
        """
        This API is used to uninstall the CWP agent.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMachine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMachineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMachineTag(
            self,
            request: models.DeleteMachineTagRequest,
            opts: Dict = None,
    ) -> models.DeleteMachineTagResponse:
        """
        This API is used to remove a tag from a server.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMachineTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMachineTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMaliciousRequests(
            self,
            request: models.DeleteMaliciousRequestsRequest,
            opts: Dict = None,
    ) -> models.DeleteMaliciousRequestsResponse:
        """
        This API is used to delete malicious request records.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMaliciousRequests"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMaliciousRequestsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMalwares(
            self,
            request: models.DeleteMalwaresRequest,
            opts: Dict = None,
    ) -> models.DeleteMalwaresResponse:
        """
        This API is used to delete trojan records.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNonlocalLoginPlaces(
            self,
            request: models.DeleteNonlocalLoginPlacesRequest,
            opts: Dict = None,
    ) -> models.DeleteNonlocalLoginPlacesResponse:
        """
        This API is used to delete unusual login location records.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNonlocalLoginPlaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNonlocalLoginPlacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUsualLoginPlaces(
            self,
            request: models.DeleteUsualLoginPlacesRequest,
            opts: Dict = None,
    ) -> models.DeleteUsualLoginPlacesResponse:
        """
        This API is used to delete one or more usual login locations.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUsualLoginPlaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUsualLoginPlacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountStatistics(
            self,
            request: models.DescribeAccountStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountStatisticsResponse:
        """
        This API is used to get the account statistics list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccountStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccounts(
            self,
            request: models.DescribeAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountsResponse:
        """
        This API is used to get the account list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentVuls(
            self,
            request: models.DescribeAgentVulsRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentVulsResponse:
        """
        This API is used to get the list of vulnerabilities on a single server.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentVuls"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentVulsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmAttribute(
            self,
            request: models.DescribeAlarmAttributeRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmAttributeResponse:
        """
        This API is used to get the alarm settings.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBruteAttacks(
            self,
            request: models.DescribeBruteAttacksRequest,
            opts: Dict = None,
    ) -> models.DescribeBruteAttacksResponse:
        """
        This API is used to get the brute force attack event list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBruteAttacks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBruteAttacksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComponentInfo(
            self,
            request: models.DescribeComponentInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeComponentInfoResponse:
        """
        This API is used to get the component information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComponentInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComponentInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComponentStatistics(
            self,
            request: models.DescribeComponentStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeComponentStatisticsResponse:
        """
        This API is used to get the component statistics list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComponentStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComponentStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComponents(
            self,
            request: models.DescribeComponentsRequest,
            opts: Dict = None,
    ) -> models.DescribeComponentsResponse:
        """
        This API is used to get the component list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComponents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComponentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHistoryAccounts(
            self,
            request: models.DescribeHistoryAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeHistoryAccountsResponse:
        """
        This API is used to get the account change history list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHistoryAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHistoryAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImpactedHosts(
            self,
            request: models.DescribeImpactedHostsRequest,
            opts: Dict = None,
    ) -> models.DescribeImpactedHostsResponse:
        """
        This API is used to get the list of servers affected by a vulnerability.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImpactedHosts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImpactedHostsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoginWhiteList(
            self,
            request: models.DescribeLoginWhiteListRequest,
            opts: Dict = None,
    ) -> models.DescribeLoginWhiteListResponse:
        """
        This API is used to get the list of login allowlist entries.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoginWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoginWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineInfo(
            self,
            request: models.DescribeMachineInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineInfoResponse:
        """
        This API is used to get server details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachines(
            self,
            request: models.DescribeMachinesRequest,
            opts: Dict = None,
    ) -> models.DescribeMachinesResponse:
        """
        This API is used to get the list of servers in a specified region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMaliciousRequests(
            self,
            request: models.DescribeMaliciousRequestsRequest,
            opts: Dict = None,
    ) -> models.DescribeMaliciousRequestsResponse:
        """
        This API is used to get malicious request data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMaliciousRequests"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMaliciousRequestsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMalwares(
            self,
            request: models.DescribeMalwaresRequest,
            opts: Dict = None,
    ) -> models.DescribeMalwaresResponse:
        """
        This API is used to get the list of trojan events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNonlocalLoginPlaces(
            self,
            request: models.DescribeNonlocalLoginPlacesRequest,
            opts: Dict = None,
    ) -> models.DescribeNonlocalLoginPlacesResponse:
        """
        This API is used to get unusual login events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNonlocalLoginPlaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNonlocalLoginPlacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOpenPortStatistics(
            self,
            request: models.DescribeOpenPortStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeOpenPortStatisticsResponse:
        """
        This API is used to get the statistics on port usage
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOpenPortStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOpenPortStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOpenPortTaskStatus(
            self,
            request: models.DescribeOpenPortTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeOpenPortTaskStatusResponse:
        """
        This API is used to get the status of a real-time port pulling task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOpenPortTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOpenPortTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOpenPorts(
            self,
            request: models.DescribeOpenPortsRequest,
            opts: Dict = None,
    ) -> models.DescribeOpenPortsResponse:
        """
        This API is used to get the port list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOpenPorts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOpenPortsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOverviewStatistics(
            self,
            request: models.DescribeOverviewStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeOverviewStatisticsResponse:
        """
        This API is used to get the overview statistics of CWP under the current account.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOverviewStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOverviewStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProVersionInfo(
            self,
            request: models.DescribeProVersionInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeProVersionInfoResponse:
        """
        This API is used to get the CWP Pro information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProVersionInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProVersionInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProcessStatistics(
            self,
            request: models.DescribeProcessStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeProcessStatisticsResponse:
        """
        This API is used to get the process statistics list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProcessStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProcessStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProcessTaskStatus(
            self,
            request: models.DescribeProcessTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeProcessTaskStatusResponse:
        """
        This API is used to get the status of a real-time process pulling task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProcessTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProcessTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProcesses(
            self,
            request: models.DescribeProcessesRequest,
            opts: Dict = None,
    ) -> models.DescribeProcessesResponse:
        """
        This API is used to get the process list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProcesses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProcessesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityDynamics(
            self,
            request: models.DescribeSecurityDynamicsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityDynamicsResponse:
        """
        This API is used to get the security event message data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityDynamics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityDynamicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityTrends(
            self,
            request: models.DescribeSecurityTrendsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityTrendsResponse:
        """
        This API is used to get the security event statistics.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityTrends"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityTrendsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTagMachines(
            self,
            request: models.DescribeTagMachinesRequest,
            opts: Dict = None,
    ) -> models.DescribeTagMachinesResponse:
        """
        This API is used to get the information of servers associated with a specified tag.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTagMachines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagMachinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTags(
            self,
            request: models.DescribeTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeTagsResponse:
        """
        This API is used to get all server tags.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsualLoginPlaces(
            self,
            request: models.DescribeUsualLoginPlacesRequest,
            opts: Dict = None,
    ) -> models.DescribeUsualLoginPlacesResponse:
        """
        This API is used to query usual login locations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsualLoginPlaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsualLoginPlacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulInfo(
            self,
            request: models.DescribeVulInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeVulInfoResponse:
        """
        This API is used to get vulnerability details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulScanResult(
            self,
            request: models.DescribeVulScanResultRequest,
            opts: Dict = None,
    ) -> models.DescribeVulScanResultResponse:
        """
        This API is used to get the vulnerability detection result.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulScanResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulScanResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVuls(
            self,
            request: models.DescribeVulsRequest,
            opts: Dict = None,
    ) -> models.DescribeVulsResponse:
        """
        This API is used to get the vulnerability list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVuls"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWeeklyReportBruteAttacks(
            self,
            request: models.DescribeWeeklyReportBruteAttacksRequest,
            opts: Dict = None,
    ) -> models.DescribeWeeklyReportBruteAttacksResponse:
        """
        This API is used to get the brute force attack data in the weekly CWP Pro report.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWeeklyReportBruteAttacks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWeeklyReportBruteAttacksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWeeklyReportInfo(
            self,
            request: models.DescribeWeeklyReportInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeWeeklyReportInfoResponse:
        """
        This API is used to get the details in the weekly CWP Pro report.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWeeklyReportInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWeeklyReportInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWeeklyReportMalwares(
            self,
            request: models.DescribeWeeklyReportMalwaresRequest,
            opts: Dict = None,
    ) -> models.DescribeWeeklyReportMalwaresResponse:
        """
        This API is used to get the trojan data in the weekly CWP Pro report.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWeeklyReportMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWeeklyReportMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWeeklyReportNonlocalLoginPlaces(
            self,
            request: models.DescribeWeeklyReportNonlocalLoginPlacesRequest,
            opts: Dict = None,
    ) -> models.DescribeWeeklyReportNonlocalLoginPlacesResponse:
        """
        This API is used to get the unusual login location data in the weekly CWP Pro report.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWeeklyReportNonlocalLoginPlaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWeeklyReportNonlocalLoginPlacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWeeklyReportVuls(
            self,
            request: models.DescribeWeeklyReportVulsRequest,
            opts: Dict = None,
    ) -> models.DescribeWeeklyReportVulsResponse:
        """
        This API is used to get the vulnerability data in the weekly CWP Pro report.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWeeklyReportVuls"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWeeklyReportVulsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWeeklyReports(
            self,
            request: models.DescribeWeeklyReportsRequest,
            opts: Dict = None,
    ) -> models.DescribeWeeklyReportsResponse:
        """
        This API is used to get the weekly report list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWeeklyReports"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWeeklyReportsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EditTags(
            self,
            request: models.EditTagsRequest,
            opts: Dict = None,
    ) -> models.EditTagsResponse:
        """
        This API is used to add or edit tags.
        """
        
        kwargs = {}
        kwargs["action"] = "EditTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EditTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportBruteAttacks(
            self,
            request: models.ExportBruteAttacksRequest,
            opts: Dict = None,
    ) -> models.ExportBruteAttacksResponse:
        """
        This API is used to export brute force attack records into a CSV file.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportBruteAttacks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportBruteAttacksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportMaliciousRequests(
            self,
            request: models.ExportMaliciousRequestsRequest,
            opts: Dict = None,
    ) -> models.ExportMaliciousRequestsResponse:
        """
        This API is used to export the malicious request file into a CSV file for download.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportMaliciousRequests"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportMaliciousRequestsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportMalwares(
            self,
            request: models.ExportMalwaresRequest,
            opts: Dict = None,
    ) -> models.ExportMalwaresResponse:
        """
        This API is used to export trojan records into a CSV file.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportNonlocalLoginPlaces(
            self,
            request: models.ExportNonlocalLoginPlacesRequest,
            opts: Dict = None,
    ) -> models.ExportNonlocalLoginPlacesResponse:
        """
        This API is used to export unusual login location events into a CSV file.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportNonlocalLoginPlaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportNonlocalLoginPlacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IgnoreImpactedHosts(
            self,
            request: models.IgnoreImpactedHostsRequest,
            opts: Dict = None,
    ) -> models.IgnoreImpactedHostsResponse:
        """
        This API is used to ignore one or more vulnerabilities.
        """
        
        kwargs = {}
        kwargs["action"] = "IgnoreImpactedHosts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IgnoreImpactedHostsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MisAlarmNonlocalLoginPlaces(
            self,
            request: models.MisAlarmNonlocalLoginPlacesRequest,
            opts: Dict = None,
    ) -> models.MisAlarmNonlocalLoginPlacesResponse:
        """
        This API is used to set the current location as the usual login location.
        """
        
        kwargs = {}
        kwargs["action"] = "MisAlarmNonlocalLoginPlaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MisAlarmNonlocalLoginPlacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAlarmAttribute(
            self,
            request: models.ModifyAlarmAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyAlarmAttributeResponse:
        """
        This API is used to modify alarm settings.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAlarmAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAlarmAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAutoOpenProVersionConfig(
            self,
            request: models.ModifyAutoOpenProVersionConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyAutoOpenProVersionConfigResponse:
        """
        This API is used to set whether to automatically activate CWP Pro for newly added servers.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAutoOpenProVersionConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAutoOpenProVersionConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoginWhiteList(
            self,
            request: models.ModifyLoginWhiteListRequest,
            opts: Dict = None,
    ) -> models.ModifyLoginWhiteListResponse:
        """
        This API is used to edit a allowlist rule.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoginWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoginWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProVersionRenewFlag(
            self,
            request: models.ModifyProVersionRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifyProVersionRenewFlagResponse:
        """
        This API is used to modify the renewal flag of CWP Pro.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProVersionRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProVersionRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenProVersion(
            self,
            request: models.OpenProVersionRequest,
            opts: Dict = None,
    ) -> models.OpenProVersionResponse:
        """
        This API is used to activate CWP Pro.
        """
        
        kwargs = {}
        kwargs["action"] = "OpenProVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenProVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecoverMalwares(
            self,
            request: models.RecoverMalwaresRequest,
            opts: Dict = None,
    ) -> models.RecoverMalwaresResponse:
        """
        This API is used to recover isolated trojan files in a batch.
        """
        
        kwargs = {}
        kwargs["action"] = "RecoverMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecoverMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RescanImpactedHost(
            self,
            request: models.RescanImpactedHostRequest,
            opts: Dict = None,
    ) -> models.RescanImpactedHostResponse:
        """
        This API is used to re-scan for vulnerabilities.
        """
        
        kwargs = {}
        kwargs["action"] = "RescanImpactedHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RescanImpactedHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SeparateMalwares(
            self,
            request: models.SeparateMalwaresRequest,
            opts: Dict = None,
    ) -> models.SeparateMalwaresResponse:
        """
        This API is used to isolate trojans.
        """
        
        kwargs = {}
        kwargs["action"] = "SeparateMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SeparateMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TrustMaliciousRequest(
            self,
            request: models.TrustMaliciousRequestRequest,
            opts: Dict = None,
    ) -> models.TrustMaliciousRequestResponse:
        """
        This API is used to trust a malicious request.
        """
        
        kwargs = {}
        kwargs["action"] = "TrustMaliciousRequest"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TrustMaliciousRequestResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TrustMalwares(
            self,
            request: models.TrustMalwaresRequest,
            opts: Dict = None,
    ) -> models.TrustMalwaresResponse:
        """
        This API is used to trust an identified trojan file.
        """
        
        kwargs = {}
        kwargs["action"] = "TrustMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TrustMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UntrustMaliciousRequest(
            self,
            request: models.UntrustMaliciousRequestRequest,
            opts: Dict = None,
    ) -> models.UntrustMaliciousRequestResponse:
        """
        This API is used to untrust a malicious request.
        """
        
        kwargs = {}
        kwargs["action"] = "UntrustMaliciousRequest"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UntrustMaliciousRequestResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UntrustMalwares(
            self,
            request: models.UntrustMalwaresRequest,
            opts: Dict = None,
    ) -> models.UntrustMalwaresResponse:
        """
        This API is used to untrust a trojan file.
        """
        
        kwargs = {}
        kwargs["action"] = "UntrustMalwares"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UntrustMalwaresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)