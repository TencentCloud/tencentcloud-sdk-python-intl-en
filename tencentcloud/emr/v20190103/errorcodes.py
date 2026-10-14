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


# CAM signature/authentication error.
AUTHFAILURE = 'AuthFailure'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Operation failed.
FAILEDOPERATION_CHECKIFSUPPORTPODSTRETCH = 'FailedOperation.CheckIfSupportPodStretch'

# DB exception.
FAILEDOPERATION_DBEXCEPTION = 'FailedOperation.DBException'

# Failed to pull resource tags.
FAILEDOPERATION_DESCRIBERESOURCETAGSFAILED = 'FailedOperation.DescribeResourceTagsFailed'

# Duplicate order. Please check the EMR console.
FAILEDOPERATION_DUPLICATEORDERNOTALLOWED = 'FailedOperation.DuplicateOrderNotAllowed'

# Failed to obtain the CAM role.
FAILEDOPERATION_GETCAMROLEFAILED = 'FailedOperation.GetCamRoleFailed'

# Failed to call the CAM service.
FAILEDOPERATION_GETCAMSERVERFAILED = 'FailedOperation.GetCamServerFailed'

# Failed to obtain the CVM specifications information.
FAILEDOPERATION_GETCVMCONFIGQUOTAFAILED = 'FailedOperation.GetCvmConfigQuotaFailed'

# Failed to call the CVM service.
FAILEDOPERATION_GETCVMSERVERFAILED = 'FailedOperation.GetCvmServerFailed'

# Failed to call the inquiry center service.
FAILEDOPERATION_GETTRADESERVERFAILED = 'FailedOperation.GetTradeServerFailed'

# Insufficient balance.
FAILEDOPERATION_INSUFFICIENTACCOUNTBALANCE = 'FailedOperation.InsufficientAccountBalance'

# No more scaling rules are allowed.
FAILEDOPERATION_MORESTRATEGYNOTALLOWED = 'FailedOperation.MoreStrategyNotAllowed'

# The Namespace has user-manually launched Pods.
FAILEDOPERATION_NAMESPACEHASUSERCUSTOMPODS = 'FailedOperation.NamespaceHasUserCustomPods'

# Unauthorized operation.
FAILEDOPERATION_NOTAUTHENTICATED = 'FailedOperation.NotAuthenticated'

# Operation failed. Pod is not supported.
FAILEDOPERATION_NOTSUPPORTPOD = 'FailedOperation.NotSupportPod'

# Operation failed.
FAILEDOPERATION_REFUNDCVMFAILED = 'FailedOperation.RefundCvmFailed'

# Operation failed.
FAILEDOPERATION_SPECDELETEDENYFORAUTOSCALESTRATEGIES = 'FailedOperation.SpecDeleteDenyForAutoScaleStrategies'

# Internal error.
INTERNALERROR = 'InternalError'

# Internal service call exception.
INTERNALERROR_ACCOUNTCGWERROR = 'InternalError.AccountCgwError'

# Internal service call exception.
INTERNALERROR_CAMCGWERROR = 'InternalError.CamCgwError'

# Internal service call exception.
INTERNALERROR_CAMERROR = 'InternalError.CamError'

# Internal service call exception.
INTERNALERROR_CBSCGWERROR = 'InternalError.CbsCgwError'

# Internal service call exception.
INTERNALERROR_CBSERROR = 'InternalError.CbsError'

# Internal service call exception.
INTERNALERROR_CDBCGWERROR = 'InternalError.CdbCgwError'

# Internal service call exception.
INTERNALERROR_CDBERROR = 'InternalError.CdbError'

# Insufficient CVM or CBS resources, or invalid software.
INTERNALERROR_CHECKQUOTAERR = 'InternalError.CheckQuotaErr'

# Internal service call exception.
INTERNALERROR_CONFIGCGWERROR = 'InternalError.ConfigCgwError'

# Internal service call exception.
INTERNALERROR_CVMERROR = 'InternalError.CvmError'

# DB query exception.
INTERNALERROR_DBQUERYEXCEPTION = 'InternalError.DBQueryException'

# OpenTSDB request exception.
INTERNALERROR_DOOPENTSDBREQUESTEXCEPTION = 'InternalError.DoOpenTSDBRequestException'

# EKS call error.
INTERNALERROR_EKSERROR = 'InternalError.EKSError'

# Internal service call exception.
INTERNALERROR_KMSERROR = 'InternalError.KmsError'

# Failed to request OpenTSDB.
INTERNALERROR_OPENTSDBHTTPRETURNCODENOTOK = 'InternalError.OpenTSDBHttpReturnCodeNotOK'

# Internal service call exception.
INTERNALERROR_PROJECTCGWERROR = 'InternalError.ProjectCgwError'

# An exception occurred when the security group API is called.
INTERNALERROR_SGERROR = 'InternalError.SgError'

# TKE call error.
INTERNALERROR_TKEERROR = 'InternalError.TKEError'

# Internal service call exception.
INTERNALERROR_TAGERROR = 'InternalError.TagError'

# Internal service call exception.
INTERNALERROR_TRADECGWERROR = 'InternalError.TradeCgwError'

# Internal service call exception.
INTERNALERROR_VPCCGWERROR = 'InternalError.VpcCgwError'

# Internal service call exception.
INTERNALERROR_VPCERROR = 'InternalError.VpcError'

# Internal service call exception.
INTERNALERROR_WOODSERVERERROR = 'InternalError.WoodServerError'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# Parameter error.
INVALIDPARAMETER_APPIDRESOURCENOTMATCH = 'InvalidParameter.AppIdResourceNotMatch'

# Invalid CpuType parameter.
INVALIDPARAMETER_CPUTYPE = 'InvalidParameter.CpuType'

# Display policy error.
INVALIDPARAMETER_DISPLAYSTRATEGYNOTMATCH = 'InvalidParameter.DisplayStrategyNotMatch'

# Parameter error.
INVALIDPARAMETER_HALESSMASTERCOUNT = 'InvalidParameter.HALessMasterCount'

# Impala query parameter exception.
INVALIDPARAMETER_IMPALAQUERYEXCEPTION = 'InvalidParameter.ImpalaQueryException'

# Invalid Common node quantity.
INVALIDPARAMETER_INCORRECTCOMMONCOUNT = 'InvalidParameter.IncorrectCommonCount'

# Invalid Master node quantity.
INVALIDPARAMETER_INCORRECTMASTERCOUNT = 'InvalidParameter.IncorrectMasterCount'

# Invalid AllNodeResourceSpec parameter.
INVALIDPARAMETER_INVALIDALLNODERESOURCESPEC = 'InvalidParameter.InvalidAllNodeResourceSpec'

# Invalid parameter: APPID.
INVALIDPARAMETER_INVALIDAPPID = 'InvalidParameter.InvalidAppId'

# Invalid auto-renewal flag.
INVALIDPARAMETER_INVALIDAUTORENEW = 'InvalidParameter.InvalidAutoRenew'

# Invalid Classification parameter value.
INVALIDPARAMETER_INVALIDCLASSIFICATION = 'InvalidParameter.InvalidClassification'

# Invalid ClickHouse cluster.
INVALIDPARAMETER_INVALIDCLICKHOUSECLUSTER = 'InvalidParameter.InvalidClickHouseCluster'

# Invalid ClientToken.
INVALIDPARAMETER_INVALIDCLIENTTOKEN = 'InvalidParameter.InvalidClientToken'

# Invalid parameter: ClusterId.
INVALIDPARAMETER_INVALIDCLUSTERID = 'InvalidParameter.InvalidClusterId'

# Parameter error.
INVALIDPARAMETER_INVALIDCOMMONDISKTYPE = 'InvalidParameter.InvalidCommonDiskType'

# Illegal metric comparison method.
INVALIDPARAMETER_INVALIDCOMPAREMETHOD = 'InvalidParameter.InvalidCompareMethod'

# Invalid component.
INVALIDPARAMETER_INVALIDCOMPONENT = 'InvalidParameter.InvalidComponent'

# At least one trigger condition is required.
INVALIDPARAMETER_INVALIDCONDITIONNUM = 'InvalidParameter.InvalidConditionNum'

# The delivered configuration file type is invalid.
INVALIDPARAMETER_INVALIDCONFIGTYPE = 'InvalidParameter.InvalidConfigType'

# Invalid Core node quantity.
INVALIDPARAMETER_INVALIDCORECOUNT = 'InvalidParameter.InvalidCoreCount'

# Parameter error.
INVALIDPARAMETER_INVALIDCOREDISKTYPE = 'InvalidParameter.InvalidCoreDiskType'

# Invalid CosBucket.
INVALIDPARAMETER_INVALIDCOSBUCKET = 'InvalidParameter.InvalidCosBucket'

# Invalid CosFileUri parameter value.
INVALIDPARAMETER_INVALIDCOSFILEURI = 'InvalidParameter.InvalidCosFileURI'

# The scale-out quantity must be greater than 0.
INVALIDPARAMETER_INVALIDCOUNT = 'InvalidParameter.InvalidCount'

# The same request can only scale out Task or Core nodes.
INVALIDPARAMETER_INVALIDCOUNTNUM = 'InvalidParameter.InvalidCountNum'

# Error message: Invalid PodParameter.
INVALIDPARAMETER_INVALIDCUSTOMIZEDPODPARAM = 'InvalidParameter.InvalidCustomizedPodParam'

# The DependService and EnableKerberos parameters conflict.
INVALIDPARAMETER_INVALIDDEPENDSERVICEANDENABLEKERBEROSCONFLICT = 'InvalidParameter.InvalidDependServiceAndEnableKerberosConflict'

# Number of invalid disks.
INVALIDPARAMETER_INVALIDDISKNUM = 'InvalidParameter.InvalidDiskNum'

# Invalid disk size.
INVALIDPARAMETER_INVALIDDISKSIZE = 'InvalidParameter.InvalidDiskSize'

# Parameter error.
INVALIDPARAMETER_INVALIDDISKTYPE = 'InvalidParameter.InvalidDiskType'

# Invalid download object parameter value.
INVALIDPARAMETER_INVALIDDOWNLOADOBJ = 'InvalidParameter.InvalidDownloadObj'

# Invalid DynamicInstanceType parameter.
INVALIDPARAMETER_INVALIDDYNAMICINSTANCETYPE = 'InvalidParameter.InvalidDynamicInstanceType'

# Invalid EKS instance.
INVALIDPARAMETER_INVALIDEKSINSTANCE = 'InvalidParameter.InvalidEksInstance'

# The specified parameter for exporting configuration files is incorrect.
INVALIDPARAMETER_INVALIDEXPORTCONFCONTEXTS = 'InvalidParameter.InvalidExportConfContexts'

# Invalid CustomConfig parameter value.
INVALIDPARAMETER_INVALIDEXTENDFIELD = 'InvalidParameter.InvalidExtendField'

# Invalid NameServiceName parameter value.
INVALIDPARAMETER_INVALIDEXTENDNAMESERVICE = 'InvalidParameter.InvalidExtendNameService'

# Invalid file path parameter value.
INVALIDPARAMETER_INVALIDFILEPATH = 'InvalidParameter.InvalidFilePath'

# Invalid filter parameter.
INVALIDPARAMETER_INVALIDFILTERKEY = 'InvalidParameter.InvalidFilterKey'

# Illegal instance billing mode.
INVALIDPARAMETER_INVALIDINSTANCECHARGETYPE = 'InvalidParameter.InvalidInstanceChargeType'

# Invalid cluster name.
INVALIDPARAMETER_INVALIDINSTANCENAME = 'InvalidParameter.InvalidInstanceName'

# Invalid instance type.
INVALIDPARAMETER_INVALIDINSTANCETYPE = 'InvalidParameter.InvalidInstanceType'

# The specified termination IP address is invalid.
INVALIDPARAMETER_INVALIDIPLIST = 'InvalidParameter.InvalidIpList'

# Invalid flow task.
INVALIDPARAMETER_INVALIDJOBFLOW = 'InvalidParameter.InvalidJobFlow'

# Invalid LoadBalancerId.
INVALIDPARAMETER_INVALIDLOADBALANCER = 'InvalidParameter.InvalidLoadBalancer'

# Invalid login settings.
INVALIDPARAMETER_INVALIDLOGINSETTING = 'InvalidParameter.InvalidLoginSetting'

# Parameter error.
INVALIDPARAMETER_INVALIDMASTERDISKTYPE = 'InvalidParameter.InvalidMasterDiskType'

# Invalid metadata database URL.
INVALIDPARAMETER_INVALIDMETADATAJDBCURL = 'InvalidParameter.InvalidMetaDataJdbcUrl'

# Invalid metadata table type.
INVALIDPARAMETER_INVALIDMETATYPE = 'InvalidParameter.InvalidMetaType'

# Invalid specifications for configuration change.
INVALIDPARAMETER_INVALIDMODIFYSPEC = 'InvalidParameter.InvalidModifySpec'

# Number of illegal nodes.
INVALIDPARAMETER_INVALIDNODECOUNT = 'InvalidParameter.InvalidNodeCount'

# Illegal node type.
INVALIDPARAMETER_INVALIDNODEFLAG = 'InvalidParameter.InvalidNodeFlag'

# Invalid NodeType.
INVALIDPARAMETER_INVALIDNODETYPE = 'InvalidParameter.InvalidNodeType'

# The SoftInfo parameter is invalid.
INVALIDPARAMETER_INVALIDPARAMTERINVALIDSOFTINFO = 'InvalidParameter.InvalidParamterInvalidSoftInfo'

# Invalid password.
INVALIDPARAMETER_INVALIDPASSWORD = 'InvalidParameter.InvalidPassword'

# Invalid payment type.
INVALIDPARAMETER_INVALIDPAYMODE = 'InvalidParameter.InvalidPaymode'

# Invalid PodNum parameter.
INVALIDPARAMETER_INVALIDPODNUM = 'InvalidParameter.InvalidPodNum'

# Invalid bootstrap operation script.
INVALIDPARAMETER_INVALIDPREEXECUTEDFILE = 'InvalidParameter.InvalidPreExecutedFile'

# Illegal metric processing method.
INVALIDPARAMETER_INVALIDPROCESSMETHOD = 'InvalidParameter.InvalidProcessMethod'

# Invalid product ID.
INVALIDPARAMETER_INVALIDPRODUCTID = 'InvalidParameter.InvalidProductId'

# Invalid product version.
INVALIDPARAMETER_INVALIDPRODUCTVERSION = 'InvalidParameter.InvalidProductVersion'

# Invalid project ID.
INVALIDPARAMETER_INVALIDPROJECTID = 'InvalidParameter.InvalidProjectId'

# Invalid Region parameter value.
INVALIDPARAMETER_INVALIDREGION = 'InvalidParameter.InvalidRegion'

# Illegal auto-renewal flag.
INVALIDPARAMETER_INVALIDRENEWFLAG = 'InvalidParameter.InvalidRenewFlag'

# Invalid ResType value.
INVALIDPARAMETER_INVALIDRESTYPE = 'InvalidParameter.InvalidResType'

# Invalid resource ID.
INVALIDPARAMETER_INVALIDRESOURCEID = 'InvalidParameter.InvalidResourceId'

# Invalid resource ID.
INVALIDPARAMETER_INVALIDRESOURCEIDS = 'InvalidParameter.InvalidResourceIds'

# Invalid resource specifications.
INVALIDPARAMETER_INVALIDRESOURCESPEC = 'InvalidParameter.InvalidResourceSpec'

# Invalid number of Router nodes to be scaled out.
INVALIDPARAMETER_INVALIDROUTERCOUNT = 'InvalidParameter.InvalidRouterCount'

# Invalid scaling action.
INVALIDPARAMETER_INVALIDSCALEACTION = 'InvalidParameter.InvalidScaleAction'

# Invalid bootstrap script execution parameters.
INVALIDPARAMETER_INVALIDSCRIPTBOOTSTRAPACTIONCONFIG = 'InvalidParameter.InvalidScriptBootstrapActionConfig'

# This EMR version does not support enabling security mode.
INVALIDPARAMETER_INVALIDSECURITYSUPPORT = 'InvalidParameter.InvalidSecuritySupport'

# Invalid security group ID.
INVALIDPARAMETER_INVALIDSERCURITYGRPUPID = 'InvalidParameter.InvalidSercurityGrpupId'

# Invalid service name.
INVALIDPARAMETER_INVALIDSERVICENAME = 'InvalidParameter.InvalidServiceName'

# The ServiceNodeInfo parameter is invalid or incorrect.
INVALIDPARAMETER_INVALIDSERVICENODEINFO = 'InvalidParameter.InvalidServiceNodeInfo'

# The InvalidSoftDeployInfo parameter is invalid or incorrect.
INVALIDPARAMETER_INVALIDSOFTDEPLOYINFO = 'InvalidParameter.InvalidSoftDeployInfo'

# The SoftInfo parameter is invalid.
INVALIDPARAMETER_INVALIDSOFTINFO = 'InvalidParameter.InvalidSoftInfo'

# Parameter error.
INVALIDPARAMETER_INVALIDSOFTWARE = 'InvalidParameter.InvalidSoftWare'

# Invalid software name.
INVALIDPARAMETER_INVALIDSOFTWARENAME = 'InvalidParameter.InvalidSoftWareName'

# Invalid software version.
INVALIDPARAMETER_INVALIDSOFTWAREVERSION = 'InvalidParameter.InvalidSoftWareVersion'

# Invalid StartTime or EndTime parameter.
INVALIDPARAMETER_INVALIDSTARTTIMEORENDTIME = 'InvalidParameter.InvalidStartTimeOrEndTime'

# Invalid StatisticPeriod or TriggerThreshold parameter.
INVALIDPARAMETER_INVALIDSTATISTICPERIODORTRIGGERTHRESHOLD = 'InvalidParameter.InvalidStatisticPeriodOrTriggerThreshold'

# Parameter error.
INVALIDPARAMETER_INVALIDSTRATEGY = 'InvalidParameter.InvalidStrategy'

# Invalid rule priority.
INVALIDPARAMETER_INVALIDSTRATEGYPRIORITY = 'InvalidParameter.InvalidStrategyPriority'

# Invalid specifications.
INVALIDPARAMETER_INVALIDSTRATEGYSPEC = 'InvalidParameter.InvalidStrategySpec'

# Unsupported scaling policy type.
INVALIDPARAMETER_INVALIDSTRATEGYTYPE = 'InvalidParameter.InvalidStrategyType'

# Invalid subnet ID.
INVALIDPARAMETER_INVALIDSUBNETID = 'InvalidParameter.InvalidSubnetId'

# Invalid high availability parameter.
INVALIDPARAMETER_INVALIDSUPPORTHA = 'InvalidParameter.InvalidSupportHA'

# The number of tasks cannot exceed 20.
INVALIDPARAMETER_INVALIDTASKCOUNT = 'InvalidParameter.InvalidTaskCount'

# Parameter error.
INVALIDPARAMETER_INVALIDTIMELAYOUT = 'InvalidParameter.InvalidTimeLayout'

# Invalid timespan.
INVALIDPARAMETER_INVALIDTIMESPAN = 'InvalidParameter.InvalidTimeSpan'

# Invalid TimeUnit.
INVALIDPARAMETER_INVALIDTIMEUNIT = 'InvalidParameter.InvalidTimeUnit'

# Invalid TKE cluster ID, or the TKE cluster does not meet the criteria.
INVALIDPARAMETER_INVALIDTKEINSTANCE = 'InvalidParameter.InvalidTkeInstance'

# Invalid input for the parent account UIN parameter.
INVALIDPARAMETER_INVALIDUINNUM = 'InvalidParameter.InvalidUinNum'

# Invalid unified metadata database.
INVALIDPARAMETER_INVALIDUNIFYMETA = 'InvalidParameter.InvalidUnifyMeta'

# Parameter error.
INVALIDPARAMETER_INVALIDVENDORTYPE = 'InvalidParameter.InvalidVendorType'

# Parameter error.
INVALIDPARAMETER_INVALIDVOLUMETYPE = 'InvalidParameter.InvalidVolumeType'

# Invalid VPC ID.
INVALIDPARAMETER_INVALIDVPCID = 'InvalidParameter.InvalidVpcId'

# Invalid WriteFile parameter value in cosFileUri.
INVALIDPARAMETER_INVALIDWRITEFILE = 'InvalidParameter.InvalidWriteFile'

# Invalid AZ.
INVALIDPARAMETER_INVALIDZONE = 'InvalidParameter.InvalidZone'

# Invalid Kerberos support flag.
INVALIDPARAMETER_KERBEROSSUPPORT = 'InvalidParameter.KerberosSupport'

# Parameter error.
INVALIDPARAMETER_LESSCOMMONCOUNT = 'InvalidParameter.LessCommonCount'

# Parameter error.
INVALIDPARAMETER_LESSTASKCOUNT = 'InvalidParameter.LessTaskCount'

# The number of CVM instances exceeds the maximum limit.
INVALIDPARAMETER_MOREMAXLIMITNUM = 'InvalidParameter.MoreMaxlimitNum'

# Invalid parameter. It does not contain required components.
INVALIDPARAMETER_NOTCONTAINMUSTSELECTSOFTWARE = 'InvalidParameter.NotContainMustSelectSoftware'

# Sorting field error.
INVALIDPARAMETER_ORDERFIELDNOTMATCH = 'InvalidParameter.OrderFieldNotMatch'

# The payment mode does not match resources.
INVALIDPARAMETER_PAYMODERESOURCENOTMATCH = 'InvalidParameter.PayModeResourceNotMatch'

# The project does not match resources.
INVALIDPARAMETER_PROJECTRESOURCENOTMATCH = 'InvalidParameter.ProjectResourceNotMatch'

# Duplicate execution time.
INVALIDPARAMETER_REPEATEDEXECUTIONTIME = 'InvalidParameter.RepeatedExecutionTime'

# Duplicate scaling rule name.
INVALIDPARAMETER_REPEATEDSTRATEGYNAME = 'InvalidParameter.RepeatedStrategyName'

# Invalid ResourceProviderType parameter.
INVALIDPARAMETER_RESOURCEPROVIDERTYPE = 'InvalidParameter.ResourceProviderType'

# This service does not support restart.
INVALIDPARAMETER_RESTARTSERVICEUNSUPPORTED = 'InvalidParameter.RestartServiceUnsupported'

# Invalid product components exist.
INVALIDPARAMETER_SOFTWARENOTINPRODUCR = 'InvalidParameter.SoftwareNotInProducr'

# Invalid product components exist.
INVALIDPARAMETER_SOFTWARENOTINPRODUCT = 'InvalidParameter.SoftwareNotInProduct'

# The policy is authorization.
INVALIDPARAMETER_UNGRANTEDPOLICY = 'InvalidParameter.UngrantedPolicy'

# Role not authorized.
INVALIDPARAMETER_UNGRANTEDROLE = 'InvalidParameter.UngrantedRole'

# Parameter error.
INVALIDPARAMETER_UNSATISFIEDSOFTDEPENDECY = 'InvalidParameter.UnsatisfiedSoftDependecy'

# The AZ does not match resources.
INVALIDPARAMETER_ZONERESOURCENOTMATCH = 'InvalidParameter.ZoneResourceNotMatch'

# Parameter value error.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Invalid TKE cluster ID, or the TKE cluster does not meet the criteria.
INVALIDPARAMETERVALUE_INVALIDTKEINSTANCE = 'InvalidParameterValue.InvalidTkeInstance'

# The quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# The CPU request quantity of the Pod exceeds the cluster limit.
LIMITEXCEEDED_PODCPULIMITEXCEEDEDAVAILABLECPU = 'LimitExceeded.PodCpuLimitExceededAvailableCpu'

# The CPU request quantity of the Pod exceeds the node limit.
LIMITEXCEEDED_PODCPULIMITEXCEEDEDNODEAVAILABLECPU = 'LimitExceeded.PodCpuLimitExceededNodeAvailableCpu'

# Requests are backlogged and exceed the limit.
LIMITEXCEEDED_REQUESTBACKLOGEXCEEDSLIMIT = 'LimitExceeded.RequestBacklogExceedsLimit'

# The number of security groups exceeds the limit.
LIMITEXCEEDED_SECURITYGROUPNUMLIMITEXCEEDED = 'LimitExceeded.SecurityGroupNumLimitExceeded'

# The number of users exceeds the limit.
LIMITEXCEEDED_USERCOUNTEXCEEDSLIMIT = 'LimitExceeded.UserCountExceedsLimit'

# Missing parameter error.
MISSINGPARAMETER = 'MissingParameter'

# Missing parameter error.
MISSINGPARAMETER_MISSINGCORERESOURCE = 'MissingParameter.MissingCoreResource'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# The number of requests exceeds the frequency limit.
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# The instance is in process.
RESOURCEINUSE_INSTANCEINPROCESS = 'ResourceInUse.InstanceInProcess'

# The specifications of the hard disk do not meet the requirements.
RESOURCEINSUFFICIENT_DISKINSUFFICIENT = 'ResourceInsufficient.DiskInsufficient'

# The node specifications are not supported or have been sold out.
RESOURCEINSUFFICIENT_INSTANCEINSUFFICIENT = 'ResourceInsufficient.InstanceInsufficient'

# Resources do not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The instance cannot be found.
RESOURCENOTFOUND_CLUSTERNOTFOUND = 'ResourceNotFound.ClusterNotFound'

# The specified CVM instance cannot be found.
RESOURCENOTFOUND_CVMINSTANCENOTFOUND = 'ResourceNotFound.CvmInstanceNotFound'

# The hardware information cannot be found.
RESOURCENOTFOUND_HARDWAREINFONOTFOUND = 'ResourceNotFound.HardwareInfoNotFound'

# The instance cannot be found.
RESOURCENOTFOUND_INSTANCENOTFOUND = 'ResourceNotFound.InstanceNotFound'

# The monitoring metadata cannot be found.
RESOURCENOTFOUND_METRICSMETANOTFOUND = 'ResourceNotFound.MetricsMetaNotFound'

# The cluster does not have alternative specifications.
RESOURCENOTFOUND_OPTIONALSPECFOUND = 'ResourceNotFound.OptionalSpecFound'

# The monitoring metadata cannot be found.
RESOURCENOTFOUND_RESOURCENOTFOUND = 'ResourceNotFound.ResourceNotFound'

# The service component configuration cannot be found.
RESOURCENOTFOUND_SERVICECONFNOTFOUND = 'ResourceNotFound.ServiceConfNotFound'

# The service component cannot be found.
RESOURCENOTFOUND_SERVICEGROUPNOTFOUND = 'ResourceNotFound.ServiceGroupNotFound'

# The service node is not found.
RESOURCENOTFOUND_SERVICENODENOTFOUND = 'ResourceNotFound.ServiceNodeNotFound'

# The specifications do not exist.
RESOURCENOTFOUND_SPECNOTFOUND = 'ResourceNotFound.SpecNotFound'

# Corresponding scaling rules are not found.
RESOURCENOTFOUND_STRATEGYNOTFOUND = 'ResourceNotFound.StrategyNotFound'

# The corresponding subnet cannot be found.
RESOURCENOTFOUND_SUBNETNOTFOUND = 'ResourceNotFound.SubnetNotFound'

# The pre-installed components of the TKE cluster are not deployed.
RESOURCENOTFOUND_TKEPRECONDITIONNOTFOUND = 'ResourceNotFound.TKEPreconditionNotFound'

# The specified tag is not found.
RESOURCENOTFOUND_TAGSNOTFOUND = 'ResourceNotFound.TagsNotFound'

# Resources are unavailable.
RESOURCEUNAVAILABLE_NOTSUPPORTNODETYPE = 'ResourceUnavailable.NotSupportNodeType'

# Resources are unavailable.
RESOURCEUNAVAILABLE_NOTSUPPORTRESOURCETYPE = 'ResourceUnavailable.NotSupportResourceType'

# Duplicate resource specifications.
RESOURCEUNAVAILABLE_REPEATSPEC = 'ResourceUnavailable.RepeatSpec'

# The current resource specifications do not have the default specifications.
RESOURCEUNAVAILABLE_RESOURCESPECNOTDEFAULTSPEC = 'ResourceUnavailable.ResourceSpecNotDefaultSpec'

# The resource specifications do not exist.
RESOURCEUNAVAILABLE_RESOURCESPECNOTEXIST = 'ResourceUnavailable.ResourceSpecNotExist'

# Resources have been sold out.
RESOURCESSOLDOUT = 'ResourcesSoldOut'

# CBS resources have been sold out.
RESOURCESSOLDOUT_CBSSOLDOUT = 'ResourcesSoldOut.CbsSoldOut'

# CVMs have been sold out.
RESOURCESSOLDOUT_CVMSOLDOUT = 'ResourcesSoldOut.CvmSoldOut'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# APPID mismatch.
UNAUTHORIZEDOPERATION_APPIDMISMATCHED = 'UnauthorizedOperation.AppIdMismatched'

# No permission to verify account operations.
UNAUTHORIZEDOPERATION_CHECKCAMAUTH = 'UnauthorizedOperation.CheckCamAuth'

# Unknown parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'

# The operation is not supported.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# This feature is supported by the allowlist.
UNSUPPORTEDOPERATION_NOTINWHITELIST = 'UnsupportedOperation.NotInWhiteList'

# This service does not support this operation.
UNSUPPORTEDOPERATION_SERVICENOTSUPPORT = 'UnsupportedOperation.ServiceNotSupport'
