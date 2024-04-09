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


# Error with CAM signature/authentication.
AUTHFAILURE = 'AuthFailure'

# `DryRun` Operation. It means that the request would have succeeded, but the `DryRun` parameter was used.
DRYRUNOPERATION = 'DryRunOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# The custom key already exists.
FAILEDOPERATION_ACCESSKEYEXIST = 'FailedOperation.AccessKeyExist'

# This API has been bound with a usage plan.
FAILEDOPERATION_APIBINDENVIRONMEN = 'FailedOperation.ApiBindEnvironmen'

# The APIs have already been bound to a usage plan. Please unbind them and try again.
FAILEDOPERATION_APIBINDENVIRONMENT = 'FailedOperation.ApiBindEnvironment'

# API error.
FAILEDOPERATION_APIERROR = 'FailedOperation.ApiError'

# The API is being manipulated. Please try again later.
FAILEDOPERATION_APIINOPERATION = 'FailedOperation.ApiInOperation'

# 
FAILEDOPERATION_BACKENDDOMAINERROR = 'FailedOperation.BackendDomainError'

# 
FAILEDOPERATION_CAMEXCEPTION = 'FailedOperation.CamException'

# An error occurred while binding a certificate.
FAILEDOPERATION_CERTIFICATEIDBINDERROR = 'FailedOperation.CertificateIdBindError'

# The certificate is an enterprise certificate and waiting to be submitted.
FAILEDOPERATION_CERTIFICATEIDENTERPRISEWAITSUBMIT = 'FailedOperation.CertificateIdEnterpriseWaitSubmit'

# The certificate does not exist or you do not have permission to view it. Please upload a valid certificate in the SSL Certificates Service Console.
FAILEDOPERATION_CERTIFICATEIDERROR = 'FailedOperation.CertificateIdError'

# The certificate has expired. Please upload a valid one.
FAILEDOPERATION_CERTIFICATEIDEXPIRED = 'FailedOperation.CertificateIdExpired'

# The certificate information is empty. Please submit a ticket for assistance.
FAILEDOPERATION_CERTIFICATEIDINFOERROR = 'FailedOperation.CertificateIdInfoError'

# The certificate is under review. Please upload a valid one.
FAILEDOPERATION_CERTIFICATEIDUNDERVERIFY = 'FailedOperation.CertificateIdUnderVerify'

# The certificate is in an unknown status. Please submit a ticket to check its specific status.
FAILEDOPERATION_CERTIFICATEIDUNKNOWNERROR = 'FailedOperation.CertificateIdUnknownError'

# The certificate has been rejected. Please upload a valid one.
FAILEDOPERATION_CERTIFICATEIDVERIFYFAIL = 'FailedOperation.CertificateIdVerifyFail'

# The Apis certificate is empty. Please upload a certificate.
FAILEDOPERATION_CERTIFICATEISNULL = 'FailedOperation.CertificateIsNull'

# API document operation failed.
FAILEDOPERATION_CODINGERROR = 'FailedOperation.CodingError'

# The Apis environment configuration is incorrect.
FAILEDOPERATION_DEFINEMAPPINGENVIRONMENTERROR = 'FailedOperation.DefineMappingEnvironmentError'

# The Apis custom path mapping cannot be empty.
FAILEDOPERATION_DEFINEMAPPINGNOTNULL = 'FailedOperation.DefineMappingNotNull'

# The Apis parameters are repeated.
FAILEDOPERATION_DEFINEMAPPINGPARAMREPEAT = 'FailedOperation.DefineMappingParamRepeat'

# The Apis custom path configuration is incorrect.
FAILEDOPERATION_DEFINEMAPPINGPATHERROR = 'FailedOperation.DefineMappingPathError'

# An error occurred while deleting the custom domain name.
FAILEDOPERATION_DELETEPATHMAPPINGSETERROR = 'FailedOperation.DeletePathMappingSetError'

# The custom domain name of the service is incorrect.
FAILEDOPERATION_DESCRIBESERVICESUBDOMAINSERROR = 'FailedOperation.DescribeServiceSubDomainsError'

# The domain name has been bound to another service.
FAILEDOPERATION_DOMAINALREADYBINDOTHERSERVICE = 'FailedOperation.DomainAlreadyBindOtherService'

# The domain name has already been bound to this service.
FAILEDOPERATION_DOMAINALREADYBINDSERVICE = 'FailedOperation.DomainAlreadyBindService'

# Unable to connect: the current domain name is not compliant. 
FAILEDOPERATION_DOMAININBLACKLIST = 'FailedOperation.DomainInBlackList'

# The domain name does not have an ICP filing through Tencent Cloud. Please get the ICP filing before binding the domain name.
FAILEDOPERATION_DOMAINNEEDBEIAN = 'FailedOperation.DomainNeedBeian'

# Failed to unbind the custom domain name, as the domain name is not bound to the service.
FAILEDOPERATION_DOMAINNOTBINDSERVICE = 'FailedOperation.DomainNotBindService'

# The domain name is not configured with a CNAME record resolving to the default domain name, or the resolution has not taken effect yet.
FAILEDOPERATION_DOMAINRESOLVEERROR = 'FailedOperation.DomainResolveError'

# Error form EIAM
FAILEDOPERATION_EIAMERROR = 'FailedOperation.EIAMError'

# Failed to bind/unbind EventBridge.
FAILEDOPERATION_EBERROR = 'FailedOperation.EbError'

# The domain name format is incorrect.
FAILEDOPERATION_FORMATERROR = 'FailedOperation.FormatError'

# Failed to get the role. Please make sure that relevant API Gateway service APIs have been authorized.
FAILEDOPERATION_GETROLEERROR = 'FailedOperation.GetRoleError'

# The instance does not exist or is invalid.
FAILEDOPERATION_INSTANCENOTEXIST = 'FailedOperation.InstanceNotExist'

# 
FAILEDOPERATION_INVALIDINPUTJSON = 'FailedOperation.InvalidInputJSON'

# The Apis custom path conflicts with the default path.
FAILEDOPERATION_ISDEFAULTMAPPING = 'FailedOperation.IsDefaultMapping'

# The entered default second-level domain name is incorrect.
FAILEDOPERATION_NETSUBDOMAINERROR = 'FailedOperation.NetSubDomainError'

# Backend error
FAILEDOPERATION_OPERATEUPSTREAM = 'FailedOperation.OperateUpstream'

# An error occurred while setting the path mapping.
FAILEDOPERATION_PATHMAPPINGSETERROR = 'FailedOperation.PathMappingSetError'

# Failed to bind/unbind SCF trigger.
FAILEDOPERATION_SCFERROR = 'FailedOperation.ScfError'

# Service error.
FAILEDOPERATION_SERVICEERROR = 'FailedOperation.ServiceError'

# The service is in use. Please try again later.
FAILEDOPERATION_SERVICEINOPERATION = 'FailedOperation.ServiceInOperation'

# The service does not exist.
FAILEDOPERATION_SERVICENOTEXIST = 'FailedOperation.ServiceNotExist'

# The custom domain name already uses the default path mapping, so no custom path can be set.
FAILEDOPERATION_SETCUSTOMPATHMAPPINGERROR = 'FailedOperation.SetCustomPathMappingError'

# The custom domain name format is incorrect.
FAILEDOPERATION_SUBDOMAINFORMATERROR = 'FailedOperation.SubDomainFormatError'

# The tag was not bound to the specified service.
FAILEDOPERATION_TAGBINDSERVICEERROR = 'FailedOperation.TagBindServiceError'

# 
FAILEDOPERATION_TASKALREADYEXIST = 'FailedOperation.TaskAlreadyExist'

# The protocol type is incorrect.
FAILEDOPERATION_UNKNOWNPROTOCOLTYPEERROR = 'FailedOperation.UnknownProtocolTypeError'

# Internal error.
INTERNALERROR = 'InternalError'

# API Gateway internal request error. Please try again later. If the problem persists, please contact the smart customer service or submit a ticket.
INTERNALERROR_APIGWEXCEPTION = 'InternalError.ApigwException'

# 
INTERNALERROR_CAMEXCEPTION = 'InternalError.CamException'

# CAuth internal request error. Please try again later. If the problem persists, please submit a ticket.
INTERNALERROR_CAUTHEXCEPTION = 'InternalError.CauthException'

# CLB internal request error. Please try again. If the problem persists, please submit a ticket.
INTERNALERROR_CLBEXCEPTION = 'InternalError.ClbException'

# 
INTERNALERROR_DBEXCEPTION = 'InternalError.DbException'

# OSS internal request error. Please try again. If the problem persists, please contact the smart customer service or submit a ticket.
INTERNALERROR_OSSEXCEPTION = 'InternalError.OssException'

# 
INTERNALERROR_RETURNABLEEXCEPTION = 'InternalError.ReturnableException'

# SCF internal request error. Please try again. If the problem persists, please contact the smart customer service or submit a ticket.
INTERNALERROR_SCFEXCEPTION = 'InternalError.ScfException'

# TSF internal request error. Please try again. If the problem persists, please contact the smart customer service or submit a ticket.
INTERNALERROR_TSFEXCEPTION = 'InternalError.TsfException'

# VPC internal request error. Please try again. If the problem persists, please contact the smart customer service or submit a ticket.
INTERNALERROR_VPCEXCEPTION = 'InternalError.VpcException'

# Incorrect parameter.
INVALIDPARAMETER = 'InvalidParameter'

# You are using the basic edition and can not be bind a plug-in.
INVALIDPARAMETER_BASICSERVICENOTALLOWATTACHPLUGIN = 'InvalidParameter.BasicServiceNotAllowAttachPlugin'

# The plugin you want to bound conflicts with existing plugins.
INVALIDPARAMETER_DUPLICATEPLUGINCONFIG = 'InvalidParameter.DuplicatePluginConfig'

# Incorrect parameter format.
INVALIDPARAMETER_FORMATERROR = 'InvalidParameter.FormatError'

# The parameter value is incorrect.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Duplicate plugin parameter values. Please modify and try again.
INVALIDPARAMETERVALUE_DUPLICATEPLUGINCONFIG = 'InvalidParameterValue.DuplicatePluginConfig'

# Invalid backend IP address.
INVALIDPARAMETERVALUE_ILLEGALPROXYIP = 'InvalidParameterValue.IllegalProxyIp'

# Incorrect key.
INVALIDPARAMETERVALUE_INVALIDACCESSKEYIDS = 'InvalidParameterValue.InvalidAccessKeyIds'

# The API business type passed in must be `OAUTH`.
INVALIDPARAMETERVALUE_INVALIDAPIBUSINESSTYPE = 'InvalidParameterValue.InvalidApiBusinessType'

# Incorrect API ID
INVALIDPARAMETERVALUE_INVALIDAPIIDS = 'InvalidParameterValue.InvalidApiIds'

# Invalid API configuration.
INVALIDPARAMETERVALUE_INVALIDAPIREQUESTCONFIG = 'InvalidParameterValue.InvalidApiRequestConfig'

# The API type is incorrect. The microservice API only supports the TSF backend service type.
INVALIDPARAMETERVALUE_INVALIDAPITYPE = 'InvalidParameterValue.InvalidApiType'

# The backend service path configuration is incorrect.
INVALIDPARAMETERVALUE_INVALIDBACKENDPATH = 'InvalidParameterValue.InvalidBackendPath'

# Invalid CLB configuration.
INVALIDPARAMETERVALUE_INVALIDCLB = 'InvalidParameterValue.InvalidClb'

# Policy error.
INVALIDPARAMETERVALUE_INVALIDCONDITION = 'InvalidParameterValue.InvalidCondition'

# The constant parameter is invalid.
INVALIDPARAMETERVALUE_INVALIDCONSTANTPARAMETERS = 'InvalidParameterValue.InvalidConstantParameters'

# The value of the `Env` parameter is incorrect. Its valid values are (release, prepub, test).
INVALIDPARAMETERVALUE_INVALIDENV = 'InvalidParameterValue.InvalidEnv'

# Invalid service environment status
INVALIDPARAMETERVALUE_INVALIDENVSTATUS = 'InvalidParameterValue.InvalidEnvStatus'

# The parameter value is incorrect.
INVALIDPARAMETERVALUE_INVALIDFILTERNOTSUPPORTEDNAME = 'InvalidParameterValue.InvalidFilterNotSupportedName'

# The value of the backend address parameter is incorrect.
INVALIDPARAMETERVALUE_INVALIDIPADDRESS = 'InvalidParameterValue.InvalidIPAddress'

# Invalid quota
INVALIDPARAMETERVALUE_INVALIDMAXREQUESTNUM = 'InvalidParameterValue.InvalidMaxRequestNum'

# The method is incorrect. For backend services in the WEBSOCKET type, the frontend method should be configured as GET.
INVALIDPARAMETERVALUE_INVALIDMETHOD = 'InvalidParameterValue.InvalidMethod'

# Plugin parameter value error. Please modify and try again.
INVALIDPARAMETERVALUE_INVALIDPLUGINCONFIG = 'InvalidParameterValue.InvalidPluginConfig'

# The backend service port is incorrect.
INVALIDPARAMETERVALUE_INVALIDPORT = 'InvalidParameterValue.InvalidPort'

# Invalid protocol type parameter.
INVALIDPARAMETERVALUE_INVALIDPROCOTOL = 'InvalidParameterValue.InvalidProcotol'

# The OAUTH 2.0 API public key parameter is in an incorrect format.
INVALIDPARAMETERVALUE_INVALIDPUBLICKEY = 'InvalidParameterValue.InvalidPublicKey'

# Incorrect region.
INVALIDPARAMETERVALUE_INVALIDREGION = 'InvalidParameterValue.InvalidRegion'

# Invalid request parameter.
INVALIDPARAMETERVALUE_INVALIDREQUESTPARAMETERS = 'InvalidParameterValue.InvalidRequestParameters'

# The SCF API parameters are invalid.
INVALIDPARAMETERVALUE_INVALIDSCFCONFIG = 'InvalidParameterValue.InvalidScfConfig'

# Invalid service configuration.
INVALIDPARAMETERVALUE_INVALIDSERVICECONFIG = 'InvalidParameterValue.InvalidServiceConfig'

# The `ServiceMockReturnMessage` parameter is incorrect.
INVALIDPARAMETERVALUE_INVALIDSERVICEMOCKRETURNMESSAGE = 'InvalidParameterValue.InvalidServiceMockReturnMessage'

# The parameter configuration is incorrect, as the parameter is not configured in the backend parameter configuration list.
INVALIDPARAMETERVALUE_INVALIDSERVICEPARAM = 'InvalidParameterValue.InvalidServiceParam'

# The `ServiceParameters` parameter is incorrect.
INVALIDPARAMETERVALUE_INVALIDSERVICEPARAMETERS = 'InvalidParameterValue.InvalidServiceParameters'

# The backend service type is incorrect. For backend services in WEBSOCKET type, the frontend protocol should be configured as WEBSOCKET.
INVALIDPARAMETERVALUE_INVALIDSERVICETYPE = 'InvalidParameterValue.InvalidServiceType'

# Incorrect tag parameters
INVALIDPARAMETERVALUE_INVALIDTAGVALUES = 'InvalidParameterValue.InvalidTagValues'

# Incorrect configuration of the TSF-type API.
INVALIDPARAMETERVALUE_INVALIDTSFCONFIG = 'InvalidParameterValue.InvalidTsfConfig'

# The backend channel does not exist or is invalid.
INVALIDPARAMETERVALUE_INVALIDUPSTREAM = 'InvalidParameterValue.InvalidUpstream'

# The URL parameters are invalid.
INVALIDPARAMETERVALUE_INVALIDURL = 'InvalidParameterValue.InvalidUrl'

# Invalid VPC information
INVALIDPARAMETERVALUE_INVALIDVPCCONFIG = 'InvalidParameterValue.InvalidVpcConfig'

# The method is incorrect. For backend services in the WEBSOCKET type, the frontend method should be configured as GET.
INVALIDPARAMETERVALUE_INVALIDWSMETHOD = 'InvalidParameterValue.InvalidWSMethod'

# The length of the parameter exceeds the limit.
INVALIDPARAMETERVALUE_LENGTHEXCEEDED = 'InvalidParameterValue.LengthExceeded'

# The number of parameters has reached the limit (100).
INVALIDPARAMETERVALUE_LIMITEXCEEDED = 'InvalidParameterValue.LimitExceeded'

# The parameter value is incorrect, as it is not an available option.
INVALIDPARAMETERVALUE_NOTINOPTIONS = 'InvalidParameterValue.NotInOptions'

# There are no modifiable items for the OAuth API.
INVALIDPARAMETERVALUE_NOTHINGMODIFYFOROAUTH = 'InvalidParameterValue.NothingModifyForOauth'

# The backend parameter configuration is incorrect, as the related frontend parameters are not configured.
INVALIDPARAMETERVALUE_PARAMETERNOTMATCH = 'InvalidParameterValue.ParameterNotMatch'

# The number of parameters exceeded limit.
INVALIDPARAMETERVALUE_PARAMETERVALUELIMITEXCEEDED = 'InvalidParameterValue.ParameterValueLimitExceeded'

# The parameter value is incorrect, as it is not within the valid value range.
INVALIDPARAMETERVALUE_RANGEEXCEEDED = 'InvalidParameterValue.RangeExceeded'

# 
INVALIDPARAMETERVALUE_TRAFFICCONTROL = 'InvalidParameterValue.TrafficControl'

# Invalid parameter value.
INVALIDPARAMETERVALUE_UNSUPPORTEDPARAMETER = 'InvalidParameterValue.UnsupportedParameter'

# The quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# The number of API documents exceeds the limit.
LIMITEXCEEDED_APIDOCLIMITEXCEEDED = 'LimitExceeded.APIDocLimitExceeded'

# Reached the upper limit of access keys.
LIMITEXCEEDED_ACCESSKEYCOUNTINUSAGEPLANLIMITEXCEEDED = 'LimitExceeded.AccessKeyCountInUsagePlanLimitExceeded'

# Number of applications bound with the service reaches the upper limit.
LIMITEXCEEDED_APIAPPCOUNTLIMITEXCEEDED = 'LimitExceeded.ApiAppCountLimitExceeded'

# The number of APIs exceeds the limit.
LIMITEXCEEDED_APICOUNTLIMITEXCEEDED = 'LimitExceeded.ApiCountLimitExceeded'

# The number of keys exceeds the limit.
LIMITEXCEEDED_APIKEYCOUNTLIMITEXCEEDED = 'LimitExceeded.ApiKeyCountLimitExceeded'

# You can set up to 3 sets of custom path mappings.
LIMITEXCEEDED_EXCEEDEDDEFINEMAPPINGLIMIT = 'LimitExceeded.ExceededDefineMappingLimit'

# The number of bound domain names exceeds the limit. You can bind up to 5 domain names by default.
LIMITEXCEEDED_EXCEEDEDDOMAINLIMIT = 'LimitExceeded.ExceededDomainLimit'

# The number of IP policies exceeds the limit.
LIMITEXCEEDED_IPSTRATEGYLIMITEXCEEDED = 'LimitExceeded.IpStrategyLimitExceeded'

# The request frequency has reached the limit. Please try again later.
LIMITEXCEEDED_REQUESTLIMITEXCEEDED = 'LimitExceeded.RequestLimitExceeded'

# Too many services are bound to the plugin. Unbind some services or increase the quota, and try again.
LIMITEXCEEDED_SERVICECOUNTFORPLUGINLIMITEXCEEDED = 'LimitExceeded.ServiceCountForPluginLimitExceeded'

# The number of services exceeds the limit. Please delete some services or increase the limit and try again.
LIMITEXCEEDED_SERVICECOUNTLIMITEXCEEDED = 'LimitExceeded.ServiceCountLimitExceeded'

# The number of usage plans exceeds the limit.
LIMITEXCEEDED_USAGEPLANLIMITEXCEEDED = 'LimitExceeded.UsagePlanLimitExceeded'

# Missing parameter.
MISSINGPARAMETER = 'MissingParameter'

# The backend service parameter is missing.
MISSINGPARAMETER_BACKENDSPECIFICPARAM = 'MissingParameter.BackendSpecificParam'

# Parameter is missing in the plugin. Please check and try again.
MISSINGPARAMETER_PLUGINCONFIG = 'MissingParameter.PluginConfig'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# The number of requests exceeds the frequency limit.
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# The resource is in use.
RESOURCEINUSE = 'ResourceInUse'

# Insufficient resource.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The key does not exist.
RESOURCENOTFOUND_INVALIDACCESSKEYID = 'ResourceNotFound.InvalidAccessKeyId'

# Incorrect `ApiId`.
RESOURCENOTFOUND_INVALIDAPI = 'ResourceNotFound.InvalidApi'

# The application ID is incorrect.
RESOURCENOTFOUND_INVALIDAPIAPP = 'ResourceNotFound.InvalidApiApp'

# The API document does not exist.
RESOURCENOTFOUND_INVALIDAPIDOC = 'ResourceNotFound.InvalidApiDoc'

# The IP policy does not exist.
RESOURCENOTFOUND_INVALIDIPSTRATEGY = 'ResourceNotFound.InvalidIPStrategy'

# Error with the OAuth service API.
RESOURCENOTFOUND_INVALIDOAUTHAPI = 'ResourceNotFound.InvalidOauthApi'

# The plugin does not exist.
RESOURCENOTFOUND_INVALIDPLUGIN = 'ResourceNotFound.InvalidPlugin'

# The corresponding service is invisible.
RESOURCENOTFOUND_INVALIDSERVICE = 'ResourceNotFound.InvalidService'

# The usage plan does not exist.
RESOURCENOTFOUND_INVALIDUSAGEPLAN = 'ResourceNotFound.InvalidUsagePlan'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# The resources have been sold out.
RESOURCESSOLDOUT = 'ResourcesSoldOut'

# The operation is unauthorized.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# You do not have permission to access the resource.
UNAUTHORIZEDOPERATION_ACCESSRESOURCE = 'UnauthorizedOperation.AccessResource'

# The user has not passed identity verification.
UNAUTHORIZEDOPERATION_UNCERTIFIEDUSER = 'UnauthorizedOperation.UncertifiedUser'

# Unknown parameter.
UNKNOWNPARAMETER = 'UnknownParameter'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# Insufficient account balance
UNSUPPORTEDOPERATION_ACCOUNTARREARS = 'UnsupportedOperation.AccountArrears'

# The key has already been bound to a usage plan.
UNSUPPORTEDOPERATION_ALREADYBINDUSAGEPLAN = 'UnsupportedOperation.AlreadyBindUsagePlan'

# 
UNSUPPORTEDOPERATION_APILISTNOTEMPTY = 'UnsupportedOperation.ApiListNotEmpty'

# The current plugin cannot be bound.
UNSUPPORTEDOPERATION_ATTACHPLUGIN = 'UnsupportedOperation.AttachPlugin'

# You are using the basic edition and only one API can be created.
UNSUPPORTEDOPERATION_BASICSERVICENOMOREAPI = 'UnsupportedOperation.BasicServiceNoMoreApi'

# 
UNSUPPORTEDOPERATION_BASICSERVICENOTALLOWATTACHPLUGIN = 'UnsupportedOperation.BasicServiceNotAllowAttachPlugin'

# Invalid log query period
UNSUPPORTEDOPERATION_CLSSEARCHTIME = 'UnsupportedOperation.ClsSearchTime'

# 
UNSUPPORTEDOPERATION_EXISTINGONLINEENVIRONMENT = 'UnsupportedOperation.ExistingOnlineEnvironment'

# Cannot force HTTPS when the protocol is HTTP.
UNSUPPORTEDOPERATION_FORCEHTTPS = 'UnsupportedOperation.ForceHttps'

# API error.
UNSUPPORTEDOPERATION_INVALIDACTION = 'UnsupportedOperation.InvalidAction'

# Backend type not supported
UNSUPPORTEDOPERATION_INVALIDENDPOINTTYPE = 'UnsupportedOperation.InvalidEndpointType'

# The service is currently isolated and therefore the operation is not supported.
UNSUPPORTEDOPERATION_INVALIDSERVICETRADE = 'UnsupportedOperation.InvalidServiceTrade'

# The current key status does not support this operation.
UNSUPPORTEDOPERATION_INVALIDSTATUS = 'UnsupportedOperation.InvalidStatus'

# The EIAM authentication API cannot be modified.
UNSUPPORTEDOPERATION_MODIFYEIAMAUTHAPI = 'UnsupportedOperation.ModifyEIAMAuthApi'

# The network type cannot be modified
UNSUPPORTEDOPERATION_MODIFYNETTYPE = 'UnsupportedOperation.ModifyNetType'

# The frontend protocol type cannot be changed.
UNSUPPORTEDOPERATION_MODIFYPROTOCOL = 'UnsupportedOperation.ModifyProtocol'

# The current usage plan is not bound to an environment.
UNSUPPORTEDOPERATION_NOUSAGEPLANENV = 'UnsupportedOperation.NoUsagePlanEnv'

# Network types cannot be reduced.
UNSUPPORTEDOPERATION_REDUCENETTYPES = 'UnsupportedOperation.ReduceNetTypes'

# 
UNSUPPORTEDOPERATION_REQUESTPOSTERROR = 'UnsupportedOperation.RequestPostError'

# The resource has been associated. Please disassociate it first.
UNSUPPORTEDOPERATION_RESOURCEASSOCIATED = 'UnsupportedOperation.ResourceAssociated'

# The key has already been bound to a usage plan. Please unbind it and try again.
UNSUPPORTEDOPERATION_RESOURCEISINUSE = 'UnsupportedOperation.ResourceIsInUse'

# The resource is not associated.
UNSUPPORTEDOPERATION_RESOURCEUNASSOCIATED = 'UnsupportedOperation.ResourceUnassociated'

# 
UNSUPPORTEDOPERATION_SERVICEEXIST = 'UnsupportedOperation.ServiceExist'

# 
UNSUPPORTEDOPERATION_TAGSNOTEMPTY = 'UnsupportedOperation.TagsNotEmpty'

# The current `Uin` is not in the manual key allowlist.
UNSUPPORTEDOPERATION_UINNOTINWHITELIST = 'UnsupportedOperation.UinNotInWhiteList'

# 
UNSUPPORTEDOPERATION_UNPACKERROR = 'UnsupportedOperation.UnpackError'

# The key has already been bound to a usage plan.
UNSUPPORTEDOPERATION_UNSUPPORTEDBINDAPIKEY = 'UnsupportedOperation.UnsupportedBindApiKey'

# The environment cannot be bound.
UNSUPPORTEDOPERATION_UNSUPPORTEDBINDENVIRONMENT = 'UnsupportedOperation.UnsupportedBindEnvironment'

# The current API has already been bound to a business API. Please unbind it and try again.
UNSUPPORTEDOPERATION_UNSUPPORTEDDELETEAPI = 'UnsupportedOperation.UnsupportedDeleteApi'

# This service is being used and cannot be deleted.
UNSUPPORTEDOPERATION_UNSUPPORTEDDELETESERVICE = 'UnsupportedOperation.UnsupportedDeleteService'

# Operation failed: There are resources associated with this upstream.
UNSUPPORTEDOPERATION_UNSUPPORTEDDELETEUPSTREAM = 'UnsupportedOperation.UnsupportedDeleteUpstream'

# Unsupported network type
UNSUPPORTEDOPERATION_UNSUPPORTEDNETTYPE = 'UnsupportedOperation.UnsupportedNetType'

# The environment cannot be unbound, as there are APIs that are not bound to a usage plan.
UNSUPPORTEDOPERATION_UNSUPPORTEDUNBINDENVIRONMENT = 'UnsupportedOperation.UnsupportedUnBindEnvironment'

# The current key status does not support this operation.
UNSUPPORTEDOPERATION_UNSUPPORTEDUPDATEAPIKEY = 'UnsupportedOperation.UnsupportedUpdateApiKey'

# The current plan is in use. Please unbind it and try again.
UNSUPPORTEDOPERATION_USAGEPLANINUSE = 'UnsupportedOperation.UsagePlanInUse'
