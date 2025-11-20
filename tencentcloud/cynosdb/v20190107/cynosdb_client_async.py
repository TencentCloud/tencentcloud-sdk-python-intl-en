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
from tencentcloud.cynosdb.v20190107 import models
from typing import Dict


class CynosdbClient(AbstractClient):
    _apiVersion = '2019-01-07'
    _endpoint = 'cynosdb.intl.tencentcloudapi.com'
    _service = 'cynosdb'

    async def ActivateInstance(
            self,
            request: models.ActivateInstanceRequest,
            opts: Dict = None,
    ) -> models.ActivateInstanceResponse:
        """
        This interface (ActivateInstance) restores access to isolated instances.
        """
        
        kwargs = {}
        kwargs["action"] = "ActivateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ActivateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddClusterSlaveZone(
            self,
            request: models.AddClusterSlaveZoneRequest,
            opts: Dict = None,
    ) -> models.AddClusterSlaveZoneResponse:
        """
        This interface (AddClusterSlaveZone) is used to enable multi-az deployment for a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "AddClusterSlaveZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddClusterSlaveZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddInstances(
            self,
            request: models.AddInstancesRequest,
            opts: Dict = None,
    ) -> models.AddInstancesResponse:
        """
        This API is used to add instances to a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "AddInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindClusterResourcePackages(
            self,
            request: models.BindClusterResourcePackagesRequest,
            opts: Dict = None,
    ) -> models.BindClusterResourcePackagesResponse:
        """
        This API is used to bind resource packages to a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "BindClusterResourcePackages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindClusterResourcePackagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseAuditService(
            self,
            request: models.CloseAuditServiceRequest,
            opts: Dict = None,
    ) -> models.CloseAuditServiceResponse:
        """
        This API is used to close the database audit service for TDSQL-C MySQL instances.
        """
        
        kwargs = {}
        kwargs["action"] = "CloseAuditService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseAuditServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseClusterPasswordComplexity(
            self,
            request: models.CloseClusterPasswordComplexityRequest,
            opts: Dict = None,
    ) -> models.CloseClusterPasswordComplexityResponse:
        """
        This API is used to close cluster password complexity.
        """
        
        kwargs = {}
        kwargs["action"] = "CloseClusterPasswordComplexity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseClusterPasswordComplexityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseProxy(
            self,
            request: models.CloseProxyRequest,
            opts: Dict = None,
    ) -> models.CloseProxyResponse:
        """
        This API is used to close the database proxy service of a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "CloseProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseProxyEndPoint(
            self,
            request: models.CloseProxyEndPointRequest,
            opts: Dict = None,
    ) -> models.CloseProxyEndPointResponse:
        """
        This API is used to close the database proxy connection address.
        """
        
        kwargs = {}
        kwargs["action"] = "CloseProxyEndPoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseProxyEndPointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseSSL(
            self,
            request: models.CloseSSLRequest,
            opts: Dict = None,
    ) -> models.CloseSSLResponse:
        """
        This API is used to disable SSL encryption.
        """
        
        kwargs = {}
        kwargs["action"] = "CloseSSL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseSSLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseWan(
            self,
            request: models.CloseWanRequest,
            opts: Dict = None,
    ) -> models.CloseWanResponse:
        """
        This interface (CloseWan) is used to disable public network.
        """
        
        kwargs = {}
        kwargs["action"] = "CloseWan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseWanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CopyClusterPasswordComplexity(
            self,
            request: models.CopyClusterPasswordComplexityRequest,
            opts: Dict = None,
    ) -> models.CopyClusterPasswordComplexityResponse:
        """
        This API is used to copy the password complexity of a replication cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "CopyClusterPasswordComplexity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CopyClusterPasswordComplexityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccounts(
            self,
            request: models.CreateAccountsRequest,
            opts: Dict = None,
    ) -> models.CreateAccountsResponse:
        """
        This API is used to create user accounts.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAuditRuleTemplate(
            self,
            request: models.CreateAuditRuleTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateAuditRuleTemplateResponse:
        """
        This API is used to create audit rule templates.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAuditRuleTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAuditRuleTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBackup(
            self,
            request: models.CreateBackupRequest,
            opts: Dict = None,
    ) -> models.CreateBackupResponse:
        """
        This API is used to create a manual backup for a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCLSDelivery(
            self,
            request: models.CreateCLSDeliveryRequest,
            opts: Dict = None,
    ) -> models.CreateCLSDeliveryResponse:
        """
        This API is used to create log delivery.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCLSDelivery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCLSDeliveryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterDatabase(
            self,
            request: models.CreateClusterDatabaseRequest,
            opts: Dict = None,
    ) -> models.CreateClusterDatabaseResponse:
        """
        This API is used to create a database.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterDatabase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterDatabaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusters(
            self,
            request: models.CreateClustersRequest,
            opts: Dict = None,
    ) -> models.CreateClustersResponse:
        """
        This API is used to purchase new clusters.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIntegrateCluster(
            self,
            request: models.CreateIntegrateClusterRequest,
            opts: Dict = None,
    ) -> models.CreateIntegrateClusterResponse:
        """
        This API is used to create a newly purchased cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIntegrateCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIntegrateClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateParamTemplate(
            self,
            request: models.CreateParamTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateParamTemplateResponse:
        """
        This API is used to create parameter templates.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateParamTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateParamTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProxy(
            self,
            request: models.CreateProxyRequest,
            opts: Dict = None,
    ) -> models.CreateProxyResponse:
        """
        This API is used to enable the database proxy of a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProxyEndPoint(
            self,
            request: models.CreateProxyEndPointRequest,
            opts: Dict = None,
    ) -> models.CreateProxyEndPointResponse:
        """
        This API is used to create a database proxy connection point.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProxyEndPoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProxyEndPointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateResourcePackage(
            self,
            request: models.CreateResourcePackageRequest,
            opts: Dict = None,
    ) -> models.CreateResourcePackageResponse:
        """
        This API is used to purchase new resource packets.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateResourcePackage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateResourcePackageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccounts(
            self,
            request: models.DeleteAccountsRequest,
            opts: Dict = None,
    ) -> models.DeleteAccountsResponse:
        """
        This API is used to delete user accounts.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAuditRuleTemplates(
            self,
            request: models.DeleteAuditRuleTemplatesRequest,
            opts: Dict = None,
    ) -> models.DeleteAuditRuleTemplatesResponse:
        """
        This API is used to delete audit rule templates.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAuditRuleTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAuditRuleTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBackup(
            self,
            request: models.DeleteBackupRequest,
            opts: Dict = None,
    ) -> models.DeleteBackupResponse:
        """
        This API is used to delete manual backups for a cluster. Automatic backups cannot be deleted.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCLSDelivery(
            self,
            request: models.DeleteCLSDeliveryRequest,
            opts: Dict = None,
    ) -> models.DeleteCLSDeliveryResponse:
        """
        This API is used to delete log delivery.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCLSDelivery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCLSDeliveryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClusterDatabase(
            self,
            request: models.DeleteClusterDatabaseRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterDatabaseResponse:
        """
        This interface is used to delete a database.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClusterDatabase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterDatabaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteParamTemplate(
            self,
            request: models.DeleteParamTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteParamTemplateResponse:
        """
        This API is used to delete a parameter template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteParamTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteParamTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountPrivileges(
            self,
            request: models.DescribeAccountPrivilegesRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountPrivilegesResponse:
        """
        This API is used to query account privileges.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccountPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccounts(
            self,
            request: models.DescribeAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountsResponse:
        """
        This API is used to query the database account list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditInstanceList(
            self,
            request: models.DescribeAuditInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditInstanceListResponse:
        """
        This API is used to obtain the instance list of database audit.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditRuleTemplates(
            self,
            request: models.DescribeAuditRuleTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditRuleTemplatesResponse:
        """
        This API is used to query audit rule template information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditRuleTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditRuleTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditRuleWithInstanceIds(
            self,
            request: models.DescribeAuditRuleWithInstanceIdsRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditRuleWithInstanceIdsResponse:
        """
        This API is used to obtain the audit rules of the instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditRuleWithInstanceIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditRuleWithInstanceIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupConfig(
            self,
            request: models.DescribeBackupConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupConfigResponse:
        """
        This API is used to obtain the backup configuration information of a specified cluster, including the full backup time period and the backup file retention time.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupDownloadRestriction(
            self,
            request: models.DescribeBackupDownloadRestrictionRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupDownloadRestrictionResponse:
        """
        This API is used to query the download source limit of the default backup configured by the user in the current region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupDownloadRestriction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupDownloadRestrictionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupDownloadUrl(
            self,
            request: models.DescribeBackupDownloadUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupDownloadUrlResponse:
        """
        This API is used to query the download link of cluster backup files.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupDownloadUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupDownloadUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupDownloadUserRestriction(
            self,
            request: models.DescribeBackupDownloadUserRestrictionRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupDownloadUserRestrictionResponse:
        """
        This API is used to query the default backup download access restrictions of user-level settings in the current region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupDownloadUserRestriction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupDownloadUserRestrictionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupList(
            self,
            request: models.DescribeBackupListRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupListResponse:
        """
        This API is used to query the backup file list of a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBinlogConfig(
            self,
            request: models.DescribeBinlogConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeBinlogConfigResponse:
        """
        This API is used to query binlog configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBinlogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBinlogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBinlogDownloadUrl(
            self,
            request: models.DescribeBinlogDownloadUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeBinlogDownloadUrlResponse:
        """
        This API is used to query the download address of Binlog.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBinlogDownloadUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBinlogDownloadUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBinlogSaveDays(
            self,
            request: models.DescribeBinlogSaveDaysRequest,
            opts: Dict = None,
    ) -> models.DescribeBinlogSaveDaysResponse:
        """
        This API is used to query the binlog retention period of a cluster in days.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBinlogSaveDays"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBinlogSaveDaysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBinlogs(
            self,
            request: models.DescribeBinlogsRequest,
            opts: Dict = None,
    ) -> models.DescribeBinlogsResponse:
        """
        This interface (DescribeBinlogs) queries the cluster binlog list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBinlogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBinlogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeChangedParamsAfterUpgrade(
            self,
            request: models.DescribeChangedParamsAfterUpgradeRequest,
            opts: Dict = None,
    ) -> models.DescribeChangedParamsAfterUpgradeResponse:
        """
        this interface is used for querying parameter comparison after specification adjustment.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeChangedParamsAfterUpgrade"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeChangedParamsAfterUpgradeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterDatabaseTables(
            self,
            request: models.DescribeClusterDatabaseTablesRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterDatabaseTablesResponse:
        """
        This API is used to access the table list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterDatabaseTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterDatabaseTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterDatabases(
            self,
            request: models.DescribeClusterDatabasesRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterDatabasesResponse:
        """
        This API is used to obtain cluster database list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterDatabases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterDatabasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterDetail(
            self,
            request: models.DescribeClusterDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterDetailResponse:
        """
        This API is used to display cluster details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterDetailDatabases(
            self,
            request: models.DescribeClusterDetailDatabasesRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterDetailDatabasesResponse:
        """
        This API is used to query database list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterDetailDatabases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterDetailDatabasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterInstanceGrps(
            self,
            request: models.DescribeClusterInstanceGrpsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterInstanceGrpsResponse:
        """
        This API is used to query instance groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterInstanceGrps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterInstanceGrpsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterParams(
            self,
            request: models.DescribeClusterParamsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterParamsResponse:
        """
        This API is used to query cluster parameters.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterParams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterParamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterPasswordComplexity(
            self,
            request: models.DescribeClusterPasswordComplexityRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterPasswordComplexityResponse:
        """
        This API is used to view the cluster password complexity details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterPasswordComplexity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterPasswordComplexityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterReadOnly(
            self,
            request: models.DescribeClusterReadOnlyRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterReadOnlyResponse:
        """
        This API is used to query the cluster read-only switch.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterReadOnly"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterReadOnlyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterTransparentEncryptInfo(
            self,
            request: models.DescribeClusterTransparentEncryptInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterTransparentEncryptInfoResponse:
        """
        This API is used to query cluster transparent encryption information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterTransparentEncryptInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterTransparentEncryptInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusters(
            self,
            request: models.DescribeClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeClustersResponse:
        """
        This API is used to describe clusters.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSecurityGroups(
            self,
            request: models.DescribeDBSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSecurityGroupsResponse:
        """
        This API is used to query instance security group information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFlow(
            self,
            request: models.DescribeFlowRequest,
            opts: Dict = None,
    ) -> models.DescribeFlowResponse:
        """
        This API is used to query task flow information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceCLSLogDelivery(
            self,
            request: models.DescribeInstanceCLSLogDeliveryRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceCLSLogDeliveryResponse:
        """
        This API is used to query instance log delivery information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceCLSLogDelivery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceCLSLogDeliveryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceDetail(
            self,
            request: models.DescribeInstanceDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceDetailResponse:
        """
        This API is used to query instance details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceErrorLogs(
            self,
            request: models.DescribeInstanceErrorLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceErrorLogsResponse:
        """
        This API is used to query the list of instance error logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceErrorLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceErrorLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceParams(
            self,
            request: models.DescribeInstanceParamsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceParamsResponse:
        """
        This API is used to query the instance parameter list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceParams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceParamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceSlowQueries(
            self,
            request: models.DescribeInstanceSlowQueriesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceSlowQueriesResponse:
        """
        This API is used to query the slow query logs of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceSlowQueries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceSlowQueriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceSpecs(
            self,
            request: models.DescribeInstanceSpecsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceSpecsResponse:
        """
        This interface (DescribeInstanceSpecs) is used to query the instance specifications available for purchase on the query purchase page.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceSpecs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceSpecsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        This API is used to query the list of instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstancesWithinSameCluster(
            self,
            request: models.DescribeInstancesWithinSameClusterRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesWithinSameClusterResponse:
        """
        This API is used to query the instance list under the same cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancesWithinSameCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesWithinSameClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntegrateTask(
            self,
            request: models.DescribeIntegrateTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeIntegrateTaskResponse:
        """
        This API is used to query cluster tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntegrateTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntegrateTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIsolatedInstances(
            self,
            request: models.DescribeIsolatedInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeIsolatedInstancesResponse:
        """
        This interface is used for querying the recycle bin instance list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIsolatedInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIsolatedInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMaintainPeriod(
            self,
            request: models.DescribeMaintainPeriodRequest,
            opts: Dict = None,
    ) -> models.DescribeMaintainPeriodResponse:
        """
        This interface (DescribeMaintainPeriod) is used to query the instance maintenance window.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMaintainPeriod"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMaintainPeriodResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeParamTemplateDetail(
            self,
            request: models.DescribeParamTemplateDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeParamTemplateDetailResponse:
        """
        This API is used to query user parameter template details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeParamTemplateDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeParamTemplateDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeParamTemplates(
            self,
            request: models.DescribeParamTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeParamTemplatesResponse:
        """
        This API is used to query all parameter template information under the user-specified product.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeParamTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeParamTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjectSecurityGroups(
            self,
            request: models.DescribeProjectSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectSecurityGroupsResponse:
        """
        This API is used to query project security group information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjectSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxies(
            self,
            request: models.DescribeProxiesRequest,
            opts: Dict = None,
    ) -> models.DescribeProxiesResponse:
        """
        This API is used to query agent list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxyNodes(
            self,
            request: models.DescribeProxyNodesRequest,
            opts: Dict = None,
    ) -> models.DescribeProxyNodesResponse:
        """
        This API is used to query the list of proxy nodes.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxyNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxyNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxySpecs(
            self,
            request: models.DescribeProxySpecsRequest,
            opts: Dict = None,
    ) -> models.DescribeProxySpecsResponse:
        """
        This API is used to query database proxy specifications.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxySpecs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxySpecsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourcePackageDetail(
            self,
            request: models.DescribeResourcePackageDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeResourcePackageDetailResponse:
        """
        This API is used to query resource package usage details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourcePackageDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourcePackageDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourcePackageList(
            self,
            request: models.DescribeResourcePackageListRequest,
            opts: Dict = None,
    ) -> models.DescribeResourcePackageListResponse:
        """
        This API is used to query resource package list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourcePackageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourcePackageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourcePackageSaleSpec(
            self,
            request: models.DescribeResourcePackageSaleSpecRequest,
            opts: Dict = None,
    ) -> models.DescribeResourcePackageSaleSpecResponse:
        """
        This API is used to query resource package specifications.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourcePackageSaleSpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourcePackageSaleSpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourcesByDealName(
            self,
            request: models.DescribeResourcesByDealNameRequest,
            opts: Dict = None,
    ) -> models.DescribeResourcesByDealNameResponse:
        """
        This interface (DescribeResourcesByDealName) is used to query order-associated instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourcesByDealName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourcesByDealNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRollbackTimeRange(
            self,
            request: models.DescribeRollbackTimeRangeRequest,
            opts: Dict = None,
    ) -> models.DescribeRollbackTimeRangeResponse:
        """
        This API is used to query the rollback time range.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRollbackTimeRange"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRollbackTimeRangeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServerlessInstanceSpecs(
            self,
            request: models.DescribeServerlessInstanceSpecsRequest,
            opts: Dict = None,
    ) -> models.DescribeServerlessInstanceSpecsResponse:
        """
        This API is used to query available specifications of Serverless instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServerlessInstanceSpecs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServerlessInstanceSpecsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServerlessStrategy(
            self,
            request: models.DescribeServerlessStrategyRequest,
            opts: Dict = None,
    ) -> models.DescribeServerlessStrategyResponse:
        """
        This API is used to query serverless policies.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServerlessStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServerlessStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlaveZones(
            self,
            request: models.DescribeSlaveZonesRequest,
            opts: Dict = None,
    ) -> models.DescribeSlaveZonesResponse:
        """
        This API is used to query from availability zones.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlaveZones"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlaveZonesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSupportProxyVersion(
            self,
            request: models.DescribeSupportProxyVersionRequest,
            opts: Dict = None,
    ) -> models.DescribeSupportProxyVersionResponse:
        """
        This API is used to query supported database proxy versions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSupportProxyVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSupportProxyVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTasks(
            self,
            request: models.DescribeTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeTasksResponse:
        """
        This API is used to query task lists.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZones(
            self,
            request: models.DescribeZonesRequest,
            opts: Dict = None,
    ) -> models.DescribeZonesResponse:
        """
        This API is used to query marketable regional availability zone information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZones"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZonesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportInstanceErrorLogs(
            self,
            request: models.ExportInstanceErrorLogsRequest,
            opts: Dict = None,
    ) -> models.ExportInstanceErrorLogsResponse:
        """
        This API is used to export the error logs of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportInstanceErrorLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportInstanceErrorLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportInstanceSlowQueries(
            self,
            request: models.ExportInstanceSlowQueriesRequest,
            opts: Dict = None,
    ) -> models.ExportInstanceSlowQueriesResponse:
        """
        This API is used to export instance slow logs.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportInstanceSlowQueries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportInstanceSlowQueriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportResourcePackageDeductDetails(
            self,
            request: models.ExportResourcePackageDeductDetailsRequest,
            opts: Dict = None,
    ) -> models.ExportResourcePackageDeductDetailsResponse:
        """
        This API is used to export the usage details of a resource package.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportResourcePackageDeductDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportResourcePackageDeductDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceCreate(
            self,
            request: models.InquirePriceCreateRequest,
            opts: Dict = None,
    ) -> models.InquirePriceCreateResponse:
        """
        This interface (InquirePriceCreate) is used for price inquiry of newly purchased clusters.
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceCreate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceCreateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceModify(
            self,
            request: models.InquirePriceModifyRequest,
            opts: Dict = None,
    ) -> models.InquirePriceModifyResponse:
        """
        This API is used to query the price for modifying the specifications of a prepaid cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceModify"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceModifyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceMultiSpec(
            self,
            request: models.InquirePriceMultiSpecRequest,
            opts: Dict = None,
    ) -> models.InquirePriceMultiSpecResponse:
        """
        This API is used to inquire prices in batch.
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceMultiSpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceMultiSpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceRenew(
            self,
            request: models.InquirePriceRenewRequest,
            opts: Dict = None,
    ) -> models.InquirePriceRenewResponse:
        """
        This API is used to query the renewal price of a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceRenew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceRenewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateCluster(
            self,
            request: models.IsolateClusterRequest,
            opts: Dict = None,
    ) -> models.IsolateClusterResponse:
        """
        This interface (IsolateCluster) is used to isolate a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateInstance(
            self,
            request: models.IsolateInstanceRequest,
            opts: Dict = None,
    ) -> models.IsolateInstanceResponse:
        """
        This API is used to isolate an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountDescription(
            self,
            request: models.ModifyAccountDescriptionRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountDescriptionResponse:
        """
        This API is used to modify the descriptions of a database account.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountDescription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountDescriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountHost(
            self,
            request: models.ModifyAccountHostRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountHostResponse:
        """
        This API is used to modify account hosts.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountPrivileges(
            self,
            request: models.ModifyAccountPrivilegesRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountPrivilegesResponse:
        """
        This API is used to modify account database and table permissions.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAuditRuleTemplates(
            self,
            request: models.ModifyAuditRuleTemplatesRequest,
            opts: Dict = None,
    ) -> models.ModifyAuditRuleTemplatesResponse:
        """
        This API is used to modify audit rule templates.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAuditRuleTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAuditRuleTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAuditService(
            self,
            request: models.ModifyAuditServiceRequest,
            opts: Dict = None,
    ) -> models.ModifyAuditServiceResponse:
        """
        This API is used to modify the audit configurations of an instance, such as audit log retention period and audit rule.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAuditService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAuditServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBackupConfig(
            self,
            request: models.ModifyBackupConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupConfigResponse:
        """
        This API is used to modify the backup configuration of a specified cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBackupDownloadRestriction(
            self,
            request: models.ModifyBackupDownloadRestrictionRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupDownloadRestrictionResponse:
        """
        This API is used to modify the download source limit of the backup file for the user in the current region. It can be configured to allow downloads from both private and public networks, only the private network, or a designated vpc or ip within the private network.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupDownloadRestriction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupDownloadRestrictionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBackupDownloadUserRestriction(
            self,
            request: models.ModifyBackupDownloadUserRestrictionRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupDownloadUserRestrictionResponse:
        """
        This API is used to modify the download source restrictions for backup files in the user's current region. It can be configured to allow downloads from both private and public networks, only from a private network, or from a designated vpc or ip within the private network.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupDownloadUserRestriction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupDownloadUserRestrictionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBackupName(
            self,
            request: models.ModifyBackupNameRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupNameResponse:
        """
        This API is used to rename a backup file.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBinlogConfig(
            self,
            request: models.ModifyBinlogConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyBinlogConfigResponse:
        """
        This API is used to modify Binlog configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBinlogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBinlogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBinlogSaveDays(
            self,
            request: models.ModifyBinlogSaveDaysRequest,
            opts: Dict = None,
    ) -> models.ModifyBinlogSaveDaysResponse:
        """
        This API is used to modify the binlog retention period in days.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBinlogSaveDays"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBinlogSaveDaysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterDatabase(
            self,
            request: models.ModifyClusterDatabaseRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterDatabaseResponse:
        """
        This API is used to modify account authorization of a database.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterDatabase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterDatabaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterName(
            self,
            request: models.ModifyClusterNameRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterNameResponse:
        """
        This API is used to modify cluster names.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterParam(
            self,
            request: models.ModifyClusterParamRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterParamResponse:
        """
        This API is used to modify cluster parameters.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterParam"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterParamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterPasswordComplexity(
            self,
            request: models.ModifyClusterPasswordComplexityRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterPasswordComplexityResponse:
        """
        This API is used to modify or enable cluster password complexity.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterPasswordComplexity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterPasswordComplexityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterReadOnly(
            self,
            request: models.ModifyClusterReadOnlyRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterReadOnlyResponse:
        """
        This API is used to modify the read-only switch of a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterReadOnly"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterReadOnlyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterSlaveZone(
            self,
            request: models.ModifyClusterSlaveZoneRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterSlaveZoneResponse:
        """
        This API is used to modify the slave availability zone of a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterSlaveZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterSlaveZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceSecurityGroups(
            self,
            request: models.ModifyDBInstanceSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceSecurityGroupsResponse:
        """
        This API is used to modify the security group bound to the instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceName(
            self,
            request: models.ModifyInstanceNameRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceNameResponse:
        """
        This API is used to modify instance name.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceParam(
            self,
            request: models.ModifyInstanceParamRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceParamResponse:
        """
        This API is used to modify the instance parameters.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceParam"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceParamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceUpgradeLimitDays(
            self,
            request: models.ModifyInstanceUpgradeLimitDaysRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceUpgradeLimitDaysResponse:
        """
        This API is used to modify the time limit for upgrading the kernel minor version of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceUpgradeLimitDays"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceUpgradeLimitDaysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMaintainPeriodConfig(
            self,
            request: models.ModifyMaintainPeriodConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyMaintainPeriodConfigResponse:
        """
        This API is used to modify maintenance time configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMaintainPeriodConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMaintainPeriodConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyParamTemplate(
            self,
            request: models.ModifyParamTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyParamTemplateResponse:
        """
        This API is used to modify a parameter template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyParamTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyParamTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProxyDesc(
            self,
            request: models.ModifyProxyDescRequest,
            opts: Dict = None,
    ) -> models.ModifyProxyDescResponse:
        """
        This API is used to modify the description of a database proxy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProxyDesc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProxyDescResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProxyRwSplit(
            self,
            request: models.ModifyProxyRwSplitRequest,
            opts: Dict = None,
    ) -> models.ModifyProxyRwSplitResponse:
        """
        This API is used to configure read-write separation for database proxy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProxyRwSplit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProxyRwSplitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResourcePackageClusters(
            self,
            request: models.ModifyResourcePackageClustersRequest,
            opts: Dict = None,
    ) -> models.ModifyResourcePackageClustersResponse:
        """
        This API is used to modify the binding relationship between resource packages and clusters.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResourcePackageClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourcePackageClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResourcePackageName(
            self,
            request: models.ModifyResourcePackageNameRequest,
            opts: Dict = None,
    ) -> models.ModifyResourcePackageNameResponse:
        """
        This API is used to modify resource package name.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResourcePackageName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourcePackageNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResourcePackagesDeductionPriority(
            self,
            request: models.ModifyResourcePackagesDeductionPriorityRequest,
            opts: Dict = None,
    ) -> models.ModifyResourcePackagesDeductionPriorityResponse:
        """
        This API is used to modify the deduction priority of the bound resource package.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResourcePackagesDeductionPriority"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourcePackagesDeductionPriorityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyServerlessStrategy(
            self,
            request: models.ModifyServerlessStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyServerlessStrategyResponse:
        """
        This API is used to modify the serverless policy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyServerlessStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyServerlessStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVipVport(
            self,
            request: models.ModifyVipVportRequest,
            opts: Dict = None,
    ) -> models.ModifyVipVportResponse:
        """
        This API is used to modify the ip and port of an instance group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVipVport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVipVportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OfflineCluster(
            self,
            request: models.OfflineClusterRequest,
            opts: Dict = None,
    ) -> models.OfflineClusterResponse:
        """
        This interface (OfflineCluster) is used to terminate clusters.
        """
        
        kwargs = {}
        kwargs["action"] = "OfflineCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OfflineClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OfflineInstance(
            self,
            request: models.OfflineInstanceRequest,
            opts: Dict = None,
    ) -> models.OfflineInstanceResponse:
        """
        This interface (OfflineInstance) is used to terminate an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "OfflineInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OfflineInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenAuditService(
            self,
            request: models.OpenAuditServiceRequest,
            opts: Dict = None,
    ) -> models.OpenAuditServiceResponse:
        """
        This API is used to enable database audit service for an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "OpenAuditService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenAuditServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenClusterPasswordComplexity(
            self,
            request: models.OpenClusterPasswordComplexityRequest,
            opts: Dict = None,
    ) -> models.OpenClusterPasswordComplexityResponse:
        """
        This API is used to enable the custom password complexity feature.
        """
        
        kwargs = {}
        kwargs["action"] = "OpenClusterPasswordComplexity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenClusterPasswordComplexityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenClusterReadOnlyInstanceGroupAccess(
            self,
            request: models.OpenClusterReadOnlyInstanceGroupAccessRequest,
            opts: Dict = None,
    ) -> models.OpenClusterReadOnlyInstanceGroupAccessResponse:
        """
        This API is used to enable read-only instance group access.
        """
        
        kwargs = {}
        kwargs["action"] = "OpenClusterReadOnlyInstanceGroupAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenClusterReadOnlyInstanceGroupAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenClusterTransparentEncrypt(
            self,
            request: models.OpenClusterTransparentEncryptRequest,
            opts: Dict = None,
    ) -> models.OpenClusterTransparentEncryptResponse:
        """
        Enable transparent data encryption for the cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "OpenClusterTransparentEncrypt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenClusterTransparentEncryptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenReadOnlyInstanceExclusiveAccess(
            self,
            request: models.OpenReadOnlyInstanceExclusiveAccessRequest,
            opts: Dict = None,
    ) -> models.OpenReadOnlyInstanceExclusiveAccessResponse:
        """
        This interface (OpenReadOnlyInstanceExclusiveAccess) is used to enable the dedicated access access group for a read-only instance.
        """
        
        kwargs = {}
        kwargs["action"] = "OpenReadOnlyInstanceExclusiveAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenReadOnlyInstanceExclusiveAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenWan(
            self,
            request: models.OpenWanRequest,
            opts: Dict = None,
    ) -> models.OpenWanResponse:
        """
        This interface (OpenWan) is used to enable external network.
        """
        
        kwargs = {}
        kwargs["action"] = "OpenWan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenWanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PauseServerless(
            self,
            request: models.PauseServerlessRequest,
            opts: Dict = None,
    ) -> models.PauseServerlessResponse:
        """
        This API is used to suspend a serverless cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "PauseServerless"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PauseServerlessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RefundResourcePackage(
            self,
            request: models.RefundResourcePackageRequest,
            opts: Dict = None,
    ) -> models.RefundResourcePackageResponse:
        """
        This API is used to refund a resource package.
        """
        
        kwargs = {}
        kwargs["action"] = "RefundResourcePackage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RefundResourcePackageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReloadBalanceProxyNode(
            self,
            request: models.ReloadBalanceProxyNodeRequest,
            opts: Dict = None,
    ) -> models.ReloadBalanceProxyNodeResponse:
        """
        This API is used to reload the database proxy of Cloud Load Balancer.
        """
        
        kwargs = {}
        kwargs["action"] = "ReloadBalanceProxyNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReloadBalanceProxyNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveClusterSlaveZone(
            self,
            request: models.RemoveClusterSlaveZoneRequest,
            opts: Dict = None,
    ) -> models.RemoveClusterSlaveZoneResponse:
        """
        This API is used to disable multi-AZ deployment for a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveClusterSlaveZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveClusterSlaveZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewClusters(
            self,
            request: models.RenewClustersRequest,
            opts: Dict = None,
    ) -> models.RenewClustersResponse:
        """
        This API is used to renew the cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "RenewClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplayInstanceAuditLog(
            self,
            request: models.ReplayInstanceAuditLogRequest,
            opts: Dict = None,
    ) -> models.ReplayInstanceAuditLogResponse:
        """
        This API is used to replay instance audit logs.
        """
        
        kwargs = {}
        kwargs["action"] = "ReplayInstanceAuditLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplayInstanceAuditLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetAccountPassword(
            self,
            request: models.ResetAccountPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetAccountPasswordResponse:
        """
        This API is used to modify the database account password.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetAccountPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetAccountPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartInstance(
            self,
            request: models.RestartInstanceRequest,
            opts: Dict = None,
    ) -> models.RestartInstanceResponse:
        """
        This API is used to reboot an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "RestartInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeServerless(
            self,
            request: models.ResumeServerlessRequest,
            opts: Dict = None,
    ) -> models.ResumeServerlessResponse:
        """
        This API is used to restore a serverless cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeServerless"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeServerlessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RollBackCluster(
            self,
            request: models.RollBackClusterRequest,
            opts: Dict = None,
    ) -> models.RollBackClusterResponse:
        """
        This API is used to perform cluster rollback.
        """
        
        kwargs = {}
        kwargs["action"] = "RollBackCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RollBackClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RollbackToNewCluster(
            self,
            request: models.RollbackToNewClusterRequest,
            opts: Dict = None,
    ) -> models.RollbackToNewClusterResponse:
        """
        This API is used to roll back to a new cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "RollbackToNewCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RollbackToNewClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchClusterDatabases(
            self,
            request: models.SearchClusterDatabasesRequest,
            opts: Dict = None,
    ) -> models.SearchClusterDatabasesResponse:
        """
        This API is used to search cluster database lists.
        """
        
        kwargs = {}
        kwargs["action"] = "SearchClusterDatabases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchClusterDatabasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchClusterTables(
            self,
            request: models.SearchClusterTablesRequest,
            opts: Dict = None,
    ) -> models.SearchClusterTablesResponse:
        """
        This API is used to search cluster data table lists.
        """
        
        kwargs = {}
        kwargs["action"] = "SearchClusterTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchClusterTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetRenewFlag(
            self,
            request: models.SetRenewFlagRequest,
            opts: Dict = None,
    ) -> models.SetRenewFlagResponse:
        """
        This API is used to set the auto-renewal feature of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "SetRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartCLSDelivery(
            self,
            request: models.StartCLSDeliveryRequest,
            opts: Dict = None,
    ) -> models.StartCLSDeliveryResponse:
        """
        This interface (StartCLSDelivery) is used to enable log delivery functionality.
        """
        
        kwargs = {}
        kwargs["action"] = "StartCLSDelivery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartCLSDeliveryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopCLSDelivery(
            self,
            request: models.StopCLSDeliveryRequest,
            opts: Dict = None,
    ) -> models.StopCLSDeliveryResponse:
        """
        This API is used to stop the log delivery feature.
        """
        
        kwargs = {}
        kwargs["action"] = "StopCLSDelivery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopCLSDeliveryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchClusterVpc(
            self,
            request: models.SwitchClusterVpcRequest,
            opts: Dict = None,
    ) -> models.SwitchClusterVpcResponse:
        """
        This API is used to replace the cluster vpc.
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchClusterVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchClusterVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchClusterZone(
            self,
            request: models.SwitchClusterZoneRequest,
            opts: Dict = None,
    ) -> models.SwitchClusterZoneResponse:
        """
        This API is used to switch the primary and secondary AZs of a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchClusterZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchClusterZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchProxyVpc(
            self,
            request: models.SwitchProxyVpcRequest,
            opts: Dict = None,
    ) -> models.SwitchProxyVpcResponse:
        """
        This API is used to replace the vpc of the database proxy.
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchProxyVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchProxyVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindClusterResourcePackages(
            self,
            request: models.UnbindClusterResourcePackagesRequest,
            opts: Dict = None,
    ) -> models.UnbindClusterResourcePackagesResponse:
        """
        This API is used to unbind resource packages from clusters.
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindClusterResourcePackages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindClusterResourcePackagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeClusterVersion(
            self,
            request: models.UpgradeClusterVersionRequest,
            opts: Dict = None,
    ) -> models.UpgradeClusterVersionResponse:
        """
        This interface (UpgradeClusterVersion) is used to update the kernel minor version.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeClusterVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeClusterVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeInstance(
            self,
            request: models.UpgradeInstanceRequest,
            opts: Dict = None,
    ) -> models.UpgradeInstanceResponse:
        """
        This interface (UpgradeInstance) is used to upgrade instances.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeProxy(
            self,
            request: models.UpgradeProxyRequest,
            opts: Dict = None,
    ) -> models.UpgradeProxyResponse:
        """
        This API is used to upgrade database proxy configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeProxyVersion(
            self,
            request: models.UpgradeProxyVersionRequest,
            opts: Dict = None,
    ) -> models.UpgradeProxyVersionResponse:
        """
        This API is used to upgrade the database proxy version.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeProxyVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeProxyVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)