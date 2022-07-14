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
INTERNALERROR_ACTIONREADTIMEOUT = 'InternalError.ActionReadTimeout'

# Exception occurs while adding the subnet/virtual node
INTERNALERROR_ADDNEWNODEERROR = 'InternalError.AddNewNodeError'

# Failed to create the APM resource
INTERNALERROR_CREATEAPMRESOURCEERROR = 'InternalError.CreateApmResourceError'

# Failed to create the underlayer cluster
INTERNALERROR_CREATEEKSCLUSTERERROR = 'InternalError.CreateEksClusterError'

# Failed to create the service.
INTERNALERROR_CREATESERVICEERROR = 'InternalError.CreateServiceError'

# The server is busy. Retry later.
INTERNALERROR_DEFAULTINTERNALERROR = 'InternalError.DefaultInternalError'

# Failed to delete the ingress
INTERNALERROR_DELETEINGRESSERROR = 'InternalError.DeleteIngressError'

# Failed to delete the application
INTERNALERROR_DELETESERVICEERROR = 'InternalError.DeleteServiceError'

# Failed to invoke the version deployment
INTERNALERROR_DEPLOYVERSIONERROR = 'InternalError.DeployVersionError'

# Failed to query the instance information
INTERNALERROR_DESCRIBERUNPODLISTERROR = 'InternalError.DescribeRunPodListError'

# Failed to query the list of ingress associated with the service.
INTERNALERROR_DESCRIBESERVICEINGRESSERROR = 'InternalError.DescribeServiceIngressError'

# Failed to query the service list
INTERNALERROR_DESCRIBESERVICELISTERROR = 'InternalError.DescribeServiceListError'

# Failed to restart
INTERNALERROR_RESTARTAPPLICATIONERROR = 'InternalError.RestartApplicationError'

# Failed to stop an application
INTERNALERROR_STOPAPPLICATIONERROR = 'InternalError.StopApplicationError'

# Failed to update the ingress
INTERNALERROR_UPDATEINGRESSERROR = 'InternalError.UpdateIngressError'

# Only one auto scaler can be specified.
INVALIDPARAMETERVALUE_AUTOSCALERLARGERTHANONE = 'InvalidParameterValue.AutoScalerLargerThanOne'

# The version number is invalid.
INVALIDPARAMETERVALUE_INVALIDDEPLOYVERSION = 'InvalidParameterValue.InvalidDeployVersion'

# 
INVALIDPARAMETERVALUE_INVALIDSERVICENAME = 'InvalidParameterValue.InvalidServiceName'

# The environment already exists.
INVALIDPARAMETERVALUE_NAMESPACEDUPLICATEERROR = 'InvalidParameterValue.NamespaceDuplicateError'

# The namespace does not belong to the current account.
INVALIDPARAMETERVALUE_NAMESPACENOTBELONGTOAPPID = 'InvalidParameterValue.NamespaceNotBelongToAppid'

# Failed to create the environment. The upper limit of environment is reached.
INVALIDPARAMETERVALUE_NAMESPACEREACHMAXIMUM = 'InvalidParameterValue.NamespaceReachMaximum'

# Failed to create the environment. The upper limit of environment is reached.
INVALIDPARAMETERVALUE_NAMESPACERESOURCEREACHMAXIMUM = 'InvalidParameterValue.NamespaceResourceReachMaximum'

# 
INVALIDPARAMETERVALUE_PUBLICREPOTYPEPARAMETERERROR = 'InvalidParameterValue.PublicRepoTypeParameterError'

# There are running pods in this application.
INVALIDPARAMETERVALUE_SERVICEFOUNDRUNNINGVERSION = 'InvalidParameterValue.ServiceFoundRunningVersion'

# 
INVALIDPARAMETERVALUE_SERVICELOWERCASE = 'InvalidParameterValue.ServiceLowerCase'

# This application name already exists.
INVALIDPARAMETERVALUE_SERVICENAMEDUPLICATEERROR = 'InvalidParameterValue.ServiceNameDuplicateError'

# Failed to create the instance. The upper limit is reached.
INVALIDPARAMETERVALUE_SERVICEPODREACHMAXIMUM = 'InvalidParameterValue.ServicePodReachMaximum'

# 
INVALIDPARAMETERVALUE_SERVICEREACHMAXIMUM = 'InvalidParameterValue.ServiceReachMaximum'

# Linkage tracing is not available for non-JAVA applications.
INVALIDPARAMETERVALUE_TRAITSTRACINGNOTSUPPORTED = 'InvalidParameterValue.TraitsTracingNotSupported'

# The version must be in lower case.
INVALIDPARAMETERVALUE_VERSIONLOWERCASE = 'InvalidParameterValue.VersionLowerCase'

# There is still traffic routed to this version.
INVALIDPARAMETERVALUE_VERSIONROUTERATENOTZERO = 'InvalidParameterValue.VersionRouteRateNotZero'

# The deployment version cannot be empty.
MISSINGPARAMETER_DEPLOYVERSIONNULL = 'MissingParameter.DeployVersionNull'

# The environment ID can not be left empty.
MISSINGPARAMETER_NAMESPACEIDNULL = 'MissingParameter.NamespaceIdNull'

# The package name cannot be left empty.
MISSINGPARAMETER_PKGNAMENULL = 'MissingParameter.PkgNameNull'

# The service ID cannot be empty.
MISSINGPARAMETER_SERVICEIDNULL = 'MissingParameter.ServiceIdNull'

# The image repository is not ready.
MISSINGPARAMETER_SVCREPONOTREADY = 'MissingParameter.SvcRepoNotReady'

# 
RESOURCEINUSE_RESOURCEALREADYLOCKED = 'ResourceInUse.ResourceAlreadyLocked'

# This resource is already bound.
RESOURCEINUSE_RESOURCEALREADYUSED = 'ResourceInUse.ResourceAlreadyUsed'

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

# Waiting for the installation of addon
RESOURCEUNAVAILABLE_WAITFORKRUISE = 'ResourceUnavailable.WaitForKruise'

# Unauthorized
UNAUTHORIZEDOPERATION_UNAUTHORIZEDOPERATION = 'UnauthorizedOperation.UnauthorizedOperation'

# 
UNSUPPORTEDOPERATION_UNSUPPORTACTION = 'UnsupportedOperation.UnsupportAction'
