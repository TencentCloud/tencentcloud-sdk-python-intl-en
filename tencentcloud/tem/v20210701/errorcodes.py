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

# Failed to create the APM resource
INTERNALERROR_CREATEAPMRESOURCEERROR = 'InternalError.CreateApmResourceError'

# Failed to create the underlayer cluster
INTERNALERROR_CREATEEKSCLUSTERERROR = 'InternalError.CreateEksClusterError'

# Failed to create the service.
INTERNALERROR_CREATESERVICEERROR = 'InternalError.CreateServiceError'

# The server is busy. Retry later.
INTERNALERROR_DEFAULTINTERNALERROR = 'InternalError.DefaultInternalError'

# Failed to delete the application
INTERNALERROR_DELETESERVICEERROR = 'InternalError.DeleteServiceError'

# Failed to invoke the version deployment
INTERNALERROR_DEPLOYVERSIONERROR = 'InternalError.DeployVersionError'

# Failed to query the instance information
INTERNALERROR_DESCRIBERUNPODLISTERROR = 'InternalError.DescribeRunPodListError'

# Failed to restart
INTERNALERROR_RESTARTAPPLICATIONERROR = 'InternalError.RestartApplicationError'

# Failed to update the ingress
INTERNALERROR_UPDATEINGRESSERROR = 'InternalError.UpdateIngressError'

# The version number is invalid.
INVALIDPARAMETERVALUE_INVALIDDEPLOYVERSION = 'InvalidParameterValue.InvalidDeployVersion'

# The environment already exists.
INVALIDPARAMETERVALUE_NAMESPACEDUPLICATEERROR = 'InvalidParameterValue.NamespaceDuplicateError'

# Failed to create the environment. The upper limit of environment is reached.
INVALIDPARAMETERVALUE_NAMESPACEREACHMAXIMUM = 'InvalidParameterValue.NamespaceReachMaximum'

# Failed to create the environment. The upper limit of environment is reached.
INVALIDPARAMETERVALUE_NAMESPACERESOURCEREACHMAXIMUM = 'InvalidParameterValue.NamespaceResourceReachMaximum'

# There are running pods in this application.
INVALIDPARAMETERVALUE_SERVICEFOUNDRUNNINGVERSION = 'InvalidParameterValue.ServiceFoundRunningVersion'

# This application name already exists.
INVALIDPARAMETERVALUE_SERVICENAMEDUPLICATEERROR = 'InvalidParameterValue.ServiceNameDuplicateError'

# Linkage tracing is not available for non-JAVA applications.
INVALIDPARAMETERVALUE_TRAITSTRACINGNOTSUPPORTED = 'InvalidParameterValue.TraitsTracingNotSupported'

# The version must be in lower case.
INVALIDPARAMETERVALUE_VERSIONLOWERCASE = 'InvalidParameterValue.VersionLowerCase'

# There is still traffic routed to this version.
INVALIDPARAMETERVALUE_VERSIONROUTERATENOTZERO = 'InvalidParameterValue.VersionRouteRateNotZero'

# 
MISSINGPARAMETER_DEPLOYVERSIONNULL = 'MissingParameter.DeployVersionNull'

# The environment ID can not be left empty.
MISSINGPARAMETER_NAMESPACEIDNULL = 'MissingParameter.NamespaceIdNull'

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
