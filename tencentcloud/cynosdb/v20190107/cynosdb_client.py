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
from tencentcloud.cynosdb.v20190107 import models


class CynosdbClient(AbstractClient):
    _apiVersion = '2019-01-07'
    _endpoint = 'cynosdb.intl.tencentcloudapi.com'
    _service = 'cynosdb'


    def ActivateInstance(self, request):
        """This API is used to remove the isolation of an instance to make it accessible again.

        :param request: Request instance for ActivateInstance.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ActivateInstanceRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ActivateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ActivateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ActivateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddClusterSlaveZone(self, request):
        """This API is used to add the replica AZ.

        :param request: Request instance for AddClusterSlaveZone.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.AddClusterSlaveZoneRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.AddClusterSlaveZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddClusterSlaveZone", params, headers=headers)
            response = json.loads(body)
            model = models.AddClusterSlaveZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddInstances(self, request):
        """This API is used to add an instance in a cluster.

        :param request: Request instance for AddInstances.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.AddInstancesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.AddInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddInstances", params, headers=headers)
            response = json.loads(body)
            model = models.AddInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindClusterResourcePackages(self, request):
        """This API is used to bind a resource pack to a cluster.

        :param request: Request instance for BindClusterResourcePackages.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.BindClusterResourcePackagesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.BindClusterResourcePackagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindClusterResourcePackages", params, headers=headers)
            response = json.loads(body)
            model = models.BindClusterResourcePackagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseAuditService(self, request):
        """This API is used to disable the audit service for a TDSQL-C for MySQL instance.

        :param request: Request instance for CloseAuditService.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CloseAuditServiceRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CloseAuditServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseAuditService", params, headers=headers)
            response = json.loads(body)
            model = models.CloseAuditServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseClusterPasswordComplexity(self, request):
        """This API is used to disable the password complexity for a cluster.

        :param request: Request instance for CloseClusterPasswordComplexity.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CloseClusterPasswordComplexityRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CloseClusterPasswordComplexityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseClusterPasswordComplexity", params, headers=headers)
            response = json.loads(body)
            model = models.CloseClusterPasswordComplexityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseProxy(self, request):
        """This API is used to disable the database proxy.

        :param request: Request instance for CloseProxy.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CloseProxyRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CloseProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseProxy", params, headers=headers)
            response = json.loads(body)
            model = models.CloseProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseWan(self, request):
        """This API is used to disable the public network.

        :param request: Request instance for CloseWan.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CloseWanRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CloseWanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseWan", params, headers=headers)
            response = json.loads(body)
            model = models.CloseWanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CopyClusterPasswordComplexity(self, request):
        """This API is used to replicate the password complexity for a cluster.

        :param request: Request instance for CopyClusterPasswordComplexity.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CopyClusterPasswordComplexityRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CopyClusterPasswordComplexityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyClusterPasswordComplexity", params, headers=headers)
            response = json.loads(body)
            model = models.CopyClusterPasswordComplexityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAccounts(self, request):
        """This API is used to create an account.

        :param request: Request instance for CreateAccounts.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CreateAccountsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CreateAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAuditRuleTemplate(self, request):
        """This API is used to create an audit rule template.

        :param request: Request instance for CreateAuditRuleTemplate.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CreateAuditRuleTemplateRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CreateAuditRuleTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAuditRuleTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAuditRuleTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBackup(self, request):
        """This API is used to create manual backup.

        :param request: Request instance for CreateBackup.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CreateBackupRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CreateBackupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBackup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBackupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClusterDatabase(self, request):
        """This API is used to create a database.

        :param request: Request instance for CreateClusterDatabase.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CreateClusterDatabaseRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CreateClusterDatabaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterDatabase", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterDatabaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClusters(self, request):
        """This API is used to create a cluster.

        :param request: Request instance for CreateClusters.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CreateClustersRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CreateClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusters", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateParamTemplate(self, request):
        """This API is used to create a parameter template.

        :param request: Request instance for CreateParamTemplate.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CreateParamTemplateRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CreateParamTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateParamTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateParamTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProxy(self, request):
        """This API is used to create a database proxy.

        :param request: Request instance for CreateProxy.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CreateProxyRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CreateProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProxy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProxyEndPoint(self, request):
        """This API is used to create a database proxy connection.

        :param request: Request instance for CreateProxyEndPoint.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CreateProxyEndPointRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CreateProxyEndPointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProxyEndPoint", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProxyEndPointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateResourcePackage(self, request):
        """This API is used to purchase a resource pack.

        :param request: Request instance for CreateResourcePackage.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CreateResourcePackageRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CreateResourcePackageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateResourcePackage", params, headers=headers)
            response = json.loads(body)
            model = models.CreateResourcePackageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAccounts(self, request):
        """This API is used to delete an account.

        :param request: Request instance for DeleteAccounts.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DeleteAccountsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DeleteAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAuditRuleTemplates(self, request):
        """This API is used to delete an audit rule template.

        :param request: Request instance for DeleteAuditRuleTemplates.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DeleteAuditRuleTemplatesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DeleteAuditRuleTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAuditRuleTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAuditRuleTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBackup(self, request):
        """This API is used to delete the manual backup for a cluster. It cannot be used to delete the automatic backup.

        :param request: Request instance for DeleteBackup.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DeleteBackupRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DeleteBackupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBackup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBackupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteClusterDatabase(self, request):
        """This API is used to delete a database.

        :param request: Request instance for DeleteClusterDatabase.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DeleteClusterDatabaseRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DeleteClusterDatabaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClusterDatabase", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClusterDatabaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteParamTemplate(self, request):
        """This API is used to delete a parameter template.

        :param request: Request instance for DeleteParamTemplate.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DeleteParamTemplateRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DeleteParamTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteParamTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteParamTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccountPrivileges(self, request):
        """This API is used to query the existing permissions of an account.

        :param request: Request instance for DescribeAccountPrivileges.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccountPrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountPrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccounts(self, request):
        """This API is used to query database management accounts.

        :param request: Request instance for DescribeAccounts.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuditRuleTemplates(self, request):
        """This API is used to query audit rule templates.

        :param request: Request instance for DescribeAuditRuleTemplates.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAuditRuleTemplatesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAuditRuleTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditRuleTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditRuleTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuditRuleWithInstanceIds(self, request):
        """This API is used to get the audit rule templates of an instance.

        :param request: Request instance for DescribeAuditRuleWithInstanceIds.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAuditRuleWithInstanceIdsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAuditRuleWithInstanceIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditRuleWithInstanceIds", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditRuleWithInstanceIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupConfig(self, request):
        """This API is used to get the backup configuration information of the specified cluster, including the full backup time range and backup file retention period.

        :param request: Request instance for DescribeBackupConfig.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBackupConfigRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBackupConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupDownloadUrl(self, request):
        """This API is used to query the download address of a cluster backup file.

        :param request: Request instance for DescribeBackupDownloadUrl.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBackupDownloadUrlRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBackupDownloadUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupDownloadUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupDownloadUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupList(self, request):
        """This API is used to query the list of backup files.

        :param request: Request instance for DescribeBackupList.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBackupListRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBackupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBinlogDownloadUrl(self, request):
        """This API is used to query the download address of a binlog.

        :param request: Request instance for DescribeBinlogDownloadUrl.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBinlogDownloadUrlRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBinlogDownloadUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBinlogDownloadUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBinlogDownloadUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBinlogSaveDays(self, request):
        """This API is used to query the binlog retention period of a cluster in days.

        :param request: Request instance for DescribeBinlogSaveDays.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBinlogSaveDaysRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBinlogSaveDaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBinlogSaveDays", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBinlogSaveDaysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBinlogs(self, request):
        """This API is used to query the list of binlogs in a cluster.

        :param request: Request instance for DescribeBinlogs.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBinlogsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBinlogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBinlogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBinlogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterDetail(self, request):
        """This API is used to show the details of an instance.

        :param request: Request instance for DescribeClusterDetail.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterDetailRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterDetailDatabases(self, request):
        """This API is used to query the database list.

        :param request: Request instance for DescribeClusterDetailDatabases.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterDetailDatabasesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterDetailDatabasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterDetailDatabases", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterDetailDatabasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterInstanceGrps(self, request):
        """This API is used to query instance groups.

        :param request: Request instance for DescribeClusterInstanceGrps.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterInstanceGrpsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterInstanceGrpsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterInstanceGrps", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterInstanceGrpsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterParams(self, request):
        """This API is used to query the parameters of a cluster.

        :param request: Request instance for DescribeClusterParams.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterParamsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterParamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterParams", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterParamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterPasswordComplexity(self, request):
        """This API is used to query the details of password complexity for a cluster.

        :param request: Request instance for DescribeClusterPasswordComplexity.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterPasswordComplexityRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterPasswordComplexityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterPasswordComplexity", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterPasswordComplexityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusters(self, request):
        """This API is used to the list of clusters.

        :param request: Request instance for DescribeClusters.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClustersRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBSecurityGroups(self, request):
        """This API is used to query the security group information of an instance.

        :param request: Request instance for DescribeDBSecurityGroups.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeDBSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeDBSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFlow(self, request):
        """This API is used to query task flow information.

        :param request: Request instance for DescribeFlow.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeFlowRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlow", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceDetail(self, request):
        """This API is used to query instance details.

        :param request: Request instance for DescribeInstanceDetail.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceDetailRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceErrorLogs(self, request):
        """This API is used to query the list of error logs for an instance.

        :param request: Request instance for DescribeInstanceErrorLogs.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceErrorLogsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceErrorLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceErrorLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceErrorLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceParams(self, request):
        """This API is used to query the parameter list of an instance.

        :param request: Request instance for DescribeInstanceParams.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceParamsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceParamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceParams", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceParamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceSlowQueries(self, request):
        """This API is used to query the slow query logs of an instance.

        :param request: Request instance for DescribeInstanceSlowQueries.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceSlowQueriesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceSlowQueriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceSlowQueries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceSlowQueriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceSpecs(self, request):
        """This API is used to query instance specifications.

        :param request: Request instance for DescribeInstanceSpecs.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceSpecsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceSpecsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceSpecs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceSpecsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        """This API is used to query the list of instances.

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMaintainPeriod(self, request):
        """This API is used to query the instance maintenance window.

        :param request: Request instance for DescribeMaintainPeriod.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeMaintainPeriodRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeMaintainPeriodResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMaintainPeriod", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMaintainPeriodResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeParamTemplateDetail(self, request):
        """This API is used to query the details of a parameter template.

        :param request: Request instance for DescribeParamTemplateDetail.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeParamTemplateDetailRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeParamTemplateDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeParamTemplateDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeParamTemplateDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeParamTemplates(self, request):
        """This API is used to query all parameter templates information of a user-specified product.

        :param request: Request instance for DescribeParamTemplates.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeParamTemplatesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeParamTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeParamTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeParamTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjectSecurityGroups(self, request):
        """This API is used to query the security group information of a project.

        :param request: Request instance for DescribeProjectSecurityGroups.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeProjectSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeProjectSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjectSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProxies(self, request):
        """This API is used to query the list of database proxies.

        :param request: Request instance for DescribeProxies.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeProxiesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeProxiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProxies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProxiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProxyNodes(self, request):
        """This API is used to query the list of proxy nodes.

        :param request: Request instance for DescribeProxyNodes.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeProxyNodesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeProxyNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProxyNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProxyNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProxySpecs(self, request):
        """This API is used to query the specifications of a database proxy.

        :param request: Request instance for DescribeProxySpecs.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeProxySpecsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeProxySpecsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProxySpecs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProxySpecsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourcePackageDetail(self, request):
        """This API is used to query the usage details of a resource pack.

        :param request: Request instance for DescribeResourcePackageDetail.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeResourcePackageDetailRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeResourcePackageDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourcePackageDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourcePackageDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourcePackageList(self, request):
        """This API is used to query the list of the resource packs.

        :param request: Request instance for DescribeResourcePackageList.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeResourcePackageListRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeResourcePackageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourcePackageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourcePackageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourcePackageSaleSpec(self, request):
        """This API is used to query the specifications of a resource pack.

        :param request: Request instance for DescribeResourcePackageSaleSpec.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeResourcePackageSaleSpecRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeResourcePackageSaleSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourcePackageSaleSpec", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourcePackageSaleSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourcesByDealName(self, request):
        """This API is used to query the list of resources by billing order ID.

        :param request: Request instance for DescribeResourcesByDealName.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeResourcesByDealNameRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeResourcesByDealNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourcesByDealName", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourcesByDealNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRollbackTimeRange(self, request):
        """This API is used to query the valid rollback time range for the specified cluster.

        :param request: Request instance for DescribeRollbackTimeRange.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeRollbackTimeRangeRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeRollbackTimeRangeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRollbackTimeRange", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRollbackTimeRangeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRollbackTimeValidity(self, request):
        """This API is used to query whether rollback is possible based on the specified time and cluster.

        :param request: Request instance for DescribeRollbackTimeValidity.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeRollbackTimeValidityRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeRollbackTimeValidityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRollbackTimeValidity", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRollbackTimeValidityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSupportProxyVersion(self, request):
        """This API is used to query the supported database proxy versions.

        :param request: Request instance for DescribeSupportProxyVersion.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeSupportProxyVersionRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeSupportProxyVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSupportProxyVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSupportProxyVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZones(self, request):
        """This API is used to query the AZ information in a purchasable region.

        :param request: Request instance for DescribeZones.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeZonesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZones", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZonesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportInstanceErrorLogs(self, request):
        """This API is used to export the error logs of an instance.

        :param request: Request instance for ExportInstanceErrorLogs.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ExportInstanceErrorLogsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ExportInstanceErrorLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportInstanceErrorLogs", params, headers=headers)
            response = json.loads(body)
            model = models.ExportInstanceErrorLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportInstanceSlowQueries(self, request):
        """This API is used to export the slow logs of an instance.

        :param request: Request instance for ExportInstanceSlowQueries.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ExportInstanceSlowQueriesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ExportInstanceSlowQueriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportInstanceSlowQueries", params, headers=headers)
            response = json.loads(body)
            model = models.ExportInstanceSlowQueriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceCreate(self, request):
        """This API is used to query the purchasable price of a cluster.

        :param request: Request instance for InquirePriceCreate.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.InquirePriceCreateRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.InquirePriceCreateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceCreate", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceCreateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceRenew(self, request):
        """This API is used to query the renewal price of a cluster.

        :param request: Request instance for InquirePriceRenew.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.InquirePriceRenewRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.InquirePriceRenewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceRenew", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceRenewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateCluster(self, request):
        """This API is used to isolate a cluster.

        :param request: Request instance for IsolateCluster.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.IsolateClusterRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.IsolateClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateCluster", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateInstance(self, request):
        """This API is used to isolate an instance.

        :param request: Request instance for IsolateInstance.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.IsolateInstanceRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.IsolateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccountDescription(self, request):
        """This API is used to modify the descriptions of a database account.

        :param request: Request instance for ModifyAccountDescription.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyAccountDescriptionRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyAccountDescriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccountDescription", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccountDescriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccountHost(self, request):
        """This API is used to modify the account host.

        :param request: Request instance for ModifyAccountHost.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyAccountHostRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyAccountHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccountHost", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccountHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccountPrivileges(self, request):
        """This API is used to modify the account permissions.

        :param request: Request instance for ModifyAccountPrivileges.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccountPrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccountPrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAuditRuleTemplates(self, request):
        """This API is used to modify an audit rule template.

        :param request: Request instance for ModifyAuditRuleTemplates.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyAuditRuleTemplatesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyAuditRuleTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAuditRuleTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAuditRuleTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAuditService(self, request):
        """This API is used to modify the audit configurations of an instance, such as audit log retention period and audit rule.

        :param request: Request instance for ModifyAuditService.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyAuditServiceRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyAuditServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAuditService", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAuditServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBackupConfig(self, request):
        """This API is used to modify the backup configuration of the specified cluster.

        :param request: Request instance for ModifyBackupConfig.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyBackupConfigRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyBackupConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBackupConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBackupConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBackupName(self, request):
        """This API is used to rename a backup file.

        :param request: Request instance for ModifyBackupName.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyBackupNameRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyBackupNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBackupName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBackupNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBinlogSaveDays(self, request):
        """This API is used to modify the binlog retention period in days.

        :param request: Request instance for ModifyBinlogSaveDays.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyBinlogSaveDaysRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyBinlogSaveDaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBinlogSaveDays", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBinlogSaveDaysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterDatabase(self, request):
        """This API is used to modify the database.

        :param request: Request instance for ModifyClusterDatabase.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterDatabaseRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterDatabaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterDatabase", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterDatabaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterName(self, request):
        """This API is used to modify cluster name.

        :param request: Request instance for ModifyClusterName.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterNameRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterParam(self, request):
        """This API is used to modify the parameters of a cluster.

        :param request: Request instance for ModifyClusterParam.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterParamRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterParamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterParam", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterParamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterPasswordComplexity(self, request):
        """This API is used to modify or enable the password complexity for a cluster.

        :param request: Request instance for ModifyClusterPasswordComplexity.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterPasswordComplexityRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterPasswordComplexityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterPasswordComplexity", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterPasswordComplexityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterSlaveZone(self, request):
        """This API is used to modify the replica AZ.

        :param request: Request instance for ModifyClusterSlaveZone.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterSlaveZoneRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterSlaveZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterSlaveZone", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterSlaveZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceSecurityGroups(self, request):
        """This API is used to modify the security groups bound to an instance.

        :param request: Request instance for ModifyDBInstanceSecurityGroups.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyDBInstanceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyDBInstanceSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceName(self, request):
        """This API is used to modify instance name.

        :param request: Request instance for ModifyInstanceName.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyInstanceNameRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyInstanceNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceParam(self, request):
        """This API is used to modify the instance parameters.

        :param request: Request instance for ModifyInstanceParam.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyInstanceParamRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyInstanceParamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceParam", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceParamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMaintainPeriodConfig(self, request):
        """This API is used to modify the maintenance time configuration.

        :param request: Request instance for ModifyMaintainPeriodConfig.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyMaintainPeriodConfigRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyMaintainPeriodConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMaintainPeriodConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMaintainPeriodConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyParamTemplate(self, request):
        """This API is used to modify a parameter template.

        :param request: Request instance for ModifyParamTemplate.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyParamTemplateRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyParamTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyParamTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyParamTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProxyDesc(self, request):
        """This API is used to modify the description of a database proxy.

        :param request: Request instance for ModifyProxyDesc.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyProxyDescRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyProxyDescResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProxyDesc", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProxyDescResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProxyRwSplit(self, request):
        """This API is used to configure the read/write separation of a database proxy.

        :param request: Request instance for ModifyProxyRwSplit.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyProxyRwSplitRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyProxyRwSplitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProxyRwSplit", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProxyRwSplitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourcePackageClusters(self, request):
        """This API is used to bind a resource pack to a cluster.

        :param request: Request instance for ModifyResourcePackageClusters.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyResourcePackageClustersRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyResourcePackageClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourcePackageClusters", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourcePackageClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourcePackageName(self, request):
        """This API is used to modify the name of a resource pack.

        :param request: Request instance for ModifyResourcePackageName.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyResourcePackageNameRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyResourcePackageNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourcePackageName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourcePackageNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVipVport(self, request):
        """This API is used to modify the IP and port of an instance group.

        :param request: Request instance for ModifyVipVport.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyVipVportRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyVipVportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVipVport", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVipVportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OfflineCluster(self, request):
        """This API is used to deactivate a cluster.

        :param request: Request instance for OfflineCluster.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.OfflineClusterRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.OfflineClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OfflineCluster", params, headers=headers)
            response = json.loads(body)
            model = models.OfflineClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OfflineInstance(self, request):
        """This API is used to deactivate an instance.

        :param request: Request instance for OfflineInstance.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.OfflineInstanceRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.OfflineInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OfflineInstance", params, headers=headers)
            response = json.loads(body)
            model = models.OfflineInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenAuditService(self, request):
        """This API is used to enable the audit service for a TDSQL-C for MySQL instance.

        :param request: Request instance for OpenAuditService.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.OpenAuditServiceRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.OpenAuditServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenAuditService", params, headers=headers)
            response = json.loads(body)
            model = models.OpenAuditServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenClusterPasswordComplexity(self, request):
        """This API is used to enable the password complexity for a cluster.

        :param request: Request instance for OpenClusterPasswordComplexity.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.OpenClusterPasswordComplexityRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.OpenClusterPasswordComplexityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenClusterPasswordComplexity", params, headers=headers)
            response = json.loads(body)
            model = models.OpenClusterPasswordComplexityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenClusterReadOnlyInstanceGroupAccess(self, request):
        """This API is used to enable the access to read-only instance group.

        :param request: Request instance for OpenClusterReadOnlyInstanceGroupAccess.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.OpenClusterReadOnlyInstanceGroupAccessRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.OpenClusterReadOnlyInstanceGroupAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenClusterReadOnlyInstanceGroupAccess", params, headers=headers)
            response = json.loads(body)
            model = models.OpenClusterReadOnlyInstanceGroupAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenReadOnlyInstanceExclusiveAccess(self, request):
        """This API is used to enable the dedicated access group for a read-only instance.

        :param request: Request instance for OpenReadOnlyInstanceExclusiveAccess.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.OpenReadOnlyInstanceExclusiveAccessRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.OpenReadOnlyInstanceExclusiveAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenReadOnlyInstanceExclusiveAccess", params, headers=headers)
            response = json.loads(body)
            model = models.OpenReadOnlyInstanceExclusiveAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenWan(self, request):
        """This API is used to enable the public network.

        :param request: Request instance for OpenWan.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.OpenWanRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.OpenWanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenWan", params, headers=headers)
            response = json.loads(body)
            model = models.OpenWanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PauseServerless(self, request):
        """This API is used to pause a serverless cluster.

        :param request: Request instance for PauseServerless.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.PauseServerlessRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.PauseServerlessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PauseServerless", params, headers=headers)
            response = json.loads(body)
            model = models.PauseServerlessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RefundResourcePackage(self, request):
        """This API is used to refund a resource pack.

        :param request: Request instance for RefundResourcePackage.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.RefundResourcePackageRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.RefundResourcePackageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RefundResourcePackage", params, headers=headers)
            response = json.loads(body)
            model = models.RefundResourcePackageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReloadBalanceProxyNode(self, request):
        """This API is used to rebalance the load on the database proxy.

        :param request: Request instance for ReloadBalanceProxyNode.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ReloadBalanceProxyNodeRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ReloadBalanceProxyNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReloadBalanceProxyNode", params, headers=headers)
            response = json.loads(body)
            model = models.ReloadBalanceProxyNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveClusterSlaveZone(self, request):
        """This API is used to delete the replica AZ.

        :param request: Request instance for RemoveClusterSlaveZone.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.RemoveClusterSlaveZoneRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.RemoveClusterSlaveZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveClusterSlaveZone", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveClusterSlaveZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetAccountPassword(self, request):
        """This API is used to reset the password of a TencentDB instance account.

        :param request: Request instance for ResetAccountPassword.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ResetAccountPasswordRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ResetAccountPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetAccountPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetAccountPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartInstance(self, request):
        """This API is used to restart an instance.

        :param request: Request instance for RestartInstance.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.RestartInstanceRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.RestartInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RestartInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumeServerless(self, request):
        """This API is used to resume a serverless cluster.

        :param request: Request instance for ResumeServerless.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ResumeServerlessRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ResumeServerlessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeServerless", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeServerlessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchClusterDatabases(self, request):
        """This API is used to search the list of cluster databases.

        :param request: Request instance for SearchClusterDatabases.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.SearchClusterDatabasesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.SearchClusterDatabasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchClusterDatabases", params, headers=headers)
            response = json.loads(body)
            model = models.SearchClusterDatabasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchClusterTables(self, request):
        """This API is used to search the list of cluster data tables.

        :param request: Request instance for SearchClusterTables.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.SearchClusterTablesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.SearchClusterTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchClusterTables", params, headers=headers)
            response = json.loads(body)
            model = models.SearchClusterTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetRenewFlag(self, request):
        """This API is used to set auto-renewal for an instance.

        :param request: Request instance for SetRenewFlag.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.SetRenewFlagRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.SetRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.SetRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchClusterVpc(self, request):
        """This API is used to modify the cluster VPC.

        :param request: Request instance for SwitchClusterVpc.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.SwitchClusterVpcRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.SwitchClusterVpcResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchClusterVpc", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchClusterVpcResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchClusterZone(self, request):
        """This API is used to switch to the replica AZ.

        :param request: Request instance for SwitchClusterZone.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.SwitchClusterZoneRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.SwitchClusterZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchClusterZone", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchClusterZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchProxyVpc(self, request):
        """This API is used to modify the database proxy VPC.

        :param request: Request instance for SwitchProxyVpc.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.SwitchProxyVpcRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.SwitchProxyVpcResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchProxyVpc", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchProxyVpcResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindClusterResourcePackages(self, request):
        """This API is used to unbind a TDSQL-C for MySQL resource pack.

        :param request: Request instance for UnbindClusterResourcePackages.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.UnbindClusterResourcePackagesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.UnbindClusterResourcePackagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindClusterResourcePackages", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindClusterResourcePackagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeClusterVersion(self, request):
        """This API is used to upgrade the kernel version of a TDSQL-C for MySQL cluster.

        :param request: Request instance for UpgradeClusterVersion.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.UpgradeClusterVersionRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.UpgradeClusterVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeClusterVersion", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeClusterVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeInstance(self, request):
        """This API is used to upgrade an instance.

        :param request: Request instance for UpgradeInstance.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.UpgradeInstanceRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.UpgradeInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeProxy(self, request):
        """This API is used to upgrade the configuration of a database proxy.

        :param request: Request instance for UpgradeProxy.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.UpgradeProxyRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.UpgradeProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeProxy", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeProxyVersion(self, request):
        """This API is used to upgrade the version of a database proxy.

        :param request: Request instance for UpgradeProxyVersion.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.UpgradeProxyVersionRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.UpgradeProxyVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeProxyVersion", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeProxyVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))