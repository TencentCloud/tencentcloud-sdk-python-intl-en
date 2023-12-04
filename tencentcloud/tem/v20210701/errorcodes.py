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


# Request timed out
FAILEDOPERATION_ACTIONREADTIMEOUT = 'FailedOperation.ActionReadTimeout'

# Failed to create the service.
FAILEDOPERATION_CREATESERVICEERROR = 'FailedOperation.CreateServiceError'

# The server is busy. Retry later.
FAILEDOPERATION_DEFAULTINTERNALERROR = 'FailedOperation.DefaultInternalError'

# Failed to delete the application
FAILEDOPERATION_DELETESERVICEERROR = 'FailedOperation.DeleteServiceError'

# Failed to query the ingress list
FAILEDOPERATION_DESCRIBEINGRESSLISTERROR = 'FailedOperation.DescribeIngressListError'

# Failed to query the instance information
FAILEDOPERATION_DESCRIBERUNPODLISTERROR = 'FailedOperation.DescribeRunPodListError'

# Failed to query the service.
FAILEDOPERATION_DESCRIBESERVICEERROR = 'FailedOperation.DescribeServiceError'

# Failed to query the service list
FAILEDOPERATION_DESCRIBESERVICELISTERROR = 'FailedOperation.DescribeServiceListError'

# Failed to update the ingress
FAILEDOPERATION_UPDATEINGRESSERROR = 'FailedOperation.UpdateIngressError'

# Request timed out
INTERNALERROR_ACTIONREADTIMEOUT = 'InternalError.ActionReadTimeout'

# Exception occurs while adding the subnet/virtual node
INTERNALERROR_ADDNEWNODEERROR = 'InternalError.AddNewNodeError'

# Failed to create the APM resource
INTERNALERROR_CREATEAPMRESOURCEERROR = 'InternalError.CreateApmResourceError'

# Failed to create the configuration.
INTERNALERROR_CREATECONFIGDATAERROR = 'InternalError.CreateConfigDataError'

# Failed to create the underlayer cluster
INTERNALERROR_CREATEEKSCLUSTERERROR = 'InternalError.CreateEksClusterError'

# Error while creating the LogConfig.
INTERNALERROR_CREATELOGCONFIGERROR = 'InternalError.CreateLogConfigError'

# Failed to create the service.
INTERNALERROR_CREATESERVICEERROR = 'InternalError.CreateServiceError'

# The server is busy. Retry later.
INTERNALERROR_DEFAULTINTERNALERROR = 'InternalError.DefaultInternalError'

# Failed to delete the ingress
INTERNALERROR_DELETEINGRESSERROR = 'InternalError.DeleteIngressError'

# Error while deleting the LogConfig.
INTERNALERROR_DELETELOGCONFIGERROR = 'InternalError.DeleteLogConfigError'

# Failed to delete the application
INTERNALERROR_DELETESERVICEERROR = 'InternalError.DeleteServiceError'

# Failed to invoke the version deployment
INTERNALERROR_DEPLOYVERSIONERROR = 'InternalError.DeployVersionError'

# Failed to query the configuration details.
INTERNALERROR_DESCRIBECONFIGDATAERROR = 'InternalError.DescribeConfigDataError'

# Failed to query the configuration list.
INTERNALERROR_DESCRIBECONFIGDATALISTERROR = 'InternalError.DescribeConfigDataListError'

# Failed to query the ingress.
INTERNALERROR_DESCRIBEINGRESSERROR = 'InternalError.DescribeIngressError'

# Failed to query the ingress list
INTERNALERROR_DESCRIBEINGRESSLISTERROR = 'InternalError.DescribeIngressListError'

# Error while querying the LogConfig.
INTERNALERROR_DESCRIBELOGCONFIGERROR = 'InternalError.DescribeLogConfigError'

# Error while querying the LogConfig list.
INTERNALERROR_DESCRIBELOGCONFIGLISTERROR = 'InternalError.DescribeLogConfigListError'

# Failed to query the instance information
INTERNALERROR_DESCRIBERUNPODLISTERROR = 'InternalError.DescribeRunPodListError'

# Failed to query the service.
INTERNALERROR_DESCRIBESERVICEERROR = 'InternalError.DescribeServiceError'

# Failed to query the list of ingress associated with the service.
INTERNALERROR_DESCRIBESERVICEINGRESSERROR = 'InternalError.DescribeServiceIngressError'

# Failed to query the service list
INTERNALERROR_DESCRIBESERVICELISTERROR = 'InternalError.DescribeServiceListError'

# Failed to modify the configuration.
INTERNALERROR_MODIFYCONFIGDATAERROR = 'InternalError.ModifyConfigDataError'

# Error while modifying the LogConfig.
INTERNALERROR_MODIFYLOGCONFIGERROR = 'InternalError.ModifyLogConfigError'

# Failed to restart
INTERNALERROR_RESTARTAPPLICATIONERROR = 'InternalError.RestartApplicationError'

# Failed to stop an application
INTERNALERROR_STOPAPPLICATIONERROR = 'InternalError.StopApplicationError'

# Exception while calling the tag-related APIs.
INTERNALERROR_TAGINTERFACEERROR = 'InternalError.TagInterfaceError'

# Failed to update the ingress
INTERNALERROR_UPDATEINGRESSERROR = 'InternalError.UpdateIngressError'

# Reached the upper limit of access policies for this application.
INVALIDPARAMETER_APPLICATIONACCESSSERVICEREACHMAXIMUM = 'InvalidParameter.ApplicationAccessServiceReachMaximum'

# For an LB application, TCP and UDP cannot be both supported..
INVALIDPARAMETER_LBSERVICECANNOTSUPPORTTCPUDPSAMETIME = 'InvalidParameter.LBServiceCannotSupportTcpUdpSameTime'

# The PortMapping rule is required.
INVALIDPARAMETER_MUSTPROVIDEPORTMAPPINGRULES = 'InvalidParameter.MustProvidePortMappingRules'

# The application name is invalid.
INVALIDPARAMETER_SERVICENAMENOTVALID = 'InvalidParameter.ServiceNameNotValid'

# The suffix of the application name is not allowed.
INVALIDPARAMETER_SERVICEUSERESERVESUFFIX = 'InvalidParameter.ServiceUseReserveSuffix'

# Reached the upper limit of PortMapping rules. 
INVALIDPARAMETER_TOOMANYPORTMAPPINGRULES = 'InvalidParameter.TooManyPortMappingRules'

# Not authorized or role not configured
INVALIDPARAMETER_UNAUTHORIZEDORMISSINGROLE = 'InvalidParameter.UnauthorizedOrMissingRole'

# Auto-creation failed because the VPC upper limit is reached.
INVALIDPARAMETER_VPCOVERQUOTA = 'InvalidParameter.VpcOverQuota'

# The APM is not bound with the current environment.
INVALIDPARAMETERVALUE_APMNOTBIND = 'InvalidParameterValue.ApmNotBind'

# Reached the upper limit of access policies for this application.
INVALIDPARAMETERVALUE_APPLICATIONACCESSSERVICEREACHMAXIMUM = 'InvalidParameterValue.ApplicationAccessServiceReachMaximum'

# The access policy name already exists.
INVALIDPARAMETERVALUE_APPLICATIONSERVICEALREADYEXIST = 'InvalidParameterValue.ApplicationServiceAlreadyExist'

# The access policy does not exist.
INVALIDPARAMETERVALUE_APPLICATIONSERVICENOTFOUND = 'InvalidParameterValue.ApplicationServiceNotFound'

# Please enable at least one type of scaling rules.
INVALIDPARAMETERVALUE_ATLEASTONESCALERRULESHOULDBEAPPLIED = 'InvalidParameterValue.AtLeastOneScalerRuleShouldBeApplied'

# Only one auto scaler can be specified.
INVALIDPARAMETERVALUE_AUTOSCALERLARGERTHANONE = 'InvalidParameterValue.AutoScalerLargerThanOne'

# 
INVALIDPARAMETERVALUE_AUTOSCALERNAMEINVALID = 'InvalidParameterValue.AutoScalerNameInvalid'

# The access mode of other applications cannot be overwritten. 
INVALIDPARAMETERVALUE_CANNOTOVERWRITEOTHERAPPLICATIONSERVICE = 'InvalidParameterValue.CannotOverWriteOtherApplicationService'

# Full update and single-entry update cannot be specified at the same time.
INVALIDPARAMETERVALUE_CANNOTUPDATESERVICEBYBOTHMETHODS = 'InvalidParameterValue.CannotUpdateServiceByBothMethods'

# This configuration already exists.
INVALIDPARAMETERVALUE_CONFIGDATAALREADYEXIST = 'InvalidParameterValue.ConfigDataAlreadyExist'

# The configuration is incorrect.
INVALIDPARAMETERVALUE_CONFIGDATAINVALID = 'InvalidParameterValue.ConfigDataInvalid'

# 
INVALIDPARAMETERVALUE_CREATENAMESPACEUNSUPPORTREGIONERROR = 'InvalidParameterValue.CreateNamespaceUnsupportRegionError'

# The specified desired capacity of the scheduled action is incorrect.
INVALIDPARAMETERVALUE_CRONHPAREPLICASINVALID = 'InvalidParameterValue.CronHpaReplicasInvalid'

# Reached the upper limit of environment created every day
INVALIDPARAMETERVALUE_DAILYCREATENAMESPACEREACHMAXIMUM = 'InvalidParameterValue.DailyCreateNamespaceReachMaximum'

# There is an auto scaler in used. Please disable it first.
INVALIDPARAMETERVALUE_DISABLESCALERBEFOREDELETE = 'InvalidParameterValue.DisableScalerBeforeDelete'

# The environment name cannot be changed.
INVALIDPARAMETERVALUE_ENVIRONMENTNAMEIMMUTABLE = 'InvalidParameterValue.EnvironmentNameImmutable'

# The desired capacity of scaling is incorrect.
INVALIDPARAMETERVALUE_HPAMETRICSINVALID = 'InvalidParameterValue.HpaMetricsInvalid'

# The minimum or maximum number for auto scaling is invalid.
INVALIDPARAMETERVALUE_HPAMINMAXINVALID = 'InvalidParameterValue.HpaMinMaxInvalid'

# Invalid elastic scaling threshold
INVALIDPARAMETERVALUE_HPATHRESHOLDINVALID = 'InvalidParameterValue.HpaThresholdInvalid'

# To enable access configuration redirection, you need to enable HTTPS.
INVALIDPARAMETERVALUE_INGRESSREWRITEREQUIREDHTTPSENABLE = 'InvalidParameterValue.IngressRewriteRequiredHttpsEnable'

# Invalid scheduled period
INVALIDPARAMETERVALUE_INVALIDCRONSCALERPERIOD = 'InvalidParameterValue.InvalidCronScalerPeriod'

# The version number is invalid.
INVALIDPARAMETERVALUE_INVALIDDEPLOYVERSION = 'InvalidParameterValue.InvalidDeployVersion'

# The access type is not supported.
INVALIDPARAMETERVALUE_INVALIDEKSSERVICETYPE = 'InvalidParameterValue.InvalidEksServiceType'

# Invalid environment parameter name. It must be a combination of [a-z], [A-Z], [0-9] and [._-]. It cannot start with a digit.
INVALIDPARAMETERVALUE_INVALIDENVNAME = 'InvalidParameterValue.InvalidEnvName'

# The length of environment variable cannot exceed 1,000.
INVALIDPARAMETERVALUE_INVALIDENVVALUE = 'InvalidParameterValue.InvalidEnvValue'

# Invalid mounting path. It cannot be /app.
INVALIDPARAMETERVALUE_INVALIDMOUNTPATH = 'InvalidParameterValue.InvalidMountPath'

# Invalid application name
INVALIDPARAMETERVALUE_INVALIDSERVICENAME = 'InvalidParameterValue.InvalidServiceName'

# Unable to identify the tenant information
INVALIDPARAMETERVALUE_INVALIDTENANTINFO = 'InvalidParameterValue.InvalidTenantInfo'

# The JDK version is required.
INVALIDPARAMETERVALUE_JDKVERSIONREQUIRED = 'InvalidParameterValue.JdkVersionRequired'

# The LogConfig already exists.
INVALIDPARAMETERVALUE_LOGCONFIGALREADYEXIST = 'InvalidParameterValue.LogConfigAlreadyExist'

# The PortMapping rule is required.
INVALIDPARAMETERVALUE_MUSTPROVIDEPORTMAPPINGRULES = 'InvalidParameterValue.MustProvidePortMappingRules'

# The environment already exists.
INVALIDPARAMETERVALUE_NAMESPACEDUPLICATEERROR = 'InvalidParameterValue.NamespaceDuplicateError'

# The namespace does not belong to the current account.
INVALIDPARAMETERVALUE_NAMESPACENOTBELONGTOAPPID = 'InvalidParameterValue.NamespaceNotBelongToAppid'

# The environment does not exist.
INVALIDPARAMETERVALUE_NAMESPACENOTFOUND = 'InvalidParameterValue.NamespaceNotFound'

# Failed to create the environment. The upper limit of environment is reached.
INVALIDPARAMETERVALUE_NAMESPACEREACHMAXIMUM = 'InvalidParameterValue.NamespaceReachMaximum'

# Failed to create the environment. The upper limit of environment is reached.
INVALIDPARAMETERVALUE_NAMESPACERESOURCEREACHMAXIMUM = 'InvalidParameterValue.NamespaceResourceReachMaximum'

# The operating system is not supported.
INVALIDPARAMETERVALUE_OSNOTSUPPORT = 'InvalidParameterValue.OsNotSupport'

# The application port mapping already exists.
INVALIDPARAMETERVALUE_PORTDUPLICATEERROR = 'InvalidParameterValue.PortDuplicateError'

# The application port is a reserved port.
INVALIDPARAMETERVALUE_PORTISRESERVED = 'InvalidParameterValue.PortIsReserved'

# Invalid post start
INVALIDPARAMETERVALUE_POSTSTARTNOTVALID = 'InvalidParameterValue.PostStartNotValid'

# 
INVALIDPARAMETERVALUE_PRESTOPNOTVALID = 'InvalidParameterValue.PreStopNotValid'

# Public image parameter error
INVALIDPARAMETERVALUE_PUBLICREPOTYPEPARAMETERERROR = 'InvalidParameterValue.PublicRepoTypeParameterError'

# The registry is not associated with the current environment.
INVALIDPARAMETERVALUE_REGISTRYNOTBIND = 'InvalidParameterValue.RegistryNotBind'

# The auto scaler name already exists.
INVALIDPARAMETERVALUE_SCALERNAMEDUPLICATED = 'InvalidParameterValue.ScalerNameDuplicated'

# There are running pods in this application.
INVALIDPARAMETERVALUE_SERVICEFOUNDRUNNINGVERSION = 'InvalidParameterValue.ServiceFoundRunningVersion'

# The application name must be in lowercase.
INVALIDPARAMETERVALUE_SERVICELOWERCASE = 'InvalidParameterValue.ServiceLowerCase'

# This application name already exists.
INVALIDPARAMETERVALUE_SERVICENAMEDUPLICATEERROR = 'InvalidParameterValue.ServiceNameDuplicateError'

# You are not the owner of this application.
INVALIDPARAMETERVALUE_SERVICENOTBELONGTOAPPID = 'InvalidParameterValue.ServiceNotBelongToAppid'

# Failed to create the instance. The upper limit is reached.
INVALIDPARAMETERVALUE_SERVICEPODREACHMAXIMUM = 'InvalidParameterValue.ServicePodReachMaximum'

# Failed to create the application. The upper limit is reached.
INVALIDPARAMETERVALUE_SERVICEREACHMAXIMUM = 'InvalidParameterValue.ServiceReachMaximum'

# The suffix of the application name is not allowed.
INVALIDPARAMETERVALUE_SERVICEUSERESERVESUFFIX = 'InvalidParameterValue.ServiceUseReserveSuffix'

# The TCR Enterprise instance name is invalid.
INVALIDPARAMETERVALUE_TCRENTINSTANCENAMENOTVALID = 'InvalidParameterValue.TcrEntInstanceNameNotValid'

# The TEM ID is incorrect.
INVALIDPARAMETERVALUE_TEMIDINVALID = 'InvalidParameterValue.TemIdInvalid'

# Linkage tracing is not available for non-JAVA applications.
INVALIDPARAMETERVALUE_TRAITSTRACINGNOTSUPPORTED = 'InvalidParameterValue.TraitsTracingNotSupported'

# The value of `version` cannot exceed 128 characters.
INVALIDPARAMETERVALUE_VERSIONLENGTHLIMIT = 'InvalidParameterValue.VersionLengthLimit'

# The version must be in lower case.
INVALIDPARAMETERVALUE_VERSIONLOWERCASE = 'InvalidParameterValue.VersionLowerCase'

# There is still traffic routed to this version.
INVALIDPARAMETERVALUE_VERSIONROUTERATENOTZERO = 'InvalidParameterValue.VersionRouteRateNotZero'

# Invalid VPC. It should be the same as the environment VPC.
INVALIDPARAMETERVALUE_VPCINVALID = 'InvalidParameterValue.VpcInvalid'

# The scaling rule name cannot be empty
MISSINGPARAMETER_AUTOSCALERNAMENULL = 'MissingParameter.AutoScalerNameNull'

# The deployment method is required.
MISSINGPARAMETER_DEPLOYMODENULL = 'MissingParameter.DeployModeNull'

# The deployment version cannot be empty.
MISSINGPARAMETER_DEPLOYVERSIONNULL = 'MissingParameter.DeployVersionNull'

# The environment name is required.
MISSINGPARAMETER_ENVIRONMENTNAMENULL = 'MissingParameter.EnvironmentNameNull'

# The image repository is required.
MISSINGPARAMETER_IMGREPONULL = 'MissingParameter.ImgRepoNull'

# The `logset` and `topic` are required.
MISSINGPARAMETER_LOGSETORTOPICNULL = 'MissingParameter.LogsetOrTopicNull'

# The minimum and maximum number for auto scaling are required.
MISSINGPARAMETER_MINMAXNUMNULL = 'MissingParameter.MinMaxNumNull'

# The environment ID can not be left empty.
MISSINGPARAMETER_NAMESPACEIDNULL = 'MissingParameter.NamespaceIdNull'

# The package name cannot be left empty.
MISSINGPARAMETER_PKGNAMENULL = 'MissingParameter.PkgNameNull'

# 
MISSINGPARAMETER_REPOSERVERNULL = 'MissingParameter.RepoServerNull'

# The scaling rule ID is missing.
MISSINGPARAMETER_SCALERIDNULL = 'MissingParameter.ScalerIdNull'

# The service ID cannot be empty.
MISSINGPARAMETER_SERVICEIDNULL = 'MissingParameter.ServiceIdNull'

# The image repository is not ready.
MISSINGPARAMETER_SVCREPONOTREADY = 'MissingParameter.SvcRepoNotReady'

# The TCR Enterprise instance name is required.
MISSINGPARAMETER_TCRENTINSTANCENAMENULL = 'MissingParameter.TcrEntInstanceNameNull'

# For intra-VPC acess, the subnet ID is required.
MISSINGPARAMETER_VPCSERVICESUBNETNULL = 'MissingParameter.VpcServiceSubnetNull'

# Insufficient account balance.
OPERATIONDENIED_BALANCENOTENOUGH = 'OperationDenied.BalanceNotEnough'

# There’re overdue payments under your account. Please make the payment first.
OPERATIONDENIED_RESOURCEISOLATED = 'OperationDenied.ResourceIsolated'

# The environment is locked.
RESOURCEINUSE_ENVIRONMENTALREADYLOCKED = 'ResourceInUse.EnvironmentAlreadyLocked'

# The specified resource is occupied by another operation. Please try again later.
RESOURCEINUSE_RESOURCEALREADYLOCKED = 'ResourceInUse.ResourceAlreadyLocked'

# This resource is already bound.
RESOURCEINUSE_RESOURCEALREADYUSED = 'ResourceInUse.ResourceAlreadyUsed'

# The application is being deployed.
RESOURCEINUSE_SERVICEDEPLOYING = 'ResourceInUse.ServiceDeploying'

# Configuration does no exist
RESOURCENOTFOUND_CONFIGDATANOTFOUND = 'ResourceNotFound.ConfigDataNotFound'

# This API is not available.
RESOURCENOTFOUND_INTERFACENOTFOUND = 'ResourceNotFound.InterfaceNotFound'

# The log configuration does not exist.
RESOURCENOTFOUND_LOGCONFIGNOTFOUND = 'ResourceNotFound.LogConfigNotFound'

# The target microservice is offline.
RESOURCENOTFOUND_MICROSERVICEOFFLINE = 'ResourceNotFound.MicroserviceOffline'

# The environment does not exist.
RESOURCENOTFOUND_NAMESPACENOTFOUND = 'ResourceNotFound.NamespaceNotFound'

# The application is not found.
RESOURCENOTFOUND_SERVICENOTFOUND = 'ResourceNotFound.ServiceNotFound'

# No running pod is found.
RESOURCENOTFOUND_SERVICERUNNINGVERSIONNOTFOUND = 'ResourceNotFound.ServiceRunningVersionNotFound'

# The environment corresponding to this version is not found.
RESOURCENOTFOUND_VERSIONNAMESPACENOTFOUND = 'ResourceNotFound.VersionNamespaceNotFound'

# The environment corresponding to this version is not found.
RESOURCENOTFOUND_VERSIONSERVICENOTFOUND = 'ResourceNotFound.VersionServiceNotFound'

# Failed to delete: The application is used by other resources. 
RESOURCEUNAVAILABLE_APPLICATIONNOTDELETABLE = 'ResourceUnavailable.ApplicationNotDeletable'

# The application is stopped.
RESOURCEUNAVAILABLE_APPLICATIONSTOPPED = 'ResourceUnavailable.ApplicationStopped'

# Waiting for the installation of addon
RESOURCEUNAVAILABLE_WAITFORKRUISE = 'ResourceUnavailable.WaitForKruise'

# TKE does not have the permission to access CLS. Please assign the permission first.
UNAUTHORIZEDOPERATION_MISSINGEKSLOGROLE = 'UnauthorizedOperation.MissingEksLogRole'

# Not authorized
UNAUTHORIZEDOPERATION_UNAUTHORIZEDOPERATION = 'UnauthorizedOperation.UnauthorizedOperation'

# ACTION not supported
UNSUPPORTEDOPERATION_UNSUPPORTACTION = 'UnsupportedOperation.UnsupportAction'
