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
from tencentcloud.cfw.v20190904 import models
from typing import Dict


class CfwClient(AbstractClient):
    _apiVersion = '2019-09-04'
    _endpoint = 'cfw.intl.tencentcloudapi.com'
    _service = 'cfw'

    async def AddAcRule(
            self,
            request: models.AddAcRuleRequest,
            opts: Dict = None,
    ) -> models.AddAcRuleResponse:
        """
        This API is used to add edge firewall rules.
        """
        
        kwargs = {}
        kwargs["action"] = "AddAcRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddAcRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddEnterpriseSecurityGroupRules(
            self,
            request: models.AddEnterpriseSecurityGroupRulesRequest,
            opts: Dict = None,
    ) -> models.AddEnterpriseSecurityGroupRulesResponse:
        """
        This API is used to create enterprise security group rules (new).
        """
        
        kwargs = {}
        kwargs["action"] = "AddEnterpriseSecurityGroupRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddEnterpriseSecurityGroupRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddNatAcRule(
            self,
            request: models.AddNatAcRuleRequest,
            opts: Dict = None,
    ) -> models.AddNatAcRuleResponse:
        """
        This API is used to add NAT access control rules.
        """
        
        kwargs = {}
        kwargs["action"] = "AddNatAcRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddNatAcRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAcRules(
            self,
            request: models.CreateAcRulesRequest,
            opts: Dict = None,
    ) -> models.CreateAcRulesResponse:
        """
        This API is used to create access control rules.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAcRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAcRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNatFwInstance(
            self,
            request: models.CreateNatFwInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateNatFwInstanceResponse:
        """
        This API is used to create a NAT firewall instance (The Region parameter is required).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNatFwInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNatFwInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNatFwInstanceWithDomain(
            self,
            request: models.CreateNatFwInstanceWithDomainRequest,
            opts: Dict = None,
    ) -> models.CreateNatFwInstanceWithDomainResponse:
        """
        This API is used to create a firewall instance with domain name (The Region parameter is required).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNatFwInstanceWithDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNatFwInstanceWithDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityGroupRules(
            self,
            request: models.CreateSecurityGroupRulesRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityGroupRulesResponse:
        """
        This API is used to create enterprise security group rules.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityGroupRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityGroupRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAcRule(
            self,
            request: models.DeleteAcRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteAcRuleResponse:
        """
        This API is used to delete a rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAcRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAcRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAllAccessControlRule(
            self,
            request: models.DeleteAllAccessControlRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteAllAccessControlRuleResponse:
        """
        This API is used to delete all rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAllAccessControlRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAllAccessControlRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteResourceGroup(
            self,
            request: models.DeleteResourceGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteResourceGroupResponse:
        """
        This API is used to delete asset groups in Asset Management.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteResourceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteResourceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityGroupRule(
            self,
            request: models.DeleteSecurityGroupRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityGroupRuleResponse:
        """
        This API is used to delete security group rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityGroupRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityGroupRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVpcInstance(
            self,
            request: models.DeleteVpcInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteVpcInstanceResponse:
        """
        This API is used to delete firewall instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVpcInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVpcInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAcLists(
            self,
            request: models.DescribeAcListsRequest,
            opts: Dict = None,
    ) -> models.DescribeAcListsResponse:
        """
        This API is used to get the access control list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAcLists"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAcListsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssociatedInstanceList(
            self,
            request: models.DescribeAssociatedInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssociatedInstanceListResponse:
        """
        This API is used to get the list of instances associated with a security group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssociatedInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssociatedInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBlockByIpTimesList(
            self,
            request: models.DescribeBlockByIpTimesListRequest,
            opts: Dict = None,
    ) -> models.DescribeBlockByIpTimesListResponse:
        """
        This API is used to get blocked IP data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBlockByIpTimesList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBlockByIpTimesListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBlockIgnoreList(
            self,
            request: models.DescribeBlockIgnoreListRequest,
            opts: Dict = None,
    ) -> models.DescribeBlockIgnoreListResponse:
        """
        This API is used to get allowlists or blocklists for intrusion prevention.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBlockIgnoreList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBlockIgnoreListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBlockStaticList(
            self,
            request: models.DescribeBlockStaticListRequest,
            opts: Dict = None,
    ) -> models.DescribeBlockStaticListResponse:
        """
        This API is used to get the most frequent attacker.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBlockStaticList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBlockStaticListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDefenseSwitch(
            self,
            request: models.DescribeDefenseSwitchRequest,
            opts: Dict = None,
    ) -> models.DescribeDefenseSwitchResponse:
        """
        This API is used to query the list of firewall toggles with Intrusion Defense enabled.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDefenseSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDefenseSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnterpriseSecurityGroupRule(
            self,
            request: models.DescribeEnterpriseSecurityGroupRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeEnterpriseSecurityGroupRuleResponse:
        """
        This API is used to get enterprise security group rules (new).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnterpriseSecurityGroupRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnterpriseSecurityGroupRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGuideScanInfo(
            self,
            request: models.DescribeGuideScanInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeGuideScanInfoResponse:
        """
        This API is used to get the scan interface information in Get Started.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGuideScanInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGuideScanInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIPStatusList(
            self,
            request: models.DescribeIPStatusListRequest,
            opts: Dict = None,
    ) -> models.DescribeIPStatusListResponse:
        """
        This API is used to get the IP protection status.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIPStatusList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIPStatusListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatAcRule(
            self,
            request: models.DescribeNatAcRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeNatAcRuleResponse:
        """
        This API is used to get the NAT access control list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatAcRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatAcRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatFwInfoCount(
            self,
            request: models.DescribeNatFwInfoCountRequest,
            opts: Dict = None,
    ) -> models.DescribeNatFwInfoCountResponse:
        """
        This API is used to get the number of a user's subnets connected to NAT firewall and the number of NAT firewall instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatFwInfoCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatFwInfoCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatFwInstance(
            self,
            request: models.DescribeNatFwInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeNatFwInstanceResponse:
        """
        This API is used to get all NAT instances of a tenant.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatFwInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatFwInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatFwInstanceWithRegion(
            self,
            request: models.DescribeNatFwInstanceWithRegionRequest,
            opts: Dict = None,
    ) -> models.DescribeNatFwInstanceWithRegionResponse:
        """
        This API is used to get the NAT instance with the region that is newly maintained by the tenant.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatFwInstanceWithRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatFwInstanceWithRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatFwInstancesInfo(
            self,
            request: models.DescribeNatFwInstancesInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeNatFwInstancesInfoResponse:
        """
        This API is used to get all NAT instances and instance card information of a tenant.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatFwInstancesInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatFwInstancesInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatFwVpcDnsLst(
            self,
            request: models.DescribeNatFwVpcDnsLstRequest,
            opts: Dict = None,
    ) -> models.DescribeNatFwVpcDnsLstResponse:
        """
        This API is used to get the VPC DNS status of NAT firewall instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatFwVpcDnsLst"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatFwVpcDnsLstResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceGroupNew(
            self,
            request: models.DescribeResourceGroupNewRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceGroupNewResponse:
        """
        This API is used to get the asset tree information in Asset Management.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceGroupNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceGroupNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleOverview(
            self,
            request: models.DescribeRuleOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleOverviewResponse:
        """
        This API is used to get the rule list overview.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroupList(
            self,
            request: models.DescribeSecurityGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupListResponse:
        """
        This API is used to get the security group rule list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSourceAsset(
            self,
            request: models.DescribeSourceAssetRequest,
            opts: Dict = None,
    ) -> models.DescribeSourceAssetResponse:
        """
        This API is used to get all asset information of an asset group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSourceAsset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSourceAssetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSwitchLists(
            self,
            request: models.DescribeSwitchListsRequest,
            opts: Dict = None,
    ) -> models.DescribeSwitchListsResponse:
        """
        This API is used to get the firewall status list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSwitchLists"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSwitchListsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTLogInfo(
            self,
            request: models.DescribeTLogInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeTLogInfoResponse:
        """
        This API is used to get the current alert monitoring data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTLogInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTLogInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTLogIpList(
            self,
            request: models.DescribeTLogIpListRequest,
            opts: Dict = None,
    ) -> models.DescribeTLogIpListResponse:
        """
        This API is used to get the most frequent attacker IP.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTLogIpList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTLogIpListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableStatus(
            self,
            request: models.DescribeTableStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeTableStatusResponse:
        """
        This API is used to get the rule list status.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUnHandleEventTabList(
            self,
            request: models.DescribeUnHandleEventTabListRequest,
            opts: Dict = None,
    ) -> models.DescribeUnHandleEventTabListResponse:
        """
        This API is used to get unhandled security events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUnHandleEventTabList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUnHandleEventTabListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcAcRule(
            self,
            request: models.DescribeVpcAcRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcAcRuleResponse:
        """
        Query Inter-VPC rules
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcAcRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcAcRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExpandCfwVertical(
            self,
            request: models.ExpandCfwVerticalRequest,
            opts: Dict = None,
    ) -> models.ExpandCfwVerticalResponse:
        """
        This API is used to increase the firewall bandwidth.
        """
        
        kwargs = {}
        kwargs["action"] = "ExpandCfwVertical"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExpandCfwVerticalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAcRule(
            self,
            request: models.ModifyAcRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyAcRuleResponse:
        """
        This API is used to modify rules.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAcRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAcRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAllPublicIPSwitchStatus(
            self,
            request: models.ModifyAllPublicIPSwitchStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyAllPublicIPSwitchStatusResponse:
        """
        This API is used to enable or disable one or multiple edge firewalls.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAllPublicIPSwitchStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAllPublicIPSwitchStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAllRuleStatus(
            self,
            request: models.ModifyAllRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyAllRuleStatusResponse:
        """
        This API is used to enable or disable all rules.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAllRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAllRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAllVPCSwitchStatus(
            self,
            request: models.ModifyAllVPCSwitchStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyAllVPCSwitchStatusResponse:
        """
        This API is used to enable or disable one or multiple VPC firewalls.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAllVPCSwitchStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAllVPCSwitchStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAssetScan(
            self,
            request: models.ModifyAssetScanRequest,
            opts: Dict = None,
    ) -> models.ModifyAssetScanResponse:
        """
        This API is used to modify asset scan settings.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAssetScan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAssetScanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBlockIgnoreList(
            self,
            request: models.ModifyBlockIgnoreListRequest,
            opts: Dict = None,
    ) -> models.ModifyBlockIgnoreListResponse:
        """
        This API is used to manage blocked/allowed IPs and domains.
        Add IPs/domains to the blocked/allowed list
        Remove IPs/domains from the blocked/allowed list
        Modify events related with the IPs/domains in the blocked/allowed list
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBlockIgnoreList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBlockIgnoreListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBlockTop(
            self,
            request: models.ModifyBlockTopRequest,
            opts: Dict = None,
    ) -> models.ModifyBlockTopResponse:
        """
        This API is used to pin or unpin a blocking log.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBlockTop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBlockTopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEnterpriseSecurityDispatchStatus(
            self,
            request: models.ModifyEnterpriseSecurityDispatchStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyEnterpriseSecurityDispatchStatusResponse:
        """
        This API is used to modify the publishing status of an enterprise security group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEnterpriseSecurityDispatchStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEnterpriseSecurityDispatchStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEnterpriseSecurityGroupRule(
            self,
            request: models.ModifyEnterpriseSecurityGroupRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyEnterpriseSecurityGroupRuleResponse:
        """
        This API is used to modify a new enterprise security group rule.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEnterpriseSecurityGroupRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEnterpriseSecurityGroupRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNatAcRule(
            self,
            request: models.ModifyNatAcRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyNatAcRuleResponse:
        """
        This API is used to modify NAT access control rules.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNatAcRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNatAcRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNatFwReSelect(
            self,
            request: models.ModifyNatFwReSelectRequest,
            opts: Dict = None,
    ) -> models.ModifyNatFwReSelectResponse:
        """
        This API is used to get the VPC or NAT list for changing associated firewall instances.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNatFwReSelect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNatFwReSelectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNatFwSwitch(
            self,
            request: models.ModifyNatFwSwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyNatFwSwitchResponse:
        """
        This API is used to enable or disable a NAT firewall.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNatFwSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNatFwSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNatFwVpcDnsSwitch(
            self,
            request: models.ModifyNatFwVpcDnsSwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyNatFwVpcDnsSwitchResponse:
        """
        This API is used to modify the VPC DNS status of NAT firewall instances.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNatFwVpcDnsSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNatFwVpcDnsSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNatSequenceRules(
            self,
            request: models.ModifyNatSequenceRulesRequest,
            opts: Dict = None,
    ) -> models.ModifyNatSequenceRulesResponse:
        """
        This API is used to change the sequence number of NAT firewall rules.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNatSequenceRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNatSequenceRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPublicIPSwitchStatus(
            self,
            request: models.ModifyPublicIPSwitchStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyPublicIPSwitchStatusResponse:
        """
        This API is used to enable or disable an edge firewall.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPublicIPSwitchStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPublicIPSwitchStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResourceGroup(
            self,
            request: models.ModifyResourceGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyResourceGroupResponse:
        """
        This API is used to modify the asset group information in Asset Management.

        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResourceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRunSyncAsset(
            self,
            request: models.ModifyRunSyncAssetRequest,
            opts: Dict = None,
    ) -> models.ModifyRunSyncAssetResponse:
        """
        This API is used to sync assets - Internet & VPC (new).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRunSyncAsset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRunSyncAssetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityGroupItemRuleStatus(
            self,
            request: models.ModifySecurityGroupItemRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityGroupItemRuleStatusResponse:
        """
        This API is used to enable or disable an enterprise security group rule.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityGroupItemRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityGroupItemRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityGroupSequenceRules(
            self,
            request: models.ModifySecurityGroupSequenceRulesRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityGroupSequenceRulesResponse:
        """
        This API is used to sort enterprise security group rules.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityGroupSequenceRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityGroupSequenceRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySequenceRules(
            self,
            request: models.ModifySequenceRulesRequest,
            opts: Dict = None,
    ) -> models.ModifySequenceRulesResponse:
        """
        This API is used to modify rule priority.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySequenceRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySequenceRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStorageSetting(
            self,
            request: models.ModifyStorageSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyStorageSettingResponse:
        """
        This API is used to modify the log retention period or to clear logs.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStorageSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStorageSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTableStatus(
            self,
            request: models.ModifyTableStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyTableStatusResponse:
        """
        This API is used to modify rule list status.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTableStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTableStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveAcRule(
            self,
            request: models.RemoveAcRuleRequest,
            opts: Dict = None,
    ) -> models.RemoveAcRuleResponse:
        """
        This API is used to delete edge firewall rules.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveAcRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveAcRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveEnterpriseSecurityGroupRule(
            self,
            request: models.RemoveEnterpriseSecurityGroupRuleRequest,
            opts: Dict = None,
    ) -> models.RemoveEnterpriseSecurityGroupRuleResponse:
        """
        This API is used to delete enterprise security group rules (new).
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveEnterpriseSecurityGroupRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveEnterpriseSecurityGroupRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveNatAcRule(
            self,
            request: models.RemoveNatAcRuleRequest,
            opts: Dict = None,
    ) -> models.RemoveNatAcRuleResponse:
        """
        This API is used to delete NAT access control rules.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveNatAcRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveNatAcRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetNatFwDnatRule(
            self,
            request: models.SetNatFwDnatRuleRequest,
            opts: Dict = None,
    ) -> models.SetNatFwDnatRuleResponse:
        """
        This API is used to configure firewall DNAT rules.
        """
        
        kwargs = {}
        kwargs["action"] = "SetNatFwDnatRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetNatFwDnatRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetNatFwEip(
            self,
            request: models.SetNatFwEipRequest,
            opts: Dict = None,
    ) -> models.SetNatFwEipResponse:
        """
        This API is used to set the firewall instance EIP. (Available for firewall instances in the "Create new" mode. only)
        """
        
        kwargs = {}
        kwargs["action"] = "SetNatFwEip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetNatFwEipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopSecurityGroupRuleDispatch(
            self,
            request: models.StopSecurityGroupRuleDispatchRequest,
            opts: Dict = None,
    ) -> models.StopSecurityGroupRuleDispatchResponse:
        """
        This API is used to stop publishing security group rules.
        """
        
        kwargs = {}
        kwargs["action"] = "StopSecurityGroupRuleDispatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopSecurityGroupRuleDispatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)