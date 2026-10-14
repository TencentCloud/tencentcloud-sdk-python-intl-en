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


# Current user is unauthorized for the create cluster instance operation. Add CAM permission.
AUTHFAILURE_UNAUTHCREATEINSTANCE = 'AuthFailure.UnAuthCreateInstance'

# Current user is unauthorized for the query cluster instance operation. Add CAM permission.
AUTHFAILURE_UNAUTHDESCRIBEINSTANCES = 'AuthFailure.UnAuthDescribeInstances'

# Unauthorized operation.
AUTHFAILURE_UNAUTHORIZEDOPERATION = 'AuthFailure.UnAuthorizedOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Insufficient resource pack quota in the availability zone.
FAILEDOPERATION_CDCQUOTAINSUFFICIENT = 'FailedOperation.CdcQuotaInsufficient'

# Cluster resource quota limit error.
FAILEDOPERATION_CLUSTERRESOURCELIMITERROR = 'FailedOperation.ClusterResourceLimitError'

# Node disk block count parameter check failed.
FAILEDOPERATION_DISKCOUNTPARAMERROR = 'FailedOperation.DiskCountParamError'

# Cluster status error.
FAILEDOPERATION_ERRORCLUSTERSTATE = 'FailedOperation.ErrorClusterState'

# Manipulation is not allowed due to EsDictionaryInfo error.
FAILEDOPERATION_ESDICTIONARYINFOERROR = 'FailedOperation.EsDictionaryInfoError'

# File name does not conform to specifications.
FAILEDOPERATION_FILENAMEERROR = 'FailedOperation.FileNameError'

# File size does not meet requirements.
FAILEDOPERATION_FILESIZEERROR = 'FailedOperation.FileSizeError'

# Error getting the tag list of the instance.
FAILEDOPERATION_GETTAGINFOERROR = 'FailedOperation.GetTagInfoError'

# The account is not bound to a credit card or paypal and cannot pay.
FAILEDOPERATION_NOPAYMENT = 'FailedOperation.NoPayment'

# The number of nodes and AZ info does not meet the corresponding operational rule.
FAILEDOPERATION_NODENUMANDZONEERROR = 'FailedOperation.NodeNumAndZoneError'

# REAL_NAME_CHECK_FAIL.
FAILEDOPERATION_NOTAUTHENTICATED = 'FailedOperation.NotAuthenticated'

# Termination protection is enabled for the current cluster. Unable to terminate it directly. Disable the protection and try again.
FAILEDOPERATION_OPENDESTROYPROTECTION = 'FailedOperation.OpenDestroyProtection'

# The instance fails to satisfy the refund condition.
FAILEDOPERATION_REFUNDERROR = 'FailedOperation.RefundError'

# Request timeout.
FAILEDOPERATION_REQUESTTIMEOUT = 'FailedOperation.RequestTimeOut'

# Scaling a local disk cluster via rolling restart is not supported.
FAILEDOPERATION_UNSUPPORTEDLOCALDISKROLLUPSCALEUPORDOWN = 'FailedOperation.UnsupportedLocalDiskRollUpScaleUpOrDown'

# Rolling restart to scale computational resources and disk quantity at the same time is not supported.
FAILEDOPERATION_UNSUPPORTEDRESETNODETYPEANDSCALEOUTDISK = 'FailedOperation.UnsupportedResetNodeTypeAndScaleOutDisk'

# Rolling restart to reduce computational resources and adjust disk size at the same time is not supported.
FAILEDOPERATION_UNSUPPORTEDRESTSCALEDOWNANDMODIFYDISK = 'FailedOperation.UnsupportedRestScaleDownAndModifyDisk'

# Unsupported backward adjustment of node configuration and disk capacity.
FAILEDOPERATION_UNSUPPORTEDREVERSEREGULATIONNODETYPEANDDISK = 'FailedOperation.UnsupportedReverseRegulationNodeTypeAndDisk'

# Internal error.
INTERNALERROR = 'InternalError'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# The APPID value does not match the expectation.
INVALIDPARAMETER_INVALIDAPPID = 'InvalidParameter.InvalidAppId'

# The value of whether to automatically use a voucher AutoVoucher does not match the expectation.
INVALIDPARAMETER_INVALIDAUTOVOUCHER = 'InvalidParameter.InvalidAutoVoucher'

# The value of ClusterName does not match the expected value.
INVALIDPARAMETER_INVALIDCLUSTERNAME = 'InvalidParameter.InvalidClusterName'

# cos auto backup information does not meet expectations.
INVALIDPARAMETER_INVALIDCOSBACKUPINFO = 'InvalidParameter.InvalidCosBackupInfo'

# The value of the cluster deployment method InvalidDeployMode does not match the expectation.
INVALIDPARAMETER_INVALIDDEPLOYMODE = 'InvalidParameter.InvalidDeployMode'

# The value of the node disk count DiskCount does not match the expectation.
INVALIDPARAMETER_INVALIDDISKCOUNT = 'InvalidParameter.InvalidDiskCount'

# The value of the node disk encryption information DiskEncrypt does not match the expectation.
INVALIDPARAMETER_INVALIDDISKENCRYPT = 'InvalidParameter.InvalidDiskEncrypt'

# Whether to enable the Enhanced ssd cloud disk DiskEnhance does not match the expectation.
INVALIDPARAMETER_INVALIDDISKENHANCE = 'InvalidParameter.InvalidDiskEnhance'

# The value of the node disk capacity DiskSize does not match the expectation.
INVALIDPARAMETER_INVALIDDISKSIZE = 'InvalidParameter.InvalidDiskSize'

# The value of the node disk type DiskType does not match the expectation.
INVALIDPARAMETER_INVALIDDISKTYPE = 'InvalidParameter.InvalidDiskType'

# The EsAcl value does not match the expectation.
INVALIDPARAMETER_INVALIDESACL = 'InvalidParameter.InvalidEsACL'

# The instance version EsVersion does not match the expectation.
INVALIDPARAMETER_INVALIDESVERSION = 'InvalidParameter.InvalidEsVersion'

# The value of the created JSON-formatted index metadata IndexMetaJson does not match expectations.
INVALIDPARAMETER_INVALIDINDEXMETAJSON = 'InvalidParameter.InvalidIndexMetaJson'

# The value of IndexName does not match the expected value.
INVALIDPARAMETER_INVALIDINDEXNAME = 'InvalidParameter.InvalidIndexName'

# The value of IndexType does not match the expected value.
INVALIDPARAMETER_INVALIDINDEXTYPE = 'InvalidParameter.InvalidIndexType'

# Invalid InstanceId. No corresponding resources were found.
INVALIDPARAMETER_INVALIDINSTANCEID = 'InvalidParameter.InvalidInstanceId'

# The Ip address value does not meet expectations.
INVALIDPARAMETER_INVALIDIP = 'InvalidParameter.InvalidIp'

# The value of IpList in the private network vip list does not meet expectations.
INVALIDPARAMETER_INVALIDIPLIST = 'InvalidParameter.InvalidIpList'

# The value of the Kibana private network access port does not match the expectation.
INVALIDPARAMETER_INVALIDKIBANAPRIVATEPORT = 'InvalidParameter.InvalidKibanaPrivatePort'

# The value of the pagination size Limit does not match the expectation.
INVALIDPARAMETER_INVALIDLIMIT = 'InvalidParameter.InvalidLimit'

# The value of the log type LogType does not match the expected value.
INVALIDPARAMETER_INVALIDLOGTYPE = 'InvalidParameter.InvalidLogType'

# The information of ZoneDetail in multi-AZ deployment does not meet expectations.
INVALIDPARAMETER_INVALIDMULTIZONEINFO = 'InvalidParameter.InvalidMultiZoneInfo'

# The value of NodeNames does not match the expected value.
INVALIDPARAMETER_INVALIDNODENAMES = 'InvalidParameter.InvalidNodeNames'

# The value of NodeNum does not match the expected value.
INVALIDPARAMETER_INVALIDNODENUM = 'InvalidParameter.InvalidNodeNum'

# The value of NodeType does not match the expected value.
INVALIDPARAMETER_INVALIDNODETYPE = 'InvalidParameter.InvalidNodeType'

# The pagination starting value Offset does not match the expectation.
INVALIDPARAMETER_INVALIDOFFSET = 'InvalidParameter.InvalidOffset'

# The value of the operation type OpType does not match the expected value.
INVALIDPARAMETER_INVALIDOPTYPE = 'InvalidParameter.InvalidOpType'

# The value of the maintenance time slot OperationDuration does not match the expectation.
INVALIDPARAMETER_INVALIDOPERATIONDURATION = 'InvalidParameter.InvalidOperationDuration'

# The value of the sorting field OrderByKey does not match the expected value.
INVALIDPARAMETER_INVALIDORDERBYKEY = 'InvalidParameter.InvalidOrderByKey'

# The value of OrderByType does not match the expected sorting method.
INVALIDPARAMETER_INVALIDORDERBYTYPE = 'InvalidParameter.InvalidOrderByType'

# The value of PrivateAccess for private network access does not match the expectation.
INVALIDPARAMETER_INVALIDPRIVATEACCESS = 'InvalidParameter.InvalidPrivateAccess'

# The value of PublicAccess for public network access does not match the expectation.
INVALIDPARAMETER_INVALIDPUBLICACCESS = 'InvalidParameter.InvalidPublicAccess'

# Invalid lucene syntax
INVALIDPARAMETER_INVALIDQUERYSTRING = 'InvalidParameter.InvalidQueryString'

# The Region value does not meet the expectation.
INVALIDPARAMETER_INVALIDREGION = 'InvalidParameter.InvalidRegion'

# The value of the selectable restart mode RestartMode does not match the expected one.
INVALIDPARAMETER_INVALIDRESTARTMODE = 'InvalidParameter.InvalidRestartMode'

# The value of RestartType does not match the expected restart mode.
INVALIDPARAMETER_INVALIDRESTARTTYPE = 'InvalidParameter.InvalidRestartType'

# The value of SubnetId for the subnet ID does not meet expectations.
INVALIDPARAMETER_INVALIDSUBNETID = 'InvalidParameter.InvalidSubnetId'

# The value of the Unified Virtual Subnet ID list does not meet expectations.
INVALIDPARAMETER_INVALIDSUBNETUIDLIST = 'InvalidParameter.InvalidSubnetUidList'

# The value of the node tag information TagInfo does not match the expected value.
INVALIDPARAMETER_INVALIDTAGINFO = 'InvalidParameter.InvalidTagInfo'

# The value of the node tag information list TagList does not match the expected value.
INVALIDPARAMETER_INVALIDTAGLIST = 'InvalidParameter.InvalidTagList'

# The value or format of a time-related parameter does not match the expected one.
INVALIDPARAMETER_INVALIDTIMEPARAM = 'InvalidParameter.InvalidTimeParam'

# The value of Type does not match the expected value.
INVALIDPARAMETER_INVALIDTYPE = 'InvalidParameter.InvalidType'

# The UIN value does not match the expectation.
INVALIDPARAMETER_INVALIDUIN = 'InvalidParameter.InvalidUin'

# The value of the updated json-formatted index metadata UpdateMetaJson does not match expectations.
INVALIDPARAMETER_INVALIDUPDATEMETAJSON = 'InvalidParameter.InvalidUpdateMetaJson'

# The value of the update type UpdateType does not match the expected value.
INVALIDPARAMETER_INVALIDUPDATETYPE = 'InvalidParameter.InvalidUpdateType'

# The value of the voucher ID list VoucherIds does not match the expectation.
INVALIDPARAMETER_INVALIDVOUCHERIDS = 'InvalidParameter.InvalidVoucherIds'

# The information of the availability zone Zone does not meet expectations.
INVALIDPARAMETER_INVALIDZONE = 'InvalidParameter.InvalidZone'

# Invalid parameter value for billing type `ChargeType`.
INVALIDPARAMETERVALUE_CHARGETYPE = 'InvalidParameterValue.ChargeType'

# Component configuration value error.
INVALIDPARAMETERVALUE_CONFIGINFO = 'InvalidParameterValue.ConfigInfo'

# Invalid ES configuration type.
INVALIDPARAMETERVALUE_ESCONFIGTYPE = 'InvalidParameterValue.EsConfigType'

# For cluster stability, currently only support installing 1 user plugin at the same time.
INVALIDPARAMETERVALUE_INSTALLPLUGINLIST = 'InvalidParameterValue.InstallPluginList'

# Instance name verification failed. Enter it according to the rule.
INVALIDPARAMETERVALUE_INSTANCENAME = 'InvalidParameterValue.InstanceName'

# Deadline conflict.
INVALIDPARAMETERVALUE_INVALIDDEADLINE = 'InvalidParameterValue.InvalidDeadline'

# Password verification is invalid.
INVALIDPARAMETERVALUE_PASSWORD = 'InvalidParameterValue.Password'

# Invalid value of the plug-in type PluginType.
INVALIDPARAMETERVALUE_PLUGINTYPE = 'InvalidParameterValue.PluginType'

# The parameter value of the auto-renewal flag RenewFlag is incorrect.
INVALIDPARAMETERVALUE_RENEWFLAG = 'InvalidParameterValue.RenewFlag'

# Invalid value of the upgrade method parameter UpgradeMode.
INVALIDPARAMETERVALUE_UPGRADEMODE = 'InvalidParameterValue.UpgradeMode'

# The number of clusters under this account exceeds the limit.
LIMITEXCEEDED_CLUSTERNUM = 'LimitExceeded.ClusterNum'

# Node count or index storage volume exceeds the limit.
LIMITEXCEEDED_NODENUMORINDICES = 'LimitExceeded.NodeNumOrIndices'

# Exceeds the maximum number of custom plugins. Please delete some custom plugins first.
LIMITEXCEEDED_PLUGININSTALL = 'LimitExceeded.PluginInstall'

# Exceed the maximum resource limit a user can possess.
LIMITEXCEEDED_RESOURCELIMIT = 'LimitExceeded.ResourceLimit'

# packet size of the backend service exceeded the quota limit
LIMITEXCEEDED_RESPONSEPACKAGEOVERSIZE = 'LimitExceeded.ResponsePackageOversize'

# time of the backend service exceeded the quota limit
LIMITEXCEEDED_RESPONSETIMEOUT = 'LimitExceeded.ResponseTimeout'

# Too many update parameter values. The limit is exceeded.
LIMITEXCEEDED_UPDATEITEMLIMIT = 'LimitExceeded.UpdateItemLimit'

# The resource is occupied.
RESOURCEINUSE = 'ResourceInUse'

# Order locked.
RESOURCEINUSE_ORDER = 'ResourceInUse.Order'

# Insufficient resources.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The account balance is insufficient.
RESOURCEINSUFFICIENT_BALANCE = 'ResourceInsufficient.Balance'

# Insufficient computing resources. Replace the availability zone or adjust the model.
RESOURCEINSUFFICIENT_CVM = 'ResourceInsufficient.CVM'

# Insufficient resources for dedicated master nodes in hidden AZs.
RESOURCEINSUFFICIENT_HIDDENZONE = 'ResourceInsufficient.HiddenZone'

# Insufficient remaining IPs in subnet.
RESOURCEINSUFFICIENT_SUBNET = 'ResourceInsufficient.Subnet'

# Insufficient available subnet IP.
RESOURCEINSUFFICIENT_SUBNETIP = 'ResourceInsufficient.SubnetIp'

# Insufficient resources in the availability zone.
RESOURCEINSUFFICIENT_ZONE = 'ResourceInsufficient.Zone'

# CAM resource is not found.
RESOURCENOTFOUND_CAMINFONOTFOUND = 'ResourceNotFound.CAMInfoNotFound'

# Failed to obtain the cluster resource.
RESOURCENOTFOUND_CLUSTERINFONOTFOUND = 'ResourceNotFound.ClusterInfoNotFound'

# Failed to obtain COS related information.
RESOURCENOTFOUND_COSINFONOTFOUND = 'ResourceNotFound.CosInfoNotFound'

# Failed to obtain the database resource.
RESOURCENOTFOUND_DBINFONOTFOUND = 'ResourceNotFound.DBInfoNotFound'

# Data node information not found.
RESOURCENOTFOUND_DATANODENOTFOUND = 'ResourceNotFound.DataNodeNotFound'

# Failed to obtain disk-related resources.
RESOURCENOTFOUND_DISKINFONOTFOUND = 'ResourceNotFound.DiskInfoNotFound'

# Failed to obtain the billing resource.
RESOURCENOTFOUND_TRADECGWNOTFOUND = 'ResourceNotFound.TradeCgwNotFound'

# Failed to obtain the VPC resource.
RESOURCENOTFOUND_VPCINFONOTFOUND = 'ResourceNotFound.VPCInfoNotFound'

# Failed to obtain the allowlist resource.
RESOURCENOTFOUND_WHITELISTNOTFOUND = 'ResourceNotFound.WhiteListNotFound'

# Uin is not in the allowlist.
UNAUTHORIZEDOPERATION_UINNOTINWHITELIST = 'UnauthorizedOperation.UinNotInWhiteList'

# The operation is not supported.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# Authentication method not supported.
UNSUPPORTEDOPERATION_BASICSECURITYTYPE = 'UnsupportedOperation.BasicSecurityType'

# Configuration adjustments are not supported for node or disk.
UNSUPPORTEDOPERATION_CHANGENODETYPE = 'UnsupportedOperation.ChangeNodeType'

# saml logon is enabled for the cluster. You cannot switch directly from https to http protocol.
UNSUPPORTEDOPERATION_CLOSEHTTPSWITHSAML = 'UnsupportedOperation.CloseHttpsWithSaml'

# Does not support this operation. Allocated tablets exist in the cluster.
UNSUPPORTEDOPERATION_CLUSTERSHARDNUM = 'UnsupportedOperation.ClusterShardNum'

# Some indexes in the cluster are closed.
UNSUPPORTEDOPERATION_CLUSTERSTATECLOSE = 'UnsupportedOperation.ClusterStateClose'

# Some indexes in the cluster have no backup.
UNSUPPORTEDOPERATION_CLUSTERSTATENOREPLICATION = 'UnsupportedOperation.ClusterStateNoReplication'

# Cluster status is abnormal (not green).
UNSUPPORTEDOPERATION_CLUSTERSTATEUNHEALTH = 'UnsupportedOperation.ClusterStateUnHealth'

# Unsupported version for cos Backup. The cluster must be restarted to allow cos Backup.
UNSUPPORTEDOPERATION_COSBACKUP = 'UnsupportedOperation.CosBackUp'

# The current running status of cvm is unsupported.
UNSUPPORTEDOPERATION_CVMSTATENOTSUPPORTED = 'UnsupportedOperation.CvmStateNotSupported'

# cvm instances that are shut down
UNSUPPORTEDOPERATION_CVMSTATUSSTOPPED = 'UnsupportedOperation.CvmStatusStopped'

# Insufficient free space on the node disk
UNSUPPORTEDOPERATION_DISKFREESPACEINSUFFICIENT = 'UnsupportedOperation.DiskFreeSpaceInsufficient'

# This operation only supports elastic cloud disks.
UNSUPPORTEDOPERATION_DISKNOTPORTABLE = 'UnsupportedOperation.DiskNotPortable'

# Current disk status not supported
UNSUPPORTEDOPERATION_DISKSTATENOTSUPPORTED = 'UnsupportedOperation.DiskStateNotSupported'

# Disk type modification path not supported
UNSUPPORTEDOPERATION_DISKTYPECHANGEPATHNOTSUPPORTED = 'UnsupportedOperation.DiskTypeChangePathNotSupported'

# An incomplete heterogeneous scaling process exists.
UNSUPPORTEDOPERATION_HETEROSCALINGEXECUTING = 'UnsupportedOperation.HeteroScalingExecuting'

# The cluster has the index setting `index.routing.allocation.require._name`, `_ip`, or `_id`.
UNSUPPORTEDOPERATION_INDEXSETTINGSREQUIRESET = 'UnsupportedOperation.IndexSettingsRequireSet'

# This operation is not supported. The service type is incorrect.
UNSUPPORTEDOPERATION_INSTANCETYPEERROR = 'UnsupportedOperation.InstanceTypeError'

# The current ES cluster edition is too low and does not support Gpu machines.
UNSUPPORTEDOPERATION_KERNELNOTSUPPORTGPU = 'UnsupportedOperation.KernelNotSupportGpu'

# The operation is not supported. The license type is incorrect.
UNSUPPORTEDOPERATION_LICENSEERROR = 'UnsupportedOperation.LicenseError'

# Local disk models are not supported.
UNSUPPORTEDOPERATION_LOCALDISK = 'UnsupportedOperation.LocalDisk'

# Configuration adjustments across multiple availability zones are not supported.
UNSUPPORTEDOPERATION_MULTIZONESUPGRADE = 'UnsupportedOperation.MultiZonesUpgrade'

# Sorry, you need to go to the ES console purchase page to complete confirmation and authentication before we can offer the selected Tencent Cloud service. If you have any questions regarding the confirmation process, contact us: https://www.tencentcloud.com/zh/contact-us.
UNSUPPORTEDOPERATION_NOTAGREEMENT = 'UnsupportedOperation.NotAgreement'

# This operation only supports data disks.
UNSUPPORTEDOPERATION_NOTDATADISK = 'UnsupportedOperation.NotDataDisk'

# The plugin is not supported.
UNSUPPORTEDOPERATION_PLUGIN = 'UnsupportedOperation.Plugin'

# Offline node blue-green change has risks. Select restart "in-place" directly.
UNSUPPORTEDOPERATION_RESTARTMODE = 'UnsupportedOperation.RestartMode'

# Vertically scale in too many resources.
UNSUPPORTEDOPERATION_SCALEDOWNTOOMUCH = 'UnsupportedOperation.ScaleDownTooMuch'

# This operation is not supported for single-node instances.
UNSUPPORTEDOPERATION_SINGLENODECLUSTERNOTSUPPORT = 'UnsupportedOperation.SingleNodeClusterNotSupport'

# This operation is not supported. The instance is not running as normal.
UNSUPPORTEDOPERATION_STATUSNOTNORMAL = 'UnsupportedOperation.StatusNotNormal'

# This operation is not supported. The instance status is incorrect.
UNSUPPORTEDOPERATION_STATUSNOTSUPPORT = 'UnsupportedOperation.StatusNotSupport'

# Disk type update not supported.
UNSUPPORTEDOPERATION_UPDATEDISKTYPE = 'UnsupportedOperation.UpdateDiskType'

# Failed to obtain the VPC resource.
UNSUPPORTEDOPERATION_VPCINFONOTFOUND = 'UnsupportedOperation.VPCInfoNotFound'

# Unsupported web component.
UNSUPPORTEDOPERATION_WEBSERVICETYPE = 'UnsupportedOperation.WebServiceType'
