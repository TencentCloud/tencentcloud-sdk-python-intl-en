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
from tencentcloud.cfw.v20190904 import models


class CfwClient(AbstractClient):
    _apiVersion = '2019-09-04'
    _endpoint = 'cfw.intl.tencentcloudapi.com'
    _service = 'cfw'


    def AddAcRule(self, request):
        """This API is used to add edge firewall rules.

        :param request: Request instance for AddAcRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.AddAcRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.AddAcRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddAcRule", params, headers=headers)
            response = json.loads(body)
            model = models.AddAcRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddEnterpriseSecurityGroupRules(self, request):
        """This API is used to create enterprise security group rules (new).

        :param request: Request instance for AddEnterpriseSecurityGroupRules.
        :type request: :class:`tencentcloud.cfw.v20190904.models.AddEnterpriseSecurityGroupRulesRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.AddEnterpriseSecurityGroupRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddEnterpriseSecurityGroupRules", params, headers=headers)
            response = json.loads(body)
            model = models.AddEnterpriseSecurityGroupRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddNatAcRule(self, request):
        """This API is used to add NAT access control rules.

        :param request: Request instance for AddNatAcRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.AddNatAcRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.AddNatAcRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddNatAcRule", params, headers=headers)
            response = json.loads(body)
            model = models.AddNatAcRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAcRules(self, request):
        """This API is used to create access control rules.

        :param request: Request instance for CreateAcRules.
        :type request: :class:`tencentcloud.cfw.v20190904.models.CreateAcRulesRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CreateAcRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAcRules", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAcRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNatFwInstance(self, request):
        """This API is used to create a NAT firewall instance (The Region parameter is required).

        :param request: Request instance for CreateNatFwInstance.
        :type request: :class:`tencentcloud.cfw.v20190904.models.CreateNatFwInstanceRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CreateNatFwInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNatFwInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNatFwInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNatFwInstanceWithDomain(self, request):
        """This API is used to create a firewall instance with domain name (The Region parameter is required).

        :param request: Request instance for CreateNatFwInstanceWithDomain.
        :type request: :class:`tencentcloud.cfw.v20190904.models.CreateNatFwInstanceWithDomainRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CreateNatFwInstanceWithDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNatFwInstanceWithDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNatFwInstanceWithDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityGroupRules(self, request):
        """This API is used to create enterprise security group rules.

        :param request: Request instance for CreateSecurityGroupRules.
        :type request: :class:`tencentcloud.cfw.v20190904.models.CreateSecurityGroupRulesRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CreateSecurityGroupRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityGroupRules", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityGroupRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAcRule(self, request):
        """This API is used to delete a rule.

        :param request: Request instance for DeleteAcRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DeleteAcRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DeleteAcRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAcRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAcRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAllAccessControlRule(self, request):
        """This API is used to delete all rules.

        :param request: Request instance for DeleteAllAccessControlRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DeleteAllAccessControlRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DeleteAllAccessControlRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAllAccessControlRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAllAccessControlRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteResourceGroup(self, request):
        """This API is used to delete asset groups in Asset Management.

        :param request: Request instance for DeleteResourceGroup.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DeleteResourceGroupRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DeleteResourceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteResourceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteResourceGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSecurityGroupRule(self, request):
        """This API is used to delete security group rules.

        :param request: Request instance for DeleteSecurityGroupRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DeleteSecurityGroupRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DeleteSecurityGroupRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityGroupRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityGroupRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVpcInstance(self, request):
        """This API is used to delete firewall instance.

        :param request: Request instance for DeleteVpcInstance.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DeleteVpcInstanceRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DeleteVpcInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVpcInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVpcInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAcLists(self, request):
        """This API is used to get the access control list.

        :param request: Request instance for DescribeAcLists.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeAcListsRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeAcListsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAcLists", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAcListsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssociatedInstanceList(self, request):
        """This API is used to get the list of instances associated with a security group.

        :param request: Request instance for DescribeAssociatedInstanceList.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeAssociatedInstanceListRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeAssociatedInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssociatedInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssociatedInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBlockByIpTimesList(self, request):
        """This API is used to get blocked IP data.

        :param request: Request instance for DescribeBlockByIpTimesList.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeBlockByIpTimesListRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeBlockByIpTimesListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBlockByIpTimesList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBlockByIpTimesListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBlockIgnoreList(self, request):
        """This API is used to get allowlists or blocklists for intrusion prevention.

        :param request: Request instance for DescribeBlockIgnoreList.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeBlockIgnoreListRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeBlockIgnoreListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBlockIgnoreList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBlockIgnoreListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBlockStaticList(self, request):
        """This API is used to get the most frequent attacker.

        :param request: Request instance for DescribeBlockStaticList.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeBlockStaticListRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeBlockStaticListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBlockStaticList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBlockStaticListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDefenseSwitch(self, request):
        """This API is used to query the list of firewall toggles with Intrusion Defense enabled.

        :param request: Request instance for DescribeDefenseSwitch.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeDefenseSwitchRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeDefenseSwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDefenseSwitch", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDefenseSwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnterpriseSecurityGroupRule(self, request):
        """This API is used to get enterprise security group rules (new).

        :param request: Request instance for DescribeEnterpriseSecurityGroupRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeEnterpriseSecurityGroupRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeEnterpriseSecurityGroupRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnterpriseSecurityGroupRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnterpriseSecurityGroupRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGuideScanInfo(self, request):
        """This API is used to get the scan interface information in Get Started.

        :param request: Request instance for DescribeGuideScanInfo.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeGuideScanInfoRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeGuideScanInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGuideScanInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGuideScanInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIPStatusList(self, request):
        """This API is used to get the IP protection status.

        :param request: Request instance for DescribeIPStatusList.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeIPStatusListRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeIPStatusListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIPStatusList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIPStatusListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNatAcRule(self, request):
        """This API is used to get the NAT access control list.

        :param request: Request instance for DescribeNatAcRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeNatAcRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeNatAcRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatAcRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatAcRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNatFwInfoCount(self, request):
        """This API is used to get the number of a user's subnets connected to NAT firewall and the number of NAT firewall instances.

        :param request: Request instance for DescribeNatFwInfoCount.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeNatFwInfoCountRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeNatFwInfoCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatFwInfoCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatFwInfoCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNatFwInstance(self, request):
        """This API is used to get all NAT instances of a tenant.

        :param request: Request instance for DescribeNatFwInstance.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeNatFwInstanceRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeNatFwInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatFwInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatFwInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNatFwInstanceWithRegion(self, request):
        """This API is used to get the NAT instance with the region that is newly maintained by the tenant.

        :param request: Request instance for DescribeNatFwInstanceWithRegion.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeNatFwInstanceWithRegionRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeNatFwInstanceWithRegionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatFwInstanceWithRegion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatFwInstanceWithRegionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNatFwInstancesInfo(self, request):
        """This API is used to get all NAT instances and instance card information of a tenant.

        :param request: Request instance for DescribeNatFwInstancesInfo.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeNatFwInstancesInfoRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeNatFwInstancesInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatFwInstancesInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatFwInstancesInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNatFwVpcDnsLst(self, request):
        """This API is used to get the VPC DNS status of NAT firewall instances.

        :param request: Request instance for DescribeNatFwVpcDnsLst.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeNatFwVpcDnsLstRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeNatFwVpcDnsLstResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatFwVpcDnsLst", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatFwVpcDnsLstResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceGroupNew(self, request):
        """This API is used to get the asset tree information in Asset Management.

        :param request: Request instance for DescribeResourceGroupNew.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeResourceGroupNewRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeResourceGroupNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceGroupNew", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceGroupNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleOverview(self, request):
        """This API is used to get the rule list overview.

        :param request: Request instance for DescribeRuleOverview.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeRuleOverviewRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeRuleOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityGroupList(self, request):
        """This API is used to get the security group rule list.

        :param request: Request instance for DescribeSecurityGroupList.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeSecurityGroupListRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeSecurityGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSourceAsset(self, request):
        """This API is used to get all asset information of an asset group.

        :param request: Request instance for DescribeSourceAsset.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeSourceAssetRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeSourceAssetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSourceAsset", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSourceAssetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSwitchLists(self, request):
        """This API is used to get the firewall status list.

        :param request: Request instance for DescribeSwitchLists.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeSwitchListsRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeSwitchListsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSwitchLists", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSwitchListsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTLogInfo(self, request):
        """This API is used to get the current alert monitoring data.

        :param request: Request instance for DescribeTLogInfo.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeTLogInfoRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeTLogInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTLogInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTLogInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTLogIpList(self, request):
        """This API is used to get the most frequent attacker IP.

        :param request: Request instance for DescribeTLogIpList.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeTLogIpListRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeTLogIpListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTLogIpList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTLogIpListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTableStatus(self, request):
        """This API is used to get the rule list status.

        :param request: Request instance for DescribeTableStatus.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeTableStatusRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeTableStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUnHandleEventTabList(self, request):
        """This API is used to get unhandled security events.

        :param request: Request instance for DescribeUnHandleEventTabList.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeUnHandleEventTabListRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeUnHandleEventTabListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUnHandleEventTabList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUnHandleEventTabListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcAcRule(self, request):
        """Query Inter-VPC rules

        :param request: Request instance for DescribeVpcAcRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeVpcAcRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeVpcAcRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcAcRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcAcRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExpandCfwVertical(self, request):
        """This API is used to increase the firewall bandwidth.

        :param request: Request instance for ExpandCfwVertical.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ExpandCfwVerticalRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ExpandCfwVerticalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExpandCfwVertical", params, headers=headers)
            response = json.loads(body)
            model = models.ExpandCfwVerticalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAcRule(self, request):
        """This API is used to modify rules.

        :param request: Request instance for ModifyAcRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyAcRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyAcRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAcRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAcRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAllPublicIPSwitchStatus(self, request):
        """This API is used to enable or disable one or multiple edge firewalls.

        :param request: Request instance for ModifyAllPublicIPSwitchStatus.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyAllPublicIPSwitchStatusRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyAllPublicIPSwitchStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAllPublicIPSwitchStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAllPublicIPSwitchStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAllRuleStatus(self, request):
        """This API is used to enable or disable all rules.

        :param request: Request instance for ModifyAllRuleStatus.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyAllRuleStatusRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyAllRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAllRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAllRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAllVPCSwitchStatus(self, request):
        """This API is used to enable or disable one or multiple VPC firewalls.

        :param request: Request instance for ModifyAllVPCSwitchStatus.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyAllVPCSwitchStatusRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyAllVPCSwitchStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAllVPCSwitchStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAllVPCSwitchStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAssetScan(self, request):
        """This API is used to modify asset scan settings.

        :param request: Request instance for ModifyAssetScan.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyAssetScanRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyAssetScanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAssetScan", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAssetScanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBlockIgnoreList(self, request):
        """This API is used to manage blocked/allowed IPs and domains.
        Add IPs/domains to the blocked/allowed list
        Remove IPs/domains from the blocked/allowed list
        Modify events related with the IPs/domains in the blocked/allowed list

        :param request: Request instance for ModifyBlockIgnoreList.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyBlockIgnoreListRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyBlockIgnoreListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBlockIgnoreList", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBlockIgnoreListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBlockTop(self, request):
        """This API is used to pin or unpin a blocking log.

        :param request: Request instance for ModifyBlockTop.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyBlockTopRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyBlockTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBlockTop", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBlockTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEnterpriseSecurityDispatchStatus(self, request):
        """This API is used to modify the publishing status of an enterprise security group.

        :param request: Request instance for ModifyEnterpriseSecurityDispatchStatus.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyEnterpriseSecurityDispatchStatusRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyEnterpriseSecurityDispatchStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEnterpriseSecurityDispatchStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEnterpriseSecurityDispatchStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEnterpriseSecurityGroupRule(self, request):
        """This API is used to modify a new enterprise security group rule.

        :param request: Request instance for ModifyEnterpriseSecurityGroupRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyEnterpriseSecurityGroupRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyEnterpriseSecurityGroupRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEnterpriseSecurityGroupRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEnterpriseSecurityGroupRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNatAcRule(self, request):
        """This API is used to modify NAT access control rules.

        :param request: Request instance for ModifyNatAcRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyNatAcRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyNatAcRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNatAcRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNatAcRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNatFwReSelect(self, request):
        """This API is used to get the VPC or NAT list for changing associated firewall instances.

        :param request: Request instance for ModifyNatFwReSelect.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyNatFwReSelectRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyNatFwReSelectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNatFwReSelect", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNatFwReSelectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNatFwSwitch(self, request):
        """This API is used to enable or disable a NAT firewall.

        :param request: Request instance for ModifyNatFwSwitch.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyNatFwSwitchRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyNatFwSwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNatFwSwitch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNatFwSwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNatFwVpcDnsSwitch(self, request):
        """This API is used to modify the VPC DNS status of NAT firewall instances.

        :param request: Request instance for ModifyNatFwVpcDnsSwitch.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyNatFwVpcDnsSwitchRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyNatFwVpcDnsSwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNatFwVpcDnsSwitch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNatFwVpcDnsSwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNatSequenceRules(self, request):
        """This API is used to change the sequence number of NAT firewall rules.

        :param request: Request instance for ModifyNatSequenceRules.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyNatSequenceRulesRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyNatSequenceRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNatSequenceRules", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNatSequenceRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPublicIPSwitchStatus(self, request):
        """This API is used to enable or disable an edge firewall.

        :param request: Request instance for ModifyPublicIPSwitchStatus.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyPublicIPSwitchStatusRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyPublicIPSwitchStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPublicIPSwitchStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPublicIPSwitchStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourceGroup(self, request):
        """This API is used to modify the asset group information in Asset Management.


        :param request: Request instance for ModifyResourceGroup.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyResourceGroupRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyResourceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourceGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRunSyncAsset(self, request):
        """This API is used to sync assets - Internet & VPC (new).

        :param request: Request instance for ModifyRunSyncAsset.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyRunSyncAssetRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyRunSyncAssetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRunSyncAsset", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRunSyncAssetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityGroupItemRuleStatus(self, request):
        """This API is used to enable or disable an enterprise security group rule.

        :param request: Request instance for ModifySecurityGroupItemRuleStatus.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifySecurityGroupItemRuleStatusRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifySecurityGroupItemRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityGroupItemRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityGroupItemRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityGroupSequenceRules(self, request):
        """This API is used to sort enterprise security group rules.

        :param request: Request instance for ModifySecurityGroupSequenceRules.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifySecurityGroupSequenceRulesRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifySecurityGroupSequenceRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityGroupSequenceRules", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityGroupSequenceRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySequenceRules(self, request):
        """This API is used to modify rule priority.

        :param request: Request instance for ModifySequenceRules.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifySequenceRulesRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifySequenceRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySequenceRules", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySequenceRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyStorageSetting(self, request):
        """This API is used to modify the log retention period or to clear logs.

        :param request: Request instance for ModifyStorageSetting.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyStorageSettingRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyStorageSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStorageSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStorageSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTableStatus(self, request):
        """This API is used to modify rule list status.

        :param request: Request instance for ModifyTableStatus.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyTableStatusRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyTableStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTableStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTableStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveAcRule(self, request):
        """This API is used to delete edge firewall rules.

        :param request: Request instance for RemoveAcRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.RemoveAcRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.RemoveAcRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveAcRule", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveAcRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveEnterpriseSecurityGroupRule(self, request):
        """This API is used to delete enterprise security group rules (new).

        :param request: Request instance for RemoveEnterpriseSecurityGroupRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.RemoveEnterpriseSecurityGroupRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.RemoveEnterpriseSecurityGroupRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveEnterpriseSecurityGroupRule", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveEnterpriseSecurityGroupRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveNatAcRule(self, request):
        """This API is used to delete NAT access control rules.

        :param request: Request instance for RemoveNatAcRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.RemoveNatAcRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.RemoveNatAcRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveNatAcRule", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveNatAcRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetNatFwDnatRule(self, request):
        """This API is used to configure firewall DNAT rules.

        :param request: Request instance for SetNatFwDnatRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.SetNatFwDnatRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.SetNatFwDnatRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetNatFwDnatRule", params, headers=headers)
            response = json.loads(body)
            model = models.SetNatFwDnatRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetNatFwEip(self, request):
        """This API is used to set the firewall instance EIP. (Available for firewall instances in the "Create new" mode. only)

        :param request: Request instance for SetNatFwEip.
        :type request: :class:`tencentcloud.cfw.v20190904.models.SetNatFwEipRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.SetNatFwEipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetNatFwEip", params, headers=headers)
            response = json.loads(body)
            model = models.SetNatFwEipResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopSecurityGroupRuleDispatch(self, request):
        """This API is used to stop publishing security group rules.

        :param request: Request instance for StopSecurityGroupRuleDispatch.
        :type request: :class:`tencentcloud.cfw.v20190904.models.StopSecurityGroupRuleDispatchRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.StopSecurityGroupRuleDispatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopSecurityGroupRuleDispatch", params, headers=headers)
            response = json.loads(body)
            model = models.StopSecurityGroupRuleDispatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))